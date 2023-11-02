# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\panelRenovables.pyc
# Compiled at: 2015-02-19 13:18:33
from Instalaciones.comprobarCampos import Comprueba, Comprueba2
from miChoice import MiChoice
import Calculos.listadosWeb as listadosWeb, wx, logging

class Panel1(wx.Panel):

    def _init_ctrls(self, prnt, id, posi, siz, styles, named):
        self.nombreInstalacion = 'Contribuciones energéticas'
        self.subgrupoChoice = MiChoice(choices=[])
        # self.fuenteRadioFuentes de energía renovable
        self.fuenteRadio= False
        # self.generacionRadioGeneración electricidad mediante renovables / Cogeneración
        self.porcentajeACSText.Enable(False)
        self.porcentajeACS = ''
        self.porcentajeACS.Enable(False)
        self.porcentajeUnidadesACS.Enable(False)
        self.porcentajeCalefaccionText.Enable(False)
        self.porcentajeCalefaccion = ''
        self.porcentajeCalefaccion.Enable(False)
        self.porcentajeUnidadesCal.Enable(False)
        self.porcentajeRefrigeracionText.Enable(False)
        self.porcentajeRefrigeracion = ''
        self.porcentajeRefrigeracion.Enable(False)
        self.porcentajeUnidadesRef.Enable(False)
        # self.captadoresCheckDefinir Captadores Solares
        self.captadoresCheck= False
        self.fChartButton.Enable(False)
        self.energiaText.Enable(False)
        self.energia = ''
        self.energia.Enable(False)
        self.energiaUnidadesText.Enable(False)
        self.calorGeneradoACSText.Enable(False)
        self.calorGeneradoACS = ''
        self.calorGeneradoACS.Enable(False)
        self.calorGeneradoACSUnidadesText.Enable(False)
        self.calorGeneradoCalText.Enable(False)
        self.calorGeneradoCal = ''
        self.calorGeneradoCal.Enable(False)
        self.calorGeneradoUnidadesCalText.Enable(False)
        self.calorGeneradoRefText.Enable(False)
        self.calorGeneradoRef = ''
        self.calorGeneradoRef.Enable(False)
        self.calorGeneradoUnidadesRefText.Enable(False)
        self.energiaConsumidaText.Enable(False)
        self.energiaConsumida = ''
        self.energiaConsumida.Enable(False)
        self.energiaConsumidaUnidadesText.Enable(False)
        self.tipoCombustibleText.Enable(False)
        self.combustibleChoice = MiChoice(choices=listadosWeb.listadoCombustibles)
        self.combustibleChoice.Enable(False)

    def OnNombreInstalacion(self, event):
        if self.nombreInstalacion == 'Contribuciones energéticas':
        else:

    def cargarRaices(self):
        raices = []
        raices.append(('Edificio Objeto', 'Edificio Objeto'))
        for i in range(len(self.parent.parent.subgrupos)):
            if self.parent.parent.subgrupos[i].nombre != 'Edificio Objeto':
                raices.append((self.parent.parent.subgrupos[i].nombre, self.parent.parent.subgrupos[i].nombre))

        return raices

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

    def __init__(self, parent, id, pos, size, style, name, real_parent=None):
        if real_parent == None:
            self.parent = parent
        else:
            self.parent = real_parent
        self.tipoSistema = 'renovables'
        self._init_ctrls(parent, id, pos, size, style, name)
        self.listaErrores = ''
        self.subgrupoChoice.SetItems(self.cargarRaices())
        self.elegirRaiz()
        return

    def OncaptadoresCheck(self, event):
        if self.captadoresCheck == True:
            self.fChartButton.Enable(True)
        else:
            self.fChartButton.Enable(False)

    def OnFuentesRenovablesCheck(self, event):
        if self.fuenteRadio == True:
            self.porcentajeACSText.Enable(True)
            self.porcentajeACS.Enable(True)
            self.porcentajeUnidadesCal.Enable(True)
            self.porcentajeCalefaccionText.Enable(True)
            self.porcentajeCalefaccion.Enable(True)
            self.porcentajeUnidadesACS.Enable(True)
            self.porcentajeRefrigeracionText.Enable(True)
            self.porcentajeRefrigeracion.Enable(True)
            self.porcentajeUnidadesRef.Enable(True)
        else:
            self.porcentajeACSText.Enable(False)
            self.porcentajeACS.Enable(False)
            self.porcentajeUnidadesCal.Enable(False)
            self.porcentajeCalefaccionText.Enable(False)
            self.porcentajeCalefaccion.Enable(False)
            self.porcentajeUnidadesACS.Enable(False)
            self.porcentajeRefrigeracionText.Enable(False)
            self.porcentajeRefrigeracion.Enable(False)
            self.porcentajeUnidadesRef.Enable(False)

    def OnGeneracionElectricaCheck(self, event):
        if self.generacionRadio == True:
            self.energiaText.Enable(True)
            self.energia.Enable(True)
            self.energiaUnidadesText.Enable(True)
            self.energiaConsumidaText.Enable(True)
            self.energiaConsumida.Enable(True)
            self.energiaConsumidaUnidadesText.Enable(True)
            self.combustibleChoice.Enable(True)
            self.tipoCombustibleText.Enable(True)
            self.calorGeneradoCalText.Enable(True)
            self.calorGeneradoCal.Enable(True)
            self.calorGeneradoUnidadesCalText.Enable(True)
            self.calorGeneradoACSText.Enable(True)
            self.calorGeneradoACS.Enable(True)
            self.calorGeneradoACSUnidadesText.Enable(True)
            self.calorGeneradoRefText.Enable(True)
            self.calorGeneradoRef.Enable(True)
            self.calorGeneradoUnidadesRefText.Enable(True)
        else:
            self.energiaText.Enable(False)
            self.energia.Enable(False)
            self.energiaUnidadesText.Enable(False)
            self.energiaConsumidaText.Enable(False)
            self.energiaConsumida.Enable(False)
            self.energiaConsumidaUnidadesText.Enable(False)
            self.combustibleChoice.Enable(False)
            self.tipoCombustibleText.Enable(False)
            self.calorGeneradoCalText.Enable(False)
            self.calorGeneradoCal.Enable(False)
            self.calorGeneradoUnidadesCalText.Enable(False)
            self.calorGeneradoACSText.Enable(False)
            self.calorGeneradoACS.Enable(False)
            self.calorGeneradoACSUnidadesText.Enable(False)
            self.calorGeneradoRefText.Enable(False)
            self.calorGeneradoRef.Enable(False)
            self.calorGeneradoUnidadesRefText.Enable(False)

    def cogerDatos(self):
        self.listaErrores = ''
        self.listaErrores += Comprueba(self.nombreInstalacion, 1, self.listaErrores, 'nombre').ErrorDevuelto
        self.listaErrores += Comprueba(self.subgrupoChoice.GetStringSelection(), 0, self.listaErrores, 'zona').ErrorDevuelto
        if self.fuenteRadio == False and self.generacionRadio == False:
            self.listaErrores = 'No se ha indicado ningún valor'
            return self.listaErrores
        porcentajeACS = self.porcentajeACS
        porcentajeCal = self.porcentajeCalefaccion
        porcentajeRef = self.porcentajeRefrigeracion
        energiaElectrica = self.energia
        energiaElectrica2 = self.energiaConsumida
        calorGeneradoCal = self.calorGeneradoCal
        calorGeneradoACS = self.calorGeneradoACS
        calorGeneradoRef = self.calorGeneradoRef
        if ',' in porcentajeACS:
            porcentajeACS = porcentajeACS.replace(',', '.')
            self.porcentajeACS= porcentajeACS
        if ',' in porcentajeCal:
            porcentajeCal = porcentajeCal.replace(',', '.')
            self.porcentajeCalefaccion= porcentajeCal
        if ',' in porcentajeRef:
            porcentajeRef = porcentajeRef.replace(',', '.')
            self.porcentajeRefrigeracion= porcentajeRef
        if ',' in energiaElectrica:
            energiaElectrica = energiaElectrica.replace(',', '.')
            self.energia= energiaElectrica
        if ',' in energiaElectrica2:
            energiaElectrica2 = energiaElectrica2.replace(',', '.')
            self.energiaConsumida= energiaElectrica2
        if ',' in calorGeneradoCal:
            calorGeneradoCal = calorGeneradoCal.replace(',', '.')
            self.calorGeneradoCal= calorGeneradoCal
        if ',' in calorGeneradoACS:
            calorGeneradoACS = calorGeneradoACS.replace(',', '.')
            self.calorGeneradoACS= calorGeneradoACS
        if ',' in calorGeneradoRef:
            calorGeneradoRef = calorGeneradoRef.replace(',', '.')
            self.calorGeneradoRef= calorGeneradoRef
        if self.fuenteRadio == True:
            if porcentajeACS == '' and porcentajeCal == '' and porcentajeRef == '':
                self.listaErrores += '\nNo se ha indicado ningún valor de fuentes de energía renovables'
            else:
                if porcentajeACS != '':
                    self.listaErrores += Comprueba2(porcentajeACS, 2, self.listaErrores, 'contribución renovable para ACS', 0.0, 100.0).ErrorDevuelto
                if porcentajeCal != '':
                    self.listaErrores += Comprueba2(porcentajeCal, 2, self.listaErrores, 'contribución renovable para calefacción', 0.0, 100.0).ErrorDevuelto
                if porcentajeRef != '':
                    self.listaErrores += Comprueba2(porcentajeRef, 2, self.listaErrores, 'contribución renovable para refrigeración', 0.0, 100.0).ErrorDevuelto
        if self.generacionRadio == True:
            if energiaElectrica == '' and energiaElectrica2 == '' and calorGeneradoCal == '' and calorGeneradoACS == '' and calorGeneradoRef == '':
                self.listaErrores += '\nNo se ha indicado ningún valor generación de electricidad mediante renovables/cogeneración'
            else:
                if energiaElectrica != '':
                    self.listaErrores += Comprueba2(energiaElectrica, 2, self.listaErrores, 'energía eléctrica generada', 0).ErrorDevuelto
                if energiaElectrica2 != '':
                    self.listaErrores += Comprueba2(energiaElectrica2, 2, self.listaErrores, 'energía consumida', 0).ErrorDevuelto
                    self.listaErrores += Comprueba(self.combustibleChoice.GetStringSelection(), 0, self.listaErrores, 'tipo de combustible').ErrorDevuelto
                if calorGeneradoACS != '':
                    self.listaErrores += Comprueba2(calorGeneradoACS, 2, self.listaErrores, 'calor recuperado para ACS', 0).ErrorDevuelto
                if calorGeneradoCal != '':
                    self.listaErrores += Comprueba2(calorGeneradoCal, 2, self.listaErrores, 'calor recuperado para calefacción', 0).ErrorDevuelto
                if calorGeneradoRef != '':
                    self.listaErrores += Comprueba2(calorGeneradoRef, 2, self.listaErrores, 'frío recuperado', 0).ErrorDevuelto
        if self.listaErrores != '':
            return self.listaErrores
        datos = []
        datos.append(self.nombreInstalacion)
        datos.append('renovable')
        if self.fuenteRadio == True:
            datosRenovable = [
             self.porcentajeACS, self.porcentajeCalefaccion,
             self.porcentajeRefrigeracion, self.captadoresCheck]
        else:
            datosRenovable = [
             '', '', '', False]
        datos.append(datosRenovable)
        if self.generacionRadio == True:
            datosElectricidad = [
             self.energia, self.calorGeneradoACS,
             self.calorGeneradoCal, self.calorGeneradoRef,
             self.energiaConsumida, self.combustibleChoice.GetStringSelection()]
        else:
            datosElectricidad = [
             '', '', '', '', '', '']
        datos.append(datosElectricidad)
        datos.append([self.fuenteRadio, self.generacionRadio])
        datos.append(self.subgrupoChoice.GetStringSelection())
        return datos

    def cargarDatos(self, datos):
        self.nombreInstalacion= datos[0]
        datosRenovable = datos[2]
        self.porcentajeACS= datosRenovable[0]
        self.porcentajeCalefaccion= datosRenovable[1]
        self.porcentajeRefrigeracion= datosRenovable[2]
        self.captadoresCheck= datosRenovable[3]
        datosElectricidad = datos[3]
        self.energia= datosElectricidad[0]
        self.calorGeneradoACS= datosElectricidad[1]
        self.calorGeneradoCal= datosElectricidad[2]
        self.calorGeneradoRef= datosElectricidad[3]
        self.energiaConsumida= datosElectricidad[4]
        self.combustibleChoice.SetStringSelection(datosElectricidad[5])
        self.fuenteRadio= datos[4][0]
        self.generacionRadio= datos[4][1]
        self.subgrupoChoice.SetStringSelection(datos[5])
        self.OnFuentesRenovablesCheck(None)
        self.OnGeneracionElectricaCheck(None)
        self.OncaptadoresCheck(None)
        return