# Embedded file name: MedidasDeMejora\anadirMedida.pyc
"""
Modulo: anadirMedida.py

Modulo que implementa el interfaz para a\xf1adir nuevas medidas de mejora a un conjunto d medidas
"""
from miChoice import MiChoice
import MedidasDeMejora.definicionInstalaciones as definicionInstalaciones
import MedidasDeMejora.ventanaAislamiento as ventanaAislamiento
import MedidasDeMejora.ventanaHuecos as ventanaHuecos
import MedidasDeMejora.ventanaPT as ventanaPT
import Calculos.listadosWeb as listadosWeb
import wx

def create(parent, panelMM):
    """
    Metodo: create
    
    
    ARGUMENTOS:
                parent:
    """
    return Dialog1(parent, panelMM)


wxID_DIALOG1, wxID_DIALOG1ANADIRMEDIDASTATICTEXT, wxID_ELEMENTOMEJORADOCHOICE, wxID_DIALOGELEMENTOMEJORADOTEXT, wxID_DIALOG1LISTCTRL, wxID_DIALOG1NOMBRESTATICTEXT, wxID_DIALOG1NOMBRETEXTCTRL, wxID_DIALOG1TIPOMEDIDACHOICE, wxID_DIALOG1TIPOMEDIDASTATICTEXT, wxID_PANELCARGARMEDIDADEFECTOBUTTON, wxID_PANELDEFINIRBUTTON = [ wx.NewId() for _init_ctrls in range(11) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo anadirMedida.py
    
    
    """

    def _init_coll_TablaResultados_Columns(self, parent):
        """
        Metodo: _init_coll_TablaResultados_Columns
        
        
        ARGUMENTOS:
                 prnt:
        """
        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_CENTER, heading=_(u'Nombre de la medida'), width=250)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_CENTER, heading=_(u'Elemento mejorado'), width=180)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_CENTER, heading=_(u'Nota caso base mejorado'), width=150)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_CENTER, heading=_(u'Comentarios'), width=180)

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls
        
        
        ARGUMENTOS:
                 prnt:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(20, 20), size=wx.Size(822, 438), style=wx.DEFAULT_DIALOG_STYLE, title=_(u'A\xf1adir una nueva medida de mejora'))
        self.SetClientSize(wx.Size(822, 438))
        self.SetBackgroundColour('white')
        self.anadirMedidaStaticText = wx.StaticText(id=wxID_DIALOG1ANADIRMEDIDASTATICTEXT, label=_(u'A\xf1adir una nueva medida de mejora al conjunto de medidas de mejora'), name=u'anadirMedidaStaticText', parent=self, pos=wx.Point(15, 15), size=wx.Size(700, 16), style=0)
        self.anadirMedidaStaticText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, u''))
        self.anadirMedidaStaticText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.CaracteristicasMedidaLinea = wx.StaticBox(id=-1, label=_(u'Caracter\xedsticas de la medida de mejora'), name=u'PropiedadesLinea', parent=self, pos=wx.Point(15, 45), size=wx.Size(792, 378), style=0)
        self.CaracteristicasMedidaLinea.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasMedidaLinea.SetForegroundColour(wx.Colour(0, 64, 128))
        self.elementoMejoradoText = wx.StaticText(id=wxID_DIALOGELEMENTOMEJORADOTEXT, label=_(u'Elemento mejorado'), name=u'tipoMedidaStaticText', parent=self, pos=wx.Point(30, 70), size=wx.Size(100, 13), style=0)
        self.elementoMejoradoChoice = MiChoice(choices=listadosWeb.listadoOpcionesElementoMejorado, id=wxID_ELEMENTOMEJORADOCHOICE, name=u'tipoMedidaChoice', parent=self, pos=wx.Point(150, 68), size=wx.Size(320, 21), style=0)
        self.elementoMejoradoChoice.SetSelection(0)
        self.elementoMejoradoChoice.Bind(wx.EVT_CHOICE, self.OnMostrarDefinicionMedidasMejora, id=wxID_ELEMENTOMEJORADOCHOICE)
        self.tipoMedidaStaticText = wx.StaticText(id=wxID_DIALOG1TIPOMEDIDASTATICTEXT, label=_(u'Tipo de medida'), name=u'definirStaticText', parent=self, pos=wx.Point(30, 100), size=wx.Size(100, 13), style=0)
        self.tipoMedidaChoice = MiChoice(choices=listadosWeb.listadoOpcionesMedidaMejora, id=wxID_DIALOG1TIPOMEDIDACHOICE, name=u'definirChoice', parent=self, pos=wx.Point(150, 98), size=wx.Size(320, 21), style=0)
        self.tipoMedidaChoice.SetSelection(0)
        self.tipoMedidaChoice.Bind(wx.EVT_CHOICE, self.OnMostrarDefinicionMedidasMejora, id=wxID_DIALOG1TIPOMEDIDACHOICE)
        self.definirButton = wx.Button(id=wxID_PANELDEFINIRBUTTON, label=_(u'Definir'), name=u'DefinirMejoraUsuBoton1', parent=self, pos=wx.Point(480, 100), size=wx.Size(45, 19), style=0)
        self.definirButton.Bind(wx.EVT_BUTTON, self.onDefinirButton, id=wxID_PANELDEFINIRBUTTON)
        self.definirButton.Show(False)
        self.listaMedidas = wx.ListCtrl(id=wxID_DIALOG1LISTCTRL, name=u'listCtrl', parent=self, pos=wx.Point(30, 130), size=wx.Size(762, 240), style=wx.LC_REPORT)
        self.listaMedidas.Enable(True)
        self.listaMedidas.Show(False)
        self._init_coll_TablaResultados_Columns(self.listaMedidas)
        self.CargarMedidaDefectoButton = wx.Button(id=wxID_PANELCARGARMEDIDADEFECTOBUTTON, label=_(u'Cargar medida seleccionada'), name=u'DefinirMedidaMejora1', parent=self, pos=wx.Point(617, 385), size=wx.Size(175, 21), style=0)
        self.CargarMedidaDefectoButton.Bind(wx.EVT_BUTTON, self.OnCargarMedidaDefectoButton, id=wxID_PANELCARGARMEDIDADEFECTOBUTTON)

    def onDefinirButton(self, event):
        """
        Metodo: onDefinirButton
        
        
        ARGUMENTOS:
                 event:
        """
        self.OnMostrarDefinicionMedidasMejora(event)

    def __init__(self, parent, panelMM):
        """
        Constructor de la clase
        
        
        ARGUMENTOS:
                 parent:
        """
        self.parent = parent
        self._init_ctrls(parent)
        self.recalcularMMPorDefecto()
        self.OnMostrarDefinicionMedidasMejora(None)
        self.dev = False
        return

    def recalcularMMPorDefecto(self):
        self.parent.parent.parent.parent.calculoMedidasPorDefecto()

    def OnMostrarDefinicionMedidasMejora(self, event):
        """
        Metodo: OnMostrarDefinicionMedidasMejora
        
        
        ARGUMENTOS:
                 event:
        """
        if self.tipoMedidaChoice.GetSelection() == 0:
            if self.elementoMejoradoChoice.GetSelection() == 0:
                self.cargarMMAislamientoDefecto()
            elif self.elementoMejoradoChoice.GetSelection() == 1:
                self.cargarMMHuecosDefecto()
            elif self.elementoMejoradoChoice.GetSelection() == 2:
                self.cargarMMPTDefecto()
            elif self.elementoMejoradoChoice.GetSelection() == 3:
                self.cargarMMInstalacionesDefecto()
            self.CargarMedidaDefectoButton.Show(True)
            self.listaMedidas.Show(True)
            self.definirButton.Show(False)
        elif self.tipoMedidaChoice.GetSelection() == 1:
            self.CargarMedidaDefectoButton.Show(False)
            self.listaMedidas.Show(False)
            self.definirButton.Show(True)
            if self.elementoMejoradoChoice.GetSelection() == 0:
                self.cargarMMAislamientoUsuario()
            elif self.elementoMejoradoChoice.GetSelection() == 1:
                self.cargarMMHuecosUsuario()
            elif self.elementoMejoradoChoice.GetSelection() == 2:
                self.cargarMMPTUsuario()
            elif self.elementoMejoradoChoice.GetSelection() == 3:
                self.cargarMMInstalacionesUsuario()

    def cargarMMAislamientoDefecto(self):
        """
        Metodo: cargarMMAislamientoDefecto
        
        """
        self.listaMedidas.DeleteAllItems()
        for i in self.parent.parent.parent.parent.listadoConjuntosMMPorDefecto:
            for j in i.mejoras[0]:
                if j[1] == u'Adici\xf3n de Aislamiento T\xe9rmico':
                    self.listaMedidas.Append([j[0], j[1], str(round(i.datosNuevoEdificio.datosResultados.emisionesMostrar, 2)) + '  ' + i.datosNuevoEdificio.datosResultados.emisiones_nota])

        self.listaMedidas.Show(True)
        self.CargarMedidaDefectoButton.Show(True)

    def cargarMMHuecosDefecto(self):
        """
        Metodo: cargarMMHuecosDefecto
        
        """
        self.listaMedidas.DeleteAllItems()
        for i in self.parent.parent.parent.parent.listadoConjuntosMMPorDefecto:
            for j in i.mejoras[0]:
                if j[1] == u'Sustituci\xf3n/mejora de Huecos':
                    self.listaMedidas.Append([j[0], j[1], str(round(i.datosNuevoEdificio.datosResultados.emisionesMostrar, 2)) + '  ' + i.datosNuevoEdificio.datosResultados.emisiones_nota])

        self.listaMedidas.Show(True)
        self.CargarMedidaDefectoButton.Show(True)

    def cargarMMPTDefecto(self):
        """
        Metodo: cargarMMPTDefecto
        
        """
        self.listaMedidas.DeleteAllItems()
        for i in self.parent.parent.parent.parent.listadoConjuntosMMPorDefecto:
            for j in i.mejoras[0]:
                if j[1] == u'Mejora de Puentes T\xe9rmicos':
                    self.listaMedidas.Append([j[0], j[1], str(round(i.datosNuevoEdificio.datosResultados.emisionesMostrar, 2)) + '  ' + i.datosNuevoEdificio.datosResultados.emisiones_nota])

        self.listaMedidas.Show(True)
        self.CargarMedidaDefectoButton.Show(True)

    def cargarMMInstalacionesDefecto(self):
        """
        Metodo: cargarMMInstalacionesDefecto
        
        """
        self.listaMedidas.DeleteAllItems()
        for i in self.parent.parent.parent.parent.listadoConjuntosMMPorDefecto:
            if i.mejoras[1][2] == True:
                self.listaMedidas.Append([i.mejoras[1][0], 'Mejora Instalaciones', str(round(i.datosNuevoEdificio.datosResultados.emisionesMostrar, 2)) + '  ' + i.datosNuevoEdificio.datosResultados.emisiones_nota])

        self.listaMedidas.Show(True)
        self.CargarMedidaDefectoButton.Show(True)

    def cargarMMAislamientoUsuario(self):
        """
        Metodo: cargarMMAislamientoUsuario
        
        """
        self.listaMedidas.Show(False)
        dlg = ventanaAislamiento.create(self.parent)
        dlg.ShowModal()
        if dlg.dev != False:
            self.dev = [dlg.dev, 'usuario']
            self.Close()

    def cargarMMHuecosUsuario(self):
        """
        Metodo: cargarMMHuecosUsuario
        
        """
        self.listaMedidas.Show(False)
        dlg = ventanaHuecos.create(self.parent, self.parent.parent.parent.parent.panelEnvolvente.ventanas)
        dlg.ShowModal()
        if dlg.dev != False:
            self.dev = [dlg.dev, 'usuario']
            self.Close()

    def cargarMMPTUsuario(self):
        """
        Metodo: cargarMMPTUsuario
        
        """
        self.listaMedidas.Show(False)
        dlg = ventanaPT.create(self.parent)
        dlg.ShowModal()
        if dlg.dev != False:
            self.dev = [dlg.dev, 'usuario']
            self.Close()

    def cargarMMInstalacionesUsuario(self):
        """
        Metodo: cargarMMInstalacionesUsuario
        
        """
        self.listaMedidas.Show(False)
        listadoInstalaciones = [self.parent.sistemasACSMM,
         self.parent.sistemasCalefaccionMM,
         self.parent.sistemasRefrigeracionMM,
         self.parent.sistemasClimatizacionMM,
         self.parent.sistemasMixto2MM,
         self.parent.sistemasMixto3MM,
         self.parent.sistemasContribucionesMM,
         self.parent.sistemasIluminacionMM,
         self.parent.sistemasVentilacionMM,
         self.parent.sistemasVentiladoresMM,
         self.parent.sistemasBombasMM,
         self.parent.sistemasTorresRefrigeracionMM]
        dlg = definicionInstalaciones.create(self.parent, listadoInstalaciones)
        dlg.ShowModal()
        if dlg.dev != False:
            self.dev = [dlg.dev, 'usuario']
            self.Close()

    def OnCargarMedidaDefectoButton(self, event):
        """
        Metodo: OnCargarMedidaDefectoButton
        
        """
        seleccionado = self.listaMedidas.GetFocusedItem()
        if seleccionado == -1:
            wx.MessageBox(_(u'Seleccione una medida de la lista'), _(u'Aviso'))
            return
        texto = self.listaMedidas.GetItemText(seleccionado)
        self.dev = [texto, 'defecto']
        self.Close()