# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\graphics\renderbase.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id $ '
__doc__ = 'Superclass for renderers to factor out common functionality and default implementations.'
from ..reportlab.graphics.shapes import *
from reportlab.lib.validators import DerivedValue
from reportlab import rl_config

def inverse(A):
    """For A affine 2D represented as 6vec return 6vec version of A**(-1)"""
    det = float(A[0] * A[3] - A[2] * A[1])
    R = [A[3] / det, -A[1] / det, -A[2] / det, A[0] / det]
    return tuple(R + [-R[0] * A[4] - R[2] * A[5], -R[1] * A[4] - R[3] * A[5]])


def mmult(A, B):
    """A postmultiplied by B"""
    return (
     A[0] * B[0] + A[2] * B[1],
     A[1] * B[0] + A[3] * B[1],
     A[0] * B[2] + A[2] * B[3],
     A[1] * B[2] + A[3] * B[3],
     A[0] * B[4] + A[2] * B[5] + A[4],
     A[1] * B[4] + A[3] * B[5] + A[5])


def getStateDelta(shape):
    """Used to compute when we need to change the graphics state.
    For example, if we have two adjacent red shapes we don't need
    to set the pen color to red in between. Returns the effect
    the given shape would have on the graphics state"""
    delta = {}
    for prop, value in shape.getProperties().items():
        if prop in STATE_DEFAULTS:
            delta[prop] = value

    return delta


class StateTracker:
    """Keeps a stack of transforms and state
    properties.  It can contain any properties you
    want, but the keys 'transform' and 'ctm' have
    special meanings.  The getCTM()
    method returns the current transformation
    matrix at any point, without needing to
    invert matrixes when you pop."""

    def __init__(self, defaults=None):
        self._deltas = []
        self._combined = []
        if defaults is None:
            defaults = STATE_DEFAULTS.copy()
        if 'transform' in defaults:
            defaults['ctm'] = defaults['transform']
        self._combined.append(defaults)
        return

    def push(self, delta):
        """Take a new state dictionary of changes and push it onto
        the stack.  After doing this, the combined state is accessible
        through getState()"""
        newstate = self._combined[-1].copy()
        for key, value in delta.items():
            if key == 'transform':
                newstate['transform'] = delta['transform']
                newstate['ctm'] = mmult(self._combined[-1]['ctm'], delta['transform'])
            else:
                newstate[key] = value

        self._combined.append(newstate)
        self._deltas.append(delta)

    def pop(self):
        """steps back one, and returns a state dictionary with the
        deltas to reverse out of wherever you are.  Depending
        on your back end, you may not need the return value,
        since you can get the complete state afterwards with getState()"""
        del self._combined[-1]
        newState = self._combined[-1]
        lastDelta = self._deltas[-1]
        del self._deltas[-1]
        reverseDelta = {}
        for key, curValue in lastDelta.items():
            prevValue = newState[key]
            if prevValue != curValue:
                if key == 'transform':
                    reverseDelta[key] = inverse(lastDelta['transform'])
                else:
                    reverseDelta[key] = prevValue

        return reverseDelta

    def getState(self):
        """returns the complete graphics state at this point"""
        return self._combined[-1]

    def getCTM(self):
        """returns the current transformation matrix at this point"""
        return self._combined[-1]['ctm']

    def __getitem__(self, key):
        """returns the complete graphics state value of key at this point"""
        return self._combined[-1][key]

    def __setitem__(self, key, value):
        """sets the complete graphics state value of key to value"""
        self._combined[-1][key] = value


def testStateTracker():
    print 'Testing state tracker'
    defaults = {'fillColor': None, 'strokeColor': None, 'fontName': None, 'transform': [1, 0, 0, 1, 0, 0]}
    from reportlab.graphics.shapes import _baseGFontName
    deltas = [{'fillColor': 'red'}, {'fillColor': 'green', 'strokeColor': 'blue', 'fontName': _baseGFontName}, {'transform': [0.5, 0, 0, 0.5, 0, 0]}, {'transform': [0.5, 0, 0, 0.5, 2, 3]}, {'strokeColor': 'red'}]
    st = StateTracker(defaults)
    print 'initial:', st.getState()
    print
    for delta in deltas:
        print 'pushing:', delta
        st.push(delta)
        print 'state:  ', st.getState(), '\n'

    for delta in deltas:
        print 'popping:', st.pop()
        print 'state:  ', st.getState(), '\n'

    return


def _expandUserNode(node, canvas):
    if isinstance(node, UserNode):
        try:
            if hasattr(node, '_canvas'):
                ocanvas = 1
            else:
                node._canvas = canvas
                ocanvas = None
            onode = node
            node = node.provideNode()
        finally:
            if not ocanvas:
                del onode._canvas

    return node


def renderScaledDrawing(d):
    renderScale = d.renderScale
    if renderScale != 1.0:
        o = d
        d = d.__class__(o.width * renderScale, o.height * renderScale)
        d.__dict__ = o.__dict__.copy()
        d.scale(renderScale, renderScale)
        d.renderScale = 1.0
    return d


