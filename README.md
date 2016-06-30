# markovy
[![PyPI version](https://badge.fury.io/py/markovy.svg)](https://badge.fury.io/py/markovy)
[![GPL Licence][licence-badge]](LICENSE)

Parody generation with Markov Chain.

## Installation
```sh
$ pip install markovy
```

## Usage Example
```python
from markovy import MarkovChain

mc = MarkovChain('./shakespeare.txt')

print(mc.make('sentence'))
# output: ["For in thy orisons Be all my sins rememb'red."]
```

## Supported Python Versions
 - python 3
 - python 2
 - pypy3
 - pypy

## API Reference

### `make()`
```python
make(what='sentence', count=1, min=5, max=10)
```

 - **what** *(String)*
   - **word:** Generates irrelevant word from the dataset.
   - **sentence** *(default)*: Generates random sentences from the dataset.
   - **paragraph:** Generates random paragraphs from the dataset.
   - **text:** Generates random texts from the dataset.
 - **count** *(Integer)*: How many *what* will you generate?
 - **min** *(Integer)*: Minimum sentence count.
 - **max** *(Integer)*: Maximum sentence count.

**PS:** All results will be returned as list.

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
