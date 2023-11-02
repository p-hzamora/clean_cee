# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: nuevoUndo.pyc
# Compiled at: 2015-02-19 13:18:34
from undo import MiniEventoUndo, UndoCambioSeleccion
import copy, wx, logging

class VistaUndo:

    def __init__(self):
        self.diccionario = {}

    def manejador(self, event):
        objeto = event.GetEventObject()
        padre = event.GetEventObject().GetParent()
        if objeto.GetValue != padre.diccionario[objeto.GetParent().Name + '.' + objeto.Name]:
            objeto.GetParent().parent.parent.parent.pilaUndo.apilar(MiniEventoUndo([
             padre.GetParent(), objeto.GetId()], copy.deepcopy(padre.diccionario[objeto.GetParent().Name + '.' + objeto.Name])), True)
            padre.diccionario[objeto.GetParent().Name + '.' + objeto.Name] = objeto.GetValue()

    def manejadorChoice(self, event):
        objeto = event.GetEventObject()
        padre = event.GetEventObject().GetParent()
        if objeto.GetSelection != padre.diccionario[objeto.GetParent().Name + '.' + objeto.Name]:
            objeto.GetParent().parent.parent.parent.pilaUndo.apilar(MiniEventoUndo([
             padre.GetParent(), objeto.GetId()], copy.deepcopy(padre.diccionario[objeto.GetParent().Name + '.' + objeto.Name])), True)
            padre.diccionario[objeto.GetParent().Name + '.' + objeto.Name] = objeto.GetSelection()
        event.Skip()

    def manejadorRadio(self, event):
        objeto = event.GetEventObject()
        padre = event.GetEventObject().GetParent()
        objeto.GetParent().parent.parent.parent.pilaUndo.apilar(MiniEventoUndo([
         padre.GetParent(), objeto.GetId()], copy.deepcopy(padre.diccionario[objeto.GetParent().Name + '.radios'])), True)
        lista = objeto.GetParent().GetRadioValues()
        padre.diccionario[objeto.GetParent().Name + '.radios'] = lista

    def manejadorArbol(self, event):
        objeto = event.GetEventObject()
        padre = event.GetEventObject().GetParent()
        objetoPila = objeto.GetParent().parent.parent.pilaUndo
        lista = padre.panelElegirObjeto.GetRadioValues()
        objBueno = lista[-1]
        lista.pop(-1)
        dicc = copy.deepcopy(padre.panel2.diccionario)
        try:
            nombre = objeto.GetItemText(objeto.GetSelection())
            padre.OnArbolCerramientos(event)
            objActual = padre.panelElegirObjeto.GetRadioValues()[-1]
            if objetoPila.pila[0].parent != 'panelDefinirEnvolvente' and objetoPila.pila[0].miniEventos.pila != []:
                objetoPila.apilar(UndoCambioSeleccion(objActual, [
                 copy.deepcopy(lista),
                 dicc, objBueno], nombre))
            lista = padre.panelElegirObjeto.GetRadioValues()
            lista.pop(-1)
            padre.panelElegirObjeto.diccionario[objeto.GetParent().Name + '.radios'] = lista
        except:
            logging.info('Excepcion en: %s' % __name__)
            objActual = padre.panelElegirObjeto.GetRadioValues()[-1]
            if objetoPila.pila[0].parent != 'panelDefinirEnvolvente' and objetoPila.pila[0].miniEventos.pila != []:
                objetoPila.apilar(UndoCambioSeleccion(objActual, [
                 copy.deepcopy(lista), dicc, objBueno]))
            lista = padre.panelElegirObjeto.GetRadioValues()
            lista.pop(-1)
            padre.panelElegirObjeto.diccionario[objeto.GetParent().Name + '.radios'] = lista

    def manejadorElegirObjeto(self, event):
        objeto = event.GetEventObject()
        padre = event.GetEventObject().GetParent()
        objetoPila = objeto.GetParent().parent.parent.parent.pilaUndo
        lista = objeto.GetParent().GetRadioValues()
        objBueno = lista[-1]
        lista.pop(-1)
        if objetoPila.pila[0].parent != 'panelDefinirEnvolvente' and objetoPila.pila[0].miniEventos.pila != []:
            objetoPila.apilar(UndoCambioSeleccion(objeto, [
             copy.deepcopy(lista),
             copy.deepcopy(padre.GetParent().panel2.diccionario), objBueno]))
        padre.diccionario[objeto.GetParent().Name + '.radios'] = lista