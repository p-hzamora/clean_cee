# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\panelDefinirInstalaciones.pyc
# Compiled at: 2014-12-09 15:09:25
import Instalaciones.panelACS as panelACS, Instalaciones.panelRenovables as panelRenovables, Instalaciones.panelCalefaccion as panelCalefaccion, Instalaciones.panelRefrigeracion as panelRefrigeracion, Instalaciones.panelClimatizacion as panelClimatizacion, Instalaciones.panelMixto2 as panelMixto2, Instalaciones.panelMixto3 as panelMixto3, Instalaciones.panelIluminacion as panelIluminacion, Instalaciones.panelVentilacion as panelVentilacion, Instalaciones.panelVentiladores as panelVentiladores, Instalaciones.panelBombas as panelBombas, Instalaciones.panelTorresRefrigeracion as panelTorresRefrigeracion, tips

class Panel1(wx.Panel):

    def _init_ctrls(self, prnt, id, posi, siz, styles, named):
        self.definirACS = False # or True, era un CheckBox que debia elegir el usuario
        self.definirACS= True
        self.definirCalefaccion = False # or True, era un CheckBox que debia elegir el usuario
        self.definirRefrigeracion = False # or True, era un CheckBox que debia elegir el usuario
        self.definirCaleYRefri = False # or True, era un CheckBox que debia elegir el usuario
        self.definirSistemasMixtosCaleyACS = False # or True, era un CheckBox que debia elegir el usuario
        self.definirSistemasMixtosClimayACS = False # or True, era un CheckBox que debia elegir el usuario
        self.contribucionesEnergeticas = False # or True, era un CheckBox que debia elegir el usuario
        self.iluminacion = False # or True, era un CheckBox que debia elegir el usuario
        self.ventilacion = False # or True, era un CheckBox que debia elegir el usuario
        self.ventiladores = False # or True, era un CheckBox que debia elegir el usuario
        self.bombas = False # or True, era un CheckBox que debia elegir el usuario
        self.torresRefrigeracion = False # or True, era un CheckBox que debia elegir el usuario
        self.staticLine = wx.StaticLine(id=wxID_WXPANEL1STATICLINE, name='staticLine', parent=self, pos=wx.Point(0, 202), size=wx.Size(710, 3), style=0)

    def __init__(self, parent, id, pos, size, style, name):
        self._init_ctrls(parent, id, pos, size, style, name)
        self.parent = parent
        self.seleccionadaAntes = 'ACS'

    def OntipoInstalacion(self, event):
        if self.definirACS == True:
            self.parent.panelRecuadro.titulo.SetLabel('Equipo de ACS')
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelACS.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.Acs(self.parent.parent.parent)
            self.seleccionadaAntes = 'ACS'
        elif self.definirCalefaccion == True:
            self.parent.panelRecuadro.titulo.SetLabel('Equipo de sólo calefacción')
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelCalefaccion.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.Calefaccion(self.parent.parent.parent)
            self.seleccionadaAntes = 'calefaccion'
        elif self.definirRefrigeracion == True:
            self.parent.panelRecuadro.titulo.SetLabel('Equipo de sólo refrigeración')
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelRefrigeracion.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.Refrigeracion(self.parent.parent.parent)
            self.seleccionadaAntes = 'refrigeracion'
        elif self.definirCaleYRefri == True:
            self.parent.panelRecuadro.titulo.SetLabel('Equipo de calefacción y refrigeración')
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelClimatizacion.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.Climatizacion(self.parent.parent.parent)
            self.seleccionadaAntes = 'climatizacion'
        elif self.definirSistemasMixtosCaleyACS == True:
            self.parent.panelRecuadro.titulo.SetLabel('Equipo mixto de calefacción y ACS')
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelMixto2.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.MixtosCaleyAcs(self.parent.parent.parent)
            self.seleccionadaAntes = 'mixto2'
        elif self.definirSistemasMixtosClimayACS == True:
            self.parent.panelRecuadro.titulo.SetLabel('Equipo mixto de calefacción, refrigeración y ACS')
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelMixto3.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.MixtosClimayAcs(self.parent.parent.parent)
            self.seleccionadaAntes = 'mixto3'
        elif self.contribucionesEnergeticas == True:
            self.parent.panelRecuadro.titulo.SetLabel('Contribuciones energéticas')
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelRenovables.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.Renovables(self.parent.parent.parent)
            self.seleccionadaAntes = 'renovables'
        elif self.iluminacion == True:
            self.parent.panelRecuadro.titulo.SetLabel('Equipos de iluminación')
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelIluminacion.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='', instalacionIluminacion=self.parent.iluminacion)
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.Iluminacion(self.parent.parent.parent)
            self.seleccionadaAntes = 'iluminacion'
        elif self.ventilacion == True:
            self.parent.panelRecuadro.titulo.SetLabel('Equipos de aire primario')
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelVentilacion.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.Ventilacion(self.parent.parent.parent)
            self.seleccionadaAntes = 'ventilacion'
        elif self.ventiladores == True:
            zona = self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()
            tipoEdificio = self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
            if zona == '' or tipoEdificio == '':
                raise Exception('Debe indicar la zona climática HE-1 y el perfil de uso en el panel de datos generales')
                self.OnVolverAnteriorSeleccion()
                return
            self.parent.panelRecuadro.titulo.SetLabel('Ventiladores')
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelVentiladores.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.ventiladores(self.parent.parent.parent)
        elif self.bombas == True:
            zona = self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()
            tipoEdificio = self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
            if zona == '' or tipoEdificio == '':
                raise Exception('Debe indicar la zona climática HE-1 y el perfil de uso en el panel de datos generales')
                self.OnVolverAnteriorSeleccion()
                return
            self.parent.panelRecuadro.titulo.SetLabel('Equipos de bombeo')
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelBombas.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.bombas(self.parent.parent.parent)
        elif self.torresRefrigeracion == True:
            zona = self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()
            tipoEdificio = self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
            if zona == '' or tipoEdificio == '':
                raise Exception('Indique la zona climática HE-1 y el perfil de uso en el panel de datos generales')
                self.OnVolverAnteriorSeleccion()
                return
            self.parent.panelRecuadro.titulo.SetLabel('Torres de refrigeración')
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelTorresRefrigeracion.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            tips.TorresRefrigeracion(self.parent.parent.parent)

    def OnVolverAnteriorSeleccion(self):
        if self.seleccionadaAntes == 'ACS':
            self.definirACS= True
        if self.seleccionadaAntes == 'calefaccion':
            self.definirCalefaccion= True
        if self.seleccionadaAntes == 'refrigeracion':
            self.definirRefrigeracion= True
        if self.seleccionadaAntes == 'climatizacion':
            self.definirCaleYRefri= True
        if self.seleccionadaAntes == 'mixto2':
            self.definirSistemasMixtosCaleyACS= True
        if self.seleccionadaAntes == 'mixto3':
            self.definirSistemasMixtosClimayACS= True
        if self.seleccionadaAntes == 'renovables':
            self.contribucionesEnergeticas= True
        if self.seleccionadaAntes == 'iluminacion':
            self.iluminacion= True
        if self.seleccionadaAntes == 'ventilacion':
            self.ventilacion= True