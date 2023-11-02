# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\panelCubiertaConTerreno.pyc
# Compiled at: 2015-02-23 10:41:14
"""
Modulo: panelCubiertaConTerreno.py

"""
from Envolvente.comprobarCampos import Comprueba
from miChoice import MiChoice
import Envolvente.apendiceE as apendiceE, Envolvente.tablasValores as tablasValores, directorios, Calculos.listadosWeb as listadosWeb, LibreriasCE3X.menuCerramientos as menuCerramientos, nuevoUndo, wx, logging
Directorio = directorios.BuscaDirectorios().Directorio
wxID_PANEL1, wxID_PANEL1AISLAMIENTOCHECK, wxID_PANEL1AISLANTERADIOBUTTON, wxID_PANEL1CERRAMIENTOSCHOICE, wxID_PANEL1ESPESORAISLANTE, wxID_PANEL1ESPESORAISLATETEXT, wxID_PANEL1LIBRERIARADIOBUTTON, wxID_PANEL1NOMBREMURO, wxID_PANEL1NOMBREMUROTEXT, wxID_PANEL1PROFUNDIDADENTERRADA, wxID_PANEL1PROFUNDIDADTEXT, wxID_PANEL1PROFUNDIDADUNIDADESTEXT, wxID_PANEL1RAISLANTE, wxID_PANEL1RAISLANTEUNIDADESTEXT, wxID_PANEL1RAISLATERADIO, wxID_PANEL1SUPERFICIEMURO, wxID_PANEL1SUPERFICIETEXT, wxID_PANEL1SUPERFICIEUNIDADESTEXT, wxID_PANEL1TIPOAISLATECHOICE, wxID_PANEL1URADIOBUTTON, wxID_PANEL1VALORU, wxID_PANEL1VALORUCHOICE, wxID_PANEL1VALORUTEXT, wxID_PANEL1LONGIMUROTEXT, wxID_PANEL1ALTURAMUROTEXT, wxID_PANEL1MULTIMUROTEXT, wxID_PANEL1LONGIMURO, wxID_PANEL1LONGITUDUNIDADESTEXT, wxID_PANEL1ALTURAMURO, wxID_PANEL1ALTURAUNIDADESTEXT, wxID_PANEL1MULTIMURO, wxID_PANEL1SUBGRUPOTEXT, wxID_PANEL1SUBGRUPOCHOICE, wxID_PANEL1UNIDADESUTEXT, wxID_PANEL1UNIDADESESPESORAISLATETEXT, wxID_PANEL1UFINALTEXT, wxID_PANEL1UFINALCUADRO, wxID_PANEL1UNIDADESUFINAL, wxID_PANEL1INERCIATEXT, wxID_PANEL1UNIDADESINERCIATEXT, wxID_PANEL1INERCIACHOICE, wxID_PANEL1LANDAUNIDADESTEXT, wxID_PANEL1LANDAAISLANTE, wxID_PANEL1LANDAAISLATETEXT, wxID_PANEL1LIBRERIABOTON, wxID_DIMENSIONESLINEATEXT, wxID_CARACTERISTICASAISLAMIENTOLINEATEXT, wxID_PANEL1AISLAMIENTOCHECK = [ wx.NewId() for _init_ctrls in range(48) ]

