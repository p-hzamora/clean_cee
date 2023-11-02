# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\panelVentilacion.pyc
# Compiled at: 2015-02-19 13:18:33
from Instalaciones.comprobarCampos import Comprueba
from miChoice import MiChoice
import logging

class Panel1(wx.Panel):

    def _init_ctrls(self, prnt, id, posi, siz, styles, named):
        self.nombreInstalacion = 'Aire primario'
        self.subgrupoChoice = MiChoice(choices=[])
        self.equipoVentilacion = ''
        # self.recuperadorCheck¿Tiene recuperador de calor?
        self.recuperadorCheck= False
        self.rendimiento = ''

    def OnNombreInstalacion(self, event):
        if self.nombreInstalacion == 'Aire primario':
        else:

    def __init__(self, parent, id, pos, size, style, name, real_parent=None):
        if real_parent == None:
            self.parent = parent
        else:
            self.parent = real_parent
        self.tipoSistema = 'ventilacion'
        self._init_ctrls(parent, id, pos, size, style, name)
        self.subgrupoChoice.SetItems(self.cargarRaices())
        self.elegirRaiz()
        return

    def elegirRaiz(self):
        try:
            sel = self.parent.arbolInstalaciones.GetSelection()
            self.subgrupoChoice.SetStringSelection('Edificio Objeto')
            raiz = self.parent.arbolInstalaciones.GetRootItem()
            while sel != raiz:
                for i in range(len(self.parent.parent.subgrupos)):
                    if self.parent.arbolInstalaciones.GetItemText(sel) == '%s' % self.parent.parent.subgrupos[i].nombre:
                        self.subgrupoChoice.SetStringSelection(self.parent.arbolInstalaciones.GetItemText(sel))
                        return

                sel = self.parent.arbolInstalaciones.GetItemParent(sel)

        except:
            logging.info('Excepcion en: %s' % __name__)
            self.subgrupoChoice.SetStringSelection('Edificio Objeto')

    def cargarRaices(self):
        raices = []
        raices.append(('Edificio Objeto', 'Edificio Objeto'))
        for i in range(len(self.parent.parent.subgrupos)):
            if self.parent.parent.subgrupos[i].nombre != 'Edificio Objeto':
                raices.append((self.parent.parent.subgrupos[i].nombre, self.parent.parent.subgrupos[i].nombre))

        return raices

    def OnRecuperadorCheck(self, event):
        if self.recuperadorCheck == True:
        else:

    def comprobarDatos(self):
        caudal = self.equipoVentilacion
        if ',' in caudal:
            caudal = caudal.replace(',', '.')
            self.equipoVentilacion= caudal
        rendimiento = self.rendimiento
        if ',' in rendimiento:
            rendimiento = rendimiento.replace(',', '.')
            self.rendimiento= rendimiento
        self.listaErrores = ''
        self.listaErrores += Comprueba(self.nombreInstalacion, 1, self.listaErrores, 'nombre').ErrorDevuelto
        self.listaErrores += Comprueba(self.subgrupoChoice.GetStringSelection(), 0, self.listaErrores, 'zona').ErrorDevuelto
        self.listaErrores += Comprueba(self.equipoVentilacion, 2, self.listaErrores, 'caudal de ventilación', 0).ErrorDevuelto
        if self.recuperadorCheck == True:
            self.listaErrores += Comprueba(self.rendimiento, 2, self.listaErrores, 'rendimiento estacional', 0, 100).ErrorDevuelto

    def cogerDatos(self):
        self.comprobarDatos()
        if self.listaErrores != '':
            return self.listaErrores
        datos = []
        datos.append(self.nombreInstalacion)
        datos.append('ventilacion')
        datos.append(self.equipoVentilacion)
        datos.append(self.recuperadorCheck)
        if self.recuperadorCheck == True:
            datos.append(self.rendimiento)
        else:
            datos.append(0)
        datos.append(self.subgrupoChoice.GetStringSelection())
        return datos

    def cargarDatos(self, datos):
        self.nombreInstalacion= datos[0]
        self.equipoVentilacion= datos[2]
        self.recuperadorCheck= datos[3]
        if self.recuperadorCheck == True:
            self.rendimiento= str(datos[4])
        else:
            self.rendimiento= ''
        self.OnRecuperadorCheck(None)
        self.subgrupoChoice.SetStringSelection(datos[5])
        return