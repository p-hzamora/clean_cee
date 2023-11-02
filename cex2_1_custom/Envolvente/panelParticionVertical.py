# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\panelParticionVertical.pyc
# Compiled at: 2015-02-23 10:45:01
"""
Modulo: panelParticionVertical.py

"""
from Envolvente.comprobarCampos import Comprueba
from miChoice import MiChoice
import Envolvente.apendiceE as apendiceE, Envolvente.tablasValores as tablasValores, directorios, Calculos.listadosWeb as listadosWeb, LibreriasCE3X.menuCerramientos as menuCerramientos, nuevoUndo, wx, logging
Directorio = directorios.BuscaDirectorios().Directorio
wxID_PANEL1NOMBREMUROTEXT, wxID_PANEL1NOMBREMURO, wxID_PANEL1SUBGRUPOTEXT, wxID_PANEL1SUBGRUPOCHOICE, wxID_CARACTERISTICASLINEATEXT, wxID_EFICIENCIALINEATEXT, wxID_PANEL1VALORUTEXT, wxID_PANEL1CHOICE1, wxID_PANEL1UFINALTEXT, wxID_PANEL1UFINALCUADRO, wxID_PANEL1UNIDADESUFINAL, wxID_PANEL1SUPERFICIEPARTICIONTEXT, wxID_PANEL1SUPERFICIEPARTICION, wxID_PANEL1SUPERFICIEUNIDADESTEXT, wxID_PANEL1STATICBITMAP1, wxID_PANEL1UCONOCIDATEXT, wxID_PANEL1VALORUCONOCIDA, wxID_PANEL1UNIDADESUCONOCIDATEXT, wxID_PANEL1VENTILACIONTEXT, wxID_PANEL1VENTILACIONCHOICE, wxID_PANEL1SUPERFICIECERRAMIENTOTEXT, wxID_PANEL1SUPERFICIECERRAMIENTO, wxID_PANEL1SUPERFICIECERRAMIENTOUNIDADESTEXT, wxID_PANEL1AISLAMIENTOCHECK, wxID_PANEL1POSICIONAISLAMIENTOCHOICE, wxID_TEMPTEXT, wxID_CARACTERISTICASPARTICIONLINEATEXT, wxID_PANEL1VALORUESTIMADATEXT, wxID_PANEL1ESTIMADACHOICE, wxID_PANEL1UPARTICIONRADIOBUTTON, wxID_PANEL1VALORUPARTICION, wxID_PANEL1UNIDADESUPARTICIONTEXT, wxID_PANEL1LIBRERIAUPARTICIONRADIOBUTTON, wxID_PANEL1UPARTICIONCERRAMIENTOSCHOICE, wxID_PANEL1LIBRERIABOTONUPARTICION, wxID_PANEL1LONGIMUROTEXT, wxID_PANEL1LONGIMURO, wxID_PANEL1LONGITUDUNIDADESTEXT, wxID_PANEL1ALTURAMUROTEXT, wxID_PANEL1ALTURAMURO, wxID_PANEL1ALTURAUNIDADESTEXT = [ wx.NewId() for _init_ctrls in range(41) ]

