# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\dialogoCurva.pyc
# Compiled at: 2014-02-25 15:39:24
"""
Modulo: dialogoCurva.py

"""
import wx
from Instalaciones.comprobarCampos import Comprueba

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return Dialog1(parent)


wxID_DIALOG1, wxID_DIALOG1BOTONACEPTAR, wxID_DIALOG1BOTONCANCELAR, wxID_VENTILADORC1, wxID_VENTILADORC2, wxID_VENTILADORC3, wxID_VENTILADORC4, wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICBOX1 = [ wx.NewId() for _init_ctrls in range(9) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo dialogoCurva.py

    """

    def _init_ctrls(self, prnt, a, b, c, d):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
                a:
                b:
                c:
                d:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(475, 379), size=wx.Size(320, 178), style=wx.DEFAULT_DIALOG_STYLE, title=_('Definir curva de consumo del equipo'))
        self.SetClientSize(wx.Size(320, 178))
        self.SetBackgroundColour('white')
        self.coeficientesText = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=_('Curva de consumo del equipo'), name='coeficientesText', parent=self, pos=wx.Point(15, 15), size=wx.Size(64, 13), style=0)
        self.coeficientesText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.coeficientesText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticBox1 = wx.StaticBox(id=wxID_DIALOG1STATICBOX1, label=_('Definir coefientes de la curva'), name='staticText1', parent=self, pos=wx.Point(15, 45), size=wx.Size(290, 80), style=0)
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticBox1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.c1Text = wx.StaticText(id=-1, label=_('C1'), name='c1Text', parent=self, pos=wx.Point(45, 70), size=wx.Size(14, 13), style=0)
        self.c2Text = wx.StaticText(id=-1, label=_('C2'), name='c2Text', parent=self, pos=wx.Point(115, 70), size=wx.Size(14, 13), style=0)
        self.c3Text = wx.StaticText(id=-1, label=_('C3'), name='c3Text', parent=self, pos=wx.Point(185, 70), size=wx.Size(14, 13), style=0)
        self.c4Text = wx.StaticText(id=-1, label=_('C4'), name='c4Text', parent=self, pos=wx.Point(255, 70), size=wx.Size(14, 13), style=0)
        self.c1 = wx.TextCtrl(id=wxID_VENTILADORC1, name='c1', parent=self, pos=wx.Point(30, 90), size=wx.Size(50, 21), style=0, value=a)
        self.c2 = wx.TextCtrl(id=wxID_VENTILADORC2, name='c2', parent=self, pos=wx.Point(100, 90), size=wx.Size(50, 21), style=0, value=b)
        self.c3 = wx.TextCtrl(id=wxID_VENTILADORC3, name='c3', parent=self, pos=wx.Point(170, 90), size=wx.Size(50, 21), style=0, value=c)
        self.c4 = wx.TextCtrl(id=wxID_VENTILADORC4, name='c4', parent=self, pos=wx.Point(240, 90), size=wx.Size(50, 21), style=0, value=d)
        self.botonAceptar = wx.Button(id=wxID_DIALOG1BOTONACEPTAR, label=_('Aceptar'), name='botonAceptar', parent=self, pos=wx.Point(15, 140), size=wx.Size(75, 23), style=0)
        self.botonAceptar.Bind(wx.EVT_BUTTON, self.OnBotonAceptarButton, id=wxID_DIALOG1BOTONACEPTAR)
        self.botonCancelar = wx.Button(id=wxID_DIALOG1BOTONCANCELAR, label=_('Cancelar'), name='botonCancelar', parent=self, pos=wx.Point(105, 140), size=wx.Size(75, 23), style=0)
        self.botonCancelar.Bind(wx.EVT_BUTTON, self.OnBotonCancelarButton, id=wxID_DIALOG1BOTONCANCELAR)
        self.dev = False

    def __init__(self, parent, a, b, c, d):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
                a:
                b:
                c:
                d:
        """
        self._init_ctrls(parent, a, b, c, d)

    def OnBotonAceptarButton(self, event):
        """
        Metodo: OnBotonAceptarButton

        ARGUMENTOS:
                event:
        """
        dato = self.c1.GetValue()
        if ',' in dato:
            self.c1.SetValue(dato.replace(',', '.'))
        dato = self.c2.GetValue()
        if ',' in dato:
            self.c2.SetValue(dato.replace(',', '.'))
        dato = self.c3.GetValue()
        if ',' in dato:
            self.c3.SetValue(dato.replace(',', '.'))
        dato = self.c4.GetValue()
        if ',' in dato:
            self.c4.SetValue(dato.replace(',', '.'))
        listaErrores = ''
        listaErrores += Comprueba(self.c1.GetValue(), 2, listaErrores, 'C1').ErrorDevuelto
        listaErrores += Comprueba(self.c2.GetValue(), 2, listaErrores, 'C2').ErrorDevuelto
        listaErrores += Comprueba(self.c3.GetValue(), 2, listaErrores, 'C3').ErrorDevuelto
        listaErrores += Comprueba(self.c4.GetValue(), 2, listaErrores, 'C4').ErrorDevuelto
        if listaErrores == '':
            self.dev = True
            self.Close()
        else:
            wx.MessageBox(_('Revise los siguientes campos:\n') + listaErrores, _('Aviso'))

    def OnBotonCancelarButton(self, event):
        """
        Metodo: OnBotonCancelarButton

        ARGUMENTOS:
                event:
        """
        self.dev = False
        self.Close()