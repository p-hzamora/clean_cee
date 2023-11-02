# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\io\__init__.pyc
# Compiled at: 2013-02-16 13:27:30
"""
==================================
Input and output (:mod:`scipy.io`)
==================================

.. currentmodule:: scipy.io

SciPy has many modules, classes, and functions available to read data
from and write data to a variety of file formats.

.. seealso:: :ref:`numpy-reference.routines.io` (in Numpy)

MATLAB® files
=============

.. autosummary::
   :toctree: generated/

   loadmat - Read a MATLAB style mat file (version 4 through 7.1)
   savemat - Write a MATLAB style mat file (version 4 through 7.1)
   whosmat - List contents of a MATLAB style mat file (version 4 through 7.1)

IDL® files
==========

.. autosummary::
   :toctree: generated/

   readsav - Read an IDL 'save' file

Matrix Market files
===================

.. autosummary::
   :toctree: generated/

   mminfo - Query matrix info from Matrix Market formatted file
   mmread - Read matrix from Matrix Market formatted file
   mmwrite - Write matrix to Matrix Market formatted file

Wav sound files (:mod:`scipy.io.wavfile`)
=========================================

.. module:: scipy.io.wavfile

.. autosummary::
   :toctree: generated/

   read
   write

Arff files (:mod:`scipy.io.arff`)
=================================

.. module:: scipy.io.arff

.. autosummary::
   :toctree: generated/

   loadarff

Netcdf (:mod:`scipy.io.netcdf`)
===============================

.. module:: scipy.io.netcdf

.. autosummary::
   :toctree: generated/

   netcdf_file - A file object for NetCDF data
   netcdf_variable - A data object for the netcdf module

"""
from __future__ import division, print_function, absolute_import
from .matlab import loadmat, savemat, whosmat, byteordercodes
from .netcdf import netcdf_file, netcdf_variable
from .mmio import mminfo, mmread, mmwrite
from .idl import readsav
from .harwell_boeing import hb_read, hb_write
__all__ = [ s for s in dir() if not s.startswith('_') ]
from numpy.testing import Tester
test = Tester().test