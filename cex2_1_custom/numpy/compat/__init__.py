# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\compat\__init__.pyc
# Compiled at: 2013-04-07 07:04:04
"""
Compatibility module.

This module contains duplicated code from Python itself or 3rd party
extensions, which may be included for the following reasons:

  * compatibility
  * we may only need a small subset of the copied library/module

"""
import _inspect, py3k
from _inspect import getargspec, formatargspec
from .py3k import *
__all__ = []
__all__.extend(_inspect.__all__)
__all__.extend(py3k.__all__)