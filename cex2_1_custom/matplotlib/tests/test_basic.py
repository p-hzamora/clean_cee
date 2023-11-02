# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\test_basic.pyc
# Compiled at: 2012-10-30 18:11:14
from __future__ import print_function
from nose.tools import assert_equal
from matplotlib.testing.decorators import knownfailureif
import sys

def test_simple():
    assert_equal(2, 2)


@knownfailureif(True)
def test_simple_knownfail():
    assert_equal(2, 3)


from pylab import *

def test_override_builtins():
    ok_to_override = set([
     '__name__', 
     '__doc__', 
     '__package__', 
     'any', 
     'all', 
     'sum'])
    if sys.version_info[0] >= 3:
        builtins = sys.modules['builtins']
    else:
        builtins = sys.modules['__builtin__']
    overridden = False
    for key in globals().keys():
        if key in dir(builtins):
            if globals()[key] != getattr(builtins, key) and key not in ok_to_override:
                print("'%s' was overridden in globals()." % key)
                overridden = True

    assert not overridden