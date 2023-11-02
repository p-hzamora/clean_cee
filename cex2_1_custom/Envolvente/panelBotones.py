# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\panelBotones.pyc
# Compiled at: 2015-02-19 13:18:33
"""
Modulo: panelBotones.py

"""
from MedidasDeMejora.funcionActualizarMMInstalacionesAlCambiarSuperficie import existenInstalacionesColgandoDeZonaModificadaOEliminadaEnConjuntosMM
from undo import eventoUndo
import Calculos.calculoSuperficies as calculoSuperficies, Envolvente.dialogoConfirma as dialogoConfirma, Envolvente.objetosEnvolvente as objetosEnvolvente, copy, undo, ventanaSubgrupo, wx, logging
wxID_PANEL1, wxID_PANEL1ANADIRBOTON, wxID_PANEL1BORRARBOTON, wxID_PANEL1MODIFICARBOTON, wxID_PANEL1VISTACLASICABOT, wxID_PANEL1VISTANORMALBOT = [ wx.NewId() for _init_ctrls in range(6) ]

class panelBotones(wx.Panel):
    """
    Clase: panelBotones del modulo panelBotones.py

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
        self.anadirBoton = wx.Button(id=wxID_PANEL1ANADIRBOTON, label=_('Añadir'), name='anadirBoton', parent=self, pos=wx.Point(0, 0), size=wx.Size(75, 23), style=wx.NO_BORDER)
        self.anadirBoton.Bind(wx.EVT_BUTTON, self.OnAnadirBotonButton, id=wxID_PANEL1ANADIRBOTON)
        self.anadirBoton.SetForegroundColour(wx.Colour(0, 64, 128))
        self.anadirBoton.SetBackgroundColour('white')
        self.modificarBoton = wx.Button(id=wxID_PANEL1MODIFICARBOTON, label=_('Modificar'), name='modificarBoton', parent=self, pos=wx.Point(90, 0), size=wx.Size(75, 23), style=wx.BU_LEFT)
        self.modificarBoton.Bind(wx.EVT_BUTTON, self.OnmodificarBoton, id=wxID_PANEL1MODIFICARBOTON)
        self.modificarBoton.SetForegroundColour(wx.Colour(0, 64, 128))
        self.modificarBoton.SetBackgroundColour('white')
        self.borrarBoton = wx.Button(id=wxID_PANEL1BORRARBOTON, label=_('Borrar'), name='borrarBoton', parent=self, pos=wx.Point(225, 0), size=wx.Size(75, 23), style=0)
        self.borrarBoton.Bind(wx.EVT_BUTTON, self.OnBorrarBotonButton, id=wxID_PANEL1BORRARBOTON)
        self.borrarBoton.SetForegroundColour(wx.Colour(0, 64, 128))
        self.borrarBoton.SetBackgroundColour('white')
        self.vistaClasicaBoton = wx.Button(id=wxID_PANEL1VISTACLASICABOT, label=_('Vista clásica'), name='vistaClasicaBoton', parent=self, pos=wx.Point(610, 0), size=wx.Size(100, 23), style=0)
        self.vistaClasicaBoton.Bind(wx.EVT_BUTTON, self.OnVistaClasicaBoton, id=wxID_PANEL1VISTACLASICABOT)
        self.vistaClasicaBoton.SetBackgroundColour(wx.Color(240, 240, 240))
        self.vistaNormalBoton = wx.Button(id=wxID_PANEL1VISTANORMALBOT, label=_('Vista normal'), name='vistaNormalBoton', parent=self, pos=wx.Point(610, 0), size=wx.Size(100, 23), style=0)
        self.vistaNormalBoton.Bind(wx.EVT_BUTTON, self.OnVistaNormalBoton, id=wxID_PANEL1VISTANORMALBOT)
        self.vistaNormalBoton.Show(False)
        self.vistaNormalBoton.SetBackgroundColour(wx.Color(240, 240, 240))

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

    def quitaBlancos(self, cadena):
        """
        Metodo: quitaBlancos

        ARGUMENTOS:
                cadena:
        """
        quita = True
        while quita == True:
            if cadena.endswith(' ') == True:
                cadena = cadena[0:len(cadena) - 1]
            else:
                quita = False

        return cadena

    def OnAnadirBotonButton(self, event):
        """
        Metodo: OnAnadirBotonButton

        ARGUMENTOS:
                event:
        """
        objeto = self.parent.panel2.cogerDatos()
        if type(objeto) == type('hola'):
            wx.MessageBox(_('Revise los siguientes campos:\n') + objeto, _('Aviso'))
            return
        if type(objeto[0]) == type([]):
            objeto = objeto[0]
        Existe = False
        Tipo = False
        tipoStr = ''
        for i in range(len(self.parent.ventanas)):
            if self.parent.ventanas[i].descripcion == objeto[0]:
                Existe = True
                if self.parent.ventanas[i].tipo == objeto[1]:
                    Tipo = True
                    tipoStr = 'ventana'
                break

        for i in range(len(self.parent.puentesTermicos)):
            if self.parent.puentesTermicos[i][0] == objeto[0]:
                Existe = True
                if self.parent.puentesTermicos[i][1] == objeto[1]:
                    Tipo = True
                    tipoStr = 'puente'
                break

        for i in range(len(self.parent.cerramientos)):
            if self.parent.cerramientos[i][0] == objeto[0]:
                Existe = True
                if self.parent.cerramientos[i][1] == objeto[1] and self.parent.cerramientos[i][-1] == objeto[-1]:
                    Tipo = True
                    tipoStr = 'cerramiento'
                break

        if Existe == True and Tipo == True:
            DeseaReemplazar = dialogoConfirma.Dialog1(self, _('El elemento que desea añadir ya existe. ¿Desea Reemplazarlo?'))
            DeseaReemplazar.ShowModal()
            if DeseaReemplazar.dev == True:
                self.OnDeseaReemplazar(self.parent.panel2.cogerDatos(), tipoStr)
                self.Close()
                return
            if DeseaReemplazar.dev == False:
                self.Close()
                return
        if Existe == True and Tipo == False:
            wx.MessageBox(_('El elemento que desea añadir ya existe y no se puede reemplazar.'), _('Aviso'))
            return
        accionesUndo = []
        datosUndo = []
        if objeto[1] == 'Hueco' or objeto[1] == 'Lucernario':
            objeto = self.parent.panel2.cogerDatos()
            if objeto[1] == 'Estimadas':
                nuevaVentana = objetosEnvolvente.HuecoEstimadas(objeto[0])
            else:
                nuevaVentana = objetosEnvolvente.HuecoConocidas(objeto[0])
            self.parent.ventanas.append(nuevaVentana)
            self.parent.cargarArbol(self.parent.arbolCerramientos)
            datosUndo.append(nuevaVentana.descripcion)
            accionesUndo.append('anadir hueco')
            self.cargarUltimoElemento(nuevaVentana.descripcion)
        elif objeto[1] == 'PT':
            self.parent.puentesTermicos.append(objeto)
            self.parent.cargarArbol(self.parent.arbolCerramientos)
            datosUndo.append(objeto[0])
            accionesUndo.append('anadir PT')
            self.cargarUltimoElemento(objeto[0])
        else:
            self.parent.cerramientos.append(objeto)
            self.parent.cargarArbol(self.parent.arbolCerramientos)
            datosUndo.append(objeto[0])
            accionesUndo.append('anadir cerramiento')
            self.cargarUltimoElemento(objeto[0])
        self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, accionesUndo, datosUndo))
        self.parent.parent.parent.pilaRedo = undo.undoManaggement()

    def cargarUltimoElemento(self, nombre):
        """
        Metodo: cargarUltimoElemento

        ARGUMENTOS:
                nombre:
        """
        array = []
        array = self.iterchildren(self.parent.arbolCerramientos, self.parent.arbolCerramientos.GetRootItem(), array)
        for i in array:
            if self.parent.arbolCerramientos.GetItemText(i) == nombre:
                self.parent.arbolCerramientos.SelectItem(i)
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

    def OnDeseaReemplazar(self, objeto, tipoObjeto):
        """
        Metodo: OnDeseaReemplazar

        ARGUMENTOS:
                objeto:
                tipoObjeto:
        """
        accionesUndo = []
        datosUndo = []
        if tipoObjeto == 'cerramiento':
            for i in range(len(self.parent.cerramientos)):
                if self.parent.cerramientos[i][0] == objeto[0]:
                    datosUndo.append([copy.deepcopy(self.parent.cerramientos[i]), objeto[0]])
                    accionesUndo.append('modificar cerramiento')
                    self.parent.cerramientos[i] = objeto
                    self.parent.cargarArbol(self.parent.arbolCerramientos)
                    break

        elif tipoObjeto == 'ventana':
            for i in range(len(self.parent.ventanas)):
                if self.parent.ventanas[i].descripcion == objeto[0][1]:
                    datosUndo.append([copy.deepcopy(self.parent.ventanas[i]), objeto[0][1]])
                    accionesUndo.append('modificar hueco')
                    if objeto[1] == 'Conocidas':
                        obj = objetosEnvolvente.HuecoConocidas(objeto[0])
                    else:
                        obj = objetosEnvolvente.HuecoEstimadas(objeto[0])
                    self.parent.ventanas[i] = obj
                    self.parent.cargarArbol(self.parent.arbolCerramientos)
                    break

        elif tipoObjeto == 'puente':
            for i in range(len(self.parent.puentesTermicos)):
                if self.parent.puentesTermicos[i][0] == objeto[0]:
                    datosUndo.append([copy.deepcopy(self.parent.puentesTermicos[i]), objeto[0]])
                    accionesUndo.append('modificar PT')
                    if float(self.parent.puentesTermicos[i][3]) == float(objeto[3]):
                        fimodificadoUsuario = self.parent.puentesTermicos[i][5]
                        indicadoUsuario = self.parent.puentesTermicos[i][6]
                        self.parent.puentesTermicos[i] = objeto
                        self.parent.puentesTermicos[i][5] = fimodificadoUsuario
                        self.parent.puentesTermicos[i][6] = indicadoUsuario
                    else:
                        indicadoUsuario = self.parent.puentesTermicos[i][6]
                        self.parent.puentesTermicos[i] = objeto
                        self.parent.puentesTermicos[i][5] = 'usuario_fi'
                        self.parent.puentesTermicos[i][6] = indicadoUsuario
                    self.parent.cargarArbol(self.parent.arbolCerramientos)
                    break

        self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, accionesUndo, datosUndo))
        self.parent.parent.parent.pilaRedo = undo.undoManaggement()

    def OnVistaClasicaBoton(self, event):
        """
        Metodo: OnVistaClasicaBoton

        ARGUMENTOS:
                event:
        """
        self.parent.panelRecuadro.titulo.Show(False)
        self.parent.panelElegirObjeto.Show(False)
        self.parent.panel2.Show(False)
        self.vistaClasicaBoton.Show(False)
        self.parent.vistaClasica.Show(True)
        self.vistaNormalBoton.Show(True)
        self.parent.vistaClasica.cargaCerramientos()
        self.parent.vistaClasica.cargaHuecos()
        self.parent.vistaClasica.cargaPTermicos()
        self.parent.vistaNormal = False
        self.anadirBoton.Show(False)
        self.modificarBoton.Show(False)
        self.borrarBoton.Show(False)

    def OnVistaNormalBoton(self, event):
        """
        Metodo: OnVistaNormalBoton

        ARGUMENTOS:
                event:
        """
        self.parent.vistaNormal = True
        try:
            self.parent.OnArbolCerramientos(None)
        except:
            logging.info('Excepcion en: %s' % __name__)

        self.parent.panelRecuadro.titulo.Show(True)
        self.parent.panelElegirObjeto.Show(True)
        self.parent.panel2.Show(True)
        self.vistaClasicaBoton.Show(True)
        self.parent.vistaClasica.Show(False)
        self.vistaNormalBoton.Show(False)
        self.anadirBoton.Show(True)
        self.modificarBoton.Show(True)
        self.borrarBoton.Show(True)
        return

    def OnmodificarBoton(self, event):
        """
        Metodo: OnmodificarBoton

        ARGUMENTOS:
                event:
        """
        try:
            item = self.parent.arbolCerramientos.GetItemText(self.parent.arbolCerramientos.GetSelection())
        except Exception:
            wx.MessageBox(_('Debe seleccionar el elemento del arbol que desea modificar.'), _('Aviso'))
            return

        root = self.parent.arbolCerramientos.GetSelection()
        if root == self.parent.arbolCerramientos.GetRootItem():
            wx.MessageBox(_('No se puede modificar la raíz del árbol.'), _('Aviso'))
            return
        accionesUndo = []
        datosUndo = []
        if self.parent.arbolCerramientos.GetChildrenCount(self.parent.arbolCerramientos.GetSelection()) > 0:
            if self.parent.arbolCerramientos.GetItemImage(self.parent.arbolCerramientos.GetSelection()) == 6:
                for i in range(len(self.parent.parent.subgrupos)):
                    if item == self.parent.parent.subgrupos[i].nombre:
                        datos = self.parent.parent.subgrupos[i]
                        break

                dlg = ventanaSubgrupo.create(self.parent, -1, wx.Point(200, 200), wx.Size(448, 240), wx.DEFAULT_DIALOG_STYLE, 'ventanaZonas', self.parent, self.parent.parent.parent.panelInstalaciones, 'modificar', item)
                dlg.cargarDatos(datos)
                dlg.ShowModal()
                return
            nuevo = self.parent.panel2.cogerDatos()
            if type(nuevo) == type('hola'):
                wx.MessageBox(_('Revise los siguientes campos:\n') + nuevo, _('Aviso'))
                return
            compruebaNombres = 'elemento no encontrado'
            if nuevo[0] != item:
                compruebaNombres = self.compruebaNombres(nuevo[0])
            compruebaTipo = self.compruebaTipo(nuevo, item)
            if compruebaTipo == False:
                wx.MessageBox(_('El elemento modificado debe ser del mismo tipo que el elemento seleccionado'), _('Aviso'))
                return
            if compruebaNombres == 'elemento no encontrado':
                cerramientoModificado = []
                for i in range(len(self.parent.cerramientos)):
                    if item == self.parent.cerramientos[i][0]:
                        datosUndo.append([copy.deepcopy(self.parent.cerramientos[i]), nuevo[0]])
                        accionesUndo.append('modificar cerramiento')
                        self.parent.cerramientos[i] = nuevo
                        cerramientoModificado = nuevo
                        break

                for i in range(len(self.parent.ventanas)):
                    if item == self.parent.ventanas[i].cerramientoAsociado:
                        datosUndo.append([copy.deepcopy(self.parent.ventanas[i]),
                         self.parent.ventanas[i].descripcion])
                        accionesUndo.append('modificar hueco')
                        self.parent.ventanas[i].cerramientoAsociado = nuevo[0]
                        self.parent.ventanas[i].orientacion = nuevo[5]
                        self.parent.ventanas[i].subgrupo = nuevo[-2]
                        if cerramientoModificado[1] == 'Fachada' and cerramientoModificado[-1] == 'aire':
                            self.parent.ventanas[i].tipo = 'Hueco'
                            self.parent.ventanas[i].correctorSolar = cerramientoModificado[5]
                        elif cerramientoModificado[1] == 'Cubierta' and cerramientoModificado[-1] == 'aire':
                            self.parent.ventanas[i].tipo = 'Lucernario'
                            self.parent.ventanas[i].correctorSolar = cerramientoModificado[5]

                for i in range(len(self.parent.puentesTermicos)):
                    if item == self.parent.puentesTermicos[i][7]:
                        datosUndo.append([copy.deepcopy(self.parent.puentesTermicos[i]),
                         self.parent.puentesTermicos[i][0]])
                        accionesUndo.append('modificar PT')
                        self.parent.puentesTermicos[i][7] = nuevo[0]
                        self.parent.puentesTermicos[i][-1] = nuevo[-2]

            else:
                wx.MessageBox(_('El nombre del elemento modificado ya existe, indique otro'), _('Aviso'))
        else:
            for i in range(len(self.parent.parent.subgrupos)):
                if item == self.parent.parent.subgrupos[i].nombre:
                    datos = self.parent.parent.subgrupos[i]
                    dlg = ventanaSubgrupo.create(self.parent, -1, wx.Point(200, 200), wx.Size(448, 240), wx.DEFAULT_DIALOG_STYLE, 'ventanaZonas', self.parent, self.parent.parent.parent.panelInstalaciones, 'modificar', item)
                    dlg.cargarDatos(datos)
                    dlg.ShowModal()
                    return

            nuevo = self.parent.panel2.cogerDatos()
            if type(nuevo) == type('hola'):
                wx.MessageBox(_('Revise los siguientes campos:\n ' + nuevo), _('Aviso'))
                return
            if type(nuevo[0]) == type([]):
                nuevo = nuevo[0]
            compruebaNombres = 'elemento no encontrado'
            if nuevo[0] != item:
                compruebaNombres = self.compruebaNombres(nuevo[0])
            compruebaTipo = self.compruebaTipo(nuevo, item)
            if compruebaTipo == False:
                wx.MessageBox(_('El elemento modificado debe ser del mismo tipo que el elemento seleccionado'), _('Aviso'))
                return
            if compruebaNombres == 'elemento no encontrado':
                if nuevo[1] == 'Lucernario' or nuevo[1] == 'Hueco':
                    for i in range(len(self.parent.ventanas)):
                        if item == self.parent.ventanas[i].descripcion:
                            nuevo = self.parent.panel2.cogerDatos()
                            datosUndo.append([copy.deepcopy(self.parent.ventanas[i]), nuevo[0][1]])
                            accionesUndo.append('modificar hueco')
                            if nuevo[1] == 'Conocidas':
                                obj = objetosEnvolvente.HuecoConocidas(nuevo[0])
                            else:
                                obj = objetosEnvolvente.HuecoEstimadas(nuevo[0])
                            self.parent.ventanas[i] = obj
                            nuevo[0] = nuevo[0][0]
                            break

                else:
                    if nuevo[1] != 'Lucernario' and nuevo[1] != 'Hueco' and nuevo[1] != 'PT':
                        for i in range(len(self.parent.cerramientos)):
                            if item == self.parent.cerramientos[i][0]:
                                datosUndo.append([copy.deepcopy(self.parent.cerramientos[i]), nuevo[0]])
                                accionesUndo.append('modificar cerramiento')
                                self.parent.cerramientos[i] = nuevo
                                break

                    else:
                        for i in range(len(self.parent.puentesTermicos)):
                            if item == self.parent.puentesTermicos[i][0]:
                                datosUndo.append([copy.deepcopy(self.parent.puentesTermicos[i]), nuevo[0]])
                                accionesUndo.append('modificar PT')
                                if float(self.parent.puentesTermicos[i][3]) == float(nuevo[3]):
                                    fimodificadoUsuario = self.parent.puentesTermicos[i][5]
                                    indicadoUsuario = self.parent.puentesTermicos[i][6]
                                    self.parent.puentesTermicos[i] = nuevo
                                    self.parent.puentesTermicos[i][5] = fimodificadoUsuario
                                    self.parent.puentesTermicos[i][6] = indicadoUsuario
                                else:
                                    indicadoUsuario = self.parent.puentesTermicos[i][6]
                                    self.parent.puentesTermicos[i] = nuevo
                                    self.parent.puentesTermicos[i][5] = 'usuario_fi'
                                    self.parent.puentesTermicos[i][6] = indicadoUsuario
                                break

            else:
                wx.MessageBox(_('El nombre del elemento modificado ya existe, indique otro'), _('Aviso'))
        self.parent.cargarArbol(self.parent.arbolCerramientos)
        self.cargarUltimoElemento(nuevo[0])
        self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, accionesUndo, datosUndo))
        self.parent.parent.parent.pilaRedo = undo.undoManaggement()

    def compruebaTipo(self, nuevo, item):
        """
        Metodo: compruebaTipo

        ARGUMENTOS:
                nuevo:
                item:
        """
        for cerr in self.parent.cerramientos:
            if item == cerr[0]:
                if nuevo[1] == cerr[1] and nuevo[-1] == cerr[-1]:
                    return True
                else:
                    return False

        for vent in self.parent.ventanas:
            if item == vent.descripcion:
                if nuevo[1] == vent.tipo:
                    return True
                else:
                    return False

        for pt in self.parent.puentesTermicos:
            if item == pt[0]:
                if nuevo[1] == pt[1]:
                    return True
                else:
                    return False

        return False

    def compruebaNombres(self, nombre):
        """
        Metodo: compruebaNombres

        ARGUMENTOS:
                nombre):  #funcion para comprobar que el nombre del conjunto que estoy poniendo no exis:
        """
        if type(nombre) == type([]):
            nombre = copy.deepcopy(nombre[0])
        for cerr in self.parent.cerramientos:
            if nombre == cerr[0]:
                return nombre

        for vent in self.parent.ventanas:
            if nombre == vent.descripcion:
                return nombre

        for pt in self.parent.puentesTermicos:
            if nombre == pt[0]:
                return nombre

        return 'elemento no encontrado'

    def ModificarRaizElemento(self, nombreViejo, nombreNuevo):
        """
        Metodo: ModificarRaizElemento

        ARGUMENTOS:
                nombreViejo:
                nombreNuevo:
        """
        for i in range(len(self.parent.cerramientos)):
            if nombreViejo == self.parent.cerramientos[i][len(self.parent.cerramientos[i]) - 2]:
                self.parent.cerramientos[i][len(self.parent.cerramientos[i]) - 2] = nombreNuevo

    def OnBorrarBotonButton(self, event):
        """
        Metodo: OnBorrarBotonButton

        ARGUMENTOS:
                event:
        """
        try:
            item = self.parent.arbolCerramientos.GetItemText(self.parent.arbolCerramientos.GetSelection())
        except Exception:
            wx.MessageBox(_('Debe seleccionar el elemento del árbol que desea eliminar.'), _('Aviso'))
            return

        root = self.parent.arbolCerramientos.GetSelection()
        if root == self.parent.arbolCerramientos.GetRootItem():
            wx.MessageBox(_('No se puede borrar la raíz del árbol.'), _('Aviso'))
            return
        borrar = dialogoConfirma.Dialog1(self, _('¿Desea borrar el elemento "') + item + '"?')
        borrar.ShowModal()
        if borrar.dev == False:
            return
        if self.parent.arbolCerramientos.GetChildrenCount(self.parent.arbolCerramientos.GetSelection()) > 0:
            borraTodo = dialogoConfirma.Dialog1(self, _('Si borra este elemento se perderán todos sus componentes. ¿Desea continuar?'))
            borraTodo.ShowModal()
            if borraTodo.dev == True:
                self.borraGrupo()
        else:
            accionesUndo = []
            datosUndo = []
            for i in range(len(self.parent.cerramientos)):
                if item == self.parent.cerramientos[i][0]:
                    datosUndo.append([copy.deepcopy(self.parent.cerramientos[i]), i])
                    accionesUndo.append('borrar cerramiento')
                    self.parent.cerramientos.pop(i)
                    break

            for i in range(len(self.parent.ventanas)):
                if item == self.parent.ventanas[i].descripcion:
                    datosUndo.append([copy.deepcopy(self.parent.ventanas[i]), i])
                    accionesUndo.append('borrar hueco')
                    self.parent.ventanas.pop(i)
                    break

            for i in range(len(self.parent.puentesTermicos)):
                if item == self.parent.puentesTermicos[i][0]:
                    datosUndo.append([copy.deepcopy(self.parent.puentesTermicos[i]), i])
                    accionesUndo.append('borrar PT')
                    self.parent.puentesTermicos.pop(i)
                    break

            for i in range(len(self.parent.parent.subgrupos)):
                if item == self.parent.parent.subgrupos[i].nombre:
                    self.borraGrupo()
                    break

            self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, accionesUndo, datosUndo))
            self.parent.parent.parent.pilaRedo = undo.undoManaggement()
        self.parent.cargarArbol(self.parent.arbolCerramientos)

    def borraGrupo(self):
        """
        Metodo: borraGrupo

                self):   ####Solo lo que tienen hij:
        """
        seleccion = self.parent.arbolCerramientos.GetSelection()
        textoSelect = self.parent.arbolCerramientos.GetItemText(seleccion)
        if self.parent.arbolCerramientos.GetItemImage(self.parent.arbolCerramientos.GetSelection()) == 6:
            for i in range(len(self.parent.parent.subgrupos)):
                if self.parent.parent.subgrupos[i].raiz == textoSelect:
                    wx.MessageBox(_('No puede borrar una zona con más subzonas dentro'), _('Aviso'))
                    return

            pertenece = False
            for i in range(len(self.parent.parent.parent.panelInstalaciones.ACS)):
                if self.parent.parent.parent.panelInstalaciones.ACS[i][-1] == textoSelect:
                    pertenece = True
                    break

            if pertenece != True:
                for i in range(len(self.parent.parent.parent.panelInstalaciones.calefaccion)):
                    if self.parent.parent.parent.panelInstalaciones.calefaccion[i][-1] == textoSelect:
                        pertenece = True
                        break

            if pertenece != True:
                for i in range(len(self.parent.parent.parent.panelInstalaciones.refrigeracion)):
                    if self.parent.parent.parent.panelInstalaciones.refrigeracion[i][-1] == textoSelect:
                        pertenece = True
                        break

            if pertenece != True:
                for i in range(len(self.parent.parent.parent.panelInstalaciones.climatizacion)):
                    if self.parent.parent.parent.panelInstalaciones.climatizacion[i][-1] == textoSelect:
                        pertenece = True
                        break

            if pertenece != True:
                for i in range(len(self.parent.parent.parent.panelInstalaciones.mixto2)):
                    if self.parent.parent.parent.panelInstalaciones.mixto2[i][-1] == textoSelect:
                        pertenece = True
                        break

            if pertenece != True:
                for i in range(len(self.parent.parent.parent.panelInstalaciones.mixto3)):
                    if self.parent.parent.parent.panelInstalaciones.mixto3[i][-1] == textoSelect:
                        pertenece = True
                        break

            if pertenece != True:
                for i in range(len(self.parent.parent.parent.panelInstalaciones.contribuciones)):
                    if self.parent.parent.parent.panelInstalaciones.contribuciones[i][-1] == textoSelect:
                        pertenece = True
                        break

            if pertenece != True:
                for i in range(len(self.parent.parent.parent.panelInstalaciones.iluminacion)):
                    if self.parent.parent.parent.panelInstalaciones.iluminacion[i][-1] == textoSelect:
                        pertenece = True
                        break

            if pertenece != True:
                for i in range(len(self.parent.parent.parent.panelInstalaciones.ventilacion)):
                    if self.parent.parent.parent.panelInstalaciones.ventilacion[i][-1] == textoSelect:
                        pertenece = True
                        break

            if pertenece != True:
                for i in range(len(self.parent.parent.parent.panelInstalaciones.ventiladores)):
                    if self.parent.parent.parent.panelInstalaciones.ventiladores[i][-1] == textoSelect:
                        pertenece = True
                        break

            if pertenece != True:
                for i in range(len(self.parent.parent.parent.panelInstalaciones.bombas)):
                    if self.parent.parent.parent.panelInstalaciones.bombas[i][-1] == textoSelect:
                        pertenece = True
                        break

            if pertenece != True:
                for i in range(len(self.parent.parent.parent.panelInstalaciones.torresRefrigeracion)):
                    if self.parent.parent.parent.panelInstalaciones.torresRefrigeracion[i][-1] == textoSelect:
                        pertenece = True
                        break

            accionesUndo = []
            datosUndo = []
            if pertenece == True:
                boolExistenInstColgandoDeZonaEliminadaEnConjuntosMM = existenInstalacionesColgandoDeZonaModificadaOEliminadaEnConjuntosMM(listadoConjuntosMM=self.parent.parent.parent.listadoConjuntosMMUsuario, subgrupoModifOElim=textoSelect)
                if boolExistenInstColgandoDeZonaEliminadaEnConjuntosMM == True:
                    mensaje = _('La zona que desea borrar tiene instalaciones asociadas. Si borra este elemento se perderán todos sus componentes. Además, se eliminarán las instalaciones de los conjuntos de medidas de mejora que cuelguen de dicho elemento y deberán ser revisadas. ¿Desea continuar?')
                else:
                    mensaje = _('La zona que desea borrar tiene instalaciones asociadas. ¿Desea borrar también estas instalaciones?')
                DeseaEliminar = dialogoConfirma.Dialog1(self, mensaje, size=(600, 125))
                DeseaEliminar.ShowModal()
                if DeseaEliminar.dev == True:
                    pass
                elif DeseaEliminar.dev == False:
                    self.Close()
                    return
            for i in range(len(self.parent.parent.subgrupos)):
                if textoSelect == self.parent.parent.subgrupos[i].nombre:
                    zonaEliminada = self.parent.parent.subgrupos[i]
                    datosUndo.append([copy.deepcopy(self.parent.parent.subgrupos[i]), i])
                    accionesUndo.append('borrar zona')
                    self.parent.parent.subgrupos.pop(i)

            cambios = self.parent.parent.parent.panelInstalaciones.panelBotones.BorrarSubgrupoInstalaciones(zonaEliminada=zonaEliminada)
            for i in range(len(cambios[0])):
                datosUndo.append(cambios[0][i])
                accionesUndo.append(cambios[1][i])

            cambios = self.BorrarSubgrupoEnvolvente(textoSelect)
            for i in range(len(cambios[0])):
                datosUndo.append(cambios[0][i])
                accionesUndo.append(cambios[1][i])

            for i in range(len(cambios[0])):
                datosUndo.append(cambios[0][i])
                accionesUndo.append(cambios[1][i])

            self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, accionesUndo, datosUndo))
            self.parent.parent.parent.pilaRedo = undo.undoManaggement()
            return
        accionesUndo = []
        datosUndo = []
        bol = False
        while bol != True:
            bol = True
            for j in range(len(self.parent.puentesTermicos)):
                if self.parent.puentesTermicos[j][7] == textoSelect:
                    datosUndo.append([copy.deepcopy(self.parent.puentesTermicos[j]), j])
                    accionesUndo.append('borrar PT')
                    self.parent.puentesTermicos.pop(j)
                    bol = False
                    break

        bol = False
        while bol != True:
            bol = True
            for j in range(len(self.parent.ventanas)):
                if self.parent.ventanas[j].cerramientoAsociado == textoSelect:
                    datosUndo.append([copy.deepcopy(self.parent.ventanas[j]), j])
                    accionesUndo.append('borrar hueco')
                    self.parent.ventanas.pop(j)
                    bol = False
                    break

        for j in range(len(self.parent.cerramientos)):
            if self.parent.cerramientos[j][0] == textoSelect:
                datosUndo.append([copy.deepcopy(self.parent.cerramientos[j]), j])
                accionesUndo.append('borrar cerramiento')
                self.parent.cerramientos.pop(j)
                break

        self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, accionesUndo, datosUndo))
        self.parent.parent.parent.pilaRedo = undo.undoManaggement()

    def BorrarSubgrupoEnvolvente(self, textoSelect):
        """
        Metodo: BorrarSubgrupoEnvolvente

        ARGUMENTOS:
                textoSelect:
        """
        cerramientosBorrar = []
        for i in range(len(self.parent.cerramientos)):
            if self.parent.cerramientos[i][len(self.parent.cerramientos[i]) - 2] == textoSelect:
                cerramientosBorrar.append(self.parent.cerramientos[i][0])

        accionesUndo = []
        datosUndo = []
        bol = False
        while bol != True:
            bol = True
            for j in range(len(self.parent.puentesTermicos)):
                if cerramientosBorrar.count(self.parent.puentesTermicos[j][7]) != 0:
                    datosUndo.append([copy.deepcopy(self.parent.puentesTermicos[j]), j])
                    accionesUndo.append('borrar PT')
                    self.parent.puentesTermicos.pop(j)
                    bol = False
                    break

        bol = False
        while bol != True:
            bol = True
            for j in range(len(self.parent.ventanas)):
                if cerramientosBorrar.count(self.parent.ventanas[j].cerramientoAsociado) != 0:
                    datosUndo.append([copy.deepcopy(self.parent.ventanas[j]), j])
                    accionesUndo.append('borrar hueco')
                    self.parent.ventanas.pop(j)
                    bol = False
                    break

        bol = False
        while bol != True:
            bol = True
            for j in range(len(self.parent.cerramientos)):
                if cerramientosBorrar.count(self.parent.cerramientos[j][0]) != 0:
                    datosUndo.append([copy.deepcopy(self.parent.cerramientos[j]), j])
                    accionesUndo.append('borrar cerramiento')
                    self.parent.cerramientos.pop(j)
                    bol = False
                    break

        return [
         datosUndo, accionesUndo]