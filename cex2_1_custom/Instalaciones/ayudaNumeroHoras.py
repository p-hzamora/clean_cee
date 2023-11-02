# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\ayudaNumeroHoras.pyc
# Compiled at: 2014-12-09 12:32:30
import Instalaciones.escalonamientoEquipos as escalonamientoEquipos, Instalaciones.perfilesTerciario as perfilesTerciario
from Instalaciones.comprobarCampos import Comprueba

def create(parent):
    return Dialog1(parent)



class Dialog1(wx.Dialog):

    def _init_ctrls(self, prnt):
        self.potencia = ''
        self.demanda = ''
        self.tgnr = ''
        self.tgnr.SetEditable(False)
        self.tgnr.Enable(False)
        self.potencia.SetToolTip(wx.ToolTip('Potencia máxima demanda por la instalación (kW)'))
        self.demanda.SetToolTip(wx.ToolTip('Demanda térmica anual (kWh). \nSi previamente ya ha realizado una calificación, en este campo, le aparecerá la demanda\ncalculada de calefacción o refrigeración, dependiendo del servicio seleccionado.'))

    def __init__(self, parent, zona, perfilUso, servicio):
        self.parent = parent
        self._init_ctrls(parent)
        self.dev = []
        self.zona = zona
        self.perfilUso = perfilUso
        self.servicio = servicio
        self.calculoDemandaCalefaccion()

    def calculoDemandaCalefaccion(self):
        if self.parent.parent.parent.parent.objEdificio.casoValido == True:
            if self.servicio == 'Calefacción':
                dda = self.parent.parent.parent.parent.objEdificio.datosResultados.ddaBrutaCal
                dda = round(dda * self.parent.parent.parent.parent.objEdificio.datosIniciales.area, 1)
            elif self.servicio == 'Refrigeración':
                dda = self.parent.parent.parent.parent.objEdificio.datosResultados.ddaBrutaRef
                dda = round(dda * self.parent.parent.parent.parent.objEdificio.datosIniciales.area, 1)
            else:
                dda = self.parent.parent.parent.parent.objEdificio.datosResultados.ddaBrutaACS
                dda = round(dda * self.parent.parent.parent.parent.objEdificio.datosIniciales.area, 1)
            self.demanda= str(dda)

    def OnAceptarButton(self, event):
        listaErrores = ''
        listaErrores += Comprueba(self.potencia, 2, listaErrores, 'potencia máxima de la instalación', 0.0).ErrorDevuelto
        listaErrores += Comprueba(self.demanda, 2, listaErrores, 'demanda de energía anual', 0.0).ErrorDevuelto
        if listaErrores == '':
            self.dev = [
             self.tgnr]
            self.Close()
        else:
            raise Exception('Revise los siguientes campos:\n' + listaErrores)

    def OnCancelarButton(self, event):
        self.Close()

    def calculoTiempoFuncionamiento(self, event):
        try:
            dato = self.potencia
            if ',' in dato:
                dato = dato.replace(',', '.')
                self.potencia= dato
                self.potencia.SetInsertionPointEnd()
            dato = self.demanda
            if ',' in dato:
                dato = dato.replace(',', '.')
                self.demanda= dato
                self.demanda.SetInsertionPointEnd()
            fcpSistema = [0.05, 
             0.15, 
             0.25, 
             0.35, 
             0.45, 
             0.55, 
             0.65, 
             0.75, 
             0.85, 
             0.95]
            if self.servicio == 'Calefacción':
                distribucionFraccionEnergia = perfilesTerciario.PerfilDemandaCalefaccion(self.zona, self.perfilUso)
            elif self.servicio == 'Refrigeración':
                distribucionFraccionEnergia = perfilesTerciario.PerfilDemandaRefrigeracion(self.zona, self.perfilUso)
            elif self.servicio == 'ACS':
                distribucionFraccionEnergia = [
                 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                 0.0, 0.0, 0.0, 1.0]
            listaFracciones = [
             1.0]
            if self.zona != '':
                porcentajeEnergiaEquipos, betaComb = escalonamientoEquipos.porcentajeEnergiaEquipos(listaFracciones, fcpSistema, distribucionFraccionEnergia)
                if self.demanda != '':
                    energiaAnualEquipos = [ float(x) * float(self.demanda) / 100.0 for x in porcentajeEnergiaEquipos ]
                    tgnr = [ round(float(energiaAnualEquipos[i]) / (float(self.potencia) * float(betaComb[i])), 1) for i in range(len(betaComb))
                           ]
                    aux = str(tgnr).replace('[', '').replace(']', '').replace("'", '')
                    aux = str(round(float(aux), 1))
                    self.tgnr= aux
        except:
            self.tgnr= ''