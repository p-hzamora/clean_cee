# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\formulaCurvaRendimiento.pyc
# Compiled at: 2015-02-05 13:57:25

def create(parent, formula, campos, valores):
    return Dialog1(parent, formula, campos, valores)



class Dialog1(wx.Dialog):

    def _init_ctrls(self, prnt, formula, campos, valores):
        totalCampos = len(campos)
        anchuraTotal = 650
        inicio = 30
        separacion = int(anchuraTotal / totalCampos)
        self.datosFormula = []
        for i in range(len(campos)):
            b = valores[i]
            self.datosFormula.append(b)


    def __init__(self, parent, formula, campos, valores):
        self._init_ctrls(parent, formula, campos, valores)
        self.campos = campos
        self.dev = False

    def OnBotonAceptarButton(self, event):
        for i in range(len(self.datosFormula)):
            a = self.datosFormula[i]
            if ',' in a:
                a = a.replace(',', '.')
                self.datosFormula[i]= a
            try:
                float(a)
            except (ValueError, TypeError):
                a = ''

            if a == '':
                raise Exception('Revise los siguientes campos:\n' + self.campos[i] + '.')
                return

        self.dev = []
        for i in self.datosFormula:
            self.dev.append(i)

        self.Close()

    def OnBotonCancelarButton(self, event):
        self.dev = False
        self.Close()