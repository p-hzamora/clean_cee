# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\lib\__init__.pyc
# Compiled at: 2013-04-07 07:04:04
from info import __doc__
from numpy.version import version as __version__
from type_check import *
from index_tricks import *
from function_base import *
from shape_base import *
from stride_tricks import *
from twodim_base import *
from ufunclike import *
import scimath as emath
from polynomial import *
from utils import *
from arraysetops import *
from npyio import *
from financial import *
import math
from arrayterator import *
from arraypad import *
__all__ = [
 'emath', 'math']
__all__ += type_check.__all__
__all__ += index_tricks.__all__
__all__ += function_base.__all__
__all__ += shape_base.__all__
__all__ += stride_tricks.__all__
__all__ += twodim_base.__all__
__all__ += ufunclike.__all__
__all__ += arraypad.__all__
__all__ += polynomial.__all__
__all__ += utils.__all__
__all__ += arraysetops.__all__
__all__ += npyio.__all__
__all__ += financial.__all__
from numpy.testing import Tester
test = Tester().test
bench = Tester().bench