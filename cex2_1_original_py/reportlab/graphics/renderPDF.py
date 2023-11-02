# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\graphics\renderPDF.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = 'Render Drawing objects within others PDFs or standalone\n\nUsage::\n    \n    import renderpdf\n    renderpdf.draw(drawing, canvas, x, y)\n\nExecute the script to see some test drawings.\nchanged\n'
from ..reportlab.graphics.shapes import *
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.utils import getStringIO
from reportlab import rl_config
from renderbase import Renderer, StateTracker, getStateDelta, renderScaledDrawing

def draw(drawing, canvas, x, y, showBoundary=rl_config._unset_):
    """As it says"""
    R = _PDFRenderer()
    R.draw(renderScaledDrawing(drawing), canvas, x, y, showBoundary=showBoundary)


class _PDFRenderer(Renderer):
    """This draws onto a PDF document.  It needs to be a class
    rather than a function, as some PDF-specific state tracking is
    needed outside of the state info in the SVG model."""

    def __init__(self):
        self._stroke = 0
        self._fill = 0
        self._tracker = StateTracker()

    def drawNode(self, node):
        """This is the recursive method called for each node
        in the tree"""
        if not (isinstance(node, Path) and node.isClipPath):
            self._canvas.saveState()
        deltas = getStateDelta(node)
        self._tracker.push(deltas)
        self.applyStateChanges(deltas, {})
        self.drawNodeDispatcher(node)
        self._tracker.pop()
        if not (isinstance(node, Path) and node.isClipPath):
            self._canvas.restoreState()

    def drawRect(self, rect):
        if rect.rx == rect.ry == 0:
            self._canvas.rect(rect.x, rect.y, rect.width, rect.height, stroke=self._stroke, fill=self._fill)
        else:
            self._canvas.roundRect(rect.x, rect.y, rect.width, rect.height, rect.rx, fill=self._fill, stroke=self._stroke)

    def drawImage(self, image):
        path = image.path
        if path and (hasattr(path, 'mode') or os.path.exists(image.path)):
            self._canvas.drawInlineImage(path, image.x, image.y, image.width, image.height)

    def drawLine(self, line):
        if self._stroke:
            self._canvas.line(line.x1, line.y1, line.x2, line.y2)

    def drawCircle(self, circle):
        self._canvas.circle(circle.cx, circle.cy, circle.r, fill=self._fill, stroke=self._stroke)

    def drawPolyLine(self, polyline):
        if self._stroke:
            assert len(polyline.points) >= 2, 'Polyline must have 2 or more points'
            head, tail = polyline.points[0:2], polyline.points[2:]
            path = self._canvas.beginPath()
            path.moveTo(head[0], head[1])
            for i in range(0, len(tail), 2):
                path.lineTo(tail[i], tail[i + 1])

            self._canvas.drawPath(path)

    def drawWedge(self, wedge):
        centerx, centery, radius, startangledegrees, endangledegrees = (
         wedge.centerx, wedge.centery, wedge.radius, wedge.startangledegrees, wedge.endangledegrees)
        yradius, radius1, yradius1 = wedge._xtraRadii()
        if yradius is None:
            yradius = radius
        angle = endangledegrees - startangledegrees
        path = self._canvas.beginPath()
        if (radius1 == 0 or radius1 is None) and (yradius1 == 0 or yradius1 is None):
            path.moveTo(centerx, centery)
            path.arcTo(centerx - radius, centery - yradius, centerx + radius, centery + yradius, startangledegrees, angle)
        else:
            path.arc(centerx - radius, centery - yradius, centerx + radius, centery + yradius, startangledegrees, angle)
            path.arcTo(centerx - radius1, centery - yradius1, centerx + radius1, centery + yradius1, endangledegrees, -angle)
        path.close()
        self._canvas.drawPath(path, fill=self._fill, stroke=self._stroke)
        return

    def drawEllipse(self, ellipse):
        x1 = ellipse.cx - ellipse.rx
        x2 = ellipse.cx + ellipse.rx
        y1 = ellipse.cy - ellipse.ry
        y2 = ellipse.cy + ellipse.ry
        self._canvas.ellipse(x1, y1, x2, y2, fill=self._fill, stroke=self._stroke)

    def drawPolygon(self, polygon):
        assert len(polygon.points) >= 2, 'Polyline must have 2 or more points'
        head, tail = polygon.points[0:2], polygon.points[2:]
        path = self._canvas.beginPath()
        path.moveTo(head[0], head[1])
        for i in range(0, len(tail), 2):
            path.lineTo(tail[i], tail[i + 1])

        path.close()
        self._canvas.drawPath(path, stroke=self._stroke, fill=self._fill)

    def drawString(self, stringObj):
        if self._fill:
            S = self._tracker.getState()
            text_anchor, x, y, text, enc = (S['textAnchor'], stringObj.x, stringObj.y, stringObj.text, stringObj.encoding)
            if text_anchor not in ('start', 'inherited'):
                font, font_size = S['fontName'], S['fontSize']
                textLen = stringWidth(text, font, font_size, enc)
                if text_anchor == 'end':
                    x -= textLen
                elif text_anchor == 'middle':
                    x -= textLen * 0.5
                else:
                    if text_anchor == 'numeric':
                        x -= numericXShift(text_anchor, text, textLen, font, font_size, enc)
                    else:
                        raise ValueError, 'bad value for textAnchor ' + str(text_anchor)
            t = self._canvas.beginText(x, y)
            t.textLine(text)
            self._canvas.drawText(t)

    def drawPath(self, path):
        from reportlab.graphics.shapes import _renderPath
        pdfPath = self._canvas.beginPath()
        drawFuncs = (pdfPath.moveTo, pdfPath.lineTo, pdfPath.curveTo, pdfPath.close)
        isClosed = _renderPath(path, drawFuncs)
        if isClosed:
            fill = self._fill
        else:
            fill = 0
        if path.isClipPath:
            self._canvas.clipPath(pdfPath, fill=fill, stroke=self._stroke)
        else:
            self._canvas.drawPath(pdfPath, fill=fill, stroke=self._stroke)

    def setStrokeColor(self, c):
        self._canvas.setStrokeColor(c)

    def setFillColor(self, c):
        self._canvas.setFillColor(c)

    def applyStateChanges(self, delta, newState):
        """This takes a set of states, and outputs the PDF operators
        needed to set those properties"""
        for key, value in delta.items():
            if key == 'transform':
                self._canvas.transform(value[0], value[1], value[2], value[3], value[4], value[5])
            elif key == 'strokeColor':
                if value is None:
                    self._stroke = 0
                else:
                    self._stroke = 1
                    self.setStrokeColor(value)
            elif key == 'strokeWidth':
                self._canvas.setLineWidth(value)
            elif key == 'strokeLineCap':
                self._canvas.setLineCap(value)
            elif key == 'strokeLineJoin':
                self._canvas.setLineJoin(value)
            elif key == 'strokeDashArray':
                if value:
                    if isinstance(value, (list, tuple)) and len(value) == 2 and isinstance(value[1], (tuple, list)):
                        phase = value[0]
                        value = value[1]
                    else:
                        phase = 0
                    self._canvas.setDash(value, phase)
                else:
                    self._canvas.setDash()
            elif key == 'fillColor':
                if value is None:
                    self._fill = 0
                else:
                    self._fill = 1
                    self.setFillColor(value)
            elif key in ('fontSize', 'fontName'):
                fontname = delta.get('fontName', self._canvas._fontname)
                fontsize = delta.get('fontSize', self._canvas._fontsize)
                self._canvas.setFont(fontname, fontsize)
            elif key == 'fillOpacity':
                if value is not None:
                    self._canvas.setFillAlpha(value)
            elif key == 'strokeOpacity':
                if value is not None:
                    self._canvas.setStrokeAlpha(value)
            elif key == 'fillOverprint':
                self._canvas.setFillOverprint(value)
            elif key == 'strokeOverprint':
                self._canvas.setStrokeOverprint(value)
            elif key == 'overprintMask':
                self._canvas.setOverprintMask(value)

        return


