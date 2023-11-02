# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\panelInstalacionesBotones.pyc
# Compiled at: 2015-02-20 14:25:47
from MedidasDeMejora.funcionActualizarMMInstalacionesAlCambiarSuperficie import eliminarSubgrupoDeConjuntosMM, existenInstalacionesColgandoDeZonaModificadaOEliminadaEnConjuntosMM, actualizarSuperficieIluminacionDeConjuntosMM
from undo import eventoUndo
import Calculos.calculoSuperficies as calculoSuperficies, Instalaciones.dialogoConfirma as dialogoConfirma, copy, undo, ventanaSubgrupo, wx, logging

class panelBotones(wx.Panel):

    def _init_ctrls(self, prnt, ide, posi, siz, styl, nam):

    def __init__(self, parent, id, pos, size, style, name):
        self._init_ctrls(parent, id, pos, size, style, name)
        self.parent = parent

    def quitaBlancos(self, cadena):
        quita = True
        while quita == True:
            if cadena.endswith(' ') == True:
                cadena = cadena[0:len(cadena) - 1]
            else:
                quita = False

        return cadena

    def OnAnadirBotonButton(self, event):
        if self.parent.panelElegirObjeto.contribucionesEnergeticas != True and self.parent.panelElegirObjeto.iluminacion != True and self.parent.panelElegirObjeto.ventilacion != True and self.parent.panelElegirObjeto.ventiladores != True and self.parent.panelElegirObjeto.bombas != True and self.parent.panelElegirObjeto.torresRefrigeracion != True:
            objeto = self.parent.cogerDatosDelPanel(self.parent.panel2)
            if type(objeto) == type('hola'):
                raise Exception('Revise los siguientes campos:\n' + objeto)
                return
        else:
            objeto = self.parent.panel2.cogerDatos()
            if objeto == []:
                return
            if type(objeto) == type('hola'):
                raise Exception('Revise los siguientes campos:\n' + objeto)
                return
        objeto[0] = self.quitaBlancos(objeto[0])
        Existe = False
        tipoAntiguo = ''
        for i in range(len(self.parent.ACS)):
            if self.parent.ACS[i][0] == objeto[0]:
                Existe = True
                tipoAntiguo = self.parent.ACS[i][1]
                break

        for i in range(len(self.parent.calefaccion)):
            if self.parent.calefaccion[i][0] == objeto[0]:
                Existe = True
                tipoAntiguo = self.parent.calefaccion[i][1]
                break

        for i in range(len(self.parent.refrigeracion)):
            if self.parent.refrigeracion[i][0] == objeto[0]:
                Existe = True
                tipoAntiguo = self.parent.refrigeracion[i][1]
                break

        for i in range(len(self.parent.climatizacion)):
            if self.parent.climatizacion[i][0] == objeto[0]:
                Existe = True
                tipoAntiguo = self.parent.climatizacion[i][1]
                break

        for i in range(len(self.parent.mixto2)):
            if self.parent.mixto2[i][0] == objeto[0]:
                Existe = True
                tipoAntiguo = self.parent.mixto2[i][1]
                break

        for i in range(len(self.parent.mixto3)):
            if self.parent.mixto3[i][0] == objeto[0]:
                Existe = True
                tipoAntiguo = self.parent.mixto3[i][1]
                break

        for i in range(len(self.parent.contribuciones)):
            if self.parent.contribuciones[i][0] == objeto[0]:
                Existe = True
                tipoAntiguo = self.parent.contribuciones[i][1]
                break

        for i in range(len(self.parent.iluminacion)):
            if self.parent.iluminacion[i][0] == objeto[0]:
                Existe = True
                tipoAntiguo = self.parent.iluminacion[i][1]
                break

        for i in range(len(self.parent.ventilacion)):
            if self.parent.ventilacion[i][0] == objeto[0]:
                Existe = True
                tipoAntiguo = self.parent.ventilacion[i][1]
                break

        for i in range(len(self.parent.ventiladores)):
            if self.parent.ventiladores[i][0] == objeto[0]:
                Existe = True
                tipoAntiguo = self.parent.ventiladores[i][1]
                break

        for i in range(len(self.parent.bombas)):
            if self.parent.bombas[i][0] == objeto[0]:
                Existe = True
                tipoAntiguo = self.parent.bombas[i][1]
                break

        for i in range(len(self.parent.torresRefrigeracion)):
            if self.parent.torresRefrigeracion[i][0] == objeto[0]:
                Existe = True
                tipoAntiguo = self.parent.torresRefrigeracion[i][1]
                break

        if Existe == True:
            DeseaReemplazar = dialogoConfirma.Dialog1(self, 'El elemento que desea añadir ya existe. ¿Desea Reemplazarlo?')
            DeseaReemplazar.ShowModal()
            if DeseaReemplazar.dev == True:
                self.OnDeseaReemplazar(objeto, tipoAntiguo)
                self.Close()
                return
            if DeseaReemplazar.dev == False:
                self.Close()
                return
        else:
            accionesUndo = []
            datosUndo = []
            if objeto[1] == 'ACS':
                self.parent.ACS.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir ACS')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif objeto[1] == 'calefaccion':
                self.parent.calefaccion.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Calefaccion')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif objeto[1] == 'refrigeracion':
                self.parent.refrigeracion.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Refrigeracion')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif objeto[1] == 'climatizacion':
                self.parent.climatizacion.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Climatizacion')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif objeto[1] == 'mixto2':
                self.parent.mixto2.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Mixto2')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif objeto[1] == 'mixto3':
                self.parent.mixto3.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Mixto3')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif objeto[1] == 'renovable':
                self.parent.contribuciones.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Contribuciones')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif objeto[1] == 'iluminacion':
                self.parent.iluminacion.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Iluminacion')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif objeto[1] == 'ventilacion':
                self.parent.ventilacion.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Ventilacion')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif objeto[1] == 'ventiladores':
                self.parent.ventiladores.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Ventiladores')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif objeto[1] == 'bombas':
                self.parent.bombas.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Bombas')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif objeto[1] == 'torresRefrigeracion':
                self.parent.torresRefrigeracion.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Torres')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, accionesUndo, datosUndo))
            self.parent.parent.parent.pilaRedo = undo.undoManaggement()
        self.cargarUltimoElemento(objeto[0])

    def cargarUltimoElemento(self, nombre):
        array = []
        array = self.iterchildren(self.parent.arbolInstalaciones, self.parent.arbolInstalaciones.GetRootItem(), array)
        for i in array:
            if self.parent.arbolInstalaciones.GetItemText(i) == nombre:
                self.parent.arbolInstalaciones.SelectItem(i)
                break

    def iterchildren(self, treectrl, node, array):
        cid, citem = treectrl.GetFirstChild(node)
        while cid.IsOk():
            array.append(cid)
            if treectrl.GetChildrenCount(cid) != 0:
                self.iterchildren(treectrl, cid, array)
            cid, citem = treectrl.GetNextChild(node, citem)

        return array

    def OnDeseaReemplazar(self, objeto, tipoAntiguo):
        tipoObjeto = objeto[1]
        accionesUndo = []
        datosUndo = []
        if tipoObjeto == tipoAntiguo:
            if tipoObjeto == 'ACS':
                for i in range(len(self.parent.ACS)):
                    if self.parent.ACS[i][0] == objeto[0]:
                        datosUndo.append([copy.deepcopy(self.parent.ACS[i]), objeto[0]])
                        accionesUndo.append('modificar ACS')
                        self.parent.ACS[i] = objeto
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                        break

            else:
                if tipoObjeto == 'calefaccion':
                    for i in range(len(self.parent.calefaccion)):
                        if self.parent.calefaccion[i][0] == objeto[0]:
                            datosUndo.append([copy.deepcopy(self.parent.calefaccion[i]), objeto[0]])
                            accionesUndo.append('modificar Calefaccion')
                            self.parent.calefaccion[i] = objeto
                            self.parent.cargarArbol(self.parent.arbolInstalaciones)
                            break

                else:
                    if tipoObjeto == 'refrigeracion':
                        for i in range(len(self.parent.refrigeracion)):
                            if self.parent.refrigeracion[i][0] == objeto[0]:
                                datosUndo.append([copy.deepcopy(self.parent.refrigeracion[i]), objeto[0]])
                                accionesUndo.append('modificar Refrigeracion')
                                self.parent.refrigeracion[i] = objeto
                                self.parent.cargarArbol(self.parent.arbolInstalaciones)
                                break

                    else:
                        if tipoObjeto == 'climatizacion':
                            for i in range(len(self.parent.climatizacion)):
                                if self.parent.climatizacion[i][0] == objeto[0]:
                                    datosUndo.append([copy.deepcopy(self.parent.climatizacion[i]), objeto[0]])
                                    accionesUndo.append('modificar Climatizacion')
                                    self.parent.climatizacion[i] = objeto
                                    self.parent.cargarArbol(self.parent.arbolInstalaciones)
                                    break

                        else:
                            if tipoObjeto == 'mixto2':
                                for i in range(len(self.parent.mixto2)):
                                    if self.parent.mixto2[i][0] == objeto[0]:
                                        datosUndo.append([copy.deepcopy(self.parent.mixto2[i]), objeto[0]])
                                        accionesUndo.append('modificar Mixto2')
                                        self.parent.mixto2[i] = objeto
                                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                                        break

                            else:
                                if tipoObjeto == 'mixto3':
                                    for i in range(len(self.parent.mixto3)):
                                        if self.parent.mixto3[i][0] == objeto[0]:
                                            datosUndo.append([copy.deepcopy(self.parent.mixto3[i]), objeto[0]])
                                            accionesUndo.append('modificar Mixto3')
                                            self.parent.mixto3[i] = objeto
                                            self.parent.cargarArbol(self.parent.arbolInstalaciones)
                                            break

                                else:
                                    if tipoObjeto == 'renovable':
                                        for i in range(len(self.parent.contribuciones)):
                                            if self.parent.contribuciones[i][0] == objeto[0]:
                                                datosUndo.append([copy.deepcopy(self.parent.contribuciones[i]), objeto[0]])
                                                accionesUndo.append('modificar Contribuciones')
                                                self.parent.contribuciones[i] = objeto
                                                self.parent.cargarArbol(self.parent.arbolInstalaciones)
                                                break

                                    else:
                                        if tipoObjeto == 'iluminacion':
                                            for i in range(len(self.parent.iluminacion)):
                                                if self.parent.iluminacion[i][0] == objeto[0]:
                                                    datosUndo.append([copy.deepcopy(self.parent.iluminacion[i]), objeto[0]])
                                                    accionesUndo.append('modificar Iluminacion')
                                                    self.parent.iluminacion[i] = objeto
                                                    self.parent.cargarArbol(self.parent.arbolInstalaciones)
                                                    break

                                        else:
                                            if tipoObjeto == 'ventilacion':
                                                for i in range(len(self.parent.ventilacion)):
                                                    if self.parent.ventilacion[i][0] == objeto[0]:
                                                        datosUndo.append([copy.deepcopy(self.parent.ventilacion[i]), objeto[0]])
                                                        accionesUndo.append('modificar Ventilacion')
                                                        self.parent.ventilacion[i] = objeto
                                                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                                                        break

                                            else:
                                                if tipoObjeto == 'ventiladores':
                                                    for i in range(len(self.parent.ventiladores)):
                                                        if self.parent.ventiladores[i][0] == objeto[0]:
                                                            datosUndo.append([copy.deepcopy(self.parent.ventiladores[i]), objeto[0]])
                                                            accionesUndo.append('modificar Ventiladores')
                                                            self.parent.ventiladores[i] = objeto
                                                            self.parent.cargarArbol(self.parent.arbolInstalaciones)
                                                            break

                                                else:
                                                    if tipoObjeto == 'bombas':
                                                        for i in range(len(self.parent.bombas)):
                                                            if self.parent.bombas[i][0] == objeto[0]:
                                                                datosUndo.append([copy.deepcopy(self.parent.bombas[i]), objeto[0]])
                                                                accionesUndo.append('modificar Bombas')
                                                                self.parent.bombas[i] = objeto
                                                                self.parent.cargarArbol(self.parent.arbolInstalaciones)
                                                                break

                                                    elif tipoObjeto == 'torresRefrigeracion':
                                                        for i in range(len(self.parent.torresRefrigeracion)):
                                                            if self.parent.torresRefrigeracion[i][0] == objeto[0]:
                                                                datosUndo.append([copy.deepcopy(self.parent.torresRefrigeracion[i]), objeto[0]])
                                                                accionesUndo.append('modificar Torres')
                                                                self.parent.torresRefrigeracion[i] = objeto
                                                                self.parent.cargarArbol(self.parent.arbolInstalaciones)
                                                                break

        else:
            if tipoAntiguo == 'ACS':
                for i in range(len(self.parent.ACS)):
                    if self.parent.ACS[i][0] == objeto[0]:
                        datosUndo.append([copy.deepcopy(self.parent.ACS[i]), i])
                        accionesUndo.append('borrar ACS')
                        self.parent.ACS.pop(i)
                        break

            elif tipoAntiguo == 'calefaccion':
                for i in range(len(self.parent.calefaccion)):
                    if self.parent.calefaccion[i][0] == objeto[0]:
                        datosUndo.append([copy.deepcopy(self.parent.calefaccion[i]), i])
                        accionesUndo.append('borrar Calefaccion')
                        self.parent.calefaccion.pop(i)
                        break

            elif tipoAntiguo == 'refrigeracion':
                for i in range(len(self.parent.refrigeracion)):
                    if self.parent.refrigeracion[i][0] == objeto[0]:
                        datosUndo.append([copy.deepcopy(self.parent.refrigeracion[i]), i])
                        accionesUndo.append('borrar Refrigeracion')
                        self.parent.refrigeracion.pop(i)
                        break

            elif tipoAntiguo == 'climatizacion':
                for i in range(len(self.parent.climatizacion)):
                    if self.parent.climatizacion[i][0] == objeto[0]:
                        datosUndo.append([copy.deepcopy(self.parent.climatizacion[i]), i])
                        accionesUndo.append('borrar Climatizacion')
                        self.parent.climatizacion.pop(i)
                        break

            elif tipoAntiguo == 'mixto2':
                for i in range(len(self.parent.mixto2)):
                    if self.parent.mixto2[i][0] == objeto[0]:
                        datosUndo.append([copy.deepcopy(self.parent.mixto2[i]), i])
                        accionesUndo.append('borrar Mixto2')
                        self.parent.mixto2.pop(i)
                        break

            elif tipoAntiguo == 'mixto3':
                for i in range(len(self.parent.mixto3)):
                    if self.parent.mixto3[i][0] == objeto[0]:
                        datosUndo.append([copy.deepcopy(self.parent.mixto3[i]), i])
                        accionesUndo.append('borrar Mixto3')
                        self.parent.mixto3.pop(i)
                        break

            elif tipoAntiguo == 'renovable':
                for i in range(len(self.parent.contribuciones)):
                    if self.parent.contribuciones[i][0] == objeto[0]:
                        datosUndo.append([copy.deepcopy(self.parent.contribuciones[i]), i])
                        accionesUndo.append('borrar Contribuciones')
                        self.parent.contribuciones.pop(i)
                        break

            elif tipoAntiguo == 'iluminacion':
                for i in range(len(self.parent.iluminacion)):
                    if self.parent.iluminacion[i][0] == objeto[0]:
                        datosUndo.append([copy.deepcopy(self.parent.iluminacion[i]), i])
                        accionesUndo.append('borrar Iluminacion')
                        self.parent.iluminacion.pop(i)
                        break

            elif tipoAntiguo == 'ventilacion':
                for i in range(len(self.parent.ventilacion)):
                    if self.parent.ventilacion[i][0] == objeto[0]:
                        datosUndo.append([copy.deepcopy(self.parent.ventilacion[i]), i])
                        accionesUndo.append('borrar Ventilacion')
                        self.parent.ventilacion.pop(i)
                        break

            elif tipoAntiguo == 'ventiladores':
                for i in range(len(self.parent.ventiladores)):
                    if self.parent.ventiladores[i][0] == objeto[0]:
                        datosUndo.append([copy.deepcopy(self.parent.ventiladores[i]), i])
                        accionesUndo.append('borrar Ventiladores')
                        self.parent.ventiladores.pop(i)
                        break

            elif tipoAntiguo == 'bombas':
                for i in range(len(self.parent.bombas)):
                    if self.parent.bombas[i][0] == objeto[0]:
                        datosUndo.append([copy.deepcopy(self.parent.bombas[i]), i])
                        accionesUndo.append('borrar Bombas')
                        self.parent.bombas.pop(i)
                        break

            elif tipoAntiguo == 'torresRefrigeracion':
                for i in range(len(self.parent.torresRefrigeracion)):
                    if self.parent.torresRefrigeracion[i][0] == objeto[0]:
                        datosUndo.append([copy.deepcopy(self.parent.torresRefrigeracion[i]), i])
                        accionesUndo.append('borrar Torres')
                        self.parent.torresRefrigeracion.pop(i)
                        break

            if tipoObjeto == 'ACS':
                self.parent.ACS.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir ACS')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif tipoObjeto == 'calefaccion':
                self.parent.calefaccion.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Calefaccion')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif tipoObjeto == 'refrigeracion':
                self.parent.refrigeracion.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Refrigeracion')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif tipoObjeto == 'climatizacion':
                self.parent.climatizacion.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Climatizacion')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif tipoObjeto == 'mixto2':
                self.parent.mixto2.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Mixto2')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif tipoObjeto == 'mixto3':
                self.parent.mixto3.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Mixto3')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif tipoObjeto == 'renovable':
                self.parent.contribuciones.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Contribuciones')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif tipoObjeto == 'iluminacion':
                self.parent.iluminacion.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Iluminacion')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif tipoObjeto == 'ventilacion':
                self.parent.ventilacion.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Ventilacion')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif tipoObjeto == 'ventiladores':
                self.parent.ventiladores.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Ventiladores')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif tipoObjeto == 'bombas':
                self.parent.bombas.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Bombas')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
            elif tipoObjeto == 'torresRefrigeracion':
                self.parent.torresRefrigeracion.append(objeto)
                datosUndo.append(objeto[0])
                accionesUndo.append('anadir Torres')
                self.parent.cargarArbol(self.parent.arbolInstalaciones)
        self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, accionesUndo, datosUndo))
        self.parent.parent.parent.pilaRedo = undo.undoManaggement()

    def OnVistaClasicaBoton(self, event):
        self.parent.vistaClasica.cargaVista()
        self.parent.vistaNormal = False

    def OnVistaNormalBoton(self, event):
        self.parent.vistaNormal = True
        try:
            self.parent.OnArbolCerramientos(None)
        except:
            logging.info('Excepcion en: %s' % __name__)

        return

    def OnmodificarBoton(self, event):
        try:
            item = self.parent.arbolInstalaciones.GetItemText(self.parent.arbolInstalaciones.GetSelection())
        except:
            raise Exception('Debe seleccionar el elemento del arbol que desea modificar.')
            return

        root = self.parent.arbolInstalaciones.GetSelection()
        if root == self.parent.arbolInstalaciones.GetRootItem():
            raise Exception('No se puede modificar la raíz del árbol.')
            return
        accionesUndo = []
        datosUndo = []
        if self.parent.arbolInstalaciones.GetChildrenCount(self.parent.arbolInstalaciones.GetSelection()) > 0:
            for i in range(len(self.parent.parent.subgrupos)):
                if item == self.parent.parent.subgrupos[i].nombre:
                    datos = self.parent.parent.subgrupos[i]
                    break

            dlg = ventanaSubgrupo.create(self.parent, -1, wx.Point(200, 200), wx.Size(448, 240), wx.DEFAULT_DIALOG_STYLE, 'ventanaZonas', self.parent.parent.parent.panelEnvolvente, self.parent, 'modificar', item)
            dlg.cargarDatos(datos)
            dlg.ShowModal()
            return
        for i in range(len(self.parent.parent.subgrupos)):
            if item == self.parent.parent.subgrupos[i].nombre:
                datos = self.parent.parent.subgrupos[i]
                dlg = ventanaSubgrupo.create(self.parent, -1, wx.Point(200, 200), wx.Size(448, 240), wx.DEFAULT_DIALOG_STYLE, 'ventanaZonas', self.parent.parent.parent.panelEnvolvente, self.parent, 'modificar', item)
                dlg.cargarDatos(datos)
                dlg.ShowModal()
                return

        if self.parent.panelElegirObjeto.contribucionesEnergeticas != True and self.parent.panelElegirObjeto.iluminacion != True and self.parent.panelElegirObjeto.ventilacion != True and self.parent.panelElegirObjeto.ventiladores != True and self.parent.panelElegirObjeto.bombas != True and self.parent.panelElegirObjeto.torresRefrigeracion != True:
            nuevo = self.parent.cogerDatosDelPanel(self.parent.panel2)
        else:
            if self.parent.panelElegirObjeto.iluminacion == True:
                instalacionAnterior = ''
                for i in range(len(self.parent.iluminacion)):
                    if item == self.parent.iluminacion[i][0]:
                        instalacionAnterior = self.parent.iluminacion[i]
                        self.parent.iluminacion.pop(i)
                        break

            nuevo = self.parent.panel2.cogerDatos()
        if type(nuevo) == type('hola'):
            raise Exception('Revise los siguientes campos:\n' + nuevo)
            if self.parent.panelElegirObjeto.iluminacion == True:
                self.parent.iluminacion.append(instalacionAnterior)
            return
        compruebaNombres = 'elemento no encontrado'
        if nuevo[0] != item:
            compruebaNombres = self.compruebaNombres(nuevo[0])
        if compruebaNombres == 'elemento no encontrado':
            encontrado = False
            if nuevo[1] == 'ACS':
                for i in range(len(self.parent.ACS)):
                    if item == self.parent.ACS[i][0]:
                        datosUndo.append([copy.deepcopy(self.parent.ACS[i]), nuevo[0]])
                        accionesUndo.append('modificar ACS')
                        self.parent.ACS[i] = nuevo
                        encontrado = True
                        break

            else:
                if nuevo[1] == 'calefaccion':
                    for i in range(len(self.parent.calefaccion)):
                        if item == self.parent.calefaccion[i][0]:
                            datosUndo.append([copy.deepcopy(self.parent.calefaccion[i]), nuevo[0]])
                            accionesUndo.append('modificar Calefaccion')
                            self.parent.calefaccion[i] = nuevo
                            encontrado = True
                            break

                elif nuevo[1] == 'refrigeracion':
                    for i in range(len(self.parent.refrigeracion)):
                        if item == self.parent.refrigeracion[i][0]:
                            datosUndo.append([copy.deepcopy(self.parent.refrigeracion[i]), nuevo[0]])
                            accionesUndo.append('modificar Refrigeracion')
                            self.parent.refrigeracion[i] = nuevo
                            encontrado = True
                            break

                elif nuevo[1] == 'climatizacion':
                    for i in range(len(self.parent.climatizacion)):
                        if item == self.parent.climatizacion[i][0]:
                            datosUndo.append([copy.deepcopy(self.parent.climatizacion[i]), nuevo[0]])
                            accionesUndo.append('modificar Climatizacion')
                            self.parent.climatizacion[i] = nuevo
                            encontrado = True
                            break

                elif nuevo[1] == 'mixto2':
                    for i in range(len(self.parent.mixto2)):
                        if item == self.parent.mixto2[i][0]:
                            datosUndo.append([copy.deepcopy(self.parent.mixto2[i]), nuevo[0]])
                            accionesUndo.append('modificar Mixto2')
                            self.parent.mixto2[i] = nuevo
                            encontrado = True
                            break

                elif nuevo[1] == 'mixto3':
                    for i in range(len(self.parent.mixto3)):
                        if item == self.parent.mixto3[i][0]:
                            datosUndo.append([copy.deepcopy(self.parent.mixto3[i]), nuevo[0]])
                            accionesUndo.append('modificar Mixto3')
                            self.parent.mixto3[i] = nuevo
                            encontrado = True
                            break

                elif nuevo[1] == 'renovable':
                    for i in range(len(self.parent.contribuciones)):
                        if item == self.parent.contribuciones[i][0]:
                            datosUndo.append([copy.deepcopy(self.parent.contribuciones[i]), nuevo[0]])
                            accionesUndo.append('modificar Contribuciones')
                            self.parent.contribuciones[i] = nuevo
                            encontrado = True
                            break

                elif nuevo[1] == 'iluminacion':
                    self.parent.iluminacion.append(nuevo)
                    datosUndo.append([copy.deepcopy(self.parent.iluminacion[i]), nuevo[0]])
                    accionesUndo.append('modificar Iluminacion')
                    encontrado = True
                elif nuevo[1] == 'ventilacion':
                    for i in range(len(self.parent.ventilacion)):
                        if item == self.parent.ventilacion[i][0]:
                            datosUndo.append([copy.deepcopy(self.parent.ventilacion[i]), nuevo[0]])
                            accionesUndo.append('modificar Ventilacion')
                            self.parent.ventilacion[i] = nuevo
                            encontrado = True
                            break

                elif nuevo[1] == 'ventiladores':
                    for i in range(len(self.parent.ventiladores)):
                        if item == self.parent.ventiladores[i][0]:
                            datosUndo.append([copy.deepcopy(self.parent.ventiladores[i]), nuevo[0]])
                            accionesUndo.append('modificar Ventiladores')
                            self.parent.ventiladores[i] = nuevo
                            encontrado = True
                            break

                elif nuevo[1] == 'bombas':
                    for i in range(len(self.parent.bombas)):
                        if item == self.parent.bombas[i][0]:
                            datosUndo.append([copy.deepcopy(self.parent.bombas[i]), nuevo[0]])
                            accionesUndo.append('modificar Bombas')
                            self.parent.bombas[i] = nuevo
                            encontrado = True
                            break

                elif nuevo[1] == 'torresRefrigeracion':
                    for i in range(len(self.parent.torresRefrigeracion)):
                        if item == self.parent.torresRefrigeracion[i][0]:
                            datosUndo.append([copy.deepcopy(self.parent.torresRefrigeracion[i]), nuevo[0]])
                            accionesUndo.append('modificar Torres')
                            self.parent.torresRefrigeracion[i] = nuevo
                            encontrado = True
                            break

                if encontrado == False:
                    cambios = self.borrarTipoAntiguo(item)
                    for i in range(len(cambios[0])):
                        datosUndo.append(cambios[0][i])
                        accionesUndo.append(cambios[1][i])

                    if nuevo[1] == 'ACS':
                        self.parent.ACS.append(nuevo)
                        datosUndo.append(nuevo[0])
                        accionesUndo.append('anadir ACS')
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                    elif nuevo[1] == 'calefaccion':
                        self.parent.calefaccion.append(nuevo)
                        datosUndo.append(nuevo[0])
                        accionesUndo.append('anadir Calefaccion')
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                    elif nuevo[1] == 'refrigeracion':
                        self.parent.refrigeracion.append(nuevo)
                        datosUndo.append(nuevo[0])
                        accionesUndo.append('anadir Refrigeracion')
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                    elif nuevo[1] == 'climatizacion':
                        self.parent.climatizacion.append(nuevo)
                        datosUndo.append(nuevo[0])
                        accionesUndo.append('anadir Climatizacion')
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                    elif nuevo[1] == 'mixto2':
                        self.parent.mixto2.append(nuevo)
                        datosUndo.append(nuevo[0])
                        accionesUndo.append('anadir Mixto2')
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                    elif nuevo[1] == 'mixto3':
                        self.parent.mixto3.append(nuevo)
                        datosUndo.append(nuevo[0])
                        accionesUndo.append('anadir Mixto3')
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                    elif nuevo[1] == 'renovable':
                        self.parent.contribuciones.append(nuevo)
                        datosUndo.append(nuevo[0])
                        accionesUndo.append('anadir Contribuciones')
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                    elif nuevo[1] == 'iluminacion':
                        self.parent.iluminacion.append(nuevo)
                        datosUndo.append(nuevo[0])
                        accionesUndo.append('anadir Iluminacion')
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                    elif nuevo[1] == 'ventilacion':
                        self.parent.ventilacion.append(nuevo)
                        datosUndo.append(nuevo[0])
                        accionesUndo.append('anadir Ventilacion')
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                    elif nuevo[1] == 'ventiladores':
                        self.parent.ventiladores.append(nuevo)
                        datosUndo.append(nuevo[0])
                        accionesUndo.append('anadir Ventiladores')
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                    elif nuevo[1] == 'bombas':
                        self.parent.bombas.append(nuevo)
                        datosUndo.append(nuevo[0])
                        accionesUndo.append('anadir Bombas')
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                    elif nuevo[1] == 'torresRefrigeracion':
                        self.parent.torresRefrigeracion.append(nuevo)
                        datosUndo.append(nuevo[0])
                        accionesUndo.append('anadir Torres')
                        self.parent.cargarArbol(self.parent.arbolInstalaciones)
                    self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, accionesUndo, datosUndo))
                    self.parent.parent.parent.pilaRedo = undo.undoManaggement()
                    return
        else:
            raise Exception('El nombre del elemento modificado ya existe,  indique otro')
            if self.parent.panelElegirObjeto.iluminacion == True:
                self.parent.iluminacion.append(instalacionAnterior)
        self.parent.cargarArbol(self.parent.arbolInstalaciones)
        self.cargarUltimoElemento(nuevo[0])
        self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, accionesUndo, datosUndo))
        self.parent.parent.parent.pilaRedo = undo.undoManaggement()

    def borrarTipoAntiguo(self, nombre):
        datosUndo = []
        accionesUndo = []
        for inst in range(len(self.parent.ACS)):
            if nombre == self.parent.ACS[inst][0]:
                datosUndo.append([copy.deepcopy(self.parent.ACS[inst]), inst])
                accionesUndo.append('borrar ACS')
                self.parent.ACS.pop(inst)
                return [
                 datosUndo, accionesUndo]

        for inst in range(len(self.parent.calefaccion)):
            if nombre == self.parent.calefaccion[inst][0]:
                datosUndo.append([copy.deepcopy(self.parent.calefaccion[inst]), inst])
                accionesUndo.append('borrar Calefaccion')
                self.parent.calefaccion.pop(inst)
                return [
                 datosUndo, accionesUndo]

        for inst in range(len(self.parent.refrigeracion)):
            if nombre == self.parent.refrigeracion[inst][0]:
                datosUndo.append([copy.deepcopy(self.parent.refrigeracion[inst]), inst])
                accionesUndo.append('borrar Refrigeracion')
                self.parent.refrigeracion.pop(inst)
                return [
                 datosUndo, accionesUndo]

        for inst in range(len(self.parent.climatizacion)):
            if nombre == self.parent.climatizacion[inst][0]:
                datosUndo.append([copy.deepcopy(self.parent.climatizacion[inst]), inst])
                accionesUndo.append('borrar Climatizacion')
                self.parent.climatizacion.pop(inst)
                return [
                 datosUndo, accionesUndo]

        for inst in range(len(self.parent.mixto2)):
            if nombre == self.parent.mixto2[inst][0]:
                datosUndo.append([copy.deepcopy(self.parent.mixto2[inst]), inst])
                accionesUndo.append('borrar Mixto2')
                self.parent.mixto2.pop(inst)
                return [
                 datosUndo, accionesUndo]

        for inst in range(len(self.parent.mixto3)):
            if nombre == self.parent.mixto3[inst][0]:
                datosUndo.append([copy.deepcopy(self.parent.mixto3[inst]), inst])
                accionesUndo.append('borrar Mixto3')
                self.parent.mixto3.pop(inst)
                return [
                 datosUndo, accionesUndo]

        for inst in range(len(self.parent.contribuciones)):
            if nombre == self.parent.contribuciones[inst][0]:
                datosUndo.append([copy.deepcopy(self.parent.contribuciones[inst]), inst])
                accionesUndo.append('borrar Contribuciones')
                self.parent.contribuciones.pop(inst)
                return [
                 datosUndo, accionesUndo]

        for inst in range(len(self.parent.ventilacion)):
            if nombre == self.parent.ventilacion[inst][0]:
                datosUndo.append([copy.deepcopy(self.parent.ventilacion[inst]), inst])
                accionesUndo.append('borrar Ventilacion')
                self.parent.ventilacion.pop(inst)
                return [
                 datosUndo, accionesUndo]

        for inst in range(len(self.parent.iluminacion)):
            if nombre == self.parent.iluminacion[inst][0]:
                datosUndo.append([copy.deepcopy(self.parent.iluminacion[inst]), inst])
                accionesUndo.append('borrar Iluminacion')
                self.parent.iluminacion.pop(inst)
                return [
                 datosUndo, accionesUndo]

        for inst in range(len(self.parent.ventiladores)):
            if nombre == self.parent.ventiladores[inst][0]:
                datosUndo.append([copy.deepcopy(self.parent.ventiladores[inst]), inst])
                accionesUndo.append('borrar Ventiladores')
                self.parent.ventiladores.pop(inst)
                return [
                 datosUndo, accionesUndo]

        for inst in range(len(self.parent.bombas)):
            if nombre == self.parent.bombas[inst][0]:
                datosUndo.append([copy.deepcopy(self.parent.bombas[inst]), inst])
                accionesUndo.append('borrar Bombas')
                self.parent.bombas.pop(inst)
                return [
                 datosUndo, accionesUndo]

        for inst in range(len(self.parent.torresRefrigeracion)):
            if nombre == self.parent.torresRefrigeracion[inst][0]:
                datosUndo.append([copy.deepcopy(self.parent.torresRefrigeracion[inst]), inst])
                accionesUndo.append('borrar Torres')
                self.parent.torresRefrigeracion.pop(inst)
                return [
                 datosUndo, accionesUndo]

        return [
         datosUndo, accionesUndo]

    def compruebaNombres(self, nombre):
        for inst in self.parent.ACS:
            if nombre == inst[0]:
                return nombre

        for inst in self.parent.calefaccion:
            if nombre == inst[0]:
                return nombre

        for inst in self.parent.refrigeracion:
            if nombre == inst[0]:
                return nombre

        for inst in self.parent.climatizacion:
            if nombre == inst[0]:
                return nombre

        for inst in self.parent.mixto2:
            if nombre == inst[0]:
                return nombre

        for inst in self.parent.mixto3:
            if nombre == inst[0]:
                return nombre

        for inst in self.parent.contribuciones:
            if nombre == inst[0]:
                return nombre

        for inst in self.parent.ventilacion:
            if nombre == inst[0]:
                return nombre

        for inst in self.parent.iluminacion:
            if nombre == inst[0]:
                return nombre

        for inst in self.parent.ventiladores:
            if nombre == inst[0]:
                return nombre

        for inst in self.parent.bombas:
            if nombre == inst[0]:
                return nombre

        for inst in self.parent.torresRefrigeracion:
            if nombre == inst[0]:
                return nombre

        return 'elemento no encontrado'

    def OnBorrarBotonButton(self, event):
        try:
            item = self.parent.arbolInstalaciones.GetItemText(self.parent.arbolInstalaciones.GetSelection())
        except:
            raise Exception('Debe seleccionar el elemento del árbol que desea eliminar.')
            return

        root = self.parent.arbolInstalaciones.GetSelection()
        if root == self.parent.arbolInstalaciones.GetRootItem():
            raise Exception('No se puede borrar la raíz del árbol.')
            return
        accionesUndo = []
        datosUndo = []
        borrar = dialogoConfirma.Dialog1(self, '¿Desea borrar el elemento "' + item + '"?')
        borrar.ShowModal()
        if borrar.dev == False:
            return
        if self.parent.arbolInstalaciones.GetChildrenCount(self.parent.arbolInstalaciones.GetSelection()) > 0:
            seleccion = self.parent.arbolInstalaciones.GetSelection()
            textoSelect = self.parent.arbolInstalaciones.GetItemText(seleccion)
            boolExistenInstColgandoDeZonaEliminadaEnConjuntosMM = existenInstalacionesColgandoDeZonaModificadaOEliminadaEnConjuntosMM(listadoConjuntosMM=self.parent.parent.parent.listadoConjuntosMMUsuario, subgrupoModifOElim=textoSelect)
            if boolExistenInstColgandoDeZonaEliminadaEnConjuntosMM == True:
                mensaje = 'Si borra este elemento se perderán todos sus componentes. Además, se eliminarán las instalaciones de los conjuntos de medidas de mejora que cuelguen de dicho elemento y deberán ser revisadas. ¿Desea continuar?'
            else:
                mensaje = 'Si borra este elemento se perderán todos sus componentes. ¿Desea continuar?'
            borraTodo = dialogoConfirma.Dialog1(self, mensaje, size=(600, 125))
            borraTodo.ShowModal()
            if borraTodo.dev == True:
                self.borraGrupo()
        else:
            for i in range(len(self.parent.ACS)):
                if item == self.parent.ACS[i][0]:
                    datosUndo.append([copy.deepcopy(self.parent.ACS[i]), i])
                    accionesUndo.append('borrar ACS')
                    self.parent.ACS.pop(i)
                    break

            for i in range(len(self.parent.calefaccion)):
                if item == self.parent.calefaccion[i][0]:
                    datosUndo.append([copy.deepcopy(self.parent.calefaccion[i]), i])
                    accionesUndo.append('borrar Calefaccion')
                    self.parent.calefaccion.pop(i)
                    break

            for i in range(len(self.parent.refrigeracion)):
                if item == self.parent.refrigeracion[i][0]:
                    datosUndo.append([copy.deepcopy(self.parent.refrigeracion[i]), i])
                    accionesUndo.append('borrar Refrigeracion')
                    self.parent.refrigeracion.pop(i)
                    break

            for i in range(len(self.parent.climatizacion)):
                if item == self.parent.climatizacion[i][0]:
                    datosUndo.append([copy.deepcopy(self.parent.climatizacion[i]), i])
                    accionesUndo.append('borrar Climatizacion')
                    self.parent.climatizacion.pop(i)
                    break

            for i in range(len(self.parent.mixto2)):
                if item == self.parent.mixto2[i][0]:
                    datosUndo.append([copy.deepcopy(self.parent.mixto2[i]), i])
                    accionesUndo.append('borrar Mixto2')
                    self.parent.mixto2.pop(i)
                    break

            for i in range(len(self.parent.mixto3)):
                if item == self.parent.mixto3[i][0]:
                    datosUndo.append([copy.deepcopy(self.parent.mixto3[i]), i])
                    accionesUndo.append('borrar Mixto3')
                    self.parent.mixto3.pop(i)
                    break

            for i in range(len(self.parent.contribuciones)):
                if item == self.parent.contribuciones[i][0]:
                    datosUndo.append([copy.deepcopy(self.parent.contribuciones[i]), i])
                    accionesUndo.append('borrar Contribuciones')
                    self.parent.contribuciones.pop(i)
                    break

            for i in range(len(self.parent.iluminacion)):
                if item == self.parent.iluminacion[i][0]:
                    datosUndo.append([copy.deepcopy(self.parent.iluminacion[i]), i])
                    accionesUndo.append('borrar Iluminacion')
                    self.parent.iluminacion.pop(i)
                    break

            for i in range(len(self.parent.ventilacion)):
                if item == self.parent.ventilacion[i][0]:
                    datosUndo.append([copy.deepcopy(self.parent.ventilacion[i]), i])
                    accionesUndo.append('borrar Ventilacion')
                    self.parent.ventilacion.pop(i)
                    break

            for i in range(len(self.parent.ventiladores)):
                if item == self.parent.ventiladores[i][0]:
                    datosUndo.append([copy.deepcopy(self.parent.ventiladores[i]), i])
                    accionesUndo.append('borrar Ventiladores')
                    self.parent.ventiladores.pop(i)
                    break

            for i in range(len(self.parent.bombas)):
                if item == self.parent.bombas[i][0]:
                    datosUndo.append([copy.deepcopy(self.parent.bombas[i]), i])
                    accionesUndo.append('borrar Bombas')
                    self.parent.bombas.pop(i)
                    break

            for i in range(len(self.parent.torresRefrigeracion)):
                if item == self.parent.torresRefrigeracion[i][0]:
                    datosUndo.append([copy.deepcopy(self.parent.torresRefrigeracion[i]), i])
                    accionesUndo.append('borrar Torres')
                    self.parent.torresRefrigeracion.pop(i)
                    break

            for i in range(len(self.parent.parent.subgrupos)):
                if item == self.parent.parent.subgrupos[i].nombre:
                    datosUndo.append([copy.deepcopy(self.parent.parent.subgrupos[i]), i])
                    accionesUndo.append('borrar zona')
                    self.borraGrupo()
                    break

            self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, accionesUndo, datosUndo))
            self.parent.parent.parent.pilaRedo = undo.undoManaggement()
        self.parent.cargarArbol(self.parent.arbolInstalaciones)

    def borraGrupo(self):
        seleccion = self.parent.arbolInstalaciones.GetSelection()
        textoSelect = self.parent.arbolInstalaciones.GetItemText(seleccion)
        for i in range(len(self.parent.parent.subgrupos)):
            if self.parent.parent.subgrupos[i].raiz == textoSelect:
                raise Exception('No puede borrar una zona con más subzonas dentro')
                return

        pertenece = False
        for i in range(len(self.parent.parent.parent.panelEnvolvente.cerramientos)):
            if self.parent.parent.parent.panelEnvolvente.cerramientos[i][-2] == textoSelect:
                pertenece = True
                break

        accionesUndo = []
        datosUndo = []
        if pertenece == True:
            DeseaEliminar = dialogoConfirma.Dialog1(self, 'La zona que desea borrar tiene cerramientos asociadas. ¿Desea borrar también estos cerramientos?')
            DeseaEliminar.ShowModal()
            if DeseaEliminar.dev == True:
                cambios = self.parent.parent.parent.panelEnvolvente.panelBotones.BorrarSubgrupoEnvolvente(textoSelect)
                for i in range(len(cambios[0])):
                    datosUndo.append(cambios[0][i])
                    accionesUndo.append(cambios[1][i])

            elif DeseaEliminar.dev == False:
                self.Close()
                return
        for i in range(len(self.parent.parent.subgrupos)):
            if textoSelect == self.parent.parent.subgrupos[i].nombre:
                zonaEliminada = self.parent.parent.subgrupos[i]
                datosUndo.append([copy.deepcopy(self.parent.parent.subgrupos[i]), i])
                accionesUndo.append('borrar zona')
                self.parent.parent.subgrupos.pop(i)
                break

        self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, accionesUndo, datosUndo))
        self.parent.parent.parent.pilaRedo = undo.undoManaggement()
        self.BorrarSubgrupoInstalaciones(zonaEliminada=zonaEliminada)

    def BorrarSubgrupoInstalaciones(self, zonaEliminada):
        accionesUndo = []
        datosUndo = []
        bol = False
        while bol != True:
            bol = True
            for j in range(len(self.parent.ACS)):
                if self.parent.ACS[j][-1] == zonaEliminada.nombre:
                    datosUndo.append([copy.deepcopy(self.parent.ACS[j]), j])
                    accionesUndo.append('borrar ACS')
                    self.parent.ACS.pop(j)
                    bol = False
                    break

        bol = False
        while bol != True:
            bol = True
            for j in range(len(self.parent.calefaccion)):
                if self.parent.calefaccion[j][-1] == zonaEliminada.nombre:
                    datosUndo.append([copy.deepcopy(self.parent.calefaccion[j]), j])
                    accionesUndo.append('borrar Calefaccion')
                    self.parent.calefaccion.pop(j)
                    bol = False
                    break

        bol = False
        while bol != True:
            bol = True
            for j in range(len(self.parent.refrigeracion)):
                if self.parent.refrigeracion[j][-1] == zonaEliminada.nombre:
                    datosUndo.append([copy.deepcopy(self.parent.refrigeracion[j]), j])
                    accionesUndo.append('borrar Refrigeracion')
                    self.parent.refrigeracion.pop(j)
                    bol = False
                    break

        bol = False
        while bol != True:
            bol = True
            for j in range(len(self.parent.climatizacion)):
                if self.parent.climatizacion[j][-1] == zonaEliminada.nombre:
                    datosUndo.append([copy.deepcopy(self.parent.climatizacion[j]), j])
                    accionesUndo.append('borrar Climatizacion')
                    self.parent.climatizacion.pop(j)
                    bol = False
                    break

        bol = False
        while bol != True:
            bol = True
            for j in range(len(self.parent.mixto2)):
                if self.parent.mixto2[j][-1] == zonaEliminada.nombre:
                    datosUndo.append([copy.deepcopy(self.parent.mixto2[j]), j])
                    accionesUndo.append('borrar Mixto2')
                    self.parent.mixto2.pop(j)
                    bol = False
                    break

        bol = False
        while bol != True:
            bol = True
            for j in range(len(self.parent.mixto3)):
                if self.parent.mixto3[j][-1] == zonaEliminada.nombre:
                    datosUndo.append([copy.deepcopy(self.parent.mixto3[j]), j])
                    accionesUndo.append('borrar Mixto3')
                    self.parent.mixto3.pop(j)
                    bol = False
                    break

        bol = False
        while bol != True:
            bol = True
            for j in range(len(self.parent.contribuciones)):
                if self.parent.contribuciones[j][-1] == zonaEliminada.nombre:
                    datosUndo.append([copy.deepcopy(self.parent.contribuciones[j]), j])
                    accionesUndo.append('borrar Contribuciones')
                    self.parent.contribuciones.pop(j)
                    bol = False
                    break

        bol = False
        while bol != True:
            bol = True
            for j in range(len(self.parent.iluminacion)):
                if self.parent.iluminacion[j][-1] == zonaEliminada.nombre:
                    datosUndo.append([copy.deepcopy(self.parent.iluminacion[j]), j])
                    accionesUndo.append('borrar Iluminacion')
                    self.parent.iluminacion.pop(j)
                    bol = False
                    break

        if self.parent.parent.parent.programa == 'GranTerciario':
            self.parent.iluminacion = calculoSuperficies.actualizarSuperficiesIluminacion(self.parent.parent.subgrupos, self.parent.parent.parent.panelDatosGenerales.superficie, self.parent.parent.parent.panelInstalaciones.iluminacion)
            try:
                if self.parent.parent.parent.panelInstalaciones.panelElegirObjeto.iluminacion == True:
                    self.parent.parent.parent.panelInstalaciones.panel2.onSeleccionarSubgrupo(None)
            except:
                logging.info('Excepcion en: %s' % __name__)

        bol = False
        while bol != True:
            bol = True
            for j in range(len(self.parent.ventilacion)):
                if self.parent.ventilacion[j][-1] == zonaEliminada.nombre:
                    datosUndo.append([copy.deepcopy(self.parent.ventilacion[j]), j])
                    accionesUndo.append('borrar Ventilacion')
                    self.parent.ventilacion.pop(j)
                    bol = False
                    break

        bol = False
        while bol != True:
            bol = True
            for j in range(len(self.parent.ventiladores)):
                if self.parent.ventiladores[j][-1] == zonaEliminada.nombre:
                    datosUndo.append([copy.deepcopy(self.parent.ventiladores[j]), j])
                    accionesUndo.append('borrar Ventiladores')
                    self.parent.ventiladores.pop(j)
                    bol = False
                    break

        bol = False
        while bol != True:
            bol = True
            for j in range(len(self.parent.bombas)):
                if self.parent.bombas[j][-1] == zonaEliminada.nombre:
                    datosUndo.append([copy.deepcopy(self.parent.bombas[j]), j])
                    accionesUndo.append('borrar Bombas')
                    self.parent.bombas.pop(j)
                    bol = False
                    break

        bol = False
        while bol != True:
            bol = True
            for j in range(len(self.parent.torresRefrigeracion)):
                if self.parent.torresRefrigeracion[j][-1] == zonaEliminada.nombre:
                    datosUndo.append([copy.deepcopy(self.parent.torresRefrigeracion[j]), j])
                    accionesUndo.append('borrar Torres')
                    self.parent.torresRefrigeracion.pop(j)
                    bol = False
                    break

        self.BorrarInstalacionesDelSubgrupoEnConjuntosMM(zonaEliminada=zonaEliminada, programa=self.parent.parent.parent.programa)
        return [datosUndo, accionesUndo]

    def BorrarInstalacionesDelSubgrupoEnConjuntosMM(self, zonaEliminada, programa):
        boolExistenInstColgandoDeZonaEliminadaEnConjuntosMM = existenInstalacionesColgandoDeZonaModificadaOEliminadaEnConjuntosMM(listadoConjuntosMM=self.parent.parent.parent.listadoConjuntosMMUsuario, subgrupoModifOElim=zonaEliminada.nombre)
        if boolExistenInstColgandoDeZonaEliminadaEnConjuntosMM == True:
            self.parent.parent.parent.listadoConjuntosMMUsuario = eliminarSubgrupoDeConjuntosMM(listadoConjuntosMM=self.parent.parent.parent.listadoConjuntosMMUsuario, subgrupoEliminado=zonaEliminada.nombre)
            if programa == 'GranTerciario':
                self.parent.parent.parent.listadoConjuntosMMUsuario = actualizarSuperficieIluminacionDeConjuntosMM(listadoConjuntosMM=self.parent.parent.parent.listadoConjuntosMMUsuario, listadoSubgrupos=self.parent.parent.subgrupos, superficieHabitable=self.parent.parent.parent.panelDatosGenerales.superficie)