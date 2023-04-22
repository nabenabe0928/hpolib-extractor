# The extractor of HPOlib

[HPOlib](https://github.com/automl/HPOlib) is a tabular benchmark for hyperparameter optimization.
Since HPOlib uses `h5py`, we cannot serialize the benchmark.
This benchmark extracts HPOlib into pickle file(S) so that we can use the benchmark even under distributed setups.

# Install of HPOlib

You can download the tabular datasets for HPOlib via the following command:
```shell
$ wget http://ml4aad.org/wp-content/uploads/2019/01/fcnet_tabular_benchmarks.tar.gz
$ tar xf fcnet_tabular_benchmarks.tar.gz
```

# Extraction

Run the following code and then you will get the extracted `.pkl` data in `pkl-data`.
By default, we extract only `valid-mse` and `runtime` for budget $\\{11,33,100\\}$.
```
$ python hpolib_extractor/extractor.py
```
If you would like to have something different, you need to modify the script by yourself.
