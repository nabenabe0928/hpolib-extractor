import itertools
import json
import os
import pickle
from typing import List

import h5py

import numpy as np

from tqdm import tqdm


SEARCH_SPACE = {
    "init_lr": [5e-4, 1e-3, 5e-3, 1e-2, 5e-2, 1e-1],
    "lr_schedule": ["cosine", "const"],
    "batch_size": [8, 16, 32, 64],
    "activation_fn_1": ["relu", "tanh"],
    "activation_fn_2": ["relu", "tanh"],
    "dropout_1": [0.0, 0.3, 0.6],
    "dropout_2": [0.0, 0.3, 0.6],
    "n_units_1": [16, 32, 64, 128, 256, 512],
    "n_units_2": [16, 32, 64, 128, 256, 512],
}
DATASET_NAMES = ["slice_localization", "protein_structure", "naval_propulsion", "parkinsons_telemonitoring"]
DATA_DIR_NAME = os.path.join(os.environ["HOME"], "tabular_benchmarks")
N_ENTRIES = np.prod([len(vs) for vs in SEARCH_SPACE.values()])


class HPOLibExtractor:
    def __init__(self, dataset_id: int, budgets: List[int] = [100]):
        self._dataset_name = DATASET_NAMES[dataset_id]
        path = os.path.join(DATA_DIR_NAME, "hpolib", f"fcnet_{self._dataset_name}_data.hdf5")
        self._db = h5py.File(path, "r")

        budget_array = np.array(budgets)
        if not np.all((1 <= budget_array) & (budget_array) <= 100):
            raise ValueError("Budget must be in [1, 100].")

        self._budgets_id = [b - 1 for b in np.sort(budgets)]
        self._collected_data = {}

    @property
    def dataset_name(self) -> str:
        return self._dataset_name

    def collect(self) -> None:
        # max_budget: 99, min_budget: 0
        loss_key = "valid_mse"
        runtime_key = "runtime"
        n_seeds = 4
        for it in tqdm(itertools.product(*(list(v) for v in SEARCH_SPACE.values())), total=N_ENTRIES):
            config = {k: v for k, v in zip(SEARCH_SPACE.keys(), it)}
            key = json.dumps(config, sort_keys=True)
            target_data = self._db[key]
            self._collected_data[key] = {
                loss_key: [{b: float(target_data[loss_key][s][b]) for b in self._budgets_id} for s in range(n_seeds)],
                runtime_key: [float(target_data[runtime_key][s]) for s in range(n_seeds)],
            }


if __name__ == "__main__":
    os.makedirs("pkl-data/", exist_ok=True)
    for i in range(4):
        extractor = HPOLibExtractor(dataset_id=i, budgets=[11, 33, 100])
        print(f"Start extracting {extractor.dataset_name}")
        extractor.collect()
        pickle.dump(extractor._collected_data, open(f"pkl-data/{extractor.dataset_name}.pkl", "wb"))
