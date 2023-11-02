# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\backends\backend_gtkagg.pyc
# Compiled at: 2012-10-30 18:11:14
"""
Render to gtk from agg
"""
from __future__ import division, print_function
import os, matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_gtk import gtk, FigureManagerGTK, FigureCanvasGTK, show, draw_if_interactive, error_msg_gtk, NavigationToolbar, PIXELS_PER_INCH, backend_version, NavigationToolbar2GTK
from matplotlib.backends._gtkagg import agg_to_gtk_drawable
DEBUG = False

class NavigationToolbar2GTKAgg(NavigationToolbar2GTK):

    def _get_canvas(self, fig):
        return FigureCanvasGTKAgg(fig)


class FigureManagerGTKAgg(FigureManagerGTK):

    def _get_toolbar(self, canvas):
        if matplotlib.rcParams['toolbar'] == 'classic':
            toolbar = NavigationToolbar(canvas, self.window)
        elif matplotlib.rcParams['toolbar'] == 'toolbar2':
            toolbar = NavigationToolbar2GTKAgg(canvas, self.window)
        else:
            toolbar = None
        return toolbar


def new_figure_manager(num, *args, **kwargs):
    """
    Create a new figure manager instance
    """
    if DEBUG:
        print('backend_gtkagg.new_figure_manager')
    FigureClass = kwargs.pop('FigureClass', Figure)
    thisFig = FigureClass(*args, **kwargs)
    return new_figure_manager_given_figure(num, thisFig)


def new_figure_manager_given_figure(num, figure):
    """
    Create a new figure manager instance for the given figure.
    """
    canvas = FigureCanvasGTKAgg(figure)
    return FigureManagerGTKAgg(canvas, num)
    if DEBUG:
        print('backend_gtkagg.new_figure_manager done')


class FigureCanvasGTKAgg(FigureCanvasGTK, FigureCanvasAgg):
    filetypes = FigureCanvasGTK.filetypes.copy()
    filetypes.update(FigureCanvasAgg.filetypes)

    def configure_event(self, widget, event=None):
        if DEBUG:
            print('FigureCanvasGTKAgg.configure_event')
        if widget.window is None:
            return
        else:
            try:
                del self.renderer
            except AttributeError:
                pass

            w, h = widget.window.get_size()
            if w == 1 or h == 1:
                return
            dpival = self.figure.dpi
            winch = w / dpival
            hinch = h / dpival
            self.figure.set_size_inches(winch, hinch)
            self._need_redraw = True
            self.resize_event()
            if DEBUG:
                print('FigureCanvasGTKAgg.configure_event end')
            return True

    def _render_figure(self, pixmap, width, height):
        if DEBUG:
            print('FigureCanvasGTKAgg.render_figure')
        FigureCanvasAgg.draw(self)
        if DEBUG:
            print('FigureCanvasGTKAgg.render_figure pixmap', pixmap)
        buf = self.buffer_rgba()
        ren = self.get_renderer()
        w = int(ren.width)
        h = int(ren.height)
        pixbuf = gtk.gdk.pixbuf_new_from_data(buf, gtk.gdk.COLORSPACE_RGB, True, 8, w, h, w * 4)
        pixmap.draw_pixbuf(pixmap.new_gc(), pixbuf, 0, 0, 0, 0, w, h, gtk.gdk.RGB_DITHER_NONE, 0, 0)
        if DEBUG:
            print('FigureCanvasGTKAgg.render_figure done')

    def blit(self, bbox=None):
        if DEBUG:
            print('FigureCanvasGTKAgg.blit', self._pixmap)
        agg_to_gtk_drawable(self._pixmap, self.renderer._renderer, bbox)
        x, y, w, h = self.allocation
        self.window.draw_drawable(self.style.fg_gc[self.state], self._pixmap, 0, 0, 0, 0, w, h)
        if DEBUG:
            print('FigureCanvasGTKAgg.done')

    def print_png(self, filename, *args, **kwargs):
        agg = self.switch_backends(FigureCanvasAgg)
        return agg.print_png(filename, *args, **kwargs)