# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: MedidasDeMejora\panelBotonesMedidas.pyc
# Compiled at: 2015-02-19 13:18:34
"""
Modulo: panelBotonesMedidas.py

"""
from MedidasDeMejora.objetoGrupoMejoras import grupoMedidasMejora, mejoraEdificioCompleto
from undo import eventoUndo
import dialogoConfirma, undo, wx, logging
wxID_PANEL1, wxID_PANEL1ANADIRBOTON, wxID_PANEL1BORRARBOTON, wxID_PANEL1MODIFICARBOTON, wxID_PANEL1VISTACLASICABOT, wxID_PANEL1VISTANORMALBOT = [ wx.NewId() for _init_ctrls in range(6) ]

class panelBotones(wx.Panel):
    """
    Clase: panelBotones del modulo panelBotonesMedidas.py

    """

    def _init_ctrls(self, prnt, ide, posi, siz, styl, nam):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
                ide:
                posi:
                siz:
                styl:
                nam:
        """
        wx.Panel.__init__(self, id=ide, name=nam, parent=prnt, pos=posi, size=siz, style=styl)
        self.SetBackgroundColour('white')
        self.guardarBoton = wx.Button(id=wxID_PANEL1ANADIRBOTON, label=_('Guardar conjunto'), name='anadirBoton', parent=self, pos=wx.Point(0, 0), size=wx.Size(100, 23), style=0)
        self.guardarBoton.Bind(wx.EVT_BUTTON, self.OnAnadirBotonButton, id=wxID_PANEL1ANADIRBOTON)
        self.guardarBoton.SetToolTip(wx.ToolTip(_('Guardar el conjunto de medidas de mejora definido.')))
        self.guardarBoton.Show(False)
        self.guardarBoton.SetForegroundColour(wx.Colour(0, 64, 128))
        self.guardarBoton.SetBackgroundColour('white')
        self.modificarBoton = wx.Button(id=wxID_PANEL1MODIFICARBOTON, label=_('Modificar conjunto'), name='modificarBoton', parent=self, pos=wx.Point(115, 0), size=wx.Size(100, 23), style=0)
        self.modificarBoton.Bind(wx.EVT_BUTTON, self.OnmodificarBoton, id=wxID_PANEL1MODIFICARBOTON)
        self.modificarBoton.Show(False)
        self.modificarBoton.SetForegroundColour(wx.Colour(0, 64, 128))
        self.modificarBoton.SetBackgroundColour('white')
        self.modificarBoton.SetToolTip(wx.ToolTip(_('Modificar el conjunto de medidas de mejora.')))
        self.borrarBoton = wx.Button(id=wxID_PANEL1BORRARBOTON, label=_('Borrar conjunto'), name='borrarBoton', parent=self, pos=wx.Point(275, 0), size=wx.Size(100, 23), style=0)
        self.borrarBoton.Bind(wx.EVT_BUTTON, self.OnBorrarBoton, id=wxID_PANEL1BORRARBOTON)
        self.borrarBoton.Show(False)
        self.borrarBoton.SetForegroundColour(wx.Colour(0, 64, 128))
        self.borrarBoton.SetBackgroundColour('white')
        self.borrarBoton.SetToolTip(wx.ToolTip(_('Eliminar el conjunto de medidas de mejora seleccionado.')))

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
        self._init_ctrls(parent, id, pos, size, style, name)
        self.parent = parent

    def compruebaNombres(self, nombre):
        """
        Metodo: compruebaNombres

        ARGUMENTOS:
                nombre:
        """
        for i in range(len(self.parent.parent.parent.listadoConjuntosMMUsuario)):
            if nombre == self.parent.parent.parent.listadoConjuntosMMUsuario[i].nombre:
                return nombre

        return 'elemento no encontrado'

    def cargarUltimoElemento(self, nombre):
        """
        Metodo: cargarUltimoElemento

        ARGUMENTOS:
                nombre:
        """
        array = []
        array = self.iterchildren(self.parent.Arbol, self.parent.Arbol.GetRootItem(), array)
        for i in array:
            if self.parent.Arbol.GetItemText(i) == nombre:
                self.parent.Arbol.SelectItem(i)
                break

    def iterchildren(self, treectrl, node, array):
        """
        Metodo: iterchildren

        ARGUMENTOS:
                treectrl:
                node:
                array):   ###Funcion que me comprueba los hijos que tengo dent:
        """
        cid, citem = treectrl.GetFirstChild(node)
        while cid.IsOk():
            array.append(cid)
            if treectrl.GetChildrenCount(cid) != 0:
                self.iterchildren(treectrl, cid, array)
            cid, citem = treectrl.GetNextChild(node, citem)

        return array

    def OnAnadirBotonButton(self, event):
        """
        Metodo: OnAnadirBotonButton

        ARGUMENTOS:
                event:
        """
        if self.parent.PanelVacio.conjuntoMedidasEnvolvente == [] and self.parent.PanelVacio.conjuntoMedidasInstalaciones == False:
            wx.MessageBox(_('No se han definido las medidas de mejora del edificio'), _('Aviso'))
            return
        else:
            if self.parent.PanelVacio.DescripcionCuadro.GetValue() == '':
                wx.MessageBox(_('No se ha indicado el nombre del conjunto de medidas definidas'), _('Aviso'))
                return
            if self.compruebaNombres(self.parent.PanelVacio.DescripcionCuadro.GetValue()) == 'elemento no encontrado':
                nuevo = grupoMedidasMejora(nombre=self.parent.PanelVacio.DescripcionCuadro.GetValue(), datosEdificioOriginal=self.parent.parent.parent.objEdificio, mejoras=self.parent.PanelVacio.listadoMedidas, caracteristicas=self.parent.PanelVacio.caracteristicasCuadro.GetValue(), otrosDatos=self.parent.PanelVacio.otrosDatosCuadro.GetValue())
                nuevo.calificacion()
                if nuevo.datosNuevoEdificio.casoValido == False:
                    wx.MessageBox(_('El conjunto de medidas de mejora no es válido, revise las medidas de mejora individuales que lo conforman'), _('Aviso'))
                    return
                self.parent.parent.parent.listadoConjuntosMMUsuario.append(nuevo)
                self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, 'anadir conjunto', nuevo.nombre))
                self.parent.parent.parent.pilaRedo = undo.undoManaggement()
                self.parent.cargarArbol(self.parent.Arbol)
                self.parent.parent.parent.panelAnalisisEconomico.panelCosteMedidas.incluirMedidas()
                self.parent.parent.parent.panelAnalisisEconomico.panelResultado.incluirConjuntosMedidas()
                self.parent.parent.parent.panelAnalisisEconomico.onNotebookChanged(None)
                self.cargarUltimoElemento(nuevo.nombre)
            else:
                wx.MessageBox(_('El nombre del conjunto de mejoras ya existe.'), _('Aviso'))
                return
            return

    def OnmodificarBoton(self, event):
        """
        Metodo: OnmodificarBoton

        ARGUMENTOS:
                event:
        """
        try:
            item = self.parent.Arbol.GetItemText(self.parent.Arbol.GetSelection())
        except:
            wx.MessageBox(_('Debe seleccionar el elemento del árbol que desea modificar.'), _('Aviso'))
            return

        if self.parent.PanelVacio.listadoMedidas == []:
            wx.MessageBox(_('No se han definido las medidas de mejora del edificio'), _('Aviso'))
            return
        else:
            if self.parent.PanelVacio.DescripcionCuadro.GetValue() == '':
                wx.MessageBox(_('No se ha indicado el nombre del conjunto de medidas.'), _('Aviso'))
                return
            if self.compruebaNombres(self.parent.PanelVacio.DescripcionCuadro.GetValue()) == 'elemento no encontrado':
                nuevo = grupoMedidasMejora(nombre=self.parent.PanelVacio.DescripcionCuadro.GetValue(), datosEdificioOriginal=self.parent.parent.parent.objEdificio, mejoras=self.parent.PanelVacio.listadoMedidas, caracteristicas=self.parent.PanelVacio.caracteristicasCuadro.GetValue(), otrosDatos=self.parent.PanelVacio.otrosDatosCuadro.GetValue())
                nuevo.calificacion()
                if nuevo.datosNuevoEdificio.casoValido == False:
                    wx.MessageBox(_('El conjunto de medidas de mejora no es válido, revise las medidas de mejora individuales que lo conforman'), _('Aviso'))
                    return
                for i in range(len(self.parent.parent.parent.listadoConjuntosMMUsuario)):
                    if self.parent.parent.parent.listadoConjuntosMMUsuario[i].nombre == item:
                        self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, 'modificar conjunto', [
                         self.parent.parent.parent.listadoConjuntosMMUsuario[i], nuevo.nombre]))
                        self.parent.parent.parent.pilaRedo = undo.undoManaggement()
                        self.parent.parent.parent.listadoConjuntosMMUsuario[i] = nuevo
                        break

                self.parent.cargarArbol(self.parent.Arbol)
                self.cargarUltimoElemento(nuevo.nombre)
            elif self.compruebaNombres(self.parent.PanelVacio.DescripcionCuadro.GetValue()) == item:
                for i in range(len(self.parent.parent.parent.listadoConjuntosMMUsuario)):
                    if self.parent.parent.parent.listadoConjuntosMMUsuario[i].nombre == item:
                        conjuntoSeleccionado = self.parent.parent.parent.listadoConjuntosMMUsuario[i]
                        break

                if isinstance(conjuntoSeleccionado, mejoraEdificioCompleto):
                    nuevo = conjuntoSeleccionado
                    nuevo.caracteristicas = self.parent.PanelVacio.caracteristicasCuadro.GetValue()
                    nuevo.otrosDatos = self.parent.PanelVacio.otrosDatosCuadro.GetValue()
                else:
                    nuevo = grupoMedidasMejora(nombre=self.parent.PanelVacio.DescripcionCuadro.GetValue(), datosEdificioOriginal=self.parent.parent.parent.objEdificio, mejoras=self.parent.PanelVacio.listadoMedidas, caracteristicas=self.parent.PanelVacio.caracteristicasCuadro.GetValue(), otrosDatos=self.parent.PanelVacio.otrosDatosCuadro.GetValue())
                    nuevo.calificacion()
                if nuevo.datosNuevoEdificio.casoValido == False:
                    wx.MessageBox(_('El conjunto de medidas de mejora no es válido, revise las medidas de mejora individuales que lo conforman'), _('Aviso'))
                    return
                for i in range(len(self.parent.parent.parent.listadoConjuntosMMUsuario)):
                    if self.parent.parent.parent.listadoConjuntosMMUsuario[i].nombre == item:
                        self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, 'modificar conjunto', [self.parent.parent.parent.listadoConjuntosMMUsuario[i], nuevo.nombre]))
                        self.parent.parent.parent.pilaRedo = undo.undoManaggement()
                        self.parent.parent.parent.listadoConjuntosMMUsuario[i] = nuevo
                        break

                self.parent.cargarArbol(self.parent.Arbol)
                self.cargarUltimoElemento(nuevo.nombre)
            else:
                wx.MessageBox(_('El nombre del conjunto de mejoras ya existe.'), _('Aviso'))
                return
            self.parent.parent.parent.panelAnalisisEconomico.panelCosteMedidas.incluirMedidas()
            self.parent.parent.parent.panelAnalisisEconomico.panelResultado.incluirConjuntosMedidas()
            self.parent.parent.parent.panelAnalisisEconomico.onNotebookChanged(None)
            return

    def OnBorrarBoton(self, event):
        """
        Metodo: OnBorrarBoton

        ARGUMENTOS:
                event:
        """
        try:
            item = self.parent.Arbol.GetItemText(self.parent.Arbol.GetSelection())
        except:
            wx.MessageBox(_('Debe seleccionar el elemento del árbol que desea eliminar.'), _('Aviso'))
            return

        borrar = dialogoConfirma.Dialog1(self, _('¿Desea borrar el elemento "') + item + '"?')
        borrar.ShowModal()
        if borrar.dev == False:
            return
        else:
            for i in range(len(self.parent.parent.parent.listadoConjuntosMMUsuario)):
                if self.parent.parent.parent.listadoConjuntosMMUsuario[i].nombre == item:
                    self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, 'borrar conjunto', [
                     self.parent.parent.parent.listadoConjuntosMMUsuario[i], i]))
                    self.parent.parent.parent.pilaRedo = undo.undoManaggement()
                    self.parent.parent.parent.listadoConjuntosMMUsuario.pop(i)
                    break

            self.parent.cargarArbol(self.parent.Arbol)
            self.parent.parent.parent.panelAnalisisEconomico.panelCosteMedidas.incluirMedidas()
            self.parent.parent.parent.panelAnalisisEconomico.panelResultado.incluirConjuntosMedidas()
            self.parent.parent.parent.panelAnalisisEconomico.onNotebookChanged(None)
            return