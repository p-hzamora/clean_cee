# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\contour.pyc
# Compiled at: 2012-10-30 18:11:14
"""
These are  classes to support contour plotting and
labelling for the axes class
"""
from __future__ import division, print_function
import warnings, matplotlib as mpl, numpy as np
from numpy import ma
import matplotlib._cntr as _cntr, matplotlib.path as mpath, matplotlib.ticker as ticker, matplotlib.cm as cm, matplotlib.colors as colors, matplotlib.collections as mcoll, matplotlib.font_manager as font_manager, matplotlib.text as text, matplotlib.cbook as cbook, matplotlib.mlab as mlab, matplotlib.mathtext as mathtext, matplotlib.patches as mpatches, matplotlib.texmanager as texmanager, matplotlib.transforms as mtrans
from matplotlib.blocking_input import BlockingContourLabeler

class ClabelText(text.Text):
    """
    Unlike the ordinary text, the get_rotation returns an updated
    angle in the pixel coordinate assuming that the input rotation is
    an angle in data coordinate (or whatever transform set).
    """

    def get_rotation(self):
        angle = text.Text.get_rotation(self)
        trans = self.get_transform()
        x, y = self.get_position()
        new_angles = trans.transform_angles(np.array([angle]), np.array([[x, y]]))
        return new_angles[0]


