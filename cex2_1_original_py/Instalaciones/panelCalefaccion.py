# Embedded file name: Instalaciones\panelCalefaccion.pyc
"""
Modulo: panelCalefaccion.py

"""
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
import wx
import logging
wxID_PANEL1, wxID_PANEL1ACUMULACIONCHECK, wxID_PANEL1COBERTURA, wxID_PANEL1COMBUSTIBLECHOICE, wxID_PANEL1DEFINIRDEMANDARADIO, wxID_PANEL1DEFINIRMETROS2RADIO, wxID_PANEL1DEFINIRTEXT, wxID_PANEL1GENERADORCHOICE, wxID_PANEL1NOMBREINSTALACION, wxID_PANEL1NOMBREINSTALACIONTEXT, wxID_PANEL1RENDIMIENTOCHOICE, wxID_PANEL1RENDIMIENTOTEXT, wxID_PANEL1STATICTEXT1, wxID_PANEL1SUBGRUPOCHOICE, wxID_PANEL1SUBGRUPOTEXT, wxID_PANEL1TEMPALTAUNIDADESTEXT, wxID_PANEL1TEMPERATURAALTA, wxID_PANEL1TEMPERATURAALTATEXT, wxID_PANEL1TEMPERATURABAJA, wxID_PANEL1TEMPERATURABAJATEXT, wxID_PANEL1TIPOCOMBUSTIBLETEXT, wxID_PANEL1TIPOGENERADORTEXT, wxID_PANEL1VALORUACHOICE, wxID_PANEL1VALORUATEXT, wxID_PANEL1VOLUMEN, wxID_PANEL1VOLUMENTEXT, wxID_PANEL1VOLUMENUNIDADESTEXT, wxID_PANEL1CHOICE1, wxID_PANEL1RADIOBUTTON1, wxID_PANEL1ACUMULACIONTEXT, wxID_PANEL1CHOICE2, wxID_PANEL1ESPESORAISTEXT, wxID_PANEL1ESPESORAISLA, wxID_PANEL1ESTADOAISTEXT, wxID_PANEL1AISLANTEBUENORADIO, wxID_PANEL1AISLANTEREGULARRADIO, wxID_PANEL1AISLANTEMALORADIO, wxID_PANEL1TIPOAISTEXT, wxID_PANEL1AISLANTEPORIURETANO, wxID_PANEL1AISLANTERESINA, wxID_PANEL1AISLANTEPOLIURETANOPROYEC, wxID_PANEL1AISLANTEMESPUMA, wxID_PANEL1UATEXT, wxID_PANEL1UAVALOR, wxID_PANEL1ANOCALDERACHOICE, wxID_PANEL1ANOCALDERATEXT, wxID_PANEL1TIPOCALDERATEXT, wxID_PANEL1TIPOCALDERACHOICE, wxID_PANEL1RENDIMIENTOMEDIOTEXT, wxID_PANEL1RENDIMIENTOMEDIO, wxID_PANEL1RENDIMIENTOCOMBUSTEXT, wxID_PANEL1RENDIMIENTOCOMBUSUNITEXT, wxID_PANEL1RENDIMIENTOMCOMBUS, wxID_PANEL1POTENCIANOMINALTEXT, wxID_PANEL1POTENCIANOMINAL, wxID_PANEL1POTENCIANOMINALUNIDADESTEXT, wxID_PANEL1AISLANTECALDERATEXT, wxID_PANEL1AISLANTECALDE, wxID_PANEL1CARGAMEDIATEXT, wxID_PANEL1CARGAMEDIA, wxID_PANEL1TIPOCALDE1RADIO, wxID_PANEL1TIPOCALDE1TEXT, wxID_PANEL1DEFINIRBOTON, wxID_PANEL1RENDGLOBALTEXT, wxID_PANEL1RENDIMIENTOGLOBAL, wxID_PANEL1RENDGLOBALUNITEXT, wxID_PANEL1ANTIEQUIPOTEXT, wxID_PANEL1MENOS5ANOSRADIO, wxID_PANEL1ENTRE515RADIO, wxID_PANEL1AISLANTEMALORADIO, wxID_PANEL1COBERTURAPORCEN, wxID_PANEL1RENDIMIENTONOMINAL, wxID_PANEL1RENDNOMINALUNITEXT, wxID_PANEL1RENDNOMINALTEXT, wxID_PANEL1CARGAMEDIAHELPBUTTON, wxID_WXVARIOSGENERADORESCHECK, wxID_PANEL1FRACCIONPOTENCIAENTRADA, wxID_PANEL1FRACCIONPOTENCIA, wxID_PANEL1DDACUBIERTABDC, wxID_PANEL1POTNOMINALTEXT, wxID_PANEL1POTNOMINAL, wxID_PANEL1RENDNOMINALPGTEXT, wxID_PANEL1RENDNOMINALPG, wxID_PANEL1FACRTORGARGAMINTEXT, wxID_PANEL1FACRTORGARGAMIN, wxID_PANEL1FACRTORGARGAMAXTEXT, wxID_PANEL1FACRTORGARGAMAX, wxID_PANEL1DEFINIRTEMPERATURASBOTON, wxID_PANEL1DEFINIRCURVABOTON, wxID_PANEL1POTNOMINALUNIDADESTEXT, wxID_PANEL1RENDNOMINALPGUNIDADESTEXT, wxID_PANEL1TEMPAMBINTTEXT, wxID_PANEL1TEMPAMBINT, wxID_PANEL1TEMPAMBINTUNIDADESTEXT, wxID_DEMANDALINEATEXT, wxID_EFICIENCIALINEATEXT, wxID_CARACTERISTICASLINEATEXT, wxID_PANEL1ANTIGUEDADCHOICE, wxID_PANEL1DEFINIRTEXT2 = [ wx.NewId() for _init_ctrls in range(99) ]

