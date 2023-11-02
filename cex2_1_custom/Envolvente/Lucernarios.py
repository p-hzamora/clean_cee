# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\Lucernarios.pyc
# Compiled at: 2015-05-29 10:08:48
"""
Modulo: Lucernarios.py

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


wxID_DIALOG1, wxID_WX_X_TEXT, wxID_WX_X_CUADRO, wxID_WX_Y_TEXT, wxID_WX_Y_CUADRO, wxID_WX_Z_TEXT, wxID_WX_Z_CUADRO, wxID_WXLUCERNARIOS_ACEPTAR, wxID_WXLUCERNARIOS_BORRAR, wxID_wxLUCERNARIOS_IMAGEN, wxID_WXLUCERNARIOS_TEXTOFOTO, wxID_WXLUCERNARIOS_CANCELAR, wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICBOX1, wxID_WXUNIDADESTEXT1, wxID_WXUNIDADESTEXT2, wxID_UNIDADESTEXT3 = [ wx.NewId() for _init_ctrls in range(17) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo Lucernarios.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(465, 202), size=wx.Size(490, 380), style=wx.DEFAULT_DIALOG_STYLE, title=_('Lucernarios'))
        self.SetClientSize(wx.Size(490, 380))
        self.SetBackgroundColour('white')
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=_('Lucernarios'), name='staticText1', parent=self, pos=wx.Point(15, 15), size=wx.Size(350, 20), style=0)
        self.staticText1.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.staticText1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticBox1 = wx.StaticBox(id=wxID_DIALOG1STATICBOX1, label=_('Dimensiones'), name='staticBox1', parent=self, pos=wx.Point(15, 45), size=wx.Size(460, 280), style=0)
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticBox1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.imagenLucernarios = wx.StaticBitmap(bitmap=wx.Bitmap(Directorio + '/Imagenes/Fotos_Sombras/Lucernarios.png', wx.BITMAP_TYPE_PNG), id=wxID_wxLUCERNARIOS_IMAGEN, name='imagenLucernarios', parent=self, pos=wx.Point(30, 60), size=wx.Size(168, 250), style=0)
        self.Texto_Foto = wx.StaticText(id=wxID_WXLUCERNARIOS_TEXTOFOTO, label=_('NOTA: En caso de lucernarios de planta elíptica o circular podrán tomarse como dimensiones características equivalentes los ejes mayor y menor o el diámetro.'), name='Texto_Foto', parent=self, pos=wx.Point(205, 270), size=wx.Size(260, 50), style=0)
        self.parent = prnt
        self.X_Text = wx.StaticText(id=wxID_WX_X_TEXT, label=_('X'), name=_('X'), parent=self, pos=wx.Point(370, 75), size=wx.Size(10, 13), style=0)
        self.X_Text.Enable(True)
        self.X_Cuadro = wx.TextCtrl(id=wxID_WX_X_CUADRO, name='X', parent=self, pos=wx.Point(385, 73), size=wx.Size(65, 21), style=0, value=self.parent.Lucernarios_X)
        self.X_Cuadro.Enable(True)
        self.Y_Text = wx.StaticText(id=wxID_WX_Y_TEXT, label=_('Y'), name=_('Y'), parent=self, pos=wx.Point(370, 125), size=wx.Size(10, 13), style=0)
        self.Y_Text.Enable(True)
        self.Y_Cuadro = wx.TextCtrl(id=wxID_WX_Y_CUADRO, name='Y', parent=self, pos=wx.Point(385, 123), size=wx.Size(65, 21), style=0, value=self.parent.Lucernarios_Y)
        self.Y_Cuadro.Enable(True)
        self.Z_Text = wx.StaticText(id=wxID_WX_Z_TEXT, label=_('Z'), name=_('Z'), parent=self, pos=wx.Point(370, 175), size=wx.Size(10, 13), style=0)
        self.Z_Text.Enable(True)
        self.Z_Cuadro = wx.TextCtrl(id=wxID_WX_Z_CUADRO, name='Z', parent=self, pos=wx.Point(385, 173), size=wx.Size(65, 21), style=0, value=self.parent.Lucernarios_Z)
        self.Z_Cuadro.Enable(True)
        self.UnidadesText1 = wx.StaticText(id=wxID_WXUNIDADESTEXT1, label=_('m'), name=_('L_TextUnidades'), parent=self, pos=wx.Point(455, 75), size=wx.Size(10, 13), style=0)
        self.UnidadesText2 = wx.StaticText(id=wxID_WXUNIDADESTEXT2, label=_('m'), name=_('H_TextUnidades'), parent=self, pos=wx.Point(455, 125), size=wx.Size(10, 13), style=0)
        self.UnidadesText3 = wx.StaticText(id=wxID_UNIDADESTEXT3, label=_('m'), name=_('D_TextUnidades'), parent=self, pos=wx.Point(455, 175), size=wx.Size(10, 13), style=0)
        self.aceptar = wx.Button(id=wxID_WXLUCERNARIOS_ACEPTAR, label=_('Aceptar'), name='aceptar', parent=self, pos=wx.Point(15, 340), size=wx.Size(75, 23), style=0)
        self.aceptar.Bind(wx.EVT_BUTTON, self.OnAceptarButton, id=wxID_WXLUCERNARIOS_ACEPTAR)
        self.cancelar = wx.Button(id=wxID_WXLUCERNARIOS_CANCELAR, label=_('Cancelar'), name='cancelar', parent=self, pos=wx.Point(105, 340), size=wx.Size(75, 23), style=0)
        self.cancelar.Bind(wx.EVT_BUTTON, self.OnCancelarButton, id=wxID_WXLUCERNARIOS_CANCELAR)
        self.borrar = wx.Button(id=wxID_WXLUCERNARIOS_BORRAR, label=_('Borrar'), name='borrar', parent=self, pos=wx.Point(240, 340), size=wx.Size(75, 23), style=0)
        self.borrar.Bind(wx.EVT_BUTTON, self.OnBorrarButton, id=wxID_WXLUCERNARIOS_BORRAR)
        self.X_Cuadro.SetToolTip(wx.ToolTip(_('Dimensión X en el plano horizontal')))
        self.Y_Cuadro.SetToolTip(wx.ToolTip(_('Dimensión Y en el plano horizontal')))
        self.Z_Cuadro.SetToolTip(wx.ToolTip(_('Profundidad Z, medida según se indica en la figura.')))

    def OnAceptarButton(self, event):
        """
        Metodo: OnAceptarButton

        ARGUMENTOS:
                event:
        """
        self.parent.Lucernarios_X = self.X_Cuadro.GetValue()
        self.parent.Lucernarios_Y = self.Y_Cuadro.GetValue()
        self.parent.Lucernarios_Z = self.Z_Cuadro.GetValue()
        if self.parent.Lucernarios_X == '' and self.parent.Lucernarios_Y == '' and self.parent.Lucernarios_Z == '':
            wx.MessageBox(_('Lucernario no definido'), _('Aviso'))
            self.parent.Lucernarios_Si = False
            self.parent.Lucernarios.SetValue(self.parent.Lucernarios_Si)
            self.Close()
        else:
            lista_errores = ''
            if ',' in self.parent.Lucernarios_X:
                self.parent.Lucernarios_X = self.parent.Lucernarios_X.replace(',', '.')
            if ',' in self.parent.Lucernarios_Y:
                self.parent.Lucernarios_Y = self.parent.Lucernarios_Y.replace(',', '.')
            if ',' in self.parent.Lucernarios_Z:
                self.parent.Lucernarios_Z = self.parent.Lucernarios_Z.replace(',', '.')
            try:
                float(self.parent.Lucernarios_X)
                if float(self.parent.Lucernarios_X) < 0:
                    self.parent.Lucernarios_X = ''
            except (ValueError, TypeError):
                self.parent.Lucernarios_X = ''

            try:
                float(self.parent.Lucernarios_Y)
                if float(self.parent.Lucernarios_Y) < 0:
                    self.parent.Lucernarios_Y = ''
            except (ValueError, TypeError):
                self.parent.Lucernarios_Y = ''

            try:
                float(self.parent.Lucernarios_Z)
                if float(self.parent.Lucernarios_Z) < 0:
                    self.parent.Lucernarios_Z = ''
            except (ValueError, TypeError):
                self.parent.Lucernarios_Z = ''

            if self.parent.Lucernarios_X == '':
                lista_errores = 'X'
            if self.parent.Lucernarios_Y == '':
                if lista_errores != '':
                    lista_errores = lista_errores + ', '
                lista_errores = lista_errores + 'Y'
            if self.parent.Lucernarios_Z == '':
                if lista_errores != '':
                    lista_errores = lista_errores + ', '
                lista_errores = lista_errores + 'Z'
            if lista_errores != '':
                wx.MessageBox(_('Revise los siguientes campos:\n') + lista_errores, _('Aviso'))
                self.parent.Lucernarios_Si = False
                self.parent.Lucernarios.SetValue(self.parent.Lucernarios_Si)
            else:
                self.parent.Lucernarios_Si = True
                self.parent.Lucernarios.SetValue(self.parent.Lucernarios_Si)
                self.Close()

    def OnBorrarButton(self, event):
        """
        Metodo: OnBorrarButton

        ARGUMENTOS:
                event:
        """
        self.X_Cuadro.SetValue('')
        self.Y_Cuadro.SetValue('')
        self.Z_Cuadro.SetValue('')

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