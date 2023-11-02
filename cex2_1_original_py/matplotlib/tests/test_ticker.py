# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\test_ticker.pyc
# Compiled at: 2012-10-30 18:11:14
from __future__ import print_function
from nose.tools import assert_raises
from numpy.testing import assert_almost_equal
import numpy as np, matplotlib.ticker as mticker

def test_MaxNLocator():
    loc = mticker.MaxNLocator(nbins=5)
    test_value = np.array([20.0, 40.0, 60.0, 80.0, 100.0])
    assert_almost_equal(loc.tick_values(20, 100), test_value)
    test_value = np.array([0.0, 0.0002, 0.0004, 0.0006, 0.0008, 0.001])
    assert_almost_equal(loc.tick_values(0.001, 0.0001), test_value)
    test_value = np.array([-1000000000000000.0, -500000000000000.0, 0.0, 500000000000000.0, 1000000000000000.0])
    assert_almost_equal(loc.tick_values(-1000000000000000.0, 1000000000000000.0), test_value)


def test_LinearLocator():
    loc = mticker.LinearLocator(numticks=3)
    test_value = np.array([-0.8, -0.3, 0.2])
    assert_almost_equal(loc.tick_values(-0.8, 0.2), test_value)


def test_MultipleLocator():
    loc = mticker.MultipleLocator(base=3.147)
    test_value = np.array([-6.294, -3.147, 0.0, 3.147, 6.294, 9.441])
    assert_almost_equal(loc.tick_values(-7, 10), test_value)


def test_LogLocator():
    loc = mticker.LogLocator(numticks=5)
    assert_raises(ValueError, loc.tick_values, 0, 1000)
    test_value = np.array([0.001, 0.1, 10.0, 
     1000.0, 100000.0, 10000000.0])
    assert_almost_equal(loc.tick_values(0.001, 110000.0), test_value)
    loc = mticker.LogLocator(base=2)
    test_value = np.array([1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0])
    assert_almost_equal(loc.tick_values(1, 100), test_value)


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'], exit=False)