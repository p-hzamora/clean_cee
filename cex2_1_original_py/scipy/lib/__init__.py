# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\lib\__init__.pyc
# Compiled at: 2013-02-16 13:27:30
"""
Python wrappers to external libraries
=====================================

- lapack -- wrappers for `LAPACK/ATLAS <http://netlib.org/lapack/>`_
            libraries
- blas -- wrappers for `BLAS/ATLAS <http://www.netlib.org/blas/>`_
          libraries

"""
from __future__ import division, print_function, absolute_import
__all__ = [
 'lapack', 'blas']
from numpy.testing import Tester
test = Tester().test