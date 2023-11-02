# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: tkCommonDialog.pyc
# Compiled at: 2011-03-08 09:43:16
from Tkinter import *

class Dialog:
    command = None

    def __init__(self, master=None, **options):
        if TkVersion < 4.2:
            raise TclError, 'this module requires Tk 4.2 or newer'
        self.master = master
        self.options = options
        if not master and options.get('parent'):
            self.master = options['parent']

    def _fixoptions(self):
        pass

    def _fixresult(self, widget, result):
        return result

    def show(self, **options):
        for k, v in options.items():
            self.options[k] = v

        self._fixoptions()
        w = Frame(self.master)
        try:
            s = w.tk.call(self.command, *w._options(self.options))
            s = self._fixresult(w, s)
        finally:
            try:
                w.destroy()
            except:
                pass

        return s