from typing import List
from functools import partial
import os
import pickle
import torch
import re
from collections import defaultdict
import logging
import numpy as np
from pathlib import Path
from tqdm import tqdm
from sklearn.metrics import r2_score
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import Dataset, DataLoader
from edit_distance import SequenceMatcher

from falcon_challenge.config import FalconTask, FalconConfig
from falcon_challenge.interface import BCIDecoder
from falcon_challenge.dataloaders import load_nwb

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Data hash map, what participant submits, keys of comparison dict
DATASET_HELDINOUT_MAP = {
    'h1': {
        'held_in': [
            'S0_set_1', 
            'S0_set_2', 
            'S1_set_1', 
            'S1_set_2', 
            'S1_set_3',
            'S2_set_1',
            'S2_set_2',
            'S3_set_1',
            'S3_set_2',
            'S4_set_1',
            'S4_set_2',
            'S5_set_1',
            'S5_set_2',
        ],
        'held_out': [
            'S6_set_1', 
            'S6_set_2', 
            'S7_set_1', 
            'S7_set_2', 
            'S8_set_1', 
            'S8_set_2', 
            'S9_set_1', 
            'S9_set_2', 
            'S10_set_1', 
            'S10_set_2', 
            'S11_set_1', 
            'S11_set_2', 
            'S12_set_1',
            'S12_set_2',
        ],
    },
    'm1': {
        'held_in': ['20120924', '20120926', '20120927', '20120928'],
        'held_out': ['20121004', '20121017', '20121022', '20121024'],
    },
    'h2': {
        'held_in': [
            '2022.05.18', 
            '2022.05.23', 
            '2022.05.25', 
            '2022.06.01', 
            '2022.06.03', 
            '2022.06.06', 
            '2022.06.08', 
            '2022.06.13', 
            '2022.06.15', 
            '2022.06.22', 
            '2022.09.01', 
            '2022.09.29', 
            '2022.10.06',
            '2022.10.18', 
            '2022.10.25', 
            '2022.10.27', 
            '2022.11.01', 
            '2022.11.03', 
            '2022.12.08',
            '2022.12.15', 
            '2023.02.28',
        ],
        'held_out': [
            '2023.04.17', 
            '2023.05.31', 
            '2023.06.28', 
            '2023.08.16', 
            '2023.10.09'
        ]
    },
    'm2': {
        'held_in': ['2020-10-19-Run1', '2020-10-19-Run2', '2020-10-20-Run1', '2020-10-20-Run2', '2020-10-27-Run1', '2020-10-27-Run2', '2020-10-28-Run1'],
        'held_out': ['2020-10-30-Run1', '2020-10-30-Run2', '2020-11-18-Run1', '2020-11-19-Run1', '2020-11-24-Run1', '2020-11-24-Run2'],
    },
}

# Used to label test server data file names to look for
HELD_IN_KEYS = {
    FalconTask.h1: ['S0_', 'S1_', 'S2_', 'S3_', 'S4_', 'S5_'],
    FalconTask.m1: ['L_20120924', 'L_20120926', 'L_20120927', 'L_20120928'],
    FalconTask.m2: ['20201019', '20201020', '20201027', '20201028'],
    FalconTask.h2: DATASET_HELDINOUT_MAP['h2']['held_in'],
}

HELD_OUT_KEYS = {
    FalconTask.h1: ['S6_', 'S7_', 'S8_', 'S9_', 'S10_', 'S11_', 'S12_'],
    FalconTask.m1: ['L_20121004', 'L_20121017', 'L_20121022', 'L_20121024'],
    FalconTask.m2: ['20201030', '20201118', '20201119', '20201124'],
    FalconTask.h2: DATASET_HELDINOUT_MAP['h2']['held_out'],
}

RECOMMENDED_BATCH_SIZES = {
    FalconTask.h1: 8,
    FalconTask.m1: 4,
    FalconTask.h2: 1,
    FalconTask.m2: 1, # TODO up
}

# Development time flag. False allows direct evaluation without payload writing, only usable for local minival.
# Should be set to true for remote evaluation.
# USE_PKLS = False
USE_PKLS = True

