# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\backends\backend_cocoaagg.pyc
# Compiled at: 2012-10-30 18:11:14
from __future__ import division, print_function
import os, sys
try:
    import objc
except ImportError:
    raise ImportError('The CococaAgg backend required PyObjC to be installed!')

from Foundation import *
from AppKit import *
from PyObjCTools import NibClassBuilder, AppHelper
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backend_bases import FigureManagerBase, FigureCanvasBase
from matplotlib.backend_bases import ShowBase
from backend_agg import FigureCanvasAgg
from matplotlib._pylab_helpers import Gcf
mplBundle = NSBundle.bundleWithPath_(os.path.dirname(__file__))

def new_figure_manager(num, *args, **kwargs):
    FigureClass = kwargs.pop('FigureClass', Figure)
    thisFig = FigureClass(*args, **kwargs)
    return new_figure_manager_given_figure(num, thisFig)


def new_figure_manager_given_figure(num, figure):
    """
    Create a new figure manager instance for the given figure.
    """
    canvas = FigureCanvasCocoaAgg(figure)
    return FigureManagerCocoaAgg(canvas, num)


class Show(ShowBase):

    def mainloop(self):
        pass


show = Show()

def draw_if_interactive():
    if matplotlib.is_interactive():
        figManager = Gcf.get_active()
        if figManager is not None:
            figManager.show()
    return


class FigureCanvasCocoaAgg(FigureCanvasAgg):

    def draw(self):
        FigureCanvasAgg.draw(self)

    def blit(self, bbox):
        pass

    def start_event_loop(self, timeout):
        FigureCanvasBase.start_event_loop_default(self, timeout)

    start_event_loop.__doc__ = FigureCanvasBase.start_event_loop_default.__doc__

    def stop_event_loop(self):
        FigureCanvasBase.stop_event_loop_default(self)

    stop_event_loop.__doc__ = FigureCanvasBase.stop_event_loop_default.__doc__


NibClassBuilder.extractClasses('Matplotlib.nib', mplBundle)

class MatplotlibController(NibClassBuilder.AutoBaseClass):

    def awakeFromNib(self):
        NSApp().setDelegate_(self)
        self.app = NSApp()
        self.canvas = Gcf.get_active().canvas
        self.plotView.canvas = self.canvas
        self.canvas.plotView = self.plotView
        self.plotWindow.setAcceptsMouseMovedEvents_(True)
        self.plotWindow.makeKeyAndOrderFront_(self)
        self.plotWindow.setDelegate_(self)
        self.plotView.setImageFrameStyle_(NSImageFrameGroove)
        self.plotView.image_ = NSImage.alloc().initWithSize_((0, 0))
        self.plotView.setImage_(self.plotView.image_)
        self.plotWindow.makeFirstResponder_(self.plotView)
        self.plotView.windowDidResize_(self)

    def windowDidResize_(self, sender):
        self.plotView.windowDidResize_(sender)

    def windowShouldClose_(self, sender):
        self.app.stop_(self)
        return objc.YES

    def saveFigure_(self, sender):
        p = NSSavePanel.savePanel()
        if p.runModal() == NSFileHandlingPanelOKButton:
            self.canvas.print_figure(p.filename())

    def printFigure_(self, sender):
        op = NSPrintOperation.printOperationWithView_(self.plotView)
        op.runOperation()


class PlotWindow(NibClassBuilder.AutoBaseClass):
    pass


