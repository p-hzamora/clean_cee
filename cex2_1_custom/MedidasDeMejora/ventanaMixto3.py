# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: MedidasDeMejora\ventanaMixto3.pyc
# Compiled at: 2015-02-17 10:45:59
"""
Modulo: ventanaMixto3.py

"""
import wx
from Instalaciones.panelMixto3 import Panel1

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return Dialog1(parent)


wxID_DIALOG1, wxID_DIALOG1ACEPTARBOTON, wxID_DIALOG1AISLANTERADIO, wxID_DIALOG1CANCELARBOTON, wxID_DIALOG1CERRAMIENTOSMEJORADOSTEXT, wxID_DIALOG1CHOICE1, wxID_DIALOG1CUBIERTACHECK, wxID_DIALOG1DESCRIPCION, wxID_DIALOG1DESCRIPCIONTEXT, wxID_DIALOG1ESPESORAISLANTE, wxID_DIALOG1ESPESORTEXT, wxID_DIALOG1ESPESORUNIDADESTEXT, wxID_DIALOG1FACHADACHECK, wxID_DIALOG1LANDAAISLANTE, wxID_DIALOG1LANDAAISLANTETEXT, wxID_DIALOG1LANDAAISLANTEUNIDADES, wxID_DIALOG1LIBRERIARADIO, wxID_DIALOG1NUEVATRANSMITEXT, wxID_DIALOG1SUELOCHECK, wxID_DIALOG1TITULOTEXT, wxID_DIALOG1URADIO, wxID_DIALOG1VALORU, wxID_DIALOG1VALURUNIDADESTEXT, wxID_DIALOG1TITULOTEXT = [ wx.NewId() for _init_ctrls in range(24) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo ventanaMixto3.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(0, 0), size=wx.Size(770, 443), style=wx.DEFAULT_DIALOG_STYLE, title=_('Cuadro incluir mejoras en ACS, Calefacción y Refrigeración'))
        self.SetClientSize(wx.Size(770, 443))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tituloText = wx.StaticText(id=wxID_DIALOG1TITULOTEXT, label=_('Medida de mejora en la instalación de calefacción, refrigeración y ACS'), name='tituloText', parent=self, pos=wx.Point(15, 15), size=wx.Size(270, 18), style=0)
        self.tituloText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.tituloText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.panel = Panel1(parent=self, id=-1, pos=wx.Point(15, 40), size=wx.Size(770, 350), style=wx.TAB_TRAVERSAL, name='panelMixto3', real_parent=prnt.parent.parent.parent.parent.panelInstalaciones)
        self.aceptarBoton = wx.Button(id=wxID_DIALOG1ACEPTARBOTON, label=_('Aceptar'), name='aceptarBoton', parent=self, pos=wx.Point(15, 405), size=wx.Size(75, 23), style=0)
        self.aceptarBoton.Bind(wx.EVT_BUTTON, self.onAceptarBoton, id=wxID_DIALOG1ACEPTARBOTON)
        self.cancelarBoton = wx.Button(id=wxID_DIALOG1CANCELARBOTON, label=_('Cancelar'), name='cancelarBoton', parent=self, pos=wx.Point(105, 405), size=wx.Size(75, 23), style=0)
        self.cancelarBoton.Bind(wx.EVT_BUTTON, self.onCancelarBoton, id=wxID_DIALOG1CANCELARBOTON)

    def __init__(self, parent):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
        """
        self._init_ctrls(parent)
        self.dev = False

    def onAceptarBoton(self, event):
        """
        Metodo: onAceptarBoton

        ARGUMENTOS:
                event:
        """
        self.dev = self.panel.parent.cogerDatosDelPanel(self.panel)
        if type(self.dev) == type('hola'):
            wx.MessageBox(_('Revise los siguientes campos:\n') + self.dev, _('Aviso'))
            return
        self.dev[1] = 'mixto3'
        self.Close()

    def onCancelarBoton(self, event):
        """
        Metodo: onCancelarBoton

        ARGUMENTOS:
                event:
        """
        self.dev = False
        self.Close()