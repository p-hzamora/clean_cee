# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\stackplot.pyc
# Compiled at: 2012-11-06 08:42:20
"""
Stacked area plot for 1D arrays inspired by Douglas Y'barbo's stackoverflow
answer:
http://stackoverflow.com/questions/2225995/how-can-i-create-stacked-line-graph-with-matplotlib

(http://stackoverflow.com/users/66549/doug)

"""
import numpy as np
__all__ = [
 'stackplot']

def stackplot(axes, x, *args, **kwargs):
    """Draws a stacked area plot.

    *x* : 1d array of dimension N

    *y* : 2d array of dimension MxN, OR any number 1d arrays each of dimension
          1xN. The data is assumed to be unstacked. Each of the following
          calls is legal::

            stackplot(x, y)               # where y is MxN
            stackplot(x, y1, y2, y3, y4)  # where y1, y2, y3, y4, are all 1xNm

    Keyword arguments:

    *colors* : A list or tuple of colors. These will be cycled through and
               used to colour the stacked areas.
               All other keyword arguments are passed to
               :func:`~matplotlib.Axes.fill_between`

    Returns *r* : A list of
    :class:`~matplotlib.collections.PolyCollection`, one for each
    element in the stacked area plot.
    """
    if len(args) == 1:
        y = np.atleast_2d(*args)
    else:
        if len(args) > 1:
            y = np.row_stack(args)
        colors = kwargs.pop('colors', None)
        if colors is not None:
            axes.set_color_cycle(colors)
        y_stack = np.cumsum(y, axis=0)
        r = []
        r.append(axes.fill_between(x, 0, y_stack[0, :], facecolor=axes._get_lines.color_cycle.next(), **kwargs))
        for i in xrange(len(y) - 1):
            r.append(axes.fill_between(x, y_stack[i, :], y_stack[i + 1, :], facecolor=axes._get_lines.color_cycle.next(), **kwargs))

    return r