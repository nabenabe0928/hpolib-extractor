import os

from hpolib_extractor import extract_hpobench


# fcnet_tabular_benchmarks.tar.gz must be located here
data_dir = os.path.join(os.environ["HOME"], "hpo_benchmarks/hpo-bench")

extract_hpobench(data_dir=data_dir)