HELDIN_OR_OUT_MAP = {
    'held_in': "Held In",
    'held_out': "Held Out",
}

def evaluate(
    test_annotation_file: str, # The annotation file for the phase
    user_submission_file: str, # * JY: This appears to always be /submission/submission.csv on EvalAI. No matter - load it as a pickle.
    phase_codename: str, # e.g. minival or test
    **kwargs
):
    r"""
        Test struct:
        {
            'h1': {
                'hash': {
                    'data': tgt,
                    'mask': mask,
                }
            }
        }
        User submission struct:
        {
            'h1': {
                'hash': pred,

                'normalized_latency': 1,
            }
        }
        Evaluate payloads with potentially multiple splits worth of data
        - Low pri: can I provide all results or just one split's worth entry? Currently providing 1, examples just provide 1, but in general would be nice to provide all. User shouldn't be able to submit more than 1, though.
    """
    # ! Want: Locally, test_annotation should be somewhere safe (tmp)
    # ! Remotely, it shoudl be /submission/submission.csv exactly.
    # Ignore explicit annotations provided and directly search for concatenated answers
    logger.info(f"Evaluation: Docker side")
    # test_annotation_file = '/dataset/evaluation_data/answer_key/minival.pkl'
    logger.info(f"Loading GT from {test_annotation_file}")
    logger.info(f"Loading submission from {user_submission_file}")
    logger.info(f"Phase: {phase_codename}")

    result = []
    # Load pickles
    try:
        with open(test_annotation_file, 'rb') as test_annotation_file, open(user_submission_file, 'rb') as user_submission_file:
            test_annotations = pickle.load(test_annotation_file)
            user_submission = pickle.load(user_submission_file)
    except Exception as e:
        logger.error(f"Checking root: {os.listdir('/')}")
        raise ValueError(f"Failed to load submission pickles: {e}. dir is {os.getcwd()}; contents {os.listdir()}.")
    for datasplit in user_submission: # datasplit e.g. h1, m1
        if datasplit not in test_annotations:
            raise ValueError(f"Missing {datasplit} in GT labels.")
        split_annotations = test_annotations[datasplit]
        split_result = {}
        split_result["Normalized Latency"] = user_submission[datasplit]["normalized_latency"]
        del user_submission[datasplit]["normalized_latency"]
        pred_dict = defaultdict(list)
        tgt_dict = defaultdict(list)
        mask_dict = defaultdict(list)
        for dataset in user_submission[datasplit]:
            dataset_pred = user_submission[datasplit][dataset]
            dataset_tgt = split_annotations[dataset]['data']
            dataset_mask = split_annotations[dataset]['mask']
            dataset_pred = dataset_pred[:dataset_mask.shape[0]] # In case excess timesteps are predicted due to batching, reduce
            if dataset in DATASET_HELDINOUT_MAP[datasplit]['held_in']:
                pred_dict['held_in'].append(dataset_pred)
                tgt_dict['held_in'].append(dataset_tgt)
                mask_dict['held_in'].append(dataset_mask)
            elif dataset in DATASET_HELDINOUT_MAP[datasplit]['held_out']:
                pred_dict['held_out'].append(dataset_pred)
                tgt_dict['held_out'].append(dataset_tgt)
                mask_dict['held_out'].append(dataset_mask)
            else:
                raise ValueError(f"Dataset {dataset} submitted but not found in held-in or held-out list of split {datasplit}.")
        for in_or_out in pred_dict:
            if len(pred_dict[in_or_out]) < len(DATASET_HELDINOUT_MAP[datasplit][in_or_out]):
                raise ValueError(f"Missing predictions for {datasplit} {in_or_out}. User submitted: {user_submission[datasplit].keys()}. Expecting more like: {HELDIN_OR_OUT_MAP[datasplit][in_or_out]}.")
            pred = np.concatenate(pred_dict[in_or_out])
            if 'h2' in datasplit:
                tgt = [y for x in tgt_dict[in_or_out] for y in x]
            else:
                tgt = np.concatenate(tgt_dict[in_or_out])
            mask = np.concatenate(mask_dict[in_or_out])
            eval_fn = FalconEvaluator.compute_metrics_edit_distance if 'h2' in datasplit else FalconEvaluator.compute_metrics_regression
            try:
                metrics = eval_fn(pred, tgt, mask)
            except Exception as e:
                raise ValueError(f"Failed to compute metrics for {datasplit} {in_or_out}: {e}")
            for k in metrics:
                split_result[f'{HELDIN_OR_OUT_MAP[in_or_out]} {k}'] = metrics[k]
        result.append({f'{phase_codename}_split_{datasplit}': split_result})

    print(f"Returning result from phase: {phase_codename}: {result}")
    # Out struct according to https://evalai.readthedocs.io/en/latest/evaluation_scripts.html
    return {"result": result, 'submission_result': result[0]}

