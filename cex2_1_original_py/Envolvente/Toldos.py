# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\Toldos.pyc
# Compiled at: 2015-05-29 10:09:51
"""
Modulo: Toldos.py

"""
import wx, directorios
Directorio = directorios.BuscaDirectorios().Directorio

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return Dialog1(parent)


wxID_DIALOG1, wxID_WXTOLDOSBORRAR, wxID_WXTOLDOSACEPTAR, wxID_wxTOLDOSIMAGEN_A, wxID_wxTOLDOSIMAGEN_B, wxID_WXTOLDOSA_TEXT, wxID_WXTOLDOSB_TEXT, wxID_WXTEJIDOA_TEXT, wxID_WXOPACOA, wxID_WXTRANSLUCIDOA, wxID_WXANGULOA_TEXT, wxID_WXANGULOACUADRO, wxID_WXTEJIDOB_TEXT, wxID_WXOPACOB, wxID_WXTRANSLUCIDOB, wxID_WXANGULOB_TEXT, wxID_WXANGULOBCUADRO, wxID_WXTOLDOSCANCELAR, wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICBOX1, wxID_WXUNIDADESANGULOATEXT, wxID_WXUNIDADESANGULOBTEXT = [ wx.NewId() for _init_ctrls in range(22) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo Toldos.py

    """
    Toldos_CasoA = False
    Toldos_CasoB = False

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
        """
        if self.parent.Toldos_AnguloA != '' and (self.parent.Toldos_OpacoA == True or self.parent.Toldos_TranslucidoA == True):
            self.Toldos_CasoA = True
        else:
            self.Toldos_CasoA = False
        if self.parent.Toldos_AnguloB != '' and (self.parent.Toldos_OpacoB == True or self.parent.Toldos_TranslucidoB == True):
            self.Toldos_CasoB = True
        else:
            self.Toldos_CasoB = False
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(465, 202), size=wx.Size(490, 380), style=wx.DEFAULT_DIALOG_STYLE, title=_('TOLDOS'))
        self.SetClientSize(wx.Size(490, 380))
        self.SetBackgroundColour('white')
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=_('Toldos'), name='staticText1', parent=self, pos=wx.Point(15, 15), size=wx.Size(350, 20), style=0)
        self.staticText1.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.staticText1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticBox1 = wx.StaticBox(id=wxID_DIALOG1STATICBOX1, label=_('Dimensiones'), name='staticBox1', parent=self, pos=wx.Point(15, 45), size=wx.Size(460, 280), style=0)
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticBox1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.imagenTOLDOS_A = wx.StaticBitmap(bitmap=wx.Bitmap(Directorio + '/Imagenes/Fotos_Sombras/Toldos_A.png', wx.BITMAP_TYPE_PNG), id=wxID_wxTOLDOSIMAGEN_A, name='imagenTOLDOS_A', parent=self, pos=wx.Point(30, 60), size=wx.Size(113, 125), style=0)
        self.imagenTOLDOS_B = wx.StaticBitmap(bitmap=wx.Bitmap(Directorio + '/Imagenes/Fotos_Sombras/Toldos_B.png', wx.BITMAP_TYPE_PNG), id=wxID_wxTOLDOSIMAGEN_B, name='imagenTOLDOS_B', parent=self, pos=wx.Point(30, 185), size=wx.Size(117, 125), style=0)
        self.parent = prnt
        self.ToldosA = wx.CheckBox(id=wxID_WXTOLDOSA_TEXT, label=_('Caso A'), name=_('Caso A'), parent=self, pos=wx.Point(270, 75), size=wx.Size(100, 13), style=0)
        self.ToldosA.SetValue(self.Toldos_CasoA)
        self.ToldosA.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.ToldosA.Bind(wx.EVT_CHECKBOX, self.OnToldosA, id=wxID_WXTOLDOSA_TEXT)
        self.ToldosB = wx.CheckBox(id=wxID_WXTOLDOSB_TEXT, label=_('Caso B'), name=_('Caso B'), parent=self, pos=wx.Point(270, 200), size=wx.Size(100, 13), style=0)
        self.ToldosB.SetValue(self.Toldos_CasoB)
        self.ToldosB.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.ToldosB.Bind(wx.EVT_CHECKBOX, self.OnToldosB, id=wxID_WXTOLDOSB_TEXT)
        self.AnguloA_Text = wx.StaticText(id=wxID_WXANGULOA_TEXT, label=_('Ángulo'), name='AnguloA', parent=self, pos=wx.Point(310, 100), size=wx.Size(38, 13), style=0)
        self.AnguloA_Text.Enable(self.Toldos_CasoA)
        self.AnguloACuadro = wx.TextCtrl(id=wxID_WXANGULOACUADRO, name='AnguloACuadro', parent=self, pos=wx.Point(350, 98), size=wx.Size(65, 21), style=0, value=str(self.parent.Toldos_AnguloA))
        self.AnguloACuadro.Enable(self.Toldos_CasoA)
        self.UnidadesAnguloAText = wx.StaticText(id=wxID_WXUNIDADESANGULOATEXT, label=_('º'), name=_('UnidadesAnguloAText'), parent=self, pos=wx.Point(420, 100), size=wx.Size(10, 13), style=0)
        self.UnidadesAnguloAText.Enable(self.Toldos_CasoA)
        self.TejidoA_Text = wx.StaticText(id=wxID_WXTEJIDOA_TEXT, label=_('Tipo de tejido:'), name='TejidoA', parent=self, pos=wx.Point(310, 125), size=wx.Size(90, 13), style=0)
        self.TejidoA_Text.Enable(self.Toldos_CasoA)
        self.OpacoA = wx.RadioButton(id=wxID_WXOPACOA, label=_('Tejido opaco'), name='OpacoA', parent=self, pos=wx.Point(350, 140), size=wx.Size(120, 13), style=wx.RB_GROUP)
        self.OpacoA.SetValue(self.parent.Toldos_OpacoA)
        self.OpacoA.Enable(self.Toldos_CasoA)
        self.TranslucidoA = wx.RadioButton(id=wxID_WXTRANSLUCIDOA, label=_('Tejido translúcido'), name='TranslucidoA', parent=self, pos=wx.Point(350, 155), size=wx.Size(120, 13), style=0)
        self.TranslucidoA.SetValue(self.parent.Toldos_TranslucidoA)
        self.TranslucidoA.Enable(self.Toldos_CasoA)
        self.AnguloB_Text = wx.StaticText(id=wxID_WXANGULOB_TEXT, label=_('Ángulo'), name='AnguloB', parent=self, pos=wx.Point(310, 225), size=wx.Size(38, 13), style=0)
        self.AnguloB_Text.Enable(self.Toldos_CasoB)
        self.AnguloBCuadro = wx.TextCtrl(id=wxID_WXANGULOBCUADRO, name='AnguloBCuadro', parent=self, pos=wx.Point(350, 223), size=wx.Size(65, 21), style=0, value=str(self.parent.Toldos_AnguloB))
        self.AnguloBCuadro.Enable(self.Toldos_CasoB)
        self.UnidadesAnguloBText = wx.StaticText(id=wxID_WXUNIDADESANGULOBTEXT, label=_('º'), name=_('UnidadesAnguloBText'), parent=self, pos=wx.Point(420, 225), size=wx.Size(10, 13), style=0)
        self.UnidadesAnguloBText.Enable(self.Toldos_CasoB)
        self.TejidoB_Text = wx.StaticText(id=wxID_WXTEJIDOB_TEXT, label=_('Tipo de tejido:'), name='TejidoB', parent=self, pos=wx.Point(310, 250), size=wx.Size(90, 13), style=0)
        self.TejidoB_Text.Enable(self.Toldos_CasoB)
        self.OpacoB = wx.RadioButton(id=wxID_WXOPACOB, label=_('Tejido opaco'), name='OpacoB', parent=self, pos=wx.Point(350, 265), size=wx.Size(120, 13), style=wx.RB_GROUP)
        self.OpacoB.SetValue(self.parent.Toldos_OpacoB)
        self.OpacoB.Enable(self.Toldos_CasoB)
        self.TranslucidoB = wx.RadioButton(id=wxID_WXTRANSLUCIDOB, label=_('Tejido translúcido'), name='TranslucidoB', parent=self, pos=wx.Point(350, 280), size=wx.Size(120, 13), style=0)
        self.TranslucidoB.SetValue(self.parent.Toldos_TranslucidoB)
        self.TranslucidoB.Enable(self.Toldos_CasoB)
        self.aceptar = wx.Button(id=wxID_WXTOLDOSACEPTAR, label=_('Aceptar'), name='aceptar', parent=self, pos=wx.Point(15, 340), size=wx.Size(75, 23), style=0)
        self.aceptar.Bind(wx.EVT_BUTTON, self.OnAceptarButton, id=wxID_WXTOLDOSACEPTAR)
        self.cancelar = wx.Button(id=wxID_WXTOLDOSCANCELAR, label=_('Cancelar'), name='cancelar', parent=self, pos=wx.Point(105, 340), size=wx.Size(75, 23), style=0)
        self.cancelar.Bind(wx.EVT_BUTTON, self.OnCancelarButton, id=wxID_WXTOLDOSCANCELAR)
        self.borrar = wx.Button(id=wxID_WXTOLDOSBORRAR, label=_('Borrar'), name='borrar', parent=self, pos=wx.Point(240, 340), size=wx.Size(75, 23), style=0)
        self.borrar.Bind(wx.EVT_BUTTON, self.OnBorrarButton, id=wxID_WXTOLDOSBORRAR)

    def OnToldosA(self, event):
        """
        Metodo: OnToldosA

        ARGUMENTOS:
                event:
        """
        if self.ToldosA.GetValue() == True:
            self.ToldosB.SetValue(False)
            self.AnguloA_Text.Enable(True)
            self.AnguloACuadro.Enable(True)
            self.UnidadesAnguloAText.Enable(True)
            self.TejidoA_Text.Enable(True)
            self.OpacoA.Enable(True)
            self.TranslucidoA.Enable(True)
            self.AnguloB_Text.Enable(False)
            self.AnguloBCuadro.Enable(False)
            self.UnidadesAnguloBText.Enable(False)
            self.TejidoB_Text.Enable(False)
            self.OpacoB.Enable(False)
            self.TranslucidoB.Enable(False)
        else:
            self.AnguloA_Text.Enable(False)
            self.AnguloACuadro.Enable(False)
            self.UnidadesAnguloAText.Enable(False)
            self.TejidoA_Text.Enable(False)
            self.OpacoA.Enable(False)
            self.TranslucidoA.Enable(False)

    def OnToldosB(self, event):
        """
        Metodo: OnToldosB

        ARGUMENTOS:
                event:
        """
        if self.ToldosB.GetValue() == True:
            self.ToldosA.SetValue(False)
            self.AnguloA_Text.Enable(False)
            self.AnguloACuadro.Enable(False)
            self.UnidadesAnguloAText.Enable(False)
            self.TejidoA_Text.Enable(False)
            self.OpacoA.Enable(False)
            self.TranslucidoA.Enable(False)
            self.AnguloB_Text.Enable(True)
            self.AnguloBCuadro.Enable(True)
            self.UnidadesAnguloBText.Enable(True)
            self.TejidoB_Text.Enable(True)
            self.OpacoB.Enable(True)
            self.TranslucidoB.Enable(True)
        else:
            self.AnguloB_Text.Enable(False)
            self.AnguloBCuadro.Enable(False)
            self.UnidadesAnguloBText.Enable(False)
            self.TejidoB_Text.Enable(False)
            self.OpacoB.Enable(False)
            self.TranslucidoB.Enable(False)

    def OnAceptarButton(self, event):
        """
        Metodo: OnAceptarButton

        ARGUMENTOS:
                event:
        """
        if self.ToldosA.GetValue() == False and self.ToldosB.GetValue() == False:
            self.parent.Toldos_AnguloB = ''
            self.parent.Toldos_OpacoB = False
            self.parent.Toldos_TranslucidoB = False
            self.parent.Toldos_AnguloA = ''
            self.parent.Toldos_OpacoA = False
            self.parent.Toldos_TranslucidoA = False
            wx.MessageBox(_('Toldo no definido'), _('Aviso'))
            self.parent.Toldos_Si = False
            self.parent.Toldos.SetValue(self.parent.Toldos_Si)
            self.Close()
        else:
            lista_errores = ''
            if self.ToldosA.GetValue() == True:
                if self.AnguloACuadro.GetValue() == '':
                    lista_errores = 'Ángulo'
                elif self.AnguloACuadro.GetValue() != '':
                    AnguloA = self.AnguloACuadro.GetValue()
                    if ',' in AnguloA:
                        AnguloA = AnguloA.replace(',', '.')
                        self.AnguloACuadro.SetValue(AnguloA)
                    try:
                        float(self.AnguloACuadro.GetValue())
                    except (ValueError, TypeError):
                        lista_errores = 'Ángulo'

                if self.OpacoA.GetValue() == False and self.TranslucidoA.GetValue() == False:
                    if lista_errores != '':
                        lista_errores = lista_errores + ', '
                    lista_errores = lista_errores + 'tipo de tejido'
                if lista_errores != '':
                    wx.MessageBox(_('Revise los siguientes campos:\n') + lista_errores, _('Aviso'))
                    self.parent.Toldos_Si = False
                    self.parent.Toldos.SetValue(self.parent.Toldos_Si)
                else:
                    self.parent.Toldos_AnguloA = self.AnguloACuadro.GetValue()
                    self.parent.Toldos_OpacoA = self.OpacoA.GetValue()
                    self.parent.Toldos_TranslucidoA = self.TranslucidoA.GetValue()
                    self.parent.Toldos_AnguloB = ''
                    self.parent.Toldos_OpacoB = False
                    self.parent.Toldos_TranslucidoB = False
                    self.parent.Toldos_Si = True
                    self.parent.Toldos.SetValue(self.parent.Toldos_Si)
                    self.Close()
            if self.ToldosB.GetValue() == True:
                if self.AnguloBCuadro.GetValue() == '':
                    lista_errores = 'Ángulo'
                elif self.AnguloBCuadro.GetValue() != '':
                    AnguloB = self.AnguloBCuadro.GetValue()
                    if ',' in AnguloB:
                        AnguloB = AnguloB.replace(',', '.')
                        self.AnguloBCuadro.SetValue(AnguloB)
                    try:
                        float(self.AnguloBCuadro.GetValue())
                    except (ValueError, TypeError):
                        lista_errores = 'Ángulo'

                if self.OpacoB.GetValue() == False and self.TranslucidoB.GetValue() == False:
                    if lista_errores != '':
                        lista_errores = lista_errores + ', '
                    lista_errores = lista_errores + 'tipo de tejido'
                if lista_errores != '':
                    wx.MessageBox(_('Revise los siguientes campos:\n') + lista_errores, _('Aviso'))
                    self.parent.Toldos_Si = False
                    self.parent.Toldos.SetValue(self.parent.Toldos_Si)
                else:
                    self.parent.Toldos_AnguloB = self.AnguloBCuadro.GetValue()
                    self.parent.Toldos_OpacoB = self.OpacoB.GetValue()
                    self.parent.Toldos_TranslucidoB = self.TranslucidoB.GetValue()
                    self.parent.Toldos_AnguloA = ''
                    self.parent.Toldos_OpacoA = False
                    self.parent.Toldos_TranslucidoA = False
                    self.parent.Toldos_Si = True
                    self.parent.Toldos.SetValue(self.parent.Toldos_Si)
                    self.Close()

    def OnBorrarButton(self, event):
        """
        Metodo: OnBorrarButton

        ARGUMENTOS:
                event:
        """
        self.ToldosA.SetValue(False)
        self.ToldosB.SetValue(False)
        self.AnguloACuadro.SetValue('')
        self.OpacoA.SetValue(False)
        self.TranslucidoA.SetValue(False)
        self.AnguloACuadro.Enable(False)
        self.OpacoA.Enable(False)
        self.TranslucidoA.Enable(False)
        self.AnguloBCuadro.SetValue('')
        self.OpacoB.SetValue(False)
        self.TranslucidoB.SetValue(False)
        self.AnguloBCuadro.Enable(False)
        self.OpacoB.Enable(False)
        self.TranslucidoB.Enable(False)

    def OnCancelarButton(self, event):
        """
        Metodo: OnCancelarButton

        ARGUMENTOS:
                event:
        """
        self.Close()

    def __init__(self, parent):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
        """
        self.parent = parent
        self._init_ctrls(parent)