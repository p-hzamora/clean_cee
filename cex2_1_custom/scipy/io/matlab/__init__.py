# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\io\matlab\__init__.pyc
# Compiled at: 2013-02-16 13:27:30
"""
Utilities for dealing with MATLAB(R) files

Notes
-----
MATLAB(R) is a registered trademark of The MathWorks, Inc., 3 Apple Hill
Drive, Natick, MA 01760-2098, USA.

"""
from __future__ import division, print_function, absolute_import
from .mio import loadmat, savemat, whosmat
from . import byteordercodes
__all__ = [
 'loadmat', 'savemat', 'whosmat', 'byteordercodes']
from numpy.testing import Tester
test = Tester().test
bench = Tester().bench