class EvalDataset(Dataset):
    r"""
        Simple class to help with batched evaluation.
        data: List of numpy arrays, one per datafile
        datafiles: str names, for cuing models which dataset is being evaluated
        trial_mode: serve trialized data (padded) or just parallelize among datafiles
    """
    def __init__(self, 
                 data: List[np.ndarray], 
                 trial_change: List[np.ndarray], 
                 targets: List[np.ndarray], 
                 eval_mask: List[np.ndarray], 
                 datafiles: List[str],
                 trial_mode=False):
        self.data = data
        self.trial_change = trial_change
        self.targets = targets
        self.eval_mask = eval_mask
        self.datafiles = datafiles
        assert not trial_mode, "Trial mode not implemented."

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return (
            self.data[idx], 
            self.targets[idx], 
            self.trial_change[idx], 
            self.eval_mask[idx], 
            idx # needed to index for datafiles which are not natively loaded for pytorch dataloader
        )
    
    def get_datafile(self, idx):
        return self.datafiles[idx]

def simple_collater(batch, task):
    r"""
        Collates a batch of data, targets, trial_change, eval_mask, and datafile_idx.
        data: List of numpy arrays, one per datafile
        datafiles: str names, for cuing models which dataset is being evaluated
    """
    data, targets, trial_change, eval_mask, datafile_idx = zip(*batch)
    data = pad_sequence([torch.tensor(d) for d in data], batch_first=False).numpy()
    if task == FalconTask.h2:
        targets = pad_sequence([torch.tensor(t) for t in targets[0]], batch_first=True).numpy()
    else:
        targets = pad_sequence([torch.tensor(t) for t in targets], batch_first=False).numpy()
    trial_change = pad_sequence([torch.tensor(t) for t in trial_change], batch_first=False).numpy()
    eval_mask = pad_sequence([torch.tensor(t) for t in eval_mask], batch_first=False).numpy() # Serves as a mask for padding as well
    datafile_idx = np.array(datafile_idx)
    return data, targets, trial_change, eval_mask, datafile_idx

