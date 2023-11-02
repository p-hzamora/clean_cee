# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: AnalisisEconomico\panelFacturas.pyc
# Compiled at: 2015-02-23 10:42:21
"""
Modulo: panelFacturas.py

"""
from Envolvente.comprobarCampos import Comprueba
from miChoice import MiChoice
import Calculos.listadosWeb as listadosWeb, wx
wxID_PANEL1, wxID_PANEL1ACSCHECK, wxID_PANEL1CALEFACCIONCHECK, wxID_PANEL1COCINACHECK, wxID_PANEL1COMBUSTIBLECHOICE, wxID_PANEL1COMBUSTIBLETEXT, wxID_PANEL1CONSUMOANUAL, wxID_PANEL1CONSUMOANUALTEXT, wxID_PANEL1CONSUMOANUALUNIDADESTEXT, wxID_PANEL1CONSUMOACS, wxID_PANEL1CONSUMOCALEFACCION, wxID_PANEL1CONSUMOCOCINA, wxID_PANEL1CONSUMOEQUIPAMIENTO, wxID_PANEL1CONSUMOILUMINACION, wxID_PANEL1CONSUMOREFRIGERACION, wxID_PANEL1DEMANSATISFECHASTEXT, wxID_PANEL1DESCRIPCIONFACTURA, wxID_PANEL1DESCRIPCIONFACTURATEXT, wxID_PANEL1DISTRIBUCIONCONSUMOSTEXT, wxID_PANEL1EQUIPAMIENTOCHECK, wxID_PANEL1FACTORCONVERSION, wxID_PANEL1FACTORCONVERSIONTEXT, wxID_PANEL1FACTORCONVERSIONUNIDADES, wxID_PANEL1ILUMINACIONCHECK, wxID_PANEL1REFRIGERACIONCHECK, wxID_PANEL1STATICTEXT1, wxID_PANEL1STATICTEXT2, wxID_PANEL1STATICTEXT3, wxID_PANEL1STATICTEXT4, wxID_PANEL1STATICTEXT5, wxID_PANEL1STATICTEXT6, wxID_PANEL1STATICTEXT7, wxID_PANEL1TITULOTEXT, wxID_PANEL1UNIDADMEDIACHOICE, wxID_PANEL1UNIDADMEDIDATEXT, wxID_PANEL1CONSUMOOTROS, wxID_PANEL1OTROSCHECK, wxID_PANEL1STATICTEXT7, wxID_PANEL1STATICTEXT8, wxID_PANEL1STATICTEXT9, wxID_PANEL1STATICTEXT10, wxID_PANEL1VENTILADORESCHECK, wxID_PANEL1BOMBASCHECK, wxID_PANEL1TORRESCHECK, wxID_PANEL1CONSUMOVENTILADORES, wxID_PANEL1CONSUMOBOMBAS, wxID_PANEL1CONSUMOTORRES = [ wx.NewId() for _init_ctrls in range(47) ]

