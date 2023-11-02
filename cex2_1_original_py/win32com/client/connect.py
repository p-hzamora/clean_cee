# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: win32com\client\connect.pyc
# Compiled at: 2011-03-19 11:51:20
"""Utilities for working with Connections"""
import win32com.server.util, pythoncom

class SimpleConnection:
    """A simple, single connection object"""

    def __init__(self, coInstance=None, eventInstance=None, eventCLSID=None, debug=0):
        self.cp = None
        self.cookie = None
        self.debug = debug
        if coInstance is not None:
            self.Connect(coInstance, eventInstance, eventCLSID)
        return

    def __del__(self):
        try:
            self.Disconnect()
        except pythoncom.error:
            pass

    def _wrap(self, obj):
        useDispatcher = None
        if self.debug:
            from win32com.server import dispatcher
            useDispatcher = dispatcher.DefaultDebugDispatcher
        return win32com.server.util.wrap(obj, useDispatcher=useDispatcher)

    def Connect(self, coInstance, eventInstance, eventCLSID=None):
        try:
            oleobj = coInstance._oleobj_
        except AttributeError:
            oleobj = coInstance

        cpc = oleobj.QueryInterface(pythoncom.IID_IConnectionPointContainer)
        if eventCLSID is None:
            eventCLSID = eventInstance.CLSID
        comEventInstance = self._wrap(eventInstance)
        self.cp = cpc.FindConnectionPoint(eventCLSID)
        self.cookie = self.cp.Advise(comEventInstance)
        return

    def Disconnect(self):
        if self.cp is not None:
            if self.cookie:
                self.cp.Unadvise(self.cookie)
                self.cookie = None
            self.cp = None
        return