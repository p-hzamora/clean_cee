# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\ayudaCargaParcialCalefaccion.pyc
# Compiled at: 2015-02-19 13:18:33
from Calculos.funcionesCalculo import betaCombDefecto
from Instalaciones.comprobarCampos import Comprueba, Comprueba2
import Instalaciones.equipos as equipos, wx, logging

class Dialog1(wx.Dialog):

    def _init_ctrls(self, prnt):
        self.fraccionPotenciaTotal = '1.0'
        self.fraccionInicio = '0.0'
        self.fraccionEnergia = ''
        self.fraccionEnergia.SetEditable(False)
        self.fraccionEnergia.Enable(False)
        self.factorCargaParcial = ''
        self.factorCargaParcial.Enable(False)
        self.factorCargaParcial.SetEditable(False)
        self.fraccionPotenciaTotal.SetToolTip(wx.ToolTip('Si exiten varias calderas que trabajan simultáneamente para dar la potencia total\ndemandada por la instalación, debe indicar en este campo la fracción de la potencia total que corresponde\na la caldera que se está introduciendo. \nPor ejemplo, si una instalación cuenta con dos calderas de 60 y 40 kW,\nse podrán definir como dos generadores independientes y cada uno de ellos \nrepresentarán respectivamente las fracciones 0.6 y 0.4 de la potencia total.'))
        self.fraccionInicio.SetToolTip(wx.ToolTip('Si exiten varias calderas que trabajan simultáneamente para dar la potencia total\ndemandada por la instalación, debe indicar en este campo la fracción de la potencia total a la que\nentra en servicio a la caldera que se está introduciendo. \nPor ejemplo, si una instalación cuenta con dos calderas de 60 y 40 kW, y la gestión\nde las calderas se realiza de tal manera que entra primero la de 60 kW y luego la de 40 kW, \ndiremos que la fracción de la potencia total a la que entra el generador de 60 kW es 0.0 \ny la fraccción de la potencia total a la que entra el generador de 40 kW es 0.6'))

    def __init__(self, parent, inicio):
        self.parent = parent
        self.dev = []
        self._init_ctrls(parent)
        self.iniciaValores(inicio)
        self.OnBotonCalcularButton(None)
        return

    def iniciaValores(self, inicio):
        self.fraccionPotenciaTotal= str(inicio[0])
        self.fraccionInicio= str(inicio[1])

    def OnBotonCalcularButton(self, event):
        zona = self.parent.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()
        if self.parent.parent.parent.parent.programa == 'Residencial':
            uso = 'Residencial'
        else:
            uso = self.parent.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
        fraccionInicio = self.fraccionInicio
        fraccionPotenciaTotal = self.fraccionPotenciaTotal
        if ',' in fraccionInicio:
            fraccionInicio = fraccionInicio.replace(',', '.')
            self.fraccionInicio= fraccionInicio
            self.fraccionInicio.SetInsertionPointEnd()
        if ',' in fraccionPotenciaTotal:
            fraccionPotenciaTotal = fraccionPotenciaTotal.replace(',', '.')
            self.fraccionPotenciaTotal= fraccionPotenciaTotal
            self.fraccionPotenciaTotal.SetInsertionPointEnd()
        try:
            porcentajeDesde = float(self.fraccionInicio)
            porcentajeDeLaPotenciaTotalAportadoPorEsteGenerador = float(self.fraccionPotenciaTotal)
            porcentajeEnergiaGenerador, betaComb = equipos.estimacionCargaEscalonadaCalefaccion(zona, uso, porcentajeDesde, porcentajeDeLaPotenciaTotalAportadoPorEsteGenerador)
            if betaComb < betaCombDefecto:
                betaComb = betaCombDefecto
            self.fraccionEnergia= str(round(sum(porcentajeEnergiaGenerador, 2)))
            self.factorCargaParcial= str(round(betaComb, 2))
        except:
            logging.info('Excepcion en: %s' % __name__)
            self.fraccionEnergia= ''
            self.factorCargaParcial= ''

    def OnBotonAplicarButton(self, event):
        dato = self.fraccionPotenciaTotal
        if ',' in dato:
            self.fraccionPotenciaTotal= dato.replace(',', '.')
        dato = self.fraccionInicio
        if ',' in dato:
            self.fraccionInicio= dato.replace(',', '.')
        listaErrores = ''
        listaErrores += Comprueba(self.fraccionPotenciaTotal, 2, listaErrores, 'fracción de la potencia total aportada por este generador', 0.0, 1.0).ErrorDevuelto
        listaErrores += Comprueba2(self.fraccionInicio, 2, listaErrores, 'fracción de la potencia total a la que entra este generador', 0.0, 1.0).ErrorDevuelto
        if listaErrores == '':
            self.dev = [
             self.fraccionEnergia, self.factorCargaParcial,
             self.fraccionPotenciaTotal, self.fraccionInicio]
            self.Close()
        else:
            raise Exception('Revise los siguientes campos:\n' + listaErrores)

    def OnBotonCancelarButton(self, event):
        self.Close()