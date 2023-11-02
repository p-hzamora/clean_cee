# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\dialogoCurva.pyc
# Compiled at: 2014-02-25 15:39:24
from Instalaciones.comprobarCampos import Comprueba

def create(parent):
    return Dialog1(parent)



class Dialog1(wx.Dialog):

    def _init_ctrls(self, prnt, a, b, c, d):
        self.c1 = a
        self.c2 = b
        self.c3 = c
        self.c4 = d
        self.dev = False

    def __init__(self, parent, a, b, c, d):
        self._init_ctrls(parent, a, b, c, d)

    def OnBotonAceptarButton(self, event):
        dato = self.c1
        if ',' in dato:
            self.c1= dato.replace(',', '.')
        dato = self.c2
        if ',' in dato:
            self.c2= dato.replace(',', '.')
        dato = self.c3
        if ',' in dato:
            self.c3= dato.replace(',', '.')
        dato = self.c4
        if ',' in dato:
            self.c4= dato.replace(',', '.')
        listaErrores = ''
        listaErrores += Comprueba(self.c1, 2, listaErrores, 'C1').ErrorDevuelto
        listaErrores += Comprueba(self.c2, 2, listaErrores, 'C2').ErrorDevuelto
        listaErrores += Comprueba(self.c3, 2, listaErrores, 'C3').ErrorDevuelto
        listaErrores += Comprueba(self.c4, 2, listaErrores, 'C4').ErrorDevuelto
        if listaErrores == '':
            self.dev = True
            self.Close()
        else:
            raise Exception('Revise los siguientes campos:\n' + listaErrores)

    def OnBotonCancelarButton(self, event):
        self.dev = False
        self.Close()