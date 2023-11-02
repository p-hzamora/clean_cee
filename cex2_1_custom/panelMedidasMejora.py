# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: panelMedidasMejora.pyc
# Compiled at: 2015-02-19 13:18:34
"""
Modulo: panelMedidasMejora.py

"""
from Calculos.funcionesCalculo import calculoContribucionSolarMinimaEdificioReferencia, compararDosConjuntosObjEdificio
from .Calculos.limitesCTEyEdifRef import *
from MedidasDeMejora.medidasMejoraDefecto import getMedidasPorDefecto
from MedidasDeMejora.objetoGrupoMejoras import mejoraEdificioCompleto
from MedidasDeMejora.panelCompararMejora import panelCompararMejora, panelCompararMejoraTerciario
from MedidasDeMejora.panelDefinirMedidasMejora import panelDefinirMedidasMejora
import Envolvente.tablasValores as tablasValores, MedidasDeMejora.panelBotonesMedidas as panelBotonesMedidas, copy, datosEdificio, directorios, sys, wx, logging
Directorio = directorios.BuscaDirectorios().Directorio
sys.path.append(Directorio)
wxID_PANELARBOLMEJORAS, wxID_PANELARBOLMEJORASARBOL, wxID_PANELARBOLMEJORASCOMPARARMEJORASBUTTON, wxID_PANELARBOLMEJORASDEFINIRMEJORASBUTTON, wxID_PANELARBOLMEJORASPANELVACIO, wxID_PANELARBOLMEJORASCERRARBUTTON, wxID_PANELARBOLMEJORASCARGAEDIFICIOSBUTTON = [ wx.NewId() for _init_ctrls in range(7) ]

