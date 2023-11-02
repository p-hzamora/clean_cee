# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: MedidasDeMejora\ventanaPT.pyc
# Compiled at: 2015-02-23 10:36:08
"""
Modulo: ventanaPT.py

"""
import wx
from Envolvente.comprobarCampos import Comprueba

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return Dialog1(parent)


wxID_DIALOG1, wxID_DIALOG1ACEPTARBOTON, wxID_DIALOG1CAJAPERSIANACHECK, wxID_DIALOG1CANCELARBOTON, wxID_DIALOG1CONTORNOHUECOCHECK, wxID_DIALOG1DESCRIPCION, wxID_DIALOG1DESCRIPCIONTEXT, wxID_DIALOG1FACHADACUBIERTACHECK, wxID_DIALOG1FACHADAFORJADOCHECK, wxID_DIALOG1FACHADAPARTICIONCHECK, wxID_DIALOG1FACHADASOLERACHECK, wxID_DIALOG1FACHADASUELOCHECK, wxID_DIALOG1FACHADAVOLADIZOCHECK, wxID_DIALOG1PILARENESQUINACHECK, wxID_DIALOG1PILARENFACHADACHECK, wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICTEXT10, wxID_DIALOG1STATICTEXT11, wxID_DIALOG1STATICTEXT12, wxID_DIALOG1STATICTEXT13, wxID_DIALOG1STATICTEXT14, wxID_DIALOG1STATICTEXT15, wxID_DIALOG1STATICTEXT16, wxID_DIALOG1STATICTEXT17, wxID_DIALOG1STATICTEXT18, wxID_DIALOG1STATICTEXT19, wxID_DIALOG1STATICTEXT2, wxID_DIALOG1STATICTEXT20, wxID_DIALOG1STATICTEXT3, wxID_DIALOG1STATICTEXT4, wxID_DIALOG1STATICTEXT5, wxID_DIALOG1STATICTEXT6, wxID_DIALOG1STATICTEXT7, wxID_DIALOG1STATICTEXT8, wxID_DIALOG1STATICTEXT9, wxID_DIALOG1TEXTCTRL1, wxID_DIALOG1TEXTCTRL10, wxID_DIALOG1TEXTCTRL2, wxID_DIALOG1TEXTCTRL3, wxID_DIALOG1TEXTCTRL4, wxID_DIALOG1TEXTCTRL5, wxID_DIALOG1TEXTCTRL6, wxID_DIALOG1TEXTCTRL7, wxID_DIALOG1TEXTCTRL8, wxID_DIALOG1TEXTCTRL9, wxID_DIALOG1TITULOTEXT, wxID_STATICBOX1 = [ wx.NewId() for _init_ctrls in range(47) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo ventanaPT.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                 prnt:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(0, 0), size=wx.Size(452, 407), style=wx.DEFAULT_DIALOG_STYLE, title=_('Cuadro incluir mejoras en Puentes Térmicos'))
        self.SetClientSize(wx.Size(452, 407))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tituloText = wx.StaticText(id=wxID_DIALOG1TITULOTEXT, label=_('Medida de mejora de los puentes térmicos'), name='tituloText', parent=self, pos=wx.Point(15, 15), size=wx.Size(270, 18), style=0)
        self.tituloText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.tituloText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.descripcionText = wx.StaticText(id=wxID_DIALOG1DESCRIPCIONTEXT, label=_('Nombre'), name='descripcionText', parent=self, pos=wx.Point(30, 50), size=wx.Size(68, 13), style=0)
        self.descripcion = wx.TextCtrl(id=wxID_DIALOG1DESCRIPCION, name='descripcion', parent=self, pos=wx.Point(150, 48), size=wx.Size(287, 21), style=0, value='')
        self.staticBox1 = wx.StaticBox(id=wxID_STATICBOX1, label=_('Definir nuevos valores de los puentes térmicos'), name='staticBox1', parent=self, pos=wx.Point(15, 80), size=wx.Size(422, 274), style=0)
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.staticBox1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.pilarEnFachadaCheck = wx.CheckBox(id=wxID_DIALOG1PILARENFACHADACHECK, label=_('Pilar integrado en fachada'), name='pilarEnFachadaCheck', parent=self, pos=wx.Point(30, 104), size=wx.Size(168, 13), style=0)
        self.pilarEnFachadaCheck.Bind(wx.EVT_CHECKBOX, self.OnCambiosChecks, id=wxID_DIALOG1PILARENFACHADACHECK)
        self.pilarEnFachadaCheck.SetValue(False)
        self.pilarEnEsquinaCheck = wx.CheckBox(id=wxID_DIALOG1PILARENESQUINACHECK, label=_('Pilar en esquina'), name='pilarEnEsquinaCheck', parent=self, pos=wx.Point(30, 128), size=wx.Size(112, 13), style=0)
        self.pilarEnEsquinaCheck.Bind(wx.EVT_CHECKBOX, self.OnCambiosChecks, id=wxID_DIALOG1PILARENESQUINACHECK)
        self.pilarEnEsquinaCheck.SetValue(False)
        self.contornoHuecoCheck = wx.CheckBox(id=wxID_DIALOG1CONTORNOHUECOCHECK, label=_('Contorno de hueco'), name='contornoHuecoCheck', parent=self, pos=wx.Point(30, 152), size=wx.Size(128, 13), style=0)
        self.contornoHuecoCheck.Bind(wx.EVT_CHECKBOX, self.OnCambiosChecks, id=wxID_DIALOG1CONTORNOHUECOCHECK)
        self.contornoHuecoCheck.SetValue(False)
        self.cajaPersianaCheck = wx.CheckBox(id=wxID_DIALOG1CAJAPERSIANACHECK, label=_('Caja de persiana'), name='cajaPersianaCheck', parent=self, pos=wx.Point(30, 176), size=wx.Size(112, 13), style=0)
        self.cajaPersianaCheck.Bind(wx.EVT_CHECKBOX, self.OnCambiosChecks, id=wxID_DIALOG1CAJAPERSIANACHECK)
        self.cajaPersianaCheck.SetValue(False)
        self.fachadaForjadoCheck = wx.CheckBox(id=wxID_DIALOG1FACHADAFORJADOCHECK, label=_('Encuentro de fachada con forjado'), name='fachadaForjadoCheck', parent=self, pos=wx.Point(30, 200), size=wx.Size(192, 13), style=0)
        self.fachadaForjadoCheck.Bind(wx.EVT_CHECKBOX, self.OnCambiosChecks, id=wxID_DIALOG1FACHADAFORJADOCHECK)
        self.fachadaForjadoCheck.SetValue(False)
        self.fachadaVoladizoCheck = wx.CheckBox(id=wxID_DIALOG1FACHADAVOLADIZOCHECK, label=_('Encuentro de fachada con voladizo'), name='fachadaVoladizoCheck', parent=self, pos=wx.Point(30, 224), size=wx.Size(184, 13), style=0)
        self.fachadaVoladizoCheck.Bind(wx.EVT_CHECKBOX, self.OnCambiosChecks, id=wxID_DIALOG1FACHADAVOLADIZOCHECK)
        self.fachadaVoladizoCheck.SetValue(False)
        self.fachadaCubiertaCheck = wx.CheckBox(id=wxID_DIALOG1FACHADACUBIERTACHECK, label=_('Encuentro de fachada con cubierta'), name='fachadaCubiertaCheck', parent=self, pos=wx.Point(30, 248), size=wx.Size(184, 13), style=0)
        self.fachadaCubiertaCheck.Bind(wx.EVT_CHECKBOX, self.OnCambiosChecks, id=wxID_DIALOG1FACHADACUBIERTACHECK)
        self.fachadaCubiertaCheck.SetValue(False)
        self.fachadaSueloCheck = wx.CheckBox(id=wxID_DIALOG1FACHADASUELOCHECK, label=_('Encuentro de fachada con suelo en contacto con aire'), name='fachadaSueloCheck', parent=self, pos=wx.Point(30, 272), size=wx.Size(272, 13), style=0)
        self.fachadaSueloCheck.Bind(wx.EVT_CHECKBOX, self.OnCambiosChecks, id=wxID_DIALOG1FACHADASUELOCHECK)
        self.fachadaSueloCheck.SetValue(False)
        self.fachadaSoleraCheck = wx.CheckBox(id=wxID_DIALOG1FACHADASOLERACHECK, label=_('Encuentro de fachada con solera'), name='fachadaSoleraCheck', parent=self, pos=wx.Point(30, 296), size=wx.Size(200, 13), style=0)
        self.fachadaSoleraCheck.Bind(wx.EVT_CHECKBOX, self.OnCambiosChecks, id=wxID_DIALOG1FACHADASOLERACHECK)
        self.fachadaSoleraCheck.SetValue(False)
        self.fachadaParticionCheck = wx.CheckBox(id=wxID_DIALOG1FACHADAPARTICIONCHECK, label=_('Encuentro de fachada con partición interior'), name='fachadaParticionCheck', parent=self, pos=wx.Point(30, 320), size=wx.Size(232, 13), style=0)
        self.fachadaParticionCheck.Bind(wx.EVT_CHECKBOX, self.OnCambiosChecks, id=wxID_DIALOG1FACHADAPARTICIONCHECK)
        self.fachadaParticionCheck.SetValue(False)
        self.fachadaParticionCheck.Show(False)
        self.textCtrl1 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1, name='textCtrl1', parent=self, pos=wx.Point(338, 102), size=wx.Size(56, 21), style=0, value='')
        self.textCtrl1.Enable(False)
        self.textCtrl2 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2, name='textCtrl2', parent=self, pos=wx.Point(338, 126), size=wx.Size(56, 21), style=0, value='')
        self.textCtrl2.Enable(False)
        self.textCtrl3 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL3, name='textCtrl3', parent=self, pos=wx.Point(338, 150), size=wx.Size(56, 21), style=0, value='')
        self.textCtrl3.Enable(False)
        self.textCtrl4 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL4, name='textCtrl4', parent=self, pos=wx.Point(338, 174), size=wx.Size(56, 21), style=0, value='')
        self.textCtrl4.Enable(False)
        self.textCtrl5 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL5, name='textCtrl5', parent=self, pos=wx.Point(338, 198), size=wx.Size(56, 21), style=0, value='')
        self.textCtrl5.Enable(False)
        self.textCtrl6 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL6, name='textCtrl6', parent=self, pos=wx.Point(338, 222), size=wx.Size(56, 21), style=0, value='')
        self.textCtrl6.Enable(False)
        self.textCtrl7 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL7, name='textCtrl7', parent=self, pos=wx.Point(338, 246), size=wx.Size(56, 21), style=0, value='')
        self.textCtrl7.Enable(False)
        self.textCtrl8 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL8, name='textCtrl8', parent=self, pos=wx.Point(338, 270), size=wx.Size(56, 21), style=0, value='')
        self.textCtrl8.Enable(False)
        self.textCtrl9 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL9, name='textCtrl9', parent=self, pos=wx.Point(338, 294), size=wx.Size(56, 21), style=0, value='')
        self.textCtrl9.Enable(False)
        self.textCtrl10 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL10, name='textCtrl10', parent=self, pos=wx.Point(338, 318), size=wx.Size(56, 21), style=0, value='')
        self.textCtrl10.Enable(False)
        self.textCtrl10.Show(False)
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=_('φ'), name='staticText1', parent=self, pos=wx.Point(320, 128), size=wx.Size(16, 13), style=0)
        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2, label=_('φ'), name='staticText2', parent=self, pos=wx.Point(320, 152), size=wx.Size(16, 13), style=0)
        self.staticText3 = wx.StaticText(id=wxID_DIALOG1STATICTEXT3, label=_('φ'), name='staticText3', parent=self, pos=wx.Point(320, 176), size=wx.Size(16, 13), style=0)
        self.staticText4 = wx.StaticText(id=wxID_DIALOG1STATICTEXT4, label=_('φ'), name='staticText4', parent=self, pos=wx.Point(320, 200), size=wx.Size(16, 13), style=0)
        self.staticText5 = wx.StaticText(id=wxID_DIALOG1STATICTEXT5, label=_('φ'), name='staticText5', parent=self, pos=wx.Point(320, 224), size=wx.Size(16, 13), style=0)
        self.staticText6 = wx.StaticText(id=wxID_DIALOG1STATICTEXT6, label=_('φ'), name='staticText6', parent=self, pos=wx.Point(320, 248), size=wx.Size(16, 13), style=0)
        self.staticText7 = wx.StaticText(id=wxID_DIALOG1STATICTEXT7, label=_('φ'), name='staticText7', parent=self, pos=wx.Point(320, 272), size=wx.Size(16, 13), style=0)
        self.staticText8 = wx.StaticText(id=wxID_DIALOG1STATICTEXT8, label=_('φ'), name='staticText8', parent=self, pos=wx.Point(320, 296), size=wx.Size(16, 13), style=0)
        self.staticText9 = wx.StaticText(id=wxID_DIALOG1STATICTEXT9, label=_('φ'), name='staticText9', parent=self, pos=wx.Point(320, 320), size=wx.Size(16, 13), style=0)
        self.staticText9.Show(False)
        self.staticText10 = wx.StaticText(id=wxID_DIALOG1STATICTEXT10, label=_('φ'), name='staticText10', parent=self, pos=wx.Point(320, 104), size=wx.Size(16, 13), style=0)
        self.staticText11 = wx.StaticText(id=wxID_DIALOG1STATICTEXT11, label=_('W/mK'), name='staticText11', parent=self, pos=wx.Point(399, 128), size=wx.Size(28, 13), style=0)
        self.staticText12 = wx.StaticText(id=wxID_DIALOG1STATICTEXT12, label=_('W/mK'), name='staticText12', parent=self, pos=wx.Point(399, 152), size=wx.Size(28, 13), style=0)
        self.staticText13 = wx.StaticText(id=wxID_DIALOG1STATICTEXT13, label=_('W/mK'), name='staticText13', parent=self, pos=wx.Point(399, 176), size=wx.Size(28, 13), style=0)
        self.staticText14 = wx.StaticText(id=wxID_DIALOG1STATICTEXT14, label=_('W/mK'), name='staticText14', parent=self, pos=wx.Point(399, 200), size=wx.Size(28, 13), style=0)
        self.staticText15 = wx.StaticText(id=wxID_DIALOG1STATICTEXT15, label=_('W/mK'), name='staticText15', parent=self, pos=wx.Point(399, 224), size=wx.Size(28, 13), style=0)
        self.staticText16 = wx.StaticText(id=wxID_DIALOG1STATICTEXT16, label=_('W/mK'), name='staticText16', parent=self, pos=wx.Point(399, 248), size=wx.Size(28, 13), style=0)
        self.staticText17 = wx.StaticText(id=wxID_DIALOG1STATICTEXT17, label=_('W/mK'), name='staticText17', parent=self, pos=wx.Point(399, 272), size=wx.Size(28, 13), style=0)
        self.staticText18 = wx.StaticText(id=wxID_DIALOG1STATICTEXT18, label=_('W/mK'), name='staticText18', parent=self, pos=wx.Point(399, 296), size=wx.Size(28, 13), style=0)
        self.staticText19 = wx.StaticText(id=wxID_DIALOG1STATICTEXT19, label=_('W/mK'), name='staticText19', parent=self, pos=wx.Point(399, 320), size=wx.Size(28, 13), style=0)
        self.staticText19.Show(False)
        self.staticText20 = wx.StaticText(id=wxID_DIALOG1STATICTEXT20, label=_('W/mK'), name='staticText20', parent=self, pos=wx.Point(399, 104), size=wx.Size(28, 13), style=0)
        self.aceptarBoton = wx.Button(id=wxID_DIALOG1ACEPTARBOTON, label=_('Aceptar'), name='aceptarBoton', parent=self, pos=wx.Point(15, 369), size=wx.Size(75, 23), style=0)
        self.aceptarBoton.Bind(wx.EVT_BUTTON, self.onAceptarBoton, id=wxID_DIALOG1ACEPTARBOTON)
        self.cancelarBoton = wx.Button(id=wxID_DIALOG1CANCELARBOTON, label=_('Cancelar'), name='cancelarBoton', parent=self, pos=wx.Point(105, 369), size=wx.Size(75, 23), style=0)
        self.cancelarBoton.Bind(wx.EVT_BUTTON, self.onCancelarBoton, id=wxID_DIALOG1CANCELARBOTON)

    def __init__(self, parent):
        """
        Constructor de la clase

        ARGUMENTOS:
                 parent:
        """
        self._init_ctrls(parent)
        self.dev = False

    def OnCambiosChecks(self, event):
        """
        Metodo: OnCambiosChecks

        ARGUMENTOS:
                event:
        """
        if self.pilarEnFachadaCheck.GetValue() == True:
            self.textCtrl1.Enable(True)
        else:
            self.textCtrl1.Enable(False)
        if self.pilarEnEsquinaCheck.GetValue() == True:
            self.textCtrl2.Enable(True)
        else:
            self.textCtrl2.Enable(False)
        if self.contornoHuecoCheck.GetValue() == True:
            self.textCtrl3.Enable(True)
        else:
            self.textCtrl3.Enable(False)
        if self.cajaPersianaCheck.GetValue() == True:
            self.textCtrl4.Enable(True)
        else:
            self.textCtrl4.Enable(False)
        if self.fachadaForjadoCheck.GetValue() == True:
            self.textCtrl5.Enable(True)
        else:
            self.textCtrl5.Enable(False)
        if self.fachadaVoladizoCheck.GetValue() == True:
            self.textCtrl6.Enable(True)
        else:
            self.textCtrl6.Enable(False)
        if self.fachadaCubiertaCheck.GetValue() == True:
            self.textCtrl7.Enable(True)
        else:
            self.textCtrl7.Enable(False)
        if self.fachadaSueloCheck.GetValue() == True:
            self.textCtrl8.Enable(True)
        else:
            self.textCtrl8.Enable(False)
        if self.fachadaSoleraCheck.GetValue() == True:
            self.textCtrl9.Enable(True)
        else:
            self.textCtrl9.Enable(False)
        if self.fachadaParticionCheck.GetValue() == True:
            self.textCtrl10.Enable(True)
        else:
            self.textCtrl10.Enable(False)

    def onAceptarBoton(self, event):
        """
        Metodo: onAceptarBoton

        ARGUMENTOS:
                event:
        """
        PT1 = self.textCtrl1.GetValue()
        PT2 = self.textCtrl2.GetValue()
        PT3 = self.textCtrl3.GetValue()
        PT4 = self.textCtrl4.GetValue()
        PT5 = self.textCtrl5.GetValue()
        PT6 = self.textCtrl6.GetValue()
        PT7 = self.textCtrl7.GetValue()
        PT8 = self.textCtrl8.GetValue()
        PT9 = self.textCtrl9.GetValue()
        PT10 = self.textCtrl10.GetValue()
        if ',' in PT1:
            PT1 = PT1.replace(',', '.')
            self.textCtrl1.SetValue(PT1)
        if ',' in PT2:
            PT2 = PT2.replace(',', '.')
            self.textCtrl2.SetValue(PT2)
        if ',' in PT3:
            PT3 = PT3.replace(',', '.')
            self.textCtrl3.SetValue(PT3)
        if ',' in PT4:
            PT4 = PT4.replace(',', '.')
            self.textCtrl4.SetValue(PT4)
        if ',' in PT5:
            PT5 = PT5.replace(',', '.')
            self.textCtrl5.SetValue(PT5)
        if ',' in PT6:
            PT6 = PT6.replace(',', '.')
            self.textCtrl6.SetValue(PT6)
        if ',' in PT7:
            PT7 = PT7.replace(',', '.')
            self.textCtrl7.SetValue(PT7)
        if ',' in PT8:
            PT8 = PT8.replace(',', '.')
            self.textCtrl8.SetValue(PT8)
        if ',' in PT9:
            PT9 = PT9.replace(',', '.')
            self.textCtrl9.SetValue(PT9)
        if ',' in PT10:
            PT10 = PT10.replace(',', '.')
            self.textCtrl10.SetValue(PT10)
        cambios = False
        error = ''
        error += Comprueba(self.descripcion.GetValue(), 0, error, _('nombre')).ErrorDevuelto
        if self.pilarEnFachadaCheck.GetValue() == True:
            cambios = True
            error += Comprueba(self.textCtrl1.GetValue(), 2, error, _('φ de pilar integrado en fachada')).ErrorDevuelto
        if self.pilarEnEsquinaCheck.GetValue() == True:
            cambios = True
            error += Comprueba(self.textCtrl2.GetValue(), 2, error, _('φ de pilar en esquina')).ErrorDevuelto
        if self.contornoHuecoCheck.GetValue() == True:
            cambios = True
            error += Comprueba(self.textCtrl3.GetValue(), 2, error, _('φ de contorno de hueco')).ErrorDevuelto
        if self.cajaPersianaCheck.GetValue() == True:
            cambios = True
            error += Comprueba(self.textCtrl4.GetValue(), 2, error, _('φ de caja de persiana')).ErrorDevuelto
        if self.fachadaForjadoCheck.GetValue() == True:
            cambios = True
            error += Comprueba(self.textCtrl5.GetValue(), 2, error, _('φ de encuentro de fachada con Forjado')).ErrorDevuelto
        if self.fachadaVoladizoCheck.GetValue() == True:
            cambios = True
            error += Comprueba(self.textCtrl6.GetValue(), 2, error, _('φ de encuentro de fachada con voladizo')).ErrorDevuelto
        if self.fachadaCubiertaCheck.GetValue() == True:
            cambios = True
            error += Comprueba(self.textCtrl7.GetValue(), 2, error, _('φ de encuentro de fachada con cubierta')).ErrorDevuelto
        if self.fachadaSueloCheck.GetValue() == True:
            cambios = True
            error += Comprueba(self.textCtrl8.GetValue(), 2, error, _('φ de encuentro de fachada con suelo en contacto con aire')).ErrorDevuelto
        if self.fachadaSoleraCheck.GetValue() == True:
            cambios = True
            error += Comprueba(self.textCtrl9.GetValue(), 2, error, _('φ de encuentro de fachada con solera')).ErrorDevuelto
        if self.fachadaParticionCheck.GetValue() == True:
            cambios = True
            error += Comprueba(self.textCtrl10.GetValue(), 2, error, _('φ de encuentro de fachada con partición interior')).ErrorDevuelto
        if error != '':
            wx.MessageBox(_('Revise los siguientes campos:\n') + error + _('.'), _('Aviso'))
            return
        if cambios == False:
            wx.MessageBox(_('No ha seleccionado ningún cambio.'), _('Aviso'))
            return
        datos = []
        datos.append(self.descripcion.GetValue())
        datos.append('Mejora de Puentes Térmicos')
        datosConcretos = []
        datosConcretos.append(self.pilarEnFachadaCheck.GetValue())
        datosConcretos.append(self.textCtrl1.GetValue())
        datosConcretos.append(self.pilarEnEsquinaCheck.GetValue())
        datosConcretos.append(self.textCtrl2.GetValue())
        datosConcretos.append(self.contornoHuecoCheck.GetValue())
        datosConcretos.append(self.textCtrl3.GetValue())
        datosConcretos.append(self.cajaPersianaCheck.GetValue())
        datosConcretos.append(self.textCtrl4.GetValue())
        datosConcretos.append(self.fachadaForjadoCheck.GetValue())
        datosConcretos.append(self.textCtrl5.GetValue())
        datosConcretos.append(self.fachadaVoladizoCheck.GetValue())
        datosConcretos.append(self.textCtrl6.GetValue())
        datosConcretos.append(self.fachadaCubiertaCheck.GetValue())
        datosConcretos.append(self.textCtrl7.GetValue())
        datosConcretos.append(self.fachadaSueloCheck.GetValue())
        datosConcretos.append(self.textCtrl8.GetValue())
        datosConcretos.append(self.fachadaSoleraCheck.GetValue())
        datosConcretos.append(self.textCtrl9.GetValue())
        datosConcretos.append(self.fachadaParticionCheck.GetValue())
        datosConcretos.append(self.textCtrl10.GetValue())
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
        self.pilarEnFachadaCheck.SetValue(datosConcretos[0])
        self.textCtrl1.SetValue(str(datosConcretos[1]))
        self.pilarEnEsquinaCheck.SetValue(datosConcretos[2])
        self.textCtrl2.SetValue(str(datosConcretos[3]))
        self.contornoHuecoCheck.SetValue(datosConcretos[4])
        self.textCtrl3.SetValue(str(datosConcretos[5]))
        self.cajaPersianaCheck.SetValue(datosConcretos[6])
        self.textCtrl4.SetValue(str(datosConcretos[7]))
        self.fachadaForjadoCheck.SetValue(datosConcretos[8])
        self.textCtrl5.SetValue(str(datosConcretos[9]))
        self.fachadaVoladizoCheck.SetValue(datosConcretos[10])
        self.textCtrl6.SetValue(str(datosConcretos[11]))
        self.fachadaCubiertaCheck.SetValue(datosConcretos[12])
        self.textCtrl7.SetValue(str(datosConcretos[13]))
        self.fachadaSueloCheck.SetValue(datosConcretos[14])
        self.textCtrl8.SetValue(str(datosConcretos[15]))
        self.fachadaSoleraCheck.SetValue(datosConcretos[16])
        self.textCtrl9.SetValue(str(datosConcretos[17]))
        self.fachadaParticionCheck.SetValue(datosConcretos[18])
        self.textCtrl10.SetValue(str(datosConcretos[19]))
        self.OnCambiosChecks(None)
        return

    def onCancelarBoton(self, event):
        """
        Metodo: onCancelarBoton

        ARGUMENTOS:
                event:
        """
        self.dev = False
        self.Close()