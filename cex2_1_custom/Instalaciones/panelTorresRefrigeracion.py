# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\panelTorresRefrigeracion.pyc
# Compiled at: 2015-02-19 13:18:33
from Instalaciones.comprobarCampos import Comprueba, Comprueba2
from miChoice import MiChoice
import Instalaciones.ayudaNumeroHoras as ayudaNumeroHoras, Instalaciones.dialogoCurva as dialogoCurva, Instalaciones.dialogoEscalones as dialogoEscalones, Instalaciones.equipos as equipos, Instalaciones.perfilesTerciario as perfilesTerciario, Calculos.listadosWeb as listadosWeb, wx, logging

class Panel1(wx.Panel):

    def _init_ctrls(self, prnt, id, posi, siz, styles, named):
        self.nombreInstalacion = 'Torre de refrigeración'
        self.subgrupoChoice = MiChoice(choices=[])
        self.torreChoice = MiChoice(choices=listadosWeb.listadoOpcionesTorreDeRefrigeracion)
        self.torreChoice.SetSelection(0)
        self.EstimacionConsumoChoice = MiChoice(choices=listadosWeb.listadoOpcionesConsumoBombasOVentiladores)
        self.EstimacionConsumoChoice.SetSelection(0)
        self.consumo = ''
        self.consumo.SetEditable(False)
        self.consumo.Enable(True)
        self.potenciaElectricaNominal = ''
        self.numeroHorasDemanda = ''

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
        if self.nombreInstalacion == 'Torre de refrigeración':
        else:

    def __init__(self, parent, id, pos, size, style, name, real_parent=None):
        if real_parent == None:
            self.parent = parent
        else:
            self.parent = real_parent
        self._init_ctrls(parent, id, pos, size, style, name)
        self.potenciaFcp = [
         '0.5', '0.5', '0.5', '0.5', '0.5', '1.0', '1.0', 
         '1.0', '1.0', '1.0']
        self.c1 = '0.3316'
        self.c2 = '-0.8856'
        self.c3 = '0.6055'
        self.c4 = '0.9484'
        self.tipoSistema = 'torresRefrigeracion'
        self.listaErrores = ''
        self.subgrupoChoice.SetItems(self.cargarRaices())
        self.rendimientoEstacionalRef = ''
        self.OnTorreChoice(None)
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
            repartoEnergiaPorcentualCaracteristico = perfilesTerciario.PerfilDemandaRefrigeracion(zona, uso)
            fcpSistema = [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]
            aux = [ repartoEnergiaPorcentualCaracteristico[i] / fcpSistema[i] for i in range(len(fcpSistema)) ]
            total = sum(aux)
            repartoTiempoPorcentualCaracteristico = [ x / total for x in aux ]
            if self.EstimacionConsumoChoice.GetSelection() == 0:
                pass
            elif self.torreChoice.GetSelection() == 0 and self.EstimacionConsumoChoice.GetSelection() == 1:
                consumoAnual = float(self.potenciaElectricaNominal) * float(self.numeroHorasDemanda)
                self.consumo= str(round(consumoAnual, 1))
            elif self.torreChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 1:
                torre = equipos.TorreRefrigeracionVelocidadVariable2()
                torre.escalonesPotencia = []
                for i in range(10):
                    torre.fcp.append(i / 10.0 + 0.1)
                    torre.escalonesPotencia.append(float(self.potenciaFcp[i]))

                torre.potenciaElectricaNominal = float(self.potenciaElectricaNominal)
                potenciaEnCadaFcp = [ torre.potFCP(x) for x in fcpSistema ]
                potenciaMediaEstacional = sum([ potenciaEnCadaFcp[i] * repartoTiempoPorcentualCaracteristico[i] for i in range(len(potenciaEnCadaFcp))
                                              ])
                consumoAnual = potenciaMediaEstacional * float(self.numeroHorasDemanda)
                self.consumo= str(round(consumoAnual, 1))
            elif self.torreChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 2:
                torre = equipos.TorreRefrigeracionVelocidadVariable()
                torre.c1 = float(self.c1)
                torre.c2 = float(self.c2)
                torre.c3 = float(self.c3)
                torre.c4 = float(self.c4)
                torre.potenciaElectricaNominal = float(self.potenciaElectricaNominal)
                potenciaEnCadaFcp = [ torre.potFCP(x) for x in fcpSistema ]
                potenciaMediaEstacional = sum([ potenciaEnCadaFcp[i] * repartoTiempoPorcentualCaracteristico[i] for i in range(len(potenciaEnCadaFcp))
                                              ])
                consumoAnual = potenciaMediaEstacional * float(self.numeroHorasDemanda)
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

    def OnTorreChoice(self, event):
        if self.torreChoice.GetSelection() == 0:
            self.EstimacionConsumoChoice.SetItems(listadosWeb.listadoOpcionesConsumoBombasOVentiladores)
        else:
            self.EstimacionConsumoChoice.SetItems(listadosWeb.listadoOpcionesConsumoBombasOVentiladoresCaudalVariable)
            self.EstimacionConsumoChoice.SetSelection(0)
        self.OnEstimacionConsumoChoice(None)
        return

    def OnEstimacionConsumoChoice(self, event):
        if self.EstimacionConsumoChoice.GetSelection() == 0:
            self.consumo.SetEditable(True)
            self.consumo.Enable(True)
        elif self.torreChoice.GetSelection() == 0 and self.EstimacionConsumoChoice.GetSelection() == 1:
            self.consumo= ''
            self.consumo.SetEditable(False)
            self.consumo.Enable(False)
        elif self.torreChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 1:
            self.consumo= ''
            self.consumo.SetEditable(False)
            self.consumo.Enable(False)
        elif self.torreChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 2:
            self.consumo= ''
            self.consumo.SetEditable(False)
            self.consumo.Enable(False)
        self.obtenerConsumoEstacional(None)
        return

    def comprobarDatos(self):
        self.listaErrores = ''
        self.listaErrores += Comprueba(self.nombreInstalacion, 1, self.listaErrores, 'nombre').ErrorDevuelto
        self.listaErrores += Comprueba(self.subgrupoChoice.GetStringSelection(), 0, self.listaErrores, 'zona').ErrorDevuelto
        self.listaErrores += Comprueba(self.torreChoice.GetStringSelection(), 0, self.listaErrores, 'tipo de generador').ErrorDevuelto
        self.listaErrores += Comprueba(self.EstimacionConsumoChoice.GetStringSelection(), 0, self.listaErrores, 'definir estimación consumo').ErrorDevuelto
        if self.EstimacionConsumoChoice.GetSelection() == 0:
            dato = self.consumo
            if ',' in dato:
                dato = dato.replace(',', '.')
                self.consumo= dato
            self.listaErrores += Comprueba(self.consumo, 2, self.listaErrores, 'consumo anual', 0.0).ErrorDevuelto
        else:
            dato = self.potenciaElectricaNominal
            if ',' in dato:
                dato = dato.replace(',', '.')
                self.potenciaElectricaNominal= dato
            dato = self.numeroHorasDemanda
            if ',' in dato:
                dato = dato.replace(',', '.')
                self.numeroHorasDemanda= dato
            if self.torreChoice.GetSelection() == 0 and self.EstimacionConsumoChoice.GetSelection() == 1:
                self.listaErrores += Comprueba(self.potenciaElectricaNominal, 2, self.listaErrores, 'potencia eléctrica', 0.0).ErrorDevuelto
                self.listaErrores += Comprueba(self.numeroHorasDemanda, 2, self.listaErrores, 'número de horas de demanda', 0.0).ErrorDevuelto
            elif self.torreChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 1:
                self.listaErrores += Comprueba(self.potenciaElectricaNominal, 2, self.listaErrores, 'potencia eléctrica', 0.0).ErrorDevuelto
                self.listaErrores += Comprueba(self.numeroHorasDemanda, 2, self.listaErrores, 'número de horas de demanda', 0.0).ErrorDevuelto
                for i in range(10):
                    dato = self.potenciaFcp[i]
                    if ',' in dato:
                        dato = dato.replace(',', '.')
                        self.potenciaFcp[i] = dato
                    self.listaErrores += Comprueba2(self.potenciaFcp[i], 2, self.listaErrores, 'posición %i erronea' % i, 0.0, 1.0).ErrorDevuelto

            elif self.torreChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 2:
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
                self.listaErrores += Comprueba(self.c1, 2, self.listaErrores, 'coeficiente C1').ErrorDevuelto
                self.listaErrores += Comprueba(self.c2, 2, self.listaErrores, 'coeficiente C2').ErrorDevuelto
                self.listaErrores += Comprueba(self.c3, 2, self.listaErrores, 'coeficiente C3').ErrorDevuelto
                self.listaErrores += Comprueba(self.c4, 2, self.listaErrores, 'coeficiente C4').ErrorDevuelto

    def cogerDatos(self):
        self.comprobarDatos()
        if self.listaErrores != '':
            return self.listaErrores
        datos = []
        datos.append(self.nombreInstalacion)
        datos.append(self.tipoSistema)
        datos.append(self.consumo)
        datos.append(self.torreChoice.GetSelection())
        datos.append(self.potenciaElectricaNominal)
        datos.append('')
        datos.append(self.EstimacionConsumoChoice.GetSelection())
        datos.append(self.numeroHorasDemanda)
        datos.append(self.c1)
        datos.append(self.c2)
        datos.append(self.c3)
        datos.append(self.c4)
        datosConcretos = []
        for i in range(10):
            datosConcretos.append(self.potenciaFcp[i])

        datos.append(datosConcretos)
        datos.append(self.subgrupoChoice.GetStringSelection())
        return datos

    def cargarDatos(self, datos):
        self.nombreInstalacion= datos[0]
        self.consumo= datos[2]
        self.torreChoice.SetSelection(datos[3])
        self.OnTorreChoice(None)
        self.potenciaElectricaNominal= datos[4]
        self.EstimacionConsumoChoice.SetSelection(datos[6])
        self.OnEstimacionConsumoChoice(None)
        self.numeroHorasDemanda= datos[7]
        self.c1 = datos[8]
        self.c2 = datos[9]
        self.c3 = datos[10]
        self.c4 = datos[11]
        datosConcretos = datos[12]
        for i in range(10):
            self.potenciaFcp[i] = datosConcretos[i]

        self.subgrupoChoice.SetStringSelection(datos[-1])
        return

    def OnNumeroHorasHelpButton(self, event):
        zona = self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()
        perfilUso = self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
        servicio = 'Refrigeración'
        if zona == '':
            print('Debe indicar la localización del edificio en el panel de datos generales', 'Estimación del número de horas de funcionamiento')
        else:
            self.parent.parent.parent.calculoCalificacion()
            ayuda = ayudaNumeroHoras.Dialog1(self, zona, perfilUso, servicio)
            ayuda.ShowModal()
            if ayuda.dev != []:
                self.numeroHorasDemanda= str(ayuda.dev[0])