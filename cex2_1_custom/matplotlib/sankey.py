# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\sankey.pyc
# Compiled at: 2012-11-08 06:38:04
"""
Module for creating Sankey diagrams using matplotlib
"""
__author__ = 'Kevin L. Davies'
__credits__ = ['Yannick Copin']
__license__ = 'BSD'
__version__ = '2011/09/16'
import numpy as np
from matplotlib.cbook import iterable, Bunch
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.transforms import Affine2D
from matplotlib import verbose
from matplotlib import docstring
RIGHT = 0
UP = 1
DOWN = 3

class Sankey:
    """
    Sankey diagram in matplotlib

      Sankey diagrams are a specific type of flow diagram, in which
      the width of the arrows is shown proportionally to the flow
      quantity.  They are typically used to visualize energy or
      material or cost transfers between processes.
      `Wikipedia (6/1/2011) <http://en.wikipedia.org/wiki/Sankey_diagram>`_

    """

    def _arc(self, quadrant=0, cw=True, radius=1, center=(0, 0)):
        """
        Return the codes and vertices for a rotated, scaled, and translated
        90 degree arc.

        Optional keyword arguments:

          ===============   ==========================================
          Keyword           Description
          ===============   ==========================================
          *quadrant*        uses 0-based indexing (0, 1, 2, or 3)
          *cw*              if True, clockwise
          *center*          (x, y) tuple of the arc's center
          ===============   ==========================================
        """
        ARC_CODES = [
         Path.LINETO,
         Path.CURVE4,
         Path.CURVE4,
         Path.CURVE4,
         Path.CURVE4,
         Path.CURVE4,
         Path.CURVE4]
        ARC_VERTICES = np.array([[1.0, 0.0],
         [
          1.0, 0.265114773],
         [
          0.894571235, 0.519642327],
         [
          0.707106781, 0.707106781],
         [
          0.519642327, 0.894571235],
         [
          0.265114773, 1.0],
         [
          0.0, 1.0]])
        if quadrant == 0 or quadrant == 2:
            if cw:
                vertices = ARC_VERTICES
            else:
                vertices = ARC_VERTICES[:, ::-1]
        elif quadrant == 1 or quadrant == 3:
            if cw:
                vertices = np.column_stack((-ARC_VERTICES[:, 1],
                 ARC_VERTICES[:, 0]))
            else:
                vertices = np.column_stack((-ARC_VERTICES[:, 0],
                 ARC_VERTICES[:, 1]))
        if quadrant > 1:
            radius = -radius
        return zip(ARC_CODES, radius * vertices + np.tile(center, (ARC_VERTICES.shape[0], 1)))

    def _add_input(self, path, angle, flow, length):
        """
        Add an input to a path and return its tip and label locations.
        """
        if angle is None:
            return ([0, 0], [0, 0])
        else:
            x, y = path[-1][1]
            dipdepth = flow / 2 * self.pitch
            if angle == RIGHT:
                x -= length
                dip = [x + dipdepth, y + flow / 2.0]
                path.extend([(Path.LINETO, [x, y]),
                 (
                  Path.LINETO, dip),
                 (
                  Path.LINETO, [x, y + flow]),
                 (
                  Path.LINETO, [x + self.gap, y + flow])])
                label_location = [dip[0] - self.offset, dip[1]]
            else:
                x -= self.gap
                if angle == UP:
                    sign = 1
                else:
                    sign = -1
                dip = [x - flow / 2, y - sign * (length - dipdepth)]
                if angle == DOWN:
                    quadrant = 2
                else:
                    quadrant = 1
                if self.radius:
                    path.extend(self._arc(quadrant=quadrant, cw=angle == UP, radius=self.radius, center=(
                     x + self.radius,
                     y - sign * self.radius)))
                else:
                    path.append((Path.LINETO, [x, y]))
                path.extend([(Path.LINETO, [x, y - sign * length]),
                 (
                  Path.LINETO, dip),
                 (
                  Path.LINETO, [x - flow, y - sign * length])])
                path.extend(self._arc(quadrant=quadrant, cw=angle == DOWN, radius=flow + self.radius, center=(
                 x + self.radius,
                 y - sign * self.radius)))
                path.append((Path.LINETO, [x - flow, y + sign * flow]))
                label_location = [dip[0], dip[1] - sign * self.offset]
            return (dip, label_location)
            return

    def _add_output(self, path, angle, flow, length):
        """
        Append an output to a path and return its tip and label locations.

        Note: *flow* is negative for an output.
        """
        if angle is None:
            return ([0, 0], [0, 0])
        else:
            x, y = path[-1][1]
            tipheight = (self.shoulder - flow / 2) * self.pitch
            if angle == RIGHT:
                x += length
                tip = [x + tipheight, y + flow / 2.0]
                path.extend([(Path.LINETO, [x, y]),
                 (
                  Path.LINETO, [x, y + self.shoulder]),
                 (
                  Path.LINETO, tip),
                 (
                  Path.LINETO, [x, y - self.shoulder + flow]),
                 (
                  Path.LINETO, [x, y + flow]),
                 (
                  Path.LINETO, [x - self.gap, y + flow])])
                label_location = [tip[0] + self.offset, tip[1]]
            else:
                x += self.gap
                if angle == UP:
                    sign = 1
                else:
                    sign = -1
                tip = [x - flow / 2.0, y + sign * (length + tipheight)]
                if angle == UP:
                    quadrant = 3
                else:
                    quadrant = 0
                if self.radius:
                    path.extend(self._arc(quadrant=quadrant, cw=angle == UP, radius=self.radius, center=(
                     x - self.radius,
                     y + sign * self.radius)))
                else:
                    path.append((Path.LINETO, [x, y]))
                path.extend([(Path.LINETO, [x, y + sign * length]),
                 (
                  Path.LINETO,
                  [x - self.shoulder,
                   y + sign * length]),
                 (
                  Path.LINETO, tip),
                 (
                  Path.LINETO,
                  [x + self.shoulder - flow,
                   y + sign * length]),
                 (
                  Path.LINETO, [x - flow, y + sign * length])])
                path.extend(self._arc(quadrant=quadrant, cw=angle == DOWN, radius=self.radius - flow, center=(
                 x - self.radius,
                 y + sign * self.radius)))
                path.append((Path.LINETO, [x - flow, y + sign * flow]))
                label_location = [tip[0], tip[1] + sign * self.offset]
            return (
             tip, label_location)
            return

    def _revert(self, path, first_action=Path.LINETO):
        """
        A path is not simply revertable by path[::-1] since the code
        specifies an action to take from the **previous** point.
        """
        reverse_path = []
        next_code = first_action
        for code, position in path[::-1]:
            reverse_path.append((next_code, position))
            next_code = code

        return reverse_path

    @docstring.dedent_interpd
    def add(self, patchlabel='', flows=None, orientations=None, labels='', trunklength=1.0, pathlengths=0.25, prior=None, connect=(0, 0), rotation=0, **kwargs):
        """
        Add a simple Sankey diagram with flows at the same hierarchical level.

        Return value is the instance of :class:`Sankey`.

        Optional keyword arguments:

          ===============   ===================================================
          Keyword           Description
          ===============   ===================================================
          *patchlabel*      label to be placed at the center of the diagram
                            Note: *label* (not *patchlabel*) will be passed to
                            the patch through ``**kwargs`` and can be used to
                            create an entry in the legend.
          *flows*           array of flow values
                            By convention, inputs are positive and outputs are
                            negative.
          *orientations*    list of orientations of the paths
                            Valid values are 1 (from/to the top), 0 (from/to
                            the left or right), or -1 (from/to the bottom).  If
                            *orientations* == 0, inputs will break in from the
                            left and outputs will break away to the right.
          *labels*          list of specifications of the labels for the flows
                            Each value may be None (no labels), '' (just label
                            the quantities), or a labeling string.  If a single
                            value is provided, it will be applied to all flows.
                            If an entry is a non-empty string, then the
                            quantity for the corresponding flow will be shown
                            below the string.  However, if the *unit* of the
                            main diagram is None, then quantities are never
                            shown, regardless of the value of this argument.
          *trunklength*     length between the bases of the input and output
                            groups
          *pathlengths*     list of lengths of the arrows before break-in or
                            after break-away
                            If a single value is given, then it will be applied
                            to the first (inside) paths on the top and bottom,
                            and the length of all other arrows will be
                            justified accordingly.  The *pathlengths* are not
                            applied to the horizontal inputs and outputs.
          *prior*           index of the prior diagram to which this diagram
                            should be connected
          *connect*         a (prior, this) tuple indexing the flow of the
                            prior diagram and the flow of this diagram which
                            should be connected
                            If this is the first diagram or *prior* is None,
                            *connect* will be ignored.
          *rotation*        angle of rotation of the diagram [deg]
                            *rotation* is ignored if this diagram is connected
                            to an existing one (using *prior* and *connect*).
                            The interpretation of the *orientations* argument
                            will be rotated accordingly (e.g., if *rotation*
                            == 90, an *orientations* entry of 1 means to/from
                            the left).
          ===============   ===================================================

        Valid kwargs are :meth:`matplotlib.patches.PathPatch` arguments:

        %(Patch)s

        As examples, ``fill=False`` and ``label='A legend entry'``.
        By default, ``facecolor='#bfd1d4'`` (light blue) and
        ``linewidth=0.5``.

        The indexing parameters (*prior* and *connect*) are zero-based.

        The flows are placed along the top of the diagram from the inside out
        in order of their index within the *flows* list or array.  They are
        placed along the sides of the diagram from the top down and along the
        bottom from the outside in.

        If the the sum of the inputs and outputs is nonzero, the discrepancy
        will appear as a cubic Bezier curve along the top and bottom edges of
        the trunk.

        .. seealso::

            :meth:`finish`
        """
        if flows is None:
            flows = np.array([1.0, -1.0])
        else:
            flows = np.array(flows)
        n = flows.shape[0]
        if rotation == None:
            rotation = 0
        else:
            rotation /= 90.0
        if orientations is None:
            orientations = [
             0, 0]
        assert len(orientations) == n, 'orientations and flows must have the same length.\norientations has length %d, but flows has length %d.' % (
         len(orientations), n)
        if labels != '' and getattr(labels, '__iter__', False):
            assert len(labels) == n, 'If labels is a list, then labels and flows must have the same length.\nlabels has length %d, but flows has length %d.' % (
             len(labels), n)
        else:
            labels = [
             labels] * n
        if not trunklength >= 0:
            raise AssertionError("trunklength is negative.\nThis isn't allowed, because it would cause poor layout.")
            if np.absolute(np.sum(flows)) > self.tolerance:
                verbose.report('The sum of the flows is nonzero (%f).\nIs the system not at steady state?' % np.sum(flows), 'helpful')
            scaled_flows = self.scale * flows
            gain = sum(max(flow, 0) for flow in scaled_flows)
            loss = sum(min(flow, 0) for flow in scaled_flows)
            if not 0.5 <= gain <= 2.0:
                verbose.report('The scaled sum of the inputs is %f.\nThis may cause poor layout.\nConsider changing the scale so that the scaled sum is approximately 1.0.' % gain, 'helpful')
            -2.0 <= loss <= -0.5 or verbose.report('The scaled sum of the outputs is %f.\nThis may cause poor layout.\nConsider changing the scale so that the scaled sum is approximately 1.0.' % gain, 'helpful')
        if prior is not None:
            assert prior >= 0, 'The index of the prior diagram is negative.'
            assert min(connect) >= 0, 'At least one of the connection indices is negative.'
            assert prior < len(self.diagrams), 'The index of the prior diagram is %d, but there are only %d other diagrams.\nThe index is zero-based.' % (
             prior, len(self.diagrams))
            assert connect[0] < len(self.diagrams[prior].flows), 'The connection index to the source diagram is %d, but that diagram has only %d flows.\nThe index is zero-based.' % (
             connect[0], len(self.diagrams[prior].flows))
            assert connect[1] < n, 'The connection index to this diagram is %d, but this diagramhas only %d flows.\n The index is zero-based.' % (
             connect[1], n)
            assert self.diagrams[prior].angles[connect[0]] is not None, 'The connection cannot be made.  Check that the magnitude of flow %d of diagram %d is greater than or equal to the specified tolerance.' % (
             connect[0], prior)
            flow_error = self.diagrams[prior].flows[connect[0]] + flows[connect[1]]
            assert abs(flow_error) < self.tolerance, 'The scaled sum of the connected flows is %f, which is not within the tolerance (%f).' % (
             flow_error, self.tolerance)
        are_inputs = [
         None] * n
        for i, flow in enumerate(flows):
            if flow >= self.tolerance:
                are_inputs[i] = True
            elif flow <= -self.tolerance:
                are_inputs[i] = False
            else:
                verbose.report('The magnitude of flow %d (%f) is below the tolerance (%f).\nIt will not be shown, and it cannot be used in a connection.' % (
                 i, flow, self.tolerance), 'helpful')

        angles = [None] * n
        for i, (orient, is_input) in enumerate(zip(orientations, are_inputs)):
            if orient == 1:
                if is_input:
                    angles[i] = DOWN
                elif is_input == False:
                    angles[i] = UP
            elif orient == 0:
                if is_input is not None:
                    angles[i] = RIGHT
            else:
                assert orient == -1, 'The value of orientations[%d] is %d, but it must be -1, 0, or 1.' % (
                 i, orient)
                if is_input:
                    angles[i] = UP
                elif is_input == False:
                    angles[i] = DOWN

        if iterable(pathlengths):
            assert len(pathlengths) == n, 'If pathlengths is a list, then pathlengths and flows must have the same length.\npathlengths has length %d, but flows has length %d.' % (
             len(pathlengths), n)
        else:
            urlength = pathlengths
            ullength = pathlengths
            lrlength = pathlengths
            lllength = pathlengths
            d = dict(RIGHT=pathlengths)
            pathlengths = [ d.get(angle, 0) for angle in angles ]
            for i, (angle, is_input, flow) in enumerate(zip(angles, are_inputs, scaled_flows)):
                if angle == DOWN and is_input:
                    pathlengths[i] = ullength
                    ullength += flow
                elif angle == UP and not is_input:
                    pathlengths[i] = urlength
                    urlength -= flow

            for i, (angle, is_input, flow) in enumerate(reversed(zip(angles, are_inputs, scaled_flows))):
                if angle == UP and is_input:
                    pathlengths[n - i - 1] = lllength
                    lllength += flow
                elif angle == DOWN and not is_input:
                    pathlengths[n - i - 1] = lrlength
                    lrlength -= flow

            has_left_input = False
            for i, (angle, is_input, spec) in enumerate(reversed(zip(angles, are_inputs, zip(scaled_flows, pathlengths)))):
                if angle == RIGHT:
                    if is_input:
                        if has_left_input:
                            pathlengths[n - i - 1] = 0
                        else:
                            has_left_input = True

            has_right_output = False
            for i, (angle, is_input, spec) in enumerate(zip(angles, are_inputs, zip(scaled_flows, pathlengths))):
                if angle == RIGHT:
                    if not is_input:
                        if has_right_output:
                            pathlengths[i] = 0
                        else:
                            has_right_output = True

            urpath = [(
              Path.MOVETO,
              [self.gap - trunklength / 2.0,
               gain / 2.0]),
             (
              Path.LINETO,
              [(self.gap - trunklength / 2.0) / 2.0,
               gain / 2.0]),
             (
              Path.CURVE4,
              [(self.gap - trunklength / 2.0) / 8.0,
               gain / 2.0]),
             (
              Path.CURVE4,
              [(trunklength / 2.0 - self.gap) / 8.0,
               -loss / 2.0]),
             (
              Path.LINETO,
              [(trunklength / 2.0 - self.gap) / 2.0,
               -loss / 2.0]),
             (
              Path.LINETO,
              [trunklength / 2.0 - self.gap,
               -loss / 2.0])]
            llpath = [
             (Path.LINETO,
              [trunklength / 2.0 - self.gap,
               loss / 2.0]),
             (
              Path.LINETO,
              [(trunklength / 2.0 - self.gap) / 2.0,
               loss / 2.0]),
             (
              Path.CURVE4,
              [(trunklength / 2.0 - self.gap) / 8.0,
               loss / 2.0]),
             (
              Path.CURVE4,
              [(self.gap - trunklength / 2.0) / 8.0,
               -gain / 2.0]),
             (
              Path.LINETO,
              [(self.gap - trunklength / 2.0) / 2.0,
               -gain / 2.0]),
             (
              Path.LINETO,
              [self.gap - trunklength / 2.0,
               -gain / 2.0])]
            lrpath = [
             (Path.LINETO,
              [trunklength / 2.0 - self.gap,
               loss / 2.0])]
            ulpath = [
             (Path.LINETO,
              [self.gap - trunklength / 2.0,
               gain / 2.0])]
            tips = np.zeros((n, 2))
            label_locations = np.zeros((n, 2))
            for i, (angle, is_input, spec) in enumerate(zip(angles, are_inputs, zip(scaled_flows, pathlengths))):
                if angle == DOWN and is_input:
                    tips[i, :], label_locations[i, :] = self._add_input(ulpath, angle, *spec)
                elif angle == UP and not is_input:
                    tips[i, :], label_locations[i, :] = self._add_output(urpath, angle, *spec)

            for i, (angle, is_input, spec) in enumerate(reversed(zip(angles, are_inputs, zip(scaled_flows, pathlengths)))):
                if angle == UP and is_input:
                    tips[n - i - 1, :], label_locations[n - i - 1, :] = self._add_input(llpath, angle, *spec)
                elif angle == DOWN and not is_input:
                    tips[n - i - 1, :], label_locations[n - i - 1, :] = self._add_output(lrpath, angle, *spec)

            has_left_input = False
            for i, (angle, is_input, spec) in enumerate(reversed(zip(angles, are_inputs, zip(scaled_flows, pathlengths)))):
                if angle == RIGHT and is_input:
                    if not has_left_input:
                        if llpath[-1][1][0] > ulpath[-1][1][0]:
                            llpath.append((Path.LINETO,
                             [ulpath[-1][1][0],
                              llpath[-1][1][1]]))
                        has_left_input = True
                    tips[n - i - 1, :], label_locations[n - i - 1, :] = self._add_input(llpath, angle, *spec)

            has_right_output = False
            for i, (angle, is_input, spec) in enumerate(zip(angles, are_inputs, zip(scaled_flows, pathlengths))):
                if angle == RIGHT and not is_input:
                    if not has_right_output:
                        if urpath[-1][1][0] < lrpath[-1][1][0]:
                            urpath.append((Path.LINETO,
                             [lrpath[-1][1][0],
                              urpath[-1][1][1]]))
                        has_right_output = True
                    tips[i, :], label_locations[i, :] = self._add_output(urpath, angle, *spec)

            if not has_left_input:
                ulpath.pop()
                llpath.pop()
            if not has_right_output:
                lrpath.pop()
                urpath.pop()
            path = urpath + self._revert(lrpath) + llpath + self._revert(ulpath) + [
             (
              Path.CLOSEPOLY, urpath[0][1])]
            codes, vertices = zip(*path)
            vertices = np.array(vertices)

            def _get_angle(a, r):
                if a is None:
                    return
                else:
                    return a + r
                    return

            if prior is None:
                if rotation != 0:
                    angles = [ _get_angle(angle, rotation) for angle in angles ]
                    rotate = Affine2D().rotate_deg(rotation * 90).transform_point
                    tips = rotate(tips)
                    label_locations = rotate(label_locations)
                    vertices = rotate(vertices)
                text = self.ax.text(0, 0, s=patchlabel, ha='center', va='center')
            else:
                rotation = self.diagrams[prior].angles[connect[0]] - angles[connect[1]]
                angles = [ _get_angle(angle, rotation) for angle in angles ]
                rotate = Affine2D().rotate_deg(rotation * 90).transform_point
                tips = rotate(tips)
                offset = self.diagrams[prior].tips[connect[0]] - tips[connect[1]]
                translate = Affine2D().translate(*offset).transform_point
                tips = translate(tips)
                label_locations = translate(rotate(label_locations))
                vertices = translate(rotate(vertices))
                kwds = dict(s=patchlabel, ha='center', va='center')
                text = self.ax.text(*offset, **kwds)
            if False:
                print 'llpath\n', llpath
                print 'ulpath\n', self._revert(ulpath)
                print 'urpath\n', urpath
                print 'lrpath\n', self._revert(lrpath)
                xs, ys = zip(*vertices)
                self.ax.plot(xs, ys, 'go-')
            patch = PathPatch(Path(vertices, codes), fc=kwargs.pop('fc', kwargs.pop('facecolor', '#bfd1d4')), lw=kwargs.pop('lw', kwargs.pop('linewidth', 0.5)), **kwargs)
            self.ax.add_patch(patch)
            for i, (number, angle) in enumerate(zip(flows, angles)):
                if labels[i] is None or angle is None:
                    labels[i] = ''
                elif self.unit is not None:
                    quantity = self.format % abs(number) + self.unit
                    if labels[i] != '':
                        labels[i] += '\n'
                    labels[i] += quantity

            texts = []
            for i, (label, location) in enumerate(zip(labels, label_locations)):
                if label:
                    s = label
                else:
                    s = ''
                texts.append(self.ax.text(x=location[0], y=location[1], s=s, ha='center', va='center'))

        self.extent = (
         min(np.min(vertices[:, 0]), np.min(label_locations[:, 0]), self.extent[0]),
         max(np.max(vertices[:, 0]), np.max(label_locations[:, 0]), self.extent[1]),
         min(np.min(vertices[:, 1]), np.min(label_locations[:, 1]), self.extent[2]),
         max(np.max(vertices[:, 1]), np.max(label_locations[:, 1]), self.extent[3]))
        self.diagrams.append(Bunch(patch=patch, flows=flows, angles=angles, tips=tips, text=text, texts=texts))
        return self

    def finish(self):
        """
        Adjust the axes and return a list of information about the Sankey
        subdiagram(s).

        Return value is a list of subdiagrams represented with the following
        fields:

          ===============   ===================================================
          Field             Description
          ===============   ===================================================
          *patch*           Sankey outline (an instance of
                            :class:`~maplotlib.patches.PathPatch`)
          *flows*           values of the flows (positive for input, negative
                            for output)
          *angles*          list of angles of the arrows [deg/90]
                            For example, if the diagram has not been rotated,
                            an input to the top side will have an angle of 3
                            (DOWN), and an output from the top side will have
                            an angle of 1 (UP).  If a flow has been skipped
                            (because its magnitude is less than *tolerance*),
                            then its angle will be None.
          *tips*            array in which each row is an [x, y] pair
                            indicating the positions of the tips (or "dips") of
                            the flow paths
                            If the magnitude of a flow is less the *tolerance*
                            for the instance of :class:`Sankey`, the flow is
                            skipped and its tip will be at the center of the
                            diagram.
          *text*            :class:`~matplotlib.text.Text` instance for the
                            label of the diagram
          *texts*           list of :class:`~matplotlib.text.Text` instances
                            for the labels of flows
          ===============   ===================================================

        .. seealso::

            :meth:`add`
        """
        self.ax.axis([self.extent[0] - self.margin,
         self.extent[1] + self.margin,
         self.extent[2] - self.margin,
         self.extent[3] + self.margin])
        self.ax.set_aspect('equal', adjustable='datalim')
        return self.diagrams

    def __init__(self, ax=None, scale=1.0, unit='', format='%G', gap=0.25, radius=0.1, shoulder=0.03, offset=0.15, head_angle=100, margin=0.4, tolerance=1e-06, **kwargs):
        """
        Create a new Sankey instance.

        Optional keyword arguments:

          ===============   ===================================================
          Field             Description
          ===============   ===================================================
          *ax*              axes onto which the data should be plotted
                            If *ax* isn't provided, new axes will be created.
          *scale*           scaling factor for the flows
                            *scale* sizes the width of the paths in order to
                            maintain proper layout.  The same scale is applied
                            to all subdiagrams.  The value should be chosen
                            such that the product of the scale and the sum of
                            the inputs is approximately 1.0 (and the product of
                            the scale and the sum of the outputs is
                            approximately -1.0).
          *unit*            string representing the physical unit associated
                            with the flow quantities
                            If *unit* is None, then none of the quantities are
                            labeled.
          *format*          a Python number formatting string to be used in
                            labeling the flow as a quantity (i.e., a number
                            times a unit, where the unit is given)
          *gap*             space between paths that break in/break away
                            to/from the top or bottom
          *radius*          inner radius of the vertical paths
          *shoulder*        size of the shoulders of output arrowS
          *offset*          text offset (from the dip or tip of the arrow)
          *head_angle*      angle of the arrow heads (and negative of the angle
                            of the tails) [deg]
          *margin*          minimum space between Sankey outlines and the edge
                            of the plot area
          *tolerance*       acceptable maximum of the magnitude of the sum of
                            flows
                            The magnitude of the sum of connected flows cannot
                            be greater than *tolerance*.
          ===============   ===================================================

        The optional arguments listed above are applied to all subdiagrams so
        that there is consistent alignment and formatting.

        If :class:`Sankey` is instantiated with any keyword arguments other
        than those explicitly listed above (``**kwargs``), they will be passed
        to :meth:`add`, which will create the first subdiagram.

        In order to draw a complex Sankey diagram, create an instance of
        :class:`Sankey` by calling it without any kwargs::

            sankey = Sankey()

        Then add simple Sankey sub-diagrams::

            sankey.add() # 1
            sankey.add() # 2
            #...
            sankey.add() # n

        Finally, create the full diagram::

            sankey.finish()

        Or, instead, simply daisy-chain those calls::

            Sankey().add().add...  .add().finish()

        .. seealso::

            :meth:`add`
            :meth:`finish`

        **Examples:**

            .. plot:: mpl_examples/api/sankey_demo_basics.py
        """
        assert gap >= 0, "The gap is negative.\nThis isn't allowed because it would cause the paths to overlap."
        assert radius <= gap, "The inner radius is greater than the path spacing.\nThis isn't allowed because it would cause the paths to overlap."
        assert head_angle >= 0, "The angle is negative.\nThis isn't allowed because it would cause inputs to look like outputs and vice versa."
        assert tolerance >= 0, 'The tolerance is negative.\nIt must be a magnitude.'
        if ax is None:
            import matplotlib.pyplot as plt
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[])
        self.diagrams = []
        self.ax = ax
        self.unit = unit
        self.format = format
        self.scale = scale
        self.gap = gap
        self.radius = radius
        self.shoulder = shoulder
        self.offset = offset
        self.margin = margin
        self.pitch = np.tan(np.pi * (1 - head_angle / 180.0) / 2.0)
        self.tolerance = tolerance
        self.extent = np.array((np.inf, -np.inf, np.inf, -np.inf))
        if len(kwargs):
            self.add(**kwargs)
        return