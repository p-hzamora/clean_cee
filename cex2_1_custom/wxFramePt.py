# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: wxFramePt.pyc
# Compiled at: 2015-02-11 12:22:46
"""
Modulo: wxFramePt.py

"""
import idioma
idioma.ini()
from Escala.escalaCalificacion import escalaTerciario
from panelCalificacion import panelCalificacion
import Informes.creaPDF, datosEdificio, directorios, Calculos.listadosWeb as listadosWeb, wx, wxFrame1
from Calculos.funcionesCalculo import getValorDefectoVentilacion
Directorio = directorios.BuscaDirectorios().Directorio

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return wxFramePt(parent)


class wxFramePt(wxFrame1.wxFrame1):
    """
    Clase: wxFramePt del modulo wxFramePt.py

    """

    def __init__(self, parent=None):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent = None:
        """
        wxFrame1.wxFrame1.__init__(self, parent=None)
        self.escala = escalaTerciario()
        self.SetTitle(_('CE3X - PT: Certificación energética simplificada de edificios existentes - Pequeño terciario'))
        self.programa = b'Peque\xf1oTerciario'
        self.panelDatosGenerales.tipoEdificioText.SetLabel(_('Perfil de uso'))
        self.panelDatosGenerales.tipoEdificioChoice.SetItems(listadosWeb.listadoCalendarios)
        self.panelDatosGenerales.tipoEdificioText.SetPosition(wx.Point(374, 120))
        self.panelDatosGenerales.tipoEdificioChoice.SetPosition(wx.Point(466, 118))
        self.panelDatosGenerales.tipoEdificioChoice.SetSize(wx.Size(165, 21))
        self.panelDatosGenerales.ventilacion.SetValue('%s' % getValorDefectoVentilacion(self.programa))
        self.panelDatosGenerales.consumoACS.Show(True)
        self.panelDatosGenerales.consumoACSText.Show(True)
        self.panelDatosGenerales.consumoACSUnidades.Show(True)
        self.panelDatosGenerales.tipoEdificioChoice.SetToolTip(wx.ToolTip(_('Tipo de uso del edificio. Depende del nivel de intensidad de las fuentes internas (alto, medio, bajo) con cuatro perfiles horarios de funcionamiento diario (8 horas, 12 horas, 16 horas, 24 horas).')))
        self.panelDatosGenerales.tipoEdificioTerciarioText.Show(True)
        self.panelDatosGenerales.tipoEdificioTerciarioChoice.Show(True)
        self.panelInstalaciones.panelElegirObjeto.iluminacion.Show(True)
        self.panelInstalaciones.panelElegirObjeto.ventilacion.Show(True)
        self.panelInstalaciones.vistaClasica.definirIluminacion.Show(True)
        self.panelInstalaciones.vistaClasica.definirVentilacion.Show(True)
        return

    def calculoCalificacion(self):
        zonaCalificacion = ''
        self.objEdificio = datosEdificio.datosEdificioTerciario(datosGenerales=self.panelDatosGenerales.exportarDatos(), datosEnvolvente=self.panelEnvolvente.cogerDatos(), datosInstalaciones=self.panelInstalaciones.exportarDatos(), programa=self.programa, subgrupos=self.notebook1.subgrupos, zonaCalificacion=zonaCalificacion, datosSombras=self.datosSombras, escala=self.escala, esEdificioExistente=self.esEdificioExistente)
        self.objEdificio.calificacion()

    def PanelResultadosCalificacion(self, objEdificio):
        """
        Metodo: PanelResultadosCalificacion

        ARGUMENTOS:
                lista_calificaciones:
                lista_limites:
                balanceContribuciones:
        """
        self.panelCalificacion = panelCalificacion(parent=self.notebook1, id=wx.NewId(), pos=self.posicion_defecto, size=(0,
                                                                                                                          0), style=0, name='')
        self.paneles.append(self.panelCalificacion)
        self.notebook1.iniciaPaneles([self.paneles[int(len(self.paneles) - 1)]], self.notebook1)
        self.notebook1.SetSelection(len(self.paneles) - 1)
        emisiones_limites = objEdificio.datosResultados.emisiones_limites
        limite_A = round(emisiones_limites[0], 1)
        limite_B = round(emisiones_limites[1], 1)
        limite_C = round(emisiones_limites[2], 1)
        limite_D = round(emisiones_limites[3], 1)
        limite_E = round(emisiones_limites[4], 1)
        limite_F = round(emisiones_limites[5], 1)
        self.panelCalificacion.ValorDdaCal.SetLabel(str(round(objEdificio.datosResultados.ddaBrutaCal, 1)))
        self.panelCalificacion.ValorDdaRef.SetLabel(str(round(objEdificio.datosResultados.ddaBrutaRef, 1)))
        self.panelCalificacion.ValorEmisCal.SetLabel(str(round(objEdificio.datosResultados.emisionesCal, 1)))
        self.panelCalificacion.ValorEmisRef.SetLabel(str(round(objEdificio.datosResultados.emisionesRef, 1)))
        self.panelCalificacion.ValorEmisACS.SetLabel(str(round(objEdificio.datosResultados.emisionesACS, 1)))
        self.panelCalificacion.ValorEmisIluminacion.SetLabel(str(round(objEdificio.datosResultados.emisionesIlum, 1)))
        self.panelCalificacion.EmisIluminacion.Show(True)
        self.panelCalificacion.Unidades6.Show(True)
        self.panelCalificacion.ValorEmisIluminacion.Show(True)
        self.panelCalificacion.NotaEmisIluminacion.Show(True)
        self.panelCalificacion.NotaDdaCal.SetLabel(objEdificio.datosResultados.ddaBrutaCal_nota)
        self.panelCalificacion.NotaDdaRef.SetLabel(objEdificio.datosResultados.ddaBrutaRef_nota)
        self.panelCalificacion.NotaEmisCal.SetLabel(objEdificio.datosResultados.emisionesCal_nota)
        self.panelCalificacion.NotaEmisRef.SetLabel(objEdificio.datosResultados.emisionesRef_nota)
        self.panelCalificacion.NotaEmisACS.SetLabel(objEdificio.datosResultados.emisionesACS_nota)
        self.panelCalificacion.NotaEmisIluminacion.SetLabel(objEdificio.datosResultados.emisionesIlum_nota)
        self.panelCalificacion.LimiteA.SetLabel(_('< ') + str(limite_A))
        self.panelCalificacion.LimiteB.SetLabel(_('< ') + str(limite_B))
        self.panelCalificacion.LimiteC.SetLabel(_('< ') + str(limite_C))
        self.panelCalificacion.LimiteD.SetLabel(_('< ') + str(limite_D))
        self.panelCalificacion.LimiteE.SetLabel(_('< ') + str(limite_E))
        self.panelCalificacion.LimiteF.SetLabel(_('< ') + str(limite_F))
        self.panelCalificacion.LimiteG.SetLabel(_('>=') + str(limite_F))
        self.panelCalificacion.NotaA.Show(False)
        self.panelCalificacion.NotaB.Show(False)
        self.panelCalificacion.NotaC.Show(False)
        self.panelCalificacion.NotaD.Show(False)
        self.panelCalificacion.NotaE.Show(False)
        self.panelCalificacion.NotaF.Show(False)
        self.panelCalificacion.NotaG.Show(False)
        self.panelCalificacion.EmisA.Show(False)
        self.panelCalificacion.EmisB.Show(False)
        self.panelCalificacion.EmisC.Show(False)
        self.panelCalificacion.EmisD.Show(False)
        self.panelCalificacion.EmisE.Show(False)
        self.panelCalificacion.EmisF.Show(False)
        self.panelCalificacion.EmisG.Show(False)
        emisionesGlobales = str(round(objEdificio.datosResultados.emisionesMostrar, 1))
        if objEdificio.datosResultados.emisiones_nota == 'A':
            self.panelCalificacion.NotaA.Show(True)
            self.panelCalificacion.EmisA.SetLabel(emisionesGlobales)
            self.panelCalificacion.EmisA.Show(True)
        if objEdificio.datosResultados.emisiones_nota == 'B':
            self.panelCalificacion.NotaB.Show(True)
            self.panelCalificacion.EmisB.SetLabel(emisionesGlobales)
            self.panelCalificacion.EmisB.Show(True)
        if objEdificio.datosResultados.emisiones_nota == 'C':
            self.panelCalificacion.NotaC.Show(True)
            self.panelCalificacion.EmisC.SetLabel(emisionesGlobales)
            self.panelCalificacion.EmisC.Show(True)
        if objEdificio.datosResultados.emisiones_nota == 'D':
            self.panelCalificacion.NotaD.Show(True)
            self.panelCalificacion.EmisD.SetLabel(emisionesGlobales)
            self.panelCalificacion.EmisD.Show(True)
        if objEdificio.datosResultados.emisiones_nota == 'E':
            self.panelCalificacion.NotaE.Show(True)
            self.panelCalificacion.EmisE.SetLabel(emisionesGlobales)
            self.panelCalificacion.EmisE.Show(True)
        if objEdificio.datosResultados.emisiones_nota == 'F':
            self.panelCalificacion.NotaF.Show(True)
            self.panelCalificacion.EmisF.SetLabel(emisionesGlobales)
            self.panelCalificacion.EmisF.Show(True)
        if objEdificio.datosResultados.emisiones_nota == 'G':
            self.panelCalificacion.NotaG.Show(True)
            self.panelCalificacion.EmisG.SetLabel(emisionesGlobales)
            self.panelCalificacion.EmisG.Show(True)
        if objEdificio.datosResultados.emisionesContrib != 0:
            self.panelCalificacion.balanceContribuciones.Show(True)
            self.panelCalificacion.balanceContribucionesUnidades.Show(True)
            self.panelCalificacion.valorBalanceContribuciones.SetLabel(str(round(objEdificio.datosResultados.emisionesContrib, 1)))
            self.panelCalificacion.valorBalanceContribuciones.Show(True)
        else:
            self.panelCalificacion.balanceContribuciones.Show(False)
            self.panelCalificacion.balanceContribucionesUnidades.Show(False)
            self.panelCalificacion.valorBalanceContribuciones.Show(False)
        self.panelCalificacion.SetSize(self.tamano_defecto)

    def OnMenuFileOpenNuevo(self, event):
        """
        Metodo: OnMenuFileOpenNuevo

        ARGUMENTOS:
                event:
        """
        wxFrame1.wxFrame1.OnMenuFileOpenNuevo(self, event)
        self.SetTitle(_('CE3X - PT: Certificación Energética Simplificada de Edificios Existentes - Pequeño Terciario'))

    def OnMenuFileSaveasMenu(self, event):
        """
        Metodo: OnMenuFileSaveasMenu

        ARGUMENTOS:
                event:
        """
        wxFrame1.wxFrame1.OnMenuFileSaveasMenu(self, event)
        self.SetTitle(_('CE3X - PT: %s') % self.filename)

    def OnMenuFileSaveMenu(self, event):
        """
        Metodo: OnMenuFileSaveMenu

        ARGUMENTOS:
                event:
        """
        wxFrame1.wxFrame1.OnMenuFileSaveMenu(self, event)
        self.SetTitle(_('CE3X - PT: %s') % self.filename)

    def OnMenuFileOpenMenu(self, event):
        """
        Metodo: OnMenuFileOpenMenu

        ARGUMENTOS:
                event:
        """
        wxFrame1.wxFrame1.OnMenuFileOpenMenu(self, event)
        self.SetTitle(_('CE3X - PT: %s') % self.filename)

    def abreArchivoDirecto(self, fichero):
        """
        Metodo: abreArchivoDirecto

        ARGUMENTOS:
                event:
        """
        wxFrame1.wxFrame1.abreArchivoDirecto(self, fichero)
        self.SetTitle(_('CE3X - PT: %s') % self.filename)