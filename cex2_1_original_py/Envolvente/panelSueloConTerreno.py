# Embedded file name: Envolvente\panelSueloConTerreno.pyc
"""
Modulo: panelSueloConTerreno.py

"""
from Envolvente.comprobarCampos import Comprueba
from miChoice import MiChoice
import Envolvente.apendiceE as apendiceE
import Envolvente.tablasValores as tablasValores
import Calculos.listadosWeb as listadosWeb
import nuevoUndo
import wx
import logging
wxID_PANEL1, wxID_PANEL1AISLAMIENTOCHECK, wxID_PANEL1AISLANTERADIOBUTTON, wxID_PANEL1CERRAMIENTOSCHOICE, wxID_PANEL1ESPESORAISLANTE, wxID_PANEL1ESPESORAISLATETEXT, wxID_PANEL1LIBRERIARADIOBUTTON, wxID_PANEL1MAYOR05RADIO, wxID_PANEL1MENOR05RADIO, wxID_PANEL1NOMBREMURO, wxID_PANEL1NOMBREMUROTEXT, wxID_PANEL1PERIMETRO, wxID_PANEL1PERIMETROTEXT, wxID_PANEL1PROFUNDIDAD, wxID_PANEL1PROFUNDIDADTEXT, wxID_PANEL1PROFUNDIDADUNIDADESTEXT, wxID_PANEL1RAISLANTE, wxID_PANEL1RAISLANTEUNIDADESTEXT, wxID_PANEL1RAISLATERADIO, wxID_PANEL1SUPERFICIEMURO, wxID_PANEL1SUPERFICIETEXT, wxID_PANEL1SUPERFICIEUNIDADESTEXT, wxID_PANEL1TIPOAISLANTECHOICE, wxID_PANEL1TIPOAISLATECHOICE, wxID_PANEL1URADIOBUTTON, wxID_PANEL1VALORU, wxID_PANEL1VALORUCHOICE, wxID_PANEL1VALORUTEXT, wxID_PANEL1ANCHOBANDATEXT, wxID_PANEL1ANCHOBANDA, wxID_PANEL1ANCHOBANDAUNIDADESTEXT, wxID_PANEL1LONGIMUROTEXT, wxID_PANEL1ALTURAMUROTEXT, wxID_PANEL1MULTIMUROTEXT, wxID_PANEL1LONGIMURO, wxID_PANEL1LONGITUDUNIDADESTEXT, wxID_PANEL1ALTURAMURO, wxID_PANEL1ALTURAUNIDADESTEXT, wxID_PANEL1MULTIMURO, wxID_PANEL1SUBGRUPOTEXT, wxID_PANEL1SUBGRUPOCHOICE, wxID_PANEL1PERIMETROUNIDADESTEXT, wxID_PANEL1UNIDADESUTEXT, wxID_PANEL1UNIDADESESPESORAISLATETEXT, wxID_PANEL1PRESISTEXT, wxID_PANEL1UFINALTEXT, wxID_PANEL1UFINALCUADRO, wxID_PANEL1UNIDADESUFINAL, wxID_PANEL1RAISLATE, wxID_PANEL1RAISLATEUNITEXT, wxID_PANEL1EPSRADIO, wxID_PANEL1ESPESORTEXT, wxID_PANEL1ESPESOR, wxID_PANEL1ESPESORUNITEXT, wxID_PANEL1RAISLATERADIO2, wxID_PANEL1RAISLATE2, wxID_PANEL1RAISLATEUNITEXT2, wxID_PANEL1EPSRADIO2, wxID_PANEL1ESPESORTEXT2, wxID_PANEL1ESPESOR2, wxID_PANEL1ESPESORUNITEXT2, wxID_DIMENSIONESLINEATEXT, wxID_CARACTERISTICASLINEATEXT, wxID_CARACTERISTICASAISLAMIENTOLINEATEXT, wxID_PANEL1TIPOAISLANTETEXT = [ wx.NewId() for _init_ctrls in range(65) ]