class Panel1(wx.Panel, nuevoUndo.VistaUndo):
    """
    Clase: Panel1 del modulo panelCubiertaConTerreno.py

    """

    def OnNombreMuro(self, event):
        """
        Metodo: OnNombreMuro

        ARGUMENTOS:
                event:
        """
        if self.nombreMuro.GetValue() == _('Cubierta con terreno'):
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
        wx.Panel.__init__(self, id=ide, name='panelCubiertaConTerreno', parent=prnt, pos=posi, size=siz, style=styl)
        self.SetBackgroundColour('white')
        self.nombreMuroText = wx.StaticText(id=wxID_PANEL1NOMBREMUROTEXT, label=_('Nombre'), name='nombreMuroText', parent=self, pos=wx.Point(15, 2), size=wx.Size(102, 13), style=0)
        self.nombreMuro = wx.TextCtrl(id=wxID_PANEL1NOMBREMURO, name='nombreMuro', parent=self, pos=wx.Point(151, 0), size=wx.Size(210, 21), style=0, value=_('Cubierta con terreno'))
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
        self.alturaMuroText = wx.StaticText(id=wxID_PANEL1ALTURAMUROTEXT, label=_('Anchura'), name='alturaMuroText', parent=self, pos=wx.Point(151, 85), size=wx.Size(28, 13), style=0)
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
        self.valorUChoice = MiChoice(choices=listadosWeb.listadoOpcionesU, id=wxID_PANEL1VALORUCHOICE, name='valorUChoice', parent=self, pos=wx.Point(151, 128), size=wx.Size(200, 21), style=0)
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
        self.UradioButton = wx.RadioButton(id=wxID_PANEL1URADIOBUTTON, label=_('Transmitancia térmica'), name='UradioButton', parent=self, pos=wx.Point(15, 167), size=wx.Size(122, 13), style=wx.RB_GROUP)
        self.UradioButton.SetValue(True)
        self.UradioButton.Show(False)
        self.UradioButton.SetToolTipString('UradioButton')
        self.UradioButton.Bind(wx.EVT_RADIOBUTTON, self.OnUradioButtonRadiobutton, id=wxID_PANEL1URADIOBUTTON)
        self.UnidadesU = wx.StaticText(id=wxID_PANEL1UNIDADESUTEXT, label=_('W/m2K'), name='UnidadesU', parent=self, pos=wx.Point(212, 167), size=wx.Size(99, 13), style=0)
        self.UnidadesU.Show(False)
        self.libreriaRadioButton = wx.RadioButton(id=wxID_PANEL1LIBRERIARADIOBUTTON, label=_('Librería cerramientos'), name='libreriaRadioButton', parent=self, pos=wx.Point(15, 197), size=wx.Size(122, 13), style=0)
        self.libreriaRadioButton.SetValue(False)
        self.libreriaRadioButton.Show(False)
        self.libreriaRadioButton.Bind(wx.EVT_RADIOBUTTON, self.OnUradioButtonRadiobutton, id=wxID_PANEL1LIBRERIARADIOBUTTON)
        self.valorU = wx.TextCtrl(id=wxID_PANEL1VALORU, name='valorU', parent=self, pos=wx.Point(151, 165), size=wx.Size(56, 21), style=0, value='')
        self.valorU.Show(False)
        self.valorU.Bind(wx.EVT_TEXT, self.calcularCaracteristicasCerramiento, id=wxID_PANEL1VALORU)
        self.inerciaText = wx.StaticText(id=wxID_PANEL1INERCIATEXT, label=_('Masa/m2'), name='inerciaText', parent=self, pos=wx.Point(290, 167), size=wx.Size(50, 13), style=0)
        self.inerciaText.Show(False)
        self.unidadesInerciaText = wx.StaticText(id=wxID_PANEL1UNIDADESINERCIATEXT, label=_('kg/m2'), name='inerciaText', parent=self, pos=wx.Point(405, 167), size=wx.Size(30, 13), style=0)
        self.unidadesInerciaText.Show(False)
        self.inercia = wx.TextCtrl(id=wxID_PANEL1INERCIACHOICE, name='inercia', parent=self, pos=wx.Point(344, 165), size=wx.Size(56, 21), style=0, value='')
        self.inercia.Bind(wx.EVT_TEXT, self.calcularCaracteristicasCerramiento, id=wxID_PANEL1INERCIACHOICE)
        self.inercia.Show(False)
        self.cerramientosChoice = wx.Choice(choices=self.parent.parent.parent.listadoCerramientos, id=wxID_PANEL1CERRAMIENTOSCHOICE, name='cerramientosChoice', parent=self, pos=wx.Point(151, 195), size=wx.Size(249, 21), style=0)
        self.cerramientosChoice.Bind(wx.EVT_CHOICE, self.calcularCaracteristicasCerramiento, id=wxID_PANEL1CERRAMIENTOSCHOICE)
        self.cerramientosChoice.Show(False)
        self.cerramientosChoice.Enable(False)
        self.cerramientosChoice.SetSelection(-1)
        self.libreriaBoton = wx.BitmapButton(id=wxID_PANEL1LIBRERIABOTON, bitmap=wx.Bitmap(Directorio + '/Imagenes/cerramientos.ico', wx.BITMAP_TYPE_ANY), parent=self, pos=wx.Point(404, 195), size=wx.Size(23, 21), style=wx.BU_AUTODRAW)
        self.libreriaBoton.Bind(wx.EVT_BUTTON, self.OnLibreriaBotonButton, id=wxID_PANEL1LIBRERIABOTON)
        self.libreriaBoton.Show(False)
        self.libreriaBoton.Enable(False)
        self.profundidadText = wx.StaticText(id=wxID_PANEL1PROFUNDIDADTEXT, label=_('Espesor de la capa de protección de tierra'), name='profundidadText', parent=self, pos=wx.Point(15, 165), size=wx.Size(120, 25), style=0)
        self.profundidadText.Show(False)
        self.profundidadEnterrada = wx.TextCtrl(id=wxID_PANEL1PROFUNDIDADENTERRADA, name='profundidadEnterrada', parent=self, pos=wx.Point(151, 162), size=wx.Size(56, 21), style=0, value='0.5')
        self.profundidadEnterrada.Bind(wx.EVT_TEXT, self.OnCambioProfundidad, id=wxID_PANEL1PROFUNDIDADENTERRADA)
        self.profundidadEnterrada.Show(False)
        self.profundidadEnterrada.SetForegroundColour(wx.Colour(100, 200, 0))
        self.profundidadEnterrada.Show(False)
        self.profundidadUnidadesText = wx.StaticText(id=wxID_PANEL1PROFUNDIDADUNIDADESTEXT, label=_('m'), name='profundidadUnidadesText', parent=self, pos=wx.Point(212, 167), size=wx.Size(34, 13), style=0)
        self.profundidadUnidadesText.Show(False)
        self.aislamientoCheck = wx.CheckBox(id=wxID_PANEL1AISLAMIENTOCHECK, label=_('Tiene aislamiento térmico'), name='aislamientoCheck', parent=self, pos=wx.Point(15, 210), size=wx.Size(150, 13), style=0)
        self.aislamientoCheck.SetValue(False)
        self.aislamientoCheck.Show(False)
        self.aislamientoCheck.Bind(wx.EVT_CHECKBOX, self.OnAislamientoCheckCheckbox, id=wxID_PANEL1AISLAMIENTOCHECK)
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
        self.landaUnidadesText = wx.StaticText(id=wxID_PANEL1LANDAUNIDADESTEXT, label=_('m'), name='landaUnidadesText', parent=self, pos=wx.Point(557, 258), size=wx.Size(54, 13), style=0)
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
        self.valorU.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1VALORU)
        self.inercia.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1INERCIACHOICE)
        self.profundidadEnterrada.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1PROFUNDIDADENTERRADA)
        self.espesorAislante.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1ESPESORAISLANTE)
        self.landaAislante.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1LANDAAISLANTE)
        self.Raislante.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1RAISLANTE)
        self.subgrupoChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1SUBGRUPOCHOICE)
        self.valorUChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1VALORUCHOICE)
        self.cerramientosChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1CERRAMIENTOSCHOICE)
        self.tipoAislateChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1TIPOAISLATECHOICE)
        self.UradioButton.Bind(wx.EVT_KILL_FOCUS, self.manejadorRadio, id=wxID_PANEL1URADIOBUTTON)
        self.libreriaRadioButton.Bind(wx.EVT_KILL_FOCUS, self.manejadorRadio, id=wxID_PANEL1LIBRERIARADIOBUTTON)
        self.aislanteRadioButton.Bind(wx.EVT_KILL_FOCUS, self.manejadorRadio, id=wxID_PANEL1AISLANTERADIOBUTTON)
        self.RaislateRadio.Bind(wx.EVT_KILL_FOCUS, self.manejadorRadio, id=wxID_PANEL1RAISLATERADIO)
        self.aislamientoCheck.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1AISLAMIENTOCHECK)

    def actualizaDiccionario(self):
        self.diccionario = {}
        self.diccionario['panelCubiertaConTerreno.nombreMuro'] = self.nombreMuro.GetValue()
        self.diccionario['panelCubiertaConTerreno.superficieMuro'] = self.superficieMuro.GetValue()
        self.diccionario['panelCubiertaConTerreno.longitudMuro'] = self.longitudMuro.GetValue()
        self.diccionario['panelCubiertaConTerreno.alturaMuro'] = self.alturaMuro.GetValue()
        self.diccionario['panelCubiertaConTerreno.multiMuro'] = self.multiMuro.GetValue()
        self.diccionario['panelCubiertaConTerreno.UFinalCuadro'] = self.UFinalCuadro.GetValue()
        self.diccionario['panelCubiertaConTerreno.valorU'] = self.valorU.GetValue()
        self.diccionario['panelCubiertaConTerreno.inercia'] = self.inercia.GetValue()
        self.diccionario['panelCubiertaConTerreno.profundidadEnterrada'] = self.profundidadEnterrada.GetValue()
        self.diccionario['panelCubiertaConTerreno.espesorAislante'] = self.espesorAislante.GetValue()
        self.diccionario['panelCubiertaConTerreno.landaAislante'] = self.landaAislante.GetValue()
        self.diccionario['panelCubiertaConTerreno.Raislante'] = self.Raislante.GetValue()
        self.diccionario['panelCubiertaConTerreno.subgrupoChoice'] = self.subgrupoChoice.GetSelection()
        self.diccionario['panelCubiertaConTerreno.valorUChoice'] = self.valorUChoice.GetSelection()
        self.diccionario['panelCubiertaConTerreno.cerramientosChoice'] = self.cerramientosChoice.GetSelection()
        self.diccionario['panelCubiertaConTerreno.tipoAislateChoice'] = self.tipoAislateChoice.GetSelection()
        self.diccionario['panelCubiertaConTerreno.radios'] = self.GetRadioValues()
        self.diccionario['panelCubiertaConTerreno.aislamientoCheck'] = self.aislamientoCheck.GetValue()

    def GetRadioValues(self):
        return [
         self.UradioButton.GetValue(),
         self.libreriaRadioButton.GetValue(),
         self.aislanteRadioButton.GetValue(),
         self.RaislateRadio.GetValue()]

    def SetRadioValues(self, lista):
        self.UradioButton.SetValue(lista[0])
        self.libreriaRadioButton.SetValue(lista[1])
        self.aislanteRadioButton.SetValue(lista[2])
        self.RaislateRadio.SetValue(lista[3])

    def cogeValoresDiccionario(self):
        self.nombreMuro.SetValue(self.diccionario['panelCubiertaConTerreno.nombreMuro'])
        self.superficieMuro.SetValue(self.diccionario['panelCubiertaConTerreno.superficieMuro'])
        self.longitudMuro.SetValue(self.diccionario['panelCubiertaConTerreno.longitudMuro'])
        self.alturaMuro.SetValue(self.diccionario['panelCubiertaConTerreno.alturaMuro'])
        self.multiMuro.SetValue(self.diccionario['panelCubiertaConTerreno.multiMuro'])
        self.UFinalCuadro.SetValue(self.diccionario['panelCubiertaConTerreno.UFinalCuadro'])
        self.valorU.SetValue(self.diccionario['panelCubiertaConTerreno.valorU'])
        self.inercia.SetValue(self.diccionario['panelCubiertaConTerreno.inercia'])
        self.profundidadEnterrada.SetValue(self.diccionario['panelCubiertaConTerreno.profundidadEnterrada'])
        self.espesorAislante.SetValue(self.diccionario['panelCubiertaConTerreno.espesorAislante'])
        self.landaAislante.SetValue(self.diccionario['panelCubiertaConTerreno.landaAislante'])
        self.Raislante.SetValue(self.diccionario['panelCubiertaConTerreno.Raislante'])
        self.subgrupoChoice.SetSelection(self.diccionario['panelCubiertaConTerreno.subgrupoChoice'])
        self.valorUChoice.SetSelection(self.diccionario['panelCubiertaConTerreno.valorUChoice'])
        self.cerramientosChoice.SetSelection(self.diccionario['panelCubiertaConTerreno.cerramientosChoice'])
        self.tipoAislateChoice.SetSelection(self.diccionario['panelCubiertaConTerreno.tipoAislateChoice'])
        self.aislamientoCheck.SetValue(self.diccionario['panelCubiertaConTerreno.aislamientoCheck'])
        lista = self.GetRadioValues()
        self.SetRadioValues(lista)
        self.OnAislamientoCheckCheckbox(None)
        self.OnValorUChoiceChoice(None)
        self.OnAislanteRadioButtonRadiobutton(None)
        self.calcularCaracteristicasCerramiento(None)
        return

    def OnLibreriaBotonButton(self, event):
        """
        Metodo: OnLibreriaBotonButton

        ARGUMENTOS:
                event:
        """
        self.dlg = menuCerramientos.create(self.parent.parent.parent)
        self.dlg.ShowModal()
        self.parent.parent.parent.listadoCerramientos = []
        for i in self.parent.parent.parent.listadoComposicionesCerramientos:
            self.parent.parent.parent.listadoCerramientos.append(i.nombre)

        self.cerramientosChoice.SetItems(self.parent.parent.parent.listadoCerramientos)
        self.dlg.Destroy()

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
                    valoresCerr = tablasValores.tablasValores('Cubierta', 'terreno', [
                     self.parent.parent.parent.panelDatosGenerales.anoConstruccionChoice.GetSelection(),
                     self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()], 'Por defecto')
                    self.UCerramiento = valoresCerr.UCerramiento
                    self.densidadCerramiento = valoresCerr.densidadCerramiento
                elif 'Estimad' in self.valorUChoice.GetStringSelection():
                    datosAislamiento = []
                    if self.aislamientoCheck.GetValue() == True:
                        if self.RaislateRadio.GetValue() == True:
                            datosAislamiento = [
                             self.Raislante.GetValue()]
                        else:
                            tipoAislante = self.tipoAislateChoice.GetStringSelection()
                            espesorAislante = self.espesorAislante.GetValue()
                            landaAislante = self.landaAislante.GetValue()
                            datosAislamiento = [tipoAislante, espesorAislante, landaAislante]
                        valoresCerr = tablasValores.tablasValores('Cubierta', 'terreno', [
                         datosAislamiento], 'Estimado')
                        U = valoresCerr.UCerramiento
                        self.UCerramiento = apendiceE.cubiertaTerreno(U, self.profundidadEnterrada.GetValue())
                        self.densidadCerramiento = valoresCerr.densidadCerramiento + 1800 * float(self.profundidadEnterrada.GetValue())
                    else:
                        valoresCerr = tablasValores.tablasValores('Cubierta', 'terreno', [
                         [
                          'SinAislamiento']], 'Estimado')
                        U = valoresCerr.UCerramiento
                        self.UCerramiento = apendiceE.cubiertaTerreno(U, self.profundidadEnterrada.GetValue())
                        self.densidadCerramiento = valoresCerr.densidadCerramiento + 1800 * float(self.profundidadEnterrada.GetValue())
                elif self.UradioButton.GetValue() == True:
                    self.UCerramiento = float(self.valorU.GetValue())
                    self.densidadCerramiento = float(self.inercia.GetValue())
                else:
                    for i in self.parent.parent.parent.listadoComposicionesCerramientos:
                        if i.nombre == self.cerramientosChoice.GetStringSelection().encode('iso-8859-15'):
                            U = float(i.transmitancia)
                            pesoTerreno = 1800.0 * float(self.profundidadEnterrada.GetValue())
                            pesoCerramiento = i.peso
                            self.densidadCerramiento = round(pesoTerreno + pesoCerramiento, 2)
                            break

                    self.UCerramiento = apendiceE.cubiertaTerreno(U, self.profundidadEnterrada.GetValue())
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

    def OnValorUChoiceChoice(self, event):
        """
        Metodo: OnValorUChoiceChoice

        ARGUMENTOS:
                event:
        """
        if 'Conocid' in self.valorUChoice.GetStringSelection():
            self.cerramientosChoice.Show(True)
            self.libreriaBoton.Show(True)
            self.valorU.Show(True)
            self.libreriaRadioButton.Show(True)
            self.UradioButton.Show(True)
            self.UnidadesU.Show(True)
            self.inercia.Show(True)
            self.unidadesInerciaText.Show(True)
            self.inerciaText.Show(True)
            self.CaracteristicasAislamientoLineaText.Show(False)
            self.Raislante.Show(False)
            self.espesorAislante.Show(False)
            self.UnidadesEspesorAislateText.Show(False)
            self.espesorAislateText.Show(False)
            self.tipoAislateChoice.Show(False)
            self.RaislateRadio.Show(False)
            self.aislanteRadioButton.Show(False)
            self.RaislanteUnidadesText.Show(False)
            self.landaAislante.Show(False)
            self.landaAislateText.Show(False)
            self.landaUnidadesText.Show(False)
            self.aislamientoCheck.Show(False)
            self.profundidadText.SetPosition(wx.Point(30, 219))
            self.profundidadEnterrada.SetPosition(wx.Point(151, 220))
            self.profundidadUnidadesText.SetPosition(wx.Point(212, 222))
            self.OnUradioButtonRadiobutton(None)
        elif 'Estimad' in self.valorUChoice.GetStringSelection():
            self.cerramientosChoice.Show(False)
            self.libreriaBoton.Show(False)
            self.valorU.Show(False)
            self.libreriaRadioButton.Show(False)
            self.UradioButton.Show(False)
            self.UnidadesU.Show(False)
            self.inercia.Show(False)
            self.unidadesInerciaText.Show(False)
            self.inerciaText.Show(False)
            self.aislamientoCheck.Show(True)
            self.Raislante.Show(True)
            self.espesorAislante.Show(True)
            self.UnidadesEspesorAislateText.Show(True)
            self.espesorAislateText.Show(True)
            self.tipoAislateChoice.Show(True)
            self.RaislateRadio.Show(True)
            self.aislanteRadioButton.Show(True)
            self.RaislanteUnidadesText.Show(True)
            self.landaAislante.Show(True)
            self.landaAislateText.Show(True)
            self.landaUnidadesText.Show(True)
            self.OnAislamientoCheckCheckbox(None)
            self.profundidadText.SetPosition(wx.Point(15, 162))
            self.profundidadEnterrada.SetPosition(wx.Point(151, 165))
            self.profundidadUnidadesText.SetPosition(wx.Point(212, 167))
            self.profundidadEnterrada.Show(True)
            self.profundidadText.Show(True)
            self.profundidadUnidadesText.Show(True)
        else:
            self.cerramientosChoice.Show(False)
            self.libreriaBoton.Show(False)
            self.valorU.Show(False)
            self.libreriaRadioButton.Show(False)
            self.UradioButton.Show(False)
            self.UnidadesU.Show(False)
            self.inercia.Show(False)
            self.unidadesInerciaText.Show(False)
            self.inerciaText.Show(False)
            self.CaracteristicasAislamientoLineaText.Show(False)
            self.Raislante.Show(False)
            self.espesorAislante.Show(False)
            self.UnidadesEspesorAislateText.Show(False)
            self.espesorAislateText.Show(False)
            self.tipoAislateChoice.Show(False)
            self.RaislateRadio.Show(False)
            self.aislanteRadioButton.Show(False)
            self.RaislanteUnidadesText.Show(False)
            self.landaAislante.Show(False)
            self.landaAislateText.Show(False)
            self.landaUnidadesText.Show(False)
            self.aislamientoCheck.Show(False)
            self.profundidadEnterrada.Show(False)
            self.profundidadText.Show(False)
            self.profundidadUnidadesText.Show(False)
        self.calcularCaracteristicasCerramiento(None)
        return

    def OnUradioButtonRadiobutton(self, event):
        """
        Metodo: OnUradioButtonRadiobutton

        ARGUMENTOS:
                event:
        """
        if self.UradioButton.GetValue() == True:
            self.cerramientosChoice.Enable(False)
            self.libreriaBoton.Enable(False)
            self.valorU.Enable(True)
            self.inercia.Enable(True)
            self.profundidadText.Show(False)
            self.profundidadEnterrada.Show(False)
            self.profundidadUnidadesText.Show(False)
        else:
            self.cerramientosChoice.Enable(True)
            self.libreriaBoton.Enable(True)
            self.valorU.Enable(False)
            self.inercia.Enable(False)
            self.profundidadText.Show(True)
            self.profundidadEnterrada.Show(True)
            self.profundidadUnidadesText.Show(True)
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
        dato = self.valorU.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.valorU.SetValue(dato)
        dato = self.inercia.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.inercia.SetValue(dato)
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
        if self.valorUChoice.GetStringSelection() == 'Conocidas':
            if self.UradioButton.GetValue() == True:
                listaErrores += Comprueba(self.valorU.GetValue(), 2, listaErrores, _('transmitancia térmica'), 0).ErrorDevuelto
                listaErrores += Comprueba(self.inercia.GetValue(), 2, listaErrores, _('masa/m2'), 0).ErrorDevuelto
            else:
                listaErrores += Comprueba(self.cerramientosChoice.GetStringSelection(), 0, listaErrores, _('librería cerramientos')).ErrorDevuelto
                listaErrores += Comprueba(self.profundidadEnterrada.GetValue(), 2, listaErrores, _('espesor de la capa de protección de tierra'), 0).ErrorDevuelto
        elif self.valorUChoice.GetStringSelection() == 'Estimadas':
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
        datos.append('Cubierta')
        datos.append(self.superficieMuro.GetValue())
        datos.append(self.UCerramiento)
        datos.append(self.densidadCerramiento)
        datos.append('Techo')
        datos.append(self.cerramientosChoice.GetStringSelection())
        datos.append('Sin patrón')
        datos.append(self.valorUChoice.GetStringSelection())
        datosConcretos = []
        if 'Conocid' in self.valorUChoice.GetStringSelection():
            datosConcretos.append(self.UradioButton.GetValue())
            datosConcretos.append(self.valorU.GetValue())
            datosConcretos.append(self.inercia.GetValue())
        elif 'Estimad' in self.valorUChoice.GetStringSelection():
            datosConcretos.append(self.aislanteRadioButton.GetValue())
            datosConcretos.append(self.tipoAislateChoice.GetStringSelection())
            datosConcretos.append(self.espesorAislante.GetValue())
            datosConcretos.append(self.Raislante.GetValue())
            datosConcretos.append(self.landaAislante.GetValue())
            datosConcretos.append(self.aislamientoCheck.GetValue())
        datos.append(datosConcretos)
        datos.append(self.profundidadEnterrada.GetValue())
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
        self.cerramientosChoice.SetStringSelection(datos[6])
        self.valorUChoice.SetStringSelection(datos[8])
        if 'Conocid' in datos[8]:
            self.UradioButton.SetValue(datos[9][0])
            self.libreriaRadioButton.SetValue(not datos[9][0])
            self.valorU.SetValue(str(datos[9][1]))
            self.inercia.SetValue(datos[9][2])
        elif 'Estimad' in datos[8]:
            self.aislanteRadioButton.SetValue(datos[9][0])
            self.RaislateRadio.SetValue(not datos[9][0])
            self.tipoAislateChoice.SetStringSelection(datos[9][1])
            self.espesorAislante.SetValue(datos[9][2])
            self.Raislante.SetValue(datos[9][3])
            self.landaAislante.SetValue(datos[9][4])
            if len(datos[9]) == 5:
                tieneAislamiento = True
            else:
                tieneAislamiento = datos[9][5]
            self.aislamientoCheck.SetValue(tieneAislamiento)
        self.OnAislamientoCheckCheckbox(None)
        self.OnValorUChoiceChoice(None)
        self.profundidadEnterrada.SetValue(datos[10])
        self.longitudMuro.SetValue(datos[11])
        self.alturaMuro.SetValue(datos[12])
        self.multiMuro.SetValue(datos[13])
        self.subgrupoChoice.SetStringSelection(datos[14])
        self.OnAislanteRadioButtonRadiobutton(None)
        self.parent.panelElegirObjeto.definirCubierta.SetValue(True)
        self.parent.panelElegirObjeto.mostrarOpcionesContactoCubierta()
        self.parent.panelElegirObjeto.contactoSuelo.SetValue(True)
        colorSombra = wx.Color(240, 240, 240)
        colorNormal = wx.Color(255, 255, 255)
        self.parent.panelElegirObjeto.definirSuelo.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirCubierta.SetBackgroundColour(colorSombra)
        self.parent.panelElegirObjeto.definirFachada.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirParticionInterior.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirHueco.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirPuenteTermico.SetBackgroundColour(colorNormal)
        self.profundidadEnterrada.SetForegroundColour(wx.Colour(0, 0, 0))
        self.bolCalcularCaracteristicas = True
        self.calcularCaracteristicasCerramiento(None)
        self.actualizaDiccionario()
        return