from reportlab.platypus import Flowable

class GraphicsFlowable(Flowable):
    """Flowable wrapper around a Pingo drawing"""

    def __init__(self, drawing):
        self.drawing = drawing
        self.width = self.drawing.width
        self.height = self.drawing.height

    def draw(self):
        draw(self.drawing, self.canv, 0, 0)


def drawToFile(d, fn, msg='', showBoundary=rl_config._unset_, autoSize=1):
    """Makes a one-page PDF with just the drawing.

    If autoSize=1, the PDF will be the same size as
    the drawing; if 0, it will place the drawing on
    an A4 page with a title above it - possibly overflowing
    if too big."""
    d = renderScaledDrawing(d)
    c = Canvas(fn)
    if msg:
        c.setFont(rl_config.defaultGraphicsFontName, 36)
        c.drawString(80, 750, msg)
    c.setTitle(msg)
    if autoSize:
        c.setPageSize((d.width, d.height))
        draw(d, c, 0, 0, showBoundary=showBoundary)
    else:
        c.setFont(rl_config.defaultGraphicsFontName, 12)
        y = 740
        i = 1
        y = y - d.height
        draw(d, c, 80, y, showBoundary=showBoundary)
    c.showPage()
    c.save()
    if sys.platform == 'mac' and not hasattr(fn, 'write'):
        try:
            import macfs, macostools
            macfs.FSSpec(fn).SetCreatorType('CARO', 'PDF ')
            macostools.touched(fn)
        except:
            pass


def drawToString(d, msg='', showBoundary=rl_config._unset_, autoSize=1):
    """Returns a PDF as a string in memory, without touching the disk"""
    s = getStringIO()
    drawToFile(d, s, msg=msg, showBoundary=showBoundary, autoSize=autoSize)
    return s.getvalue()


def test():
    from reportlab.graphics.shapes import _baseGFontName, _baseGFontNameBI
    c = Canvas('renderPDF.pdf')
    c.setFont(_baseGFontName, 36)
    c.drawString(80, 750, 'Graphics Test')
    from reportlab.graphics import testshapes
    drawings = []
    for funcname in dir(testshapes):
        if funcname[0:10] == 'getDrawing':
            drawing = eval('testshapes.' + funcname + '()')
            docstring = eval('testshapes.' + funcname + '.__doc__')
            drawings.append((drawing, docstring))

    c.setFont(_baseGFontName, 12)
    y = 740
    i = 1
    for drawing, docstring in drawings:
        assert docstring is not None, 'Drawing %d has no docstring!' % i
        if y < 300:
            c.showPage()
            y = 740
        y = y - 30
        c.setFont(_baseGFontNameBI, 12)
        c.drawString(80, y, 'Drawing %d' % i)
        c.setFont(_baseGFontName, 12)
        y = y - 14
        textObj = c.beginText(80, y)
        textObj.textLines(docstring)
        c.drawText(textObj)
        y = textObj.getY()
        y = y - drawing.height
        draw(drawing, c, 80, y)
        i = i + 1

    if y != 740:
        c.showPage()
    c.save()
    print 'saved renderPDF.pdf'
    return


if __name__ == '__main__':
    test()