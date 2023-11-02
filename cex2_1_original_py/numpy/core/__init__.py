# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\core\__init__.pyc
# Compiled at: 2013-04-07 07:04:04
from info import __doc__
from numpy.version import version as __version__
import multiarray, umath, _internal, numerictypes as nt
multiarray.set_typeDict(nt.sctypeDict)
import numeric
from numeric import *
import fromnumeric
from fromnumeric import *
import defchararray as char, records as rec
from records import *
from memmap import *
from defchararray import chararray
import scalarmath, function_base
from function_base import *
import machar
from machar import *
import getlimits
from getlimits import *
import shape_base
from shape_base import *
del nt
from fromnumeric import amax as max, amin as min, round_ as round
from numeric import absolute as abs
__all__ = [
 'char', 'rec', 'memmap']
__all__ += numeric.__all__
__all__ += fromnumeric.__all__
__all__ += rec.__all__
__all__ += ['chararray']
__all__ += function_base.__all__
__all__ += machar.__all__
__all__ += getlimits.__all__
__all__ += shape_base.__all__
from numpy.testing import Tester
test = Tester().test
bench = Tester().bench

def _ufunc_reconstruct(module, name):
    mod = __import__(module)
    return getattr(mod, name)


def _ufunc_reduce(func):
    from pickle import whichmodule
    name = func.__name__
    return (_ufunc_reconstruct, (whichmodule(func, name), name))


import sys
if sys.version_info[0] < 3:
    import copy_reg as copyreg
else:
    import copyreg
copyreg.pickle(ufunc, _ufunc_reduce, _ufunc_reconstruct)
del copyreg
del sys
del _ufunc_reduce