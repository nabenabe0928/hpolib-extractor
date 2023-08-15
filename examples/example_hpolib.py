import os

from hpolib_extractor import extract_hpolib, extract_indiv_hpolib


# fcnet_tabular_benchmarks.tar.gz must be located here
data_dir = os.path.join(os.environ["HOME"], "hpo_benchmarks/hpolib")
# Choose epochs from 1 to 100
epochs = [11, 33, 100]

extract_hpolib(data_dir=data_dir, epochs=epochs)
extract_indiv_hpolib(data_dir=data_dir)
