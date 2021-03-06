# DSpace Custom API Methods

dspace.py provides a Python class for interacting with the 
[DSpaceTools API](https://github.com/mbl-cli/DspaceTools/wiki/API), which is a custom
REST API for the [ASU Digital HPS Repository](http://hpsrepository.asu.edu).

You can find documentation 
[here](http://erickpeirson.github.io/DSpace-Custom-API-Methods/)

## Usage

Clone the most recent version of this project:

```$ git clone https://github.com/erickpeirson/DSpace-Custom-API-Methods.git```

Or download the project from [https://github.com/erickpeirson/DSpace-Custom-API-Methods].

Make sure that dspace.py is in your import path, and use:

```python
>>> from dspace import DSpace
>>> d = DSpace('my_public_key', 'my_private_key', 'http://path/to/rest/endpoint')
```

## Questions?
Ask [Erick](https://cbs.asu.edu/gradinfo/?page_id=49)

## License
DSpace Custom API Methods is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

DSpace Custom API Methods is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
[GNU General Public License](http://www.gnu.org/licenses/) for more details.

![alt text](http://www.gnu.org/graphics/gplv3-127x51.png "GNU GPL 3")

## About
DSpace Custom API Methods is developed by the 
[ASU Digital Innovation Group (DigInG)](http://devo-evo.lab.asu.edu/diging),
part of the [Laubichler Lab](http://devo-evo.lab.asu.edu) in the Center for Biology & 
Society, School of Life Sciences.

This material is based upon work supported by the National Science Foundation Graduate 
Research Fellowship Program under Grant No. 2011131209, and NSF Doctoral Dissertation 
Research Improvement Grant No. 1256752.