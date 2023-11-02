# Embedded file name: Instalaciones\panelACS.pyc
"""
Modulo: panelACS.py

"""
from Calculos.funcionesCalculo import rendCombustionDefecto, betaCombDefecto, rendNominalJoule, diccCOPNominalDefecto
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
import math
import wx
import logging
wxID_PANEL1, wxID_PANEL1ACUMULACIONCHECK, wxID_PANEL1COBERTURA, wxID_PANEL1COMBUSTIBLECHOICE, wxID_PANEL1DEFINIRDEMANDARADIO, wxID_PANEL1DEFINIRMETROS2RADIO, wxID_PANEL1DEFINIRTEXT, wxID_PANEL1GENERADORCHOICE, wxID_PANEL1NOMBREINSTALACION, wxID_PANEL1NOMBREINSTALACIONTEXT, wxID_PANEL1RENDIMIENTOCHOICE, wxID_PANEL1RENDIMIENTOTEXT, wxID_PANEL1STATICTEXT1, wxID_PANEL1SUBGRUPOCHOICE, wxID_PANEL1SUBGRUPOTEXT, wxID_PANEL1TEMPALTAUNIDADESTEXT, wxID_PANEL1TEMPERATURAALTA, wxID_PANEL1TEMPERATURAALTATEXT, wxID_PANEL1TEMPERATURABAJA, wxID_PANEL1TEMPERATURABAJATEXT, wxID_PANEL1TIPOCOMBUSTIBLETEXT, wxID_PANEL1TIPOGENERADORTEXT, wxID_PANEL1VALORUACHOICE, wxID_PANEL1VALORUATEXT, wxID_PANEL1VOLUMEN, wxID_PANEL1VOLUMENTEXT, wxID_PANEL1VOLUMENUNIDADESTEXT, wxID_PANEL1CHOICE1, wxID_PANEL1RADIOBUTTON1, wxID_PANEL1ACUMULACIONTEXT, wxID_PANEL1CHOICE2, wxID_PANEL1ESPESORAISTEXT, wxID_PANEL1ESPESORAISLA, wxID_PANEL1ESTADOAISTEXT, wxID_PANEL1AISLANTEBUENORADIO, wxID_PANEL1AISLANTEREGULARRADIO, wxID_PANEL1AISLANTEMALORADIO, wxID_PANEL1TIPOAISTEXT, wxID_PANEL1AISLANTEPORIURETANO, wxID_PANEL1AISLANTERESINA, wxID_PANEL1AISLANTEPOLIURETANOPROYEC, wxID_PANEL1AISLANTEMESPUMA, wxID_PANEL1UATEXT, wxID_PANEL1UAVALOR, wxID_PANEL1ANOCALDERACHOICE, wxID_PANEL1ANOCALDERATEXT, wxID_PANEL1TIPOCALDERATEXT, wxID_PANEL1TIPOCALDERACHOICE, wxID_PANEL1RENDIMIENTOMEDIOTEXT, wxID_PANEL1RENDIMIENTOMEDIO, wxID_PANEL1RENDIMIENTOCOMBUSTEXT, wxID_PANEL1RENDIMIENTOCOMBUSUNITEXT, wxID_PANEL1RENDIMIENTOMCOMBUS, wxID_PANEL1POTENCIANOMINALTEXT, wxID_PANEL1POTENCIANOMINAL, wxID_PANEL1POTENCIANOMINALUNIDADESTEXT, wxID_PANEL1AISLANTECALDERATEXT, wxID_PANEL1AISLANTECALDE, wxID_PANEL1CARGAMEDIATEXT, wxID_PANEL1CARGAMEDIA, wxID_PANEL1TIPOCALDE1RADIO, wxID_PANEL1TIPOCALDE1TEXT, wxID_PANEL1DEFINIRBOTON, wxID_PANEL1RENDGLOBALTEXT, wxID_PANEL1RENDIMIENTOGLOBAL, wxID_PANEL1RENDGLOBALUNITEXT, wxID_PANEL1ANTIEQUIPOTEXT, wxID_PANEL1MENOS5ANOSRADIO, wxID_PANEL1ENTRE515RADIO, wxID_PANEL1AISLANTEMALORADIO, wxID_PANEL1RENDIMIENTONOMINAL, wxID_PANEL1RENDNOMINALUNITEXT, wxID_PANEL1RENDNOMINALTEXT, wxID_PANEL1AISLAMIENTOACUMULACIONCHOICE, wxID_PANEL1CARGAMEDIAHELPBUTTON, wxID_WXVARIOSGENERADORESCHECK, wxID_PANEL1FRACCIONPOTENCIAENTRADA, wxID_PANEL1FRACCIONPOTENCIA, wxID_PANEL1DDACUBIERTABDC, wxID_PANEL1POTNOMINALTEXT, wxID_PANEL1POTNOMINAL, wxID_PANEL1COBERTURAPORCEN, wxID_PANEL1RENDNOMINALPGTEXT, wxID_PANEL1RENDNOMINALPG, wxID_PANEL1FACRTORGARGAMINTEXT, wxID_PANEL1FACRTORGARGAMIN, wxID_PANEL1FACRTORGARGAMAXTEXT, wxID_PANEL1FACRTORGARGAMAX, wxID_PANEL1DEFINIRTEMPERATURASBOTON, wxID_PANEL1DEFINIRCURVABOTON, wxID_PANEL1POTNOMINALUNIDADESTEXT, wxID_PANEL1RENDNOMINALPGUNIDADESTEXT, wxID_PANEL1TEMPAMBINTTEXT, wxID_PANEL1TEMPAMBINT, wxID_PANEL1TEMPAMBINTUNIDADESTEXT, wxID_CARACTERISTICASLINEATEXT, wxID_DEMANDALINEATEXT, wxID_EFICIENCIALINEATEXT, wxID_ACUMULACIONLINEATEXT, wxID_PANEL1ANTIGUEDADCHOICE, wxID_PANEL1DEFINIRTEXT2, wxID_PANEL1MULTIPLICADORTEXT, wxID_PANEL1MULTIPLICADOR = [ wx.NewId() for _init_ctrls in range(103) ]

