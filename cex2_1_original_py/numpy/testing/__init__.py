# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\testing\__init__.pyc
# Compiled at: 2013-04-07 07:04:04
"""Common test support for all numpy test scripts.

This single module should provide all the common functionality for numpy tests
in a single location, so that test scripts can just import it and work right
away.
"""
from unittest import TestCase
import decorators as dec
from .utils import *
from .numpytest import *
from nosetester import NoseTester as Tester
from nosetester import run_module_suite
test = Tester().test