class ContourLabeler():
    """Mixin to provide labelling capability to ContourSet"""

    def clabel(self, *args, **kwargs):
        """
        Label a contour plot.

        Call signature::

          clabel(cs, **kwargs)

        Adds labels to line contours in *cs*, where *cs* is a
        :class:`~matplotlib.contour.ContourSet` object returned by
        contour.

        ::

          clabel(cs, v, **kwargs)

        only labels contours listed in *v*.

        Optional keyword arguments:

          *fontsize*:
            size in points or relative size eg 'smaller', 'x-large'

          *colors*:
            - if *None*, the color of each label matches the color of
              the corresponding contour

            - if one string color, e.g. *colors* = 'r' or *colors* =
              'red', all labels will be plotted in this color

            - if a tuple of matplotlib color args (string, float, rgb, etc),
              different labels will be plotted in different colors in the order
              specified

          *inline*:
            controls whether the underlying contour is removed or
            not. Default is *True*.

          *inline_spacing*:
            space in pixels to leave on each side of label when
            placing inline.  Defaults to 5.  This spacing will be
            exact for labels at locations where the contour is
            straight, less so for labels on curved contours.

          *fmt*:
            a format string for the label. Default is '%1.3f'
            Alternatively, this can be a dictionary matching contour
            levels with arbitrary strings to use for each contour level
            (i.e., fmt[level]=string), or it can be any callable, such
            as a :class:`~matplotlib.ticker.Formatter` instance, that
            returns a string when called with a numeric contour level.

          *manual*:
            if *True*, contour labels will be placed manually using
            mouse clicks.  Click the first button near a contour to
            add a label, click the second button (or potentially both
            mouse buttons at once) to finish adding labels.  The third
            button can be used to remove the last label added, but
            only if labels are not inline.  Alternatively, the keyboard
            can be used to select label locations (enter to end label
            placement, delete or backspace act like the third mouse button,
            and any other key will select a label location).

            *manual* can be an iterable object of x,y tuples. Contour labels
            will be created as if mouse is clicked at each x,y positions.

          *rightside_up*:
            if *True* (default), label rotations will always be plus
            or minus 90 degrees from level.

          *use_clabeltext*:
            if *True* (default is False), ClabelText class (instead of
            matplotlib.Text) is used to create labels. ClabelText
            recalculates rotation angles of texts during the drawing time,
            therefore this can be used if aspect of the axes changes.

        .. plot:: mpl_examples/pylab_examples/contour_demo.py
        """
        fontsize = kwargs.get('fontsize', None)
        inline = kwargs.get('inline', 1)
        inline_spacing = kwargs.get('inline_spacing', 5)
        self.labelFmt = kwargs.get('fmt', '%1.3f')
        _colors = kwargs.get('colors', None)
        self._use_clabeltext = kwargs.get('use_clabeltext', False)
        self.labelManual = kwargs.get('manual', False)
        self.rightside_up = kwargs.get('rightside_up', True)
        if len(args) == 0:
            levels = self.levels
            indices = range(len(self.cvalues))
        elif len(args) == 1:
            levlabs = list(args[0])
            indices, levels = [], []
            for i, lev in enumerate(self.levels):
                if lev in levlabs:
                    indices.append(i)
                    levels.append(lev)

            if len(levels) < len(levlabs):
                msg = 'Specified levels ' + str(levlabs)
                msg += "\n don't match available levels "
                msg += str(self.levels)
                raise ValueError(msg)
        else:
            raise TypeError('Illegal arguments to clabel, see help(clabel)')
        self.labelLevelList = levels
        self.labelIndiceList = indices
        self.labelFontProps = font_manager.FontProperties()
        if fontsize == None:
            font_size = int(self.labelFontProps.get_size_in_points())
        elif type(fontsize) not in [int, float, str]:
            raise TypeError('Font size must be an integer number.')
        elif type(fontsize) == str:
            font_size = int(self.labelFontProps.get_size_in_points())
        else:
            self.labelFontProps.set_size(fontsize)
            font_size = fontsize
        self.labelFontSizeList = [
         font_size] * len(levels)
        if _colors == None:
            self.labelMappable = self
            self.labelCValueList = np.take(self.cvalues, self.labelIndiceList)
        else:
            cmap = colors.ListedColormap(_colors, N=len(self.labelLevelList))
            self.labelCValueList = range(len(self.labelLevelList))
            self.labelMappable = cm.ScalarMappable(cmap=cmap, norm=colors.NoNorm())
        self.labelXYs = []
        if cbook.iterable(self.labelManual):
            for x, y in self.labelManual:
                self.add_label_near(x, y, inline, inline_spacing)

        elif self.labelManual:
            print('Select label locations manually using first mouse button.')
            print('End manual selection with second mouse button.')
            if not inline:
                print('Remove last label by clicking third mouse button.')
            blocking_contour_labeler = BlockingContourLabeler(self)
            blocking_contour_labeler(inline, inline_spacing)
        else:
            self.labels(inline, inline_spacing)
        self.cl = self.labelTexts
        self.cl_xy = self.labelXYs
        self.cl_cvalues = self.labelCValues
        self.labelTextsList = cbook.silent_list('text.Text', self.labelTexts)
        return self.labelTextsList

    def print_label(self, linecontour, labelwidth):
        """Return *False* if contours are too short for a label."""
        lcsize = len(linecontour)
        if lcsize > 10 * labelwidth:
            return True
        else:
            xmax = np.amax(linecontour[:, 0])
            xmin = np.amin(linecontour[:, 0])
            ymax = np.amax(linecontour[:, 1])
            ymin = np.amin(linecontour[:, 1])
            lw = labelwidth
            if xmax - xmin > 1.2 * lw or ymax - ymin > 1.2 * lw:
                return True
            return False

    def too_close(self, x, y, lw):
        """Return *True* if a label is already near this location."""
        for loc in self.labelXYs:
            d = np.sqrt((x - loc[0]) ** 2 + (y - loc[1]) ** 2)
            if d < 1.2 * lw:
                return True

        return False

    def get_label_coords(self, distances, XX, YY, ysize, lw):
        """
        Return x, y, and the index of a label location.

        Labels are plotted at a location with the smallest
        deviation of the contour from a straight line
        unless there is another label nearby, in which case
        the next best place on the contour is picked up.
        If all such candidates are rejected, the beginning
        of the contour is chosen.
        """
        hysize = int(ysize / 2)
        adist = np.argsort(distances)
        for ind in adist:
            x, y = XX[ind][hysize], YY[ind][hysize]
            if self.too_close(x, y, lw):
                continue
            return (
             x, y, ind)

        ind = adist[0]
        x, y = XX[ind][hysize], YY[ind][hysize]
        return (x, y, ind)

    def get_label_width(self, lev, fmt, fsize):
        """
        Return the width of the label in points.
        """
        if not cbook.is_string_like(lev):
            lev = self.get_text(lev, fmt)
        lev, ismath = text.Text.is_math_text(lev)
        if ismath == 'TeX':
            if not hasattr(self, '_TeX_manager'):
                self._TeX_manager = texmanager.TexManager()
            lw, _, _ = self._TeX_manager.get_text_width_height_descent(lev, fsize)
        elif ismath:
            if not hasattr(self, '_mathtext_parser'):
                self._mathtext_parser = mathtext.MathTextParser('bitmap')
            img, _ = self._mathtext_parser.parse(lev, dpi=72, prop=self.labelFontProps)
            lw = img.get_width()
        else:
            lw = len(lev) * fsize * 0.6
        return lw

    def get_real_label_width(self, lev, fmt, fsize):
        """
        This computes actual onscreen label width.
        This uses some black magic to determine onscreen extent of non-drawn
        label.  This magic may not be very robust.

        This method is not being used, and may be modified or removed.
        """
        xx = np.mean(np.asarray(self.ax.axis()).reshape(2, 2), axis=1)
        t = text.Text(xx[0], xx[1])
        self.set_label_props(t, self.get_text(lev, fmt), 'k')
        bbox = t.get_window_extent(renderer=self.ax.figure.canvas.renderer)
        lw = np.diff(bbox.corners()[0::2, 0])[0]
        return lw

    def set_label_props(self, label, text, color):
        """set the label properties - color, fontsize, text"""
        label.set_text(text)
        label.set_color(color)
        label.set_fontproperties(self.labelFontProps)
        label.set_clip_box(self.ax.bbox)

    def get_text(self, lev, fmt):
        """get the text of the label"""
        if cbook.is_string_like(lev):
            return lev
        else:
            if isinstance(fmt, dict):
                return fmt[lev]
            if callable(fmt):
                return fmt(lev)
            return fmt % lev

    def locate_label(self, linecontour, labelwidth):
        """
        Find a good place to plot a label (relatively flat
        part of the contour).
        """
        nsize = len(linecontour)
        if labelwidth > 1:
            xsize = int(np.ceil(nsize / labelwidth))
        else:
            xsize = 1
        if xsize == 1:
            ysize = nsize
        else:
            ysize = int(labelwidth)
        XX = np.resize(linecontour[:, 0], (xsize, ysize))
        YY = np.resize(linecontour[:, 1], (xsize, ysize))
        yfirst = YY[:, 0].reshape(xsize, 1)
        ylast = YY[:, -1].reshape(xsize, 1)
        xfirst = XX[:, 0].reshape(xsize, 1)
        xlast = XX[:, -1].reshape(xsize, 1)
        s = (yfirst - YY) * (xlast - xfirst) - (xfirst - XX) * (ylast - yfirst)
        L = np.sqrt((xlast - xfirst) ** 2 + (ylast - yfirst) ** 2).ravel()
        dist = np.add.reduce([ abs(s)[i] / L[i] for i in range(xsize) ], -1)
        x, y, ind = self.get_label_coords(dist, XX, YY, ysize, labelwidth)
        lc = [ tuple(l) for l in linecontour ]
        dind = lc.index((x, y))
        return (
         x, y, dind)

    def calc_label_rot_and_inline(self, slc, ind, lw, lc=None, spacing=5):
        """
        This function calculates the appropriate label rotation given
        the linecontour coordinates in screen units, the index of the
        label location and the label width.

        It will also break contour and calculate inlining if *lc* is
        not empty (lc defaults to the empty list if None).  *spacing*
        is the space around the label in pixels to leave empty.

        Do both of these tasks at once to avoid calling mlab.path_length
        multiple times, which is relatively costly.

        The method used here involves calculating the path length
        along the contour in pixel coordinates and then looking
        approximately label width / 2 away from central point to
        determine rotation and then to break contour if desired.
        """
        if lc is None:
            lc = []
        hlw = lw / 2.0
        closed = mlab.is_closed_polygon(slc)
        if closed:
            slc = np.r_[(slc[ind:-1], slc[:ind + 1])]
            if len(lc):
                lc = np.r_[(lc[ind:-1], lc[:ind + 1])]
            ind = 0
        pl = mlab.path_length(slc)
        pl = pl - pl[ind]
        xi = np.array([-hlw, hlw])
        if closed:
            dp = np.array([pl[-1], 0])
        else:
            dp = np.zeros_like(xi)
        ll = mlab.less_simple_linear_interpolation(pl, slc, dp + xi, extrap=True)
        dd = np.diff(ll, axis=0).ravel()
        if np.all(dd == 0):
            rotation = 0.0
        else:
            rotation = np.arctan2(dd[1], dd[0]) * 180.0 / np.pi
        if self.rightside_up:
            if rotation > 90:
                rotation = rotation - 180.0
            if rotation < -90:
                rotation = 180.0 + rotation
        nlc = []
        if len(lc):
            xi = dp + xi + np.array([-spacing, spacing])
            I = mlab.less_simple_linear_interpolation(pl, np.arange(len(pl)), xi, extrap=False)
            if not np.isnan(I[0]) and int(I[0]) != I[0]:
                xy1 = mlab.less_simple_linear_interpolation(pl, lc, [xi[0]])
            if not np.isnan(I[1]) and int(I[1]) != I[1]:
                xy2 = mlab.less_simple_linear_interpolation(pl, lc, [xi[1]])
            I = [
             np.floor(I[0]), np.ceil(I[1])]
            if closed:
                if np.all(~np.isnan(I)):
                    nlc.append(np.r_[(xy2, lc[I[1]:I[0] + 1], xy1)])
            else:
                if not np.isnan(I[0]):
                    nlc.append(np.r_[(lc[:I[0] + 1], xy1)])
                if not np.isnan(I[1]):
                    nlc.append(np.r_[(xy2, lc[I[1]:])])
        return (
         rotation, nlc)

    def _get_label_text(self, x, y, rotation):
        dx, dy = self.ax.transData.inverted().transform_point((x, y))
        t = text.Text(dx, dy, rotation=rotation, horizontalalignment='center', verticalalignment='center')
        return t

    def _get_label_clabeltext(self, x, y, rotation):
        transDataInv = self.ax.transData.inverted()
        dx, dy = transDataInv.transform_point((x, y))
        drotation = transDataInv.transform_angles(np.array([rotation]), np.array([[x, y]]))
        t = ClabelText(dx, dy, rotation=drotation[0], horizontalalignment='center', verticalalignment='center')
        return t

    def _add_label(self, t, x, y, lev, cvalue):
        color = self.labelMappable.to_rgba(cvalue, alpha=self.alpha)
        _text = self.get_text(lev, self.labelFmt)
        self.set_label_props(t, _text, color)
        self.labelTexts.append(t)
        self.labelCValues.append(cvalue)
        self.labelXYs.append((x, y))
        self.ax.add_artist(t)

    def add_label(self, x, y, rotation, lev, cvalue):
        """
        Add contour label using :class:`~matplotlib.text.Text` class.
        """
        t = self._get_label_text(x, y, rotation)
        self._add_label(t, x, y, lev, cvalue)

    def add_label_clabeltext(self, x, y, rotation, lev, cvalue):
        """
        Add contour label using :class:`ClabelText` class.
        """
        t = self._get_label_clabeltext(x, y, rotation)
        self._add_label(t, x, y, lev, cvalue)

    def add_label_near(self, x, y, inline=True, inline_spacing=5, transform=None):
        """
        Add a label near the point (x, y) of the given transform.
        If transform is None, data transform is used. If transform is
        False, IdentityTransform is used.

        *inline*:
          controls whether the underlying contour is removed or
          not. Default is *True*.

        *inline_spacing*:
          space in pixels to leave on each side of label when
          placing inline.  Defaults to 5.  This spacing will be
          exact for labels at locations where the contour is
          straight, less so for labels on curved contours.
        """
        if transform is None:
            transform = self.ax.transData
        if transform:
            x, y = transform.transform_point((x, y))
        conmin, segmin, imin, xmin, ymin = self.find_nearest_contour(x, y, self.labelIndiceList)[:5]
        lmin = self.labelIndiceList.index(conmin)
        paths = self.collections[conmin].get_paths()
        lc = paths[segmin].vertices
        slc = self.ax.transData.transform(lc)
        lw = self.get_label_width(self.labelLevelList[lmin], self.labelFmt, self.labelFontSizeList[lmin])
        if inline:
            lcarg = lc
        else:
            lcarg = None
        rotation, nlc = self.calc_label_rot_and_inline(slc, imin, lw, lcarg, inline_spacing)
        self.add_label(xmin, ymin, rotation, self.labelLevelList[lmin], self.labelCValueList[lmin])
        if inline:
            paths.pop(segmin)
            for n in nlc:
                if len(n) > 1:
                    paths.append(mpath.Path(n))

        return

    def pop_label(self, index=-1):
        """Defaults to removing last label, but any index can be supplied"""
        self.labelCValues.pop(index)
        t = self.labelTexts.pop(index)
        t.remove()

    def labels(self, inline, inline_spacing):
        if self._use_clabeltext:
            add_label = self.add_label_clabeltext
        else:
            add_label = self.add_label
        for icon, lev, fsize, cvalue in zip(self.labelIndiceList, self.labelLevelList, self.labelFontSizeList, self.labelCValueList):
            con = self.collections[icon]
            trans = con.get_transform()
            lw = self.get_label_width(lev, self.labelFmt, fsize)
            lw *= self.ax.figure.dpi / 72.0
            additions = []
            paths = con.get_paths()
            for segNum, linepath in enumerate(paths):
                lc = linepath.vertices
                slc0 = trans.transform(lc)
                if mlab.is_closed_polygon(lc):
                    slc = np.r_[(slc0, slc0[1:2, :])]
                else:
                    slc = slc0
                if self.print_label(slc, lw):
                    x, y, ind = self.locate_label(slc, lw)
                    if inline:
                        lcarg = lc
                    else:
                        lcarg = None
                    rotation, new = self.calc_label_rot_and_inline(slc0, ind, lw, lcarg, inline_spacing)
                    add_label(x, y, rotation, lev, cvalue)
                    if inline:
                        for n in new:
                            if len(n) > 1:
                                additions.append(mpath.Path(n))

                else:
                    additions.append(linepath)

            if inline:
                del paths[:]
                paths.extend(additions)

        return


