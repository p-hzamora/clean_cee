# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\panelTorresRefrigeracion.pyc
# Compiled at: 2015-02-19 13:18:33
"""
Modulo: panelTorresRefrigeracion.py

"""
from Instalaciones.comprobarCampos import Comprueba, Comprueba2
from miChoice import MiChoice
import Instalaciones.ayudaNumeroHoras as ayudaNumeroHoras, Instalaciones.dialogoCurva as dialogoCurva, Instalaciones.dialogoEscalones as dialogoEscalones, Instalaciones.equipos as equipos, Instalaciones.perfilesTerciario as perfilesTerciario, Calculos.listadosWeb as listadosWeb, wx, logging
wxID_PANEL1, wxID_PANEL1TORRECHOICE, wxID_PANEL1NOMBREINSTALACION, wxID_PANEL1NOMBREINSTALACIONTEXT, wxID_PANEL1RENDIMIENTOTEXT, wxID_PANEL1SUBGRUPOCHOICE, wxID_PANEL1SUBGRUPOTEXT, wxID_PANEL1TIPOTORRETEXT, wxID_PANEL1ESTIMACIONCONSUMOTEXT, wxID_PANEL1ESTIMACIONCONSUMO, wxID_TORRECONSTANTEPOTENCIAELECTRICANOMINAL, wxID_TORRECONSTANTENUMEROHORASDEMANDA, wxID_TORRECONSTANTECONSUMO, wxID_TORREC1, wxID_TORREC2, wxID_TORREC3, wxID_TORREC4, wxID_POTENCIAFCPGRID1, wxID_CARACTERISTICASLINEATEXT, wxID_EFICIENCIALINEATEXT, wxID_DIALOG1BOTONCURVA, wxID_DIALOG1BOTONESCALONES, wxID_AYUDANUMEROHORASDEMANDA = [ wx.NewId() for _init_ctrls in range(23) ]

