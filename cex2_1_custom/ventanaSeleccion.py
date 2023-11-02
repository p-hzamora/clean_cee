# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: ventanaSeleccion.pyc
# Compiled at: 2014-02-25 15:39:24
"""
Modulo: ventanaSeleccion.py

"""
import wx, sys, idioma
idioma.ini()
import directorios
Directorio = directorios.BuscaDirectorios().Directorio

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return Dialog1(parent)


wxID_DIALOG1, wxID_DIALOG1BUTTON1, wxID_DIALOG1BUTTON2, wxID_DIALOG1BUTTON3, wxID_PANEL1IMAGEN1, wxID_PANEL1IMAGEN2, wxID_PANEL1IMAGEN3, wxID_PANEL1DEFINIR, wxID_CARACTERISTICASLINEATEXT = [ wx.NewId() for _init_ctrls in range(9) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo ventanaSeleccion.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
        """
        x, y = wx.GetDisplaySize()
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point((x - 450) / 2, (y - 300) / 2), size=wx.Size(490, 300), style=wx.BORDER_DOUBLE, title='CE3X')
        self.SetClientSize(wx.Size(490, 300))
        self.SetBackgroundColour('white')
        _icon = wx.Icon(Directorio + '/Imagenes/logoCex.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(_icon)
        self.defiirText = wx.StaticText(id=wxID_PANEL1DEFINIR, label=_('Certificación energética simplificada de edificios existentes'), name='defiirText', parent=self, pos=wx.Point(15, 50), size=wx.Size(475, 18), style=0)
        self.defiirText.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.defiirText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.CaracteristicasLineaText = wx.StaticBox(id=wxID_CARACTERISTICASLINEATEXT, label=_('Tipo de edificio'), name='CaracteristicasLineaText', parent=self, pos=wx.Point(15, 120), size=wx.Size(460, 150), style=0)
        self.CaracteristicasLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.button1 = wx.Button(id=wxID_DIALOG1BUTTON1, label=_('Residencial'), name='button1', parent=self, pos=wx.Point(70, 175), size=wx.Size(75, 45), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button, id=wxID_DIALOG1BUTTON1)
        self.button1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.button1.SetBackgroundColour('white')
        self.button2 = wx.Button(id=wxID_DIALOG1BUTTON2, label=_('Pequeño\nterciario'), name='button2', parent=self, pos=wx.Point(200, 175), size=wx.Size(75, 45), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button, id=wxID_DIALOG1BUTTON2)
        self.button2.SetForegroundColour(wx.Colour(0, 64, 128))
        self.button2.SetBackgroundColour('white')
        self.button3 = wx.Button(id=wxID_DIALOG1BUTTON3, label=_('Gran\nterciario'), name='button3', parent=self, pos=wx.Point(330, 175), size=wx.Size(75, 45), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button, id=wxID_DIALOG1BUTTON3)
        self.button3.SetForegroundColour(wx.Colour(0, 64, 128))
        self.button3.SetBackgroundColour('white')

    def __init__(self, parent):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
        """
        self._init_ctrls(parent)
        self.dev = None
        return

    def OnButton1Button(self, event):
        """
        Metodo: OnButton1Button

        ARGUMENTOS:
                event:
        """
        self.dev = 'residencial'
        self.Close()

    def OnButton2Button(self, event):
        """
        Metodo: OnButton2Button

        ARGUMENTOS:
                event:
        """
        self.dev = 'PT'
        self.Close()

    def OnButton3Button(self, event):
        """
        Metodo: OnButton3Button

        ARGUMENTOS:
                event:
        """
        self.dev = 'GT'
        self.Close()