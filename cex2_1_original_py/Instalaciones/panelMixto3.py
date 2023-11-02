# Embedded file name: Instalaciones\panelMixto3.pyc
"""
Modulo: panelMixto3.py

"""
from Calculos.funcionesCalculo import diccCOPNominalDefecto, diccEERNominalDefecto
from Instalaciones.comprobarCampos import Comprueba, Comprueba2
from Instalaciones.funcionCalculoRendimientoEstacional import calculoRendimientoMedioEstacional
from miChoice import MiChoice
import Calculos.listadosWeb as listadosWeb
import Instalaciones.equipos as equipos
import math
import wx
import logging
wxID_PANEL1, wxID_PANEL1ACUMULACIONCHECK, wxID_PANEL1COBERTURA, wxID_PANEL1COMBUSTIBLECHOICE, wxID_PANEL1DEFINIRDEMANDARADIO, wxID_PANEL1DEFINIRMETROS2RADIO, wxID_PANEL1DEFINIRTEXT, wxID_PANEL1GENERADORCHOICE, wxID_PANEL1METROSUNIDADESTEXT, wxID_PANEL1NOMBREINSTALACION, wxID_PANEL1NOMBREINSTALACIONTEXT, wxID_PANEL1PORCENTAJEUNIDADESTEXT, wxID_PANEL1RENDIMIENTOCHOICE, wxID_PANEL1RENDIMIENTOTEXT, wxID_PANEL1STATICTEXT1, wxID_PANEL1SUBGRUPOCHOICE, wxID_PANEL1SUBGRUPOTEXT, wxID_PANEL1TEMPALTAUNIDADESTEXT, wxID_PANEL1TEMPERATURAALTA, wxID_PANEL1TEMPERATURAALTATEXT, wxID_PANEL1TEMPERATURABAJA, wxID_PANEL1TEMPERATURABAJATEXT, wxID_PANEL1TIPOCOMBUSTIBLETEXT, wxID_PANEL1TIPOGENERADORTEXT, wxID_PANEL1VALORUACHOICE, wxID_PANEL1VALORUATEXT, wxID_PANEL1VOLUMEN, wxID_PANEL1VOLUMENTEXT, wxID_PANEL1VOLUMENUNIDADESTEXT, wxID_PANEL1CHOICE1, wxID_PANEL1RADIOBUTTON1, wxID_PANEL1ACUMULACIONTEXT, wxID_PANEL1CHOICE2, wxID_PANEL1ESPESORAISTEXT, wxID_PANEL1ESPESORAISLA, wxID_PANEL1ESTADOAISTEXT, wxID_PANEL1AISLANTEBUENORADIO, wxID_PANEL1AISLANTEREGULARRADIO, wxID_PANEL1AISLANTEMALORADIO, wxID_PANEL1TIPOAISTEXT, wxID_PANEL1AISLANTEPORIURETANO, wxID_PANEL1AISLANTERESINA, wxID_PANEL1AISLANTEPOLIURETANOPROYEC, wxID_PANEL1AISLANTEMESPUMA, wxID_PANEL1UATEXT, wxID_PANEL1UAVALOR, wxID_PANEL1ANOCALDERACHOICE, wxID_PANEL1ANOCALDERATEXT, wxID_PANEL1TIPOCALDERATEXT, wxID_PANEL1TIPOCALDERACHOICE, wxID_PANEL1RENDIMIENTOMEDIOTEXT, wxID_PANEL1RENDIMIENTOMEDIO, wxID_PANEL1RENDIMIENTOCOMBUSTEXT, wxID_PANEL1RENDIMIENTOCOMBUSUNITEXT, wxID_PANEL1RENDIMIENTOMCOMBUS, wxID_PANEL1AISLANTECALDERATEXT, wxID_PANEL1AISLANTECALDE, wxID_PANEL1CARGAMEDIATEXT, wxID_PANEL1CARGAMEDIA, wxID_PANEL1TIPOCALDE1RADIO, wxID_PANEL1TIPOCALDE1TEXT, wxID_PANEL1DEFINIRBOTON, wxID_PANEL1RENDNOMINALTEXT, wxID_PANEL1RENDIMIENTONOMINAL, wxID_PANEL1RENDNOMINALUNITEXT, wxID_PANEL1DEFINIRMETROS2RADIO2, wxID_PANEL1RADIOBUTTON12, wxID_PANEL1COBERTURA2, wxID_PANEL1METROSUNIDADESTEXT2, wxID_PANEL1PORCENTAJEUNIDADESTEXT2, wxID_PANEL1ANTIEQUIPOTEXT, wxID_PANEL1MENOS5ANOSRADIO, wxID_PANEL1ENTRE515RADIO, wxID_PANEL1AISLANTEMALORADIO, wxID_PANEL1STATICLINE1, wxID_PANEL1CALEFACTEXT, wxID_PANEL1STATICLINE2, wxID_PANEL1REFRIGTEXT, wxID_PANEL1ACSEXT, wxID_PANEL1DEFINIRMETROS2RADIO2, wxID_PANEL1RADIOBUTTON12, wxID_PANEL1COBERTURA2, wxID_PANEL1METROSUNIDADESTEXT2, wxID_PANEL1PORCENTAJEUNIDADESTEXT2, wxID_PANEL1RENDNOMINALTEXT2, wxID_PANEL1RENDIMIENTONOMINAL2, wxID_PANEL1RENDNOMINALUNITEXT2, wxID_PANEL1RENDIMIENTOMEDIOTEXT2, wxID_PANEL1RENDIMIENTOMEDIO2, wxID_PANEL1RENDIMIENTOMEDIOTEXT2, wxID_PANEL1DEFINIRMETROS2RADIO3, wxID_PANEL1RADIOBUTTON13, wxID_PANEL1COBERTURA3, wxID_PANEL1METROSUNIDADESTEXT3, wxID_PANEL1PORCENTAJEUNIDADESTEXT3, wxID_PANEL1RENDNOMINALTEXT3, wxID_PANEL1RENDIMIENTONOMINAL3, wxID_PANEL1RENDNOMINALUNITEXT3, wxID_PANEL1RENDIMIENTOMEDIOTEXT3, wxID_PANEL1RENDIMIENTOMEDIO3, wxID_PANEL1RENDIMIENTOMEDIOTEXT3, wxID_PANEL1DEFINIRMETROS2RADIO3, wxID_PANEL1RADIOBUTTON13, wxID_PANEL1COBERTURA3, wxID_PANEL1METROSUNIDADESTEXT3, wxID_PANEL1PORCENTAJEUNIDADESTEXT3, wxID_PANEL1RENDIMIENTOGLOBALTEXT, wxID_PANEL1RENDIMIENTOGLOBAL, wxID_PANEL1RENDIMIENTOGLOBALTEXT, wxID_PANEL1RENDIMIENTOGLOBALTEXT2, wxID_PANEL1RENDIMIENTOGLOBAL2, wxID_PANEL1RENDIMIENTOGLOBALTEXT2, wxID_PANEL1RENDIMIENTOGLOBALTEXT3, wxID_PANEL1RENDIMIENTOGLOBAL3, wxID_PANEL1RENDIMIENTOGLOBALTEXT3, wxID_PANEL1AISLAMIENTOACUMULACIONCHOICE, wxID_CARACTERISTICASLINEATEXT, wxID_DEMANDALINEATEXT, wxID_PANEL1DEFINIRTEXT2, wxID_PANEL1DEFINIRTEXT3, wxID_EFICIENCIALINEATEXT, wxID_PANEL1COBERTURAPORCEN3, wxID_PANEL1COBERTURAPORCEN2, wxID_PANEL1COBERTURAPORCEN, wxID_ACUMULACIONLINEATEXT, wxID_PANEL1ANTIGUEDADCHOICE, wxID_PANEL1MULTIPLICADORTEXT, wxID_PANEL1MULTIPLICADOR = [ wx.NewId() for _init_ctrls in range(128) ]

