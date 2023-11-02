# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\panelHuecos.pyc
# Compiled at: 2015-02-23 10:30:00
"""
Modulo: panelHuecos.py

"""
from miChoice import MiChoice
import Envolvente.absortividad_cuadro as absortividad_cuadro, Envolvente.eltos_sombras as eltos_sombras, Envolvente.tablasValores as tablasValores, directorios, Calculos.listadosWeb as listadosWeb, LibreriasCE3X.menuMarcos as menuMarcos, LibreriasCE3X.menuVidrios as menuVidrios, nuevoUndo, wx, logging
Directorio = directorios.BuscaDirectorios().Directorio
wxID_PANEL1, wxID_PANEL1ABSORTIVIDADBOTON, wxID_PANEL1CERRAMIENTOCHOICE, wxID_PANEL1CERRAMIENTOTEXT, wxID_PANEL1DECRIPCIONHUECO, wxID_PANEL1DESCRIPCIONTEXT, wxID_PANEL1GVIDIRO, wxID_PANEL1GVIDRIOTEXT, wxID_PANEL1LIBRERIAMATERIALESTEXT, wxID_PANEL1MATERIALESCHOICE, wxID_PANEL1ORIENTACIONHUECO, wxID_PANEL1ORIENTACIONTEXT, wxID_PANEL1PORCENTAJEMARCO, wxID_PANEL1PORCENTAJEMARCOTEXT, wxID_PANEL1PORCENTAJEUNIDADESTEXT, wxID_PANEL1PROPIEDADESTERMICASCHOICE, wxID_PANEL1PROPIEDADESTERMICASTEXT, wxID_PANEL1PROTECCIONSOLARBOTON, wxID_PANEL1UMARCOUNIDADESTEXT, wxID_PANEL1SUPERFICIEHUECO, wxID_PANEL1SUPERFICIETEXT, wxID_PANEL1SUPERFICIEUNIDADESTEXT, wxID_PANEL1TIPOMARCOCHIOCE, wxID_PANEL1TIPOMARCOTEXT, wxID_PANEL1TIPOVIDRIOCHOICE, wxID_PANEL1TIPOVIDRIOTEXT, wxID_PANEL1UMARCO, wxID_PANEL1UMARCOTEXT, wxID_PANEL1UVIDRIO, wxID_PANEL1UVIDRIORADIO, wxID_PANEL1UVIDRIOUNIDADESTEXT, wxID_PANEL1PERMEABILIDADAIRE, wxID_PANEL1PERMEABILIDADAIRECHOICE, wxID_PANEL1PERMEABILIDAD, wxID_PANEL1PERMEABILIDADAIREUNIDADES, wxID_PANEL1LONGIMUROTEXT, wxID_PANEL1LONGIMURO, wxID_PANEL1LONGITUDUNIDADESTEXT, wxID_PANEL1ALTURAMUROTEXT, wxID_PANEL1ALTURAMURO, wxID_PANEL1ALTURAUNIDADESTEXT, wxID_PANEL1MULTIMUROTEXT, wxID_PANEL1ALTURAMURO, wxID_PANEL1MULTIMURO, wxID_PANEL1SUPERFICIEUNIDADESTEXT, wxID_PANEL1LIBRERIAMARCOSTEXT, wxID_PANEL1MARCOSCHOICE, wxID_PANEL1UVIDRIOTEXTTABLAS, wxID_PANEL1UVIDRIOTABLAS, wxID_PANEL1UVIDRIOUNIDADESTEXTTABLAS, wxID_PANEL1GVIDRIOTEXTTABLAS, wxID_PANEL1GVIDRIOTABLAS, wxID_PANEL1UMARCOTEXTTABLAS, wxID_PANEL1UMARCOTABLAS, wxID_PANEL1UMARCOUNIDADESTEXTTABLAS, wxID_PANEL1CONTRAVENTANACHECK, wxID_PANEL1CONTRAVENTANA2CHECK, wxID_PANEL1LIBRERIABOTON, wxID_LINEATEXT, wxID_PANEL1LIBRERIABOTON2, wxID_PANEL1OBSTACULOSREMOTOSCHOICE, wxID_PANEL1DISPOSITIVOCONTROLCHECK, wxID_CARACTERISTICASTEXT, wxID_PANEL1ABSORTIVIDADMARCO = [ wx.NewId() for _init_ctrls in range(64) ]

