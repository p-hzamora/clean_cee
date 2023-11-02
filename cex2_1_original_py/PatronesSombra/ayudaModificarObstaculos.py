# Embedded file name: PatronesSombra\ayudaModificarObstaculos.pyc
"""
Modulo: ayudaModificarObstaculos.py


Modulo de ayuda ppara la confirmaci\xf3n de modificaci\xf3n de obst\xe1culos remostos
"""
import wx

def create(parent):
    """
    Metodo: create
    devuelve instancia de la clase Dialog1
    
    ARGUMENTOS:
                parent:
    
    
    """
    return Dialog1(parent)


wxID_DIALOG1, wxID_DIALOG1ACEPTAR, wxID_DIALOG1CANCELAR, wxID_DIALOG1STATICTEXT1 = [ wx.NewId() for _init_ctrls in range(4) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo ayudaModificarObstaculos.py
    
    Ventana de confirmaci\xf3n de modificaci\xf3n de los patrones de sombras
    """

    def _init_ctrls(self, prnt, mensaje, mensaje1):
        """
        Metodo: _init_ctrls
        Iniciaci\xf3n de elementos gr\xe1ficos (llamado desde el constructor)
        
        ARGUMENTOS:
                prnt:
                mensaje:
                mensaje1:
        
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(428, 302), size=wx.Size(367, 165), style=wx.DEFAULT_DIALOG_STYLE, title=_(u'\xbfDesea modificar el patr\xf3n de sombras?'))
        self.SetClientSize(wx.Size(359, 131))
        self.SetBackgroundColour('white')
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=mensaje1 + mensaje + u'\n\xbfDesea continuar con la modificaci\xf3n?', name='staticText1', parent=self, pos=wx.Point(24, 25), size=wx.Size(300, 50), style=0)
        self.aceptar = wx.Button(id=wxID_DIALOG1ACEPTAR, label=_(u'Continuar'), name=u'aceptar', parent=self, pos=wx.Point(80, 90), size=wx.Size(75, 23), style=0)
        self.aceptar.Bind(wx.EVT_BUTTON, self.OnAceptarButton, id=wxID_DIALOG1ACEPTAR)
        self.cancelar = wx.Button(id=wxID_DIALOG1CANCELAR, label=_(u'Cancelar'), name=u'cancelar', parent=self, pos=wx.Point(194, 90), size=wx.Size(75, 23), style=0)
        self.cancelar.Bind(wx.EVT_BUTTON, self.OnCancelarButton, id=wxID_DIALOG1CANCELAR)

    def __init__(self, parent, mensaje, mensaje1):
        """
        Constructor de la clase
        
        
        ARGUMENTOS:
                parent:
                mensaje:
                mensaje1:
        """
        self._init_ctrls(parent, mensaje, mensaje1)
        self.dev = False

    def OnAceptarButton(self, event):
        """
        Metodo: OnAceptarButton
        Manejador del evento de presionar el bot\xf3n Aceptar
        
        ARGUMENTOS:
                event:
        
        
        """
        self.dev = True
        self.Close()

    def OnCancelarButton(self, event):
        """
        Metodo: OnCancelarButton
        Manejador del evento de presionar el bot\xf3n Cancelar
        
        
        ARGUMENTOS:
                event:
        """
        self.dev = False
        self.Close()