class Panel1(wx.Panel, nuevoUndo.VistaUndo):
    """
    Clase: Panel1 del modulo panelParticionVertical.py

    """

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
        wx.Panel.__init__(self, id=ide, name='panelParticionVertical', parent=prnt, pos=posi, size=siz, style=styl)
        self.SetBackgroundColour('white')
        self.nombreMuroText = wx.StaticText(id=wxID_PANEL1NOMBREMUROTEXT, label=_('Nombre'), name='nombreMuroText', parent=self, pos=wx.Point(15, 2), size=wx.Size(102, 13), style=0)
        self.nombreMuro = wx.TextCtrl(id=wxID_PANEL1NOMBREMURO, name='nombreMuro', parent=self, pos=wx.Point(200, 0), size=wx.Size(180, 21), style=0, value=_('Partición vertical'))
        self.nombreMuro.SetForegroundColour(wx.Colour(100, 200, 0))
        self.nombreMuro.Bind(wx.EVT_TEXT, self.OnNombreMuro, id=wxID_PANEL1NOMBREMURO)
        self.subgrupoText = wx.StaticText(id=wxID_PANEL1SUBGRUPOTEXT, label=_('Zona'), name='subgrupoText', parent=self, pos=wx.Point(435, 2), size=wx.Size(50, 13), style=0)
        self.subgrupoChoice = MiChoice(choices=[], id=wxID_PANEL1SUBGRUPOCHOICE, name='subgrupoChoice', parent=self, pos=wx.Point(496, 0), size=wx.Size(214, 21), style=0)
        self.CaracteristicasLineaText = wx.StaticBox(id=wxID_CARACTERISTICASLINEATEXT, label=_('Dimensiones'), name='LineaText', parent=self, pos=wx.Point(0, 28), size=wx.Size(710, 98), style=0)
        self.CaracteristicasLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.superficieParticionText = wx.StaticText(id=wxID_PANEL1SUPERFICIEPARTICIONTEXT, label=_('Superficie de la partición'), name='superficieParticionText', parent=self, pos=wx.Point(15, 51), size=wx.Size(180, 13), style=0)
        self.superficieParticion = wx.TextCtrl(id=wxID_PANEL1SUPERFICIEPARTICION, name='superficieParticion', parent=self, pos=wx.Point(200, 49), size=wx.Size(80, 21), style=0, value='')
        self.superficieParticion.Bind(wx.EVT_TEXT, self.OnCambioSuperficie, id=wxID_PANEL1SUPERFICIEPARTICION)
        self.superficieUnidadesText = wx.StaticText(id=wxID_PANEL1SUPERFICIEUNIDADESTEXT, label=_('m2'), name='superficieUnidadesText', parent=self, pos=wx.Point(285, 51), size=wx.Size(14, 13), style=0)
        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(Directorio + '/Imagenes/InteriorVertical.bmp', wx.BITMAP_TYPE_BMP), id=wxID_PANEL1STATICBITMAP1, name='staticBitmap1', parent=self, pos=wx.Point(496, 36), size=wx.Size(186, 87), style=0)
        self.longitudMuroText = wx.StaticText(id=wxID_PANEL1LONGIMUROTEXT, label=_('Longitud'), name='longitudMuroText', parent=self, pos=wx.Point(200, 74), size=wx.Size(28, 13), style=0)
        self.longitudMuro = wx.TextCtrl(id=wxID_PANEL1LONGIMURO, name='longitudMuro', parent=self, pos=wx.Point(240, 72), size=wx.Size(40, 15), style=0, value='')
        self.longitudMuro.Bind(wx.EVT_TEXT, self.OnCambioLAMText, id=wxID_PANEL1LONGIMURO)
        self.LongitudUnidadesText = wx.StaticText(id=wxID_PANEL1LONGITUDUNIDADESTEXT, label=_('m'), name='profundidadUnidadesText', parent=self, pos=wx.Point(285, 74), size=wx.Size(14, 13), style=0)
        self.alturaMuroText = wx.StaticText(id=wxID_PANEL1ALTURAMUROTEXT, label=_('Altura'), name='alturaMuroText', parent=self, pos=wx.Point(200, 90), size=wx.Size(28, 13), style=0)
        self.alturaMuro = wx.TextCtrl(id=wxID_PANEL1ALTURAMURO, name='alturaMuro', parent=self, pos=wx.Point(240, 88), size=wx.Size(40, 15), style=0, value='')
        self.alturaMuro.Bind(wx.EVT_TEXT, self.OnCambioLAMText, id=wxID_PANEL1ALTURAMURO)
        self.alturaMuroUnidades = wx.StaticText(id=wxID_PANEL1ALTURAUNIDADESTEXT, label=_('m'), name='alturaMuroUnidades', parent=self, pos=wx.Point(285, 90), size=wx.Size(14, 13), style=0)
        self.longitudMuroText.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.LongitudUnidadesText.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.alturaMuroText.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.alturaMuroUnidades.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.EficienciaLineaText = wx.StaticBox(id=wxID_EFICIENCIALINEATEXT, label=_('Parámetros característicos para el cálculo de la U global'), name='EficienciaLineaText', parent=self, pos=wx.Point(0, 130), size=wx.Size(710, 212), style=0)
        self.EficienciaLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.EficienciaLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.valorUText = wx.StaticText(id=wxID_PANEL1VALORUTEXT, label=_('Propiedades térmicas: Uglobal'), name='valorUText', parent=self, pos=wx.Point(15, 154), size=wx.Size(160, 13), style=0)
        self.valorUText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.valorUChoice = MiChoice(choices=listadosWeb.listadoOpcionesU, id=wxID_PANEL1CHOICE1, name='valorUChoice', parent=self, pos=wx.Point(200, 151), size=wx.Size(180, 21), style=0)
        self.valorUChoice.SetStringSelection('Por defecto')
        self.valorUChoice.Bind(wx.EVT_CHOICE, self.OnValorUChoice, id=wxID_PANEL1CHOICE1)
        self.UFinalText = wx.StaticText(id=wxID_PANEL1UFINALTEXT, label=_('Transmitancia térmica'), name='UFinalText', parent=self, pos=wx.Point(460, 155), size=wx.Size(124, 25), style=0)
        self.UFinalText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.UFinalCuadro = wx.TextCtrl(id=wxID_PANEL1UFINALCUADRO, name='UFinalCuadro', parent=self, pos=wx.Point(601, 153), size=wx.Size(56, 21), style=0, value='')
        self.UFinalCuadro.Enable(False)
        self.unidadesUFinal = wx.StaticText(id=wxID_PANEL1UNIDADESUFINAL, label=_('W/m2K'), name='UFinalText', parent=self, pos=wx.Point(662, 155), size=wx.Size(40, 13), style=0)
        self.unidadesUFinal.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.UFinalText.SetForegroundColour(wx.Colour(100, 100, 100))
        self.unidadesUFinal.SetForegroundColour(wx.Colour(100, 100, 100))
        self.UconocidaText = wx.StaticText(id=wxID_PANEL1UCONOCIDATEXT, label=_('Transmitancia térmica'), name='UconocidaText', parent=self, pos=wx.Point(460, 155), size=wx.Size(124, 13), style=wx.RB_GROUP)
        self.UconocidaText.Show(False)
        self.valorUConocida = wx.TextCtrl(id=wxID_PANEL1VALORUCONOCIDA, name='valorU', parent=self, pos=wx.Point(601, 153), size=wx.Size(56, 21), style=0, value='')
        self.valorUConocida.Show(False)
        self.valorUConocida.Bind(wx.EVT_TEXT, self.calcularCaracteristicasCerramiento, id=wxID_PANEL1VALORUCONOCIDA)
        self.UnidadesUConocida = wx.StaticText(id=wxID_PANEL1UNIDADESUCONOCIDATEXT, label=_('W/m2K'), name='UnidadesUConocida', parent=self, pos=wx.Point(662, 155), size=wx.Size(40, 13), style=0)
        self.UnidadesUConocida.Show(False)
        self.ventilacionText = wx.StaticText(id=wxID_PANEL1VENTILACIONTEXT, label=_('Grado ventilación del espacio NH'), name='ventilacionText', parent=self, pos=wx.Point(15, 180), size=wx.Size(183, 13), style=0)
        self.ventilacionText.Show(False)
        self.ventilacionChoice = MiChoice(choices=listadosWeb.listadoOpcionesVentilacionEspacioNH, id=wxID_PANEL1VENTILACIONCHOICE, name='ventilacionChoice', parent=self, pos=wx.Point(200, 178), size=wx.Size(180, 21), style=0)
        self.ventilacionChoice.SetSelection(0)
        self.ventilacionChoice.Show(False)
        self.ventilacionChoice.Bind(wx.EVT_CHOICE, self.calcularCaracteristicasCerramiento, id=wxID_PANEL1VENTILACIONCHOICE)
        self.aislamientoCheck = wx.CheckBox(id=wxID_PANEL1AISLAMIENTOCHECK, label=_('Tiene aislamiento térmico'), name='aislamientoCheck', parent=self, pos=wx.Point(15, 205), size=wx.Size(176, 13), style=0)
        self.aislamientoCheck.SetValue(False)
        self.aislamientoCheck.Show(False)
        self.aislamientoCheck.Bind(wx.EVT_CHECKBOX, self.OnAislamientoCheck, id=wxID_PANEL1AISLAMIENTOCHECK)
        self.posicionAislamientoChoice = MiChoice(choices=listadosWeb.listadoOpcionesPosicionAislamientoParticion, id=wxID_PANEL1POSICIONAISLAMIENTOCHOICE, name='posicionAislamientoChoice', parent=self, pos=wx.Point(200, 203), size=wx.Size(180, 21), style=0)
        self.posicionAislamientoChoice.Show(False)
        self.posicionAislamientoChoice.SetSelection(1)
        self.posicionAislamientoChoice.Bind(wx.EVT_CHOICE, self.calcularCaracteristicasCerramiento, id=wxID_PANEL1POSICIONAISLAMIENTOCHOICE)
        self.tempText = wx.StaticText(id=wxID_TEMPTEXT, label=_(''), name='tempText', parent=self, pos=wx.Point(400, 300), size=wx.Size(1, 1), style=0)
        self.tempText.Show(False)
        self.superficieCerramientoText = wx.StaticText(id=wxID_PANEL1SUPERFICIECERRAMIENTOTEXT, label=_('Superficie del cerramiento'), name='superficieCerramientoText', parent=self, pos=wx.Point(460, 205), size=wx.Size(124, 13), style=0)
        self.superficieCerramientoText.Show(False)
        self.superficieCerramiento = wx.TextCtrl(id=wxID_PANEL1SUPERFICIECERRAMIENTO, name='superficieCerramiento', parent=self, pos=wx.Point(601, 203), size=wx.Size(56, 21), style=0, value='')
        self.superficieCerramiento.Show(False)
        self.superficieCerramiento.Bind(wx.EVT_TEXT, self.calcularCaracteristicasCerramiento, id=wxID_PANEL1SUPERFICIECERRAMIENTO)
        self.superficieCerramientoUnidadesText = wx.StaticText(id=wxID_PANEL1SUPERFICIECERRAMIENTOUNIDADESTEXT, label=_('m2'), name='superficieUnidadesText', parent=self, pos=wx.Point(662, 205), size=wx.Size(15, 13), style=0)
        self.superficieCerramientoUnidadesText.Show(False)
        self.CaracteristicasParticionLineaText = wx.StaticBox(id=wxID_CARACTERISTICASPARTICIONLINEATEXT, label=_('Definir la transmitancia térmica de la partición'), name='LineaText', parent=self, pos=wx.Point(15, 230), size=wx.Size(680, 100), style=0)
        self.CaracteristicasParticionLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasParticionLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.CaracteristicasParticionLineaText.Show(False)
        self.valorUEstimadaText = wx.StaticText(id=wxID_PANEL1VALORUESTIMADATEXT, label=_('Definir Upartición'), name='valorUEstimadaText', parent=self, pos=wx.Point(30, 253), size=wx.Size(165, 13), style=0)
        self.valorUEstimadaText.Show(False)
        self.valorUEstimadaChoice = MiChoice(choices=listadosWeb.listadoOpcionesUParticion, id=wxID_PANEL1ESTIMADACHOICE, name='valorUEstimadaChoice', parent=self, pos=wx.Point(200, 251), size=wx.Size(180, 21), style=0)
        self.valorUEstimadaChoice.SetStringSelection('Por defecto')
        self.valorUEstimadaChoice.Show(False)
        self.valorUEstimadaChoice.Bind(wx.EVT_CHOICE, self.OnValorUChoiceEstimada, id=wxID_PANEL1ESTIMADACHOICE)
        self.UparticionRadioButton = wx.RadioButton(id=wxID_PANEL1UPARTICIONRADIOBUTTON, label=_('Transmitancia térmica Up'), name='UparticionRadioButton', parent=self, pos=wx.Point(30, 278), size=wx.Size(168, 13), style=wx.RB_GROUP)
        self.UparticionRadioButton.SetValue(True)
        self.UparticionRadioButton.Show(False)
        self.UparticionRadioButton.Bind(wx.EVT_RADIOBUTTON, self.OnUParticionRadioButton, id=wxID_PANEL1UPARTICIONRADIOBUTTON)
        self.valorUparticion = wx.TextCtrl(id=wxID_PANEL1VALORUPARTICION, name='valorUparticion', parent=self, pos=wx.Point(200, 276), size=wx.Size(56, 21), style=0, value='')
        self.valorUparticion.Show(False)
        self.valorUparticion.Bind(wx.EVT_TEXT, self.calcularCaracteristicasCerramiento, id=wxID_PANEL1VALORUPARTICION)
        self.UnidadesUparticion = wx.StaticText(id=wxID_PANEL1UNIDADESUPARTICIONTEXT, label=_('W/m2K'), name='UnidadesUparticion', parent=self, pos=wx.Point(261, 278), size=wx.Size(99, 13), style=0)
        self.UnidadesUparticion.Show(False)
        self.libreriaUparticionRadioButton = wx.RadioButton(id=wxID_PANEL1LIBRERIAUPARTICIONRADIOBUTTON, label=_('Librería de cerramientos'), name='libreriaRadioButton', parent=self, pos=wx.Point(30, 303), size=wx.Size(136, 13), style=0)
        self.libreriaUparticionRadioButton.SetValue(False)
        self.libreriaUparticionRadioButton.Show(False)
        self.libreriaUparticionRadioButton.Bind(wx.EVT_RADIOBUTTON, self.OnUParticionRadioButton, id=wxID_PANEL1LIBRERIAUPARTICIONRADIOBUTTON)
        self.cerramientosUparticionChoice = wx.Choice(choices=self.parent.parent.parent.listadoCerramientos, id=wxID_PANEL1UPARTICIONCERRAMIENTOSCHOICE, name='cerramientosChoice', parent=self, pos=wx.Point(200, 301), size=wx.Size(262, 21), style=0)
        self.cerramientosUparticionChoice.Show(False)
        self.cerramientosUparticionChoice.Enable(False)
        self.cerramientosUparticionChoice.Bind(wx.EVT_CHOICE, self.calcularCaracteristicasCerramiento, id=wxID_PANEL1UPARTICIONCERRAMIENTOSCHOICE)
        self.libreriaBotonUparticion = wx.BitmapButton(id=wxID_PANEL1LIBRERIABOTONUPARTICION, bitmap=wx.Bitmap(Directorio + '/Imagenes/cerramientos.ico', wx.BITMAP_TYPE_ANY), parent=self, pos=wx.Point(467, 301), size=wx.Size(23, 21), style=wx.BU_AUTODRAW)
        self.libreriaBotonUparticion.Bind(wx.EVT_BUTTON, self.OnLibreriaBotonButton, id=wxID_PANEL1LIBRERIABOTONUPARTICION)
        self.libreriaBotonUparticion.Show(False)
        self.libreriaBotonUparticion.Enable(False)
        self.nombreMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1NOMBREMURO)
        self.superficieParticion.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1SUPERFICIEPARTICION)
        self.longitudMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1LONGIMURO)
        self.alturaMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1ALTURAMURO)
        self.UFinalCuadro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1UFINALCUADRO)
        self.valorUConocida.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1VALORUCONOCIDA)
        self.superficieCerramiento.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1SUPERFICIECERRAMIENTO)
        self.valorUparticion.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1VALORUPARTICION)
        self.subgrupoChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1SUBGRUPOCHOICE)
        self.valorUChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1CHOICE1)
        self.ventilacionChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1VENTILACIONCHOICE)
        self.posicionAislamientoChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1POSICIONAISLAMIENTOCHOICE)
        self.valorUEstimadaChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1ESTIMADACHOICE)
        self.cerramientosUparticionChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1UPARTICIONCERRAMIENTOSCHOICE)
        self.UparticionRadioButton.Bind(wx.EVT_KILL_FOCUS, self.manejadorRadio, id=wxID_PANEL1UPARTICIONRADIOBUTTON)
        self.libreriaUparticionRadioButton.Bind(wx.EVT_KILL_FOCUS, self.manejadorRadio, id=wxID_PANEL1LIBRERIAUPARTICIONRADIOBUTTON)
        self.aislamientoCheck.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1AISLAMIENTOCHECK)

    def actualizaDiccionario(self):
        self.diccionario = {}
        self.diccionario['panelParticionVertical.nombreMuro'] = self.nombreMuro.GetValue()
        self.diccionario['panelParticionVertical.superficieParticion'] = self.superficieParticion.GetValue()
        self.diccionario['panelParticionVertical.longitudMuro'] = self.longitudMuro.GetValue()
        self.diccionario['panelParticionVertical.alturaMuro'] = self.alturaMuro.GetValue()
        self.diccionario['panelParticionVertical.UFinalCuadro'] = self.UFinalCuadro.GetValue()
        self.diccionario['panelParticionVertical.valorUConocida'] = self.valorUConocida.GetValue()
        self.diccionario['panelParticionVertical.superficieCerramiento'] = self.superficieCerramiento.GetValue()
        self.diccionario['panelParticionVertical.valorUparticion'] = self.valorUparticion.GetValue()
        self.diccionario['panelParticionVertical.subgrupoChoice'] = self.subgrupoChoice.GetSelection()
        self.diccionario['panelParticionVertical.valorUChoice'] = self.valorUChoice.GetSelection()
        self.diccionario['panelParticionVertical.ventilacionChoice'] = self.ventilacionChoice.GetSelection()
        self.diccionario['panelParticionVertical.posicionAislamientoChoice'] = self.posicionAislamientoChoice.GetSelection()
        self.diccionario['panelParticionVertical.valorUEstimadaChoice'] = self.valorUEstimadaChoice.GetSelection()
        self.diccionario['panelParticionVertical.cerramientosUparticionChoice'] = self.cerramientosUparticionChoice.GetSelection()
        self.diccionario['panelParticionVertical.radios'] = self.GetRadioValues()
        self.diccionario['panelParticionVertical.aislamientoCheck'] = self.aislamientoCheck.GetValue()

    def GetRadioValues(self):
        return [
         self.UparticionRadioButton.GetValue(),
         self.libreriaUparticionRadioButton.GetValue()]

    def SetRadioValues(self, lista):
        self.UparticionRadioButton.SetValue(lista[0])
        self.libreriaUparticionRadioButton.SetValue(lista[1])

    def cogeValoresDiccionario(self):
        self.nombreMuro.SetValue(self.diccionario['panelParticionVertical.nombreMuro'])
        self.superficieParticion.SetValue(self.diccionario['panelParticionVertical.superficieParticion'])
        self.longitudMuro.SetValue(self.diccionario['panelParticionVertical.longitudMuro'])
        self.alturaMuro.SetValue(self.diccionario['panelParticionVertical.alturaMuro'])
        self.UFinalCuadro.SetValue(self.diccionario['panelParticionVertical.UFinalCuadro'])
        self.valorUConocida.SetValue(self.diccionario['panelParticionVertical.valorUConocida'])
        self.superficieCerramiento.SetValue(self.diccionario['panelParticionVertical.superficieCerramiento'])
        self.valorUparticion.SetValue(self.diccionario['panelParticionVertical.valorUparticion'])
        self.subgrupoChoice.SetSelection(self.diccionario['panelParticionVertical.subgrupoChoice'])
        self.valorUChoice.SetSelection(self.diccionario['panelParticionVertical.valorUChoice'])
        self.ventilacionChoice.SetSelection(self.diccionario['panelParticionVertical.ventilacionChoice'])
        self.posicionAislamientoChoice.SetSelection(self.diccionario['panelParticionVertical.posicionAislamientoChoice'])
        self.valorUEstimadaChoice.SetSelection(self.diccionario['panelParticionVertical.valorUEstimadaChoice'])
        self.cerramientosUparticionChoice.SetSelection(self.diccionario['panelParticionVertical.cerramientosUparticionChoice'])
        self.aislamientoCheck.SetValue(self.diccionario['panelParticionVertical.aislamientoCheck'])
        lista = self.GetRadioValues()
        self.SetRadioValues(lista)
        self.OnValorUChoice(None)
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

    def OnSuperficieText(self, event):
        """
        Metodo: OnSuperficieText

        ARGUMENTOS:
                event:
        """
        if self.bol == True:
            self.longitudMuro.SetValue('')
            self.alturaMuro.SetValue('')

    def OnCambioLAMText(self, event):
        """
        Metodo: OnCambioLAMText

        ARGUMENTOS:
                event:
        """
        longitud = self.longitudMuro.GetValue()
        altura = self.alturaMuro.GetValue()
        if ',' in longitud:
            longitud = longitud.replace(',', '.')
            self.longitudMuro.SetValue(longitud)
            self.longitudMuro.SetInsertionPointEnd()
        if ',' in altura:
            altura = altura.replace(',', '.')
            self.alturaMuro.SetValue(altura)
            self.alturaMuro.SetInsertionPointEnd()
        try:
            lon = float(self.longitudMuro.GetValue())
            alt = float(self.alturaMuro.GetValue())
            self.bol = False
            superficieTotal = round(lon * alt, 2)
            self.superficieParticion.SetValue(str(superficieTotal))
            self.bol = True
        except (ValueError, TypeError):
            pass

    def OnCambioSuperficie(self, event):
        """
        Metodo: OnCambioSuperficie

        ARGUMENTOS:
                event:
        """
        if self.bol == True:
            self.longitudMuro.SetValue('')
            self.alturaMuro.SetValue('')
        self.calcularCaracteristicasCerramiento(None)
        return

    def OnNombreMuro(self, event):
        """
        Metodo: OnNombreMuro

        ARGUMENTOS:
                event:
        """
        if self.nombreMuro.GetValue() == _('Partición vertical'):
            self.nombreMuro.SetForegroundColour(wx.Colour(100, 200, 0))
        else:
            self.nombreMuro.SetForegroundColour(wx.Colour(0, 0, 0))

    def OnValorUChoice(self, event):
        """
        Metodo: OnValorUChoice

        ARGUMENTOS:
                event:
        """
        if self.valorUChoice.GetStringSelection() == 'Por defecto':
            self.UFinalText.Show(True)
            self.UFinalCuadro.Show(True)
            self.unidadesUFinal.Show(True)
            self.UconocidaText.Show(False)
            self.valorUConocida.Show(False)
            self.UnidadesUConocida.Show(False)
            self.ventilacionText.Show(False)
            self.ventilacionChoice.Show(False)
            self.superficieCerramientoText.Show(False)
            self.superficieCerramiento.Show(False)
            self.superficieCerramientoUnidadesText.Show(False)
            self.aislamientoCheck.Show(False)
            self.posicionAislamientoChoice.Show(False)
            self.CaracteristicasParticionLineaText.Show(False)
            self.valorUEstimadaText.Show(False)
            self.valorUEstimadaChoice.Show(False)
            self.UparticionRadioButton.Show(False)
            self.valorUparticion.Show(False)
            self.UnidadesUparticion.Show(False)
            self.libreriaUparticionRadioButton.Show(False)
            self.cerramientosUparticionChoice.Show(False)
            self.libreriaBotonUparticion.Show(False)
        elif self.valorUChoice.GetStringSelection() == 'Conocidas':
            self.UFinalText.Show(False)
            self.UFinalCuadro.Show(False)
            self.unidadesUFinal.Show(False)
            self.UconocidaText.Show(True)
            self.valorUConocida.Show(True)
            self.UnidadesUConocida.Show(True)
            self.ventilacionText.Show(False)
            self.ventilacionChoice.Show(False)
            self.superficieCerramientoText.Show(False)
            self.superficieCerramiento.Show(False)
            self.superficieCerramientoUnidadesText.Show(False)
            self.aislamientoCheck.Show(False)
            self.posicionAislamientoChoice.Show(False)
            self.CaracteristicasParticionLineaText.Show(False)
            self.valorUEstimadaText.Show(False)
            self.valorUEstimadaChoice.Show(False)
            self.UparticionRadioButton.Show(False)
            self.valorUparticion.Show(False)
            self.UnidadesUparticion.Show(False)
            self.libreriaUparticionRadioButton.Show(False)
            self.cerramientosUparticionChoice.Show(False)
            self.libreriaBotonUparticion.Show(False)
        elif self.valorUChoice.GetStringSelection() == 'Estimadas':
            self.UFinalText.Show(True)
            self.UFinalCuadro.Show(True)
            self.unidadesUFinal.Show(True)
            self.UconocidaText.Show(False)
            self.valorUConocida.Show(False)
            self.UnidadesUConocida.Show(False)
            self.ventilacionText.Show(True)
            self.ventilacionChoice.Show(True)
            self.superficieCerramientoText.Show(True)
            self.superficieCerramiento.Show(True)
            self.superficieCerramientoUnidadesText.Show(True)
            self.aislamientoCheck.Show(True)
            self.OnAislamientoCheck(None)
            self.CaracteristicasParticionLineaText.Show(True)
            self.valorUEstimadaText.Show(True)
            self.valorUEstimadaChoice.Show(True)
            self.OnValorUChoiceEstimada(None)
        self.calcularCaracteristicasCerramiento(None)
        return

    def OnAislamientoCheck(self, event):
        """
        Metodo: OnAislamientoCheck

        ARGUMENTOS:
                event:
        """
        if self.aislamientoCheck.GetValue() == True:
            self.tempText.Show(True)
            self.posicionAislamientoChoice.Show(True)
        elif self.aislamientoCheck.GetValue() == False:
            self.posicionAislamientoChoice.Show(False)
        self.tempText.Show(False)
        self.calcularCaracteristicasCerramiento(None)
        return

    def OnValorUChoiceEstimada(self, event):
        """
        Metodo: OnValorUChoiceEstimada

        funcion que hace que aparezca campos si elige la opcion Conocida o por defecto en Uparticion(opcion estimada)

        ARGUMENTOS:
                event:
        """
        if self.valorUEstimadaChoice.GetStringSelection() == 'Conocida':
            self.UparticionRadioButton.Show(True)
            self.valorUparticion.Show(True)
            self.UnidadesUparticion.Show(True)
            self.libreriaUparticionRadioButton.Show(True)
            self.cerramientosUparticionChoice.Show(True)
            self.libreriaBotonUparticion.Show(True)
            self.OnUParticionRadioButton(None)
        elif self.valorUEstimadaChoice.GetStringSelection() == 'Por defecto':
            self.UparticionRadioButton.Show(False)
            self.valorUparticion.Show(False)
            self.UnidadesUparticion.Show(False)
            self.libreriaUparticionRadioButton.Show(False)
            self.cerramientosUparticionChoice.Show(False)
            self.libreriaBotonUparticion.Show(False)
        self.calcularCaracteristicasCerramiento(None)
        return

    def OnUParticionRadioButton(self, event):
        """
        Metodo: OnUradioButton

        funcion que hace que se bloqueen o se desbloqueen al elegir radiobutton en Uparticion(opcion estimada)/opcion conocida
        ARGUMENTOS:
                event:
        """
        if self.UparticionRadioButton.GetValue() == True:
            self.valorUparticion.Enable(True)
            self.cerramientosUparticionChoice.Enable(False)
            self.libreriaBotonUparticion.Enable(False)
        else:
            self.valorUparticion.Enable(False)
            self.cerramientosUparticionChoice.Enable(True)
            self.libreriaBotonUparticion.Enable(True)
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

        try:
            self.cerramientosUparticionChoice.SetItems(self.parent.parent.parent.listadoCerramientos)
        except:
            logging.info('Excepcion en: %s' % __name__)

        self.dlg.Destroy()

    def calcularCaracteristicasCerramiento(self, event):
        """
        Metodo: calcularCaracteristicasCerramiento

        ARGUMENTOS:
                event:
        """
        if self.bolCalcularCaracteristicas == True:
            try:
                if self.valorUChoice.GetStringSelection() == 'Por defecto':
                    valoresCerr = tablasValores.tablasValores('Particion', 'Vertical', [
                     self.parent.parent.parent.panelDatosGenerales.anoConstruccionChoice.GetSelection(),
                     self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection(),
                     self.parent.parent.parent.panelDatosGenerales.NBE], 'Por defecto')
                    self.UCerramiento = valoresCerr.UCerramiento
                    self.densidadCerramiento = valoresCerr.densidadCerramiento
                elif self.valorUChoice.GetStringSelection() == 'Conocidas':
                    self.UCerramiento = float(self.valorUConocida.GetValue())
                    self.densidadCerramiento = 60.0
                elif self.valorUChoice.GetStringSelection() == 'Estimadas':
                    gradoVentilacion = self.ventilacionChoice.GetSelection()
                    Api = self.superficieParticion.GetValue()
                    Ae = self.superficieCerramiento.GetValue()
                    if self.aislamientoCheck.GetValue() == False:
                        casoAislamiento = 'Ninguno'
                    elif self.posicionAislamientoChoice.GetStringSelection() == 'La partición':
                        casoAislamiento = 'AisladoParticion'
                    elif self.posicionAislamientoChoice.GetStringSelection() == 'El cerramiento':
                        casoAislamiento = 'AisladoCerramiento'
                    elif self.posicionAislamientoChoice.GetStringSelection() == 'Ambos':
                        casoAislamiento = 'Ambos'
                    else:
                        casoAislamiento = 'Ninguno'
                    b = apendiceE.particionesInterioresCaso1(Api, Ae, casoAislamiento, gradoVentilacion)
                    if self.valorUEstimadaChoice.GetStringSelection() == 'Por defecto':
                        if self.aislamientoCheck.GetValue() == True and self.posicionAislamientoChoice.GetStringSelection() != 'El cerramiento':
                            tieneAislamiento = True
                        else:
                            tieneAislamiento = False
                        valoresCerr = tablasValores.tablasValores('Particion', 'Vertical', [
                         self.parent.parent.parent.panelDatosGenerales.anoConstruccionChoice.GetSelection(),
                         self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection(),
                         self.parent.parent.parent.panelDatosGenerales.NBE,
                         tieneAislamiento], 'Estimado')
                        Uparticion = valoresCerr.UCerramiento
                        self.densidadCerramiento = valoresCerr.densidadCerramiento
                    elif self.UparticionRadioButton.GetValue() == True:
                        Uparticion = float(self.valorUparticion.GetValue())
                        self.densidadCerramiento = 60.0
                    elif self.libreriaUparticionRadioButton.GetValue() == True:
                        for i in self.parent.parent.parent.listadoComposicionesCerramientos:
                            if i.nombre == self.cerramientosUparticionChoice.GetStringSelection().encode('iso-8859-15'):
                                Up_sinRs = float(i.transmitancia)
                                self.densidadCerramiento = round(i.peso, 2)
                                break

                        Uparticion = apendiceE.particionesInterioresResistencias(Up_sinRs, 'Vertical')
                    self.UCerramiento = float(b) * float(Uparticion)
                self.UCerramiento = round(self.UCerramiento, 2)
                self.cargarTransmitanciaTermicaGlobal()
            except:
                logging.info('Excepcion en: %s' % __name__)
                self.UCerramiento = ''
                self.densidadCerramiento = ''
                self.cargarTransmitanciaTermicaGlobal()

    def cargarTransmitanciaTermicaGlobal(self):
        """
        Metodo: cargarTransmitanciaTermicaGlobal

        """
        self.UFinalCuadro.SetValue(str(self.UCerramiento))

    def comprobarDatos(self):
        """
        Metodo: comprobarDatos

        """
        dato = self.superficieParticion.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.superficieParticion.SetValue(dato)
        dato = self.valorUConocida.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.valorUConocida.SetValue(dato)
        dato = self.superficieCerramiento.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.superficieCerramiento.SetValue(dato)
        dato = self.valorUparticion.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.valorUparticion.SetValue(dato)
        listaErrores = ''
        listaErrores += Comprueba(self.nombreMuro.GetValue(), 1, listaErrores, _('nombre')).ErrorDevuelto
        listaErrores += Comprueba(self.subgrupoChoice.GetStringSelection(), 0, listaErrores, _('zona')).ErrorDevuelto
        listaErrores += Comprueba(self.superficieParticion.GetValue(), 2, listaErrores, _('superficie'), 0).ErrorDevuelto
        if self.valorUChoice.GetStringSelection() == 'Por defecto':
            pass
        elif self.valorUChoice.GetStringSelection() == 'Conocidas':
            listaErrores += Comprueba(self.valorUConocida.GetValue(), 2, listaErrores, _('transmitancia térmica global'), 0).ErrorDevuelto
        elif self.valorUChoice.GetStringSelection() == 'Estimadas':
            listaErrores += Comprueba(self.ventilacionChoice.GetStringSelection(), 0, listaErrores, _('grado de ventilación del espacio no habitable')).ErrorDevuelto
            listaErrores += Comprueba(self.superficieCerramiento.GetValue(), 2, listaErrores, _('superficie del cerramiento'), 0).ErrorDevuelto
            if self.valorUEstimadaChoice.GetStringSelection() == 'Conocida':
                if self.UparticionRadioButton.GetValue() == True:
                    listaErrores += Comprueba(self.valorUparticion.GetValue(), 2, listaErrores, _('transmitancia térmica de la partición'), 0).ErrorDevuelto
                elif self.libreriaUparticionRadioButton.GetValue() == True:
                    listaErrores += Comprueba(self.cerramientosUparticionChoice.GetStringSelection(), 0, listaErrores, _('librería de cerramientos')).ErrorDevuelto
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
        datos.append('Partición Interior')
        datos.append(self.superficieParticion.GetValue())
        datos.append(self.UCerramiento)
        datos.append(self.densidadCerramiento)
        datos.append('')
        datos.append('')
        datos.append('Sin patrón')
        datos.append(self.valorUChoice.GetStringSelection())
        datosConcretos = []
        if self.valorUChoice.GetStringSelection() == 'Por defecto':
            pass
        elif self.valorUChoice.GetStringSelection() == 'Conocidas':
            datosConcretos.append(self.valorUConocida.GetValue())
        elif self.valorUChoice.GetStringSelection() == 'Estimadas':
            datosConcretos.append(self.ventilacionChoice.GetStringSelection())
            datosConcretos.append(self.superficieCerramiento.GetValue())
            datosConcretos.append(self.aislamientoCheck.GetValue())
            datosConcretos.append(self.posicionAislamientoChoice.GetStringSelection())
            datosConcretos.append(self.valorUEstimadaChoice.GetStringSelection())
            if self.valorUEstimadaChoice.GetStringSelection() == 'Por defecto':
                pass
            elif self.valorUEstimadaChoice.GetStringSelection() == 'Conocida':
                datosConcretos.append(self.UparticionRadioButton.GetValue())
                datosConcretos.append(self.valorUparticion.GetValue())
                datosConcretos.append(self.cerramientosUparticionChoice.GetStringSelection())
        datos.append(datosConcretos)
        datos.append(self.longitudMuro.GetValue())
        datos.append(self.alturaMuro.GetValue())
        datos.append('')
        datos.append(self.subgrupoChoice.GetStringSelection())
        datos.append('vertical')
        return datos

    def cargarDatos(self, datos):
        """
        Metodo: cargarDatos

        ARGUMENTOS:
                datos:
        """
        self.bolCalcularCaracteristicas = False
        self.nombreMuro.SetValue(datos[0])
        self.superficieParticion.SetValue(datos[2])
        self.valorUChoice.SetStringSelection(datos[6])
        self.valorUChoice.SetStringSelection(datos[8])
        if datos[8] == 'Por defecto':
            pass
        elif datos[8] == 'Conocidas':
            datosConcretos = datos[9]
            self.valorUConocida.SetValue(datosConcretos[0])
        elif datos[8] == 'Estimadas':
            datosConcretos = datos[9]
            self.ventilacionChoice.SetStringSelection(datosConcretos[0])
            self.superficieCerramiento.SetValue(datosConcretos[1])
            self.aislamientoCheck.SetValue(datosConcretos[2])
            self.posicionAislamientoChoice.SetStringSelection(datosConcretos[3])
            self.valorUEstimadaChoice.SetStringSelection(datosConcretos[4])
            if datosConcretos[4] == 'Por defecto':
                pass
            elif datosConcretos[4] == 'Conocida':
                self.UparticionRadioButton.SetValue(datosConcretos[5])
                self.valorUparticion.SetValue(datosConcretos[6])
                self.libreriaUparticionRadioButton.SetValue(not datosConcretos[5])
                self.cerramientosUparticionChoice.SetStringSelection(datosConcretos[7])
        self.OnValorUChoice(None)
        self.longitudMuro.SetValue(datos[10])
        self.alturaMuro.SetValue(datos[11])
        self.subgrupoChoice.SetStringSelection(datos[13])
        self.bolCalcularCaracteristicas = True
        self.calcularCaracteristicasCerramiento(None)
        self.parent.panelElegirObjeto.definirParticionInterior.SetValue(True)
        self.parent.panelElegirObjeto.mostrarOpcionesContactoParticion()
        self.parent.panelElegirObjeto.vertical.SetValue(True)
        colorSombra = wx.Color(240, 240, 240)
        colorNormal = wx.Color(255, 255, 255)
        self.parent.panelElegirObjeto.definirSuelo.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirCubierta.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirFachada.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirParticionInterior.SetBackgroundColour(colorSombra)
        self.parent.panelElegirObjeto.definirHueco.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirPuenteTermico.SetBackgroundColour(colorNormal)
        self.actualizaDiccionario()
        return