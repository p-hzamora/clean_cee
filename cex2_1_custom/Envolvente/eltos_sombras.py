# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\eltos_sombras.pyc
# Compiled at: 2015-02-23 10:39:23
"""
Modulo: eltos_sombras.py

"""
import wx, Envolvente.Voladizos as Voladizos, Envolvente.Retranqueos as Retranqueos, Envolvente.Lamas_Horizontales as Lamas_Horizontales, Envolvente.Lamas_Verticales as Lamas_Verticales, Envolvente.Toldos as Toldos, Envolvente.Lucernarios as Lucernarios
from Envolvente.comprobarCampos import Comprueba

def create(parent, frame):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
                frame:
    """
    return Dialog1(parent, frame)


wxID_DIALOG1, wxID_DIALOG1STATICTEXT1, wxID_WXELTOSSOMBRASVOLADIZO, wxID_WXELTOSSOMBRASRETRANQUEO, wxID_WXELTOSSOMBRASLAMAS_HORIZONTALES, wxID_WXELTOSSOMBRASLAMAS_VERTICALES, wxID_WXELTOSSOMBRASTOLDOS, wxID_WXELTOSSOMBRASLUCERNARIOS, wxID_WXELTOSSOMBRASLUCERNARIOS, wxID_WXELTOSSOMBRASACEPTAR, wxID_WXELTOSSOMBRASBORRAR, wxID_WXELTOSSOMBRASDEFINIR_VOLADIZOS, wxID_WXELTOSSOMBRASDEFINIR_RETRANQUEOS, wxID_WXELTOSSOMBRASDEFINIR_LAMAS_HORIZONTALES, wxID_WXELTOSSOMBRASDEFINIR_LAMAS_VERTICALES, wxID_WXELTOSSOMBRASDEFINIR_TOLDOS, wxID_WXELTOSSOMBRASDEFINIR_LUCERNARIOS, wxID_WXPANEL3PERFILSOMBRASTEXT, wxID_WXPANEL3PERFILSOMBRAS, wxID_DIALOG1STATICBOX1, wxID_WXELTOSSOMBRASOTRO, wxID_PANEL1OTROVALORVERANO, wxID_PANEL1OTROVALORINVIERNO, wxID_PANEL1OTROTEXTINVIERNO, wxID_PANEL1OTROTEXTVERANO = [ wx.NewId() for _init_ctrls in range(25) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo eltos_sombras.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(465, 202), size=wx.Size(465, 318), style=wx.DEFAULT_DIALOG_STYLE, title=_('Elementos de sombreamiento'))
        self.SetClientSize(wx.Size(465, 318))
        self.SetBackgroundColour('white')
        self.Voladizo_L = self.parent.Voladizo_L
        self.Voladizo_H = self.parent.Voladizo_H
        self.Voladizo_D = self.parent.Voladizo_D
        self.Retranqueo_H = self.parent.Retranqueo_H
        self.Retranqueo_W = self.parent.Retranqueo_W
        self.Retranqueo_R = self.parent.Retranqueo_R
        self.Lamas_Horizontales_BETA = self.parent.Lamas_Horizontales_BETA
        self.Lamas_Verticales_BETA = self.parent.Lamas_Verticales_BETA
        self.Toldos_AnguloA = self.parent.Toldos_AnguloA
        self.Toldos_OpacoA = self.parent.Toldos_OpacoA
        self.Toldos_TranslucidoA = self.parent.Toldos_TranslucidoA
        self.Toldos_AnguloB = self.parent.Toldos_AnguloB
        self.Toldos_OpacoB = self.parent.Toldos_OpacoB
        self.Toldos_TranslucidoB = self.parent.Toldos_TranslucidoB
        self.Lucernarios_X = self.parent.Lucernarios_X
        self.Lucernarios_Y = self.parent.Lucernarios_Y
        self.Lucernarios_Z = self.parent.Lucernarios_Z
        if self.Voladizo_L != '' and self.Voladizo_D != '' and self.Voladizo_H != '':
            self.Voladizos_Si = True
        else:
            self.Voladizos_Si = False
        if self.Retranqueo_H != '' and self.Retranqueo_W != '' and self.Retranqueo_R != '':
            self.Retranqueos_Si = True
        else:
            self.Retranqueos_Si = False
        if self.Lamas_Horizontales_BETA[0] != '':
            self.Lamas_Horizontales_Si = True
        else:
            self.Lamas_Horizontales_Si = False
        if self.Lamas_Verticales_BETA[0] != '':
            self.Lamas_Verticales_Si = True
        else:
            self.Lamas_Verticales_Si = False
        if self.Toldos_AnguloA != '' and (self.Toldos_OpacoA == True or self.Toldos_TranslucidoA == True) or self.Toldos_AnguloB != '' and (self.Toldos_OpacoB == True or self.Toldos_TranslucidoB == True):
            self.Toldos_Si = True
        else:
            self.Toldos_Si = False
        if self.Lucernarios_X != '' and self.Lucernarios_Y != '' and self.Lucernarios_Z != '':
            self.Lucernarios_Si = True
        else:
            self.Lucernarios_Si = False
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=_('Elementos de sombreamiento'), name='staticText1', parent=self, pos=wx.Point(15, 15), size=wx.Size(350, 20), style=0)
        self.staticText1.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.staticText1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticBox1 = wx.StaticBox(id=wxID_DIALOG1STATICBOX1, label=_('Seleccionar los elementos de sombreamientos correspondientes'), name='staticText1', parent=self, pos=wx.Point(15, 45), size=wx.Size(435, 220), style=0)
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticBox1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.Voladizo = wx.CheckBox(id=wxID_WXELTOSSOMBRASVOLADIZO, label=_('  Voladizo'), name='Voladizo', parent=self, pos=wx.Point(30, 70), size=wx.Size(125, 20), style=0)
        self.Voladizo.Enable(True)
        self.Voladizo.SetValue(self.Voladizos_Si)
        self.Voladizo.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Voladizo.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.Voladizo.Bind(wx.EVT_CHECKBOX, self.OnVoladizos, id=wxID_WXELTOSSOMBRASVOLADIZO)
        self.definir_voladizos = wx.Button(id=wxID_WXELTOSSOMBRASDEFINIR_VOLADIZOS, label=_('Definir'), name='definir_voladizos', parent=self, pos=wx.Point(190, 72), size=wx.Size(75, 15), style=0)
        self.definir_voladizos.Bind(wx.EVT_BUTTON, self.OnDefinirVoladizos, id=wxID_WXELTOSSOMBRASDEFINIR_VOLADIZOS)
        self.Retranqueo = wx.CheckBox(id=wxID_WXELTOSSOMBRASRETRANQUEO, label=_('  Retranqueo'), name='Retranqueo', parent=self, pos=wx.Point(30, 95), size=wx.Size(125, 20), style=0)
        self.Retranqueo.Enable(True)
        self.Retranqueo.SetValue(self.Retranqueos_Si)
        self.Retranqueo.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Retranqueo.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.Retranqueo.Bind(wx.EVT_CHECKBOX, self.OnRetranqueos, id=wxID_WXELTOSSOMBRASRETRANQUEO)
        self.definir_retranqueos = wx.Button(id=wxID_WXELTOSSOMBRASDEFINIR_RETRANQUEOS, label=_('Definir'), name='definir_retranqueos', parent=self, pos=wx.Point(190, 97), size=wx.Size(75, 15), style=0)
        self.definir_retranqueos.Enable(True)
        self.definir_retranqueos.Bind(wx.EVT_BUTTON, self.OnDefinirRetranqueos, id=wxID_WXELTOSSOMBRASDEFINIR_RETRANQUEOS)
        self.Lamas_Horizontales = wx.CheckBox(id=wxID_WXELTOSSOMBRASLAMAS_HORIZONTALES, label=_('  Lamas horizontales'), name='Lamas_Horizontales', parent=self, pos=wx.Point(30, 120), size=wx.Size(125, 20), style=0)
        self.Lamas_Horizontales.Enable(True)
        self.Lamas_Horizontales.SetValue(self.Lamas_Horizontales_Si)
        self.Lamas_Horizontales.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Lamas_Horizontales.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.Lamas_Horizontales.Bind(wx.EVT_CHECKBOX, self.OnLamas_Horizontales, id=wxID_WXELTOSSOMBRASLAMAS_HORIZONTALES)
        self.definir_Lamas_Horizontales = wx.Button(id=wxID_WXELTOSSOMBRASDEFINIR_LAMAS_HORIZONTALES, label=_('Definir'), name='definir_lamas_horizontales', parent=self, pos=wx.Point(190, 122), size=wx.Size(75, 15), style=0)
        self.definir_Lamas_Horizontales.Enable(True)
        self.definir_Lamas_Horizontales.Bind(wx.EVT_BUTTON, self.OnDefinirLamas_Horizontales, id=wxID_WXELTOSSOMBRASDEFINIR_LAMAS_HORIZONTALES)
        self.Lamas_Verticales = wx.CheckBox(id=wxID_WXELTOSSOMBRASLAMAS_VERTICALES, label=_('  Lamas verticales'), name='Lamas_Verticales', parent=self, pos=wx.Point(30, 145), size=wx.Size(125, 20), style=0)
        self.Lamas_Verticales.Enable(True)
        self.Lamas_Verticales.SetValue(self.Lamas_Verticales_Si)
        self.Lamas_Verticales.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Lamas_Verticales.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.Lamas_Verticales.Bind(wx.EVT_CHECKBOX, self.OnLamas_Verticales, id=wxID_WXELTOSSOMBRASLAMAS_VERTICALES)
        self.definir_Lamas_Verticales = wx.Button(id=wxID_WXELTOSSOMBRASDEFINIR_LAMAS_VERTICALES, label=_('Definir'), name='definir_lamas_verticales', parent=self, pos=wx.Point(190, 147), size=wx.Size(75, 15), style=0)
        self.definir_Lamas_Verticales.Enable(True)
        self.definir_Lamas_Verticales.Bind(wx.EVT_BUTTON, self.OnDefinirLamas_Verticales, id=wxID_WXELTOSSOMBRASDEFINIR_LAMAS_VERTICALES)
        self.Toldos = wx.CheckBox(id=wxID_WXELTOSSOMBRASTOLDOS, label=_('  Toldos'), name='Toldos', parent=self, pos=wx.Point(30, 170), size=wx.Size(125, 20), style=0)
        self.Toldos.Enable(True)
        self.Toldos.SetValue(self.Toldos_Si)
        self.Toldos.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Toldos.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.Toldos.Bind(wx.EVT_CHECKBOX, self.OnToldos, id=wxID_WXELTOSSOMBRASTOLDOS)
        self.definir_Toldos = wx.Button(id=wxID_WXELTOSSOMBRASDEFINIR_TOLDOS, label=_('Definir'), name='definir_toldos', parent=self, pos=wx.Point(190, 172), size=wx.Size(75, 15), style=0)
        self.definir_Toldos.Enable(True)
        self.definir_Toldos.Bind(wx.EVT_BUTTON, self.OnDefinirToldos, id=wxID_WXELTOSSOMBRASDEFINIR_TOLDOS)
        self.Lucernarios = wx.CheckBox(id=wxID_WXELTOSSOMBRASLUCERNARIOS, label=_('  Lucernarios'), name='Lucernarios', parent=self, pos=wx.Point(30, 195), size=wx.Size(125, 20), style=0)
        self.Lucernarios.Enable(True)
        self.Lucernarios.SetValue(self.Lucernarios_Si)
        self.Lucernarios.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Lucernarios.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.Lucernarios.Bind(wx.EVT_CHECKBOX, self.OnLucernarios, id=wxID_WXELTOSSOMBRASLUCERNARIOS)
        self.definir_Lucernarios = wx.Button(id=wxID_WXELTOSSOMBRASDEFINIR_LUCERNARIOS, label=_('Definir'), name='definir_LUCERNARIOS', parent=self, pos=wx.Point(190, 197), size=wx.Size(75, 15), style=0)
        self.definir_Lucernarios.Enable(True)
        self.definir_Lucernarios.Bind(wx.EVT_BUTTON, self.OnDefinirLucernarios, id=wxID_WXELTOSSOMBRASDEFINIR_LUCERNARIOS)
        self.Otro = wx.CheckBox(id=wxID_WXELTOSSOMBRASOTRO, label=_('  Corrector del factor solar'), name='Otro', parent=self, pos=wx.Point(30, 240), size=wx.Size(150, 20), style=0)
        self.Otro.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Otro.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.Otro.Bind(wx.EVT_CHECKBOX, self.OnOtro, id=wxID_WXELTOSSOMBRASOTRO)
        self.otroTextInvierno = wx.StaticText(id=wxID_PANEL1OTROTEXTINVIERNO, label=_('Invierno'), name='descripcionText', parent=self, pos=wx.Point(200, 223), size=wx.Size(150, 13), style=0)
        self.otroTextVerano = wx.StaticText(id=wxID_PANEL1OTROTEXTVERANO, label=_('Verano'), name='descripcionText', parent=self, pos=wx.Point(273, 223), size=wx.Size(150, 13), style=0)
        self.otroValorInvierno = wx.TextCtrl(id=wxID_PANEL1OTROVALORINVIERNO, name='otroValorInvierno', parent=self, pos=wx.Point(190, 238), size=wx.Size(56, 21), style=0, value=self.parent.OtroInvierno)
        self.otroValorVerano = wx.TextCtrl(id=wxID_PANEL1OTROVALORVERANO, name='otroValorVerano', parent=self, pos=wx.Point(265, 238), size=wx.Size(56, 21), style=0, value=self.parent.OtroVerano)
        if self.otroValorInvierno.GetValue() != '' and self.otroValorVerano.GetValue() != '':
            self.Otro_Si = True
        else:
            self.Otro_Si = False
        self.Otro.SetValue(self.Otro_Si)
        self.OnOtro(None)
        self.aceptar = wx.Button(id=wxID_WXELTOSSOMBRASACEPTAR, label=_('Aceptar'), name='aceptar', parent=self, pos=wx.Point(15, 280), size=wx.Size(75, 23), style=0)
        self.aceptar.Bind(wx.EVT_BUTTON, self.OnAceptarButton, id=wxID_WXELTOSSOMBRASACEPTAR)
        self.borrar = wx.Button(id=wxID_WXELTOSSOMBRASBORRAR, label=_('Borrar todos'), name='borrar', parent=self, pos=wx.Point(105, 280), size=wx.Size(75, 23), style=0)
        self.borrar.Bind(wx.EVT_BUTTON, self.OnBorrarButton, id=wxID_WXELTOSSOMBRASBORRAR)
        self.definir_voladizos.SetToolTip(wx.ToolTip(_('Defina las características del voladizo.')))
        self.definir_retranqueos.SetToolTip(wx.ToolTip(_('Defina las características del retranqueo.')))
        self.definir_Lamas_Horizontales.SetToolTip(wx.ToolTip(_('Defina las características de las lamas horizontales.')))
        self.definir_Lamas_Verticales.SetToolTip(wx.ToolTip(_('Defina las características de las lamas verticales.')))
        self.definir_Toldos.SetToolTip(wx.ToolTip(_('Defina las características del toldo.')))
        self.definir_Lucernarios.SetToolTip(wx.ToolTip(_('Defina las características de los lucernarios.')))
        self.Voladizo.SetToolTip(wx.ToolTip(_('Si se encuentra activado indica la existencia de un voladizo.')))
        self.Retranqueo.SetToolTip(wx.ToolTip(_('Si se encuentra activado indica la existencia de un retranqueo.')))
        self.Lamas_Horizontales.SetToolTip(wx.ToolTip(_('Si se encuentra activado indica la existencia de unas lamas horizontales.')))
        self.Lamas_Verticales.SetToolTip(wx.ToolTip(_('Si se encuentra activado indica la existencia de unas lamas verticales.')))
        self.Toldos.SetToolTip(wx.ToolTip(_('Si se encuentra activado indica la existencia de un toldo.')))
        self.Lucernarios.SetToolTip(wx.ToolTip(_('Si se encuentra activado indica la existencia de un lucernario.')))
        return

    def OnVoladizos(self, event):
        """
        Metodo: OnVoladizos

        ARGUMENTOS:
                event):
        """
        self.parent.Voladizos_Si = self.Voladizo.GetValue()
        if self.parent.Voladizos_Si == False:
            self.parent.Voladizo_L = ''
            self.parent.Voladizo_H = ''
            self.parent.Voladizo_D = ''

    def OnDefinirVoladizos(self, event):
        """
        Metodo: OnDefinirVoladizos

        ARGUMENTOS:
                event:
        """
        dlg = Voladizos.create(self)
        dlg.ShowModal()

    def OnRetranqueos(self, event):
        """
        Metodo: OnRetranqueos

        ARGUMENTOS:
                event):
        """
        self.parent.Retranqueos_Si = self.Retranqueo.GetValue()
        if self.parent.Retranqueos_Si == False:
            self.parent.Retranqueo_H = ''
            self.parent.Retranqueo_W = ''
            self.parent.Retranqueo_R = ''

    def OnDefinirRetranqueos(self, event):
        """
        Metodo: OnDefinirRetranqueos

        ARGUMENTOS:
                event:
        """
        dlg = Retranqueos.create(self)
        dlg.ShowModal()

    def OnLamas_Horizontales(self, event):
        """
        Metodo: OnLamas_Horizontales

        ARGUMENTOS:
                event):
        """
        self.parent.Lamas_Horizontales_Si = self.Lamas_Horizontales.GetValue()
        if self.parent.Lamas_Horizontales_Si == False:
            self.parent.Lamas_Horizontales_BETA = [
             '', 0, 0]

    def OnDefinirLamas_Horizontales(self, event):
        """
        Metodo: OnDefinirLamas_Horizontales

        ARGUMENTOS:
                event:
        """
        dlg = Lamas_Horizontales.create(self)
        dlg.ShowModal()

    def OnLamas_Verticales(self, event):
        """
        Metodo: OnLamas_Verticales

        ARGUMENTOS:
                event):
        """
        self.parent.Lamas_Verticales_Si = self.Lamas_Verticales.GetValue()
        if self.parent.Lamas_Verticales_Si == False:
            self.parent.Lamas_Verticales_BETA = [
             '', 0, 0]

    def OnDefinirLamas_Verticales(self, event):
        """
        Metodo: OnDefinirLamas_Verticales

        ARGUMENTOS:
                event:
        """
        dlg = Lamas_Verticales.create(self)
        dlg.ShowModal()

    def OnToldos(self, event):
        """
        Metodo: OnToldos

        ARGUMENTOS:
                event):
        """
        self.parent.Toldos_Si = self.Toldos.GetValue()
        if self.parent.Toldos_Si == False:
            self.parent.Toldos_AnguloA = ''
            self.parent.Toldos_OpacoA = False
            self.parent.Toldos_TranslucidoA = False
            self.parent.Toldos_AnguloB = ''
            self.parent.Toldos_OpacoB = False
            self.parent.Toldos_TranslucidoB = False

    def OnDefinirToldos(self, event):
        """
        Metodo: OnDefinirToldos

        ARGUMENTOS:
                event:
        """
        dlg = Toldos.create(self)
        dlg.ShowModal()

    def OnLucernarios(self, event):
        """
        Metodo: OnLucernarios

        ARGUMENTOS:
                event:
        """
        self.parent.Lucernarios_Si = self.Lucernarios.GetValue()
        if self.parent.Lucernarios_Si == False:
            self.parent.Lucernarios_X = self.parent.Lucernarios_X
            self.parent.Lucernarios_Y = self.parent.Lucernarios_Y
            self.parent.Lucernarios_Z = self.parent.Lucernarios_Z

    def OnOtro(self, event):
        """
        Metodo: OnOtro

        ARGUMENTOS:
                event):
        """
        if self.Otro.GetValue() == True:
            self.otroValorInvierno.Show(True)
            self.otroValorVerano.Show(True)
            self.otroTextInvierno.Show(True)
            self.otroTextVerano.Show(True)
        else:
            self.otroValorInvierno.Show(False)
            self.otroValorVerano.Show(False)
            self.otroTextInvierno.Show(False)
            self.otroTextVerano.Show(False)

    def OnDefinirLucernarios(self, event):
        """
        Metodo: OnDefinirLucernarios

        ARGUMENTOS:
                event:
        """
        dlg = Lucernarios.create(self)
        dlg.ShowModal()

    def OnAceptarButton(self, event):
        """
        Metodo: OnAceptarButton

        ARGUMENTOS:
                event:
        """
        if self.Voladizo.GetValue() == True:
            self.parent.Voladizo_L = self.Voladizo_L
            self.parent.Voladizo_H = self.Voladizo_H
            self.parent.Voladizo_D = self.Voladizo_D
        else:
            self.parent.Voladizo_L = ''
            self.parent.Voladizo_H = ''
            self.parent.Voladizo_D = ''
        if self.Retranqueo.GetValue() == True:
            self.parent.Retranqueo_H = self.Retranqueo_H
            self.parent.Retranqueo_W = self.Retranqueo_W
            self.parent.Retranqueo_R = self.Retranqueo_R
        else:
            self.parent.Retranqueo_H = ''
            self.parent.Retranqueo_W = ''
            self.parent.Retranqueo_R = ''
        if self.Lamas_Horizontales.GetValue() == True:
            self.parent.Lamas_Horizontales_BETA = self.Lamas_Horizontales_BETA
        else:
            self.parent.Lamas_Horizontales_BETA = [
             '', 0, 0]
        if self.Lamas_Verticales.GetValue() == True:
            self.parent.Lamas_Verticales_BETA = self.Lamas_Verticales_BETA
        else:
            self.parent.Lamas_Verticales_BETA = [
             '', 0, 0]
        if self.Toldos.GetValue() == True:
            self.parent.Toldos_AnguloA = self.Toldos_AnguloA
            self.parent.Toldos_OpacoA = self.Toldos_OpacoA
            self.parent.Toldos_TranslucidoA = self.Toldos_TranslucidoA
            self.parent.Toldos_AnguloB = self.Toldos_AnguloB
            self.parent.Toldos_OpacoB = self.Toldos_OpacoB
            self.parent.Toldos_TranslucidoB = self.Toldos_TranslucidoB
        else:
            self.parent.Toldos_AnguloA = ''
            self.parent.Toldos_OpacoA = False
            self.parent.Toldos_TranslucidoA = False
            self.parent.Toldos_AnguloB = ''
            self.parent.Toldos_OpacoB = False
            self.parent.Toldos_TranslucidoB = False
        if self.Lucernarios.GetValue() == True:
            self.parent.Lucernarios_X = self.Lucernarios_X
            self.parent.Lucernarios_Y = self.Lucernarios_Y
            self.parent.Lucernarios_Z = self.Lucernarios_Z
        else:
            self.parent.Lucernarios_X = ''
            self.parent.Lucernarios_Y = ''
            self.parent.Lucernarios_Z = ''
        self.parent.Voladizos_Si = self.Voladizo.GetValue()
        self.parent.Retranqueos_Si = self.Retranqueo.GetValue()
        self.parent.Lamas_Horizontales_Si = self.Lamas_Horizontales.GetValue()
        self.parent.Lamas_Verticales_Si = self.Lamas_Verticales.GetValue()
        self.parent.Toldos_Si = self.Toldos.GetValue()
        self.parent.Lucernarios_Si = self.Lucernarios.GetValue()
        if self.Otro.GetValue() == True:
            listaErrores = ''
            otroValor = self.otroValorInvierno.GetValue()
            if ',' in otroValor:
                otroValor = otroValor.replace(',', '.')
                self.otroValorInvierno.SetValue(otroValor)
            listaErrores += Comprueba(self.otroValorInvierno.GetValue(), 2, listaErrores, _('corrector del factor solar de invierno'), 0.0, 1.0).ErrorDevuelto
            otroValor = self.otroValorVerano.GetValue()
            if ',' in otroValor:
                otroValor = otroValor.replace(',', '.')
                self.otroValorVerano.SetValue(otroValor)
            listaErrores += Comprueba(self.otroValorVerano.GetValue(), 2, listaErrores, _('corrector del factor solar de verano'), 0.0, 1.0).ErrorDevuelto
            if listaErrores != '':
                wx.MessageBox(_('Revise los siguientes campos:\n') + listaErrores, _('Aviso'))
                return
            self.parent.Otro_Si = True
            self.parent.OtroInvierno = self.otroValorInvierno.GetValue()
            self.parent.OtroVerano = self.otroValorVerano.GetValue()
        else:
            self.parent.Otro_Si = False
            self.parent.OtroInvierno = ''
            self.parent.OtroVerano = ''
        self.Close()

    def OnBorrarButton(self, event):
        """
        Metodo: OnBorrarButton

        ARGUMENTOS:
                event:
        """
        self.Voladizo_L = ''
        self.Voladizo_H = ''
        self.Voladizo_D = ''
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
        self.otroValorInvierno.SetValue('')
        self.otroValorVerano.SetValue('')
        self.Voladizos_Si = False
        self.Retranqueos_Si = False
        self.Lamas_Horizontales_Si = False
        self.Lamas_Verticales_Si = False
        self.Toldos_Si = False
        self.Lucernarios_Si = False
        self.Otro_Si = False
        self.parent.Voladizo_L = self.Voladizo_L
        self.parent.Voladizo_H = self.Voladizo_H
        self.parent.Voladizo_D = self.Voladizo_D
        self.parent.Retranqueo_H = self.Retranqueo_H
        self.parent.Retranqueo_W = self.Retranqueo_W
        self.parent.Retranqueo_R = self.Retranqueo_R
        self.parent.Lamas_Horizontales_BETA = self.Lamas_Horizontales_BETA
        self.parent.Lamas_Verticales_BETA = self.Lamas_Verticales_BETA
        self.parent.Toldos_AnguloA = self.Toldos_AnguloA
        self.parent.Toldos_OpacoA = self.Toldos_OpacoA
        self.parent.Toldos_TranslucidoA = self.Toldos_TranslucidoA
        self.parent.Toldos_AnguloB = self.Toldos_AnguloB
        self.parent.Toldos_OpacoB = self.Toldos_OpacoB
        self.parent.Toldos_TranslucidoB = self.Toldos_TranslucidoB
        self.parent.Lucernarios_X = self.Lucernarios_X
        self.parent.Lucernarios_Y = self.Lucernarios_Y
        self.parent.Lucernarios_Z = self.Lucernarios_Z
        self.parent.OtroInvierno = self.otroValorInvierno.GetValue()
        self.parent.OtroVerano = self.otroValorVerano.GetValue()
        self.parent.Voladizos_Si = self.Voladizos_Si
        self.parent.Retranqueos_Si = self.Retranqueos_Si
        self.parent.Lamas_Horizontales_Si = self.Lamas_Horizontales_Si
        self.parent.Lamas_Verticales_Si = self.Lamas_Verticales_Si
        self.parent.Toldos_Si = self.Toldos_Si
        self.parent.Lucernarios_Si = self.Lucernarios_Si
        self.parent.Otro_Si = self.Otro_Si
        self.Voladizo.SetValue(self.Voladizos_Si)
        self.Retranqueo.SetValue(self.Retranqueos_Si)
        self.Lamas_Horizontales.SetValue(self.Lamas_Horizontales_Si)
        self.Lamas_Verticales.SetValue(self.Lamas_Verticales_Si)
        self.Toldos.SetValue(self.Toldos_Si)
        self.Lucernarios.SetValue(self.Lucernarios_Si)
        self.Otro.SetValue(self.Otro_Si)

    def __init__(self, parent, frame):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
                frame:
        """
        self.frame = frame
        self.parent = parent
        self._init_ctrls(parent)