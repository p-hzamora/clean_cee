# Embedded file name: AnalisisEconomico\panelBotonesAnalisis.pyc
"""
Modulo: panelBotonesAnalisis.py
M\xf3dulo que implementa la funcionalidad de los botones que se muestran en el panelAnalisisEconomicos
"""
import wx
import dialogoConfirma
wxID_PANEL1, wxID_PANEL1ANADIRBOTON, wxID_PANEL1BORRARBOTON, wxID_PANEL1MODIFICARBOTON, wxID_PANEL1VISTACLASICABOT, wxID_PANEL1VISTANORMALBOT = [ wx.NewId() for _init_ctrls in range(6) ]

class panelBotones(wx.Panel):
    """
    Clase: panelBotones del modulo panelBotonesAnalisis.py
    Clase que hereda de wxPanel y le a\xf1ade la funcionalidad necesaria para manejar los botones del panelAnalisisEconomico
    
    """

    def _init_ctrls(self, prnt, ide, posi, siz, styl, nam):
        """
        Metodo: _init_ctrls
        
        
        ARGUMENTOS:
                prnt: Instancia de panelAnalisisEconomico
                ide: Identificador num\xe9rico (entero)
                posi: Posici\xf3n que ocupa en notaci\xf3n x,y (enteros)
                siz: Tama\xf1o en notaci\xf3n (x,y) (enteros)
                styl: Estilo (wx.Panle styles)
                nam: string con nombre del panel
        """
        wx.Panel.__init__(self, id=ide, name=nam, parent=prnt, pos=posi, size=siz, style=styl)
        self.SetBackgroundColour('white')
        self.anadirBoton = wx.Button(id=wxID_PANEL1ANADIRBOTON, label=_(u'A\xf1adir'), name=u'anadirBoton', parent=self, pos=wx.Point(0, 0), size=wx.Size(75, 23), style=0)
        self.anadirBoton.Bind(wx.EVT_BUTTON, self.OnAnadirBotonButton, id=wxID_PANEL1ANADIRBOTON)
        self.anadirBoton.SetForegroundColour(wx.Colour(0, 64, 128))
        self.anadirBoton.SetBackgroundColour('white')
        self.modificarBoton = wx.Button(id=wxID_PANEL1MODIFICARBOTON, label=_(u'Modificar'), name=u'modificarBoton', parent=self, pos=wx.Point(90, 0), size=wx.Size(75, 23), style=0)
        self.modificarBoton.Bind(wx.EVT_BUTTON, self.OnmodificarBoton, id=wxID_PANEL1MODIFICARBOTON)
        self.modificarBoton.SetForegroundColour(wx.Colour(0, 64, 128))
        self.modificarBoton.SetBackgroundColour('white')
        self.borrarBoton = wx.Button(id=wxID_PANEL1BORRARBOTON, label=_(u'Borrar'), name=u'borrarBoton', parent=self, pos=wx.Point(225, 0), size=wx.Size(75, 23), style=0)
        self.borrarBoton.Bind(wx.EVT_BUTTON, self.OnBorrarBotonButton, id=wxID_PANEL1BORRARBOTON)
        self.borrarBoton.SetForegroundColour(wx.Colour(0, 64, 128))
        self.borrarBoton.SetBackgroundColour('white')

    def compruebaNombres(self, nombre):
        """
        Metodo: compruebaNombres
        Funci\xf3n que comprueba si existe o no un nombre de factura
        Si no existe devuelve 'elemento no encontrado', en caso contrario los datos de la factura
        
        ARGUMENTOS:
                nombre:
        """
        for i in range(len(self.parent.objetosFactura)):
            if nombre == self.parent.objetosFactura[i][0]:
                return i

        return 'elemento no encontrado'

    def OnAnadirBotonButton(self, event):
        """
        Metodo: OnAnadirBotonButton
        Manejador del evento de que el usuario haga click en AnadirBoton
        
        ARGUMENTOS:
                event: Instancia de la clase manejadora del evento
        """
        objeto = self.parent.panelFacturas.cogerDatos()
        if type(objeto) == type(u'hola'):
            wx.MessageBox(_(u'No ha definido ') + objeto + _(u'.'), _(u'Aviso'))
            return
        if self.compruebaNombres(self.parent.panelFacturas.descripcionFactura.GetValue()) == 'elemento no encontrado':
            self.parent.objetosFactura.append(objeto)
            self.parent.cargaArbol()
        else:
            wx.MessageBox(_(u'El nombre de la factura ya existe.'), _(u'Aviso'))
            return

    def OnmodificarBoton(self, event):
        """
        Metodo: OnAnadirBotonButton
        Manejador del evento de que el usuario haga click en modificarBoton
        
        ARGUMENTOS:
                event: Instancia de la clase manejadora del evento
        """
        try:
            item = self.parent.arbolMejoras.GetItemText(self.parent.arbolMejoras.GetSelection())
        except:
            wx.MessageBox(_(u'Debe seleccionar el elemento del arbol que desea modificar.'), _(u'Aviso'))
            return

        root = self.parent.arbolMejoras.GetSelection()
        if root == self.parent.arbolMejoras.GetRootItem():
            wx.MessageBox(_(u'No se puede modificar la ra\xedz del \xe1rbol.'), _(u'Aviso'))
            return
        nuevo = self.parent.panelFacturas.cogerDatos()
        if type(nuevo) == type(u'hola'):
            wx.MessageBox(_(u'No ha definido ') + nuevo + _(u'.'), _(u'Aviso'))
            return
        for i in range(len(self.parent.objetosFactura)):
            if item == self.parent.objetosFactura[i][0]:
                self.parent.objetosFactura[i] = nuevo
                break

        self.parent.cargaArbol()

    def OnBorrarBotonButton(self, event):
        """
        Metodo: OnAnadirBotonButton
        Manejador del evento de que el usuario haga click en BorrarBoton
        
        ARGUMENTOS:
                event: Instancia de la clase manejadora del evento
        """
        try:
            item = self.parent.arbolMejoras.GetItemText(self.parent.arbolMejoras.GetSelection())
        except:
            wx.MessageBox(_(u'Debe seleccionar el elemento del arbol que desea borrar.'), _(u'Aviso'))
            return

        root = self.parent.arbolMejoras.GetSelection()
        if root == self.parent.arbolMejoras.GetRootItem():
            wx.MessageBox(_(u'No se puede borrar la ra\xedz del \xe1rbol.'), _(u'Aviso'))
            return
        borrar = dialogoConfirma.Dialog1(self, _(u'\xbfDesea borrar el elemento "') + item + '"?')
        borrar.ShowModal()
        if borrar.dev == False:
            return
        for i in range(len(self.parent.objetosFactura)):
            if item == self.parent.objetosFactura[i][0]:
                self.parent.objetosFactura.pop(i)
                break

        self.parent.cargaArbol()

    def __init__(self, parent, id, pos, size, style, name):
        """
        Constructor de la clase
        
        
        ARGUMENTOS:
                parent: instancia del panel al que pertenece
                id: identificador num\xe9rico (entero)
                pos: posicion que ocupa en coordenadas x,y (enteros)
                size: tama\xf1o en notaci\xf3n x,y (enteros)
                style: estilo(wx.grid.Grid styles)
                name: string con el nombre del panel
        """
        self.parent = parent
        self._init_ctrls(parent, id, pos, size, style, name)