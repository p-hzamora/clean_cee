# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\quiver.pyc
# Compiled at: 2012-10-30 18:11:14
"""
Support for plotting vector fields.

Presently this contains Quiver and Barb. Quiver plots an arrow in the
direction of the vector, with the size of the arrow related to the
magnitude of the vector.

Barbs are like quiver in that they point along a vector, but
the magnitude of the vector is given schematically by the presence of barbs
or flags on the barb.

This will also become a home for things such as standard
deviation ellipses, which can and will be derived very easily from
the Quiver code.
"""
from __future__ import print_function, division
import numpy as np
from numpy import ma
import matplotlib.collections as collections, matplotlib.transforms as transforms, matplotlib.text as mtext, matplotlib.artist as martist
from matplotlib.artist import allow_rasterization
from matplotlib import docstring
import matplotlib.font_manager as font_manager, matplotlib.cbook as cbook
from matplotlib.cbook import delete_masked_points
from matplotlib.patches import CirclePolygon
import math
_quiver_doc = '\nPlot a 2-D field of arrows.\n\ncall signatures::\n\n  quiver(U, V, **kw)\n  quiver(U, V, C, **kw)\n  quiver(X, Y, U, V, **kw)\n  quiver(X, Y, U, V, C, **kw)\n\nArguments:\n\n  *X*, *Y*:\n    The x and y coordinates of the arrow locations (default is tail of\n    arrow; see *pivot* kwarg)\n\n  *U*, *V*:\n    Give the x and y components of the arrow vectors\n\n  *C*:\n    An optional array used to map colors to the arrows\n\nAll arguments may be 1-D or 2-D arrays or sequences. If *X* and *Y*\nare absent, they will be generated as a uniform grid.  If *U* and *V*\nare 2-D arrays but *X* and *Y* are 1-D, and if ``len(X)`` and ``len(Y)``\nmatch the column and row dimensions of *U*, then *X* and *Y* will be\nexpanded with :func:`numpy.meshgrid`.\n\n*U*, *V*, *C* may be masked arrays, but masked *X*, *Y* are not\nsupported at present.\n\nKeyword arguments:\n\n  *units*: [ \'width\' | \'height\' | \'dots\' | \'inches\' | \'x\' | \'y\' | \'xy\' ]\n    Arrow units; the arrow dimensions *except for length* are in\n    multiples of this unit.\n\n    * \'width\' or \'height\': the width or height of the axes\n\n    * \'dots\' or \'inches\': pixels or inches, based on the figure dpi\n\n    * \'x\', \'y\', or \'xy\': *X*, *Y*, or sqrt(X^2+Y^2) data units\n\n    The arrows scale differently depending on the units.  For\n    \'x\' or \'y\', the arrows get larger as one zooms in; for other\n    units, the arrow size is independent of the zoom state.  For\n    \'width or \'height\', the arrow size increases with the width and\n    height of the axes, respectively, when the the window is resized;\n    for \'dots\' or \'inches\', resizing does not change the arrows.\n\n\n  *angles*: [ \'uv\' | \'xy\' | array ]\n    With the default \'uv\', the arrow aspect ratio is 1, so that\n    if *U*==*V* the angle of the arrow on the plot is 45 degrees\n    CCW from the *x*-axis.\n    With \'xy\', the arrow points from (x,y) to (x+u, y+v).\n    Alternatively, arbitrary angles may be specified as an array\n    of values in degrees, CCW from the *x*-axis.\n\n  *scale*: [ *None* | float ]\n    Data units per arrow length unit, e.g. m/s per plot width; a smaller\n    scale parameter makes the arrow longer.  If *None*, a simple\n    autoscaling algorithm is used, based on the average vector length\n    and the number of vectors.  The arrow length unit is given by\n    the *scale_units* parameter\n\n  *scale_units*: *None*, or any of the *units* options.\n    For example, if *scale_units* is \'inches\', *scale* is 2.0, and\n    ``(u,v) = (1,0)``, then the vector will be 0.5 inches long.\n    If *scale_units* is \'width\', then the vector will be half the width\n    of the axes.\n\n    If *scale_units* is \'x\' then the vector will be 0.5 x-axis\n    units.  To plot vectors in the x-y plane, with u and v having\n    the same units as x and y, use\n    "angles=\'xy\', scale_units=\'xy\', scale=1".\n\n  *width*:\n    Shaft width in arrow units; default depends on choice of units,\n    above, and number of vectors; a typical starting value is about\n    0.005 times the width of the plot.\n\n  *headwidth*: scalar\n    Head width as multiple of shaft width, default is 3\n\n  *headlength*: scalar\n    Head length as multiple of shaft width, default is 5\n\n  *headaxislength*: scalar\n    Head length at shaft intersection, default is 4.5\n\n  *minshaft*: scalar\n    Length below which arrow scales, in units of head length. Do not\n    set this to less than 1, or small arrows will look terrible!\n    Default is 1\n\n  *minlength*: scalar\n    Minimum length as a multiple of shaft width; if an arrow length\n    is less than this, plot a dot (hexagon) of this diameter instead.\n    Default is 1.\n\n  *pivot*: [ \'tail\' | \'middle\' | \'tip\' ]\n    The part of the arrow that is at the grid point; the arrow rotates\n    about this point, hence the name *pivot*.\n\n  *color*: [ color | color sequence ]\n    This is a synonym for the\n    :class:`~matplotlib.collections.PolyCollection` facecolor kwarg.\n    If *C* has been set, *color* has no effect.\n\nThe defaults give a slightly swept-back arrow; to make the head a\ntriangle, make *headaxislength* the same as *headlength*. To make the\narrow more pointed, reduce *headwidth* or increase *headlength* and\n*headaxislength*. To make the head smaller relative to the shaft,\nscale down all the head parameters. You will probably do best to leave\nminshaft alone.\n\nlinewidths and edgecolors can be used to customize the arrow\noutlines. Additional :class:`~matplotlib.collections.PolyCollection`\nkeyword arguments:\n\n%(PolyCollection)s\n' % docstring.interpd.params
_quiverkey_doc = "\nAdd a key to a quiver plot.\n\nCall signature::\n\n  quiverkey(Q, X, Y, U, label, **kw)\n\nArguments:\n\n  *Q*:\n    The Quiver instance returned by a call to quiver.\n\n  *X*, *Y*:\n    The location of the key; additional explanation follows.\n\n  *U*:\n    The length of the key\n\n  *label*:\n    A string with the length and units of the key\n\nKeyword arguments:\n\n  *coordinates* = [ 'axes' | 'figure' | 'data' | 'inches' ]\n    Coordinate system and units for *X*, *Y*: 'axes' and 'figure' are\n    normalized coordinate systems with 0,0 in the lower left and 1,1\n    in the upper right; 'data' are the axes data coordinates (used for\n    the locations of the vectors in the quiver plot itself); 'inches'\n    is position in the figure in inches, with 0,0 at the lower left\n    corner.\n\n  *color*:\n    overrides face and edge colors from *Q*.\n\n  *labelpos* = [ 'N' | 'S' | 'E' | 'W' ]\n    Position the label above, below, to the right, to the left of the\n    arrow, respectively.\n\n  *labelsep*:\n    Distance in inches between the arrow and the label.  Default is\n    0.1\n\n  *labelcolor*:\n    defaults to default :class:`~matplotlib.text.Text` color.\n\n  *fontproperties*:\n    A dictionary with keyword arguments accepted by the\n    :class:`~matplotlib.font_manager.FontProperties` initializer:\n    *family*, *style*, *variant*, *size*, *weight*\n\nAny additional keyword arguments are used to override vector\nproperties taken from *Q*.\n\nThe positioning of the key depends on *X*, *Y*, *coordinates*, and\n*labelpos*.  If *labelpos* is 'N' or 'S', *X*, *Y* give the position\nof the middle of the key arrow.  If *labelpos* is 'E', *X*, *Y*\npositions the head, and if *labelpos* is 'W', *X*, *Y* positions the\ntail; in either of these two cases, *X*, *Y* is somewhere in the\nmiddle of the arrow+label key object.\n"