class Panel1(wx.Panel, nuevoUndo.VistaUndo):
    """
    Clase: Panel1 del modulo panelSueloConTerreno.py
    
    
    """

    def OnNombreMuro(self, event):
        """
        Metodo: OnNombreMuro
        
        
        ARGUMENTOS:
                event:
        """
        if self.nombreMuro.GetValue() == _(u'Suelo con terreno'):
            self.nombreMuro.SetForegroundColour(wx.Colour(100, 200, 0))
        else:
            self.nombreMuro.SetForegroundColour(wx.Colour(0, 0, 0))

    def _init_ctrls(self, prnt, ide, posi, siz, styl, named):
        """
        Metodo: _init_ctrls
        
        
        ARGUMENTOS:
                prnt:
                ide:
                posi:
                siz:
                styl:
                named:
        """
        wx.Panel.__init__(self, id=ide, name='panelSueloConTerreno', parent=prnt, pos=posi, size=siz, style=styl)
        self.SetBackgroundColour('white')
        self.nombreMuroText = wx.StaticText(id=wxID_PANEL1NOMBREMUROTEXT, label=_(u'Nombre'), name=u'nombreMuroText', parent=self, pos=wx.Point(15, 2), size=wx.Size(102, 13), style=0)
        self.nombreMuro = wx.TextCtrl(id=wxID_PANEL1NOMBREMURO, name=u'nombreMuro', parent=self, pos=wx.Point(151, 0), size=wx.Size(210, 21), style=0, value=_(u'Suelo con terreno'))
        self.nombreMuro.SetForegroundColour(wx.Colour(100, 200, 0))
        self.nombreMuro.Bind(wx.EVT_TEXT, self.OnNombreMuro, id=wxID_PANEL1NOMBREMURO)
        self.subgrupoText = wx.StaticText(id=wxID_PANEL1SUBGRUPOTEXT, label=_(u'Zona'), name=u'subgrupoText', parent=self, pos=wx.Point(435, 2), size=wx.Size(50, 13), style=0)
        self.subgrupoChoice = MiChoice(choices=[], id=wxID_PANEL1SUBGRUPOCHOICE, name=u'subgrupoChoice', parent=self, pos=wx.Point(496, 0), size=wx.Size(214, 21), style=0)
        self.EficienciaLineaText = wx.StaticBox(id=-1, label=_(u'Par\xe1metros caracter\xedsticos del cerramiento'), name='EficienciaLineaText', parent=self, pos=wx.Point(0, 107), size=wx.Size(710, 235), style=0)
        self.EficienciaLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.EficienciaLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.DimensionesLineaText = wx.StaticBox(id=wxID_DIMENSIONESLINEATEXT, label=_(u'Dimensiones'), name='LineaText', parent=self, pos=wx.Point(0, 26), size=wx.Size(361, 77), style=0)
        self.DimensionesLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.DimensionesLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.CaracteristicasLineaText = wx.StaticBox(id=wxID_CARACTERISTICASLINEATEXT, label=_(u'Caracter\xedsticas'), name='LineaText', parent=self, pos=wx.Point(373, 26), size=wx.Size(337, 77), style=0)
        self.CaracteristicasLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.superficieText = wx.StaticText(id=wxID_PANEL1SUPERFICIETEXT, label=_(u'Superficie'), name=u'superficieText', parent=self, pos=wx.Point(15, 46), size=wx.Size(51, 13), style=0)
        self.superficieMuro = wx.TextCtrl(id=wxID_PANEL1SUPERFICIEMURO, name=u'superficieMuro', parent=self, pos=wx.Point(151, 44), size=wx.Size(80, 21), style=0, value=u'')
        self.superficieMuro.Bind(wx.EVT_TEXT, self.OnCambioSuperficie, id=wxID_PANEL1SUPERFICIEMURO)
        self.superficieUnidadesText = wx.StaticText(id=wxID_PANEL1SUPERFICIEUNIDADESTEXT, label=_(u'm2'), name=u'superficieUnidadesText', parent=self, pos=wx.Point(236, 46), size=wx.Size(14, 13), style=0)
        self.longitudMuroText = wx.StaticText(id=wxID_PANEL1LONGIMUROTEXT, label=_(u'Longitud'), name=u'longitudMuroText', parent=self, pos=wx.Point(151, 69), size=wx.Size(28, 13), style=0)
        self.longitudMuro = wx.TextCtrl(id=wxID_PANEL1LONGIMURO, name=u'longitudMuro', parent=self, pos=wx.Point(191, 67), size=wx.Size(40, 15), style=0, value=u'')
        self.longitudMuro.Bind(wx.EVT_TEXT, self.OnCambioLAMText, id=wxID_PANEL1LONGIMURO)
        self.LongitudUnidadesText = wx.StaticText(id=wxID_PANEL1LONGITUDUNIDADESTEXT, label=_(u'm'), name=u'profundidadUnidadesText', parent=self, pos=wx.Point(236, 67), size=wx.Size(14, 13), style=0)
        self.alturaMuroText = wx.StaticText(id=wxID_PANEL1ALTURAMUROTEXT, label=_(u'Anchura'), name=u'alturaMuroText', parent=self, pos=wx.Point(151, 85), size=wx.Size(28, 13), style=0)
        self.alturaMuro = wx.TextCtrl(id=wxID_PANEL1ALTURAMURO, name=u'alturaMuro', parent=self, pos=wx.Point(191, 83), size=wx.Size(40, 15), style=0, value=u'')
        self.alturaMuro.Bind(wx.EVT_TEXT, self.OnCambioLAMText, id=wxID_PANEL1ALTURAMURO)
        self.alturaMuroUnidades = wx.StaticText(id=wxID_PANEL1ALTURAUNIDADESTEXT, label=_(u'm'), name=u'alturaMuroUnidades', parent=self, pos=wx.Point(236, 85), size=wx.Size(14, 13), style=0)
        self.multiMuroText = wx.StaticText(id=wxID_PANEL1MULTIMUROTEXT, label=_(u'Multiplicador'), name=u'multiMuroText', parent=self, pos=wx.Point(0, 94), size=wx.Size(80, 13), style=0)
        self.multiMuroText.Show(False)
        self.multiMuro = wx.TextCtrl(id=wxID_PANEL1MULTIMURO, name=u'multiMuro', parent=self, pos=wx.Point(120, 94), size=wx.Size(80, 21), style=0, value=u'1')
        self.multiMuro.Show(False)
        self.multiMuro.Bind(wx.EVT_TEXT, self.OnCambioLAMText, id=wxID_PANEL1MULTIMURO)
        self.longitudMuroText.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.LongitudUnidadesText.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.alturaMuroText.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.alturaMuroUnidades.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.profundidadText = wx.StaticText(id=wxID_PANEL1PROFUNDIDADTEXT, label=_(u'Profundidad'), name=u'profundidadText', parent=self, pos=wx.Point(388, 64), size=wx.Size(62, 13), style=0)
        self.menor05Radio = wx.RadioButton(id=wxID_PANEL1MENOR05RADIO, label=_(u'Menor o igual que 0.5 m'), name=u'menor05Radio', parent=self, pos=wx.Point(496, 46), size=wx.Size(136, 13), style=wx.RB_GROUP)
        self.menor05Radio.SetValue(True)
        self.menor05Radio.Bind(wx.EVT_RADIOBUTTON, self.OnMenor05Radio, id=wxID_PANEL1MENOR05RADIO)
        self.mayor05Radio = wx.RadioButton(id=wxID_PANEL1MAYOR05RADIO, label=_(u'Mayor que 0.5 m'), name=u'mayor05Radio', parent=self, pos=wx.Point(496, 72), size=wx.Size(103, 13), style=0)
        self.mayor05Radio.SetValue(False)
        self.mayor05Radio.Bind(wx.EVT_RADIOBUTTON, self.OnMayor05Radio, id=wxID_PANEL1MAYOR05RADIO)
        self.profundidad = wx.TextCtrl(id=wxID_PANEL1PROFUNDIDAD, name=u'profundidad', parent=self, pos=wx.Point(601, 71), size=wx.Size(56, 15), style=0, value=u'')
        self.profundidad.Enable(False)
        self.profundidad.Bind(wx.EVT_TEXT, self.calcularCaracteristicasCerramiento, id=wxID_PANEL1PROFUNDIDAD)
        self.profundidadUnidadesText = wx.StaticText(id=wxID_PANEL1PROFUNDIDADUNIDADESTEXT, label=_(u'm'), name=u'profundidadUnidadesText', parent=self, pos=wx.Point(662, 72), size=wx.Size(10, 13), style=0)
        self.profundidadUnidadesText.Enable(False)
        self.valorUText = wx.StaticText(id=wxID_PANEL1VALORUTEXT, label=_(u'Propiedades t\xe9rmicas'), name=u'valorUText', parent=self, pos=wx.Point(15, 131), size=wx.Size(118, 13), style=0)
        self.valorUText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.valorUChoice = MiChoice(choices=listadosWeb.listadoOpcionesUSueloTerreno, id=wxID_PANEL1VALORUCHOICE, name=u'valorUChoice', parent=self, pos=wx.Point(151, 128), size=wx.Size(200, 21), style=0)
        self.valorUChoice.Bind(wx.EVT_CHOICE, self.OnValorUChoiceChoice, id=wxID_PANEL1VALORUCHOICE)
        self.valorUChoice.SetStringSelection('Por defecto')
        self.UFinalText = wx.StaticText(id=wxID_PANEL1UFINALTEXT, label=_(u'Transmitancia t\xe9rmica'), name=u'UFinalText', parent=self, pos=wx.Point(460, 130), size=wx.Size(110, 25), style=0)
        self.UFinalText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.UFinalCuadro = wx.TextCtrl(id=wxID_PANEL1UFINALCUADRO, name=u'UFinalCuadro', parent=self, pos=wx.Point(601, 128), size=wx.Size(56, 21), style=0, value=u'')
        self.UFinalCuadro.Enable(False)
        self.unidadesUFinal = wx.StaticText(id=wxID_PANEL1UNIDADESUFINAL, label=_(u'W/m2K'), name=u'UFinalText', parent=self, pos=wx.Point(662, 130), size=wx.Size(40, 13), style=0)
        self.unidadesUFinal.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.UFinalText.SetForegroundColour(wx.Colour(100, 100, 100))
        self.unidadesUFinal.SetForegroundColour(wx.Colour(100, 100, 100))
        self.perimetroText = wx.StaticText(id=wxID_PANEL1PERIMETROTEXT, label=_(u'Per\xedmetro'), name=u'perimetroText', parent=self, pos=wx.Point(15, 155), size=wx.Size(50, 13), style=0)
        self.perimetroText.Show(False)
        self.perimetro = wx.TextCtrl(id=wxID_PANEL1PERIMETRO, name=u'perimetro', parent=self, pos=wx.Point(151, 153), size=wx.Size(56, 21), style=0, value=u'')
        self.perimetro.Bind(wx.EVT_TEXT, self.OnCambioPerimetro, id=wxID_PANEL1PERIMETRO)
        self.perimetro.SetForegroundColour(wx.Colour(100, 200, 0))
        self.perimetro.Show(False)
        self.PerimetroUnidadesText = wx.StaticText(id=wxID_PANEL1PERIMETROUNIDADESTEXT, label=_(u'm'), name=u'PerimetroUnidadesText', parent=self, pos=wx.Point(212, 155), size=wx.Size(10, 13), style=0)
        self.PerimetroUnidadesText.Show(False)
        self.aislamientoCheck = wx.CheckBox(id=wxID_PANEL1AISLAMIENTOCHECK, label=_(u'Tiene aislamiento t\xe9rmico'), name=u'aislamientoCheck', parent=self, pos=wx.Point(15, 185), size=wx.Size(150, 13), style=0)
        self.aislamientoCheck.SetValue(False)
        self.aislamientoCheck.Bind(wx.EVT_CHECKBOX, self.OnAislamientoCheckCheckbox, id=wxID_PANEL1AISLAMIENTOCHECK)
        self.aislamientoCheck.Show(False)
        self.CaracteristicasAislamientoLineaText = wx.StaticBox(id=wxID_CARACTERISTICASAISLAMIENTOLINEATEXT, label=_(u'Caracter\xedsticas del aislamiento t\xe9rmico'), name='LineaText', parent=self, pos=wx.Point(15, 210), size=wx.Size(680, 122), style=0)
        self.CaracteristicasAislamientoLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasAislamientoLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.CaracteristicasAislamientoLineaText.Show(False)
        self.tipoAislanteText = wx.StaticText(id=wxID_PANEL1TIPOAISLANTETEXT, label=_(u'Tipo de aislamiento'), name=u'tipoAislanteText', parent=self, pos=wx.Point(30, 233), size=wx.Size(120, 13), style=0)
        self.tipoAislanteText.Show(False)
        self.posicionAislanteChoice = MiChoice(choices=listadosWeb.listadoOpcionesAislamientoSueloTerreno, id=wxID_PANEL1TIPOAISLANTECHOICE, name=u'posicionAislanteChoice', parent=self, pos=wx.Point(151, 231), size=wx.Size(200, 21), style=0)
        self.posicionAislanteChoice.SetSelection(0)
        self.posicionAislanteChoice.Bind(wx.EVT_CHOICE, self.OnposicionAislanteChoice, id=wxID_PANEL1TIPOAISLANTECHOICE)
        self.posicionAislanteChoice.Show(False)
        self.resistenciaText = wx.StaticText(id=wxID_PANEL1PRESISTEXT, label=_(u'Definir Ra'), name=u'resistenciaText', parent=self, pos=wx.Point(30, 258), size=wx.Size(120, 21), style=0)
        self.resistenciaText.Show(False)
        self.resistenciaChoice = MiChoice(choices=listadosWeb.listadoOpcionesConocimientoAislamientoSueloTerreno, id=wxID_PANEL1TIPOAISLATECHOICE, name=u'resistenciaChoice', parent=self, pos=wx.Point(151, 256), size=wx.Size(200, 21), style=0)
        self.resistenciaChoice.SetSelection(1)
        self.resistenciaChoice.Show(False)
        self.resistenciaChoice.Bind(wx.EVT_CHOICE, self.onResistenciaChoice, id=wxID_PANEL1TIPOAISLATECHOICE)
        self.EspesorRadioButton = wx.RadioButton(id=wxID_PANEL1EPSRADIO, label=_(u'Espesor aislamiento'), name=u'EspesorRadioButton', parent=self, pos=wx.Point(30, 283), size=wx.Size(118, 13), style=wx.RB_GROUP)
        self.EspesorRadioButton.Bind(wx.EVT_RADIOBUTTON, self.onRaislanteRadio, id=wxID_PANEL1EPSRADIO)
        self.EspesorRadioButton.Show(False)
        self.espesor = wx.TextCtrl(id=wxID_PANEL1ESPESOR, name=u'espesor', parent=self, pos=wx.Point(151, 281), size=wx.Size(56, 21), style=0, value=u'')
        self.espesor.Bind(wx.EVT_TEXT, self.calcularCaracteristicasCerramiento, id=wxID_PANEL1ESPESOR)
        self.espesor.Show(False)
        self.espesor.Enable(True)
        self.espesorUnidadesText = wx.StaticText(id=wxID_PANEL1ESPESORUNITEXT, label=_(u'm'), name=u'espesorUnidadesText', parent=self, pos=wx.Point(212, 283), size=wx.Size(15, 13), style=0)
        self.espesorUnidadesText.Show(False)
        self.RaislateRadio = wx.RadioButton(id=wxID_PANEL1RAISLATERADIO, label=_(u'Ra'), name=u'RaislateRadio', parent=self, pos=wx.Point(30, 308), size=wx.Size(85, 13), style=0)
        self.RaislateRadio.Bind(wx.EVT_RADIOBUTTON, self.onRaislanteRadio, id=wxID_PANEL1RAISLATERADIO)
        self.RaislateRadio.Show(False)
        self.Raislate = wx.TextCtrl(id=wxID_PANEL1RAISLATE, name=u'Raislate', parent=self, pos=wx.Point(151, 306), size=wx.Size(56, 21), style=0, value=u'')
        self.Raislate.Bind(wx.EVT_TEXT, self.calcularCaracteristicasCerramiento, id=wxID_PANEL1RAISLATE)
        self.Raislate.Show(False)
        self.Raislate.Enable(False)
        self.RaislateUnidadesText = wx.StaticText(id=wxID_PANEL1RAISLATEUNITEXT, label=_(u'm2K/W'), name=u'RaislateUnidadesText', parent=self, pos=wx.Point(212, 308), size=wx.Size(40, 13), style=0)
        self.RaislateUnidadesText.Show(False)
        self.EspesorRadioButton2 = wx.RadioButton(id=wxID_PANEL1EPSRADIO2, label=_(u'Espesor aislamiento'), name=u'EspesorRadioButton2', parent=self, pos=wx.Point(30, 258), size=wx.Size(118, 13), style=wx.RB_GROUP)
        self.EspesorRadioButton2.Bind(wx.EVT_RADIOBUTTON, self.onRaislanteRadio2, id=wxID_PANEL1EPSRADIO2)
        self.EspesorRadioButton2.Show(False)
        self.espesor2 = wx.TextCtrl(id=wxID_PANEL1ESPESOR2, name=u'espesor2', parent=self, pos=wx.Point(151, 256), size=wx.Size(56, 21), style=0, value=u'')
        self.espesor2.Bind(wx.EVT_TEXT, self.calcularCaracteristicasCerramiento, id=wxID_PANEL1ESPESOR2)
        self.espesor2.Show(False)
        self.espesor2.Enable(True)
        self.espesorUnidadesText2 = wx.StaticText(id=wxID_PANEL1ESPESORUNITEXT2, label=_(u'm'), name=u'espesorUnidadesText2', parent=self, pos=wx.Point(212, 258), size=wx.Size(180, 13), style=0)
        self.espesorUnidadesText2.Show(False)
        self.RaislateRadio2 = wx.RadioButton(id=wxID_PANEL1RAISLATERADIO2, label=_(u'Rf'), name=u'RaislateRadio2', parent=self, pos=wx.Point(30, 283), size=wx.Size(85, 13), style=0)
        self.RaislateRadio2.Bind(wx.EVT_RADIOBUTTON, self.onRaislanteRadio2, id=wxID_PANEL1RAISLATERADIO2)
        self.RaislateRadio2.Show(False)
        self.Raislate2 = wx.TextCtrl(id=wxID_PANEL1RAISLATE2, name=u'Raislate2', parent=self, pos=wx.Point(151, 281), size=wx.Size(56, 21), style=0, value=u'')
        self.Raislate2.Bind(wx.EVT_TEXT, self.calcularCaracteristicasCerramiento, id=wxID_PANEL1RAISLATE2)
        self.Raislate2.Show(False)
        self.Raislate2.Enable(False)
        self.RaislateUnidadesText2 = wx.StaticText(id=wxID_PANEL1RAISLATEUNITEXT2, label=_(u'm2K/W'), name=u'RaislateUnidadesText2', parent=self, pos=wx.Point(212, 283), size=wx.Size(40, 13), style=0)
        self.RaislateUnidadesText2.Show(False)
        self.nombreMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1NOMBREMURO)
        self.superficieMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1SUPERFICIEMURO)
        self.longitudMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1LONGIMURO)
        self.alturaMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1ALTURAMURO)
        self.multiMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1MULTIMURO)
        self.profundidad.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1PROFUNDIDAD)
        self.UFinalCuadro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1UFINALCUADRO)
        self.perimetro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1PERIMETRO)
        self.espesor.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1ESPESOR)
        self.Raislate.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1RAISLATE)
        self.espesor2.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1ESPESOR2)
        self.Raislate2.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1RAISLATE2)
        self.subgrupoChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1SUBGRUPOCHOICE)
        self.valorUChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1VALORUCHOICE)
        self.posicionAislanteChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1TIPOAISLANTECHOICE)
        self.resistenciaChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1TIPOAISLATECHOICE)
        self.menor05Radio.Bind(wx.EVT_KILL_FOCUS, self.manejadorRadio, id=wxID_PANEL1MENOR05RADIO)
        self.mayor05Radio.Bind(wx.EVT_KILL_FOCUS, self.manejadorRadio, id=wxID_PANEL1MAYOR05RADIO)
        self.EspesorRadioButton.Bind(wx.EVT_KILL_FOCUS, self.manejadorRadio, id=wxID_PANEL1EPSRADIO)
        self.RaislateRadio.Bind(wx.EVT_KILL_FOCUS, self.manejadorRadio, id=wxID_PANEL1RAISLATERADIO)
        self.EspesorRadioButton2.Bind(wx.EVT_KILL_FOCUS, self.manejadorRadio, id=wxID_PANEL1EPSRADIO2)
        self.RaislateRadio2.Bind(wx.EVT_KILL_FOCUS, self.manejadorRadio, id=wxID_PANEL1RAISLATERADIO2)
        self.aislamientoCheck.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1AISLAMIENTOCHECK)

    def actualizaDiccionario(self):
        self.diccionario = {}
        self.diccionario['panelSueloConTerreno.nombreMuro'] = self.nombreMuro.GetValue()
        self.diccionario['panelSueloConTerreno.superficieMuro'] = self.superficieMuro.GetValue()
        self.diccionario['panelSueloConTerreno.longitudMuro'] = self.longitudMuro.GetValue()
        self.diccionario['panelSueloConTerreno.alturaMuro'] = self.alturaMuro.GetValue()
        self.diccionario['panelSueloConTerreno.multiMuro'] = self.multiMuro.GetValue()
        self.diccionario['panelSueloConTerreno.profundidad'] = self.profundidad.GetValue()
        self.diccionario['panelSueloConTerreno.UFinalCuadro'] = self.UFinalCuadro.GetValue()
        self.diccionario['panelSueloConTerreno.perimetro'] = self.perimetro.GetValue()
        self.diccionario['panelSueloConTerreno.espesor'] = self.espesor.GetValue()
        self.diccionario['panelSueloConTerreno.Raislate'] = self.Raislate.GetValue()
        self.diccionario['panelSueloConTerreno.espesor2'] = self.espesor2.GetValue()
        self.diccionario['panelSueloConTerreno.Raislate2'] = self.Raislate2.GetValue()
        self.diccionario['panelSueloConTerreno.subgrupoChoice'] = self.subgrupoChoice.GetSelection()
        self.diccionario['panelSueloConTerreno.valorUChoice'] = self.valorUChoice.GetSelection()
        self.diccionario['panelSueloConTerreno.posicionAislanteChoice'] = self.posicionAislanteChoice.GetSelection()
        self.diccionario['panelSueloConTerreno.resistenciaChoice'] = self.resistenciaChoice.GetSelection()
        self.diccionario['panelSueloConTerreno.radios'] = self.GetRadioValues()
        self.diccionario['panelSueloConTerreno.aislamientoCheck'] = self.aislamientoCheck.GetValue()

    def GetRadioValues(self):
        return [self.menor05Radio.GetValue(),
         self.mayor05Radio.GetValue(),
         self.EspesorRadioButton.GetValue(),
         self.RaislateRadio.GetValue(),
         self.EspesorRadioButton2.GetValue(),
         self.RaislateRadio2.GetValue()]

    def SetRadioValues(self, lista):
        self.menor05Radio.SetValue(lista[0])
        self.mayor05Radio.SetValue(lista[1])
        self.EspesorRadioButton.SetValue(lista[2])
        self.RaislateRadio.SetValue(lista[3])
        self.EspesorRadioButton2.SetValue(lista[4])
        self.RaislateRadio2.SetValue(lista[5])

    def cogeValoresDiccionario(self):
        self.nombreMuro.SetValue(self.diccionario['panelSueloConTerreno.nombreMuro'])
        self.superficieMuro.SetValue(self.diccionario['panelSueloConTerreno.superficieMuro'])
        self.longitudMuro.SetValue(self.diccionario['panelSueloConTerreno.longitudMuro'])
        self.alturaMuro.SetValue(self.diccionario['panelSueloConTerreno.alturaMuro'])
        self.multiMuro.SetValue(self.diccionario['panelSueloConTerreno.multiMuro'])
        self.profundidad.SetValue(self.diccionario['panelSueloConTerreno.profundidad'])
        self.UFinalCuadro.SetValue(self.diccionario['panelSueloConTerreno.UFinalCuadro'])
        self.perimetro.SetValue(self.diccionario['panelSueloConTerreno.perimetro'])
        self.espesor.SetValue(self.diccionario['panelSueloConTerreno.espesor'])
        self.Raislate.SetValue(self.diccionario['panelSueloConTerreno.Raislate'])
        self.espesor2.SetValue(self.diccionario['panelSueloConTerreno.espesor2'])
        self.Raislate2.SetValue(self.diccionario['panelSueloConTerreno.Raislate2'])
        self.subgrupoChoice.SetSelection(self.diccionario['panelSueloConTerreno.subgrupoChoice'])
        self.valorUChoice.SetSelection(self.diccionario['panelSueloConTerreno.valorUChoice'])
        self.posicionAislanteChoice.SetSelection(self.diccionario['panelSueloConTerreno.posicionAislanteChoice'])
        self.resistenciaChoice.SetSelection(self.diccionario['panelSueloConTerreno.resistenciaChoice'])
        self.aislamientoCheck.SetValue(self.diccionario['panelSueloConTerreno.aislamientoCheck'])
        lista = self.GetRadioValues()
        self.SetRadioValues(lista)
        self.OnMayor05Radio(None)
        self.OnMenor05Radio(None)
        self.OnValorUChoiceChoice(None)
        self.onRaislanteRadio(None)
        self.onRaislanteRadio2(None)
        self.onResistenciaChoice(None)
        self.OnAislamientoCheckCheckbox(None)
        return

    def onRaislanteRadio(self, event):
        """
        Metodo: onRaislanteRadio
        
        
        ARGUMENTOS:
                event:
        """
        if self.RaislateRadio.GetValue() == True:
            self.Raislate.Enable(True)
            self.espesor.Enable(False)
        else:
            self.Raislate.Enable(False)
            self.espesor.Enable(True)
        self.calcularCaracteristicasCerramiento(None)
        return

    def onRaislanteRadio2(self, event):
        """
        Metodo: onRaislanteRadio2
        
        
        ARGUMENTOS:
                event:
        """
        if self.RaislateRadio2.GetValue() == True:
            self.Raislate2.Enable(True)
            self.espesor2.Enable(False)
        else:
            self.Raislate2.Enable(False)
            self.espesor2.Enable(True)
        self.calcularCaracteristicasCerramiento(None)
        return

    def onResistenciaChoice(self, event):
        """
        Metodo: onResistenciaChoice
        
        
        ARGUMENTOS:
                event:
        """
        if 'Conocid' in self.resistenciaChoice.GetStringSelection():
            if self.aislamientoCheck.GetValue() == True and self.menor05Radio.GetValue() == True:
                self.RaislateRadio.Show(True)
                self.Raislate.Show(True)
                self.RaislateUnidadesText.Show(True)
                self.EspesorRadioButton.Show(True)
                self.espesor.Show(True)
                self.espesorUnidadesText.Show(True)
            elif self.aislamientoCheck.GetValue() == True and self.mayor05Radio.GetValue() == True:
                self.RaislateRadio2.Show(True)
                self.Raislate2.Show(True)
                self.RaislateUnidadesText2.Show(True)
                self.EspesorRadioButton2.Show(True)
                self.espesor2.Show(True)
                self.espesorUnidadesText2.Show(True)
        else:
            self.RaislateRadio.Show(False)
            self.Raislate.Show(False)
            self.RaislateUnidadesText.Show(False)
            self.EspesorRadioButton.Show(False)
            self.espesor.Show(False)
            self.espesorUnidadesText.Show(False)
            self.RaislateRadio2.Show(False)
            self.Raislate2.Show(False)
            self.RaislateUnidadesText2.Show(False)
            self.EspesorRadioButton2.Show(False)
            self.espesor2.Show(False)
            self.espesorUnidadesText2.Show(False)
        self.calcularCaracteristicasCerramiento(None)
        return

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
        self._init_ctrls(parent, id, pos, size, style, name)
        self.bol = True
        self.subgrupoChoice.SetItems(self.cargarRaices())
        self.elegirRaiz()
        self.bolCalcularCaracteristicas = True
        self.UCerramiento = ''
        self.densidadCerramiento = ''
        self.calcularCaracteristicasCerramiento(None)
        self.resistenciaText.SetLabel(_(u'Definir Ra'))
        self.resistenciaText.SetSize(wx.Size(120, 21))
        self.actualizaDiccionario()
        return

    def cargarTransmitanciaTermicaGlobal(self):
        """
        Metodo: cargarTransmitanciaTermicaGlobal
        
        
        """
        try:
            if float(self.UCerramiento) >= 0.0:
                self.UFinalCuadro.SetValue(str(self.UCerramiento))
            else:
                self.UFinalCuadro.SetValue('')
        except (ValueError, TypeError):
            self.UFinalCuadro.SetValue('')

    def calcularCaracteristicasCerramiento(self, event):
        """
        Metodo: calcularCaracteristicasCerramiento
        
        
        ARGUMENTOS:
                event:
        """
        if self.bolCalcularCaracteristicas == True:
            try:
                if self.menor05Radio.GetValue() == True:
                    profundidad = '-0.5'
                else:
                    profundidad = '+0.5'
                if 'Por defecto' in self.valorUChoice.GetStringSelection():
                    if profundidad == '+0.5' and float(self.profundidad.GetValue()) <= 0.5:
                        self.UCerramiento = ''
                    else:
                        valoresCerr = tablasValores.tablasValores('Suelo', 'terreno', [self.parent.parent.parent.panelDatosGenerales.anoConstruccionChoice.GetSelection(), self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection(), profundidad], 'Por defecto')
                        self.UCerramiento = valoresCerr.UCerramiento
                        self.densidadCerramiento = valoresCerr.densidadCerramiento
                elif 'Estimad' in self.valorUChoice.GetStringSelection():
                    self.densidadCerramiento = 750
                    try:
                        B = float(self.superficieMuro.GetValue()) / (0.5 * float(self.perimetro.GetValue()))
                    except ZeroDivisionError:
                        B = 100.0

                    if profundidad == '-0.5':
                        if self.aislamientoCheck.GetValue() == False:
                            D = 0
                            Ra = 0
                        else:
                            if self.posicionAislanteChoice.GetStringSelection() == 'Continuo':
                                D = 1.5
                            else:
                                D = 0.5
                            if self.resistenciaChoice.GetStringSelection() == 'No conocida':
                                Ra = 0.5
                            elif self.RaislateRadio.GetValue() == True:
                                Ra = float(self.Raislate.GetValue())
                            else:
                                Ra = float(self.espesor.GetValue()) / 0.046
                        self.UCerramiento = apendiceE.sueloTerrenoCaso1(D, Ra, B)
                    else:
                        z = float(self.profundidad.GetValue())
                        if z <= 0.5:
                            self.UCerramiento = ''
                        if self.aislamientoCheck.GetValue() == False:
                            Rf = 0.12
                        elif self.resistenciaChoice.GetStringSelection() == 'No conocida':
                            Rf = 0.5
                        elif self.RaislateRadio2.GetValue() == True:
                            Rf = float(self.Raislate2.GetValue())
                        else:
                            Rf = float(self.espesor2.GetValue()) / 0.046 + 0.12
                        self.UCerramiento = apendiceE.sueloTerrenoCaso2(z, Rf, B)
                self.UCerramiento = round(self.UCerramiento, 2)
                self.cargarTransmitanciaTermicaGlobal()
            except:
                logging.info(u'Excepcion en: %s' % __name__)
                self.UCerramiento = ''
                self.cargarTransmitanciaTermicaGlobal()

    def elegirRaiz(self):
        """
        Metodo: elegirRaiz
        
        
        """
        try:
            sel = self.parent.arbolCerramientos.GetSelection()
            self.subgrupoChoice.SetStringSelection(u'Edificio Objeto')
            raiz = self.parent.arbolCerramientos.GetRootItem()
            while sel != raiz:
                for i in range(len(self.parent.parent.subgrupos)):
                    if self.parent.arbolCerramientos.GetItemText(sel) == self.parent.parent.subgrupos[i].nombre:
                        self.subgrupoChoice.SetStringSelection(self.parent.arbolCerramientos.GetItemText(sel))
                        return

                sel = self.parent.arbolCerramientos.GetItemParent(sel)

        except:
            logging.info(u'Excepcion en: %s' % __name__)
            self.subgrupoChoice.SetStringSelection(u'Edificio Objeto')

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

    def OnCambioPerimetro(self, event):
        """
        Metodo: OnCambioPerimetro
        
        
        ARGUMENTOS:
                event:
        """
        self.perimetro.SetForegroundColour(wx.Colour(0, 0, 0))
        self.calcularCaracteristicasCerramiento(None)
        return

    def OnCambioSuperficie(self, event):
        """
        Metodo: OnCambioSuperficie
        
        
        ARGUMENTOS:
                event:
        """
        if self.bol == True:
            self.longitudMuro.SetValue('')
            self.alturaMuro.SetValue('')
            self.multiMuro.SetValue('1')
        self.calcularCaracteristicasCerramiento(None)
        return

    def OnCambioLAMText(self, event):
        """
        Metodo: OnCambioLAMText
        
        
        ARGUMENTOS:
                event:
        """
        longitud = self.longitudMuro.GetValue()
        altura = self.alturaMuro.GetValue()
        multiplicador = self.multiMuro.GetValue()
        if ',' in longitud:
            longitud = longitud.replace(',', '.')
            self.longitudMuro.SetValue(longitud)
            self.longitudMuro.SetInsertionPointEnd()
        if ',' in altura:
            altura = altura.replace(',', '.')
            self.alturaMuro.SetValue(altura)
            self.alturaMuro.SetInsertionPointEnd()
        if ',' in multiplicador:
            multiplicador = multiplicador.replace(',', '.')
            self.multiMuro.SetValue(multiplicador)
            self.multiMuro.SetInsertionPointEnd()
        try:
            lon = float(self.longitudMuro.GetValue())
            alt = float(self.alturaMuro.GetValue())
            mul = float(self.multiMuro.GetValue())
            self.bol = False
            superficieTotal = round(lon * alt * mul, 2)
            self.superficieMuro.SetValue(str(superficieTotal))
            self.bol = True
        except (ValueError, TypeError):
            pass

    def OnposicionAislanteChoice(self, event):
        """
        Metodo: OnposicionAislanteChoice
        
        
        ARGUMENTOS:
                event): ###Indica si tiene que dejar ver la opcino ancho de banda o :
        """
        self.calcularCaracteristicasCerramiento(None)
        return

    def OnMayor05Radio(self, event):
        """
        Metodo: OnMayor05Radio
        
        
        ARGUMENTOS:
                event:
        """
        self.profundidad.Enable(True)
        self.profundidadUnidadesText.Enable(True)
        self.resistenciaText.SetLabel(_(u'Definir Rf'))
        self.resistenciaText.SetSize(wx.Size(120, 21))
        if 'Estimad' in self.valorUChoice.GetStringSelection():
            self.posicionAislanteChoice.Show(False)
            self.tipoAislanteText.Show(False)
            self.resistenciaText.SetPosition(wx.Point(30, 233))
            self.resistenciaChoice.SetPosition(wx.Point(151, 231))
        if 'Estimad' in self.valorUChoice.GetStringSelection() and self.aislamientoCheck.GetValue() == True and 'Conocid' in self.resistenciaChoice.GetStringSelection():
            self.RaislateRadio2.Show(True)
            self.Raislate2.Show(True)
            self.RaislateUnidadesText2.Show(True)
            self.EspesorRadioButton2.Show(True)
            self.espesor2.Show(True)
            self.espesorUnidadesText2.Show(True)
            self.RaislateRadio.Show(False)
            self.Raislate.Show(False)
            self.RaislateUnidadesText.Show(False)
            self.EspesorRadioButton.Show(False)
            self.espesor.Show(False)
            self.espesorUnidadesText.Show(False)
        else:
            self.RaislateRadio.Show(False)
            self.Raislate.Show(False)
            self.RaislateUnidadesText.Show(False)
            self.EspesorRadioButton.Show(False)
            self.espesor.Show(False)
            self.espesorUnidadesText.Show(False)
            self.RaislateRadio2.Show(False)
            self.Raislate2.Show(False)
            self.RaislateUnidadesText2.Show(False)
            self.EspesorRadioButton2.Show(False)
            self.espesor2.Show(False)
            self.espesorUnidadesText2.Show(False)
            self.posicionAislanteChoice.Show(False)
            self.tipoAislanteText.Show(False)
        self.calcularCaracteristicasCerramiento(None)
        return

    def OnMenor05Radio(self, event):
        """
        Metodo: OnMenor05Radio
        
        
        ARGUMENTOS:
                event:
        """
        self.resistenciaText.SetLabel(_(u'Definir Ra'))
        self.resistenciaText.SetSize(wx.Size(120, 21))
        self.profundidad.Enable(False)
        self.profundidadUnidadesText.Enable(False)
        if 'Estimad' in self.valorUChoice.GetStringSelection() and self.aislamientoCheck.GetValue() == True:
            self.posicionAislanteChoice.Show(True)
            self.tipoAislanteText.Show(True)
            self.resistenciaText.SetPosition(wx.Point(30, 258))
            self.resistenciaChoice.SetPosition(wx.Point(151, 256))
        else:
            self.posicionAislanteChoice.Show(False)
            self.tipoAislanteText.Show(False)
        if 'Estimad' in self.valorUChoice.GetStringSelection() and self.aislamientoCheck.GetValue() == True and 'Conocid' in self.resistenciaChoice.GetStringSelection():
            self.RaislateRadio.Show(True)
            self.Raislate.Show(True)
            self.RaislateUnidadesText.Show(True)
            self.EspesorRadioButton.Show(True)
            self.espesor.Show(True)
            self.espesorUnidadesText.Show(True)
            self.RaislateRadio2.Show(False)
            self.Raislate2.Show(False)
            self.RaislateUnidadesText2.Show(False)
            self.EspesorRadioButton2.Show(False)
            self.espesor2.Show(False)
            self.espesorUnidadesText2.Show(False)
        else:
            self.RaislateRadio.Show(False)
            self.Raislate.Show(False)
            self.RaislateUnidadesText.Show(False)
            self.EspesorRadioButton.Show(False)
            self.espesor.Show(False)
            self.espesorUnidadesText.Show(False)
            self.RaislateRadio2.Show(False)
            self.Raislate2.Show(False)
            self.RaislateUnidadesText2.Show(False)
            self.EspesorRadioButton2.Show(False)
            self.espesor2.Show(False)
            self.espesorUnidadesText2.Show(False)
        self.calcularCaracteristicasCerramiento(None)
        return

    def OnAislamientoCheckCheckbox(self, event):
        """
        Metodo: OnAislamientoCheckCheckbox
        
        
        ARGUMENTOS:
                event):   ###Cuando pulso si Tiene aislamiento T\xe9rmi:
        """
        if self.aislamientoCheck.GetValue() == True:
            self.CaracteristicasAislamientoLineaText.Show(True)
            self.resistenciaChoice.Show(True)
            self.resistenciaText.Show(True)
            if self.menor05Radio.GetValue() == True:
                self.posicionAislanteChoice.Show(True)
                self.tipoAislanteText.Show(True)
                self.resistenciaText.SetPosition(wx.Point(30, 258))
                self.resistenciaChoice.SetPosition(wx.Point(151, 256))
            else:
                self.posicionAislanteChoice.Show(False)
                self.tipoAislanteText.Show(False)
                self.resistenciaText.SetPosition(wx.Point(30, 233))
                self.resistenciaChoice.SetPosition(wx.Point(151, 231))
            if self.menor05Radio.GetValue() == True and 'Conocid' in self.resistenciaChoice.GetStringSelection():
                self.posicionAislanteChoice.Show(True)
                self.tipoAislanteText.Show(True)
                self.RaislateRadio.Show(True)
                self.Raislate.Show(True)
                self.RaislateUnidadesText.Show(True)
                self.EspesorRadioButton.Show(True)
                self.espesor.Show(True)
                self.espesorUnidadesText.Show(True)
                self.RaislateRadio2.Show(False)
                self.Raislate2.Show(False)
                self.RaislateUnidadesText2.Show(False)
                self.EspesorRadioButton2.Show(False)
                self.espesor2.Show(False)
                self.espesorUnidadesText2.Show(False)
            elif self.mayor05Radio.GetValue() == True and 'Conocid' in self.resistenciaChoice.GetStringSelection():
                self.posicionAislanteChoice.Show(False)
                self.tipoAislanteText.Show(False)
                self.RaislateRadio2.Show(True)
                self.Raislate2.Show(True)
                self.RaislateUnidadesText2.Show(True)
                self.EspesorRadioButton2.Show(True)
                self.espesor2.Show(True)
                self.espesorUnidadesText2.Show(True)
                self.RaislateRadio.Show(False)
                self.Raislate.Show(False)
                self.RaislateUnidadesText.Show(False)
                self.EspesorRadioButton.Show(False)
                self.espesor.Show(False)
                self.espesorUnidadesText.Show(False)
            else:
                self.RaislateRadio.Show(False)
                self.Raislate.Show(False)
                self.RaislateUnidadesText.Show(False)
                self.EspesorRadioButton.Show(False)
                self.espesor.Show(False)
                self.espesorUnidadesText.Show(False)
                self.RaislateRadio2.Show(False)
                self.Raislate2.Show(False)
                self.RaislateUnidadesText2.Show(False)
                self.EspesorRadioButton2.Show(False)
                self.espesor2.Show(False)
                self.espesorUnidadesText2.Show(False)
        else:
            self.CaracteristicasAislamientoLineaText.Show(False)
            self.resistenciaChoice.Show(False)
            self.posicionAislanteChoice.Show(False)
            self.tipoAislanteText.Show(False)
            self.resistenciaText.Show(False)
            self.RaislateRadio.Show(False)
            self.Raislate.Show(False)
            self.RaislateUnidadesText.Show(False)
            self.EspesorRadioButton.Show(False)
            self.espesor.Show(False)
            self.espesorUnidadesText.Show(False)
            self.RaislateRadio2.Show(False)
            self.Raislate2.Show(False)
            self.RaislateUnidadesText2.Show(False)
            self.EspesorRadioButton2.Show(False)
            self.espesor2.Show(False)
            self.espesorUnidadesText2.Show(False)
        self.calcularCaracteristicasCerramiento(None)
        return

    def OnValorUChoiceChoice(self, event):
        """
        Metodo: OnValorUChoiceChoice
        
        
        ARGUMENTOS:
                event:
        """
        if 'Estimad' in self.valorUChoice.GetStringSelection():
            self.perimetro.Show(True)
            self.perimetroText.Show(True)
            self.PerimetroUnidadesText.Show(True)
            self.aislamientoCheck.Show(True)
            if self.menor05Radio.GetValue() == True:
                self.OnMenor05Radio(None)
            else:
                self.OnMayor05Radio(None)
            self.OnAislamientoCheckCheckbox(None)
            self.OnposicionAislanteChoice(None)
        else:
            self.CaracteristicasAislamientoLineaText.Show(False)
            self.perimetro.Show(False)
            self.perimetroText.Show(False)
            self.PerimetroUnidadesText.Show(False)
            self.aislamientoCheck.Show(False)
            self.resistenciaChoice.Show(False)
            self.posicionAislanteChoice.Show(False)
            self.tipoAislanteText.Show(False)
            self.resistenciaText.Show(False)
            self.RaislateRadio.Show(False)
            self.Raislate.Show(False)
            self.RaislateUnidadesText.Show(False)
            self.EspesorRadioButton.Show(False)
            self.espesor.Show(False)
            self.espesorUnidadesText.Show(False)
            self.RaislateRadio2.Show(False)
            self.Raislate2.Show(False)
            self.RaislateUnidadesText2.Show(False)
            self.EspesorRadioButton2.Show(False)
            self.espesor2.Show(False)
            self.espesorUnidadesText2.Show(False)
        self.calcularCaracteristicasCerramiento(None)
        return

    def comprobarDatos(self):
        """
        Metodo: comprobarDatos
        
        
                self):
        """
        listaErrores = u''
        dato = self.superficieMuro.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.superficieMuro.SetValue(dato)
        dato = self.profundidad.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.profundidad.SetValue(dato)
        dato = self.perimetro.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.perimetro.SetValue(dato)
        dato = self.espesor.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.espesor.SetValue(dato)
        dato = self.Raislate.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.Raislate.SetValue(dato)
        dato = self.espesor2.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.espesor2.SetValue(dato)
        dato = self.Raislate2.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.Raislate2.SetValue(dato)
        listaErrores += Comprueba(self.nombreMuro.GetValue(), 1, listaErrores, _(u'nombre')).ErrorDevuelto
        listaErrores += Comprueba(self.subgrupoChoice.GetStringSelection(), 0, listaErrores, _(u'zona')).ErrorDevuelto
        listaErrores += Comprueba(self.superficieMuro.GetValue(), 2, listaErrores, _(u'superficie'), 0).ErrorDevuelto
        if self.menor05Radio.GetValue() == True:
            if self.valorUChoice.GetStringSelection() == 'Estimadas':
                listaErrores += Comprueba(self.perimetro.GetValue(), 2, listaErrores, _(u'per\xedmetro'), 0).ErrorDevuelto
                if self.aislamientoCheck.GetValue() == True:
                    if self.resistenciaChoice.GetStringSelection() == 'Conocida':
                        if self.EspesorRadioButton.GetValue() == True:
                            listaErrores += Comprueba(self.espesor.GetValue(), 2, listaErrores, _(u'espesor'), 0).ErrorDevuelto
                        else:
                            listaErrores += Comprueba(self.Raislate.GetValue(), 2, listaErrores, _(u'resistencia del aislamiento'), 0).ErrorDevuelto
            elif self.valorUChoice.GetStringSelection() == 'Por defecto':
                pass
        else:
            listaErrores += Comprueba(self.profundidad.GetValue(), 2, listaErrores, _(u'profundidad'), 0.500001).ErrorDevuelto
            if self.valorUChoice.GetStringSelection() == 'Estimadas':
                listaErrores += Comprueba(self.perimetro.GetValue(), 2, listaErrores, _(u'per\xedmetro'), 0).ErrorDevuelto
                if self.aislamientoCheck.GetValue() == True:
                    if self.resistenciaChoice.GetStringSelection() == 'Conocida':
                        if self.EspesorRadioButton2.GetValue() == True:
                            listaErrores += Comprueba(self.espesor2.GetValue(), 2, listaErrores, _(u'espesor del aislamiento'), 0).ErrorDevuelto
                        else:
                            listaErrores += Comprueba(self.Raislate2.GetValue(), 2, listaErrores, _(u'resistencia del suelo'), 0).ErrorDevuelto
            elif self.valorUChoice.GetStringSelection() == 'Por defecto':
                pass
        return listaErrores

    def cogerDatos(self):
        """
        Metodo: cogerDatos
        
        
        """
        listaErrores = self.comprobarDatos()
        if listaErrores != u'':
            return listaErrores
        datos = []
        datos.append(self.nombreMuro.GetValue())
        datos.append('Suelo')
        datos.append(self.superficieMuro.GetValue())
        datos.append(self.UCerramiento)
        datos.append(self.densidadCerramiento)
        datos.append('Suelo')
        datos.append('')
        datos.append(u'Sin patr\xf3n')
        datos.append(self.valorUChoice.GetStringSelection())
        datos.append(self.menor05Radio.GetValue())
        datos.append(self.profundidad.GetValue())
        datosOpciones = []
        if 'Estimad' in self.valorUChoice.GetStringSelection():
            if self.menor05Radio.GetValue() == True:
                datosOpciones.append(self.perimetro.GetValue())
                datosOpciones.append(self.aislamientoCheck.GetValue())
                datosOpciones.append(self.posicionAislanteChoice.GetStringSelection())
                datosOpciones.append(self.resistenciaChoice.GetStringSelection())
                datosOpciones.append(self.RaislateRadio.GetValue())
                datosOpciones.append(self.Raislate.GetValue())
                datosOpciones.append(self.EspesorRadioButton.GetValue())
                datosOpciones.append(self.espesor.GetValue())
            else:
                datosOpciones.append(self.perimetro.GetValue())
                datosOpciones.append(self.aislamientoCheck.GetValue())
                datosOpciones.append(self.posicionAislanteChoice.GetStringSelection())
                datosOpciones.append(self.resistenciaChoice.GetStringSelection())
                datosOpciones.append(self.RaislateRadio2.GetValue())
                datosOpciones.append(self.Raislate2.GetValue())
                datosOpciones.append(self.EspesorRadioButton2.GetValue())
                datosOpciones.append(self.espesor2.GetValue())
                datosOpciones.append(self.profundidad.GetValue())
        datos.append(datosOpciones)
        datos.append(self.longitudMuro.GetValue())
        datos.append(self.alturaMuro.GetValue())
        datos.append(self.multiMuro.GetValue())
        datos.append(self.subgrupoChoice.GetStringSelection())
        datos.append('terreno')
        return datos

    def cargarDatos(self, datos):
        """
        Metodo: cargarDatos
        
        
        ARGUMENTOS:
                datos:
        """
        self.nombreMuro.SetValue(datos[0])
        self.superficieMuro.SetValue(datos[2])
        self.valorUChoice.SetStringSelection(datos[8])
        self.menor05Radio.SetValue(datos[9])
        self.mayor05Radio.SetValue(not datos[9])
        if datos[9] == False:
            self.profundidad.Enable(True)
            self.profundidad.SetValue(datos[10])
            self.OnMayor05Radio(None)
        else:
            self.profundidad.Enable(False)
            self.OnMenor05Radio(None)
        self.OnValorUChoiceChoice(None)
        if 'Estimad' in datos[8]:
            if datos[9] == True:
                self.perimetro.SetValue(datos[11][0])
                self.aislamientoCheck.SetValue(datos[11][1])
                self.posicionAislanteChoice.SetStringSelection(datos[11][2])
                self.resistenciaChoice.SetStringSelection(datos[11][3])
                self.RaislateRadio.SetValue(datos[11][4])
                self.Raislate.SetValue(datos[11][5])
                self.EspesorRadioButton.SetValue(datos[11][6])
                self.espesor.SetValue(datos[11][7])
                self.onRaislanteRadio(None)
            else:
                self.perimetro.SetValue(datos[11][0])
                self.aislamientoCheck.SetValue(datos[11][1])
                self.posicionAislanteChoice.SetStringSelection(datos[11][2])
                self.resistenciaChoice.SetStringSelection(datos[11][3])
                self.RaislateRadio2.SetValue(datos[11][4])
                self.Raislate2.SetValue(datos[11][5])
                self.EspesorRadioButton2.SetValue(datos[11][6])
                self.espesor2.SetValue(datos[11][7])
                self.onRaislanteRadio2(None)
        self.longitudMuro.SetValue(datos[12])
        self.alturaMuro.SetValue(datos[13])
        self.multiMuro.SetValue(datos[14])
        self.subgrupoChoice.SetStringSelection(datos[15])
        self.parent.panelElegirObjeto.definirSuelo.SetValue(True)
        self.parent.panelElegirObjeto.mostrarOpcionesContactoCubierta()
        self.parent.panelElegirObjeto.contactoSuelo.SetValue(True)
        colorSombra = wx.Color(240, 240, 240)
        colorNormal = wx.Color(255, 255, 255)
        self.parent.panelElegirObjeto.definirSuelo.SetBackgroundColour(colorSombra)
        self.parent.panelElegirObjeto.definirCubierta.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirFachada.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirParticionInterior.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirHueco.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirPuenteTermico.SetBackgroundColour(colorNormal)
        self.onResistenciaChoice(None)
        self.OnAislamientoCheckCheckbox(None)
        self.actualizaDiccionario()
        return