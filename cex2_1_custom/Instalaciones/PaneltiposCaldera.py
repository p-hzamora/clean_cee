# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\PaneltiposCaldera.pyc
# Compiled at: 2014-02-25 15:39:24
"""
Modulo: PaneltiposCaldera.py

"""
import wx
wxID_DIALOG1, wxID_PANEL1MAYOR10RADIO, wxID_PANEL1MENOR10RADIO, wxID_PANEL1TIPOCALDE1RADIO, wxID_PANEL1TIPOCALDE1TEXT, wxID_PANEL1TIPOCALDE2RADIO, wxID_PANEL1TIPOCALDE2TEXT, wxID_PANEL1TIPOCALDE3RADIO, wxID_PANEL1TIPOCALDE3TEXT, wxID_PANEL1TIPOCALDE4RADIO, wxID_PANEL1TIPOCALDE4TEXT, wxID_PANEL1TIPOCALDE5RADIO, wxID_PANEL1TIPOCALDE5TEXT, wxID_PANEL2TIPOCALDE2TEXT, wxID_PANEL1ACEPTARBOTON, wxID_PANEL1CANCELARBOTON, wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICBOX1 = [ wx.NewId() for _init_ctrls in range(18) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo PaneltiposCaldera.py

    """

    def __init__(self, parent, inicio):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
                inicio:
        """
        self._init_ctrls(parent)
        self.iniciaValores(inicio)

    def iniciaValores(self, inicio):
        """
        Metodo: iniciaValores

        ARGUMENTOS:
                inicio:
        """
        self.resultados = []
        for i in inicio:
            self.resultados.append(i)

        self.tipoCalde1Radio.SetValue(self.resultados[0])
        self.tipoCalde2Radio.SetValue(self.resultados[1])
        self.tipoCalde3Radio.SetValue(self.resultados[2])
        self.tipoCalde4Radio.SetValue(self.resultados[3])
        self.tipoCalde5Radio.SetValue(self.resultados[4])
        self.menor10MetrosRadio.SetValue(self.resultados[5])
        self.mayor10MetrosRadio.SetValue(self.resultados[6])
        self.OnTipoCalderaRadios(None)
        return

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(110, 180), size=wx.Size(580, 340), style=wx.DEFAULT_DIALOG_STYLE, title=_('Características de la caldera'))
        self.SetBackgroundColour('white')
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=_('Características de la caldera'), name='staticText1', parent=self, pos=wx.Point(15, 15), size=wx.Size(350, 20), style=0)
        self.staticText1.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.staticText1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticBox1 = wx.StaticBox(id=wxID_DIALOG1STATICBOX1, label=_('Definir las características de la caldera'), name='staticText1', parent=self, pos=wx.Point(15, 45), size=wx.Size(540, 220), style=0)
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticBox1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.tipoCalde1Radio = wx.RadioButton(id=wxID_PANEL1TIPOCALDE1RADIO, label='', name='tipoCalde1Radio', parent=self, pos=wx.Point(30, 70), size=wx.Size(12, 13), style=wx.RB_GROUP)
        self.tipoCalde1Radio.Bind(wx.EVT_RADIOBUTTON, self.OnTipoCalderaRadios, id=wxID_PANEL1TIPOCALDE1RADIO)
        self.tipoCalde1Text = wx.StaticText(id=wxID_PANEL1TIPOCALDE1TEXT, label=_('Utiliza  combustibles  líquidos o  gaseosos  con  ventilador  antes de  la  cámara de combustión y  cierre \nautomático de la entrada con el quemador apagado'), name='tipoCalde1Text', parent=self, pos=wx.Point(45, 65), size=wx.Size(505, 30), style=0)
        self.tipoCalde2Radio = wx.RadioButton(id=wxID_PANEL1TIPOCALDE2RADIO, label='', name='tipoCalde2Radio', parent=self, pos=wx.Point(30, 110), size=wx.Size(12, 13), style=0)
        self.tipoCalde2Radio.Bind(wx.EVT_RADIOBUTTON, self.OnTipoCalderaRadios, id=wxID_PANEL1TIPOCALDE2RADIO)
        self.tipoCalde2Text = wx.StaticText(id=wxID_PANEL2TIPOCALDE2TEXT, label=_('Quemadores con premezclado'), name='tipoCalde2Text', parent=self, pos=wx.Point(45, 110), size=wx.Size(400, 24), style=0)
        self.tipoCalde3Radio = wx.RadioButton(id=wxID_PANEL1TIPOCALDE3RADIO, label='', name='tipoCalde3Radio', parent=self, pos=wx.Point(30, 150), size=wx.Size(12, 13), style=0)
        self.tipoCalde3Radio.Bind(wx.EVT_RADIOBUTTON, self.OnTipoCalderaRadios, id=wxID_PANEL1TIPOCALDE3RADIO)
        self.tipoCalde3Text = wx.StaticText(id=wxID_PANEL1TIPOCALDE3TEXT, label=_('Caldera  mural  a  gas con ventilador y  evacuación de los  productos  de combustión a través del  muro'), name='tipoCalde3Text', parent=self, pos=wx.Point(45, 150), size=wx.Size(505, 28), style=0)
        self.tipoCalde4Radio = wx.RadioButton(id=wxID_PANEL1TIPOCALDE4RADIO, label='', name='tipoCalde4Radio', parent=self, pos=wx.Point(30, 190), size=wx.Size(12, 13), style=0)
        self.tipoCalde4Radio.Bind(wx.EVT_RADIOBUTTON, self.OnTipoCalderaRadios, id=wxID_PANEL1TIPOCALDE4RADIO)
        self.tipoCalde4Text = wx.StaticText(id=wxID_PANEL1TIPOCALDE4TEXT, label=_('Caldera que utiliza combustibles líquidos o gaseosos con el ventilador antes de la cámara de combustión \ny sin cierre de la entrada de aire con quemador apagado'), name='tipoCalde4Text', parent=self, pos=wx.Point(45, 185), size=wx.Size(505, 25), style=0)
        self.tipoCalde5Radio = wx.RadioButton(id=wxID_PANEL1TIPOCALDE5RADIO, label='', name='tipoCalde5Radio', parent=self, pos=wx.Point(30, 230), size=wx.Size(12, 13), style=0)
        self.tipoCalde5Radio.Bind(wx.EVT_RADIOBUTTON, self.OnTipoCalderaRadios, id=wxID_PANEL1TIPOCALDE5RADIO)
        self.tipoCalde5Text = wx.StaticText(id=wxID_PANEL1TIPOCALDE5TEXT, label=_('Caldera atmosférica a gas'), name='tipoCalde5Text', parent=self, pos=wx.Point(45, 230), size=wx.Size(300, 24), style=0)
        self.menor10MetrosRadio = wx.RadioButton(id=wxID_PANEL1MENOR10RADIO, label=_('Altura de la chimenea < 10 m'), name='menor10MetrosRadio', parent=self, pos=wx.Point(360, 210), size=wx.Size(160, 13), style=wx.RB_GROUP)
        self.menor10MetrosRadio.Show(False)
        self.mayor10MetrosRadio = wx.RadioButton(id=wxID_PANEL1MAYOR10RADIO, label=_('Altura de la chimenea > 10 m'), name='mayor10MetrosRadio', parent=self, pos=wx.Point(360, 230), size=wx.Size(160, 13), style=0)
        self.mayor10MetrosRadio.Show(False)
        self.aceptarBoton = wx.Button(id=wxID_PANEL1ACEPTARBOTON, label=_('Aceptar'), name='aceptarBoton', parent=self, pos=wx.Point(15, 280), size=wx.Size(75, 23), style=0)
        self.aceptarBoton.Bind(wx.EVT_BUTTON, self.OnAceptarButton, id=wxID_PANEL1ACEPTARBOTON)
        self.cancelarBoton = wx.Button(id=wxID_PANEL1CANCELARBOTON, label=_('Cancelar'), name='cancelarBoton', parent=self, pos=wx.Point(105, 280), size=wx.Size(75, 23), style=0)
        self.cancelarBoton.Bind(wx.EVT_BUTTON, self.OnCancelarButton, id=wxID_PANEL1CANCELARBOTON)

    def OnTipoCalderaRadios(self, event):
        """
        Metodo: OnTipoCalderaRadios

        ARGUMENTOS:
                event:
        """
        if self.tipoCalde4Radio.GetValue() == True or self.tipoCalde5Radio.GetValue() == True:
            self.menor10MetrosRadio.Show(True)
            self.mayor10MetrosRadio.Show(True)
        else:
            self.menor10MetrosRadio.Show(False)
            self.mayor10MetrosRadio.Show(False)

    def OnAceptarButton(self, event):
        """
        Metodo: OnAceptarButton

        ARGUMENTOS:
                event:
        """
        self.resultados = []
        self.resultados.append(self.tipoCalde1Radio.GetValue())
        self.resultados.append(self.tipoCalde2Radio.GetValue())
        self.resultados.append(self.tipoCalde3Radio.GetValue())
        self.resultados.append(self.tipoCalde4Radio.GetValue())
        self.resultados.append(self.tipoCalde5Radio.GetValue())
        self.resultados.append(self.menor10MetrosRadio.GetValue())
        self.resultados.append(self.mayor10MetrosRadio.GetValue())
        self.Close()

    def OnCancelarButton(self, event):
        """
        Metodo: OnCancelarButton

        ARGUMENTOS:
                event:
        """
        self.resultados = []
        self.Close()