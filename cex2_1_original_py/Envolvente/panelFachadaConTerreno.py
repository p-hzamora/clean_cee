# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\panelFachadaConTerreno.pyc
# Compiled at: 2015-02-23 10:43:01
"""
Modulo: panelFachadaConTerreno.py

"""
from Envolvente.comprobarCampos import Comprueba
from miChoice import MiChoice
import Envolvente.apendiceE as apendiceE, Envolvente.tablasValores as tablasValores, Calculos.listadosWeb as listadosWeb, nuevoUndo, wx, logging
wxID_PANEL1, wxID_PANEL1AISLAMIENTOCHECK, wxID_PANEL1NOMBREMURO, wxID_PANEL1NOMBREMUROTEXT, wxID_PANEL1PROFUNDIDADENTERRADA, wxID_PANEL1PROFUNDIDADTEXT, wxID_PANEL1PROFUNDIDADUNIDADESTEXT, wxID_PANEL1SUPERFICIEMURO, wxID_PANEL1SUPERFICIETEXT, wxID_PANEL1SUPERFICIEUNIDADESTEXT, wxID_PANEL1VALORUCHOICE, wxID_PANEL1AISLAMIENTOCHECK, wxID_PANEL1VALORUTEXT, wxID_PANEL1URADIOBUTTON, wxID_PANEL1LIBRERIARADIOBUTTON, wxID_PANEL1VALORU, wxID_PANEL1CERRAMIENTOSCHOICE, wxID_PANEL1LONGIMUROTEXT, wxID_PANEL1ALTURAMUROTEXT, wxID_PANEL1MULTIMUROTEXT, wxID_PANEL1LONGIMURO, wxID_PANEL1ALTURAMURO, wxID_PANEL1MULTIMURO, wxID_PANEL1LONGITUDUNIDADESTEXT, wxID_PANEL1ALTURAUNIDADESTEXT, wxID_PANEL1SUBGRUPOTEXT, wxID_PANEL1SUBGRUPOCHOICE, wxID_PANEL1UNIDADESUTEXT, wxID_PANEL1AISLANTERADIOBUTTON, wxID_PANEL1RAISLATERADIO, wxID_PANEL1ESPESORAISLANTE, wxID_PANEL1RAISLANTE, wxID_PANEL1RAISLANTEUNIDADESTEXT, wxID_PANEL1UNIDADESESPESORTEXT, wxID_PANEL1UFINALTEXT, wxID_PANEL1UFINALCUADRO, wxID_PANEL1UNIDADESUFINAL, wxID_PANEL1TIPOAISLATECHOICE, wxID_PANEL1ESPESORAISLATETEXT, wxID_PANEL1ESPESORAISLANTE, wxID_PANEL1UNIDADESESPESORAISLATETEXT, wxID_PANEL1LANDAAISLATETEXT, wxID_PANEL1LANDAAISLANTE, wxID_PANEL1LANDAUNIDADESTEXT, wxID_DIMENSIONESLINEATEXT, wxID_CARACTERISTICASAISLAMIENTOLINEATEXT = [ wx.NewId() for _init_ctrls in range(46) ]

