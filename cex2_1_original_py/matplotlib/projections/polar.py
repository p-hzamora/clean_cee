# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\projections\polar.pyc
# Compiled at: 2012-10-30 18:11:14
from __future__ import print_function
import math, warnings, numpy as np, matplotlib
rcParams = matplotlib.rcParams
from matplotlib.axes import Axes
import matplotlib.axis as maxis
from matplotlib import cbook
from matplotlib import docstring
from matplotlib.patches import Circle
from matplotlib.path import Path
from matplotlib.ticker import Formatter, Locator, FormatStrFormatter
from matplotlib.transforms import Affine2D, Affine2DBase, Bbox, BboxTransformTo, IdentityTransform, Transform, TransformWrapper, ScaledTranslation, blended_transform_factory, BboxTransformToMaxOnly
import matplotlib.spines as mspines

class PolarTransform(Transform):
    """
    The base polar transform.  This handles projection *theta* and
    *r* into Cartesian coordinate space *x* and *y*, but does not
    perform the ultimate affine transformation into the correct
    position.
    """
    input_dims = 2
    output_dims = 2
    is_separable = False

    def __init__(self, axis=None, use_rmin=True):
        Transform.__init__(self)
        self._axis = axis
        self._use_rmin = use_rmin

    def transform_non_affine(self, tr):
        xy = np.empty(tr.shape, np.float_)
        if self._axis is not None:
            if self._use_rmin:
                rmin = self._axis.viewLim.ymin
            else:
                rmin = 0
            theta_offset = self._axis.get_theta_offset()
            theta_direction = self._axis.get_theta_direction()
        else:
            rmin = 0
            theta_offset = 0
            theta_direction = 1
        t = tr[:, 0:1]
        r = tr[:, 1:2]
        x = xy[:, 0:1]
        y = xy[:, 1:2]
        t *= theta_direction
        t += theta_offset
        if rmin != 0:
            r = r - rmin
            mask = r < 0
            x[:] = np.where(mask, np.nan, r * np.cos(t))
            y[:] = np.where(mask, np.nan, r * np.sin(t))
        else:
            x[:] = r * np.cos(t)
            y[:] = r * np.sin(t)
        return xy

    transform_non_affine.__doc__ = Transform.transform_non_affine.__doc__

    def transform_path_non_affine(self, path):
        vertices = path.vertices
        if len(vertices) == 2 and vertices[(0, 0)] == vertices[(1, 0)]:
            return Path(self.transform(vertices), path.codes)
        ipath = path.interpolated(path._interpolation_steps)
        return Path(self.transform(ipath.vertices), ipath.codes)

    transform_path_non_affine.__doc__ = Transform.transform_path_non_affine.__doc__

    def inverted(self):
        return PolarAxes.InvertedPolarTransform(self._axis, self._use_rmin)

    inverted.__doc__ = Transform.inverted.__doc__


class PolarAffine(Affine2DBase):
    """
    The affine part of the polar projection.  Scales the output so
    that maximum radius rests on the edge of the axes circle.
    """

    def __init__(self, scale_transform, limits):
        """
        *limits* is the view limit of the data.  The only part of
        its bounds that is used is ymax (for the radius maximum).
        The theta range is always fixed to (0, 2pi).
        """
        Affine2DBase.__init__(self)
        self._scale_transform = scale_transform
        self._limits = limits
        self.set_children(scale_transform, limits)
        self._mtx = None
        return

    def get_matrix(self):
        if self._invalid:
            limits_scaled = self._limits.transformed(self._scale_transform)
            yscale = limits_scaled.ymax - limits_scaled.ymin
            affine = Affine2D().scale(0.5 / yscale).translate(0.5, 0.5)
            self._mtx = affine.get_matrix()
            self._inverted = None
            self._invalid = 0
        return self._mtx

    get_matrix.__doc__ = Affine2DBase.get_matrix.__doc__

    def __getstate__(self):
        return {}


