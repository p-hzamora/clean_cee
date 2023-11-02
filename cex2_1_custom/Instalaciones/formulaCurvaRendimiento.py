# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\formulaCurvaRendimiento.pyc
# Compiled at: 2015-02-05 13:57:25
"""
Modulo: formulaCurvaRendimiento.py

"""
import wx

def create(parent, formula, campos, valores):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
                formula:
                campos:
                valores:
    """
    return Dialog1(parent, formula, campos, valores)


wxID_DIALOG1, wxID_DIALOG1FORMULATEXT, wxID_DIALOG1ACEPTARBOTON, wxID_DIALOG1CANCELARBOTON = [ wx.NewId() for _init_ctrls in range(4) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo formulaCurvaRendimiento.py

    """

    def _init_ctrls(self, prnt, formula, campos, valores):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
                formula:
                campos:
                valores:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(371, 309), size=wx.Size(720, 210), style=wx.DEFAULT_DIALOG_STYLE, title=_('Curva modificadora'))
        self.SetClientSize(wx.Size(720, 210))
        self.SetBackgroundColour('white')
        self.formulaText = wx.StaticText(id=wxID_DIALOG1FORMULATEXT, label=formula, name='formulaText', parent=self, pos=wx.Point(20, 32), size=wx.Size(648, 50), style=0)
        self.formulaText.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        totalCampos = len(campos)
        anchuraTotal = 650
        inicio = 30
        separacion = int(anchuraTotal / totalCampos)
        self.datosFormula = []
        for i in range(len(campos)):
            a = wx.StaticText(id=-1, label=campos[i], name=campos[i], parent=self, pos=wx.Point(inicio + separacion * i + 20, 80), size=wx.Size(20, 13), style=0)
            a.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
            b = wx.TextCtrl(id=-1, name=campos[i], parent=self, pos=wx.Point(inicio + separacion * i, 100), size=wx.Size(50, 21), style=0, value=valores[i])
            self.datosFormula.append(b)

        self.aceptarBoton = wx.Button(id=wxID_DIALOG1ACEPTARBOTON, label=_('Aceptar'), name='aceptarBoton', parent=self, pos=wx.Point(250, 176), size=wx.Size(75, 23), style=0)
        self.aceptarBoton.Bind(wx.EVT_BUTTON, self.OnBotonAceptarButton, id=wxID_DIALOG1ACEPTARBOTON)
        self.cancelarBoton = wx.Button(id=wxID_DIALOG1CANCELARBOTON, label=_('Cancelar'), name='cancelarBoton', parent=self, pos=wx.Point(375, 176), size=wx.Size(75, 23), style=0)
        self.cancelarBoton.Bind(wx.EVT_BUTTON, self.OnBotonCancelarButton, id=wxID_DIALOG1CANCELARBOTON)

    def __init__(self, parent, formula, campos, valores):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
                formula:
                campos:
                valores:
        """
        self._init_ctrls(parent, formula, campos, valores)
        self.campos = campos
        self.dev = False

    def OnBotonAceptarButton(self, event):
        """
        Metodo: OnBotonAceptarButton

        ARGUMENTOS:
                event:
        """
        for i in range(len(self.datosFormula)):
            a = self.datosFormula[i].GetValue()
            if ',' in a:
                a = a.replace(',', '.')
                self.datosFormula[i].SetValue(a)
            try:
                float(a)
            except (ValueError, TypeError):
                a = ''

            if a == '':
                wx.MessageBox(_('Revise los siguientes campos:\n') + self.campos[i] + _('.'), _('Aviso'))
                return

        self.dev = []
        for i in self.datosFormula:
            self.dev.append(i.GetValue())

        self.Close()

    def OnBotonCancelarButton(self, event):
        """
        Metodo: OnBotonCancelarButton

        ARGUMENTOS:
                event:
        """
        self.dev = False
        self.Close()