class Renderer:
    """Virtual superclass for graphics renderers."""

    def __init__(self):
        self._tracker = StateTracker()
        self._nodeStack = []

    def undefined(self, operation):
        raise ValueError, '%s operation not defined at superclass class=%s' % (operation, self.__class__)

    def draw(self, drawing, canvas, x=0, y=0, showBoundary=rl_config._unset_):
        """This is the top level function, which draws the drawing at the given
        location. The recursive part is handled by drawNode."""
        if showBoundary is rl_config._unset_:
            showBoundary = rl_config.showBoundary
        self._canvas = canvas
        canvas.__dict__['_drawing'] = self._drawing = drawing
        drawing._parent = None
        try:
            if showBoundary:
                canvas.rect(x, y, drawing.width, drawing.height)
            canvas.saveState()
            self.initState(x, y)
            self.drawNode(drawing)
            self.pop()
            canvas.restoreState()
        finally:
            del self._canvas
            del self._drawing
            del canvas._drawing
            del drawing._parent

        return

    def initState(self, x, y):
        deltas = STATE_DEFAULTS.copy()
        deltas['transform'] = [1, 0, 0, 1, x, y]
        self._tracker.push(deltas)
        self.applyStateChanges(deltas, {})

    def pop(self):
        self._tracker.pop()

    def drawNode(self, node):
        """This is the recursive method called for each node
        in the tree"""
        self.undefined('drawNode')

    def getStateValue(self, key):
        """Return current state parameter for given key"""
        currentState = self._tracker._combined[-1]
        return currentState[key]

    def fillDerivedValues(self, node):
        """Examine a node for any values which are Derived,
        and replace them with their calculated values.
        Generally things may look at the drawing or their
        parent.
        
        """
        for key, value in node.__dict__.items():
            if isinstance(value, DerivedValue):
                newValue = value.getValue(self, key)
                node.__dict__[key] = newValue

    def drawNodeDispatcher(self, node):
        """dispatch on the node's (super) class: shared code"""
        canvas = getattr(self, '_canvas', None)
        try:
            node = _expandUserNode(node, canvas)
            if not node:
                return
            if hasattr(node, '_canvas'):
                ocanvas = 1
            else:
                node._canvas = canvas
                ocanvas = None
            self.fillDerivedValues(node)
            dtcb = getattr(node, '_drawTimeCallback', None)
            if dtcb:
                dtcb(node, canvas=canvas, renderer=self)
            if isinstance(node, Line):
                self.drawLine(node)
            elif isinstance(node, Image):
                self.drawImage(node)
            elif isinstance(node, Rect):
                self.drawRect(node)
            elif isinstance(node, Circle):
                self.drawCircle(node)
            elif isinstance(node, Ellipse):
                self.drawEllipse(node)
            elif isinstance(node, PolyLine):
                self.drawPolyLine(node)
            elif isinstance(node, Polygon):
                self.drawPolygon(node)
            elif isinstance(node, Path):
                self.drawPath(node)
            elif isinstance(node, String):
                self.drawString(node)
            elif isinstance(node, Group):
                self.drawGroup(node)
            elif isinstance(node, Wedge):
                self.drawWedge(node)
            else:
                print 'DrawingError', 'Unexpected element %s in drawing!' % str(node)
        finally:
            if not ocanvas:
                del node._canvas

        return

    _restores = {'stroke': '_stroke', 'stroke_width': '_lineWidth', 'stroke_linecap': '_lineCap', 'stroke_linejoin': '_lineJoin', 
       'fill': '_fill', 'font_family': '_font', 'font_size': '_fontSize'}

    def drawGroup(self, group):
        canvas = getattr(self, '_canvas', None)
        for node in group.getContents():
            node = _expandUserNode(node, canvas)
            if not node:
                continue
            self.fillDerivedValues(node)
            try:
                if hasattr(node, '_canvas'):
                    ocanvas = 1
                else:
                    node._canvas = canvas
                    ocanvas = None
                node._parent = group
                self.drawNode(node)
            finally:
                del node._parent
                if not ocanvas:
                    del node._canvas

        return

    def drawWedge(self, wedge):
        polygon = wedge.asPolygon()
        self.drawPolygon(polygon)

    def drawPath(self, path):
        polygons = path.asPolygons()
        for polygon in polygons:
            self.drawPolygon(polygon)

    def drawRect(self, rect):
        self.undefined('drawRect')

    def drawLine(self, line):
        self.undefined('drawLine')

    def drawCircle(self, circle):
        self.undefined('drawCircle')

    def drawPolyLine(self, p):
        self.undefined('drawPolyLine')

    def drawEllipse(self, ellipse):
        self.undefined('drawEllipse')

    def drawPolygon(self, p):
        self.undefined('drawPolygon')

    def drawString(self, stringObj):
        self.undefined('drawString')

    def applyStateChanges(self, delta, newState):
        """This takes a set of states, and outputs the operators
        needed to set those properties"""
        self.undefined('applyStateChanges')


if __name__ == '__main__':
    print 'this file has no script interpretation'
    print __doc__