# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\Retranqueos.pyc
# Compiled at: 2015-03-17 10:52:55
"""
Modulo: Retranqueos.py

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


wxID_DIALOG1, wxID_WXRETRANQUEOSH_TEXT, wxID_WXRETRANQUEOSW_TEXT, wxID_WXRETRANQUEOSR_TEXT, wxID_WXRETRANQUEOSH_CUADRO, wxID_WXRETRANQUEOSW_CUADRO, wxID_WXRETRANQUEOSR_CUADRO, wxID_WXRETRANQUEOSACEPTAR, wxID_WXRETRANQUEOSBORRAR, wxID_wxRETRANQUEOSIMAGEN, wxID_WXRETRANQUEOSCANCELAR, wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICBOX1, wxID_WXUNIDADESTEXT1, wxID_WXUNIDADESTEXT2, wxID_UNIDADESTEXT3 = [ wx.NewId() for _init_ctrls in range(16) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo Retranqueos.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(465, 202), size=wx.Size(490, 380), style=wx.DEFAULT_DIALOG_STYLE, title=_('Retranqueos'))
        self.SetClientSize(wx.Size(490, 380))
        self.SetBackgroundColour('white')
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=_('Retranqueos'), name='staticText1', parent=self, pos=wx.Point(15, 15), size=wx.Size(350, 20), style=0)
        self.staticText1.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.staticText1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticBox1 = wx.StaticBox(id=wxID_DIALOG1STATICBOX1, label=_('Dimensiones'), name='staticBox1', parent=self, pos=wx.Point(15, 45), size=wx.Size(460, 280), style=0)
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticBox1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.imagenRETRANQUEOs = wx.StaticBitmap(bitmap=wx.Bitmap(Directorio + '/Imagenes/Fotos_Sombras/Retranqueos.png', wx.BITMAP_TYPE_PNG), id=wxID_wxRETRANQUEOSIMAGEN, name='imagenretranqueoss', parent=self, pos=wx.Point(30, 60), size=wx.Size(164, 250), style=0)
        self.parent = prnt
        self.H_Text = wx.StaticText(id=wxID_WXRETRANQUEOSH_TEXT, label=_('H'), name=_('H'), parent=self, pos=wx.Point(370, 75), size=wx.Size(10, 13), style=0)
        self.H_Text.Enable(True)
        self.H_Cuadro = wx.TextCtrl(id=wxID_WXRETRANQUEOSH_CUADRO, name='H', parent=self, pos=wx.Point(385, 73), size=wx.Size(65, 21), style=0, value=self.parent.Retranqueo_H)
        self.H_Cuadro.Enable(True)
        self.W_Text = wx.StaticText(id=wxID_WXRETRANQUEOSW_TEXT, label=_('W'), name=_('W'), parent=self, pos=wx.Point(370, 125), size=wx.Size(10, 13), style=0)
        self.W_Text.Enable(True)
        self.W_Cuadro = wx.TextCtrl(id=wxID_WXRETRANQUEOSW_CUADRO, name='W', parent=self, pos=wx.Point(385, 123), size=wx.Size(65, 21), style=0, value=self.parent.Retranqueo_W)
        self.W_Cuadro.Enable(True)
        self.R_Text = wx.StaticText(id=wxID_WXRETRANQUEOSR_TEXT, label=_('R'), name=_('R'), parent=self, pos=wx.Point(370, 175), size=wx.Size(10, 13), style=0)
        self.R_Text.Enable(True)
        self.R_Cuadro = wx.TextCtrl(id=wxID_WXRETRANQUEOSR_CUADRO, name='R', parent=self, pos=wx.Point(385, 173), size=wx.Size(65, 21), style=0, value=self.parent.Retranqueo_R)
        self.R_Cuadro.Enable(True)
        self.UnidadesText1 = wx.StaticText(id=wxID_WXUNIDADESTEXT1, label=_('m'), name=_('L_TextUnidades'), parent=self, pos=wx.Point(455, 75), size=wx.Size(10, 13), style=0)
        self.UnidadesText2 = wx.StaticText(id=wxID_WXUNIDADESTEXT2, label=_('m'), name=_('H_TextUnidades'), parent=self, pos=wx.Point(455, 125), size=wx.Size(10, 13), style=0)
        self.UnidadesText3 = wx.StaticText(id=wxID_UNIDADESTEXT3, label=_('m'), name=_('D_TextUnidades'), parent=self, pos=wx.Point(455, 175), size=wx.Size(10, 13), style=0)
        self.aceptar = wx.Button(id=wxID_WXRETRANQUEOSACEPTAR, label=_('Aceptar'), name='aceptar', parent=self, pos=wx.Point(15, 340), size=wx.Size(75, 23), style=0)
        self.aceptar.Bind(wx.EVT_BUTTON, self.OnAceptarButton, id=wxID_WXRETRANQUEOSACEPTAR)
        self.cancelar = wx.Button(id=wxID_WXRETRANQUEOSCANCELAR, label=_('Cancelar'), name='cancelar', parent=self, pos=wx.Point(105, 340), size=wx.Size(75, 23), style=0)
        self.cancelar.Bind(wx.EVT_BUTTON, self.OnCancelarButton, id=wxID_WXRETRANQUEOSCANCELAR)
        self.borrar = wx.Button(id=wxID_WXRETRANQUEOSBORRAR, label=_('Borrar'), name='borrar', parent=self, pos=wx.Point(240, 340), size=wx.Size(75, 23), style=0)
        self.borrar.Bind(wx.EVT_BUTTON, self.OnBorrarButton, id=wxID_WXRETRANQUEOSBORRAR)

    def OnAceptarButton(self, event):
        """
        Metodo: OnAceptarButton

        ARGUMENTOS:
                event:
        """
        self.parent.Retranqueo_H = self.H_Cuadro.GetValue()
        self.parent.Retranqueo_W = self.W_Cuadro.GetValue()
        self.parent.Retranqueo_R = self.R_Cuadro.GetValue()
        if self.parent.Retranqueo_H == '' and self.parent.Retranqueo_W == '' and self.parent.Retranqueo_R == '':
            wx.MessageBox(_('Retranqueo no definido'))
            self.parent.Retranqueos_Si = False
            self.parent.Retranqueo.SetValue(self.parent.Retranqueos_Si)
            self.Close()
        else:
            lista_errores = ''
            if ',' in self.parent.Retranqueo_H:
                self.parent.Retranqueo_H = self.parent.Retranqueo_H.replace(',', '.')
            if ',' in self.parent.Retranqueo_W:
                self.parent.Retranqueo_W = self.parent.Retranqueo_W.replace(',', '.')
            if ',' in self.parent.Retranqueo_R:
                self.parent.Retranqueo_R = self.parent.Retranqueo_R.replace(',', '.')
            try:
                float(self.parent.Retranqueo_H)
                if float(self.parent.Retranqueo_H) < 0:
                    self.parent.Retranqueo_H = ''
            except (ValueError, TypeError):
                self.parent.Retranqueo_H = ''

            try:
                float(self.parent.Retranqueo_W)
                if float(self.parent.Retranqueo_W) < 0:
                    self.parent.Retranqueo_W = ''
            except (ValueError, TypeError):
                self.parent.Retranqueo_W = ''

            try:
                float(self.parent.Retranqueo_R)
                if float(self.parent.Retranqueo_R) < 0:
                    self.parent.Retranqueo_R = ''
            except (ValueError, TypeError):
                self.parent.Retranqueo_R = ''

            if self.parent.Retranqueo_H == '':
                lista_errores = 'H'
            if self.parent.Retranqueo_W == '':
                if lista_errores != '':
                    lista_errores = lista_errores + ', '
                lista_errores = lista_errores + 'W'
            if self.parent.Retranqueo_R == '':
                if lista_errores != '':
                    lista_errores = lista_errores + ', '
                lista_errores = lista_errores + 'R'
            if lista_errores != '':
                wx.MessageBox(_('Revise los siguientes campos:\n') + lista_errores, _('Aviso'))
                self.parent.Retranqueos_Si = False
                self.parent.Retranqueo.SetValue(self.parent.Retranqueos_Si)
            else:
                self.parent.Retranqueos_Si = True
                self.parent.Retranqueo.SetValue(self.parent.Retranqueos_Si)
                self.Close()

    def OnBorrarButton(self, event):
        """
        Metodo: OnBorrarButton

        ARGUMENTOS:
                event:
        """
        self.H_Cuadro.SetValue('')
        self.W_Cuadro.SetValue('')
        self.R_Cuadro.SetValue('')

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
            if parent.parent.alturaMuro.GetValue() != '' and self.parent.Retranqueo_H == '':
                self.H_Cuadro.SetValue(parent.parent.alturaMuro.GetValue())
            if parent.parent.longitudMuro.GetValue() != '' and self.parent.Retranqueo_W == '':
                self.W_Cuadro.SetValue(parent.parent.longitudMuro.GetValue())
        except:
            logging.info('Excepcion en: %s' % __name__)