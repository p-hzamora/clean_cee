# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\graphics\charts\markers.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = 'This modules defines a collection of markers used in charts.\n\nThe make* functions return a simple shape or a widget as for\nthe smiley.\n'
from reportlab.lib import colors
from reportlab.graphics.shapes import Rect, Line, Circle, Polygon
from reportlab.graphics.widgets.signsandsymbols import SmileyFace

def makeEmptySquare(x, y, size, color):
    """Make an empty square marker."""
    d = size / 2.0
    rect = Rect(x - d, y - d, 2 * d, 2 * d)
    rect.strokeColor = color
    rect.fillColor = None
    return rect


def makeFilledSquare(x, y, size, color):
    """Make a filled square marker."""
    d = size / 2.0
    rect = Rect(x - d, y - d, 2 * d, 2 * d)
    rect.strokeColor = color
    rect.fillColor = color
    return rect


def makeFilledDiamond(x, y, size, color):
    """Make a filled diamond marker."""
    d = size / 2.0
    poly = Polygon((x - d, y, x, y + d, x + d, y, x, y - d))
    poly.strokeColor = color
    poly.fillColor = color
    return poly


def makeEmptyCircle(x, y, size, color):
    """Make a hollow circle marker."""
    d = size / 2.0
    circle = Circle(x, y, d)
    circle.strokeColor = color
    circle.fillColor = colors.white
    return circle


def makeFilledCircle(x, y, size, color):
    """Make a hollow circle marker."""
    d = size / 2.0
    circle = Circle(x, y, d)
    circle.strokeColor = color
    circle.fillColor = color
    return circle


def makeSmiley(x, y, size, color):
    """Make a smiley marker."""
    d = size
    s = SmileyFace()
    s.fillColor = color
    s.x = x - d
    s.y = y - d
    s.size = d * 2
    return s