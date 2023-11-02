# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tri\triplot.pyc
# Compiled at: 2012-10-30 18:11:14
from __future__ import print_function
from matplotlib.cbook import ls_mapper
from matplotlib.patches import PathPatch
from matplotlib.path import Path
from matplotlib.tri.triangulation import Triangulation
import numpy as np

def triplot(ax, *args, **kwargs):
    """
    Draw a unstructured triangular grid as lines and/or markers.

    The triangulation to plot can be specified in one of two ways;
    either::

      triplot(triangulation, ...)

    where triangulation is a :class:`~matplotlib.tri.Triangulation`
    object, or

    ::

      triplot(x, y, ...)
      triplot(x, y, triangles, ...)
      triplot(x, y, triangles=triangles, ...)
      triplot(x, y, mask=mask, ...)
      triplot(x, y, triangles, mask=mask, ...)

    in which case a Triangulation object will be created.  See
    :class:`~matplotlib.tri.Triangulation` for a explanation of these
    possibilities.

    The remaining args and kwargs are the same as for
    :meth:`~matplotlib.axes.Axes.plot`.

    **Example:**

        .. plot:: mpl_examples/pylab_examples/triplot_demo.py
    """
    import matplotlib.axes
    tri, args, kwargs = Triangulation.get_from_args_and_kwargs(*args, **kwargs)
    x = tri.x
    y = tri.y
    edges = tri.edges
    fmt = ''
    if len(args) > 0:
        fmt = args[0]
    linestyle, marker, color = matplotlib.axes._process_plot_format(fmt)
    if linestyle is not None and linestyle is not 'None':
        kw = kwargs.copy()
        kw.pop('marker', None)
        kw['linestyle'] = ls_mapper[linestyle]
        kw['edgecolor'] = color
        kw['facecolor'] = None
        vertices = np.column_stack((x[edges].flatten(), y[edges].flatten()))
        codes = ([Path.MOVETO] + [Path.LINETO]) * len(edges)
        path = Path(vertices, codes)
        pathpatch = PathPatch(path, **kw)
        ax.add_patch(pathpatch)
    kwargs['linestyle'] = ''
    ax.plot(x, y, *args, **kwargs)
    return