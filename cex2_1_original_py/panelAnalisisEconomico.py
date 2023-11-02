# Embedded file name: panelAnalisisEconomico.pyc
"""
Modulo: panelAnalisisEconomico.py

"""
import wx
import AnalisisEconomico.panelResultadoAnalisis as panelResultadoAnalisis
import AnalisisEconomico.panelFacturas as panelFacturas
import AnalisisEconomico.panelDatosEconomicos as panelDatosEconomicos
import AnalisisEconomico.panelCosteMedidas as panelCosteMedidas
from AnalisisEconomico.panelBotonesAnalisis import panelBotones
wxID_PANEL1, wxID_PANEL1ARBOLMEJORAS, wxID_PANEL1NOTEBOOK1, wxID_PANEL1TREECTRL1, wxID_WXPANEL6CERRAR, wxID_PANELANALISISECONOMICOCERRARBUTTON = [ wx.NewId() for _init_ctrls in range(6) ]

class Panel1(wx.Panel):
    """
    Clase: Panel1 del modulo panelAnalisisEconomico.py
    
    
    """

    def _init_coll_notebook1_Pages(self, parent):
        """
        Metodo: _init_coll_notebook1_Pages
        
        
        ARGUMENTOS:
                parent:
        """
        parent.AddPage(page=self.panelFacturas, select=True, text=_(u'Facturas'), imageId=-1)
        parent.AddPage(page=self.panelDatosEconomicos, select=False, text=_(u'Datos econ\xf3micos'), imageId=-1)
        parent.AddPage(page=self.panelCosteMedidas, select=False, text=_(u'Coste de las medidas'), imageId=-1)
        parent.AddPage(page=self.panelResultado, select=False, text=_(u'Resultado'), imageId=-1)

    def _init_ctrls(self, prnt, id_prnt, pos_prnt, size_prnt, style_prnt, name_prnt):
        """
        Metodo: _init_ctrls
        
        
        ARGUMENTOS:
                prnt:
                id_prnt:
                pos_prnt:
                size_prnt:
                style_prnt:
                name_prnt:
        """
        wx.Panel.__init__(self, id=id_prnt, name=name_prnt, parent=prnt, pos=pos_prnt, size=size_prnt, style=style_prnt)
        self.SetBackgroundColour('white')
        self.arbolMejoras = wx.TreeCtrl(id=wxID_PANEL1TREECTRL1, name='treeCtrl1', parent=self, pos=wx.Point(0, 8), size=wx.Size(216, 584), style=wx.TR_HAS_BUTTONS)
        self.arbolMejoras.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnArbolMejoras, id=wxID_PANEL1TREECTRL1)
        self.panelBotones = panelBotones(id=-1, name='panelBotones', parent=self, pos=wx.Point(230, 600), size=wx.Size(600, 100), style=wx.TAB_TRAVERSAL)
        self.CerrarButton = wx.Button(id=wxID_PANELANALISISECONOMICOCERRARBUTTON, label=_(u'Cerrar'), name=u'CerrarButton', parent=self, pos=wx.Point(860, 600), size=wx.Size(80, 23), style=0)
        self.CerrarButton.Bind(wx.EVT_BUTTON, self.OnCerrarButton, id=wxID_PANELANALISISECONOMICOCERRARBUTTON)
        self.CerrarButton.SetBackgroundColour(wx.Color(240, 240, 240))
        self.notebook1 = wx.Notebook(id=wxID_PANEL1NOTEBOOK1, name='notebook1', parent=self, pos=wx.Point(230, 0), size=wx.Size(740, 593), style=0)
        self.notebook1.Show(False)
        self.panelFacturas = panelFacturas.Panel1(parent=self.notebook1, id=-1, pos=wx.Point(0, 8), size=wx.Size(720, 593), style=0, name='', real_parent=self)
        self.panelDatosEconomicos = panelDatosEconomicos.Panel1(parent=self.notebook1, id=-1, pos=wx.Point(0, 8), size=wx.Size(720, 593), style=0, name='', real_parent=self)
        self.panelCosteMedidas = panelCosteMedidas.Panel1(parent=self.notebook1, id=-1, pos=wx.Point(0, 8), size=wx.Size(720, 593), style=0, name='', real_parent=self)
        self.panelResultado = panelResultadoAnalisis.Panel1(parent=self.notebook1, id=-1, pos=wx.Point(0, 8), size=wx.Size(720, 593), style=0, name='', real_parent=self)
        self._init_coll_notebook1_Pages(self.notebook1)

    def OnArbolMejoras(self, event):
        """
        Metodo: OnArbolMejoras
        
        
        ARGUMENTOS:
                event:
        """
        if self.notebook1.GetSelection() == 0:
            nombre = self.arbolMejoras.GetItemText(self.arbolMejoras.GetSelection())
            for i in self.objetosFactura:
                if nombre == i[0]:
                    self.panelFacturas.cargarDatos(i)
                    break

    def cogerDatos(self):
        """
        Metodo: cogerDatos
        
        
        
        """
        datos = []
        datos.append(self.objetosFactura)
        datos.append(self.panelDatosEconomicos.cogerDatos())
        datos.append(self.panelCosteMedidas.cogerDatos())
        datos.append(self.panelResultado.cogerDatos())
        return datos

    def cargarDatos(self, datos):
        """
        Metodo: cargarDatos
        
        
        ARGUMENTOS:
                datos:
        """
        self.objetosFactura = []
        for i in datos[0]:
            self.objetosFactura.append(i)

        datosInicializarFacturas = ['',
         '',
         '',
         '',
         '',
         [['', False],
          ['', False],
          ['', False],
          ['', False],
          ['', False],
          ['', False],
          ['', False],
          ['', False]]]
        self.panelFacturas.cargarDatos(datos=datosInicializarFacturas)
        self.cargaArbol()
        self.panelDatosEconomicos.cargarDatos(datos[1])
        self.panelCosteMedidas.cargarDatos(datos[2])
        self.panelResultado.incluirConjuntosMedidas()
        self.notebook1.SetSelection(0)

    def __init__(self, parent, id, pos, size, style, name):
        """
        Constructor de la clase
        
        
        ARGUMENTOS:
                parent:
                id:
                pos:
                size:
                style:
                name:
        """
        self.parent = parent
        self._init_ctrls(parent, id, pos, size, style, name)
        self.nombre = _(u'An\xe1lisis econ\xf3mico')
        self.notebook1.Show(True)
        self.objetosFactura = []
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.onNotebookChanged)

    def onNotebookChanged(self, event):
        """
        Metodo: onNotebookChanged
        
        
        ARGUMENTOS:
                event:
        """
        if self.notebook1.GetSelection() == 0:
            self.cargaArbol()
            self.panelBotones.anadirBoton.Show(True)
            self.panelBotones.modificarBoton.Show(True)
            self.panelBotones.borrarBoton.Show(True)
        elif self.notebook1.GetSelection() == 1:
            self.cargaArbol()
            self.panelBotones.anadirBoton.Show(False)
            self.panelBotones.modificarBoton.Show(False)
            self.panelBotones.borrarBoton.Show(False)
        elif self.notebook1.GetSelection() == 2:
            self.parent.parent.panelMedidasMejora.cargarArbol(self.arbolMejoras)
            self.panelBotones.anadirBoton.Show(False)
            self.panelBotones.modificarBoton.Show(False)
            self.panelBotones.borrarBoton.Show(False)
        elif self.notebook1.GetSelection() == 3:
            self.parent.parent.panelMedidasMejora.cargarArbol(self.arbolMejoras)
            self.panelBotones.anadirBoton.Show(False)
            self.panelBotones.modificarBoton.Show(False)
            self.panelBotones.borrarBoton.Show(False)
            self.OnRecalcularAnalisisEconomico()

    def OnRecalcularAnalisisEconomico(self):
        """
        Al pinchar en la pesta\xf1a de resultados, revisa si es necesario recalcular el an\xe1lisis econ\xf3mico.
        Si ha hecho cambios en el caso base o en las medidas de mejora, ya estar\xe1n recalculados. 
        S\xf3lo har\xeda calculo econ\xf3mico 
        """
        self.parent.parent.calculoAnalisisEconomico()

    def cargaArbol(self):
        """
        Metodo: cargaArbol
        
        
                self):    ####Cargo arbol de Factur:
        """
        self.arbolMejoras.DeleteAllItems()
        root = self.arbolMejoras.AddRoot(_(u'Facturas'))
        self.arbolMejoras.SetItemTextColour(root, 'black')
        self.arbolMejoras.SetItemBold(root)
        for i in self.objetosFactura:
            self.arbolMejoras.AppendItem(root, i[0])

        self.arbolMejoras.Expand(root)

    def OnCerrarButton(self, event):
        """
        Metodo: OnCerrarButton
        
        
        ARGUMENTOS:
                event:
        """
        items = self.parent.parent.menuCalificar.GetMenuItems()
        items[2].Enable(True)
        self.parent.parent.botonEconomico11.Enable(True)
        identificador = self.GetId()
        for i in range(len(self.parent.parent.paneles)):
            if self.parent.parent.paneles[i].GetId() == identificador:
                self.parent.parent.paneles.pop(i)
                break

        pagina = self.parent.GetSelection()
        self.parent.RemovePage(pagina)
        self.parent.parent.panelAnalisisEconomico.Show(False)