# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Menus\asistenciaIdae.pyc
# Compiled at: 2014-02-18 15:21:03
"""
Modulo: asistenciaIdae.py

"""
import wx, webbrowser
wxID_DIALOG1, wxID_PANEL2ACEPTARBOTON, wxID_TEXTO1TEXT, wxID_TEXTO2TEXT, wxID_FRAME1MASINFOTEXT = [ wx.NewId() for _init_ctrls in range(5) ]

def create(parent):
    """
    Metodo: create
    """
    return Dialog1(parent)


class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo asistenciaIdae.py

    """

    def _init_ctrls(self, parent):
        """
        Metodo: _init_ctrls
        
        ARGUMENTOS:
                parent:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=parent, pos=wx.Point(475, 40), size=wx.Size(500, 326), style=wx.DEFAULT_DIALOG_STYLE, title=_('Asistencia técnica y consultas'))
        self.SetClientSize(wx.Size(500, 326))
        self.SetBackgroundColour('white')
        self.texto1Text = wx.StaticText(id=wxID_TEXTO1TEXT, label='Servicio de Información al Ciudadano en Eficiencia Energética y Energías Renovables (SICER)', name='texto1Text', parent=self, pos=wx.Point(15, 15), size=wx.Size(470, 40), style=0)
        self.texto1Text.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.texto1Text.SetForegroundColour(wx.Colour(0, 64, 128))
        self.texto1Text.SetSize(wx.Size(470, 40))
        texto = 'Para cualquier consulta relativa al procedimiento CE³X, su uso, estructura de la herramienta, estructura del fichero generado u otros temas relacionados, puede dirigirse al Servicio de Información al Ciudadano en Eficiencia Energética y Energías Renovables (SICER):\n\n    ▘  Correo electrónico: ciudadano@idae.es\n    ▘  Teléfono: 913 14 66 73 (10 a 14 h de lunes a viernes)\n    ▘  Fax: 91 523 04 14\n    ▘  Correo postal: Instituto para la Diversificación y Ahorro de la Energía \n                             Calle Madera 8, 28004-Madrid'
        self.texto2Text = wx.StaticText(id=wxID_TEXTO2TEXT, label=texto, name='texto2Text', parent=self, pos=wx.Point(15, 80), size=wx.Size(630, 175), style=0)
        self.texto2Text.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, ''))
        self.texto2Text.SetSize(wx.Size(470, 175))
        self.masInfo = wx.StaticText(id=wxID_FRAME1MASINFOTEXT, label=_('+ info'), name='uVidrioText', parent=self, pos=wx.Point(435, 270), size=wx.Size(50, 13), style=0)
        self.masInfo.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, True, ''))
        self.masInfo.SetForegroundColour(wx.Colour(0, 64, 128))
        self.masInfo.Bind(wx.EVT_LEFT_DOWN, self.OnMasInfo)
        self.aceptarBoton = wx.Button(id=wxID_PANEL2ACEPTARBOTON, label=_('Aceptar'), name='aceptarBoton', parent=self, pos=wx.Point(15, 298), size=wx.Size(125, 23), style=0)
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

    def OnMasInfo(self, event):
        webbrowser.open_new('http://www.idae.es/index.php/relcategoria./mod.global/mem.formEnvioInfo')