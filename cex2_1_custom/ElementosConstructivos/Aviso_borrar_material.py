# Embedded file name: ElementosConstructivos\Aviso_borrar_material.pyc
"""
Modulo: Aviso_borrar_material.py
Implementa el cuadro de dialogo que se muestra cuando el usuario bora o modifica un material
"""
import wx

def create(parent, num):
    """
    Metodo: create
    Devuelve una instancia de la clase Aviso_borrar_material
    
    ARGUMENTOS:
                parent: Instancia de panelBotonesAnalisis
                num: entero que elige el mensaje a mostrar
    """
    return Aviso_borrar_material(parent, num)


wxID_AVISO_BORRAR_MATERIAL, wxID_AVISO_BORRAR_MATERIALBOTON_ACEPTAR, wxID_AVISO_BORRAR_MATERIALBOTON_CANCELAR, wxID_AVISO_BORRAR_MATERIALSTATICTEXT1 = [ wx.NewId() for _init_ctrls in range(4) ]

class Aviso_borrar_material(wx.Dialog):
    """
    Clase: Aviso_borrar_material del modulo Aviso_borrar_material.py
    Clase que implementa el cuadro de dialogo que se muestra al usuario cuando intenta borrar o modificar
    materiales de la base de datos del sistema
    
    """

    def _init_ctrls(self, prnt, num):
        """
        Metodo: _init_ctrls
        Inicia los componenetes gr\xe1ficos del Cuadro de di\xe1logo (llamado desde el constructor)
        
        ARGUMENTOS:
                prnt: Instancia de panelBotonoesAnalisis
                num: Enteros que determina el mensaje a mostrar
        """
        mensaje = []
        mensaje.append('\xbfDesea borrar el elemento seleccionado?')
        mensaje.append('\xbfDesea borrar el grupo  seleccionado?')
        mensaje.append('\xbfDesea modificar el elemento seleccionado?')
        wx.Dialog.__init__(self, id=wxID_AVISO_BORRAR_MATERIAL, name=u'Aviso_borrar_material', parent=prnt, pos=wx.Point(475, 379), size=wx.Size(300, 100), style=wx.DEFAULT_DIALOG_STYLE, title=_(u'Aviso'))
        self.SetBackgroundColour('white')
        self.SetClientSize(wx.Size(300, 100))
        self.Bind(wx.EVT_CLOSE, self.OnAviso_borrar_materialClose)
        self.boton_aceptar = wx.Button(id=wxID_AVISO_BORRAR_MATERIALBOTON_ACEPTAR, label=_(u'Acceptar'), name=u'boton_aceptar', parent=self, pos=wx.Point(50, 60), size=wx.Size(90, 23), style=0)
        self.boton_aceptar.Bind(wx.EVT_BUTTON, self.OnBoton_aceptarButton, id=wxID_AVISO_BORRAR_MATERIALBOTON_ACEPTAR)
        self.boton_cancelar = wx.Button(id=wxID_AVISO_BORRAR_MATERIALBOTON_CANCELAR, label=_(u'Cancelar'), name=u'boton_cancelar', parent=self, pos=wx.Point(160, 60), size=wx.Size(90, 23), style=0)
        self.boton_cancelar.Bind(wx.EVT_BUTTON, self.OnBoton_cancelarButton, id=wxID_AVISO_BORRAR_MATERIALBOTON_CANCELAR)
        self.staticText1 = wx.StaticText(id=wxID_AVISO_BORRAR_MATERIALSTATICTEXT1, label=mensaje[num], name='staticText1', parent=self, pos=wx.Point(30, 20), size=wx.Size(250, 13), style=0)

    def __init__(self, parent, num):
        """
        Constructor de la clase
        
        
        ARGUMENTOS:
                parent: instancia de panelBotonesAnalisis
                num: entero que determina el mensaje a mostrar
                    0 -> \xbfDesea borrar el elemento seleccionado?
                    1 -> \xbfDesea borrar el grupo  seleccionado?
                    2 -> \xbfDesea modificar el elemento seleccionado?
        """
        self._init_ctrls(parent, num)
        self.borrar = False

    def OnBoton_aceptarButton(self, event):
        """
        Metodo: OnBoton_aceptarButton
        Manejador del evento de que el usuario haga click en Boton_aceptar
        Devuelve True
        ARGUMENTOS:
                event: Instancia de la clase manejadora del evento
        """
        self.Close()
        self.borrar = True
        return self.borrar

    def OnBoton_cancelarButton(self, event):
        """
        Manejador del evento de que el usuario haga click en Boton_cancelar
        Devuelve False
        ARGUMENTOS:
                event: Instancia de la clase manejadora del evento
        """
        self.Close()
        self.borrar = False
        return self.borrar

    def OnAviso_borrar_materialClose(self, event):
        """
        Metodo: OnAviso_borrar_materialClose
        Manejador del evento de que el usuario haga click en Boton_borrar
        Devuelve False
        ARGUMENTOS:
                event: Instancia de la clase manejadora del evento
        """
        self.Destroy()
        self.borrar = False
        return self.borrar