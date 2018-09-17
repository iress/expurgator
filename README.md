# expurgator

Censor sensitive string data in Python.

## Quickstart

Install with:

```sh
pip install expurgator
```


## Usage

Like so:

```python
from expurgator import shallow_dict_expurgator

orig_dict = {'user': 'johnsmith', 'pass': 'supersecret'}
censored_dict = shallow_dict_expurgator(orig_dict)

# censored_dict is now:
# {'user': 'johnsmith', 'pass': '<SensitiveString>'}
```


## Building

To build this library as a wheel:

```sh
python setup.py bdist_wheel --universal
```


## Testing

First, make sure you have pytest installed:

```sh
pip install pytest
```

To run all tests, simply do:

```sh
py.test
```


## Legal

Copyright 2018 [IRESS Ltd](https://www.iress.com/).

License: Apache License 2.0.
