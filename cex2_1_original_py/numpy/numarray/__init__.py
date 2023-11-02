# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\numarray\__init__.pyc
# Compiled at: 2013-04-07 07:04:04
from util import *
from numerictypes import *
from functions import *
from ufuncs import *
from compat import *
from session import *
import util, numerictypes, functions, ufuncs, compat, session
__all__ = [
 'session', 'numerictypes']
__all__ += util.__all__
__all__ += numerictypes.__all__
__all__ += functions.__all__
__all__ += ufuncs.__all__
__all__ += compat.__all__
__all__ += session.__all__
del util
del functions
del ufuncs
del compat
from numpy.testing import Tester
test = Tester().test
bench = Tester().bench