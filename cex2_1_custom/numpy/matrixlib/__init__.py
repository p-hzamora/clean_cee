# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\matrixlib\__init__.pyc
# Compiled at: 2013-04-07 07:04:04
"""Sub-package containing the matrix class and related functions."""
from .defmatrix import *
__all__ = defmatrix.__all__
from numpy.testing import Tester
test = Tester().test
bench = Tester().bench