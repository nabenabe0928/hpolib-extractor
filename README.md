# The extractor of HPOlib

[HPOlib](https://github.com/automl/HPOlib) is a tabular benchmark for hyperparameter optimization.
Since HPOlib uses `h5py`, we cannot serialize the benchmark.
This benchmark extracts HPOlib into pickle file(s) so that we can use the benchmark even under distributed setups.
Note that we picklize python dict objects, so in principle, the pickle files should work for arbitrary python versions.

We added the option for the MLP bench of [HPOBench](https://github.com/automl/HPOBench/) as well.

## Install of the package

You can use either `pip install` or `git clone`:

```shell
$ cd ~/
$ pip install hpolib-extractor
```

Or

```shell
$ git clone https://github.com/nabenabe0928/hpolib-extractor
$ pip install -r requirements.txt
```

## Install of HPOlib

You can download the tabular datasets for HPOlib via the following command:
```shell
$ cd <YOUR_DATA_PATH>
$ wget http://ml4aad.org/wp-content/uploads/2019/01/fcnet_tabular_benchmarks.tar.gz
$ tar xf fcnet_tabular_benchmarks.tar.gz
$ mv fcnet_tabular_benchmarks/*.hdf5 .
$ rm -r fcnet_tabular_benchmarks/
```

## Install of HPOBench

The tabular datasets for HPOBench via the following command:
```shell
$ cd <YOUR_DATA_PATH>
$ wget https://ndownloader.figshare.com/files/30379005
$ unzip nn.zip
```

## Extraction

Run the following code for HPOlib and then you will get the extracted `.pkl` data in the specified path.

```python
from hpolib_extractor import extract_hpolib


data_dir = "YOUR_DATA_PATH/"  # fcnet_tabular_benchmarks.tar.gz must be located here
epochs = [11, 33, 100]  # Choose epochs from 1 to 100
extract_hpolib(data_dir=data_dir, epochs=epochs)
```

By default, we extract only `valid-mse` and `runtime` and we can specify which epochs to store.
It is obvious, but if we specify more epochs, the data size is going to be larger.


For HPOBench, use the following code:

```python
from hpolib_extractor import extract_hpobench


data_dir = "YOUR_DATA_PATH/"  # fcnet_tabular_benchmarks.tar.gz must be located here
extract_hpobench(data_dir=data_dir)
```

The codes are available in [examples](examples/).
