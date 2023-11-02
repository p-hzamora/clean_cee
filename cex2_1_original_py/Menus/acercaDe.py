# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Menus\acercaDe.pyc
# Compiled at: 2015-02-17 17:58:12
"""
Modulo: acercaDE.py

"""
import wx, webbrowser, directorios
Directorio = directorios.BuscaDirectorios().Directorio
from Calculos.listados import versionCEX
from BeautifulSoup import BeautifulSoup
wxID_DIALOG1, wxID_PANEL2ACEPTARBOTON, wxID_TEXTOTEXT = [ wx.NewId() for _init_ctrls in range(3) ]

def create(parent):
    """
    Metodo: create
    """
    return Dialog1(parent)


class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo acercaDe.py

    """

    def _init_ctrls(self, parent):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                parent:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=parent, pos=wx.Point(475, 40), size=wx.Size(645, 653), style=wx.DEFAULT_DIALOG_STYLE, title=_('Acerca del procedimiento CE³X'))
        self.SetClientSize(wx.Size(645, 473))
        self.SetBackgroundColour('white')
        imageCenerFile = Directorio + '\\Imagenes\\cenerLogo.jpg'
        imageCener = wx.Image(imageCenerFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imagenCener = wx.BitmapButton(id=-1, bitmap=imageCener, parent=self, pos=wx.Point(15, 15), size=wx.Size(300, 80), style=wx.BU_AUTODRAW)
        self.imagenCener.Bind(wx.EVT_BUTTON, self.logoCenerClick)
        imageEfinovaFile = Directorio + '\\Imagenes\\efinovatic_310x81.jpg'
        imageEfinova = wx.Image(imageEfinovaFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imagenEfinova = wx.BitmapButton(id=-1, bitmap=imageEfinova, parent=self, pos=wx.Point(320, 15), size=wx.Size(310, 81), style=wx.BU_AUTODRAW)
        self.imagenEfinova.Bind(wx.EVT_BUTTON, self.logoEfinovaClick)
        texto = '\nCE³X v.%s\n\nEl desarrollo del procedimiento CE³X de certificación energética de edificios existentes fue adjudicado mediante concurso público abierto, organizado por el Instituto para la Diversificación y Ahorro de la Energía, al equipo de trabajo dirigido por:\n\n    ▘  Miguel Ángel Pascual Buisán como director del proyecto (Efinovatic)\n    ▘  Inés Díaz Regodón como responsable de arquitectura (CENER)\n    ▘  Edurne Zubiri Azqueta como responsable de ingeniería (Efinovatic)\n\n\nEl equipo de trabajo también ha estado formado por:\n    Centro Nacional de Energías Renovables- CENER. Departamento de Energética Edificatoria\n      •  Florencio Manteca González\n      •  María Fernández Boneta\n      •  Marta Sampedro Bores\n      •  Segio Díaz de Garayo\n      •  Francisco Serna Lumbreras\n      •  Javier Llorente Yoldi\n\n' % versionCEX
        self.textoText = wx.StaticText(id=wxID_TEXTOTEXT, label=texto, name='textoText', parent=self, pos=wx.Point(15, 110), size=wx.Size(630, 320), style=0)
        self.textoText.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, ''))
        self.textoText.SetSize(wx.Size(630, 320))
        self.aceptarBoton = wx.Button(id=wxID_PANEL2ACEPTARBOTON, label=_('Aceptar'), name='aceptarBoton', parent=self, pos=wx.Point(15, 440), size=wx.Size(125, 23), style=0)
        self.aceptarBoton.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Verdana'))
        self.aceptarBoton.Bind(wx.EVT_BUTTON, self.OnAceptarBoton, id=wxID_PANEL2ACEPTARBOTON)

    def __init__(self, parent):
        """
        Constructor de la clase
        """
        self._init_ctrls(parent)

    def OnAceptarBoton(self, event):
        """
        Metodo: OnAceptarBoton
        """
        self.Close()

    def logoCenerClick(self, event):
        webbrowser.open_new('http://www.cener.com')

    def logoEfinovaClick(self, event):
        webbrowser.open_new('http://www.efinovatic.es')