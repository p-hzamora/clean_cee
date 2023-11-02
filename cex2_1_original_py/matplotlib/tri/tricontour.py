# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tri\tricontour.pyc
# Compiled at: 2012-10-30 18:11:14
from __future__ import print_function
from matplotlib.contour import ContourSet
from matplotlib.tri.triangulation import Triangulation
import matplotlib._tri as _tri, numpy as np

class TriContourSet(ContourSet):
    """
    Create and store a set of contour lines or filled regions for
    a triangular grid.

    User-callable method: clabel

    Useful attributes:
      ax:
        the axes object in which the contours are drawn
      collections:
        a silent_list of LineCollections or PolyCollections
      levels:
        contour levels
      layers:
        same as levels for line contours; half-way between
        levels for filled contours.  See _process_colors method.
    """

    def __init__(self, ax, *args, **kwargs):
        """
        Draw triangular grid contour lines or filled regions,
        depending on whether keyword arg 'filled' is False
        (default) or True.

        The first argument of the initializer must be an axes
        object.  The remaining arguments and keyword arguments
        are described in TriContourSet.tricontour_doc.
        """
        ContourSet.__init__(self, ax, *args, **kwargs)

    def _process_args(self, *args, **kwargs):
        """
        Process args and kwargs.
        """
        if isinstance(args[0], TriContourSet):
            C = args[0].cppContourGenerator
            if self.levels is None:
                self.levels = args[0].levels
        else:
            tri, z = self._contour_args(args, kwargs)
            C = _tri.TriContourGenerator(tri.get_cpp_triangulation(), z)
            x0 = tri.x.min()
            x1 = tri.x.max()
            y0 = tri.y.min()
            y1 = tri.y.max()
            self.ax.update_datalim([(x0, y0), (x1, y1)])
            self.ax.autoscale_view()
        self.cppContourGenerator = C
        return

    def _get_allsegs_and_allkinds(self):
        """
        Create and return allsegs and allkinds by calling underlying C code.
        """
        allsegs = []
        if self.filled:
            lowers, uppers = self._get_lowers_and_uppers()
            allkinds = []
            for lower, upper in zip(lowers, uppers):
                segs, kinds = self.cppContourGenerator.create_filled_contour(lower, upper)
                allsegs.append([segs])
                allkinds.append([kinds])

        else:
            allkinds = None
            for level in self.levels:
                segs = self.cppContourGenerator.create_contour(level)
                allsegs.append(segs)

        return (
         allsegs, allkinds)

    def _contour_args(self, args, kwargs):
        if self.filled:
            fn = 'contourf'
        else:
            fn = 'contour'
        tri, args, kwargs = Triangulation.get_from_args_and_kwargs(*args, **kwargs)
        z = np.asarray(args[0])
        if z.shape != tri.x.shape:
            raise ValueError('z array must have same length as triangulation xand y arrays')
        self.zmax = z.max()
        self.zmin = z.min()
        if self.logscale and self.zmin <= 0:
            raise ValueError('Cannot %s log of negative values.' % fn)
        self._contour_level_args(z, args[1:])
        return (tri, z)

    tricontour_doc = "\n        Draw contours on an unstructured triangular grid.\n        :func:`~matplotlib.pyplot.tricontour` and\n        :func:`~matplotlib.pyplot.tricontourf` draw contour lines and\n        filled contours, respectively.  Except as noted, function\n        signatures and return values are the same for both versions.\n\n        The triangulation can be specified in one of two ways; either::\n\n          tricontour(triangulation, ...)\n\n        where triangulation is a :class:`~matplotlib.tri.Triangulation`\n        object, or\n\n        ::\n\n          tricontour(x, y, ...)\n          tricontour(x, y, triangles, ...)\n          tricontour(x, y, triangles=triangles, ...)\n          tricontour(x, y, mask=mask, ...)\n          tricontour(x, y, triangles, mask=mask, ...)\n\n        in which case a Triangulation object will be created.  See\n        :class:`~matplotlib.tri.Triangulation` for a explanation of\n        these possibilities.\n\n        The remaining arguments may be::\n\n          tricontour(..., Z)\n\n        where *Z* is the array of values to contour, one per point\n        in the triangulation.  The level values are chosen\n        automatically.\n\n        ::\n\n          tricontour(..., Z, N)\n\n        contour *N* automatically-chosen levels.\n\n        ::\n\n          tricontour(..., Z, V)\n\n        draw contour lines at the values specified in sequence *V*\n\n        ::\n\n          tricontourf(..., Z, V)\n\n        fill the (len(*V*)-1) regions between the values in *V*\n\n        ::\n\n          tricontour(Z, **kwargs)\n\n        Use keyword args to control colors, linewidth, origin, cmap ... see\n        below for more details.\n\n        ``C = tricontour(...)`` returns a\n        :class:`~matplotlib.contour.TriContourSet` object.\n\n        Optional keyword arguments:\n\n          *colors*: [ *None* | string | (mpl_colors) ]\n            If *None*, the colormap specified by cmap will be used.\n\n            If a string, like 'r' or 'red', all levels will be plotted in this\n            color.\n\n            If a tuple of matplotlib color args (string, float, rgb, etc),\n            different levels will be plotted in different colors in the order\n            specified.\n\n          *alpha*: float\n            The alpha blending value\n\n          *cmap*: [ *None* | Colormap ]\n            A cm :class:`~matplotlib.colors.Colormap` instance or\n            *None*. If *cmap* is *None* and *colors* is *None*, a\n            default Colormap is used.\n\n          *norm*: [ *None* | Normalize ]\n            A :class:`matplotlib.colors.Normalize` instance for\n            scaling data values to colors. If *norm* is *None* and\n            *colors* is *None*, the default linear scaling is used.\n\n          *levels* [level0, level1, ..., leveln]\n            A list of floating point numbers indicating the level\n            curves to draw; eg to draw just the zero contour pass\n            ``levels=[0]``\n\n          *origin*: [ *None* | 'upper' | 'lower' | 'image' ]\n            If *None*, the first value of *Z* will correspond to the\n            lower left corner, location (0,0). If 'image', the rc\n            value for ``image.origin`` will be used.\n\n            This keyword is not active if *X* and *Y* are specified in\n            the call to contour.\n\n          *extent*: [ *None* | (x0,x1,y0,y1) ]\n\n            If *origin* is not *None*, then *extent* is interpreted as\n            in :func:`matplotlib.pyplot.imshow`: it gives the outer\n            pixel boundaries. In this case, the position of Z[0,0]\n            is the center of the pixel, not a corner. If *origin* is\n            *None*, then (*x0*, *y0*) is the position of Z[0,0], and\n            (*x1*, *y1*) is the position of Z[-1,-1].\n\n            This keyword is not active if *X* and *Y* are specified in\n            the call to contour.\n\n          *locator*: [ *None* | ticker.Locator subclass ]\n            If *locator* is None, the default\n            :class:`~matplotlib.ticker.MaxNLocator` is used. The\n            locator is used to determine the contour levels if they\n            are not given explicitly via the *V* argument.\n\n          *extend*: [ 'neither' | 'both' | 'min' | 'max' ]\n            Unless this is 'neither', contour levels are automatically\n            added to one or both ends of the range so that all data\n            are included. These added ranges are then mapped to the\n            special colormap values which default to the ends of the\n            colormap range, but can be set via\n            :meth:`matplotlib.colors.Colormap.set_under` and\n            :meth:`matplotlib.colors.Colormap.set_over` methods.\n\n          *xunits*, *yunits*: [ *None* | registered units ]\n            Override axis units by specifying an instance of a\n            :class:`matplotlib.units.ConversionInterface`.\n\n\n        tricontour-only keyword arguments:\n\n          *linewidths*: [ *None* | number | tuple of numbers ]\n            If *linewidths* is *None*, the default width in\n            ``lines.linewidth`` in ``matplotlibrc`` is used.\n\n            If a number, all levels will be plotted with this linewidth.\n\n            If a tuple, different levels will be plotted with different\n            linewidths in the order specified\n\n          *linestyles*: [ *None* | 'solid' | 'dashed' | 'dashdot' | 'dotted' ]\n            If *linestyles* is *None*, the 'solid' is used.\n\n            *linestyles* can also be an iterable of the above strings\n            specifying a set of linestyles to be used. If this\n            iterable is shorter than the number of contour levels\n            it will be repeated as necessary.\n\n            If contour is using a monochrome colormap and the contour\n            level is less than 0, then the linestyle specified\n            in ``contour.negative_linestyle`` in ``matplotlibrc``\n            will be used.\n\n        tricontourf-only keyword arguments:\n\n          *antialiased*: [ *True* | *False* ]\n            enable antialiasing\n\n          *nchunk*: [ 0 | integer ]\n            If 0, no subdivision of the domain. Specify a positive integer to\n            divide the domain into subdomains of roughly *nchunk* by *nchunk*\n            points. This may never actually be advantageous, so this option may\n            be removed. Chunking introduces artifacts at the chunk boundaries\n            unless *antialiased* is *False*.\n\n        Note: tricontourf fills intervals that are closed at the top; that\n        is, for boundaries *z1* and *z2*, the filled region is::\n\n            z1 < z <= z2\n\n        There is one exception: if the lowest boundary coincides with\n        the minimum value of the *z* array, then that minimum value\n        will be included in the lowest interval.\n\n        **Examples:**\n\n        .. plot:: mpl_examples/pylab_examples/tricontour_demo.py\n        "


def tricontour(ax, *args, **kwargs):
    if not ax._hold:
        ax.cla()
    kwargs['filled'] = False
    return TriContourSet(ax, *args, **kwargs)


tricontour.__doc__ = TriContourSet.tricontour_doc

def tricontourf(ax, *args, **kwargs):
    if not ax._hold:
        ax.cla()
    kwargs['filled'] = True
    return TriContourSet(ax, *args, **kwargs)


tricontourf.__doc__ = TriContourSet.tricontour_doc