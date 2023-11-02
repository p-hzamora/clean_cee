# Embedded file name: Instalaciones\panelRefrigeracion.pyc
from Calculos.funcionesCalculo import diccEERNominalDefecto
from Instalaciones.comprobarCampos import Comprueba, Comprueba2
from Instalaciones.equipos import ExpansionDirectaAireAireBombaDeCalorModoFrio, ExpansionDirectaAguaAireBombaDeCalorModoFrio, VRVModoFrio, ExpansionDirectaAguaAireBombaDeCalorModoFrioVRV
from Instalaciones.funcionCalculoRendimientoEstacional import calculoRendimientoMedioEstacional
from miChoice import MiChoice
import Calculos.listadosWeb as listadosWeb
import Instalaciones.dialogoTemperaturas as dialogoTemperaturas
import Instalaciones.equipos as equipos
import Instalaciones.formulaCurvaRendimiento as formulaCurvaRendimiento
import Instalaciones.perfilesTerciario as perfilesTerciario
import logging

class Panel1(wx.Panel):

    def _init_ctrls(self, prnt, id, posi, siz, styles, named):
        self.nombreInstalacion = 'S\xf3lo refrigeraci\xf3n'
        self.subgrupoChoice = MiChoice(choices=[])
        self.generadorChoice = MiChoice(choices=listadosWeb.listadoInstalacionesElectrico)
        self.generadorChoice.SetSelection(0)
        self.combustibleChoice = MiChoice(choices=listadosWeb.listadoCombustibles)
        self.combustibleChoice.SetSelection(2)
        self.coberturaMetros = u''
        self.coberturaPorcentaje = u''
        self.rendimientoChoice = MiChoice(choices=self.parent.listadoOpcionesInstalaciones)
        self.rendimientoChoice.SetSelection(1)
        self.rendimientoGlobal.Enable(False)
        self.definirAntiguedadChoice = MiChoice(choices=listadosWeb.listadoOpcionesAntiguedad)
        self.definirAntiguedadChoice.SetSelection(2)
        eerNominalDefecto = diccEERNominalDefecto[self.definirAntiguedadChoice.GetSelection()]
        self.rendimientoNominal = '%s' % eerNominalDefecto
        self.potNominal = u''
        self.rendNominalPG = ''
        self.caracteristicasBDCChoice = MiChoice(choices=listadosWeb.listadoOpcionesBdC)
        self.caracteristicasBDCChoice.SetSelection(0)
        if self.parent.parent.parent.programa == 'GranTerciario':
        self.temperaturaAmbienteInt = u''
        self.factorCargaMinimo = u''
        self.factorCargaMaximo = u''
        # self.VariosGeneradoresCheck\xbfExisten varios generadores escalonados?
        self.VariosGeneradoresCheck.Enable(True)
        self.VariosGeneradoresCheck= False
        self.FraccionPotencia = u'1.0'
        self.fraccionPotenciaEntrada = u'0.0'
        self.ddaCubiertaBDC = u''
        self.ddaCubiertaBDC.Enable(False)

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

    def onCaracteristicasBDC(self, event):
        self.getCurvaRendimientoPorDefecto()
        if self.caracteristicasBDCChoice.GetSelection() == 0 or self.caracteristicasBDCChoice.GetSelection() == 2:
            self.temperaturaAmbienteIntText.SetLabel('Temperatura h\xfameda interior')
        else:
            self.temperaturaAmbienteIntText.SetLabel('Temperatura impulsi\xf3n agua')
        self.obtenerRendimientoEstacional(None)
        return

    def OnNombreInstalacion(self, event):
        if self.nombreInstalacion == 'S\xf3lo refrigeraci\xf3n':
        else:

    def OnPotNominal(self, event):
        self.obtenerRendimientoEstacional(None)
        return

    def actualizarRendimientoNominalEquiposElectricos(self):
        try:
            float(self.rendimientoNominal)
            valorValido = True
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            valorValido = False

        listadoValoresStr = [ str(x) for x in diccEERNominalDefecto.values() ]
        if self.rendimientoNominal in listadoValoresStr or valorValido == False:
            rendNominalDefecto = diccEERNominalDefecto[self.definirAntiguedadChoice.GetSelection()]
            self.rendimientoNominal= '%s' % rendNominalDefecto

    def OnAntiguedadChoice(self, event):
        self.actualizarRendimientoNominalEquiposElectricos()
        self.obtenerRendimientoEstacional(None)
        return

    def OnRendimientoNominal(self, event):
        eerNominalDefecto = diccEERNominalDefecto[self.definirAntiguedadChoice.GetSelection()]
        try:
            if float(self.rendimientoNominal) == eerNominalDefecto:
            else:
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        self.obtenerRendimientoEstacional(None)
        return

    def OnRendNominalPG(self, event):
        self.obtenerRendimientoEstacional(None)
        return

    def OndefinirTemperaturasBoton(self, event):
        dlg = dialogoTemperaturas.create(self, self.temperaturas)
        dlg.ShowModal()
        if dlg.dev != False:
            self.temperaturas[0] = dlg.dev[0]
            self.temperaturas[1] = dlg.dev[1]
            self.temperaturas[2] = dlg.dev[2]

    def OndefinirCurvaBoton(self, event):
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
        self.getCurvaRendimientoPorDefecto()
        if self.generadorChoice.GetStringSelection() == u'Maquina frigor\xedfica':
            if self.caracteristicasBDCChoice.GetStringSelection() == u'Aire-Aire':
                formula = 'conRef_FCP=  A0 + A1*fcp + A2*fcp\xb2 + A3*fcp\xb3  \nconRef_Thint_Text =  B0 + B1*Thint + B2*Thint\xb2 + B3*Text + B4*Text\xb2 + B5*Thint*Text'
            elif self.caracteristicasBDCChoice.GetStringSelection() == u'Aire-Agua':
                formula = 'conRef_FCP=  A0 + A1*fcp + A2*fcp\xb2 + A3*fcp\xb3  \nconRef_Timp,a_Text =  B0 + B1*Timp,a + B2*Timp,a\xb2 + B3*Text + B4*Text\xb2 + B5*Timp,a*Text'
            elif self.caracteristicasBDCChoice.GetStringSelection() == u'Agua-Aire':
                formula = 'conRef_FCP=  A0 + A1*fcp + A2*fcp\xb2 + A3*fcp\xb3  \nconRef_Thint_Tcond =  B0 + B1*Thint + B2*Thint\xb2 + B3*Tcond + B4*Tcond\xb2 + B5*Thint*Tcond'
            elif self.caracteristicasBDCChoice.GetStringSelection() == u'Agua-Agua':
                formula = 'conRef_FCP=  A0 + A1*fcp + A2*fcp\xb2 + A3*fcp\xb3  \nconRef_Timp,a_Tcond =  B0 + B1*Timp,a + B2*Timp,a\xb2 + B3*Tcond + B4*Tcond\xb2 + B5*Timp,a*Tcond'
            dlg = formulaCurvaRendimiento.create(self, formula, campos, self.curvaRendimiento)
            dlg.ShowModal()
        elif self.generadorChoice.GetStringSelection() == u'M\xe1quina frigor\xedfica - Caudal Ref. Variable':
            if self.caracteristicasBDCChoice.GetStringSelection() == u'Aire-Aire':
                formula = 'conRef_FCP=  A0 + A1*fcp + A2*fcp\xb2 + A3*fcp\xb3  \nconRef_Thint_Text =  B0 + B1*Thint + B2*Thint\xb2 + B3*Text + B4*Text\xb2 + B5*Thint*Text'
            elif self.caracteristicasBDCChoice.GetStringSelection() == u'Aire-Agua':
                formula = 'conRef_FCP=  A0 + A1*fcp + A2*fcp\xb2 + A3*fcp\xb3  \nconRef_Timp,a_Text =  B0 + B1*Timp,a + B2*Timp,a\xb2 + B3*Text + B4*Text\xb2 + B5*Timp,a*Text'
            elif self.caracteristicasBDCChoice.GetStringSelection() == u'Agua-Aire':
                formula = 'conRef_FCP=  A0 + A1*fcp + A2*fcp\xb2 + A3*fcp\xb3  \nconRef_Thint_Tcond =  B0 + B1*Thint + B2*Thint\xb2 + B3*Tcond + B4*Tcond\xb2 + B5*Thint*Tcond'
            elif self.caracteristicasBDCChoice.GetStringSelection() == u'Agua-Agua':
                formula = 'conRef_FCP=  A0 + A1*fcp + A2*fcp\xb2 + A3*fcp\xb3  \nconRef_Timp,a_Tcond =  B0 + B1*Timp,a + B2*Timp,a\xb2 + B3*Tcond + B4*Tcond\xb2 + B5*Timp,a*Tcond'
            dlg = formulaCurvaRendimiento.create(self, formula, campos, self.curvaRendimiento)
            dlg.ShowModal()
        if dlg.dev != False:
            self.curvaRendimiento = []
            for i in dlg.dev:
                self.curvaRendimiento.append(i)

        self.obtenerRendimientoEstacional(None)
        return

    def OnVariosGeneradoresCheck(self, event):
        self.obtenerRendimientoEstacional(event)
        if self.generadorChoice.GetStringSelection() in (u'Maquina frigor\xedfica', u'M\xe1quina frigor\xedfica - Caudal Ref. Variable') and 'Estimado' in self.rendimientoChoice.GetStringSelection():
            if self.VariosGeneradoresCheck == True:
            else:
        else:

    def __init__(self, parent, id, pos, size, style, name, real_parent = None):
        if real_parent == None:
            self.parent = parent
        else:
            self.parent = real_parent
        self.temperaturas = [20, 85, 60]
        equipo = ExpansionDirectaAireAireBombaDeCalorModoFrio()
        self.curvaRendimiento = equipo.getCurva()
        self._init_ctrls(parent, id, pos, size, style, name)
        self.tipoSistema = 'refrigeracion'
        self.listaErrores = u''
        self.subgrupoChoice.SetItems(self.cargarRaices())
        self.rendimientoEstacionalRef = ''
        self.OnrendimientoChoice(None)
        self.OnVariosGeneradoresCheck(None)
        self.booleano = True
        self.elegirRaiz()
        self.obtenerRendimientoEstacional(None)
        return

    def obtenerRendimientoEstacional(self, event):
        kwargsConocido = {'rendEstACS': '',
         'rendEstCal': '',
         'rendEstRef': self.rendimietoMedio}
        fraccionPotencia = self.FraccionPotencia.replace(',', '.')
        fraccionPotenciaEntrada = self.fraccionPotenciaEntrada.replace(',', '.')
        kwargsBdCEst = {'rendNominalACS': '',
         'rendNominalCal': '',
         'rendNominalRef': self.rendimientoNominal,
         'variosGeneradoresCheck': self.VariosGeneradoresCheck,
         'fraccionPotencia': fraccionPotencia,
         'fraccionPotenciaEntrada': fraccionPotenciaEntrada,
         'tipoBdC': self.caracteristicasBDCChoice.GetStringSelection()}
        kwargsBdCSgCurva = {'curvaRendimiento': self.curvaRendimiento,
         'rendNominalPG': self.rendNominalPG,
         'factorCargaMinimo': self.factorCargaMinimo,
         'factorCargaMaximo': self.factorCargaMaximo,
         'potNominal': self.potNominal,
         'temperaturaAmbienteInt': self.temperaturaAmbienteInt,
         'tipoBdC': self.caracteristicasBDCChoice.GetStringSelection()}
        kwargs = {}
        kwargs.update(kwargsConocido)
        kwargs.update(kwargsBdCEst)
        kwargs.update(kwargsBdCSgCurva)
        zonaHE1 = self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()
        programa = self.parent.parent.parent.programa
        tipoEdificio = self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
        modoDefinicion = self.rendimientoChoice.GetStringSelection()
        tipoEquipo = self.generadorChoice.GetStringSelection()
        combustible = self.combustibleChoice.GetStringSelection()
        resultado = calculoRendimientoMedioEstacional(zonaHE1=zonaHE1, programa=programa, tipoEdificio=tipoEdificio, tipoInstalacion=self.tipoSistema, modoDefinicion=modoDefinicion, tipoEquipo=tipoEquipo, combustible=combustible, **kwargs)
        if modoDefinicion == u'Estimado seg\xfan Instalaci\xf3n':
            self.rendimientoEstacionalRef, fraccionEnergia = resultado
            if self.VariosGeneradoresCheck == True:
                self.ddaCubiertaBDC= str(round(sum(fraccionEnergia * 100.0, 1)))
        else:
            self.rendimientoEstacionalRef = resultado
        self.escribirRendimientoGlobal()

    def escribirRendimientoGlobal(self):
        self.rendimientoGlobal= str(self.rendimientoEstacionalRef)

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
        self.getCurvaRendimientoPorDefecto()
        antes = self.rendimientoChoice.GetStringSelection()
        if u'Equipo de Rendimiento Constante' == self.generadorChoice.GetStringSelection():
            self.rendimientoChoice.SetItems([self.parent.listadoOpcionesInstalaciones[0]])
            self.rendimientoChoice.SetSelection(0)
        else:
            self.rendimientoChoice.SetItems(self.parent.listadoOpcionesInstalaciones)
            self.rendimientoChoice.SetStringSelection(antes)
        self.OnrendimientoChoice(None)
        return

    def getCurvaRendimientoPorDefecto(self):
        if self.rendimientoChoice.GetStringSelection() == u'Estimado seg\xfan curva de rendimiento':
            if self.generadorChoice.GetStringSelection() == u'Maquina frigor\xedfica':
                if self.caracteristicasBDCChoice.GetStringSelection() in (u'Aire-Aire', u'Aire-Agua'):
                    equipo = ExpansionDirectaAireAireBombaDeCalorModoFrio()
                else:
                    equipo = ExpansionDirectaAguaAireBombaDeCalorModoFrio()
                self.curvaRendimiento = equipo.getCurva()
            elif self.generadorChoice.GetStringSelection() == u'M\xe1quina frigor\xedfica - Caudal Ref. Variable':
                if self.caracteristicasBDCChoice.GetStringSelection() in (u'Aire-Aire', u'Aire-Agua'):
                    equipo = VRVModoFrio()
                else:
                    equipo = ExpansionDirectaAguaAireBombaDeCalorModoFrioVRV()
                self.curvaRendimiento = equipo.getCurva()
        else:
            self.curvaRendimiento = []

    def OnrendimientoChoice(self, event):
        if 'Conocido' in self.rendimientoChoice.GetStringSelection():
        elif u'Estimado seg\xfan Instalaci\xf3n' in self.rendimientoChoice.GetStringSelection():
            self.actualizarRendimientoNominalEquiposElectricos()
            if self.parent.parent.parent.programa == 'GranTerciario':
            self.OnVariosGeneradoresCheck(None)
        else:
            if self.parent.parent.parent.programa == 'GranTerciario':
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
            self.listaErrores += Comprueba(self.rendimientoNominal, 2, self.listaErrores, 'rendimiento nominal', 0.09).ErrorDevuelto
            if self.VariosGeneradoresCheck == True:
                self.listaErrores += Comprueba(self.FraccionPotencia, 2, self.listaErrores, 'fracci\xf3n de la potencia total que aporta el generador', 0.0, 1.0).ErrorDevuelto
                self.listaErrores += Comprueba2(self.fraccionPotenciaEntrada, 2, self.listaErrores, 'fracci\xf3n potencia total a la que entra el generador', 0.0, 1.0).ErrorDevuelto
        else:
            self.listaErrores += Comprueba(self.potNominal, 2, self.listaErrores, 'potencia nominal', 0).ErrorDevuelto
            self.listaErrores += Comprueba(self.rendNominalPG, 2, self.listaErrores, 'rendimiento/COP Nominal', 0).ErrorDevuelto
            self.listaErrores += Comprueba2(self.factorCargaMinimo, 2, self.listaErrores, 'factor de carga parcial m\xednimo', 0.0, 1.0).ErrorDevuelto
            if Comprueba2(self.factorCargaMinimo, 2, self.listaErrores, 'factor de carga parcial m\xednimo', 0.0, 1.0).ErrorDevuelto == '':
                self.listaErrores += Comprueba(self.factorCargaMaximo, 2, self.listaErrores, 'factor de carga parcial m\xe1ximo', float(self.factorCargaMinimo), 1.0).ErrorDevuelto
            else:
                self.listaErrores += Comprueba(self.factorCargaMaximo, 2, self.listaErrores, 'factor de carga parcial m\xe1ximo', 0.0, 1.0).ErrorDevuelto
            if 'Bomba' in self.generadorChoice.GetStringSelection():
                self.listaErrores += Comprueba(self.temperaturaAmbienteInt, 2, self.listaErrores, 'temperatura ambiente interior', 0).ErrorDevuelto
        if u'Conocido' not in rendi and self.listaErrores == '':
            if self.rendimientoEstacionalRef != '':
                self.listaErrores += Comprueba(str(self.rendimientoEstacionalRef), 2, self.listaErrores, 'rendimiento medio estacional', 0.0).ErrorDevuelto