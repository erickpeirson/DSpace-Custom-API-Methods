.. . documentation master file, created by
   sphinx-quickstart on Wed Jan 29 10:37:13 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the DSPace Custom API Methods documentation!
=======================================================

The dspace module provides :class:`.DSpace`, a class for interacting with the
`DSpaceTools API <https://github.com/mbl-cli/DspaceTools/wiki/API>`_, 
which is a custom REST API for the 
`ASU Digital HPS Repository <http://hpsrepository.asu.edu>`_.

.. toctree::
   :maxdepth: 4

   dspace

Usage
-----

Clone the most recent version of this project::

	$ git clone https://github.com/erickpeirson/DSpace-Custom-API-Methods.git

Or download the project from https://github.com/erickpeirson/DSpace-Custom-API-Methods.

Make sure that dspace.py is in your import path, and use::

	>>> from dspace import DSpace
	>>> d = DSpace('my_public_key', 'my_private_key', 'http://path/to/rest/endpoint')

Questions?
----------
Ask `Erick <https://cbs.asu.edu/gradinfo/?page_id=49>`_.

License
-------
DSpace Custom API Methods is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

DSpace Custom API Methods is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
`GNU General Public License <http://www.gnu.org/licenses/>`_ for more details.

.. image:: http://www.gnu.org/graphics/gplv3-127x51.png

About
-----
DSpace Custom API Methods is developed by the 
`ASU Digital Innovation Group (DigInG) <http://devo-evo.lab.asu.edu/diging>`_,
part of the `Laubichler Lab <http://devo-evo.lab.asu.edu>`_ in the Center for Biology & 
Society, School of Life Sciences.

This material is based upon work supported by the National Science Foundation Graduate 
Research Fellowship Program under Grant No. 2011131209, and NSF Doctoral Dissertation 
Research Improvement Grant No. 1256752.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

