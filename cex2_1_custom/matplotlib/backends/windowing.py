# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\backends\windowing.pyc
# Compiled at: 2012-10-30 18:11:14
"""
MS Windows-specific helper for TkAgg and FltkAgg backends.

With rcParams['tk.window_focus'] default of False, it is
effectively disabled.

It uses a tiny C++ extension module to access MS Win functions.
"""
from __future__ import print_function
from matplotlib import rcParams
try:
    if not rcParams['tk.window_focus']:
        raise ImportError
    from matplotlib._windowing import GetForegroundWindow, SetForegroundWindow
except ImportError:

    def GetForegroundWindow():
        return 0


    def SetForegroundWindow(hwnd):
        pass


class FocusManager:

    def __init__(self):
        self._shellWindow = GetForegroundWindow()

    def __del__(self):
        SetForegroundWindow(self._shellWindow)