class PlotView(NibClassBuilder.AutoBaseClass):

    def updatePlot(self):
        w, h = self.canvas.get_width_height()
        for i in xrange(self.image_.representations().count()):
            self.image_.removeRepresentation_(self.image_.representations().objectAtIndex_(i))

        self.image_.setSize_((w, h))
        brep = NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_((
         self.canvas.buffer_rgba(), '', '', '', ''), w, h, 8, 4, True, False, NSCalibratedRGBColorSpace, w * 4, 32)
        self.image_.addRepresentation_(brep)
        self.setNeedsDisplay_(True)

    def windowDidResize_(self, sender):
        w, h = self.bounds().size
        dpi = self.canvas.figure.dpi
        self.canvas.figure.set_size_inches(w / dpi, h / dpi)
        self.canvas.draw()
        self.updatePlot()

    def mouseDown_(self, event):
        dblclick = event.clickCount() == 2
        loc = self.convertPoint_fromView_(event.locationInWindow(), None)
        type = event.type()
        if type == NSLeftMouseDown:
            button = 1
        else:
            print('Unknown mouse event type:', type, file=sys.stderr)
            button = -1
        self.canvas.button_press_event(loc.x, loc.y, button, dblclick=dblclick)
        self.updatePlot()
        return

    def mouseDragged_(self, event):
        loc = self.convertPoint_fromView_(event.locationInWindow(), None)
        self.canvas.motion_notify_event(loc.x, loc.y)
        self.updatePlot()
        return

    def mouseUp_(self, event):
        loc = self.convertPoint_fromView_(event.locationInWindow(), None)
        type = event.type()
        if type == NSLeftMouseUp:
            button = 1
        else:
            print('Unknown mouse event type:', type, file=sys.stderr)
            button = -1
        self.canvas.button_release_event(loc.x, loc.y, button)
        self.updatePlot()
        return

    def keyDown_(self, event):
        self.canvas.key_press_event(event.characters())
        self.updatePlot()

    def keyUp_(self, event):
        self.canvas.key_release_event(event.characters())
        self.updatePlot()


class MPLBootstrap(NSObject):

    def startWithBundle_(self, bundle):
        if not bundle.loadNibFile_externalNameTable_withZone_('Matplotlib.nib', {}, None):
            print('Unable to load Matplotlib Cocoa UI!', file=sys.stderr)
            sys.exit()
        return


class FigureManagerCocoaAgg(FigureManagerBase):

    def __init__(self, canvas, num):
        FigureManagerBase.__init__(self, canvas, num)
        try:
            WMEnable('Matplotlib')
        except:
            pass

    def show(self):
        self.bootstrap = MPLBootstrap.alloc().init().performSelectorOnMainThread_withObject_waitUntilDone_('startWithBundle:', mplBundle, False)
        NSApplication.sharedApplication().run()


FigureManager = FigureManagerCocoaAgg

def S(*args):
    return ('').join(args)


OSErr = objc._C_SHT
OUTPSN = 'o^{ProcessSerialNumber=LL}'
INPSN = 'n^{ProcessSerialNumber=LL}'
FUNCTIONS = [
 (
  'GetCurrentProcess', S(OSErr, OUTPSN)),
 (
  'SetFrontProcess', S(OSErr, INPSN)),
 (
  'CPSSetProcessName', S(OSErr, INPSN, objc._C_CHARPTR)),
 (
  'CPSEnableForegroundOperation', S(OSErr, INPSN))]

def WMEnable(name='Python'):
    if isinstance(name, unicode):
        name = name.encode('utf8')
    mainBundle = NSBundle.mainBundle()
    bPath = os.path.split(os.path.split(os.path.split(sys.executable)[0])[0])[0]
    if mainBundle.bundlePath() == bPath:
        return True
    else:
        bndl = NSBundle.bundleWithPath_(objc.pathForFramework('/System/Library/Frameworks/ApplicationServices.framework'))
        if bndl is None:
            print('ApplicationServices missing', file=sys.stderr)
            return False
        d = {}
        objc.loadBundleFunctions(bndl, d, FUNCTIONS)
        for fn, sig in FUNCTIONS:
            if fn not in d:
                print('Missing', fn, file=sys.stderr)
                return False

        err, psn = d['GetCurrentProcess']()
        if err:
            print('GetCurrentProcess', (err, psn), file=sys.stderr)
            return False
        err = d['CPSSetProcessName'](psn, name)
        if err:
            print('CPSSetProcessName', (err, psn), file=sys.stderr)
            return False
        err = d['CPSEnableForegroundOperation'](psn)
        if err:
            return False
        err = d['SetFrontProcess'](psn)
        if err:
            print('SetFrontProcess', (err, psn), file=sys.stderr)
            return False
        return True