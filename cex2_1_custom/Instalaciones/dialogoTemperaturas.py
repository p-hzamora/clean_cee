# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\dialogoTemperaturas.pyc
# Compiled at: 2014-02-25 15:39:24

def create(parent, temps):
    return Dialog1(parent, temps)



class Dialog1(wx.Dialog):

    def _init_ctrls(self, prnt, temps):
        self.tempMin = str(temps[0])
        self.tempMax = str(temps[1])
        self.tempSalida = str(temps[2])
        self.tempMin.SetToolTip(wx.ToolTip('Temperatura mínima de impulsión del agua que acepta el equipo.\nSi se emplea un valor inferior, el consumo energético será el correspondiente\na este temperatura.'))
        self.tempMax.SetToolTip(wx.ToolTip('Temperatura máxima de impulsión del agua que acepta el equipo.\nSi se emplea un valor superior, el consumo energético será el correspondiente\na este temperatura.'))
        self.tempSalida.SetToolTip(wx.ToolTip('Temperatura de impulsión al agua.'))

    def __init__(self, parent, temps):
        self._init_ctrls(parent, temps)
        self.dev = False

    def OnBotonAceptarButton(self, event):
        tmpMin = self.tempMin
        tmpMax = self.tempMax
        tmpSal = self.tempSalida
        listaErrores = ''
        if ',' in tmpMin:
            tmpMin = tmpMin.replace(',', '.')
            self.tempMin= tmpMin
        if ',' in tmpMax:
            tmpMax = tmpMax.replace(',', '.')
            self.tempMax= tmpMax
        if ',' in tmpSal:
            tmpSal = tmpSal.replace(',', '.')
            self.tempSalida= tmpSal
        try:
            float(tmpMin)
            if float(tmpMin) < 0:
                tmpMin = ''
        except (ValueError, TypeError):
            tmpMin = ''

        try:
            float(tmpMax)
            if float(tmpMax) < 0:
                tmpMax = ''
        except (ValueError, TypeError):
            tmpMax = ''

        try:
            float(tmpSal)
            if float(tmpSal) < 0:
                tmpSal = ''
        except (ValueError, TypeError):
            tmpSal = ''

        if tmpMin == '':
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'temperatura mínima'
        if tmpMax == '':
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'temperatura máxima'
        if tmpSal == '':
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'temperatura de salida'
        if listaErrores != '':
            raise Exception('Revise los siguientes campos:\n' + listaErrores + '.')
            return
        self.dev = [
         float(tmpMin), float(tmpMax), float(tmpSal)]
        self.Close()

    def OnBotonCancelarButton(self, event):
        self.dev = False
        self.Close()