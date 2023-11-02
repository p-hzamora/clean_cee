# Embedded file name: Instalaciones\panelMixto2.pyc
from Calculos.funcionesCalculo import rendCombustionDefecto, betaCombDefecto, diccCOPNominalDefecto, rendNominalJoule
from Calculos.listadosWeb import listadoCombustiblesEquiposElectricos
from Instalaciones.comprobarCampos import Comprueba, Comprueba2
from Instalaciones.funcionCalculoRendimientoEstacional import calculoRendimientoMedioEstacional
from miChoice import MiChoice
import Calculos.listadosWeb as listadosWeb
import Instalaciones.PaneltiposCaldera as PaneltiposCaldera
import Instalaciones.ayudaCargaParcialCalefaccion as ayudaCargaParcialCalefaccion
import Instalaciones.equipos as equipos
import Instalaciones.tablasValoresInstalaciones as tablasValoresInstalaciones
import math
import logging

class Panel1(wx.Panel):

    def _init_ctrls(self, prnt, id, posi, siz, styles, named):
        self.nombreInstalacion = 'Calefacci\xf3n y ACS'
        self.subgrupoChoice = MiChoice(choices=[])
        self.generadorChoice = MiChoice(choices=listadosWeb.listadoInstalaciones)
        self.generadorChoice.SetSelection(0)
        self.combustibleChoice = MiChoice(choices=listadosWeb.listadoCombustibles)
        self.combustibleChoice.SetSelection(0)
        self.coberturaMetros = u''
        self.coberturaPorcentaje = u''
        self.coberturaMetros2 = u''
        self.coberturaPorcentaje2 = u''
        self.rendimientoChoice = MiChoice(choices=self.parent.listadoOpcionesInstalacionesMixtos)
        self.rendimientoChoice.SetSelection(1)
        self.potenciaNominal = u'24.0'
        self.cargaMedia= '%s' % betaCombDefecto
        self.rendimientoCombustion= '%s' % rendCombustionDefecto
        self.aislanteCaldera = MiChoice(choices=listadosWeb.listadoOpcionesAislamientoCaldera)
        self.aislanteCaldera.SetSelection(2)
        self.definirAntiguedadChoice = MiChoice(choices=listadosWeb.listadoOpcionesAntiguedad)
        self.definirAntiguedadChoice.SetSelection(2)
        self.rendimientoNominal = '100.0'
        self.rendimientoGlobal.Enable(False)
        self.rendimientoGlobal2.Enable(False)
        # self.acumulacionCheckCon Acumulaci\xf3n
        self.acumulacionCheck= False
        self.valorUAChoice = MiChoice(choices=listadosWeb.listadoOpcionesAcumulacion)
        self.valorUAChoice.SetSelection(2)
        self.volumen = u''
        self.multiplicador = u''
        self.multiplicador= '1'
        self.aislamientoAcumulacionChoice = MiChoice(choices=listadosWeb.listadoOpcionesAislamientoAcumulacion)
        self.aislamientoAcumulacionChoice.SetSelection(0)
        self.espesorAislamiento = u''
        self.UAvalor = u''
        self.temperaturaAlta = u''
        self.temperaturaAlta= '80'
        self.temperaturaBaja = u''
        self.temperaturaBaja= '60'

    def OnsubgrupoChoice(self, event):
        self.coberturaPorcentaje= '100'
        self.coberturaPorcentaje2= '100'

    def OnNombreInstalacion(self, event):
        if self.nombreInstalacion == 'Calefacci\xf3n y ACS':
        else:

    def OnCobertura(self, event):
        if self.booleano == True:
            self.booleano = False
            if self.subgrupoChoice.GetStringSelection() == u'Edificio Objeto':
                try:
                    superficieTotal = float(self.parent.parent.parent.panelDatosGenerales.superficie)
                    superficieActual = float(self.coberturaMetros)
                    porcentaje = round(superficieActual * 100 / superficieTotal, 2)
                    self.coberturaPorcentaje= str(porcentaje)
                except (ValueError, TypeError):
                    self.coberturaPorcentaje= ''
                except ZeroDivisionError:
                    self.coberturaPorcentaje= ''

            else:
                for i in self.parent.parent.subgrupos:
                    if i.nombre == self.subgrupoChoice.GetStringSelection():
                        mTotales = float(i.superficie)
                        break

                try:
                    mActuales = float(self.coberturaMetros)
                    porcentaje = round(mActuales * 100 / mTotales, 2)
                    self.coberturaPorcentaje= str(porcentaje)
                except (ValueError, TypeError):
                    self.coberturaPorcentaje= ''
                except ZeroDivisionError:
                    self.coberturaPorcentaje= ''

            self.booleano = True

    def OnCoberturaPorcentaje(self, event):
        if self.booleano == True:
            self.booleano = False
            if self.subgrupoChoice.GetStringSelection() == u'Edificio Objeto':
                try:
                    superficieTotal = float(self.parent.parent.parent.panelDatosGenerales.superficie)
                    porcentajeActual = float(self.coberturaPorcentaje)
                    mAcuales = round(porcentajeActual * superficieTotal / 100.0, 2)
                    self.coberturaMetros= str(mAcuales)
                except (ValueError, TypeError):
                    self.coberturaMetros= ''
                except ZeroDivisionError:
                    self.coberturaMetros= ''

            else:
                for i in self.parent.parent.subgrupos:
                    if i.nombre == self.subgrupoChoice.GetStringSelection():
                        mTotales = float(i.superficie)
                        break

                try:
                    porcentaje = float(self.coberturaPorcentaje)
                    mAcuales = round(porcentaje * mTotales / 100.0, 2)
                    self.coberturaMetros= str(mAcuales)
                except (ValueError, TypeError):
                    self.coberturaMetros= ''
                except ZeroDivisionError:
                    self.coberturaMetros= ''

            self.booleano = True

    def OnCobertura2(self, event):
        if self.booleano == True:
            self.booleano = False
            if self.subgrupoChoice.GetStringSelection() == u'Edificio Objeto':
                try:
                    superficieTotal = float(self.parent.parent.parent.panelDatosGenerales.superficie)
                    superficieActual = float(self.coberturaMetros2)
                    porcentaje = round(superficieActual * 100 / superficieTotal, 2)
                    self.coberturaPorcentaje2= str(porcentaje)
                except (ValueError, TypeError):
                    self.coberturaPorcentaje2= ''
                except ZeroDivisionError:
                    self.coberturaPorcentaje2= ''

            else:
                for i in self.parent.parent.subgrupos:
                    if i.nombre == self.subgrupoChoice.GetStringSelection():
                        mTotales = float(i.superficie)
                        break

                try:
                    mActuales = float(self.coberturaMetros2)
                    porcentaje = round(mActuales * 100 / mTotales, 2)
                    self.coberturaPorcentaje2= str(porcentaje)
                except (ValueError, TypeError):
                    self.coberturaPorcentaje2= ''
                except ZeroDivisionError:
                    self.coberturaPorcentaje2= ''

            self.booleano = True

    def OnCoberturaPorcentaje2(self, event):
        if self.booleano == True:
            self.booleano = False
            if self.subgrupoChoice.GetStringSelection() == u'Edificio Objeto':
                try:
                    superficieTotal = float(self.parent.parent.parent.panelDatosGenerales.superficie)
                    porcentajeActual = float(self.coberturaPorcentaje2)
                    mAcuales = round(porcentajeActual * superficieTotal / 100.0, 2)
                    self.coberturaMetros2= str(mAcuales)
                except (ValueError, TypeError):
                    self.coberturaMetros2= ''
                except ZeroDivisionError:
                    self.coberturaMetros2= ''

            else:
                for i in self.parent.parent.subgrupos:
                    if i.nombre == self.subgrupoChoice.GetStringSelection():
                        mTotales = float(i.superficie)
                        break

                try:
                    porcentaje = float(self.coberturaPorcentaje2)
                    mAcuales = round(porcentaje * mTotales / 100.0, 2)
                    self.coberturaMetros2= str(mAcuales)
                except (ValueError, TypeError):
                    self.coberturaMetros2= ''
                except ZeroDivisionError:
                    self.coberturaMetros2= ''

            self.booleano = True

    def OnPotenciaNominal(self, event):
        if self.potenciaNominal == '24.0':
        else:
        self.obtenerRendimientoEstacional(None)
        return

    def OndefinirCalderaBoton(self, event):
        if self.vectorTipoCaldera != []:
            datos = PaneltiposCaldera.Dialog1(self, self.vectorTipoCaldera)
        else:
            datos = PaneltiposCaldera.Dialog1(self, [True,
             False,
             False,
             False,
             False,
             True,
             False])
        datos.ShowModal()
        if datos.resultados != []:
            self.vectorTipoCaldera = []
            for i in datos.resultados:
                self.vectorTipoCaldera.append(i)

        self.obtenerRendimientoEstacional(None)
        return

    def __init__(self, parent, id, pos, size, style, name, real_parent = None):
        if real_parent == None:
            self.parent = parent
        else:
            self.parent = real_parent
        self.booleano = True
        self.rendimientoEstacionalACS = ''
        self.rendimientoEstacionalCal = ''
        self._init_ctrls(parent, id, pos, size, style, name)
        self.tipoSistema = 'mixto2'
        self.listaErrores = u''
        self.subgrupoChoice.SetItems(self.cargarRaices())
        self.OnrendimientoChoice(None)
        self.elegirRaiz()
        self.vectorTipoCaldera = [False,
         False,
         True,
         False,
         False,
         True,
         False]
        self.arrayAyudaCalefaccion = [1.0, 0.0]
        self.obtenerRendimientoEstacional(None)
        return

    def obtenerRendimientoEstacional(self, event):
        kwargsCalderaEst = {'aislanteCaldera': self.aislanteCaldera.GetStringSelection(),
         'rendCombCaldera': self.rendimientoCombustion,
         'potenciaCaldera': self.potenciaNominal,
         'cargaMediaCaldera': self.cargaMedia}
        kwargsConocido = {'rendEstACS': self.rendimietoMedio,
         'rendEstCal': self.rendimietoMedio2,
         'rendEstRef': ''}
        kwargsJouleEst = {'rendNominal': self.rendimientoNominal}
        kwargsBdCEst = {'rendNominalACS': self.rendimientoNominal,
         'rendNominalCal': self.rendimientoNominal,
         'rendNominalRef': '',
         'variosGeneradoresCheck': False,
         'fraccionPotencia': '',
         'fraccionPotenciaEntrada': ''}
        kwargs = {}
        kwargs.update(kwargsCalderaEst)
        kwargs.update(kwargsConocido)
        kwargs.update(kwargsJouleEst)
        kwargs.update(kwargsBdCEst)
        zonaHE1 = self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()
        programa = self.parent.parent.parent.programa
        tipoEdificio = self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
        modoDefinicion = self.rendimientoChoice.GetStringSelection()
        tipoEquipo = self.generadorChoice.GetStringSelection()
        combustible = self.combustibleChoice.GetStringSelection()
        resultado = calculoRendimientoMedioEstacional(zonaHE1=zonaHE1, programa=programa, tipoEdificio=tipoEdificio, tipoInstalacion=self.tipoSistema, modoDefinicion=modoDefinicion, tipoEquipo=tipoEquipo, combustible=combustible, **kwargs)
        if modoDefinicion == u'Estimado seg\xfan Instalaci\xf3n' and tipoEquipo in (u'Caldera Est\xe1ndar', u'Caldera Condensaci\xf3n', u'Caldera Baja Temperatura', u'Efecto Joule'):
            self.rendimientoEstacionalCal = resultado
            self.rendimientoEstacionalACS = resultado
        else:
            self.rendimientoEstacionalACS, self.rendimientoEstacionalCal = resultado
        self.escribirRendimientoGlobal()

    def escribirRendimientoGlobal(self):
        self.rendimientoGlobal= str(self.rendimientoEstacionalACS)
        self.rendimientoGlobal2= str(self.rendimientoEstacionalCal)

    def cambioCargaMedia(self, event):
        try:
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        self.obtenerRendimientoEstacional(None)
        return

    def elegirRaiz(self):
        sel = self.parent.arbolInstalaciones.GetSelection()
        try:
            self.subgrupoChoice.SetStringSelection(u'Edificio Objeto')
            raiz = self.parent.arbolInstalaciones.GetRootItem()
            while sel != raiz:
                for i in range(len(self.parent.parent.subgrupos)):
                    if self.parent.arbolInstalaciones.GetItemText(sel) == '%s' % self.parent.parent.subgrupos[i].nombre:
                        self.subgrupoChoice.SetStringSelection(self.parent.arbolInstalaciones.GetItemText(sel))
                        self.OnsubgrupoChoice(None)
                        return

                sel = self.parent.arbolInstalaciones.GetItemParent(sel)

        except:
            logging.info(u'Excepcion en: %s' % __name__)
            self.subgrupoChoice.SetStringSelection(u'Edificio Objeto')

        self.OnsubgrupoChoice(None)
        return

    def cargarRaices(self):
        raices = []
        raices.append((u'Edificio Objeto', 'Edificio Objeto'))
        for i in range(len(self.parent.parent.subgrupos)):
            if self.parent.parent.subgrupos[i].nombre != u'Edificio Objeto':
                raices.append((self.parent.parent.subgrupos[i].nombre, self.parent.parent.subgrupos[i].nombre))

        return raices

    def OngeneradorChoice(self, event):
        antes = self.rendimientoChoice.GetStringSelection()
        if u'Equipo de Rendimiento Constante' == self.generadorChoice.GetStringSelection():
            self.rendimientoChoice.SetItems([self.parent.listadoOpcionesInstalacionesMixtos[0]])
            self.rendimientoChoice.SetSelection(0)
        else:
            self.rendimientoChoice.SetItems(self.parent.listadoOpcionesInstalacionesMixtos)
            self.rendimientoChoice.SetStringSelection(antes)
        if u'Efecto Joule' in self.generadorChoice.GetStringSelection():
            self.combustibleChoice.SetItems(listadoCombustiblesEquiposElectricos)
            self.combustibleChoice.SetSelection(0)
        else:
            antes = self.combustibleChoice.GetSelection()
            self.combustibleChoice.SetItems(listadosWeb.listadoCombustibles)
            if u'Bomba' in self.generadorChoice.GetStringSelection():
                self.combustibleChoice.SetStringSelection(u'Electricidad')
            else:
                self.combustibleChoice.SetSelection(antes)
        self.OnrendimientoChoice(None)
        return

    def OnTemperaturaAlta(self, event):
        try:
        except:
            logging.info(u'Excepcion en: %s' % __name__)

    def OnTemperaturaBaja(self, event):
        try:
        except:
            logging.info(u'Excepcion en: %s' % __name__)

    def actualizarRendimientoNominalEquiposElectricos(self):
        try:
            float(self.rendimientoNominal)
            valorValido = True
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            valorValido = False

        listadoValoresStr = [ str(x) for x in diccCOPNominalDefecto.values() ]
        if self.rendimientoNominal in listadoValoresStr or self.rendimientoNominal == str(rendNominalJoule) or valorValido == False:
            if u'Bomba' in self.generadorChoice.GetStringSelection():
                rendNominalDefecto = diccCOPNominalDefecto[self.definirAntiguedadChoice.GetSelection()]
            else:
                rendNominalDefecto = rendNominalJoule
            self.rendimientoNominal= '%s' % rendNominalDefecto

    def OnCombustibleChoice(self, event):
        self.OnrendimientoChoice(None)
        self.obtenerRendimientoEstacional(None)
        return

    def OnAntiguedadChoice(self, event):
        self.actualizarRendimientoNominalEquiposElectricos()
        self.obtenerRendimientoEstacional(None)
        return

    def OnRendimientoCombustion(self, event):
        try:
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        self.obtenerRendimientoEstacional(None)
        return

    def OnRendimientoNominal(self, event):
        try:
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        self.obtenerRendimientoEstacional(None)
        return

    def OnrendimientoChoice(self, event):
        if 'Conocido' in self.rendimientoChoice.GetStringSelection():
            self.ACSText.SetPosition(wx.Point(15, 180))
            self.calefaccionText.SetPosition(wx.Point(15, 205))
        else:
            if 'Caldera' in self.generadorChoice.GetStringSelection() and self.combustibleChoice.GetStringSelection() != u'Electricidad':
                self.rendimientoGlobalText.SetPosition(wx.Point(435, 130))
                self.rendimientoGlobal.SetPosition(wx.Point(617, 128))
                self.rendimientoGlobalUnidadesText.SetPosition(wx.Point(682, 130))
                self.rendimientoGlobalText.SetLabel(u'Rendimiento medio estacional\n        (ACS y Calefacci\xf3n)')
            else:
                if self.generadorChoice.GetStringSelection() == u'Efecto Joule' or u'Caldera' in self.generadorChoice.GetStringSelection() and self.combustibleChoice.GetStringSelection() == u'Electricidad':
                else:
                self.ACSText.SetPosition(wx.Point(350, 180))
                self.calefaccionText.SetPosition(wx.Point(350, 205))
                self.rendimientoGlobalText.SetPosition(wx.Point(435, 180))
                self.rendimientoGlobal.SetPosition(wx.Point(617, 178))
                self.rendimientoGlobalUnidadesText.SetPosition(wx.Point(680, 180))
                self.rendimientoGlobalText.SetLabel(u'Rendimiento medio estacional')
                self.actualizarRendimientoNominalEquiposElectricos()
        self.obtenerRendimientoEstacional(None)
        return

    def OnAcumulacionCheck(self, event):
        if self.acumulacionCheck == True:
            self.OnvalorUAChoice(None)
        else:
        self.OnCalcularValorUAAcumulacion(None)
        return

    def OnvalorUAChoice(self, event):
        if 'Conocido' in self.valorUAChoice.GetStringSelection():
            if self.acumulacionCheck == True:
                self.UAText.SetForegroundColour('black')
                self.UAText.SetLabel('UA')
                self.UAvalor.Enable(True)
                self.UAUnidadesText.SetForegroundColour('black')
                self.UAUnidadesText.SetLabel('W/K')
        elif 'Estimado' in self.valorUAChoice.GetStringSelection():
            if self.acumulacionCheck == True:
                self.UAText.SetLabel('UA')
                self.UAvalor.Enable(False)
                self.UAUnidadesText.SetLabel('W/K')
        elif self.acumulacionCheck == True:
            self.UAText.SetLabel('UA')
            self.UAvalor.Enable(False)
            self.UAUnidadesText.SetLabel('W/K')
        self.OnCalcularValorUAAcumulacion(None)
        return

    def OnCalcularValorUAAcumulacion(self, event):
        UA = ''
        try:
            if 'Conocido' in self.valorUAChoice.GetStringSelection():
                UA = self.UAvalor
            else:
                volumen = float(self.volumen) / 1000.0
                r = 0.5
                h = volumen / (math.pi * r ** 2)
                multiplicador = float(self.multiplicador)
                Area = (2 * math.pi * r ** 2 + 2 * math.pi * r * h) * multiplicador
                if self.valorUAChoice.GetStringSelection() == u'Por defecto':
                    Rtotal = 0.1 + 0.01 / 0.028
                    UA = 1 / Rtotal * Area
                else:
                    espesor = float(self.espesorAislamiento)
                    aislamiento = self.aislamientoAcumulacionChoice.GetSelection()
                    if aislamiento == 0:
                        conductividad = 0.02
                    elif aislamiento == 1:
                        conductividad = 0.024
                    elif aislamiento == 2:
                        conductividad = 0.024
                    elif aislamiento == 3:
                        conductividad = 0.034
                    elif aislamiento == 4:
                        conductividad = 0.035
                    elif aislamiento == 5:
                        conductividad = 0.036
                    elif aislamiento == 6:
                        conductividad = 0.037
                    elif aislamiento == 7:
                        conductividad = 0.038
                    elif aislamiento == 8:
                        conductividad = 0.042
                    else:
                        conductividad = 0.054
                    UA = conductividad / espesor * Area
            if UA < 0.0:
                UA = ''
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        if UA != '':
            self.UAvalor= str(round(float(UA, 1)))
        else:
            self.UAvalor= UA

    def comprobarDatos(self):
        dato = self.coberturaMetros
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.coberturaMetros= dato
        dato = self.coberturaPorcentaje
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.coberturaPorcentaje= dato
        dato = self.coberturaMetros2
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.coberturaMetros2= dato
        dato = self.coberturaPorcentaje2
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.coberturaPorcentaje2= dato
        dato = self.rendimietoMedio
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.rendimietoMedio= dato
        dato = self.rendimietoMedio2
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.rendimietoMedio2= dato
        dato = self.rendimientoCombustion
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.rendimientoCombustion= dato
        dato = self.potenciaNominal
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.potenciaNominal= dato
        dato = self.cargaMedia
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.cargaMedia= dato
        dato = self.rendimientoNominal
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.rendimientoNominal= dato
        dato = self.UAvalor
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.UAvalor= dato
        dato = self.espesorAislamiento
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.espesorAislamiento= dato
        dato = self.volumen
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.volumen= dato
        dato = self.multiplicador
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.multiplicador= dato
        dato = self.temperaturaAlta
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.temperaturaAlta= dato
        dato = self.temperaturaBaja
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.temperaturaBaja= dato
        dato = self.UAvalor
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.UAvalor= dato
        self.listaErrores = u''
        self.listaErrores += Comprueba(self.nombreInstalacion, 1, self.listaErrores, 'nombre').ErrorDevuelto
        self.listaErrores += Comprueba(self.subgrupoChoice.GetStringSelection(), 0, self.listaErrores, 'zona').ErrorDevuelto
        self.listaErrores += Comprueba(self.generadorChoice.GetStringSelection(), 0, self.listaErrores, 'tipo de generador').ErrorDevuelto
        self.listaErrores += Comprueba(self.combustibleChoice.GetStringSelection(), 0, self.listaErrores, 'tipo de combustible').ErrorDevuelto
        self.listaErrores += Comprueba(self.rendimientoChoice.GetStringSelection(), 0, self.listaErrores, 'definir rendimiento').ErrorDevuelto
        if self.parent.parent.parent.panelDatosGenerales.superficie == '':
            self.listaErrores += Comprueba2(self.coberturaPorcentaje, 2, self.listaErrores, 'porcentaje de demanda (ACS) de la zona cubierto', 0, 100).ErrorDevuelto
        else:
            self.listaErrores += Comprueba2(self.coberturaPorcentaje, 2, self.listaErrores, 'porcentaje de demanda de la zona cubierto o m2 cubiertos por el equipo (ACS)', 0, 100).ErrorDevuelto
        if self.parent.parent.parent.panelDatosGenerales.superficie == '':
            self.listaErrores += Comprueba2(self.coberturaPorcentaje2, 2, self.listaErrores, 'porcentaje de demanda (calefacci\xf3n) de la zona cubierto', 0, 100).ErrorDevuelto
        else:
            self.listaErrores += Comprueba2(self.coberturaPorcentaje2, 2, self.listaErrores, 'porcentaje de demanda de la zona cubierto o m2 cubiertos por el equipo (calefacci\xf3n)', 0, 100).ErrorDevuelto
        rendi = self.rendimientoChoice.GetStringSelection()
        if 'Conocido' in rendi:
            self.listaErrores += Comprueba(self.rendimietoMedio, 2, self.listaErrores, 'rendimiento medio estacional (ACS)', 0).ErrorDevuelto
            self.listaErrores += Comprueba(self.rendimietoMedio2, 2, self.listaErrores, 'rendimiento medio estacional (calefacci\xf3n)', 0).ErrorDevuelto
        elif 'Estimado' in rendi:
            if 'Caldera' in self.generadorChoice.GetStringSelection() and self.combustibleChoice.GetStringSelection() != u'Electricidad':
                self.listaErrores += Comprueba(self.aislanteCaldera.GetStringSelection(), 0, self.listaErrores, 'aislamiento caldera').ErrorDevuelto
                self.listaErrores += Comprueba(self.rendimientoCombustion, 2, self.listaErrores, 'rendimiento de combusti\xf3n', 0).ErrorDevuelto
                self.listaErrores += Comprueba(self.potenciaNominal, 2, self.listaErrores, 'potencia nominal', 0).ErrorDevuelto
                self.listaErrores += Comprueba(self.cargaMedia, 2, self.listaErrores, 'carga media real \xdfcmb', 0, 1).ErrorDevuelto
                if self.vectorTipoCaldera == []:
                    if self.listaErrores != u'':
                        self.listaErrores += u',  '
                    self.listaErrores += 'caracter\xedsticas Caldera'
            else:
                self.listaErrores += Comprueba(self.rendimientoNominal, 2, self.listaErrores, 'rendimiento nominal', 0).ErrorDevuelto
        if u'Conocido' not in rendi and self.listaErrores == '':
            if self.rendimientoEstacionalACS != '':
                self.listaErrores += Comprueba(str(self.rendimientoEstacionalACS), 2, self.listaErrores, 'rendimiento medio estacional para ACS', 0.0).ErrorDevuelto
            if self.rendimientoEstacionalCal != '':
                self.listaErrores += Comprueba(str(self.rendimientoEstacionalCal), 2, self.listaErrores, 'rendimiento medio estacional para calefacci\xf3n', 0.0).ErrorDevuelto
        if self.acumulacionCheck == True:
            self.listaErrores += Comprueba(self.temperaturaAlta, 2, self.listaErrores, 'T\xaa alta').ErrorDevuelto
            self.listaErrores += Comprueba(self.temperaturaBaja, 2, self.listaErrores, 'T\xaa baja').ErrorDevuelto
            self.listaErrores += Comprueba(self.valorUAChoice.GetStringSelection(), 0, self.listaErrores, 'valor UA').ErrorDevuelto
            valorUA = self.valorUAChoice.GetStringSelection()
            if 'Conocido' in valorUA:
                self.listaErrores += Comprueba(self.UAvalor, 2, self.listaErrores, u'UA', 0).ErrorDevuelto
            else:
                self.listaErrores += Comprueba(self.volumen, 2, self.listaErrores, 'volumen de un dep\xf3sito', 0).ErrorDevuelto
                self.listaErrores += Comprueba(self.multiplicador, 2, self.listaErrores, 'multiplicador', 0).ErrorDevuelto
                if 'Estimado' in valorUA:
                    self.listaErrores += Comprueba(self.espesorAislamiento, 2, self.listaErrores, 'espesor del aislamiento', 0).ErrorDevuelto
            try:
                saltoTermico = float(self.temperaturaAlta) - float(self.temperaturaBaja)
                if saltoTermico <= 0.0:
                    self.listaErrores += '\nla temperatura de consigna alta debe ser mayor que la temperatura de consigna baja'
            except (ValueError, TypeError):
                pass

    def onCargaMediaHelpButton(self, event):
        if self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection() == '' and self.parent.parent.parent.programa != 'Residencial' and self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection() == '':
            print('Debe indicar la localizaci\xf3n del edificio y el perfil de uso en el panel de datos generales', 'Estimaci\xf3n de la carga media estacional')
        elif self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection() == '':
            print('Debe indicar la localizaci\xf3n del edificio en el panel de datos generales', 'Estimaci\xf3n de la carga media estacional')
        elif self.parent.parent.parent.programa != 'Residencial' and self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection() == '':
            print('Debe indicar el perfil de uso del edificio en el panel de datos generales', 'Estimaci\xf3n de la carga media estacional')
        else:
            ayuda = ayudaCargaParcialCalefaccion.Dialog1(self, self.arrayAyudaCalefaccion)
            ayuda.ShowModal()
            if ayuda.dev != []:
                self.cargaMedia= ayuda.dev[1]
                self.arrayAyudaCalefaccion = [ayuda.dev[2], ayuda.dev[3]]