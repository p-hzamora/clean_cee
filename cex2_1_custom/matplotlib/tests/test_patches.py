# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\test_patches.pyc
# Compiled at: 2012-10-30 18:11:14
"""
Tests specific to the patches module.
"""
from numpy.testing import assert_array_equal
from matplotlib.patches import Polygon

def test_Polygon_close():
    """
    Github issue #1018 identified a bug in the Polygon handling
    of the closed attribute; the path was not getting closed
    when set_xy was used to set the vertices.
    """
    xy = [
     [
      0, 0], [0, 1], [1, 1]]
    xyclosed = xy + [[0, 0]]
    p = Polygon(xy, closed=True)
    assert_array_equal(p.get_xy(), xyclosed)
    p.set_xy(xy)
    assert_array_equal(p.get_xy(), xyclosed)
    p = Polygon(xyclosed, closed=False)
    assert_array_equal(p.get_xy(), xy)
    p.set_xy(xyclosed)
    assert_array_equal(p.get_xy(), xy)
    p = Polygon(xy, closed=False)
    assert_array_equal(p.get_xy(), xy)
    p.set_xy(xy)
    assert_array_equal(p.get_xy(), xy)
    p = Polygon(xyclosed, closed=True)
    assert_array_equal(p.get_xy(), xyclosed)
    p.set_xy(xyclosed)
    assert_array_equal(p.get_xy(), xyclosed)