class QuiverKey(martist.Artist):
    """ Labelled arrow for use as a quiver plot scale key."""
    halign = {'N': 'center', 'S': 'center', 'E': 'left', 'W': 'right'}
    valign = {'N': 'bottom', 'S': 'top', 'E': 'center', 'W': 'center'}
    pivot = {'N': 'mid', 'S': 'mid', 'E': 'tip', 'W': 'tail'}

    def __init__(self, Q, X, Y, U, label, **kw):
        martist.Artist.__init__(self)
        self.Q = Q
        self.X = X
        self.Y = Y
        self.U = U
        self.coord = kw.pop('coordinates', 'axes')
        self.color = kw.pop('color', None)
        self.label = label
        self._labelsep_inches = kw.pop('labelsep', 0.1)
        self.labelsep = self._labelsep_inches * Q.ax.figure.dpi

        def on_dpi_change(fig):
            self.labelsep = self._labelsep_inches * fig.dpi
            self._initialized = False

        Q.ax.figure.callbacks.connect('dpi_changed', on_dpi_change)
        self.labelpos = kw.pop('labelpos', 'N')
        self.labelcolor = kw.pop('labelcolor', None)
        self.fontproperties = kw.pop('fontproperties', dict())
        self.kw = kw
        _fp = self.fontproperties
        self.text = mtext.Text(text=label, horizontalalignment=self.halign[self.labelpos], verticalalignment=self.valign[self.labelpos], fontproperties=font_manager.FontProperties(**_fp))
        if self.labelcolor is not None:
            self.text.set_color(self.labelcolor)
        self._initialized = False
        self.zorder = Q.zorder + 0.1
        return

    __init__.__doc__ = _quiverkey_doc

    def _init(self):
        if True:
            self._set_transform()
            _pivot = self.Q.pivot
            self.Q.pivot = self.pivot[self.labelpos]
            _mask = self.Q.Umask
            self.Q.Umask = ma.nomask
            self.verts = self.Q._make_verts(np.array([self.U]), np.zeros((1, )))
            self.Q.Umask = _mask
            self.Q.pivot = _pivot
            kw = self.Q.polykw
            kw.update(self.kw)
            self.vector = collections.PolyCollection(self.verts, offsets=[
             (
              self.X, self.Y)], transOffset=self.get_transform(), **kw)
            if self.color is not None:
                self.vector.set_color(self.color)
            self.vector.set_transform(self.Q.get_transform())
            self._initialized = True
        return

    def _text_x(self, x):
        if self.labelpos == 'E':
            return x + self.labelsep
        else:
            if self.labelpos == 'W':
                return x - self.labelsep
            return x

    def _text_y(self, y):
        if self.labelpos == 'N':
            return y + self.labelsep
        else:
            if self.labelpos == 'S':
                return y - self.labelsep
            return y

    @allow_rasterization
    def draw(self, renderer):
        self._init()
        self.vector.draw(renderer)
        x, y = self.get_transform().transform_point((self.X, self.Y))
        self.text.set_x(self._text_x(x))
        self.text.set_y(self._text_y(y))
        self.text.draw(renderer)

    def _set_transform(self):
        if self.coord == 'data':
            self.set_transform(self.Q.ax.transData)
        elif self.coord == 'axes':
            self.set_transform(self.Q.ax.transAxes)
        elif self.coord == 'figure':
            self.set_transform(self.Q.ax.figure.transFigure)
        elif self.coord == 'inches':
            self.set_transform(self.Q.ax.figure.dpi_scale_trans)
        else:
            raise ValueError('unrecognized coordinates')

    def set_figure(self, fig):
        martist.Artist.set_figure(self, fig)
        self.text.set_figure(fig)

    def contains(self, mouseevent):
        if self.text.contains(mouseevent)[0] or self.vector.contains(mouseevent)[0]:
            return (True, {})
        return (
         False, {})

    quiverkey_doc = _quiverkey_doc