class InvertedPolarTransform(Transform):
    """
    The inverse of the polar transform, mapping Cartesian
    coordinate space *x* and *y* back to *theta* and *r*.
    """
    input_dims = 2
    output_dims = 2
    is_separable = False

    def __init__(self, axis=None, use_rmin=True):
        Transform.__init__(self)
        self._axis = axis
        self._use_rmin = use_rmin

    def transform_non_affine(self, xy):
        if self._axis is not None:
            if self._use_rmin:
                rmin = self._axis.viewLim.ymin
            else:
                rmin = 0
            theta_offset = self._axis.get_theta_offset()
            theta_direction = self._axis.get_theta_direction()
        else:
            rmin = 0
            theta_offset = 0
            theta_direction = 1
        x = xy[:, 0:1]
        y = xy[:, 1:]
        r = np.sqrt(x * x + y * y)
        theta = np.arccos(x / r)
        theta = np.where(y < 0, 2 * np.pi - theta, theta)
        theta -= theta_offset
        theta *= theta_direction
        r += rmin
        return np.concatenate((theta, r), 1)

    transform_non_affine.__doc__ = Transform.transform_non_affine.__doc__

    def inverted(self):
        return PolarAxes.PolarTransform(self._axis, self._use_rmin)

    inverted.__doc__ = Transform.inverted.__doc__


class ThetaFormatter(Formatter):
    """
    Used to format the *theta* tick labels.  Converts the native
    unit of radians into degrees and adds a degree symbol.
    """

    def __call__(self, x, pos=None):
        if rcParams['text.usetex'] and not rcParams['text.latex.unicode']:
            return '$%0.0f^\\circ$' % (x / np.pi * 180.0)
        else:
            return '%0.0f°' % (x / np.pi * 180.0)


class RadialLocator(Locator):
    """
    Used to locate radius ticks.

    Ensures that all ticks are strictly positive.  For all other
    tasks, it delegates to the base
    :class:`~matplotlib.ticker.Locator` (which may be different
    depending on the scale of the *r*-axis.
    """

    def __init__(self, base):
        self.base = base

    def __call__(self):
        ticks = self.base()
        return [ x for x in ticks if x > 0 ]

    def autoscale(self):
        return self.base.autoscale()

    def pan(self, numsteps):
        return self.base.pan(numsteps)

    def zoom(self, direction):
        return self.base.zoom(direction)

    def refresh(self):
        return self.base.refresh()

    def view_limits(self, vmin, vmax):
        vmin, vmax = self.base.view_limits(vmin, vmax)
        return (0, vmax)


