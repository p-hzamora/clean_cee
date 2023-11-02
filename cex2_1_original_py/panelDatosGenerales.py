# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: panelDatosGenerales.pyc
# Compiled at: 2015-02-19 13:18:34
"""
Modulo: panelDatosGenerales.py

"""
from Calculos.funcionesCalculo import getValorDefectoVentilacion, getValorDdaACSVersionesAnteriores, getValorVentilacionNoGuardado
from Calculos.listados import Localizacion
from Envolvente.funcionActualizarEnvolvente import actualizarEnvolvente
from Instalaciones.comprobarCampos import Comprueba, Comprueba2
from Instalaciones.funcionActualizarInstalacionesGeneracion import actualizarInstalacionesGeneracion, actualizarRendimientoConjuntosMM
from MedidasDeMejora.funcionActualizarMMInstalacionesAlCambiarSuperficie import existenInstalacionesColgandoDeZonaModificadaOEliminadaEnConjuntosMM, actualizarCoberturaDeConjuntosMM, actualizarSuperficieIluminacionDeConjuntosMM
from PIL import Image
from miChoice import MiChoice
from undo import eventoUndo
import Calculos.calculoPerdidasSombras as calculoPerdidasSombras, Calculos.calculoSuperficies as calculoSuperficies, Calculos.listadosWeb as listadosWeb, DatosGenerales.ayudaNormativaVigente as ayudaNormativaVigente, DatosGenerales.trataImagenes as trataImagenes, Envolvente.tablasValores as tablasValores, Instalaciones.equipos as equipos, Instalaciones.perfilesTerciario as perfilesTerciario, StringIO, base64, copy, directorios, wx, logging
Directorio = directorios.BuscaDirectorios().Directorio
wxID_PANEL1, wxID_PANEL1ALTURAMEDIALIBRE, wxID_PANEL1ANOCONSTRUCCIONCHOICE, wxID_PANEL1ANOCONSTRUCCIONTEXT, wxID_PANEL1CIUDADCHOICE, wxID_PANEL1HE1, wxID_PANEL1HE1TEXT, wxID_PANEL1HE4, wxID_PANEL1HE4TEXT, wxID_PANEL1LOCALIDADTEXT, wxID_PANEL1METROSCUADRADOSTEXT, wxID_PANEL1METROSTEXT, wxID_PANEL1NUMEROPLANTAS, wxID_PANEL1NUMEROPLANTASTEXT, wxID_PANEL1SUPERFICIEACONDICIONADA, wxID_PANEL1SUPERFICIEACONDICIONADATEXT, wxID_PANEL1PROVINCIACHOICE, wxID_PANEL1PROVINCIATEXT, wxID_PANEL1DEFINICIONEDIFICIOTEXT, wxID_PANEL1ALTURATEXT, wxID_PANEL1MASATEXT, wxID_PANEL1SUPERFICIE, wxID_PANEL1SUPERFICIETEXT, wxID_PANEL1TIPOEDIFICIOCHOICE, wxID_PANEL1TIPOEDIFICIOTEXT, wxID_PANEL1CHOICE1, wxID_PANEL1ZONACLIMATICATEXT, wxID_PANEL1MASAPARTICIONES, wxID_PANEL1SUPERFICIEACONDICIONADAUNIDADESTEXT, wxID_PANEL1DATOSGENERALESTEXT, wxID_WXPANEL1EXTRAPENINSULAR, wxID_PANEL1OTROCUADRO, wxID_WXBLOWERDOORCHECK, wxID_PANEL1Q50TEXT, wxID_PANEL1Q50CUADRO, wxID_PANEL1NTEXT, wxID_PANEL1NCUADRO, wxID_PANEL1Q50UNIDADES, wxID_WXPANEL1EXENTOH4, wxID_WXPANEL1EXENTOH42, wxID_PANEL1MODIFICARBOTON, wxID_PANEL1BDTText, wxID_PANEL1PROHIBICIONTEXT, wxID_PANEL1IMAGENBOTON, wxID_PANEL1IMAGEN, wxID_PANEL1PLANO, wxID_PANEL1PLANOBOTON, wxID_PANEL1ANOCONSTRUCCIONNUMEROTEXT, wxID_PANEL1ANOCONSTRUCCIONNUMEROCUADRO, wxID_PANEL1TIPOEDIFICIOTERCIARIOTEXT, wxID_PANEL1TIPOEDIFICIOTERCIARIOCHOICE, wxID_PANEL1VENTILACIONTEXT, wxID_PANEL1VENTILACION, wxID_PANEL1VENTILACIONUNIDADESTEXT = [ wx.NewId() for _init_ctrls in range(54) ]