def _parse_args(*args):
    X, Y, U, V, C = [
     None] * 5
    args = list(args)
    if len(args) == 3 or len(args) == 5:
        C = np.atleast_1d(args.pop(-1))
    V = np.atleast_1d(args.pop(-1))
    U = np.atleast_1d(args.pop(-1))
    if U.ndim == 1:
        nr, nc = 1, U.shape[0]
    else:
        nr, nc = U.shape
    if len(args) == 2:
        X, Y = [ np.array(a).ravel() for a in args ]
        if len(X) == nc and len(Y) == nr:
            X, Y = [ a.ravel() for a in np.meshgrid(X, Y) ]
    else:
        indexgrid = np.meshgrid(np.arange(nc), np.arange(nr))
        X, Y = [ np.ravel(a) for a in indexgrid ]
    return (
     X, Y, U, V, C)


class Quiver(collections.PolyCollection):
    """
    Specialized PolyCollection for arrows.

    The only API method is set_UVC(), which can be used
    to change the size, orientation, and color of the
    arrows; their locations are fixed when the class is
    instantiated.  Possibly this method will be useful
    in animations.

    Much of the work in this class is done in the draw()
    method so that as much information as possible is available
    about the plot.  In subsequent draw() calls, recalculation
    is limited to things that might have changed, so there
    should be no performance penalty from putting the calculations
    in the draw() method.
    """

    @docstring.Substitution(_quiver_doc)
    def __init__(self, ax, *args, **kw):
        """
        The constructor takes one required argument, an Axes
        instance, followed by the args and kwargs described
        by the following pylab interface documentation:
        %s
        """
        self.ax = ax
        X, Y, U, V, C = _parse_args(*args)
        self.X = X
        self.Y = Y
        self.XY = np.hstack((X[:, np.newaxis], Y[:, np.newaxis]))
        self.N = len(X)
        self.scale = kw.pop('scale', None)
        self.headwidth = kw.pop('headwidth', 3)
        self.headlength = float(kw.pop('headlength', 5))
        self.headaxislength = kw.pop('headaxislength', 4.5)
        self.minshaft = kw.pop('minshaft', 1)
        self.minlength = kw.pop('minlength', 1)
        self.units = kw.pop('units', 'width')
        self.scale_units = kw.pop('scale_units', None)
        self.angles = kw.pop('angles', 'uv')
        self.width = kw.pop('width', None)
        self.color = kw.pop('color', 'k')
        self.pivot = kw.pop('pivot', 'tail')
        self.transform = kw.pop('transform', ax.transData)
        kw.setdefault('facecolors', self.color)
        kw.setdefault('linewidths', (0, ))
        collections.PolyCollection.__init__(self, [], offsets=self.XY, transOffset=self.transform, closed=False, **kw)
        self.polykw = kw
        self.set_UVC(U, V, C)
        self._initialized = False
        self.keyvec = None
        self.keytext = None

        def on_dpi_change(fig):
            self._new_UV = True
            self._initialized = False

        self.ax.figure.callbacks.connect('dpi_changed', on_dpi_change)
        return

    def _init(self):
        """
        Initialization delayed until first draw;
        allow time for axes setup.
        """
        if True:
            trans = self._set_transform()
            ax = self.ax
            sx, sy = trans.inverted().transform_point((
             ax.bbox.width, ax.bbox.height))
            self.span = sx
            if self.width is None:
                sn = max(8, min(25, math.sqrt(self.N)))
                self.width = 0.06 * self.span / sn
        return

    @allow_rasterization
    def draw(self, renderer):
        self._init()
        if self._new_UV or self.angles == 'xy' or self.scale_units in ('x', 'y', 'xy'):
            verts = self._make_verts(self.U, self.V)
            self.set_verts(verts, closed=False)
            self._new_UV = False
        collections.PolyCollection.draw(self, renderer)

    def set_UVC(self, U, V, C=None):
        U = ma.masked_invalid(U, copy=False).ravel()
        V = ma.masked_invalid(V, copy=False).ravel()
        mask = ma.mask_or(U.mask, V.mask, copy=False, shrink=True)
        if C is not None:
            C = ma.masked_invalid(C, copy=False).ravel()
            mask = ma.mask_or(mask, C.mask, copy=False, shrink=True)
            if mask is ma.nomask:
                C = C.filled()
            else:
                C = ma.array(C, mask=mask, copy=False)
        self.U = U.filled(1)
        self.V = V.filled(1)
        self.Umask = mask
        if C is not None:
            self.set_array(C)
        self._new_UV = True
        return

    def _dots_per_unit(self, units):
        """
        Return a scale factor for converting from units to pixels
        """
        ax = self.ax
        if units in ('x', 'y', 'xy'):
            if units == 'x':
                dx0 = ax.viewLim.width
                dx1 = ax.bbox.width
            elif units == 'y':
                dx0 = ax.viewLim.height
                dx1 = ax.bbox.height
            else:
                dxx0 = ax.viewLim.width
                dxx1 = ax.bbox.width
                dyy0 = ax.viewLim.height
                dyy1 = ax.bbox.height
                dx1 = np.sqrt(dxx1 * dxx1 + dyy1 * dyy1)
                dx0 = np.sqrt(dxx0 * dxx0 + dyy0 * dyy0)
            dx = dx1 / dx0
        elif units == 'width':
            dx = ax.bbox.width
        elif units == 'height':
            dx = ax.bbox.height
        elif units == 'dots':
            dx = 1.0
        elif units == 'inches':
            dx = ax.figure.dpi
        else:
            raise ValueError('unrecognized units')
        return dx

    def _set_transform(self):
        """
        Sets the PolygonCollection transform to go
        from arrow width units to pixels.
        """
        dx = self._dots_per_unit(self.units)
        self._trans_scale = dx
        trans = transforms.Affine2D().scale(dx)
        self.set_transform(trans)
        return trans

    def _angles_lengths(self, U, V, eps=1):
        xy = self.ax.transData.transform(self.XY)
        uv = np.hstack((U[:, np.newaxis], V[:, np.newaxis]))
        xyp = self.ax.transData.transform(self.XY + eps * uv)
        dxy = xyp - xy
        angles = np.arctan2(dxy[:, 1], dxy[:, 0])
        lengths = np.absolute(dxy[:, 0] + dxy[:, 1] * complex(0.0, 1.0)) / eps
        return (angles, lengths)

    def _make_verts(self, U, V):
        uv = U + V * complex(0.0, 1.0)
        if self.angles == 'xy' and self.scale_units == 'xy':
            angles, lengths = self._angles_lengths(U, V, eps=1)
        elif self.angles == 'xy' or self.scale_units == 'xy':
            angles, lengths = self._angles_lengths(U, V, eps=np.abs(self.ax.dataLim.extents).max() * 0.001)
        if self.scale_units == 'xy':
            a = lengths
        else:
            a = np.absolute(uv)
        if self.scale is None:
            sn = max(10, math.sqrt(self.N))
            if self.Umask is not ma.nomask:
                amean = a[~self.Umask].mean()
            else:
                amean = a.mean()
            scale = 1.8 * amean * sn / self.span
        if self.scale_units is None:
            if self.scale is None:
                self.scale = scale
            widthu_per_lenu = 1.0
        else:
            if self.scale_units == 'xy':
                dx = 1
            else:
                dx = self._dots_per_unit(self.scale_units)
            widthu_per_lenu = dx / self._trans_scale
            if self.scale is None:
                self.scale = scale * widthu_per_lenu
        length = a * (widthu_per_lenu / (self.scale * self.width))
        X, Y = self._h_arrows(length)
        if self.angles == 'xy':
            theta = angles
        elif self.angles == 'uv':
            theta = np.angle(uv)
        else:
            theta = ma.masked_invalid(self.angles, copy=True).filled(0)
            theta = theta.ravel()
            theta *= np.pi / 180.0
        theta.shape = (
         theta.shape[0], 1)
        xy = (X + Y * complex(0.0, 1.0)) * np.exp(complex(0.0, 1.0) * theta) * self.width
        xy = xy[:, :, np.newaxis]
        XY = np.concatenate((xy.real, xy.imag), axis=2)
        if self.Umask is not ma.nomask:
            XY = ma.array(XY)
            XY[self.Umask] = ma.masked
        return XY

    def _h_arrows(self, length):
        """ length is in arrow width units """
        minsh = self.minshaft * self.headlength
        N = len(length)
        length = length.reshape(N, 1)
        np.clip(length, 0, 65536, out=length)
        x = np.array([0, -self.headaxislength,
         -self.headlength, 0], np.float64)
        x = x + np.array([0, 1, 1, 1]) * length
        y = 0.5 * np.array([1, 1, self.headwidth, 0], np.float64)
        y = np.repeat(y[np.newaxis, :], N, axis=0)
        x0 = np.array([0, minsh - self.headaxislength,
         minsh - self.headlength, minsh], np.float64)
        y0 = 0.5 * np.array([1, 1, self.headwidth, 0], np.float64)
        ii = [0, 1, 2, 3, 2, 1, 0, 0]
        X = x.take(ii, 1)
        Y = y.take(ii, 1)
        Y[:, 3:-1] *= -1
        X0 = x0.take(ii)
        Y0 = y0.take(ii)
        Y0[3:-1] *= -1
        shrink = length / minsh
        X0 = shrink * X0[np.newaxis, :]
        Y0 = shrink * Y0[np.newaxis, :]
        short = np.repeat(length < minsh, 8, axis=1)
        cbook._putmask(X, short, X0)
        cbook._putmask(Y, short, Y0)
        if self.pivot[:3] == 'mid':
            X -= 0.5 * X[:, 3, np.newaxis]
        elif self.pivot[:3] == 'tip':
            X = X - X[:, 3, np.newaxis]
        tooshort = length < self.minlength
        if tooshort.any():
            th = np.arange(0, 8, 1, np.float64) * (np.pi / 3.0)
            x1 = np.cos(th) * self.minlength * 0.5
            y1 = np.sin(th) * self.minlength * 0.5
            X1 = np.repeat(x1[np.newaxis, :], N, axis=0)
            Y1 = np.repeat(y1[np.newaxis, :], N, axis=0)
            tooshort = np.repeat(tooshort, 8, 1)
            cbook._putmask(X, tooshort, X1)
            cbook._putmask(Y, tooshort, Y1)
        return (X, Y)

    quiver_doc = _quiver_doc