class ContourSet(cm.ScalarMappable, ContourLabeler):
    """
    Store a set of contour lines or filled regions.

    User-callable method: clabel

    Useful attributes:
      ax:
        The axes object in which the contours are drawn

      collections:
        a silent_list of LineCollections or PolyCollections

      levels:
        contour levels

      layers:
        same as levels for line contours; half-way between
        levels for filled contours.  See :meth:`_process_colors`.
    """

    def __init__(self, ax, *args, **kwargs):
        """
        Draw contour lines or filled regions, depending on
        whether keyword arg 'filled' is *False* (default) or *True*.

        The first three arguments must be:

          *ax*: axes object.

          *levels*: [level0, level1, ..., leveln]
            A list of floating point numbers indicating the contour
            levels.

          *allsegs*: [level0segs, level1segs, ...]
            List of all the polygon segments for all the *levels*.
            For contour lines ``len(allsegs) == len(levels)``, and for
            filled contour regions ``len(allsegs) = len(levels)-1``.

            level0segs = [polygon0, polygon1, ...]

            polygon0 = array_like [[x0,y0], [x1,y1], ...]

          *allkinds*: *None* or [level0kinds, level1kinds, ...]
            Optional list of all the polygon vertex kinds (code types), as
            described and used in Path.   This is used to allow multiply-
            connected paths such as holes within filled polygons.
            If not *None*, len(allkinds) == len(allsegs).

            level0kinds = [polygon0kinds, ...]

            polygon0kinds = [vertexcode0, vertexcode1, ...]

            If *allkinds* is not *None*, usually all polygons for a particular
            contour level are grouped together so that

            level0segs = [polygon0] and level0kinds = [polygon0kinds].

        Keyword arguments are as described in
        :class:`~matplotlib.contour.QuadContourSet` object.

        **Examples:**

        .. plot:: mpl_examples/misc/contour_manual.py
        """
        self.ax = ax
        self.levels = kwargs.get('levels', None)
        self.filled = kwargs.get('filled', False)
        self.linewidths = kwargs.get('linewidths', None)
        self.linestyles = kwargs.get('linestyles', None)
        self.hatches = kwargs.get('hatches', [None])
        self.alpha = kwargs.get('alpha', None)
        self.origin = kwargs.get('origin', None)
        self.extent = kwargs.get('extent', None)
        cmap = kwargs.get('cmap', None)
        self.colors = kwargs.get('colors', None)
        norm = kwargs.get('norm', None)
        vmin = kwargs.get('vmin', None)
        vmax = kwargs.get('vmax', None)
        self.extend = kwargs.get('extend', 'neither')
        self.antialiased = kwargs.get('antialiased', None)
        if self.antialiased is None and self.filled:
            self.antialiased = False
        self.nchunk = kwargs.get('nchunk', 0)
        self.locator = kwargs.get('locator', None)
        if isinstance(norm, colors.LogNorm) or isinstance(self.locator, ticker.LogLocator):
            self.logscale = True
            if norm is None:
                norm = colors.LogNorm()
            if self.extend is not 'neither':
                raise ValueError('extend kwarg does not work yet with log scale')
        else:
            self.logscale = False
        if self.origin is not None:
            assert self.origin in ('lower', 'upper', 'image')
            assert self.extent is not None and len(self.extent) == 4
        if self.colors is not None and cmap is not None:
            raise ValueError('Either colors or cmap must be None')
        if self.origin == 'image':
            self.origin = mpl.rcParams['image.origin']
        self._transform = kwargs.get('transform', None)
        self._process_args(*args, **kwargs)
        self._process_levels()
        if self.colors is not None:
            ncolors = len(self.levels)
            if self.filled:
                ncolors -= 1
            cmap = colors.ListedColormap(self.colors, N=ncolors)
        if self.filled:
            self.collections = cbook.silent_list('mcoll.PathCollection')
        else:
            self.collections = cbook.silent_list('mcoll.LineCollection')
        self.labelTexts = []
        self.labelCValues = []
        kw = {'cmap': cmap}
        if norm is not None:
            kw['norm'] = norm
        cm.ScalarMappable.__init__(self, **kw)
        if vmin is not None:
            self.norm.vmin = vmin
        if vmax is not None:
            self.norm.vmax = vmax
        self._process_colors()
        self.allsegs, self.allkinds = self._get_allsegs_and_allkinds()
        if self.filled:
            if self.linewidths is not None:
                warnings.warn('linewidths is ignored by contourf')
            lowers, uppers = self._get_lowers_and_uppers()
            if self.allkinds is None:
                self.allkinds = [
                 None] * len(self.allsegs)
            for level, level_upper, segs, kinds in zip(lowers, uppers, self.allsegs, self.allkinds):
                paths = self._make_paths(segs, kinds)
                zorder = kwargs.get('zorder', 1)
                col = mcoll.PathCollection(paths, antialiaseds=(
                 self.antialiased,), edgecolors='none', alpha=self.alpha, transform=self.get_transform(), zorder=zorder)
                self.ax.add_collection(col)
                self.collections.append(col)

        else:
            tlinewidths = self._process_linewidths()
            self.tlinewidths = tlinewidths
            tlinestyles = self._process_linestyles()
            aa = self.antialiased
            if aa is not None:
                aa = (
                 self.antialiased,)
            for level, width, lstyle, segs in zip(self.levels, tlinewidths, tlinestyles, self.allsegs):
                zorder = kwargs.get('zorder', 2)
                col = mcoll.LineCollection(segs, antialiaseds=aa, linewidths=width, linestyle=lstyle, alpha=self.alpha, transform=self.get_transform(), zorder=zorder)
                col.set_label('_nolegend_')
                self.ax.add_collection(col, False)
                self.collections.append(col)

        self.changed()
        return

    def get_transform(self):
        """
        Return the :class:`~matplotlib.transforms.Transform`
        instance used by this ContourSet.
        """
        if self._transform is None:
            self._transform = self.ax.transData
        elif not isinstance(self._transform, mtrans.Transform) and hasattr(self._transform, '_as_mpl_transform'):
            self._transform = self._transform._as_mpl_transform(self.ax)
        return self._transform

    def __getstate__(self):
        state = self.__dict__.copy()
        state['Cntr'] = None
        return state

    def legend_elements(self, variable_name='x', str_format=str):
        """
        Return a list of artist and labels suitable for passing through
        to :func:`plt.legend` which represent this ContourSet.

        Args:

            *variable_name*: the string used inside the inequality used
              on the labels

            *str_format*: function used to format the numbers in the labels
        """
        artists = []
        labels = []
        if self.filled:
            lowers, uppers = self._get_lowers_and_uppers()
            n_levels = len(self.collections)
            for i, (collection, lower, upper) in enumerate(zip(self.collections, lowers, uppers)):
                patch = mpatches.Rectangle((0, 0), 1, 1, facecolor=collection.get_facecolor()[0], hatch=collection.get_hatch(), alpha=collection.get_alpha())
                artists.append(patch)
                lower = str_format(lower)
                upper = str_format(upper)
                if i == 0 and self.extend in ('min', 'both'):
                    labels.append('$%s \\leq %s$' % (variable_name, lower))
                elif i == n_levels - 1 and self.extend in ('max', 'both'):
                    labels.append('$%s > %s$' % (variable_name, upper))
                else:
                    labels.append('$%s < %s \\leq %s$' % (lower, variable_name, upper))

        else:
            for collection, level in zip(self.collections, self.levels):
                patch = mcoll.LineCollection(None)
                patch.update_from(collection)
                artists.append(patch)
                level = str_format(level)
                labels.append('$%s = %s$' % (variable_name, level))

        return (
         artists, labels)

    def _process_args(self, *args, **kwargs):
        """
        Process *args* and *kwargs*; override in derived classes.

        Must set self.levels, self.zmin and self.zmax, and update axes
        limits.
        """
        self.levels = args[0]
        self.allsegs = args[1]
        self.allkinds = len(args) > 2 and args[2] or None
        self.zmax = np.amax(self.levels)
        self.zmin = np.amin(self.levels)
        self._auto = False
        if self.filled:
            if len(self.allsegs) != len(self.levels) - 1:
                raise ValueError('must be one less number of segments as levels')
        else:
            if len(self.allsegs) != len(self.levels):
                raise ValueError('must be same number of segments as levels')
            if self.allkinds is not None and len(self.allkinds) != len(self.allsegs):
                raise ValueError('allkinds has different length to allsegs')
            havelimits = False
            for segs in self.allsegs:
                for seg in segs:
                    seg = np.asarray(seg)
                    if havelimits:
                        min = np.minimum(min, seg.min(axis=0))
                        max = np.maximum(max, seg.max(axis=0))
                    else:
                        min = seg.min(axis=0)
                        max = seg.max(axis=0)
                        havelimits = True

        if havelimits:
            self.ax.update_datalim([min, max])
            self.ax.autoscale_view(tight=True)
        return

    def _get_allsegs_and_allkinds(self):
        """
        Override in derived classes to create and return allsegs and allkinds.
        allkinds can be None.
        """
        return (
         self.allsegs, self.allkinds)

    def _get_lowers_and_uppers(self):
        """
        Return (lowers,uppers) for filled contours.
        """
        lowers = self._levels[:-1]
        if self.zmin == lowers[0]:
            lowers = lowers.copy()
            if self.logscale:
                lowers[0] = 0.99 * self.zmin
            else:
                lowers[0] -= 1
        uppers = self._levels[1:]
        return (lowers, uppers)

    def _make_paths(self, segs, kinds):
        if kinds is not None:
            return [ mpath.Path(seg, codes=kind) for seg, kind in zip(segs, kinds) ]
        else:
            return [ mpath.Path(seg) for seg in segs ]
            return

    def changed(self):
        tcolors = [ (tuple(rgba),) for rgba in self.to_rgba(self.cvalues, alpha=self.alpha)
                  ]
        self.tcolors = tcolors
        hatches = self.hatches * len(tcolors)
        for color, hatch, collection in zip(tcolors, hatches, self.collections):
            if self.filled:
                collection.set_facecolor(color)
                collection.set_hatch(hatch)
            else:
                collection.set_color(color)

        for label, cv in zip(self.labelTexts, self.labelCValues):
            label.set_alpha(self.alpha)
            label.set_color(self.labelMappable.to_rgba(cv))

        cm.ScalarMappable.changed(self)

    def _autolev(self, z, N):
        """
        Select contour levels to span the data.

        We need two more levels for filled contours than for
        line contours, because for the latter we need to specify
        the lower and upper boundary of each range. For example,
        a single contour boundary, say at z = 0, requires only
        one contour line, but two filled regions, and therefore
        three levels to provide boundaries for both regions.
        """
        if self.locator is None:
            if self.logscale:
                self.locator = ticker.LogLocator()
            else:
                self.locator = ticker.MaxNLocator(N + 1)
        zmax = self.zmax
        zmin = self.zmin
        lev = self.locator.tick_values(zmin, zmax)
        self._auto = True
        if self.filled:
            return lev
        else:
            return lev[(lev > zmin) & (lev < zmax)]

    def _contour_level_args(self, z, args):
        """
        Determine the contour levels and store in self.levels.
        """
        if self.filled:
            fn = 'contourf'
        else:
            fn = 'contour'
        self._auto = False
        if self.levels is None:
            if len(args) == 0:
                lev = self._autolev(z, 7)
            else:
                level_arg = args[0]
                try:
                    if type(level_arg) == int:
                        lev = self._autolev(z, level_arg)
                    else:
                        lev = np.asarray(level_arg).astype(np.float64)
                except:
                    raise TypeError('Last %s arg must give levels; see help(%s)' % (fn, fn))

            self.levels = lev
        if self.filled and len(self.levels) < 2:
            raise ValueError('Filled contours require at least 2 levels.')
        return

    def _process_levels(self):
        """
        Assign values to :attr:`layers` based on :attr:`levels`,
        adding extended layers as needed if contours are filled.

        For line contours, layers simply coincide with levels;
        a line is a thin layer.  No extended levels are needed
        with line contours.
        """
        self.vmin = np.amin(self.levels)
        self.vmax = np.amax(self.levels)
        self._levels = list(self.levels)
        if not self.filled:
            self.layers = self.levels
            return
        if self.extend in ('both', 'min'):
            self._levels.insert(0, min(self.levels[0], self.zmin) - 1)
        if self.extend in ('both', 'max'):
            self._levels.append(max(self.levels[-1], self.zmax) + 1)
        self._levels = np.asarray(self._levels)
        self.layers = 0.5 * (self._levels[:-1] + self._levels[1:])
        if self.extend in ('both', 'min'):
            self.layers[0] = -np.inf
        if self.extend in ('both', 'max'):
            self.layers[-1] = np.inf

    def _process_colors(self):
        """
        Color argument processing for contouring.

        Note that we base the color mapping on the contour levels
        and layers, not on the actual range of the Z values.  This
        means we don't have to worry about bad values in Z, and we
        always have the full dynamic range available for the selected
        levels.

        The color is based on the midpoint of the layer, except for
        extended end layers.  By default, the norm vmin and vmax
        are the extreme values of the non-extended levels.  Hence,
        the layer color extremes are not the extreme values of
        the colormap itself, but approach those values as the number
        of levels increases.  An advantage of this scheme is that
        line contours, when added to filled contours, take on
        colors that are consistent with those of the filled regions;
        for example, a contour line on the boundary between two
        regions will have a color intermediate between those
        of the regions.

        """
        self.monochrome = self.cmap.monochrome
        if self.colors is not None:
            i0, i1 = 0, len(self.levels)
            if self.filled:
                i1 -= 1
            if self.extend in ('both', 'min'):
                i0 = -1
            if self.extend in ('both', 'max'):
                i1 += 1
            self.cvalues = list(range(i0, i1))
            self.set_norm(colors.NoNorm())
        else:
            self.cvalues = self.layers
        self.set_array(self.levels)
        self.autoscale_None()
        if self.extend in ('both', 'max', 'min'):
            self.norm.clip = False
        return

    def _process_linewidths(self):
        linewidths = self.linewidths
        Nlev = len(self.levels)
        if linewidths is None:
            tlinewidths = [
             (
              mpl.rcParams['lines.linewidth'],)] * Nlev
        else:
            if not cbook.iterable(linewidths):
                linewidths = [
                 linewidths] * Nlev
            else:
                linewidths = list(linewidths)
                if len(linewidths) < Nlev:
                    nreps = int(np.ceil(Nlev / len(linewidths)))
                    linewidths = linewidths * nreps
                if len(linewidths) > Nlev:
                    linewidths = linewidths[:Nlev]
            tlinewidths = [ (w,) for w in linewidths ]
        return tlinewidths

    def _process_linestyles(self):
        linestyles = self.linestyles
        Nlev = len(self.levels)
        if linestyles is None:
            tlinestyles = [
             'solid'] * Nlev
            if self.monochrome:
                neg_ls = mpl.rcParams['contour.negative_linestyle']
                eps = -(self.zmax - self.zmin) * 1e-15
                for i, lev in enumerate(self.levels):
                    if lev < eps:
                        tlinestyles[i] = neg_ls

        elif cbook.is_string_like(linestyles):
            tlinestyles = [
             linestyles] * Nlev
        elif cbook.iterable(linestyles):
            tlinestyles = list(linestyles)
            if len(tlinestyles) < Nlev:
                nreps = int(np.ceil(Nlev / len(linestyles)))
                tlinestyles = tlinestyles * nreps
            if len(tlinestyles) > Nlev:
                tlinestyles = tlinestyles[:Nlev]
        else:
            raise ValueError('Unrecognized type for linestyles kwarg')
        return tlinestyles

    def get_alpha(self):
        """returns alpha to be applied to all ContourSet artists"""
        return self.alpha

    def set_alpha(self, alpha):
        """sets alpha for all ContourSet artists"""
        self.alpha = alpha
        self.changed()

    def find_nearest_contour(self, x, y, indices=None, pixel=True):
        """
        Finds contour that is closest to a point.  Defaults to
        measuring distance in pixels (screen space - useful for manual
        contour labeling), but this can be controlled via a keyword
        argument.

        Returns a tuple containing the contour, segment, index of
        segment, x & y of segment point and distance to minimum point.

        Call signature::

          conmin,segmin,imin,xmin,ymin,dmin = find_nearest_contour(
                     self, x, y, indices=None, pixel=True )

        Optional keyword arguments:

          *indices*:
            Indexes of contour levels to consider when looking for
            nearest point.  Defaults to using all levels.

          *pixel*:
            If *True*, measure distance in pixel space, if not, measure
            distance in axes space.  Defaults to *True*.

        """
        if indices == None:
            indices = range(len(self.levels))
        dmin = 10000000000.0
        conmin = None
        segmin = None
        xmin = None
        ymin = None
        for icon in indices:
            con = self.collections[icon]
            trans = con.get_transform()
            paths = con.get_paths()
            for segNum, linepath in enumerate(paths):
                lc = linepath.vertices
                if pixel:
                    lc = trans.transform(lc)
                ds = (lc[:, 0] - x) ** 2 + (lc[:, 1] - y) ** 2
                d = min(ds)
                if d < dmin:
                    dmin = d
                    conmin = icon
                    segmin = segNum
                    imin = mpl.mlab.find(ds == d)[0]
                    xmin = lc[(imin, 0)]
                    ymin = lc[(imin, 1)]

        return (
         conmin, segmin, imin, xmin, ymin, dmin)


