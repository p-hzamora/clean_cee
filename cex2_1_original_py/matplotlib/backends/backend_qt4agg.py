# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\backends\backend_qt4agg.pyc
# Compiled at: 2012-11-06 08:42:20
"""
Render to qt from agg
"""
from __future__ import division, print_function
import os, sys, ctypes, matplotlib
from matplotlib.figure import Figure
from backend_agg import FigureCanvasAgg
from backend_qt4 import QtCore, QtGui, FigureManagerQT, FigureCanvasQT, show, draw_if_interactive, backend_version, NavigationToolbar2QT
DEBUG = False
_decref = ctypes.pythonapi.Py_DecRef
_decref.argtypes = [ctypes.py_object]
_decref.restype = None

def new_figure_manager(num, *args, **kwargs):
    """
    Create a new figure manager instance
    """
    if DEBUG:
        print('backend_qtagg.new_figure_manager')
    FigureClass = kwargs.pop('FigureClass', Figure)
    thisFig = FigureClass(*args, **kwargs)
    return new_figure_manager_given_figure(num, thisFig)


def new_figure_manager_given_figure(num, figure):
    """
    Create a new figure manager instance for the given figure.
    """
    canvas = FigureCanvasQTAgg(figure)
    return FigureManagerQT(canvas, num)


class NavigationToolbar2QTAgg(NavigationToolbar2QT):

    def _get_canvas(self, fig):
        return FigureCanvasQTAgg(fig)


class FigureManagerQTAgg(FigureManagerQT):

    def _get_toolbar(self, canvas, parent):
        if matplotlib.rcParams['toolbar'] == 'classic':
            print('Classic toolbar is not supported')
        elif matplotlib.rcParams['toolbar'] == 'toolbar2':
            toolbar = NavigationToolbar2QTAgg(canvas, parent)
        else:
            toolbar = None
        return toolbar


class FigureCanvasQTAgg(FigureCanvasQT, FigureCanvasAgg):
    """
    The canvas the figure renders into.  Calls the draw and print fig
    methods, creates the renderers, etc...

    Public attribute

      figure - A Figure instance
   """

    def __init__(self, figure):
        if DEBUG:
            print('FigureCanvasQtAgg: ', figure)
        FigureCanvasQT.__init__(self, figure)
        FigureCanvasAgg.__init__(self, figure)
        self.drawRect = False
        self.rect = []
        self.blitbox = None
        self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)
        return

    def drawRectangle(self, rect):
        self.rect = rect
        self.drawRect = True
        self.repaint()

    def paintEvent(self, e):
        """
        Copy the image from the Agg canvas to the qt.drawable.
        In Qt, all drawing should be done inside of here when a widget is
        shown onscreen.
        """
        if DEBUG:
            print('FigureCanvasQtAgg.paintEvent: ', self, self.get_width_height())
        if self.blitbox is None:
            if QtCore.QSysInfo.ByteOrder == QtCore.QSysInfo.LittleEndian:
                stringBuffer = self.renderer._renderer.tostring_bgra()
            else:
                stringBuffer = self.renderer._renderer.tostring_argb()
            refcnt = sys.getrefcount(stringBuffer)
            qImage = QtGui.QImage(stringBuffer, self.renderer.width, self.renderer.height, QtGui.QImage.Format_ARGB32)
            p = QtGui.QPainter(self)
            p.drawPixmap(QtCore.QPoint(0, 0), QtGui.QPixmap.fromImage(qImage))
            if self.drawRect:
                p.setPen(QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.DotLine))
                p.drawRect(self.rect[0], self.rect[1], self.rect[2], self.rect[3])
            p.end()
            del qImage
            if refcnt != sys.getrefcount(stringBuffer):
                _decref(stringBuffer)
        else:
            bbox = self.blitbox
            l, b, r, t = bbox.extents
            w = int(r) - int(l)
            h = int(t) - int(b)
            t = int(b) + h
            reg = self.copy_from_bbox(bbox)
            stringBuffer = reg.to_string_argb()
            qImage = QtGui.QImage(stringBuffer, w, h, QtGui.QImage.Format_ARGB32)
            pixmap = QtGui.QPixmap.fromImage(qImage)
            p = QtGui.QPainter(self)
            p.drawPixmap(QtCore.QPoint(l, self.renderer.height - t), pixmap)
            p.end()
            self.blitbox = None
        self.drawRect = False
        return

    def draw(self):
        """
        Draw the figure with Agg, and queue a request
        for a Qt draw.
        """
        FigureCanvasAgg.draw(self)
        self.update()

    def blit(self, bbox=None):
        """
        Blit the region in bbox
        """
        self.blitbox = bbox
        l, b, w, h = bbox.bounds
        t = b + h
        self.repaint(l, self.renderer.height - t, w, h)

    def print_figure(self, *args, **kwargs):
        FigureCanvasAgg.print_figure(self, *args, **kwargs)
        self.draw()