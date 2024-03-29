import os

from hpolib_extractor import extract_hpobench, extract_indiv_hpobench


# fcnet_tabular_benchmarks.tar.gz must be located here
data_dir = os.path.join(os.environ["HOME"], "hpo_benchmarks/hpobench")

extract_hpobench(data_dir=data_dir)
extract_indiv_hpobench(data_dir=data_dir)
