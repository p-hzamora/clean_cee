# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: undo.pyc
# Compiled at: 2014-10-23 12:59:57
"""
Modulo: undo.py

"""
import copy, wx

class EventoInicial:

    def __init__(self):
        self.miniEventos = undoManaggement()
        self.accion = 'inicioPila'
        self.parent = None
        return

    def contraEvento(self, opcion=None):
        pass

    def borraMiniEventos(self):
        self.miniEventos.vaciarPila()


class undoManaggement:
    """
    Clase: undoManaggement del modulo undo.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.pila = []

    def apilarMini(self, evento):
        try:
            self.pila[0].miniEventos.apilar(evento)
        except IndexError:
            self.vaciarPila()
            self.pila[0].miniEventos.apilar(evento)

    def apilar(self, evento, mini=False):
        """
        Metodo: apilar

        ARGUMENTOS:
                evento):##cada vez que ocurra un evento que queramos recoger en el UNDO:
                apilam:
        """
        if mini == True:
            self.apilarMini(evento)
            return
        self.pila.insert(0, evento)
        if len(self.pila) > 40:
            self.pila.pop(40)

    def desempilar(self):
        """
        Metodo: desempilar

                self):## cada vez que se presione el boton de UNDO desapilam:
        """
        evento = self.pila[0]
        self.pila.pop(0)
        if len(self.pila) == 0:
            self.pila = [
             EventoInicial()]
        return evento

    def vaciarPila(self):
        """
        Metodo: vaciarPila

        """
        self.pila = [
         EventoInicial()]


class UndoCambioSeleccion:
    """
    Clase: UndoCambioSeleccion del modulo undo.py

    """

    def __init__(self, objetoOrigen, datos, itemArbol=None):
        """
        Constructor de la clase

        ARGUMENTOS:
            objetoOrigen:
            datos:
        """
        self.accion = objetoOrigen
        self.datos = datos
        self.parent = objetoOrigen.GetParent()
        self.miniEventos = undoManaggement()
        self.itemArbol = itemArbol

    def contraEvento(self, opcion):
        pila = self.accion.GetParent().parent.parent.parent.pilaUndo.pila
        if pila[0].miniEventos.pila == []:
            self.accion.GetParent().parent.parent.parent.deshacerUltimoPaso(None)
            return
        else:
            if len(pila[0].miniEventos.pila) == 1 and pila[0].miniEventos.pila[0].accion == 'inicioPila':
                self.accion.GetParent().parent.parent.parent.deshacerUltimoPaso(None)
                return
            datosRedo = [
             copy.deepcopy(self.accion.GetParent().diccionario[self.accion.GetParent().Name + '.radios'])]
            self.accion.GetParent().diccionario[self.accion.GetParent().Name + '.radios'] = self.datos[0]
            datosRedo.append(copy.deepcopy(self.accion.GetParent().GetParent().panel2.diccionario))
            if self.itemArbol != None:
                item = self.buscaElementosEnvolvente(self.itemArbol)
                arbol = self.accion.GetParent().GetParent().arbolCerramientos
                self.itemArbol = arbol.GetItemText(arbol.GetSelection())
                self.accion.GetParent().GetParent().arbolCerramientos.SelectItem(item)
                self.accion.GetParent().parent.parent.parent.pilaUndo.desempilar()
            else:
                self.accion.GetParent().SetRadioValues(self.datos[0])
                ev = wx.PyCommandEvent(wx.EVT_RADIOBUTTON.typeId, self.datos[-1].GetId())
                self.datos[-1].GetEventHandler().ProcessEvent(ev)
            datosRedo.append(self.accion)
            self.accion.GetParent().GetParent().panel2.diccionario = self.datos[1]
            self.accion.GetParent().GetParent().panel2.cogeValoresDiccionario()
            if opcion == 0:
                self.accion.GetParent().parent.parent.parent.pilaRedo.apilar(UndoCambioSeleccion(self.datos[-1], datosRedo, self.itemArbol))
                self.accion.GetParent().parent.parent.parent.deshacerUltimoPaso(None)
            elif opcion == 1:
                self.accion.GetParent().parent.parent.parent.pilaUndo.apilar(UndoCambioSeleccion(self.datos[-1], datosRedo, self.itemArbol))
                self.accion.GetParent().parent.parent.parent.rehacerUltimoPaso(None)
            return

    def buscaElementosEnvolvente(self, nombre):
        for i in self.accion.GetParent().GetParent().elementosArbol:
            name = self.accion.GetParent().GetParent().arbolCerramientos.GetItemText(i)
            if name == nombre:
                return i


class MiniEventoUndo:
    """
    Clase: MiniEventoUndo del modulo undo.py

    """

    def __init__(self, objetoOrigen, datos):
        """
        Constructor de la clase

        ARGUMENTOS:
            objetoOrigen:
            datos:
        """
        self.accion = objetoOrigen
        self.datos = datos

    def contraEvento(self, opcion):
        objeto = self.accion[0].panel2.FindWindowById(self.accion[1])
        if str(type(objeto)) == "<class 'wx._controls.TextCtrl'>":
            objeto.ChangeValue(self.datos)
            ev = wx.PyCommandEvent(wx.EVT_TEXT.typeId, objeto.GetId())
            wx.PostEvent(objeto.GetEventHandler(), ev)
        elif str(type(objeto)) == "<class 'wx._controls.Choice'>":
            objeto.SetSelection(self.datos)
            ev = wx.PyCommandEvent(wx.EVT_CHOICE.typeId, objeto.GetId())
            wx.PostEvent(objeto.GetEventHandler(), ev)
        elif str(type(objeto)) == "<class 'wx._controls.CheckBox'>":
            objeto.SetValue(self.datos)
            ev = wx.PyCommandEvent(wx.EVT_CHECKBOX.typeId, objeto.GetId())
            wx.PostEvent(objeto.GetEventHandler(), ev)
        elif str(type(objeto)) == "<class 'wx._controls.RadioButton'>":
            datosRedo = copy.deepcopy(objeto.GetParent().diccionario[objeto.GetParent().Name + '.radios'])
            objeto.GetParent().SetRadioValues(self.datos)
            ev = wx.PyCommandEvent(wx.EVT_RADIOBUTTON.typeId, objeto.GetId())
            wx.PostEvent(objeto.GetEventHandler(), ev)
        if str(type(objeto)) == "<class 'wx._controls.RadioButton'>":
            datosRedo = copy.deepcopy(objeto.GetParent().diccionario[objeto.GetParent().Name + '.radios'])
            objeto.GetParent().diccionario[objeto.GetParent().Name + '.radios'] = self.datos
        else:
            datosRedo = copy.deepcopy(objeto.GetParent().diccionario[objeto.GetParent().Name + '.' + objeto.Name])
            objeto.GetParent().diccionario[objeto.GetParent().Name + '.' + objeto.Name] = self.datos
        if opcion == 0:
            objeto.GetParent().parent.parent.parent.pilaRedo.apilar(MiniEventoUndo(self.accion, datosRedo), True)
        elif opcion == 1:
            objeto.GetParent().parent.parent.parent.pilaUndo.apilar(MiniEventoUndo(self.accion, datosRedo), True)

    def borraMiniEventos(self):
        pass


class eventoUndo:
    """
    Clase: eventoUndo del modulo undo.py

    """

    def __init__(self, panelOrigen, accion, datos):
        """
        Constructor de la clase

        ARGUMENTOS:
                panelOrigen:
                accion:
                datos:
        """
        self.parent = panelOrigen
        self.accion = accion
        self.datos = datos
        self.miniEventos = undoManaggement()

    def borraMiniEventos(self):
        self.miniEventos.vaciarPila()

    def buscaElementoEnvolvente(self, nombre):
        """
        Metodo: buscaElementoEnvolvente

        ARGUMENTOS:
                nombre:
        """
        for i in self.parent.elementosArbol:
            name = self.parent.arbolCerramientos.GetItemText(i)
            if name == nombre:
                return i

    def buscaElementoInstalaciones(self, nombre):
        """
        Metodo: buscaElementoInstalaciones

        ARGUMENTOS:
                nombre:
        """
        for i in self.parent.elementosArbol:
            name = self.parent.arbolInstalaciones.GetItemText(i)
            if name == nombre:
                return i

    def buscaElementoMM(self, nombre):
        """
        Metodo: buscaElementoMM

        ARGUMENTOS:
                nombre:
        """
        for i in self.parent.elementosArbol:
            name = self.parent.Arbol.GetItemText(i)
            if name == nombre:
                return i

    def contraEvento(self, opcion):
        """
        Metodo: contraEvento

        ARGUMENTOS:
                opcion):  ##funcion a la que llamaremos una vez se ejecute la accion de UN:
        """
        datosRedo = []
        accionesRedo = []
        if self.parent.GetName() == 'panelEnvolvente':
            for i in range(len(self.accion) - 1, -1, -1):
                if self.accion[i] == 'borrar cerramiento':
                    self.parent.cerramientos.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir cerramiento')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolCerramientos)
                        self.parent.parent.SetSelection(2)
                        item = self.buscaElementoEnvolvente(self.datos[i][0][0])
                        self.parent.arbolCerramientos.SelectItem(item)
                elif self.accion[i] == 'borrar PT':
                    self.parent.puentesTermicos.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir PT')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolCerramientos)
                        self.parent.parent.SetSelection(2)
                        item = self.buscaElementoEnvolvente(self.datos[i][0][0])
                        self.parent.arbolCerramientos.SelectItem(item)
                elif self.accion[i] == 'borrar hueco':
                    self.parent.ventanas.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0].descripcion)
                    accionesRedo.append('anadir hueco')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolCerramientos)
                        self.parent.parent.SetSelection(2)
                        item = self.buscaElementoEnvolvente(self.datos[i][0].descripcion)
                        self.parent.arbolCerramientos.SelectItem(item)
                elif self.accion[i] == 'modificar cerramiento':
                    for j in range(len(self.parent.cerramientos)):
                        if self.parent.cerramientos[j][0] == self.datos[i][1]:
                            datosRedo.append([copy.deepcopy(self.parent.cerramientos[j]), self.datos[i][0][0]])
                            accionesRedo.append('modificar cerramiento')
                            self.parent.cerramientos[j] = self.datos[i][0]
                            break

                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolCerramientos)
                        self.parent.parent.SetSelection(2)
                        item = self.buscaElementoEnvolvente(self.datos[i][0][0])
                        self.parent.arbolCerramientos.SelectItem(item)
                elif self.accion[i] == 'modificar PT':
                    for j in range(len(self.parent.puentesTermicos)):
                        if self.parent.puentesTermicos[j][0] == self.datos[i][1]:
                            datosRedo.append([copy.deepcopy(self.parent.puentesTermicos[j]), self.datos[i][0][0]])
                            accionesRedo.append('modificar PT')
                            self.parent.puentesTermicos[j] = self.datos[i][0]
                            break

                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolCerramientos)
                        self.parent.parent.SetSelection(2)
                        item = self.buscaElementoEnvolvente(self.datos[i][0][0])
                        self.parent.arbolCerramientos.SelectItem(item)
                elif self.accion[i] == 'modificar hueco':
                    for j in range(len(self.parent.ventanas)):
                        if self.parent.ventanas[j].descripcion == self.datos[i][1]:
                            datosRedo.append([copy.deepcopy(self.parent.ventanas[j]), self.datos[i][0].descripcion])
                            accionesRedo.append('modificar hueco')
                            self.parent.ventanas[j] = self.datos[i][0]
                            break

                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolCerramientos)
                        self.parent.parent.SetSelection(2)
                        item = self.buscaElementoEnvolvente(self.datos[i][0].descripcion)
                        self.parent.arbolCerramientos.SelectItem(item)
                elif self.accion[i] == 'anadir cerramiento':
                    for j in range(len(self.parent.cerramientos)):
                        if i == 0:
                            self.parent.parent.SetSelection(2)
                            item = self.buscaElementoEnvolvente(self.datos[i])
                            self.parent.arbolCerramientos.SelectItem(item)
                        if self.parent.cerramientos[j][0] == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.cerramientos[j]), j])
                            accionesRedo.append('borrar cerramiento')
                            self.parent.cerramientos.pop(j)
                            break

                    self.parent.cargarArbol(self.parent.arbolCerramientos)
                elif self.accion[i] == 'anadir PT':
                    for j in range(len(self.parent.puentesTermicos)):
                        if i == 0:
                            self.parent.parent.SetSelection(2)
                            item = self.buscaElementoEnvolvente(self.datos[i])
                            self.parent.arbolCerramientos.SelectItem(item)
                        if self.parent.puentesTermicos[j][0] == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.puentesTermicos[j]), j])
                            accionesRedo.append('borrar PT')
                            self.parent.puentesTermicos.pop(j)
                            break

                    self.parent.cargarArbol(self.parent.arbolCerramientos)
                elif self.accion[i] == 'anadir hueco':
                    for j in range(len(self.parent.ventanas)):
                        if i == 0:
                            self.parent.parent.SetSelection(2)
                            item = self.buscaElementoEnvolvente(self.datos[i])
                            self.parent.arbolCerramientos.SelectItem(item)
                        if self.parent.ventanas[j].descripcion == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.ventanas[j]), j])
                            accionesRedo.append('borrar hueco')
                            self.parent.ventanas.pop(j)
                            break

                    self.parent.cargarArbol(self.parent.arbolCerramientos)
                elif self.accion[i] == 'anadir zona':
                    for j in range(len(self.parent.parent.subgrupos)):
                        if i == 0:
                            self.parent.parent.SetSelection(2)
                            item = self.buscaElementoEnvolvente(self.datos[i])
                            self.parent.arbolCerramientos.SelectItem(item)
                        if self.parent.parent.subgrupos[j].nombre == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.parent.subgrupos[j]), j])
                            accionesRedo.append('borrar zona')
                            self.parent.parent.subgrupos.pop(j)
                            break

                    self.parent.cargarArbol(self.parent.arbolCerramientos)
                elif self.accion[i] == 'modificar zona':
                    for j in range(len(self.parent.parent.subgrupos)):
                        if self.parent.parent.subgrupos[j].nombre == self.datos[i][1]:
                            datosRedo.append([copy.deepcopy(self.parent.parent.subgrupos[j]), self.datos[i][0].nombre])
                            accionesRedo.append('modificar zona')
                            self.parent.parent.subgrupos[j] = self.datos[i][0]
                            break

                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolCerramientos)
                        self.parent.parent.SetSelection(2)
                        item = self.buscaElementoEnvolvente(self.datos[i][0].nombre)
                        self.parent.arbolCerramientos.SelectItem(item)
                elif self.accion[i] == 'borrar zona':
                    self.parent.parent.subgrupos.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0].nombre)
                    self.parent.parent.subgrupos.insert(self.datos[i][1], self.datos[i][0])
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolCerramientos)
                        self.parent.parent.SetSelection(2)
                        item = self.buscaElementoEnvolvente(self.datos[i][0].nombre)
                        self.parent.arbolCerramientos.SelectItem(item)
                elif self.accion[i] == 'borrar ACS':
                    self.parent.parent.parent.panelInstalaciones.ACS.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir ACS')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolCerramientos)
                        self.parent.parent.SetSelection(2)
                        item = self.buscaElementoEnvolvente(self.datos[i][0][0])
                        self.parent.arbolCerramientos.SelectItem(item)
                elif self.accion[i] == 'borrar Calefaccion':
                    self.parent.parent.parent.panelInstalaciones.calefaccion.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Calefaccion')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolCerramientos)
                        self.parent.parent.SetSelection(2)
                        item = self.buscaElementoEnvolvente(self.datos[i][0][0])
                        self.parent.arbolCerramientos.SelectItem(item)
                elif self.accion[i] == 'borrar Refrigeracion':
                    self.parent.parent.parent.panelInstalaciones.refrigeracion.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Refrigeracion')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolCerramientos)
                        self.parent.parent.SetSelection(2)
                        item = self.buscaElementoEnvolvente(self.datos[i][0][0])
                        self.parent.arbolCerramientos.SelectItem(item)
                elif self.accion[i] == 'borrar Climatizacion':
                    self.parent.parent.parent.panelInstalaciones.climatizacion.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Climatizacion')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolCerramientos)
                        self.parent.parent.SetSelection(2)
                        item = self.buscaElementoEnvolvente(self.datos[i][0][0])
                        self.parent.arbolCerramientos.SelectItem(item)
                elif self.accion[i] == 'borrar Mixto2':
                    self.parent.parent.parent.panelInstalaciones.mixto2.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Mixto2')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolCerramientos)
                        self.parent.parent.SetSelection(2)
                        item = self.buscaElementoEnvolvente(self.datos[i][0][0])
                        self.parent.arbolCerramientos.SelectItem(item)
                elif self.accion[i] == 'borrar Mixto3':
                    self.parent.parent.parent.panelInstalaciones.mixto3.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Mixto3')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolCerramientos)
                        self.parent.parent.SetSelection(2)
                        item = self.buscaElementoEnvolvente(self.datos[i][0][0])
                        self.parent.arbolCerramientos.SelectItem(item)
                elif self.accion[i] == 'borrar Contribuciones':
                    self.parent.parent.parent.panelInstalaciones.contribuciones.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Contribuciones')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolCerramientos)
                        self.parent.parent.SetSelection(2)
                        item = self.buscaElementoEnvolvente(self.datos[i][0][0])
                        self.parent.arbolCerramientos.SelectItem(item)
                elif self.accion[i] == 'borrar Iluminacion':
                    self.parent.parent.parent.panelInstalaciones.iluminacion.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Iluminacion')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolCerramientos)
                        self.parent.parent.SetSelection(2)
                        item = self.buscaElementoEnvolvente(self.datos[i][0][0])
                        self.parent.arbolCerramientos.SelectItem(item)
                elif self.accion[i] == 'borrar Ventilacion':
                    self.parent.parent.parent.panelInstalaciones.ventilacion.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Ventilacion')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolCerramientos)
                        self.parent.parent.SetSelection(2)
                        item = self.buscaElementoEnvolvente(self.datos[i][0][0])
                        self.parent.arbolCerramientos.SelectItem(item)
                elif self.accion[i] == 'borrar Ventiladores':
                    self.parent.parent.parent.panelInstalaciones.ventiladores.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Ventiladores')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolCerramientos)
                        self.parent.parent.SetSelection(2)
                        item = self.buscaElementoEnvolvente(self.datos[i][0][0])
                        self.parent.arbolCerramientos.SelectItem(item)
                elif self.accion[i] == 'borrar Bombas':
                    self.parent.parent.parent.panelInstalaciones.bombas.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Bombas')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolCerramientos)
                        self.parent.parent.SetSelection(2)
                        item = self.buscaElementoEnvolvente(self.datos[i][0][0])
                        self.parent.arbolCerramientos.SelectItem(item)
                elif self.accion[i] == 'borrar Torres':
                    self.parent.parent.parent.panelInstalaciones.torresRefrigeracion.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Torres')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolCerramientos)
                        self.parent.parent.SetSelection(2)
                        item = self.buscaElementoEnvolvente(self.datos[i][0][0])
                        self.parent.arbolCerramientos.SelectItem(item)
                elif self.accion[i] == 'anadir ACS':
                    for j in range(len(self.parent.parent.parent.panelInstalaciones.ACS)):
                        if self.parent.parent.parent.panelInstalaciones.ACS[j][0] == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.parent.parent.panelInstalaciones.ACS[j]), j])
                            accionesRedo.append('borrar ACS')
                            self.parent.parent.parent.panelInstalaciones.ACS.pop(j)
                            break

                    self.parent.parent.parent.panelInstalaciones.cargarArbol(self.parent.parent.parent.panelInstalaciones.arbolInstalaciones)
                elif self.accion[i] == 'anadir Calefaccion':
                    for j in range(len(self.parent.parent.parent.panelInstalaciones.calefaccion)):
                        if self.parent.parent.parent.panelInstalaciones.calefaccion[j][0] == self.datos[i]:
                            datosRedo.append([
                             copy.deepcopy(self.parent.parent.parent.panelInstalaciones.calefaccion[j]), j])
                            accionesRedo.append('borrar Calefaccion')
                            self.parent.parent.parent.panelInstalaciones.calefaccion.pop(j)
                            break

                    self.parent.parent.parent.panelInstalaciones.cargarArbol(self.parent.parent.parent.panelInstalaciones.arbolInstalaciones)
                elif self.accion[i] == 'anadir Refrigeracion':
                    for j in range(len(self.parent.refrigeracion)):
                        if self.parent.parent.parent.panelInstalaciones.refrigeracion[j][0] == self.datos[i]:
                            datosRedo.append([
                             copy.deepcopy(self.parent.parent.parent.panelInstalaciones.refrigeracion[j]), j])
                            accionesRedo.append('borrar Refrigeracion')
                            self.parent.parent.parent.panelInstalaciones.refrigeracion.pop(j)
                            break

                    self.parent.parent.parent.panelInstalaciones.cargarArbol(self.parent.parent.parent.panelInstalaciones.arbolInstalaciones)
                elif self.accion[i] == 'anadir Climatizacion':
                    for j in range(len(self.parent.parent.parent.panelInstalaciones.climatizacion)):
                        if self.parent.parent.parent.panelInstalaciones.climatizacion[j][0] == self.datos[i]:
                            datosRedo.append([
                             copy.deepcopy(self.parent.parent.parent.panelInstalaciones.climatizacion[j]), j])
                            accionesRedo.append('borrar Climatizacion')
                            self.parent.parent.parent.panelInstalaciones.climatizacion.pop(j)
                            break

                    self.parent.parent.parent.panelInstalaciones.cargarArbol(self.parent.parent.parent.panelInstalaciones.arbolInstalaciones)
                elif self.accion[i] == 'anadir Mixto2':
                    for j in range(len(self.parent.parent.parent.panelInstalaciones.mixto2)):
                        if self.parent.parent.parent.panelInstalaciones.mixto2[j][0] == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.parent.parent.panelInstalaciones.mixto2[j]), j])
                            accionesRedo.append('borrar Mixto2')
                            self.parent.parent.parent.panelInstalaciones.mixto2.pop(j)
                            break

                    self.parent.parent.parent.panelInstalaciones.cargarArbol(self.parent.parent.parent.panelInstalaciones.arbolInstalaciones)
                elif self.accion[i] == 'anadir Mixto3':
                    for j in range(len(self.parent.parent.parent.panelInstalaciones.mixto3)):
                        if self.parent.parent.parent.panelInstalaciones.mixto3[j][0] == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.parent.parent.panelInstalaciones.mixto3[j]), j])
                            accionesRedo.append('borrar Mixto3')
                            self.parent.parent.parent.panelInstalaciones.mixto3.pop(j)
                            break

                    self.parent.parent.parent.panelInstalaciones.cargarArbol(self.parent.parent.parent.panelInstalaciones.arbolInstalaciones)
                elif self.accion[i] == 'anadir Contribuciones':
                    for j in range(len(self.parent.parent.parent.panelInstalaciones.contribuciones)):
                        if self.parent.parent.parent.panelInstalaciones.contribuciones[j][0] == self.datos[i]:
                            datosRedo.append([
                             copy.deepcopy(self.parent.parent.parent.panelInstalaciones.contribuciones[j]), j])
                            accionesRedo.append('borrar Contribuciones')
                            self.parent.parent.parent.panelInstalaciones.contribuciones.pop(j)
                            break

                    self.parent.parent.parent.panelInstalaciones.cargarArbol(self.parent.parent.parent.panelInstalaciones.arbolInstalaciones)
                elif self.accion[i] == 'anadir Iluminacion':
                    for j in range(len(self.parent.parent.parent.panelInstalaciones.iluminacion)):
                        if self.parent.parent.parent.panelInstalaciones.iluminacion[j][0] == self.datos[i]:
                            datosRedo.append([
                             copy.deepcopy(self.parent.parent.parent.panelInstalaciones.iluminacion[j]), j])
                            accionesRedo.append('borrar Iluminacion')
                            self.parent.parent.parent.panelInstalaciones.iluminacion.pop(j)
                            break

                    self.parent.parent.parent.panelInstalaciones.cargarArbol(self.parent.parent.parent.panelInstalaciones.arbolInstalaciones)
                elif self.accion[i] == 'anadir Ventilacion':
                    for j in range(len(self.parent.parent.parent.panelInstalaciones.ventilacion)):
                        if self.parent.parent.parent.panelInstalaciones.ventilacion[j][0] == self.datos[i]:
                            datosRedo.append([
                             copy.deepcopy(self.parent.parent.parent.panelInstalaciones.ventilacion[j]), j])
                            accionesRedo.append('borrar Ventilacion')
                            self.parent.parent.parent.panelInstalaciones.ventilacion.pop(j)
                            break

                    self.parent.parent.parent.panelInstalaciones.cargarArbol(self.parent.parent.parent.panelInstalaciones.arbolInstalaciones)
                elif self.accion[i] == 'anadir Ventiladores':
                    for j in range(len(self.parent.parent.parent.panelInstalaciones.ventiladores)):
                        if self.parent.parent.parent.panelInstalaciones.ventiladores[j][0] == self.datos[i]:
                            datosRedo.append([
                             copy.deepcopy(self.parent.parent.parent.panelInstalaciones.ventiladores[j]), j])
                            accionesRedo.append('borrar Ventiladores')
                            self.parent.parent.parent.panelInstalaciones.ventiladores.pop(j)
                            break

                    self.parent.parent.parent.panelInstalaciones.cargarArbol(self.parent.parent.parent.panelInstalaciones.arbolInstalaciones)
                elif self.accion[i] == 'anadir Bombas':
                    for j in range(len(self.parent.parent.parent.panelInstalaciones.bombas)):
                        if self.parent.parent.parent.panelInstalaciones.bombas[j][0] == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.parent.parent.panelInstalaciones.bombas[j]), j])
                            accionesRedo.append('borrar Bombas')
                            self.parent.parent.parent.panelInstalaciones.bombas.pop(j)
                            break

                    self.parent.parent.parent.panelInstalaciones.cargarArbol(self.parent.parent.parent.panelInstalaciones.arbolInstalaciones)
                elif self.accion[i] == 'anadir Torres':
                    for j in range(len(self.parent.parent.parent.panelInstalaciones.torresRefrigeracion)):
                        if self.parent.parent.parent.panelInstalaciones.torresRefrigeracion[j][0] == self.datos[i]:
                            datosRedo.append([
                             copy.deepcopy(self.parent.parent.parent.panelInstalaciones.torresRefrigeracion[j]), j])
                            accionesRedo.append('borrar Torres')
                            self.parent.parent.parent.panelInstalaciones.torresRefrigeracion.pop(j)
                            break

                    self.parent.parent.parent.panelInstalaciones.cargarArbol(self.parent.parent.parent.panelInstalaciones.arbolInstalaciones)

            if opcion == 0:
                self.parent.parent.parent.pilaRedo.apilar(eventoUndo(self.parent, accionesRedo, datosRedo))
            elif opcion == 1:
                self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, accionesRedo, datosRedo))
        elif self.parent.GetName() == 'panelInstalaciones':
            for i in range(len(self.accion) - 1, -1, -1):
                if self.accion[i] == 'borrar ACS':
                    self.parent.ACS.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir ACS')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'borrar Calefaccion':
                    self.parent.calefaccion.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Calefaccion')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'borrar Refrigeracion':
                    self.parent.refrigeracion.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Refrigeracion')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'borrar Climatizacion':
                    self.parent.climatizacion.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Climatizacion')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'borrar Mixto2':
                    self.parent.mixto2.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Mixto2')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'borrar Mixto3':
                    self.parent.mixto3.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Mixto3')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'borrar Contribuciones':
                    self.parent.contribuciones.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Contribuciones')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'borrar Iluminacion':
                    self.parent.iluminacion.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Iluminacion')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'borrar Ventilacion':
                    self.parent.ventilacion.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Ventilacion')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'borrar Ventiladores':
                    self.parent.ventiladores.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Ventiladores')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'borrar Bombas':
                    self.parent.bombas.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Bombas')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'borrar Torres':
                    self.parent.torresRefrigeracion.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir Torres')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'modificar ACS':
                    for j in range(len(self.parent.ACS)):
                        if self.parent.ACS[j][0] == self.datos[i][1]:
                            datosRedo.append([copy.deepcopy(self.parent.ACS[j]), self.datos[i][0][0]])
                            accionesRedo.append('modificar ACS')
                            self.parent.ACS[j] = self.datos[i][0]
                            break

                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'modificar Calefaccion':
                    for j in range(len(self.parent.calefaccion)):
                        if self.parent.calefaccion[j][0] == self.datos[i][1]:
                            datosRedo.append([copy.deepcopy(self.parent.calefaccion[j]), self.datos[i][0][0]])
                            accionesRedo.append('modificar Calefaccion')
                            self.parent.calefaccion[j] = self.datos[i][0]
                            break

                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'modificar Refrigeracion':
                    for j in range(len(self.parent.refrigeracion)):
                        if self.parent.refrigeracion[j][0] == self.datos[i][1]:
                            datosRedo.append([copy.deepcopy(self.parent.refrigeracion[j]), self.datos[i][0][0]])
                            accionesRedo.append('modificar Refrigeracion')
                            self.parent.refrigeracion[j] = self.datos[i][0]
                            break

                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'modificar Climatizacion':
                    for j in range(len(self.parent.climatizacion)):
                        if self.parent.climatizacion[j][0] == self.datos[i][1]:
                            datosRedo.append([copy.deepcopy(self.parent.climatizacion[j]), self.datos[i][0][0]])
                            accionesRedo.append('modificar Climatizacion')
                            self.parent.climatizacion[j] = self.datos[i][0]
                            break

                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'modificar Mixto2':
                    for j in range(len(self.parent.mixto2)):
                        if self.parent.mixto2[j][0] == self.datos[i][1]:
                            datosRedo.append([copy.deepcopy(self.parent.mixto2[j]), self.datos[i][0][0]])
                            accionesRedo.append('modificar Mixto2')
                            self.parent.mixto2[j] = self.datos[i][0]
                            break

                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'modificar Mixto3':
                    for j in range(len(self.parent.mixto3)):
                        if self.parent.mixto3[j][0] == self.datos[i][1]:
                            datosRedo.append([copy.deepcopy(self.parent.mixto3[j]), self.datos[i][0][0]])
                            accionesRedo.append('modificar Mixto3')
                            self.parent.mixto3[j] = self.datos[i][0]
                            break

                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'modificar Contribuciones':
                    for j in range(len(self.parent.contribuciones)):
                        if self.parent.contribuciones[j][0] == self.datos[i][1]:
                            datosRedo.append([copy.deepcopy(self.parent.contribuciones[j]), self.datos[i][0][0]])
                            accionesRedo.append('modificar Contribuciones')
                            self.parent.contribuciones[j] = self.datos[i][0]
                            break

                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'modificar Iluminacion':
                    for j in range(len(self.parent.iluminacion)):
                        if self.parent.iluminacion[j][0] == self.datos[i][1]:
                            datosRedo.append([copy.deepcopy(self.parent.iluminacion[j]), self.datos[i][0][0]])
                            accionesRedo.append('modificar Iluminacion')
                            self.parent.iluminacion[j] = self.datos[i][0]
                            break

                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'modificar Ventilacion':
                    for j in range(len(self.parent.ventilacion)):
                        if self.parent.ventilacion[j][0] == self.datos[i][1]:
                            datosRedo.append([copy.deepcopy(self.parent.ventilacion[j]), self.datos[i][0][0]])
                            accionesRedo.append('modificar Ventilacion')
                            self.parent.ventilacion[j] = self.datos[i][0]
                            break

                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'modificar Ventiladores':
                    for j in range(len(self.parent.ventiladores)):
                        if self.parent.ventiladores[j][0] == self.datos[i][1]:
                            datosRedo.append([copy.deepcopy(self.parent.ventiladores[j]), self.datos[i][0][0]])
                            accionesRedo.append('modificar Ventiladores')
                            self.parent.ventiladores[j] = self.datos[i][0]
                            break

                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'modificar Bombas':
                    for j in range(len(self.parent.bombas)):
                        if self.parent.bombas[j][0] == self.datos[i][1]:
                            datosRedo.append([copy.deepcopy(self.parent.bombas[j]), self.datos[i][0][0]])
                            accionesRedo.append('modificar Bombas')
                            self.parent.bombas[j] = self.datos[i][0]
                            break

                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'modificar Torres':
                    for j in range(len(self.parent.torresRefrigeracion)):
                        if self.parent.torresRefrigeracion[j][0] == self.datos[i][1]:
                            datosRedo.append([copy.deepcopy(self.parent.torresRefrigeracion[j]), self.datos[i][0][0]])
                            accionesRedo.append('modificar Torres')
                            self.parent.torresRefrigeracion[j] = self.datos[i][0]
                            break

                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0][0])
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'anadir ACS':
                    for j in range(len(self.parent.ACS)):
                        if self.parent.ACS[j][0] == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.ACS[j]), j])
                            accionesRedo.append('borrar ACS')
                            self.parent.ACS.pop(j)
                            break

                    self.parent.cargarArbol(self.parent.arbolInstalaciones)
                elif self.accion[i] == 'anadir Calefaccion':
                    for j in range(len(self.parent.calefaccion)):
                        if self.parent.calefaccion[j][0] == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.calefaccion[j]), j])
                            accionesRedo.append('borrar Calefaccion')
                            self.parent.calefaccion.pop(j)
                            break

                    self.parent.cargarArbol(self.parent.arbolInstalaciones)
                elif self.accion[i] == 'anadir Refrigeracion':
                    for j in range(len(self.parent.refrigeracion)):
                        if self.parent.refrigeracion[j][0] == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.refrigeracion[j]), j])
                            accionesRedo.append('borrar Refrigeracion')
                            self.parent.refrigeracion.pop(j)
                            break

                    self.parent.cargarArbol(self.parent.arbolInstalaciones)
                elif self.accion[i] == 'anadir Climatizacion':
                    for j in range(len(self.parent.climatizacion)):
                        if self.parent.climatizacion[j][0] == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.climatizacion[j]), j])
                            accionesRedo.append('borrar Climatizacion')
                            self.parent.climatizacion.pop(j)
                            break

                    self.parent.cargarArbol(self.parent.arbolInstalaciones)
                elif self.accion[i] == 'anadir Mixto2':
                    for j in range(len(self.parent.mixto2)):
                        if self.parent.mixto2[j][0] == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.mixto2[j]), j])
                            accionesRedo.append('borrar Mixto2')
                            self.parent.mixto2.pop(j)
                            break

                    self.parent.cargarArbol(self.parent.arbolInstalaciones)
                elif self.accion[i] == 'anadir Mixto3':
                    for j in range(len(self.parent.mixto3)):
                        if self.parent.mixto3[j][0] == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.mixto3[j]), j])
                            accionesRedo.append('borrar Mixto3')
                            self.parent.mixto3.pop(j)
                            break

                    self.parent.cargarArbol(self.parent.arbolInstalaciones)
                elif self.accion[i] == 'anadir Contribuciones':
                    for j in range(len(self.parent.contribuciones)):
                        if self.parent.contribuciones[j][0] == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.contribuciones[j]), j])
                            accionesRedo.append('borrar Contribuciones')
                            self.parent.contribuciones.pop(j)
                            break

                    self.parent.cargarArbol(self.parent.arbolInstalaciones)
                elif self.accion[i] == 'anadir Iluminacion':
                    for j in range(len(self.parent.iluminacion)):
                        if self.parent.iluminacion[j][0] == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.iluminacion[j]), j])
                            accionesRedo.append('borrar Iluminacion')
                            self.parent.iluminacion.pop(j)
                            break

                    self.parent.cargarArbol(self.parent.arbolInstalaciones)
                elif self.accion[i] == 'anadir Ventilacion':
                    for j in range(len(self.parent.ventilacion)):
                        if self.parent.ventilacion[j][0] == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.ventilacion[j]), j])
                            accionesRedo.append('borrar Ventilacion')
                            self.parent.ventilacion.pop(j)
                            break

                    self.parent.cargarArbol(self.parent.arbolInstalaciones)
                elif self.accion[i] == 'anadir Ventiladores':
                    for j in range(len(self.parent.ventiladores)):
                        if self.parent.ventiladores[j][0] == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.ventiladores[j]), j])
                            accionesRedo.append('borrar Ventiladores')
                            self.parent.ventiladores.pop(j)
                            break

                    self.parent.cargarArbol(self.parent.arbolInstalaciones)
                elif self.accion[i] == 'anadir Bombas':
                    for j in range(len(self.parent.bombas)):
                        if self.parent.bombas[j][0] == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.bombas[j]), j])
                            accionesRedo.append('borrar Bombas')
                            self.parent.bombas.pop(j)
                            break

                    self.parent.cargarArbol(self.parent.arbolInstalaciones)
                elif self.accion[i] == 'anadir Torres':
                    for j in range(len(self.parent.torresRefrigeracion)):
                        if self.parent.torresRefrigeracion[j][0] == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.torresRefrigeracion[j]), j])
                            accionesRedo.append('borrar Torres')
                            self.parent.torresRefrigeracion.pop(j)
                            break

                    self.parent.cargarArbol(self.parent.arbolInstalaciones)
                elif self.accion[i] == 'borrar zona':
                    self.parent.parent.subgrupos.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0].nombre)
                    accionesRedo.append('anadir zona')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0].nombre)
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'anadir zona':
                    for j in range(len(self.parent.parent.subgrupos)):
                        if self.parent.parent.subgrupos[j].nombre == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.parent.subgrupos[j]), j])
                            accionesRedo.append('borrar zona')
                            self.parent.parent.subgrupos.pop(j)
                            break

                    self.parent.cargarArbol(self.parent.arbolInstalaciones)
                elif self.accion[i] == 'modificar zona':
                    for j in range(len(self.parent.parent.subgrupos)):
                        if self.parent.parent.subgrupos[j].nombre == self.datos[i][1]:
                            datosRedo.append([copy.deepcopy(self.parent.parent.subgrupos[j]), self.datos[i][0].nombre])
                            accionesRedo.append('modificar zona')
                            self.parent.parent.subgrupos[j] = self.datos[i][0]
                            break

                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0].nombre)
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'borrar cerramiento':
                    self.parent.parent.parent.panelEnvolvente.cerramientos.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir cerramiento')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0].nombre)
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'borrar PT':
                    self.parent.parent.parent.panelEnvolvente.puentesTermicos.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0][0])
                    accionesRedo.append('anadir PT')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0].nombre)
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'borrar hueco':
                    self.parent.parent.parent.panelEnvolvente.ventanas.insert(self.datos[i][1], self.datos[i][0])
                    datosRedo.append(self.datos[i][0].descripcion)
                    accionesRedo.append('anadir hueco')
                    if i == 0:
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        self.parent.parent.SetSelection(3)
                        item = self.buscaElementoInstalaciones(self.datos[i][0].nombre)
                        self.parent.arbolInstalaciones.SelectItem(item)
                elif self.accion[i] == 'anadir cerramiento':
                    for j in range(len(self.parent.parent.parent.panelEnvolvente.cerramientos)):
                        if self.parent.parent.parent.panelEnvolvente.cerramientos[j][0] == self.datos[i]:
                            datosRedo.append([
                             copy.deepcopy(self.parent.parent.parent.panelEnvolvente.cerramientos[j]), j])
                            accionesRedo.append('borrar cerramiento')
                            self.parent.parent.parent.panelEnvolvente.cerramientos.pop(j)
                            break

                    self.parent.parent.parent.panelEnvolvente.cargarArbol(self.parent.parent.parent.panelEnvolvente.arbolCerramientos)
                elif self.accion[i] == 'anadir PT':
                    for j in range(len(self.parent.parent.parent.panelEnvolvente.puentesTermicos)):
                        if self.parent.parent.parent.panelEnvolvente.puentesTermicos[j][0] == self.datos[i]:
                            datosRedo.append([
                             copy.deepcopy(self.parent.parent.parent.panelEnvolvente.puentesTermicos[j]), j])
                            accionesRedo.append('borrar PT')
                            self.parent.parent.parent.panelEnvolvente.puentesTermicos.pop(j)
                            break

                    self.parent.parent.parent.panelEnvolvente.cargarArbol(self.parent.parent.parent.panelEnvolvente.arbolCerramientos)
                elif self.accion[i] == 'anadir hueco':
                    for j in range(len(self.parent.parent.parent.panelEnvolvente.ventanas)):
                        if self.parent.parent.parent.panelEnvolvente.ventanas[j].descripcion == self.datos[i]:
                            datosRedo.append([copy.deepcopy(self.parent.parent.parent.panelEnvolvente.ventanas[j]), j])
                            accionesRedo.append('borrar hueco')
                            self.parent.parent.parent.panelEnvolvente.ventanas.pop(j)
                            break

                    self.parent.parent.parent.panelEnvolvente.cargarArbol(self.parent.parent.parent.panelEnvolvente.arbolCerramientos)

            if opcion == 0:
                self.parent.parent.parent.pilaRedo.apilar(eventoUndo(self.parent, accionesRedo, datosRedo))
            elif opcion == 1:
                self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, accionesRedo, datosRedo))
        elif self.parent.GetName() == 'panelMedidasMejora':
            if self.accion == 'borrar conjunto':
                self.parent.ListadoMedidasUsuario.insert(self.datos[1], self.datos[0])
                datosRedo = self.datos[0].nombre
                accionesRedo = 'anadir conjunto'
                self.parent.cargarArbol(self.parent.Arbol)
                item = self.buscaElementoMM(self.datos[0].nombre)
                self.parent.Arbol.SelectItem(item)
                self.parent.Arbol.Expand(item)
            elif self.accion == 'modificar conjunto':
                for i in range(len(self.parent.ListadoMedidasUsuario)):
                    if self.parent.ListadoMedidasUsuario[i].nombre == self.datos[1]:
                        datosRedo = [
                         copy.deepcopy(self.parent.ListadoMedidasUsuario[i]), self.datos[0].nombre]
                        accionesRedo = 'modificar conjunto'
                        self.parent.ListadoMedidasUsuario[i] = self.datos[0]
                        break

                self.parent.cargarArbol(self.parent.Arbol)
                item = self.buscaElementoMM(self.datos[0].nombre)
                self.parent.Arbol.SelectItem(item)
                self.parent.Arbol.Expand(item)
            elif self.accion == 'anadir conjunto':
                for i in range(len(self.parent.ListadoMedidasUsuario)):
                    if self.parent.ListadoMedidasUsuario[i].nombre == self.datos:
                        datosRedo = [
                         copy.deepcopy(self.parent.ListadoMedidasUsuario[i]), i]
                        accionesRedo = 'borrar conjunto'
                        self.parent.ListadoMedidasUsuario.pop(i)
                        break

                self.parent.cargarArbol(self.parent.Arbol)
            if opcion == 0:
                self.parent.parent.parent.pilaRedo.apilar(eventoUndo(self.parent, accionesRedo, datosRedo))
            elif opcion == 1:
                self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, accionesRedo, datosRedo))
        elif self.parent.GetName() == 'panelDatosGenerales':
            self.parent.parent.SetSelection(1)
            if self.accion == 'anoConstruccionChoice':
                datosRedo = copy.deepcopy(self.parent.diccionario['anoConstruccionChoice'])
                accionesRedo = 'anoConstruccionChoice'
                self.parent.anoConstruccionChoice.SetSelection(self.datos)
                self.parent.diccionario['anoConstruccionChoice'] = self.datos
                self.parent.OnAnoConstruccionChoice(None)
            elif self.accion == 'provinciaChoice':
                datosRedo = copy.deepcopy(self.parent.diccionario['provinciaChoice'])
                accionesRedo = 'provinciaChoice'
                self.parent.provinciaChoice.SetSelection(self.datos)
                self.parent.parent.parent.panelDatosAdministrativos.provinciaChoice.SetSelection(self.datos)
                self.parent.diccionario['provinciaChoice'] = self.datos
                self.parent.OnProvinciaChoice(None)
                self.parent.parent.parent.panelDatosAdministrativos.OnProvinciaChoice(None)
            elif self.accion == 'tipoEdificioChoice':
                datosRedo = copy.deepcopy(self.parent.diccionario['tipoEdificioChoice'])
                accionesRedo = 'tipoEdificioChoice'
                self.parent.tipoEdificioChoice.SetSelection(self.datos)
                self.parent.diccionario['tipoEdificioChoice'] = self.datos
                self.parent.OnTipoEdificioChoice(None)
            elif self.accion == 'masaParticiones':
                datosRedo = copy.deepcopy(self.parent.diccionario['masaParticiones'])
                accionesRedo = 'masaParticiones'
                self.parent.masaParticiones.SetSelection(self.datos)
                self.parent.diccionario['masaParticiones'] = self.datos
                self.parent.OnMasaParticiones(None)
            elif self.accion == 'choice1':
                datosRedo = copy.deepcopy(self.parent.diccionario['choice1'])
                accionesRedo = 'choice1'
                self.parent.localidadChoice.SetSelection(self.datos)
                self.parent.parent.parent.panelDatosAdministrativos.localidadChoice.SetSelection(self.datos)
                self.parent.diccionario['choice1'] = self.datos
                self.parent.OnLocalidadChoice(None)
                self.parent.parent.parent.panelDatosAdministrativos.OnLocalidadChoice(None)
            elif self.accion == 'he1':
                datosRedo = copy.deepcopy(self.parent.diccionario['he1'])
                accionesRedo = 'he1'
                self.parent.HE1.SetSelection(self.datos)
                self.parent.diccionario['he1'] = self.datos
                self.parent.OnHE1(None)
            elif self.accion == 'he4':
                datosRedo = copy.deepcopy(self.parent.diccionario['he4'])
                accionesRedo = 'he4'
                self.parent.HE4.SetSelection(self.datos)
                self.parent.diccionario['he4'] = self.datos
                self.parent.OnHE4(None)
            elif self.accion == 'BlowerDoorCheck':
                datosRedo = copy.deepcopy(self.parent.diccionario['BlowerDoorCheck'])
                accionesRedo = 'BlowerDoorCheck'
                self.parent.BlowerDoorCheck.SetValue(self.datos)
                self.parent.diccionario['BlowerDoorCheck'] = self.datos
                self.parent.OnBlowerDoorCheck(None)
            elif self.accion == 'Extrapeninsular':
                datosRedo = copy.deepcopy(self.parent.diccionario['Extrapeninsular'])
                accionesRedo = 'Extrapeninsular'
                self.parent.Extrapeninsular.SetValue(self.datos)
                self.parent.diccionario['Extrapeninsular'] = self.datos
                self.parent.OnExtrapeninsularCheckBox(None)
            elif self.accion == 'ExentoHE4':
                datosRedo = copy.deepcopy(self.parent.diccionario['ExentoHE4'])
                accionesRedo = 'ExentoHE4'
                self.parent.ExentoHE4.SetValue(self.datos)
                self.parent.diccionario['ExentoHE4'] = self.datos
                self.parent.OnExentoHE4(None)
            elif self.accion == 'superficie':
                datosRedo = copy.deepcopy(self.parent.diccionario['superficie'])
                accionesRedo = 'superficie'
                self.parent.superficie.ChangeValue(self.datos)
                self.parent.diccionario['superficie'] = self.datos
            elif self.accion == 'alturaMediaLibre':
                datosRedo = copy.deepcopy(self.parent.diccionario['alturaMediaLibre'])
                accionesRedo = 'alturaMediaLibre'
                self.parent.alturaMediaLibre.ChangeValue(self.datos)
                self.parent.diccionario['alturaMediaLibre'] = self.datos
            elif self.accion == 'numeroPlantas':
                datosRedo = copy.deepcopy(self.parent.diccionario['numeroPlantas'])
                accionesRedo = 'numeroPlantas'
                self.parent.numeroPlantas.ChangeValue(self.datos)
                self.parent.diccionario['numeroPlantas'] = self.datos
            elif self.accion == 'ventilacion':
                datosRedo = copy.deepcopy(self.parent.diccionario['ventilacion'])
                accionesRedo = 'ventilacion'
                self.parent.ventilacion.ChangeValue(self.datos)
                self.parent.diccionario['ventilacion'] = self.datos
            elif self.accion == 'consumoACS':
                datosRedo = copy.deepcopy(self.parent.diccionario['consumoACS'])
                accionesRedo = 'consumoACS'
                self.parent.consumoACS.ChangeValue(self.datos)
                self.parent.diccionario['consumoACS'] = self.datos
            elif self.accion == 'Q50Cuadro':
                datosRedo = copy.deepcopy(self.parent.diccionario['Q50Cuadro'])
                accionesRedo = 'Q50Cuadro'
                self.parent.Q50Cuadro.ChangeValue(self.datos)
                self.parent.diccionario['Q50Cuadro'] = self.datos
            elif self.accion == 'otroCuadro':
                datosRedo = copy.deepcopy(self.parent.diccionario['otroCuadro'])
                self.parent.parent.parent.panelDatosAdministrativos.otroCuadro.SetValue(self.datos)
                accionesRedo = 'otroCuadro'
                self.parent.otroCuadro.ChangeValue(self.datos)
                self.parent.diccionario['otroCuadro'] = self.datos
            elif self.accion == 'NCuadro':
                datosRedo = copy.deepcopy(self.parent.diccionario['NCuadro'])
                accionesRedo = 'NCuadro'
                self.parent.NCuadro.ChangeValue(self.datos)
                self.parent.diccionario['NCuadro'] = self.datos
            if opcion == 0:
                self.parent.parent.parent.pilaRedo.apilar(eventoUndo(self.parent, accionesRedo, datosRedo))
            elif opcion == 1:
                self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, accionesRedo, datosRedo))
        elif self.parent.GetName() == 'panelDatosAdministrativos':
            self.parent.parent.SetSelection(0)
            if self.accion == 'nombreEdificio':
                datosRedo = copy.deepcopy(self.parent.diccionario['nombreEdificio'])
                accionesRedo = 'nombreEdificio'
                self.parent.nombreEdificio.ChangeValue(self.datos)
                self.parent.diccionario['nombreEdificio'] = self.datos
            elif self.accion == 'direccionEdificio':
                datosRedo = copy.deepcopy(self.parent.diccionario['direccionEdificio'])
                accionesRedo = 'direccionEdificio'
                self.parent.direccionEdificio.ChangeValue(self.datos)
                self.parent.diccionario['direccionEdificio'] = self.datos
            elif self.accion == 'nombreCliente':
                datosRedo = copy.deepcopy(self.parent.diccionario['nombreCliente'])
                accionesRedo = 'nombreCliente'
                self.parent.nombreCliente.ChangeValue(self.datos)
                self.parent.diccionario['nombreCliente'] = self.datos
            elif self.accion == 'contactoCliente':
                datosRedo = copy.deepcopy(self.parent.diccionario['contactoCliente'])
                accionesRedo = 'contactoCliente'
                self.parent.contactoCliente.ChangeValue(self.datos)
                self.parent.diccionario['contactoCliente'] = self.datos
            elif self.accion == 'direccionCliente':
                datosRedo = copy.deepcopy(self.parent.diccionario['direccionCliente'])
                accionesRedo = 'direccionCliente'
                self.parent.direccionCliente.ChangeValue(self.datos)
                self.parent.diccionario['direccionCliente'] = self.datos
            elif self.accion == 'telefonoCliente':
                datosRedo = copy.deepcopy(self.parent.diccionario['telefonoCliente'])
                accionesRedo = 'telefonoCliente'
                self.parent.telefonoCliente.ChangeValue(self.datos)
                self.parent.diccionario['telefonoCliente'] = self.datos
            elif self.accion == 'mailCliente':
                datosRedo = copy.deepcopy(self.parent.diccionario['mailCliente'])
                accionesRedo = 'mailCliente'
                self.parent.mailCliente.ChangeValue(self.datos)
                self.parent.diccionario['mailCliente'] = self.datos
            elif self.accion == 'certificadorEmpresa':
                datosRedo = copy.deepcopy(self.parent.diccionario['certificadorEmpresa'])
                accionesRedo = 'certificadorEmpresa'
                self.parent.certificadorEmpresa.ChangeValue(self.datos)
                self.parent.diccionario['certificadorEmpresa'] = self.datos
            elif self.accion == 'certificadorAutor':
                datosRedo = copy.deepcopy(self.parent.diccionario['certificadorAutor'])
                accionesRedo = 'certificadorAutor'
                self.parent.certificadorAutor.ChangeValue(self.datos)
                self.parent.diccionario['certificadorAutor'] = self.datos
            elif self.accion == 'certificadorTelefono':
                datosRedo = copy.deepcopy(self.parent.diccionario['certificadorTelefono'])
                accionesRedo = 'certificadorTelefono'
                self.parent.certificadorTelefono.ChangeValue(self.datos)
                self.parent.diccionario['certificadorTelefono'] = self.datos
            elif self.accion == 'certificadorMail':
                datosRedo = copy.deepcopy(self.parent.diccionario['certificadorMail'])
                accionesRedo = 'certificadorMail'
                self.parent.certificadorMail.ChangeValue(self.datos)
                self.parent.diccionario['certificadorMail'] = self.datos
            if opcion == 0:
                self.parent.parent.parent.pilaRedo.apilar(eventoUndo(self.parent, accionesRedo, datosRedo))
            elif opcion == 1:
                self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, accionesRedo, datosRedo))
        elif self.accion == 'guardar':
            self.parent.deshacerUltimoPaso(None)
        return