class Panel1(wx.Panel):
    """
    Clase: Panel1 del modulo panelCalefaccion.py
    
    
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
        self.nombreInstalacion = wx.TextCtrl(id=wxID_PANEL1NOMBREINSTALACION, name=u'nombreInstalacion', parent=self, pos=wx.Point(170, 0), size=wx.Size(230, 21), style=0, value=_(u'S\xf3lo calefacci\xf3n'))
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
        self.definirText2 = wx.StaticText(id=wxID_PANEL1DEFINIRTEXT2, label=_(u'Calefacci\xf3n'), name=u'definirText', parent=self, pos=wx.Point(542, 39), size=wx.Size(70, 13), style=0)
        self.definirMetros2Radio = wx.StaticText(id=wxID_PANEL1DEFINIRMETROS2RADIO, label=_(u'Superficie (m2)'), name=u'definirMetros2Radio', parent=self, pos=wx.Point(435, 58), size=wx.Size(81, 13), style=wx.RB_GROUP)
        self.definirDemandaRadio = wx.StaticText(id=wxID_PANEL1RADIOBUTTON1, label=_(u'Porcentaje (%)'), name='definirDemandaRadio', parent=self, pos=wx.Point(435, 80), size=wx.Size(100, 13), style=0)
        self.coberturaMetros = wx.TextCtrl(id=wxID_PANEL1COBERTURA, name=u'coberturaMetros', parent=self, pos=wx.Point(540, 55), size=wx.Size(60, 21), style=0, value=u'')
        self.coberturaMetros.SetForegroundColour(wx.Colour(100, 200, 0))
        self.coberturaMetros.Bind(wx.EVT_TEXT, self.OnCobertura, id=wxID_PANEL1COBERTURA)
        self.coberturaPorcentaje = wx.TextCtrl(id=wxID_PANEL1COBERTURAPORCEN, name=u'coberturaPorcentaje', parent=self, pos=wx.Point(540, 77), size=wx.Size(60, 21), style=0, value=u'')
        self.coberturaPorcentaje.SetForegroundColour(wx.Colour(100, 200, 0))
        self.coberturaPorcentaje.Bind(wx.EVT_TEXT, self.OnCoberturaPorcentaje, id=wxID_PANEL1COBERTURAPORCEN)
        self.EficienciaLineaText = wx.StaticBox(id=wxID_EFICIENCIALINEATEXT, label=_(u'Rendimiento medio estacional'), name='EficienciaLineaText', parent=self, pos=wx.Point(0, 107), size=wx.Size(710, 135), style=0)
        self.EficienciaLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.EficienciaLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.rendimientoText = wx.StaticText(id=wxID_PANEL1RENDIMIENTOTEXT, label=_(u'Rendimiento estacional'), name=u'rendimientoText', parent=self, pos=wx.Point(15, 130), size=wx.Size(150, 25), style=0)
        self.rendimientoText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.rendimientoChoice = MiChoice(choices=self.parent.listadoOpcionesInstalaciones, id=wxID_PANEL1CHOICE1, name='rendimientoChoice', parent=self, pos=wx.Point(170, 128), size=wx.Size(220, 21), style=0)
        self.rendimientoChoice.SetSelection(1)
        self.rendimientoChoice.Bind(wx.EVT_CHOICE, self.OnrendimientoChoice, id=wxID_PANEL1CHOICE1)
        self.potenciaNominalText = wx.StaticText(id=wxID_PANEL1POTENCIANOMINALTEXT, label=_(u'Potencia nominal'), name=u'potenciaNominalText', parent=self, pos=wx.Point(15, 155), size=wx.Size(120, 13), style=0)
        self.potenciaNominalText.Show(False)
        self.potenciaNominal = wx.TextCtrl(id=wxID_PANEL1POTENCIANOMINAL, name=u'potenciaNominal', parent=self, pos=wx.Point(170, 153), size=wx.Size(60, 21), style=0, value='24.0')
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
        self.rendimientoCombustion.Show(False)
        self.rendimientoCombustion.SetValue('%s' % rendCombustionDefecto)
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
        self.definirAntiguedadText = wx.StaticText(id=wxID_PANEL1ANTIEQUIPOTEXT, label=_(u'Antig\xfcedad del equipo'), name=u'definirAntiguedadText', parent=self, pos=wx.Point(15, 155), size=wx.Size(120, 13), style=0)
        self.definirAntiguedadText.Show(False)
        self.definirAntiguedadChoice = MiChoice(choices=listadosWeb.listadoOpcionesAntiguedad, id=wxID_PANEL1ANTIGUEDADCHOICE, name=u'antiguedadChoice', parent=self, pos=wx.Point(170, 153), size=wx.Size(135, 21), style=0)
        self.definirAntiguedadChoice.SetSelection(2)
        self.definirAntiguedadChoice.Bind(wx.EVT_CHOICE, self.OnAntiguedadChoice, id=wxID_PANEL1ANTIGUEDADCHOICE)
        self.definirAntiguedadChoice.Show(False)
        self.rendimientoNominalText = wx.StaticText(id=wxID_PANEL1RENDNOMINALTEXT, label=_(u'Rendimiento nominal'), name=u'rendimientoNominalText', parent=self, pos=wx.Point(15, 180), size=wx.Size(140, 13), style=0)
        self.rendimientoNominalText.Show(False)
        self.rendimientoNominal = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTONOMINAL, name=u'rendimientoNominal', parent=self, pos=wx.Point(170, 178), size=wx.Size(60, 21), style=0, value='100.0')
        self.rendimientoNominal.SetForegroundColour(wx.Colour(100, 200, 0))
        self.rendimientoNominal.Show(False)
        self.rendimientoNominal.Bind(wx.EVT_TEXT, self.OnRendimientoNominal, id=wxID_PANEL1RENDIMIENTONOMINAL)
        self.rendimientoNominalUnidadesText = wx.StaticText(id=wxID_PANEL1RENDNOMINALUNITEXT, label=_(u'%'), name=u'rendimientoNominalUnidadesText', parent=self, pos=wx.Point(235, 180), size=wx.Size(15, 13), style=0)
        self.rendimientoNominalUnidadesText.Show(False)
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
        self.VariosGeneradoresCheck = wx.CheckBox(id=wxID_WXVARIOSGENERADORESCHECK, label=_(u'\xbfExisten varios generadores escalonados?'), name='VariosGeneradoresCheck', parent=self, pos=wx.Point(357, 155), size=wx.Size(300, 20), style=0)
        self.VariosGeneradoresCheck.Enable(True)
        self.VariosGeneradoresCheck.SetValue(False)
        self.VariosGeneradoresCheck.Show(False)
        self.VariosGeneradoresCheck.Bind(wx.EVT_CHECKBOX, self.OnVariosGeneradoresCheck, id=wxID_WXVARIOSGENERADORESCHECK)
        self.FraccionPotenciaText = wx.StaticText(id=-1, label=_(u'Fracci\xf3n de la potencia total que aporta este generador'), name='FraccionPotenciaText', parent=self, pos=wx.Point(357, 179), size=wx.Size(275, 13), style=0)
        self.FraccionPotenciaText.Show(False)
        self.fraccionPotenciaEntradaText = wx.StaticText(id=-1, label=_(u'Fracci\xf3n potencia total a la que entra este generador'), name='FraccionPotenciaEntradaText', parent=self, pos=wx.Point(357, 199), size=wx.Size(275, 13), style=0)
        self.fraccionPotenciaEntradaText.Show(False)
        self.ddaCubiertaBDCText = wx.StaticText(id=-1, label=_(u'Demanda cubierta'), name='DemandaCubiertaText', parent=self, pos=wx.Point(357, 219), size=wx.Size(275, 13), style=0)
        self.ddaCubiertaBDCText.Show(False)
        self.ddaCubiertaBDCPorcentaje = wx.StaticText(id=-1, label=_(u'%'), name='DemandaCubiertaText', parent=self, pos=wx.Point(682, 219), size=wx.Size(15, 13), style=0)
        self.ddaCubiertaBDCPorcentaje.Show(False)
        self.FraccionPotencia = wx.TextCtrl(id=wxID_PANEL1FRACCIONPOTENCIA, name=u'FraccionPotencia', parent=self, pos=wx.Point(637, 177), size=wx.Size(40, 15), style=0, value=u'1.0')
        self.FraccionPotencia.Show(False)
        self.FraccionPotencia.Bind(wx.EVT_TEXT, self.obtenerRendimientoEstacional, id=wxID_PANEL1FRACCIONPOTENCIA)
        self.fraccionPotenciaEntrada = wx.TextCtrl(id=wxID_PANEL1FRACCIONPOTENCIAENTRADA, name=u'FraccionPotenciaEntrada', parent=self, pos=wx.Point(637, 197), size=wx.Size(40, 15), style=0, value=u'0.0')
        self.fraccionPotenciaEntrada.Show(False)
        self.fraccionPotenciaEntrada.Bind(wx.EVT_TEXT, self.obtenerRendimientoEstacional, id=wxID_PANEL1FRACCIONPOTENCIAENTRADA)
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
        self.temperaturaAmbienteIntText = wx.StaticText(id=wxID_PANEL1TEMPAMBINTTEXT, label=_(u'Temperatura ambiente interior'), name=u'temperaturaAmbienteIntText', parent=self, pos=wx.Point(435, 155), size=wx.Size(150, 13), style=0)
        self.temperaturaAmbienteIntText.Show(False)
        self.temperaturaAmbienteInt = wx.TextCtrl(id=wxID_PANEL1TEMPAMBINT, name=u'temperaturaAmbienteIntText', parent=self, pos=wx.Point(617, 153), size=wx.Size(60, 16), style=0, value=u'20.0')
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

    def OnsubgrupoChoice(self, event):
        """
        Metodo: OnsubgrupoChoice
        Simplemente pone el valor del porcentaje al 100%, el .SetValue() llama al evento asociado,
        en este caso OncoberturaPorcentaje()
        
        ARGUMENTOS:
                event:
        """
        self.coberturaPorcentaje.SetValue('100')

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

    def OnNombreInstalacion(self, event):
        """
        Metodo: OnNombreInstalacion
        
        
        ARGUMENTOS:
                event:
        """
        if self.nombreInstalacion.GetValue() == _(u'S\xf3lo calefacci\xf3n'):
            self.nombreInstalacion.SetForegroundColour(wx.Colour(100, 200, 0))
        else:
            self.nombreInstalacion.SetForegroundColour(wx.Colour(0, 0, 0))

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
            self.temperaturas[0] = float(dlg.dev[0])
            self.temperaturas[1] = float(dlg.dev[1])
            self.temperaturas[2] = float(dlg.dev[2])
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
        """
        Metodo: OnVariosGeneradoresCheck
        
        
        ARGUMENTOS:
                event:
        """
        self.obtenerRendimientoEstacional(event)
        if self.combustibleChoice.GetStringSelection() == u'Electricidad' and self.generadorChoice.GetStringSelection() != u'Equipo de Rendimiento Constante' and u'Estimado seg\xfan Instalaci\xf3n' in self.rendimientoChoice.GetStringSelection():
            if self.VariosGeneradoresCheck.GetValue() == True:
                self.FraccionPotenciaText.Show(True)
                self.fraccionPotenciaEntradaText.Show(True)
                self.fraccionPotenciaEntrada.Show(True)
                self.FraccionPotencia.Show(True)
                self.ddaCubiertaBDCText.Show(True)
                self.ddaCubiertaBDC.Show(True)
                self.ddaCubiertaBDCPorcentaje.Show(True)
            else:
                self.FraccionPotenciaText.Show(False)
                self.fraccionPotenciaEntradaText.Show(False)
                self.fraccionPotenciaEntrada.Show(False)
                self.FraccionPotencia.Show(False)
                self.ddaCubiertaBDCText.Show(False)
                self.ddaCubiertaBDC.Show(False)
                self.ddaCubiertaBDCPorcentaje.Show(False)
        else:
            self.FraccionPotenciaText.Show(False)
            self.fraccionPotenciaEntradaText.Show(False)
            self.fraccionPotenciaEntrada.Show(False)
            self.FraccionPotencia.Show(False)
            self.ddaCubiertaBDCText.Show(False)
            self.ddaCubiertaBDC.Show(False)
            self.ddaCubiertaBDCPorcentaje.Show(False)

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
        """
        Metodo: obtenerRendimientoEstacional
        Esta funcion calcula el rendimiento medio estacional en funcion de las caracter\xedsticas
        del generadro
        
        
        ARGUMENTOS:
                event: No se hace nada con el   
        """
        kwargsCalderaEst = {'aislanteCaldera': self.aislanteCaldera.GetStringSelection(),
         'rendCombCaldera': self.rendimientoCombustion.GetValue(),
         'potenciaCaldera': self.potenciaNominal.GetValue(),
         'cargaMediaCaldera': self.cargaMedia.GetValue()}
        kwargsConocido = {'rendEstACS': '',
         'rendEstCal': self.rendimietoMedio.GetValue(),
         'rendEstRef': ''}
        kwargsJouleEst = {'rendNominal': self.rendimientoNominal.GetValue()}
        fraccionPotencia = self.FraccionPotencia.GetValue().replace(',', '.')
        fraccionPotenciaEntrada = self.fraccionPotenciaEntrada.GetValue().replace(',', '.')
        kwargsBdCEst = {'rendNominalACS': '',
         'rendNominalCal': self.rendimientoNominal.GetValue(),
         'rendNominalRef': '',
         'variosGeneradoresCheck': self.VariosGeneradoresCheck.GetValue(),
         'fraccionPotencia': fraccionPotencia,
         'fraccionPotenciaEntrada': fraccionPotenciaEntrada}
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
        resultado = calculoRendimientoMedioEstacional(zonaHE1=zonaHE1, programa=programa, tipoEdificio=tipoEdificio, tipoInstalacion=self.tipoSistema, modoDefinicion=modoDefinicion, tipoEquipo=tipoEquipo, combustible=combustible, **kwargs)
        if modoDefinicion == u'Estimado seg\xfan Instalaci\xf3n' and tipoEquipo not in (u'Caldera Est\xe1ndar', u'Caldera Condensaci\xf3n', u'Caldera Baja Temperatura', u'Efecto Joule', u'Equipo de Rendimiento Constante'):
            self.rendimientoEstacionalCal, fraccionEnergia = resultado
            if self.VariosGeneradoresCheck.GetValue() == True:
                self.ddaCubiertaBDC.SetValue(str(round(sum(fraccionEnergia) * 100.0, 1)))
        else:
            self.rendimientoEstacionalCal = resultado
        self.escribirRendimientoGlobal()

    def escribirRendimientoGlobal(self):
        """
        Metodo: escribirRendimientoGlobal
        
        
        """
        self.rendimientoGlobal.SetValue(str(self.rendimientoEstacionalCal))

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
                self.rendNominalPGText.SetPosition(wx.Point(15, 176))
            elif self.generadorChoice.GetStringSelection() == u'Equipo de Rendimiento Constante':
                self.rendNominalPGText.SetLabel(_(u'Rendimiento nominal a plena carga'))
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
        """
        M\xe9todo: actualizarRendimientoNominalEquiposElectricos
        Si ha cambiado a equipo efecto joule o caldera, en rendimiento nominal se pone 100 %
        
        """
        try:
            float(self.rendimientoNominal.GetValue())
            valorValido = True
        except:
            logging.info(u'Excepcion en: %s' % __name__)
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

    def OnrendimientoChoice(self, event):
        """
        Metodo: OnrendimientoChoice
        
        
        ARGUMENTOS:
                event:
        Se llama al cambiar de tipo de equipo, de tipo de combustible o de modoDefini\xf3n
        Indica qu\xe9 se tiene que mostrar y que no
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
            self.rendNominalPGUnidadesText.Show(False)
            self.temperaturaAmbienteIntUnidadesText.Show(False)
            self.temperaturaAmbienteIntText.Show(False)
            self.temperaturaAmbienteInt.Show(False)
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
            self.VariosGeneradoresCheck.Show(False)
            self.FraccionPotenciaText.Show(False)
            self.fraccionPotenciaEntradaText.Show(False)
            self.fraccionPotenciaEntrada.Show(False)
            self.FraccionPotencia.Show(False)
            self.ddaCubiertaBDCText.Show(False)
            self.ddaCubiertaBDC.Show(False)
            self.ddaCubiertaBDCPorcentaje.Show(False)
            self.potNominalUnidadesText.Show(False)
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
            self.rendNominalPGUnidadesText.Show(False)
            self.potNominalUnidadesText.Show(False)
            self.temperaturaAmbienteIntUnidadesText.Show(False)
            self.temperaturaAmbienteIntText.Show(False)
            self.temperaturaAmbienteInt.Show(False)
            self.rendimientoMedioText.Show(False)
            self.rendimietoMedio.Show(False)
            self.rendimientoMedioUnidadesText.Show(False)
            self.rendimientoGlobalText.Show(True)
            self.rendimientoGlobal.Show(True)
            self.rendimientoGlobalUnidadesText.Show(True)
            if 'Caldera' in self.generadorChoice.GetStringSelection() and self.combustibleChoice.GetStringSelection() != u'Electricidad':
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
                self.VariosGeneradoresCheck.Show(False)
                self.FraccionPotenciaText.Show(False)
                self.fraccionPotenciaEntradaText.Show(False)
                self.fraccionPotenciaEntrada.Show(False)
                self.FraccionPotencia.Show(False)
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
                    self.VariosGeneradoresCheck.Show(False)
                    self.VariosGeneradoresCheck.SetValue(False)
                else:
                    self.definirAntiguedadText.Show(True)
                    self.definirAntiguedadChoice.Show(True)
                    self.VariosGeneradoresCheck.Show(True)
                self.rendimientoNominalText.Show(True)
                self.rendimientoNominal.Show(True)
                self.rendimientoNominalUnidadesText.Show(True)
                self.OnVariosGeneradoresCheck(None)
                self.actualizarRendimientoNominalEquiposElectricos()
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
            self.definirAntiguedadText.Show(False)
            self.definirAntiguedadChoice.Show(False)
            self.rendimientoNominalText.Show(False)
            self.rendimientoNominal.Show(False)
            self.rendimientoNominalUnidadesText.Show(False)
            self.VariosGeneradoresCheck.Show(False)
            self.rendimientoMedioText.Show(False)
            self.rendimietoMedio.Show(False)
            self.rendimientoMedioUnidadesText.Show(False)
            self.rendimientoGlobalText.Show(True)
            self.rendimientoGlobal.Show(True)
            self.rendimientoGlobalUnidadesText.Show(True)
            self.rendimientoNominalText.Show(False)
            self.rendimientoNominal.Show(False)
            self.rendimientoNominalUnidadesText.Show(False)
            self.FraccionPotenciaText.Show(False)
            self.fraccionPotenciaEntradaText.Show(False)
            self.fraccionPotenciaEntrada.Show(False)
            self.FraccionPotencia.Show(False)
            self.ddaCubiertaBDCText.Show(False)
            self.ddaCubiertaBDC.Show(False)
            self.ddaCubiertaBDCPorcentaje.Show(False)
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

    def comprobarDatos(self):
        """
        Metodo: comprobarDatos
        
        
        """
        dato = self.potNominal.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.potNominal.SetValue(dato)
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
        dato = self.FraccionPotencia.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.FraccionPotencia.SetValue(dato)
        dato = self.fraccionPotenciaEntrada.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.fraccionPotenciaEntrada.SetValue(dato)
        dato = self.ddaCubiertaBDC.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.ddaCubiertaBDC.SetValue(dato)
        dato = self.temperaturaAmbienteInt.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.temperaturaAmbienteInt.SetValue(dato)
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
        if 'Conocido' in rendi:
            self.listaErrores += Comprueba(self.rendimietoMedio.GetValue(), 2, self.listaErrores, _(u'rendimiento medio estacional'), 0).ErrorDevuelto
        elif u'Estimado seg\xfan Instalaci\xf3n' in rendi:
            if 'Caldera' in self.generadorChoice.GetStringSelection():
                self.listaErrores += Comprueba(self.aislanteCaldera.GetStringSelection(), 0, self.listaErrores, _(u'aislamiento de la caldera')).ErrorDevuelto
                self.listaErrores += Comprueba(self.rendimientoCombustion.GetValue(), 2, self.listaErrores, _(u'rendimiento de combusti\xf3n'), 0).ErrorDevuelto
                self.listaErrores += Comprueba(self.potenciaNominal.GetValue(), 2, self.listaErrores, _(u'potencia nominal'), 0).ErrorDevuelto
                self.listaErrores += Comprueba(self.cargaMedia.GetValue(), 2, self.listaErrores, _(u'carga media real \xdfcmb'), 0, 1).ErrorDevuelto
                if self.vectorTipoCaldera == []:
                    if self.listaErrores != u'':
                        self.listaErrores += u', '
                    self.listaErrores += _(u'caracter\xedsticas caldera')
            else:
                self.listaErrores += Comprueba(self.rendimientoNominal.GetValue(), 2, self.listaErrores, _(u'rendimiento nominal'), 0.0).ErrorDevuelto
                if self.VariosGeneradoresCheck.GetValue() == True:
                    errorFraccionPotencia = Comprueba(self.FraccionPotencia.GetValue(), 2, self.listaErrores, _(u'fracci\xf3n de la potencia que aporta el generador'), 0.0, 1.0).ErrorDevuelto
                    self.listaErrores += errorFraccionPotencia
                    errorFraccionEntrada = Comprueba2(self.fraccionPotenciaEntrada.GetValue(), 2, self.listaErrores, _(u'fracci\xf3n de la potencia a la que entra el generador'), 0.0, 1.0).ErrorDevuelto
                    self.listaErrores += errorFraccionEntrada
        else:
            self.listaErrores += Comprueba(self.potNominal.GetValue(), 2, self.listaErrores, _(u'potencia nominal'), 0).ErrorDevuelto
            self.listaErrores += Comprueba(self.rendNominalPG.GetValue(), 2, self.listaErrores, _(u'rendimiento/COP nominal'), 0).ErrorDevuelto
            self.listaErrores += Comprueba2(self.factorCargaMinimo.GetValue(), 2, self.listaErrores, _(u'factor de carga parcial m\xednimo'), 0.0, 1.0).ErrorDevuelto
            if Comprueba2(self.factorCargaMinimo.GetValue(), 2, self.listaErrores, _(u'factor de carga parcial m\xednimo'), 0.0, 1.0).ErrorDevuelto == '':
                self.listaErrores += Comprueba(self.factorCargaMaximo.GetValue(), 2, self.listaErrores, _(u'factor de carga parcial m\xe1ximo'), float(self.factorCargaMinimo.GetValue()), 1.0).ErrorDevuelto
            else:
                self.listaErrores += Comprueba(self.factorCargaMaximo.GetValue(), 2, self.listaErrores, _(u'factor de carga parcial m\xe1ximo'), 0.0, 1.0).ErrorDevuelto
            if 'Bomba' in self.generadorChoice.GetStringSelection():
                self.listaErrores += Comprueba(self.temperaturaAmbienteInt.GetValue(), 2, self.listaErrores, _(u'temperatura ambiente interior'), 0).ErrorDevuelto
        if u'Conocido' not in rendi and self.listaErrores == '':
            if self.rendimientoEstacionalCal != '':
                self.listaErrores += Comprueba(str(self.rendimientoEstacionalCal), 2, self.listaErrores, _(u'rendimiento medio estacional'), 0.0).ErrorDevuelto

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