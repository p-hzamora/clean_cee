# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: pywin\mfc\object.pyc
# Compiled at: 2011-03-19 11:51:18
import sys, win32ui

class Object:

    def __init__(self, initObj=None):
        self.__dict__['_obj_'] = initObj
        if initObj is not None:
            initObj.AttachObject(self)
        return

    def __del__(self):
        self.close()

    def __getattr__(self, attr):
        if not attr.startswith('__'):
            try:
                o = self.__dict__['_obj_']
                if o is not None:
                    return getattr(o, attr)
                if attr[0] != '_' and attr[-1] != '_':
                    raise win32ui.error('The MFC object has died.')
            except KeyError:
                pass

        raise AttributeError(attr)
        return

    def OnAttachedObjectDeath(self):
        self._obj_ = None
        return

    def close(self):
        if '_obj_' in self.__dict__:
            if self._obj_ is not None:
                self._obj_.AttachObject(None)
                self._obj_ = None
        return


class CmdTarget(Object):

    def __init__(self, initObj):
        Object.__init__(self, initObj)

    def HookNotifyRange(self, handler, firstID, lastID):
        oldhandlers = []
        for i in range(firstID, lastID + 1):
            oldhandlers.append(self.HookNotify(handler, i))

        return oldhandlers

    def HookCommandRange(self, handler, firstID, lastID):
        oldhandlers = []
        for i in range(firstID, lastID + 1):
            oldhandlers.append(self.HookCommand(handler, i))

        return oldhandlers

    def HookCommandUpdateRange(self, handler, firstID, lastID):
        oldhandlers = []
        for i in range(firstID, lastID + 1):
            oldhandlers.append(self.HookCommandUpdate(handler, i))

        return oldhandlers