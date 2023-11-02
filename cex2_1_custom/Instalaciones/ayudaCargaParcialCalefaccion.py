# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\ayudaCargaParcialCalefaccion.pyc
# Compiled at: 2015-02-19 13:18:33
"""
Modulo: ayudaCargaParcialCalefaccion.py

"""
from Calculos.funcionesCalculo import betaCombDefecto
from Instalaciones.comprobarCampos import Comprueba, Comprueba2
import Instalaciones.equipos as equipos, wx, logging
wxID_DIALOG1, wxID_DIALOG1BOTONAPLICAR, wxID_DIALOG1BOTONCALCULAR, wxID_DIALOG1FACTORCARGAPARCIAL, wxID_DIALOG1FRACCIONENERGIA, wxID_DIALOG1FRACCIONINICIO, wxID_DIALOG1FRACCIONPOTENCIATOTAL, wxID_FRACCIONPOTENCIATOTALTEXT, wxID_DIALOG1FRACCIONINICIOTEXT, wxID_DIALOG1STATICTEXT3, wxID_DIALOG1STATICTEXT4, wxID_DIALOG1BOTONCANCELAR, wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICBOX1 = [ wx.NewId() for _init_ctrls in range(14) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo ayudaCargaParcialCalefaccion.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(513, 269), size=wx.Size(440, 248), style=wx.DEFAULT_DIALOG_STYLE, title=_('Estimación de la carga media estacional'))
        self.SetClientSize(wx.Size(440, 248))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=_('Estimación de la carga media estacional'), name='staticText1', parent=self, pos=wx.Point(15, 15), size=wx.Size(350, 20), style=0)
        self.staticText1.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.staticText1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticBox1 = wx.StaticBox(id=wxID_DIALOG1STATICBOX1, label=_('Parámetros del funcionamiento del equipo'), name='staticText1', parent=self, pos=wx.Point(15, 45), size=wx.Size(410, 150), style=0)
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticBox1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.fraccionPotenciaTotalText = wx.StaticText(id=wxID_FRACCIONPOTENCIATOTALTEXT, label=_('Fracción de la potencia total aportada por este generador'), name='staticText1', parent=self, pos=wx.Point(30, 70), size=wx.Size(283, 13), style=0)
        self.fraccionInicioText = wx.StaticText(id=wxID_DIALOG1FRACCIONINICIOTEXT, label=_('Fracción de la potencia total a la que entra este generador'), name='staticText2', parent=self, pos=wx.Point(30, 100), size=wx.Size(287, 13), style=0)
        self.fraccionPotenciaTotal = wx.TextCtrl(id=wxID_DIALOG1FRACCIONPOTENCIATOTAL, name='fraccionPotenciaTotal', parent=self, pos=wx.Point(350, 68), size=wx.Size(60, 21), style=0, value='1.0')
        self.fraccionPotenciaTotal.Bind(wx.EVT_TEXT, self.OnBotonCalcularButton, id=wxID_DIALOG1FRACCIONPOTENCIATOTAL)
        self.fraccionInicio = wx.TextCtrl(id=wxID_DIALOG1FRACCIONINICIO, name='fraccionInicio', parent=self, pos=wx.Point(350, 98), size=wx.Size(60, 21), style=0, value='0.0')
        self.fraccionInicio.Bind(wx.EVT_TEXT, self.OnBotonCalcularButton, id=wxID_DIALOG1FRACCIONINICIO)
        self.staticText3 = wx.StaticText(id=wxID_DIALOG1STATICTEXT3, label=_('Fracción de la energía total que es aportada por este generador'), name='staticText3', parent=self, pos=wx.Point(30, 130), size=wx.Size(313, 13), style=0)
        self.staticText3.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.staticText4 = wx.StaticText(id=wxID_DIALOG1STATICTEXT4, label=_('Factor de carga parcial media estacional'), name='staticText4', parent=self, pos=wx.Point(30, 160), size=wx.Size(197, 13), style=0)
        self.staticText4.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.fraccionEnergia = wx.TextCtrl(id=wxID_DIALOG1FRACCIONENERGIA, name='fraccionEnergia', parent=self, pos=wx.Point(350, 128), size=wx.Size(60, 21), style=0, value='')
        self.fraccionEnergia.SetEditable(False)
        self.fraccionEnergia.Enable(False)
        self.factorCargaParcial = wx.TextCtrl(id=wxID_DIALOG1FACTORCARGAPARCIAL, name='factorCargaParcial', parent=self, pos=wx.Point(350, 158), size=wx.Size(60, 21), style=0, value='')
        self.factorCargaParcial.Enable(False)
        self.factorCargaParcial.SetEditable(False)
        self.botonAplicar = wx.Button(id=wxID_DIALOG1BOTONAPLICAR, label=_('Aceptar'), name='botonAplicar', parent=self, pos=wx.Point(15, 210), size=wx.Size(75, 23), style=0)
        self.botonAplicar.Bind(wx.EVT_BUTTON, self.OnBotonAplicarButton, id=wxID_DIALOG1BOTONAPLICAR)
        self.botonCancelar = wx.Button(id=wxID_DIALOG1BOTONCANCELAR, label=_('Cancelar'), name='botonCancelar', parent=self, pos=wx.Point(105, 210), size=wx.Size(75, 23), style=0)
        self.botonCancelar.Bind(wx.EVT_BUTTON, self.OnBotonCancelarButton, id=wxID_DIALOG1BOTONCANCELAR)
        self.fraccionPotenciaTotal.SetToolTip(wx.ToolTip(_('Si exiten varias calderas que trabajan simultáneamente para dar la potencia total\ndemandada por la instalación, debe indicar en este campo la fracción de la potencia total que corresponde\na la caldera que se está introduciendo. \nPor ejemplo, si una instalación cuenta con dos calderas de 60 y 40 kW,\nse podrán definir como dos generadores independientes y cada uno de ellos \nrepresentarán respectivamente las fracciones 0.6 y 0.4 de la potencia total.')))
        self.fraccionInicio.SetToolTip(wx.ToolTip(_('Si exiten varias calderas que trabajan simultáneamente para dar la potencia total\ndemandada por la instalación, debe indicar en este campo la fracción de la potencia total a la que\nentra en servicio a la caldera que se está introduciendo. \nPor ejemplo, si una instalación cuenta con dos calderas de 60 y 40 kW, y la gestión\nde las calderas se realiza de tal manera que entra primero la de 60 kW y luego la de 40 kW, \ndiremos que la fracción de la potencia total a la que entra el generador de 60 kW es 0.0 \ny la fraccción de la potencia total a la que entra el generador de 40 kW es 0.6')))

    def __init__(self, parent, inicio):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
                inicio:
        """
        self.parent = parent
        self.dev = []
        self._init_ctrls(parent)
        self.iniciaValores(inicio)
        self.OnBotonCalcularButton(None)
        return

    def iniciaValores(self, inicio):
        """
        Metodo: iniciaValores

        ARGUMENTOS:
                inicio:
        """
        self.fraccionPotenciaTotal.SetValue(str(inicio[0]))
        self.fraccionInicio.SetValue(str(inicio[1]))

    def OnBotonCalcularButton(self, event):
        """
        Metodo: OnBotonCalcularButton

        ARGUMENTOS:
                event:
        """
        zona = self.parent.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()
        if self.parent.parent.parent.parent.programa == 'Residencial':
            uso = 'Residencial'
        else:
            uso = self.parent.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
        fraccionInicio = self.fraccionInicio.GetValue()
        fraccionPotenciaTotal = self.fraccionPotenciaTotal.GetValue()
        if ',' in fraccionInicio:
            fraccionInicio = fraccionInicio.replace(',', '.')
            self.fraccionInicio.SetValue(fraccionInicio)
            self.fraccionInicio.SetInsertionPointEnd()
        if ',' in fraccionPotenciaTotal:
            fraccionPotenciaTotal = fraccionPotenciaTotal.replace(',', '.')
            self.fraccionPotenciaTotal.SetValue(fraccionPotenciaTotal)
            self.fraccionPotenciaTotal.SetInsertionPointEnd()
        try:
            porcentajeDesde = float(self.fraccionInicio.GetValue())
            porcentajeDeLaPotenciaTotalAportadoPorEsteGenerador = float(self.fraccionPotenciaTotal.GetValue())
            porcentajeEnergiaGenerador, betaComb = equipos.estimacionCargaEscalonadaCalefaccion(zona, uso, porcentajeDesde, porcentajeDeLaPotenciaTotalAportadoPorEsteGenerador)
            if betaComb < betaCombDefecto:
                betaComb = betaCombDefecto
            self.fraccionEnergia.SetValue(str(round(sum(porcentajeEnergiaGenerador), 2)))
            self.factorCargaParcial.SetValue(str(round(betaComb, 2)))
        except:
            logging.info('Excepcion en: %s' % __name__)
            self.fraccionEnergia.SetValue('')
            self.factorCargaParcial.SetValue('')

    def OnBotonAplicarButton(self, event):
        """
        Metodo: OnBotonAplicarButton

        ARGUMENTOS:
                event:
        """
        dato = self.fraccionPotenciaTotal.GetValue()
        if ',' in dato:
            self.fraccionPotenciaTotal.SetValue(dato.replace(',', '.'))
        dato = self.fraccionInicio.GetValue()
        if ',' in dato:
            self.fraccionInicio.SetValue(dato.replace(',', '.'))
        listaErrores = ''
        listaErrores += Comprueba(self.fraccionPotenciaTotal.GetValue(), 2, listaErrores, _('fracción de la potencia total aportada por este generador'), 0.0, 1.0).ErrorDevuelto
        listaErrores += Comprueba2(self.fraccionInicio.GetValue(), 2, listaErrores, _('fracción de la potencia total a la que entra este generador'), 0.0, 1.0).ErrorDevuelto
        if listaErrores == '':
            self.dev = [
             self.fraccionEnergia.GetValue(), self.factorCargaParcial.GetValue(),
             self.fraccionPotenciaTotal.GetValue(), self.fraccionInicio.GetValue()]
            self.Close()
        else:
            wx.MessageBox(_('Revise los siguientes campos:\n') + listaErrores, _('Aviso'))

    def OnBotonCancelarButton(self, event):
        """
        Metodo: OnBotonCancelarButton

        ARGUMENTOS:
                event:
        """
        self.Close()