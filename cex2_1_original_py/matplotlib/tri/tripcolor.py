# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tri\tripcolor.pyc
# Compiled at: 2012-10-30 18:11:14
from __future__ import print_function
from matplotlib.collections import PolyCollection, TriMesh
from matplotlib.colors import Normalize
from matplotlib.tri.triangulation import Triangulation
import numpy as np

def tripcolor(ax, *args, **kwargs):
    """
    Create a pseudocolor plot of an unstructured triangular grid.

    The triangulation can be specified in one of two ways; either::

      tripcolor(triangulation, ...)

    where triangulation is a :class:`~matplotlib.tri.Triangulation`
    object, or

    ::

      tripcolor(x, y, ...)
      tripcolor(x, y, triangles, ...)
      tripcolor(x, y, triangles=triangles, ...)
      tripcolor(x, y, mask=mask, ...)
      tripcolor(x, y, triangles, mask=mask, ...)

    in which case a Triangulation object will be created.  See
    :class:`~matplotlib.tri.Triangulation` for a explanation of these
    possibilities.

    The next argument must be *C*, the array of color values, either
    one per point in the triangulation if color values are defined at
    points, or one per triangle in the triangulation if color values
    are defined at triangles. If there are the same number of points
    and triangles in the triangulation it is assumed that color
    values are defined at points; to force the use of color values at
    triangles use the kwarg *facecolors*=C instead of just *C*.

    *shading* may be 'flat' (the default) or 'gouraud'. If *shading*
    is 'flat' and C values are defined at points, the color values
    used for each triangle are from the mean C of the triangle's
    three points. If *shading* is 'gouraud' then color values must be
    defined at points.  *shading* of 'faceted' is deprecated;
    please use *edgecolors* instead.

    The remaining kwargs are the same as for
    :meth:`~matplotlib.axes.Axes.pcolor`.

    **Example:**

        .. plot:: mpl_examples/pylab_examples/tripcolor_demo.py
    """
    if not ax._hold:
        ax.cla()
    alpha = kwargs.pop('alpha', 1.0)
    norm = kwargs.pop('norm', None)
    cmap = kwargs.pop('cmap', None)
    vmin = kwargs.pop('vmin', None)
    vmax = kwargs.pop('vmax', None)
    shading = kwargs.pop('shading', 'flat')
    facecolors = kwargs.pop('facecolors', None)
    tri, args, kwargs = Triangulation.get_from_args_and_kwargs(*args, **kwargs)
    if facecolors is not None:
        C = facecolors
    else:
        C = np.asarray(args[0])
    if facecolors is None and len(C) == len(tri.triangles) and len(C) != len(tri.x) and shading != 'gouraud':
        facecolors = C
    if facecolors is None and len(C) != len(tri.x) or facecolors is not None and len(C) != len(tri.triangles):
        raise ValueError('Length of color values array must be the same as either the number of triangulation points or triangles')
    linewidths = (0.25, )
    if 'linewidth' in kwargs:
        kwargs['linewidths'] = kwargs.pop('linewidth')
    kwargs.setdefault('linewidths', linewidths)
    if shading == 'faceted':
        edgecolors = 'k'
    else:
        edgecolors = 'none'
    if 'edgecolor' in kwargs:
        kwargs['edgecolors'] = kwargs.pop('edgecolor')
    ec = kwargs.setdefault('edgecolors', edgecolors)
    if 'antialiased' in kwargs:
        kwargs['antialiaseds'] = kwargs.pop('antialiased')
    if 'antialiaseds' not in kwargs and ec.lower() == 'none':
        kwargs['antialiaseds'] = False
    if shading == 'gouraud':
        if facecolors is not None:
            raise ValueError('Gouraud shading does not support the use of facecolors kwarg')
        if len(C) != len(tri.x):
            raise ValueError('For gouraud shading, the length of color values array must be the same as the number of triangulation points')
        collection = TriMesh(tri, **kwargs)
    else:
        maskedTris = tri.get_masked_triangles()
        verts = np.concatenate((tri.x[maskedTris][(..., np.newaxis)],
         tri.y[maskedTris][(..., np.newaxis)]), axis=2)
        if facecolors is None:
            C = C[maskedTris].mean(axis=1)
        elif tri.mask is not None:
            C = C.compress(1 - tri.mask)
        collection = PolyCollection(verts, **kwargs)
    collection.set_alpha(alpha)
    collection.set_array(C)
    assert norm is not None and isinstance(norm, Normalize)
    collection.set_cmap(cmap)
    collection.set_norm(norm)
    if vmin is not None or vmax is not None:
        collection.set_clim(vmin, vmax)
    else:
        collection.autoscale_None()
    ax.grid(False)
    minx = tri.x.min()
    maxx = tri.x.max()
    miny = tri.y.min()
    maxy = tri.y.max()
    corners = ((minx, miny), (maxx, maxy))
    ax.update_datalim(corners)
    ax.autoscale_view()
    ax.add_collection(collection)
    return collection