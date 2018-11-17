# cnames

cnames generates a namedtuple for pandas dataframe columns.
When added to the pandas DataFrame class through monkey patching
column names can obtained through tab completion in interactive mode.

## Getting Started

### Prerequisites
This module uses
[namedtuples](https://docs.python.org/2.7/library/collections.html#collections.namedtuple)
which were introduced in Python 2.6.
Code was developed and tested on Python 3,
Pandas 0.18.1 and IPython 5.3.0.

```
Python >= 2.6
Pandas >= 0.18.1
```

### Installing
Use pip to install via wheel.
If you have downloaded the module locally
then change to that directory and use pip


```
pip install cnames-0.1-py2.py3-none-any.whl
```

You can also install via URL

```
pip install https://github.com/ebenp/cnames/raw/master/dist/cnames-0.1-py2.py3-none-any.whl
```

## Running tests

A test dataframe under the main() statement in cnames.py is available for use.

### Usage

After import assign cnames to the DataFrame class.

```
import pandas as pd
import cnames

# monkey-patch the DataFrame class
pd.DataFrame.cnames = cnames
```

To use cnames call the function on the
desired DataFrame in interactive mode, in IPython or
a debugging environment

```
# tab completetion will populate with
column names along with DataFrame attributes and methods

df.cnames().<tab completion>
```

## Contributing

Please feel free to submit issues or pull requests.

## Versioning

For the versions available, see the [tags on this repository](https://github.com/ebenp/cnames/tags).

## Authors

* **Eben Pendleton** - *Initial work* - [ebenp](https://github.com/ebenp)


Modified from a stackoverflow [answer](https://stackoverflow.com/a/25418058).
Answer was given by user [Maturin](https://stackoverflow.com/users/2778224/maturin).
Thanks!

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Moddfied from an [answer](https://stackoverflow.com/a/25418058)
given by user [Maturin](https://stackoverflow.com/users/2778224/maturin).
Thanks!
