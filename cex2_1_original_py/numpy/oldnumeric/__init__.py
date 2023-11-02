# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\oldnumeric\__init__.pyc
# Compiled at: 2013-04-07 07:04:04
from numpy import *

def _move_axis_to_0(a, axis):
    if axis == 0:
        return a
    n = len(a.shape)
    if axis < 0:
        axis += n
    axes = range(1, axis + 1) + [0] + range(axis + 1, n)
    return transpose(a, axes)


from compat import *
from functions import *
from precision import *
from ufuncs import *
from misc import *
import compat, precision, functions, misc, ufuncs, numpy
__version__ = numpy.__version__
del numpy
__all__ = [
 '__version__']
__all__ += compat.__all__
__all__ += precision.__all__
__all__ += functions.__all__
__all__ += ufuncs.__all__
__all__ += misc.__all__
del compat
del functions
del precision
del ufuncs
del misc
from numpy.testing import Tester
test = Tester().test
bench = Tester().bench