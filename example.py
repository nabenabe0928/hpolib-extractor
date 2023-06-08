import os

from hpolib_extractor import extract


# fcnet_tabular_benchmarks.tar.gz must be located here
data_dir = os.path.join(os.environ["HOME"], "hpo_benchmarks/hpolib")
# Choose epochs from 1 to 100
epochs = [11, 33, 100]

extract(data_dir=data_dir, epochs=epochs)