class Panel1(wx.Panel, nuevoUndo.VistaUndo):
    """
    Clase: Panel1 del modulo panelFachadaConTerreno.py

    """

    def OnNombreMuro(self, event):
        """
        Metodo: OnNombreMuro

        ARGUMENTOS:
                event:
        """
        if self.nombreMuro.GetValue() == _('Muro con terreno'):
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
        wx.Panel.__init__(self, id=ide, name='panelFachadaConTerreno', parent=prnt, pos=posi, size=siz, style=styl)
        self.SetBackgroundColour('white')
        self.nombreMuroText = wx.StaticText(id=wxID_PANEL1NOMBREMUROTEXT, label=_('Nombre'), name='nombreMuroText', parent=self, pos=wx.Point(15, 2), size=wx.Size(102, 13), style=0)
        self.nombreMuro = wx.TextCtrl(id=wxID_PANEL1NOMBREMURO, name='nombreMuro', parent=self, pos=wx.Point(151, 0), size=wx.Size(210, 21), style=0, value=_('Muro con terreno'))
        self.nombreMuro.SetForegroundColour(wx.Colour(100, 200, 0))
        self.nombreMuro.Bind(wx.EVT_TEXT, self.OnNombreMuro, id=wxID_PANEL1NOMBREMURO)
        self.subgrupoText = wx.StaticText(id=wxID_PANEL1SUBGRUPOTEXT, label=_('Zona'), name='subgrupoText', parent=self, pos=wx.Point(435, 2), size=wx.Size(50, 13), style=0)
        self.subgrupoChoice = MiChoice(choices=[], id=wxID_PANEL1SUBGRUPOCHOICE, name='subgrupoChoice', parent=self, pos=wx.Point(496, 0), size=wx.Size(214, 21), style=0)
        self.EficienciaLineaText = wx.StaticBox(id=-1, label=_('Parámetros característicos del cerramiento'), name='EficienciaLineaText', parent=self, pos=wx.Point(0, 107), size=wx.Size(710, 235), style=0)
        self.EficienciaLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.EficienciaLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.DimensionesLineaText = wx.StaticBox(id=wxID_DIMENSIONESLINEATEXT, label=_('Dimensiones'), name='LineaText', parent=self, pos=wx.Point(0, 26), size=wx.Size(361, 77), style=0)
        self.DimensionesLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.DimensionesLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.superficieText = wx.StaticText(id=wxID_PANEL1SUPERFICIETEXT, label=_('Superficie'), name='superficieText', parent=self, pos=wx.Point(15, 46), size=wx.Size(51, 13), style=0)
        self.superficieMuro = wx.TextCtrl(id=wxID_PANEL1SUPERFICIEMURO, name='superficieMuro', parent=self, pos=wx.Point(151, 44), size=wx.Size(80, 21), style=0, value='')
        self.superficieMuro.Bind(wx.EVT_TEXT, self.OnCambioSuperficie, id=wxID_PANEL1SUPERFICIEMURO)
        self.superficieUnidadesText = wx.StaticText(id=wxID_PANEL1SUPERFICIEUNIDADESTEXT, label=_('m2'), name='superficieUnidadesText', parent=self, pos=wx.Point(236, 46), size=wx.Size(14, 13), style=0)
        self.longitudMuroText = wx.StaticText(id=wxID_PANEL1LONGIMUROTEXT, label=_('Longitud'), name='longitudMuroText', parent=self, pos=wx.Point(151, 69), size=wx.Size(28, 13), style=0)
        self.longitudMuro = wx.TextCtrl(id=wxID_PANEL1LONGIMURO, name='longitudMuro', parent=self, pos=wx.Point(191, 67), size=wx.Size(40, 15), style=0, value='')
        self.longitudMuro.Bind(wx.EVT_TEXT, self.OnCambioLAMText, id=wxID_PANEL1LONGIMURO)
        self.LongitudUnidadesText = wx.StaticText(id=wxID_PANEL1LONGITUDUNIDADESTEXT, label=_('m'), name='profundidadUnidadesText', parent=self, pos=wx.Point(236, 69), size=wx.Size(14, 13), style=0)
        self.alturaMuroText = wx.StaticText(id=wxID_PANEL1ALTURAMUROTEXT, label=_('Altura'), name='alturaMuroText', parent=self, pos=wx.Point(151, 85), size=wx.Size(28, 13), style=0)
        self.alturaMuro = wx.TextCtrl(id=wxID_PANEL1ALTURAMURO, name='alturaMuro', parent=self, pos=wx.Point(191, 83), size=wx.Size(40, 15), style=0, value='')
        self.alturaMuro.Bind(wx.EVT_TEXT, self.OnCambioLAMText, id=wxID_PANEL1ALTURAMURO)
        self.alturaMuroUnidades = wx.StaticText(id=wxID_PANEL1ALTURAUNIDADESTEXT, label=_('m'), name='alturaMuroUnidades', parent=self, pos=wx.Point(236, 85), size=wx.Size(14, 13), style=0)
        self.multiMuroText = wx.StaticText(id=wxID_PANEL1MULTIMUROTEXT, label=_('Multiplicador'), name='multiMuroText', parent=self, pos=wx.Point(0, 94), size=wx.Size(80, 13), style=0)
        self.multiMuroText.Show(False)
        self.multiMuro = wx.TextCtrl(id=wxID_PANEL1MULTIMURO, name='multiMuro', parent=self, pos=wx.Point(120, 94), size=wx.Size(80, 21), style=0, value='1')
        self.multiMuro.Show(False)
        self.multiMuro.Bind(wx.EVT_TEXT, self.OnCambioLAMText, id=wxID_PANEL1MULTIMURO)
        self.longitudMuroText.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.LongitudUnidadesText.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.alturaMuroText.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.alturaMuroUnidades.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.valorUText = wx.StaticText(id=wxID_PANEL1VALORUTEXT, label=_('Propiedades térmicas'), name='valorUText', parent=self, pos=wx.Point(15, 131), size=wx.Size(118, 13), style=0)
        self.valorUText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.valorUChoice = MiChoice(choices=listadosWeb.listadoOpcionesUFachadaTerreno, id=wxID_PANEL1VALORUCHOICE, name='valorUChoice', parent=self, pos=wx.Point(151, 128), size=wx.Size(200, 21), style=0)
        self.valorUChoice.Bind(wx.EVT_CHOICE, self.OnValorUChoiceChoice, id=wxID_PANEL1VALORUCHOICE)
        self.valorUChoice.SetStringSelection('Por defecto')
        self.UFinalText = wx.StaticText(id=wxID_PANEL1UFINALTEXT, label=_('Transmitancia térmica'), name='UFinalText', parent=self, pos=wx.Point(460, 130), size=wx.Size(110, 25), style=0)
        self.UFinalText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.UFinalCuadro = wx.TextCtrl(id=wxID_PANEL1UFINALCUADRO, name='UFinalCuadro', parent=self, pos=wx.Point(601, 128), size=wx.Size(56, 21), style=0, value='')
        self.UFinalCuadro.Enable(False)
        self.unidadesUFinal = wx.StaticText(id=wxID_PANEL1UNIDADESUFINAL, label=_('W/m2K'), name='UFinalText', parent=self, pos=wx.Point(662, 130), size=wx.Size(40, 13), style=0)
        self.unidadesUFinal.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.UFinalText.SetForegroundColour(wx.Colour(100, 100, 100))
        self.unidadesUFinal.SetForegroundColour(wx.Colour(100, 100, 100))
        self.profundidadText = wx.StaticText(id=wxID_PANEL1PROFUNDIDADTEXT, label=_('Profundidad de la parte enterrada'), name='profundidadText', parent=self, pos=wx.Point(15, 164), size=wx.Size(120, 25), style=0)
        self.profundidadText.Show(False)
        self.profundidadEnterrada = wx.TextCtrl(id=wxID_PANEL1PROFUNDIDADENTERRADA, name='profundidadEnterrada', parent=self, pos=wx.Point(151, 165), size=wx.Size(56, 21), style=0, value='0.5')
        self.profundidadEnterrada.Bind(wx.EVT_TEXT, self.OnCambioProfundidad, id=wxID_PANEL1PROFUNDIDADENTERRADA)
        self.profundidadEnterrada.SetForegroundColour(wx.Colour(100, 200, 0))
        self.profundidadEnterrada.Show(False)
        self.profundidadUnidadesText = wx.StaticText(id=wxID_PANEL1PROFUNDIDADUNIDADESTEXT, label=_('m'), name='profundidadUnidadesText', parent=self, pos=wx.Point(212, 167), size=wx.Size(10, 13), style=0)
        self.profundidadUnidadesText.Show(False)
        self.aislamientoCheck = wx.CheckBox(id=wxID_PANEL1AISLAMIENTOCHECK, label=_('Tiene aislamiento térmico'), name='aislamientoCheck', parent=self, pos=wx.Point(15, 210), size=wx.Size(150, 13), style=0)
        self.aislamientoCheck.SetValue(False)
        self.aislamientoCheck.Bind(wx.EVT_CHECKBOX, self.OnAislamientoCheckCheckbox, id=wxID_PANEL1AISLAMIENTOCHECK)
        self.aislamientoCheck.Show(False)
        self.CaracteristicasAislamientoLineaText = wx.StaticBox(id=wxID_CARACTERISTICASAISLAMIENTOLINEATEXT, label=_('Características del aislamiento térmico'), name='LineaText', parent=self, pos=wx.Point(15, 235), size=wx.Size(680, 95), style=0)
        self.CaracteristicasAislamientoLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasAislamientoLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.CaracteristicasAislamientoLineaText.Show(False)
        self.aislanteRadioButton = wx.RadioButton(id=wxID_PANEL1AISLANTERADIOBUTTON, label=_('Tipo de aislamiento'), name='aislanteRadioButton', parent=self, pos=wx.Point(30, 258), size=wx.Size(120, 16), style=wx.RB_GROUP)
        self.aislanteRadioButton.SetValue(True)
        self.aislanteRadioButton.Show(False)
        self.aislanteRadioButton.Bind(wx.EVT_RADIOBUTTON, self.OnAislanteRadioButtonRadiobutton, id=wxID_PANEL1AISLANTERADIOBUTTON)
        self.RaislateRadio = wx.RadioButton(id=wxID_PANEL1RAISLATERADIO, label=_('Ra'), name='RaislateRadio', parent=self, pos=wx.Point(30, 288), size=wx.Size(81, 13), style=0)
        self.RaislateRadio.SetValue(False)
        self.RaislateRadio.Show(False)
        self.RaislateRadio.Bind(wx.EVT_RADIOBUTTON, self.OnAislanteRadioButtonRadiobutton, id=wxID_PANEL1RAISLATERADIO)
        self.tipoAislateChoice = MiChoice(choices=listadosWeb.listadoOpcionesAislamiento2, id=wxID_PANEL1TIPOAISLATECHOICE, name='tipoAislateChoice', parent=self, pos=wx.Point(151, 256), size=wx.Size(100, 21), style=0)
        self.tipoAislateChoice.Show(False)
        self.tipoAislateChoice.Bind(wx.EVT_CHOICE, self.onTipoAislateChoice, id=wxID_PANEL1TIPOAISLATECHOICE)
        self.espesorAislateText = wx.StaticText(id=wxID_PANEL1ESPESORAISLATETEXT, label=_('Espesor'), name='espesorAislateText', parent=self, pos=wx.Point(300, 258), size=wx.Size(41, 13), style=0)
        self.espesorAislateText.Show(False)
        self.espesorAislante = wx.TextCtrl(id=wxID_PANEL1ESPESORAISLANTE, name='espesorAislante', parent=self, pos=wx.Point(344, 256), size=wx.Size(56, 21), style=0, value='')
        self.espesorAislante.Show(False)
        self.espesorAislante.Bind(wx.EVT_TEXT, self.calcularCaracteristicasCerramiento, id=wxID_PANEL1ESPESORAISLANTE)
        self.UnidadesEspesorAislateText = wx.StaticText(id=wxID_PANEL1UNIDADESESPESORAISLATETEXT, label=_('m'), name='espesorAislateText', parent=self, pos=wx.Point(405, 258), size=wx.Size(10, 13), style=0)
        self.UnidadesEspesorAislateText.Show(False)
        self.landaAislateText = wx.StaticText(id=wxID_PANEL1LANDAAISLATETEXT, label=_('λ'), name='landaAislateText', parent=self, pos=wx.Point(474, 258), size=wx.Size(15, 13), style=0)
        self.landaAislateText.Show(False)
        self.landaAislante = wx.TextCtrl(id=wxID_PANEL1LANDAAISLANTE, name='landaAislante', parent=self, pos=wx.Point(496, 256), size=wx.Size(56, 21), style=0, value='')
        self.landaAislante.Bind(wx.EVT_TEXT, self.calcularCaracteristicasCerramiento, id=wxID_PANEL1LANDAAISLANTE)
        self.landaAislante.Show(False)
        self.landaUnidadesText = wx.StaticText(id=wxID_PANEL1LANDAUNIDADESTEXT, label=_('W/mK'), name='landaUnidadesText', parent=self, pos=wx.Point(557, 258), size=wx.Size(54, 13), style=0)
        self.landaUnidadesText.Show(False)
        self.Raislante = wx.TextCtrl(id=wxID_PANEL1RAISLANTE, name='Raislante', parent=self, pos=wx.Point(151, 286), size=wx.Size(56, 21), style=0, value='')
        self.Raislante.Show(False)
        self.Raislante.Enable(False)
        self.Raislante.Bind(wx.EVT_TEXT, self.calcularCaracteristicasCerramiento, id=wxID_PANEL1RAISLANTE)
        self.RaislanteUnidadesText = wx.StaticText(id=wxID_PANEL1RAISLANTEUNIDADESTEXT, label=_('m2K/W'), name='RaislanteUnidadesText', parent=self, pos=wx.Point(212, 288), size=wx.Size(34, 13), style=0)
        self.RaislanteUnidadesText.Show(False)
        self.nombreMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1NOMBREMURO)
        self.superficieMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1SUPERFICIEMURO)
        self.longitudMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1LONGIMURO)
        self.alturaMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1ALTURAMURO)
        self.multiMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1MULTIMURO)
        self.UFinalCuadro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1UFINALCUADRO)
        self.profundidadEnterrada.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1PROFUNDIDADENTERRADA)
        self.espesorAislante.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1ESPESORAISLANTE)
        self.landaAislante.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1LANDAAISLANTE)
        self.Raislante.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1RAISLANTE)
        self.subgrupoChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1SUBGRUPOCHOICE)
        self.valorUChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1VALORUCHOICE)
        self.tipoAislateChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1TIPOAISLATECHOICE)
        self.aislanteRadioButton.Bind(wx.EVT_KILL_FOCUS, self.manejadorRadio, id=wxID_PANEL1AISLANTERADIOBUTTON)
        self.RaislateRadio.Bind(wx.EVT_KILL_FOCUS, self.manejadorRadio, id=wxID_PANEL1RAISLATERADIO)
        self.aislamientoCheck.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1AISLAMIENTOCHECK)

    def actualizaDiccionario(self):
        self.diccionario = {}
        self.diccionario['panelFachadaConTerreno.nombreMuro'] = self.nombreMuro.GetValue()
        self.diccionario['panelFachadaConTerreno.superficieMuro'] = self.superficieMuro.GetValue()
        self.diccionario['panelFachadaConTerreno.longitudMuro'] = self.longitudMuro.GetValue()
        self.diccionario['panelFachadaConTerreno.alturaMuro'] = self.alturaMuro.GetValue()
        self.diccionario['panelFachadaConTerreno.multiMuro'] = self.multiMuro.GetValue()
        self.diccionario['panelFachadaConTerreno.UFinalCuadro'] = self.UFinalCuadro.GetValue()
        self.diccionario['panelFachadaConTerreno.profundidadEnterrada'] = self.profundidadEnterrada.GetValue()
        self.diccionario['panelFachadaConTerreno.espesorAislante'] = self.espesorAislante.GetValue()
        self.diccionario['panelFachadaConTerreno.landaAislante'] = self.landaAislante.GetValue()
        self.diccionario['panelFachadaConTerreno.Raislante'] = self.Raislante.GetValue()
        self.diccionario['panelFachadaConTerreno.subgrupoChoice'] = self.subgrupoChoice.GetSelection()
        self.diccionario['panelFachadaConTerreno.valorUChoice'] = self.valorUChoice.GetSelection()
        self.diccionario['panelFachadaConTerreno.tipoAislateChoice'] = self.tipoAislateChoice.GetSelection()
        self.diccionario['panelFachadaConTerreno.radios'] = self.GetRadioValues()
        self.diccionario['panelFachadaConTerreno.aislamientoCheck'] = self.aislamientoCheck.GetValue()

    def GetRadioValues(self):
        return [
         self.aislanteRadioButton.GetValue(),
         self.RaislateRadio.GetValue()]

    def SetRadioValues(self, lista):
        self.aislanteRadioButton.SetValue(lista[0])
        self.RaislateRadio.SetValue(lista[1])

    def cogeValoresDiccionario(self):
        self.nombreMuro.SetValue(self.diccionario['panelFachadaConTerreno.nombreMuro'])
        self.superficieMuro.SetValue(self.diccionario['panelFachadaConTerreno.superficieMuro'])
        self.longitudMuro.SetValue(self.diccionario['panelFachadaConTerreno.longitudMuro'])
        self.alturaMuro.SetValue(self.diccionario['panelFachadaConTerreno.alturaMuro'])
        self.multiMuro.SetValue(self.diccionario['panelFachadaConTerreno.multiMuro'])
        self.UFinalCuadro.SetValue(self.diccionario['panelFachadaConTerreno.UFinalCuadro'])
        self.profundidadEnterrada.SetValue(self.diccionario['panelFachadaConTerreno.profundidadEnterrada'])
        self.espesorAislante.SetValue(self.diccionario['panelFachadaConTerreno.espesorAislante'])
        self.landaAislante.SetValue(self.diccionario['panelFachadaConTerreno.landaAislante'])
        self.Raislante.SetValue(self.diccionario['panelFachadaConTerreno.Raislante'])
        self.subgrupoChoice.SetSelection(self.diccionario['panelFachadaConTerreno.subgrupoChoice'])
        self.valorUChoice.SetSelection(self.diccionario['panelFachadaConTerreno.valorUChoice'])
        self.tipoAislateChoice.SetSelection(self.diccionario['panelFachadaConTerreno.tipoAislateChoice'])
        self.aislamientoCheck.SetValue(self.diccionario['panelFachadaConTerreno.aislamientoCheck'])
        lista = self.GetRadioValues()
        self.SetRadioValues(lista)
        self.OnValorUChoiceChoice(None)
        self.OnAislamientoCheckCheckbox(None)
        self.OnAislanteRadioButtonRadiobutton(None)
        self.calcularCaracteristicasCerramiento(None)
        return

    def onTipoAislateChoice(self, event):
        """
        Metodo: onTipoAislateChoice

        ARGUMENTOS:
                event:
        """
        if self.tipoAislateChoice.GetStringSelection() == 'Otro':
            self.espesorAislante.Enable(True)
            self.landaAislateText.Show(True)
            self.landaAislante.Show(True)
            self.landaUnidadesText.Show(True)
        elif self.tipoAislateChoice.GetStringSelection() == 'Desconocido':
            self.espesorAislante.Enable(False)
            self.landaAislateText.Show(False)
            self.landaAislante.Show(False)
            self.landaUnidadesText.Show(False)
        else:
            self.espesorAislante.Enable(True)
            self.landaAislateText.Show(False)
            self.landaAislante.Show(False)
            self.landaUnidadesText.Show(False)
        self.calcularCaracteristicasCerramiento(None)
        return

    def cargarTransmitanciaTermicaGlobal(self):
        """
        Metodo: cargarTransmitanciaTermicaGlobal

        """
        self.UFinalCuadro.SetValue(str(self.UCerramiento))

    def calcularCaracteristicasCerramiento(self, event):
        """
        Metodo: calcularCaracteristicasCerramiento

        ARGUMENTOS:
                event:
        """
        if self.bolCalcularCaracteristicas == True:
            try:
                if 'Por defecto' in self.valorUChoice.GetStringSelection():
                    valoresCerr = tablasValores.tablasValores('Fachada', 'terreno', [
                     self.parent.parent.parent.panelDatosGenerales.anoConstruccionChoice.GetSelection(),
                     self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()], 'Por defecto')
                    self.UCerramiento = valoresCerr.UCerramiento
                    self.densidadCerramiento = valoresCerr.densidadCerramiento
                elif 'Estimad' in self.valorUChoice.GetStringSelection():
                    datosAislamiento = []
                    tieneAislamiento = self.aislamientoCheck.GetValue()
                    if self.RaislateRadio.GetValue() == True:
                        datosAislamiento = [
                         self.Raislante.GetValue()]
                    else:
                        tipoAislante = self.tipoAislateChoice.GetStringSelection()
                        espesorAislante = self.espesorAislante.GetValue()
                        landaAislante = self.landaAislante.GetValue()
                        datosAislamiento = [tipoAislante, espesorAislante, landaAislante]
                    valoresCerr = tablasValores.tablasValores('Fachada', 'terreno', [
                     tieneAislamiento, datosAislamiento], 'Estimado')
                    U = valoresCerr.UCerramiento
                    Rm = 1.0 / float(U)
                    self.UCerramiento = apendiceE.murosEnContactoConElTerreno(Rm, float(self.profundidadEnterrada.GetValue()))
                    self.densidadCerramiento = valoresCerr.densidadCerramiento
                self.UCerramiento = round(self.UCerramiento, 2)
                self.cargarTransmitanciaTermicaGlobal()
            except:
                logging.info('Excepcion en: %s' % __name__)
                self.UCerramiento = ''
                self.densidadCerramiento = ''
                self.cargarTransmitanciaTermicaGlobal()

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
        self.UCerramiento = ''
        self.densidadCerramiento = ''
        self.bolCalcularCaracteristicas = True
        self.calcularCaracteristicasCerramiento(None)
        self.actualizaDiccionario()
        return

    def elegirRaiz(self):
        """
        Metodo: elegirRaiz

        """
        try:
            sel = self.parent.arbolCerramientos.GetSelection()
            self.subgrupoChoice.SetStringSelection('Edificio Objeto')
            raiz = self.parent.arbolCerramientos.GetRootItem()
            while sel != raiz:
                for i in range(len(self.parent.parent.subgrupos)):
                    if self.parent.arbolCerramientos.GetItemText(sel) == self.parent.parent.subgrupos[i].nombre:
                        self.subgrupoChoice.SetStringSelection(self.parent.arbolCerramientos.GetItemText(sel))
                        return

                sel = self.parent.arbolCerramientos.GetItemParent(sel)

        except:
            logging.info('Excepcion en: %s' % __name__)
            self.subgrupoChoice.SetStringSelection('Edificio Objeto')

    def cargarRaices(self):
        """
        Metodo: cargarRaices

        """
        raices = []
        raices.append(('Edificio Objeto', _('Edificio Objeto')))
        for i in range(len(self.parent.parent.subgrupos)):
            if self.parent.parent.subgrupos[i].nombre != 'Edificio Objeto':
                raices.append((self.parent.parent.subgrupos[i].nombre, self.parent.parent.subgrupos[i].nombre))

        return raices

    def OnCambioProfundidad(self, event):
        """
        Metodo: OnCambioProfundidad

        ARGUMENTOS:
                event:
        """
        self.profundidadEnterrada.SetForegroundColour(wx.Colour(0, 0, 0))
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

    def OnAislamientoCheckCheckbox(self, event):
        """
        Metodo: OnAislamientoCheckCheckbox

        ARGUMENTOS:
                event:
        """
        if self.aislamientoCheck.GetValue() == True:
            self.Raislante.Show(True)
            self.espesorAislante.Show(True)
            self.UnidadesEspesorAislateText.Show(True)
            self.espesorAislateText.Show(True)
            self.tipoAislateChoice.Show(True)
            self.RaislateRadio.Show(True)
            self.aislanteRadioButton.Show(True)
            self.RaislanteUnidadesText.Show(True)
            self.onTipoAislateChoice(None)
            self.CaracteristicasAislamientoLineaText.Show(True)
        else:
            self.Raislante.Show(False)
            self.espesorAislante.Show(False)
            self.UnidadesEspesorAislateText.Show(False)
            self.espesorAislateText.Show(False)
            self.tipoAislateChoice.Show(False)
            self.RaislateRadio.Show(False)
            self.aislanteRadioButton.Show(False)
            self.RaislanteUnidadesText.Show(False)
            self.landaAislateText.Show(False)
            self.landaAislante.Show(False)
            self.landaUnidadesText.Show(False)
            self.CaracteristicasAislamientoLineaText.Show(False)
        self.calcularCaracteristicasCerramiento(None)
        return

    def OnValorUChoiceChoice(self, event):
        """
        Metodo: OnValorUChoiceChoice

        ARGUMENTOS:
                event:
        """
        if 'Estimad' in self.valorUChoice.GetStringSelection():
            self.profundidadText.Show(True)
            self.aislamientoCheck.Show(True)
            self.profundidadEnterrada.Show(True)
            self.profundidadUnidadesText.Show(True)
            self.OnAislamientoCheckCheckbox(None)
        else:
            self.CaracteristicasAislamientoLineaText.Show(False)
            self.espesorAislateText.Show(False)
            self.espesorAislante.Show(False)
            self.UnidadesEspesorAislateText.Show(False)
            self.landaAislateText.Show(False)
            self.landaAislante.Show(False)
            self.landaUnidadesText.Show(False)
            self.Raislante.Show(False)
            self.RaislanteUnidadesText.Show(False)
            self.RaislateRadio.Show(False)
            self.aislanteRadioButton.Show(False)
            self.profundidadText.Show(False)
            self.aislamientoCheck.Show(False)
            self.profundidadEnterrada.Show(False)
            self.profundidadUnidadesText.Show(False)
            self.tipoAislateChoice.Show(False)
        self.calcularCaracteristicasCerramiento(None)
        return

    def OnAislanteRadioButtonRadiobutton(self, event):
        """
        Metodo: OnAislanteRadioButtonRadiobutton

        ARGUMENTOS:
                event:
        """
        if self.aislanteRadioButton.GetValue() == True:
            self.espesorAislante.Enable(True)
            self.espesorAislateText.Enable(True)
            self.UnidadesEspesorAislateText.Enable(True)
            self.landaAislante.Enable(True)
            self.tipoAislateChoice.Enable(True)
            self.Raislante.Enable(False)
        else:
            self.espesorAislante.Enable(False)
            self.landaAislante.Enable(False)
            self.tipoAislateChoice.Enable(False)
            self.Raislante.Enable(True)
        self.calcularCaracteristicasCerramiento(None)
        return

    def comprobarDatos(self):
        """
        Metodo: comprobarDatos

                self):
        """
        listaErrores = ''
        dato = self.superficieMuro.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.superficieMuro.SetValue(dato)
        dato = self.profundidadEnterrada.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.profundidadEnterrada.SetValue(dato)
        dato = self.espesorAislante.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.espesorAislante.SetValue(dato)
        dato = self.landaAislante.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.landaAislante.SetValue(dato)
        dato = self.Raislante.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.Raislante.SetValue(dato)
        listaErrores += Comprueba(self.nombreMuro.GetValue(), 1, listaErrores, _('nombre')).ErrorDevuelto
        listaErrores += Comprueba(self.subgrupoChoice.GetStringSelection(), 0, listaErrores, _('zona')).ErrorDevuelto
        listaErrores += Comprueba(self.superficieMuro.GetValue(), 2, listaErrores, _('superficie'), 0).ErrorDevuelto
        if self.valorUChoice.GetStringSelection() == 'Estimadas':
            listaErrores += Comprueba(self.profundidadEnterrada.GetValue(), 2, listaErrores, _('espesor de la capa de protección de tierra'), 0).ErrorDevuelto
            if self.aislamientoCheck.GetValue() == True:
                if self.aislanteRadioButton.GetValue() == True:
                    listaErrores += Comprueba(self.tipoAislateChoice.GetStringSelection(), 0, listaErrores, _('tipo de aislamiento')).ErrorDevuelto
                    listaErrores += Comprueba(self.espesorAislante.GetValue(), 2, listaErrores, _('espesor'), 0).ErrorDevuelto
                    if self.tipoAislateChoice.GetStringSelection() == 'Otro':
                        listaErrores += Comprueba(self.landaAislante.GetValue(), 2, listaErrores, _('λ del aislamiento'), 0).ErrorDevuelto
                else:
                    listaErrores += Comprueba(self.Raislante.GetValue(), 2, listaErrores, _('Ra'), 0).ErrorDevuelto
        elif self.valorUChoice.GetStringSelection() == 'Por defecto':
            pass
        return listaErrores

    def cogerDatos(self):
        """
        Metodo: cogerDatos

        """
        listaErrores = self.comprobarDatos()
        if listaErrores != '':
            return listaErrores
        datos = []
        datos.append(self.nombreMuro.GetValue())
        datos.append('Fachada')
        datos.append(self.superficieMuro.GetValue())
        datos.append(self.UCerramiento)
        datos.append(self.densidadCerramiento)
        datos.append('')
        datos.append('')
        datos.append('Sin patrón')
        datos.append(self.valorUChoice.GetStringSelection())
        datosConcretos = []
        if 'Estimad' in self.valorUChoice.GetStringSelection():
            datosConcretos.append(self.aislamientoCheck.GetValue())
            datosConcretos.append(self.profundidadEnterrada.GetValue())
            datosConcretos.append(self.aislanteRadioButton.GetValue())
            datosConcretos.append(self.tipoAislateChoice.GetStringSelection())
            datosConcretos.append(self.espesorAislante.GetValue())
            datosConcretos.append(self.landaAislante.GetValue())
            datosConcretos.append(self.Raislante.GetValue())
        datos.append(datosConcretos)
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
        self.bolCalcularCaracteristicas = False
        self.nombreMuro.SetValue(datos[0])
        self.superficieMuro.SetValue(datos[2])
        self.valorUChoice.SetStringSelection(datos[8])
        self.OnValorUChoiceChoice(None)
        if 'Estimad' in datos[8]:
            self.aislamientoCheck.SetValue(datos[9][0])
            self.profundidadEnterrada.SetValue(datos[9][1])
            self.aislanteRadioButton.SetValue(datos[9][2])
            self.RaislateRadio.SetValue(not datos[9][2])
            self.tipoAislateChoice.SetStringSelection(datos[9][3])
            self.espesorAislante.SetValue(datos[9][4])
            self.landaAislante.SetValue(datos[9][5])
            self.Raislante.SetValue(datos[9][6])
        self.longitudMuro.SetValue(datos[10])
        self.alturaMuro.SetValue(datos[11])
        self.multiMuro.SetValue(datos[12])
        self.subgrupoChoice.SetStringSelection(datos[13])
        self.OnAislamientoCheckCheckbox(None)
        self.OnAislanteRadioButtonRadiobutton(None)
        self.parent.panelElegirObjeto.definirFachada.SetValue(True)
        self.parent.panelElegirObjeto.mostrarOpcionesContacto()
        self.parent.panelElegirObjeto.contactoSuelo.SetValue(True)
        colorSombra = wx.Color(240, 240, 240)
        colorNormal = wx.Color(255, 255, 255)
        self.parent.panelElegirObjeto.definirSuelo.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirCubierta.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirFachada.SetBackgroundColour(colorSombra)
        self.parent.panelElegirObjeto.definirParticionInterior.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirHueco.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirPuenteTermico.SetBackgroundColour(colorNormal)
        self.profundidadEnterrada.SetForegroundColour(wx.Colour(0, 0, 0))
        self.bolCalcularCaracteristicas = True
        self.calcularCaracteristicasCerramiento(None)
        self.actualizaDiccionario()
        return