class panelDatosGenerales(wx.Panel):
    """
    Clase: panelDatosGenerales del modulo panelDatosGenerales.py

    """

    def _init_ctrls(self, prnt, id_prnt, pos_prnt, size_prnt, style_prnt, name_prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                  prnt:
                 id_prnt:
                 pos_prnt:
                 size_prnt:
                 style_prnt:
                 name_prnt:
        """
        wx.Panel.__init__(self, id=id_prnt, name=name_prnt, parent=prnt, pos=pos_prnt, size=size_prnt, style=style_prnt | wx.TAB_TRAVERSAL)
        self.SetBackgroundColour('white')
        self.datosGeneralesText = wx.StaticBox(id=wxID_PANEL1DATOSGENERALESTEXT, label=_('Datos generales'), name='datosGeneralesText', parent=self, pos=wx.Point(32, 32), size=wx.Size(896, 183), style=0)
        self.datosGeneralesText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.datosGeneralesText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.normativaText = wx.StaticText(id=wxID_PANEL1ANOCONSTRUCCIONTEXT, label=_('Normativa vigente'), name='anoConstruccionText', parent=self, pos=wx.Point(56, 76), size=wx.Size(106, 13), style=0)
        self.anoConstruccionChoice = MiChoice(choices=listadosWeb.normativaVigente, id=wxID_PANEL1ANOCONSTRUCCIONCHOICE, name='anoConstruccionChoice', parent=self, pos=wx.Point(174, 74), size=wx.Size(130, 21), style=0)
        self.anoConstruccionChoice.Bind(wx.EVT_CHOICE, self.OnAnoConstruccionChoice, id=wxID_PANEL1ANOCONSTRUCCIONCHOICE)
        self.normativaHelpButton = wx.Button(id=wxID_PANEL1MODIFICARBOTON, label=_(' ?'), name='normativaHelpButton', parent=self, pos=wx.Point(312, 74), size=wx.Size(20, 20), style=0)
        self.normativaHelpButton.Bind(wx.EVT_BUTTON, self.onNormativaHelpButton, id=wxID_PANEL1MODIFICARBOTON)
        self.anoConstruccionNumeroText = wx.StaticText(id=wxID_PANEL1ANOCONSTRUCCIONNUMEROTEXT, label=_('Año construcción'), name='anoConstruccionText', parent=self, pos=wx.Point(374, 76), size=wx.Size(82, 13), style=0)
        self.anoConstruccionNumeroCuadro = wx.TextCtrl(id=wxID_PANEL1ANOCONSTRUCCIONNUMEROCUADRO, name='anoConstruccionNumeroCuadro', parent=self, pos=wx.Point(466, 74), size=wx.Size(165, 21), style=0, value='')
        self.tipoEdificioTerciarioText = wx.StaticText(id=wxID_PANEL1TIPOEDIFICIOTERCIARIOTEXT, label=_('Tipo de edificio'), name='tipoEdificioText', parent=self, pos=wx.Point(56, 120), size=wx.Size(82, 13), style=0)
        self.tipoEdificioTerciarioText.Show(False)
        self.tipoEdificioTerciarioChoice = MiChoice(choices=listadosWeb.tipoEdificioTerciario, id=wxID_PANEL1TIPOEDIFICIOTERCIARIOCHOICE, name='tipoEdificioTerciarioChoice', parent=self, pos=wx.Point(174, 118), size=wx.Size(158, 21), style=0)
        self.tipoEdificioTerciarioChoice.Show(False)
        self.tipoEdificioText = wx.StaticText(id=wxID_PANEL1TIPOEDIFICIOTEXT, label=_('Tipo de edificio'), name='tipoEdificioText', parent=self, pos=wx.Point(56, 120), size=wx.Size(75, 13), style=0)
        self.tipoEdificioChoice = MiChoice(choices=listadosWeb.tipoEdificioResidencial, id=wxID_PANEL1TIPOEDIFICIOCHOICE, name='tipoEdificioChoice', parent=self, pos=wx.Point(174, 118), size=wx.Size(158, 21), style=0)
        self.tipoEdificioChoice.Bind(wx.EVT_CHOICE, self.OnTipoEdificioChoice, id=wxID_PANEL1TIPOEDIFICIOCHOICE)
        self.provinciaText = wx.StaticText(id=wxID_PANEL1PROVINCIATEXT, label=_('Provincia/Ciudad\n          autónoma'), name='provinciaText', parent=self, pos=wx.Point(55, 164), size=wx.Size(110, 25), style=0)
        self.provinciaChoice = MiChoice(choices=Localizacion().getListadoProvincias(), id=wxID_PANEL1PROVINCIACHOICE, name='provinciaChoice', parent=self, pos=wx.Point(174, 162), size=wx.Size(158, 21), style=0)
        self.provinciaChoice.Bind(wx.EVT_CHOICE, self.OnProvinciaChoice, id=wxID_PANEL1PROVINCIACHOICE)
        self.localidadText = wx.StaticText(id=wxID_PANEL1LOCALIDADTEXT, label=_('Localidad'), name='localidadText', parent=self, pos=wx.Point(374, 164), size=wx.Size(48, 13), style=0)
        self.localidadChoice = MiChoice(choices=[], id=wxID_PANEL1CHOICE1, name='choice1', parent=self, pos=wx.Point(466, 162), size=wx.Size(165, 21), style=0)
        self.localidadChoice.Bind(wx.EVT_CHOICE, self.OnLocalidadChoice, id=wxID_PANEL1CHOICE1)
        self.otroCuadro = wx.TextCtrl(id=wxID_PANEL1OTROCUADRO, name='otroCuadro', parent=self, pos=wx.Point(466, 184), size=wx.Size(165, 21), style=0, value='')
        self.otroCuadro.Show(False)
        self.otroCuadro.Bind(wx.EVT_KILL_FOCUS, self.OnOtroCuadro, id=wxID_PANEL1OTROCUADRO)
        self.zonaClimaticaText = wx.StaticText(id=wxID_PANEL1ZONACLIMATICATEXT, label=_('Zona climática '), name='zonaClimaticaText', parent=self, pos=wx.Point(661, 164), size=wx.Size(76, 13), style=0)
        self.HE1Text = wx.StaticText(id=wxID_PANEL1HE1TEXT, label=_('HE-1'), name='HE1Text', parent=self, pos=wx.Point(760, 136), size=wx.Size(75, 13), style=0)
        self.HE4Text = wx.StaticText(id=wxID_PANEL1HE4TEXT, label=_('HE-4'), name='HE4Text', parent=self, pos=wx.Point(842, 136), size=wx.Size(23, 13), style=0)
        self.HE1 = MiChoice(choices=[], id=wxID_PANEL1HE1, name='he1', parent=self, pos=wx.Point(745, 162), size=wx.Size(72, 21), style=0)
        self.HE1.Bind(wx.EVT_CHOICE, self.OnHE1, id=wxID_PANEL1HE1)
        self.HE1.Enable(False)
        self.HE4 = MiChoice(choices=listadosWeb.listadoZonaHE4, id=wxID_PANEL1HE4, name='he4', parent=self, pos=wx.Point(832, 162), size=wx.Size(72, 21), style=0)
        self.HE4.Bind(wx.EVT_CHOICE, self.OnHE4, id=wxID_PANEL1HE4)
        self.HE4.Enable(False)
        self.Extrapeninsular = wx.CheckBox(id=wxID_WXPANEL1EXTRAPENINSULAR, label=_('Extrapeninsular'), name='Extrapeninsular', parent=self, pos=wx.Point(614, 189), size=wx.Size(125, 20), style=0)
        self.Extrapeninsular.SetValue(False)
        self.Extrapeninsular.Show(False)
        self.ExentoHE4 = wx.CheckBox(id=wxID_WXPANEL1EXENTOH4, label=_('Edificio  protegido  en '), name='ExentoHE4', parent=self, pos=wx.Point(787, 189), size=wx.Size(120, 20), style=0)
        self.ExentoHE4.SetValue(False)
        self.ExentoHE4.Show(False)
        self.definicionEdificioText = wx.StaticBox(id=wxID_PANEL1DEFINICIONEDIFICIOTEXT, label=_('Definición edificio '), name='DefinicionEdificioText', parent=self, pos=wx.Point(32, 224), size=wx.Size(896, 351), style=0)
        self.definicionEdificioText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.definicionEdificioText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.superficieText = wx.StaticText(id=wxID_PANEL1SUPERFICIETEXT, label=_('Superficie útil habitable'), name='superficieText', parent=self, pos=wx.Point(56, 256), size=wx.Size(117, 13), style=0)
        self.metrosCuadradosText = wx.StaticText(id=wxID_PANEL1METROSCUADRADOSTEXT, label=_('m2'), name='metrosCuadradosText', parent=self, pos=wx.Point(310, 256), size=wx.Size(22, 13), style=0)
        self.alturaText = wx.StaticText(id=wxID_PANEL1ALTURATEXT, label=_('Altura libre de planta'), name='AlturaText', parent=self, pos=wx.Point(56, 296), size=wx.Size(107, 13), style=0)
        self.metrosText = wx.StaticText(id=wxID_PANEL1METROSTEXT, label=_('m'), name='metrosText', parent=self, pos=wx.Point(310, 296), size=wx.Size(8, 13), style=0)
        self.numeroPlantasText = wx.StaticText(id=wxID_PANEL1NUMEROPLANTASTEXT, label=_('Número de plantas habitables'), name='numeroPlantasText', parent=self, pos=wx.Point(56, 336), size=wx.Size(147, 13), style=0)
        self.ventilacionText = wx.StaticText(id=wxID_PANEL1VENTILACIONTEXT, label=_('Ventilación del inmueble'), name='ventilacionText', parent=self, pos=wx.Point(56, 376), size=wx.Size(147, 13), style=0)
        self.ventilacionUnidadesText = wx.StaticText(id=wxID_PANEL1VENTILACIONUNIDADESTEXT, label=_('ren/h'), name='ventilacionUnidadesText', parent=self, pos=wx.Point(310, 376), size=wx.Size(30, 13), style=0)
        self.consumoACSText = wx.StaticText(id=wxID_PANEL1SUPERFICIEACONDICIONADATEXT, label=_('Consumo total diario de ACS'), name='superficieAcondicionadaText', parent=self, pos=wx.Point(56, 416), size=wx.Size(147, 13), style=0)
        self.consumoACSUnidades = wx.StaticText(id=wxID_PANEL1SUPERFICIEACONDICIONADAUNIDADESTEXT, label=_('l/día'), name='superficieAcondicionadaUnidadesText', parent=self, pos=wx.Point(310, 416), size=wx.Size(22, 13), style=0)
        self.masaText = wx.StaticText(id=wxID_PANEL1MASATEXT, label=_('Masa de las particiones internas '), name='masaText', parent=self, pos=wx.Point(56, 456), size=wx.Size(147, 13), style=0)
        self.superficie = wx.TextCtrl(id=wxID_PANEL1SUPERFICIE, name='superficie', parent=self, pos=wx.Point(230, 254), size=wx.Size(70, 21), style=wx.TE_PROCESS_ENTER, value='')
        self.superficie.Bind(wx.EVT_TEXT_ENTER, self.OnCambioSuperficie, id=wxID_PANEL1SUPERFICIE)
        self.superficie.Bind(wx.EVT_KILL_FOCUS, self.OnCambioSuperficie2, id=wxID_PANEL1SUPERFICIE)
        self.alturaMediaLibre = wx.TextCtrl(id=wxID_PANEL1ALTURAMEDIALIBRE, name='alturaMediaLibre', parent=self, pos=wx.Point(230, 294), size=wx.Size(70, 21), style=0, value='')
        self.alturaMediaLibre.SetValue('2.7')
        self.alturaMediaLibre.Bind(wx.EVT_KILL_FOCUS, self.OnAlturaMediaLibre, id=wxID_PANEL1ALTURAMEDIALIBRE)
        self.numeroPlantas = wx.TextCtrl(id=wxID_PANEL1NUMEROPLANTAS, name='numeroPlantas', parent=self, pos=wx.Point(230, 334), size=wx.Size(70, 21), style=0, value='')
        self.numeroPlantas.Bind(wx.EVT_KILL_FOCUS, self.OnNumeroPlantas, id=wxID_PANEL1NUMEROPLANTAS)
        valorDefectoVentilacion = getValorDefectoVentilacion(self.parent.parent.programa)
        self.ventilacion = wx.TextCtrl(id=wxID_PANEL1VENTILACION, name='ventilacion', parent=self, pos=wx.Point(230, 374), size=wx.Size(70, 21), style=0, value='%s' % valorDefectoVentilacion)
        self.ventilacion.Bind(wx.EVT_KILL_FOCUS, self.OnVentilacion, id=wxID_PANEL1VENTILACION)
        self.consumoACS = wx.TextCtrl(id=wxID_PANEL1SUPERFICIEACONDICIONADA, name='superficieAcondicionada', parent=self, pos=wx.Point(230, 414), size=wx.Size(70, 21), style=0, value='')
        self.consumoACS.Bind(wx.EVT_KILL_FOCUS, self.OnConsumoACS, id=wxID_PANEL1SUPERFICIEACONDICIONADA)
        self.masaParticiones = MiChoice(choices=listadosWeb.listadoMasas, id=wxID_PANEL1MASAPARTICIONES, name='masaParticiones', parent=self, pos=wx.Point(230, 454), size=wx.Size(70, 21), style=0)
        self.masaParticiones.SetSelection(1)
        self.masaParticiones.Bind(wx.EVT_KILL_FOCUS, self.OnMasaParticiones, id=wxID_PANEL1MASAPARTICIONES)
        self.BlowerDoorCheck = wx.CheckBox(id=wxID_WXBLOWERDOORCHECK, label=_('Se ha ensayado la estanqueidad del edificio'), name='BlowerDoorCheck', parent=self, pos=wx.Point(56, 496), size=wx.Size(276, 20), style=0)
        self.BlowerDoorCheck.Enable(True)
        self.BlowerDoorCheck.SetValue(False)
        self.BlowerDoorCheck.Bind(wx.EVT_CHECKBOX, self.OnBlowerDoorCheck, id=wxID_WXBLOWERDOORCHECK)
        self.BDTText = wx.StaticText(id=wxID_PANEL1BDTText, label=_('Ensayo Blower Door Test: '), name='BDTText', parent=self, pos=wx.Point(86, 521), size=wx.Size(150, 13), style=0)
        self.BDTText.Show(False)
        self.Q50Text = wx.StaticText(id=wxID_PANEL1Q50TEXT, label=_('q50'), name='Q50Text', parent=self, pos=wx.Point(225, 521), size=wx.Size(22, 13), style=0)
        self.Q50Text.Show(False)
        self.Q50Cuadro = wx.TextCtrl(id=wxID_PANEL1Q50CUADRO, name='Q50Cuadro', parent=self, pos=wx.Point(250, 519), size=wx.Size(50, 21), style=0, value='')
        self.Q50Cuadro.Show(False)
        self.Q50Cuadro.Bind(wx.EVT_KILL_FOCUS, self.OnQ50Cuadro, id=wxID_PANEL1Q50CUADRO)
        self.Q50Unidades = wx.StaticText(id=wxID_PANEL1Q50UNIDADES, label=_('l/s'), name='Q50Unidades', parent=self, pos=wx.Point(310, 521), size=wx.Size(22, 13), style=0)
        self.Q50Unidades.Show(False)
        self.NText = wx.StaticText(id=wxID_PANEL1NTEXT, label=_('n'), name='NText', parent=self, pos=wx.Point(225, 546), size=wx.Size(22, 13), style=0)
        self.NText.Show(False)
        self.NCuadro = wx.TextCtrl(id=wxID_PANEL1NCUADRO, name='NCuadro', parent=self, pos=wx.Point(250, 544), size=wx.Size(50, 21), style=0, value='')
        self.NCuadro.Show(False)
        self.NCuadro.Bind(wx.EVT_KILL_FOCUS, self.OnNCuadro, id=wxID_PANEL1NCUADRO)
        self.imagenButton = wx.Button(id=wxID_PANEL1IMAGENBOTON, label=_('Imagen edificio'), name='imagenButton', parent=self, pos=wx.Point(427, 544), size=wx.Size(100, 21), style=0)
        self.imagenButton.Bind(wx.EVT_BUTTON, self.onImagenButton, id=wxID_PANEL1IMAGENBOTON)
        self.panelImagen = wx.Panel(id=-1, name='panelImagen', parent=self, pos=wx.Point(338, 262), size=wx.Size(278, 278), style=0)
        self.imagen = wx.StaticBitmap(bitmap=wx.Bitmap(Directorio + '/Imagenes/Fotos_Materiales/blanco.bmp'), id=wxID_PANEL1IMAGEN, name='staticBitmap1', parent=self.panelImagen, pos=wx.Point(0, 0), size=wx.Size(278, 278), style=0)
        self.planoButton = wx.Button(id=wxID_PANEL1PLANOBOTON, label=_('Plano situación'), name='planoButton', parent=self, pos=wx.Point(715, 544), size=wx.Size(100, 21), style=0)
        self.planoButton.Bind(wx.EVT_BUTTON, self.onPlanoButton, id=wxID_PANEL1PLANOBOTON)
        self.panelPlano = wx.Panel(id=-1, name='panelPlano', parent=self, pos=wx.Point(626, 262), size=wx.Size(278, 278), style=0)
        self.plano = wx.StaticBitmap(bitmap=wx.Bitmap(Directorio + '/Imagenes/Fotos_Materiales/blanco.bmp'), id=wxID_PANEL1PLANO, name='staticBitmap1', parent=self.panelPlano, pos=wx.Point(0, 0), size=wx.Size(278, 278), style=0)

    def OnNCuadro(self, event):
        """
        Metodo: OnNCuadro

        ARGUMENTOS:
                event:
        """
        if self.diccionario['NCuadro'] != self.NCuadro.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'NCuadro', copy.deepcopy(self.diccionario['NCuadro'])))
            self.diccionario['NCuadro'] = self.NCuadro.GetValue()

    def OnQ50Cuadro(self, event):
        """
        Metodo: OnQ50Cuadro

        ARGUMENTOS:
                event:
        """
        if self.diccionario['Q50Cuadro'] != self.Q50Cuadro.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'Q50Cuadro', copy.deepcopy(self.diccionario['Q50Cuadro'])))
            self.diccionario['Q50Cuadro'] = self.Q50Cuadro.GetValue()

    def OnConsumoACS(self, event):
        """
        Metodo: OnConsumoACS

        ARGUMENTOS:
                 event:
        """
        if self.diccionario['consumoACS'] != self.consumoACS.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'consumoACS', copy.deepcopy(self.diccionario['consumoACS'])))
            self.diccionario['consumoACS'] = self.consumoACS.GetValue()

    def OnNumeroPlantas(self, event):
        """
        Metodo: OnNumeroPlantas

        ARGUMENTOS:
                 event:
        """
        if self.diccionario['numeroPlantas'] != self.numeroPlantas.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'numeroPlantas', copy.deepcopy(self.diccionario['numeroPlantas'])))
            self.diccionario['numeroPlantas'] = self.numeroPlantas.GetValue()

    def OnVentilacion(self, event):
        if self.diccionario['ventilacion'] != self.ventilacion.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'ventilacion', copy.deepcopy(self.diccionario['ventilacion'])))
            self.diccionario['ventilacion'] = self.ventilacion.GetValue()

    def OnAlturaMediaLibre(self, event):
        """
        Metodo: OnAlturaMediaLibre

        ARGUMENTOS:
                 event:
        """
        if self.diccionario['alturaMediaLibre'] != self.alturaMediaLibre.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'alturaMediaLibre', copy.deepcopy(self.diccionario['alturaMediaLibre'])))
            self.diccionario['alturaMediaLibre'] = self.alturaMediaLibre.GetValue()

    def OnOtroCuadro(self, event):
        """
        Metodo: OnOtroCuadro

        ARGUMENTOS:
                 event:
        """
        if self.diccionario['otroCuadro'] != self.otroCuadro.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'otroCuadro', copy.deepcopy(self.diccionario['otroCuadro'])))
            self.diccionario['otroCuadro'] = self.otroCuadro.GetValue()
        self.parent.parent.panelDatosAdministrativos.otroCuadro.SetValue(self.otroCuadro.GetValue())

    def OnMasaParticiones(self, event):
        """
        Metodo: OnMasaParticiones

        ARGUMENTOS:
                event:
        """
        if self.diccionario['masaParticiones'] != self.masaParticiones.GetSelection():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'masaParticiones', copy.deepcopy(self.diccionario['masaParticiones'])))
            self.diccionario['masaParticiones'] = self.masaParticiones.GetSelection()

    def OnTipoEdificioChoice(self, event):
        """
        Metodo: OnTipoEdificioChoice

        ARGUMENTOS:
                event:
        """
        if self.diccionario['tipoEdificioChoice'] != self.tipoEdificioChoice.GetSelection():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'tipoEdificioChoice', copy.deepcopy(self.diccionario['tipoEdificioChoice'])))
            self.diccionario['tipoEdificioChoice'] = self.tipoEdificioChoice.GetSelection()
        self.OnActualizarArraysEnvolvente(None)
        self.OnActualizarArraysInstalaciones(None)
        return

    def OnAnoConstruccionChoice(self, event):
        """
        Metodo: OnAnoConstruccionChoice

        ARGUMENTOS:
                event:
        """
        if self.diccionario['anoConstruccionChoice'] != self.anoConstruccionChoice.GetSelection():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'anoConstruccionChoice', copy.deepcopy(self.diccionario['anoConstruccionChoice'])))
            self.diccionario['anoConstruccionChoice'] = self.anoConstruccionChoice.GetSelection()
        self.OnActualizarArraysEnvolvente(None)
        self.OnActualizarEstanqueidadHuecos()
        return

    def OnCambioSuperficie(self, event):
        """
        Metodo: OnCambioSuperficie

        ARGUMENTOS:
                 event:
        """
        if self.diccionario['superficie'] != self.superficie.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'superficie', copy.deepcopy(self.diccionario['superficie'])))
            self.diccionario['superficie'] = self.superficie.GetValue()

    def OnCambioSuperficie2(self, event):
        """
        Metodo: OnCambioSuperficie2

        ARGUMENTOS:
                 event:
        """
        superficie = self.superficie.GetValue()
        if ',' in superficie:
            superficie = superficie.replace(',', '.')
            self.superficie.SetValue(superficie)
        error = ''
        error = Comprueba(self.superficie.GetValue(), 2, error, 'error en superficie', 0).ErrorDevuelto
        if error != '':
            wx.MessageBox(_('Revise el valor de la superficie útil habitable indicada'), _('Aviso'))
            return
        else:
            superficie = float(self.superficie.GetValue())
            superficieZonas = 0.0
            for i in self.parent.subgrupos:
                if i.raiz == 'Edificio Objeto':
                    superficieZonas += float(i.superficie)

            if superficieZonas > superficie:
                wx.MessageBox(_('Las zonas definidas ocupan una superficie de ') + str(superficieZonas) + _('m2 y es mayor que la superficie útil habitable indicada.\nSi desea indicar un valor menor de superficie útil habitable, revise las zonas indicadas.'), _('Aviso'))
                self.superficie.SetValue(str(superficieZonas))
                return
            boolExistenInstColgandoDeZonaElimOModifEnConjuntosMM = existenInstalacionesColgandoDeZonaModificadaOEliminadaEnConjuntosMM(listadoConjuntosMM=self.parent.parent.listadoConjuntosMMUsuario, subgrupoModifOElim='Edificio Objeto')
            if boolExistenInstColgandoDeZonaElimOModifEnConjuntosMM == True:
                mensaje = _('Al modificar la superficie útil habitable se actualizan las superficies cubiertas por las instalaciones.\nRevise las instalaciones del edificio y las medidas de mejora de instalaciones definidas.')
            else:
                mensaje = _('Al modificar la superficie útil habitable se actualizan las superficies cubiertas por las instalaciones.\nRevise dichos valores.')
            if self.parent.parent.panelInstalaciones.ACS != [] or self.parent.parent.panelInstalaciones.calefaccion != [] or self.parent.parent.panelInstalaciones.refrigeracion != [] or self.parent.parent.panelInstalaciones.climatizacion != [] or self.parent.parent.panelInstalaciones.mixto2 != [] or self.parent.parent.panelInstalaciones.mixto3 != []:
                wx.MessageBox(mensaje, _('Aviso'))
                listadoInstalacionesSuperficiesInicial = [
                 self.parent.parent.panelInstalaciones.ACS,
                 self.parent.parent.panelInstalaciones.calefaccion,
                 self.parent.parent.panelInstalaciones.refrigeracion,
                 self.parent.parent.panelInstalaciones.climatizacion,
                 self.parent.parent.panelInstalaciones.mixto2,
                 self.parent.parent.panelInstalaciones.mixto3]
                listadoInstalacionesSuperficies = calculoSuperficies.actualizarSuperficiesInstalaciones(listadoInstalaciones=listadoInstalacionesSuperficiesInicial, superficieCambiada=self.superficie.GetValue(), zonaCambiada='Edificio Objeto')
                self.parent.parent.panelInstalaciones.ACS = listadoInstalacionesSuperficies[0]
                self.parent.parent.panelInstalaciones.calefaccion = listadoInstalacionesSuperficies[1]
                self.parent.parent.panelInstalaciones.refrigeracion = listadoInstalacionesSuperficies[2]
                self.parent.parent.panelInstalaciones.climatizacion = listadoInstalacionesSuperficies[3]
                self.parent.parent.panelInstalaciones.mixto2 = listadoInstalacionesSuperficies[4]
                self.parent.parent.panelInstalaciones.mixto3 = listadoInstalacionesSuperficies[5]
            if boolExistenInstColgandoDeZonaElimOModifEnConjuntosMM == True:
                self.parent.parent.listadoConjuntosMMUsuario = actualizarCoberturaDeConjuntosMM(listadoConjuntosMM=self.parent.parent.listadoConjuntosMMUsuario, superficieCambiada=self.superficie.GetValue(), zonaCambiada='Edificio Objeto')
            if self.parent.parent.programa == 'GranTerciario':
                self.parent.parent.panelInstalaciones.iluminacion = calculoSuperficies.actualizarSuperficiesIluminacion(self.parent.subgrupos, self.superficie.GetValue(), self.parent.parent.panelInstalaciones.iluminacion)
                if boolExistenInstColgandoDeZonaElimOModifEnConjuntosMM == True:
                    self.parent.parent.listadoConjuntosMMUsuario = actualizarSuperficieIluminacionDeConjuntosMM(listadoConjuntosMM=self.parent.parent.listadoConjuntosMMUsuario, listadoSubgrupos=self.parent.subgrupos, superficieHabitable=self.superficie.GetValue())
            if self.parent.parent.panelInstalaciones.panel2.tipoSistema == 'ACS':
                self.parent.parent.panelInstalaciones.panel2.OnCoberturaPorcentaje(None)
            elif self.parent.parent.panelInstalaciones.panel2.tipoSistema == 'calefaccion':
                self.parent.parent.panelInstalaciones.panel2.OnCoberturaPorcentaje(None)
            elif self.parent.parent.panelInstalaciones.panel2.tipoSistema == 'refrigeracion':
                self.parent.parent.panelInstalaciones.panel2.OnCoberturaPorcentaje(None)
            elif self.parent.parent.panelInstalaciones.panel2.tipoSistema == 'climatizacion':
                self.parent.parent.panelInstalaciones.panel2.OnCoberturaPorcentaje(None)
                self.parent.parent.panelInstalaciones.panel2.OnCoberturaPorcentaje2(None)
            elif self.parent.parent.panelInstalaciones.panel2.tipoSistema == 'mixto2':
                self.parent.parent.panelInstalaciones.panel2.OnCoberturaPorcentaje(None)
                self.parent.parent.panelInstalaciones.panel2.OnCoberturaPorcentaje2(None)
            elif self.parent.parent.panelInstalaciones.panel2.tipoSistema == 'mixto3':
                self.parent.parent.panelInstalaciones.panel2.OnCoberturaPorcentaje(None)
                self.parent.parent.panelInstalaciones.panel2.OnCoberturaPorcentaje2(None)
                self.parent.parent.panelInstalaciones.panel2.OnCoberturaPorcentaje3(None)
            elif self.parent.parent.panelInstalaciones.panel2.tipoSistema == 'iluminacion':
                self.parent.parent.panelInstalaciones.panel2.onSeleccionarSubgrupo(None)
            try:
                self.parent.parent.panelInstalaciones.vistaClasica.cargaVista()
            except:
                logging.info('Excepcion en: %s' % __name__)

            self.OnCambioSuperficie(None)
            return

    def PILToWX(self, image):
        """convert a PIL image to a wxImage
        """
        if image.mode != 'RGB':
            image = image.convert('RGB')
        imageData = image.tostring('raw', 'RGB')
        imageWx = wx.EmptyImage(image.size[0], image.size[1])
        imageWx.SetData(imageData)
        return imageWx

    def cargaImagenGuardadaString(self, imagenString, imagenSituacion):
        """
        Metodo: carga la imagen guardada desde un string

        ARGUMENTOS:
                imagenString: 
        """
        try:
            if imagenString != '':
                pilImage = Image.open(StringIO.StringIO(base64.b64decode(imagenString)))
                tamanoImagen = pilImage.size
                tamanoDisponible = (278, 278)
                factorAjuste = 1.0
                if float(tamanoDisponible[0]) / float(tamanoImagen[0]) <= float(tamanoDisponible[1]) / float(tamanoImagen[1]):
                    factorAjuste = float(tamanoDisponible[0]) / float(tamanoImagen[0])
                else:
                    factorAjuste = float(tamanoDisponible[1]) / float(tamanoImagen[1])
                pilImage = pilImage.resize((int(tamanoImagen[0] * factorAjuste), int(tamanoImagen[1] * factorAjuste)))
                bmp = wx.Image(Directorio + '/Imagenes/Fotos_Materiales/blanco.bmp')
                imagenSituacion.SetBitmap(wx.EmptyBitmap(400, 350))
                bmp = bmp.Scale(400, 350, wx.IMAGE_QUALITY_HIGH)
                imagenSituacion.SetBitmap(wx.BitmapFromImage(bmp))
                imagenSituacion.Refresh()
                bmp = self.PILToWX(pilImage).ConvertToBitmap()
                imagenSituacion.SetBitmap(bmp)
                imagenSituacion.Refresh()
            else:
                bmp = wx.Image(Directorio + '/Imagenes/Fotos_Materiales/blanco.bmp')
                imagenSituacion.SetBitmap(wx.EmptyBitmap(400, 350))
                bmp = bmp.Scale(400, 350, wx.IMAGE_QUALITY_HIGH)
                imagenSituacion.SetBitmap(wx.BitmapFromImage(bmp))
        except:
            logging.info('Excepcion en: %s' % __name__)
            bmp = wx.Image(Directorio + '/Imagenes/Fotos_Materiales/blanco.bmp')
            imagenSituacion.SetBitmap(wx.EmptyBitmap(400, 350))
            bmp = bmp.Scale(400, 350, wx.IMAGE_QUALITY_HIGH)
            imagenSituacion.SetBitmap(wx.BitmapFromImage(bmp))

    def onImagenButton(self, event):
        """
        Metodo: onImagenButton

        ARGUMENTOS:
                event:
        """
        tipoArchivo = 'All files (*.*)|*.*'
        dlg = wx.FileDialog(self, message='Seleccione una imagen del edificio', defaultDir=Directorio + '/Imagenes', style=wx.FD_MULTIPLE, wildcard=tipoArchivo)
        if dlg.ShowModal() == wx.ID_OK:
            imageFile = dlg.GetPath()
            self.imagenString = trataImagenes.trataImagen(imageFile)
            self.cargaImagenGuardadaString(self.imagenString, self.imagen)

    def onPlanoButton(self, event):
        """
        Metodo: onPlanoButton

        ARGUMENTOS:
                event:
        """
        tipoArchivo = 'All files (*.*)|*.*'
        dlg = wx.FileDialog(self, message=b'Seleccione el plano de situaci\xf3n del edificio', defaultDir=Directorio + '/Imagenes', style=wx.FD_MULTIPLE, wildcard=tipoArchivo)
        if dlg.ShowModal() == wx.ID_OK:
            imageFile = dlg.GetPath()
            self.planoString = trataImagenes.trataImagen(imageFile)
            self.cargaImagenGuardadaString(self.planoString, self.plano)

    def onNormativaHelpButton(self, event):
        """
        Metodo: onNormativaHelpButton

        ARGUMENTOS:
                event:
        """
        annoConstr = self.anoConstruccionNumeroCuadro.GetValue()
        ayuda = ayudaNormativaVigente.Dialog1(self, annoConstr)
        ayuda.ShowModal()
        if ayuda.dev != False:
            if ayuda.dev[0] == True:
                self.anoConstruccionChoice.SetSelection(0)
            elif ayuda.dev[1] == True:
                self.anoConstruccionChoice.SetSelection(1)
            else:
                if ayuda.dev[2] == True:
                    self.anoConstruccionChoice.SetSelection(2)
                else:
                    self.anoConstruccionChoice.SetSelection(3)
        self.OnActualizarArraysEnvolvente(None)
        return

    def OnHE1(self, event):
        """
        Metodo: OnHE1

        ARGUMENTOS:
                event:
        """
        if self.diccionario['he1'] != self.HE1.GetSelection():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'he1', copy.deepcopy(self.diccionario['he1'])))
            self.diccionario['he1'] = self.HE1.GetSelection()
        nombreCiudadRepresentativa, zonaHE1CiudadRepresentativa, zonaNBECiudadRepresentativa, zonaHE4CiudadRepresentativa = Localizacion().getCiudadRepresentativa(self.HE1.GetStringSelection())
        self.HE4.SetStringSelection(zonaHE4CiudadRepresentativa)
        self.NBE = zonaNBECiudadRepresentativa
        self.OnActualizarArraysEnvolvente(None)
        self.OnActualizarArraysInstalaciones(None)
        return

    def OnHE4(self, event):
        """
        Metodo: OnHE4

        ARGUMENTOS:
                event:
        """
        if self.diccionario['he4'] != self.HE4.GetSelection():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'he4', copy.deepcopy(self.diccionario['he4'])))
            self.diccionario['he4'] = self.HE4.GetSelection()

    def OnProvinciaChoice(self, event):
        """
        Metodo: OnProvinciaChoice

        ARGUMENTOS:
                event:
        """
        if self.diccionario['provinciaChoice'] != self.provinciaChoice.GetSelection():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'provinciaChoice', copy.deepcopy(self.diccionario['provinciaChoice'])))
            self.diccionario['provinciaChoice'] = self.provinciaChoice.GetSelection()
        listadoCiudades = []
        listadoCiudades = Localizacion().getLocalidadesDeProvincia(self.provinciaChoice.GetStringSelection())
        self.localidadChoice.SetItems(listadoCiudades)
        self.otroCuadro.Show(False)
        if self.provinciaChoice.GetStringSelection() == 'Ceuta' or self.provinciaChoice.GetStringSelection() == 'Melilla' or self.provinciaChoice.GetStringSelection() == 'Illes Balears' or self.provinciaChoice.GetStringSelection() == 'Las Palmas' or self.provinciaChoice.GetStringSelection() == 'Santa Cruz de Tenerife':
            self.Extrapeninsular.SetValue(True)
            self.HE1.SetItems(listadosWeb.listadoZonaHE1_extrapeninsular)
        else:
            self.HE1.SetItems(listadosWeb.listadoZonaHE1_peninsular)
            self.Extrapeninsular.SetValue(False)
        self.HE1.Enable(False)
        self.HE1.SetSelection(-1)
        self.HE4.Enable(False)
        self.HE4.SetSelection(-1)
        self.parent.parent.panelDatosAdministrativos.provinciaChoice.SetStringSelection(self.provinciaChoice.GetStringSelection())
        self.parent.parent.panelDatosAdministrativos.OnProvinciaChoiceRecargar()
        self.recalcularPatronesSombra()

    def OnProvinciaChoiceRecargar(self):
        """
        Metodo: OnProvinciaChoiceRecargar

        """
        listadoCiudades = []
        listadoCiudades = Localizacion().getLocalidadesDeProvincia(self.provinciaChoice.GetStringSelection())
        self.localidadChoice.SetItems(listadoCiudades)
        self.otroCuadro.Show(False)
        if self.provinciaChoice.GetStringSelection() == 'Ceuta' or self.provinciaChoice.GetStringSelection() == 'Melilla' or self.provinciaChoice.GetStringSelection() == 'Illes Balears' or self.provinciaChoice.GetStringSelection() == 'Las Palmas' or self.provinciaChoice.GetStringSelection() == 'Santa Cruz de Tenerife':
            self.Extrapeninsular.SetValue(True)
            self.HE1.SetItems(listadosWeb.listadoZonaHE1_extrapeninsular)
        else:
            self.HE1.SetItems(listadosWeb.listadoZonaHE1_peninsular)
            self.Extrapeninsular.SetValue(False)
        self.HE1.Enable(False)
        self.HE1.SetSelection(-1)
        self.HE4.Enable(False)
        self.HE4.SetSelection(-1)
        self.recalcularPatronesSombra()

    def OnLocalidadChoice(self, event):
        """
        Metodo: OnLocalidadChoice

        ARGUMENTOS:
                 event:
        """
        if self.diccionario['choice1'] != self.localidadChoice.GetSelection():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'choice1', copy.deepcopy(self.diccionario['choice1'])))
            self.diccionario['choice1'] = self.localidadChoice.GetSelection()
        if self.localidadChoice.GetStringSelection() != 'Otro':
            i = Localizacion().getPosicionProvincias(self.provinciaChoice.GetStringSelection())
            j = self.localidadChoice.GetSelection()
            self.HE1.SetStringSelection(Localizacion().getHE1correspondiente(i, j))
            self.HE4.SetStringSelection(Localizacion().getHE4correspondiente(i, j))
            self.NBE = Localizacion().getNBEcorrespondiente(i, j)
            self.otroCuadro.Show(False)
            self.HE1.Enable(False)
            self.HE4.Enable(False)
        else:
            self.otroCuadro.Show(True)
            self.HE1.Enable(True)
            self.HE4.Enable(True)
            i = Localizacion().getPosicionProvincias(self.provinciaChoice.GetStringSelection())
            j = 0
            self.HE1.SetStringSelection(Localizacion().getHE1correspondiente(i, j))
            self.HE4.SetStringSelection(Localizacion().getHE4correspondiente(i, j))
            nombreCiudadRepresentativa, zonaHE1CiudadRepresentativa, zonaNBECiudadRepresentativa, zonaHE4CiudadRepresentativa = Localizacion().getCiudadRepresentativa(self.HE1.GetStringSelection())
            self.NBE = zonaNBECiudadRepresentativa
        self.OnActualizarArraysEnvolvente(None)
        self.OnActualizarArraysInstalaciones(None)
        self.parent.parent.panelDatosAdministrativos.localidadChoice.SetStringSelection(self.localidadChoice.GetStringSelection())
        self.parent.parent.panelDatosAdministrativos.OnLocalidadChoiceRecargar()
        return

    def OnLocalidadChoiceRecargar(self):
        """
        Metodo: OnLocalidadChoiceRecargar
        """
        if self.diccionario['choice1'] != self.localidadChoice.GetSelection():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'choice1', copy.deepcopy(self.diccionario['choice1'])))
            self.diccionario['choice1'] = self.localidadChoice.GetSelection()
        if self.localidadChoice.GetStringSelection() != 'Otro':
            i = Localizacion().getPosicionProvincias(self.provinciaChoice.GetStringSelection())
            j = self.localidadChoice.GetSelection()
            self.HE1.SetStringSelection(Localizacion().getHE1correspondiente(i, j))
            self.HE4.SetStringSelection(Localizacion().getHE4correspondiente(i, j))
            self.NBE = Localizacion().getNBEcorrespondiente(i, j)
            self.otroCuadro.Show(False)
            self.HE1.Enable(False)
            self.HE4.Enable(False)
        else:
            self.otroCuadro.Show(True)
            self.HE1.Enable(True)
            self.HE4.Enable(True)
            i = Localizacion().getPosicionProvincias(self.provinciaChoice.GetStringSelection())
            j = 0
            self.HE1.SetStringSelection(Localizacion().getHE1correspondiente(i, j))
            self.HE4.SetStringSelection(Localizacion().getHE4correspondiente(i, j))
            nombreCiudadRepresentativa, zonaHE1CiudadRepresentativa, zonaNBECiudadRepresentativa, zonaHE4CiudadRepresentativa = Localizacion().getCiudadRepresentativa(self.HE1.GetStringSelection())
            self.NBE = zonaNBECiudadRepresentativa
        self.OnActualizarArraysEnvolvente(None)
        self.OnActualizarArraysInstalaciones(None)
        return

    def exportarDatos(self):
        """
        Metodo: exportarDatos

        """
        listaErrores = ''
        superficie = self.superficie.GetValue()
        altura = self.alturaMediaLibre.GetValue()
        numeroPlantas = self.numeroPlantas.GetValue()
        ventilacion = self.ventilacion.GetValue()
        consumoACS = self.consumoACS.GetValue()
        Q50Cuadro = self.Q50Cuadro.GetValue()
        NCuadro = self.NCuadro.GetValue()
        if ',' in superficie:
            superficie = superficie.replace(',', '.')
            self.superficie.SetValue(superficie)
        if ',' in altura:
            altura = altura.replace(',', '.')
            self.alturaMediaLibre.SetValue(altura)
        if ',' in numeroPlantas:
            numeroPlantas = numeroPlantas.replace(',', '.')
            self.numeroPlantas.SetValue(numeroPlantas)
        if ',' in ventilacion:
            ventilacion = ventilacion.replace(',', '.')
            self.ventilacion.SetValue(ventilacion)
        if ',' in consumoACS:
            consumoACS = consumoACS.replace(',', '.')
            self.consumoACS.SetValue(consumoACS)
        if ',' in Q50Cuadro:
            Q50Cuadro = Q50Cuadro.replace(',', '.')
            self.Q50Cuadro.SetValue(Q50Cuadro)
        if ',' in NCuadro:
            NCuadro = NCuadro.replace(',', '.')
            self.NCuadro.SetValue(NCuadro)
        listaErrores += Comprueba(self.anoConstruccionChoice.GetStringSelection(), 0, listaErrores, _('normativa vigente')).ErrorDevuelto
        listaErrores += Comprueba(self.anoConstruccionNumeroCuadro.GetValue(), 2, listaErrores, _('año de construcción del edificio'), 0).ErrorDevuelto
        if self.parent.parent.programa == 'Residencial':
            listaErrores += Comprueba(self.tipoEdificioChoice.GetStringSelection(), 0, listaErrores, _('tipo de edificio')).ErrorDevuelto
        else:
            listaErrores += Comprueba(self.tipoEdificioChoice.GetStringSelection(), 0, listaErrores, _('perfil de uso')).ErrorDevuelto
            listaErrores += Comprueba(self.tipoEdificioTerciarioChoice.GetStringSelection(), 0, listaErrores, _('tipo de edificio')).ErrorDevuelto
        listaErrores += Comprueba(self.provinciaChoice.GetStringSelection(), 0, listaErrores, _('provincia')).ErrorDevuelto
        listaErrores += Comprueba(self.localidadChoice.GetStringSelection(), 0, listaErrores, _('localidad')).ErrorDevuelto
        listaErrores += Comprueba(self.superficie.GetValue(), 2, listaErrores, _('superficie útil habitable'), 0).ErrorDevuelto
        listaErrores += Comprueba(self.alturaMediaLibre.GetValue(), 2, listaErrores, _('altura libre de planta'), 0).ErrorDevuelto
        listaErrores += Comprueba(self.ventilacion.GetValue(), 2, listaErrores, _('ventilacion del inmueble'), 0).ErrorDevuelto
        listaErrores += Comprueba(self.numeroPlantas.GetValue(), 2, listaErrores, _('número de plantas habitables'), 0).ErrorDevuelto
        if self.parent.parent.programa != 'Residencial':
            listaErrores += Comprueba2(self.consumoACS.GetValue(), 2, listaErrores, _('consumo de ACS'), 0).ErrorDevuelto
        else:
            listaErrores += Comprueba(self.consumoACS.GetValue(), 2, listaErrores, _('consumo de ACS'), 0).ErrorDevuelto
        listaErrores += Comprueba(self.masaParticiones.GetStringSelection(), 0, listaErrores, _('masa de las particiones')).ErrorDevuelto
        if self.BlowerDoorCheck.GetValue() == True:
            listaErrores += Comprueba(self.Q50Cuadro.GetValue(), 2, listaErrores, _('ensayo Blower Door Test: q50'), 0).ErrorDevuelto
            listaErrores += Comprueba(self.NCuadro.GetValue(), 2, listaErrores, _('ensayo Blower Door Test: n'), 0).ErrorDevuelto
        if listaErrores != '':
            wx.MessageBox(_('Revise los siguientes campos de la pestaña de Datos Generales:\n') + listaErrores, _('Aviso'))
            datosPanelDatosGenerales = []
            return datosPanelDatosGenerales
        datosPanelDatosGenerales = self.cogerDatos()
        return datosPanelDatosGenerales

    def comprobarPlanoEIMagenEdificio(self):
        """
        Metodo: exportarDatos

        """
        listaErrores = ''
        if self.planoString == '' and self.imagenString == '':
            wx.MessageBox(_('Cargue una imagen del edificio y el plano de situación en la pestaña de Datos Generales'), _('Aviso'))
            return 'falta plano e imagen'
        if self.imagenString == '':
            wx.MessageBox(_('Cargue una imagen del edificio en la pestaña de Datos Generales'), _('Aviso'))
            return 'falta imagen'
        if self.planoString == '':
            wx.MessageBox(_('Cargue el plano de situación del edificio en la pestaña de Datos Generales'), _('Aviso'))
            return 'falta plano'
        return ''

    def OnBlowerDoorCheck(self, event):
        """
        Metodo: OnBlowerDoorCheck

        ARGUMENTOS:
                 event:
        """
        if self.diccionario['BlowerDoorCheck'] != self.BlowerDoorCheck.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'BlowerDoorCheck', copy.deepcopy(self.diccionario['BlowerDoorCheck'])))
            self.diccionario['BlowerDoorCheck'] = self.BlowerDoorCheck.GetValue()
        if self.BlowerDoorCheck.GetValue() == True:
            self.Q50Text.Show(True)
            self.Q50Cuadro.Show(True)
            self.Q50Unidades.Show(True)
            self.NText.Show(True)
            self.NCuadro.Show(True)
            self.BDTText.Show(True)
        else:
            self.Q50Text.Show(False)
            self.Q50Cuadro.Show(False)
            self.Q50Unidades.Show(False)
            self.NText.Show(False)
            self.NCuadro.Show(False)
            self.BDTText.Show(False)

    def __init__(self, parent, id, pos, size, style, name):
        """
        Constructor de la clase

        ARGUMENTOS:
                 parent:
                 id:
                 pos:
                 size:
                 style:
                 name:
        """
        self.parent = parent
        self.NBE = ''
        self._init_ctrls(parent, id, pos, size, style, name)
        self.nombre = _('Datos generales')
        self.imagenString = ''
        self.planoString = ''
        self.actualizaDiccionario()
        self.parent.parent.panelDatosAdministrativos.provinciaChoice.SetItems(Localizacion().getListadoProvincias())

    def cogerDatos(self):
        """
        Metodo: cogerDatos

        """
        datos = []
        datos.append(self.anoConstruccionChoice.GetStringSelection())
        datos.append(self.tipoEdificioChoice.GetStringSelection())
        datos.append(self.provinciaChoice.GetStringSelection())
        datos.append(self.localidadChoice.GetStringSelection())
        datos.append(self.HE1.GetStringSelection())
        datos.append(self.HE4.GetStringSelection())
        datos.append(self.superficie.GetValue())
        datos.append(self.alturaMediaLibre.GetValue())
        datos.append(self.numeroPlantas.GetValue())
        datos.append(self.consumoACS.GetValue())
        datos.append(self.masaParticiones.GetStringSelection())
        datos.append(self.Extrapeninsular.GetValue())
        datos.append(self.otroCuadro.GetValue())
        datos.append([self.BlowerDoorCheck.GetValue(), self.Q50Cuadro.GetValue(), self.NCuadro.GetValue()])
        datos.append(self.ExentoHE4.GetValue())
        datos.append(self.NBE)
        datos.append(self.ventilacion.GetValue())
        datos.append(self.imagenString)
        datos.append(self.planoString)
        datos.append(self.anoConstruccionNumeroCuadro.GetValue())
        datos.append(self.tipoEdificioTerciarioChoice.GetStringSelection())
        return datos

    def cargarDatos(self, datos):
        """
        Metodo: cargarDatos

        ARGUMENTOS:
                datos:
        """
        if datos[0] == '':
            self.anoConstruccionChoice.SetSelection(-1)
        else:
            self.anoConstruccionChoice.SetStringSelection(datos[0])
        if datos[1] == '':
            self.tipoEdificioChoice.SetSelection(-1)
        else:
            try:
                self.tipoEdificioChoice.SetStringSelection(datos[1])
            except:
                logging.info('Excepcion en: %s' % __name__)

            if datos[2] == '':
                self.provinciaChoice.SetSelection(-1)
            else:
                self.provinciaChoice.SetStringSelection(datos[2])
                self.OnProvinciaChoiceRecargar()
            if datos[3] == '':
                self.localidadChoice.SetSelection(-1)
            else:
                self.localidadChoice.SetStringSelection(datos[3])
            if datos[3] == 'Otro':
                self.otroCuadro.SetValue(datos[12])
                self.otroCuadro.Show(True)
                self.HE1.Enable(True)
                self.HE4.Enable(True)
            else:
                self.otroCuadro.Show(False)
                self.HE1.Enable(False)
                self.HE4.Enable(False)
            if datos[4] == '':
                self.HE1.SetSelection(-1)
            else:
                self.HE1.SetStringSelection(datos[4])
            if datos[5] == '':
                self.HE4.SetSelection(-1)
            else:
                self.HE4.SetStringSelection(datos[5])
            superficie = datos[6]
            altura = datos[7]
            self.superficie.SetValue(superficie)
            self.alturaMediaLibre.SetValue(altura)
            self.numeroPlantas.SetValue(datos[8])
            consumoACS = datos[9]
            if self.parent.parent.versionArchivoGuardado < 1.9 and self.parent.parent.programa == 'Residencial':
                consumoACS = '%s' % getValorDdaACSVersionesAnteriores(versionArchivoGuardado=self.parent.parent.versionArchivoGuardado, programa=self.parent.parent.programa, tipoEdificio=datos[1], superficie=superficie)
            self.consumoACS.SetValue(consumoACS)
            if datos[10] == '':
                self.masaParticiones.SetSelection(-1)
            else:
                self.masaParticiones.SetStringSelection(datos[10])
            self.Extrapeninsular.SetValue(datos[11])
            self.BlowerDoorCheck.SetValue(datos[13][0])
            self.Q50Cuadro.SetValue(datos[13][1])
            self.NCuadro.SetValue(datos[13][2])
            self.OnBlowerDoorCheck(None)
            self.ExentoHE4.SetValue(datos[14])
            self.NBE = datos[15]
            try:
                float(datos[16])
                valorVentilacion = datos[16]
            except:
                logging.info('Excepcion en: %s' % __name__)
                valorVentilacion = '%s' % getValorVentilacionNoGuardado(versionArchivoGuardado=self.parent.parent.versionArchivoGuardado, programa=self.parent.parent.programa, altura=altura)

        self.ventilacion.SetValue(valorVentilacion)
        self.imagenString = datos[17]
        self.planoString = datos[18]
        self.anoConstruccionNumeroCuadro.SetValue(datos[19])
        if datos[20] == '':
            self.tipoEdificioTerciarioChoice.SetSelection(-1)
        else:
            self.tipoEdificioTerciarioChoice.SetStringSelection(datos[20])
        self.cargaImagenGuardadaString(self.imagenString, self.imagen)
        self.cargaImagenGuardadaString(self.planoString, self.plano)
        self.actualizaDiccionario()
        return

    def OnActualizarEstanqueidadHuecos(self):
        """
        Metodo: OnActualizarEstanqueidadHuecos

        """
        seleccionadoHueco = self.parent.parent.panelEnvolvente.panelElegirObjeto.definirHueco.GetValue()
        if seleccionadoHueco == True:
            selecAnterior = self.parent.parent.panelEnvolvente.panel2.permeabilidadAireChoice.GetStringSelection()
            if self.anoConstruccionChoice.GetSelection() == 2 or self.anoConstruccionChoice.GetSelection() == 3:
                listadoEstanqueidad = listadosWeb.listadoOpcionesEstanqueidadCTE
                self.parent.parent.panelEnvolvente.panel2.permeabilidadAireChoice.SetItems(listadoEstanqueidad)
                if selecAnterior == 'Poco estanco':
                    self.parent.parent.panelEnvolvente.panel2.permeabilidadAireChoice.SetStringSelection('Valor conocido')
                self.parent.parent.panelEnvolvente.panel2.OnPermeabilidadAireChoice(None)
            else:
                listadoEstanqueidad = listadosWeb.listadoOpcionesEstanqueidad
                self.parent.parent.panelEnvolvente.panel2.permeabilidadAireChoice.SetItems(listadoEstanqueidad)
                self.parent.parent.panelEnvolvente.panel2.permeabilidadAireChoice.SetStringSelection(selecAnterior)
                self.parent.parent.panelEnvolvente.panel2.OnPermeabilidadAireChoice(None)
        return

    def OnActualizarArraysEnvolvente(self, event):
        """
        Metodo: OnActualizarArraysEnvolvente

        ARGUMENTOS:
                event:
        """
        self.parent.parent.panelEnvolvente.cerramientos = actualizarEnvolvente(listadoCerramientos=self.parent.parent.panelEnvolvente.cerramientos, normativaVigente=self.anoConstruccionChoice.GetSelection(), zonaHE1=self.HE1.GetStringSelection(), zonaNBE=self.NBE)
        try:
            self.parent.parent.panelEnvolvente.panel2.calcularCaracteristicasCerramiento(None)
        except:
            logging.info('Excepcion en: %s' % __name__)

        try:
            self.parent.parent.panelEnvolvente.vistaClasica.cargaCerramientos()
        except:
            logging.info('Excepcion en: %s' % __name__)

        return

    def OnActualizarArraysInstalaciones(self, event):
        """
        Metodo: OnActualizarArraysInstalaciones

        ARGUMENTOS:
                event:
        """
        zonaHE1 = self.HE1.GetStringSelection()
        programa = self.parent.parent.programa
        if self.parent.parent.programa == 'Residencial':
            uso = 'Residencial'
        else:
            uso = self.tipoEdificioChoice.GetStringSelection()
        self.parent.parent.panelInstalaciones.ACS, self.parent.parent.panelInstalaciones.calefaccion, self.parent.parent.panelInstalaciones.refrigeracion, self.parent.parent.panelInstalaciones.climatizacion, self.parent.parent.panelInstalaciones.mixto2, self.parent.parent.panelInstalaciones.mixto3 = actualizarInstalacionesGeneracion(instACS=self.parent.parent.panelInstalaciones.ACS, instCal=self.parent.parent.panelInstalaciones.calefaccion, instRef=self.parent.parent.panelInstalaciones.refrigeracion, instClima=self.parent.parent.panelInstalaciones.climatizacion, instMixto2=self.parent.parent.panelInstalaciones.mixto2, instMixto3=self.parent.parent.panelInstalaciones.mixto3, zonaHE1=zonaHE1, programa=programa, tipoEdificio=uso)
        self.parent.parent.listadoConjuntosMMUsuario = actualizarRendimientoConjuntosMM(listadoConjuntosMM=self.parent.parent.listadoConjuntosMMUsuario, zonaHE1=zonaHE1, programa=programa, tipoEdificio=uso)
        try:
            self.parent.parent.panelInstalaciones.panel2.obtenerRendimientoEstacional(None)
        except:
            logging.info('Excepcion en: %s' % __name__)

        try:
            self.parent.parent.panelInstalaciones.vistaClasica.cargaVista()
        except:
            logging.info('Excepcion en: %s' % __name__)

        return

    def actualizaDiccionario(self):
        """
        Metodo: actualizaDiccionario

        """
        self.diccionario = {}
        self.diccionario['anoConstruccionChoice'] = self.anoConstruccionChoice.GetSelection()
        self.diccionario['provinciaChoice'] = self.provinciaChoice.GetSelection()
        self.diccionario['tipoEdificioChoice'] = self.tipoEdificioChoice.GetSelection()
        self.diccionario['choice1'] = self.localidadChoice.GetSelection()
        self.diccionario['he1'] = self.HE1.GetSelection()
        self.diccionario['he4'] = self.HE4.GetSelection()
        self.diccionario['masaParticiones'] = self.masaParticiones.GetSelection()
        self.diccionario['BlowerDoorCheck'] = self.BlowerDoorCheck.GetValue()
        self.diccionario['Extrapeninsular'] = self.Extrapeninsular.GetValue()
        self.diccionario['ExentoHE4'] = self.ExentoHE4.GetValue()
        self.diccionario['superficie'] = self.superficie.GetValue()
        self.diccionario['alturaMediaLibre'] = self.alturaMediaLibre.GetValue()
        self.diccionario['numeroPlantas'] = self.numeroPlantas.GetValue()
        self.diccionario['ventilacion'] = self.ventilacion.GetValue()
        self.diccionario['consumoACS'] = self.consumoACS.GetValue()
        self.diccionario['Q50Cuadro'] = self.Q50Cuadro.GetValue()
        self.diccionario['otroCuadro'] = self.otroCuadro.GetValue()
        self.diccionario['NCuadro'] = self.NCuadro.GetValue()

    def recalcularPatronesSombra(self):
        """
        Metodo: recalcularPatronesSombra

        """
        for patron in self.parent.parent.datosSombras:
            listaPuntos = patron[1]
            porcentajes = calculoPerdidasSombras.calculoPorcentajesSombras(listaPuntos, self.provinciaChoice.GetStringSelection())
            patron[2] = porcentajes