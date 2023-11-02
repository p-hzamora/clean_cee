# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: pywin\mfc\thread.pyc
# Compiled at: 2011-03-19 11:51:18
import object, win32ui

class WinThread(object.CmdTarget):

    def __init__(self, initObj=None):
        if initObj is None:
            initObj = win32ui.CreateThread()
        object.CmdTarget.__init__(self, initObj)
        return

    def InitInstance(self):
        pass

    def ExitInstance(self):
        pass


class WinApp(WinThread):

    def __init__(self, initApp=None):
        if initApp is None:
            initApp = win32ui.GetApp()
        WinThread.__init__(self, initApp)
        return