_barbs_doc = '\nPlot a 2-D field of barbs.\n\nCall signatures::\n\n  barb(U, V, **kw)\n  barb(U, V, C, **kw)\n  barb(X, Y, U, V, **kw)\n  barb(X, Y, U, V, C, **kw)\n\nArguments:\n\n  *X*, *Y*:\n    The x and y coordinates of the barb locations\n    (default is head of barb; see *pivot* kwarg)\n\n  *U*, *V*:\n    Give the x and y components of the barb shaft\n\n  *C*:\n    An optional array used to map colors to the barbs\n\nAll arguments may be 1-D or 2-D arrays or sequences. If *X* and *Y*\nare absent, they will be generated as a uniform grid.  If *U* and *V*\nare 2-D arrays but *X* and *Y* are 1-D, and if ``len(X)`` and ``len(Y)``\nmatch the column and row dimensions of *U*, then *X* and *Y* will be\nexpanded with :func:`numpy.meshgrid`.\n\n*U*, *V*, *C* may be masked arrays, but masked *X*, *Y* are not\nsupported at present.\n\nKeyword arguments:\n\n  *length*:\n    Length of the barb in points; the other parts of the barb\n    are scaled against this.\n    Default is 9\n\n  *pivot*: [ \'tip\' | \'middle\' ]\n    The part of the arrow that is at the grid point; the arrow rotates\n    about this point, hence the name *pivot*.  Default is \'tip\'\n\n  *barbcolor*: [ color | color sequence ]\n    Specifies the color all parts of the barb except any flags.  This\n    parameter is analagous to the *edgecolor* parameter for polygons,\n    which can be used instead. However this parameter will override\n    facecolor.\n\n  *flagcolor*: [ color | color sequence ]\n    Specifies the color of any flags on the barb.  This parameter is\n    analagous to the *facecolor* parameter for polygons, which can be\n    used instead. However this parameter will override facecolor.  If\n    this is not set (and *C* has not either) then *flagcolor* will be\n    set to match *barbcolor* so that the barb has a uniform color. If\n    *C* has been set, *flagcolor* has no effect.\n\n  *sizes*:\n    A dictionary of coefficients specifying the ratio of a given\n    feature to the length of the barb. Only those values one wishes to\n    override need to be included.  These features include:\n\n        - \'spacing\' - space between features (flags, full/half barbs)\n\n        - \'height\' - height (distance from shaft to top) of a flag or\n          full barb\n\n        - \'width\' - width of a flag, twice the width of a full barb\n\n        - \'emptybarb\' - radius of the circle used for low magnitudes\n\n  *fill_empty*:\n    A flag on whether the empty barbs (circles) that are drawn should\n    be filled with the flag color.  If they are not filled, they will\n    be drawn such that no color is applied to the center.  Default is\n    False\n\n  *rounding*:\n    A flag to indicate whether the vector magnitude should be rounded\n    when allocating barb components.  If True, the magnitude is\n    rounded to the nearest multiple of the half-barb increment.  If\n    False, the magnitude is simply truncated to the next lowest\n    multiple.  Default is True\n\n  *barb_increments*:\n    A dictionary of increments specifying values to associate with\n    different parts of the barb. Only those values one wishes to\n    override need to be included.\n\n        - \'half\' - half barbs (Default is 5)\n\n        - \'full\' - full barbs (Default is 10)\n\n        - \'flag\' - flags (default is 50)\n\n  *flip_barb*:\n    Either a single boolean flag or an array of booleans.  Single\n    boolean indicates whether the lines and flags should point\n    opposite to normal for all barbs.  An array (which should be the\n    same size as the other data arrays) indicates whether to flip for\n    each individual barb.  Normal behavior is for the barbs and lines\n    to point right (comes from wind barbs having these features point\n    towards low pressure in the Northern Hemisphere.)  Default is\n    False\n\nBarbs are traditionally used in meteorology as a way to plot the speed\nand direction of wind observations, but can technically be used to\nplot any two dimensional vector quantity.  As opposed to arrows, which\ngive vector magnitude by the length of the arrow, the barbs give more\nquantitative information about the vector magnitude by putting slanted\nlines or a triangle for various increments in magnitude, as show\nschematically below::\n\n :     /\\    \\\n :    /  \\    \\\n :   /    \\    \\    \\\n :  /      \\    \\    \\\n : ------------------------------\n\n.. note the double \\ at the end of each line to make the figure\n.. render correctly\n\nThe largest increment is given by a triangle (or "flag"). After those\ncome full lines (barbs). The smallest increment is a half line.  There\nis only, of course, ever at most 1 half line.  If the magnitude is\nsmall and only needs a single half-line and no full lines or\ntriangles, the half-line is offset from the end of the barb so that it\ncan be easily distinguished from barbs with a single full line.  The\nmagnitude for the barb shown above would nominally be 65, using the\nstandard increments of 50, 10, and 5.\n\nlinewidths and edgecolors can be used to customize the barb.\nAdditional :class:`~matplotlib.collections.PolyCollection` keyword\narguments:\n\n%(PolyCollection)s\n' % docstring.interpd.params
docstring.interpd.update(barbs_doc=_barbs_doc)

