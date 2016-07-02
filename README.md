# markovy
[![PyPI version](https://badge.fury.io/py/markovy.svg)](https://badge.fury.io/py/markovy)
[![Build Status](https://travis-ci.org/halilkaya/markovy.svg?branch=master)](https://travis-ci.org/halilkaya/markovy)
[![Coverage Status](https://coveralls.io/repos/github/halilkaya/markovy/badge.svg?branch=master)](https://coveralls.io/github/halilkaya/markovy?branch=master)
[![Code Health](https://landscape.io/github/halilkaya/markovy/master/landscape.svg?style=flat)](https://landscape.io/github/halilkaya/markovy/master)
[![GPL Licence][licence-badge]](LICENSE)

Parody generation with Markov Chain.

## Installation
```sh
$ pip install markovy
```

## Usage Example
```python
from markovy import MarkovChain

with open('./shakespeare.txt') as f:
  mc = MarkovChain(f)

print(mc.make_sentence())
# output: ["For in thy orisons Be all my sins rememb'red."]
```

## Supported Python Versions
 - python 3
 - python 2
 - pypy3
 - pypy

## Running Tests
To run tests, you have to install **unittest** first:
```sh
$ pip install unittest
```
Then, just run **tests.py**:
```sh
$ python tests.py
```

## API Reference

### `__init__()`
```python
__init__(dataset)
```

 - **dataset:**
   - **file-like object:** Dataset can be file-like object as in usage example above.
   - **string:** A string to be parsed can be given as dataset.
   - **list:** A parsed word list can be given as dataset.

### `make_word()`
```python
make_word(count=1)
```
Generates random word from the dataset.

 - **count** *(Integer)*: How many *what* will you generate? Default value is 1.

### `make_sentence()`
```python
make_sentence(count=1)
```
Generates random sentences from the dataset.

 - **count** *(Integer)*: How many *what* will you generate? Default value is 1.

### `make_paragraph()`
```python
make_paragraph(count=1, minimum=5, maximum=10)
```
Generates random paragraphs from the dataset.

 - **count** *(Integer)*: How many *what* will you generate? Default value is 1.
 - **minimum** *(Integer)*: Minimum sentence count. Default value is 5.
 - **maximum** *(Integer)*: Maximum sentence count. Default value is 10.

### `make_text()`
```python
make_text(count=1, minimum=5, maximum=10)
```
Generates random texts from the dataset.

 - **count** *(Integer)*: How many *what* will you generate? Default value is 1.
 - **minimum** *(Integer)*: Minimum sentence count. Default value is 5.
 - **maximum** *(Integer)*: Maximum sentence count. Default value is 10.

**PS:** All results will be returned as list.

## Contributors
 - [Berker Peksağ](https://github.com/berkerpeksag)

## Contributing
 - Random walking method is used on the current version. You can add weights for each words in chain to generate more logical outputs.

## Thanks
 - The idea came up while discussing with [Fatih Erikli](https://github.com/fatiherikli) and he suggested me to write a Python module for Markov Chain algorithm.

## License
```
Python module for Markov Chain algorithm.
Copyright (C) 2016  Halil Kaya

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
```
[See Full License](https://github.com/halilkaya/markovy/blob/master/LICENSE)

[licence-badge]:http://img.shields.io/badge/licence-GPL-brightgreen.svg
