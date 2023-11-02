# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\dialogoConfirma.pyc
# Compiled at: 2015-02-06 07:49:55

def create(parent):
    return Dialog1(parent)



class Dialog1(wx.Dialog):

    def _init_ctrls(self, prnt, cad, size):
        self.dev = False

    def __init__(self, parent, cad, size=(392, 125)):
        self._init_ctrls(parent, cad, size)

    def OnBotonAceptarButton(self, event):
        self.dev = True
        self.Close()

    def OnBotonCancelarButton(self, event):
        self.dev = False
        self.Close()