# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\PaneltiposCaldera.pyc
# Compiled at: 2014-02-25 15:39:24

class Dialog1(wx.Dialog):

    def __init__(self, parent, inicio):
        self._init_ctrls(parent)
        self.iniciaValores(inicio)

    def iniciaValores(self, inicio):
        self.resultados = []
        for i in inicio:
            self.resultados.append(i)

        self.tipoCalde1Radio= self.resultados[0]
        self.tipoCalde2Radio= self.resultados[1]
        self.tipoCalde3Radio= self.resultados[2]
        self.tipoCalde4Radio= self.resultados[3]
        self.tipoCalde5Radio= self.resultados[4]
        self.menor10MetrosRadio= self.resultados[5]
        self.mayor10MetrosRadio= self.resultados[6]
        self.OnTipoCalderaRadios(None)
        return

    def _init_ctrls(self, prnt):
        self.tipoCalde1Radio = False # or True, era un CheckBox que debia elegir el usuario
        self.tipoCalde2Radio = False # or True, era un CheckBox que debia elegir el usuario
        self.tipoCalde3Radio = False # or True, era un CheckBox que debia elegir el usuario
        self.tipoCalde4Radio = False # or True, era un CheckBox que debia elegir el usuario
        self.tipoCalde5Radio = False # or True, era un CheckBox que debia elegir el usuario
        self.menor10MetrosRadio = False # or True, era un CheckBox que debia elegir el usuario
        self.mayor10MetrosRadio = False # or True, era un CheckBox que debia elegir el usuario

    def OnTipoCalderaRadios(self, event):
        if self.tipoCalde4Radio == True or self.tipoCalde5Radio == True:
        else:

    def OnAceptarButton(self, event):
        self.resultados = []
        self.resultados.append(self.tipoCalde1Radio)
        self.resultados.append(self.tipoCalde2Radio)
        self.resultados.append(self.tipoCalde3Radio)
        self.resultados.append(self.tipoCalde4Radio)
        self.resultados.append(self.tipoCalde5Radio)
        self.resultados.append(self.menor10MetrosRadio)
        self.resultados.append(self.mayor10MetrosRadio)
        self.Close()

    def OnCancelarButton(self, event):
        self.resultados = []
        self.Close()