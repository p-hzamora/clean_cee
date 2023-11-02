# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\panelVentiladores.pyc
# Compiled at: 2015-02-19 13:18:33
from Instalaciones.comprobarCampos import Comprueba, Comprueba2
from miChoice import MiChoice
import Instalaciones.ayudaNumeroHoras as ayudaNumeroHoras, Instalaciones.dialogoCurva as dialogoCurva, Instalaciones.dialogoEscalones as dialogoEscalones, Instalaciones.equipos as equipos, Instalaciones.perfilesTerciario as perfilesTerciario
from Calculos.funcionesCalculo import calculoNumeroHorasOcupacionEdificio
import Calculos.listadosWeb as listadosWeb, wx, logging

class Panel1(wx.Panel):

    def _init_ctrls(self, prnt, id, posi, siz, styles, named):
        self.nombreInstalacion = 'Ventilador'
        self.subgrupoChoice = MiChoice(choices=[])
        self.ventiladorChoice = MiChoice(choices=listadosWeb.listadoOpcionesVentiladores)
        self.ventiladorChoice.SetSelection(0)
        self.seleccionServicio = MiChoice(choices=listadosWeb.listadoOpcionesServicioVentiladores)
        self.seleccionServicio.SetHelpText('Seleccione el servicio al que está asignada este ventilador. En el que caso de que se encuentre asignada a varios servicios,  deberá crear varios ventiladores,  asignando cada una de ellos al servicio correspondiente. ')
        self.seleccionServicio.SetLabel('')
        self.seleccionServicio.SetSelection(0)
        self.EstimacionConsumoChoice = MiChoice(choices=listadosWeb.listadoOpcionesConsumoBombasOVentiladores)
        self.EstimacionConsumoChoice.SetSelection(0)
        self.consumo = ''
        self.consumo.SetEditable(False)
        self.consumo.Enable(True)
        self.potenciaElectricaNominal = ''
        self.numeroHorasDemanda = ''
        self.funcionamientoNoDemanda = wx.RadioBox(choices=['Si', 'No'], id=wxID_FUNCIONAMIENTONODEMANDABOX1, label='¿Funciona el ventilador cuando no hay demanda térmica?', majorDimension=2, name='radioBox1', parent=self, pos=wx.Point(0, 247), size=wx.Size(710, 95), style=wx.RA_SPECIFY_COLS)
        self.funcionamientoNoDemanda.SetSelection(1)
        self.horasTemporadaAcs = ''
        self.horasTemporadaAcs= str(self.numeroHorasAcs)
        self.horasTemporadaCalefaccion = ''
        self.horasTemporadaCalefaccion= str(self.numeroHorasCalefaccion)
        self.horasTemporadaRefrigeracion = ''
        self.horasTemporadaRefrigeracion= str(self.numeroHorasRefrigeracion)
        self.fraccionPotenciaNoDemanda = ''
        self.fraccionPotenciaNoDemanda= '0.3'

    def OnBotonDefinirEscalones(self, event):
        dlg = dialogoEscalones.Dialog1(self, self.potenciaFcp)
        dlg.ShowModal()
        if dlg.dev == True:
            self.potenciaFcp = []
            for i in range(10):
                self.potenciaFcp.append(dlg.potenciaFcp.GetCellValue(0, i))

            self.obtenerConsumoEstacional(None)
            dlg.Destroy()
        return

    def OnBotonDefinirCurva(self, event):
        dlg = dialogoCurva.Dialog1(self, self.c1, self.c2, self.c3, self.c4)
        dlg.ShowModal()
        if dlg.dev == True:
            self.c1 = dlg.c1
            self.c2 = dlg.c2
            self.c3 = dlg.c3
            self.c4 = dlg.c4
            self.obtenerConsumoEstacional(None)
            dlg.Destroy()
        return

    def OnNombreInstalacion(self, event):
        if self.nombreInstalacion == 'Ventilador':
        else:

    def OnfuncionamientoNoDemandaRadiobox(self, event):
        eleccion = self.seleccionServicio.GetSelection()
        if eleccion == 0 and self.horasTemporadaCalefaccion == '':
            self.calculoNumeroHorasTemporada()
            self.horasTemporadaCalefaccion= str(self.numeroHorasCalefaccion)
        elif eleccion == 1 and self.horasTemporadaRefrigeracion == '':
            self.calculoNumeroHorasTemporada()
            self.horasTemporadaRefrigeracion= str(self.numeroHorasRefrigeracion)
        if self.fraccionPotenciaNoDemanda == '':
            self.fraccionPotenciaNoDemanda= '0.3'
        if self.funcionamientoNoDemanda.GetSelection() == 0:
            if eleccion == 0:
            elif eleccion == 1:
        else:
        self.obtenerConsumoEstacional(None)
        return

    def calculoNumeroHorasTemporada(self):
        if self.parent.parent.parent.programa == 'Residencial':
            self.numeroHorasAcs = 8760.0
            self.numeroHorasCalefaccion = 5760.0
            self.numeroHorasRefrigeracion = 2880.0
        else:
            tipoEdificio = self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
            numeroHoras = calculoNumeroHorasOcupacionEdificio(tipoEdificio)
            self.numeroHorasAcs = numeroHoras
            self.numeroHorasCalefaccion = numeroHoras
            self.numeroHorasRefrigeracion = numeroHoras

    def __init__(self, parent, id, pos, size, style, name, real_parent=None):
        if real_parent == None:
            self.parent = parent
        else:
            self.parent = real_parent
        self.numeroHorasAcs = ''
        self.numeroHorasCalefaccion = ''
        self.numeroHorasRefrigeracion = ''
        self.calculoNumeroHorasTemporada()
        self._init_ctrls(parent, id, pos, size, style, name)
        self.potenciaFcp = [
         '0.15', '0.15', '0.16', '0.2', '0.25', '0.34', '0.45', 
         '0.62', '0.83', '1.0']
        self.c1 = '0.199'
        self.c2 = '-0.4144'
        self.c3 = '0.81118'
        self.c4 = '0.4542'
        self.tipoSistema = 'ventiladores'
        self.listaErrores = ''
        self.subgrupoChoice.SetItems(self.cargarRaices())
        self.rendimientoEstacionalRef = ''
        self.OnVentiladorChoice(None)
        self.OnEstimacionConsumoChoice(None)
        self.OnfuncionamientoNoDemandaRadiobox(None)
        self.elegirRaiz()
        self.obtenerConsumoEstacional(None)
        return

    def obtenerConsumoEstacional(self, event):
        try:
            zona = self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()
            if self.parent.parent.parent.programa == 'Residencial':
                uso = 'Residencial'
            else:
                uso = self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
            if self.seleccionServicio.GetStringSelection() == 'Calefacción':
                repartoEnergiaPorcentualCaracteristico = perfilesTerciario.PerfilDemandaCalefaccion(zona, uso)
            elif self.seleccionServicio.GetStringSelection() == 'Refrigeración':
                repartoEnergiaPorcentualCaracteristico = perfilesTerciario.PerfilDemandaRefrigeracion(zona, uso)
            fcpSistema = [
             0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 
             0.75, 0.85, 0.95]
            aux = [ repartoEnergiaPorcentualCaracteristico[i] / fcpSistema[i] for i in range(len(fcpSistema)) ]
            total = sum(aux)
            repartoTiempoPorcentualCaracteristico = [ x / total for x in aux ]
            eleccion = self.seleccionServicio.GetSelection()
            horasTodaTemporada = 0
            if self.funcionamientoNoDemanda.GetSelection() == 0:
                if eleccion == 0:
                    horasTodaTemporada = float(self.horasTemporadaCalefaccion)
                    horasDemanda = float(self.numeroHorasDemanda)
                    if horasTodaTemporada < horasDemanda:
                        self.consumo= ''
                        return
                elif eleccion == 1:
                    horasTodaTemporada = float(self.horasTemporadaRefrigeracion)
                    horasDemanda = float(self.numeroHorasDemanda)
                    if horasTodaTemporada < horasDemanda:
                        self.consumo= ''
                        return
            if self.EstimacionConsumoChoice.GetSelection() == 0:
                pass
            elif self.ventiladorChoice.GetSelection() == 0 and self.EstimacionConsumoChoice.GetSelection() == 1:
                consumoAnual = float(self.potenciaElectricaNominal) * float(self.numeroHorasDemanda)
                horasAdicionales = horasTodaTemporada - float(self.numeroHorasDemanda)
                if horasAdicionales < 0:
                    horasAdicionales = 0
                if self.funcionamientoNoDemanda.GetSelection() == 0:
                    consumoAnual += horasAdicionales * float(self.potenciaElectricaNominal) * float(self.fraccionPotenciaNoDemanda)
                self.consumo= str(round(consumoAnual, 1))
            elif self.ventiladorChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 1:
                ventilador = equipos.ventiladorCaudalVariable2()
                ventilador.escalonesPotencia = []
                for i in range(10):
                    ventilador.fcp.append(i / 10.0 + 0.1)
                    ventilador.escalonesPotencia.append(float(self.potenciaFcp[i]))

                ventilador.potenciaElectricaNominal = float(self.potenciaElectricaNominal)
                potenciaEnCadaFcp = [ ventilador.potFCP(x) for x in fcpSistema ]
                potenciaMediaEstacional = sum([ potenciaEnCadaFcp[i] * repartoTiempoPorcentualCaracteristico[i] for i in range(len(potenciaEnCadaFcp))
                                              ])
                consumoAnual = potenciaMediaEstacional * float(self.numeroHorasDemanda)
                horasAdicionales = horasTodaTemporada - float(self.numeroHorasDemanda)
                if horasAdicionales < 0:
                    horasAdicionales = 0
                if self.funcionamientoNoDemanda.GetSelection() == 0:
                    consumoAnual += horasAdicionales * ventilador.potFCP(float(self.fraccionPotenciaNoDemanda))
                self.consumo= str(round(consumoAnual, 1))
            elif self.ventiladorChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 2:
                ventilador = equipos.ventiladorCaudalVariable()
                ventilador.c1 = float(self.c1)
                ventilador.c2 = float(self.c2)
                ventilador.c3 = float(self.c3)
                ventilador.c4 = float(self.c4)
                ventilador.potenciaElectricaNominal = float(self.potenciaElectricaNominal)
                potenciaEnCadaFcp = [ ventilador.potFCP(x) for x in fcpSistema ]
                potenciaMediaEstacional = sum([ potenciaEnCadaFcp[i] * repartoTiempoPorcentualCaracteristico[i] for i in range(len(potenciaEnCadaFcp))
                                              ])
                consumoAnual = potenciaMediaEstacional * float(self.numeroHorasDemanda)
                horasAdicionales = horasTodaTemporada - float(self.numeroHorasDemanda)
                if horasAdicionales < 0:
                    horasAdicionales = 0
                if self.funcionamientoNoDemanda.GetSelection() == 0:
                    consumoAnual += horasAdicionales * ventilador.potFCP(float(self.fraccionPotenciaNoDemanda))
                self.consumo= str(round(consumoAnual, 1))
        except:
            self.consumo= ''

    def elegirRaiz(self):
        sel = self.parent.arbolInstalaciones.GetSelection()
        try:
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

    def OnVentiladorChoice(self, event):
        if self.ventiladorChoice.GetSelection() == 0:
            self.EstimacionConsumoChoice.SetItems(listadosWeb.listadoOpcionesConsumoBombasOVentiladores)
            self.EstimacionConsumoChoice.SetSelection(0)
        else:
            self.EstimacionConsumoChoice.SetItems(listadosWeb.listadoOpcionesConsumoBombasOVentiladoresCaudalVariable)
            self.EstimacionConsumoChoice.SetSelection(0)
        self.OnEstimacionConsumoChoice(None)
        return

    def OnEstimacionConsumoChoice(self, event):
        if self.EstimacionConsumoChoice.GetSelection() == 0:
            self.consumo.SetEditable(True)
            self.consumo.Enable(True)
            self.OnfuncionamientoNoDemandaRadiobox(None)
        else:
            self.OnfuncionamientoNoDemandaRadiobox(None)
            if self.ventiladorChoice.GetSelection() == 0 and self.EstimacionConsumoChoice.GetSelection() == 1:
                self.consumo= ''
                self.consumo.SetEditable(False)
                self.consumo.Enable(False)
            elif self.ventiladorChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 1:
                self.consumo= ''
                self.consumo.SetEditable(False)
                self.consumo.Enable(False)
            elif self.ventiladorChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 2:
                self.consumo= ''
                self.consumo.SetEditable(False)
                self.consumo.Enable(False)
        self.obtenerConsumoEstacional(None)
        return

    def comprobarDatos(self):
        self.listaErrores = ''
        self.listaErrores += Comprueba(self.nombreInstalacion, 1, self.listaErrores, 'nombre').ErrorDevuelto
        self.listaErrores += Comprueba(self.subgrupoChoice.GetStringSelection(), 0, self.listaErrores, 'zona').ErrorDevuelto
        self.listaErrores += Comprueba(self.ventiladorChoice.GetStringSelection(), 0, self.listaErrores, 'tipo de ventilador').ErrorDevuelto
        self.listaErrores += Comprueba(self.EstimacionConsumoChoice.GetStringSelection(), 0, self.listaErrores, 'definir estimación consumo').ErrorDevuelto
        self.listaErrores += Comprueba(self.seleccionServicio.GetStringSelection(), 0, self.listaErrores, 'servicio').ErrorDevuelto
        if self.EstimacionConsumoChoice.GetSelection() == 0:
            dato = self.consumo
            if ',' in dato:
                dato = dato.replace(',', '.')
                self.consumo= dato
            self.listaErrores += Comprueba(self.consumo, 2, self.listaErrores, 'consumo anual (kWh)', 0.0).ErrorDevuelto
        else:
            dato = self.potenciaElectricaNominal
            if ',' in dato:
                dato = dato.replace(',', '.')
                self.potenciaElectricaNominal= dato
            dato = self.numeroHorasDemanda
            if ',' in dato:
                dato = dato.replace(',', '.')
                self.numeroHorasDemanda= dato
            if self.ventiladorChoice.GetSelection() == 0 and self.EstimacionConsumoChoice.GetSelection() == 1:
                self.listaErrores += Comprueba(self.potenciaElectricaNominal, 2, self.listaErrores, 'potencia eléctrica', 0.0).ErrorDevuelto
                self.listaErrores += Comprueba(self.numeroHorasDemanda, 2, self.listaErrores, 'número de horas de demanda', 0.0).ErrorDevuelto
            elif self.ventiladorChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 1:
                self.listaErrores += Comprueba(self.potenciaElectricaNominal, 2, self.listaErrores, 'potencia eléctrica', 0.0).ErrorDevuelto
                self.listaErrores += Comprueba(self.numeroHorasDemanda, 2, self.listaErrores, 'número de horas de demanda', 0.0).ErrorDevuelto
                for i in range(10):
                    dato = self.potenciaFcp[i]
                    if ',' in dato:
                        dato = dato.replace(',', '.')
                        self.potenciaFcp[i] = dato
                    self.listaErrores += Comprueba2(self.potenciaFcp[i], 2, self.listaErrores, 'posición %i erronea' % i, 0.0, 1.0).ErrorDevuelto

            elif self.ventiladorChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 2:
                dato = self.c1
                if ',' in dato:
                    dato = dato.replace(',', '.')
                    self.c1 = dato
                dato = self.c2
                if ',' in dato:
                    dato = dato.replace(',', '.')
                    self.c2 = dato
                dato = self.c3
                if ',' in dato:
                    dato = dato.replace(',', '.')
                    self.c3 = dato
                dato = self.c4
                if ',' in dato:
                    dato = dato.replace(',', '.')
                    self.c4 = dato
                self.listaErrores += Comprueba(self.potenciaElectricaNominal, 2, self.listaErrores, 'potencia eléctrica', 0.0).ErrorDevuelto
                self.listaErrores += Comprueba(self.numeroHorasDemanda, 2, self.listaErrores, 'número de horas de demanda', 0.0).ErrorDevuelto
                self.listaErrores += Comprueba(self.c1, 2, self.listaErrores, 'Coeficiente C1').ErrorDevuelto
                self.listaErrores += Comprueba(self.c2, 2, self.listaErrores, 'Coeficiente C2').ErrorDevuelto
                self.listaErrores += Comprueba(self.c3, 2, self.listaErrores, 'Coeficiente C3').ErrorDevuelto
                self.listaErrores += Comprueba(self.c4, 2, self.listaErrores, 'Coeficiente C4').ErrorDevuelto
            ErrorNumeroHorasDemanda = Comprueba(self.numeroHorasDemanda, 2, self.listaErrores, 'número de horas de demanda', 0.0).ErrorDevuelto
            if self.funcionamientoNoDemanda.GetSelection() == 0:
                if self.seleccionServicio.GetSelection() == 0:
                    dato = self.horasTemporadaCalefaccion
                    if ',' in dato:
                        dato = dato.replace(',', '.')
                        self.horasTemporadaCalefaccion= dato
                    dato = self.fraccionPotenciaNoDemanda
                    if ',' in dato:
                        dato = dato.replace(',', '.')
                        self.fraccionPotenciaNoDemanda= dato
                    if ErrorNumeroHorasDemanda != '':
                        self.listaErrores += Comprueba(self.horasTemporadaCalefaccion, 2, self.listaErrores, 'duración temporada de calefacción', 0.0).ErrorDevuelto
                    else:
                        self.listaErrores += Comprueba2(self.horasTemporadaCalefaccion, 2, self.listaErrores, 'duración temporada de calefacción', float(self.numeroHorasDemanda)).ErrorDevuelto
                    self.listaErrores += Comprueba(self.fraccionPotenciaNoDemanda, 2, self.listaErrores, 'fracción potencia durante no demanda', 0.0, 1.0).ErrorDevuelto
                elif self.seleccionServicio.GetSelection() == 1:
                    dato = self.horasTemporadaRefrigeracion
                    if ',' in dato:
                        dato = dato.replace(',', '.')
                        self.horasTemporadaRefrigeracion= dato
                    dato = self.fraccionPotenciaNoDemanda
                    if ',' in dato:
                        dato = dato.replace(',', '.')
                        self.fraccionPotenciaNoDemanda= dato
                    if ErrorNumeroHorasDemanda != '':
                        self.listaErrores += Comprueba(self.horasTemporadaRefrigeracion, 2, self.listaErrores, 'duración temporada de refrigeración', 0.0).ErrorDevuelto
                    else:
                        self.listaErrores += Comprueba2(self.horasTemporadaRefrigeracion, 2, self.listaErrores, 'duración temporada de refrigeración', float(self.numeroHorasDemanda)).ErrorDevuelto
                    self.listaErrores += Comprueba(self.fraccionPotenciaNoDemanda, 2, self.listaErrores, 'fracción potencia durante no demanda', 0.0, 1.0).ErrorDevuelto

    def OnSeleccionServicioChoice(self, event):
        eleccion = self.seleccionServicio.GetSelection()
        if self.funcionamientoNoDemanda.GetSelection() == 0:
            if eleccion == 0:
            elif eleccion == 1:
        else:
        self.OnEstimacionConsumoChoice(None)
        return

    def cogerDatos(self):
        self.comprobarDatos()
        if self.listaErrores != '':
            return self.listaErrores
        datos = []
        datos.append(self.nombreInstalacion)
        datos.append(self.tipoSistema)
        datos.append(self.consumo)
        datos.append(self.ventiladorChoice.GetSelection())
        datos.append(self.potenciaElectricaNominal)
        datos.append('')
        datos.append(self.EstimacionConsumoChoice.GetSelection())
        datos.append(self.numeroHorasDemanda)
        datos.append(self.c1)
        datos.append(self.c2)
        datos.append(self.c3)
        datos.append(self.c4)
        datos.append(self.seleccionServicio.GetSelection())
        if self.funcionamientoNoDemanda.GetSelection() == 0:
            datos.append(self.horasTemporadaAcs)
            datos.append(self.horasTemporadaCalefaccion)
            datos.append(self.horasTemporadaRefrigeracion)
            datos.append(self.fraccionPotenciaNoDemanda)
        else:
            datos.append('')
            datos.append('')
            datos.append('')
            datos.append('')
        datosConcretos = []
        for i in range(10):
            datosConcretos.append(self.potenciaFcp[i])

        datos.append(datosConcretos)
        datos.append(self.funcionamientoNoDemanda.GetSelection())
        datos.append(self.subgrupoChoice.GetStringSelection())
        return datos

    def cargarDatos(self, datos):
        self.nombreInstalacion= datos[0]
        self.consumo= datos[2]
        self.ventiladorChoice.SetSelection(datos[3])
        self.OnVentiladorChoice(None)
        self.potenciaElectricaNominal= datos[4]
        self.EstimacionConsumoChoice.SetSelection(datos[6])
        self.OnEstimacionConsumoChoice(None)
        self.numeroHorasDemanda= datos[7]
        self.c1 = datos[8]
        self.c2 = datos[9]
        self.c3 = datos[10]
        self.c4 = datos[11]
        self.seleccionServicio.SetSelection(datos[12])
        self.horasTemporadaAcs= datos[13]
        self.horasTemporadaCalefaccion= datos[14]
        self.horasTemporadaRefrigeracion= datos[15]
        self.fraccionPotenciaNoDemanda= datos[16]
        datosConcretos = datos[17]
        for i in range(10):
            self.potenciaFcp[i] = datosConcretos[i]

        self.funcionamientoNoDemanda.SetSelection(datos[18])
        self.OnfuncionamientoNoDemandaRadiobox(None)
        self.subgrupoChoice.SetStringSelection(datos[-1])
        return

    def OnNumeroHorasHelpButton(self, event):
        zona = self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()
        perfilUso = self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
        servicio = self.seleccionServicio.GetStringSelection()
        if zona == '':
            print('Debe indicar la localización del edificio en el panel de datos generales', 'Estimación del número de horas de funcionamiento')
        else:
            self.parent.parent.parent.calculoCalificacion()
            ayuda = ayudaNumeroHoras.Dialog1(self, zona, perfilUso, servicio)
            ayuda.ShowModal()
            if ayuda.dev != []:
                self.numeroHorasDemanda= str(ayuda.dev[0])