class Panel1(wx.Panel):
    """
    Clase: Panel1 del modulo panelTorresRefrigeracion.py

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
        wx.Panel.__init__(self, id=id, name=named, parent=prnt, pos=posi, size=siz, style=styles)
        self.SetBackgroundColour('white')
        self.nombreInstalacionText = wx.StaticText(id=wxID_PANEL1NOMBREINSTALACIONTEXT, label=_('Nombre'), name='nombreInstalacionText', parent=self, pos=wx.Point(15, 2), size=wx.Size(102, 13), style=0)
        self.nombreInstalacion = wx.TextCtrl(id=wxID_PANEL1NOMBREINSTALACION, name='nombreInstalacion', parent=self, pos=wx.Point(170, 0), size=wx.Size(230, 21), style=0, value=_('Torre de refrigeración'))
        self.nombreInstalacion.SetForegroundColour(wx.Colour(100, 200, 0))
        self.nombreInstalacion.Bind(wx.EVT_TEXT, self.OnNombreInstalacion, id=wxID_PANEL1NOMBREINSTALACION)
        self.subgrupoText = wx.StaticText(id=wxID_PANEL1SUBGRUPOTEXT, label=_('Zona'), name='subgrupoText', parent=self, pos=wx.Point(435, 2), size=wx.Size(50, 13), style=0)
        self.subgrupoChoice = MiChoice(choices=[], id=wxID_PANEL1SUBGRUPOCHOICE, name='subgrupoChoice', parent=self, pos=wx.Point(496, 0), size=wx.Size(214, 21), style=0)
        self.tipoTorreText = wx.StaticText(id=wxID_PANEL1TIPOTORRETEXT, label=_('Tipo de torre'), name='tipoGeneradorText', parent=self, pos=wx.Point(15, 46), size=wx.Size(89, 13), style=0)
        self.CaracteristicasLineaText = wx.StaticBox(id=wxID_CARACTERISTICASLINEATEXT, label=_('Características'), name='CaracteristicasLineaText', parent=self, pos=wx.Point(0, 26), size=wx.Size(400, 77), style=0)
        self.CaracteristicasLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.torreChoice = MiChoice(choices=listadosWeb.listadoOpcionesTorreDeRefrigeracion, id=wxID_PANEL1TORRECHOICE, name='torreChoice', parent=self, pos=wx.Point(170, 44), size=wx.Size(222, 21), style=0)
        self.torreChoice.SetSelection(0)
        self.torreChoice.Bind(wx.EVT_CHOICE, self.OnTorreChoice, id=wxID_PANEL1TORRECHOICE)
        self.EficienciaLineaText = wx.StaticBox(id=wxID_EFICIENCIALINEATEXT, label=_('Consumo energético anual'), name='EficienciaLineaText', parent=self, pos=wx.Point(0, 107), size=wx.Size(710, 135), style=0)
        self.EficienciaLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.EficienciaLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.EstimacionConsumoText = wx.StaticText(id=wxID_PANEL1ESTIMACIONCONSUMOTEXT, label=_('Consumo energético'), name='rendimientoText', parent=self, pos=wx.Point(15, 130), size=wx.Size(155, 25), style=0)
        self.EstimacionConsumoText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.EstimacionConsumoChoice = MiChoice(choices=listadosWeb.listadoOpcionesConsumoBombasOVentiladores, id=wxID_PANEL1ESTIMACIONCONSUMO, name='rendimientoChoice', parent=self, pos=wx.Point(170, 128), size=wx.Size(220, 21), style=0)
        self.EstimacionConsumoChoice.SetSelection(0)
        self.EstimacionConsumoChoice.Bind(wx.EVT_CHOICE, self.OnEstimacionConsumoChoice, id=wxID_PANEL1ESTIMACIONCONSUMO)
        self.consumoAnualText = wx.StaticText(id=-1, label=_('Consumo energético anual'), name='consumoAnualText', parent=self, pos=wx.Point(435, 130), size=wx.Size(180, 13), style=0)
        self.consumo = wx.TextCtrl(id=wxID_TORRECONSTANTECONSUMO, name='consumo', parent=self, pos=wx.Point(617, 128), size=wx.Size(60, 21), style=0, value='')
        self.consumo.SetEditable(False)
        self.consumo.Enable(True)
        self.consumoAnualUnidades = wx.StaticText(id=-1, label=_('kWh'), name='consumoAnualText', parent=self, pos=wx.Point(682, 130), size=wx.Size(20, 13), style=0)
        self.potenciaText = wx.StaticText(id=-1, label=_('Potencia eléctrica nominal'), name='potenciaText', parent=self, pos=wx.Point(15, 155), size=wx.Size(120, 13), style=0)
        self.potenciaText.Show(False)
        self.potenciaElectricaNominal = wx.TextCtrl(id=wxID_TORRECONSTANTEPOTENCIAELECTRICANOMINAL, name='potenciaElectricaNominal', parent=self, pos=wx.Point(170, 153), size=wx.Size(60, 21), style=0, value='')
        self.potenciaElectricaNominal.Show(False)
        self.potenciaElectricaNominal.Bind(wx.EVT_TEXT, self.obtenerConsumoEstacional, id=wxID_TORRECONSTANTEPOTENCIAELECTRICANOMINAL)
        self.potenciaUnidades = wx.StaticText(id=-1, label=_('kW'), name='potenciaText', parent=self, pos=wx.Point(235, 155), size=wx.Size(20, 13), style=0)
        self.potenciaUnidades.Show(False)
        self.numeroHorasDemandaText = wx.StaticText(id=-1, label=_('Número de horas de demanda'), name='numeroHorasDemandaText', parent=self, pos=wx.Point(15, 180), size=wx.Size(150, 13), style=0)
        self.numeroHorasDemandaText.Show(False)
        self.numeroHorasDemanda = wx.TextCtrl(id=wxID_TORRECONSTANTENUMEROHORASDEMANDA, name='numeroHorasDemanda', parent=self, pos=wx.Point(170, 178), size=wx.Size(60, 21), style=0, value='')
        self.numeroHorasDemanda.Show(False)
        self.numeroHorasDemanda.Bind(wx.EVT_TEXT, self.obtenerConsumoEstacional, id=wxID_TORRECONSTANTENUMEROHORASDEMANDA)
        self.numeroHorasDemandaUnidades = wx.StaticText(id=-1, label=_('h'), name='numeroHorasDemanda', parent=self, pos=wx.Point(235, 180), size=wx.Size(20, 13), style=0)
        self.numeroHorasDemandaUnidades.Show(False)
        self.botonDefinirCurva = wx.Button(id=wxID_DIALOG1BOTONCURVA, label=_('Definir curva de consumo'), name='botonDefinirCurva', parent=self, pos=wx.Point(496, 178), size=wx.Size(181, 21), style=0)
        self.botonDefinirCurva.Bind(wx.EVT_BUTTON, self.OnBotonDefinirCurva, id=wxID_DIALOG1BOTONCURVA)
        self.botonDefinirCurva.Show(False)
        self.botonDefinirEscalones = wx.Button(id=wxID_DIALOG1BOTONESCALONES, label=_('Definir consumo por escalones'), name='botonDefinirEscalones', parent=self, pos=wx.Point(496, 178), size=wx.Size(181, 21), style=0)
        self.botonDefinirEscalones.Bind(wx.EVT_BUTTON, self.OnBotonDefinirEscalones, id=wxID_DIALOG1BOTONESCALONES)
        self.botonDefinirEscalones.Show(False)
        self.numeroHorasHelpButton = wx.Button(id=wxID_AYUDANUMEROHORASDEMANDA, label=_(' ?'), name='numeroHorasHelpButton', parent=self, pos=wx.Point(250, 178), size=wx.Size(20, 20), style=0)
        self.numeroHorasHelpButton.Bind(wx.EVT_BUTTON, self.OnNumeroHorasHelpButton, id=wxID_AYUDANUMEROHORASDEMANDA)
        self.numeroHorasHelpButton.Show(False)

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
        if self.nombreInstalacion.GetValue() == _('Torre de refrigeración'):
            self.nombreInstalacion.SetForegroundColour(wx.Colour(100, 200, 0))
        else:
            self.nombreInstalacion.SetForegroundColour(wx.Colour(0, 0, 0))

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
        self._init_ctrls(parent, id, pos, size, style, name)
        self.potenciaFcp = [
         '0.5', '0.5', '0.5', '0.5', '0.5', '1.0', '1.0', 
         '1.0', '1.0', '1.0']
        self.c1 = '0.3316'
        self.c2 = '-0.8856'
        self.c3 = '0.6055'
        self.c4 = '0.9484'
        self.tipoSistema = 'torresRefrigeracion'
        self.listaErrores = ''
        self.subgrupoChoice.SetItems(self.cargarRaices())
        self.rendimientoEstacionalRef = ''
        self.OnTorreChoice(None)
        self.elegirRaiz()
        self.obtenerConsumoEstacional(None)
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
            repartoEnergiaPorcentualCaracteristico = perfilesTerciario.PerfilDemandaRefrigeracion(zona, uso)
            fcpSistema = [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]
            aux = [ repartoEnergiaPorcentualCaracteristico[i] / fcpSistema[i] for i in range(len(fcpSistema)) ]
            total = sum(aux)
            repartoTiempoPorcentualCaracteristico = [ x / total for x in aux ]
            if self.EstimacionConsumoChoice.GetSelection() == 0:
                pass
            elif self.torreChoice.GetSelection() == 0 and self.EstimacionConsumoChoice.GetSelection() == 1:
                consumoAnual = float(self.potenciaElectricaNominal.GetValue()) * float(self.numeroHorasDemanda.GetValue())
                self.consumo.SetValue(str(round(consumoAnual, 1)))
            elif self.torreChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 1:
                torre = equipos.TorreRefrigeracionVelocidadVariable2()
                torre.escalonesPotencia = []
                for i in range(10):
                    torre.fcp.append(i / 10.0 + 0.1)
                    torre.escalonesPotencia.append(float(self.potenciaFcp[i]))

                torre.potenciaElectricaNominal = float(self.potenciaElectricaNominal.GetValue())
                potenciaEnCadaFcp = [ torre.potFCP(x) for x in fcpSistema ]
                potenciaMediaEstacional = sum([ potenciaEnCadaFcp[i] * repartoTiempoPorcentualCaracteristico[i] for i in range(len(potenciaEnCadaFcp))
                                              ])
                consumoAnual = potenciaMediaEstacional * float(self.numeroHorasDemanda.GetValue())
                self.consumo.SetValue(str(round(consumoAnual, 1)))
            elif self.torreChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 2:
                torre = equipos.TorreRefrigeracionVelocidadVariable()
                torre.c1 = float(self.c1)
                torre.c2 = float(self.c2)
                torre.c3 = float(self.c3)
                torre.c4 = float(self.c4)
                torre.potenciaElectricaNominal = float(self.potenciaElectricaNominal.GetValue())
                potenciaEnCadaFcp = [ torre.potFCP(x) for x in fcpSistema ]
                potenciaMediaEstacional = sum([ potenciaEnCadaFcp[i] * repartoTiempoPorcentualCaracteristico[i] for i in range(len(potenciaEnCadaFcp))
                                              ])
                consumoAnual = potenciaMediaEstacional * float(self.numeroHorasDemanda.GetValue())
                self.consumo.SetValue(str(round(consumoAnual, 1)))
        except:
            self.consumo.SetValue('')

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

    def OnTorreChoice(self, event):
        """
        Metodo: OnTorreChoice

        ARGUMENTOS:
                event:
        """
        if self.torreChoice.GetSelection() == 0:
            self.EstimacionConsumoChoice.SetItems(listadosWeb.listadoOpcionesConsumoBombasOVentiladores)
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
            self.numeroHorasHelpButton.Show(False)
            self.potenciaText.Show(False)
            self.potenciaUnidades.Show(False)
            self.numeroHorasDemandaUnidades.Show(False)
            self.potenciaElectricaNominal.Show(False)
            self.botonDefinirEscalones.Show(False)
            self.botonDefinirCurva.Show(False)
        elif self.torreChoice.GetSelection() == 0 and self.EstimacionConsumoChoice.GetSelection() == 1:
            self.consumo.SetValue('')
            self.consumo.SetEditable(False)
            self.consumo.Enable(False)
            self.consumoAnualText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
            self.consumoAnualUnidades.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
            self.consumoAnualText.SetForegroundColour(wx.Colour(100, 100, 100))
            self.consumoAnualUnidades.SetForegroundColour(wx.Colour(100, 100, 100))
            self.numeroHorasDemanda.Show(True)
            self.numeroHorasDemandaText.Show(True)
            self.numeroHorasHelpButton.Show(True)
            self.potenciaText.Show(True)
            self.potenciaUnidades.Show(True)
            self.numeroHorasDemandaUnidades.Show(True)
            self.potenciaElectricaNominal.Show(True)
            self.botonDefinirEscalones.Show(False)
            self.botonDefinirCurva.Show(False)
        elif self.torreChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 1:
            self.consumo.SetValue('')
            self.consumo.SetEditable(False)
            self.consumo.Enable(False)
            self.consumoAnualText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
            self.consumoAnualUnidades.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
            self.consumoAnualText.SetForegroundColour(wx.Colour(100, 100, 100))
            self.consumoAnualUnidades.SetForegroundColour(wx.Colour(100, 100, 100))
            self.numeroHorasDemanda.Show(True)
            self.numeroHorasDemandaText.Show(True)
            self.numeroHorasHelpButton.Show(True)
            self.potenciaText.Show(True)
            self.potenciaUnidades.Show(True)
            self.numeroHorasDemandaUnidades.Show(True)
            self.potenciaElectricaNominal.Show(True)
            self.botonDefinirEscalones.Show(True)
            self.botonDefinirCurva.Show(False)
        elif self.torreChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 2:
            self.consumo.SetValue('')
            self.consumo.SetEditable(False)
            self.consumo.Enable(False)
            self.consumoAnualText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
            self.consumoAnualUnidades.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
            self.consumoAnualText.SetForegroundColour(wx.Colour(100, 100, 100))
            self.consumoAnualUnidades.SetForegroundColour(wx.Colour(100, 100, 100))
            self.numeroHorasDemanda.Show(True)
            self.numeroHorasDemandaText.Show(True)
            self.numeroHorasHelpButton.Show(True)
            self.potenciaText.Show(True)
            self.potenciaUnidades.Show(True)
            self.numeroHorasDemandaUnidades.Show(True)
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
        self.listaErrores += Comprueba(self.torreChoice.GetStringSelection(), 0, self.listaErrores, _('tipo de generador')).ErrorDevuelto
        self.listaErrores += Comprueba(self.EstimacionConsumoChoice.GetStringSelection(), 0, self.listaErrores, _('definir estimación consumo')).ErrorDevuelto
        if self.EstimacionConsumoChoice.GetSelection() == 0:
            dato = self.consumo.GetValue()
            if ',' in dato:
                dato = dato.replace(',', '.')
                self.consumo.SetValue(dato)
            self.listaErrores += Comprueba(self.consumo.GetValue(), 2, self.listaErrores, _('consumo anual'), 0.0).ErrorDevuelto
        else:
            dato = self.potenciaElectricaNominal.GetValue()
            if ',' in dato:
                dato = dato.replace(',', '.')
                self.potenciaElectricaNominal.SetValue(dato)
            dato = self.numeroHorasDemanda.GetValue()
            if ',' in dato:
                dato = dato.replace(',', '.')
                self.numeroHorasDemanda.SetValue(dato)
            if self.torreChoice.GetSelection() == 0 and self.EstimacionConsumoChoice.GetSelection() == 1:
                self.listaErrores += Comprueba(self.potenciaElectricaNominal.GetValue(), 2, self.listaErrores, _('potencia eléctrica'), 0.0).ErrorDevuelto
                self.listaErrores += Comprueba(self.numeroHorasDemanda.GetValue(), 2, self.listaErrores, _('número de horas de demanda'), 0.0).ErrorDevuelto
            elif self.torreChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 1:
                self.listaErrores += Comprueba(self.potenciaElectricaNominal.GetValue(), 2, self.listaErrores, _('potencia eléctrica'), 0.0).ErrorDevuelto
                self.listaErrores += Comprueba(self.numeroHorasDemanda.GetValue(), 2, self.listaErrores, _('número de horas de demanda'), 0.0).ErrorDevuelto
                for i in range(10):
                    dato = self.potenciaFcp[i]
                    if ',' in dato:
                        dato = dato.replace(',', '.')
                        self.potenciaFcp[i] = dato
                    self.listaErrores += Comprueba2(self.potenciaFcp[i], 2, self.listaErrores, 'posición %i erronea' % i, 0.0, 1.0).ErrorDevuelto

            elif self.torreChoice.GetSelection() == 1 and self.EstimacionConsumoChoice.GetSelection() == 2:
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
                self.listaErrores += Comprueba(self.numeroHorasDemanda.GetValue(), 2, self.listaErrores, _('número de horas de demanda'), 0.0).ErrorDevuelto
                self.listaErrores += Comprueba(self.c1, 2, self.listaErrores, _('coeficiente C1')).ErrorDevuelto
                self.listaErrores += Comprueba(self.c2, 2, self.listaErrores, _('coeficiente C2')).ErrorDevuelto
                self.listaErrores += Comprueba(self.c3, 2, self.listaErrores, _('coeficiente C3')).ErrorDevuelto
                self.listaErrores += Comprueba(self.c4, 2, self.listaErrores, _('coeficiente C4')).ErrorDevuelto

    def cogerDatos(self):
        """
        Metodo: cogerDatos

        """
        self.comprobarDatos()
        if self.listaErrores != '':
            return self.listaErrores
        datos = []
        datos.append(self.nombreInstalacion.GetValue())
        datos.append(self.tipoSistema)
        datos.append(self.consumo.GetValue())
        datos.append(self.torreChoice.GetSelection())
        datos.append(self.potenciaElectricaNominal.GetValue())
        datos.append('')
        datos.append(self.EstimacionConsumoChoice.GetSelection())
        datos.append(self.numeroHorasDemanda.GetValue())
        datos.append(self.c1)
        datos.append(self.c2)
        datos.append(self.c3)
        datos.append(self.c4)
        datosConcretos = []
        for i in range(10):
            datosConcretos.append(self.potenciaFcp[i])

        datos.append(datosConcretos)
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
        self.torreChoice.SetSelection(datos[3])
        self.OnTorreChoice(None)
        self.potenciaElectricaNominal.SetValue(datos[4])
        self.EstimacionConsumoChoice.SetSelection(datos[6])
        self.OnEstimacionConsumoChoice(None)
        self.numeroHorasDemanda.SetValue(datos[7])
        self.c1 = datos[8]
        self.c2 = datos[9]
        self.c3 = datos[10]
        self.c4 = datos[11]
        datosConcretos = datos[12]
        for i in range(10):
            self.potenciaFcp[i] = datosConcretos[i]

        self.subgrupoChoice.SetStringSelection(datos[-1])
        return

    def OnNumeroHorasHelpButton(self, event):
        """
        Metodo: OnNumeroHorasHelpButton

        ARGUMENTOS:
                event:
        """
        zona = self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()
        perfilUso = self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
        servicio = 'Refrigeración'
        if zona == '':
            wx.MessageBox(_('Debe indicar la localización del edificio en el panel de datos generales'), _('Estimación del número de horas de funcionamiento'))
        else:
            self.parent.parent.parent.calculoCalificacion()
            ayuda = ayudaNumeroHoras.Dialog1(self, zona, perfilUso, servicio)
            ayuda.ShowModal()
            if ayuda.dev != []:
                self.numeroHorasDemanda.SetValue(str(ayuda.dev[0]))