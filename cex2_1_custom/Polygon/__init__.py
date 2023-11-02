# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Polygon\__init__.pyc
# Compiled at: 2012-05-23 14:14:46
from cPolygon import *
__version__ = version
__author__ = author
__license__ = license
del version
del author
del license

def __createPolygon(contour, hole):
    """rebuild Polygon from pickled data"""
    p = Polygon()
    map(p.addContour, contour, hole)
    return p


def __tuples(a):
    """map an array or list of lists to a tuple of tuples"""
    return tuple(map(tuple, a))


def __reducePolygon(p):
    """return pickle data for Polygon """
    return (
     __createPolygon, (tuple([ __tuples(x) for x in p ]), p.isHole()))


import copy_reg
copy_reg.constructor(__createPolygon)
copy_reg.pickle(Polygon, __reducePolygon)
del copy_reg