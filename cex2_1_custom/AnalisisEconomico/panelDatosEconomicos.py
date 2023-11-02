# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: AnalisisEconomico\panelDatosEconomicos.pyc
# Compiled at: 2014-12-02 13:00:06
"""
Modulo: panelDatosEconomicos.py

"""
import wx
wxID_PANEL1, wxID_PANEL1BIOCARBUTEXT, wxID_PANEL1BIOMASATEXT, wxID_PANEL1CARBONTEXT, wxID_PANEL1ELECTRICIDADTEXT, wxID_PANEL1GASNATURALTEXT, wxID_PANEL1GASOLEOCTEXT, wxID_PANEL1GLPTEXT, wxID_PANEL1INCREMENTOPRECIOENERGIA, wxID_PANEL1INCREMENTOPRECIOENERGIATEXT, wxID_PANEL1PITOINTERES, wxID_PANEL1PRECIOBIOCARBU, wxID_PANEL1PRECIOBIOMASA, wxID_PANEL1PRECIOCARBON, wxID_PANEL1PRECIOELECTRICIDAD, wxID_PANEL1PRECIOGASNATURAL, wxID_PANEL1PRECIOGASOLEOC, wxID_PANEL1PRECOGLP, wxID_PANEL1TIPOINTERESTEXT, wxID_PANEL1TITULOPRECIOTEXT, wxID_PANEL1TITULOTEXT, wxID_PANEL1BIOMASADENSIFICADATEXT, wxID_PANEL1PRECIOBIOMASADENSIFICADA, wxID_PANEL1GASNATURALTEXTUNIDADES, wxID_PANEL1GASOLEOCTEXTUNIDADES, wxID_PANEL1ELECTRICIDADTEXTUNIDADES, wxID_PANEL1GLPTEXTUNIDADES, wxID_PANEL1CARBONTEXTUNIDADES, wxID_PANEL1BIOCARBUTEXTUNIDADES, wxID_PANEL1BIOMASATEXTUNIDADES, wxID_PANEL1BIOMASADENSIFICADATEXTUNIDADES, wxID_PANEL1INCREMENTOPRECIOENERGIATEXTUNIDADES, wxID_PANEL1TIPOINTERESTEXTUNIDADES = [ wx.NewId() for _init_ctrls in range(33) ]

