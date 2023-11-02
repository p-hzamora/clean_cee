# Embedded file name: Instalaciones\panelCalefaccion.pyc
from Calculos.funcionesCalculo import rendCombustionDefecto, betaCombDefecto, diccCOPNominalDefecto, rendNominalJoule
from Calculos.listadosWeb import listadoCombustiblesEquiposElectricos
from Instalaciones.comprobarCampos import Comprueba, Comprueba2
from Instalaciones.funcionCalculoRendimientoEstacional import calculoRendimientoMedioEstacional
from miChoice import MiChoice
import Calculos.listadosWeb as listadosWeb
import Instalaciones.PaneltiposCaldera as PaneltiposCaldera
import Instalaciones.ayudaCargaParcialCalefaccion as ayudaCargaParcialCalefaccion
import Instalaciones.dialogoTemperaturas as dialogoTemperaturas
import Instalaciones.equipos as equipos
import Instalaciones.formulaCurvaRendimiento as formulaCurvaRendimiento
import Instalaciones.perfilesTerciario as perfilesTerciario
import Instalaciones.tablasValoresInstalaciones as tablasValoresInstalaciones
import logging

class Panel1(wx.Panel):

    def _init_ctrls(self, prnt, id, posi, siz, styles, named):
        self.nombreInstalacion = 'S\xf3lo calefacci\xf3n'
        self.subgrupoChoice = MiChoice(choices=[])
        self.generadorChoice = MiChoice(choices=listadosWeb.listadoInstalaciones)
        self.generadorChoice.SetSelection(0)
        self.combustibleChoice = MiChoice(choices=listadosWeb.listadoCombustibles)
        self.combustibleChoice.SetSelection(0)
        self.coberturaMetros = u''
        self.coberturaPorcentaje = u''
        self.rendimientoChoice = MiChoice(choices=self.parent.listadoOpcionesInstalaciones)
        self.rendimientoChoice.SetSelection(1)
        self.potenciaNominal = '24.0'
        self.cargaMedia= '%s' % betaCombDefecto
        self.rendimientoCombustion= '%s' % rendCombustionDefecto
        self.aislanteCaldera = MiChoice(choices=listadosWeb.listadoOpcionesAislamientoCaldera)
        self.aislanteCaldera.SetSelection(2)
        self.definirAntiguedadChoice = MiChoice(choices=listadosWeb.listadoOpcionesAntiguedad)
        self.definirAntiguedadChoice.SetSelection(2)
        self.rendimientoNominal = '100.0'
        self.rendimientoGlobal.Enable(False)
        # self.VariosGeneradoresCheck\xbfExisten varios generadores escalonados?
        self.VariosGeneradoresCheck.Enable(True)
        self.VariosGeneradoresCheck= False
        self.FraccionPotencia = u'1.0'
        self.fraccionPotenciaEntrada = u'0.0'
        self.ddaCubiertaBDC = u''
        self.ddaCubiertaBDC.Enable(False)
        self.potNominal = u''
        self.rendNominalPG = u''
        self.temperaturaAmbienteInt = u'20.0'
        self.factorCargaMinimo = u'0.15'
        self.factorCargaMaximo = u'1.0'

    def OnsubgrupoChoice(self, event):
        self.coberturaPorcentaje= '100'

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

    def OnNombreInstalacion(self, event):
        if self.nombreInstalacion == 'S\xf3lo calefacci\xf3n':
        else:

    def OnPotenciaNominal(self, event):
        if self.potenciaNominal == '24.0':
        else:
        self.obtenerRendimientoEstacional(None)
        return

    def OndefinirTemperaturasBoton(self, event):
        dlg = dialogoTemperaturas.create(self, self.temperaturas)
        dlg.ShowModal()
        if dlg.dev != False:
            self.temperaturas[0] = float(dlg.dev[0])
            self.temperaturas[1] = float(dlg.dev[1])
            self.temperaturas[2] = float(dlg.dev[2])
        self.obtenerRendimientoEstacional(None)
        return

    def OndefinirCurvaBoton(self, event):
        if self.generadorChoice.GetStringSelection() == u'Caldera Est\xe1ndar':
            formula = 'Eff =  A0 + A1*fcp + A2*fcp\xb2 + A3*fcp\xb3'
            campos = ['A0',
             'A1',
             'A2',
             'A3']
            dlg = formulaCurvaRendimiento.create(self, formula, campos, self.curvaRendimiento)
            dlg.ShowModal()
        elif self.generadorChoice.GetStringSelection() == u'Caldera Condensaci\xf3n':
            formula = 'Eff =  A0 + A1*fcp + A2*fcp\xb2 + A3*Tw + A4*Tw\xb2 + A5*fcp*Tw'
            campos = ['A0',
             'A1',
             'A2',
             'A3',
             'A4',
             'A5']
            dlg = formulaCurvaRendimiento.create(self, formula, campos, self.curvaRendimiento)
            dlg.ShowModal()
        elif self.generadorChoice.GetStringSelection() == u'Caldera Baja Temperatura':
            formula = 'Eff =  A0 + A1*fcp + A2*fcp\xb2 + A3*Tw + A4*Tw\xb2 + A5*fcp*Tw \n      + A6*fcp\xb3 + A7*Tw\xb3 + A8*fcp\xb2*Tw + A9*fcp*Tw\xb2'
            campos = ['A0',
             'A1',
             'A2',
             'A3',
             'A4',
             'A5',
             'A6',
             'A7',
             'A8',
             'A9']
            dlg = formulaCurvaRendimiento.create(self, formula, campos, self.curvaRendimiento)
            dlg.ShowModal()
        elif self.generadorChoice.GetStringSelection() == u'Bomba de Calor':
            formula = 'conCal_FCP =  A0 + A1*fcp + A2*fcp\xb2 + A3*fcp\xb3   \nconCal_Tint_Thext = B0 + B1*Tint + B2*Tint\xb2 + B3*Thext + B4*Thext\xb2 + B5*Tint*Thext'
            campos = ['A0',
             'A1',
             'A2',
             'A3',
             'B0',
             'B1',
             'B2',
             'B3',
             'B4',
             'B5']
            dlg = formulaCurvaRendimiento.create(self, formula, campos, self.curvaRendimiento)
            dlg.ShowModal()
        elif self.generadorChoice.GetStringSelection() == u'Bomba de Calor - Caudal Ref. Variable':
            formula = 'conCal_FCP =  A0 + A1*fcp + A2*fcp\xb2 + A3*fcp\xb3  \nconCal_Tint_Thext = B0 + B1*Tint + B2*Tint\xb2 + B3*Thext + B4*Thext\xb2 + B5*Tint*Thext'
            campos = ['A0',
             'A1',
             'A2',
             'A3',
             'B0',
             'B1',
             'B2',
             'B3',
             'B4',
             'B5']
            dlg = formulaCurvaRendimiento.create(self, formula, campos, self.curvaRendimiento)
            dlg.ShowModal()
        elif self.generadorChoice.GetStringSelection() == u'Efecto Joule':
            pass
        elif self.generadorChoice.GetStringSelection() == u'Equipo de Rendimiento Constante':
            pass
        if dlg.dev != False:
            self.curvaRendimiento = []
            for i in dlg.dev:
                self.curvaRendimiento.append(i)

        self.obtenerRendimientoEstacional(None)
        return

    def OnVariosGeneradoresCheck(self, event):
        self.obtenerRendimientoEstacional(event)
        if self.combustibleChoice.GetStringSelection() == u'Electricidad' and self.generadorChoice.GetStringSelection() != u'Equipo de Rendimiento Constante' and u'Estimado seg\xfan Instalaci\xf3n' in self.rendimientoChoice.GetStringSelection():
            if self.VariosGeneradoresCheck == True:
            else:
        else:

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
        self.temperaturas = [20, 85, 60]
        self.curvaRendimiento = ['0.89305015622789352',
         '0.45702553179343713',
         '-0.60789791967901996',
         '0.23878599898375633']
        self._init_ctrls(parent, id, pos, size, style, name)
        self.tipoSistema = 'calefaccion'
        self.listaErrores = u''
        self.subgrupoChoice.SetItems(self.cargarRaices())
        self.OnrendimientoChoice(None)
        self.rendimientoEstacionalCal = ''
        self.OnVariosGeneradoresCheck(None)
        self.booleano = True
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
        kwargsConocido = {'rendEstACS': '',
         'rendEstCal': self.rendimietoMedio,
         'rendEstRef': ''}
        kwargsJouleEst = {'rendNominal': self.rendimientoNominal}
        fraccionPotencia = self.FraccionPotencia.replace(',', '.')
        fraccionPotenciaEntrada = self.fraccionPotenciaEntrada.replace(',', '.')
        kwargsBdCEst = {'rendNominalACS': '',
         'rendNominalCal': self.rendimientoNominal,
         'rendNominalRef': '',
         'variosGeneradoresCheck': self.VariosGeneradoresCheck,
         'fraccionPotencia': fraccionPotencia,
         'fraccionPotenciaEntrada': fraccionPotenciaEntrada}
        kwargsCalderaSgCurva = {'curvaRendimiento': self.curvaRendimiento,
         'rendNominalPG': self.rendNominalPG,
         'factorCargaMinimo': self.factorCargaMinimo,
         'factorCargaMaximo': self.factorCargaMaximo,
         'potNominal': self.potNominal,
         'temperaturas': self.temperaturas}
        kwargsBdCSgCurva = {'curvaRendimiento': self.curvaRendimiento,
         'rendNominalPG': self.rendNominalPG,
         'factorCargaMinimo': self.factorCargaMinimo,
         'factorCargaMaximo': self.factorCargaMaximo,
         'potNominal': self.potNominal,
         'temperaturaAmbienteInt': self.temperaturaAmbienteInt}
        kwargs = {}
        kwargs.update(kwargsCalderaEst)
        kwargs.update(kwargsConocido)
        kwargs.update(kwargsJouleEst)
        kwargs.update(kwargsBdCEst)
        kwargs.update(kwargsCalderaSgCurva)
        kwargs.update(kwargsBdCSgCurva)
        zonaHE1 = self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()
        programa = self.parent.parent.parent.programa
        tipoEdificio = self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
        modoDefinicion = self.rendimientoChoice.GetStringSelection()
        tipoEquipo = self.generadorChoice.GetStringSelection()
        combustible = self.combustibleChoice.GetStringSelection()
        resultado = calculoRendimientoMedioEstacional(zonaHE1=zonaHE1, programa=programa, tipoEdificio=tipoEdificio, tipoInstalacion=self.tipoSistema, modoDefinicion=modoDefinicion, tipoEquipo=tipoEquipo, combustible=combustible, **kwargs)
        if modoDefinicion == u'Estimado seg\xfan Instalaci\xf3n' and tipoEquipo not in (u'Caldera Est\xe1ndar', u'Caldera Condensaci\xf3n', u'Caldera Baja Temperatura', u'Efecto Joule', u'Equipo de Rendimiento Constante'):
            self.rendimientoEstacionalCal, fraccionEnergia = resultado
            if self.VariosGeneradoresCheck == True:
                self.ddaCubiertaBDC= str(round(sum(fraccionEnergia * 100.0, 1)))
        else:
            self.rendimientoEstacionalCal = resultado
        self.escribirRendimientoGlobal()

    def escribirRendimientoGlobal(self):
        self.rendimientoGlobal= str(self.rendimientoEstacionalCal)

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
        try:
            if float(self.generadorChoice.GetSelection()) == 0.0:
                self.curvaRendimiento = ['0.89305015622789352',
                 '0.45702553179343713',
                 '-0.60789791967901996',
                 '0.23878599898375633']
                self.rendNominalPGText.SetLabel('Rendimiento nominal a plena carga')
                self.rendNominalPGText.SetSize(wx.Size(130, 27))
                self.rendNominalPGText.SetPosition(wx.Point(15, 176))
                self.combustibleChoice.SetSelection(0)
            elif float(self.generadorChoice.GetSelection()) == 1.0:
                self.curvaRendimiento = ['1.12',
                 '0.014',
                 '-0.02599',
                 '0',
                 '-1.4e-9',
                 '-0.001536']
                self.rendNominalPGText.SetLabel('Rendimiento nominal a plena carga')
                self.rendNominalPGText.SetSize(wx.Size(130, 27))
                self.rendNominalPGText.SetPosition(wx.Point(15, 176))
                self.combustibleChoice.SetSelection(0)
            elif float(self.generadorChoice.GetSelection()) == 2:
                self.curvaRendimiento = ['1.1117',
                 '0.0786',
                 '-0.40042',
                 '0',
                 '-0.000156783',
                 '0.009384599',
                 '0.234257955',
                 '1.32927E-06',
                 '-0.004446701',
                 '-1.22498E-05']
                self.rendNominalPGText.SetLabel('Rendimiento nominal a plena carga')
                self.rendNominalPGText.SetSize(wx.Size(130, 27))
                self.rendNominalPGText.SetPosition(wx.Point(15, 176))
                self.combustibleChoice.SetSelection(0)
            elif self.generadorChoice.GetStringSelection() == u'Bomba de Calor':
                self.curvaRendimiento = ['0.0856522',
                 '0.938814',
                 '-0.183436',
                 '0.15897',
                 '1.20122',
                 '0',
                 '0',
                 '-0.0400633',
                 '0.0010877',
                 '0']
                self.rendNominalPGText.SetLabel('Rendimiento nominal a plena carga')
                self.rendNominalPGText.SetSize(wx.Size(130, 27))
                self.rendNominalPGText.SetPosition(wx.Point(15, 176))
                self.combustibleChoice.SetSelection(2)
            elif self.generadorChoice.GetStringSelection() == u'Bomba de Calor - Caudal Ref. Variable':
                self.rendNominalPGText.SetLabel('Rendimiento nominal a plena carga')
                self.rendNominalPGText.SetSize(wx.Size(130, 27))
                self.rendNominalPGText.SetPosition(wx.Point(15, 176))
                self.curvaRendimiento = ['0.85',
                 '0.15',
                 '0',
                 '0',
                 '1.20122',
                 '0',
                 '0',
                 '-0.0400633',
                 '0.0010877',
                 '0']
                self.combustibleChoice.SetSelection(2)
            elif self.generadorChoice.GetStringSelection() == u'Efecto Joule':
                self.rendNominalPGText.SetLabel('Rendimiento nominal a plena carga')
                self.rendNominalPGText.SetSize(wx.Size(130, 27))
                self.rendNominalPGText.SetPosition(wx.Point(15, 176))
            elif self.generadorChoice.GetStringSelection() == u'Equipo de Rendimiento Constante':
                self.rendNominalPGText.SetLabel('Rendimiento nominal a plena carga')
                self.rendNominalPGText.SetSize(wx.Size(130, 27))
                self.rendNominalPGText.SetPosition(wx.Point(15, 176))
            self.cargaTipoCombustible()
            self.cargaModoObtencion()
            self.OnrendimientoChoice(None)
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        return

    def cargaModoObtencion(self):
        antes = self.rendimientoChoice.GetStringSelection()
        if u'Equipo de Rendimiento Constante' == self.generadorChoice.GetStringSelection():
            self.rendimientoChoice.SetItems([self.parent.listadoOpcionesInstalaciones[0]])
            self.rendimientoChoice.SetSelection(0)
        elif u'Efecto Joule' in self.generadorChoice.GetStringSelection() or self.generadorChoice.GetStringSelection() in (u'Caldera Est\xe1ndar', u'Caldera Condensaci\xf3n', u'Caldera Baja Temperatura') and self.combustibleChoice.GetStringSelection() == u'Electricidad':
            self.rendimientoChoice.SetItems([self.parent.listadoOpcionesInstalaciones[0], self.parent.listadoOpcionesInstalaciones[1]])
            self.rendimientoChoice.SetSelection(1)
        else:
            self.rendimientoChoice.SetItems(self.parent.listadoOpcionesInstalaciones)
            self.rendimientoChoice.SetStringSelection(antes)

    def cargaTipoCombustible(self):
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
        self.cargaModoObtencion()
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
        elif u'Estimado seg\xfan Instalaci\xf3n' in self.rendimientoChoice.GetStringSelection():
            if 'Caldera' in self.generadorChoice.GetStringSelection() and self.combustibleChoice.GetStringSelection() != u'Electricidad':
            else:
                if self.generadorChoice.GetStringSelection() == u'Efecto Joule' or u'Caldera' in self.generadorChoice.GetStringSelection() and self.combustibleChoice.GetStringSelection() == u'Electricidad':
                    self.VariosGeneradoresCheck= False
                else:
                self.OnVariosGeneradoresCheck(None)
                self.actualizarRendimientoNominalEquiposElectricos()
        else:
            if 'Caldera' in self.generadorChoice.GetStringSelection():
            elif 'Bomba' in self.generadorChoice.GetStringSelection():
        self.obtenerRendimientoEstacional(None)
        return

    def comprobarDatos(self):
        dato = self.potNominal
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.potNominal= dato
        dato = self.rendNominalPG
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.rendNominalPG= dato
        dato = self.factorCargaMinimo
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.factorCargaMinimo= dato
        dato = self.factorCargaMaximo
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.factorCargaMaximo= dato
        dato = self.coberturaMetros
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.coberturaMetros= dato
        dato = self.coberturaPorcentaje
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.coberturaPorcentaje= dato
        dato = self.rendimietoMedio
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.rendimietoMedio= dato
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
        dato = self.FraccionPotencia
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.FraccionPotencia= dato
        dato = self.fraccionPotenciaEntrada
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.fraccionPotenciaEntrada= dato
        dato = self.ddaCubiertaBDC
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.ddaCubiertaBDC= dato
        dato = self.temperaturaAmbienteInt
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.temperaturaAmbienteInt= dato
        self.listaErrores = u''
        self.listaErrores += Comprueba(self.nombreInstalacion, 1, self.listaErrores, 'nombre').ErrorDevuelto
        self.listaErrores += Comprueba(self.subgrupoChoice.GetStringSelection(), 0, self.listaErrores, 'zona').ErrorDevuelto
        self.listaErrores += Comprueba(self.generadorChoice.GetStringSelection(), 0, self.listaErrores, 'tipo de generador').ErrorDevuelto
        self.listaErrores += Comprueba(self.combustibleChoice.GetStringSelection(), 0, self.listaErrores, 'tipo de combustible').ErrorDevuelto
        self.listaErrores += Comprueba(self.rendimientoChoice.GetStringSelection(), 0, self.listaErrores, 'definir rendimiento').ErrorDevuelto
        if self.parent.parent.parent.panelDatosGenerales.superficie == '':
            self.listaErrores += Comprueba2(self.coberturaPorcentaje, 2, self.listaErrores, 'porcentaje de demanda de la zona cubierto', 0, 100).ErrorDevuelto
        else:
            self.listaErrores += Comprueba2(self.coberturaPorcentaje, 2, self.listaErrores, 'porcentaje de demanda de la zona cubierto o m2 cubiertos por el equipo', 0, 100).ErrorDevuelto
        rendi = self.rendimientoChoice.GetStringSelection()
        if 'Conocido' in rendi:
            self.listaErrores += Comprueba(self.rendimietoMedio, 2, self.listaErrores, 'rendimiento medio estacional', 0).ErrorDevuelto
        elif u'Estimado seg\xfan Instalaci\xf3n' in rendi:
            if 'Caldera' in self.generadorChoice.GetStringSelection():
                self.listaErrores += Comprueba(self.aislanteCaldera.GetStringSelection(), 0, self.listaErrores, 'aislamiento de la caldera').ErrorDevuelto
                self.listaErrores += Comprueba(self.rendimientoCombustion, 2, self.listaErrores, 'rendimiento de combusti\xf3n', 0).ErrorDevuelto
                self.listaErrores += Comprueba(self.potenciaNominal, 2, self.listaErrores, 'potencia nominal', 0).ErrorDevuelto
                self.listaErrores += Comprueba(self.cargaMedia, 2, self.listaErrores, 'carga media real \xdfcmb', 0, 1).ErrorDevuelto
                if self.vectorTipoCaldera == []:
                    if self.listaErrores != u'':
                        self.listaErrores += u', '
                    self.listaErrores += 'caracter\xedsticas caldera'
            else:
                self.listaErrores += Comprueba(self.rendimientoNominal, 2, self.listaErrores, 'rendimiento nominal', 0.0).ErrorDevuelto
                if self.VariosGeneradoresCheck == True:
                    errorFraccionPotencia = Comprueba(self.FraccionPotencia, 2, self.listaErrores, 'fracci\xf3n de la potencia que aporta el generador', 0.0, 1.0).ErrorDevuelto
                    self.listaErrores += errorFraccionPotencia
                    errorFraccionEntrada = Comprueba2(self.fraccionPotenciaEntrada, 2, self.listaErrores, 'fracci\xf3n de la potencia a la que entra el generador', 0.0, 1.0).ErrorDevuelto
                    self.listaErrores += errorFraccionEntrada
        else:
            self.listaErrores += Comprueba(self.potNominal, 2, self.listaErrores, 'potencia nominal', 0).ErrorDevuelto
            self.listaErrores += Comprueba(self.rendNominalPG, 2, self.listaErrores, 'rendimiento/COP nominal', 0).ErrorDevuelto
            self.listaErrores += Comprueba2(self.factorCargaMinimo, 2, self.listaErrores, 'factor de carga parcial m\xednimo', 0.0, 1.0).ErrorDevuelto
            if Comprueba2(self.factorCargaMinimo, 2, self.listaErrores, 'factor de carga parcial m\xednimo', 0.0, 1.0).ErrorDevuelto == '':
                self.listaErrores += Comprueba(self.factorCargaMaximo, 2, self.listaErrores, 'factor de carga parcial m\xe1ximo', float(self.factorCargaMinimo), 1.0).ErrorDevuelto
            else:
                self.listaErrores += Comprueba(self.factorCargaMaximo, 2, self.listaErrores, 'factor de carga parcial m\xe1ximo', 0.0, 1.0).ErrorDevuelto
            if 'Bomba' in self.generadorChoice.GetStringSelection():
                self.listaErrores += Comprueba(self.temperaturaAmbienteInt, 2, self.listaErrores, 'temperatura ambiente interior', 0).ErrorDevuelto
        if u'Conocido' not in rendi and self.listaErrores == '':
            if self.rendimientoEstacionalCal != '':
                self.listaErrores += Comprueba(str(self.rendimientoEstacionalCal), 2, self.listaErrores, 'rendimiento medio estacional', 0.0).ErrorDevuelto

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