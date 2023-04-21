# The extractor of HPOlib

[HPOlib](https://github.com/automl/HPOlib) is a tabular benchmark for hyperparameter optimization.
Since HPOlib uses `h5py`, we cannot serialize the benchmark.
This benchmark extracts HPOlib into pickle file(S) so that we can use the benchmark even under distributed setups.

