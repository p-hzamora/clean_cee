# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\panelDefinirInstalaciones.pyc
# Compiled at: 2014-12-09 15:09:25
"""
Modulo: panelDefinirInstalaciones.py

"""
import wx, Instalaciones.panelACS as panelACS, Instalaciones.panelRenovables as panelRenovables, Instalaciones.panelCalefaccion as panelCalefaccion, Instalaciones.panelRefrigeracion as panelRefrigeracion, Instalaciones.panelClimatizacion as panelClimatizacion, Instalaciones.panelMixto2 as panelMixto2, Instalaciones.panelMixto3 as panelMixto3, Instalaciones.panelIluminacion as panelIluminacion, Instalaciones.panelVentilacion as panelVentilacion, Instalaciones.panelVentiladores as panelVentiladores, Instalaciones.panelBombas as panelBombas, Instalaciones.panelTorresRefrigeracion as panelTorresRefrigeracion, tips
wxID_PANEL1, wxID_PANEL1DEFIIRTEXT, wxID_PANEL1DEFINIRACS, wxID_PANEL1DEFINIRCALEFACCION, wxID_PANEL1DEFINIRCLIMATIZACION, wxID_PANEL1DEFINIRREFRIGERACION, wxID_PANEL1DEFINIRSISTEMASMIXTOS, wxID_PANEL1DEFINIR, wxID_PANEL1UNIZONAGUA, wxID_PANEL1MULTIZONAGUA, wxID_PANEL1MULTIZONAIRE, wxID_PANEL1UNIZONAIRE, wxID_PANEL1MULTIZONAIRECONDUC, wxID_PANEL1MULTIZONAIREEXPANSION, wxID_PANEL1DEFINIRSISTEMASMIXTOSCLIMA, wxID_PANEL1CONTRIBUCIONES, wxID_PANEL1VENTILACION, wxID_WXPANEL1STATICLINE, wxID_PANEL1ILUMINACIONES, wxID_PANEL1VENTILADORES, wxID_PANEL1BOMBEO, wxID_PANEL1TORRESREFRIGERACION = [ wx.NewId() for _init_ctrls in range(22) ]

