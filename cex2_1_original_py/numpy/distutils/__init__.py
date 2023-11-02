# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\distutils\__init__.pyc
# Compiled at: 2013-04-07 07:04:04
import sys
if sys.version_info[0] < 3:
    from __version__ import version as __version__
    import ccompiler, unixccompiler
    from info import __doc__
    from npy_pkg_config import *
    try:
        import __config__
        _INSTALLED = True
    except ImportError:
        _INSTALLED = False

else:
    from numpy.distutils.__version__ import version as __version__
    import numpy.distutils.ccompiler, numpy.distutils.unixccompiler
    from numpy.distutils.info import __doc__
    from numpy.distutils.npy_pkg_config import *
    try:
        import numpy.distutils.__config__
        _INSTALLED = True
    except ImportError:
        _INSTALLED = False

if _INSTALLED:
    from numpy.testing import Tester
    test = Tester().test
    bench = Tester().bench