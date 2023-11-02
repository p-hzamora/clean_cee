# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\graphics\charts\dotbox.pyc
# Compiled at: 2013-03-27 15:37:42
from reportlab.lib.colors import blue, _PCMYK_black
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.shapes import Circle, Drawing, Group, Line, Rect, String
from reportlab.graphics.widgetbase import Widget
from reportlab.lib.attrmap import *
from reportlab.lib.validators import *
from reportlab.lib.units import cm
from reportlab.pdfbase.pdfmetrics import getFont
from reportlab.graphics.charts.lineplots import _maxWidth

class DotBox(Widget):
    """Returns a dotbox widget."""
    _attrMap = AttrMap(xlabels=AttrMapValue(isNoneOrListOfNoneOrStrings, desc='List of text labels for boxes on left hand side'), ylabels=AttrMapValue(isNoneOrListOfNoneOrStrings, desc='Text label for second box on left hand side'), labelFontName=AttrMapValue(isString, desc='Name of font used for the labels'), labelFontSize=AttrMapValue(isNumber, desc='Size of font used for the labels'), labelOffset=AttrMapValue(isNumber, desc='Space between label text and grid edge'), strokeWidth=AttrMapValue(isNumber, desc='Width of the grid and dot outline'), gridDivWidth=AttrMapValue(isNumber, desc="Width of each 'box'"), gridColor=AttrMapValue(isColor, desc='Colour for the box and gridding'), dotDiameter=AttrMapValue(isNumber, desc="Diameter of the circle used for the 'dot'"), dotColor=AttrMapValue(isColor, desc='Colour of the circle on the box'), dotXPosition=AttrMapValue(isNumber, desc='X Position of the circle'), dotYPosition=AttrMapValue(isNumber, desc='X Position of the circle'), x=AttrMapValue(isNumber, desc='X Position of dotbox'), y=AttrMapValue(isNumber, desc='Y Position of dotbox'))

    def __init__(self):
        self.xlabels = [
         'Value', 'Blend', 'Growth']
        self.ylabels = ['Small', 'Medium', 'Large']
        self.labelFontName = 'Helvetica'
        self.labelFontSize = 6
        self.labelOffset = 5
        self.strokeWidth = 0.5
        self.gridDivWidth = 0.5 * cm
        self.gridColor = colors.Color(25 / 255.0, 77 / 255.0, 135 / 255.0)
        self.dotDiameter = 0.4 * cm
        self.dotColor = colors.Color(232 / 255.0, 224 / 255.0, 119 / 255.0)
        self.dotXPosition = 1
        self.dotYPosition = 1
        self.x = 30
        self.y = 5

    def _getDrawingDimensions(self):
        leftPadding = rightPadding = topPadding = bottomPadding = 5
        tx = len(self.xlabels) * self.gridDivWidth
        tx = tx + leftPadding + rightPadding + self.labelOffset
        tx = tx + _maxWidth(self.xlabels, self.labelFontName, self.labelFontSize)
        ty = len(self.ylabels) * self.gridDivWidth
        ty = ty + topPadding + bottomPadding + self.labelOffset
        ty = ty + _maxWidth(self.ylabels, self.labelFontName, self.labelFontSize)
        return (
         tx, ty)

    def demo(self, drawing=None):
        if not drawing:
            tx, ty = self._getDrawingDimensions()
            drawing = Drawing(tx, ty)
        drawing.add(self.draw())
        return drawing

    def draw(self):
        g = Group()
        g.add(Rect(self.x, self.y, len(self.xlabels) * self.gridDivWidth, len(self.ylabels) * self.gridDivWidth, strokeColor=self.gridColor, strokeWidth=self.strokeWidth, fillColor=None))
        for f in range(1, len(self.ylabels)):
            g.add(Line(strokeColor=self.gridColor, strokeWidth=self.strokeWidth, x1=self.x, y1=self.y + f * self.gridDivWidth, x2=self.x + len(self.xlabels) * self.gridDivWidth, y2=self.y + f * self.gridDivWidth))

        for f in range(1, len(self.xlabels)):
            g.add(Line(strokeColor=self.gridColor, strokeWidth=self.strokeWidth, x1=self.x + f * self.gridDivWidth, y1=self.y, x2=self.x + f * self.gridDivWidth, y2=self.y + len(self.ylabels) * self.gridDivWidth))

        g.add(Circle(strokeColor=self.gridColor, strokeWidth=self.strokeWidth, fillColor=self.dotColor, cx=self.x + self.dotXPosition * self.gridDivWidth, cy=self.y + self.dotYPosition * self.gridDivWidth, r=self.dotDiameter / 2.0))
        ascent = getFont(self.labelFontName).face.ascent
        if ascent == 0:
            ascent = 0.718
        ascent = ascent * self.labelFontSize
        if self.ylabels != None:
            for f in range(len(self.ylabels) - 1, -1, -1):
                if self.ylabels[f] != None:
                    g.add(String(strokeColor=self.gridColor, text=self.ylabels[f], fontName=self.labelFontName, fontSize=self.labelFontSize, fillColor=_PCMYK_black, x=self.x - self.labelOffset, y=self.y + (f * self.gridDivWidth + (self.gridDivWidth - ascent) / 2.0), textAnchor='end'))

        if self.xlabels != None:
            for f in range(0, len(self.xlabels)):
                if self.xlabels[f] != None:
                    l = Label()
                    l.x = self.x + f * self.gridDivWidth + (self.gridDivWidth + ascent) / 2.0
                    l.y = self.y + len(self.ylabels) * self.gridDivWidth + self.labelOffset
                    l.angle = 90
                    l.textAnchor = 'start'
                    l.fontName = self.labelFontName
                    l.fontSize = self.labelFontSize
                    l.fillColor = _PCMYK_black
                    l.setText(self.xlabels[f])
                    l.boxAnchor = 'sw'
                    l.draw()
                    g.add(l)

        return g


if __name__ == '__main__':
    d = DotBox()
    d.demo().save(fnRoot='dotbox')