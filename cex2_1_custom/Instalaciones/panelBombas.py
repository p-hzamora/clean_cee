# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\panelBombas.pyc
# Compiled at: 2015-02-19 13:18:33
"""
Modulo: panelBombas.py

"""
from Instalaciones.comprobarCampos import Comprueba, Comprueba2
from miChoice import MiChoice
import Instalaciones.ayudaNumeroHoras as ayudaNumeroHoras, Instalaciones.dialogoCurva as dialogoCurva, Instalaciones.dialogoEscalones as dialogoEscalones, Instalaciones.equipos as equipos, Instalaciones.perfilesTerciario as perfilesTerciario
from Calculos.funcionesCalculo import calculoNumeroHorasOcupacionEdificio
import Calculos.listadosWeb as listadosWeb, wx, logging
wxID_PANEL1, wxID_PANEL1BOMBACHOICE, wxID_PANEL1NOMBREINSTALACION, wxID_PANEL1NOMBREINSTALACIONTEXT, wxID_PANEL1RENDIMIENTOTEXT, wxID_PANEL1SUBGRUPOCHOICE, wxID_PANEL1SUBGRUPOTEXT, wxID_PANEL1ESTIMACIONCONSUMO, wxID_BOMBACONSTANTEPOTENCIAELECTRICANOMINAL, wxID_BOMBACONSTANTENUMEROHORASDEMANDA, wxID_BOMBACONSTANTECONSUMO, wxID_BOMBAC1, wxID_BOMBAC2, wxID_BOMBAC3, wxID_BOMBAC4, wxID_POTENCIAFCPGRID1, wxID_BOMBASELECCIONSERVICIO, wxID_FUNCIONAMIENTONODEMANDABOX1, wxID_BOMBANUMEROHORASDEMANDA, wxID_BOMBAFRACCIONPOTENCIANODEMANDA, wxID_BOMBAHORASTEMPORADAREFRIGERACION, wxID_BOMBAHORASTEMPORADACALEFACCION, wxID_BOMBAHORASTEMPORADAACS, wxID_CARACTERISTICASLINEATEXT, wxID_EFICIENCIALINEATEXT, wxID_DIALOG1BOTONCURVA, wxID_DIALOG1BOTONESCALONES, wxID_AYUDANUMEROHORASDEMANDA = [ wx.NewId() for _init_ctrls in range(28) ]

