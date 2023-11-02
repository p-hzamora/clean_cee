# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\sparse\linalg\eigen\__init__.pyc
# Compiled at: 2013-02-16 13:27:32
"""
Sparse Eigenvalue Solvers
-------------------------

The submodules of sparse.linalg.eigen:
    1. lobpcg: Locally Optimal Block Preconditioned Conjugate Gradient Method

"""
from __future__ import division, print_function, absolute_import
from ...arpack import *
from ...lobpcg import *
__all__ = [ s for s in dir() if not s.startswith('_') ]
from numpy.testing import Tester
test = Tester().test
bench = Tester().bench