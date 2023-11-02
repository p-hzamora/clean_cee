# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\weave\__init__.pyc
# Compiled at: 2013-03-29 22:51:36
"""
C/C++ integration
=================

        inline     -- a function for including C/C++ code within Python
        blitz      -- a function for compiling Numeric expressions to C++
        ext_tools  -- a module that helps construct C/C++ extension modules.
        accelerate -- a module that inline accelerates Python functions

.. note:: On Linux one needs to have the Python development headers installed
          in order to be able to compile things with the `weave` module.
          Since this is a runtime dependency these headers (typically in a
          pythonX.Y-dev package) are not always installed when installing
          scipy.

"""
from __future__ import absolute_import, print_function
import sys
if sys.version_info[0] >= 3:
    raise ImportError('scipy.weave only supports Python 2.x')
from .weave_version import weave_version as __version__
try:
    from .blitz_tools import blitz
except ImportError:
    pass

from .inline_tools import inline
from . import ext_tools
from .ext_tools import ext_module, ext_function
try:
    from .accelerate_tools import accelerate
except:
    pass

from numpy.testing import Tester
test = Tester().test