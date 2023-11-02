# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\dialogoTemperaturas.pyc
# Compiled at: 2014-02-25 15:39:24
"""
Modulo: dialogoTemperaturas.py

"""
import wx

def create(parent, temps):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
                temps:
    """
    return Dialog1(parent, temps)


wxID_DIALOG1, wxID_DIALOG1ACEPTARBOTON, wxID_DIALOG1CANCELARBOTON, wxID_DIALOG1TEMPERATURAMINIMATEXT, wxID_DIALOG1STATICTEXT2, wxID_DIALOG1STATICTEXT3, wxID_DIALOG1TEMPMAX, wxID_DIALOG1TEMPMIN, wxID_DIALOG1TEMPSALIDA, wxID_DIALOG1STATICTEXT4, wxID_DIALOG1STATICTEXT5, wxID_DIALOG1STATICTEXT6, wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICBOX1 = [ wx.NewId() for _init_ctrls in range(14) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo dialogoTemperaturas.py

    """

    def _init_ctrls(self, prnt, temps):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
                temps:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(461, 289), size=wx.Size(307, 218), style=wx.DEFAULT_DIALOG_STYLE, title=_('Definición de Temperaturas'))
        self.SetClientSize(wx.Size(307, 218))
        self.SetBackgroundColour('white')
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=_('Definición de temperaturas'), name='staticText1', parent=self, pos=wx.Point(15, 15), size=wx.Size(350, 20), style=0)
        self.staticText1.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.staticText1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticBox1 = wx.StaticBox(id=wxID_DIALOG1STATICBOX1, label=_('Definir las temperaturas del agua'), name='staticText1', parent=self, pos=wx.Point(15, 45), size=wx.Size(277, 120), style=0)
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticBox1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.tempMinText = wx.StaticText(id=wxID_DIALOG1TEMPERATURAMINIMATEXT, label=_('Temperatura mínima de impulsión'), name='staticText1', parent=self, pos=wx.Point(30, 70), size=wx.Size(158, 13), style=0)
        self.tempMin = wx.TextCtrl(id=wxID_DIALOG1TEMPMIN, name='tempMin', parent=self, pos=wx.Point(206, 68), size=wx.Size(56, 21), style=0, value=str(temps[0]))
        self.staticText6 = wx.StaticText(id=wxID_DIALOG1STATICTEXT6, label=_('ºC'), name='staticText6', parent=self, pos=wx.Point(267, 70), size=wx.Size(15, 13), style=0)
        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2, label=_('Temperatura máxima de impulsión'), name='staticText2', parent=self, pos=wx.Point(30, 100), size=wx.Size(162, 13), style=0)
        self.tempMax = wx.TextCtrl(id=wxID_DIALOG1TEMPMAX, name='tempMax', parent=self, pos=wx.Point(206, 98), size=wx.Size(56, 21), style=0, value=str(temps[1]))
        self.staticText5 = wx.StaticText(id=wxID_DIALOG1STATICTEXT5, label=_('ºC'), name='staticText5', parent=self, pos=wx.Point(267, 100), size=wx.Size(15, 13), style=0)
        self.staticText3 = wx.StaticText(id=wxID_DIALOG1STATICTEXT3, label=_('Temperatura de salida del agua'), name='staticText3', parent=self, pos=wx.Point(30, 130), size=wx.Size(151, 13), style=0)
        self.tempSalida = wx.TextCtrl(id=wxID_DIALOG1TEMPSALIDA, name='tempSalida', parent=self, pos=wx.Point(206, 128), size=wx.Size(56, 21), style=0, value=str(temps[2]))
        self.staticText4 = wx.StaticText(id=wxID_DIALOG1STATICTEXT4, label=_('ºC'), name='staticText4', parent=self, pos=wx.Point(267, 130), size=wx.Size(15, 13), style=0)
        self.aceptarBoton = wx.Button(id=wxID_DIALOG1ACEPTARBOTON, label=_('Aceptar'), name='aceptarBoton', parent=self, pos=wx.Point(15, 180), size=wx.Size(75, 23), style=0)
        self.aceptarBoton.Bind(wx.EVT_BUTTON, self.OnBotonAceptarButton, id=wxID_DIALOG1ACEPTARBOTON)
        self.cancelarBoton = wx.Button(id=wxID_DIALOG1CANCELARBOTON, label=_('Cancelar'), name='cancelarBoton', parent=self, pos=wx.Point(105, 180), size=wx.Size(75, 23), style=0)
        self.cancelarBoton.Bind(wx.EVT_BUTTON, self.OnBotonCancelarButton, id=wxID_DIALOG1CANCELARBOTON)
        self.tempMin.SetToolTip(wx.ToolTip(_('Temperatura mínima de impulsión del agua que acepta el equipo.\nSi se emplea un valor inferior, el consumo energético será el correspondiente\na este temperatura.')))
        self.tempMax.SetToolTip(wx.ToolTip(_('Temperatura máxima de impulsión del agua que acepta el equipo.\nSi se emplea un valor superior, el consumo energético será el correspondiente\na este temperatura.')))
        self.tempSalida.SetToolTip(wx.ToolTip(_('Temperatura de impulsión al agua.')))

    def __init__(self, parent, temps):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
                temps:
        """
        self._init_ctrls(parent, temps)
        self.dev = False

    def OnBotonAceptarButton(self, event):
        """
        Metodo: OnBotonAceptarButton

        ARGUMENTOS:
                event:
        """
        tmpMin = self.tempMin.GetValue()
        tmpMax = self.tempMax.GetValue()
        tmpSal = self.tempSalida.GetValue()
        listaErrores = ''
        if ',' in tmpMin:
            tmpMin = tmpMin.replace(',', '.')
            self.tempMin.SetValue(tmpMin)
        if ',' in tmpMax:
            tmpMax = tmpMax.replace(',', '.')
            self.tempMax.SetValue(tmpMax)
        if ',' in tmpSal:
            tmpSal = tmpSal.replace(',', '.')
            self.tempSalida.SetValue(tmpSal)
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
            listaErrores += _('temperatura mínima')
        if tmpMax == '':
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += _('temperatura máxima')
        if tmpSal == '':
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += _('temperatura de salida')
        if listaErrores != '':
            wx.MessageBox(_('Revise los siguientes campos:\n') + listaErrores + _('.'), _('Aviso'))
            return
        self.dev = [
         float(tmpMin), float(tmpMax), float(tmpSal)]
        self.Close()

    def OnBotonCancelarButton(self, event):
        """
        Metodo: OnBotonCancelarButton

        ARGUMENTOS:
                event:
        """
        self.dev = False
        self.Close()