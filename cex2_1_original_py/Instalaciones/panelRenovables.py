# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\panelRenovables.pyc
# Compiled at: 2015-02-19 13:18:33
"""
Modulo: panelRenovables.py

"""
from Instalaciones.comprobarCampos import Comprueba, Comprueba2
from miChoice import MiChoice
import Calculos.listadosWeb as listadosWeb, wx, logging
wxID_PANEL1, wxID_PANEL1CAPTADORESCHECK, wxID_PANEL1ENERGIA, wxID_PANEL1ENERGIATEXT, wxID_PANEL1ENERGIAUNIDADESTEXT, wxID_PANEL1FCHARTBUTTON, wxID_PANEL1FUENTERADIO, wxID_PANEL1GENERACIONRADIO, wxID_PANEL1PORCENTAJEACS, wxID_PANEL1PORCENTAJEACSTEXT, wxID_PANEL1PORCENTAJECALEFACCION, wxID_PANEL1PORCENTAJECALEFACCIONTEXT, wxID_PANEL1STATICTEXT1, wxID_PANEL1STATICTEXT2, wxID_PANEL1ACUMULACIONTEXT, wxID_PANEL1CHOICE2, wxID_PANEL1ESPESORAISTEXT, wxID_PANEL1ESPESORAISLA, wxID_PANEL1ESTADOAISTEXT, wxID_PANEL1AISLANTEBUENORADIO, wxID_PANEL1AISLANTEREGULARRADIO, wxID_PANEL1AISLANTEMALORADIO, wxID_PANEL1TIPOAISTEXT, wxID_PANEL1AISLANTEPORIURETANO, wxID_PANEL1AISLANTERESINA, wxID_PANEL1AISLANTEPOLIURETANOPROYEC, wxID_PANEL1AISLANTEMESPUMA, wxID_PANEL1UATEXT, wxID_PANEL1UAVALOR, wxID_PANEL1ANOCALDERACHOICE, wxID_PANEL1ANOCALDERATEXT, wxID_PANEL1TIPOCALDERATEXT, wxID_PANEL1TIPOCALDERACHOICE, wxID_PANEL1RENDIMIENTOMEDIOTEXT, wxID_PANEL1RENDIMIENTOMEDIO, wxID_PANEL1VALORUATEXT, wxID_PANEL1VOLUMEN, wxID_PANEL1VOLUMENTEXT, wxID_PANEL1VOLUMENUNIDADESTEXT, wxID_PANEL1CHOICE1, wxID_PANEL1RADIOBUTTON1, wxID_PANEL1TEMPERATURAALTATEXT, wxID_PANEL1TEMPERATURAALTA, wxID_PANEL1TEMPALTAUNIDADESTEXT, wxID_PANEL1TEMPERATURABAJATEXT, wxID_PANEL1TEMPERATURABAJA, wxID_PANEL1CONACSRADIO, wxID_PANEL1INDEPENRADIO, wxID_PANEL1STATICTEXT11, wxID_PANEL1NOMBREINSTALACIONTEXT, wxID_PANEL1NOMBREINSTALACION, wxID_PANEL1SUBGRUPOTEXT, wxID_PANEL1SUBGRUPOCHOICE, wxID_PANEL1PORCENTAJEREFRIGERACIONTEXT, wxID_PANEL1PORCENTAJEREFRIGERACION, wxID_PANEL1PORCENTAJEUNIDADESREF, wxID_PANEL1TIPOCOMBUSTIBLETEXT, wxID_PANEL1COMBUSTIBLECHOICE, wxID_PANEL1FUENTESLINEATEXT, wxID_PANEL1GENERACIONLINEATEXT, wxID_PANEL1CALORGENERADOCALTEXT, wxID_PANEL1CALORGENERADOCAL, wxID_PANEL1CALORGENERADOUNIDADESCALTEXT, wxID_PANEL1CALORGENERADOACSTEXT, wxID_PANEL1CALORGENERADOACS, wxID_PANEL1CALORGENERADOUNIDADESACSTEXT, wxID_PANEL1CALORGENERADOREFTEXT, wxID_PANEL1CALORGENERADOREF, wxID_PANEL1CALORGENERADOUNIDADESREFTEXT = [ wx.NewId() for _init_ctrls in range(69) ]