class FalconEvaluator:

    def __init__(self, eval_remote=False, split='h1'):
        self.eval_remote = eval_remote
        assert split in ['h1', 'h2', 'm1', 'm2'], "Split must be h1, h2, m1, or m2."
        self.dataset: FalconTask = getattr(FalconTask, split)
        self.cfg = FalconConfig(self.dataset)

    @staticmethod
    def get_eval_handles(is_remote: bool, dataset: FalconTask, phase: str = 'minival'):
        if is_remote: # i.e. definitely docker
            data_dir = os.environ.get("EVAL_DATA_PATH")
        else: # possibly docker or local
            if os.path.exists(f"./data/{dataset.name}"):
                logger.info("Using local data directory.")
                data_dir = "data"
            else:
                data_dir = os.environ.get("EVAL_DATA_PATH") # a local docker eval
        data_dir = Path(data_dir) / dataset.name
        if phase == 'test': # TODO wire wherever test is actually stored on remote
            eval_dir = data_dir / f"eval"
        else:
            eval_dir = data_dir / "minival"
        return sorted(list(eval_dir.glob("*val*.nwb")))

    def get_eval_files(self, phase: str = 'minival'):
        logger.info("Searching for evaluation data.")
        handles = self.get_eval_handles(self.eval_remote, self.dataset, phase=phase)
        logger.info(f"Found {len(handles)} files.")
        if len(handles) == 0:
            raise FileNotFoundError(f"No files found in {self.dataset.name} for phase {phase}. Note test phase data is only available on EvalAI remote.")
        return handles
    
    def predict_files(self, decoder: BCIDecoder, eval_files: List):
        # returns triple dict, keyed by datafile hash and contains preds, targets, and eval_mask respective
        # TODO this does not return uniquely identifiable data if eval_files is partial, e.g. if we only has set 2 of a day with 2 sets, we'll happily just provide partial predictions.
        # Pre-loop before starting batch loads
        file_neural_data = []
        file_trial_change = []
        file_targets = []
        file_eval_mask = []
        datafiles = list(sorted(eval_files))
        for datafile in datafiles:
            if not datafile.exists():
                raise FileNotFoundError(f"File {datafile} not found.")
            neural_data, decoding_targets, trial_change, eval_mask = load_nwb(datafile, dataset=self.dataset)
            file_neural_data.append(neural_data)
            file_trial_change.append(trial_change)
            file_targets.append(decoding_targets)
            file_eval_mask.append(eval_mask)
    
        dataset = EvalDataset(
            data=file_neural_data,
            trial_change=file_trial_change,
            targets=file_targets,
            eval_mask=file_eval_mask,
            datafiles=datafiles,
        )
        
        all_preds = defaultdict(list)
        all_targets = defaultdict(list)
        all_eval_mask = defaultdict(list)
        
        num_workers = 8
        simple_collater_partial = partial(simple_collater, task=self.dataset)
        dataloader = DataLoader(
            dataset, shuffle=False,
            batch_size=decoder.batch_size,
            num_workers=num_workers,
            persistent_workers=num_workers > 0,
            collate_fn=simple_collater_partial,
        )
        # from time import time
        # for neural_data, decoding_targets, trial_change, eval_mask, datafile in tqdm(dataset):
        for neural_data, decoding_targets, trial_change, eval_mask, datafile_idx in tqdm(dataloader):
            neural_data: np.ndarray
            decoding_targets: np.ndarray
            trial_change: np.ndarray
            eval_mask: np.ndarray
            datafile_idx: np.ndarray
            decoder.reset(dataset_tags=[dataset.datafiles[idx] for idx in datafile_idx])
            trial_preds = []
            # loop_times = []
            for neural_observations, trial_delta_obs, step_mask in zip(neural_data, trial_change, eval_mask):
                neural_observations: np.ndarray
                trial_delta_obs: np.ndarray
                step_mask: np.ndarray
                if self.dataset == FalconTask.h2:
                    assert neural_data.shape[1] == 1, "H2 expects batch size 1."
                    if step_mask[0]:
                        decoder.predict(neural_observations)
                    if trial_delta_obs[0]:
                        trial_preds.append(decoder.on_done(trial_delta_obs))
                else:
                    # loop_start = time()
                    decoder.on_done(trial_delta_obs)
                    trial_preds.append(decoder.predict(neural_observations))
                    
                    # if step_mask.any():
                    #     trial_preds.append(decoder.predict(neural_observations))
                    # else:
                    #     decoder.observe(neural_observations)
                    #     trial_preds.append(np.full((decoder.batch_size, self.cfg.out_dim), np.nan))
                # loop_times.append(time() - loop_start)
            # loop_times = np.array(loop_times)
            # print(f"Loop {len(loop_times)}: {loop_times.mean()} +/- {loop_times.std()}")
            
            if self.dataset == FalconTask.h2:
                datafile_hash = self.cfg.hash_dataset(dataset.get_datafile(datafile_idx[0]))
                all_preds[datafile_hash].append(trial_preds)
                all_targets[datafile_hash].append(decoding_targets)
                all_eval_mask[datafile_hash].append(eval_mask)
            else:
                trial_preds = np.stack(trial_preds) # -> T x B x H
                for idx in range(len(datafile_idx)):
                    datafile_hash = self.cfg.hash_dataset(dataset.get_datafile(datafile_idx[idx]))
                    all_preds[datafile_hash].append(trial_preds[:, idx])
                    all_targets[datafile_hash].append(decoding_targets[:, idx])
                    all_eval_mask[datafile_hash].append(eval_mask[:, idx])
        for k in all_preds:
            if self.dataset == FalconTask.h2:
                all_preds[k] = [x for y in all_preds[k] for x in y]
                all_targets[k] = [x for y in all_targets[k] for x in y]
            else:
                all_preds[k] = np.concatenate(all_preds[k])
                all_targets[k] = np.concatenate(all_targets[k])
            all_eval_mask[k] = np.concatenate(all_eval_mask[k])
        return all_preds, all_targets, all_eval_mask

    def evaluate_files(self, decoder: BCIDecoder, eval_files: List):
        all_preds, all_targets, all_eval_mask = self.predict_files(decoder, eval_files)
        metrics = self.compute_metrics(all_preds, all_targets, all_eval_mask)
        return metrics

    def evaluate(
            self, 
            decoder: BCIDecoder, 
            phase: str, 
            held_out_only: bool = False, 
            specific_keys: List = []
        ):
        r"""
            Note: Locally, this can produce metrics, but locally and remotely it should also write a submission file 
            that the actual evaluator on remote uses. The evaluation is done separately on remote.

            held_out_only: Only run predictions on held out
            specific_keys: Overrides held_out_only. Only run predictions on datafiles with specific keys.
        """
        assert phase in ['minival', 'test'], "Phase must be minival or test."
        if phase == 'minival' and (held_out_only or specific_keys):
            logger.warning("Ignoring held_out_only and specific_keys for minival phase.")
            held_out_only = False
        if decoder.batch_size > RECOMMENDED_BATCH_SIZES[self.dataset]:
            raise ValueError(f"Decoder batch size {decoder.batch_size} is larger than limit {RECOMMENDED_BATCH_SIZES[self.dataset]} for {self.dataset}")
        
        np.random.seed(0)
        # ! TODO ideally seed other libraries as well...? Is that our responsibility?
        
        eval_files = self.get_eval_files(phase=phase)
        metrics = {}
        prediction_env_var = "PREDICTION_PATH" if self.eval_remote else "PREDICTION_PATH_LOCAL"
        prediction_path = os.environ.get(prediction_env_var, './local_prediction.pkl')
        if not prediction_path:
            raise ValueError("PREDICTION_PATH not set in remote env which expects it. Cannot forward to separate evaluate runscript.")
        gt_path = os.environ.get("GT_PATH", './local_gt.pkl')
        if not gt_path:
            raise ValueError("GT_PATH not set in remote env which expects it. Cannot forward to separate evaluate runscript.")
            
        if phase == 'test':
            eval_files_held_in = [f for f in eval_files if any(k in f.name for k in HELD_IN_KEYS[self.dataset])]
            eval_files_held_out = [f for f in eval_files if any(k in f.name for k in HELD_OUT_KEYS[self.dataset])]
            assert len(eval_files) == len(eval_files_held_in) + len(eval_files_held_out), f"Mismatch in extracted eval #: Eval file state is not consistent with benchmark creation settings. Found {len(eval_files)} files, {len(eval_files_held_in)} held in, {len(eval_files_held_out)} held out."

            if specific_keys:
                raise NotImplementedError("not sure what metrics to compute for specific keys yet.")
            elif held_out_only:
                eval_files_held_in = []
            all_preds, all_targets, all_eval_mask = self.predict_files(decoder, eval_files_held_out)
            if eval_files_held_in:
                all_preds_held_in, all_targets_held_in, all_eval_mask_held_in = self.predict_files(decoder, eval_files_held_in)
                all_preds.update(all_preds_held_in)
                all_targets.update(all_targets_held_in)
                all_eval_mask.update(all_eval_mask_held_in)

        else:
            all_preds, all_targets, all_eval_mask = self.predict_files(decoder, eval_files)
        # Indirect remote setup to satisfy EvalAI interface. Save metrics / comparison to file.
        if USE_PKLS:
            inner_pred = {**all_preds}
            inner_tgt_spoof = { # spoof for local mirror of eval ai path, in reality targets are already compiled on eval ai side.
                k: {
                    'data': all_targets[k][all_eval_mask[k]] if self.dataset != FalconTask.h2 else all_targets[k],
                    'mask': all_eval_mask[k],
                } for k in all_targets
            }
            inner_pred['normalized_latency'] = 1 # TODO - CW insert timing code
            pred_payload = {self.dataset.name: inner_pred}
            truth_payload = {self.dataset.name: inner_tgt_spoof}
        else:
            pass
            
        if USE_PKLS:
            Path(prediction_path).parent.mkdir(parents=True, exist_ok=True)
            with open(prediction_path, 'wb') as f:
                pickle.dump(pred_payload, f)
            Path(gt_path).parent.mkdir(parents=True, exist_ok=True)
            with open(gt_path, 'wb') as f:
                pickle.dump(truth_payload, f)
            import time

            if self.eval_remote:
                print("Sleeping before exiting for remote eval - feel free to interrupt for local eval.", flush=True)
                # Gunjan, EvalAI contact says that current static code eval has an issue where the submission dump is only polled by the EvalAI worker comparison script every 5 minutes
                # Sleep so it's definitely available
                time.sleep(300) 
            else:
                return evaluate(
                    test_annotation_file=gt_path,
                    user_submission_file=prediction_path,
                    phase_codename=phase
                )
        else:
            for k, v in metrics.items():
                logger.info("{}: {}".format(k, v))
        
    @staticmethod
    def compute_metrics_regression(preds, targets, eval_mask):
        # assumes targets are already masked
        preds = preds[eval_mask]
        if not targets.shape[0] == preds.shape[0]:
            raise ValueError(f"Targets and predictions have different lengths: {targets.shape[0]} vs {preds.shape[0]}.")
        return {
            "R2": r2_score(targets, preds, multioutput='variance_weighted'),
            "R2 Std.": 0, # TODO Clay
        }

    @staticmethod
    def compute_metrics_edit_distance(preds, targets, eval_mask):
        if len(preds) != len(targets):
            raise ValueError(f"Targets and predictions have different lengths: {len(targets)} vs {len(preds)}.")
        
        def _to_words(s):
            return s.replace(">", " ").replace(r"([~,!?])", r" \1").split(" ")
        
        char_counts = []
        word_counts = []
        char_distances = []
        word_distances = []
        for pred, target in zip(preds, targets):
            target = "".join([chr(c) for c in target if c != 0])
            matcher = SequenceMatcher([c for c in pred], [c for c in target])
            char_distances.append(matcher.distance())
            char_counts.append(len(target))

            pred = _to_words(pred)
            target = _to_words(target)
            matcher = SequenceMatcher(pred, target)
            word_distances.append(matcher.distance())
            word_counts.append(len(target))

        return {
            "WER": np.sum(word_distances) / np.sum(word_counts),
            "CER": np.sum(char_distances) / np.sum(char_counts),
            "WER Std.": np.std(np.array(word_distances) / np.array(word_counts)),
            "CER Std.": np.std(np.array(char_distances) / np.array(char_counts)),
        }

    def compute_metrics(self, all_preds, all_targets, all_eval_mask=None):
        r"""
            all_preds: array of shape (n_timesteps, k_dim)
            all_targets: array of shape (n_timesteps, k_dim)
            all_eval_mask: array of shape (n_timesteps, k_dim). True if we should evaluate this timestep.
        """
        if self.dataset in [FalconTask.h1, FalconTask.m1, FalconTask.m2]:
            metrics = self.compute_metrics_regression(all_preds, all_targets, all_eval_mask)
        elif self.dataset in [FalconTask.h2]:
            metrics = self.compute_metrics_edit_distance(all_preds, all_targets, all_eval_mask)
        else:
            raise ValueError(f"Unknown dataset {self.dataset}")
        return metrics


r"""
    JY isn't too clear what happens eval-server side on submission but 1 of 2 patterns seem plausible:
    1. Server receives dockerfile and runs it blind.
    - Submitted docker code should call evaluation with config that points to GT data that only lives remotely.
    - This is the pattern that the Habitat challenge uses.
    In order for the image to access the test data, we can mount the data when we run on eval side.
    `docker run -v /path/on/host:/path/in/container your_image_name`
    2. Evaluator
    - Server receives dockerfile, and runs python evaluate.py --code Dockerfile
    And somehow the evaluator will dynamically import the agent code to run it.
"""