class QuadContourSet(ContourSet):
    """
    Create and store a set of contour lines or filled regions.

    User-callable method: :meth:`clabel`

    Useful attributes:
      ax:
        The axes object in which the contours are drawn

      collections:
        A silent_list of LineCollections or PolyCollections

      levels:
        Contour levels

      layers:
        Same as levels for line contours; half-way between
        levels for filled contours.  See :meth:`_process_colors` method.
    """

    def __init__(self, ax, *args, **kwargs):
        """
        Calculate and draw contour lines or filled regions, depending
        on whether keyword arg 'filled' is False (default) or True.

        The first argument of the initializer must be an axes
        object.  The remaining arguments and keyword arguments
        are described in QuadContourSet.contour_doc.
        """
        ContourSet.__init__(self, ax, *args, **kwargs)

    def _process_args(self, *args, **kwargs):
        """
        Process args and kwargs.
        """
        if isinstance(args[0], QuadContourSet):
            C = args[0].Cntr
            if self.levels is None:
                self.levels = args[0].levels
            self.zmin = args[0].zmin
            self.zmax = args[0].zmax
        else:
            x, y, z = self._contour_args(args, kwargs)
            _mask = ma.getmask(z)
            if _mask is ma.nomask:
                _mask = None
            C = _cntr.Cntr(x, y, z.filled(), _mask)
            t = self.get_transform()
            if t != self.ax.transData and any(t.contains_branch_seperately(self.ax.transData)):
                trans_to_data = t - self.ax.transData
                pts = np.vstack([x.flat, y.flat]).T
                transformed_pts = trans_to_data.transform(pts)
                x = transformed_pts[(Ellipsis, 0)]
                y = transformed_pts[(Ellipsis, 1)]
            x0 = ma.minimum(x)
            x1 = ma.maximum(x)
            y0 = ma.minimum(y)
            y1 = ma.maximum(y)
            self.ax.update_datalim([(x0, y0), (x1, y1)])
            self.ax.autoscale_view(tight=True)
        self.Cntr = C
        return

    def _get_allsegs_and_allkinds(self):
        """
        Create and return allsegs and allkinds by calling underlying C code.
        """
        allsegs = []
        if self.filled:
            lowers, uppers = self._get_lowers_and_uppers()
            allkinds = []
            for level, level_upper in zip(lowers, uppers):
                nlist = self.Cntr.trace(level, level_upper, nchunk=self.nchunk)
                nseg = len(nlist) // 2
                segs = nlist[:nseg]
                kinds = nlist[nseg:]
                allsegs.append(segs)
                allkinds.append(kinds)

        else:
            allkinds = None
            for level in self.levels:
                nlist = self.Cntr.trace(level)
                nseg = len(nlist) // 2
                segs = nlist[:nseg]
                allsegs.append(segs)

        return (
         allsegs, allkinds)

    def _contour_args(self, args, kwargs):
        if self.filled:
            fn = 'contourf'
        else:
            fn = 'contour'
        Nargs = len(args)
        if Nargs <= 2:
            z = ma.asarray(args[0], dtype=np.float64)
            x, y = self._initialize_x_y(z)
            args = args[1:]
        elif Nargs <= 4:
            x, y, z = self._check_xyz(args[:3], kwargs)
            args = args[3:]
        else:
            raise TypeError('Too many arguments to %s; see help(%s)' % (fn, fn))
        z = ma.masked_invalid(z, copy=False)
        self.zmax = ma.maximum(z)
        self.zmin = ma.minimum(z)
        if self.logscale and self.zmin <= 0:
            z = ma.masked_where(z <= 0, z)
            warnings.warn('Log scale: values of z <= 0 have been masked')
            self.zmin = z.min()
        self._contour_level_args(z, args)
        return (x, y, z)

    def _check_xyz(self, args, kwargs):
        """
        For functions like contour, check that the dimensions
        of the input arrays match; if x and y are 1D, convert
        them to 2D using meshgrid.

        Possible change: I think we should make and use an ArgumentError
        Exception class (here and elsewhere).
        """
        x, y = args[:2]
        self.ax._process_unit_info(xdata=x, ydata=y, kwargs=kwargs)
        x = self.ax.convert_xunits(x)
        y = self.ax.convert_yunits(y)
        x = np.asarray(x, dtype=np.float64)
        y = np.asarray(y, dtype=np.float64)
        z = ma.asarray(args[2], dtype=np.float64)
        if z.ndim != 2:
            raise TypeError('Input z must be a 2D array.')
        else:
            Ny, Nx = z.shape
        if x.shape == z.shape and y.shape == z.shape:
            return (x, y, z)
        if x.ndim != 1 or y.ndim != 1:
            raise TypeError('Inputs x and y must be 1D or 2D.')
        nx, = x.shape
        ny, = y.shape
        if nx != Nx or ny != Ny:
            raise TypeError('Length of x must be number of columns in z,\n' + 'and length of y must be number of rows.')
        x, y = np.meshgrid(x, y)
        return (x, y, z)

    def _initialize_x_y(self, z):
        """
        Return X, Y arrays such that contour(Z) will match imshow(Z)
        if origin is not None.
        The center of pixel Z[i,j] depends on origin:
        if origin is None, x = j, y = i;
        if origin is 'lower', x = j + 0.5, y = i + 0.5;
        if origin is 'upper', x = j + 0.5, y = Nrows - i - 0.5
        If extent is not None, x and y will be scaled to match,
        as in imshow.
        If origin is None and extent is not None, then extent
        will give the minimum and maximum values of x and y.
        """
        if z.ndim != 2:
            raise TypeError('Input must be a 2D array.')
        else:
            Ny, Nx = z.shape
        if self.origin is None:
            if self.extent is None:
                return np.meshgrid(np.arange(Nx), np.arange(Ny))
            else:
                x0, x1, y0, y1 = self.extent
                x = np.linspace(x0, x1, Nx)
                y = np.linspace(y0, y1, Ny)
                return np.meshgrid(x, y)

        if self.extent is None:
            x0, x1, y0, y1 = (
             0, Nx, 0, Ny)
        else:
            x0, x1, y0, y1 = self.extent
        dx = float(x1 - x0) / Nx
        dy = float(y1 - y0) / Ny
        x = x0 + (np.arange(Nx) + 0.5) * dx
        y = y0 + (np.arange(Ny) + 0.5) * dy
        if self.origin == 'upper':
            y = y[::-1]
        return np.meshgrid(x, y)

    contour_doc = "\n        Plot contours.\n\n        :func:`~matplotlib.pyplot.contour` and\n        :func:`~matplotlib.pyplot.contourf` draw contour lines and\n        filled contours, respectively.  Except as noted, function\n        signatures and return values are the same for both versions.\n\n        :func:`~matplotlib.pyplot.contourf` differs from the MATLAB\n        version in that it does not draw the polygon edges.\n        To draw edges, add line contours with\n        calls to :func:`~matplotlib.pyplot.contour`.\n\n\n        Call signatures::\n\n          contour(Z)\n\n        make a contour plot of an array *Z*. The level values are chosen\n        automatically.\n\n        ::\n\n          contour(X,Y,Z)\n\n        *X*, *Y* specify the (x, y) coordinates of the surface\n\n        ::\n\n          contour(Z,N)\n          contour(X,Y,Z,N)\n\n        contour *N* automatically-chosen levels.\n\n        ::\n\n          contour(Z,V)\n          contour(X,Y,Z,V)\n\n        draw contour lines at the values specified in sequence *V*\n\n        ::\n\n          contourf(..., V)\n\n        fill the ``len(V)-1`` regions between the values in *V*\n\n        ::\n\n          contour(Z, **kwargs)\n\n        Use keyword args to control colors, linewidth, origin, cmap ... see\n        below for more details.\n\n        *X* and *Y* must both be 2-D with the same shape as *Z*, or they\n        must both be 1-D such that ``len(X)`` is the number of columns in\n        *Z* and ``len(Y)`` is the number of rows in *Z*.\n\n        ``C = contour(...)`` returns a\n        :class:`~matplotlib.contour.QuadContourSet` object.\n\n        Optional keyword arguments:\n\n          *colors*: [ *None* | string | (mpl_colors) ]\n            If *None*, the colormap specified by cmap will be used.\n\n            If a string, like 'r' or 'red', all levels will be plotted in this\n            color.\n\n            If a tuple of matplotlib color args (string, float, rgb, etc),\n            different levels will be plotted in different colors in the order\n            specified.\n\n          *alpha*: float\n            The alpha blending value\n\n          *cmap*: [ *None* | Colormap ]\n            A cm :class:`~matplotlib.colors.Colormap` instance or\n            *None*. If *cmap* is *None* and *colors* is *None*, a\n            default Colormap is used.\n\n          *norm*: [ *None* | Normalize ]\n            A :class:`matplotlib.colors.Normalize` instance for\n            scaling data values to colors. If *norm* is *None* and\n            *colors* is *None*, the default linear scaling is used.\n\n          *vmin*, *vmax*: [ *None* | scalar ]\n            If not *None*, either or both of these values will be\n            supplied to the :class:`matplotlib.colors.Normalize`\n            instance, overriding the default color scaling based on\n            *levels*.\n\n          *levels*: [level0, level1, ..., leveln]\n            A list of floating point numbers indicating the level\n            curves to draw; eg to draw just the zero contour pass\n            ``levels=[0]``\n\n          *origin*: [ *None* | 'upper' | 'lower' | 'image' ]\n            If *None*, the first value of *Z* will correspond to the\n            lower left corner, location (0,0). If 'image', the rc\n            value for ``image.origin`` will be used.\n\n            This keyword is not active if *X* and *Y* are specified in\n            the call to contour.\n\n          *extent*: [ *None* | (x0,x1,y0,y1) ]\n\n            If *origin* is not *None*, then *extent* is interpreted as\n            in :func:`matplotlib.pyplot.imshow`: it gives the outer\n            pixel boundaries. In this case, the position of Z[0,0]\n            is the center of the pixel, not a corner. If *origin* is\n            *None*, then (*x0*, *y0*) is the position of Z[0,0], and\n            (*x1*, *y1*) is the position of Z[-1,-1].\n\n            This keyword is not active if *X* and *Y* are specified in\n            the call to contour.\n\n          *locator*: [ *None* | ticker.Locator subclass ]\n            If *locator* is *None*, the default\n            :class:`~matplotlib.ticker.MaxNLocator` is used. The\n            locator is used to determine the contour levels if they\n            are not given explicitly via the *V* argument.\n\n          *extend*: [ 'neither' | 'both' | 'min' | 'max' ]\n            Unless this is 'neither', contour levels are automatically\n            added to one or both ends of the range so that all data\n            are included. These added ranges are then mapped to the\n            special colormap values which default to the ends of the\n            colormap range, but can be set via\n            :meth:`matplotlib.colors.Colormap.set_under` and\n            :meth:`matplotlib.colors.Colormap.set_over` methods.\n\n          *xunits*, *yunits*: [ *None* | registered units ]\n            Override axis units by specifying an instance of a\n            :class:`matplotlib.units.ConversionInterface`.\n\n          *antialiased*: [ *True* | *False* ]\n            enable antialiasing, overriding the defaults.  For\n            filled contours, the default is *True*.  For line contours,\n            it is taken from rcParams['lines.antialiased'].\n\n        contour-only keyword arguments:\n\n          *linewidths*: [ *None* | number | tuple of numbers ]\n            If *linewidths* is *None*, the default width in\n            ``lines.linewidth`` in ``matplotlibrc`` is used.\n\n            If a number, all levels will be plotted with this linewidth.\n\n            If a tuple, different levels will be plotted with different\n            linewidths in the order specified\n\n          *linestyles*: [ *None* | 'solid' | 'dashed' | 'dashdot' | 'dotted' ]\n            If *linestyles* is *None*, the default is 'solid' unless\n            the lines are monochrome.  In that case, negative\n            contours will take their linestyle from the ``matplotlibrc``\n            ``contour.negative_linestyle`` setting.\n\n            *linestyles* can also be an iterable of the above strings\n            specifying a set of linestyles to be used. If this\n            iterable is shorter than the number of contour levels\n            it will be repeated as necessary.\n\n        contourf-only keyword arguments:\n\n          *nchunk*: [ 0 | integer ]\n            If 0, no subdivision of the domain. Specify a positive integer to\n            divide the domain into subdomains of roughly *nchunk* by *nchunk*\n            points. This may never actually be advantageous, so this option may\n            be removed. Chunking introduces artifacts at the chunk boundaries\n            unless *antialiased* is *False*.\n\n          *hatches*:\n            A list of cross hatch patterns to use on the filled areas.\n            If None, no hatching will be added to the contour.\n            Hatching is supported in the PostScript, PDF, SVG and Agg\n            backends only.\n\n\n        Note: contourf fills intervals that are closed at the top; that\n        is, for boundaries *z1* and *z2*, the filled region is::\n\n            z1 < z <= z2\n\n        There is one exception: if the lowest boundary coincides with\n        the minimum value of the *z* array, then that minimum value\n        will be included in the lowest interval.\n\n        **Examples:**\n\n        .. plot:: mpl_examples/pylab_examples/contour_demo.py\n\n        .. plot:: mpl_examples/pylab_examples/contourf_demo.py\n        "