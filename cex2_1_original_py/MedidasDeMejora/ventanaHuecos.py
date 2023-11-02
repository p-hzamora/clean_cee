# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: MedidasDeMejora\ventanaHuecos.pyc
# Compiled at: 2015-02-23 10:53:16
"""
Modulo: ventanaHuecos.py

"""
from Instalaciones.comprobarCampos import Comprueba, Comprueba2
from miChoice import MiChoice
import Envolvente.eltos_sombras as eltos_sombras, directorios, Calculos.listadosWeb as listadosWeb, LibreriasCE3X.menuMarcos as menuMarcos, LibreriasCE3X.menuVidrios as menuVidrios, wx, logging
Directorio = directorios.BuscaDirectorios().Directorio

def create(parent, huecos):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
                huecos:
    """
    return Dialog1(parent, huecos)


wxID_DIALOG1, wxID_DIALOG1ACEPTARBOTON, wxID_DIALOG1CANCELARBOTON, wxID_DIALOG1CLASEVENTANASCHOICE, wxID_DIALOG1CLASEVENTANASRADIO, wxID_DIALOG1DESCRIPCION, wxID_DIALOG1DESCRIPCIONTEXT, wxID_DIALOG1GVIDRIO, wxID_DIALOG1GVIDRIOTEXT, wxID_DIALOG1HUECOSCHECK, wxID_DIALOG1LIBRERIAMARCOSCHOICE, wxID_DIALOG1LIBRERIAMARCOSRADIO, wxID_DIALOG1LIBRERIAVIDRIOSCHOICE, wxID_DIALOG1LIBRERIAVIDRIOSRADIO, wxID_DIALOG1LUCERNARIOSCHECK, wxID_DIALOG1PERMEABILIDAD, wxID_DIALOG1PERMEABILIDADAIRE, wxID_DIALOG1PERMEABILIDADAIREUNIDADESTEXT, wxID_DIALOG1PERMEABILIDADCHECK, wxID_DIALOG1PERMEABILIDADCHOICE, wxID_DIALOG1PERMEABILIDADRADIO, wxID_DIALOG1PERMEABILIDADUNIDADESTEXT, wxID_DIALOG1PORCENTAJEMARCOCHECK, wxID_DIALOG1PROPIEDADESMARCOCHECK, wxID_DIALOG1PROPIEDADESVIDRIOCHECK, wxID_DIALOG1TITULOTEXT, wxID_DIALOG1UMARCO, wxID_DIALOG1UMARCORADIO, wxID_DIALOG1UMARCOUNIDADESTEXT, wxID_DIALOG1UVIDRIO, wxID_DIALOG1UVIDRIORADIO, wxID_PANEL1PERMEABILIDAD, wxID_PANEL1PERMEABILIDADAIREUNIDADES, wxID_DIALOG1HUECOSNORTECHECK, wxID_DIALOG1HUECOSESTECHECK, wxID_DIALOG1HUECOSOESTECHECK, wxID_DIALOG1HUECOSSURCHECK, wxID_DIALOG1HUECOSNOROESTECHECK, wxID_DIALOG1HUECOSNORESTECHECK, wxID_DIALOG1HUECOSSUROESTECHECK, wxID_DIALOG1HUECOSSURESTECHECK, wxID_DIALOG1TIENECONTRAVENTANACHECK, wxID_DIALOG1TIPODOBLEVENTANACHOICE, wxID_DIALOG1DISPOPROTECCIONCHECK, wxID_DIALOG1DEFINIRPROTECCIONESBOTON, wxID_DIALOG1UVIDRIOUNIDADESTEXT, wxID_STATICBOX1, wxID_STATICBOX2, wxID_STATICBOX3, wxID_STATICBOX4, wxID_STATICBOX5, wxID_STATICBOX6, wxID_DOBLEVENTANATEXT, wxID_STATICBOX7, wxID_DIALOG1PERMEABILIDADTEXT, wxID_PANEL1LIBRERIABOTON, wxID_PANEL1LIBRERIAMARCOSBOTON = [ wx.NewId() for _init_ctrls in range(57) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo ventanaHuecos.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                 prnt:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(0, 0), size=wx.Size(572, 668), style=wx.DEFAULT_DIALOG_STYLE, title=_('Medida de mejora en los huecos'))
        self.SetClientSize(wx.Size(572, 668))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tituloText = wx.StaticText(id=wxID_DIALOG1TITULOTEXT, label=_('Medida de mejora en los huecos'), name='tituloText', parent=self, pos=wx.Point(24, 16), size=wx.Size(253, 18), style=0)
        self.tituloText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.tituloText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.descripcionText = wx.StaticText(id=wxID_DIALOG1DESCRIPCIONTEXT, label=_('Nombre'), name='descripcionText', parent=self, pos=wx.Point(30, 50), size=wx.Size(68, 13), style=0)
        self.descripcion = wx.TextCtrl(id=wxID_DIALOG1DESCRIPCION, name='descripcion', parent=self, pos=wx.Point(150, 48), size=wx.Size(407, 21), style=0, value='')
        self.staticBox1 = wx.StaticBox(id=wxID_STATICBOX1, label=_('Seleccionar las orientaciones dónde se mejoran los huecos'), name='staticBox1', parent=self, pos=wx.Point(15, 80), size=wx.Size(542, 80), style=0)
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.staticBox1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.huecosNorteCheck = wx.CheckBox(id=wxID_DIALOG1HUECOSNORTECHECK, label=_('Norte'), name='huecosNorteCheck', parent=self, pos=wx.Point(30, 105), size=wx.Size(70, 13), style=0)
        self.huecosNorteCheck.SetValue(False)
        self.huecosNorOesteCheck = wx.CheckBox(id=wxID_DIALOG1HUECOSNOROESTECHECK, label=_('NO'), name='huecosNorOesteCheck', parent=self, pos=wx.Point(30, 120), size=wx.Size(70, 13), style=0)
        self.huecosNorOesteCheck.SetValue(False)
        self.huecosNorEsteCheck = wx.CheckBox(id=wxID_DIALOG1HUECOSNORESTECHECK, label=_('NE'), name='huecosNorEsteCheck', parent=self, pos=wx.Point(30, 135), size=wx.Size(70, 13), style=0)
        self.huecosNorEsteCheck.SetValue(False)
        self.huecosSurCheck = wx.CheckBox(id=wxID_DIALOG1HUECOSSURCHECK, label=_('Sur'), name='huecosSurCheck', parent=self, pos=wx.Point(150, 105), size=wx.Size(70, 13), style=0)
        self.huecosSurCheck.SetValue(False)
        self.huecosSurOesteCheck = wx.CheckBox(id=wxID_DIALOG1HUECOSSUROESTECHECK, label=_('SO'), name='huecosSurOesteCheck', parent=self, pos=wx.Point(150, 120), size=wx.Size(70, 13), style=0)
        self.huecosSurOesteCheck.SetValue(False)
        self.huecosSurEsteCheck = wx.CheckBox(id=wxID_DIALOG1HUECOSSURESTECHECK, label=_('SE'), name='huecosSurEsteCheck', parent=self, pos=wx.Point(150, 135), size=wx.Size(70, 13), style=0)
        self.huecosSurEsteCheck.SetValue(False)
        self.lucernariosCheck = wx.CheckBox(id=wxID_DIALOG1LUCERNARIOSCHECK, label=_('Lucernarios'), name='lucernariosCheck', parent=self, pos=wx.Point(270, 105), size=wx.Size(70, 13), style=0)
        self.lucernariosCheck.SetValue(False)
        self.huecosOesteCheck = wx.CheckBox(id=wxID_DIALOG1HUECOSOESTECHECK, label=_('Oeste'), name='huecosOesteCheck', parent=self, pos=wx.Point(270, 120), size=wx.Size(70, 13), style=0)
        self.huecosOesteCheck.SetValue(False)
        self.huecosEsteCheck = wx.CheckBox(id=wxID_DIALOG1HUECOSESTECHECK, label=_('Este'), name='huecosEsteCheck', parent=self, pos=wx.Point(270, 135), size=wx.Size(70, 13), style=0)
        self.huecosEsteCheck.SetValue(False)
        self.staticBox2 = wx.StaticBox(id=wxID_STATICBOX2, label='                                                                          ', name='staticBox1', parent=self, pos=wx.Point(15, 168), size=wx.Size(542, 81), style=0)
        self.staticBox2.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.staticBox2.SetForegroundColour(wx.Colour(0, 64, 128))
        self.propiedadesVidrioCheck = wx.CheckBox(id=wxID_DIALOG1PROPIEDADESVIDRIOCHECK, label=_('Nuevos parámetros característicos del vidrio'), name='fuenteRadio', parent=self, pos=wx.Point(30, 168), size=wx.Size(250, 15), style=0)
        self.propiedadesVidrioCheck.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.propiedadesVidrioCheck.SetForegroundColour(wx.Colour(0, 64, 128))
        self.propiedadesVidrioCheck.SetValue(False)
        self.propiedadesVidrioCheck.Bind(wx.EVT_CHECKBOX, self.OnCambioCheckbox, id=wxID_DIALOG1PROPIEDADESVIDRIOCHECK)
        self.UvidrioRadio = wx.RadioButton(id=wxID_DIALOG1UVIDRIORADIO, label=_('Uvidrio'), name='UvidrioRadio', parent=self, pos=wx.Point(30, 193), size=wx.Size(81, 13), style=wx.RB_GROUP)
        self.UvidrioRadio.Bind(wx.EVT_RADIOBUTTON, self.OnPropiedadesVidrioRadiobutton, id=wxID_DIALOG1UVIDRIORADIO)
        self.UvidrioRadio.SetValue(True)
        self.UvidrioRadio.Show(False)
        self.libreriaVidriosRadio = wx.RadioButton(id=wxID_DIALOG1LIBRERIAVIDRIOSRADIO, label=_('Librería de vidrios'), name='libreriaVidriosRadio', parent=self, pos=wx.Point(30, 218), size=wx.Size(104, 13), style=0)
        self.libreriaVidriosRadio.Bind(wx.EVT_RADIOBUTTON, self.OnPropiedadesVidrioRadiobutton, id=wxID_DIALOG1LIBRERIAVIDRIOSRADIO)
        self.libreriaVidriosRadio.SetValue(False)
        self.libreriaVidriosRadio.Show(False)
        self.Uvidrio = wx.TextCtrl(id=wxID_DIALOG1UVIDRIO, name='Uvidrio', parent=self, pos=wx.Point(150, 191), size=wx.Size(56, 21), style=0, value='')
        self.Uvidrio.Show(False)
        self.UvidrioUnidadesText = wx.StaticText(id=wxID_DIALOG1UVIDRIOUNIDADESTEXT, label=_('W/m2K'), name='UmarcoUnidadesText', parent=self, pos=wx.Point(211, 193), size=wx.Size(34, 13), style=0)
        self.UvidrioUnidadesText.Show(False)
        self.GvidrioText = wx.StaticText(id=wxID_DIALOG1GVIDRIOTEXT, label=_('Gvidrio'), name='GvidrioText', parent=self, pos=wx.Point(282, 193), size=wx.Size(33, 13), style=0)
        self.GvidrioText.Show(False)
        self.Gvidrio = wx.TextCtrl(id=wxID_DIALOG1GVIDRIO, name='Gvidrio', parent=self, pos=wx.Point(325, 191), size=wx.Size(56, 21), style=0, value='')
        self.Gvidrio.Show(False)
        self.libreriaVidriosChoice = wx.Choice(choices=[], id=wxID_DIALOG1LIBRERIAVIDRIOSCHOICE, name='libreriaVidriosChoice', parent=self, pos=wx.Point(150, 216), size=wx.Size(235, 21), style=0)
        self.libreriaVidriosChoice.Show(False)
        self.libreriaBotonVidrios = wx.BitmapButton(id=wxID_PANEL1LIBRERIABOTON, bitmap=wx.Bitmap(Directorio + '/Imagenes/ventana.ico', wx.BITMAP_TYPE_ANY), parent=self, pos=wx.Point(390, 215), size=wx.Size(23, 23), style=wx.BU_AUTODRAW)
        self.libreriaBotonVidrios.Bind(wx.EVT_BUTTON, self.OnLibreriaVidriosButton, id=wxID_PANEL1LIBRERIABOTON)
        self.libreriaBotonVidrios.Show(False)
        self.staticBox3 = wx.StaticBox(id=wxID_STATICBOX3, label='                                                                            ', name='staticBox1', parent=self, pos=wx.Point(15, 257), size=wx.Size(542, 76), style=0)
        self.staticBox3.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.staticBox3.SetForegroundColour(wx.Colour(0, 64, 128))
        self.permeabilidadCheck = wx.CheckBox(id=wxID_DIALOG1PERMEABILIDADCHECK, label=_('Nueva permeabilidad del aire del hueco'), name='permeabilidadCheck', parent=self, pos=wx.Point(30, 257), size=wx.Size(210, 13), style=0)
        self.permeabilidadCheck.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.permeabilidadCheck.SetValue(False)
        self.permeabilidadCheck.SetForegroundColour(wx.Colour(0, 64, 128))
        self.permeabilidadCheck.Bind(wx.EVT_CHECKBOX, self.OnCambioCheckbox, id=wxID_DIALOG1PERMEABILIDADCHECK)
        self.claseVentanasRadio = wx.RadioButton(id=wxID_DIALOG1CLASEVENTANASRADIO, label=_('Clase de ventanas'), name='claseVentanasRadio', parent=self, pos=wx.Point(30, 282), size=wx.Size(118, 13), style=wx.RB_GROUP)
        self.claseVentanasRadio.Bind(wx.EVT_RADIOBUTTON, self.OnPermeabilidadRadiobutton, id=wxID_DIALOG1CLASEVENTANASRADIO)
        self.claseVentanasRadio.SetValue(True)
        self.claseVentanasRadio.Show(False)
        self.permeabilidadRadio = wx.RadioButton(id=wxID_DIALOG1PERMEABILIDADRADIO, label=_('Permeabilidad'), name='permeabilidadRadio', parent=self, pos=wx.Point(30, 307), size=wx.Size(81, 13), style=0)
        self.permeabilidadRadio.Bind(wx.EVT_RADIOBUTTON, self.OnPermeabilidadRadiobutton, id=wxID_DIALOG1PERMEABILIDADRADIO)
        self.permeabilidadRadio.SetValue(False)
        self.permeabilidadRadio.Show(False)
        self.claseVentanasChoice = MiChoice(choices=listadosWeb.listaClasesVentanas, id=wxID_DIALOG1CLASEVENTANASCHOICE, name='claseVentanasChoice', parent=self, pos=wx.Point(150, 280), size=wx.Size(140, 21), style=0)
        self.claseVentanasChoice.SetSelection(1)
        self.claseVentanasChoice.Show(False)
        self.permeabilidadChoice = MiChoice(choices=listadosWeb.listadoOpcionesEstanqueidad, id=wxID_DIALOG1PERMEABILIDADCHOICE, name='permeabilidadChoice', parent=self, pos=wx.Point(150, 305), size=wx.Size(140, 21), style=0)
        self.permeabilidadChoice.SetSelection(0)
        self.permeabilidadChoice.Bind(wx.EVT_CHOICE, self.OnPermeabilidadAireChoice, id=wxID_DIALOG1PERMEABILIDADCHOICE)
        self.permeabilidadChoice.Show(False)
        self.permeabilidadAire = wx.TextCtrl(id=wxID_PANEL1PERMEABILIDAD, name='permeabilidadAire', parent=self, pos=wx.Point(295, 305), size=wx.Size(56, 21), style=0, value='')
        self.permeabilidadAire.Show(False)
        self.permeabilidadAireUnidadesText = wx.StaticText(id=wxID_PANEL1PERMEABILIDADAIREUNIDADES, label=_('m3/hm2 a 100Pa'), name='permeabilidadAireUnidadesText', parent=self, pos=wx.Point(356, 307), size=wx.Size(140, 21), style=0)
        self.permeabilidadAireUnidadesText.Show(False)
        self.staticBox4 = wx.StaticBox(id=wxID_STATICBOX4, label='                                                       ', name='staticBox1', parent=self, pos=wx.Point(15, 341), size=wx.Size(542, 56), style=0)
        self.staticBox4.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.staticBox4.SetForegroundColour(wx.Colour(0, 64, 128))
        self.porcentajeMarcoCheck = wx.CheckBox(id=wxID_DIALOG1PORCENTAJEMARCOCHECK, label=_('Nuevo porcentaje de marco'), name='porcentajeMarcoCheck', parent=self, pos=wx.Point(30, 341), size=wx.Size(160, 13), style=0)
        self.porcentajeMarcoCheck.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.porcentajeMarcoCheck.SetForegroundColour(wx.Colour(0, 64, 128))
        self.porcentajeMarcoCheck.SetValue(False)
        self.porcentajeMarcoCheck.Bind(wx.EVT_CHECKBOX, self.OnCambioCheckbox, id=wxID_DIALOG1PORCENTAJEMARCOCHECK)
        self.porcentajeMarcoText = wx.StaticText(id=wxID_DIALOG1PERMEABILIDADTEXT, label=_('Porcentaje de marco'), name='porcentajeMarco', parent=self, pos=wx.Point(30, 366), size=wx.Size(108, 13), style=0)
        self.porcentajeMarcoText.Show(False)
        self.porcentajeMarco = wx.TextCtrl(id=wxID_DIALOG1PERMEABILIDAD, name='permeabilidad', parent=self, pos=wx.Point(150, 364), size=wx.Size(56, 21), style=0, value='')
        self.porcentajeMarco.Show(False)
        self.porcentajeMarcoUnidadesText = wx.StaticText(id=wxID_DIALOG1PERMEABILIDADUNIDADESTEXT, label=_('%'), name='porcentajeMarco', parent=self, pos=wx.Point(211, 366), size=wx.Size(11, 13), style=0)
        self.porcentajeMarcoUnidadesText.Show(False)
        self.staticBox5 = wx.StaticBox(id=wxID_STATICBOX5, label='                                                       ', name='staticBox1', parent=self, pos=wx.Point(15, 405), size=wx.Size(542, 81), style=0)
        self.staticBox5.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.staticBox5.SetForegroundColour(wx.Colour(0, 64, 128))
        self.propiedadesMarcoCheck = wx.CheckBox(id=wxID_DIALOG1PROPIEDADESMARCOCHECK, label=_('Nuevas propiedades de marco'), name='propiedadesMarcoCheck', parent=self, pos=wx.Point(30, 405), size=wx.Size(170, 13), style=0)
        self.propiedadesMarcoCheck.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.propiedadesMarcoCheck.SetForegroundColour(wx.Colour(0, 64, 128))
        self.propiedadesMarcoCheck.SetValue(False)
        self.propiedadesMarcoCheck.Bind(wx.EVT_CHECKBOX, self.OnCambioCheckbox, id=wxID_DIALOG1PROPIEDADESMARCOCHECK)
        self.UmarcoRadio = wx.RadioButton(id=wxID_DIALOG1UMARCORADIO, label=_('Umarco'), name='UmarcoRadio', parent=self, pos=wx.Point(30, 430), size=wx.Size(81, 13), style=wx.RB_GROUP)
        self.UmarcoRadio.Bind(wx.EVT_RADIOBUTTON, self.OnPropiedadesMarcoRadiobutton, id=wxID_DIALOG1UMARCORADIO)
        self.UmarcoRadio.SetValue(True)
        self.UmarcoRadio.Show(False)
        self.libreriaMarcosRadio = wx.RadioButton(id=wxID_DIALOG1LIBRERIAMARCOSRADIO, label=_('Librería de marcos'), name='libreriaMarcosRadio', parent=self, pos=wx.Point(30, 455), size=wx.Size(104, 13), style=0)
        self.libreriaMarcosRadio.Bind(wx.EVT_RADIOBUTTON, self.OnPropiedadesMarcoRadiobutton, id=wxID_DIALOG1LIBRERIAMARCOSRADIO)
        self.libreriaMarcosRadio.SetValue(False)
        self.libreriaMarcosRadio.Show(False)
        self.Umarco = wx.TextCtrl(id=wxID_DIALOG1UMARCO, name='Umarco', parent=self, pos=wx.Point(150, 428), size=wx.Size(56, 21), style=0, value='')
        self.Umarco.Show(False)
        self.UmarcoUnidadesText = wx.StaticText(id=wxID_DIALOG1UMARCOUNIDADESTEXT, label=_('W/m2K'), name='UmarcoUnidadesText', parent=self, pos=wx.Point(211, 430), size=wx.Size(34, 13), style=0)
        self.UmarcoUnidadesText.Show(False)
        self.libreriaMarcosChoice = wx.Choice(choices=[], id=wxID_DIALOG1LIBRERIAMARCOSCHOICE, name='libreriaMarcosChoice', parent=self, pos=wx.Point(150, 453), size=wx.Size(235, 21), style=0)
        self.libreriaMarcosChoice.Show(False)
        self.libreriaBotonMarcos = wx.BitmapButton(id=wxID_PANEL1LIBRERIAMARCOSBOTON, bitmap=wx.Bitmap(Directorio + '/Imagenes/marco.ico', wx.BITMAP_TYPE_ANY), parent=self, pos=wx.Point(390, 452), size=wx.Size(23, 23), style=wx.BU_AUTODRAW)
        self.libreriaBotonMarcos.Bind(wx.EVT_BUTTON, self.OnLibreriaMarcosButton, id=wxID_PANEL1LIBRERIAMARCOSBOTON)
        self.libreriaBotonMarcos.Show(False)
        self.staticBox6 = wx.StaticBox(id=wxID_STATICBOX6, label='                                                ', name='staticBox1', parent=self, pos=wx.Point(15, 494), size=wx.Size(542, 56), style=0)
        self.staticBox6.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.staticBox6.SetForegroundColour(wx.Colour(0, 64, 128))
        self.tieneDobleVentanaCheck = wx.CheckBox(id=wxID_DIALOG1TIENECONTRAVENTANACHECK, label=_('Definir doble ventana'), name='tieneDobleVentanaCheck', parent=self, pos=wx.Point(30, 494), size=wx.Size(130, 13), style=0)
        self.tieneDobleVentanaCheck.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.tieneDobleVentanaCheck.SetForegroundColour(wx.Colour(0, 64, 128))
        self.tieneDobleVentanaCheck.SetValue(False)
        self.tieneDobleVentanaCheck.Bind(wx.EVT_CHECKBOX, self.OnCambioCheckbox, id=wxID_DIALOG1TIENECONTRAVENTANACHECK)
        self.dobleVentanaText = wx.StaticText(id=wxID_DOBLEVENTANATEXT, label=_('Características doble ventana'), name='dobleVentanaText', parent=self, pos=wx.Point(30, 519), size=wx.Size(193, 13), style=0)
        self.dobleVentanaText.Show(False)
        self.tipoDobleVentanaChoice = MiChoice(choices=listadosWeb.listaOpcionesDobleVentana, id=wxID_DIALOG1TIPODOBLEVENTANACHOICE, name='tipoDobleVentanaChoice', parent=self, pos=wx.Point(200, 517), size=wx.Size(140, 21), style=0)
        self.tipoDobleVentanaChoice.SetSelection(0)
        self.tipoDobleVentanaChoice.Show(False)
        self.staticBox7 = wx.StaticBox(id=wxID_STATICBOX7, label='                                                        ', name='staticBox1', parent=self, pos=wx.Point(15, 558), size=wx.Size(542, 56), style=0)
        self.staticBox7.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.staticBox7.SetForegroundColour(wx.Colour(0, 64, 128))
        self.dipositivosProteccionCheck = wx.CheckBox(id=wxID_DIALOG1DISPOPROTECCIONCHECK, label=_('Definir dispositivos de protección solar'), name='dipositivosProteccionCheck', parent=self, pos=wx.Point(30, 558), size=wx.Size(220, 13), style=0)
        self.dipositivosProteccionCheck.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.dipositivosProteccionCheck.SetForegroundColour(wx.Colour(0, 64, 128))
        self.dipositivosProteccionCheck.SetValue(False)
        self.dipositivosProteccionCheck.Bind(wx.EVT_CHECKBOX, self.OnCambioCheckbox, id=wxID_DIALOG1DISPOPROTECCIONCHECK)
        self.definirProteccionesBoton = wx.Button(id=wxID_DIALOG1DEFINIRPROTECCIONESBOTON, label=_('Definir protecciones solares'), name='aceptarBoton', parent=self, pos=wx.Point(30, 581), size=wx.Size(140, 21), style=0)
        self.definirProteccionesBoton.Bind(wx.EVT_BUTTON, self.onDefinirProteccionesBoton, id=wxID_DIALOG1DEFINIRPROTECCIONESBOTON)
        self.definirProteccionesBoton.Show(False)
        self.tempText = wx.StaticText(id=-1, label=_(''), name='tempText', parent=self, pos=wx.Point(200, 581), size=wx.Size(1, 1), style=0)
        self.tempText.Show(False)
        self.aceptarBoton = wx.Button(id=wxID_DIALOG1ACEPTARBOTON, label=_('Aceptar'), name='aceptarBoton', parent=self, pos=wx.Point(15, 632), size=wx.Size(75, 23), style=0)
        self.aceptarBoton.Bind(wx.EVT_BUTTON, self.onAceptarBoton, id=wxID_DIALOG1ACEPTARBOTON)
        self.cancelarBoton = wx.Button(id=wxID_DIALOG1CANCELARBOTON, label=_('Cancelar'), name='cancelarBoton', parent=self, pos=wx.Point(105, 632), size=wx.Size(75, 23), style=0)
        self.cancelarBoton.Bind(wx.EVT_BUTTON, self.onCancelarBoton, id=wxID_DIALOG1CANCELARBOTON)

    def __init__(self, parent, huecos):
        """
        Constructor de la clase

        ARGUMENTOS:
                 parent :
                 huecos:
        """
        self.parent = parent
        self._init_ctrls(parent)
        self.dev = False
        self.cargarOpcionesLibreria()
        orientaciones = [
         'Norte', 'NO', 'NE', 'Sur', 'SO', 'SE', 'Techo', 
         'Oeste', 
         'Este']
        for i in huecos:
            if i.orientacion in orientaciones:
                a = orientaciones.index(i.orientacion)
                orientaciones[a] = 0

        if orientaciones[0] == 0:
            self.huecosNorteCheck.SetValue(True)
        else:
            self.huecosNorteCheck.Enable(False)
        if orientaciones[1] == 0:
            self.huecosNorOesteCheck.SetValue(True)
        else:
            self.huecosNorOesteCheck.Enable(False)
        if orientaciones[2] == 0:
            self.huecosNorEsteCheck.SetValue(True)
        else:
            self.huecosNorEsteCheck.Enable(False)
        if orientaciones[3] == 0:
            self.huecosSurCheck.SetValue(True)
        else:
            self.huecosSurCheck.Enable(False)
        if orientaciones[4] == 0:
            self.huecosSurOesteCheck.SetValue(True)
        else:
            self.huecosSurOesteCheck.Enable(False)
        if orientaciones[5] == 0:
            self.huecosSurEsteCheck.SetValue(True)
        else:
            self.huecosSurEsteCheck.Enable(False)
        if orientaciones[6] == 0:
            self.lucernariosCheck.SetValue(True)
        else:
            self.lucernariosCheck.Enable(False)
        if orientaciones[7] == 0:
            self.huecosOesteCheck.SetValue(True)
        else:
            self.huecosOesteCheck.Enable(False)
        if orientaciones[8] == 0:
            self.huecosEsteCheck.SetValue(True)
        else:
            self.huecosEsteCheck.Enable(False)
        self._init_vars()

    def _init_vars(self):
        """
        Metodo: _init_vars

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
        self.Elto_Sombra = 'Sin Obstáculos Remotos'

    def OnLibreriaMarcosButton(self, event):
        """
        Metodo: OnLibreriaMarcosButton

        ARGUMENTOS:
                event:
        """
        self.dlg = menuMarcos.create(self.parent.parent.parent)
        self.dlg.ShowModal()
        if self.dlg.dev != False:
            nombreMarco = str(self.dlg.dev[0])
            listaMarco = self.libreriaMarcosChoice.GetItems()
            listaMarco.append(nombreMarco)
            self.libreriaMarcosChoice.SetItems(listaMarco)
            self.libreriaMarcosChoice.SetStringSelection(nombreMarco)
        self.dlg.Destroy()

    def OnLibreriaVidriosButton(self, event):
        """
        Metodo: OnLibreriaVidriosButton

        ARGUMENTOS:
                event:
        """
        self.dlg = menuVidrios.create(self.parent.parent.parent)
        self.dlg.ShowModal()
        if self.dlg.dev != False:
            nombreVidrio = str(self.dlg.dev[0])
            listaHuecos = self.libreriaVidriosChoice.GetItems()
            listaHuecos.append(nombreVidrio)
            self.libreriaVidriosChoice.SetItems(listaHuecos)
            self.libreriaVidriosChoice.SetStringSelection(nombreVidrio)
        self.dlg.Destroy()

    def onDefinirProteccionesBoton(self, event):
        """
        Metodo: onDefinirProteccionesBoton

        ARGUMENTOS:
                event:
        """
        dlg = eltos_sombras.create(self, self.parent.parent.parent.parent)
        dlg.ShowModal()

    def OnPropiedadesMarcoRadiobutton(self, event):
        """
        Metodo: OnPropiedadesMarcoRadiobutton

        ARGUMENTOS:
                event:
        """
        if self.UmarcoRadio.GetValue() == True:
            self.Umarco.Show(True)
            self.UmarcoUnidadesText.Show(True)
            self.libreriaMarcosChoice.Show(False)
            self.libreriaBotonMarcos.Show(False)
        else:
            self.Umarco.Show(False)
            self.UmarcoUnidadesText.Show(False)
            self.libreriaMarcosChoice.Show(True)
            self.libreriaBotonMarcos.Show(True)

    def OnPermeabilidadRadiobutton(self, event):
        """
        Metodo: OnPermeabilidadRadiobutton

        ARGUMENTOS:
                event:
        """
        if self.claseVentanasRadio.GetValue() == True:
            self.claseVentanasChoice.Show(True)
            self.permeabilidadChoice.Show(False)
            self.permeabilidadAire.Show(False)
            self.permeabilidadAireUnidadesText.Show(False)
        else:
            self.claseVentanasChoice.Show(False)
            self.permeabilidadChoice.Show(True)
            self.permeabilidadAire.Show(True)
            self.permeabilidadAireUnidadesText.Show(True)
            self.OnPermeabilidadAireChoice(event)

    def PermeabilidadVentanas(self):
        """
        Metodo: PermeabilidadVentanas

        """
        if self.permeabilidadChoice.GetStringSelection() == 'Estanco':
            self.permeabilidadAire.SetValue('50')
        elif self.permeabilidadChoice.GetStringSelection() == 'Poco estanco':
            self.permeabilidadAire.SetValue('100')

    def OnPropiedadesVidrioRadiobutton(self, event):
        """
        Metodo: OnPropiedadesVidrioRadiobutton

        ARGUMENTOS:
                event:
        """
        if self.UvidrioRadio.GetValue() == True:
            self.Uvidrio.Show(True)
            self.Gvidrio.Show(True)
            self.libreriaVidriosChoice.Show(False)
            self.libreriaBotonVidrios.Show(False)
            self.GvidrioText.Show(True)
            self.UvidrioUnidadesText.Show(True)
        else:
            self.Uvidrio.Show(False)
            self.Gvidrio.Show(False)
            self.libreriaVidriosChoice.Show(True)
            self.libreriaBotonVidrios.Show(True)
            self.GvidrioText.Show(False)
            self.UvidrioUnidadesText.Show(False)

    def OnCambioCheckbox(self, event):
        """
        Metodo: OnCambioCheckbox

        ARGUMENTOS:
                event:
        """
        if self.propiedadesVidrioCheck.GetValue() == True:
            self.UvidrioRadio.Show(True)
            self.libreriaVidriosRadio.Show(True)
            self.OnPropiedadesVidrioRadiobutton(event)
        else:
            self.UvidrioRadio.Show(False)
            self.libreriaVidriosRadio.Show(False)
            self.Uvidrio.Show(False)
            self.Gvidrio.Show(False)
            self.GvidrioText.Show(False)
            self.UvidrioUnidadesText.Show(False)
            self.libreriaVidriosChoice.Show(False)
            self.libreriaBotonVidrios.Show(False)
        if self.permeabilidadCheck.GetValue() == True:
            self.claseVentanasRadio.Show(True)
            self.permeabilidadRadio.Show(True)
            self.OnPermeabilidadRadiobutton(event)
        else:
            self.claseVentanasRadio.Show(False)
            self.permeabilidadRadio.Show(False)
            self.claseVentanasChoice.Show(False)
            self.permeabilidadChoice.Show(False)
            self.permeabilidadAire.Show(False)
            self.permeabilidadAireUnidadesText.Show(False)
        if self.porcentajeMarcoCheck.GetValue() == True:
            self.porcentajeMarco.Show(True)
            self.porcentajeMarcoUnidadesText.Show(True)
            self.porcentajeMarcoText.Show(True)
        else:
            self.porcentajeMarco.Show(False)
            self.porcentajeMarcoUnidadesText.Show(False)
            self.porcentajeMarcoText.Show(False)
        if self.propiedadesMarcoCheck.GetValue() == True:
            self.UmarcoRadio.Show(True)
            self.libreriaMarcosRadio.Show(True)
            self.OnPropiedadesMarcoRadiobutton(event)
        else:
            self.UmarcoRadio.Show(False)
            self.libreriaMarcosRadio.Show(False)
            self.Umarco.Show(False)
            self.UmarcoUnidadesText.Show(False)
            self.libreriaMarcosChoice.Show(False)
            self.libreriaBotonMarcos.Show(False)
        if self.tieneDobleVentanaCheck.GetValue() == True:
            self.tipoDobleVentanaChoice.Show(True)
            self.dobleVentanaText.Show(True)
        else:
            self.tipoDobleVentanaChoice.Show(False)
            self.dobleVentanaText.Show(False)
        if self.dipositivosProteccionCheck.GetValue() == True:
            self.definirProteccionesBoton.Show(True)
            self.tempText.Show(True)
        else:
            self.definirProteccionesBoton.Show(False)
            self.tempText.Show(False)

    def cargarOpcionesLibreria(self):
        """
        Metodo: cargarOpcionesLibreria

        """
        vidrios = []
        for i in self.parent.parent.parent.parent.libreriaVidriosMarcos:
            if i[-1] == 'vidrio':
                vidrios.append(i[0])

        self.libreriaVidriosChoice.Clear()
        self.libreriaVidriosChoice.SetItems(vidrios)
        marcos = []
        for i in self.parent.parent.parent.parent.libreriaVidriosMarcos:
            if i[-1] == 'marco':
                marcos.append(i[0])

        self.libreriaMarcosChoice.Clear()
        self.libreriaMarcosChoice.SetItems(marcos)

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
        try:
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
        except:
            wx.MessageBox(_('Datos de obstáculos remotos incompletos o erróneos'), _('Aviso'))
            self._init_vars()

    def onAceptarBoton(self, event):
        """
        Metodo: onAceptarBoton

        ARGUMENTOS:
                event:
        """
        Uvidrio = self.Uvidrio.GetValue()
        Gvidrio = self.Gvidrio.GetValue()
        permeabilidadAire = self.permeabilidadAire.GetValue()
        porcentajeMarco = self.porcentajeMarco.GetValue()
        Umarco = self.Umarco.GetValue()
        if ',' in Uvidrio:
            Uvidrio = Uvidrio.replace(',', '.')
            self.Uvidrio.SetValue(Uvidrio)
        if ',' in Gvidrio:
            Gvidrio = Gvidrio.replace(',', '.')
            self.Gvidrio.SetValue(Gvidrio)
        if ',' in permeabilidadAire:
            permeabilidadAire = permeabilidadAire.replace(',', '.')
            self.permeabilidadAire.SetValue(permeabilidadAire)
        if ',' in porcentajeMarco:
            porcentajeMarco = porcentajeMarco.replace(',', '.')
            self.porcentajeMarco.SetValue(porcentajeMarco)
        if ',' in Umarco:
            Umarco = Umarco.replace(',', '.')
            self.Umarco.SetValue(Umarco)
        cambios = False
        error = ''
        error += Comprueba(self.descripcion.GetValue(), 0, error, _('nombre')).ErrorDevuelto
        if self.propiedadesVidrioCheck.GetValue() == True:
            cambios = True
            if self.UvidrioRadio.GetValue() == True:
                error += Comprueba(self.Uvidrio.GetValue(), 2, error, _('Uvidrio'), 0).ErrorDevuelto
                error += Comprueba2(self.Gvidrio.GetValue(), 2, error, _('Gvidrio'), 0, 1).ErrorDevuelto
            else:
                error += Comprueba(self.libreriaVidriosChoice.GetStringSelection(), 0, error, _('librería de vidrios')).ErrorDevuelto
        if self.permeabilidadCheck.GetValue() == True:
            cambios = True
            if self.claseVentanasRadio.GetValue() == True:
                error += Comprueba(self.claseVentanasChoice.GetStringSelection(), 0, error, _('clase de ventana')).ErrorDevuelto
            else:
                error += Comprueba(self.permeabilidadChoice.GetStringSelection(), 0, error, _('permeabilidad')).ErrorDevuelto
                if self.permeabilidadChoice.GetStringSelection() == 'Valor conocido':
                    error += Comprueba(self.permeabilidadAire.GetValue(), 2, error, _('valor de permeabilidad conocida'), 0).ErrorDevuelto
        if self.porcentajeMarcoCheck.GetValue() == True:
            cambios = True
            error += Comprueba(self.porcentajeMarco.GetValue(), 2, error, _('porcentade de marco'), 0, 100).ErrorDevuelto
        if self.propiedadesMarcoCheck.GetValue() == True:
            cambios = True
            if self.UmarcoRadio.GetValue() == True:
                error += Comprueba(self.Umarco.GetValue(), 2, error, _('Umarco'), 0).ErrorDevuelto
            else:
                error += Comprueba(self.libreriaMarcosChoice.GetStringSelection(), 0, error, _('librería de marcos')).ErrorDevuelto
        if self.tieneDobleVentanaCheck.GetValue() == True:
            cambios = True
            error += Comprueba(self.tipoDobleVentanaChoice.GetStringSelection(), 0, error, _('tipo de ventana doble'), 0).ErrorDevuelto
        if self.dipositivosProteccionCheck.GetValue() == True:
            cambios = True
        if error != '':
            wx.MessageBox(_('Revise los siguientes campos:\n') + error + _('.'), _('Aviso'))
            return
        if cambios == False:
            wx.MessageBox(_('No ha seleccionado ningún cambio.'), _('Aviso'))
            return
        orientaciones = [
         self.huecosNorteCheck.GetValue(), self.huecosNorOesteCheck.GetValue(),
         self.huecosNorEsteCheck.GetValue(),
         self.huecosSurCheck.GetValue(), self.huecosSurOesteCheck.GetValue(),
         self.huecosSurEsteCheck.GetValue(),
         self.lucernariosCheck.GetValue(), self.huecosOesteCheck.GetValue(),
         self.huecosEsteCheck.GetValue()]
        if True not in orientaciones:
            wx.MessageBox(_('No ha seleccionado ninguna orientación a la que afectan los cambios.'), _('Aviso'))
            return
        datos = []
        datos.append(self.descripcion.GetValue())
        datos.append('Sustitución/mejora de Huecos')
        datosConcretos = []
        datosConcretos.append(orientaciones)
        datosConcretos.append(self.propiedadesVidrioCheck.GetValue())
        datosConcretos.append(self.UvidrioRadio.GetValue())
        datosConcretos.append(self.Uvidrio.GetValue())
        datosConcretos.append(self.Gvidrio.GetValue())
        datosConcretos.append(self.libreriaVidriosChoice.GetStringSelection())
        datosConcretos.append(self.permeabilidadCheck.GetValue())
        datosConcretos.append(self.claseVentanasRadio.GetValue())
        datosConcretos.append(self.claseVentanasChoice.GetStringSelection())
        datosConcretos.append(self.permeabilidadChoice.GetStringSelection())
        datosConcretos.append(self.permeabilidadAire.GetValue())
        datosConcretos.append(self.porcentajeMarcoCheck.GetValue())
        datosConcretos.append(self.porcentajeMarco.GetValue())
        datosConcretos.append(self.propiedadesMarcoCheck.GetValue())
        datosConcretos.append(self.UmarcoRadio.GetValue())
        datosConcretos.append(self.Umarco.GetValue())
        datosConcretos.append(self.libreriaMarcosChoice.GetStringSelection())
        datosConcretos.append(self.tieneDobleVentanaCheck.GetValue())
        datosConcretos.append(self.tipoDobleVentanaChoice.GetStringSelection())
        datosConcretos.append(self.dipositivosProteccionCheck.GetValue())
        datosConcretos.append(self.cogerDatosSombras())
        datos.append(datosConcretos)
        self.dev = datos
        self.Close()

    def cargarDatos(self, datos):
        """
        Metodo: cargarDatos

        ARGUMENTOS:
                datos:
        """
        self.descripcion.SetValue(datos[0])
        datosConcretos = datos[2]
        self.huecosNorteCheck.SetValue(datosConcretos[0][0])
        self.huecosNorOesteCheck.SetValue(datosConcretos[0][1])
        self.huecosNorEsteCheck.SetValue(datosConcretos[0][2])
        self.huecosSurCheck.SetValue(datosConcretos[0][3])
        self.huecosSurOesteCheck.SetValue(datosConcretos[0][4])
        self.huecosSurEsteCheck.SetValue(datosConcretos[0][5])
        self.lucernariosCheck.SetValue(datosConcretos[0][6])
        self.huecosOesteCheck.SetValue(datosConcretos[0][7])
        self.huecosEsteCheck.SetValue(datosConcretos[0][8])
        self.propiedadesVidrioCheck.SetValue(datosConcretos[1])
        self.UvidrioRadio.SetValue(datosConcretos[2])
        self.libreriaVidriosRadio.SetValue(not datosConcretos[2])
        self.Uvidrio.SetValue(str(datosConcretos[3]))
        self.Gvidrio.SetValue(str(datosConcretos[4]))
        self.libreriaVidriosChoice.SetItems([datosConcretos[5]])
        self.libreriaVidriosChoice.SetStringSelection(datosConcretos[5])
        self.permeabilidadCheck.SetValue(datosConcretos[6])
        self.claseVentanasRadio.SetValue(datosConcretos[7])
        self.permeabilidadRadio.SetValue(not datosConcretos[7])
        self.claseVentanasChoice.SetStringSelection(datosConcretos[8])
        self.permeabilidadChoice.SetStringSelection(datosConcretos[9])
        self.permeabilidadAire.SetValue(str(datosConcretos[10]))
        self.porcentajeMarcoCheck.SetValue(datosConcretos[11])
        self.porcentajeMarco.SetValue(str(datosConcretos[12]))
        self.propiedadesMarcoCheck.SetValue(datosConcretos[13])
        self.UmarcoRadio.SetValue(datosConcretos[14])
        self.libreriaMarcosRadio.SetValue(not datosConcretos[14])
        self.Umarco.SetValue(str(datosConcretos[15]))
        self.libreriaMarcosChoice.SetItems([datosConcretos[16]])
        self.libreriaMarcosChoice.SetStringSelection(datosConcretos[16])
        self.tieneDobleVentanaCheck.SetValue(datosConcretos[17])
        self.tipoDobleVentanaChoice.SetStringSelection(datosConcretos[18])
        self.dipositivosProteccionCheck.SetValue(datosConcretos[19])
        self.cargarDatosSombras(datosConcretos[20])
        self.OnCambioCheckbox(None)
        return

    def onCancelarBoton(self, event):
        """
        Metodo: onCancelarBoton

        ARGUMENTOS:
                event:
        """
        self.dev = False
        self.Close()

    def OnPermeabilidadAireChoice(self, event):
        """
        Metodo: OnPermeabilidadAireChoice

        ARGUMENTOS:
                event:
        """
        if self.permeabilidadChoice.GetStringSelection() == 'Valor conocido':
            self.permeabilidadAire.Enable(True)
        else:
            self.permeabilidadAire.Enable(False)
        self.PermeabilidadVentanas()