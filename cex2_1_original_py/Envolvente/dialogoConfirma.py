# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\dialogoConfirma.pyc
# Compiled at: 2015-02-10 17:36:18
"""
Modulo: dialogoConfirma.py

"""
import wx

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return Dialog1(parent)


wxID_DIALOG1, wxID_DIALOG1BOTONACEPTAR, wxID_DIALOG1BOTONCANCELAR, wxID_DIALOG1STATICTEXT1 = [ wx.NewId() for _init_ctrls in range(4) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo dialogoConfirma.py

    """

    def _init_ctrls(self, prnt, cad, size):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
                cad:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(475, 379), size=wx.Size(size[0], size[1]), style=wx.DEFAULT_DIALOG_STYLE, title=_('Aviso'))
        self.SetBackgroundColour('white')
        self.botonAceptar = wx.Button(id=wxID_DIALOG1BOTONACEPTAR, label=_('Aceptar'), name='botonAceptar', parent=self, pos=wx.Point(size[0] / 2 - 106, 60), size=wx.Size(80, 23), style=0)
        self.botonAceptar.Bind(wx.EVT_BUTTON, self.OnBotonAceptarButton, id=wxID_DIALOG1BOTONACEPTAR)
        self.botonCancelar = wx.Button(id=wxID_DIALOG1BOTONCANCELAR, label=_('Cancelar'), name='botonCancelar', parent=self, pos=wx.Point(size[0] / 2 + 6, 60), size=wx.Size(80, 23), style=0)
        self.botonCancelar.Bind(wx.EVT_BUTTON, self.OnBotonCancelarButton, id=wxID_DIALOG1BOTONCANCELAR)
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=cad, name='staticText1', parent=self, pos=wx.Point(32, 16), size=wx.Size(size[0] - 64, 40), style=0)
        self.dev = False

    def __init__(self, parent, cad, size=(392, 125)):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
                cad:
        """
        self._init_ctrls(parent, cad, size)

    def OnBotonAceptarButton(self, event):
        """
        Metodo: OnBotonAceptarButton

        ARGUMENTOS:
                event:
        """
        self.dev = True
        self.Close()

    def OnBotonCancelarButton(self, event):
        """
        Metodo: OnBotonCancelarButton

        ARGUMENTOS:
                event:
        """
        self.dev = False
        self.Close()


class Dialog2(wx.Dialog):
    """
    Clase: Dialog1 del modulo dialogoConfirma.py

    """

    def _init_ctrls(self, prnt, cad):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
                cad:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(475, 379), size=wx.Size(400, 118), style=wx.DEFAULT_DIALOG_STYLE, title=_('Aviso'))
        self.SetClientSize(wx.Size(392, 140))
        self.SetBackgroundColour('white')
        self.botonAceptar = wx.Button(id=wxID_DIALOG1BOTONACEPTAR, label=_('Aceptar'), name='botonAceptar', parent=self, pos=wx.Point(104, 100), size=wx.Size(80, 23), style=0)
        self.botonAceptar.Bind(wx.EVT_BUTTON, self.OnBotonAceptarButton, id=wxID_DIALOG1BOTONACEPTAR)
        self.botonCancelar = wx.Button(id=wxID_DIALOG1BOTONCANCELAR, label=_('Cancelar'), name='botonCancelar', parent=self, pos=wx.Point(216, 100), size=wx.Size(80, 23), style=0)
        self.botonCancelar.Bind(wx.EVT_BUTTON, self.OnBotonCancelarButton, id=wxID_DIALOG1BOTONCANCELAR)
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=cad, name='staticText1', parent=self, pos=wx.Point(32, 16), size=wx.Size(336, 60), style=0)
        self.dev = False

    def __init__(self, parent, cad):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
                cad:
        """
        self._init_ctrls(parent, cad)

    def OnBotonAceptarButton(self, event):
        """
        Metodo: OnBotonAceptarButton

        ARGUMENTOS:
                event:
        """
        self.dev = True
        self.Close()

    def OnBotonCancelarButton(self, event):
        """
        Metodo: OnBotonCancelarButton

        ARGUMENTOS:
                event:
        """
        self.dev = False
        self.Close()