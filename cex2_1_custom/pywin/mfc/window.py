# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: pywin\mfc\window.pyc
# Compiled at: 2011-03-19 11:51:18
import object, win32ui, win32con

class Wnd(object.CmdTarget):

    def __init__(self, initobj=None):
        object.CmdTarget.__init__(self, initobj)
        if self._obj_:
            self._obj_.HookMessage(self.OnDestroy, win32con.WM_DESTROY)

    def OnDestroy(self, msg):
        pass


class FrameWnd(Wnd):

    def __init__(self, wnd):
        Wnd.__init__(self, wnd)


class MDIChildWnd(FrameWnd):

    def __init__(self, wnd=None):
        if wnd is None:
            wnd = win32ui.CreateMDIChild()
        FrameWnd.__init__(self, wnd)
        return

    def OnCreateClient(self, cp, context):
        if context is not None and context.template is not None:
            context.template.CreateView(self, context)
        return


class MDIFrameWnd(FrameWnd):

    def __init__(self, wnd=None):
        if wnd is None:
            wnd = win32ui.CreateMDIFrame()
        FrameWnd.__init__(self, wnd)
        return