class Panel1(wx.Panel):
    """
    Clase: Panel1 del modulo panelDatosEconomicos.py

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
        self.tituloText = wx.StaticText(id=wxID_PANEL1TITULOTEXT, label=_('Definición de los parámetros económicos'), name='tituloText', parent=self, pos=wx.Point(15, 24), size=wx.Size(344, 18), style=0)
        self.tituloText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.tituloText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.CaracteristicasLinea = wx.StaticBox(id=wxID_PANEL1TITULOPRECIOTEXT, label=_('Precio asociado a los diferentes combustibles'), name='CaracteristicasLinea', parent=self, pos=wx.Point(15, 70), size=wx.Size(695, 274), style=0)
        self.CaracteristicasLinea.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasLinea.SetForegroundColour(wx.Colour(0, 0, 100))
        self.CaracteristicasLinea2 = wx.StaticBox(id=wxID_PANEL1TITULOPRECIOTEXT, label=_('Datos económicos'), name='CaracteristicasLinea', parent=self, pos=wx.Point(15, 359), size=wx.Size(695, 100), style=0)
        self.CaracteristicasLinea2.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasLinea2.SetForegroundColour(wx.Colour(0, 0, 100))
        self.gasNaturalText = wx.StaticText(id=wxID_PANEL1GASNATURALTEXT, label=_('Gas Natural'), name='gasNaturalText', parent=self, pos=wx.Point(30, 100), size=wx.Size(56, 13), style=0)
        self.gasoleoCText = wx.StaticText(id=wxID_PANEL1GASOLEOCTEXT, label=_('Gasóleo-C'), name='gasoleoCText', parent=self, pos=wx.Point(30, 130), size=wx.Size(49, 13), style=0)
        self.electricidadText = wx.StaticText(id=wxID_PANEL1ELECTRICIDADTEXT, label=_('Electricidad'), name='electricidadText', parent=self, pos=wx.Point(30, 160), size=wx.Size(54, 13), style=0)
        self.GLPText = wx.StaticText(id=wxID_PANEL1GLPTEXT, label=_('GLP'), name='GLPText', parent=self, pos=wx.Point(30, 190), size=wx.Size(18, 13), style=0)
        self.carbonText = wx.StaticText(id=wxID_PANEL1CARBONTEXT, label=_('Carbón'), name='carbonText', parent=self, pos=wx.Point(30, 220), size=wx.Size(35, 13), style=0)
        self.biocarbuText = wx.StaticText(id=wxID_PANEL1BIOCARBUTEXT, label=_('Biocarburante'), name='biocarbuText', parent=self, pos=wx.Point(30, 250), size=wx.Size(67, 13), style=0)
        self.biomasaText = wx.StaticText(id=wxID_PANEL1BIOMASATEXT, label=_('Biomasa no densificada'), name='biomasaText', parent=self, pos=wx.Point(30, 280), size=wx.Size(170, 13), style=0)
        self.biomasaDensificadaText = wx.StaticText(id=wxID_PANEL1BIOMASADENSIFICADATEXT, label=_('Biomasa densificada (pelets)'), name='biomasaDensificadaText', parent=self, pos=wx.Point(30, 310), size=wx.Size(230, 13), style=0)
        self.precioGasNatural = wx.TextCtrl(id=wxID_PANEL1PRECIOGASNATURAL, name='precioGasNatural', parent=self, pos=wx.Point(265, 98), size=wx.Size(60, 21), style=0, value='')
        self.precioGasoleoC = wx.TextCtrl(id=wxID_PANEL1PRECIOGASOLEOC, name='precioGasoleoC', parent=self, pos=wx.Point(265, 128), size=wx.Size(60, 21), style=0, value='')
        self.precioElectricidad = wx.TextCtrl(id=wxID_PANEL1PRECIOELECTRICIDAD, name='precioElectricidad', parent=self, pos=wx.Point(265, 158), size=wx.Size(60, 21), style=0, value='')
        self.precoGLP = wx.TextCtrl(id=wxID_PANEL1PRECOGLP, name='precoGLP', parent=self, pos=wx.Point(265, 188), size=wx.Size(60, 21), style=0, value='')
        self.precioCarbon = wx.TextCtrl(id=wxID_PANEL1PRECIOCARBON, name='precioCarbon', parent=self, pos=wx.Point(265, 218), size=wx.Size(60, 21), style=0, value='')
        self.precioBiocarbu = wx.TextCtrl(id=wxID_PANEL1PRECIOBIOCARBU, name='precioBiocarbu', parent=self, pos=wx.Point(265, 248), size=wx.Size(60, 21), style=0, value='')
        self.precioBiomasa = wx.TextCtrl(id=wxID_PANEL1PRECIOBIOMASA, name='precioBiomasa', parent=self, pos=wx.Point(265, 278), size=wx.Size(60, 21), style=0, value='')
        self.precioBiomasaDensificada = wx.TextCtrl(id=wxID_PANEL1PRECIOBIOMASADENSIFICADA, name='precioBiomasaDensificada', parent=self, pos=wx.Point(265, 308), size=wx.Size(60, 21), style=0, value='')
        self.incrementoPrecioEnergiaText = wx.StaticText(id=wxID_PANEL1INCREMENTOPRECIOENERGIATEXT, label=_('Incremento anual del precio de la energía'), name='incrementoPrecioEnergiaText', parent=self, pos=wx.Point(30, 389), size=wx.Size(230, 13), style=0)
        self.incrementoPrecioEnergia = wx.TextCtrl(id=wxID_PANEL1INCREMENTOPRECIOENERGIA, name='incrementoPrecioEnergia', parent=self, pos=wx.Point(265, 387), size=wx.Size(60, 21), style=0, value='')
        self.tipoInteresText = wx.StaticText(id=wxID_PANEL1TIPOINTERESTEXT, label=_('Tipo de interés o coste de oportunidad'), name='tipoInteresText', parent=self, pos=wx.Point(30, 419), size=wx.Size(230, 13), style=0)
        self.tipoInteres = wx.TextCtrl(id=wxID_PANEL1PITOINTERES, name='pitoInteres', parent=self, pos=wx.Point(265, 417), size=wx.Size(60, 21), style=0, value='')
        self.gasNaturalTextUnidades = wx.StaticText(id=wxID_PANEL1GASNATURALTEXTUNIDADES, label=_('€/kWh'), name='gasNaturalText', parent=self, pos=wx.Point(330, 100), size=wx.Size(30, 13), style=0)
        self.gasoleoCTexUnidadest = wx.StaticText(id=wxID_PANEL1GASOLEOCTEXTUNIDADES, label=_('€/kWh'), name='gasoleoCText', parent=self, pos=wx.Point(330, 130), size=wx.Size(30, 13), style=0)
        self.electricidadTextUnidades = wx.StaticText(id=wxID_PANEL1ELECTRICIDADTEXTUNIDADES, label=_('€/kWh'), name='electricidadText', parent=self, pos=wx.Point(330, 160), size=wx.Size(30, 13), style=0)
        self.GLPTextUnidades = wx.StaticText(id=wxID_PANEL1GLPTEXTUNIDADES, label=_('€/kWh'), name='GLPText', parent=self, pos=wx.Point(330, 190), size=wx.Size(30, 13), style=0)
        self.carbonTextUnidades = wx.StaticText(id=wxID_PANEL1CARBONTEXTUNIDADES, label=_('€/kWh'), name='carbonText', parent=self, pos=wx.Point(330, 220), size=wx.Size(30, 13), style=0)
        self.biocarbuTextUnidades = wx.StaticText(id=wxID_PANEL1BIOCARBUTEXTUNIDADES, label=_('€/kWh'), name='biocarbuText', parent=self, pos=wx.Point(330, 250), size=wx.Size(30, 13), style=0)
        self.biomasaTextUnidades = wx.StaticText(id=wxID_PANEL1BIOMASATEXTUNIDADES, label=_('€/kWh'), name='biomasaText', parent=self, pos=wx.Point(330, 280), size=wx.Size(30, 13), style=0)
        self.biomasaDensificadaTextUnidades = wx.StaticText(id=wxID_PANEL1BIOMASADENSIFICADATEXTUNIDADES, label=_('€/kWh'), name='biomasaDensificadaText', parent=self, pos=wx.Point(330, 310), size=wx.Size(30, 13), style=0)
        self.incrementoPrecioEnergiaTextUnidades = wx.StaticText(id=wxID_PANEL1INCREMENTOPRECIOENERGIATEXTUNIDADES, label=_('%'), name='incrementoPrecioEnergiaText', parent=self, pos=wx.Point(330, 389), size=wx.Size(30, 13), style=0)
        self.tipoInteresTextUnidades = wx.StaticText(id=wxID_PANEL1TIPOINTERESTEXTUNIDADES, label=_('%'), name='tipoInteresText', parent=self, pos=wx.Point(330, 419), size=wx.Size(30, 13), style=0)

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

    def cogerDatos(self):
        """
        Metodo: cogerDatos

        """
        if ',' in self.precioGasNatural.GetValue():
            self.precioGasNatural.SetValue(self.precioGasNatural.GetValue().replace(',', '.'))
        if ',' in self.precioGasoleoC.GetValue():
            self.precioGasoleoC.SetValue(self.precioGasoleoC.GetValue().replace(',', '.'))
        if ',' in self.precioElectricidad.GetValue():
            self.precioElectricidad.SetValue(self.precioElectricidad.GetValue().replace(',', '.'))
        if ',' in self.precoGLP.GetValue():
            self.precoGLP.SetValue(self.precoGLP.GetValue().replace(',', '.'))
        if ',' in self.precioCarbon.GetValue():
            self.precioCarbon.SetValue(self.precioCarbon.GetValue().replace(',', '.'))
        if ',' in self.precioBiocarbu.GetValue():
            self.precioBiocarbu.SetValue(self.precioBiocarbu.GetValue().replace(',', '.'))
        if ',' in self.precioBiomasa.GetValue():
            self.precioBiomasa.SetValue(self.precioBiomasa.GetValue().replace(',', '.'))
        if ',' in self.precioBiomasaDensificada.GetValue():
            self.precioBiomasaDensificada.SetValue(self.precioBiomasaDensificada.GetValue().replace(',', '.'))
        if ',' in self.incrementoPrecioEnergia.GetValue():
            self.incrementoPrecioEnergia.SetValue(self.incrementoPrecioEnergia.GetValue().replace(',', '.'))
        if ',' in self.tipoInteres.GetValue():
            self.tipoInteres.SetValue(self.tipoInteres.GetValue().replace(',', '.'))
        datos = []
        datos.append(self.precioGasNatural.GetValue())
        datos.append(self.precioGasoleoC.GetValue())
        datos.append(self.precioElectricidad.GetValue())
        datos.append(self.precoGLP.GetValue())
        datos.append(self.precioCarbon.GetValue())
        datos.append(self.precioBiocarbu.GetValue())
        datos.append(self.precioBiomasa.GetValue())
        datos.append(self.precioBiomasaDensificada.GetValue())
        datos.append(self.incrementoPrecioEnergia.GetValue())
        datos.append(self.tipoInteres.GetValue())
        return datos

    def cargarDatos(self, datos):
        """
        Metodo: cargarDatos

        ARGUMENTOS:
                datos:
        """
        self.precioGasNatural.SetValue(datos[0])
        self.precioGasoleoC.SetValue(datos[1])
        self.precioElectricidad.SetValue(datos[2])
        self.precoGLP.SetValue(datos[3])
        self.precioCarbon.SetValue(datos[4])
        self.precioBiocarbu.SetValue(datos[5])
        self.precioBiomasa.SetValue(datos[6])
        self.precioBiomasaDensificada.SetValue(datos[7])
        self.incrementoPrecioEnergia.SetValue(datos[8])
        self.tipoInteres.SetValue(datos[9])