class Panel1(wx.Panel):
    """
    Clase: Panel1 del modulo panelFacturas.py

    """

    def _init_ctrls(self, prnt, id_prnt, pos_prnt, size_prnt, style_prnt, name_prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                  prnt:
                 id_prnt:
                 pos_prnt:
                 size_prnt:
                 style_prnt:
                 name_prnt:
        """
        wx.Panel.__init__(self, id=id_prnt, name=name_prnt, parent=prnt, pos=pos_prnt, size=size_prnt, style=style_prnt | wx.TAB_TRAVERSAL)
        self.SetBackgroundColour('white')
        self.tituloText = wx.StaticText(id=wxID_PANEL1STATICTEXT1, label=_('Definición de Factura Energética'), name='tituloText', parent=self, pos=wx.Point(15, 24), size=wx.Size(155, 13), style=0)
        self.tituloText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.tituloText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.CaracteristicasLinea = wx.StaticBox(id=-1, label=_('Datos de la factura'), name='CaracteristicasLinea', parent=self, pos=wx.Point(15, 70), size=wx.Size(695, 400), style=0)
        self.CaracteristicasLinea.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasLinea.SetForegroundColour(wx.Colour(0, 0, 100))
        self.descripcionFacturaText = wx.StaticText(id=wxID_PANEL1DESCRIPCIONFACTURATEXT, label=_('Nombre'), name='descripcionFacturaText', parent=self, pos=wx.Point(30, 100), size=wx.Size(118, 13), style=0)
        self.descripcionFactura = wx.TextCtrl(id=wxID_PANEL1DESCRIPCIONFACTURA, name='descripcionFactura', parent=self, pos=wx.Point(200, 98), size=wx.Size(480, 21), style=0, value='')
        self.combustibleText = wx.StaticText(id=wxID_PANEL1COMBUSTIBLETEXT, label=_('Combustible'), name='combustibleText', parent=self, pos=wx.Point(30, 130), size=wx.Size(58, 13), style=0)
        self.combustibleChoice = MiChoice(choices=listadosWeb.listadoCombustibles, id=wxID_PANEL1COMBUSTIBLECHOICE, name='combustibleChoice', parent=self, pos=wx.Point(200, 127), size=wx.Size(200, 21), style=0)
        self.combustibleChoice.Bind(wx.EVT_CHOICE, self.OnCombustibleChoice, id=wxID_PANEL1COMBUSTIBLECHOICE)
        self.unidadMedidaText = wx.StaticText(id=wxID_PANEL1STATICTEXT7, label=_('Unidad de medida'), name='unidadMedidaText', parent=self, pos=wx.Point(456, 130), size=wx.Size(85, 13), style=0)
        self.unidadMedidaText.Show(False)
        self.unidadMediaChoice = wx.Choice(choices=['kg', 'm3'], id=wxID_PANEL1UNIDADMEDIACHOICE, name='unidadMediaChoice', parent=self, pos=wx.Point(580, 127), size=wx.Size(100, 21), style=0)
        self.unidadMediaChoice.Bind(wx.EVT_CHOICE, self.OnUnidadMediaChoice, id=wxID_PANEL1UNIDADMEDIACHOICE)
        self.unidadMediaChoice.Show(False)
        self.consumoAnualText = wx.StaticText(id=wxID_PANEL1CONSUMOANUALTEXT, label=_('Consumo anual'), name='consumoAnualText', parent=self, pos=wx.Point(30, 160), size=wx.Size(74, 13), style=0)
        self.consumoAnualUnidadesText = wx.StaticText(id=wxID_PANEL1CONSUMOANUALUNIDADESTEXT, label=_('kWh'), name='consumoAnualUnidadesText', parent=self, pos=wx.Point(265, 160), size=wx.Size(21, 13), style=0)
        self.consumoAnual = wx.TextCtrl(id=wxID_PANEL1CONSUMOANUAL, name='consumoAnual', parent=self, pos=wx.Point(200, 157), size=wx.Size(60, 21), style=0, value='')
        self.factorConversionText = wx.StaticText(id=wxID_PANEL1FACTORCONVERSIONTEXT, label=_('Factor de conversión'), name='factorConversionText', parent=self, pos=wx.Point(456, 160), size=wx.Size(103, 13), style=0)
        self.factorConversionText.Show(False)
        self.factorConversion = wx.TextCtrl(id=wxID_PANEL1FACTORCONVERSION, name='factorConversion', parent=self, pos=wx.Point(580, 157), size=wx.Size(60, 21), style=0, value='1')
        self.factorConversion.Show(False)
        self.factorConversionUnidades = wx.StaticText(id=wxID_PANEL1FACTORCONVERSIONUNIDADES, label=_('kWh'), name='factorConversionUnidades', parent=self, pos=wx.Point(644, 160), size=wx.Size(25, 13), style=0)
        self.factorConversionUnidades.Show(False)
        self.demanSatisfechasText = wx.StaticText(id=wxID_PANEL1DEMANSATISFECHASTEXT, label=_('Demandas satisfechas'), name='demanSatisfechasText', parent=self, pos=wx.Point(30, 200), size=wx.Size(145, 13), style=0)
        self.distribucionConsumosText = wx.StaticText(id=wxID_PANEL1DISTRIBUCIONCONSUMOSTEXT, label=_('Distribución de consumos'), name='distribucionConsumosText', parent=self, pos=wx.Point(180, 200), size=wx.Size(126, 13), style=0)
        self.ACScheck = wx.CheckBox(id=wxID_PANEL1ACSCHECK, label=_('ACS'), name='ACScheck', parent=self, pos=wx.Point(60, 230), size=wx.Size(70, 13), style=0)
        self.ACScheck.SetValue(False)
        self.ACScheck.Bind(wx.EVT_CHECKBOX, self.OnACScheck, id=wxID_PANEL1ACSCHECK)
        self.calefaccionCheck = wx.CheckBox(id=wxID_PANEL1CALEFACCIONCHECK, label=_('Calefacción'), name='calefaccionCheck', parent=self, pos=wx.Point(60, 260), size=wx.Size(70, 13), style=0)
        self.calefaccionCheck.SetValue(False)
        self.calefaccionCheck.Bind(wx.EVT_CHECKBOX, self.OnCalefaccionCheck, id=wxID_PANEL1CALEFACCIONCHECK)
        self.refrigeracionCheck = wx.CheckBox(id=wxID_PANEL1REFRIGERACIONCHECK, label=_('Refrigeración'), name='refrigeracionCheck', parent=self, pos=wx.Point(60, 290), size=wx.Size(96, 13), style=0)
        self.refrigeracionCheck.SetValue(False)
        self.refrigeracionCheck.Bind(wx.EVT_CHECKBOX, self.OnRefrigeracionCheck, id=wxID_PANEL1REFRIGERACIONCHECK)
        self.iluminacionCheck = wx.CheckBox(id=wxID_PANEL1ILUMINACIONCHECK, label=_('Iluminación'), name='iluminacionCheck', parent=self, pos=wx.Point(60, 320), size=wx.Size(70, 13), style=0)
        self.iluminacionCheck.SetValue(False)
        self.iluminacionCheck.Bind(wx.EVT_CHECKBOX, self.OnIluminacionCheck, id=wxID_PANEL1ILUMINACIONCHECK)
        self.iluminacionCheck.Show(False)
        self.ventiladoresCheck = wx.CheckBox(id=wxID_PANEL1VENTILADORESCHECK, label=_('Ventiladores'), name='ventiladoresCheck', parent=self, pos=wx.Point(60, 350), size=wx.Size(80, 13), style=0)
        self.ventiladoresCheck.SetValue(False)
        self.ventiladoresCheck.Bind(wx.EVT_CHECKBOX, self.OnVentiladoresCheck, id=wxID_PANEL1VENTILADORESCHECK)
        self.ventiladoresCheck.Show(False)
        self.bombasCheck = wx.CheckBox(id=wxID_PANEL1BOMBASCHECK, label=_('Equipos de bombeo'), name='BombasCheck', parent=self, pos=wx.Point(60, 380), size=wx.Size(130, 13), style=0)
        self.bombasCheck.SetValue(False)
        self.bombasCheck.Bind(wx.EVT_CHECKBOX, self.OnBombasCheck, id=wxID_PANEL1BOMBASCHECK)
        self.bombasCheck.Show(False)
        self.torresCheck = wx.CheckBox(id=wxID_PANEL1TORRESCHECK, label=_('Torres de refrigeración'), name='torresCheck', parent=self, pos=wx.Point(60, 410), size=wx.Size(130, 13), style=0)
        self.torresCheck.SetValue(False)
        self.torresCheck.Bind(wx.EVT_CHECKBOX, self.OnTorresCheck, id=wxID_PANEL1TORRESCHECK)
        self.torresCheck.Show(False)
        self.otrosCheck = wx.CheckBox(id=wxID_PANEL1OTROSCHECK, label=_('Otros'), name='otrosCheck', parent=self, pos=wx.Point(60, 320), size=wx.Size(60, 13), style=0)
        self.otrosCheck.SetValue(False)
        self.otrosCheck.Bind(wx.EVT_CHECKBOX, self.OnOtrosCheck, id=wxID_PANEL1OTROSCHECK)
        self.consumoACS = wx.TextCtrl(id=wxID_PANEL1CONSUMOACS, name='consumoACS', parent=self, pos=wx.Point(200, 228), size=wx.Size(60, 21), style=0, value='')
        self.consumoACS.Enable(False)
        self.consumoCalefaccion = wx.TextCtrl(id=wxID_PANEL1CONSUMOCALEFACCION, name='consumoCalefaccion', parent=self, pos=wx.Point(200, 258), size=wx.Size(60, 21), style=0, value='')
        self.consumoCalefaccion.Enable(False)
        self.consumoRefrigeracion = wx.TextCtrl(id=wxID_PANEL1CONSUMOREFRIGERACION, name='consumoRefrigeracion', parent=self, pos=wx.Point(200, 288), size=wx.Size(60, 21), style=0, value='')
        self.consumoRefrigeracion.Enable(False)
        self.consumoIluminacion = wx.TextCtrl(id=wxID_PANEL1CONSUMOILUMINACION, name='consumoIluminacion', parent=self, pos=wx.Point(200, 318), size=wx.Size(60, 21), style=0, value='')
        self.consumoIluminacion.Enable(False)
        self.consumoIluminacion.Show(False)
        self.consumoVentiladores = wx.TextCtrl(id=wxID_PANEL1CONSUMOVENTILADORES, name='consumoVentiladores', parent=self, pos=wx.Point(200, 348), size=wx.Size(60, 21), style=0, value='')
        self.consumoVentiladores.Enable(False)
        self.consumoVentiladores.Show(False)
        self.consumoBombas = wx.TextCtrl(id=wxID_PANEL1CONSUMOBOMBAS, name='consumoBombas', parent=self, pos=wx.Point(200, 378), size=wx.Size(60, 21), style=0, value='')
        self.consumoBombas.Enable(False)
        self.consumoBombas.Show(False)
        self.consumoTorres = wx.TextCtrl(id=wxID_PANEL1CONSUMOTORRES, name='consumoIluminacion', parent=self, pos=wx.Point(200, 408), size=wx.Size(60, 21), style=0, value='')
        self.consumoTorres.Enable(False)
        self.consumoTorres.Show(False)
        self.consumoOtros = wx.TextCtrl(id=wxID_PANEL1CONSUMOOTROS, name='consumoOtros', parent=self, pos=wx.Point(200, 318), size=wx.Size(60, 21), style=0, value='')
        self.consumoOtros.Enable(False)
        self.staticText2 = wx.StaticText(id=wxID_PANEL1STATICTEXT2, label=_('%'), name='staticText2', parent=self, pos=wx.Point(265, 230), size=wx.Size(11, 13), style=0)
        self.staticText3 = wx.StaticText(id=wxID_PANEL1STATICTEXT3, label=_('%'), name='staticText3', parent=self, pos=wx.Point(265, 260), size=wx.Size(11, 13), style=0)
        self.staticText4 = wx.StaticText(id=wxID_PANEL1STATICTEXT4, label=_('%'), name='staticText4', parent=self, pos=wx.Point(265, 290), size=wx.Size(11, 13), style=0)
        self.staticText6 = wx.StaticText(id=wxID_PANEL1STATICTEXT6, label=_('%'), name='staticText6', parent=self, pos=wx.Point(265, 320), size=wx.Size(11, 13), style=0)
        self.staticText7 = wx.StaticText(id=wxID_PANEL1STATICTEXT7, label=_('%'), name='staticText7', parent=self, pos=wx.Point(265, 320), size=wx.Size(11, 13), style=0)
        self.staticText7.Show(False)
        self.staticText8 = wx.StaticText(id=wxID_PANEL1STATICTEXT8, label=_('%'), name='staticText8', parent=self, pos=wx.Point(265, 350), size=wx.Size(11, 13), style=0)
        self.staticText8.Show(False)
        self.staticText9 = wx.StaticText(id=wxID_PANEL1STATICTEXT9, label=_('%'), name='staticText9', parent=self, pos=wx.Point(265, 380), size=wx.Size(11, 13), style=0)
        self.staticText9.Show(False)
        self.staticText10 = wx.StaticText(id=wxID_PANEL1STATICTEXT10, label=_('%'), name='staticText10', parent=self, pos=wx.Point(265, 410), size=wx.Size(11, 13), style=0)
        self.staticText10.Show(False)

    def __init__(self, parent, id, pos, size, style, name, real_parent):
        """
        Constructor de la clase

        ARGUMENTOS:
                 parent:
                 id:
                 pos:
                 size:
                 style:
                 name:
                real_parent:
        """
        self.parent = real_parent
        self._init_ctrls(parent, id, pos, size, style, name)

    def OnUnidadMediaChoice(self, event):
        """
        Metodo: OnUnidadMediaChoice

        ARGUMENTOS:
                event:
        """
        self.consumoAnualUnidadesText.SetLabel(self.unidadMediaChoice.GetStringSelection())
        self.factorConversionUnidades.SetLabel(_('kWh/') + self.unidadMediaChoice.GetStringSelection())

    def OnCombustibleChoice(self, event):
        """
        Metodo: OnCombustibleChoice

        ARGUMENTOS:
                event:
        """
        if self.combustibleChoice.GetStringSelection() == 'Gas Natural':
            self.unidadMedidaText.Show(False)
            self.unidadMediaChoice.Show(False)
            self.consumoAnualUnidadesText.SetLabel(_('kWh'))
            self.factorConversionText.Show(False)
            self.factorConversion.Show(False)
            self.factorConversionUnidades.Show(False)
            self.factorConversion.SetValue('1')
        elif self.combustibleChoice.GetStringSelection() == 'Gasóleo-C':
            self.unidadMedidaText.Show(False)
            self.unidadMediaChoice.Show(False)
            self.consumoAnualUnidadesText.SetLabel(_('l'))
            self.factorConversionText.Show(True)
            self.factorConversion.Show(True)
            self.factorConversionUnidades.Show(True)
            self.factorConversionUnidades.SetLabel(_('kWh/l'))
        elif self.combustibleChoice.GetStringSelection() == 'Electricidad':
            self.unidadMedidaText.Show(False)
            self.unidadMediaChoice.Show(False)
            self.consumoAnualUnidadesText.SetLabel(_('kWh'))
            self.factorConversionText.Show(False)
            self.factorConversion.Show(False)
            self.factorConversionUnidades.Show(False)
            self.factorConversion.SetValue('1')
        elif self.combustibleChoice.GetStringSelection() == 'GLP':
            self.unidadMedidaText.Show(True)
            self.unidadMediaChoice.Show(True)
            self.consumoAnualUnidadesText.SetLabel(self.unidadMediaChoice.GetStringSelection())
            self.factorConversionUnidades.SetLabel(_('kWh/') + self.unidadMediaChoice.GetStringSelection())
            self.factorConversionText.Show(True)
            self.factorConversion.Show(True)
            self.factorConversionUnidades.Show(True)
        elif self.combustibleChoice.GetStringSelection() == 'Carbón':
            self.unidadMedidaText.Show(False)
            self.unidadMediaChoice.Show(False)
            self.consumoAnualUnidadesText.SetLabel(_('Kg'))
            self.factorConversionText.Show(True)
            self.factorConversion.Show(True)
            self.factorConversionUnidades.Show(True)
            self.factorConversionUnidades.SetLabel(_('kWh/Kg'))
        elif self.combustibleChoice.GetStringSelection() == 'Biocarburante':
            self.unidadMedidaText.Show(False)
            self.unidadMediaChoice.Show(False)
            self.consumoAnualUnidadesText.SetLabel(_('l'))
            self.factorConversionText.Show(True)
            self.factorConversion.Show(True)
            self.factorConversionUnidades.Show(True)
            self.factorConversionUnidades.SetLabel(_('kWh/l'))
        elif self.combustibleChoice.GetStringSelection() == 'Biomasa/Renovable':
            self.unidadMedidaText.Show(False)
            self.unidadMediaChoice.Show(False)
            self.consumoAnualUnidadesText.SetLabel(_('Kg'))
            self.factorConversionText.Show(True)
            self.factorConversion.Show(True)
            self.factorConversionUnidades.Show(True)
            self.factorConversionUnidades.SetLabel(_('kWh/Kg'))
        if self.parent.parent.parent.programa == b'Peque\xf1oTerciario' and self.combustibleChoice.GetStringSelection() == 'Electricidad':
            self.consumoOtros.SetPosition(wx.Point(200, 348))
            self.otrosCheck.SetPosition(wx.Point(60, 350))
            self.staticText6.SetPosition(wx.Point(265, 350))
            self.consumoIluminacion.Show(True)
            self.iluminacionCheck.Show(True)
            self.staticText7.Show(True)
            self.consumoVentiladores.Show(False)
            self.ventiladoresCheck.Show(False)
            self.staticText8.Show(False)
            self.consumoBombas.Show(False)
            self.bombasCheck.Show(False)
            self.staticText9.Show(False)
            self.consumoTorres.Show(False)
            self.torresCheck.Show(False)
            self.staticText10.Show(False)
        elif self.parent.parent.parent.programa == 'GranTerciario' and self.combustibleChoice.GetStringSelection() == 'Electricidad':
            self.consumoOtros.SetPosition(wx.Point(200, 438))
            self.otrosCheck.SetPosition(wx.Point(60, 440))
            self.staticText6.SetPosition(wx.Point(265, 440))
            self.consumoIluminacion.Show(True)
            self.iluminacionCheck.Show(True)
            self.staticText7.Show(True)
            self.consumoVentiladores.Show(True)
            self.ventiladoresCheck.Show(True)
            self.staticText8.Show(True)
            self.consumoBombas.Show(True)
            self.bombasCheck.Show(True)
            self.staticText9.Show(True)
            self.consumoTorres.Show(True)
            self.torresCheck.Show(True)
            self.staticText10.Show(True)
        else:
            self.consumoOtros.SetPosition(wx.Point(200, 318))
            self.otrosCheck.SetPosition(wx.Point(60, 320))
            self.staticText6.SetPosition(wx.Point(265, 320))
            self.consumoIluminacion.Show(False)
            self.iluminacionCheck.Show(False)
            self.staticText7.Show(False)
            self.consumoVentiladores.Show(False)
            self.ventiladoresCheck.Show(False)
            self.staticText8.Show(False)
            self.consumoBombas.Show(False)
            self.bombasCheck.Show(False)
            self.staticText9.Show(False)
            self.consumoTorres.Show(False)
            self.torresCheck.Show(False)
            self.staticText10.Show(False)

    def OnOtrosCheck(self, event):
        """
        Metodo: OnOtrosCheck

        ARGUMENTOS:
                event:
        """
        if self.otrosCheck.GetValue() == True:
            self.consumoOtros.Enable(True)
        else:
            self.consumoOtros.Enable(False)

    def OnIluminacionCheck(self, event):
        """
        Metodo: OnIluminacionCheck

        ARGUMENTOS:
                event:
        """
        if self.iluminacionCheck.GetValue() == True:
            self.consumoIluminacion.Enable(True)
        else:
            self.consumoIluminacion.Enable(False)

    def OnVentiladoresCheck(self, event):
        """
        Metodo: OnVentiladoresCheck

        ARGUMENTOS:
                event:
        """
        if self.ventiladoresCheck.GetValue() == True:
            self.consumoVentiladores.Enable(True)
        else:
            self.consumoVentiladores.Enable(False)

    def OnBombasCheck(self, event):
        """
        Metodo: OnBombasCheck

        ARGUMENTOS:
                event:
        """
        if self.bombasCheck.GetValue() == True:
            self.consumoBombas.Enable(True)
        else:
            self.consumoBombas.Enable(False)

    def OnTorresCheck(self, event):
        """
        Metodo: OnTorresCheck

        ARGUMENTOS:
                event:
        """
        if self.torresCheck.GetValue() == True:
            self.consumoTorres.Enable(True)
        else:
            self.consumoTorres.Enable(False)

    def OnRefrigeracionCheck(self, event):
        """
        Metodo: OnRefrigeracionCheck

        ARGUMENTOS:
                event:
        """
        if self.refrigeracionCheck.GetValue() == True:
            self.consumoRefrigeracion.Enable(True)
        else:
            self.consumoRefrigeracion.Enable(False)

    def OnCalefaccionCheck(self, event):
        """
        Metodo: OnCalefaccionCheck

        ARGUMENTOS:
                event:
        """
        if self.calefaccionCheck.GetValue() == True:
            self.consumoCalefaccion.Enable(True)
        else:
            self.consumoCalefaccion.Enable(False)

    def OnACScheck(self, event):
        """
        Metodo: OnACScheck

        ARGUMENTOS:
                event:
        """
        if self.ACScheck.GetValue() == True:
            self.consumoACS.Enable(True)
        else:
            self.consumoACS.Enable(False)

    def comprobarDatos(self):
        """
        Metodo: comprobarDatos

        """
        consumoAnual = self.consumoAnual.GetValue()
        factorConversion = self.factorConversion.GetValue()
        consumoACS = self.consumoACS.GetValue()
        consumoCal = self.consumoCalefaccion.GetValue()
        consumoRef = self.consumoRefrigeracion.GetValue()
        consumoIlum = self.consumoIluminacion.GetValue()
        consumoVentiladores = self.consumoVentiladores.GetValue()
        consumoBombas = self.consumoBombas.GetValue()
        consumoTorres = self.consumoTorres.GetValue()
        consumoOtros = self.consumoOtros.GetValue()
        if ',' in consumoAnual:
            consumoAnual = consumoAnual.replace(',', '.')
            self.consumoAnual.SetValue(consumoAnual)
        if ',' in factorConversion:
            factorConversion = factorConversion.replace(',', '.')
            self.factorConversion.SetValue(factorConversion)
        if ',' in consumoACS:
            consumoACS = consumoACS.replace(',', '.')
            self.consumoACS.SetValue(consumoACS)
        if ',' in consumoCal:
            consumoCal = consumoCal.replace(',', '.')
            self.consumoCalefaccion.SetValue(consumoCal)
        if ',' in consumoRef:
            consumoRef = consumoRef.replace(',', '.')
            self.consumoRefrigeracion.SetValue(consumoRef)
        if ',' in consumoIlum:
            consumoIlum = consumoIlum.replace(',', '.')
            self.consumoIluminacion.SetValue(consumoIlum)
        if ',' in consumoVentiladores:
            consumoVentiladores = consumoVentiladores.replace(',', '.')
            self.consumoVentiladores.SetValue(consumoVentiladores)
        if ',' in consumoBombas:
            consumoBombas = consumoBombas.replace(',', '.')
            self.consumoBombas.SetValue(consumoBombas)
        if ',' in consumoTorres:
            consumoTorres = consumoTorres.replace(',', '.')
            self.consumoTorres.SetValue(consumoTorres)
        if ',' in consumoOtros:
            consumoOtros = consumoOtros.replace(',', '.')
            self.consumoOtros.SetValue(consumoOtros)
        listaErrores = ''
        listaErrores += Comprueba(self.descripcionFactura.GetValue(), 1, listaErrores, _('nombre')).ErrorDevuelto
        listaErrores += Comprueba(self.combustibleChoice.GetStringSelection(), 0, listaErrores, _('combustible')).ErrorDevuelto
        if self.combustibleChoice.GetStringSelection() == 'GLP':
            listaErrores += Comprueba(self.unidadMediaChoice.GetStringSelection(), 0, listaErrores, _('unidad de medida')).ErrorDevuelto
        if self.combustibleChoice.GetStringSelection() != 'Electricidad':
            if self.combustibleChoice.GetStringSelection() != 'Gas Natural':
                listaErrores += Comprueba(self.factorConversion.GetValue(), 2, listaErrores, _('factor de conversión'), 0).ErrorDevuelto
        listaErrores += Comprueba(self.consumoAnual.GetValue(), 2, listaErrores, _('consumo anual'), 0).ErrorDevuelto
        suma = 0
        if self.ACScheck.GetValue() == True:
            listaErrores += Comprueba(self.consumoACS.GetValue(), 2, listaErrores, _('consumo de ACS'), 0).ErrorDevuelto
            try:
                suma = suma + float(self.consumoACS.GetValue())
            except ValueError:
                pass

        if self.calefaccionCheck.GetValue() == True:
            listaErrores += Comprueba(self.consumoCalefaccion.GetValue(), 2, listaErrores, _('consumo de calefacción'), 0).ErrorDevuelto
            try:
                suma = suma + float(self.consumoCalefaccion.GetValue())
            except ValueError:
                pass

        if self.refrigeracionCheck.GetValue() == True:
            listaErrores += Comprueba(self.consumoRefrigeracion.GetValue(), 2, listaErrores, _('consumo de refrigeración'), 0).ErrorDevuelto
            try:
                suma = suma + float(self.consumoRefrigeracion.GetValue())
            except ValueError:
                pass

        if self.otrosCheck.GetValue() == True:
            listaErrores += Comprueba(self.consumoOtros.GetValue(), 2, listaErrores, _('consumo de otros'), 0).ErrorDevuelto
            try:
                suma = suma + float(self.consumoOtros.GetValue())
            except ValueError:
                pass

        if self.iluminacionCheck.GetValue() == True and self.combustibleChoice.GetStringSelection() == 'Electricidad' and self.parent.parent.parent.programa != 'Residencial':
            listaErrores += Comprueba(self.consumoIluminacion.GetValue(), 2, listaErrores, _('consumo de iluminacion'), 0).ErrorDevuelto
            try:
                suma = suma + float(self.consumoIluminacion.GetValue())
            except ValueError:
                pass

        if self.ventiladoresCheck.GetValue() == True and self.combustibleChoice.GetStringSelection() == 'Electricidad' and self.parent.parent.parent.programa == 'GranTerciario':
            listaErrores += Comprueba(self.consumoVentiladores.GetValue(), 2, listaErrores, _('consumo de ventiladores'), 0).ErrorDevuelto
            try:
                suma = suma + float(self.consumoVentiladores.GetValue())
            except ValueError:
                pass

        if self.bombasCheck.GetValue() == True and self.combustibleChoice.GetStringSelection() == 'Electricidad' and self.parent.parent.parent.programa == 'GranTerciario':
            listaErrores += Comprueba(self.consumoBombas.GetValue(), 2, listaErrores, _('consumo de equipos de bombeo'), 0).ErrorDevuelto
            try:
                suma = suma + float(self.consumoBombas.GetValue())
            except ValueError:
                pass

        if self.torresCheck.GetValue() == True and self.combustibleChoice.GetStringSelection() == 'Electricidad' and self.parent.parent.parent.programa == 'GranTerciario':
            listaErrores += Comprueba(self.consumoTorres.GetValue(), 2, listaErrores, _('consumo de torres de refrigeración'), 0).ErrorDevuelto
            try:
                suma = suma + float(self.consumoTorres.GetValue())
            except ValueError:
                pass

        if suma != 100:
            return _('correctamente la factura. Las demandas deben sumar el 100%')
        return listaErrores

    def cogerDatos(self):
        """
        Metodo: cogerDatos

        """
        listaErrores = self.comprobarDatos()
        if listaErrores != '':
            return listaErrores
        datos = []
        datos.append(self.descripcionFactura.GetValue())
        datos.append(self.combustibleChoice.GetStringSelection())
        datos.append(self.unidadMediaChoice.GetStringSelection())
        datos.append(self.consumoAnual.GetValue())
        datos.append(self.factorConversion.GetValue())
        if self.combustibleChoice.GetStringSelection() == 'Electricidad' and self.parent.parent.parent.programa == b'Peque\xf1oTerciario':
            datosInstalacion = [
             [
              '', False], ['', False], ['', False], ['', False], ['', False]]
        elif self.combustibleChoice.GetStringSelection() == 'Electricidad' and self.parent.parent.parent.programa == 'GranTerciario':
            datosInstalacion = [
             [
              '', False], ['', False], ['', False], ['', False],
             [
              '', False], ['', False], ['', False], ['', False]]
        else:
            datosInstalacion = [
             [
              '', False], ['', False], ['', False], ['', False]]
        datosInstalacion[0][1] = self.ACScheck.GetValue()
        datosInstalacion[1][1] = self.calefaccionCheck.GetValue()
        datosInstalacion[2][1] = self.refrigeracionCheck.GetValue()
        if self.combustibleChoice.GetStringSelection() == 'Electricidad' and self.parent.parent.parent.programa == b'Peque\xf1oTerciario':
            datosInstalacion[3][1] = self.iluminacionCheck.GetValue()
            datosInstalacion[4][1] = self.otrosCheck.GetValue()
        elif self.combustibleChoice.GetStringSelection() == 'Electricidad' and self.parent.parent.parent.programa == 'GranTerciario':
            datosInstalacion[3][1] = self.iluminacionCheck.GetValue()
            datosInstalacion[4][1] = self.ventiladoresCheck.GetValue()
            datosInstalacion[5][1] = self.bombasCheck.GetValue()
            datosInstalacion[6][1] = self.torresCheck.GetValue()
            datosInstalacion[7][1] = self.otrosCheck.GetValue()
        else:
            datosInstalacion[3][1] = self.otrosCheck.GetValue()
        datosInstalacion[0][0] = self.consumoACS.GetValue()
        datosInstalacion[1][0] = self.consumoCalefaccion.GetValue()
        datosInstalacion[2][0] = self.consumoRefrigeracion.GetValue()
        if self.combustibleChoice.GetStringSelection() == 'Electricidad' and self.parent.parent.parent.programa == b'Peque\xf1oTerciario':
            datosInstalacion[3][0] = self.consumoIluminacion.GetValue()
            datosInstalacion[4][0] = self.consumoOtros.GetValue()
        elif self.combustibleChoice.GetStringSelection() == 'Electricidad' and self.parent.parent.parent.programa == 'GranTerciario':
            datosInstalacion[3][0] = self.consumoIluminacion.GetValue()
            datosInstalacion[4][0] = self.consumoVentiladores.GetValue()
            datosInstalacion[5][0] = self.consumoBombas.GetValue()
            datosInstalacion[6][0] = self.consumoTorres.GetValue()
            datosInstalacion[7][0] = self.consumoOtros.GetValue()
        else:
            datosInstalacion[3][0] = self.consumoOtros.GetValue()
        datos.append(datosInstalacion)
        return datos

    def cargarDatos(self, datos):
        """
        Metodo: cargarDatos

        ARGUMENTOS:
                datos:
        """
        self.descripcionFactura.SetValue(datos[0])
        self.combustibleChoice.SetStringSelection(datos[1])
        self.unidadMediaChoice.SetStringSelection(datos[2])
        self.consumoAnual.SetValue(datos[3])
        self.factorConversion.SetValue(datos[4])
        datosInstalacion = datos[5]
        self.ACScheck.SetValue(datosInstalacion[0][1])
        self.calefaccionCheck.SetValue(datosInstalacion[1][1])
        self.refrigeracionCheck.SetValue(datosInstalacion[2][1])
        if self.combustibleChoice.GetStringSelection() == 'Electricidad' and self.parent.parent.parent.programa == b'Peque\xf1oTerciario':
            self.iluminacionCheck.SetValue(datosInstalacion[3][1])
            self.otrosCheck.SetValue(datosInstalacion[4][1])
        elif self.combustibleChoice.GetStringSelection() == 'Electricidad' and self.parent.parent.parent.programa == 'GranTerciario':
            self.iluminacionCheck.SetValue(datosInstalacion[3][1])
            self.ventiladoresCheck.SetValue(datosInstalacion[4][1])
            self.bombasCheck.SetValue(datosInstalacion[5][1])
            self.torresCheck.SetValue(datosInstalacion[6][1])
            self.otrosCheck.SetValue(datosInstalacion[7][1])
        else:
            self.otrosCheck.SetValue(datosInstalacion[3][1])
        self.consumoACS.SetValue(datosInstalacion[0][0])
        self.consumoCalefaccion.SetValue(datosInstalacion[1][0])
        self.consumoRefrigeracion.SetValue(datosInstalacion[2][0])
        if self.combustibleChoice.GetStringSelection() == 'Electricidad' and self.parent.parent.parent.programa == b'Peque\xf1oTerciario':
            self.consumoIluminacion.SetValue(datosInstalacion[3][0])
            self.consumoOtros.SetValue(datosInstalacion[4][0])
        elif self.combustibleChoice.GetStringSelection() == 'Electricidad' and self.parent.parent.parent.programa == 'GranTerciario':
            self.consumoIluminacion.SetValue(datosInstalacion[3][0])
            self.consumoVentiladores.SetValue(datosInstalacion[4][0])
            self.consumoBombas.SetValue(datosInstalacion[5][0])
            self.consumoTorres.SetValue(datosInstalacion[6][0])
            self.consumoOtros.SetValue(datosInstalacion[7][0])
        else:
            self.consumoOtros.SetValue(datosInstalacion[3][0])
        self.OnOtrosCheck(None)
        self.OnRefrigeracionCheck(None)
        self.OnCalefaccionCheck(None)
        self.OnACScheck(None)
        self.OnUnidadMediaChoice(None)
        self.OnCombustibleChoice(None)
        self.OnIluminacionCheck(None)
        self.OnVentiladoresCheck(None)
        self.OnBombasCheck(None)
        self.OnTorresCheck(None)
        return