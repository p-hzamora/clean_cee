# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\nxutils.pyc
# Compiled at: 2012-10-30 18:11:14
import warnings
from matplotlib import path

def pnpoly(x, y, xyverts):
    """
    inside = pnpoly(x, y, xyverts)

    Return 1 if x,y is inside the polygon, 0 otherwise.

    *xyverts*
        a sequence of x,y vertices.

    A point on the boundary may be treated as inside or outside.

    .. deprecated:: 1.2.0
        Use :meth:`~matplotlib.path.Path.contains_point` instead.
    """
    warnings.warn('nxutils is deprecated.  Use matplotlib.path.Path.contains_point instead.', DeprecationWarning)
    p = path.Path(xyverts)
    return p.contains_point(x, y)


def points_inside_poly(xypoints, xyverts):
    """
    mask = points_inside_poly(xypoints, xyverts)

    Returns a boolean ndarray, True for points inside the polygon.

    *xypoints*
        a sequence of N x,y pairs.

    *xyverts*
        sequence of x,y vertices of the polygon.

    A point on the boundary may be treated as inside or outside.

    .. deprecated:: 1.2.0
        Use :meth:`~matplotlib.path.Path.contains_points` instead.
    """
    warnings.warn('nxutils is deprecated.  Use matplotlib.path.Path.contains_points instead.', DeprecationWarning)
    p = path.Path(xyverts)
    return p.contains_points(xypoints)