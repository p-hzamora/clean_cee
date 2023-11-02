# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\graphics\testdrawings.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id $ '
__doc__ = 'Defines some standard drawings to use as test cases\n\nThis contains a number of routines to generate test drawings\nfor reportlab/graphics.  For now they are contrived, but we will expand them\nto try and trip up any parser. Feel free to add more.\n\n'
from ..reportlab.graphics.shapes import *
from reportlab.lib import colors

def getDrawing1():
    """Hello World, on a rectangular background"""
    D = Drawing(400, 200)
    D.add(Rect(50, 50, 300, 100, fillColor=colors.yellow))
    D.add(String(180, 100, 'Hello World', fillColor=colors.red))
    return D


def getDrawing2():
    """This demonstrates the basic shapes.  There are
    no groups or references.  Each solid shape should have
    a purple fill."""
    D = Drawing(400, 200)
    D.add(Line(10, 10, 390, 190))
    D.add(Circle(100, 100, 20, fillColor=colors.purple))
    D.add(Circle(200, 100, 20, fillColor=colors.purple))
    D.add(Circle(300, 100, 20, fillColor=colors.purple))
    D.add(Wedge(330, 100, 40, -10, 40, fillColor=colors.purple))
    D.add(PolyLine([120, 10, 130, 20, 140, 10, 150, 20, 160, 10, 
     170, 20, 180, 
     10, 190, 20, 200, 10]))
    D.add(Polygon([300, 20, 350, 20, 390, 80, 300, 75, 330, 40]))
    D.add(Ellipse(50, 150, 40, 20))
    D.add(Rect(120, 150, 60, 30, strokeWidth=10, strokeColor=colors.red, fillColor=colors.yellow))
    D.add(Rect(220, 150, 60, 30, 10, 10))
    D.add(String(10, 50, 'Basic Shapes', fillColor=colors.black))
    return D


if __name__ == '__main__':
    print __doc__