class Panel1(wx.Panel):
    """
    Clase: Panel1 del modulo panelMixto3.py
    
    
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
        self.nombreInstalacion = wx.TextCtrl(id=wxID_PANEL1NOMBREINSTALACION, name=u'nombreInstalacion', parent=self, pos=wx.Point(170, 0), size=wx.Size(230, 21), style=0, value=_(u'Calefacci\xf3n,  refrigeraci\xf3n y ACS'))
        self.nombreInstalacion.SetForegroundColour(wx.Colour(100, 200, 0))
        self.nombreInstalacion.Bind(wx.EVT_TEXT, self.OnNombreInstalacion, id=wxID_PANEL1NOMBREINSTALACION)
        self.subgrupoText = wx.StaticText(id=wxID_PANEL1SUBGRUPOTEXT, label=_(u'Zona'), name=u'subgrupoText', parent=self, pos=wx.Point(435, 2), size=wx.Size(60, 13), style=0)
        self.subgrupoChoice = MiChoice(choices=[], id=wxID_PANEL1SUBGRUPOCHOICE, name=u'subgrupoChoice', parent=self, pos=wx.Point(496, 0), size=wx.Size(200, 21), style=0)
        self.subgrupoChoice.Bind(wx.EVT_CHOICE, self.OnsubgrupoChoice, id=wxID_PANEL1SUBGRUPOCHOICE)
        self.tipoGeneradorText = wx.StaticText(id=wxID_PANEL1TIPOGENERADORTEXT, label=_(u'Tipo de generador'), name=u'tipoGeneradorText', parent=self, pos=wx.Point(15, 46), size=wx.Size(102, 13), style=0)
        self.CaracteristicasLineaText = wx.StaticBox(id=wxID_CARACTERISTICASLINEATEXT, label=_(u'Caracter\xedsticas'), name='CaracteristicasLineaText', parent=self, pos=wx.Point(0, 26), size=wx.Size(400, 77), style=0)
        self.CaracteristicasLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.generadorChoice = MiChoice(choices=listadosWeb.listadoInstalacionesClimatizacion, id=wxID_PANEL1GENERADORCHOICE, name=u'generadorChoice', parent=self, pos=wx.Point(170, 44), size=wx.Size(200, 21), style=0)
        self.generadorChoice.SetSelection(0)
        self.generadorChoice.Bind(wx.EVT_CHOICE, self.OngeneradorChoice, id=wxID_PANEL1GENERADORCHOICE)
        self.tipoCombustibleText = wx.StaticText(id=wxID_PANEL1TIPOCOMBUSTIBLETEXT, label=_(u'Tipo de combustible'), name=u'tipoCombustibleText', parent=self, pos=wx.Point(15, 71), size=wx.Size(110, 13), style=0)
        self.combustibleChoice = MiChoice(choices=listadosWeb.listadoCombustibles, id=wxID_PANEL1COMBUSTIBLECHOICE, name=u'combustibleChoice', parent=self, pos=wx.Point(170, 69), size=wx.Size(200, 21), style=0)
        self.combustibleChoice.SetSelection(2)
        self.combustibleChoice.Bind(wx.EVT_CHOICE, self.obtenerRendimientoEstacional, id=wxID_PANEL1COMBUSTIBLECHOICE)
        self.DemandaLineaText = wx.StaticBox(id=wxID_DEMANDALINEATEXT, label=_(u'Demanda cubierta'), name='DemandaLineaText', parent=self, pos=wx.Point(425, 26), size=wx.Size(285, 77), style=0)
        self.DemandaLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.DemandaLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.definirText3 = wx.StaticText(id=wxID_PANEL1DEFINIRTEXT3, label=_(u'ACS'), name=u'definirText', parent=self, pos=wx.Point(537, 39), size=wx.Size(40, 13), style=0)
        self.definirText = wx.StaticText(id=wxID_PANEL1DEFINIRTEXT, label=_(u'Calefacci\xf3n'), name=u'definirText', parent=self, pos=wx.Point(585, 39), size=wx.Size(70, 13), style=0)
        self.definirText2 = wx.StaticText(id=wxID_PANEL1DEFINIRTEXT2, label=_(u'Refrigeraci\xf3n'), name=u'definirText', parent=self, pos=wx.Point(643, 39), size=wx.Size(66, 13), style=0)
        self.definirMetros2Radio = wx.StaticText(id=wxID_PANEL1DEFINIRMETROS2RADIO, label=_(u'Superficie (m2)'), name=u'definirMetros2Radio', parent=self, pos=wx.Point(435, 58), size=wx.Size(81, 13), style=wx.RB_GROUP)
        self.definirDemandaRadio = wx.StaticText(id=wxID_PANEL1RADIOBUTTON1, label=_(u'Porcentaje (%)'), name='definirDemandaRadio', parent=self, pos=wx.Point(435, 80), size=wx.Size(80, 13), style=0)
        self.coberturaMetros3 = wx.TextCtrl(id=wxID_PANEL1COBERTURA3, name=u'cobertura3', parent=self, pos=wx.Point(520, 55), size=wx.Size(55, 21), style=0, value=u'')
        self.coberturaMetros3.SetForegroundColour(wx.Colour(100, 200, 0))
        self.coberturaMetros3.Bind(wx.EVT_TEXT, self.OnCobertura3, id=wxID_PANEL1COBERTURA3)
        self.coberturaPorcentaje3 = wx.TextCtrl(id=wxID_PANEL1COBERTURAPORCEN3, name=u'coberturaPorcentaje3', parent=self, pos=wx.Point(520, 77), size=wx.Size(55, 21), style=0, value=u'')
        self.coberturaPorcentaje3.SetForegroundColour(wx.Colour(100, 200, 0))
        self.coberturaPorcentaje3.Bind(wx.EVT_TEXT, self.OnCoberturaPorcentaje3, id=wxID_PANEL1COBERTURAPORCEN3)
        self.coberturaMetros = wx.TextCtrl(id=wxID_PANEL1COBERTURA, name=u'cobertura', parent=self, pos=wx.Point(585, 55), size=wx.Size(55, 21), style=0, value=u'')
        self.coberturaMetros.Bind(wx.EVT_TEXT, self.OnCobertura, id=wxID_PANEL1COBERTURA)
        self.coberturaMetros.SetForegroundColour(wx.Colour(100, 200, 0))
        self.coberturaPorcentaje = wx.TextCtrl(id=wxID_PANEL1COBERTURAPORCEN, name=u'coberturaPorcentaje', parent=self, pos=wx.Point(585, 77), size=wx.Size(55, 21), style=0, value=u'')
        self.coberturaPorcentaje.SetForegroundColour(wx.Colour(100, 200, 0))
        self.coberturaPorcentaje.Bind(wx.EVT_TEXT, self.OnCoberturaPorcentaje, id=wxID_PANEL1COBERTURAPORCEN)
        self.coberturaMetros2 = wx.TextCtrl(id=wxID_PANEL1COBERTURA2, name=u'coberturaMetros2', parent=self, pos=wx.Point(650, 55), size=wx.Size(55, 21), style=0, value=u'')
        self.coberturaMetros2.SetForegroundColour(wx.Colour(100, 200, 0))
        self.coberturaMetros2.Bind(wx.EVT_TEXT, self.OnCobertura2, id=wxID_PANEL1COBERTURA2)
        self.coberturaPorcentaje2 = wx.TextCtrl(id=wxID_PANEL1COBERTURAPORCEN2, name=u'coberturaPorcentaje2', parent=self, pos=wx.Point(650, 77), size=wx.Size(55, 21), style=0, value=u'')
        self.coberturaPorcentaje2.SetForegroundColour(wx.Colour(100, 200, 0))
        self.coberturaPorcentaje2.Bind(wx.EVT_TEXT, self.OnCoberturaPorcentaje2, id=wxID_PANEL1COBERTURAPORCEN2)
        self.EficienciaLineaText = wx.StaticBox(id=wxID_EFICIENCIALINEATEXT, label=_(u'Rendimiento medio estacional'), name='EficienciaLineaText', parent=self, pos=wx.Point(0, 107), size=wx.Size(710, 135), style=0)
        self.EficienciaLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.EficienciaLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.rendimientoText = wx.StaticText(id=wxID_PANEL1RENDIMIENTOTEXT, label=_(u'Rendimiento estacional'), name=u'rendimientoText', parent=self, pos=wx.Point(15, 130), size=wx.Size(102, 13), style=0)
        self.rendimientoText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.rendimientoChoice = MiChoice(choices=self.parent.listadoOpcionesInstalacionesMixtos, id=wxID_PANEL1CHOICE1, name='rendimientoChoice', parent=self, pos=wx.Point(170, 128), size=wx.Size(200, 21), style=0)
        self.rendimientoChoice.SetSelection(1)
        self.rendimientoChoice.Bind(wx.EVT_CHOICE, self.OnrendimientoChoice, id=wxID_PANEL1CHOICE1)
        self.definirAntiguedadText = wx.StaticText(id=wxID_PANEL1ANTIEQUIPOTEXT, label=_(u'Antig\xfcedad del equipo'), name=u'definirAntiguedadText', parent=self, pos=wx.Point(15, 155), size=wx.Size(120, 13), style=0)
        self.definirAntiguedadText.Show(False)
        self.definirAntiguedadChoice = MiChoice(choices=listadosWeb.listadoOpcionesAntiguedad, id=wxID_PANEL1ANTIGUEDADCHOICE, name=u'antiguedadChoice', parent=self, pos=wx.Point(170, 153), size=wx.Size(135, 21), style=0)
        self.definirAntiguedadChoice.SetSelection(2)
        self.definirAntiguedadChoice.Bind(wx.EVT_CHOICE, self.OnAntiguedadChoice, id=wxID_PANEL1ANTIGUEDADCHOICE)
        self.definirAntiguedadChoice.Show(False)
        self.ACSText = wx.StaticText(id=wxID_PANEL1ACSEXT, label=_(u'A.C.S'), name=u'calefaccionText', parent=self, pos=wx.Point(15, 180), size=wx.Size(14, 13), style=0)
        self.ACSText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, u''))
        self.ACSText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.rendimientoNominalText3 = wx.StaticText(id=wxID_PANEL1RENDNOMINALTEXT3, label=_(u'Rendimiento nominal'), name=u'rendimientoNominalText3', parent=self, pos=wx.Point(170, 180), size=wx.Size(100, 13), style=0)
        self.rendimientoNominalText3.Show(True)
        copNominalDefecto = diccCOPNominalDefecto[self.definirAntiguedadChoice.GetSelection()]
        self.rendimientoNominal3 = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTONOMINAL3, name=u'rendimientoNominal3', parent=self, pos=wx.Point(275, 178), size=wx.Size(80, 18), style=0, value='%s' % copNominalDefecto)
        self.rendimientoNominal3.SetForegroundColour(wx.Colour(100, 200, 0))
        self.rendimientoNominal3.Show(True)
        self.rendimientoNominal3.Bind(wx.EVT_TEXT, self.OnRendimientoNominal3, id=wxID_PANEL1RENDIMIENTONOMINAL3)
        self.rendimientoNominalUnidadesText3 = wx.StaticText(id=wxID_PANEL1RENDNOMINALUNITEXT3, label=_(u'%'), name=u'rendimientoNominalUnidadesText3', parent=self, pos=wx.Point(360, 180), size=wx.Size(15, 13), style=0)
        self.rendimientoNominalUnidadesText3.Show(True)
        self.rendimientoMedioText3 = wx.StaticText(id=wxID_PANEL1RENDIMIENTOMEDIOTEXT3, label=_(u'Rendimiento medio estacional'), name=u'rendimientoMedioText3', parent=self, pos=wx.Point(170, 180), size=wx.Size(200, 13), style=0)
        self.rendimientoMedioText3.Show(False)
        self.rendimietoMedio3 = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTOMEDIO3, name=u'rendimietoMedio3', parent=self, pos=wx.Point(375, 178), size=wx.Size(80, 18), style=0)
        self.rendimietoMedio3.Show(False)
        self.rendimietoMedio3.Bind(wx.EVT_TEXT, self.obtenerRendimientoEstacional, id=wxID_PANEL1RENDIMIENTOMEDIO3)
        self.rendimientoMedioUnidadesText3 = wx.StaticText(id=wxID_PANEL1RENDIMIENTOMEDIOTEXT3, label=_(u'%'), name=u'rendimientoMedioUnidadesText3', parent=self, pos=wx.Point(460, 180), size=wx.Size(15, 13), style=0)
        self.rendimientoMedioUnidadesText3.Show(False)
        self.calefaccionText = wx.StaticText(id=wxID_PANEL1CALEFACTEXT, label=_(u'Calefacci\xf3n'), name=u'calefaccionText', parent=self, pos=wx.Point(15, 200), size=wx.Size(14, 13), style=0)
        self.calefaccionText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, u''))
        self.calefaccionText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.rendimientoNominalText = wx.StaticText(id=wxID_PANEL1RENDNOMINALTEXT, label=_(u'Rendimiento nominal'), name=u'rendimientoNominalText', parent=self, pos=wx.Point(170, 200), size=wx.Size(100, 13), style=0)
        self.rendimientoNominalText.Show(True)
        copNominalDefecto = diccCOPNominalDefecto[self.definirAntiguedadChoice.GetSelection()]
        self.rendimientoNominal = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTONOMINAL, name=u'rendimientoNominal', parent=self, pos=wx.Point(275, 198), size=wx.Size(80, 18), style=0, value='%s' % copNominalDefecto)
        self.rendimientoNominal.SetForegroundColour(wx.Colour(100, 200, 0))
        self.rendimientoNominal.Show(True)
        self.rendimientoNominal.Bind(wx.EVT_TEXT, self.OnRendimientoNominal, id=wxID_PANEL1RENDIMIENTONOMINAL)
        self.rendimientoNominalUnidadesText = wx.StaticText(id=wxID_PANEL1RENDNOMINALUNITEXT, label=_(u'%'), name=u'rendimientoNominalUnidadesText', parent=self, pos=wx.Point(360, 200), size=wx.Size(15, 13), style=0)
        self.rendimientoNominalUnidadesText.Show(True)
        self.rendimientoMedioText = wx.StaticText(id=wxID_PANEL1RENDIMIENTOMEDIOTEXT, label=_(u'Rendimiento medio estacional'), name=u'rendimientoMedioText', parent=self, pos=wx.Point(170, 200), size=wx.Size(200, 13), style=0)
        self.rendimientoMedioText.Show(False)
        self.rendimietoMedio = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTOMEDIO, name=u'rendimietoMedio', parent=self, pos=wx.Point(375, 198), size=wx.Size(80, 18), style=0)
        self.rendimietoMedio.Show(False)
        self.rendimietoMedio.Bind(wx.EVT_TEXT, self.obtenerRendimientoEstacional, id=wxID_PANEL1RENDIMIENTOMEDIO)
        self.rendimientoMedioUnidadesText = wx.StaticText(id=wxID_PANEL1RENDIMIENTOMEDIOTEXT, label=_(u'%'), name=u'rendimientoMedioUnidadesText', parent=self, pos=wx.Point(460, 200), size=wx.Size(15, 13), style=0)
        self.rendimientoMedioUnidadesText.Show(False)
        self.refrigeracionText = wx.StaticText(id=wxID_PANEL1REFRIGTEXT, label=_(u'Refrigeraci\xf3n'), name=u'calefaccionText', parent=self, pos=wx.Point(15, 220), size=wx.Size(14, 13), style=0)
        self.refrigeracionText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, u''))
        self.refrigeracionText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.rendimientoNominalText2 = wx.StaticText(id=wxID_PANEL1RENDNOMINALTEXT2, label=_(u'Rendimiento nominal'), name=u'rendimientoNominalText2', parent=self, pos=wx.Point(170, 220), size=wx.Size(100, 13), style=0)
        self.rendimientoNominalText2.Show(True)
        eerNominalDefecto = diccEERNominalDefecto[self.definirAntiguedadChoice.GetSelection()]
        self.rendimientoNominal2 = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTONOMINAL2, name=u'rendimientoNominal', parent=self, pos=wx.Point(275, 218), size=wx.Size(80, 18), style=0, value='%s' % eerNominalDefecto)
        self.rendimientoNominal2.SetForegroundColour(wx.Colour(100, 200, 0))
        self.rendimientoNominal2.Show(True)
        self.rendimientoNominal2.Bind(wx.EVT_TEXT, self.OnRendimientoNominal2, id=wxID_PANEL1RENDIMIENTONOMINAL2)
        self.rendimientoNominalUnidadesText2 = wx.StaticText(id=wxID_PANEL1RENDNOMINALUNITEXT2, label=_(u'%'), name=u'rendimientoNominalUnidadesText2', parent=self, pos=wx.Point(360, 220), size=wx.Size(15, 13), style=0)
        self.rendimientoNominalUnidadesText2.Show(True)
        self.rendimientoMedioText2 = wx.StaticText(id=wxID_PANEL1RENDIMIENTOMEDIOTEXT2, label=_(u'Rendimiento medio estacional'), name=u'rendimientoMedioText2', parent=self, pos=wx.Point(170, 220), size=wx.Size(200, 13), style=0)
        self.rendimientoMedioText2.Show(False)
        self.rendimietoMedio2 = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTOMEDIO2, name=u'rendimietoMedio2', parent=self, pos=wx.Point(375, 218), size=wx.Size(80, 18), style=0)
        self.rendimietoMedio2.Show(False)
        self.rendimietoMedio2.Bind(wx.EVT_TEXT, self.obtenerRendimientoEstacional, id=wxID_PANEL1RENDIMIENTOMEDIO2)
        self.rendimientoMedioUnidadesText2 = wx.StaticText(id=wxID_PANEL1RENDIMIENTOMEDIOTEXT2, label=_(u'%'), name=u'rendimientoMedioUnidadesText2', parent=self, pos=wx.Point(460, 220), size=wx.Size(12, 13), style=0)
        self.rendimientoMedioUnidadesText2.Show(False)
        self.rendimientoGlobalText3 = wx.StaticText(id=wxID_PANEL1RENDIMIENTOGLOBALTEXT3, label=_(u'Rendimiento medio estacional'), name=u'rendimientoMedioText', parent=self, pos=wx.Point(435, 180), size=wx.Size(150, 13), style=0)
        self.rendimientoGlobalText3.Show(True)
        self.rendimientoGlobalText3.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.rendimientoGlobal3 = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTOGLOBAL3, name=u'rendimietoMedio', parent=self, pos=wx.Point(617, 178), size=wx.Size(60, 18), style=0)
        self.rendimientoGlobal3.Show(True)
        self.rendimientoGlobal3.Enable(False)
        self.rendimientoGlobalUnidadesText3 = wx.StaticText(id=wxID_PANEL1RENDIMIENTOGLOBALTEXT3, label=_(u'%'), name=u'rendimientoMedioUnidadesText', parent=self, pos=wx.Point(682, 180), size=wx.Size(15, 13), style=0)
        self.rendimientoGlobalUnidadesText3.Show(True)
        self.rendimientoGlobalUnidadesText3.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.rendimientoGlobalText = wx.StaticText(id=wxID_PANEL1RENDIMIENTOGLOBALTEXT, label=_(u'Rendimiento medio estacional'), name=u'rendimientoMedioText', parent=self, pos=wx.Point(435, 200), size=wx.Size(150, 13), style=0)
        self.rendimientoGlobalText.Show(True)
        self.rendimientoGlobalText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.rendimientoGlobal = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTOGLOBAL, name=u'rendimietoMedio', parent=self, pos=wx.Point(617, 198), size=wx.Size(60, 18), style=0)
        self.rendimientoGlobal.Show(True)
        self.rendimientoGlobal.Enable(False)
        self.rendimientoGlobalUnidadesText = wx.StaticText(id=wxID_PANEL1RENDIMIENTOGLOBALTEXT, label=_(u'%'), name=u'rendimientoMedioUnidadesText', parent=self, pos=wx.Point(682, 200), size=wx.Size(15, 13), style=0)
        self.rendimientoGlobalUnidadesText.Show(True)
        self.rendimientoGlobalUnidadesText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.rendimientoGlobalText2 = wx.StaticText(id=wxID_PANEL1RENDIMIENTOGLOBALTEXT2, label=_(u'Rendimiento medio estacional'), name=u'rendimientoMedioText', parent=self, pos=wx.Point(435, 220), size=wx.Size(150, 13), style=0)
        self.rendimientoGlobalText2.Show(True)
        self.rendimientoGlobalText2.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.rendimientoGlobal2 = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTOGLOBAL2, name=u'rendimietoMedio', parent=self, pos=wx.Point(617, 218), size=wx.Size(60, 18), style=0)
        self.rendimientoGlobal2.Show(True)
        self.rendimientoGlobal2.Enable(False)
        self.rendimientoGlobalUnidadesText2 = wx.StaticText(id=wxID_PANEL1RENDIMIENTOGLOBALTEXT2, label=_(u'%'), name=u'rendimientoMedioUnidadesText', parent=self, pos=wx.Point(682, 220), size=wx.Size(15, 13), style=0)
        self.rendimientoGlobalUnidadesText2.Show(True)
        self.rendimientoGlobalUnidadesText2.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.rendimientoGlobalText.SetForegroundColour(wx.Colour(100, 100, 100))
        self.rendimientoGlobalUnidadesText.SetForegroundColour(wx.Colour(100, 100, 100))
        self.rendimientoGlobalText2.SetForegroundColour(wx.Colour(100, 100, 100))
        self.rendimientoGlobalUnidadesText2.SetForegroundColour(wx.Colour(100, 100, 100))
        self.rendimientoGlobalText3.SetForegroundColour(wx.Colour(100, 100, 100))
        self.rendimientoGlobalUnidadesText3.SetForegroundColour(wx.Colour(100, 100, 100))
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
        
        
        ARGUMENTOS:
                event:
        """
        self.coberturaPorcentaje.SetValue('100')
        self.coberturaPorcentaje2.SetValue('100')
        self.coberturaPorcentaje3.SetValue('100')

    def OnNombreInstalacion(self, event):
        """
        Metodo: OnNombreInstalacion
        
        
        ARGUMENTOS:
                event:
        """
        if self.nombreInstalacion.GetValue() == _(u'Calefacci\xf3n,  refrigeraci\xf3n y ACS'):
            self.nombreInstalacion.SetForegroundColour(wx.Colour(100, 200, 0))
        else:
            self.nombreInstalacion.SetForegroundColour(wx.Colour(0, 0, 0))

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
        if self.rendimientoNominal.GetValue() in listadoValoresStr or valorValido == False:
            rendNominalDefecto = diccCOPNominalDefecto[self.definirAntiguedadChoice.GetSelection()]
            self.rendimientoNominal.SetValue('%s' % rendNominalDefecto)
            self.rendimientoNominal.SetForegroundColour(wx.Colour(100, 200, 0))
        try:
            float(self.rendimientoNominal2.GetValue())
            valorValido = True
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            valorValido = False

        listadoValoresStr = [ str(x) for x in diccEERNominalDefecto.values() ]
        if self.rendimientoNominal2.GetValue() in listadoValoresStr or valorValido == False:
            rendNominalDefecto = diccEERNominalDefecto[self.definirAntiguedadChoice.GetSelection()]
            self.rendimientoNominal2.SetValue('%s' % rendNominalDefecto)
            self.rendimientoNominal2.SetForegroundColour(wx.Colour(100, 200, 0))
        try:
            float(self.rendimientoNominal3.GetValue())
            valorValido = True
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            valorValido = False

        listadoValoresStr = [ str(x) for x in diccCOPNominalDefecto.values() ]
        if self.rendimientoNominal3.GetValue() in listadoValoresStr or valorValido == False:
            rendNominalDefecto = diccCOPNominalDefecto[self.definirAntiguedadChoice.GetSelection()]
            self.rendimientoNominal3.SetValue('%s' % rendNominalDefecto)
            self.rendimientoNominal3.SetForegroundColour(wx.Colour(100, 200, 0))

    def OnAntiguedadChoice(self, event):
        self.actualizarRendimientoNominalEquiposElectricos()
        self.obtenerRendimientoEstacional(None)
        return

    def OnRendimientoNominal(self, event):
        """
        Metodo: OnRendimientoNominal
        
        
        ARGUMENTOS:
                event:
        """
        copNominalDefecto = diccCOPNominalDefecto[self.definirAntiguedadChoice.GetSelection()]
        try:
            if float(self.rendimientoNominal.GetValue()) == copNominalDefecto:
                self.rendimientoNominal.SetForegroundColour(wx.Colour(100, 200, 0))
            else:
                self.rendimientoNominal.SetForegroundColour(wx.Colour(0, 0, 0))
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        self.obtenerRendimientoEstacional(None)
        return

    def OnRendimientoNominal2(self, event):
        """
        Metodo: OnRendimientoNominal2
        
        
        ARGUMENTOS:
                event:
        """
        eerNominalDefecto = diccEERNominalDefecto[self.definirAntiguedadChoice.GetSelection()]
        try:
            if float(self.rendimientoNominal2.GetValue()) == eerNominalDefecto:
                self.rendimientoNominal2.SetForegroundColour(wx.Colour(100, 200, 0))
            else:
                self.rendimientoNominal2.SetForegroundColour(wx.Colour(0, 0, 0))
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        self.obtenerRendimientoEstacional(None)
        return

    def OnRendimientoNominal3(self, event):
        """
        Metodo: OnRendimientoNominal3
        
        
        ARGUMENTOS:
                event:
        """
        copNominalDefecto = diccCOPNominalDefecto[self.definirAntiguedadChoice.GetSelection()]
        try:
            if float(self.rendimientoNominal3.GetValue()) == copNominalDefecto:
                self.rendimientoNominal3.SetForegroundColour(wx.Colour(100, 200, 0))
            else:
                self.rendimientoNominal3.SetForegroundColour(wx.Colour(0, 0, 0))
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        self.obtenerRendimientoEstacional(None)
        return

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
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaPorcentaje.SetValue('')
                except ZeroDivisionError:
                    logging.info(u'Excepcion en: %s' % __name__)
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
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaPorcentaje.SetValue('')
                except ZeroDivisionError:
                    logging.info(u'Excepcion en: %s' % __name__)
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
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaMetros.SetValue('')
                except ZeroDivisionError:
                    logging.info(u'Excepcion en: %s' % __name__)
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
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaMetros.SetValue('')
                except ZeroDivisionError:
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaMetros.SetValue('')

            self.booleano = True

    def OnCobertura2(self, event):
        """
        Metodo: OnCobertura2
        
        
        ARGUMENTOS:
                event:
        """
        if self.booleano == True:
            self.booleano = False
            if self.subgrupoChoice.GetStringSelection() == u'Edificio Objeto':
                try:
                    superficieTotal = float(self.parent.parent.parent.panelDatosGenerales.superficie.GetValue())
                    superficieActual = float(self.coberturaMetros2.GetValue())
                    porcentaje = round(superficieActual * 100 / superficieTotal, 2)
                    self.coberturaPorcentaje2.SetValue(str(porcentaje))
                except (ValueError, TypeError):
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaPorcentaje2.SetValue('')
                except ZeroDivisionError:
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaPorcentaje2.SetValue('')

            else:
                for i in self.parent.parent.subgrupos:
                    if i.nombre == self.subgrupoChoice.GetStringSelection():
                        mTotales = float(i.superficie)
                        break

                try:
                    mActuales = float(self.coberturaMetros2.GetValue())
                    porcentaje = round(mActuales * 100 / mTotales, 2)
                    self.coberturaPorcentaje2.SetValue(str(porcentaje))
                except (ValueError, TypeError):
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaPorcentaje2.SetValue('')
                except ZeroDivisionError:
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaPorcentaje2.SetValue('')

            self.booleano = True

    def OnCoberturaPorcentaje2(self, event):
        """
        Metodo: OnCoberturaPorcentaje2
        
        
        ARGUMENTOS:
                event:
        """
        if self.booleano == True:
            self.booleano = False
            if self.subgrupoChoice.GetStringSelection() == u'Edificio Objeto':
                try:
                    superficieTotal = float(self.parent.parent.parent.panelDatosGenerales.superficie.GetValue())
                    porcentajeActual = float(self.coberturaPorcentaje2.GetValue())
                    mAcuales = round(porcentajeActual * superficieTotal / 100.0, 2)
                    self.coberturaMetros2.SetValue(str(mAcuales))
                except (ValueError, TypeError):
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaMetros2.SetValue('')
                except ZeroDivisionError:
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaMetros2.SetValue('')

            else:
                for i in self.parent.parent.subgrupos:
                    if i.nombre == self.subgrupoChoice.GetStringSelection():
                        mTotales = float(i.superficie)
                        break

                try:
                    porcentaje = float(self.coberturaPorcentaje2.GetValue())
                    mAcuales = round(porcentaje * mTotales / 100.0, 2)
                    self.coberturaMetros2.SetValue(str(mAcuales))
                except (ValueError, TypeError):
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaMetros2.SetValue('')
                except ZeroDivisionError:
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaMetros2.SetValue('')

            self.booleano = True

    def OnCobertura3(self, event):
        """
        Metodo: OnCobertura3
        
        
        ARGUMENTOS:
                event:
        """
        if self.booleano == True:
            self.booleano = False
            if self.subgrupoChoice.GetStringSelection() == u'Edificio Objeto':
                try:
                    superficieTotal = float(self.parent.parent.parent.panelDatosGenerales.superficie.GetValue())
                    superficieActual = float(self.coberturaMetros3.GetValue())
                    porcentaje = round(superficieActual * 100 / superficieTotal, 2)
                    self.coberturaPorcentaje3.SetValue(str(porcentaje))
                except (ValueError, TypeError):
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaPorcentaje3.SetValue('')
                except ZeroDivisionError:
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaPorcentaje3.SetValue('')

            else:
                for i in self.parent.parent.subgrupos:
                    if i.nombre == self.subgrupoChoice.GetStringSelection():
                        mTotales = float(i.superficie)
                        break

                try:
                    mActuales = float(self.coberturaMetros3.GetValue())
                    porcentaje = round(mActuales * 100 / mTotales, 2)
                    self.coberturaPorcentaje3.SetValue(str(porcentaje))
                except (ValueError, TypeError):
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaPorcentaje3.SetValue('')
                except ZeroDivisionError:
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaPorcentaje3.SetValue('')

            self.booleano = True

    def OnCoberturaPorcentaje3(self, event):
        """
        Metodo: OnCoberturaPorcentaje3
        
        
        ARGUMENTOS:
                event:
        """
        if self.booleano == True:
            self.booleano = False
            if self.subgrupoChoice.GetStringSelection() == u'Edificio Objeto':
                try:
                    superficieTotal = float(self.parent.parent.parent.panelDatosGenerales.superficie.GetValue())
                    porcentajeActual = float(self.coberturaPorcentaje3.GetValue())
                    mAcuales = round(porcentajeActual * superficieTotal / 100.0, 2)
                    self.coberturaMetros3.SetValue(str(mAcuales))
                except (ValueError, TypeError):
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaMetros3.SetValue('')
                except ZeroDivisionError:
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaMetros3.SetValue('')

            else:
                for i in self.parent.parent.subgrupos:
                    if i.nombre == self.subgrupoChoice.GetStringSelection():
                        mTotales = float(i.superficie)
                        break

                try:
                    porcentaje = float(self.coberturaPorcentaje3.GetValue())
                    mAcuales = round(porcentaje * mTotales / 100.0, 2)
                    self.coberturaMetros3.SetValue(str(mAcuales))
                except (ValueError, TypeError):
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaMetros3.SetValue('')
                except ZeroDivisionError:
                    logging.info(u'Excepcion en: %s' % __name__)
                    self.coberturaMetros3.SetValue('')

            self.booleano = True

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
        self.booleano = True
        self.rendimientoEstacionalCal = ''
        self.rendimientoEstacionalRef = ''
        self.rendimientoEstacionalACS = ''
        self._init_ctrls(parent, id, pos, size, style, name)
        self.tipoSistema = 'mixto3'
        self.listaErrores = u''
        self.subgrupoChoice.SetItems(self.cargarRaices())
        self.OnrendimientoChoice(None)
        self.elegirRaiz()
        self.obtenerRendimientoEstacional(None)
        return

    def obtenerRendimientoEstacional(self, event):
        """
        Metodo: obtenerRendimientoEstacional
        
        
        ARGUMENTOS:
                 event):  #funcion para otener el rendimiento medio estacion:
        """
        kwargsConocido = {'rendEstACS': self.rendimietoMedio3.GetValue(),
         'rendEstCal': self.rendimietoMedio.GetValue(),
         'rendEstRef': self.rendimietoMedio2.GetValue()}
        kwargsBdCEst = {'rendNominalACS': self.rendimientoNominal3.GetValue(),
         'rendNominalCal': self.rendimientoNominal.GetValue(),
         'rendNominalRef': self.rendimientoNominal2.GetValue(),
         'variosGeneradoresCheck': False,
         'fraccionPotencia': '',
         'fraccionPotenciaEntrada': ''}
        kwargs = {}
        kwargs.update(kwargsConocido)
        kwargs.update(kwargsBdCEst)
        zonaHE1 = self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()
        programa = self.parent.parent.parent.programa
        tipoEdificio = self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
        modoDefinicion = self.rendimientoChoice.GetStringSelection()
        tipoEquipo = self.generadorChoice.GetStringSelection()
        combustible = self.combustibleChoice.GetStringSelection()
        resultado = calculoRendimientoMedioEstacional(zonaHE1=zonaHE1, programa=programa, tipoEdificio=tipoEdificio, tipoInstalacion=self.tipoSistema, modoDefinicion=modoDefinicion, tipoEquipo=tipoEquipo, combustible=combustible, **kwargs)
        self.rendimientoEstacionalACS, self.rendimientoEstacionalCal, self.rendimientoEstacionalRef = resultado
        self.escribirRendimientoGlobal()

    def escribirRendimientoGlobal(self):
        """
        Metodo: escribirRendimientoGlobal
        
        
        """
        self.rendimientoGlobal.SetValue(str(self.rendimientoEstacionalCal))
        self.rendimientoGlobal2.SetValue(str(self.rendimientoEstacionalRef))
        self.rendimientoGlobal3.SetValue(str(self.rendimientoEstacionalACS))

    def elegirRaiz(self):
        """
        Metodo: elegirRaiz
        
        
                self)::
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
        antes = self.rendimientoChoice.GetStringSelection()
        if u'Equipo de Rendimiento Constante' == self.generadorChoice.GetStringSelection():
            self.rendimientoChoice.SetItems([self.parent.listadoOpcionesInstalacionesMixtos[0]])
            self.rendimientoChoice.SetSelection(0)
        else:
            self.rendimientoChoice.SetItems(self.parent.listadoOpcionesInstalacionesMixtos)
            self.rendimientoChoice.SetStringSelection(antes)
        self.OnrendimientoChoice(None)
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
        Se llama al cambiar de tipo de equipo, o de modoDefini\xf3n
        """
        if 'Conocido' in self.rendimientoChoice.GetStringSelection():
            self.rendimientoMedioText.Show(True)
            self.rendimietoMedio.Show(True)
            self.rendimientoMedioUnidadesText.Show(True)
            self.rendimientoNominalText.Show(False)
            self.rendimientoNominal.Show(False)
            self.rendimientoNominalUnidadesText.Show(False)
            self.definirAntiguedadChoice.Show(False)
            self.definirAntiguedadText.Show(False)
            self.rendimientoMedioText2.Show(True)
            self.rendimietoMedio2.Show(True)
            self.rendimientoMedioUnidadesText2.Show(True)
            self.rendimientoNominalText2.Show(False)
            self.rendimientoNominal2.Show(False)
            self.rendimientoNominalUnidadesText2.Show(False)
            self.rendimientoMedioText3.Show(True)
            self.rendimietoMedio3.Show(True)
            self.rendimientoMedioUnidadesText3.Show(True)
            self.rendimientoNominalText3.Show(False)
            self.rendimientoNominal3.Show(False)
            self.rendimientoNominalUnidadesText3.Show(False)
            self.rendimientoGlobalText.Show(False)
            self.rendimientoGlobal.Show(False)
            self.rendimientoGlobalUnidadesText.Show(False)
            self.rendimientoGlobalText2.Show(False)
            self.rendimientoGlobal2.Show(False)
            self.rendimientoGlobalUnidadesText2.Show(False)
            self.rendimientoGlobalText3.Show(False)
            self.rendimientoGlobal3.Show(False)
            self.rendimientoGlobalUnidadesText3.Show(False)
        else:
            self.rendimientoMedioText.Show(False)
            self.rendimietoMedio.Show(False)
            self.rendimientoMedioUnidadesText.Show(False)
            self.rendimientoNominalText.Show(True)
            self.rendimientoNominal.Show(True)
            self.rendimientoNominalUnidadesText.Show(True)
            self.definirAntiguedadChoice.Show(True)
            self.definirAntiguedadText.Show(True)
            self.rendimientoMedioText2.Show(False)
            self.rendimietoMedio2.Show(False)
            self.rendimientoMedioUnidadesText2.Show(False)
            self.rendimientoNominalText2.Show(True)
            self.rendimientoNominal2.Show(True)
            self.rendimientoNominalUnidadesText2.Show(True)
            self.rendimientoMedioText3.Show(False)
            self.rendimietoMedio3.Show(False)
            self.rendimientoMedioUnidadesText3.Show(False)
            self.rendimientoNominalText3.Show(True)
            self.rendimientoNominal3.Show(True)
            self.rendimientoNominalUnidadesText3.Show(True)
            self.rendimientoGlobalText.Show(True)
            self.rendimientoGlobal.Show(True)
            self.rendimientoGlobalUnidadesText.Show(True)
            self.rendimientoGlobalText2.Show(True)
            self.rendimientoGlobal2.Show(True)
            self.rendimientoGlobalUnidadesText2.Show(True)
            self.rendimientoGlobalText3.Show(True)
            self.rendimientoGlobal3.Show(True)
            self.rendimientoGlobalUnidadesText3.Show(True)
            self.actualizarRendimientoNominalEquiposElectricos()
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
        dato = self.coberturaMetros2.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.coberturaMetros2.SetValue(dato)
        dato = self.coberturaPorcentaje2.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.coberturaPorcentaje2.SetValue(dato)
        dato = self.coberturaMetros3.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.coberturaMetros3.SetValue(dato)
        dato = self.coberturaPorcentaje3.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.coberturaPorcentaje3.SetValue(dato)
        dato = self.rendimietoMedio.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.rendimietoMedio.SetValue(dato)
        dato = self.rendimietoMedio2.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.rendimietoMedio2.SetValue(dato)
        dato = self.rendimietoMedio3.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.rendimietoMedio3.SetValue(dato)
        dato = self.rendimientoNominal.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.rendimientoNominal.SetValue(dato)
        dato = self.rendimientoNominal2.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.rendimientoNominal2.SetValue(dato)
        dato = self.rendimientoNominal3.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.rendimientoNominal3.SetValue(dato)
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
        self.listaErrores = u''
        self.listaErrores += Comprueba(self.nombreInstalacion.GetValue(), 1, self.listaErrores, _(u'nombre')).ErrorDevuelto
        self.listaErrores += Comprueba(self.subgrupoChoice.GetStringSelection(), 0, self.listaErrores, _(u'zona')).ErrorDevuelto
        self.listaErrores += Comprueba(self.generadorChoice.GetStringSelection(), 0, self.listaErrores, _(u'tipo de generador')).ErrorDevuelto
        self.listaErrores += Comprueba(self.combustibleChoice.GetStringSelection(), 0, self.listaErrores, _(u'tipo de combustible')).ErrorDevuelto
        self.listaErrores += Comprueba(self.rendimientoChoice.GetStringSelection(), 0, self.listaErrores, _(u'definir rendimiento')).ErrorDevuelto
        if self.parent.parent.parent.panelDatosGenerales.superficie.GetValue() == '':
            self.listaErrores += Comprueba2(self.coberturaPorcentaje3.GetValue(), 2, self.listaErrores, _(u'porcentaje de demanda (ACS) de la zona cubierto'), 0, 100).ErrorDevuelto
        else:
            self.listaErrores += Comprueba2(self.coberturaPorcentaje3.GetValue(), 2, self.listaErrores, _(u'porcentaje de demanda de la zona cubierto o m2 cubiertos por el equipo (ACS)'), 0, 100).ErrorDevuelto
        if self.parent.parent.parent.panelDatosGenerales.superficie.GetValue() == '':
            self.listaErrores += Comprueba2(self.coberturaPorcentaje.GetValue(), 2, self.listaErrores, _(u'porcentaje de demanda (calefacci\xf3n) de la zona cubierto'), 0, 100).ErrorDevuelto
        else:
            self.listaErrores += Comprueba2(self.coberturaPorcentaje.GetValue(), 2, self.listaErrores, _(u'porcentaje de demanda de la zona cubierto o m2 cubiertos por el equipo (calefacci\xf3n)'), 0, 100).ErrorDevuelto
        if self.parent.parent.parent.panelDatosGenerales.superficie.GetValue() == '':
            self.listaErrores += Comprueba2(self.coberturaPorcentaje2.GetValue(), 2, self.listaErrores, _(u'porcentaje de demanda (refrigeraci\xf3n) de la zona cubierto'), 0, 100).ErrorDevuelto
        else:
            self.listaErrores += Comprueba2(self.coberturaPorcentaje2.GetValue(), 2, self.listaErrores, _(u'porcentaje de demanda de la zona cubierto o m2 cubiertos por el equipo (refrigeraci\xf3n)'), 0, 100).ErrorDevuelto
        rendi = self.rendimientoChoice.GetStringSelection()
        if 'Conocido' in rendi:
            self.listaErrores += Comprueba(self.rendimietoMedio.GetValue(), 2, self.listaErrores, _(u'rendimiento medio estacional (calefacci\xf3n)'), 0).ErrorDevuelto
            self.listaErrores += Comprueba(self.rendimietoMedio2.GetValue(), 2, self.listaErrores, _(u'rendimiento medio estacional (refrigeraci\xf3n)'), 0).ErrorDevuelto
            self.listaErrores += Comprueba(self.rendimietoMedio3.GetValue(), 2, self.listaErrores, _(u'rendimiento medio estacional (ACS)'), 0).ErrorDevuelto
        else:
            self.listaErrores += Comprueba(self.rendimientoNominal.GetValue(), 2, self.listaErrores, _(u'rendimiento nominal (calefacci\xf3n)'), 0.09).ErrorDevuelto
            self.listaErrores += Comprueba(self.rendimientoNominal2.GetValue(), 2, self.listaErrores, _(u'rendimiento nominal (refrigeraci\xf3n)'), 0.09).ErrorDevuelto
            self.listaErrores += Comprueba(self.rendimientoNominal3.GetValue(), 2, self.listaErrores, _(u'rendimiento nominal (ACS)'), 0.09).ErrorDevuelto
        if u'Conocido' not in rendi and self.listaErrores == '':
            if self.rendimientoEstacionalACS != '':
                self.listaErrores += Comprueba(str(self.rendimientoEstacionalACS), 2, self.listaErrores, _(u'rendimiento medio estacional para ACS'), 0.0).ErrorDevuelto
            if self.rendimientoEstacionalCal != '':
                self.listaErrores += Comprueba(str(self.rendimientoEstacionalCal), 2, self.listaErrores, _(u'rendimiento medio estacional para calefacci\xf3n'), 0.0).ErrorDevuelto
            if self.rendimientoEstacionalRef != '':
                self.listaErrores += Comprueba(str(self.rendimientoEstacionalRef), 2, self.listaErrores, _(u'rendimiento medio estacional para refrigeraci\xf3n'), 0.0).ErrorDevuelto
        if self.acumulacionCheck.GetValue() == True:
            self.listaErrores += Comprueba(self.temperaturaAlta.GetValue(), 2, self.listaErrores, _(u'T\xaa alta')).ErrorDevuelto
            self.listaErrores += Comprueba(self.temperaturaBaja.GetValue(), 2, self.listaErrores, _(u'T\xaa baja')).ErrorDevuelto
            self.listaErrores += Comprueba(self.valorUAChoice.GetStringSelection(), 0, self.listaErrores, _(u'valor UA')).ErrorDevuelto
            valorUA = self.valorUAChoice.GetStringSelection()
            if 'Conocido' in valorUA:
                self.listaErrores += Comprueba(self.UAvalor.GetValue(), 2, self.listaErrores, _(u'UA'), 0).ErrorDevuelto
            else:
                self.listaErrores += Comprueba(self.volumen.GetValue(), 2, self.listaErrores, _(u'volumen de un dep\xf3sito'), 0).ErrorDevuelto
                self.listaErrores += Comprueba(self.multiplicador.GetValue(), 2, self.listaErrores, _(u'multiplicador'), 0).ErrorDevuelto
                if 'Estimado' in valorUA:
                    self.listaErrores += Comprueba(self.espesorAislamiento.GetValue(), 2, self.listaErrores, _(u'espesor del aislamiento'), 0).ErrorDevuelto
            try:
                saltoTermico = float(self.temperaturaAlta.GetValue()) - float(self.temperaturaBaja.GetValue())
                if saltoTermico <= 0.0:
                    self.listaErrores += _(u'\nla temperatura de consiga alta debe ser mayor que la temperatura de consigna baja')
            except (ValueError, TypeError):
                logging.info(u'Excepcion en: %s' % __name__)