class panelMedidasMejora(wx.Panel):
    """
    Clase: panelMedidasMejora del modulo panelMedidasMejora.py

    """

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
        self.nombre = _('Medidas de mejora')
        self._init_ctrls(parent, id, pos, size, style, name)
        self.calificacionCasoBase = []
        self.elementosArbol = []

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
        self.Arbol = wx.TreeCtrl(id=wxID_PANELARBOLMEJORASARBOL, name='Arbol', parent=self, pos=wx.Point(0, 8), size=wx.Size(216, 584), style=wx.TR_HAS_BUTTONS)
        self.Arbol.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnArbolSeleccionarItem, id=wxID_PANELARBOLMEJORASARBOL)
        self.DefinirMejorasButton = wx.BitmapButton(bitmap=wx.Bitmap(Directorio + '/Imagenes/nuevoConjuntoMejoras.ico', wx.BITMAP_TYPE_ANY), id=wxID_PANELARBOLMEJORASDEFINIRMEJORASBUTTON, name='definirConjunto', parent=self, pos=wx.Point(0, 600), size=wx.Size(23, 23), style=wx.BU_AUTODRAW)
        self.DefinirMejorasButton.Bind(wx.EVT_BUTTON, self.OnDefinirMejorasButton, id=wxID_PANELARBOLMEJORASDEFINIRMEJORASBUTTON)
        self.CompararMejorasButton = wx.BitmapButton(bitmap=wx.Bitmap(Directorio + '/Imagenes/compararConjuntosMM.ico', wx.BITMAP_TYPE_ANY), id=wxID_PANELARBOLMEJORASCOMPARARMEJORASBUTTON, name='comparaMedidas', parent=self, pos=wx.Point(30, 600), size=wx.Size(23, 23), style=wx.BU_AUTODRAW)
        self.CompararMejorasButton.Bind(wx.EVT_BUTTON, self.OnCompararMejorasButton, id=wxID_PANELARBOLMEJORASCOMPARARMEJORASBUTTON)
        self.cargaEdificioButton = wx.BitmapButton(bitmap=wx.Bitmap(Directorio + '/Imagenes/cargarEdificioMejorado.ico', wx.BITMAP_TYPE_ANY), id=wxID_PANELARBOLMEJORASCARGAEDIFICIOSBUTTON, name='cargaEdificio', parent=self, pos=wx.Point(60, 600), size=wx.Size(23, 23), style=wx.BU_AUTODRAW)
        self.cargaEdificioButton.Bind(wx.EVT_BUTTON, self.OnCargaEdificioButton, id=wxID_PANELARBOLMEJORASCARGAEDIFICIOSBUTTON)
        self.CerrarButton = wx.Button(id=wxID_PANELARBOLMEJORASCERRARBUTTON, label=_('Cerrar'), name='CerrarButton', parent=self, pos=wx.Point(860, 600), size=wx.Size(80, 23), style=0)
        self.CerrarButton.Bind(wx.EVT_BUTTON, self.OnCerrarButton, id=wxID_PANELARBOLMEJORASCERRARBUTTON)
        self.CerrarButton.SetBackgroundColour(wx.Color(240, 240, 240))
        self.panelBotones = panelBotonesMedidas.panelBotones(id=-1, name='panelBotones', parent=self, pos=wx.Point(230, 600), size=wx.Size(650, 100), style=wx.TAB_TRAVERSAL)

    def OnCargaEdificioButton(self, event):
        """
        Metodo: OnCargaEdificioButton

        ARGUMENTOS:
                event:
        """
        dlg = wx.FileDialog(self, 'Seleccione un archivo', 'Ejemplos/', '', '*.cex', wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath().split('\\')[-1]
            conjuntoEdificioCompletoMejorado = mejoraEdificioCompleto(fileName=dlg.GetPath(), datosEdificioOriginal=self.parent.parent.objEdificio)
            aux = conjuntoEdificioCompletoMejorado.calificacion()
            if type(aux) is unicode:
                wx.MessageBox(aux, _('Aviso'))
                return
            if conjuntoEdificioCompletoMejorado.datosNuevoEdificio.casoValido == False:
                wx.MessageBox(_('El edificio mejorado no puede ser cargado. Revise sus propiedades en el fichero de origen.'), _('Aviso'))
                return
            self.parent.parent.listadoConjuntosMMUsuario.append(conjuntoEdificioCompletoMejorado)
            self.cargarArbol(self.Arbol)
            self.parent.parent.panelAnalisisEconomico.panelCosteMedidas.incluirMedidas()
            self.parent.parent.panelAnalisisEconomico.panelResultado.incluirConjuntosMedidas()
            self.parent.parent.panelAnalisisEconomico.onNotebookChanged(None)
            self.PanelVacio.Destroy()
            self.PanelVacio = panelDefinirMedidasMejora(parent=self, pos=wx.Point(230, 8), size=wx.Size(770, 584), style=wx.TAB_TRAVERSAL, name='PanelVacio', id=-1, conjuntoMM=conjuntoEdificioCompletoMejorado)
            self.PanelVacio.DescripcionCuadro.Enable(False)
            self.panelBotones.modificarBoton.Show(True)
            self.panelBotones.borrarBoton.Show(True)
        return

    def obtenerNombreConjunto(self):
        """
        Metodo: obtenerNombreConjunto

        """
        nombres = []
        for i in self.parent.parent.listadoConjuntosMMUsuario:
            nombres.append(i.nombre)

        cont = 1
        nom = 'Nuevo Conjunto '
        while 1:
            nombre = nom + str(cont)
            if nombre not in nombres:
                break
            else:
                cont = cont + 1

        return nombre

    def expandidosEnArbol(self, arbol):
        """
        Metodo: expandidosEnArbol

        ARGUMENTOS:
                arbol:
        """
        elem = []
        for i in self.elementosArbol:
            if arbol.IsExpanded(i):
                elem.append(arbol.GetItemText(i))

        return elem

    def expandirAnteriores(self, elementos, arbol):
        """
        Metodo: expandirAnteriores

        ARGUMENTOS:
                elementos:
                arbol:
        """
        for i in elementos:
            for j in self.elementosArbol:
                if i == arbol.GetItemText(j):
                    arbol.Expand(j)
                    break

    def cargarArbol(self, arbol):
        """
        Metodo: cargarArbol

        ARGUMENTOS:
                arbol):    ###Funcion que carga el contenido de las listas de medidas en el Arb:
        """
        elementosExpandidos = self.expandidosEnArbol(arbol)
        arbol.DeleteAllItems()
        self.elementosArbol = []
        valores_usuario = arbol.AddRoot(_('Conjuntos de medidas definidos'))
        arbol.SetItemTextColour(valores_usuario, wx.Colour(0, 64, 128))
        arbol.SetItemBold(valores_usuario)
        for i in self.parent.parent.listadoConjuntosMMUsuario:
            item = arbol.AppendItem(valores_usuario, i.nombre)
            self.elementosArbol.append(item)
            arbol.SetItemTextColour(item, 'black')
            if type(i.mejoras) == type('edificio completo'):
                sub_item = arbol.AppendItem(item, 'Nuevo Edificio Completo')
                arbol.SetItemTextColour(sub_item, 'black')
            else:
                if i.mejoras[1][2] == True:
                    sub_item = arbol.AppendItem(item, 'Nuevas Instalaciones')
                    arbol.SetItemTextColour(sub_item, 'black')
                for sub_i in i.mejoras[0]:
                    sub_item = arbol.AppendItem(item, sub_i[0])
                    arbol.SetItemTextColour(sub_item, 'black')

        arbol.Expand(valores_usuario)
        self.expandirAnteriores(elementosExpandidos, arbol)

    def OnArbolSeleccionarItem(self, event):
        """
        Metodo: OnArbolSeleccionarItem

        ARGUMENTOS:
                 event:
        """
        ItemSeleccionado = self.Arbol.GetSelection()
        ItemSeleccionado = self.Arbol.GetItemText(ItemSeleccionado)
        if ItemSeleccionado == _('Conjuntos de medidas definidos'):
            self.PanelVacio.Destroy()
            if self.parent.parent.programa == 'Residencial':
                self.PanelVacio = panelCompararMejora(parent=self, pos=wx.Point(230, 8), size=wx.Size(770, 584), style=wx.TAB_TRAVERSAL, name='PanelVacio', id=-1)
                self.PanelVacio.CargarDatos()
            else:
                self.PanelVacio = panelCompararMejoraTerciario(parent=self, pos=wx.Point(230, 8), size=wx.Size(770, 584), style=wx.TAB_TRAVERSAL, name='PanelVacio', id=-1)
                self.PanelVacio.CargarDatos()
            self.panelBotones.guardarBoton.Show(False)
            self.panelBotones.modificarBoton.Show(False)
            self.panelBotones.borrarBoton.Show(False)
        else:
            itempadre = self.Arbol.GetItemParent(self.Arbol.GetSelection())
            itempadre = self.Arbol.GetItemText(itempadre)
            if itempadre == _('Conjuntos de medidas definidos'):
                self.PanelVacio.Destroy()
                conjuntoSeleccionado = self.obtenerConjuntoSeleccionado(ItemSeleccionado)
                self.PanelVacio = panelDefinirMedidasMejora(parent=self, pos=wx.Point(230, 8), size=wx.Size(770, 584), style=wx.TAB_TRAVERSAL, name='PanelVacio', id=-1, conjuntoMM=conjuntoSeleccionado)
            else:
                abuelo = self.Arbol.GetItemParent(self.Arbol.GetItemParent(self.Arbol.GetSelection()))
                abuelo = self.Arbol.GetItemText(abuelo)
                if abuelo == _('Conjuntos de medidas definidos'):
                    self.Arbol.SelectItem(self.Arbol.GetItemParent(self.Arbol.GetSelection()))
        event.Skip()

    def obtenerConjuntoSeleccionado(self, elemento):
        """
        Metodo: obtenerConjuntoSeleccionado

        """
        for conjuntoMM in self.parent.parent.listadoConjuntosMMUsuario:
            if conjuntoMM.nombre == elemento:
                return conjuntoMM

    def OnDefinirMejorasButton(self, event):
        """
        Metodo: OnDefinirMejorasButton

        ARGUMENTOS:
                 event:
        """
        self.PanelVacio.Destroy()
        self.PanelVacio = panelDefinirMedidasMejora(parent=self, pos=wx.Point(230, 8), size=wx.Size(770, 584), style=wx.TAB_TRAVERSAL, name='PanelVacio', id=-1)
        self.panelBotones.guardarBoton.Show(True)
        self.panelBotones.modificarBoton.Show(True)
        self.panelBotones.borrarBoton.Show(True)

    def OnCompararMejorasButton(self, event):
        """
        Metodo: OnCompararMejorasButton

        ARGUMENTOS:
                 event:
        """
        self.PanelVacio.Destroy()
        if self.parent.parent.programa == 'Residencial':
            self.PanelVacio = panelCompararMejora(parent=self, pos=wx.Point(230, 8), size=wx.Size(770, 584), style=wx.TAB_TRAVERSAL, name='PanelVacio', id=-1)
        else:
            self.PanelVacio = panelCompararMejoraTerciario(parent=self, pos=wx.Point(230, 8), size=wx.Size(770, 584), style=wx.TAB_TRAVERSAL, name='PanelVacio', id=-1)
        self.panelBotones.guardarBoton.Show(False)
        self.panelBotones.modificarBoton.Show(False)
        self.panelBotones.borrarBoton.Show(False)
        event.Skip()

    def OnCerrarButton(self, event):
        """
        Metodo: OnCerrarButton

        ARGUMENTOS:
                 event:
        """
        items = self.parent.parent.menuCalificar.GetMenuItems()
        items[1].Enable(True)
        self.parent.parent.botonMejoras11.Enable(True)
        identificador = self.GetId()
        pagina = self.parent.GetSelection()
        identificador = self.GetId()
        for i in range(len(self.parent.parent.paneles)):
            if self.parent.parent.paneles[i].GetId() == identificador:
                self.parent.parent.paneles.pop(i)
                break

        self.parent.RemovePage(pagina)
        self.parent.parent.panelMedidasMejora.Show(False)

    def abrirPanelMedidasMejora(self):
        """
        Metodo: onCalcularMedidas
        Calcula medidas por defecto conjuntos de medidas que haya creado el usuario
        """
        try:
            self.PanelVacio.Destroy()
        except:
            logging.info('Excepcion en: %s' % __name__)

        self.PanelVacio = panelDefinirMedidasMejora(parent=self, pos=wx.Point(230, 8), size=wx.Size(770, 584), style=wx.TAB_TRAVERSAL, name='PanelVacio', id=-1)
        self.panelBotones.guardarBoton.Show(True)
        self.panelBotones.modificarBoton.Show(True)
        self.panelBotones.borrarBoton.Show(True)
        self.cargarArbol(self.Arbol)