class Panel1(wx.Panel):
    """
    Clase: Panel1 del modulo panelBombas.py

    """

    def _init_ctrls(self, prnt, id, posi, siz, styles, named):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
                id:
                posi:
                siz:
                styles:
                named:
        """
        wx.Panel.__init__(self, id=wxID_PANEL1, name=named, parent=prnt, pos=posi, size=siz, style=styles)
        self.SetBackgroundColour('white')
        self.nombreInstalacionText = wx.StaticText(id=wxID_PANEL1NOMBREINSTALACIONTEXT, label=_('Nombre'), name='nombreInstalacionText', parent=self, pos=wx.Point(15, 2), size=wx.Size(102, 13), style=0)
        self.nombreInstalacion = wx.TextCtrl(id=wxID_PANEL1NOMBREINSTALACION, name='nombreInstalacion', parent=self, pos=wx.Point(170, 0), size=wx.Size(230, 21), style=0, value=_('Bomba'))
        self.nombreInstalacion.SetForegroundColour(wx.Colour(100, 200, 0))
        self.nombreInstalacion.Bind(wx.EVT_TEXT, self.OnNombreInstalacion, id=wxID_PANEL1NOMBREINSTALACION)
        self.subgrupoText = wx.StaticText(id=wxID_PANEL1SUBGRUPOTEXT, label=_('Zona'), name='subgrupoText', parent=self, pos=wx.Point(435, 2), size=wx.Size(50, 13), style=0)
        self.subgrupoChoice = MiChoice(choices=[], id=wxID_PANEL1SUBGRUPOCHOICE, name='subgrupoChoice', parent=self, pos=wx.Point(496, 0), size=wx.Size(214, 21), style=0)
        self.tipoBombaText = wx.StaticText(id=-1, label=_('Tipo de bomba'), name='tipoBombaText', parent=self, pos=wx.Point(15, 46), size=wx.Size(89, 13), style=0)
        self.CaracteristicasLineaText = wx.StaticBox(id=wxID_CARACTERISTICASLINEATEXT, label=_('Características'), name='CaracteristicasLineaText', parent=self, pos=wx.Point(0, 26), size=wx.Size(400, 77), style=0)
        self.CaracteristicasLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.bombaChoice = MiChoice(choices=listadosWeb.listadoOpcionesBombas, id=wxID_PANEL1BOMBACHOICE, name='bombaChoice', parent=self, pos=wx.Point(170, 44), size=wx.Size(220, 21), style=0)
        self.bombaChoice.SetSelection(0)
        self.bombaChoice.Bind(wx.EVT_CHOICE, self.OnBombaChoice, id=wxID_PANEL1BOMBACHOICE)
        self.seleccionServicioText = wx.StaticText(id=-1, label=_('Servicio'), name='staticText12', parent=self, pos=wx.Point(15, 71), size=wx.Size(96, 13), style=0)
        self.seleccionServicio = MiChoice(choices=listadosWeb.listadoOpcionesServicioBombas, id=wxID_BOMBASELECCIONSERVICIO, name='seleccionServicio', parent=self, pos=wx.Point(170, 69), size=wx.Size(220, 21), style=0)
        self.seleccionServicio.SetSelection(1)
        self.seleccionServicio.SetHelpText(_('Seleccione el servicio al que está asignada esta bomba o grupo de bombeo. En el que caso de que se encuentre asignada a varios servicios, deberá crear varias bombas o grupos de bombeo, asignando cada una de ellas al servicio correspondiente. '))
        self.seleccionServicio.SetLabel('')
        self.seleccionServicio.Bind(wx.EVT_CHOICE, self.OnSeleccionServicioChoice, id=wxID_BOMBASELECCIONSERVICIO)
        self.EficienciaLineaText = wx.StaticBox(id=wxID_EFICIENCIALINEATEXT, label=_('Consumo energético anual'), name='EficienciaLineaText', parent=self, pos=wx.Point(0, 107), size=wx.Size(710, 135), style=0)
        self.EficienciaLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.EficienciaLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.EstimacionConsumoText = wx.StaticText(id=-1, label=_('Consumo energético'), name='rendimientoText', parent=self, pos=wx.Point(15, 130), size=wx.Size(150, 25), style=0)
        self.EstimacionConsumoText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.EstimacionConsumoChoice = MiChoice(choices=listadosWeb.listadoOpcionesConsumoBombasOVentiladores, id=wxID_PANEL1ESTIMACIONCONSUMO, name='rendimientoChoice', parent=self, pos=wx.Point(170, 128), size=wx.Size(220, 21), style=0)
        self.EstimacionConsumoChoice.SetSelection(0)
        self.EstimacionConsumoChoice.Bind(wx.EVT_CHOICE, self.OnEstimacionConsumoChoice, id=wxID_PANEL1ESTIMACIONCONSUMO)
        self.consumoAnualText = wx.StaticText(id=-1, label=_('Consumo energético anual'), name='consumoAnualText', parent=self, pos=wx.Point(435, 130), size=wx.Size(180, 13), style=0)
        self.consumo = wx.TextCtrl(id=wxID_BOMBACONSTANTECONSUMO, name='consumo', parent=self, pos=wx.Point(617, 128), size=wx.Size(60, 21), style=0, value='')
        self.consumo.SetEditable(False)
        self.consumo.Enable(True)
        self.consumoAnualUnidades = wx.StaticText(id=-1, label=_('kWh'), name='consumoAnualText', parent=self, pos=wx.Point(682, 130), size=wx.Size(20, 13), style=0)
        self.consumoAnualText.SetForegroundColour(wx.Colour(100, 100, 100))
        self.consumoAnualUnidades.SetForegroundColour(wx.Colour(100, 100, 100))
        self.potenciaText = wx.StaticText(id=-1, label=_('Potencia eléctrica'), name='potenciaText', parent=self, pos=wx.Point(15, 155), size=wx.Size(120, 13), style=0)
        self.potenciaText.Show(False)
        self.potenciaElectricaNominal = wx.TextCtrl(id=wxID_BOMBACONSTANTEPOTENCIAELECTRICANOMINAL, name='potenciaElectricaNominal', parent=self, pos=wx.Point(170, 153), size=wx.Size(60, 21), style=0, value='')
        self.potenciaElectricaNominal.Show(False)
        self.potenciaElectricaNominal.Bind(wx.EVT_TEXT, self.obtenerConsumoEstacional, id=wxID_BOMBACONSTANTEPOTENCIAELECTRICANOMINAL)
        self.potenciaUnidades = wx.StaticText(id=-1, label=_('kW'), name='potenciaText', parent=self, pos=wx.Point(235, 155), size=wx.Size(20, 13), style=0)
        self.potenciaUnidades.Show(False)
        self.numeroHorasDemandaText = wx.StaticText(id=-1, label=_('Número de horas de demanda'), name='numeroHorasDemandaText', parent=self, pos=wx.Point(15, 180), size=wx.Size(150, 13), style=0)
        self.numeroHorasDemandaText.Show(False)
        self.numeroHorasDemanda = wx.TextCtrl(id=wxID_BOMBACONSTANTENUMEROHORASDEMANDA, name='numeroHorasDemanda', parent=self, pos=wx.Point(170, 178), size=wx.Size(60, 21), style=0, value='')
        self.numeroHorasDemanda.Show(False)
        self.numeroHorasDemanda.Bind(wx.EVT_TEXT, self.obtenerConsumoEstacional, id=wxID_BOMBACONSTANTENUMEROHORASDEMANDA)
        self.numeroHorasDemandaUnidades = wx.StaticText(id=-1, label=_('h'), name='numeroHorasDemanda', parent=self, pos=wx.Point(235, 180), size=wx.Size(20, 13), style=0)
        self.numeroHorasDemandaUnidades.Show(False)
        self.numeroHorasHelpButton = wx.Button(id=wxID_AYUDANUMEROHORASDEMANDA, label=_(' ?'), name='numeroHorasHelpButton', parent=self, pos=wx.Point(250, 178), size=wx.Size(20, 21), style=0)
        self.numeroHorasHelpButton.Bind(wx.EVT_BUTTON, self.OnNumeroHorasHelpButton, id=wxID_AYUDANUMEROHORASDEMANDA)
        self.numeroHorasHelpButton.Show(False)
        self.botonDefinirCurva = wx.Button(id=wxID_DIALOG1BOTONCURVA, label=_('Definir curva de consumo'), name='botonDefinirCurva', parent=self, pos=wx.Point(496, 178), size=wx.Size(181, 21), style=0)
        self.botonDefinirCurva.Bind(wx.EVT_BUTTON, self.OnBotonDefinirCurva, id=wxID_DIALOG1BOTONCURVA)
        self.botonDefinirCurva.Show(False)
        self.botonDefinirEscalones = wx.Button(id=wxID_DIALOG1BOTONESCALONES, label=_('Definir consumo por escalones'), name='botonDefinirEscalones', parent=self, pos=wx.Point(496, 178), size=wx.Size(181, 21), style=0)
        self.botonDefinirEscalones.Bind(wx.EVT_BUTTON, self.OnBotonDefinirEscalones, id=wxID_DIALOG1BOTONESCALONES)
        self.botonDefinirEscalones.Show(False)
        self.funcionamientoNoDemanda = wx.RadioBox(choices=[_('Si'),
         _('No')], id=wxID_FUNCIONAMIENTONODEMANDABOX1, label=_('¿Funciona la bomba cuando no hay demanda térmica?'), majorDimension=2, name='radioBox1', parent=self, pos=wx.Point(0, 247), size=wx.Size(710, 95), style=wx.RA_SPECIFY_COLS)
        self.funcionamientoNoDemanda.SetSelection(1)
        self.funcionamientoNoDemanda.Bind(wx.EVT_RADIOBOX, self.OnfuncionamientoNoDemandaRadiobox, id=wxID_FUNCIONAMIENTONODEMANDABOX1)
        self.horasTemporadaAcsText = wx.StaticText(id=-1, label=_('Duración temporada de ACS'), name='horasTemporadaAcsText', parent=self.funcionamientoNoDemanda, pos=wx.Point(15, 45), size=wx.Size(215, 13), style=0)
        self.horasTemporadaAcsText.Show(False)
        self.horasTemporadaAcs = wx.TextCtrl(id=wxID_BOMBAHORASTEMPORADAACS, name='horasTemporadaAcs', parent=self.funcionamientoNoDemanda, pos=wx.Point(230, 43), size=wx.Size(60, 21), style=0, value='')
        self.horasTemporadaAcs.Show(False)
        self.horasTemporadaAcs.SetValue(str(self.numeroHorasAcs))
        self.horasTemporadaAcs.Bind(wx.EVT_TEXT, self.obtenerConsumoEstacional, id=wxID_BOMBAHORASTEMPORADAACS)
        self.horasTemporadaCalefaccionText = wx.StaticText(id=-1, label=_('Duración temporada de calefacción'), name='horasTemporadaCalefaccionText', parent=self.funcionamientoNoDemanda, pos=wx.Point(15, 45), size=wx.Size(215, 13), style=0)
        self.horasTemporadaCalefaccionText.Show(False)
        self.horasTemporadaCalefaccion = wx.TextCtrl(id=wxID_BOMBAHORASTEMPORADACALEFACCION, name='horasTemporadaCalefaccion', parent=self.funcionamientoNoDemanda, pos=wx.Point(230, 43), size=wx.Size(60, 21), style=0, value='')
        self.horasTemporadaCalefaccion.Show(False)
        self.horasTemporadaCalefaccion.SetValue(str(self.numeroHorasCalefaccion))
        self.horasTemporadaCalefaccion.Bind(wx.EVT_TEXT, self.obtenerConsumoEstacional, id=wxID_BOMBAHORASTEMPORADACALEFACCION)
        self.horasTemporadaRefrigeracionText = wx.StaticText(id=-1, label=_('Duración temporada refrigeración'), name='horasTemporadaRefrigeracionText', parent=self.funcionamientoNoDemanda, pos=wx.Point(15, 45), size=wx.Size(215, 13), style=0)
        self.horasTemporadaRefrigeracionText.Show(False)
        self.horasTemporadaRefrigeracion = wx.TextCtrl(id=wxID_BOMBAHORASTEMPORADAREFRIGERACION, name='horasTemporadaRefrigeracion', parent=self.funcionamientoNoDemanda, pos=wx.Point(230, 43), size=wx.Size(60, 21), style=0, value='')
        self.horasTemporadaRefrigeracion.Show(False)
        self.horasTemporadaRefrigeracion.SetValue(str(self.numeroHorasRefrigeracion))
        self.horasTemporadaRefrigeracion.Bind(wx.EVT_TEXT, self.obtenerConsumoEstacional, id=wxID_BOMBAHORASTEMPORADAREFRIGERACION)
        self.horasTemporadaUnidades = wx.StaticText(id=-1, label=_('h'), name='horasTemporadaUnidades', parent=self.funcionamientoNoDemanda, pos=wx.Point(295, 45), size=wx.Size(20, 13), style=0)
        self.horasTemporadaUnidades.Show(False)
        self.fraccionPotenciaNoDemandaText = wx.StaticText(id=-1, label=_('Fracción potencia durante no demanda'), name='fraccionPotenciaNoDemandaText', parent=self.funcionamientoNoDemanda, pos=wx.Point(15, 70), size=wx.Size(215, 13), style=0)
        self.fraccionPotenciaNoDemandaText.Show(False)
        self.fraccionPotenciaNoDemanda = wx.TextCtrl(id=wxID_BOMBAFRACCIONPOTENCIANODEMANDA, name='fraccionPotenciaNoDemanda', parent=self.funcionamientoNoDemanda, pos=wx.Point(230, 68), size=wx.Size(60, 21), style=0, value='')
        self.fraccionPotenciaNoDemanda.Show(False)
        self.fraccionPotenciaNoDemanda.SetValue('0.3')
        self.fraccionPotenciaNoDemanda.Bind(wx.EVT_TEXT, self.obtenerConsumoEstacional, id=wxID_BOMBAFRACCIONPOTENCIANODEMANDA)

    def OnBotonDefinirEscalones(self, event):
        """
        Metodo: OnBotonDefinirEscalones

        ARGUMENTOS:
                event:
        """
        dlg = dialogoEscalones.Dialog1(self, self.potenciaFcp)
        dlg.ShowModal()
        if dlg.dev == True:
            self.potenciaFcp = []
            for i in range(10):
                self.potenciaFcp.append(dlg.potenciaFcp.GetCellValue(0, i))

            self.obtenerConsumoEstacional(None)
            dlg.Destroy()
        return

    def OnBotonDefinirCurva(self, event):
        """
        Metodo: OnBotonDefinirCurva

        ARGUMENTOS:
                event:
        """
        dlg = dialogoCurva.Dialog1(self, self.c1, self.c2, self.c3, self.c4)
        dlg.ShowModal()
        if dlg.dev == True:
            self.c1 = dlg.c1.GetValue()
            self.c2 = dlg.c2.GetValue()
            self.c3 = dlg.c3.GetValue()
            self.c4 = dlg.c4.GetValue()
            self.obtenerConsumoEstacional(None)
            dlg.Destroy()
        return

    def OnNombreInstalacion(self, event):
        """
        Metodo: OnNombreInstalacion

        ARGUMENTOS:
                event:
        """
        if self.nombreInstalacion.GetValue() == _('Bomba'):
            self.nombreInstalacion.SetForegroundColour(wx.Colour(100, 200, 0))
        else:
            self.nombreInstalacion.SetForegroundColour(wx.Colour(0, 0, 0))

    def OnfuncionamientoNoDemandaRadiobox(self, event):
        """
        Metodo: OnfuncionamientoNoDemandaRadiobox

        ARGUMENTOS:
                event:
        """
        eleccion = self.seleccionServicio.GetSelection()
        if eleccion == 0 and self.horasTemporadaAcs.GetValue() == '':
            self.calculoNumeroHorasTemporada()
            self.horasTemporadaAcs.SetValue(str(self.numeroHorasAcs))
        if eleccion == 1 and self.horasTemporadaCalefaccion.GetValue() == '':
            self.calculoNumeroHorasTemporada()
            self.horasTemporadaCalefaccion.SetValue(str(self.numeroHorasCalefaccion))
        elif eleccion == 2 and self.horasTemporadaRefrigeracion.GetValue() == '':
            self.calculoNumeroHorasTemporada()
            self.horasTemporadaRefrigeracion.SetValue(str(self.numeroHorasRefrigeracion))
        if self.fraccionPotenciaNoDemanda.GetValue() == '':
            self.fraccionPotenciaNoDemanda.SetValue('0.3')
        if self.funcionamientoNoDemanda.GetSelection() == 0:
            if eleccion == 0:
                self.horasTemporadaAcsText.Show(True)
                self.horasTemporadaAcs.Show(True)
                self.horasTemporadaCalefaccionText.Show(False)
                self.horasTemporadaCalefaccion.Show(False)
                self.horasTemporadaRefrigeracionText.Show(False)
                self.horasTemporadaRefrigeracion.Show(False)
                self.fraccionPotenciaNoDemandaText.Show(True)
                self.fraccionPotenciaNoDemanda.Show(True)
                self.horasTemporadaUnidades.Show(True)
            else:
                if eleccion == 1:
                    self.horasTemporadaAcsText.Show(False)
                    self.horasTemporadaAcs.Show(False)
                    self.horasTemporadaCalefaccionText.Show(True)
                    self.horasTemporadaCalefaccion.Show(True)
                    self.horasTemporadaRefrigeracionText.Show(False)
                    self.horasTemporadaRefrigeracion.Show(False)
                    self.fraccionPotenciaNoDemandaText.Show(True)
                    self.fraccionPotenciaNoDemanda.Show(True)
                    self.horasTemporadaUnidades.Show(True)
                elif eleccion == 2:
                    self.horasTemporadaAcsText.Show(False)
                    self.horasTemporadaAcs.Show(False)
                    self.horasTemporadaCalefaccionText.Show(False)
                    self.horasTemporadaCalefaccion.Show(False)
                    self.horasTemporadaRefrigeracionText.Show(True)
                    self.horasTemporadaRefrigeracion.Show(True)
                    self.fraccionPotenciaNoDemandaText.Show(True)
                    self.fraccionPotenciaNoDemanda.Show(True)
                    self.horasTemporadaUnidades.Show(True)
        else:
            self.horasTemporadaAcsText.Show(False)
            self.horasTemporadaAcs.Show(False)
            self.horasTemporadaCalefaccionText.Show(False)
            self.horasTemporadaCalefaccion.Show(False)
            self.horasTemporadaRefrigeracionText.Show(False)
            self.horasTemporadaRefrigeracion.Show(False)
            self.fraccionPotenciaNoDemandaText.Show(False)
            self.fraccionPotenciaNoDemanda.Show(False)
            self.horasTemporadaUnidades.Show(False)
        self.obtenerConsumoEstacional(None)
        return

    def calculoNumeroHorasTemporada(self):
        """
        Metodo: OnNombreInstalacion

        """
        if self.parent.parent.parent.programa == 'Residencial':
            self.numeroHorasAcs = 8760.0
            self.numeroHorasCalefaccion = 5760.0
            self.numeroHorasRefrigeracion = 2880.0
        else:
            tipoEdificio = self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
            numeroHoras = calculoNumeroHorasOcupacionEdificio(tipoEdificio)
            self.numeroHorasAcs = numeroHoras
            self.numeroHorasCalefaccion = numeroHoras
            self.numeroHorasRefrigeracion = numeroHoras

    def __init__(self, parent, id, pos, size, style, name, real_parent=None):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
                id:
                pos:
                size:
                style:
                name:
                real_parent = None:
        """
        if real_parent == None:
            self.parent = parent
        else:
            self.parent = real_parent
        self.numeroHorasAcs = ''
        self.numeroHorasCalefaccion = ''
        self.numeroHorasRefrigeracion = ''
        self.calculoNumeroHorasTemporada()
        self._init_ctrls(parent, id, pos, size, style, name)
        self.potenciaFcp = [
         '0.5', '0.5', '0.5', '0.5', '0.5', '1.0', '1.0', 
         '1.0', '1.0', '1.0']
        self.c1 = '0.6'
        self.c2 = '0.4'
        self.c3 = '0.0'
        self.c4 = '0.0'
        self.tipoSistema = 'bombas'
        self.listaErrores = ''
        self.subgrupoChoice.SetItems(self.cargarRaices())
        self.rendimientoEstacionalRef = ''
        self.OnBombaChoice(None)
        self.elegirRaiz()
        self.obtenerConsumoEstacional(None)
        return

    def elegirRaiz(self):
        """
        Metodo: elegirRaiz

        """
        sel = self.parent.arbolInstalaciones.GetSelection()
        try:
            self.subgrupoChoice.SetStringSelection('Edificio Objeto')
            raiz = self.parent.arbolInstalaciones.GetRootItem()
            while sel != raiz:
                for i in range(len(self.parent.parent.subgrupos)):
                    if self.parent.arbolInstalaciones.GetItemText(sel) == '%s' % self.parent.parent.subgrupos[i].nombre:
                        self.subgrupoChoice.SetStringSelection(self.parent.arbolInstalaciones.GetItemText(sel))
                        return

                sel = self.parent.arbolInstalaciones.GetItemParent(sel)

        except:
            logging.info('Excepcion en: %s' % __name__)
            self.subgrupoChoice.SetStringSelection('Edificio Objeto')

    def cargarRaices(self):
        """
        Metodo: cargarRaices

        """
        raices = []
        raices.append(('Edificio Objeto', _('Edificio Objeto')))
        for i in range(len(self.parent.parent.subgrupos)):
            if self.parent.parent.subgrupos[i].nombre != 'Edificio Objeto':
                raices.append((self.parent.parent.subgrupos[i].nombre, self.parent.parent.subgrupos[i].nombre))

        return raices

    def OnBombaChoice(self, event):
        """
        Metodo: OnBombaChoice

        ARGUMENTOS:
                event:
        """
        if self.bombaChoice.GetSelection() == 0:
            self.EstimacionConsumoChoice.SetItems(listadosWeb.listadoOpcionesConsumoBombasOVentiladores)
            self.EstimacionConsumoChoice.SetSelection(0)
        else:
            self.EstimacionConsumoChoice.SetItems(listadosWeb.listadoOpcionesConsumoBombasOVentiladoresCaudalVariable)
            self.EstimacionConsumoChoice.SetSelection(0)
        self.OnEstimacionConsumoChoice(None)
        return

    def OnEstimacionConsumoChoice(self, event):
        """
        Metodo: OnEstimacionConsumoChoice

        ARGUMENTOS:
                event:
        """
        if self.EstimacionConsumoChoice.GetSelection() == 0:
            self.consumo.SetEditable(True)
            self.consumo.Enable(True)
            self.consumoAnualText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
            self.consumoAnualUnidades.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
            self.consumoAnualText.SetForegroundColour(wx.Colour(0, 0, 0))
            self.consumoAnualUnidades.SetForegroundColour(wx.Colour(0, 0, 0))
            self.numeroHorasDemanda.Show(False)
            self.numeroHorasDemandaText.Show(False)
            self.potenciaText.Show(False)
            self.potenciaUnidades.Show(False)
            self.numeroHorasDemandaUnidades.Show(False)
            self.numeroHorasHelpButton.Show(False)
            self.potenciaElectricaNominal.Show(False)
            self.botonDefinirEscalones.Show(False)
            self.botonDefinirCurva.Show(False)
            self.funcionamientoNoDemanda.Show(False)
            self.OnfuncionamientoNoDemandaRadiobox(None)
        else:
            self.funcionamientoNoDemanda.Show(True)
            self.OnfuncionamientoNoDemandaRadiobox(None)
            if self.bombaChoice.GetSelection() == 0 and self.EstimacionConsumoChoice.GetSelection() == 1:
                self.consumo.SetValue('')
                self.consumo.SetEditable(False)
                self.consumo.Enable(False)
                self.consumoAnualText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
                self.consumoAnualUnidades.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
                self.consumoAnualText.SetForegroundColour(wx.Colour(100, 100, 100))
                self.consumoAnualUnidades.SetForegroundColour(wx.Colour(100, 100, 100))
                self.numeroHorasDemanda.Show(True)
                self.numeroHorasDemandaText.Show(True)
                self.potenciaText.Show(True)
                self.potenciaUnidades.Show(True)
                self.numeroHorasDemandaUnidades.Show(True)
                self.numeroHorasHelpButton.Show(True)
                self.potenciaElectricaNominal.Show(True)
                self.botonDefinirEscalones.Show(False)
                self.botonDefinirCurva.Show(False)
            elif self.bombaChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 1:
                self.consumo.SetValue('')
                self.consumo.SetEditable(False)
                self.consumo.Enable(False)
                self.consumoAnualText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
                self.consumoAnualUnidades.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
                self.consumoAnualText.SetForegroundColour(wx.Colour(100, 100, 100))
                self.consumoAnualUnidades.SetForegroundColour(wx.Colour(100, 100, 100))
                self.numeroHorasDemanda.Show(True)
                self.numeroHorasDemandaText.Show(True)
                self.potenciaText.Show(True)
                self.potenciaUnidades.Show(True)
                self.numeroHorasDemandaUnidades.Show(True)
                self.numeroHorasHelpButton.Show(True)
                self.potenciaElectricaNominal.Show(True)
                self.botonDefinirEscalones.Show(True)
                self.botonDefinirCurva.Show(False)
            elif self.bombaChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 2:
                self.consumo.SetValue('')
                self.consumo.SetEditable(False)
                self.consumo.Enable(False)
                self.consumoAnualText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
                self.consumoAnualUnidades.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
                self.consumoAnualText.SetForegroundColour(wx.Colour(100, 100, 100))
                self.consumoAnualUnidades.SetForegroundColour(wx.Colour(100, 100, 100))
                self.numeroHorasDemanda.Show(True)
                self.numeroHorasDemandaText.Show(True)
                self.potenciaText.Show(True)
                self.potenciaUnidades.Show(True)
                self.numeroHorasDemandaUnidades.Show(True)
                self.numeroHorasHelpButton.Show(True)
                self.potenciaElectricaNominal.Show(True)
                self.botonDefinirEscalones.Show(False)
                self.botonDefinirCurva.Show(True)
        self.obtenerConsumoEstacional(None)
        return

    def comprobarDatos(self):
        """
        Metodo: comprobarDatos

        """
        self.listaErrores = ''
        self.listaErrores += Comprueba(self.nombreInstalacion.GetValue(), 1, self.listaErrores, _('nombre')).ErrorDevuelto
        self.listaErrores += Comprueba(self.subgrupoChoice.GetStringSelection(), 0, self.listaErrores, _('zona')).ErrorDevuelto
        self.listaErrores += Comprueba(self.bombaChoice.GetStringSelection(), 0, self.listaErrores, _('tipo de generador')).ErrorDevuelto
        self.listaErrores += Comprueba(self.EstimacionConsumoChoice.GetStringSelection(), 0, self.listaErrores, _('definir estimación consumo')).ErrorDevuelto
        self.listaErrores += Comprueba(self.seleccionServicio.GetStringSelection(), 0, self.listaErrores, _('servicio')).ErrorDevuelto
        if self.EstimacionConsumoChoice.GetSelection() == 0:
            dato = self.consumo.GetValue()
            if ',' in dato:
                dato = dato.replace(',', '.')
                self.consumo.SetValue(dato)
            self.listaErrores += Comprueba(self.consumo.GetValue(), 2, self.listaErrores, _('consumo energético anual'), 0.0).ErrorDevuelto
        else:
            dato = self.potenciaElectricaNominal.GetValue()
            if ',' in dato:
                dato = dato.replace(',', '.')
                self.potenciaElectricaNominal.SetValue(dato)
            dato = self.numeroHorasDemanda.GetValue()
            if ',' in dato:
                dato = dato.replace(',', '.')
                self.numeroHorasDemanda.SetValue(dato)
            if self.bombaChoice.GetSelection() == 0 and self.EstimacionConsumoChoice.GetSelection() == 1:
                self.listaErrores += Comprueba(self.potenciaElectricaNominal.GetValue(), 2, self.listaErrores, _('potencia eléctrica'), 0.0).ErrorDevuelto
                self.listaErrores += Comprueba(self.numeroHorasDemanda.GetValue(), 2, self.listaErrores, _('número de horas de demanda'), 0.0).ErrorDevuelto
            elif self.bombaChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 1:
                self.listaErrores += Comprueba(self.potenciaElectricaNominal.GetValue(), 2, self.listaErrores, _('potencia eléctrica'), 0.0).ErrorDevuelto
                self.listaErrores += Comprueba(self.numeroHorasDemanda.GetValue(), 2, self.listaErrores, _('número de horas de demanda'), 0.0).ErrorDevuelto
                for i in range(10):
                    dato = self.potenciaFcp[i]
                    if ',' in dato:
                        dato = dato.replace(',', '.')
                        self.potenciaFcp[i] = dato
                    self.listaErrores += Comprueba2(self.potenciaFcp[i], 2, self.listaErrores, _('posición %i erronea') % i, 0.0, 1.0).ErrorDevuelto

            elif self.bombaChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 2:
                dato = self.c1
                if ',' in dato:
                    dato = dato.replace(',', '.')
                    self.c1 = dato
                dato = self.c2
                if ',' in dato:
                    dato = dato.replace(',', '.')
                    self.c2 = dato
                dato = self.c3
                if ',' in dato:
                    dato = dato.replace(',', '.')
                    self.c3 = dato
                dato = self.c4
                if ',' in dato:
                    dato = dato.replace(',', '.')
                    self.c4 = dato
                self.listaErrores += Comprueba(self.potenciaElectricaNominal.GetValue(), 2, self.listaErrores, _('potencia eléctrica'), 0.0).ErrorDevuelto
                self.listaErrores += Comprueba(self.numeroHorasDemanda.GetValue(), 2, self.listaErrores, 'número de horas de demanda', 0.0).ErrorDevuelto
                self.listaErrores += Comprueba(self.c1, 2, self.listaErrores, _('coeficiente C1')).ErrorDevuelto
                self.listaErrores += Comprueba(self.c2, 2, self.listaErrores, _('coeficiente C2')).ErrorDevuelto
                self.listaErrores += Comprueba(self.c3, 2, self.listaErrores, _('coeficiente C3')).ErrorDevuelto
                self.listaErrores += Comprueba(self.c4, 2, self.listaErrores, _('coeficiente C4')).ErrorDevuelto
            ErrorNumeroHorasDemanda = Comprueba(self.numeroHorasDemanda.GetValue(), 2, self.listaErrores, _('número de horas de demanda'), 0.0).ErrorDevuelto
            if self.funcionamientoNoDemanda.GetSelection() == 0:
                if self.seleccionServicio.GetSelection() == 0:
                    dato = self.horasTemporadaAcs.GetValue()
                    if ',' in dato:
                        dato = dato.replace(',', '.')
                        self.horasTemporadaAcs.SetValue(dato)
                    dato = self.fraccionPotenciaNoDemanda.GetValue()
                    if ',' in dato:
                        dato = dato.replace(',', '.')
                        self.fraccionPotenciaNoDemanda.SetValue(dato)
                    if ErrorNumeroHorasDemanda != '':
                        self.listaErrores += Comprueba(self.horasTemporadaAcs.GetValue(), 2, self.listaErrores, _('número de horas temporada ACS'), 0.0).ErrorDevuelto
                    else:
                        self.listaErrores += Comprueba2(self.horasTemporadaAcs.GetValue(), 2, self.listaErrores, _('número de horas temporada ACS'), float(self.numeroHorasDemanda.GetValue())).ErrorDevuelto
                    self.listaErrores += Comprueba(self.fraccionPotenciaNoDemanda.GetValue(), 2, self.listaErrores, _('fracción potencia durante no demanda'), 0.0, 1.0).ErrorDevuelto
                else:
                    if self.seleccionServicio.GetSelection() == 1:
                        dato = self.horasTemporadaCalefaccion.GetValue()
                        if ',' in dato:
                            dato = dato.replace(',', '.')
                            self.horasTemporadaCalefaccion.SetValue(dato)
                        dato = self.fraccionPotenciaNoDemanda.GetValue()
                        if ',' in dato:
                            dato = dato.replace(',', '.')
                            self.fraccionPotenciaNoDemanda.SetValue(dato)
                        if ErrorNumeroHorasDemanda != '':
                            self.listaErrores += Comprueba(self.horasTemporadaCalefaccion.GetValue(), 2, self.listaErrores, _('duración temporada de calefacción'), 0.0).ErrorDevuelto
                        else:
                            self.listaErrores += Comprueba2(self.horasTemporadaCalefaccion.GetValue(), 2, self.listaErrores, _('duración temporada de calefacción'), float(self.numeroHorasDemanda.GetValue())).ErrorDevuelto
                        self.listaErrores += Comprueba(self.fraccionPotenciaNoDemanda.GetValue(), 2, self.listaErrores, _('fracción potencia durante no demanda'), 0.0, 1.0).ErrorDevuelto
                    elif self.seleccionServicio.GetSelection() == 2:
                        dato = self.horasTemporadaRefrigeracion.GetValue()
                        if ',' in dato:
                            dato = dato.replace(',', '.')
                            self.horasTemporadaRefrigeracion.SetValue(dato)
                        dato = self.fraccionPotenciaNoDemanda.GetValue()
                        if ',' in dato:
                            dato = dato.replace(',', '.')
                            self.fraccionPotenciaNoDemanda.SetValue(dato)
                        if ErrorNumeroHorasDemanda != '':
                            self.listaErrores += Comprueba(self.horasTemporadaRefrigeracion.GetValue(), 2, self.listaErrores, _('duración temporada de refrigeración'), 0.0).ErrorDevuelto
                        else:
                            self.listaErrores += Comprueba2(self.horasTemporadaRefrigeracion.GetValue(), 2, self.listaErrores, _('duración temporada de refrigeración'), float(self.numeroHorasDemanda.GetValue())).ErrorDevuelto
                        self.listaErrores += Comprueba(self.fraccionPotenciaNoDemanda.GetValue(), 2, self.listaErrores, _('fracción potencia durante no demanda'), 0.0, 1.0).ErrorDevuelto

    def OnSeleccionServicioChoice(self, event):
        """
        Metodo: OnSeleccionServicioChoice

        ARGUMENTOS:
                event:
        """
        eleccion = self.seleccionServicio.GetSelection()
        if self.funcionamientoNoDemanda.GetSelection() == 0:
            if eleccion == 0:
                self.horasTemporadaAcsText.Show(True)
                self.horasTemporadaAcs.Show(True)
                self.horasTemporadaCalefaccionText.Show(False)
                self.horasTemporadaCalefaccion.Show(False)
                self.horasTemporadaRefrigeracionText.Show(False)
                self.horasTemporadaRefrigeracion.Show(False)
                self.fraccionPotenciaNoDemandaText.Show(False)
                self.fraccionPotenciaNoDemanda.Show(False)
                self.fraccionPotenciaNoDemanda.Show(False)
            else:
                if eleccion == 1:
                    self.horasTemporadaAcsText.Show(False)
                    self.horasTemporadaAcs.Show(False)
                    self.horasTemporadaCalefaccionText.Show(True)
                    self.horasTemporadaCalefaccion.Show(True)
                    self.horasTemporadaRefrigeracionText.Show(False)
                    self.horasTemporadaRefrigeracion.Show(False)
                    self.fraccionPotenciaNoDemandaText.Show(True)
                    self.fraccionPotenciaNoDemanda.Show(True)
                    self.horasTemporadaUnidades.Show(True)
                elif eleccion == 2:
                    self.horasTemporadaAcsText.Show(False)
                    self.horasTemporadaAcs.Show(False)
                    self.horasTemporadaCalefaccionText.Show(False)
                    self.horasTemporadaCalefaccion.Show(False)
                    self.horasTemporadaRefrigeracionText.Show(True)
                    self.horasTemporadaRefrigeracion.Show(True)
                    self.fraccionPotenciaNoDemandaText.Show(True)
                    self.fraccionPotenciaNoDemanda.Show(True)
                    self.horasTemporadaUnidades.Show(True)
        else:
            self.horasTemporadaAcsText.Show(False)
            self.horasTemporadaAcs.Show(False)
            self.horasTemporadaCalefaccionText.Show(False)
            self.horasTemporadaCalefaccion.Show(False)
            self.horasTemporadaRefrigeracionText.Show(False)
            self.horasTemporadaRefrigeracion.Show(False)
            self.fraccionPotenciaNoDemandaText.Show(False)
            self.fraccionPotenciaNoDemanda.Show(False)
            self.horasTemporadaUnidades.Show(False)
        self.OnEstimacionConsumoChoice(None)
        return

    def cogerDatos(self):
        """
        Metodo: cogerDatos

        """
        self.comprobarDatos()
        if self.listaErrores != '':
            return self.listaErrores
        else:
            datos = []
            datos.append(self.nombreInstalacion.GetValue())
            datos.append(self.tipoSistema)
            datos.append(self.consumo.GetValue())
            datos.append(self.bombaChoice.GetSelection())
            datos.append(self.potenciaElectricaNominal.GetValue())
            datos.append('')
            datos.append(self.EstimacionConsumoChoice.GetSelection())
            datos.append(self.numeroHorasDemanda.GetValue())
            datos.append(self.c1)
            datos.append(self.c2)
            datos.append(self.c3)
            datos.append(self.c4)
            datos.append(self.seleccionServicio.GetSelection())
            self.OnSeleccionServicioChoice(None)
            if self.funcionamientoNoDemanda.GetSelection() == 0:
                datos.append(self.horasTemporadaAcs.GetValue())
                datos.append(self.horasTemporadaCalefaccion.GetValue())
                datos.append(self.horasTemporadaRefrigeracion.GetValue())
                datos.append(self.fraccionPotenciaNoDemanda.GetValue())
            else:
                datos.append('')
                datos.append('')
                datos.append('')
                datos.append('')
            datosConcretos = []
            for i in range(10):
                datosConcretos.append(self.potenciaFcp[i])

            datos.append(datosConcretos)
            datos.append(self.funcionamientoNoDemanda.GetSelection())
            datos.append(self.subgrupoChoice.GetStringSelection())
            return datos

    def cargarDatos(self, datos):
        """
        Metodo: cargarDatos

        ARGUMENTOS:
                datos:
        """
        self.nombreInstalacion.SetValue(datos[0])
        self.consumo.SetValue(datos[2])
        self.bombaChoice.SetSelection(datos[3])
        self.OnBombaChoice(None)
        self.potenciaElectricaNominal.SetValue(datos[4])
        self.EstimacionConsumoChoice.SetSelection(datos[6])
        self.OnEstimacionConsumoChoice(None)
        self.numeroHorasDemanda.SetValue(datos[7])
        self.c1 = datos[8]
        self.c2 = datos[9]
        self.c3 = datos[10]
        self.c4 = datos[11]
        self.seleccionServicio.SetSelection(datos[12])
        self.horasTemporadaAcs.SetValue(datos[13])
        self.horasTemporadaCalefaccion.SetValue(datos[14])
        self.horasTemporadaRefrigeracion.SetValue(datos[15])
        self.fraccionPotenciaNoDemanda.SetValue(datos[16])
        datosConcretos = datos[17]
        for i in range(10):
            self.potenciaFcp[i] = datosConcretos[i]

        self.funcionamientoNoDemanda.SetSelection(datos[18])
        self.OnfuncionamientoNoDemandaRadiobox(None)
        self.subgrupoChoice.SetStringSelection(datos[-1])
        return

    def obtenerConsumoEstacional(self, event):
        """
        Metodo: obtenerConsumoEstacional

        ARGUMENTOS:
                event):  #funcion para otener el rendimiento medio estacion:
        """
        try:
            zona = self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()
            if self.parent.parent.parent.programa == 'Residencial':
                uso = 'Residencial'
            else:
                uso = self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
            if self.seleccionServicio.GetStringSelection() == 'Calefacción':
                repartoEnergiaPorcentualCaracteristico = perfilesTerciario.PerfilDemandaCalefaccion(zona, uso)
            elif self.seleccionServicio.GetStringSelection() == 'Refrigeración':
                repartoEnergiaPorcentualCaracteristico = perfilesTerciario.PerfilDemandaRefrigeracion(zona, uso)
            else:
                repartoEnergiaPorcentualCaracteristico = [
                 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                 0.0, 0.0, 0.0, 1.0]
            fcpSistema = [
             0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 
             0.75, 0.85, 0.95]
            aux = [ repartoEnergiaPorcentualCaracteristico[i] / fcpSistema[i] for i in range(len(fcpSistema)) ]
            total = sum(aux)
            repartoTiempoPorcentualCaracteristico = [ x / total for x in aux ]
            eleccion = self.seleccionServicio.GetSelection()
            horasTodaTemporada = 0
            if self.funcionamientoNoDemanda.GetSelection() == 0:
                if eleccion == 0:
                    horasTodaTemporada = float(self.horasTemporadaAcs.GetValue())
                    horasDemanda = float(self.numeroHorasDemanda.GetValue())
                    if horasTodaTemporada < horasDemanda:
                        self.consumo.SetValue('')
                        return
                else:
                    if eleccion == 1:
                        horasTodaTemporada = float(self.horasTemporadaCalefaccion.GetValue())
                        horasDemanda = float(self.numeroHorasDemanda.GetValue())
                        if horasTodaTemporada < horasDemanda:
                            self.consumo.SetValue('')
                            return
                    elif eleccion == 2:
                        horasTodaTemporada = float(self.horasTemporadaRefrigeracion.GetValue())
                        horasDemanda = float(self.numeroHorasDemanda.GetValue())
                        if horasTodaTemporada < horasDemanda:
                            self.consumo.SetValue('')
                            return
            if self.EstimacionConsumoChoice.GetSelection() == 0:
                pass
            elif self.bombaChoice.GetSelection() == 0 and self.EstimacionConsumoChoice.GetSelection() == 1:
                consumoAnual = float(self.potenciaElectricaNominal.GetValue()) * float(self.numeroHorasDemanda.GetValue())
                horasAdicionales = horasTodaTemporada - float(self.numeroHorasDemanda.GetValue())
                if horasAdicionales < 0:
                    horasAdicionales = 0
                if self.funcionamientoNoDemanda.GetSelection() == 0:
                    consumoAnual += horasAdicionales * float(self.potenciaElectricaNominal.GetValue()) * float(self.fraccionPotenciaNoDemanda.GetValue())
                self.consumo.SetValue(str(round(consumoAnual, 1)))
            elif self.bombaChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 1:
                bomba = equipos.bombaCaudalVariable2()
                bomba.escalonesPotencia = []
                for i in range(10):
                    bomba.fcp.append(i / 10.0 + 0.1)
                    bomba.escalonesPotencia.append(float(self.potenciaFcp[i]))

                bomba.potenciaElectricaNominal = float(self.potenciaElectricaNominal.GetValue())
                potenciaEnCadaFcp = [ bomba.potFCP(x) for x in fcpSistema ]
                potenciaMediaEstacional = sum([ potenciaEnCadaFcp[i] * repartoTiempoPorcentualCaracteristico[i] for i in range(len(potenciaEnCadaFcp))
                                              ])
                consumoAnual = potenciaMediaEstacional * float(self.numeroHorasDemanda.GetValue())
                horasAdicionales = horasTodaTemporada - float(self.numeroHorasDemanda.GetValue())
                if horasAdicionales < 0:
                    horasAdicionales = 0
                if self.funcionamientoNoDemanda.GetSelection() == 0:
                    consumoAnual += horasAdicionales * bomba.potFCP(float(self.fraccionPotenciaNoDemanda.GetValue()))
                self.consumo.SetValue(str(round(consumoAnual, 1)))
            elif self.bombaChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 2:
                bomba = equipos.bombaCaudalVariable()
                bomba.c1 = float(self.c1)
                bomba.c2 = float(self.c2)
                bomba.c3 = float(self.c3)
                bomba.c4 = float(self.c4)
                bomba.potenciaElectricaNominal = float(self.potenciaElectricaNominal.GetValue())
                potenciaEnCadaFcp = [ bomba.potFCP(x) for x in fcpSistema ]
                potenciaMediaEstacional = sum([ potenciaEnCadaFcp[i] * repartoTiempoPorcentualCaracteristico[i] for i in range(len(potenciaEnCadaFcp))
                                              ])
                consumoAnual = potenciaMediaEstacional * float(self.numeroHorasDemanda.GetValue())
                horasAdicionales = horasTodaTemporada - float(self.numeroHorasDemanda.GetValue())
                if horasAdicionales < 0:
                    horasAdicionales = 0
                if self.funcionamientoNoDemanda.GetSelection() == 0:
                    consumoAnual += horasAdicionales * bomba.potFCP(float(self.fraccionPotenciaNoDemanda.GetValue()))
                self.consumo.SetValue(str(round(consumoAnual, 1)))
        except:
            self.consumo.SetValue('')

    def OnNumeroHorasHelpButton(self, event):
        """
        Metodo: OnNumeroHorasHelpButton

        ARGUMENTOS:
                event:
        """
        zona = self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()
        perfilUso = self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
        servicio = self.seleccionServicio.GetStringSelection()
        if zona == '':
            wx.MessageBox(_('Debe indicar la localización del edificio en el panel de datos generales'), _('Estimación del número de horas de funcionamiento'))
        else:
            self.parent.parent.parent.calculoCalificacion()
            ayuda = ayudaNumeroHoras.Dialog1(self, zona, perfilUso, servicio)
            ayuda.ShowModal()
            if ayuda.dev != []:
                self.numeroHorasDemanda.SetValue(str(ayuda.dev[0]))