class Barbs(collections.PolyCollection):
    """
    Specialized PolyCollection for barbs.

    The only API method is :meth:`set_UVC`, which can be used to
    change the size, orientation, and color of the arrows.  Locations
    are changed using the :meth:`set_offsets` collection method.
    Possibly this method will be useful in animations.

    There is one internal function :meth:`_find_tails` which finds
    exactly what should be put on the barb given the vector magnitude.
    From there :meth:`_make_barbs` is used to find the vertices of the
    polygon to represent the barb based on this information.
    """

    @docstring.interpd
    def __init__(self, ax, *args, **kw):
        """
        The constructor takes one required argument, an Axes
        instance, followed by the args and kwargs described
        by the following pylab interface documentation:
        %(barbs_doc)s
        """
        self._pivot = kw.pop('pivot', 'tip')
        self._length = kw.pop('length', 7)
        barbcolor = kw.pop('barbcolor', None)
        flagcolor = kw.pop('flagcolor', None)
        self.sizes = kw.pop('sizes', dict())
        self.fill_empty = kw.pop('fill_empty', False)
        self.barb_increments = kw.pop('barb_increments', dict())
        self.rounding = kw.pop('rounding', True)
        self.flip = kw.pop('flip_barb', False)
        transform = kw.pop('transform', ax.transData)
        if None in (barbcolor, flagcolor):
            kw['edgecolors'] = 'face'
            if flagcolor:
                kw['facecolors'] = flagcolor
            else:
                if barbcolor:
                    kw['facecolors'] = barbcolor
                else:
                    kw.setdefault('facecolors', 'k')
        else:
            kw['edgecolors'] = barbcolor
            kw['facecolors'] = flagcolor
        x, y, u, v, c = _parse_args(*args)
        self.x = x
        self.y = y
        xy = np.hstack((x[:, np.newaxis], y[:, np.newaxis]))
        barb_size = self._length ** 2 / 4
        collections.PolyCollection.__init__(self, [], (barb_size,), offsets=xy, transOffset=transform, **kw)
        self.set_transform(transforms.IdentityTransform())
        self.set_UVC(u, v, c)
        return

    def _find_tails(self, mag, rounding=True, half=5, full=10, flag=50):
        """
        Find how many of each of the tail pieces is necessary.  Flag
        specifies the increment for a flag, barb for a full barb, and half for
        half a barb. Mag should be the magnitude of a vector (ie. >= 0).

        This returns a tuple of:

            (*number of flags*, *number of barbs*, *half_flag*, *empty_flag*)

        *half_flag* is a boolean whether half of a barb is needed,
        since there should only ever be one half on a given
        barb. *empty_flag* flag is an array of flags to easily tell if
        a barb is empty (too low to plot any barbs/flags.
        """
        if rounding:
            mag = half * (mag / half + 0.5).astype(np.int)
        num_flags = np.floor(mag / flag).astype(np.int)
        mag = np.mod(mag, flag)
        num_barb = np.floor(mag / full).astype(np.int)
        mag = np.mod(mag, full)
        half_flag = mag >= half
        empty_flag = ~(half_flag | (num_flags > 0) | (num_barb > 0))
        return (
         num_flags, num_barb, half_flag, empty_flag)

    def _make_barbs(self, u, v, nflags, nbarbs, half_barb, empty_flag, length, pivot, sizes, fill_empty, flip):
        """
        This function actually creates the wind barbs.  *u* and *v*
        are components of the vector in the *x* and *y* directions,
        respectively.

        *nflags*, *nbarbs*, and *half_barb*, empty_flag* are,
        *respectively, the number of flags, number of barbs, flag for
        *half a barb, and flag for empty barb, ostensibly obtained
        *from :meth:`_find_tails`.

        *length* is the length of the barb staff in points.

        *pivot* specifies the point on the barb around which the
        entire barb should be rotated.  Right now, valid options are
        'head' and 'middle'.

        *sizes* is a dictionary of coefficients specifying the ratio
        of a given feature to the length of the barb. These features
        include:

            - *spacing*: space between features (flags, full/half
               barbs)

            - *height*: distance from shaft of top of a flag or full
               barb

            - *width* - width of a flag, twice the width of a full barb

            - *emptybarb* - radius of the circle used for low
               magnitudes

        *fill_empty* specifies whether the circle representing an
        empty barb should be filled or not (this changes the drawing
        of the polygon).

        *flip* is a flag indicating whether the features should be flipped to
        the other side of the barb (useful for winds in the southern
        hemisphere.

        This function returns list of arrays of vertices, defining a polygon for
        each of the wind barbs.  These polygons have been rotated to properly
        align with the vector direction.
        """
        spacing = length * sizes.get('spacing', 0.125)
        full_height = length * sizes.get('height', 0.4)
        full_width = length * sizes.get('width', 0.25)
        empty_rad = length * sizes.get('emptybarb', 0.15)
        pivot_points = dict(tip=0.0, middle=-length / 2.0)
        if flip:
            full_height = -full_height
        endx = 0.0
        endy = pivot_points[pivot.lower()]
        angles = -(ma.arctan2(v, u) + np.pi / 2)
        circ = CirclePolygon((0, 0), radius=empty_rad).get_verts()
        if fill_empty:
            empty_barb = circ
        else:
            empty_barb = np.concatenate((circ, circ[::-1]))
        barb_list = []
        for index, angle in np.ndenumerate(angles):
            if empty_flag[index]:
                barb_list.append(empty_barb)
                continue
            poly_verts = [(endx, endy)]
            offset = length
            for i in range(nflags[index]):
                if offset != length:
                    offset += spacing / 2.0
                poly_verts.extend([[endx, endy + offset],
                 [
                  endx + full_height, endy - full_width / 2 + offset],
                 [
                  endx, endy - full_width + offset]])
                offset -= full_width + spacing

            for i in range(nbarbs[index]):
                poly_verts.extend([(endx, endy + offset),
                 (
                  endx + full_height, endy + offset + full_width / 2),
                 (
                  endx, endy + offset)])
                offset -= spacing

            if half_barb[index]:
                if offset == length:
                    poly_verts.append((endx, endy + offset))
                    offset -= 1.5 * spacing
                poly_verts.extend([(endx, endy + offset),
                 (
                  endx + full_height / 2, endy + offset + full_width / 4),
                 (
                  endx, endy + offset)])
            poly_verts = transforms.Affine2D().rotate(-angle).transform(poly_verts)
            barb_list.append(poly_verts)

        return barb_list

    def set_UVC(self, U, V, C=None):
        self.u = ma.masked_invalid(U, copy=False).ravel()
        self.v = ma.masked_invalid(V, copy=False).ravel()
        if C is not None:
            c = ma.masked_invalid(C, copy=False).ravel()
            x, y, u, v, c = delete_masked_points(self.x.ravel(), self.y.ravel(), self.u, self.v, c)
        else:
            x, y, u, v = delete_masked_points(self.x.ravel(), self.y.ravel(), self.u, self.v)
        magnitude = np.sqrt(u * u + v * v)
        flags, barbs, halves, empty = self._find_tails(magnitude, self.rounding, **self.barb_increments)
        plot_barbs = self._make_barbs(u, v, flags, barbs, halves, empty, self._length, self._pivot, self.sizes, self.fill_empty, self.flip)
        self.set_verts(plot_barbs)
        if C is not None:
            self.set_array(c)
        xy = np.hstack((x[:, np.newaxis], y[:, np.newaxis]))
        self._offsets = xy
        return

    def set_offsets(self, xy):
        """
        Set the offsets for the barb polygons.  This saves the offets passed in
        and actually sets version masked as appropriate for the existing U/V
        data. *offsets* should be a sequence.

        ACCEPTS: sequence of pairs of floats
        """
        self.x = xy[:, 0]
        self.y = xy[:, 1]
        x, y, u, v = delete_masked_points(self.x.ravel(), self.y.ravel(), self.u, self.v)
        xy = np.hstack((x[:, np.newaxis], y[:, np.newaxis]))
        collections.PolyCollection.set_offsets(self, xy)

    set_offsets.__doc__ = collections.PolyCollection.set_offsets.__doc__
    barbs_doc = _barbs_doc