class PolarAxes(Axes):
    """
    A polar graph projection, where the input dimensions are *theta*, *r*.

    Theta starts pointing east and goes anti-clockwise.
    """
    name = 'polar'

    def __init__(self, *args, **kwargs):
        """
        Create a new Polar Axes for a polar plot.

        The following optional kwargs are supported:

          - *resolution*: The number of points of interpolation between
            each pair of data points.  Set to 1 to disable
            interpolation.
        """
        self.resolution = kwargs.pop('resolution', 1)
        self._default_theta_offset = kwargs.pop('theta_offset', 0)
        self._default_theta_direction = kwargs.pop('theta_direction', 1)
        if self.resolution not in (None, 1):
            warnings.warn('The resolution kwarg to Polar plots is now ignored.\nIf you need to interpolate data points, consider running\ncbook.simple_linear_interpolation on the data before passing to matplotlib.')
        Axes.__init__(self, *args, **kwargs)
        self.set_aspect('equal', adjustable='box', anchor='C')
        self.cla()
        return

    __init__.__doc__ = Axes.__init__.__doc__

    def cla(self):
        Axes.cla(self)
        self.title.set_y(1.05)
        self.xaxis.set_major_formatter(self.ThetaFormatter())
        self.xaxis.isDefault_majfmt = True
        angles = np.arange(0.0, 360.0, 45.0)
        self.set_thetagrids(angles)
        self.yaxis.set_major_locator(self.RadialLocator(self.yaxis.get_major_locator()))
        self.grid(rcParams['polaraxes.grid'])
        self.xaxis.set_ticks_position('none')
        self.yaxis.set_ticks_position('none')
        self.yaxis.set_tick_params(label1On=True)
        self.set_theta_offset(self._default_theta_offset)
        self.set_theta_direction(self._default_theta_direction)

    def _init_axis(self):
        """move this out of __init__ because non-separable axes don't use it"""
        self.xaxis = maxis.XAxis(self)
        self.yaxis = maxis.YAxis(self)
        self._update_transScale()

    def _set_lim_and_transforms(self):
        self.transAxes = BboxTransformTo(self.bbox)
        self.transScale = TransformWrapper(IdentityTransform())
        self.transProjection = self.PolarTransform(self)
        self.transPureProjection = self.PolarTransform(self, use_rmin=False)
        self.transProjectionAffine = self.PolarAffine(self.transScale, self.viewLim)
        self.transData = self.transScale + self.transProjection + (self.transProjectionAffine + self.transAxes)
        self._xaxis_transform = self.transPureProjection + self.PolarAffine(IdentityTransform(), Bbox.unit()) + self.transAxes
        self._theta_label1_position = Affine2D().translate(0.0, 1.1)
        self._xaxis_text1_transform = self._theta_label1_position + self._xaxis_transform
        self._theta_label2_position = Affine2D().translate(0.0, 1.0 / 1.1)
        self._xaxis_text2_transform = self._theta_label2_position + self._xaxis_transform
        self._yaxis_transform = Affine2D().scale(np.pi * 2.0, 1.0) + self.transData
        self._r_label_position = ScaledTranslation(22.5, 0.0, Affine2D())
        self._yaxis_text_transform = self._r_label_position + Affine2D().scale(1.0 / 360.0, 1.0) + self._yaxis_transform

    def get_xaxis_transform(self, which='grid'):
        assert which in ('tick1', 'tick2', 'grid')
        return self._xaxis_transform

    def get_xaxis_text1_transform(self, pad):
        return (
         self._xaxis_text1_transform, 'center', 'center')

    def get_xaxis_text2_transform(self, pad):
        return (
         self._xaxis_text2_transform, 'center', 'center')

    def get_yaxis_transform(self, which='grid'):
        assert which in ('tick1', 'tick2', 'grid')
        return self._yaxis_transform

    def get_yaxis_text1_transform(self, pad):
        angle = self._r_label_position.to_values()[4]
        if angle < 90.0:
            return (self._yaxis_text_transform, 'bottom', 'left')
        else:
            if angle < 180.0:
                return (self._yaxis_text_transform, 'bottom', 'right')
            if angle < 270.0:
                return (self._yaxis_text_transform, 'top', 'right')
            return (self._yaxis_text_transform, 'top', 'left')

    def get_yaxis_text2_transform(self, pad):
        angle = self._r_label_position.to_values()[4]
        if angle < 90.0:
            return (self._yaxis_text_transform, 'top', 'right')
        else:
            if angle < 180.0:
                return (self._yaxis_text_transform, 'top', 'left')
            if angle < 270.0:
                return (self._yaxis_text_transform, 'bottom', 'left')
            return (self._yaxis_text_transform, 'bottom', 'right')

    def _gen_axes_patch(self):
        return Circle((0.5, 0.5), 0.5)

    def _gen_axes_spines(self):
        return {'polar': mspines.Spine.circular_spine(self, (0.5, 0.5), 0.5)}

    def set_rmax(self, rmax):
        self.viewLim.y1 = rmax

    def get_rmax(self):
        return self.viewLim.ymax

    def set_rmin(self, rmin):
        self.viewLim.y0 = rmin

    def get_rmin(self):
        return self.viewLim.ymin

    def set_theta_offset(self, offset):
        """
        Set the offset for the location of 0 in radians.
        """
        self._theta_offset = offset

    def get_theta_offset(self):
        """
        Get the offset for the location of 0 in radians.
        """
        return self._theta_offset

    def set_theta_zero_location(self, loc):
        """
        Sets the location of theta's zero.  (Calls set_theta_offset
        with the correct value in radians under the hood.)

        May be one of "N", "NW", "W", "SW", "S", "SE", "E", or "NE".
        """
        mapping = {'N': np.pi * 0.5, 
           'NW': np.pi * 0.75, 
           'W': np.pi, 
           'SW': np.pi * 1.25, 
           'S': np.pi * 1.5, 
           'SE': np.pi * 1.75, 
           'E': 0, 
           'NE': np.pi * 0.25}
        return self.set_theta_offset(mapping[loc])

    def set_theta_direction(self, direction):
        """
        Set the direction in which theta increases.

        clockwise, -1:
           Theta increases in the clockwise direction

        counterclockwise, anticlockwise, 1:
           Theta increases in the counterclockwise direction
        """
        if direction in ('clockwise', ):
            self._direction = -1
        elif direction in ('counterclockwise', 'anticlockwise'):
            self._direction = 1
        elif direction in (1, -1):
            self._direction = direction
        else:
            raise ValueError('direction must be 1, -1, clockwise or counterclockwise')

    def get_theta_direction(self):
        """
        Get the direction in which theta increases.

        -1:
           Theta increases in the clockwise direction

        1:
           Theta increases in the counterclockwise direction
        """
        return self._direction

    def set_rlim(self, *args, **kwargs):
        if 'rmin' in kwargs:
            kwargs['ymin'] = kwargs.pop('rmin')
        if 'rmax' in kwargs:
            kwargs['ymax'] = kwargs.pop('rmax')
        return self.set_ylim(*args, **kwargs)

    def set_yscale(self, *args, **kwargs):
        Axes.set_yscale(self, *args, **kwargs)
        self.yaxis.set_major_locator(self.RadialLocator(self.yaxis.get_major_locator()))

    def set_rscale(self, *args, **kwargs):
        return Axes.set_yscale(self, *args, **kwargs)

    def set_rticks(self, *args, **kwargs):
        return Axes.set_yticks(self, *args, **kwargs)

    @docstring.dedent_interpd
    def set_thetagrids(self, angles, labels=None, frac=None, fmt=None, **kwargs):
        """
        Set the angles at which to place the theta grids (these
        gridlines are equal along the theta dimension).  *angles* is in
        degrees.

        *labels*, if not None, is a ``len(angles)`` list of strings of
        the labels to use at each angle.

        If *labels* is None, the labels will be ``fmt %% angle``

        *frac* is the fraction of the polar axes radius at which to
        place the label (1 is the edge). Eg. 1.05 is outside the axes
        and 0.95 is inside the axes.

        Return value is a list of tuples (*line*, *label*), where
        *line* is :class:`~matplotlib.lines.Line2D` instances and the
        *label* is :class:`~matplotlib.text.Text` instances.

        kwargs are optional text properties for the labels:

        %(Text)s

        ACCEPTS: sequence of floats
        """
        angles = self.convert_yunits(angles)
        angles = np.asarray(angles, np.float_)
        self.set_xticks(angles * (np.pi / 180.0))
        if labels is not None:
            self.set_xticklabels(labels)
        else:
            if fmt is not None:
                self.xaxis.set_major_formatter(FormatStrFormatter(fmt))
            if frac is not None:
                self._theta_label1_position.clear().translate(0.0, frac)
                self._theta_label2_position.clear().translate(0.0, 1.0 / frac)
            for t in self.xaxis.get_ticklabels():
                t.update(kwargs)

        return (
         self.xaxis.get_ticklines(), self.xaxis.get_ticklabels())

    @docstring.dedent_interpd
    def set_rgrids(self, radii, labels=None, angle=None, fmt=None, **kwargs):
        """
        Set the radial locations and labels of the *r* grids.

        The labels will appear at radial distances *radii* at the
        given *angle* in degrees.

        *labels*, if not None, is a ``len(radii)`` list of strings of the
        labels to use at each radius.

        If *labels* is None, the built-in formatter will be used.

        Return value is a list of tuples (*line*, *label*), where
        *line* is :class:`~matplotlib.lines.Line2D` instances and the
        *label* is :class:`~matplotlib.text.Text` instances.

        kwargs are optional text properties for the labels:

        %(Text)s

        ACCEPTS: sequence of floats
        """
        radii = self.convert_xunits(radii)
        radii = np.asarray(radii)
        rmin = radii.min()
        if rmin <= 0:
            raise ValueError('radial grids must be strictly positive')
        self.set_yticks(radii)
        if labels is not None:
            self.set_yticklabels(labels)
        else:
            if fmt is not None:
                self.yaxis.set_major_formatter(FormatStrFormatter(fmt))
            if angle is None:
                angle = self._r_label_position.to_values()[4]
            self._r_label_position._t = (
             angle, 0.0)
            self._r_label_position.invalidate()
            for t in self.yaxis.get_ticklabels():
                t.update(kwargs)

        return (
         self.yaxis.get_gridlines(), self.yaxis.get_ticklabels())

    def set_xscale(self, scale, *args, **kwargs):
        if scale != 'linear':
            raise NotImplementedError('You can not set the xscale on a polar plot.')

    def set_xlim(self, *args, **kargs):
        self.viewLim.intervalx = (
         0.0, np.pi * 2.0)

    def format_coord(self, theta, r):
        """
        Return a format string formatting the coordinate using Unicode
        characters.
        """
        theta /= math.pi
        return 'θ=%0.3fπ (%0.3f°), r=%0.3f' % (theta, theta * 180.0, r)

    def get_data_ratio(self):
        """
        Return the aspect ratio of the data itself.  For a polar plot,
        this should always be 1.0
        """
        return 1.0

    def can_zoom(self):
        """
        Return *True* if this axes supports the zoom box button functionality.

        Polar axes do not support zoom boxes.
        """
        return False

    def can_pan(self):
        """
        Return *True* if this axes supports the pan/zoom button functionality.

        For polar axes, this is slightly misleading. Both panning and
        zooming are performed by the same button. Panning is performed
        in azimuth while zooming is done along the radial.
        """
        return True

    def start_pan(self, x, y, button):
        angle = np.deg2rad(self._r_label_position.to_values()[4])
        mode = ''
        if button == 1:
            epsilon = np.pi / 45.0
            t, r = self.transData.inverted().transform_point((x, y))
            if t >= angle - epsilon and t <= angle + epsilon:
                mode = 'drag_r_labels'
        elif button == 3:
            mode = 'zoom'
        self._pan_start = cbook.Bunch(rmax=self.get_rmax(), trans=self.transData.frozen(), trans_inverse=self.transData.inverted().frozen(), r_label_angle=self._r_label_position.to_values()[4], x=x, y=y, mode=mode)

    def end_pan(self):
        del self._pan_start

    def drag_pan(self, button, key, x, y):
        p = self._pan_start
        if p.mode == 'drag_r_labels':
            startt, startr = p.trans_inverse.transform_point((p.x, p.y))
            t, r = p.trans_inverse.transform_point((x, y))
            dt0 = t - startt
            dt1 = startt - t
            if abs(dt1) < abs(dt0):
                dt = abs(dt1) * sign(dt0) * -1.0
            else:
                dt = dt0 * -1.0
            dt = dt / np.pi * 180.0
            self._r_label_position._t = (
             p.r_label_angle - dt, 0.0)
            self._r_label_position.invalidate()
            trans, vert1, horiz1 = self.get_yaxis_text1_transform(0.0)
            trans, vert2, horiz2 = self.get_yaxis_text2_transform(0.0)
            for t in self.yaxis.majorTicks + self.yaxis.minorTicks:
                t.label1.set_va(vert1)
                t.label1.set_ha(horiz1)
                t.label2.set_va(vert2)
                t.label2.set_ha(horiz2)

        elif p.mode == 'zoom':
            startt, startr = p.trans_inverse.transform_point((p.x, p.y))
            t, r = p.trans_inverse.transform_point((x, y))
            dr = r - startr
            scale = r / startr
            self.set_rmax(p.rmax / scale)


PolarAxes.PolarTransform = PolarTransform
PolarAxes.PolarAffine = PolarAffine
PolarAxes.InvertedPolarTransform = InvertedPolarTransform
PolarAxes.ThetaFormatter = ThetaFormatter
PolarAxes.RadialLocator = RadialLocator