class panelHuecos(wx.Panel, nuevoUndo.VistaUndo):
    """
    Clase: panelHuecos del modulo panelHuecos.py

    """

    def OnDescripcionHueco(self, event):
        """
        Metodo: OnDescripcionHueco

        ARGUMENTOS:
                event:
        """
        if self.decripcionHueco.GetValue() == 'Hueco':
            self.decripcionHueco.SetForegroundColour(wx.Colour(100, 200, 0))
        else:
            self.decripcionHueco.SetForegroundColour(wx.Colour(0, 0, 0))

    def _init_ctrls(self, prnt, ide, posi, siz, styl, nam):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                 prnt:
                ide:
                 posi:
                 siz:
                 styl:
                 nam:
        """
        wx.Panel.__init__(self, id=ide, name='panelHuecos', parent=prnt, pos=posi, size=siz, style=styl)
        self.SetBackgroundColour('white')
        self.descripcionText = wx.StaticText(id=wxID_PANEL1DESCRIPCIONTEXT, label=_('Nombre'), name='descripcionText', parent=self, pos=wx.Point(15, 2), size=wx.Size(102, 13), style=0)
        self.decripcionHueco = wx.TextCtrl(id=wxID_PANEL1DECRIPCIONHUECO, name='decripcionHueco', parent=self, pos=wx.Point(143, 0), size=wx.Size(210, 21), style=0, value='Hueco')
        self.decripcionHueco.SetForegroundColour(wx.Colour(100, 200, 0))
        self.decripcionHueco.Bind(wx.EVT_TEXT, self.OnDescripcionHueco, id=wxID_PANEL1DECRIPCIONHUECO)
        self.cerramientoText = wx.StaticText(id=wxID_PANEL1CERRAMIENTOTEXT, label=_('Cerramiento asociado'), name='cerramientoText', parent=self, pos=wx.Point(15, 25), size=wx.Size(118, 13), style=0)
        self.cerramientoChoice = wx.Choice(choices=[], id=wxID_PANEL1CERRAMIENTOCHOICE, name='cerramientoChoice', parent=self, pos=wx.Point(143, 23), size=wx.Size(210, 21), style=0)
        self.cerramientoChoice.Bind(wx.EVT_CHOICE, self.OnCaracteristicasCerramiento, id=wxID_PANEL1CERRAMIENTOCHOICE)
        self.orientacionText = wx.StaticText(id=wxID_PANEL1ORIENTACIONTEXT, label=_('Orientación'), name='orientacionText', parent=self, pos=wx.Point(420, 25), size=wx.Size(70, 13), style=0)
        self.orientacionHueco = wx.TextCtrl(id=wxID_PANEL1ORIENTACIONHUECO, name='orientacionHueco', parent=self, pos=wx.Point(500, 23), size=wx.Size(210, 21), style=0, value='')
        self.orientacionHueco.Enable(False)
        self.DimensionesLineaText = wx.StaticBox(id=wxID_LINEATEXT, label=_('Dimensiones'), name='LineaText', parent=self, pos=wx.Point(0, 50), size=wx.Size(308, 145), style=0)
        self.DimensionesLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.DimensionesLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.EficienciaLineaText = wx.StaticBox(id=-1, label=_('Parámetros característicos del hueco'), name='EficienciaLineaText', parent=self, pos=wx.Point(0, 200), size=wx.Size(710, 142), style=0)
        self.EficienciaLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.EficienciaLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.longitudMuroText = wx.StaticText(id=wxID_PANEL1LONGIMUROTEXT, label=_('Longitud'), name='longitudMuroText', parent=self, pos=wx.Point(15, 69), size=wx.Size(102, 13), style=0)
        self.longitudMuro = wx.TextCtrl(id=wxID_PANEL1LONGIMURO, name='longitudMuro', parent=self, pos=wx.Point(143, 67), size=wx.Size(56, 21), style=0, value='')
        self.longitudMuro.Bind(wx.EVT_TEXT, self.OnCambioLAMText, id=wxID_PANEL1LONGIMURO)
        self.LongitudUnidadesText = wx.StaticText(id=wxID_PANEL1LONGITUDUNIDADESTEXT, label=_('m'), name='profundidadUnidadesText', parent=self, pos=wx.Point(204, 69), size=wx.Size(14, 13), style=0)
        self.alturaMuroText = wx.StaticText(id=wxID_PANEL1ALTURAMUROTEXT, label=_('Altura'), name='alturaMuroText', parent=self, pos=wx.Point(15, 91), size=wx.Size(40, 13), style=0)
        self.alturaMuro = wx.TextCtrl(id=wxID_PANEL1ALTURAMURO, name='alturaMuro', parent=self, pos=wx.Point(143, 89), size=wx.Size(56, 21), style=0, value='')
        self.alturaMuro.Bind(wx.EVT_TEXT, self.OnCambioLAMText, id=wxID_PANEL1ALTURAMURO)
        self.alturaMuroUnidades = wx.StaticText(id=wxID_PANEL1ALTURAUNIDADESTEXT, label=_('m'), name='alturaMuroUnidades', parent=self, pos=wx.Point(204, 91), size=wx.Size(14, 13), style=0)
        self.multiMuroText = wx.StaticText(id=wxID_PANEL1MULTIMUROTEXT, label=_('Multiplicador'), name='multiMuroText', parent=self, pos=wx.Point(15, 113), size=wx.Size(80, 13), style=0)
        self.multiMuro = wx.TextCtrl(id=wxID_PANEL1MULTIMURO, name='multiMuro', parent=self, pos=wx.Point(143, 111), size=wx.Size(56, 21), style=0, value='1')
        self.multiMuro.Bind(wx.EVT_TEXT, self.OnCambioLAMText, id=wxID_PANEL1MULTIMURO)
        self.superficieText = wx.StaticText(id=wxID_PANEL1SUPERFICIETEXT, label=_('Superficie'), name='superficieText', parent=self, pos=wx.Point(15, 146), size=wx.Size(103, 13), style=0)
        self.superficieHueco = wx.TextCtrl(id=wxID_PANEL1SUPERFICIEHUECO, name='superficieHueco', parent=self, pos=wx.Point(143, 144), size=wx.Size(56, 21), style=0, value='')
        self.superficieHueco.Bind(wx.EVT_TEXT, self.OnCambioSuperficie, id=wxID_PANEL1SUPERFICIEHUECO)
        self.superficieUnidadesText = wx.StaticText(id=wxID_PANEL1SUPERFICIEUNIDADESTEXT, label=_('m2'), name='superficieUnidadesText', parent=self, pos=wx.Point(204, 148), size=wx.Size(14, 13), style=0)
        self.porcentajeMarcoText = wx.StaticText(id=wxID_PANEL1PORCENTAJEMARCOTEXT, label=_('Porcentaje de marco'), name='porcentajeMarcoText', parent=self, pos=wx.Point(15, 168), size=wx.Size(103, 13), style=0)
        self.porcentajeMarco = wx.TextCtrl(id=wxID_PANEL1PORCENTAJEMARCO, name='porcentajeMarco', parent=self, pos=wx.Point(143, 166), size=wx.Size(56, 21), style=0, value='20')
        self.porcentajeMarco.Bind(wx.EVT_TEXT, self.OnCambioPorcentaje, id=wxID_PANEL1PORCENTAJEMARCO)
        self.porcentajeMarco.SetForegroundColour(wx.Colour(100, 200, 0))
        self.porcentajeUnidadesText = wx.StaticText(id=wxID_PANEL1PORCENTAJEUNIDADESTEXT, label=_('%'), name='porcentajeUnidadesText', parent=self, pos=wx.Point(204, 168), size=wx.Size(11, 13), style=0)
        self.CaracteristicasLineaText = wx.StaticBox(id=wxID_CARACTERISTICASTEXT, label=_('Características'), name='CaracteristicasLineaText', parent=self, pos=wx.Point(320, 50), size=wx.Size(390, 145), style=0)
        self.CaracteristicasLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        if self.parent.parent.parent.panelDatosGenerales.anoConstruccionChoice.GetSelection() == 2 or self.parent.parent.parent.panelDatosGenerales.anoConstruccionChoice.GetSelection() == 3:
            listadoEstanqueidad = listadosWeb.listadoOpcionesEstanqueidadCTE
        else:
            listadoEstanqueidad = listadosWeb.listadoOpcionesEstanqueidad
        self.permeabilidadAireText = wx.StaticText(id=wxID_PANEL1PERMEABILIDADAIRE, label=_('Permeabilidad del hueco'), name='permeabilidadAireText', parent=self, pos=wx.Point(330, 69), size=wx.Size(125, 21), style=0)
        self.permeabilidadAireChoice = MiChoice(choices=listadoEstanqueidad, id=wxID_PANEL1PERMEABILIDADAIRECHOICE, name='permeabilidadAireChoice', parent=self, pos=wx.Point(500, 67), size=wx.Size(104, 21), style=0)
        self.permeabilidadAireChoice.SetSelection(0)
        self.permeabilidadAireChoice.Bind(wx.EVT_CHOICE, self.OnPermeabilidadAireChoice, id=wxID_PANEL1PERMEABILIDADAIRECHOICE)
        self.permeabilidadAire = wx.TextCtrl(id=wxID_PANEL1PERMEABILIDAD, name='permeabilidadAire', parent=self, pos=wx.Point(610, 67), size=wx.Size(50, 21), style=0, value='')
        self.permeabilidadAire.Enable(False)
        self.PermeabilidadVentanas()
        self.permeabilidadAireUnidadesText = wx.StaticText(id=wxID_PANEL1PERMEABILIDADAIREUNIDADES, label=_('m3/hm2'), name='permeabilidadAireUnidadesText', parent=self, pos=wx.Point(665, 69), size=wx.Size(42, 21), style=0)
        self.absortividadText = wx.StaticText(id=wxID_PANEL1PERMEABILIDADAIRE, label=_('Absortividad del marco'), name='permeabilidadAireText', parent=self, pos=wx.Point(330, 92), size=wx.Size(125, 21), style=0)
        self.absortividadBoton = wx.Button(id=wxID_PANEL1ABSORTIVIDADBOTON, label=_('α'), name='absortividadBoton', parent=self, pos=wx.Point(500, 91), size=wx.Size(104, 23), style=0)
        self.absortividadBoton.Bind(wx.EVT_BUTTON, self.OnAbsortividadBotonButton, id=wxID_PANEL1ABSORTIVIDADBOTON)
        self.absortividadMarco = wx.TextCtrl(id=wxID_PANEL1ABSORTIVIDADMARCO, name='absortividadMarco', parent=self, pos=wx.Point(610, 92), size=wx.Size(50, 21), style=0, value='0.75')
        self.absortividadMarco.SetForegroundColour(wx.Colour(100, 200, 0))
        self.absortividadMarco.Bind(wx.EVT_TEXT, self.onAbsortividadMarco, id=wxID_PANEL1ABSORTIVIDADMARCO)
        self.dispositivoProteccionSolarCheck = wx.CheckBox(id=wxID_PANEL1DISPOSITIVOCONTROLCHECK, label=_('Dispositivo de protección solar'), name='dispositivoProteccionSolarCheck', parent=self, pos=wx.Point(330, 121), size=wx.Size(168, 13), style=0)
        self.dispositivoProteccionSolarCheck.Bind(wx.EVT_CHECKBOX, self.dispositivoProteccionSolar, id=wxID_PANEL1DISPOSITIVOCONTROLCHECK)
        self.proteccionSolarBoton = wx.Button(id=wxID_PANEL1PROTECCIONSOLARBOTON, label=_('Dispositivo de protección solar'), name='proteccionSolarBoton', parent=self, pos=wx.Point(500, 118), size=wx.Size(160, 23), style=0)
        self.proteccionSolarBoton.Enable(False)
        self.proteccionSolarBoton.Bind(wx.EVT_BUTTON, self.OnProteccionSolarBotonButton, id=wxID_PANEL1PROTECCIONSOLARBOTON)
        self.obstaculosRemotosText = wx.StaticText(id=wxID_PANEL1PERMEABILIDADAIRE, label=_('Patrón de sombras'), name='obstaculosRemotosText', parent=self, pos=wx.Point(330, 148), size=wx.Size(125, 21), style=0)
        self.obstaculosRemotosChoice = MiChoice(choices=self.parent.parent.parent.nuevoListadoSombras, id=wxID_PANEL1OBSTACULOSREMOTOSCHOICE, name='permeabilidadAireChoice', parent=self, pos=wx.Point(500, 146), size=wx.Size(160, 23), style=0)
        self.obstaculosRemotosChoice.SetSelection(0)
        self.tieneContraventanaCheck = wx.CheckBox(id=wxID_PANEL1CONTRAVENTANACHECK, label=_('Doble ventana'), name='tieneContraventanaCheck', parent=self, pos=wx.Point(330, 173), size=wx.Size(145, 13), style=0)
        self.tieneContraventanaCheck.Show(True)
        self.tieneContraventanaCheck.Bind(wx.EVT_CHECKBOX, self.calcularCaracteristicasVidrio, id=wxID_PANEL1CONTRAVENTANACHECK)
        self.propiedadesTermicasText = wx.StaticText(id=wxID_PANEL1PROPIEDADESTERMICASTEXT, label=_('Propiedades térmicas'), name='propiedadesTermicasText', parent=self, pos=wx.Point(15, 223), size=wx.Size(118, 13), style=0)
        self.propiedadesTermicasText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.propiedadesTermicasChoice = MiChoice(choices=listadosWeb.listadoOpcionesPropiedadesTermicasHuecos, id=wxID_PANEL1PROPIEDADESTERMICASCHOICE, name='propiedadesTermicasChoice', parent=self, pos=wx.Point(143, 221), size=wx.Size(137, 21), style=0)
        self.propiedadesTermicasChoice.SetSelection(1)
        self.propiedadesTermicasChoice.Bind(wx.EVT_CHOICE, self.OnPropiedadesTermicasChoice, id=wxID_PANEL1PROPIEDADESTERMICASCHOICE)
        self.UvidrioRadio = wx.StaticText(id=wxID_PANEL1UVIDRIORADIO, label=_('U vidrio'), name='UvidrioRadio', parent=self, pos=wx.Point(15, 248), size=wx.Size(90, 13), style=0)
        self.UvidrioRadio.Show(False)
        self.Uvidrio = wx.TextCtrl(id=wxID_PANEL1UVIDRIO, name='Uvidrio', parent=self, pos=wx.Point(143, 246), size=wx.Size(56, 21), style=0, value='')
        self.Uvidrio.Bind(wx.EVT_TEXT, self.OnBorrarVidrioSeleccionado, id=wxID_PANEL1UVIDRIO)
        self.Uvidrio.Show(False)
        self.UvidrioUnidadesText = wx.StaticText(id=wxID_PANEL1UVIDRIOUNIDADESTEXT, label=_('W/m2K'), name='UvidrioUnidadesText', parent=self, pos=wx.Point(204, 246), size=wx.Size(34, 13), style=0)
        self.UvidrioUnidadesText.Show(False)
        self.GvidrioText = wx.StaticText(id=wxID_PANEL1GVIDRIOTEXT, label=_('g vidrio'), name='GvidrioText', parent=self, pos=wx.Point(15, 273), size=wx.Size(39, 13), style=0)
        self.GvidrioText.Show(False)
        self.Gvidrio = wx.TextCtrl(id=wxID_PANEL1GVIDIRO, name='Gvidrio', parent=self, pos=wx.Point(143, 271), size=wx.Size(56, 21), style=0, value='')
        self.Gvidrio.Bind(wx.EVT_TEXT, self.OnBorrarVidrioSeleccionado, id=wxID_PANEL1GVIDIRO)
        self.Gvidrio.Show(False)
        self.libreriaBotonVidrios = wx.BitmapButton(id=wxID_PANEL1LIBRERIABOTON, bitmap=wx.Bitmap(Directorio + '/Imagenes/ventana.ico', wx.BITMAP_TYPE_ANY), parent=self, pos=wx.Point(252, 258), size=wx.Size(23, 23), style=wx.BU_AUTODRAW)
        self.libreriaBotonVidrios.Bind(wx.EVT_BUTTON, self.OnLibreriaVidriosButton, id=wxID_PANEL1LIBRERIABOTON)
        self.libreriaBotonVidrios.Show(False)
        self.UmarcoText = wx.StaticText(id=wxID_PANEL1UMARCOTEXT, label=_('U marco'), name='UmarcoText', parent=self, pos=wx.Point(15, 298), size=wx.Size(43, 13), style=0)
        self.UmarcoText.Show(False)
        self.Umarco = wx.TextCtrl(id=wxID_PANEL1UMARCO, name='Umarco', parent=self, pos=wx.Point(143, 296), size=wx.Size(56, 21), style=0, value='')
        self.Umarco.Bind(wx.EVT_TEXT, self.OnBorrarMarcoSeleccionado, id=wxID_PANEL1UMARCO)
        self.Umarco.Show(False)
        self.UmarcoUnidadesText = wx.StaticText(id=wxID_PANEL1UMARCOUNIDADESTEXT, label=_('W/m2K'), name='UmarcoUnidadesText', parent=self, pos=wx.Point(204, 298), size=wx.Size(34, 13), style=0)
        self.UmarcoUnidadesText.Show(False)
        imageMarc = Directorio + '/Imagenes/marco.ico'
        imageMarcos = wx.Image(imageMarc, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.libreriaBotonMarcos = wx.BitmapButton(id=wxID_PANEL1LIBRERIABOTON2, bitmap=imageMarcos, parent=self, pos=wx.Point(252, 296), size=wx.Size(23, 23), style=wx.BU_AUTODRAW)
        self.libreriaBotonMarcos.Bind(wx.EVT_BUTTON, self.OnLibreriaMarcosButton, id=wxID_PANEL1LIBRERIABOTON2)
        self.libreriaBotonMarcos.Show(False)
        self.libreriaMaterialesText = wx.StaticText(id=wxID_PANEL1LIBRERIAMATERIALESTEXT, label=_('Vidrio seleccionado'), name='libreriaMarcosText', parent=self, pos=wx.Point(330, 260), size=wx.Size(102, 13), style=0)
        self.libreriaMaterialesText.Show(False)
        self.vidriosCuadro = wx.TextCtrl(id=wxID_PANEL1MATERIALESCHOICE, name='materialesCuadro', parent=self, pos=wx.Point(500, 258), size=wx.Size(200, 21), style=0, value='')
        self.vidriosCuadro.Show(False)
        self.vidriosCuadro.Enable(False)
        self.libreriaMarcosText = wx.StaticText(id=wxID_PANEL1LIBRERIAMARCOSTEXT, label=_('Marco seleccionado'), name='libreriaMarcosText', parent=self, pos=wx.Point(330, 298), size=wx.Size(100, 13), style=0)
        self.libreriaMarcosText.Show(False)
        self.marcosCuadro = wx.TextCtrl(id=wxID_PANEL1MARCOSCHOICE, name='marcosCuadro', parent=self, pos=wx.Point(500, 296), size=wx.Size(200, 21), style=0, value='')
        self.marcosCuadro.Show(False)
        self.marcosCuadro.Enable(False)
        self.tipoVidrioText = wx.StaticText(id=wxID_PANEL1TIPOVIDRIOTEXT, label=_('Tipo de vidrio'), name='tipoVidrioText', parent=self, pos=wx.Point(15, 248), size=wx.Size(68, 13), style=0)
        self.tipoVidrioText.Show(True)
        self.tipoVidrioChoice = MiChoice(choices=listadosWeb.listadoOpcionesVidrios, id=wxID_PANEL1TIPOVIDRIOCHOICE, name='tipoVidrioChoice', parent=self, pos=wx.Point(143, 246), size=wx.Size(137, 21), style=0)
        self.tipoVidrioChoice.SetSelection(1)
        self.tipoVidrioChoice.Show(True)
        self.tipoVidrioChoice.Bind(wx.EVT_CHOICE, self.calcularCaracteristicasVidrio, id=wxID_PANEL1TIPOVIDRIOCHOICE)
        self.tipoMarcoText = wx.StaticText(id=wxID_PANEL1TIPOMARCOTEXT, label=_('Tipo de marco'), name='tipoMarcoText', parent=self, pos=wx.Point(15, 273), size=wx.Size(71, 13), style=0)
        self.tipoMarcoText.Show(True)
        self.tipoMarcoChoice = MiChoice(choices=listadosWeb.listadoOpcionesMarcos, id=wxID_PANEL1TIPOMARCOCHIOCE, name='tipoMarcoChoice', parent=self, pos=wx.Point(143, 271), size=wx.Size(137, 21), style=0)
        self.tipoMarcoChoice.SetSelection(0)
        self.tipoMarcoChoice.Show(True)
        self.tipoMarcoChoice.Bind(wx.EVT_CHOICE, self.calcularCaracteristicasVidrio, id=wxID_PANEL1TIPOMARCOCHIOCE)
        self.UvidrioTextTablas = wx.StaticText(id=wxID_PANEL1UVIDRIOTEXTTABLAS, label=_('U vidrio'), name='UvidrioTextTablas', parent=self, pos=wx.Point(538, 248), size=wx.Size(56, 13), style=0)
        self.UvidrioTextTablas.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.UvidrioTablas = wx.TextCtrl(id=wxID_PANEL1UVIDRIOTABLAS, name='UvidrioTablas', parent=self, pos=wx.Point(610, 246), size=wx.Size(50, 21), style=0, value='')
        self.UvidrioTablas.Enable(False)
        self.UvidrioUnidadesTextTablas = wx.StaticText(id=wxID_PANEL1UVIDRIOUNIDADESTEXTTABLAS, label=_('W/m2K'), name='UvidrioUnidadesTextTablas', parent=self, pos=wx.Point(665, 248), size=wx.Size(34, 13), style=0)
        self.UvidrioUnidadesTextTablas.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.GvidrioTextTablas = wx.StaticText(id=wxID_PANEL1GVIDRIOTEXTTABLAS, label=_('g vidrio'), name='GvidrioTextTablas', parent=self, pos=wx.Point(538, 273), size=wx.Size(39, 13), style=0)
        self.GvidrioTextTablas.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.GvidrioTablas = wx.TextCtrl(id=wxID_PANEL1GVIDRIOTABLAS, name='GvidrioTablas', parent=self, pos=wx.Point(610, 271), size=wx.Size(50, 21), style=0, value='')
        self.GvidrioTablas.Enable(False)
        self.UmarcoTextTablas = wx.StaticText(id=wxID_PANEL1UMARCOTEXTTABLAS, label=_('U marco'), name='UmarcoTextTablas', parent=self, pos=wx.Point(538, 298), size=wx.Size(43, 13), style=0)
        self.UmarcoTextTablas.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.UmarcoTablas = wx.TextCtrl(id=wxID_PANEL1UMARCOTABLAS, name='Umarco', parent=self, pos=wx.Point(610, 296), size=wx.Size(50, 21), style=0, value='')
        self.UmarcoTablas.Enable(False)
        self.UmarcoUnidadesTextTablas = wx.StaticText(id=wxID_PANEL1UMARCOUNIDADESTEXTTABLAS, label=_('W/m2K'), name='UmarcoUnidadesTextTablas', parent=self, pos=wx.Point(665, 298), size=wx.Size(34, 13), style=0)
        self.UmarcoUnidadesTextTablas.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.UvidrioTextTablas.SetForegroundColour(wx.Colour(100, 100, 100))
        self.UvidrioUnidadesTextTablas.SetForegroundColour(wx.Colour(100, 100, 100))
        self.GvidrioTextTablas.SetForegroundColour(wx.Colour(100, 100, 100))
        self.UmarcoTextTablas.SetForegroundColour(wx.Colour(100, 100, 100))
        self.UmarcoUnidadesTextTablas.SetForegroundColour(wx.Colour(100, 100, 100))
        self.decripcionHueco.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1DECRIPCIONHUECO)
        self.orientacionHueco.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1ORIENTACIONHUECO)
        self.longitudMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1LONGIMURO)
        self.alturaMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1ALTURAMURO)
        self.multiMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1MULTIMURO)
        self.superficieHueco.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1SUPERFICIEHUECO)
        self.porcentajeMarco.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1PORCENTAJEMARCO)
        self.permeabilidadAire.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1PERMEABILIDAD)
        self.absortividadMarco.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1ABSORTIVIDADMARCO)
        self.Uvidrio.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1UVIDRIO)
        self.Gvidrio.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1GVIDIRO)
        self.Umarco.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1UMARCO)
        self.vidriosCuadro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1MATERIALESCHOICE)
        self.marcosCuadro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1MARCOSCHOICE)
        self.UvidrioTablas.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1UVIDRIOTABLAS)
        self.GvidrioTablas.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1GVIDRIOTABLAS)
        self.UmarcoTablas.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1UMARCOTABLAS)
        self.cerramientoChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1CERRAMIENTOCHOICE)
        self.permeabilidadAireChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1PERMEABILIDADAIRECHOICE)
        self.obstaculosRemotosChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1OBSTACULOSREMOTOSCHOICE)
        self.propiedadesTermicasChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1PROPIEDADESTERMICASCHOICE)
        self.tipoVidrioChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1TIPOVIDRIOCHOICE)
        self.tipoMarcoChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1TIPOMARCOCHIOCE)
        self.dispositivoProteccionSolarCheck.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1DISPOSITIVOCONTROLCHECK)
        self.tieneContraventanaCheck.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1CONTRAVENTANACHECK)

    def actualizaDiccionario(self):
        self.diccionario = {}
        self.diccionario['panelHuecos.decripcionHueco'] = self.decripcionHueco.GetValue()
        self.diccionario['panelHuecos.orientacionHueco'] = self.orientacionHueco.GetValue()
        self.diccionario['panelHuecos.longitudMuro'] = self.longitudMuro.GetValue()
        self.diccionario['panelHuecos.alturaMuro'] = self.alturaMuro.GetValue()
        self.diccionario['panelHuecos.multiMuro'] = self.multiMuro.GetValue()
        self.diccionario['panelHuecos.superficieHueco'] = self.superficieHueco.GetValue()
        self.diccionario['panelHuecos.porcentajeMarco'] = self.porcentajeMarco.GetValue()
        self.diccionario['panelHuecos.permeabilidadAire'] = self.permeabilidadAire.GetValue()
        self.diccionario['panelHuecos.absortividadMarco'] = self.absortividadMarco.GetValue()
        self.diccionario['panelHuecos.Uvidrio'] = self.Uvidrio.GetValue()
        self.diccionario['panelHuecos.Gvidrio'] = self.Gvidrio.GetValue()
        self.diccionario['panelHuecos.Umarco'] = self.Umarco.GetValue()
        self.diccionario['panelHuecos.vidriosCuadro'] = self.vidriosCuadro.GetValue()
        self.diccionario['panelHuecos.marcosCuadro'] = self.marcosCuadro.GetValue()
        self.diccionario['panelHuecos.UvidrioTablas'] = self.UvidrioTablas.GetValue()
        self.diccionario['panelHuecos.GvidrioTablas'] = self.GvidrioTablas.GetValue()
        self.diccionario['panelHuecos.UmarcoTablas'] = self.UmarcoTablas.GetValue()
        self.diccionario['panelHuecos.cerramientoChoice'] = self.cerramientoChoice.GetSelection()
        self.diccionario['panelHuecos.permeabilidadAireChoice'] = self.permeabilidadAireChoice.GetSelection()
        self.diccionario['panelHuecos.obstaculosRemotosChoice'] = self.obstaculosRemotosChoice.GetSelection()
        self.diccionario['panelHuecos.propiedadesTermicasChoice'] = self.propiedadesTermicasChoice.GetSelection()
        self.diccionario['panelHuecos.tipoVidrioChoice'] = self.tipoVidrioChoice.GetSelection()
        self.diccionario['panelHuecos.tipoMarcoChoice'] = self.tipoMarcoChoice.GetSelection()
        self.diccionario['panelHuecos.dispositivoProteccionSolarCheck'] = self.dispositivoProteccionSolarCheck.GetValue()
        self.diccionario['panelHuecos.tieneContraventanaCheck'] = self.tieneContraventanaCheck.GetValue()

    def cogeValoresDiccionario(self):
        self.decripcionHueco.SetValue(self.diccionario['panelHuecos.decripcionHueco'])
        self.orientacionHueco.SetValue(self.diccionario['panelHuecos.orientacionHueco'])
        self.longitudMuro.SetValue(self.diccionario['panelHuecos.longitudMuro'])
        self.alturaMuro.SetValue(self.diccionario['panelHuecos.alturaMuro'])
        self.multiMuro.SetValue(self.diccionario['panelHuecos.multiMuro'])
        self.superficieHueco.SetValue(self.diccionario['panelHuecos.superficieHueco'])
        self.porcentajeMarco.SetValue(self.diccionario['panelHuecos.porcentajeMarco'])
        self.permeabilidadAire.SetValue(self.diccionario['panelHuecos.permeabilidadAire'])
        self.absortividadMarco.SetValue(self.diccionario['panelHuecos.absortividadMarco'])
        self.Uvidrio.SetValue(self.diccionario['panelHuecos.Uvidrio'])
        self.Gvidrio.SetValue(self.diccionario['panelHuecos.Gvidrio'])
        self.Umarco.SetValue(self.diccionario['panelHuecos.Umarco'])
        self.vidriosCuadro.SetValue(self.diccionario['panelHuecos.vidriosCuadro'])
        self.marcosCuadro.SetValue(self.diccionario['panelHuecos.marcosCuadro'])
        self.UvidrioTablas.SetValue(self.diccionario['panelHuecos.UvidrioTablas'])
        self.GvidrioTablas.SetValue(self.diccionario['panelHuecos.GvidrioTablas'])
        self.UmarcoTablas.SetValue(self.diccionario['panelHuecos.UmarcoTablas'])
        self.cerramientoChoice.SetSelection(self.diccionario['panelHuecos.cerramientoChoice'])
        self.permeabilidadAireChoice.SetSelection(self.diccionario['panelHuecos.permeabilidadAireChoice'])
        self.obstaculosRemotosChoice.SetSelection(self.diccionario['panelHuecos.obstaculosRemotosChoice'])
        self.propiedadesTermicasChoice.SetSelection(self.diccionario['panelHuecos.propiedadesTermicasChoice'])
        self.tipoVidrioChoice.SetSelection(self.diccionario['panelHuecos.tipoVidrioChoice'])
        self.tipoMarcoChoice.SetSelection(self.diccionario['panelHuecos.tipoMarcoChoice'])
        self.dispositivoProteccionSolarCheck.SetValue(self.diccionario['panelHuecos.dispositivoProteccionSolarCheck'])
        self.tieneContraventanaCheck.SetValue(self.diccionario['panelHuecos.tieneContraventanaCheck'])
        self.OnPermeabilidadAireChoice(None)
        self.OnPropiedadesTermicasChoice(None)
        self.dispositivoProteccionSolar(None)
        return

    def dispositivoProteccionSolar(self, event):
        """
        Metodo: dispositivoProteccionSolar

        ARGUMENTOS:
                event:
        """
        if self.dispositivoProteccionSolarCheck.GetValue() == True:
            self.proteccionSolarBoton.Enable(True)
        else:
            self.proteccionSolarBoton.Enable(False)

    def OnLibreriaVidriosButton(self, event):
        """
        Metodo: OnLibreriaVidriosButton

        ARGUMENTOS:
                event:
        """
        self.dlg = menuVidrios.create(self.parent.parent.parent)
        self.dlg.ShowModal()
        if self.dlg.dev != False:
            self.Uvidrio.SetValue(str(self.dlg.dev[3]))
            self.Gvidrio.SetValue(str(self.dlg.dev[2]))
            self.vidriosCuadro.SetValue(str(self.dlg.dev[0]))
            self.mostrarVidrioSeleccionado()
        self.dlg.Destroy()

    def OnLibreriaMarcosButton(self, event):
        """
        Metodo: OnLibreriaMarcosButton

        ARGUMENTOS:
                event:
        """
        self.dlg = menuMarcos.create(self.parent.parent.parent)
        self.dlg.ShowModal()
        if self.dlg.dev != False:
            self.Umarco.SetValue(str(self.dlg.dev[3]))
            self.marcosCuadro.SetValue(str(self.dlg.dev[0]))
            self.absortividadMarco.SetValue(str(self.dlg.dev[2]))
            self.mostrarMarcoSeleccionado()
        self.dlg.Destroy()

    def OnBorrarVidrioSeleccionado(self, event):
        """
        Metodo: OnBorrarVidrioSeleccionado

        ARGUMENTOS:
                event:
        """
        self.vidriosCuadro.SetValue('')
        self.vidriosCuadro.Show(False)
        self.libreriaMaterialesText.Show(False)

    def OnBorrarMarcoSeleccionado(self, event):
        """
        Metodo: OnBorrarMarcoSeleccionado

        ARGUMENTOS:
                event:
        """
        self.marcosCuadro.SetValue('')
        self.marcosCuadro.Show(False)
        self.libreriaMarcosText.Show(False)

    def mostrarVidrioSeleccionado(self):
        """
        Metodo: mostrarVidrioSeleccionado

        """
        if self.vidriosCuadro.GetValue() != '':
            self.vidriosCuadro.Show(True)
            self.libreriaMaterialesText.Show(True)
        else:
            self.vidriosCuadro.Show(False)
            self.libreriaMaterialesText.Show(False)

    def mostrarMarcoSeleccionado(self):
        """
        Metodo: mostrarMarcoSeleccionado

        """
        if self.marcosCuadro.GetValue() != '':
            self.marcosCuadro.Show(True)
            self.libreriaMarcosText.Show(True)
        else:
            self.marcosCuadro.Show(False)
            self.libreriaMarcosText.Show(False)

    def calcularCaracteristicasVidrio(self, event):
        """
        Metodo: calcularCaracteristicasVidrio

        ARGUMENTOS:
                event:
        """
        Uvidrio = ''
        Gvidrio = ''
        Umarco = ''
        if self.propiedadesTermicasChoice.GetStringSelection() == 'Estimadas':
            caracteristicasHuecos = tablasValores.tablasValores('Hueco', None, [self.tipoVidrioChoice.GetStringSelection(),
             self.tipoMarcoChoice.GetStringSelection()], None)
            if float(self.porcentajeMarco.GetValue()) != 100.0:
                Uvidrio = caracteristicasHuecos.UCerramiento
                Gvidrio = caracteristicasHuecos.FSHueco
            else:
                Uvidrio = ''
                Gvidrio = ''
            Umarco = caracteristicasHuecos.UMarco
            if self.tieneContraventanaCheck.GetValue() == True:
                if float(self.porcentajeMarco.GetValue()) != 100.0:
                    Uvidrio = 1.0 / (1.0 / Uvidrio + 0.18)
                    Gvidrio = Gvidrio * 0.82
                Umarco = 1.0 / (1.0 / Umarco + 0.18)
        self.MostrarValoresGlobalesVidrios(Uvidrio, Gvidrio, Umarco)
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
        cerramientos = self.cargarCerramientos()
        self._init_vars_()
        self.bol = True
        self.elegirCerramientoSeleccionado(cerramientos)
        self.calcularCaracteristicasVidrio(None)
        self.actualizaDiccionario()
        return

    def cargarCerramientos(self):
        """
        Metodo: cargarCerramientos

        """
        cerramientos = []
        for i in self.parent.cerramientos:
            if i[len(i) - 1] == 'aire' and i[1] != 'Suelo':
                cerramientos.append(i[0])

        self.cerramientoChoice.AppendItems(cerramientos)
        return cerramientos

    def elegirCerramientoSeleccionado(self, cerramientos):
        """
        Metodo: elegirCerramientoSeleccionado

        ARGUMENTOS:
                 cerramientos):  ###Selecciono cerramiento que esta seleccionado en el arb:
        """
        sel = self.parent.arbolCerramientos.GetSelection()
        self.cerramientoChoice.SetSelection(-1)
        try:
            seleccionArbol = self.parent.arbolCerramientos.GetItemText(sel)
            if 'Hueco' in seleccionArbol or 'PT' in seleccionArbol:
                sel = self.parent.arbolCerramientos.GetItemParent(sel)
                seleccionArbol = self.parent.arbolCerramientos.GetItemText(sel)
            for cerr in cerramientos:
                if self.parent.arbolCerramientos.GetItemText(sel) == cerr:
                    self.cerramientoChoice.SetStringSelection(cerr)
                    self.OnCaracteristicasCerramiento(None)
                    return

        except:
            logging.info('Excepcion en: %s' % __name__)
            self.cerramientoChoice.SetSelection(-1)

        return

    def OnCaracteristicasCerramiento(self, event):
        """
        Metodo: OnCaracteristicasCerramiento

        ARGUMENTOS:
                 event:
        """
        cerramientoEscogido = self.cerramientoChoice.GetStringSelection()
        orientacionEscogida = ''
        for i in self.parent.cerramientos:
            tipoNombre = i[0]
            if tipoNombre == cerramientoEscogido:
                orientacionEscogida = i[5]
                patronSombrasEscogido = i[7]
                break

        self.orientacionHueco.SetValue(_(orientacionEscogida))
        self.Elto_Sombra = patronSombrasEscogido
        if self.obstaculosRemotosChoice.GetStringSelection() == 'Sin patrón':
            self.obstaculosRemotosChoice.SetStringSelection(patronSombrasEscogido)

    def modificarProteccionesSolares(self):
        """
        Metodo: modificarProteccionesSolares

        """
        if self.Voladizos_Si == True:
            self.Voladizo_H = self.alturaMuro.GetValue()
        if self.Retranqueos_Si == True:
            self.Retranqueo_H = self.alturaMuro.GetValue()
            self.Retranqueo_W = self.longitudMuro.GetValue()
        if self.Lucernarios_Si == True:
            self.Lucernarios_X = self.alturaMuro.GetValue()
            self.Lucernarios_Y = self.longitudMuro.GetValue()

    def _init_vars_(self):
        """
        Metodo: _init_vars_

        """
        self.Voladizo_L = ''
        self.Voladizo_D = ''
        self.Voladizo_H = ''
        self.Retranqueo_H = ''
        self.Retranqueo_W = ''
        self.Retranqueo_R = ''
        self.Lamas_Horizontales_BETA = [
         '', 0, 0]
        self.Lamas_Verticales_BETA = ['', 0, 0]
        self.Toldos_AnguloA = ''
        self.Toldos_OpacoA = False
        self.Toldos_TranslucidoA = False
        self.Toldos_AnguloB = ''
        self.Toldos_OpacoB = False
        self.Toldos_TranslucidoB = False
        self.Lucernarios_X = ''
        self.Lucernarios_Y = ''
        self.Lucernarios_Z = ''
        self.OtroInvierno = ''
        self.OtroVerano = ''
        self.Voladizos_Si = False
        self.Retranqueos_Si = False
        self.Lamas_Horizontales_Si = False
        self.Lamas_Verticales_Si = False
        self.Toldos_Si = False
        self.Lucernarios_Si = False
        self.Otro_Si = False
        self.matriz_absortividad = [
         [
          0.2, 0.3, ''],
         [
          0.3, 0.5, 0.7],
         [
          0.35, 0.55, 0.75],
         [
          0.5, 0.75, 0.92],
         [
          0.65, 0.8, 0.9],
         [
          0.4, 0.7, 0.88],
         [
          0.5, 0.8, 0.95],
         [
          0.4, 0.65, ''],
         [
          '', 0.96, '']]
        self.contador_fila_absortividad = 3
        self.contador_col_absortividad = 1
        self.Elto_Sombra = 'Sin Obstáculos Remotos'

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
            self.superficieHueco.SetValue(str(superficieTotal))
            self.bol = True
        except (ValueError, TypeError):
            pass

        self.modificarProteccionesSolares()

    def onAbsortividadMarco(self, event):
        """
        Metodo: onAbsortividadMarco

        ARGUMENTOS:
                event:
        """
        self.absortividadMarco.SetForegroundColour(wx.Colour(0, 0, 0))

    def OnCambioPorcentaje(self, event):
        """
        Metodo: OnCambioPorcentaje

        ARGUMENTOS:
                event:
        """
        self.porcentajeMarco.SetForegroundColour(wx.Colour(0, 0, 0))
        self.calcularCaracteristicasVidrio(None)
        return

    def BloquearDesbloquearConocidas(self):
        """
        Metodo: BloquearDesbloquearConocidas

        """
        if 'Conocidas' in self.propiedadesTermicasChoice.GetStringSelection():
            try:
                if float(self.porcentajeMarco.GetValue()) >= 100.0:
                    self.Uvidrio.Enable(False)
                    self.Uvidrio.SetValue('')
                    self.Gvidrio.Enable(False)
                    self.Gvidrio.SetValue('')
                    self.libreriaBotonVidrios.Enable(False)
                    self.vidriosCuadro.Show(False)
                else:
                    self.Uvidrio.Enable(True)
                    self.Gvidrio.Enable(True)
                    self.libreriaBotonVidrios.Enable(True)
                    self.vidriosCuadro.Show(True)
            except (ValueError, TypeError):
                self.Uvidrio.Enable(True)
                self.Gvidrio.Enable(True)
                self.libreriaBotonVidrios.Enable(True)
                self.vidriosCuadro.Show(True)

        else:
            try:
                if float(self.porcentajeMarco.GetValue()) >= 100.0:
                    self.tipoVidrioChoice.Enable(False)
                    self.tipoVidrioChoice.SetSelection(-1)
                    self.UvidrioTablas.SetValue('')
                    self.GvidrioTablas.SetValue('')
                else:
                    self.tipoVidrioChoice.Enable(True)
            except (ValueError, TypeError):
                self.tipoVidrioChoice.Enable(True)

    def MostrarValoresGlobalesVidrios(self, Uvidrio, Gvidrio, Umarco):
        """
        Metodo: MostrarValoresGlobalesVidrios

        ARGUMENTOS:
                 Uvidrio:
                Gvidrio:
                Umarco:
        """
        if 'Conocidas' in self.propiedadesTermicasChoice.GetStringSelection():
            try:
                if float(self.porcentajeMarco.GetValue()) >= 100.0:
                    self.Uvidrio.Enable(False)
                    self.Uvidrio.SetValue('')
                    self.Gvidrio.Enable(False)
                    self.Gvidrio.SetValue('')
                    self.libreriaBotonVidrios.Enable(False)
                    self.vidriosCuadro.Show(False)
                else:
                    self.Uvidrio.Enable(True)
                    self.Gvidrio.Enable(True)
                    self.libreriaBotonVidrios.Enable(True)
                    self.vidriosCuadro.Show(True)
            except (ValueError, TypeError):
                self.Uvidrio.Enable(True)
                self.Gvidrio.Enable(True)
                self.libreriaBotonVidrios.Enable(True)
                self.vidriosCuadro.Show(True)

            self.mostrarVidrioSeleccionado()
        else:
            try:
                if float(self.porcentajeMarco.GetValue()) >= 100.0:
                    self.UvidrioTablas.SetValue(Uvidrio)
                    self.GvidrioTablas.SetValue(Gvidrio)
                    self.UmarcoTablas.SetValue(str(round(float(Umarco), 2)))
                    self.tipoVidrioChoice.Enable(False)
                    self.tipoVidrioChoice.SetSelection(-1)
                else:
                    self.UvidrioTablas.SetValue(str(round(float(Uvidrio), 2)))
                    self.GvidrioTablas.SetValue(str(round(float(Gvidrio), 2)))
                    self.UmarcoTablas.SetValue(str(round(float(Umarco), 2)))
            except (ValueError, TypeError):
                self.tipoVidrioChoice.Enable(True)

    def OnPropiedadesTermicasChoice(self, event):
        """
        Metodo: OnPropiedadesTermicasChoice

        ARGUMENTOS:
                event):
        """
        if 'Conocidas' in self.propiedadesTermicasChoice.GetStringSelection():
            self.Gvidrio.Show(True)
            self.GvidrioText.Show(True)
            self.UvidrioUnidadesText.Show(True)
            self.Uvidrio.Show(True)
            self.UvidrioRadio.Show(True)
            self.UmarcoText.Show(True)
            self.Umarco.Show(True)
            self.UmarcoUnidadesText.Show(True)
            self.libreriaBotonVidrios.Show(True)
            self.libreriaBotonMarcos.Show(True)
            self.tipoVidrioText.Show(False)
            self.tipoVidrioChoice.Show(False)
            self.tipoMarcoText.Show(False)
            self.tipoMarcoChoice.Show(False)
            self.mostrarMarcoSeleccionado()
            self.UvidrioTextTablas.Show(False)
            self.UvidrioTablas.Show(False)
            self.UvidrioUnidadesTextTablas.Show(False)
            self.GvidrioTextTablas.Show(False)
            self.GvidrioTablas.Show(False)
            self.UmarcoTextTablas.Show(False)
            self.UmarcoTablas.Show(False)
            self.UmarcoUnidadesTextTablas.Show(False)
            self.calcularCaracteristicasVidrio(None)
            self.mostrarVidrioSeleccionado()
        else:
            self.Gvidrio.Show(False)
            self.GvidrioText.Show(False)
            self.UvidrioUnidadesText.Show(False)
            self.Uvidrio.Show(False)
            self.UvidrioRadio.Show(False)
            self.UmarcoText.Show(False)
            self.Umarco.Show(False)
            self.UmarcoUnidadesText.Show(False)
            self.libreriaMaterialesText.Show(False)
            self.vidriosCuadro.Show(False)
            self.libreriaMarcosText.Show(False)
            self.marcosCuadro.Show(False)
            self.libreriaBotonVidrios.Show(False)
            self.libreriaBotonMarcos.Show(False)
            self.tipoVidrioText.Show(True)
            self.tipoVidrioChoice.Show(True)
            self.tipoMarcoText.Show(True)
            self.tipoMarcoChoice.Show(True)
            self.tieneContraventanaCheck.Show(True)
            self.UvidrioTextTablas.Show(True)
            self.UvidrioTablas.Show(True)
            self.UvidrioUnidadesTextTablas.Show(True)
            self.GvidrioTextTablas.Show(True)
            self.GvidrioTablas.Show(True)
            self.UmarcoTextTablas.Show(True)
            self.UmarcoTablas.Show(True)
            self.UmarcoUnidadesTextTablas.Show(True)
            self.calcularCaracteristicasVidrio(None)
        return

    def PermeabilidadVentanas(self):
        """
        Metodo: PermeabilidadVentanas

        """
        if self.permeabilidadAireChoice.GetStringSelection() == 'Estanco':
            self.permeabilidadAire.SetValue('50')
        elif self.permeabilidadAireChoice.GetStringSelection() == 'Poco estanco':
            self.permeabilidadAire.SetValue('100')

    def OnPermeabilidadAireChoice(self, event):
        """
        Metodo: OnPermeabilidadAireChoice

        ARGUMENTOS:
                event:
        """
        if self.permeabilidadAireChoice.GetStringSelection() == 'Valor conocido':
            self.permeabilidadAire.Enable(True)
        else:
            self.permeabilidadAire.Enable(False)
        self.PermeabilidadVentanas()

    def OnAbsortividadBotonButton(self, event):
        """
        Metodo: OnAbsortividadBotonButton

        ARGUMENTOS:
                 event:
        """
        dlg = absortividad_cuadro.create(self)
        dlg.ShowModal()
        if dlg.dev == False:
            return
        self.absortividadMarco.SetValue(str(dlg.dev))

    def OnProteccionSolarBotonButton(self, event):
        """
        Metodo: OnProteccionSolarBotonButton

        ARGUMENTOS:
                 event:
        """
        dlg = eltos_sombras.create(self, self.parent.parent.parent)
        dlg.ShowModal()
        self.clickarProteccionSolar()

    def clickarProteccionSolar(self):
        """
        Metodo: clickarProteccionSolar

        """
        if self.Voladizos_Si == True or self.Retranqueos_Si == True or self.Lamas_Horizontales_Si == True or self.Lamas_Verticales_Si == True or self.Toldos_Si == True or self.Lucernarios_Si == True or self.Otro_Si == True:
            self.dispositivoProteccionSolarCheck.SetValue(True)
            self.proteccionSolarBoton.Enable(True)
        else:
            self.dispositivoProteccionSolarCheck.SetValue(False)
            self.proteccionSolarBoton.Enable(False)

    def cogerDatosSombras(self):
        """
        Metodo: cogerDatosSombras

        """
        sombras = []
        sombras.append(self.Voladizo_L)
        sombras.append(self.Voladizo_D)
        sombras.append(self.Voladizo_H)
        sombras.append(self.Retranqueo_H)
        sombras.append(self.Retranqueo_W)
        sombras.append(self.Retranqueo_R)
        sombras.append(self.Lamas_Horizontales_BETA)
        sombras.append(self.Lamas_Verticales_BETA)
        sombras.append(self.Toldos_AnguloA)
        sombras.append(self.Toldos_OpacoA)
        sombras.append(self.Toldos_TranslucidoA)
        sombras.append(self.Toldos_AnguloB)
        sombras.append(self.Toldos_OpacoB)
        sombras.append(self.Toldos_TranslucidoB)
        sombras.append(self.Lucernarios_X)
        sombras.append(self.Lucernarios_Y)
        sombras.append(self.Lucernarios_Z)
        sombras.append(self.Voladizos_Si)
        sombras.append(self.Retranqueos_Si)
        sombras.append(self.Lamas_Horizontales_Si)
        sombras.append(self.Lamas_Verticales_Si)
        sombras.append(self.Toldos_Si)
        sombras.append(self.Lucernarios_Si)
        sombras.append(self.Otro_Si)
        sombras.append([self.OtroInvierno, self.OtroVerano])
        return sombras

    def cargarDatosSombras(self, datos):
        """
        Metodo: cargarDatosSombras

        ARGUMENTOS:
                datos:
        """
        self.Voladizo_L = datos[0]
        self.Voladizo_D = datos[1]
        self.Voladizo_H = datos[2]
        self.Retranqueo_H = datos[3]
        self.Retranqueo_W = datos[4]
        self.Retranqueo_R = datos[5]
        self.Lamas_Horizontales_BETA = datos[6]
        self.Lamas_Verticales_BETA = datos[7]
        self.Toldos_AnguloA = datos[8]
        self.Toldos_OpacoA = datos[9]
        self.Toldos_TranslucidoA = datos[10]
        self.Toldos_AnguloB = datos[11]
        self.Toldos_OpacoB = datos[12]
        self.Toldos_TranslucidoB = datos[13]
        self.Lucernarios_X = datos[14]
        self.Lucernarios_Y = datos[15]
        self.Lucernarios_Z = datos[16]
        self.Voladizos_Si = datos[17]
        self.Retranqueos_Si = datos[18]
        self.Lamas_Horizontales_Si = datos[19]
        self.Lamas_Verticales_Si = datos[20]
        self.Toldos_Si = datos[21]
        self.Lucernarios_Si = datos[22]
        if datos[23] == True or datos[23] == False:
            self.Otro_Si = datos[23]
            self.OtroInvierno = datos[24][0]
            self.OtroVerano = datos[24][1]
        else:
            self.Otro_Si = False
            self.OtroInvierno = ''
            self.OtroVerano = ''

    def comprobarDatos(self):
        """
        Metodo: comprobarDatos

        """
        listaErrores = ''
        listaErrores2 = ''
        descripcion = self.decripcionHueco.GetValue()
        cerrAsociado = self.cerramientoChoice.GetStringSelection()
        superficie = self.superficieHueco.GetValue()
        porcMarco = self.porcentajeMarco.GetValue()
        permeabi = self.permeabilidadAireChoice.GetStringSelection()
        propi = self.propiedadesTermicasChoice.GetStringSelection()
        absor = self.absortividadMarco.GetValue()
        if ',' in superficie:
            superficie = superficie.replace(',', '.')
            self.superficieHueco.SetValue(superficie)
        try:
            float(superficie)
            if float(superficie) < 0:
                superficie = ''
        except (ValueError, TypeError):
            superficie = ''

        if ',' in porcMarco:
            porcMarco = porcMarco.replace(',', '.')
            self.porcentajeMarco.SetValue(superficie)
        if ',' in absor:
            absor = absor.replace(',', '.')
            self.absortividadMarco.SetValue(absor)
        try:
            float(porcMarco)
            if float(porcMarco) < 0:
                porcMarco = ''
            elif float(porcMarco) > 100.0:
                listaErrores2 += 'El porcentaje de marco no puede ser superior al 100 %\n'
        except (ValueError, TypeError):
            porcMarco = ''

        try:
            float(absor)
            if float(absor) < 0:
                absor = ''
            elif float(absor) > 1:
                listaErrores2 += 'La absortividad no puede ser superior a 1 \n'
        except (ValueError, TypeError):
            absor = ''

        if descripcion == '':
            listaErrores += 'nombre'
        if cerrAsociado == '':
            if listaErrores != '':
                listaErrores += ',  '
            listaErrores += 'cerramiento asociado'
        if superficie == '':
            if listaErrores != '':
                listaErrores += ',  '
            listaErrores += 'superficie'
        if porcMarco == '':
            if listaErrores != '':
                listaErrores += ',  '
            listaErrores += 'porcentaje de marco'
        if absor == '':
            if listaErrores != '':
                listaErrores += ',  '
            listaErrores += 'absortividad'
        if permeabi == 'Valor conocido':
            valorPermeab = self.permeabilidadAire.GetValue()
            if ',' in valorPermeab:
                valorPermeab = valorPermeab.replace(',', '.')
                self.permeabilidadAire.SetValue(valorPermeab)
            try:
                float(valorPermeab)
                if float(valorPermeab) < 0:
                    valorPermeab = ''
            except (ValueError, TypeError):
                valorPermeab = ''

            if valorPermeab == '':
                if listaErrores != '':
                    listaErrores += ',  '
                listaErrores += 'permeabilidad al aire'
        if propi == '':
            if listaErrores != '':
                listaErrores += ',  '
            listaErrores += 'propiedades térmicas'
        elif 'Conocidas' in propi:
            try:
                if float(porcMarco) < 100.0:
                    valor = self.Uvidrio.GetValue()
                    if ',' in valor:
                        valor = valor.replace(',', '.')
                        self.Uvidrio.SetValue(valor)
                    try:
                        float(valor)
                        if float(valor) < 0:
                            valor = ''
                    except (ValueError, TypeError):
                        valor = ''

                    if valor == '':
                        if listaErrores != '':
                            listaErrores += ',  '
                        listaErrores += 'U vidrio'
                    valor = self.Gvidrio.GetValue()
                    if ',' in valor:
                        valor = valor.replace(',', '.')
                        self.Gvidrio.SetValue(valor)
                    try:
                        float(valor)
                        if float(valor) < 0 or float(valor) > 1:
                            listaErrores2 += 'El factor solar del vidrio no puede ser mayor que 1 ni menor que 0\n'
                    except (ValueError, TypeError):
                        valor = ''

                    if valor == '':
                        if listaErrores != '':
                            listaErrores += ',  '
                        listaErrores += 'G vidrio'
                valor = self.Umarco.GetValue()
                if ',' in valor:
                    valor = valor.replace(',', '.')
                    self.Umarco.SetValue(valor)
                try:
                    float(valor)
                    if float(valor) < 0:
                        valor = ''
                except (ValueError, TypeError):
                    valor = ''

                if valor == '':
                    if listaErrores != '':
                        listaErrores += ',  '
                    listaErrores += 'U marco'
            except (ValueError, TypeError):
                valor = self.Uvidrio.GetValue()
                if ',' in valor:
                    valor = valor.replace(',', '.')
                    self.Uvidrio.SetValue(valor)
                try:
                    float(valor)
                    if float(valor) < 0:
                        valor = ''
                except (ValueError, TypeError):
                    valor = ''

                if valor == '':
                    if listaErrores != '':
                        listaErrores += ',  '
                    listaErrores += 'U vidrio'
                valor = self.Gvidrio.GetValue()
                if ',' in valor:
                    valor = valor.replace(',', '.')
                    self.Gvidrio.SetValue(valor)
                try:
                    float(valor)
                    if float(valor) < 0 or float(valor) > 1:
                        listaErrores2 += 'El factor solar del vidrio no puede ser mayor que 1 ni menor que \n'
                except:
                    logging.info('Excepcion en: %s' % __name__)
                    valor = ''

                if valor == '':
                    if listaErrores != '':
                        listaErrores += ',  '
                    listaErrores += 'G del vidrio'
                valor = self.Umarco.GetValue()
                if ',' in valor:
                    valor = valor.replace(',', '.')
                    self.Umarco.SetValue(valor)
                try:
                    float(valor)
                    if float(valor) < 0:
                        valor = ''
                except (ValueError, TypeError):
                    valor = ''

                if valor == '':
                    if listaErrores != '':
                        listaErrores += ',  '
                    listaErrores += 'U marco'

        elif 'Estimadas' in propi:
            valor = self.tipoVidrioChoice.GetStringSelection()
            try:
                if float(porcMarco) < 100.0:
                    if valor == '':
                        if listaErrores != '':
                            listaErrores += ',  '
                        listaErrores += 'tipo de vidrio'
            except (ValueError, TypeError):
                if valor == '':
                    if listaErrores != '':
                        listaErrores += ',  '
                    listaErrores += 'tipo de vidrio'

            valor = self.tipoMarcoChoice.GetStringSelection()
            if valor == '':
                if listaErrores != '':
                    listaErrores += ',  '
                listaErrores += 'tipo de marco'
        if listaErrores2 != '':
            listaErrores += '\n' + listaErrores2
        return listaErrores

    def cogerDatos(self):
        """
        Metodo: cogerDatos

        """
        listaErrores = self.comprobarDatos()
        if listaErrores != '':
            return listaErrores
        datos = []
        datos.append(self.decripcionHueco.GetValue())
        if 'Techo' == self.orientacionHueco.GetValue():
            datos.append(_('Lucernario'))
        else:
            datos.append(_('Hueco'))
        datos.append(self.superficieHueco.GetValue())
        datos.append(self.orientacionHueco.GetValue())
        datos.append(self.porcentajeMarco.GetValue())
        if self.dispositivoProteccionSolarCheck.GetValue() == True:
            aux = tablasValores.obtenerCorrectoresFactorSolar(self.orientacionHueco.GetValue(), self.Voladizo_L, self.Voladizo_D, self.Voladizo_H, self.Retranqueo_H, self.Retranqueo_W, self.Retranqueo_R, self.Lamas_Horizontales_BETA, self.Lamas_Verticales_BETA, self.Toldos_AnguloA, self.Toldos_OpacoA, self.Toldos_TranslucidoA, self.Toldos_AnguloB, self.Toldos_OpacoB, self.Toldos_TranslucidoB, self.Lucernarios_X, self.Lucernarios_Y, self.Lucernarios_Z, self.Voladizos_Si, self.Retranqueos_Si, self.Lamas_Horizontales_Si, self.Lamas_Verticales_Si, self.Lucernarios_Si, self.Toldos_Si, self.Otro_Si, self.OtroInvierno, self.OtroVerano)
            corrFS = aux[0]
        else:
            corrFS = [
             1.0, 1.0, 1.0]
        datos.append(corrFS)
        datos.append(self.cerramientoChoice.GetStringSelection())
        datos.append(self.permeabilidadAireChoice.GetStringSelection())
        datos.append(self.permeabilidadAire.GetValue())
        datos.append(self.absortividadMarco.GetValue())
        datos.append([self.contador_fila_absortividad, self.contador_col_absortividad])
        datos.append(self.dispositivoProteccionSolarCheck.GetValue())
        datos.append(self.cogerDatosSombras())
        datos.append(self.obstaculosRemotosChoice.GetStringSelection())
        datos.append(self.tieneContraventanaCheck.GetValue())
        datos.append(self.longitudMuro.GetValue())
        datos.append(self.alturaMuro.GetValue())
        datos.append(self.multiMuro.GetValue())
        datos.append(self.vidriosCuadro.GetValue())
        datos.append(self.marcosCuadro.GetValue())
        datos.append(self.Uvidrio.GetValue())
        datos.append(self.Gvidrio.GetValue())
        datos.append(self.Umarco.GetValue())
        datos.append(self.tipoVidrioChoice.GetStringSelection())
        datos.append(self.tipoMarcoChoice.GetStringSelection())
        subgrupo = self.subgrupoAlquePertenece(self.cerramientoChoice.GetStringSelection())
        datos.append(subgrupo)
        definicionPropiedadesTermicas = self.propiedadesTermicasChoice.GetStringSelection()
        return [
         datos, definicionPropiedadesTermicas]

    def subgrupoAlquePertenece(self, cerramiento):
        """
        Metodo: subgrupoAlquePertenece

        ARGUMENTOS:
                cerramiento:
        """
        for i in self.parent.cerramientos:
            if i[0] == cerramiento:
                subgrupo = i[-2]
                break

        return subgrupo

    def cargarDatos(self, datos):
        """
        Metodo: cargarDatos

        ARGUMENTOS:
                datos:
        """
        self.decripcionHueco.SetValue(datos.descripcion)
        self.superficieHueco.SetValue(datos.superficie)
        self.orientacionHueco.SetValue(_(datos.orientacion))
        self.porcentajeMarco.SetValue(datos.porcMarco)
        self.cerramientoChoice.SetStringSelection(datos.cerramientoAsociado)
        listadoEstanqueidad = self.permeabilidadAireChoice.GetItems()
        if datos.permeabilidadChoice not in listadoEstanqueidad:
            self.permeabilidadAireChoice.SetStringSelection('Valor conocido')
        else:
            self.permeabilidadAireChoice.SetStringSelection(datos.permeabilidadChoice)
        self.permeabilidadAire.SetValue(datos.permeabilidadValor)
        self.OnPermeabilidadAireChoice(None)
        self.dispositivoProteccionSolarCheck.SetValue(datos.tieneProteccionSolar)
        self.obstaculosRemotosChoice.SetStringSelection(datos.patronSombras)
        self.absortividadMarco.SetValue(str(datos.absortividadValor))
        self.contador_fila_absortividad = datos.absortividadPosiciones[0]
        self.contador_col_absortividad = datos.absortividadPosiciones[1]
        self.tieneContraventanaCheck.SetValue(datos.dobleVentana)
        self.longitudMuro.SetValue(datos.longitud)
        self.alturaMuro.SetValue(datos.altura)
        self.multiMuro.SetValue(datos.multiplicador)
        self.parent.panelElegirObjeto.definirHueco.SetValue(True)
        self.parent.panelElegirObjeto.noMostrarOpcionesContacto()
        colorSombra = wx.Color(240, 240, 240)
        colorNormal = wx.Color(255, 255, 255)
        self.parent.panelElegirObjeto.definirSuelo.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirCubierta.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirFachada.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirParticionInterior.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirHueco.SetBackgroundColour(colorSombra)
        self.parent.panelElegirObjeto.definirPuenteTermico.SetBackgroundColour(colorNormal)
        if datos.__tipo__ == 'HuecoConocidas':
            self.propiedadesTermicasChoice.SetStringSelection('Conocidas')
            self.Uvidrio.SetValue(str(datos.UvidrioConocido))
            self.Gvidrio.SetValue(str(datos.GvidrioConocido))
            self.Umarco.SetValue(str(datos.UmarcoConocido))
            self.vidriosCuadro.SetValue(datos.vidrioSeleccionado)
            self.marcosCuadro.SetValue(datos.marcoSeleccionado)
            self.mostrarVidrioSeleccionado()
            self.mostrarMarcoSeleccionado()
        else:
            self.propiedadesTermicasChoice.SetStringSelection('Estimadas')
            self.tipoVidrioChoice.SetStringSelection(datos.tipoVidrio)
            self.tipoMarcoChoice.SetStringSelection(datos.tipoMarco)
        self.OnPropiedadesTermicasChoice(None)
        self.cargarDatosSombras(datos.elementosProteccionSolar)
        self.dispositivoProteccionSolar(None)
        self.actualizaDiccionario()
        return