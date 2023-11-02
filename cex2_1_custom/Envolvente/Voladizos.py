# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\Voladizos.pyc
# Compiled at: 2015-05-29 10:10:08
"""
Modulo: Voladizos.py

"""
import wx, logging, directorios
Directorio = directorios.BuscaDirectorios().Directorio

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return Dialog1(parent)


wxID_DIALOG1, wxID_WXVOLADIZOSL_TEXT, wxID_WXVOLADIZOSH_TEXT, wxID_WXVOLADIZOSD_TEXT, wxID_WXVOLADIZOSL_CUADRO, wxID_WXVOLADIZOSH_CUADRO, wxID_WXVOLADIZOSD_CUADRO, wxID_WXVOLADIZOSACEPTAR, wxID_WXVOLADIZOSBORRAR, wxID_wxVOLADIZOSIMAGEN, wxID_WXVOLADIZOSTEXTOFOTO, wxID_WXVOLADIZOSCANCELAR, wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICBOX1, wxID_WXUNIDADESTEXT1, wxID_WXUNIDADESTEXT2, wxID_UNIDADESTEXT3 = [ wx.NewId() for _init_ctrls in range(17) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo Voladizos.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(465, 202), size=wx.Size(490, 380), style=wx.DEFAULT_DIALOG_STYLE, title=_('Voladizos'))
        self.SetClientSize(wx.Size(490, 380))
        self.SetBackgroundColour('white')
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=_('Voladizos'), name='staticText1', parent=self, pos=wx.Point(15, 15), size=wx.Size(350, 20), style=0)
        self.staticText1.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.staticText1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticBox1 = wx.StaticBox(id=wxID_DIALOG1STATICBOX1, label=_('Dimensiones'), name='staticBox1', parent=self, pos=wx.Point(15, 45), size=wx.Size(460, 280), style=0)
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticBox1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.imagenVoladizos = wx.StaticBitmap(bitmap=wx.Bitmap(Directorio + '/Imagenes/Fotos_Sombras/Voladizos.png', wx.BITMAP_TYPE_PNG), id=wxID_wxVOLADIZOSIMAGEN, name='imagenVoladizos', parent=self, pos=wx.Point(30, 60), size=wx.Size(165, 250), style=0)
        self.Texto_Foto = wx.StaticText(id=wxID_WXVOLADIZOSTEXTOFOTO, label=_('NOTA: En caso de que exista un retranqueo, la longitud L se medirá desde el centro del acristalamiento.'), name='Texto_Foto', parent=self, pos=wx.Point(200, 290), size=wx.Size(270, 30), style=0)
        self.parent = prnt
        self.L_Text = wx.StaticText(id=wxID_WXVOLADIZOSL_TEXT, label=_('L'), name=_('L'), parent=self, pos=wx.Point(370, 75), size=wx.Size(10, 13), style=0)
        self.L_Text.Enable(True)
        self.L_Cuadro = wx.TextCtrl(id=wxID_WXVOLADIZOSL_CUADRO, name='L', parent=self, pos=wx.Point(385, 73), size=wx.Size(65, 21), style=0, value=self.parent.Voladizo_L)
        self.L_Cuadro.Enable(True)
        self.H_Text = wx.StaticText(id=wxID_WXVOLADIZOSH_TEXT, label=_('H'), name=_('H'), parent=self, pos=wx.Point(370, 125), size=wx.Size(10, 13), style=0)
        self.H_Text.Enable(True)
        self.H_Cuadro = wx.TextCtrl(id=wxID_WXVOLADIZOSH_CUADRO, name='H', parent=self, pos=wx.Point(385, 123), size=wx.Size(65, 21), style=0, value=self.parent.Voladizo_H)
        self.H_Cuadro.Enable(True)
        self.D_Text = wx.StaticText(id=wxID_WXVOLADIZOSD_TEXT, label=_('D'), name=_('D'), parent=self, pos=wx.Point(370, 175), size=wx.Size(10, 13), style=0)
        self.D_Text.Enable(True)
        self.D_Cuadro = wx.TextCtrl(id=wxID_WXVOLADIZOSD_CUADRO, name='D', parent=self, pos=wx.Point(385, 173), size=wx.Size(65, 21), style=0, value=self.parent.Voladizo_D)
        self.D_Cuadro.Enable(True)
        self.UnidadesText1 = wx.StaticText(id=wxID_WXUNIDADESTEXT1, label=_('m'), name=_('L_TextUnidades'), parent=self, pos=wx.Point(455, 75), size=wx.Size(10, 13), style=0)
        self.UnidadesText2 = wx.StaticText(id=wxID_WXUNIDADESTEXT2, label=_('m'), name=_('H_TextUnidades'), parent=self, pos=wx.Point(455, 125), size=wx.Size(10, 13), style=0)
        self.UnidadesText3 = wx.StaticText(id=wxID_UNIDADESTEXT3, label=_('m'), name=_('D_TextUnidades'), parent=self, pos=wx.Point(455, 175), size=wx.Size(10, 13), style=0)
        self.aceptar = wx.Button(id=wxID_WXVOLADIZOSACEPTAR, label=_('Aceptar'), name='aceptar', parent=self, pos=wx.Point(15, 340), size=wx.Size(75, 23), style=0)
        self.aceptar.Bind(wx.EVT_BUTTON, self.OnAceptarButton, id=wxID_WXVOLADIZOSACEPTAR)
        self.cancelar = wx.Button(id=wxID_WXVOLADIZOSCANCELAR, label=_('Cancelar'), name='cancelar', parent=self, pos=wx.Point(105, 340), size=wx.Size(75, 23), style=0)
        self.cancelar.Bind(wx.EVT_BUTTON, self.OnCancelarButton, id=wxID_WXVOLADIZOSCANCELAR)
        self.borrar = wx.Button(id=wxID_WXVOLADIZOSBORRAR, label=_('Borrar'), name='borrar', parent=self, pos=wx.Point(240, 340), size=wx.Size(75, 23), style=0)
        self.borrar.Bind(wx.EVT_BUTTON, self.OnBorrarButton, id=wxID_WXVOLADIZOSBORRAR)

    def OnAceptarButton(self, event):
        """
        Metodo: OnAceptarButton

        ARGUMENTOS:
                event:
        """
        self.parent.Voladizo_L = self.L_Cuadro.GetValue()
        self.parent.Voladizo_H = self.H_Cuadro.GetValue()
        self.parent.Voladizo_D = self.D_Cuadro.GetValue()
        if self.parent.Voladizo_L == '' and self.parent.Voladizo_H == '' and self.parent.Voladizo_D == '':
            wx.MessageBox(_('Voladizo no definido'), _('Aviso'))
            self.parent.Voladizos_Si = False
            self.parent.Voladizo.SetValue(self.parent.Voladizos_Si)
            self.Close()
        else:
            lista_errores = ''
            if ',' in self.parent.Voladizo_L:
                self.parent.Voladizo_L = self.parent.Voladizo_L.replace(',', '.')
            if ',' in self.parent.Voladizo_H:
                self.parent.Voladizo_H = self.parent.Voladizo_H.replace(',', '.')
            if ',' in self.parent.Voladizo_D:
                self.parent.Voladizo_D = self.parent.Voladizo_D.replace(',', '.')
            try:
                float(self.parent.Voladizo_L)
                if float(self.parent.Voladizo_L) < 0:
                    self.parent.Voladizo_L = ''
            except (ValueError, TypeError):
                self.parent.Voladizo_L = ''

            try:
                float(self.parent.Voladizo_H)
                if float(self.parent.Voladizo_H) < 0:
                    self.parent.Voladizo_H = ''
            except (ValueError, TypeError):
                self.parent.Voladizo_H = ''

            try:
                float(self.parent.Voladizo_D)
                if float(self.parent.Voladizo_D) < 0:
                    self.parent.Voladizo_D = ''
            except (ValueError, TypeError):
                self.parent.Voladizo_D = ''

            if self.parent.Voladizo_L == '':
                lista_errores = 'L'
            if self.parent.Voladizo_H == '':
                if lista_errores != '':
                    lista_errores = lista_errores + ', '
                lista_errores = lista_errores + 'H'
            if self.parent.Voladizo_D == '':
                if lista_errores != '':
                    lista_errores = lista_errores + ', '
                lista_errores = lista_errores + 'D'
            if lista_errores != '':
                wx.MessageBox(_('Revise los siguientes campos:\n') + lista_errores, _('Aviso'))
                self.parent.Voladizos_Si = False
                self.parent.Voladizo.SetValue(self.parent.Voladizos_Si)
            else:
                self.parent.Voladizos_Si = True
                self.parent.Voladizo.SetValue(self.parent.Voladizos_Si)
                self.Close()

    def OnBorrarButton(self, event):
        """
        Metodo: OnBorrarButton

        ARGUMENTOS:
                event:
        """
        self.L_Cuadro.SetValue('')
        self.H_Cuadro.SetValue('')
        self.D_Cuadro.SetValue('')

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
        try:
            if parent.parent.alturaMuro.GetValue() != '' and self.parent.Voladizo_H == '':
                self.H_Cuadro.SetValue(parent.parent.alturaMuro.GetValue())
        except:
            logging.info('Excepcion en: %s' % __name__)