class Panel1(wx.Panel):
    """
    Clase: Panel1 del modulo panelACS.py
    
    
    """

    def _init_ctrls(self, prnt, id, posi, siz, styles, named):
        """
        Metodo: _init_ctrls
        
        
        ARGUMENTOS:
                prnt:
                id:
                posi:
                siz:
                styles:
                named:
        """
        wx.Panel.__init__(self, id=wxID_PANEL1, name=named, parent=prnt, pos=posi, size=siz, style=styles)
        self.SetBackgroundColour('white')
        self.nombreInstalacionText = wx.StaticText(id=wxID_PANEL1NOMBREINSTALACIONTEXT, label=_(u'Nombre'), name=u'nombreInstalacionText', parent=self, pos=wx.Point(15, 2), size=wx.Size(102, 13), style=0)
        self.nombreInstalacion = wx.TextCtrl(id=wxID_PANEL1NOMBREINSTALACION, name=u'nombreInstalacion', parent=self, pos=wx.Point(170, 0), size=wx.Size(230, 21), style=0, value=_(u'Equipo ACS'))
        self.nombreInstalacion.SetForegroundColour(wx.Colour(100, 200, 0))
        self.nombreInstalacion.Bind(wx.EVT_TEXT, self.OnNombreInstalacion, id=wxID_PANEL1NOMBREINSTALACION)
        self.subgrupoText = wx.StaticText(id=wxID_PANEL1SUBGRUPOTEXT, label=_(u'Zona'), name=u'subgrupoText', parent=self, pos=wx.Point(435, 2), size=wx.Size(50, 13), style=0)
        self.subgrupoChoice = MiChoice(choices=[], id=wxID_PANEL1SUBGRUPOCHOICE, name=u'subgrupoChoice', parent=self, pos=wx.Point(496, 0), size=wx.Size(214, 21), style=0)
        self.subgrupoChoice.Bind(wx.EVT_CHOICE, self.OnsubgrupoChoice, id=wxID_PANEL1SUBGRUPOCHOICE)
        self.CaracteristicasLineaText = wx.StaticBox(id=wxID_CARACTERISTICASLINEATEXT, label=_(u'Caracter\xedsticas'), name='CaracteristicasLineaText', parent=self, pos=wx.Point(0, 26), size=wx.Size(400, 77), style=0)
        self.CaracteristicasLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.tipoGeneradorText = wx.StaticText(id=wxID_PANEL1TIPOGENERADORTEXT, label=_(u'Tipo de generador'), name=u'tipoGeneradorText', parent=self, pos=wx.Point(15, 46), size=wx.Size(89, 13), style=0)
        self.generadorChoice = MiChoice(choices=listadosWeb.listadoInstalaciones, id=wxID_PANEL1GENERADORCHOICE, name=u'generadorChoice', parent=self, pos=wx.Point(170, 44), size=wx.Size(220, 21), style=0)
        self.generadorChoice.SetSelection(0)
        self.generadorChoice.Bind(wx.EVT_CHOICE, self.OngeneradorChoice, id=wxID_PANEL1GENERADORCHOICE)
        self.tipoCombustibleText = wx.StaticText(id=wxID_PANEL1TIPOCOMBUSTIBLETEXT, label=_(u'Tipo de combustible'), name=u'tipoCombustibleText', parent=self, pos=wx.Point(15, 71), size=wx.Size(96, 13), style=0)
        self.combustibleChoice = MiChoice(choices=listadosWeb.listadoCombustibles, id=wxID_PANEL1COMBUSTIBLECHOICE, name=u'combustibleChoice', parent=self, pos=wx.Point(170, 69), size=wx.Size(220, 21), style=0)
        self.combustibleChoice.SetSelection(0)
        self.combustibleChoice.Bind(wx.EVT_CHOICE, self.OnCombustibleChoice, id=wxID_PANEL1COMBUSTIBLECHOICE)
        self.DemandaLineaText = wx.StaticBox(id=wxID_DEMANDALINEATEXT, label=_(u'Demanda cubierta'), name='DemandaLineaText', parent=self, pos=wx.Point(425, 26), size=wx.Size(285, 77), style=0)
        self.DemandaLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.DemandaLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.definirText2 = wx.StaticText(id=wxID_PANEL1DEFINIRTEXT2, label=_(u'ACS'), name=u'definirText', parent=self, pos=wx.Point(559, 39), size=wx.Size(70, 13), style=0)
        self.definirMetros2Radio = wx.StaticText(id=wxID_PANEL1DEFINIRMETROS2RADIO, label=_(u'Superficie (m2)'), name=u'definirMetros2Radio', parent=self, pos=wx.Point(435, 58), size=wx.Size(81, 13), style=0)
        self.definirDemandaRadio = wx.StaticText(id=wxID_PANEL1RADIOBUTTON1, label=_(u'Porcentaje (%)'), name='definirDemandaRadio', parent=self, pos=wx.Point(435, 80), size=wx.Size(100, 13), style=0)
        self.coberturaMetros = wx.TextCtrl(id=wxID_PANEL1COBERTURA, name=u'coberturaMetros', parent=self, pos=wx.Point(540, 55), size=wx.Size(60, 21), style=0, value=u'')
        self.coberturaMetros.SetForegroundColour(wx.Colour(100, 200, 0))
        self.coberturaMetros.Bind(wx.EVT_TEXT, self.OnCobertura, id=wxID_PANEL1COBERTURA)
        self.coberturaPorcentaje = wx.TextCtrl(id=wxID_PANEL1COBERTURAPORCEN, name=u'coberturaPorcentaje', parent=self, pos=wx.Point(540, 77), size=wx.Size(60, 21), style=0, value=u'')
        self.coberturaPorcentaje.SetForegroundColour(wx.Colour(100, 200, 0))
        self.coberturaPorcentaje.Bind(wx.EVT_TEXT, self.OnCoberturaPorcentaje, id=wxID_PANEL1COBERTURAPORCEN)
        self.rendimientoText = wx.StaticText(id=wxID_PANEL1RENDIMIENTOTEXT, label=_(u'Rendimiento estacional'), name=u'rendimientoText', parent=self, pos=wx.Point(15, 130), size=wx.Size(150, 25), style=0)
        self.rendimientoText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.rendimientoChoice = MiChoice(choices=self.parent.listadoOpcionesInstalaciones, id=wxID_PANEL1CHOICE1, name='rendimientoChoice', parent=self, pos=wx.Point(170, 128), size=wx.Size(220, 21), style=0)
        self.rendimientoChoice.SetSelection(1)
        self.rendimientoChoice.Bind(wx.EVT_CHOICE, self.OnrendimientoChoice, id=wxID_PANEL1CHOICE1)
        self.EficienciaLineaText = wx.StaticBox(id=wxID_EFICIENCIALINEATEXT, label=_(u'Rendimiento medio estacional'), name='EficienciaLineaText', parent=self, pos=wx.Point(0, 107), size=wx.Size(710, 135), style=0)
        self.EficienciaLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.EficienciaLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.potenciaNominalText = wx.StaticText(id=wxID_PANEL1POTENCIANOMINALTEXT, label=_(u'Potencia nominal'), name=u'potenciaNominalText', parent=self, pos=wx.Point(15, 155), size=wx.Size(120, 13), style=0)
        self.potenciaNominalText.Show(False)
        self.potenciaNominal = wx.TextCtrl(id=wxID_PANEL1POTENCIANOMINAL, name=u'potenciaNominal', parent=self, pos=wx.Point(170, 153), size=wx.Size(60, 21), style=0, value=u'24.0')
        self.potenciaNominal.SetForegroundColour(wx.Colour(100, 200, 0))
        self.potenciaNominal.Show(False)
        self.potenciaNominal.Bind(wx.EVT_TEXT, self.OnPotenciaNominal, id=wxID_PANEL1POTENCIANOMINAL)
        self.potenciaNominalUnidadesText = wx.StaticText(id=wxID_PANEL1POTENCIANOMINALUNIDADESTEXT, label=_(u'kW'), name=u'potenciaNominalUnidadesText', parent=self, pos=wx.Point(235, 155), size=wx.Size(15, 13), style=0)
        self.potenciaNominalUnidadesText.Show(False)
        self.cargaMediaText = wx.StaticText(id=wxID_PANEL1CARGAMEDIATEXT, label=_(u'Carga media real \xdfcmb'), name=u'cargaMediaText', parent=self, pos=wx.Point(15, 180), size=wx.Size(142, 13), style=0)
        self.cargaMediaText.Show(False)
        self.cargaMedia = wx.TextCtrl(id=wxID_PANEL1CARGAMEDIA, name=u'cargaMedia', parent=self, pos=wx.Point(170, 178), size=wx.Size(60, 21), style=0)
        self.cargaMedia.Show(False)
        self.cargaMedia.SetValue('%s' % betaCombDefecto)
        self.cargaMedia.SetForegroundColour(wx.Colour(100, 200, 0))
        self.cargaMedia.Bind(wx.EVT_TEXT, self.cambioCargaMedia, id=wxID_PANEL1CARGAMEDIA)
        self.cargaMediaHelpButton = wx.Button(id=wxID_PANEL1CARGAMEDIAHELPBUTTON, label=_(u' ?'), name=u'normativaHelpButton', parent=self, pos=wx.Point(235, 178), size=wx.Size(20, 21), style=0)
        self.cargaMediaHelpButton.Bind(wx.EVT_BUTTON, self.onCargaMediaHelpButton, id=wxID_PANEL1CARGAMEDIAHELPBUTTON)
        self.cargaMediaHelpButton.Show(False)
        self.rendimientoCombustionText = wx.StaticText(id=wxID_PANEL1RENDIMIENTOCOMBUSTEXT, label=_(u'Rendimiento de combusti\xf3n'), name=u'rendimientoCombustionText', parent=self, pos=wx.Point(15, 205), size=wx.Size(142, 13), style=0)
        self.rendimientoCombustionText.Show(False)
        self.rendimientoCombustion = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTOMCOMBUS, name=u'rendimientoCombustion', parent=self, pos=wx.Point(170, 203), size=wx.Size(60, 21), style=0)
        self.rendimientoCombustion.SetValue('%s' % rendCombustionDefecto)
        self.rendimientoCombustion.Show(False)
        self.rendimientoCombustion.SetForegroundColour(wx.Colour(100, 200, 0))
        self.rendimientoCombustion.Bind(wx.EVT_TEXT, self.OnRendimientoCombustion, id=wxID_PANEL1RENDIMIENTOMCOMBUS)
        self.rendimientoCombustionUnidadesText = wx.StaticText(id=wxID_PANEL1RENDIMIENTOCOMBUSUNITEXT, label=_(u'%'), name=u'rendimientoCombustionUnidadesText', parent=self, pos=wx.Point(235, 205), size=wx.Size(105, 13), style=0)
        self.rendimientoCombustionUnidadesText.Show(False)
        self.aislenteCalderaText = wx.StaticText(id=wxID_PANEL1AISLANTECALDERATEXT, label=_(u'Aislamiento de la caldera'), name=u'aislenteCalderaText', parent=self, pos=wx.Point(365, 180), size=wx.Size(140, 13), style=0)
        self.aislenteCalderaText.Show(False)
        self.aislanteCaldera = MiChoice(choices=listadosWeb.listadoOpcionesAislamientoCaldera, id=wxID_PANEL1AISLANTECALDE, name=u'aislanteCaldera', parent=self, pos=wx.Point(497, 178), size=wx.Size(180, 21), style=0)
        self.aislanteCaldera.SetSelection(2)
        self.aislanteCaldera.Show(False)
        self.aislanteCaldera.Bind(wx.EVT_CHOICE, self.obtenerRendimientoEstacional, id=wxID_PANEL1AISLANTECALDE)
        self.definirCalderaBoton = wx.Button(id=wxID_PANEL1DEFINIRBOTON, label=_(u'Caracter\xedsticas de la caldera'), name=u'definirCalderaBoton', parent=self, pos=wx.Point(497, 203), size=wx.Size(180, 21), style=0)
        self.definirCalderaBoton.Bind(wx.EVT_BUTTON, self.OndefinirCalderaBoton, id=wxID_PANEL1DEFINIRBOTON)
        self.definirCalderaBoton.Show(False)
        self.rendimientoMedioText = wx.StaticText(id=wxID_PANEL1RENDIMIENTOMEDIOTEXT, label=_(u'Rendimiento medio estacional'), name=u'rendimientoMedioText', parent=self, pos=wx.Point(435, 130), size=wx.Size(30, 13), style=0)
        self.rendimientoMedioText.Show(False)
        self.rendimientoMedioText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.rendimietoMedio = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTOMEDIO, name=u'rendimietoMedio', parent=self, pos=wx.Point(617, 128), size=wx.Size(60, 21), style=0)
        self.rendimietoMedio.Show(False)
        self.rendimietoMedio.Bind(wx.EVT_TEXT, self.obtenerRendimientoEstacional, id=wxID_PANEL1RENDIMIENTOMEDIO)
        self.rendimientoMedioUnidadesText = wx.StaticText(id=wxID_PANEL1RENDIMIENTOMEDIOTEXT, label=_(u'%'), name=u'rendimientoMedioUnidadesText', parent=self, pos=wx.Point(682, 130), size=wx.Size(15, 13), style=0)
        self.rendimientoMedioUnidadesText.Show(False)
        self.VariosGeneradoresCheck = wx.CheckBox(id=wxID_WXVARIOSGENERADORESCHECK, label=_(u'\xbfExisten varios generadores escalonados?'), name='VariosGeneradoresCheck', parent=self, pos=wx.Point(357, 155), size=wx.Size(300, 20), style=0)
        self.VariosGeneradoresCheck.Enable(False)
        self.VariosGeneradoresCheck.SetValue(False)
        self.VariosGeneradoresCheck.Show(False)
        self.FraccionPotencia = wx.TextCtrl(id=wxID_PANEL1FRACCIONPOTENCIA, name=u'FraccionPotencia', parent=self, pos=wx.Point(637, 177), size=wx.Size(40, 15), style=0, value=u'1.0')
        self.FraccionPotencia.Show(False)
        self.fraccionPotenciaEntrada = wx.TextCtrl(id=wxID_PANEL1FRACCIONPOTENCIAENTRADA, name=u'FraccionPotenciaEntrada', parent=self, pos=wx.Point(637, 197), size=wx.Size(40, 15), style=0, value=u'0.0')
        self.fraccionPotenciaEntrada.Show(False)
        self.definirAntiguedadText = wx.StaticText(id=wxID_PANEL1ANTIEQUIPOTEXT, label=_(u'Antig\xfcedad del equipo'), name=u'definirAntiguedadText', parent=self, pos=wx.Point(15, 155), size=wx.Size(120, 13), style=0)
        self.definirAntiguedadText.Show(False)
        self.definirAntiguedadChoice = MiChoice(choices=listadosWeb.listadoOpcionesAntiguedad, id=wxID_PANEL1ANTIGUEDADCHOICE, name=u'antiguedadChoice', parent=self, pos=wx.Point(170, 153), size=wx.Size(135, 21), style=0)
        self.definirAntiguedadChoice.SetSelection(2)
        self.definirAntiguedadChoice.Bind(wx.EVT_CHOICE, self.OnAntiguedadChoice, id=wxID_PANEL1ANTIGUEDADCHOICE)
        self.definirAntiguedadChoice.Show(False)
        self.rendimientoNominalText = wx.StaticText(id=wxID_PANEL1RENDNOMINALTEXT, label=_(u'Rendimiento nominal'), name=u'rendimientoNominalText', parent=self, pos=wx.Point(15, 180), size=wx.Size(140, 13), style=0)
        self.rendimientoNominalText.Show(False)
        self.rendimientoNominal = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTONOMINAL, name=u'rendimientoNominal', parent=self, pos=wx.Point(170, 178), size=wx.Size(60, 21), style=0, value='%s' % rendNominalJoule)
        self.rendimientoNominal.SetForegroundColour(wx.Colour(100, 200, 0))
        self.rendimientoNominal.Show(False)
        self.rendimientoNominal.Bind(wx.EVT_TEXT, self.OnRendimientoNominal, id=wxID_PANEL1RENDIMIENTONOMINAL)
        self.rendimientoNominalUnidadesText = wx.StaticText(id=wxID_PANEL1RENDNOMINALUNITEXT, label=_(u'%'), name=u'rendimientoNominalUnidadesText', parent=self, pos=wx.Point(235, 180), size=wx.Size(15, 13), style=0)
        self.rendimientoNominalUnidadesText.Show(False)
        self.ddaCubiertaBDCText = wx.StaticText(id=-1, label=_(u'Demanda Cubierta'), name='DemandaCubiertaText', parent=self, pos=wx.Point(357, 219), size=wx.Size(275, 13), style=0)
        self.ddaCubiertaBDCText.Show(False)
        self.ddaCubiertaBDCPorcentaje = wx.StaticText(id=-1, label=_(u'%'), name='DemandaCubiertaText', parent=self, pos=wx.Point(682, 219), size=wx.Size(15, 13), style=0)
        self.ddaCubiertaBDCPorcentaje.Show(False)
        self.ddaCubiertaBDC = wx.TextCtrl(id=wxID_PANEL1DDACUBIERTABDC, name=u'ddaCubiertaBDC', parent=self, pos=wx.Point(637, 217), size=wx.Size(40, 15), style=0, value=u'')
        self.ddaCubiertaBDC.Show(False)
        self.ddaCubiertaBDC.Enable(False)
        self.potNominalText = wx.StaticText(id=wxID_PANEL1POTNOMINALTEXT, label=_(u'Potencia nominal'), name=u'potNominalText', parent=self, pos=wx.Point(15, 155), size=wx.Size(150, 13), style=0)
        self.potNominalText.Show(False)
        self.potNominalUnidadesText = wx.StaticText(id=wxID_PANEL1POTNOMINALUNIDADESTEXT, label=_(u'kW'), name=u'potNominalText', parent=self, pos=wx.Point(235, 155), size=wx.Size(15, 13), style=0)
        self.potNominalUnidadesText.Show(False)
        self.potNominal = wx.TextCtrl(id=wxID_PANEL1POTNOMINAL, name=u'potNominal', parent=self, pos=wx.Point(170, 153), size=wx.Size(60, 21), style=0, value=u'')
        self.potNominal.Show(False)
        self.potNominal.Bind(wx.EVT_TEXT, self.obtenerRendimientoEstacional, id=wxID_PANEL1POTNOMINAL)
        self.rendNominalPGText = wx.StaticText(id=wxID_PANEL1RENDNOMINALPGTEXT, label=_(u'Rendimiento nominal a plena carga'), name=u'rendNominalPGText', parent=self, pos=wx.Point(15, 176), size=wx.Size(130, 27), style=0)
        self.rendNominalPGText.Show(False)
        self.rendNominalPGUnidadesText = wx.StaticText(id=wxID_PANEL1RENDNOMINALPGUNIDADESTEXT, label=_(u'%'), name=u'potNominalText', parent=self, pos=wx.Point(235, 180), size=wx.Size(15, 13), style=0)
        self.rendNominalPGUnidadesText.Show(False)
        self.rendNominalPG = wx.TextCtrl(id=wxID_PANEL1RENDNOMINALPG, name=u'rendNominalPG', parent=self, pos=wx.Point(170, 178), size=wx.Size(60, 21), style=0, value=u'')
        self.rendNominalPG.Show(False)
        self.rendNominalPG.Bind(wx.EVT_TEXT, self.obtenerRendimientoEstacional, id=wxID_PANEL1RENDNOMINALPG)
        self.temperaturaAmbienteIntText = wx.StaticText(id=wxID_PANEL1TEMPAMBINTTEXT, label=_(u'Temperatura acumulaci\xf3n'), name=u'temperaturaAmbienteIntText', parent=self, pos=wx.Point(435, 155), size=wx.Size(150, 13), style=0)
        self.temperaturaAmbienteIntText.Show(False)
        self.temperaturaAmbienteInt = wx.TextCtrl(id=wxID_PANEL1TEMPAMBINT, name=u'temperaturaAmbienteIntText', parent=self, pos=wx.Point(617, 153), size=wx.Size(60, 16), style=0, value=u'50.0')
        self.temperaturaAmbienteInt.Show(False)
        self.temperaturaAmbienteInt.Bind(wx.EVT_TEXT, self.obtenerRendimientoEstacional, id=wxID_PANEL1TEMPAMBINT)
        self.temperaturaAmbienteIntUnidadesText = wx.StaticText(id=wxID_PANEL1TEMPAMBINTUNIDADESTEXT, label=_(u'\xbaC'), name=u'temperaturaAmbienteIntUnidadesText', parent=self, pos=wx.Point(682, 155), size=wx.Size(16, 13), style=0)
        self.temperaturaAmbienteIntUnidadesText.Show(False)
        self.factorCargaMinimoText = wx.StaticText(id=wxID_PANEL1FACRTORGARGAMINTEXT, label=_(u'Factor de carga parcial m\xednimo'), name=u'factorCargaMinimoText', parent=self, pos=wx.Point(435, 173), size=wx.Size(150, 13), style=0)
        self.factorCargaMinimoText.Show(False)
        self.factorCargaMinimo = wx.TextCtrl(id=wxID_PANEL1FACRTORGARGAMIN, name=u'factorCargaMinimo', parent=self, pos=wx.Point(617, 171), size=wx.Size(60, 16), style=0, value=u'0.15')
        self.factorCargaMinimo.Show(False)
        self.factorCargaMinimo.Bind(wx.EVT_TEXT, self.obtenerRendimientoEstacional, id=wxID_PANEL1FACRTORGARGAMIN)
        self.factorCargaMaximoText = wx.StaticText(id=wxID_PANEL1FACRTORGARGAMAXTEXT, label=_(u'Factor de carga parcial m\xe1ximo'), name=u'factorCargaMaximoText', parent=self, pos=wx.Point(435, 191), size=wx.Size(150, 13), style=0)
        self.factorCargaMaximoText.Show(False)
        self.factorCargaMaximo = wx.TextCtrl(id=wxID_PANEL1FACRTORGARGAMAX, name=u'factorCargaMaximo', parent=self, pos=wx.Point(617, 189), size=wx.Size(60, 16), style=0, value=u'1.0')
        self.factorCargaMaximo.Show(False)
        self.factorCargaMaximo.Bind(wx.EVT_TEXT, self.obtenerRendimientoEstacional, id=wxID_PANEL1FACRTORGARGAMAX)
        self.definirTemperaturasBoton = wx.Button(id=wxID_PANEL1DEFINIRTEMPERATURASBOTON, label=_(u'Definir temperaturas'), name=u'definirTemperaturasBoton', parent=self, pos=wx.Point(435, 151), size=wx.Size(145, 21), style=0)
        self.definirTemperaturasBoton.Bind(wx.EVT_BUTTON, self.OndefinirTemperaturasBoton, id=wxID_PANEL1DEFINIRTEMPERATURASBOTON)
        self.definirTemperaturasBoton.Show(False)
        self.definirCurvaBoton = wx.Button(id=wxID_PANEL1DEFINIRCURVABOTON, label=_(u'Definir curva modificadora'), name=u'definirCurvaBoton', parent=self, pos=wx.Point(435, 209), size=wx.Size(145, 21), style=0)
        self.definirCurvaBoton.Bind(wx.EVT_BUTTON, self.OndefinirCurvaBoton, id=wxID_PANEL1DEFINIRCURVABOTON)
        self.definirCurvaBoton.Show(False)
        self.rendimientoGlobalText = wx.StaticText(id=wxID_PANEL1RENDGLOBALTEXT, label=_(u'Rendimiento medio estacional'), name=u'rendimientoGlobalText', parent=self, pos=wx.Point(435, 130), size=wx.Size(30, 13), style=0)
        self.rendimientoGlobalText.Show(True)
        self.rendimientoGlobalText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.rendimientoGlobal = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTOGLOBAL, name=u'rendimientoGlobal', parent=self, pos=wx.Point(617, 128), size=wx.Size(60, 21), style=0)
        self.rendimientoGlobal.Show(True)
        self.rendimientoGlobal.Enable(False)
        self.rendimientoGlobalUnidadesText = wx.StaticText(id=wxID_PANEL1RENDGLOBALUNITEXT, label=_(u'%'), name=u'rendimientoGlobalUnidadesText', parent=self, pos=wx.Point(682, 130), size=wx.Size(15, 13), style=0)
        self.rendimientoGlobalUnidadesText.Show(True)
        self.rendimientoGlobalUnidadesText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.rendimientoGlobalText.SetForegroundColour(wx.Colour(100, 100, 100))
        self.rendimientoGlobalUnidadesText.SetForegroundColour(wx.Colour(100, 100, 100))
        self.AcumulacionLineaText = wx.StaticBox(id=wxID_ACUMULACIONLINEATEXT, label=_(u'               '), name='AcumulacionLineaText', parent=self, pos=wx.Point(0, 247), size=wx.Size(710, 95), style=0)
        self.AcumulacionLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.AcumulacionLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.acumulacionCheck = wx.CheckBox(id=wxID_PANEL1ACUMULACIONTEXT, label=_(u'Con Acumulaci\xf3n'), name=u'acumulacionCheck', parent=self, pos=wx.Point(10, 247), size=wx.Size(104, 13), style=0)
        self.acumulacionCheck.SetValue(False)
        self.acumulacionCheck.Bind(wx.EVT_CHECKBOX, self.OnAcumulacionCheck, id=wxID_PANEL1ACUMULACIONTEXT)
        self.valorUAText = wx.StaticText(id=wxID_PANEL1VALORUATEXT, label=_(u'Valor UA'), name=u'valorUAText', parent=self, pos=wx.Point(15, 267), size=wx.Size(42, 13), style=0)
        self.valorUAText.Show(False)
        self.valorUAChoice = MiChoice(choices=listadosWeb.listadoOpcionesAcumulacion, id=wxID_PANEL1CHOICE2, name='valorUAChoice', parent=self, pos=wx.Point(170, 265), size=wx.Size(140, 21), style=0)
        self.valorUAChoice.Show(False)
        self.valorUAChoice.SetSelection(2)
        self.valorUAChoice.Bind(wx.EVT_CHOICE, self.OnvalorUAChoice, id=wxID_PANEL1CHOICE2)
        self.volumenText = wx.StaticText(id=wxID_PANEL1VOLUMENTEXT, label=_(u'Volumen de un dep\xf3sito'), name=u'volumenText', parent=self, pos=wx.Point(15, 291), size=wx.Size(140, 13), style=0)
        self.volumenText.Show(False)
        self.volumen = wx.TextCtrl(id=wxID_PANEL1VOLUMEN, name=u'volumen', parent=self, pos=wx.Point(170, 289), size=wx.Size(60, 20), style=0, value=u'')
        self.volumen.Bind(wx.EVT_TEXT, self.OnCalcularValorUAAcumulacion, id=wxID_PANEL1VOLUMEN)
        self.volumen.Show(False)
        self.volumenUnidadesText = wx.StaticText(id=wxID_PANEL1VOLUMENUNIDADESTEXT, label=_(u'l'), name=u'volumenUnidadesText', parent=self, pos=wx.Point(235, 291), size=wx.Size(2, 13), style=0)
        self.volumenUnidadesText.Show(False)
        self.multiplicadorText = wx.StaticText(id=wxID_PANEL1MULTIPLICADORTEXT, label=_(u'Multiplicador'), name=u'volumenText', parent=self, pos=wx.Point(350, 291), size=wx.Size(61, 13), style=0)
        self.multiplicadorText.Show(False)
        self.multiplicador = wx.TextCtrl(id=wxID_PANEL1MULTIPLICADOR, name=u'multiplicador', parent=self, pos=wx.Point(420, 289), size=wx.Size(60, 20), style=0, value=u'')
        self.multiplicador.SetValue('1')
        self.multiplicador.Show(False)
        self.multiplicador.Bind(wx.EVT_TEXT, self.OnCalcularValorUAAcumulacion, id=wxID_PANEL1MULTIPLICADOR)
        self.tipoAislamientoText = wx.StaticText(id=wxID_PANEL1TIPOAISTEXT, label=_(u'Tipo de aislamiento'), name='tipoAislamientoText', parent=self, pos=wx.Point(15, 315), size=wx.Size(150, 16), style=0)
        self.tipoAislamientoText.Show(False)
        self.aislamientoAcumulacionChoice = MiChoice(choices=listadosWeb.listadoOpcionesAislamientoAcumulacion, id=wxID_PANEL1AISLAMIENTOACUMULACIONCHOICE, name=u'aislamientoAcumulacionChoice', parent=self, pos=wx.Point(170, 313), size=wx.Size(140, 21), style=0)
        self.aislamientoAcumulacionChoice.SetSelection(0)
        self.aislamientoAcumulacionChoice.Show(False)
        self.aislamientoAcumulacionChoice.Bind(wx.EVT_CHOICE, self.OnCalcularValorUAAcumulacion, id=wxID_PANEL1AISLAMIENTOACUMULACIONCHOICE)
        self.espesorAislamientoText = wx.StaticText(id=wxID_PANEL1ESPESORAISTEXT, label=_(u'Espesor'), name='espesorAislamientoText', parent=self, pos=wx.Point(350, 315), size=wx.Size(60, 16), style=0)
        self.espesorAislamientoText.Show(False)
        self.espesorAislamiento = wx.TextCtrl(id=wxID_PANEL1ESPESORAISLA, name=u'espesorAislamiento', parent=self, pos=wx.Point(420, 313), size=wx.Size(60, 21), style=0, value=u'')
        self.espesorAislamiento.Show(False)
        self.espesorAislamiento.Bind(wx.EVT_TEXT, self.OnCalcularValorUAAcumulacion, id=wxID_PANEL1ESPESORAISLA)
        self.espesorAislamientoUnidadesText = wx.StaticText(id=wxID_PANEL1ESPESORAISTEXT, label=_(u'm'), name='espesorAislamientoUnidadesText', parent=self, pos=wx.Point(485, 315), size=wx.Size(20, 16), style=0)
        self.espesorAislamientoUnidadesText.Show(False)
        self.UAText = wx.StaticText(id=wxID_PANEL1UATEXT, label=_(u'UA'), name='UAText', parent=self, pos=wx.Point(542, 267), size=wx.Size(30, 16), style=0)
        self.UAText.Show(False)
        self.UAvalor = wx.TextCtrl(id=wxID_PANEL1UAVALOR, name=u'UAvalor', parent=self, pos=wx.Point(617, 265), size=wx.Size(60, 21), style=0, value=u'')
        self.UAvalor.Show(False)
        self.UAUnidadesText = wx.StaticText(id=wxID_PANEL1UATEXT, label=_(u'W/K'), name='UAUnidadesText', parent=self, pos=wx.Point(682, 267), size=wx.Size(25, 16), style=0)
        self.UAUnidadesText.Show(False)
        self.temperaturaAltaText = wx.StaticText(id=wxID_PANEL1TEMPERATURAALTATEXT, label=_(u'T\xaa alta'), name=u'temperaturaAltaText', parent=self, pos=wx.Point(542, 291), size=wx.Size(41, 13), style=0)
        self.temperaturaAltaText.Show(False)
        self.temperaturaAlta = wx.TextCtrl(id=wxID_PANEL1TEMPERATURAALTA, name=u'temperaturaAlta', parent=self, pos=wx.Point(617, 289), size=wx.Size(60, 20), style=0, value=u'')
        self.temperaturaAlta.SetValue('80')
        self.temperaturaAlta.SetForegroundColour(wx.Colour(100, 200, 0))
        self.temperaturaAlta.Bind(wx.EVT_TEXT, self.OnTemperaturaAlta, id=wxID_PANEL1TEMPERATURAALTA)
        self.temperaturaAlta.Show(False)
        self.tempAltaUnidadesText = wx.StaticText(id=wxID_PANEL1TEMPALTAUNIDADESTEXT, label=_(u'\xbaC'), name=u'tempAltaUnidadesText', parent=self, pos=wx.Point(682, 291), size=wx.Size(12, 13), style=0)
        self.tempAltaUnidadesText.Show(False)
        self.temperaturaBajaText = wx.StaticText(id=wxID_PANEL1TEMPERATURABAJATEXT, label=_(u'T\xaa baja'), name=u'temperaturaBajaText', parent=self, pos=wx.Point(542, 315), size=wx.Size(50, 13), style=0)
        self.temperaturaBajaText.Show(False)
        self.temperaturaBaja = wx.TextCtrl(id=wxID_PANEL1TEMPERATURABAJA, name=u'temperaturaBaja', parent=self, pos=wx.Point(617, 313), size=wx.Size(60, 20), style=0, value=u'')
        self.temperaturaBaja.SetValue('60')
        self.temperaturaBaja.SetForegroundColour(wx.Colour(100, 200, 0))
        self.temperaturaBaja.Bind(wx.EVT_TEXT, self.OnTemperaturaBaja, id=wxID_PANEL1TEMPERATURABAJA)
        self.temperaturaBaja.Show(False)
        self.staticText1 = wx.StaticText(id=wxID_PANEL1STATICTEXT1, label=_(u'\xbaC'), name='staticText1', parent=self, pos=wx.Point(682, 315), size=wx.Size(12, 16), style=0)
        self.staticText1.Show(False)

    def OnsubgrupoChoice(self, event):
        """
        Metodo: OnsubgrupoChoice
        Simplemente pone el valor del porcentaje al 100%, el .SetValue() llama al evento asociado,
        en este caso OncoberturaPorcentaje()
        
        ARGUMENTOS:
                event:
        """
        self.coberturaPorcentaje.SetValue('100')

    def OnNombreInstalacion(self, event):
        """
        Metodo: OnNombreInstalacion
        
        
        ARGUMENTOS:
                event:
        """
        if self.nombreInstalacion.GetValue() == _(u'Equipo ACS'):
            self.nombreInstalacion.SetForegroundColour(wx.Colour(100, 200, 0))
        else:
            self.nombreInstalacion.SetForegroundColour(wx.Colour(0, 0, 0))

    def OnCobertura(self, event):
        """
        Metodo: OnCobertura
        
        
        ARGUMENTOS:
                event:
        """
        if self.booleano == True:
            self.booleano = False
            if self.subgrupoChoice.GetStringSelection() == u'Edificio Objeto':
                try:
                    superficieTotal = float(self.parent.parent.parent.panelDatosGenerales.superficie.GetValue())
                    superficieActual = float(self.coberturaMetros.GetValue())
                    porcentaje = round(superficieActual * 100 / superficieTotal, 2)
                    self.coberturaPorcentaje.SetValue(str(porcentaje))
                except (ValueError, TypeError):
                    self.coberturaPorcentaje.SetValue('')
                except ZeroDivisionError:
                    self.coberturaPorcentaje.SetValue('')

            else:
                for i in self.parent.parent.subgrupos:
                    if i.nombre == self.subgrupoChoice.GetStringSelection():
                        mTotales = float(i.superficie)
                        break

                try:
                    mActuales = float(self.coberturaMetros.GetValue())
                    porcentaje = round(mActuales * 100 / mTotales, 2)
                    self.coberturaPorcentaje.SetValue(str(porcentaje))
                except (ValueError, TypeError):
                    self.coberturaPorcentaje.SetValue('')
                except ZeroDivisionError:
                    self.coberturaPorcentaje.SetValue('')

            self.booleano = True

    def OnCoberturaPorcentaje(self, event):
        """
        Metodo: OnCoberturaPorcentaje
        
        
        ARGUMENTOS:
                event:
        """
        if self.booleano == True:
            self.booleano = False
            if self.subgrupoChoice.GetStringSelection() == u'Edificio Objeto':
                try:
                    superficieTotal = float(self.parent.parent.parent.panelDatosGenerales.superficie.GetValue())
                    porcentajeActual = float(self.coberturaPorcentaje.GetValue())
                    mAcuales = round(porcentajeActual * superficieTotal / 100.0, 2)
                    self.coberturaMetros.SetValue(str(mAcuales))
                except (ValueError, TypeError):
                    self.coberturaMetros.SetValue('')
                except ZeroDivisionError:
                    self.coberturaMetros.SetValue('')

            else:
                for i in self.parent.parent.subgrupos:
                    if i.nombre == self.subgrupoChoice.GetStringSelection():
                        mTotales = float(i.superficie)
                        break

                try:
                    porcentaje = float(self.coberturaPorcentaje.GetValue())
                    mAcuales = round(porcentaje * mTotales / 100.0, 2)
                    self.coberturaMetros.SetValue(str(mAcuales))
                except (ValueError, TypeError):
                    self.coberturaMetros.SetValue('')
                except ZeroDivisionError:
                    self.coberturaMetros.SetValue('')

            self.booleano = True

    def OnPotenciaNominal(self, event):
        """
        Metodo: OnPotenciaNominal
        
        
        ARGUMENTOS:
                event:
        """
        if self.potenciaNominal.GetValue() == '24.0':
            self.potenciaNominal.SetForegroundColour(wx.Colour(100, 200, 0))
        else:
            self.potenciaNominal.SetForegroundColour(wx.Colour(0, 0, 0))
        self.obtenerRendimientoEstacional(None)
        return

    def OndefinirTemperaturasBoton(self, event):
        """
        Metodo: OndefinirTemperaturasBoton
        
        
        ARGUMENTOS:
                event:
        """
        dlg = dialogoTemperaturas.create(self, self.temperaturas)
        dlg.ShowModal()
        if dlg.dev != False:
            self.temperaturas[0] = dlg.dev[0]
            self.temperaturas[1] = dlg.dev[1]
            self.temperaturas[2] = dlg.dev[2]
        self.obtenerRendimientoEstacional(None)
        return

    def OndefinirCurvaBoton(self, event):
        """
        Metodo: OndefinirCurvaBoton
        
        
        ARGUMENTOS:
                event:
        """
        if self.generadorChoice.GetStringSelection() == u'Caldera Est\xe1ndar':
            formula = 'Eff =  A0 + A1*fcp + A2*fcp\xb2 + A3*fcp\xb3'
            campos = ['A0',
             'A1',
             'A2',
             'A3']
            dlg = formulaCurvaRendimiento.create(self, formula, campos, self.curvaRendimiento)
            dlg.ShowModal()
        elif self.generadorChoice.GetStringSelection() == u'Caldera Condensaci\xf3n':
            formula = 'Eff = A0 + A1*fcp + A2*fcp\xb2 + A3*Tw + A4*Tw\xb2 + A5*fcp*Tw'
            campos = ['A0',
             'A1',
             'A2',
             'A3',
             'A4',
             'A5']
            dlg = formulaCurvaRendimiento.create(self, formula, campos, self.curvaRendimiento)
            dlg.ShowModal()
        elif self.generadorChoice.GetStringSelection() == u'Caldera Baja Temperatura':
            formula = 'Eff = A0 + A1*fcp + A2*fcp\xb2 + A3*Tw + A4*Tw\xb2 + A5*fcp*Tw \n      + A6*fcp\xb3 + A7*Tw\xb3 + A8*fcp\xb2*Tw + A9*fcp*Tw\xb2'
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
            formula = 'conCal_FCP = A0 + A1*fcp + A2*fcp\xb2 + A3*fcp\xb3   \nconCal_Tint_Thext = B0 + B1*Tint + B2*Tint\xb2 + B3*Thext + B4*Thext\xb2 + B5*Tint*Thext'
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

    def OndefinirCalderaBoton(self, event):
        """
        Metodo: OndefinirCalderaBoton
        
        
        ARGUMENTOS:
                event:
        """
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
        """
        Constructor de la clase
        
        
        ARGUMENTOS:
                parent:
                id:
                pos:
                size:
                style:
                name:
                real_parent = None:
        """
        if real_parent == None:
            self.parent = parent
        else:
            self.parent = real_parent
        self._init_ctrls(parent, id, pos, size, style, name)
        self.tipoSistema = 'ACS'
        self.temperaturas = [50, 85, 50]
        self.curvaRendimiento = ['0.89305015622789352',
         '0.45702553179343713',
         '-0.60789791967901996',
         '0.23878599898375633']
        self.listaErrores = u''
        self.subgrupoChoice.SetItems(self.cargarRaices())
        self.OnrendimientoChoice(None)
        self.rendimientoEstacionalACS = ''
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
        """
        Metodo: obtenerRendimientoEstacional
        funcion para otener el rendimiento medio estacional
        
        ARGUMENTOS:
                event:  
        """
        kwargsCalderaEst = {'aislanteCaldera': self.aislanteCaldera.GetStringSelection(),
         'rendCombCaldera': self.rendimientoCombustion.GetValue(),
         'potenciaCaldera': self.potenciaNominal.GetValue(),
         'cargaMediaCaldera': self.cargaMedia.GetValue()}
        kwargsConocido = {'rendEstACS': self.rendimietoMedio.GetValue(),
         'rendEstCal': '',
         'rendEstRef': ''}
        kwargsJouleEst = {'rendNominal': self.rendimientoNominal.GetValue()}
        kwargsBdCEst = {'rendNominalACS': self.rendimientoNominal.GetValue(),
         'rendNominalCal': '',
         'rendNominalRef': '',
         'variosGeneradoresCheck': False,
         'fraccionPotencia': '',
         'fraccionPotenciaEntrada': ''}
        kwargsCalderaSgCurva = {'curvaRendimiento': self.curvaRendimiento,
         'rendNominalPG': self.rendNominalPG.GetValue(),
         'factorCargaMinimo': self.factorCargaMinimo.GetValue(),
         'factorCargaMaximo': self.factorCargaMaximo.GetValue(),
         'potNominal': self.potNominal.GetValue(),
         'temperaturas': self.temperaturas}
        kwargsBdCSgCurva = {'curvaRendimiento': self.curvaRendimiento,
         'rendNominalPG': self.rendNominalPG.GetValue(),
         'factorCargaMinimo': self.factorCargaMinimo.GetValue(),
         'factorCargaMaximo': self.factorCargaMaximo.GetValue(),
         'potNominal': self.potNominal.GetValue(),
         'temperaturaAmbienteInt': self.temperaturaAmbienteInt.GetValue()}
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
        self.rendimientoEstacionalACS = calculoRendimientoMedioEstacional(zonaHE1=zonaHE1, programa=programa, tipoEdificio=tipoEdificio, tipoInstalacion=self.tipoSistema, modoDefinicion=modoDefinicion, tipoEquipo=tipoEquipo, combustible=combustible, **kwargs)
        self.escribirRendimientoGlobal()

    def escribirRendimientoGlobal(self):
        """
        Metodo: escribirRendimientoGlobal
        
        
        """
        self.rendimientoGlobal.SetValue(str(self.rendimientoEstacionalACS))

    def cambioCargaMedia(self, event):
        """
        Metodo: cambioCargaMedia
        
        
        ARGUMENTOS:
                event:
        """
        try:
            self.cargaMedia.SetForegroundColour(wx.Colour(0, 0, 0))
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        self.obtenerRendimientoEstacional(None)
        return

    def elegirRaiz(self):
        """
        Metodo: elegirRaiz
        
        
        """
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
        """
        Metodo: cargarRaices
        
        
        """
        raices = []
        raices.append((u'Edificio Objeto', _(u'Edificio Objeto')))
        for i in range(len(self.parent.parent.subgrupos)):
            if self.parent.parent.subgrupos[i].nombre != u'Edificio Objeto':
                raices.append((self.parent.parent.subgrupos[i].nombre, self.parent.parent.subgrupos[i].nombre))

        return raices

    def OngeneradorChoice(self, event):
        """
        Metodo: OngeneradorChoice
        
        
        ARGUMENTOS:
                event:
        """
        try:
            if float(self.generadorChoice.GetSelection()) == 0.0:
                self.curvaRendimiento = ['0.89305015622789352',
                 '0.45702553179343713',
                 '-0.60789791967901996',
                 '0.23878599898375633']
                self.rendNominalPGText.SetLabel(_(u'Rendimiento nominal a plena carga'))
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
                self.rendNominalPGText.SetLabel(_(u'Rendimiento nominal a plena carga'))
                self.rendNominalPGText.SetSize(wx.Size(130, 27))
                self.rendNominalPGText.SetPosition(wx.Point(15, 176))
                self.combustibleChoice.SetSelection(0)
            elif float(self.generadorChoice.GetSelection()) == 2.0:
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
                self.rendNominalPGText.SetLabel(_(u'Rendimiento nominal a plena carga'))
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
                self.rendNominalPGText.SetLabel(_(u'Rendimiento nominal a plena carga'))
                self.rendNominalPGText.SetSize(wx.Size(130, 27))
                self.rendNominalPGText.SetPosition(wx.Point(15, 176))
                self.combustibleChoice.SetSelection(2)
            elif self.generadorChoice.GetStringSelection() == u'Bomba de Calor - Caudal Ref. Variable':
                self.rendNominalPGText.SetLabel(_(u'Rendimiento nominal a plena carga'))
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
                self.rendNominalPGText.SetLabel(_(u'Rendimiento nominal a plena carga'))
                self.rendNominalPGText.SetSize(wx.Size(130, 27))
                self.rendNominalPGText.SetPosition(wx.Point(15, 180))
            elif self.generadorChoice.GetStringSelection() == u'Equipo de Rendimiento Constante':
                self.rendNominalPGText.SetLabel(_(u'Rendimiento nominal a plena carga'))
                self.rendNominalPGText.SetSize(wx.Size(130, 27))
                self.rendNominalPGText.SetPosition(wx.Point(15, 176))
            self.cargaTipoCombustible()
            self.cargaModoObtencion()
            self.OnrendimientoChoice(None)
        except Exception as e:
            pass

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
        """
        M\xe9todo: actualizarRendimientoNominalEquiposElectricos
        Si ha cambiado a equipo efecto joule o caldera, en rendimiento nominal se pone 100 %
        
        """
        try:
            float(self.rendimientoNominal.GetValue())
            valorValido = True
        except:
            valorValido = False

        listadoValoresStr = [ str(x) for x in diccCOPNominalDefecto.values() ]
        if self.rendimientoNominal.GetValue() in listadoValoresStr or self.rendimientoNominal.GetValue() == str(rendNominalJoule) or valorValido == False:
            if u'Bomba' in self.generadorChoice.GetStringSelection():
                rendNominalDefecto = diccCOPNominalDefecto[self.definirAntiguedadChoice.GetSelection()]
            else:
                rendNominalDefecto = rendNominalJoule
            self.rendimientoNominal.SetValue('%s' % rendNominalDefecto)
            self.rendimientoNominal.SetForegroundColour(wx.Colour(100, 200, 0))

    def OnCombustibleChoice(self, event):
        """
        Metodo: OnCombustibleChoice
        
        
        ARGUMENTOS:
                event:
        """
        self.cargaModoObtencion()
        self.OnrendimientoChoice(None)
        self.obtenerRendimientoEstacional(None)
        return

    def OnAntiguedadChoice(self, event):
        self.actualizarRendimientoNominalEquiposElectricos()
        self.obtenerRendimientoEstacional(None)
        return

    def OnRendimientoCombustion(self, event):
        """
        Metodo: OnRendimientoCombustion
        
        
        ARGUMENTOS:
                event:
        """
        try:
            self.rendimientoCombustion.SetForegroundColour(wx.Colour(0, 0, 0))
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        self.obtenerRendimientoEstacional(None)
        return

    def OnRendimientoNominal(self, event):
        """
        Metodo: OnRendimientoNominal
        
        
        ARGUMENTOS:
                event:
        """
        try:
            self.rendimientoNominal.SetForegroundColour(wx.Colour(0, 0, 0))
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        self.obtenerRendimientoEstacional(None)
        return

    def OnTemperaturaAlta(self, event):
        """
        Metodo: OnTemperaturaAlta
        
        
        ARGUMENTOS:
                event:
        """
        try:
            self.temperaturaAlta.SetForegroundColour(wx.Colour(0, 0, 0))
        except:
            logging.info(u'Excepcion en: %s' % __name__)

    def OnTemperaturaBaja(self, event):
        """
        Metodo: OnTemperaturaBaja
        
        
        ARGUMENTOS:
                event:
        """
        try:
            self.temperaturaBaja.SetForegroundColour(wx.Colour(0, 0, 0))
        except:
            logging.info(u'Excepcion en: %s' % __name__)

    def OnrendimientoChoice(self, event):
        """
        Metodo: OnrendimientoChoice
        
        
        ARGUMENTOS:
                event:
        Se llama al cambiar de tipo de equipo, de tipo de combustible o de modoDefini\xf3n
        """
        if 'Conocido' in self.rendimientoChoice.GetStringSelection():
            self.potNominalText.Show(False)
            self.potNominal.Show(False)
            self.rendNominalPGText.Show(False)
            self.rendNominalPG.Show(False)
            self.factorCargaMinimoText.Show(False)
            self.factorCargaMinimo.Show(False)
            self.factorCargaMaximoText.Show(False)
            self.factorCargaMaximo.Show(False)
            self.factorCargaMaximo.Show(False)
            self.definirCurvaBoton.Show(False)
            self.definirTemperaturasBoton.Show(False)
            self.temperaturaAmbienteIntUnidadesText.Show(False)
            self.temperaturaAmbienteIntText.Show(False)
            self.temperaturaAmbienteInt.Show(False)
            self.rendNominalPGUnidadesText.Show(False)
            self.potNominalUnidadesText.Show(False)
            self.rendimientoMedioText.Show(True)
            self.rendimietoMedio.Show(True)
            self.rendimientoMedioUnidadesText.Show(True)
            self.rendimientoGlobalText.Show(False)
            self.rendimientoGlobal.Show(False)
            self.rendimientoGlobalUnidadesText.Show(False)
            self.definirAntiguedadText.Show(False)
            self.definirAntiguedadChoice.Show(False)
            self.rendimientoNominalText.Show(False)
            self.rendimientoNominal.Show(False)
            self.rendimientoNominalUnidadesText.Show(False)
            self.rendimientoCombustionText.Show(False)
            self.aislanteCaldera.Show(False)
            self.aislenteCalderaText.Show(False)
            self.rendimientoCombustion.Show(False)
            self.rendimientoCombustionUnidadesText.Show(False)
            self.cargaMediaText.Show(False)
            self.cargaMedia.Show(False)
            self.cargaMediaHelpButton.Show(False)
            self.definirCalderaBoton.Show(False)
            self.potenciaNominalText.Show(False)
            self.potenciaNominal.Show(False)
            self.potenciaNominalUnidadesText.Show(False)
            self.ddaCubiertaBDCText.Show(False)
            self.ddaCubiertaBDC.Show(False)
            self.ddaCubiertaBDCPorcentaje.Show(False)
        elif u'Estimado seg\xfan Instalaci\xf3n' in self.rendimientoChoice.GetStringSelection():
            self.potNominalText.Show(False)
            self.potNominal.Show(False)
            self.rendNominalPGText.Show(False)
            self.rendNominalPG.Show(False)
            self.factorCargaMinimoText.Show(False)
            self.factorCargaMinimo.Show(False)
            self.factorCargaMaximoText.Show(False)
            self.factorCargaMaximo.Show(False)
            self.factorCargaMaximo.Show(False)
            self.definirCurvaBoton.Show(False)
            self.definirTemperaturasBoton.Show(False)
            self.temperaturaAmbienteIntUnidadesText.Show(False)
            self.temperaturaAmbienteIntText.Show(False)
            self.temperaturaAmbienteInt.Show(False)
            self.rendNominalPGUnidadesText.Show(False)
            self.potNominalUnidadesText.Show(False)
            self.rendimientoMedioText.Show(False)
            self.rendimietoMedio.Show(False)
            self.rendimientoMedioUnidadesText.Show(False)
            self.rendimientoGlobalText.Show(True)
            self.rendimientoGlobal.Show(True)
            self.rendimientoGlobalUnidadesText.Show(True)
            self.ddaCubiertaBDCText.Show(False)
            self.ddaCubiertaBDC.Show(False)
            if u'Caldera' in self.generadorChoice.GetStringSelection() and self.combustibleChoice.GetStringSelection() != u'Electricidad':
                self.rendimientoCombustionText.Show(True)
                self.aislanteCaldera.Show(True)
                self.aislenteCalderaText.Show(True)
                self.rendimientoCombustion.Show(True)
                self.rendimientoCombustionUnidadesText.Show(True)
                self.cargaMediaText.Show(True)
                self.cargaMedia.Show(True)
                self.cargaMediaHelpButton.Show(True)
                self.definirCalderaBoton.Show(False)
                self.potenciaNominalText.Show(True)
                self.potenciaNominal.Show(True)
                self.potenciaNominalUnidadesText.Show(True)
                self.definirAntiguedadText.Show(False)
                self.definirAntiguedadChoice.Show(False)
                self.rendimientoNominalText.Show(False)
                self.rendimientoNominal.Show(False)
                self.rendimientoNominalUnidadesText.Show(False)
                self.ddaCubiertaBDCText.Show(False)
                self.ddaCubiertaBDC.Show(False)
                self.ddaCubiertaBDCPorcentaje.Show(False)
            else:
                self.rendimientoCombustionText.Show(False)
                self.aislanteCaldera.Show(False)
                self.aislenteCalderaText.Show(False)
                self.rendimientoCombustion.Show(False)
                self.rendimientoCombustionUnidadesText.Show(False)
                self.cargaMediaText.Show(False)
                self.cargaMedia.Show(False)
                self.cargaMediaHelpButton.Show(False)
                self.definirCalderaBoton.Show(False)
                self.potenciaNominalText.Show(False)
                self.potenciaNominal.Show(False)
                self.potenciaNominalUnidadesText.Show(False)
                if self.generadorChoice.GetStringSelection() == u'Efecto Joule' or u'Caldera' in self.generadorChoice.GetStringSelection() and self.combustibleChoice.GetStringSelection() == u'Electricidad':
                    self.definirAntiguedadText.Show(False)
                    self.definirAntiguedadChoice.Show(False)
                else:
                    self.definirAntiguedadText.Show(True)
                    self.definirAntiguedadChoice.Show(True)
                self.rendimientoNominalText.Show(True)
                self.rendimientoNominal.Show(True)
                self.rendimientoNominalUnidadesText.Show(True)
                self.actualizarRendimientoNominalEquiposElectricos()
        else:
            self.rendimientoMedioText.Show(False)
            self.rendimietoMedio.Show(False)
            self.rendimientoMedioUnidadesText.Show(False)
            self.rendimientoCombustionText.Show(False)
            self.aislanteCaldera.Show(False)
            self.aislenteCalderaText.Show(False)
            self.rendimientoCombustion.Show(False)
            self.rendimientoCombustionUnidadesText.Show(False)
            self.cargaMediaText.Show(False)
            self.cargaMedia.Show(False)
            self.cargaMediaHelpButton.Show(False)
            self.definirCalderaBoton.Show(False)
            self.potenciaNominalText.Show(False)
            self.potenciaNominal.Show(False)
            self.potenciaNominalUnidadesText.Show(False)
            self.definirAntiguedadText.Show(False)
            self.definirAntiguedadChoice.Show(False)
            self.rendimientoNominalText.Show(False)
            self.rendimientoNominal.Show(False)
            self.rendimientoNominalUnidadesText.Show(False)
            self.ddaCubiertaBDCText.Show(False)
            self.ddaCubiertaBDC.Show(False)
            self.ddaCubiertaBDCPorcentaje.Show(False)
            self.rendimientoGlobalText.Show(True)
            self.rendimientoGlobal.Show(True)
            self.rendimientoGlobalUnidadesText.Show(True)
            self.potNominalText.Show(True)
            self.potNominal.Show(True)
            self.rendNominalPGText.Show(True)
            self.rendNominalPG.Show(True)
            self.factorCargaMinimoText.Show(True)
            self.factorCargaMinimo.Show(True)
            self.factorCargaMaximoText.Show(True)
            self.factorCargaMaximo.Show(True)
            self.factorCargaMaximo.Show(True)
            self.definirCurvaBoton.Show(True)
            self.rendNominalPGUnidadesText.Show(True)
            self.potNominalUnidadesText.Show(True)
            if 'Caldera' in self.generadorChoice.GetStringSelection():
                self.definirTemperaturasBoton.Show(True)
                self.temperaturaAmbienteIntUnidadesText.Show(False)
                self.temperaturaAmbienteIntText.Show(False)
                self.temperaturaAmbienteInt.Show(False)
            elif 'Bomba' in self.generadorChoice.GetStringSelection():
                self.definirTemperaturasBoton.Show(False)
                self.temperaturaAmbienteIntUnidadesText.Show(True)
                self.temperaturaAmbienteIntText.Show(True)
                self.temperaturaAmbienteInt.Show(True)
        self.obtenerRendimientoEstacional(None)
        return

    def OnAcumulacionCheck(self, event):
        """
        Metodo: OnAcumulacionCheck
        
        
        ARGUMENTOS:
                event:
        """
        if self.acumulacionCheck.GetValue() == True:
            self.temperaturaAltaText.Show(True)
            self.temperaturaAlta.Show(True)
            self.tempAltaUnidadesText.Show(True)
            self.temperaturaBajaText.Show(True)
            self.temperaturaBaja.Show(True)
            self.staticText1.Show(True)
            self.valorUAText.Show(True)
            self.valorUAChoice.Show(True)
            self.OnvalorUAChoice(None)
            self.UAText.Show(True)
            self.UAvalor.Show(True)
            self.UAUnidadesText.Show(True)
        else:
            self.volumenText.Show(False)
            self.volumen.Show(False)
            self.volumenUnidadesText.Show(False)
            self.multiplicadorText.Show(False)
            self.multiplicador.Show(False)
            self.temperaturaAltaText.Show(False)
            self.temperaturaAlta.Show(False)
            self.tempAltaUnidadesText.Show(False)
            self.temperaturaBajaText.Show(False)
            self.temperaturaBaja.Show(False)
            self.staticText1.Show(False)
            self.valorUAText.Show(False)
            self.valorUAChoice.Show(False)
            self.espesorAislamientoText.Show(False)
            self.espesorAislamiento.Show(False)
            self.espesorAislamientoUnidadesText.Show(False)
            self.tipoAislamientoText.Show(False)
            self.aislamientoAcumulacionChoice.Show(False)
            self.UAText.Show(False)
            self.UAvalor.Show(False)
            self.UAUnidadesText.Show(False)
        self.OnCalcularValorUAAcumulacion(None)
        return

    def OnvalorUAChoice(self, event):
        """
        Metodo: OnvalorUAChoice
        
        
        ARGUMENTOS:
                event:
        """
        if 'Conocido' in self.valorUAChoice.GetStringSelection():
            if self.acumulacionCheck.GetValue() == True:
                self.UAText.SetForegroundColour('black')
                self.UAText.SetLabel(_(u'UA'))
                self.UAvalor.Enable(True)
                self.UAUnidadesText.SetForegroundColour('black')
                self.UAUnidadesText.SetLabel(_(u'W/K'))
                self.espesorAislamientoText.Show(False)
                self.espesorAislamiento.Show(False)
                self.espesorAislamientoUnidadesText.Show(False)
                self.tipoAislamientoText.Show(False)
                self.aislamientoAcumulacionChoice.Show(False)
                self.volumenText.Show(False)
                self.volumen.Show(False)
                self.volumenUnidadesText.Show(False)
                self.multiplicadorText.Show(False)
                self.multiplicador.Show(False)
        elif 'Estimado' in self.valorUAChoice.GetStringSelection():
            if self.acumulacionCheck.GetValue() == True:
                self.UAText.SetForegroundColour(wx.Colour(100, 100, 100))
                self.UAText.SetLabel(_(u'UA'))
                self.UAvalor.Enable(False)
                self.UAUnidadesText.SetForegroundColour(wx.Colour(100, 100, 100))
                self.UAUnidadesText.SetLabel(_(u'W/K'))
                self.espesorAislamientoText.Show(True)
                self.espesorAislamiento.Show(True)
                self.espesorAislamientoUnidadesText.Show(True)
                self.tipoAislamientoText.Show(True)
                self.aislamientoAcumulacionChoice.Show(True)
                self.volumenText.Show(True)
                self.volumen.Show(True)
                self.volumenUnidadesText.Show(True)
                self.multiplicadorText.Show(True)
                self.multiplicador.Show(True)
        elif self.acumulacionCheck.GetValue() == True:
            self.UAText.SetForegroundColour(wx.Colour(100, 100, 100))
            self.UAText.SetLabel(_(u'UA'))
            self.UAvalor.Enable(False)
            self.UAUnidadesText.SetForegroundColour(wx.Colour(100, 100, 100))
            self.UAUnidadesText.SetLabel(_(u'W/K'))
            self.espesorAislamientoText.Show(False)
            self.espesorAislamiento.Show(False)
            self.espesorAislamientoUnidadesText.Show(False)
            self.tipoAislamientoText.Show(False)
            self.aislamientoAcumulacionChoice.Show(False)
            self.volumenText.Show(True)
            self.volumen.Show(True)
            self.volumenUnidadesText.Show(True)
            self.multiplicadorText.Show(True)
            self.multiplicador.Show(True)
        self.OnCalcularValorUAAcumulacion(None)
        return

    def OnCalcularValorUAAcumulacion(self, event):
        """
        Metodo: OnCalcularValorUAAcumulacion
        
        
        """
        UA = ''
        try:
            if 'Conocido' in self.valorUAChoice.GetStringSelection():
                UA = self.UAvalor.GetValue()
            else:
                volumen = float(self.volumen.GetValue()) / 1000.0
                r = 0.5
                h = volumen / (math.pi * r ** 2)
                multiplicador = float(self.multiplicador.GetValue())
                Area = (2 * math.pi * r ** 2 + 2 * math.pi * r * h) * multiplicador
                if self.valorUAChoice.GetStringSelection() == u'Por defecto':
                    Rtotal = 0.1 + 0.01 / 0.028
                    UA = 1 / Rtotal * Area
                else:
                    espesor = float(self.espesorAislamiento.GetValue())
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
            self.UAvalor.SetValue(str(round(float(UA), 1)))
        else:
            self.UAvalor.SetValue(UA)

    def comprobarDatos(self):
        """
        Metodo: comprobarDatos
        
        
        """
        dato = self.coberturaMetros.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.coberturaMetros.SetValue(dato)
        dato = self.coberturaPorcentaje.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.coberturaPorcentaje.SetValue(dato)
        dato = self.rendimietoMedio.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.rendimietoMedio.SetValue(dato)
        dato = self.rendimientoCombustion.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.rendimientoCombustion.SetValue(dato)
        dato = self.potenciaNominal.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.potenciaNominal.SetValue(dato)
        dato = self.cargaMedia.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.cargaMedia.SetValue(dato)
        dato = self.rendimientoNominal.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.rendimientoNominal.SetValue(dato)
        dato = self.volumen.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.volumen.SetValue(dato)
        dato = self.multiplicador.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.multiplicador.SetValue(dato)
        dato = self.temperaturaAlta.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.temperaturaAlta.SetValue(dato)
        dato = self.temperaturaBaja.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.temperaturaBaja.SetValue(dato)
        dato = self.UAvalor.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.UAvalor.SetValue(dato)
        dato = self.espesorAislamiento.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.espesorAislamiento.SetValue(dato)
        dato = self.rendNominalPG.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.rendNominalPG.SetValue(dato)
        dato = self.factorCargaMinimo.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.factorCargaMinimo.SetValue(dato)
        dato = self.factorCargaMaximo.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.factorCargaMaximo.SetValue(dato)
        dato = self.temperaturaAmbienteInt.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.temperaturaAmbienteInt.SetValue(dato)
        dato = self.potNominal.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.potNominal.SetValue(dato)
        dato = self.ddaCubiertaBDC.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.ddaCubiertaBDC.SetValue(dato)
        self.listaErrores = u''
        self.listaErrores += Comprueba(self.nombreInstalacion.GetValue(), 1, self.listaErrores, _(u'nombre')).ErrorDevuelto
        self.listaErrores += Comprueba(self.subgrupoChoice.GetStringSelection(), 0, self.listaErrores, _(u'zona')).ErrorDevuelto
        self.listaErrores += Comprueba(self.generadorChoice.GetStringSelection(), 0, self.listaErrores, _(u'tipo de generador')).ErrorDevuelto
        self.listaErrores += Comprueba(self.combustibleChoice.GetStringSelection(), 0, self.listaErrores, _(u'tipo de combustible')).ErrorDevuelto
        self.listaErrores += Comprueba(self.rendimientoChoice.GetStringSelection(), 0, self.listaErrores, _(u'definir rendimiento')).ErrorDevuelto
        if self.parent.parent.parent.panelDatosGenerales.superficie.GetValue() == '':
            self.listaErrores += Comprueba2(self.coberturaPorcentaje.GetValue(), 2, self.listaErrores, _(u'porcentaje de demanda de la zona cubierto'), 0, 100).ErrorDevuelto
        else:
            self.listaErrores += Comprueba2(self.coberturaPorcentaje.GetValue(), 2, self.listaErrores, _(u'porcentaje de demanda de la zona cubierto o m2 cubiertos por el equipo'), 0, 100).ErrorDevuelto
        rendi = self.rendimientoChoice.GetStringSelection()
        if u'Conocido' in rendi:
            self.listaErrores += Comprueba(self.rendimietoMedio.GetValue(), 2, self.listaErrores, _(u'rendimiento medio estacional'), 0).ErrorDevuelto
        elif u'Estimado seg\xfan Instalaci\xf3n' in rendi:
            if 'Caldera' in self.generadorChoice.GetStringSelection() and self.combustibleChoice.GetStringSelection() != u'Electricidad':
                self.listaErrores += Comprueba(self.aislanteCaldera.GetStringSelection(), 0, self.listaErrores, _(u'aislamiento de la caldera')).ErrorDevuelto
                self.listaErrores += Comprueba(self.rendimientoCombustion.GetValue(), 2, self.listaErrores, _(u'rendimiento de combusti\xf3n'), 0).ErrorDevuelto
                self.listaErrores += Comprueba(self.potenciaNominal.GetValue(), 2, self.listaErrores, _(u'potencia nominal'), 0).ErrorDevuelto
                self.listaErrores += Comprueba(self.cargaMedia.GetValue(), 2, self.listaErrores, _(u'carga media real \xdfcmb'), 0, 1).ErrorDevuelto
                if self.vectorTipoCaldera == []:
                    if self.listaErrores != u'':
                        self.listaErrores += u', '
                    self.listaErrores += _(u'caracter\xedsticas caldera')
            else:
                self.listaErrores += Comprueba(self.rendimientoNominal.GetValue(), 2, self.listaErrores, _(u'rendimiento nominal'), 0).ErrorDevuelto
        else:
            self.listaErrores += Comprueba(self.potNominal.GetValue(), 2, self.listaErrores, _(u'potencia nominal'), 0).ErrorDevuelto
            self.listaErrores += Comprueba(self.rendNominalPG.GetValue(), 2, self.listaErrores, _(u'rendimiento/COP nominal'), 0).ErrorDevuelto
            self.listaErrores += Comprueba2(self.factorCargaMinimo.GetValue(), 2, self.listaErrores, _(u'factor de carga parcial m\xednimo'), 0.0, 1.0).ErrorDevuelto
            if Comprueba2(self.factorCargaMinimo.GetValue(), 2, self.listaErrores, _(u'factor de carga parcial m\xednimo'), 0.0, 1.0).ErrorDevuelto == '':
                self.listaErrores += Comprueba(self.factorCargaMaximo.GetValue(), 2, self.listaErrores, _(u'factor de carga parcial m\xe1ximo'), float(self.factorCargaMinimo.GetValue()), 1.0).ErrorDevuelto
            else:
                self.listaErrores += Comprueba(self.factorCargaMaximo.GetValue(), 2, self.listaErrores, _(u'factor de carga parcial m\xe1ximo'), 0.0, 1.0).ErrorDevuelto
            if 'Bomba' in self.generadorChoice.GetStringSelection():
                self.listaErrores += Comprueba(self.temperaturaAmbienteInt.GetValue(), 2, self.listaErrores, _(u'temperatura acumulaci\xf3n'), 0).ErrorDevuelto
        if u'Conocido' not in rendi and self.listaErrores == '':
            if self.rendimientoEstacionalACS != '':
                self.listaErrores += Comprueba(str(self.rendimientoEstacionalACS), 2, self.listaErrores, _(u'rendimiento medio estacional'), 0.0).ErrorDevuelto
        if self.acumulacionCheck.GetValue() == True:
            self.listaErrores += Comprueba(self.temperaturaAlta.GetValue(), 2, self.listaErrores, _(u'T\xaa alta')).ErrorDevuelto
            self.listaErrores += Comprueba(self.temperaturaBaja.GetValue(), 2, self.listaErrores, _(u'T\xaa baja')).ErrorDevuelto
            self.listaErrores += Comprueba(self.valorUAChoice.GetStringSelection(), 0, self.listaErrores, _(u'valor UA')).ErrorDevuelto
            valorUA = self.valorUAChoice.GetStringSelection()
            if u'Conocido' in valorUA:
                self.listaErrores += Comprueba(self.UAvalor.GetValue(), 2, self.listaErrores, _(u'UA'), 0).ErrorDevuelto
            else:
                self.listaErrores += Comprueba(self.volumen.GetValue(), 2, self.listaErrores, _(u'volumen de un dep\xf3sito'), 0).ErrorDevuelto
                self.listaErrores += Comprueba(self.multiplicador.GetValue(), 2, self.listaErrores, _(u'multiplicador'), 0).ErrorDevuelto
                if u'Estimado' in valorUA:
                    self.listaErrores += Comprueba(self.espesorAislamiento.GetValue(), 2, self.listaErrores, _(u'espesor del aislamiento'), 0).ErrorDevuelto
            try:
                saltoTermico = float(self.temperaturaAlta.GetValue()) - float(self.temperaturaBaja.GetValue())
                if saltoTermico <= 0.0:
                    self.listaErrores += _(u'\nla temperatura de consiga alta debe ser mayor que la temperatura de consigna baja')
            except (ValueError, TypeError):
                pass

    def onCargaMediaHelpButton(self, event):
        """
        Metodo: onCargaMediaHelpButton
        
        
        ARGUMENTOS:
                event:
        """
        if self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection() == '' and self.parent.parent.parent.programa != 'Residencial' and self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection() == '':
            wx.MessageBox(_(u'Debe indicar la localizaci\xf3n del edificio y el perfil de uso en el panel de datos generales'), _(u'Estimaci\xf3n de la carga media estacional'))
        elif self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection() == '':
            wx.MessageBox(_(u'Debe indicar la localizaci\xf3n del edificio en el panel de datos generales'), _(u'Estimaci\xf3n de la carga media estacional'))
        elif self.parent.parent.parent.programa != 'Residencial' and self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection() == '':
            wx.MessageBox(_(u'Debe indicar el perfil de uso del edificio en el panel de datos generales'), _(u'Estimaci\xf3n de la carga media estacional'))
        else:
            ayuda = ayudaCargaParcialCalefaccion.Dialog1(self, self.arrayAyudaCalefaccion)
            ayuda.ShowModal()
            if ayuda.dev != []:
                self.cargaMedia.SetValue(ayuda.dev[1])
                self.arrayAyudaCalefaccion = [ayuda.dev[2], ayuda.dev[3]]