class Panel1(wx.Panel):
    """
    Clase: Panel1 del modulo panelDefinirInstalaciones.py

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
        self.defiirText = wx.StaticText(id=wxID_PANEL1DEFINIR, label=_('Instalaciones del edificio'), name='defiirText', parent=self, pos=wx.Point(0, 0), size=wx.Size(222, 18), style=0)
        self.defiirText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.defiirText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.definirACS = wx.RadioButton(id=wxID_PANEL1DEFINIRACS, label=_('Equipo de ACS'), name='definirACS', parent=self, pos=wx.Point(20, 30), size=wx.Size(100, 13), style=wx.RB_GROUP)
        self.definirACS.SetValue(True)
        self.definirACS.Bind(wx.EVT_RADIOBUTTON, self.OntipoInstalacion, id=wxID_PANEL1DEFINIRACS)
        self.definirCalefaccion = wx.RadioButton(id=wxID_PANEL1DEFINIRCALEFACCION, label=_('Equipo de sólo calefacción'), name='definirCalefaccion', parent=self, pos=wx.Point(20, 60), size=wx.Size(200, 13), style=0)
        self.definirCalefaccion.Bind(wx.EVT_RADIOBUTTON, self.OntipoInstalacion, id=wxID_PANEL1DEFINIRCALEFACCION)
        self.definirRefrigeracion = wx.RadioButton(id=wxID_PANEL1DEFINIRREFRIGERACION, label=_('Equipo de sólo refrigeración'), name='definirRefrigeracion', parent=self, pos=wx.Point(20, 90), size=wx.Size(200, 13), style=0)
        self.definirRefrigeracion.Bind(wx.EVT_RADIOBUTTON, self.OntipoInstalacion, id=wxID_PANEL1DEFINIRREFRIGERACION)
        self.definirCaleYRefri = wx.RadioButton(id=wxID_PANEL1DEFINIRCLIMATIZACION, label=_('Equipo de calefacción y refrigeración'), name='definirCaleYRefri', parent=self, pos=wx.Point(20, 120), size=wx.Size(250, 13), style=0)
        self.definirCaleYRefri.Bind(wx.EVT_RADIOBUTTON, self.OntipoInstalacion, id=wxID_PANEL1DEFINIRCLIMATIZACION)
        self.definirSistemasMixtosCaleyACS = wx.RadioButton(id=wxID_PANEL1DEFINIRSISTEMASMIXTOS, label=_('Equipo mixto de calefacción y ACS'), name='definirSistemasMixtosCaleyACS', parent=self, pos=wx.Point(20, 150), size=wx.Size(200, 13), style=0)
        self.definirSistemasMixtosCaleyACS.Bind(wx.EVT_RADIOBUTTON, self.OntipoInstalacion, id=wxID_PANEL1DEFINIRSISTEMASMIXTOS)
        self.definirSistemasMixtosClimayACS = wx.RadioButton(id=wxID_PANEL1DEFINIRSISTEMASMIXTOSCLIMA, label=_('Equipo mixto de calefacción, refrigeración y ACS'), name='definirSistemasMixtosClimayACS', parent=self, pos=wx.Point(20, 180), size=wx.Size(270, 13), style=0)
        self.definirSistemasMixtosClimayACS.Bind(wx.EVT_RADIOBUTTON, self.OntipoInstalacion, id=wxID_PANEL1DEFINIRSISTEMASMIXTOSCLIMA)
        self.contribucionesEnergeticas = wx.RadioButton(id=wxID_PANEL1CONTRIBUCIONES, label=_('Contribuciones energéticas'), name='contribucionesEnergeticas', parent=self, pos=wx.Point(350, 30), size=wx.Size(250, 13), style=0)
        self.contribucionesEnergeticas.Bind(wx.EVT_RADIOBUTTON, self.OntipoInstalacion, id=wxID_PANEL1CONTRIBUCIONES)
        self.iluminacion = wx.RadioButton(id=wxID_PANEL1ILUMINACIONES, label=_('Equipos de iluminación'), name='iluminacion', parent=self, pos=wx.Point(350, 60), size=wx.Size(250, 13), style=0)
        self.iluminacion.Bind(wx.EVT_RADIOBUTTON, self.OntipoInstalacion, id=wxID_PANEL1ILUMINACIONES)
        self.iluminacion.Show(False)
        self.ventilacion = wx.RadioButton(id=wxID_PANEL1VENTILACION, label=_('Equipos de aire primario'), name='ventilacion', parent=self, pos=wx.Point(350, 90), size=wx.Size(250, 13), style=0)
        self.ventilacion.Bind(wx.EVT_RADIOBUTTON, self.OntipoInstalacion, id=wxID_PANEL1VENTILACION)
        self.ventilacion.Show(False)
        self.ventiladores = wx.RadioButton(id=wxID_PANEL1VENTILADORES, label=_('Ventiladores'), name='ventiladores', parent=self, pos=wx.Point(350, 120), size=wx.Size(250, 13), style=0)
        self.ventiladores.Bind(wx.EVT_RADIOBUTTON, self.OntipoInstalacion, id=wxID_PANEL1VENTILADORES)
        self.ventiladores.Show(False)
        self.bombas = wx.RadioButton(id=wxID_PANEL1BOMBEO, label=_('Equipos de bombeo'), name='bombeo', parent=self, pos=wx.Point(350, 150), size=wx.Size(250, 13), style=0)
        self.bombas.Bind(wx.EVT_RADIOBUTTON, self.OntipoInstalacion, id=wxID_PANEL1BOMBEO)
        self.bombas.Show(False)
        self.torresRefrigeracion = wx.RadioButton(id=wxID_PANEL1TORRESREFRIGERACION, label=_('Torres de refrigeración'), name='torresRefrigeracion', parent=self, pos=wx.Point(350, 180), size=wx.Size(250, 13), style=0)
        self.torresRefrigeracion.Bind(wx.EVT_RADIOBUTTON, self.OntipoInstalacion, id=wxID_PANEL1TORRESREFRIGERACION)
        self.torresRefrigeracion.Show(False)
        self.staticLine = wx.StaticLine(id=wxID_WXPANEL1STATICLINE, name='staticLine', parent=self, pos=wx.Point(0, 202), size=wx.Size(710, 3), style=0)
        self.staticLine.SetBackgroundColour(wx.Colour(0, 64, 128))

    def __init__(self, parent, id, pos, size, style, name):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
                id:
                pos:
                size:
                style:
                name:
        """
        self._init_ctrls(parent, id, pos, size, style, name)
        self.parent = parent
        self.seleccionadaAntes = 'ACS'

    def OntipoInstalacion(self, event):
        """
        Metodo: OntipoInstalacion

        ARGUMENTOS:
                event:
        """
        if self.definirACS.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Equipo de ACS'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelACS.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.Acs(self.parent.parent.parent)
            self.seleccionadaAntes = 'ACS'
        elif self.definirCalefaccion.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Equipo de sólo calefacción'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelCalefaccion.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.Calefaccion(self.parent.parent.parent)
            self.seleccionadaAntes = 'calefaccion'
        elif self.definirRefrigeracion.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Equipo de sólo refrigeración'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelRefrigeracion.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.Refrigeracion(self.parent.parent.parent)
            self.seleccionadaAntes = 'refrigeracion'
        elif self.definirCaleYRefri.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Equipo de calefacción y refrigeración'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelClimatizacion.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.Climatizacion(self.parent.parent.parent)
            self.seleccionadaAntes = 'climatizacion'
        elif self.definirSistemasMixtosCaleyACS.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Equipo mixto de calefacción y ACS'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelMixto2.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.MixtosCaleyAcs(self.parent.parent.parent)
            self.seleccionadaAntes = 'mixto2'
        elif self.definirSistemasMixtosClimayACS.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Equipo mixto de calefacción, refrigeración y ACS'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelMixto3.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.MixtosClimayAcs(self.parent.parent.parent)
            self.seleccionadaAntes = 'mixto3'
        elif self.contribucionesEnergeticas.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Contribuciones energéticas'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelRenovables.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.Renovables(self.parent.parent.parent)
            self.seleccionadaAntes = 'renovables'
        elif self.iluminacion.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Equipos de iluminación'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelIluminacion.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='', instalacionIluminacion=self.parent.iluminacion)
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.Iluminacion(self.parent.parent.parent)
            self.seleccionadaAntes = 'iluminacion'
        elif self.ventilacion.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Equipos de aire primario'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelVentilacion.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.Ventilacion(self.parent.parent.parent)
            self.seleccionadaAntes = 'ventilacion'
        elif self.ventiladores.GetValue() == True:
            zona = self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()
            tipoEdificio = self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
            if zona == '' or tipoEdificio == '':
                wx.MessageBox(_('Debe indicar la zona climática HE-1 y el perfil de uso en el panel de datos generales'), _('Aviso'))
                self.OnVolverAnteriorSeleccion()
                return
            self.parent.panelRecuadro.titulo.SetLabel(_('Ventiladores'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelVentiladores.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.ventiladores(self.parent.parent.parent)
        elif self.bombas.GetValue() == True:
            zona = self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()
            tipoEdificio = self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
            if zona == '' or tipoEdificio == '':
                wx.MessageBox(_('Debe indicar la zona climática HE-1 y el perfil de uso en el panel de datos generales'), _('Aviso'))
                self.OnVolverAnteriorSeleccion()
                return
            self.parent.panelRecuadro.titulo.SetLabel(_('Equipos de bombeo'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelBombas.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.bombas(self.parent.parent.parent)
        elif self.torresRefrigeracion.GetValue() == True:
            zona = self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()
            tipoEdificio = self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
            if zona == '' or tipoEdificio == '':
                wx.MessageBox(_('Indique la zona climática HE-1 y el perfil de uso en el panel de datos generales'), _('Aviso'))
                self.OnVolverAnteriorSeleccion()
                return
            self.parent.panelRecuadro.titulo.SetLabel(_('Torres de refrigeración'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelTorresRefrigeracion.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.TorresRefrigeracion(self.parent.parent.parent)

    def OnVolverAnteriorSeleccion(self):
        """
        Metodo: OnVolverAnteriorSeleccion

        """
        if self.seleccionadaAntes == 'ACS':
            self.definirACS.SetValue(True)
        if self.seleccionadaAntes == 'calefaccion':
            self.definirCalefaccion.SetValue(True)
        if self.seleccionadaAntes == 'refrigeracion':
            self.definirRefrigeracion.SetValue(True)
        if self.seleccionadaAntes == 'climatizacion':
            self.definirCaleYRefri.SetValue(True)
        if self.seleccionadaAntes == 'mixto2':
            self.definirSistemasMixtosCaleyACS.SetValue(True)
        if self.seleccionadaAntes == 'mixto3':
            self.definirSistemasMixtosClimayACS.SetValue(True)
        if self.seleccionadaAntes == 'renovables':
            self.contribucionesEnergeticas.SetValue(True)
        if self.seleccionadaAntes == 'iluminacion':
            self.iluminacion.SetValue(True)
        if self.seleccionadaAntes == 'ventilacion':
            self.ventilacion.SetValue(True)