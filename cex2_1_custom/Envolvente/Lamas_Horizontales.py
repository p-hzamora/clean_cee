# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\Lamas_Horizontales.pyc
# Compiled at: 2015-05-29 10:08:18
"""
Modulo: Lamas_Horizontales.py

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


wxID_DIALOG1, wxID_WXLAMAS_HORIZONTALES_BETA_TEXT, wxID_WXLAMAS_HORIZONTALES_BETA_CUADRO, wxID_WXLAMAS_HORIZONTALES_ACEPTAR, wxID_WXLAMAS_HORIZONTALES_BORRAR, wxID_wxLAMAS_HORIZONTALES_IMAGEN, wxID_WXLAMAS_HORIZONTALES_CANCELAR, wxID_WXTRANSMISIVIDAD_Text, wxID_WXTRANSMISIVIDADCuadro, wxID_WXREFLECTIVIDAD_Text, wxID_WXREFLECTIVIDADCuadro, wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICBOX1, wxID_WXUNIDADESTEXT1, wxID_WXUNIDADESTEXT2, wxID_UNIDADESTEXT3 = [ wx.NewId() for _init_ctrls in range(16) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo Lamas_Horizontales.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(465, 202), size=wx.Size(490, 380), style=wx.DEFAULT_DIALOG_STYLE, title=_('Lamas Horizontales'))
        self.SetClientSize(wx.Size(490, 380))
        self.SetBackgroundColour('white')
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=_('Lamas horizontales'), name='staticText1', parent=self, pos=wx.Point(15, 15), size=wx.Size(350, 20), style=0)
        self.staticText1.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.staticText1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticBox1 = wx.StaticBox(id=wxID_DIALOG1STATICBOX1, label=_('Dimensiones'), name='staticBox1', parent=self, pos=wx.Point(15, 45), size=wx.Size(460, 280), style=0)
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticBox1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.imagenLamasHorizontales = wx.StaticBitmap(bitmap=wx.Bitmap(Directorio + '/Imagenes/Fotos_Sombras/Lamas_Horizontales.png', wx.BITMAP_TYPE_PNG), id=wxID_wxLAMAS_HORIZONTALES_IMAGEN, name='imagenLamasHorizontales', parent=self, pos=wx.Point(30, 60), size=wx.Size(229, 200), style=0)
        self.parent = prnt
        Beta = self.parent.Lamas_Horizontales_BETA[0]
        Transmisividad = self.parent.Lamas_Horizontales_BETA[1]
        Reflectividad = self.parent.Lamas_Horizontales_BETA[2]
        self.BETA_Text = wx.StaticText(id=wxID_WXLAMAS_HORIZONTALES_BETA_TEXT, label=_('Ángulo de inclinación'), name='BETA', parent=self, pos=wx.Point(270, 75), size=wx.Size(110, 13), style=0)
        self.BETA_Text.Enable(True)
        self.BETA_Cuadro = wx.TextCtrl(id=wxID_WXLAMAS_HORIZONTALES_BETA_CUADRO, name='BETA', parent=self, pos=wx.Point(385, 73), size=wx.Size(65, 21), style=0, value=Beta)
        self.BETA_Cuadro.Enable(True)
        self.TRANSMISIVIDAD_Text = wx.StaticText(id=wxID_WXTRANSMISIVIDAD_Text, label=_('Transmisividad'), name=_('Transmisividad'), parent=self, pos=wx.Point(270, 125), size=wx.Size(110, 13), style=0)
        self.TRANSMISIVIDAD_Text.Enable(True)
        self.TRANSMISIVIDADCuadro = wx.TextCtrl(id=wxID_WXTRANSMISIVIDADCuadro, name='TransmisividadCuadro', parent=self, pos=wx.Point(385, 123), size=wx.Size(65, 21), style=0, value=str(Transmisividad))
        self.TRANSMISIVIDADCuadro.Enable(True)
        self.REFLECTIVIDAD_Text = wx.StaticText(id=wxID_WXREFLECTIVIDAD_Text, label=_('Reflectividad'), name=_('Reflectividad'), parent=self, pos=wx.Point(270, 175), size=wx.Size(110, 13), style=0)
        self.TRANSMISIVIDAD_Text.Enable(True)
        self.REFLECTIVIDADCuadro = wx.TextCtrl(id=wxID_WXREFLECTIVIDADCuadro, name='ReflectividadCuadro', parent=self, pos=wx.Point(385, 173), size=wx.Size(65, 21), style=0, value=str(Reflectividad))
        self.TRANSMISIVIDADCuadro.Enable(True)
        self.UnidadesText1 = wx.StaticText(id=wxID_WXUNIDADESTEXT1, label=_('º'), name=_('L_TextUnidades'), parent=self, pos=wx.Point(455, 75), size=wx.Size(10, 13), style=0)
        self.aceptar = wx.Button(id=wxID_WXLAMAS_HORIZONTALES_ACEPTAR, label=_('Aceptar'), name='aceptar', parent=self, pos=wx.Point(15, 340), size=wx.Size(75, 23), style=0)
        self.aceptar.Bind(wx.EVT_BUTTON, self.OnAceptarButton, id=wxID_WXLAMAS_HORIZONTALES_ACEPTAR)
        self.cancelar = wx.Button(id=wxID_WXLAMAS_HORIZONTALES_CANCELAR, label=_('Cancelar'), name='cancelar', parent=self, pos=wx.Point(105, 340), size=wx.Size(75, 23), style=0)
        self.cancelar.Bind(wx.EVT_BUTTON, self.OnCancelarButton, id=wxID_WXLAMAS_HORIZONTALES_CANCELAR)
        self.borrar = wx.Button(id=wxID_WXLAMAS_HORIZONTALES_BORRAR, label=_('Borrar'), name='borrar', parent=self, pos=wx.Point(240, 340), size=wx.Size(75, 23), style=0)
        self.borrar.Bind(wx.EVT_BUTTON, self.OnBorrarButton, id=wxID_WXLAMAS_HORIZONTALES_BORRAR)
        self.BETA_Cuadro.SetToolTip(wx.ToolTip(_('Ángulo de inclinación de la lama respecto al eje horizontal.')))
        self.TRANSMISIVIDADCuadro.SetToolTip(wx.ToolTip(_('Transmisividad de la lama. Lama opaca = 0.')))
        self.REFLECTIVIDADCuadro.SetToolTip(wx.ToolTip(_('Reflectividad de la superficie de la lama.')))

    def OnAceptarButton(self, event):
        """
        Metodo: OnAceptarButton

        ARGUMENTOS:
                event:
        """
        Beta = self.BETA_Cuadro.GetValue()
        Transmisividad = self.TRANSMISIVIDADCuadro.GetValue()
        Reflectividad = self.REFLECTIVIDADCuadro.GetValue()
        self.parent.Lamas_Horizontales_BETA = [
         Beta, Transmisividad, Reflectividad]
        if self.parent.Lamas_Horizontales_BETA[0] == '' or self.parent.Lamas_Horizontales_BETA[1] == '' or self.parent.Lamas_Horizontales_BETA[2] == '':
            wx.MessageBox(_('Lamas no definidas'), _('Aviso'))
            self.parent.Lamas_Horizontales_Si = False
            self.parent.Lamas_Horizontales.SetValue(self.parent.Lamas_Horizontales_Si)
            self.parent.Lamas_Horizontales_BETA = ['', 0, 0]
            self.Close()
        else:
            lista_errores = ''
            if ',' in self.parent.Lamas_Horizontales_BETA[0]:
                self.parent.Lamas_Horizontales_BETA[0] = self.parent.Lamas_Horizontales_BETA[0].replace(',', '.')
            if ',' in self.parent.Lamas_Horizontales_BETA[1]:
                self.parent.Lamas_Horizontales_BETA[1] = self.parent.Lamas_Horizontales_BETA[1].replace(',', '.')
            if ',' in self.parent.Lamas_Horizontales_BETA[2]:
                self.parent.Lamas_Horizontales_BETA[2] = self.parent.Lamas_Horizontales_BETA[2].replace(',', '.')
            try:
                float(self.parent.Lamas_Horizontales_BETA[0])
                if float(self.parent.Lamas_Horizontales_BETA[0]) < 0:
                    self.parent.Lamas_Horizontales_BETA[0] = ''
            except (ValueError, TypeError):
                self.parent.Lamas_Horizontales_BETA[0] = ''

            try:
                float(self.parent.Lamas_Horizontales_BETA[1])
                if float(self.parent.Lamas_Horizontales_BETA[1]) < 0 or float(self.parent.Lamas_Horizontales_BETA[1]) > 1:
                    self.parent.Lamas_Horizontales_BETA[1] = ''
            except (ValueError, TypeError):
                self.parent.Lamas_Horizontales_BETA[1] = ''

            try:
                float(self.parent.Lamas_Horizontales_BETA[2])
                if float(self.parent.Lamas_Horizontales_BETA[2]) < 0 or float(self.parent.Lamas_Horizontales_BETA[2]) > 1:
                    self.parent.Lamas_Horizontales_BETA[2] = ''
            except (ValueError, TypeError):
                self.parent.Lamas_Horizontales_BETA[2] = ''

            if self.parent.Lamas_Horizontales_BETA[0] == '':
                lista_errores = 'Ángulo'
            if self.parent.Lamas_Horizontales_BETA[1] == '':
                if lista_errores != '':
                    lista_errores += ', '
                lista_errores += 'transmisividad'
            if self.parent.Lamas_Horizontales_BETA[2] == '':
                if lista_errores != '':
                    lista_errores += ', '
                lista_errores += 'reflectividad'
            if lista_errores != '':
                wx.MessageBox(_('Revise los siguientes campos:\n') + lista_errores, _('Aviso'))
                self.parent.Lamas_Horizontales_Si = False
                self.parent.Lamas_Horizontales.SetValue(self.parent.Lamas_Horizontales_Si)
            else:
                self.parent.Lamas_Horizontales_Si = True
                self.parent.Lamas_Horizontales.SetValue(self.parent.Lamas_Horizontales_Si)
                self.Close()

    def OnBorrarButton(self, event):
        """
        Metodo: OnBorrarButton

        ARGUMENTOS:
                event:
        """
        self.BETA_Cuadro.SetValue('')
        self.TRANSMISIVIDADCuadro.SetValue('0')
        self.REFLECTIVIDADCuadro.SetValue('0')

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