# The extractor of HPOlib

[HPOlib](https://github.com/automl/HPOlib) is a tabular benchmark for hyperparameter optimization.
Since HPOlib uses `h5py`, we cannot serialize the benchmark.
This benchmark extracts HPOlib into pickle file(s) so that we can use the benchmark even under distributed setups.

# Install of HPOlib

You can download the tabular datasets for HPOlib via the following command:
```shell
$ wget http://ml4aad.org/wp-content/uploads/2019/01/fcnet_tabular_benchmarks.tar.gz
$ tar xf fcnet_tabular_benchmarks.tar.gz
```

# Install of the package

You can use either `pip install` or `git clone`:

```shell
$ pip install hpolib-extractor
```

Or

```shell
$ git clone https://github.com/nabenabe0928/hpolib-extractor
$ pip install -r requirements.txt
```

# Extraction

Run the following code and then you will get the extracted `.pkl` data in the specified path.

```python
from hpolib_extractor import extract


data_dir = "YOUR_DATA_PATH/"  # fcnet_tabular_benchmarks.tar.gz must be located here
epochs = [11, 33, 100]  # Choose epochs from 1 to 100
extract(data_dir=data_dir, epochs=epochs)
```

By default, we extract only `valid-mse` and `runtime` and we can specify which epochs to store.
It is obvious, but if we specify more epochs, the data size is going to be larger.