class Panel1(wx.Panel):
    """
    Clase: Panel1 del modulo panelRenovables.py

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
        self.nombreInstalacion = wx.TextCtrl(id=wxID_PANEL1NOMBREINSTALACION, name='nombreInstalacion', parent=self, pos=wx.Point(170, 0), size=wx.Size(230, 21), style=0, value=_('Contribuciones energéticas'))
        self.nombreInstalacion.SetForegroundColour(wx.Colour(100, 200, 0))
        self.nombreInstalacion.Bind(wx.EVT_TEXT, self.OnNombreInstalacion, id=wxID_PANEL1NOMBREINSTALACION)
        self.subgrupoText = wx.StaticText(id=wxID_PANEL1SUBGRUPOTEXT, label=_('Zona'), name='subgrupoText', parent=self, pos=wx.Point(435, 2), size=wx.Size(50, 13), style=0)
        self.subgrupoChoice = MiChoice(choices=[], id=wxID_PANEL1SUBGRUPOCHOICE, name='subgrupoChoice', parent=self, pos=wx.Point(496, 0), size=wx.Size(214, 21), style=0)
        self.fuentesLineaText = wx.StaticBox(id=wxID_PANEL1FUENTESLINEATEXT, label=_('                                                                '), name='fuentesLineaText', parent=self, pos=wx.Point(0, 40), size=wx.Size(710, 118), style=0)
        self.fuentesLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.generacionLineaText = wx.StaticBox(id=wxID_PANEL1GENERACIONLINEATEXT, label=_('                                                                                                                       '), name='generacionLineaText', parent=self, pos=wx.Point(0, 195), size=wx.Size(710, 149), style=0)
        self.generacionLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.fuenteRadio = wx.CheckBox(id=wxID_PANEL1FUENTERADIO, label=_('Fuentes de energía renovable'), name='fuenteRadio', parent=self, pos=wx.Point(10, 40), size=wx.Size(200, 15), style=0)
        self.fuenteRadio.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Georgia'))
        self.fuenteRadio.SetForegroundColour(wx.Colour(0, 64, 128))
        self.fuenteRadio.SetValue(False)
        self.fuenteRadio.Bind(wx.EVT_CHECKBOX, self.OnFuentesRenovablesCheck, id=wxID_PANEL1FUENTERADIO)
        self.generacionRadio = wx.CheckBox(id=wxID_PANEL1GENERACIONRADIO, label=_('Generación electricidad mediante renovables / Cogeneración'), name='generacionRadio', parent=self, pos=wx.Point(10, 195), size=wx.Size(370, 15), style=0)
        self.generacionRadio.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Georgia'))
        self.generacionRadio.SetForegroundColour(wx.Colour(0, 64, 128))
        self.generacionRadio.Bind(wx.EVT_CHECKBOX, self.OnGeneracionElectricaCheck, id=wxID_PANEL1GENERACIONRADIO)
        self.porcentajeACSText = wx.StaticText(id=wxID_PANEL1PORCENTAJEACSTEXT, label=_('Porcentaje de demanda de ACS cubierto'), name='porcentajeACSText', parent=self, pos=wx.Point(15, 69), size=wx.Size(194, 13), style=0)
        self.porcentajeACSText.Enable(False)
        self.porcentajeACS = wx.TextCtrl(id=wxID_PANEL1PORCENTAJEACS, name='porcentajeACS', parent=self, pos=wx.Point(280, 67), size=wx.Size(60, 21), style=0, value='')
        self.porcentajeACS.Enable(False)
        self.porcentajeUnidadesACS = wx.StaticText(id=wxID_PANEL1STATICTEXT2, label=_('%'), name='staticText2', parent=self, pos=wx.Point(350, 69), size=wx.Size(11, 13), style=0)
        self.porcentajeUnidadesACS.Enable(False)
        self.porcentajeCalefaccionText = wx.StaticText(id=wxID_PANEL1PORCENTAJECALEFACCIONTEXT, label=_('Porcentaje de demanda de calefacción cubierto'), name='porcentajeCalefaccionText', parent=self, pos=wx.Point(15, 98), size=wx.Size(229, 13), style=0)
        self.porcentajeCalefaccionText.Enable(False)
        self.porcentajeCalefaccion = wx.TextCtrl(id=wxID_PANEL1PORCENTAJECALEFACCION, name='porcentajeCalefaccion', parent=self, pos=wx.Point(280, 96), size=wx.Size(60, 21), style=0, value='')
        self.porcentajeCalefaccion.Enable(False)
        self.porcentajeUnidadesCal = wx.StaticText(id=wxID_PANEL1STATICTEXT11, label=_('%'), name='staticText1', parent=self, pos=wx.Point(350, 98), size=wx.Size(11, 13), style=0)
        self.porcentajeUnidadesCal.Enable(False)
        self.porcentajeRefrigeracionText = wx.StaticText(id=wxID_PANEL1PORCENTAJEREFRIGERACIONTEXT, label=_('Porcentaje de demanda de refrigeración cubierto'), name='porcentajeCalefaccionText', parent=self, pos=wx.Point(15, 127), size=wx.Size(240, 13), style=0)
        self.porcentajeRefrigeracionText.Enable(False)
        self.porcentajeRefrigeracion = wx.TextCtrl(id=wxID_PANEL1PORCENTAJEREFRIGERACION, name='porcentajeCalefaccion', parent=self, pos=wx.Point(280, 125), size=wx.Size(60, 21), style=0, value='')
        self.porcentajeRefrigeracion.Enable(False)
        self.porcentajeUnidadesRef = wx.StaticText(id=wxID_PANEL1PORCENTAJEUNIDADESREF, label=_('%'), name='staticText1', parent=self, pos=wx.Point(350, 127), size=wx.Size(11, 13), style=0)
        self.porcentajeUnidadesRef.Enable(False)
        self.captadoresCheck = wx.CheckBox(id=wxID_PANEL1CAPTADORESCHECK, label=_('Definir Captadores Solares'), name='captadoresCheck', parent=self, pos=wx.Point(420, 100), size=wx.Size(152, 13), style=0)
        self.captadoresCheck.SetValue(False)
        self.captadoresCheck.Show(False)
        self.captadoresCheck.Bind(wx.EVT_CHECKBOX, self.OncaptadoresCheck, id=wxID_PANEL1CAPTADORESCHECK)
        self.fChartButton = wx.Button(id=wxID_PANEL1FCHARTBUTTON, label=_('Cálculo f-chart'), name='fChartButton', parent=self, pos=wx.Point(580, 98), size=wx.Size(100, 21), style=0)
        self.fChartButton.Enable(False)
        self.fChartButton.Show(False)
        self.energiaText = wx.StaticText(id=wxID_PANEL1ENERGIATEXT, label=_('Energía eléctrica generada para autoconsumo'), name='energiaText', parent=self, pos=wx.Point(15, 226), size=wx.Size(260, 13), style=0)
        self.energiaText.Enable(False)
        self.energia = wx.TextCtrl(id=wxID_PANEL1ENERGIA, name='energia', parent=self, pos=wx.Point(280, 224), size=wx.Size(60, 21), style=0, value='')
        self.energia.Enable(False)
        self.energiaUnidadesText = wx.StaticText(id=wxID_PANEL1ENERGIAUNIDADESTEXT, label=_('kWh/año'), name='energiaUnidadesText', parent=self, pos=wx.Point(350, 226), size=wx.Size(43, 13), style=0)
        self.energiaUnidadesText.Enable(False)
        self.calorGeneradoACSText = wx.StaticText(id=wxID_PANEL1CALORGENERADOACSTEXT, label=_('Calor recuperado para ACS'), name='calorGeneradoACSText', parent=self, pos=wx.Point(15, 255), size=wx.Size(185, 13), style=0)
        self.calorGeneradoACSText.Enable(False)
        self.calorGeneradoACS = wx.TextCtrl(id=wxID_PANEL1CALORGENERADOACS, name='calorGeneradoACS', parent=self, pos=wx.Point(280, 253), size=wx.Size(60, 21), style=0, value='')
        self.calorGeneradoACS.Enable(False)
        self.calorGeneradoACSUnidadesText = wx.StaticText(id=wxID_PANEL1CALORGENERADOUNIDADESACSTEXT, label=_('kWh/año'), name='calorGeneradoACSText', parent=self, pos=wx.Point(350, 255), size=wx.Size(43, 13), style=0)
        self.calorGeneradoACSUnidadesText.Enable(False)
        self.calorGeneradoCalText = wx.StaticText(id=wxID_PANEL1CALORGENERADOCALTEXT, label=_('Calor recuperado para calefacción'), name='calorGeneradoCalText', parent=self, pos=wx.Point(15, 284), size=wx.Size(185, 13), style=0)
        self.calorGeneradoCalText.Enable(False)
        self.calorGeneradoCal = wx.TextCtrl(id=wxID_PANEL1CALORGENERADOCAL, name='calorGeneradoCal', parent=self, pos=wx.Point(280, 282), size=wx.Size(60, 21), style=0, value='')
        self.calorGeneradoCal.Enable(False)
        self.calorGeneradoUnidadesCalText = wx.StaticText(id=wxID_PANEL1CALORGENERADOUNIDADESCALTEXT, label=_('kWh/año'), name='calorGeneradoUnidadesCalText', parent=self, pos=wx.Point(350, 284), size=wx.Size(43, 13), style=0)
        self.calorGeneradoUnidadesCalText.Enable(False)
        self.calorGeneradoRefText = wx.StaticText(id=wxID_PANEL1CALORGENERADOREFTEXT, label=_('Frío recuperado'), name='calorGeneradoRefText', parent=self, pos=wx.Point(15, 313), size=wx.Size(185, 13), style=0)
        self.calorGeneradoRefText.Enable(False)
        self.calorGeneradoRef = wx.TextCtrl(id=wxID_PANEL1CALORGENERADOREF, name='calorGeneradoRef', parent=self, pos=wx.Point(280, 311), size=wx.Size(60, 21), style=0, value='')
        self.calorGeneradoRef.Enable(False)
        self.calorGeneradoUnidadesRefText = wx.StaticText(id=wxID_PANEL1CALORGENERADOUNIDADESREFTEXT, label=_('kWh/año'), name='calorGeneradoUnidadesRefText', parent=self, pos=wx.Point(350, 313), size=wx.Size(43, 13), style=0)
        self.calorGeneradoUnidadesRefText.Enable(False)
        self.energiaConsumidaText = wx.StaticText(id=wxID_PANEL1ENERGIATEXT, label=_('Energía consumida'), name='energiaText', parent=self, pos=wx.Point(450, 226), size=wx.Size(93, 13), style=0)
        self.energiaConsumidaText.Enable(False)
        self.energiaConsumida = wx.TextCtrl(id=wxID_PANEL1ENERGIA, name='energia', parent=self, pos=wx.Point(560, 224), size=wx.Size(60, 21), style=0, value='')
        self.energiaConsumida.Enable(False)
        self.energiaConsumidaUnidadesText = wx.StaticText(id=wxID_PANEL1ENERGIAUNIDADESTEXT, label=_('kWh/año'), name='energiaUnidadesText', parent=self, pos=wx.Point(630, 226), size=wx.Size(43, 13), style=0)
        self.energiaConsumidaUnidadesText.Enable(False)
        self.tipoCombustibleText = wx.StaticText(id=wxID_PANEL1TIPOCOMBUSTIBLETEXT, label=_('Tipo de combustible'), name='tipoCombustibleText', parent=self, pos=wx.Point(450, 255), size=wx.Size(96, 13), style=0)
        self.tipoCombustibleText.Enable(False)
        self.combustibleChoice = MiChoice(choices=listadosWeb.listadoCombustibles, id=wxID_PANEL1COMBUSTIBLECHOICE, name='combustibleChoice', parent=self, pos=wx.Point(560, 253), size=wx.Size(120, 21), style=0)
        self.combustibleChoice.Enable(False)

    def OnNombreInstalacion(self, event):
        """
        Metodo: OnNombreInstalacion

        ARGUMENTOS:
                event:
        """
        if self.nombreInstalacion.GetValue() == _('Contribuciones energéticas'):
            self.nombreInstalacion.SetForegroundColour(wx.Colour(100, 200, 0))
        else:
            self.nombreInstalacion.SetForegroundColour(wx.Colour(0, 0, 0))

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

    def elegirRaiz(self):
        """
        Metodo: elegirRaiz

        """
        try:
            sel = self.parent.arbolInstalaciones.GetSelection()
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
        self.tipoSistema = 'renovables'
        self._init_ctrls(parent, id, pos, size, style, name)
        self.listaErrores = ''
        self.subgrupoChoice.SetItems(self.cargarRaices())
        self.elegirRaiz()
        return

    def OncaptadoresCheck(self, event):
        """
        Metodo: OncaptadoresCheck

        ARGUMENTOS:
                event:
        """
        if self.captadoresCheck.GetValue() == True:
            self.fChartButton.Enable(True)
        else:
            self.fChartButton.Enable(False)

    def OnFuentesRenovablesCheck(self, event):
        """
        Metodo: OnFuentesRenovablesCheck

        ARGUMENTOS:
                event:
        """
        if self.fuenteRadio.GetValue() == True:
            self.porcentajeACSText.Enable(True)
            self.porcentajeACS.Enable(True)
            self.porcentajeUnidadesCal.Enable(True)
            self.porcentajeCalefaccionText.Enable(True)
            self.porcentajeCalefaccion.Enable(True)
            self.porcentajeUnidadesACS.Enable(True)
            self.porcentajeRefrigeracionText.Enable(True)
            self.porcentajeRefrigeracion.Enable(True)
            self.porcentajeUnidadesRef.Enable(True)
        else:
            self.porcentajeACSText.Enable(False)
            self.porcentajeACS.Enable(False)
            self.porcentajeUnidadesCal.Enable(False)
            self.porcentajeCalefaccionText.Enable(False)
            self.porcentajeCalefaccion.Enable(False)
            self.porcentajeUnidadesACS.Enable(False)
            self.porcentajeRefrigeracionText.Enable(False)
            self.porcentajeRefrigeracion.Enable(False)
            self.porcentajeUnidadesRef.Enable(False)

    def OnGeneracionElectricaCheck(self, event):
        """
        Metodo: OnGeneracionElectricaCheck

        ARGUMENTOS:
                event:
        """
        if self.generacionRadio.GetValue() == True:
            self.energiaText.Enable(True)
            self.energia.Enable(True)
            self.energiaUnidadesText.Enable(True)
            self.energiaConsumidaText.Enable(True)
            self.energiaConsumida.Enable(True)
            self.energiaConsumidaUnidadesText.Enable(True)
            self.combustibleChoice.Enable(True)
            self.tipoCombustibleText.Enable(True)
            self.calorGeneradoCalText.Enable(True)
            self.calorGeneradoCal.Enable(True)
            self.calorGeneradoUnidadesCalText.Enable(True)
            self.calorGeneradoACSText.Enable(True)
            self.calorGeneradoACS.Enable(True)
            self.calorGeneradoACSUnidadesText.Enable(True)
            self.calorGeneradoRefText.Enable(True)
            self.calorGeneradoRef.Enable(True)
            self.calorGeneradoUnidadesRefText.Enable(True)
        else:
            self.energiaText.Enable(False)
            self.energia.Enable(False)
            self.energiaUnidadesText.Enable(False)
            self.energiaConsumidaText.Enable(False)
            self.energiaConsumida.Enable(False)
            self.energiaConsumidaUnidadesText.Enable(False)
            self.combustibleChoice.Enable(False)
            self.tipoCombustibleText.Enable(False)
            self.calorGeneradoCalText.Enable(False)
            self.calorGeneradoCal.Enable(False)
            self.calorGeneradoUnidadesCalText.Enable(False)
            self.calorGeneradoACSText.Enable(False)
            self.calorGeneradoACS.Enable(False)
            self.calorGeneradoACSUnidadesText.Enable(False)
            self.calorGeneradoRefText.Enable(False)
            self.calorGeneradoRef.Enable(False)
            self.calorGeneradoUnidadesRefText.Enable(False)

    def cogerDatos(self):
        """
        Metodo: cogerDatos

        """
        self.listaErrores = ''
        self.listaErrores += Comprueba(self.nombreInstalacion.GetValue(), 1, self.listaErrores, 'nombre').ErrorDevuelto
        self.listaErrores += Comprueba(self.subgrupoChoice.GetStringSelection(), 0, self.listaErrores, 'zona').ErrorDevuelto
        if self.fuenteRadio.GetValue() == False and self.generacionRadio.GetValue() == False:
            self.listaErrores = 'No se ha indicado ningún valor'
            return self.listaErrores
        porcentajeACS = self.porcentajeACS.GetValue()
        porcentajeCal = self.porcentajeCalefaccion.GetValue()
        porcentajeRef = self.porcentajeRefrigeracion.GetValue()
        energiaElectrica = self.energia.GetValue()
        energiaElectrica2 = self.energiaConsumida.GetValue()
        calorGeneradoCal = self.calorGeneradoCal.GetValue()
        calorGeneradoACS = self.calorGeneradoACS.GetValue()
        calorGeneradoRef = self.calorGeneradoRef.GetValue()
        if ',' in porcentajeACS:
            porcentajeACS = porcentajeACS.replace(',', '.')
            self.porcentajeACS.SetValue(porcentajeACS)
        if ',' in porcentajeCal:
            porcentajeCal = porcentajeCal.replace(',', '.')
            self.porcentajeCalefaccion.SetValue(porcentajeCal)
        if ',' in porcentajeRef:
            porcentajeRef = porcentajeRef.replace(',', '.')
            self.porcentajeRefrigeracion.SetValue(porcentajeRef)
        if ',' in energiaElectrica:
            energiaElectrica = energiaElectrica.replace(',', '.')
            self.energia.SetValue(energiaElectrica)
        if ',' in energiaElectrica2:
            energiaElectrica2 = energiaElectrica2.replace(',', '.')
            self.energiaConsumida.SetValue(energiaElectrica2)
        if ',' in calorGeneradoCal:
            calorGeneradoCal = calorGeneradoCal.replace(',', '.')
            self.calorGeneradoCal.SetValue(calorGeneradoCal)
        if ',' in calorGeneradoACS:
            calorGeneradoACS = calorGeneradoACS.replace(',', '.')
            self.calorGeneradoACS.SetValue(calorGeneradoACS)
        if ',' in calorGeneradoRef:
            calorGeneradoRef = calorGeneradoRef.replace(',', '.')
            self.calorGeneradoRef.SetValue(calorGeneradoRef)
        if self.fuenteRadio.GetValue() == True:
            if porcentajeACS == '' and porcentajeCal == '' and porcentajeRef == '':
                self.listaErrores += _('\nNo se ha indicado ningún valor de fuentes de energía renovables')
            else:
                if porcentajeACS != '':
                    self.listaErrores += Comprueba2(porcentajeACS, 2, self.listaErrores, _('contribución renovable para ACS'), 0.0, 100.0).ErrorDevuelto
                if porcentajeCal != '':
                    self.listaErrores += Comprueba2(porcentajeCal, 2, self.listaErrores, _('contribución renovable para calefacción'), 0.0, 100.0).ErrorDevuelto
                if porcentajeRef != '':
                    self.listaErrores += Comprueba2(porcentajeRef, 2, self.listaErrores, _('contribución renovable para refrigeración'), 0.0, 100.0).ErrorDevuelto
        if self.generacionRadio.GetValue() == True:
            if energiaElectrica == '' and energiaElectrica2 == '' and calorGeneradoCal == '' and calorGeneradoACS == '' and calorGeneradoRef == '':
                self.listaErrores += _('\nNo se ha indicado ningún valor generación de electricidad mediante renovables/cogeneración')
            else:
                if energiaElectrica != '':
                    self.listaErrores += Comprueba2(energiaElectrica, 2, self.listaErrores, _('energía eléctrica generada'), 0).ErrorDevuelto
                if energiaElectrica2 != '':
                    self.listaErrores += Comprueba2(energiaElectrica2, 2, self.listaErrores, _('energía consumida'), 0).ErrorDevuelto
                    self.listaErrores += Comprueba(self.combustibleChoice.GetStringSelection(), 0, self.listaErrores, _('tipo de combustible')).ErrorDevuelto
                if calorGeneradoACS != '':
                    self.listaErrores += Comprueba2(calorGeneradoACS, 2, self.listaErrores, _('calor recuperado para ACS'), 0).ErrorDevuelto
                if calorGeneradoCal != '':
                    self.listaErrores += Comprueba2(calorGeneradoCal, 2, self.listaErrores, _('calor recuperado para calefacción'), 0).ErrorDevuelto
                if calorGeneradoRef != '':
                    self.listaErrores += Comprueba2(calorGeneradoRef, 2, self.listaErrores, _('frío recuperado'), 0).ErrorDevuelto
        if self.listaErrores != '':
            return self.listaErrores
        datos = []
        datos.append(self.nombreInstalacion.GetValue())
        datos.append('renovable')
        if self.fuenteRadio.GetValue() == True:
            datosRenovable = [
             self.porcentajeACS.GetValue(), self.porcentajeCalefaccion.GetValue(),
             self.porcentajeRefrigeracion.GetValue(), self.captadoresCheck.GetValue()]
        else:
            datosRenovable = [
             '', '', '', False]
        datos.append(datosRenovable)
        if self.generacionRadio.GetValue() == True:
            datosElectricidad = [
             self.energia.GetValue(), self.calorGeneradoACS.GetValue(),
             self.calorGeneradoCal.GetValue(), self.calorGeneradoRef.GetValue(),
             self.energiaConsumida.GetValue(), self.combustibleChoice.GetStringSelection()]
        else:
            datosElectricidad = [
             '', '', '', '', '', '']
        datos.append(datosElectricidad)
        datos.append([self.fuenteRadio.GetValue(), self.generacionRadio.GetValue()])
        datos.append(self.subgrupoChoice.GetStringSelection())
        return datos

    def cargarDatos(self, datos):
        """
        Metodo: cargarDatos

        ARGUMENTOS:
                datos:
        """
        self.nombreInstalacion.SetValue(datos[0])
        datosRenovable = datos[2]
        self.porcentajeACS.SetValue(datosRenovable[0])
        self.porcentajeCalefaccion.SetValue(datosRenovable[1])
        self.porcentajeRefrigeracion.SetValue(datosRenovable[2])
        self.captadoresCheck.SetValue(datosRenovable[3])
        datosElectricidad = datos[3]
        self.energia.SetValue(datosElectricidad[0])
        self.calorGeneradoACS.SetValue(datosElectricidad[1])
        self.calorGeneradoCal.SetValue(datosElectricidad[2])
        self.calorGeneradoRef.SetValue(datosElectricidad[3])
        self.energiaConsumida.SetValue(datosElectricidad[4])
        self.combustibleChoice.SetStringSelection(datosElectricidad[5])
        self.fuenteRadio.SetValue(datos[4][0])
        self.generacionRadio.SetValue(datos[4][1])
        self.subgrupoChoice.SetStringSelection(datos[5])
        self.OnFuentesRenovablesCheck(None)
        self.OnGeneracionElectricaCheck(None)
        self.OncaptadoresCheck(None)
        return