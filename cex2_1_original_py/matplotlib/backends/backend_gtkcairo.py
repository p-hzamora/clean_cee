# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\backends\backend_gtkcairo.pyc
# Compiled at: 2012-10-30 18:11:14
"""
GTK+ Matplotlib interface using cairo (not GDK) drawing operations.
Author: Steve Chaplin
"""
from __future__ import print_function
import gtk
if gtk.pygtk_version < (2, 7, 0):
    import cairo.gtk
from matplotlib.backends import backend_cairo
from .matplotlib.backends.backend_gtk import *
backend_version = 'PyGTK(%d.%d.%d) ' % gtk.pygtk_version + 'Pycairo(%s)' % backend_cairo.backend_version
_debug = False

def new_figure_manager(num, *args, **kwargs):
    """
    Create a new figure manager instance
    """
    if _debug:
        print('backend_gtkcairo.%s()' % fn_name())
    FigureClass = kwargs.pop('FigureClass', Figure)
    thisFig = FigureClass(*args, **kwargs)
    return new_figure_manager_given_figure(num, thisFig)


def new_figure_manager_given_figure(num, figure):
    """
    Create a new figure manager instance for the given figure.
    """
    canvas = FigureCanvasGTKCairo(figure)
    return FigureManagerGTK(canvas, num)


class RendererGTKCairo(backend_cairo.RendererCairo):
    if gtk.pygtk_version >= (2, 7, 0):

        def set_pixmap(self, pixmap):
            self.gc.ctx = pixmap.cairo_create()

    else:

        def set_pixmap(self, pixmap):
            self.gc.ctx = cairo.gtk.gdk_cairo_create(pixmap)


class FigureCanvasGTKCairo(backend_cairo.FigureCanvasCairo, FigureCanvasGTK):
    filetypes = FigureCanvasGTK.filetypes.copy()
    filetypes.update(backend_cairo.FigureCanvasCairo.filetypes)

    def _renderer_init(self):
        """Override to use cairo (rather than GDK) renderer"""
        if _debug:
            print('%s.%s()' % (self.__class__.__name__, _fn_name()))
        self._renderer = RendererGTKCairo(self.figure.dpi)


class FigureManagerGTKCairo(FigureManagerGTK):

    def _get_toolbar(self, canvas):
        if matplotlib.rcParams['toolbar'] == 'classic':
            toolbar = NavigationToolbar(canvas, self.window)
        elif matplotlib.rcParams['toolbar'] == 'toolbar2':
            toolbar = NavigationToolbar2GTKCairo(canvas, self.window)
        else:
            toolbar = None
        return toolbar


class NavigationToolbar2Cairo(NavigationToolbar2GTK):

    def _get_canvas(self, fig):
        return FigureCanvasGTKCairo(fig)