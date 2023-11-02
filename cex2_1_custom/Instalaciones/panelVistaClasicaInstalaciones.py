# Embedded file name: Instalaciones\panelVistaClasicaInstalaciones.pyc
"""
Modulo: panelVistaClasicaInstalaciones.py

"""
from Calculos.listadosWeb import listadoCombustibles, getTraduccion, tablaZona1, tablaZona2, listadoInstalaciones, listadoOpcionesInstalacionesTerciario, listadoInstalacionesElectrico, listadoInstalacionesClimatizacion, listadoOpcionesConsumoBombasOVentiladores, getPosicionKeyEnListado, listadoOpcionesVentiladores, listadoOpcionesBombas, listadoOpcionesTorreDeRefrigeracion, listadoOpcionesServicioVentiladores, listadoOpcionesServicioBombas, listadoOpcionesConsumoBombasOVentiladoresCaudalVariable
from Instalaciones.comprobarCampos import Comprueba, Comprueba2
from miChoiceGrid import MiChoiceGrid
from miGrid import MyGrid
import Instalaciones.dialogoConfirma as dialogoConfirma
import wx
import logging
wxID_PANEL1LISTCTRL1, wxID_WXPANEL2LISTCTRL1, wxID_WXPANEL2LISTHUECOS, wxID_PANEL1GRID1, wxID_PANEL1GRID2, wxID_PANEL1GRID3, wxID_PANEL1GRID4, wxID_PANEL1GRID5, wxID_PANEL1GRID8, wxID_PANEL1GRID7, wxID_PANEL1GRID6, wxID_PANEL1DEFINIRACS, wxID_PANEL1DEFINIRCALEFACCION, wxID_PANEL1DEFINIRREFRIGERACION, wxID_PANEL1CONTRIBUCIONES, wxID_PANEL1ILUMINACIONES, wxID_PANEL1VENTILACION, wxID_PANEL1GTRADIO, wxID_PANEL1ANADIRBOTON, wxID_PANEL1DEFINIR, wxID_WXPANEL1STATICLINE = [ wx.NewId() for _init_ctrls in range(21) ]

class Panel1(wx.Panel):
    """
    Clase: Panel1 del modulo panelVistaClasicaInstalaciones.py
    
    
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
        self.defiirText = wx.StaticText(id=wxID_PANEL1DEFINIR, label=_(u'Instalaciones del edificio'), name='defiirText', parent=self, pos=wx.Point(0, 0), size=wx.Size(222, 18), style=0)
        self.defiirText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, u''))
        self.defiirText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.definirACS = wx.RadioButton(id=wxID_PANEL1DEFINIRACS, label=_(u'Equipos de ACS'), name=u'definirACS', parent=self, pos=wx.Point(20, 30), size=wx.Size(100, 13), style=wx.RB_GROUP)
        self.definirACS.SetValue(True)
        self.definirACS.Bind(wx.EVT_RADIOBUTTON, self.onACSRadio, id=wxID_PANEL1DEFINIRACS)
        self.definirCalefaccion = wx.RadioButton(id=wxID_PANEL1DEFINIRCALEFACCION, label=_(u'Equipos de calefacci\xf3n'), name=u'definirCalefaccion', parent=self, pos=wx.Point(20, 70), size=wx.Size(200, 13), style=0)
        self.definirCalefaccion.Bind(wx.EVT_RADIOBUTTON, self.onCalefaccionRadio, id=wxID_PANEL1DEFINIRCALEFACCION)
        self.definirRefrigeracion = wx.RadioButton(id=wxID_PANEL1DEFINIRREFRIGERACION, label=_(u'Equipos de refrigeraci\xf3n'), name=u'definirRefrigeracion', parent=self, pos=wx.Point(20, 110), size=wx.Size(200, 13), style=0)
        self.definirRefrigeracion.Bind(wx.EVT_RADIOBUTTON, self.onRefrigeracionRadio, id=wxID_PANEL1DEFINIRREFRIGERACION)
        self.contribucionesEnergeticas = wx.RadioButton(id=wxID_PANEL1CONTRIBUCIONES, label=_(u'Contribuciones energ\xe9ticas'), name=u'contribucionesEnergeticas', parent=self, pos=wx.Point(20, 150), size=wx.Size(250, 13), style=0)
        self.contribucionesEnergeticas.Bind(wx.EVT_RADIOBUTTON, self.onRenobablesRadio, id=wxID_PANEL1CONTRIBUCIONES)
        self.definirIluminacion = wx.RadioButton(id=wxID_PANEL1ILUMINACIONES, label=_(u'Equipos de iluminaci\xf3n'), name=u'iluminacion', parent=self, pos=wx.Point(350, 30), size=wx.Size(250, 13), style=0)
        self.definirIluminacion.Bind(wx.EVT_RADIOBUTTON, self.onIluminacionRadio, id=wxID_PANEL1ILUMINACIONES)
        self.definirIluminacion.Show(False)
        self.definirVentilacion = wx.RadioButton(id=wxID_PANEL1VENTILACION, label=_(u'Equipos de aire primario'), name=u'ventilacion', parent=self, pos=wx.Point(350, 70), size=wx.Size(250, 13), style=0)
        self.definirVentilacion.Bind(wx.EVT_RADIOBUTTON, self.onVentilacionRadio, id=wxID_PANEL1VENTILACION)
        self.definirVentilacion.Show(False)
        self.definirEquposGT = wx.RadioButton(id=wxID_PANEL1GTRADIO, label=_(u'Equipos espec\xedficos de gran terciario'), name=u'ventilacion', parent=self, pos=wx.Point(350, 110), size=wx.Size(250, 13), style=0)
        self.definirEquposGT.Bind(wx.EVT_RADIOBUTTON, self.onEquiposGTRadio, id=wxID_PANEL1GTRADIO)
        self.definirEquposGT.Show(False)
        self.listaACS = MyGrid(id=wxID_PANEL1GRID6, parent=self, pos=wx.Point(0, 232), size=wx.Size(710, 308), style=wx.RAISED_BORDER)
        self.listaACS.Bind(wx.grid.EVT_GRID_CELL_CHANGE, self.onListaACS, id=wxID_PANEL1GRID6)
        self._init_coll_listaACS_Columns(self.listaACS)
        self.listaCalefaccion = MyGrid(id=wxID_PANEL1GRID7, parent=self, pos=wx.Point(0, 232), size=wx.Size(710, 308), style=wx.RAISED_BORDER)
        self.listaCalefaccion.Bind(wx.grid.EVT_GRID_CELL_CHANGE, self.onListaCalefaccion, id=wxID_PANEL1GRID7)
        self._init_coll_listaCalefaccion_Columns(self.listaCalefaccion)
        self.listaRefrigeracion = MyGrid(id=wxID_PANEL1GRID8, parent=self, pos=wx.Point(0, 232), size=wx.Size(710, 308), style=wx.RAISED_BORDER)
        self.listaRefrigeracion.Bind(wx.grid.EVT_GRID_CELL_CHANGE, self.onListaRefrigeracion, id=wxID_PANEL1GRID8)
        self._init_coll_listaRefrigeracion_Columns(self.listaRefrigeracion)
        self.listaIluminacion = MyGrid(id=wxID_PANEL1GRID1, parent=self, pos=wx.Point(0, 232), size=wx.Size(710, 308), style=wx.RAISED_BORDER)
        self.listaIluminacion.Bind(wx.grid.EVT_GRID_CELL_CHANGE, self.onListaIluminacion, id=wxID_PANEL1GRID1)
        self._init_coll_listaIluminacion_Columns(self.listaIluminacion)
        self.listaAirePrimario = MyGrid(id=wxID_PANEL1GRID2, parent=self, pos=wx.Point(0, 232), size=wx.Size(710, 308), style=wx.RAISED_BORDER)
        self.listaAirePrimario.Bind(wx.grid.EVT_GRID_CELL_CHANGE, self.onListaAirePrimario, id=wxID_PANEL1GRID2)
        self._init_coll_listaAirePrimario_Columns(self.listaAirePrimario)
        self.listaGT = MyGrid(id=wxID_PANEL1GRID3, parent=self, pos=wx.Point(0, 232), size=wx.Size(710, 308), style=wx.RAISED_BORDER)
        self.listaGT.Bind(wx.grid.EVT_GRID_CELL_CHANGE, self.onListaGT, id=wxID_PANEL1GRID3)
        self._init_coll_listaGT_Columns(self.listaGT)
        self.listaRenovables = MyGrid(id=wxID_PANEL1GRID5, parent=self, pos=wx.Point(0, 232), size=wx.Size(710, 308), style=wx.RAISED_BORDER)
        self.listaRenovables.Bind(wx.grid.EVT_GRID_CELL_CHANGE, self.onListaRenovables, id=wxID_PANEL1GRID5)
        self._init_coll_listaRenovables_Columns(self.listaRenovables)
        self.staticLine = wx.StaticLine(id=wxID_WXPANEL1STATICLINE, name='staticLine', parent=self, pos=wx.Point(0, 202), size=wx.Size(710, 3), style=0)
        self.staticLine.SetBackgroundColour(wx.Colour(0, 64, 128))
        self.guardarBoton = wx.Button(id=wxID_PANEL1ANADIRBOTON, label=_(u'Guardar cambios'), name=u'anadirBoton', parent=self, pos=wx.Point(610, 555), size=wx.Size(100, 23), style=0)
        self.guardarBoton.Bind(wx.EVT_BUTTON, self.onGuardarBoton, id=wxID_PANEL1ANADIRBOTON)
        self.listaACS.AutoSizeColumns()
        self.listaACS.Show(True)
        self.listaCalefaccion.AutoSizeColumns()
        self.listaCalefaccion.Show(False)
        self.listaRefrigeracion.AutoSizeColumns()
        self.listaRefrigeracion.Show(False)
        self.listaIluminacion.AutoSizeColumns()
        self.listaIluminacion.Show(False)
        self.listaAirePrimario.AutoSizeColumns()
        self.listaAirePrimario.Show(False)
        self.listaGT.AutoSizeColumns()
        self.listaGT.Show(False)
        self.listaRenovables.AutoSizeColumns()
        self.listaRenovables.Show(False)
        self.listaActual = 'ACS'

    def onACSRadio(self, event):
        """
        Metodo: onACSRadio
        
        
        ARGUMENTOS:
                event:
        """
        self.seleccionCorrecta('ACS', '')

    def onCalefaccionRadio(self, event):
        """
        Metodo: onCalefaccionRadio
        
        
        ARGUMENTOS:
                event:
        """
        self.seleccionCorrecta('calefaccion', '')

    def onRefrigeracionRadio(self, event):
        """
        Metodo: onRefrigeracionRadio
        
        
        ARGUMENTOS:
                event:
        """
        self.seleccionCorrecta('refrigeracion', '')

    def onRenobablesRadio(self, event):
        """
        Metodo: onRenobablesRadio
        
        
        ARGUMENTOS:
                event:
        """
        self.seleccionCorrecta('renovables', '')

    def onIluminacionRadio(self, event):
        """
        Metodo: onIluminacionRadio
        
        
        ARGUMENTOS:
                event:
        """
        self.seleccionCorrecta('iluminacion', '')

    def onVentilacionRadio(self, event):
        """
        Metodo: onVentilacionRadio
        
        
        ARGUMENTOS:
                event:
        """
        self.seleccionCorrecta('ventilacion', '')

    def onEquiposGTRadio(self, event):
        """
        Metodo: onEquiposGTRadio
        
        
        ARGUMENTOS:
                event:
        """
        self.seleccionCorrecta('GT', '')

    def _init_coll_listaRenovables_Columns(self, parent):
        """
        Metodo: _init_coll_listaRenovables_Columns
        
        
        ARGUMENTOS:
                parent:
        """
        parent.CreateGrid(0, 11)
        parent.SetColLabelValue(0, _(u'Nombre'))
        parent.SetColLabelValue(1, _(u'Zona'))
        parent.SetColLabelValue(2, _(u'% demanda ACS\ncubierto con renovables'))
        parent.SetColLabelValue(3, _(u'% calefacci\xf3n\ncubierto con renovables'))
        parent.SetColLabelValue(4, _(u'% refrigeraci\xf3n\ncubierto con renovables'))
        parent.SetColLabelValue(5, _(u'Energ\xeda el\xe9ctrica generada con\nrenovables/cogeneraci\xf3n (kwh/a\xf1o)'))
        parent.SetColLabelValue(6, _(u'Calor recuperado para\nACS (kwh/a\xf1o)'))
        parent.SetColLabelValue(7, _(u'Calor recuperado para\ncalefacci\xf3n (kwh/a\xf1o)'))
        parent.SetColLabelValue(8, _(u'Fr\xedo recuperado\n(kwh/a\xf1o)'))
        parent.SetColLabelValue(9, _(u'Energ\xeda consumida en\ngeneraci\xf3n de electricidad (kwh/a\xf1o)'))
        parent.SetColLabelValue(10, _(u'Combustible'))

    def _init_coll_listaIluminacion_Columns(self, parent):
        """
        Metodo: _init_coll_listaIluminacion_Columns
        
        
        ARGUMENTOS:
                parent:
        """
        parent.CreateGrid(0, 8)
        parent.SetColLabelValue(0, _(u'Nombre'))
        parent.SetColLabelValue(1, _(u'Zona'))
        parent.SetColLabelValue(2, _(u'Superficie\n(m2)'))
        parent.SetColLabelValue(3, _(u'Zona\nrepresentaci\xf3n'))
        parent.SetColLabelValue(4, _(u'Actividad'))
        parent.SetColLabelValue(5, _(u'Modo definici\xf3n'))
        parent.SetColLabelValue(6, _(u'Potencia\n(W)'))
        parent.SetColLabelValue(7, _(u'Iluminancia\n(lux)'))

    def _init_coll_listaAirePrimario_Columns(self, parent):
        """
        Metodo: _init_coll_listaAirePrimario_Columns
        
        
        ARGUMENTOS:
                parent:
        """
        parent.CreateGrid(0, 5)
        parent.SetColLabelValue(0, _(u'Nombre'))
        parent.SetColLabelValue(1, _(u'Zona'))
        parent.SetColLabelValue(2, _(u'Caudal de ventilaci\xf3n (m3/h)'))
        parent.SetColLabelValue(3, _(u'Recuperaci\xf3n de calor'))
        parent.SetColLabelValue(4, _(u'Rendimiento del recuperador (%)'))

    def _init_coll_listaGT_Columns(self, parent):
        """
        Metodo: _init_coll_listaAirePrimario_Columns
        
        
        ARGUMENTOS:
                parent:
        """
        parent.CreateGrid(0, 6)
        parent.SetColLabelValue(0, _(u'Nombre'))
        parent.SetColLabelValue(1, _(u'Zona'))
        parent.SetColLabelValue(2, _(u'Tipo de equipo'))
        parent.SetColLabelValue(3, _(u'Servicio'))
        parent.SetColLabelValue(4, _(u'Modo definici\xf3n'))
        parent.SetColLabelValue(5, _(u'Consumo anual (kWh)'))

    def _init_coll_listaACS_Columns(self, parent):
        """
        Metodo: _init_coll_listaACS_Columns
        
        
        ARGUMENTOS:
                parent:
        """
        parent.CreateGrid(0, 10)
        parent.SetColLabelValue(0, _(u'Nombre'))
        parent.SetColLabelValue(1, _(u'Tipo de equipo'))
        parent.SetColLabelValue(2, _(u'Modo definici\xf3n'))
        parent.SetColLabelValue(3, _(u'Tipo generador'))
        parent.SetColLabelValue(4, _(u'Combustible'))
        parent.SetColLabelValue(5, _(u'Rendimiento\nestacional (%)'))
        parent.SetColLabelValue(6, _(u'm2 cubiertos'))
        parent.SetColLabelValue(7, _(u'Demanda\ncubierta (%)'))
        parent.SetColLabelValue(8, _(u'Zona'))
        parent.SetColLabelValue(9, _(u'Acumulaci\xf3n'))

    def _init_coll_listaCalefaccion_Columns(self, parent):
        """
        Metodo: _init_coll_listaCalefaccion_Columns
        
        
        ARGUMENTOS:
                parent:
        """
        parent.CreateGrid(0, 9)
        parent.SetColLabelValue(0, _(u'Nombre'))
        parent.SetColLabelValue(1, _(u'Tipo de equipo'))
        parent.SetColLabelValue(2, _(u'Modo definici\xf3n'))
        parent.SetColLabelValue(3, _(u'Tipo generador'))
        parent.SetColLabelValue(4, _(u'Combustible'))
        parent.SetColLabelValue(5, _(u'Rendimiento\nestacional (%)'))
        parent.SetColLabelValue(6, _(u'm2 cubiertos'))
        parent.SetColLabelValue(7, _(u'Demanda\ncubierta (%)'))
        parent.SetColLabelValue(8, _(u'Zona'))

    def _init_coll_listaRefrigeracion_Columns(self, parent):
        """
        Metodo: _init_coll_listaRefrigeracion_Columns
        
        
        ARGUMENTOS:
                parent:
        """
        parent.CreateGrid(0, 9)
        parent.SetColLabelValue(0, _(u'Nombre'))
        parent.SetColLabelValue(1, _(u'Tipo de equipo'))
        parent.SetColLabelValue(2, _(u'Modo definici\xf3n'))
        parent.SetColLabelValue(3, _(u'Tipo generador'))
        parent.SetColLabelValue(4, _(u'Combustible'))
        parent.SetColLabelValue(5, _(u'Rendimiento\nestacional (%)'))
        parent.SetColLabelValue(6, _(u'm2 cubiertos'))
        parent.SetColLabelValue(7, _(u'Demanda\ncubierta (%)'))
        parent.SetColLabelValue(8, _(u'Zona'))

    def seleccionCorrecta(self, tabla, item):
        """
        Metodo: seleccionCorrecta
        
        
        ARGUMENTOS:
                tabla:
                item:
        """
        if self.cambios == True:
            if self.confirmacionUsuario():
                if self.realizaCambios() == False:
                    self.parent.arbolInstalaciones.SelectItem(self.parent.arbolInstalaciones.GetRootItem())
                    return
            else:
                self.cargaVista()
        if tabla == 'ACS':
            self.listaACS.Show(True)
            self.listaCalefaccion.Show(False)
            self.listaRefrigeracion.Show(False)
            self.listaIluminacion.Show(False)
            self.listaAirePrimario.Show(False)
            self.listaGT.Show(False)
            self.listaRenovables.Show(False)
            self.listaActual = 'ACS'
            for i in range(self.listaACS.GetNumberRows()):
                if item == self.listaACS.GetCellValue(i, 0):
                    self.listaACS.SelectRow(i)
                    return

        elif tabla == 'calefaccion':
            self.listaACS.Show(False)
            self.listaCalefaccion.Show(True)
            self.listaRefrigeracion.Show(False)
            self.listaIluminacion.Show(False)
            self.listaAirePrimario.Show(False)
            self.listaGT.Show(False)
            self.listaRenovables.Show(False)
            self.listaActual = 'calefaccion'
            for i in range(self.listaCalefaccion.GetNumberRows()):
                if item == self.listaCalefaccion.GetCellValue(i, 0):
                    self.listaCalefaccion.SelectRow(i)
                    return

        elif tabla == 'refrigeracion':
            self.listaACS.Show(False)
            self.listaCalefaccion.Show(False)
            self.listaRefrigeracion.Show(True)
            self.listaIluminacion.Show(False)
            self.listaAirePrimario.Show(False)
            self.listaGT.Show(False)
            self.listaRenovables.Show(False)
            self.listaActual = 'refrigeracion'
            for i in range(self.listaRefrigeracion.GetNumberRows()):
                if item == self.listaRefrigeracion.GetCellValue(i, 0):
                    self.listaRefrigeracion.SelectRow(i)
                    return

        elif tabla == 'iluminacion':
            self.listaACS.Show(False)
            self.listaCalefaccion.Show(False)
            self.listaRefrigeracion.Show(False)
            self.listaIluminacion.Show(True)
            self.listaAirePrimario.Show(False)
            self.listaGT.Show(False)
            self.listaRenovables.Show(False)
            self.listaActual = 'iluminacion'
            for i in range(self.listaIluminacion.GetNumberRows()):
                if item == self.listaIluminacion.GetCellValue(i, 0):
                    self.listaIluminacion.SelectRow(i)
                    return

        elif tabla == 'ventilacion':
            self.listaACS.Show(False)
            self.listaCalefaccion.Show(False)
            self.listaRefrigeracion.Show(False)
            self.listaIluminacion.Show(False)
            self.listaAirePrimario.Show(True)
            self.listaGT.Show(False)
            self.listaRenovables.Show(False)
            self.listaActual = 'ventilacion'
            for i in range(self.listaAirePrimario.GetNumberRows()):
                if item == self.listaAirePrimario.GetCellValue(i, 0):
                    self.listaAirePrimario.SelectRow(i)
                    return

        elif tabla == 'GT':
            self.listaACS.Show(False)
            self.listaCalefaccion.Show(False)
            self.listaRefrigeracion.Show(False)
            self.listaIluminacion.Show(False)
            self.listaAirePrimario.Show(False)
            self.listaGT.Show(True)
            self.listaRenovables.Show(False)
            self.listaActual = 'GT'
            for i in range(self.listaGT.GetNumberRows()):
                if item == self.listaGT.GetCellValue(i, 0):
                    self.listaGT.SelectRow(i)
                    return

        elif tabla == 'renovables':
            self.listaACS.Show(False)
            self.listaCalefaccion.Show(False)
            self.listaRefrigeracion.Show(False)
            self.listaIluminacion.Show(False)
            self.listaAirePrimario.Show(False)
            self.listaGT.Show(False)
            self.listaRenovables.Show(True)
            self.listaActual = 'renovables'
            for i in range(self.listaRenovables.GetNumberRows()):
                if item == self.listaRenovables.GetCellValue(i, 0):
                    self.listaRenovables.SelectRow(i)
                    return

    def onListaIluminacion(self, event):
        """
        Metodo: onListaIluminacion
        
        
        ARGUMENTOS:
                event:
        """
        self.cambios = True
        if event.GetCol() == 5:
            if self.listaIluminacion.GetCellValue(event.GetRow(), event.GetCol()) == 'Conocido':
                self.listaIluminacion.SetReadOnly(event.GetRow(), event.GetCol())
                self.listaIluminacion.SetReadOnly(event.GetRow(), 6, False)

    def onListaRenovables(self, event):
        """
        Metodo: onListaRenovables
        
        
        ARGUMENTOS:
                event:
        """
        self.cambios = True

    def onListaAirePrimario(self, event):
        """
        Metodo: onListaAirePrimario
        
        
        ARGUMENTOS:
                event:
        """
        self.cambios = True
        if event.GetCol() == 3:
            if self.listaAirePrimario.GetCellValue(event.GetRow(), event.GetCol()) == 'Si':
                self.listaAirePrimario.SetCellValue(event.GetRow(), 4, '')
            else:
                self.listaAirePrimario.SetCellValue(event.GetRow(), 4, '0')

    def onListaGT(self, event):
        """
        Metodo: onListaGT
        
        
        ARGUMENTOS:
                event:
        """
        self.cambios = True
        if event.GetCol() == 4:
            if self.listaGT.GetCellValue(event.GetRow(), event.GetCol()) == 'Conocido':
                self.listaGT.SetReadOnly(event.GetRow(), event.GetCol())
                self.listaGT.SetReadOnly(event.GetRow(), 5, False)

    def onListaACS(self, event):
        """
        Metodo: onListaACS
        
        
        ARGUMENTOS:
                event:
        """
        self.cambios = True
        if event.GetCol() == 2:
            if self.listaACS.GetCellValue(event.GetRow(), event.GetCol()) == 'Conocido':
                self.listaACS.SetReadOnly(event.GetRow(), event.GetCol())
                self.listaACS.SetReadOnly(event.GetRow(), 5, False)
                self.listaACS.SetReadOnly(event.GetRow(), 3, False)
                self.listaACS.SetReadOnly(event.GetRow(), 4, False)
                generador = wx.grid.GridCellChoiceEditor(self.parent.listadoInstalaciones)
                combus = wx.grid.GridCellChoiceEditor(self.parent.listadoCombustibles)
                generadorClima = wx.grid.GridCellChoiceEditor(self.parent.listadoInstalacionesClimatizacion)
                if self.listaACS.GetCellValue(event.GetRow(), 1) in (u'ACS', u'ACS y Calefacci\xf3n'):
                    self.listaACS.SetCellEditor(event.GetRow(), 3, generador)
                    self.listaACS.SetCellEditor(event.GetRow(), 4, combus)
                else:
                    self.listaACS.SetCellEditor(event.GetRow(), 3, generadorClima)
                    self.listaACS.SetCellEditor(event.GetRow(), 4, combus)
        if event.GetCol() == 6:
            try:
                m = float(self.listaACS.GetCellValue(event.GetRow(), event.GetCol()))
                if self.listaACS.GetCellValue(event.GetRow(), 8) == 'Edificio Objeto':
                    total = float(self.parent.parent.parent.panelDatosGenerales.superficie.GetValue())
                else:
                    for i in self.parent.parent.subgrupos:
                        if i.nombre == self.listaACS.GetCellValue(event.GetRow(), 8):
                            total = float(i.superficie)

                p = round(m * 100 / total, 2)
                self.listaACS.SetCellValue(event.GetRow(), 7, str(p))
            except:
                logging.info(u'Excepcion en: %s' % __name__)

        if event.GetCol() == 7:
            try:
                p = float(self.listaACS.GetCellValue(event.GetRow(), event.GetCol()))
                if self.listaACS.GetCellValue(event.GetRow(), 8) == 'Edificio Objeto':
                    total = float(self.parent.parent.parent.panelDatosGenerales.superficie.GetValue())
                else:
                    for i in self.parent.parent.subgrupos:
                        if i.nombre == self.listaACS.GetCellValue(event.GetRow(), 8):
                            total = float(i.superficie)

                m = round(p * total / 100, 2)
                self.listaACS.SetCellValue(event.GetRow(), 6, str(m))
            except:
                logging.info(u'Excepcion en: %s' % __name__)

    def onListaCalefaccion(self, event):
        """
        Metodo: onListaCalefaccion
        
        
        ARGUMENTOS:
                event:
        """
        self.cambios = True
        if event.GetCol() == 2:
            if self.listaCalefaccion.GetCellValue(event.GetRow(), event.GetCol()) == 'Conocido':
                self.listaCalefaccion.SetReadOnly(event.GetRow(), event.GetCol())
                self.listaCalefaccion.SetReadOnly(event.GetRow(), 5, False)
                self.listaCalefaccion.SetReadOnly(event.GetRow(), 3, False)
                self.listaCalefaccion.SetReadOnly(event.GetRow(), 4, False)
                generador = wx.grid.GridCellChoiceEditor(self.parent.listadoInstalaciones)
                combus = wx.grid.GridCellChoiceEditor(self.parent.listadoCombustibles)
                generadorClima = wx.grid.GridCellChoiceEditor(self.parent.listadoInstalacionesClimatizacion)
                if self.listaCalefaccion.GetCellValue(event.GetRow(), 1) in (u'Calefacci\xf3n', u'ACS y Calefacci\xf3n'):
                    self.listaCalefaccion.SetCellEditor(event.GetRow(), 3, generador)
                    self.listaCalefaccion.SetCellEditor(event.GetRow(), 4, combus)
                else:
                    self.listaCalefaccion.SetCellEditor(event.GetRow(), 3, generadorClima)
                    self.listaCalefaccion.SetCellEditor(event.GetRow(), 4, combus)
        if event.GetCol() == 6:
            try:
                m = float(self.listaCalefaccion.GetCellValue(event.GetRow(), event.GetCol()))
                if self.listaCalefaccion.GetCellValue(event.GetRow(), 8) == 'Edificio Objeto':
                    total = float(self.parent.parent.parent.panelDatosGenerales.superficie.GetValue())
                else:
                    for i in self.parent.parent.subgrupos:
                        if i.nombre == self.listaCalefaccion.GetCellValue(event.GetRow(), 8):
                            total = float(i.superficie)

                p = round(m * 100 / total, 2)
                self.listaCalefaccion.SetCellValue(event.GetRow(), 7, str(p))
            except:
                logging.info(u'Excepcion en: %s' % __name__)

        if event.GetCol() == 7:
            try:
                p = float(self.listaCalefaccion.GetCellValue(event.GetRow(), event.GetCol()))
                if self.listaCalefaccion.GetCellValue(event.GetRow(), 8) == 'Edificio Objeto':
                    total = float(self.parent.parent.parent.panelDatosGenerales.superficie.GetValue())
                else:
                    for i in self.parent.parent.subgrupos:
                        if i.nombre == self.listaCalefaccion.GetCellValue(event.GetRow(), 8):
                            total = float(i.superficie)

                m = round(p * total / 100, 2)
                self.listaCalefaccion.SetCellValue(event.GetRow(), 6, str(m))
            except:
                logging.info(u'Excepcion en: %s' % __name__)

    def onListaRefrigeracion(self, event):
        """
        Metodo: onListaRefrigeracion
        
        
        ARGUMENTOS:
                event:
        """
        self.cambios = True
        if event.GetCol() == 2:
            if self.listaRefrigeracion.GetCellValue(event.GetRow(), event.GetCol()) == 'Conocido':
                self.listaRefrigeracion.SetReadOnly(event.GetRow(), event.GetCol())
                self.listaRefrigeracion.SetReadOnly(event.GetRow(), 5, False)
        if event.GetCol() == 6:
            try:
                m = float(self.listaRefrigeracion.GetCellValue(event.GetRow(), event.GetCol()))
                if self.listaRefrigeracion.GetCellValue(event.GetRow(), 8) == 'Edificio Objeto':
                    total = float(self.parent.parent.parent.panelDatosGenerales.superficie.GetValue())
                else:
                    for i in self.parent.parent.subgrupos:
                        if i.nombre == self.listaRefrigeracion.GetCellValue(event.GetRow(), 8):
                            total = float(i.superficie)

                p = round(m * 100 / total, 2)
                self.listaRefrigeracion.SetCellValue(event.GetRow(), 7, str(p))
            except:
                pass

        if event.GetCol() == 7:
            try:
                p = float(self.listaRefrigeracion.GetCellValue(event.GetRow(), event.GetCol()))
                if self.listaRefrigeracion.GetCellValue(event.GetRow(), 8) == 'Edificio Objeto':
                    total = float(self.parent.parent.parent.panelDatosGenerales.superficie.GetValue())
                else:
                    for i in self.parent.parent.subgrupos:
                        if i.nombre == self.listaRefrigeracion.GetCellValue(event.GetRow(), 8):
                            total = float(i.superficie)

                m = round(p * total / 100, 2)
                self.listaRefrigeracion.SetCellValue(event.GetRow(), 6, str(m))
            except:
                logging.info(u'Excepcion en: %s' % __name__)

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
        self.cambios = False

    def cargarListaEquipoGeneracion(self, listaTabla, listaInst, queCubreLaInstalacion):
        """
        M\xe9todo: cargarListaEquipoGeneracion
        Atributos:
            listaTabla: tabla que voy construyendo
            listaInst: array con instalaciones
            queCubreLaInstalacion: 'ACS', 'calefacci\xf3n', 'refrigeracion' xa saber qeu rendimiento medio estacional hay que coger
        Recarga la tabla correspondientes
        """
        if queCubreLaInstalacion == 'ACS':
            contadorArray = 0
        elif queCubreLaInstalacion == 'calefaccion':
            contadorArray = 1
        elif queCubreLaInstalacion == 'refrigeracion':
            contadorArray = 2
        diccTipoSistema = {'ACS': u'ACS',
         'calefaccion': u'Calefacci\xf3n',
         'refrigeracion': u'Refrigeraci\xf3n',
         'climatizacion': u'Calefacci\xf3n y refrigeraci\xf3n',
         'mixto2': u'ACS y calefacci\xf3n',
         'mixto3': u'ACS, calefacci\xf3n y refrigeraci\xf3n'}
        opcionesTipoCombustible = MiChoiceGrid(choices=listadoCombustibles)
        listaTabla.ampliaDiccionarioTraduccion(opcionesTipoCombustible.traduccion)
        opcionesModoDefinicion = MiChoiceGrid(choices=listadoOpcionesInstalacionesTerciario)
        listaTabla.ampliaDiccionarioTraduccion(opcionesModoDefinicion.traduccion)
        cnt = 0
        for i in range(len(listaInst)):
            listaTabla.AppendRows(1)
            listaTabla.SetCellValue(cnt, 0, listaInst[i][0])
            listaTabla.SetReadOnly(cnt, 0)
            tipoSistema = listaInst[i][1]
            if tipoSistema in ('ACS', 'mixto2', 'calefaccion'):
                listInstalaciones = listadoInstalaciones
            elif tipoSistema in ('refrigeracion',):
                listInstalaciones = listadoInstalacionesElectrico
            elif tipoSistema in ('climatizacion', 'mixto3'):
                listInstalaciones = listadoInstalacionesClimatizacion
            opcionesTipoGenerador = MiChoiceGrid(choices=listInstalaciones)
            listaTabla.ampliaDiccionarioTraduccion(opcionesTipoGenerador.traduccion)
            tipo = diccTipoSistema[tipoSistema]
            listaTabla.ampliaDiccionarioTraduccion({_(tipo): tipo})
            listaTabla.SetCellValue(cnt, 1, tipo)
            listaTabla.SetReadOnly(cnt, 1)
            listaTabla.SetCellEditor(i, 2, opcionesModoDefinicion)
            listaTabla.SetCellValue(cnt, 2, listaInst[i][6])
            listaTabla.SetReadOnly(cnt, 2)
            listaTabla.SetCellEditor(i, 3, opcionesTipoGenerador)
            listaTabla.SetCellValue(cnt, 3, listaInst[i][3])
            listaTabla.SetReadOnly(cnt, 3)
            combustible = getTraduccion(listado=listadoCombustibles, elemento=listaInst[i][4])
            listaTabla.SetCellEditor(i, 4, opcionesTipoCombustible)
            listaTabla.SetCellValue(cnt, 4, combustible)
            listaTabla.SetReadOnly(cnt, 4)
            listaTabla.SetCellValue(cnt, 5, str(listaInst[i][2][contadorArray]))
            listaTabla.SetReadOnly(cnt, 5)
            listaTabla.SetCellValue(cnt, 6, str(listaInst[i][5][contadorArray][0]))
            listaTabla.SetCellValue(cnt, 7, str(listaInst[i][5][contadorArray][1]))
            listaTabla.ampliaDiccionarioTraduccion({_(listaInst[i][-1]): listaInst[i][-1]})
            listaTabla.SetCellValue(cnt, 8, listaInst[i][-1])
            listaTabla.SetReadOnly(cnt, 8)
            if queCubreLaInstalacion == 'ACS':
                if listaInst[i][8][0] == True:
                    listaTabla.SetCellValue(cnt, 9, 'Si')
                else:
                    listaTabla.SetCellValue(cnt, 9, 'No')
                listaTabla.SetReadOnly(cnt, 9)
            cnt += 1

    def cargarListaACS(self):
        """
        Metodo: cargarACS
        
        
        """
        try:
            self.listaACS.DeleteRows(0, self.listaGT.GetNumberRows())
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            self.listaACS.DeleteRows(0, self.listaACS.GetNumberRows())
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        listaInstalacionesQueCubrenACS = self.parent.ACS + self.parent.mixto2 + self.parent.mixto3
        self.cargarListaEquipoGeneracion(listaTabla=self.listaACS, listaInst=listaInstalacionesQueCubrenACS, queCubreLaInstalacion='ACS')
        self.listaACS.AutoSizeColumns()

    def cargarListaCalefaccion(self):
        """
        Metodo: cargarListaCalefaccion
        
        
        """
        try:
            self.listaCalefaccion.DeleteRows(0, self.listaCalefaccion.GetNumberRows())
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        listaInstalacionesQueCubrenCal = self.parent.calefaccion + self.parent.mixto2 + self.parent.climatizacion + self.parent.mixto3
        self.cargarListaEquipoGeneracion(listaTabla=self.listaCalefaccion, listaInst=listaInstalacionesQueCubrenCal, queCubreLaInstalacion='calefaccion')
        self.listaCalefaccion.AutoSizeColumns()

    def cargarListaRefrigeracion(self):
        """
        Metodo: cargarListaRefrigeracion
        
        
        """
        try:
            self.listaRefrigeracion.DeleteRows(0, self.listaRefrigeracion.GetNumberRows())
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        listaInstalacionesQueCubrenRef = self.parent.refrigeracion + self.parent.climatizacion + self.parent.mixto3
        self.cargarListaEquipoGeneracion(listaTabla=self.listaRefrigeracion, listaInst=listaInstalacionesQueCubrenRef, queCubreLaInstalacion='refrigeracion')
        self.listaRefrigeracion.AutoSizeColumns()

    def cargarListaGT(self):
        """
        Metodo: cargarListaGT
        """
        try:
            self.listaGT.DeleteRows(0, self.listaGT.GetNumberRows())
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        listadoEquiposGT = self.parent.ventiladores + self.parent.bombas + self.parent.torresRefrigeracion
        for i in range(len(listadoEquiposGT)):
            self.listaGT.AppendRows(1)
            self.listaGT.SetCellValue(i, 0, listadoEquiposGT[i][0])
            self.listaGT.SetReadOnly(i, 0)
            self.listaGT.ampliaDiccionarioTraduccion({_(listadoEquiposGT[i][-1]): listadoEquiposGT[i][-1]})
            self.listaGT.SetCellValue(i, 1, listadoEquiposGT[i][-1])
            self.listaGT.SetReadOnly(i, 1)
            if listadoEquiposGT[i][1] == 'ventiladores':
                tipoEquipo = listadoOpcionesVentiladores[listadoEquiposGT[i][3]][0]
            elif listadoEquiposGT[i][1] == 'bombas':
                tipoEquipo = listadoOpcionesBombas[listadoEquiposGT[i][3]][0]
            elif listadoEquiposGT[i][1] == 'torresRefrigeracion':
                tipoEquipo = listadoOpcionesTorreDeRefrigeracion[listadoEquiposGT[i][3]][0]
            self.listaGT.ampliaDiccionarioTraduccion({_(tipoEquipo): tipoEquipo})
            self.listaGT.SetCellValue(i, 2, tipoEquipo)
            self.listaGT.SetReadOnly(i, 2)
            if listadoEquiposGT[i][1] == 'ventiladores':
                servicio = listadoOpcionesServicioVentiladores[listadoEquiposGT[i][12]][0]
                self.listaGT.ampliaDiccionarioTraduccion({_(servicio): servicio})
                self.listaGT.SetCellValue(i, 3, servicio)
            if listadoEquiposGT[i][1] == 'bombas':
                servicio = listadoOpcionesServicioBombas[listadoEquiposGT[i][12]][0]
                self.listaGT.ampliaDiccionarioTraduccion({_(servicio): servicio})
                self.listaGT.SetCellValue(i, 3, servicio)
            elif listadoEquiposGT[i][1] == 'torresRefrigeracion':
                self.listaGT.SetCellValue(i, 3, '-')
            self.listaGT.SetReadOnly(i, 3)
            if tipoEquipo in (u'Ventilador de caudal constante', u'Bomba de caudal constante', u'Torre de refrigeraci\xf3n: 1 velocidad'):
                modoDefinicion = listadoOpcionesConsumoBombasOVentiladores[listadoEquiposGT[i][6]][0]
            else:
                modoDefinicion = listadoOpcionesConsumoBombasOVentiladoresCaudalVariable[listadoEquiposGT[i][6]][0]
            self.listaGT.ampliaDiccionarioTraduccion({_(modoDefinicion): modoDefinicion})
            self.listaGT.SetCellValue(i, 4, modoDefinicion)
            self.listaGT.SetReadOnly(i, 4)
            self.listaGT.SetCellValue(i, 5, listadoEquiposGT[i][2])
            if listadoEquiposGT[i][6] != 0:
                self.listaGT.SetReadOnly(i, 5)

        self.listaGT.AutoSizeColumns()

    def cargarListaAirePrimario(self):
        """
        Metodo: cargarListaAirePrimario
        
        
        """
        try:
            self.listaAirePrimario.DeleteRows(0, self.listaAirePrimario.GetNumberRows())
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        opcionesRecuperadorCalor = MiChoiceGrid(choices=[(True, _(u'Si')), (False, _(u'No'))])
        self.listaAirePrimario.ampliaDiccionarioTraduccion(opcionesRecuperadorCalor.traduccion)
        for i in range(len(self.parent.ventilacion)):
            self.listaAirePrimario.AppendRows(1)
            self.listaAirePrimario.SetCellValue(i, 0, self.parent.ventilacion[i][0])
            self.listaAirePrimario.SetReadOnly(i, 0)
            self.listaAirePrimario.ampliaDiccionarioTraduccion({_(self.parent.ventilacion[i][-1]): self.parent.ventilacion[i][-1]})
            self.listaAirePrimario.SetCellValue(i, 1, self.parent.ventilacion[i][-1])
            self.listaAirePrimario.SetReadOnly(i, 1)
            self.listaAirePrimario.SetCellValue(i, 2, self.parent.ventilacion[i][2])
            self.listaAirePrimario.SetCellEditor(i, 3, opcionesRecuperadorCalor)
            self.listaAirePrimario.SetCellValue(i, 3, self.parent.ventilacion[i][3])
            self.listaAirePrimario.SetCellValue(i, 4, str(self.parent.ventilacion[i][4]))

        self.listaAirePrimario.AutoSizeColumns()

    def cargarListaIluminacion(self):
        """
        Metodo: cargarListaIluminacion
        
        
        """
        try:
            self.listaIluminacion.DeleteRows(0, self.listaIluminacion.GetNumberRows())
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        opcionesAcividad1 = MiChoiceGrid(choices=tablaZona1)
        opcionesAcividad2 = MiChoiceGrid(choices=tablaZona2)
        self.listaIluminacion.ampliaDiccionarioTraduccion(opcionesAcividad1.traduccion)
        self.listaIluminacion.ampliaDiccionarioTraduccion(opcionesAcividad2.traduccion)
        opcionesZonaRepresentacion = MiChoiceGrid(choices=[(True, _(u'Si')), (False, _(u'No'))])
        self.listaIluminacion.ampliaDiccionarioTraduccion(opcionesZonaRepresentacion.traduccion)
        for i in range(len(self.parent.iluminacion)):
            self.listaIluminacion.AppendRows(1)
            self.listaIluminacion.SetCellValue(i, 0, self.parent.iluminacion[i][0])
            self.listaIluminacion.SetReadOnly(i, 0)
            self.listaIluminacion.ampliaDiccionarioTraduccion({_(self.parent.iluminacion[i][-1]): self.parent.iluminacion[i][-1]})
            self.listaIluminacion.SetCellValue(i, 1, self.parent.iluminacion[i][-1])
            self.listaIluminacion.SetReadOnly(i, 1)
            self.listaIluminacion.SetCellValue(i, 2, str(self.parent.iluminacion[i][5]))
            self.listaIluminacion.SetReadOnly(i, 2)
            self.listaIluminacion.SetCellEditor(i, 3, opcionesZonaRepresentacion)
            self.listaIluminacion.SetCellValue(i, 3, self.parent.iluminacion[i][6])
            self.listaIluminacion.SetReadOnly(i, 3)
            if self.parent.iluminacion[i][6] == True:
                self.listaIluminacion.SetCellEditor(i, 4, opcionesAcividad2)
            else:
                self.listaIluminacion.SetCellEditor(i, 4, opcionesAcividad1)
            self.listaIluminacion.SetCellValue(i, 4, self.parent.iluminacion[i][7])
            self.listaIluminacion.ampliaDiccionarioTraduccion({_(self.parent.iluminacion[i][8]): self.parent.iluminacion[i][8]})
            self.listaIluminacion.SetCellValue(i, 5, self.parent.iluminacion[i][8])
            self.listaIluminacion.SetReadOnly(i, 5)
            try:
                potencia = round(float(self.parent.iluminacion[i][2]), 1)
            except:
                logging.info(u'Excepcion en: %s' % __name__)
                potencia = ''

            self.listaIluminacion.SetCellValue(i, 6, str(potencia))
            if 'Estimado' in self.parent.iluminacion[i][8]:
                self.listaIluminacion.SetReadOnly(i, 6)
                self.listaIluminacion.SetReadOnly(i, 7)
            self.listaIluminacion.SetCellValue(i, 7, self.parent.iluminacion[i][9][1])

        self.listaIluminacion.AutoSizeColumns()

    def cargarListaRenovables(self):
        """
        Metodo: cargarListaRenovables
        
        
        """
        try:
            self.listaRenovables.DeleteRows(0, self.listaRenovables.GetNumberRows())
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        opcionesTipoCombustible = MiChoiceGrid(choices=listadoCombustibles)
        self.listaRenovables.ampliaDiccionarioTraduccion(opcionesTipoCombustible.traduccion)
        for i in range(len(self.parent.contribuciones)):
            self.listaRenovables.AppendRows(1)
            self.listaRenovables.SetCellValue(i, 0, self.parent.contribuciones[i][0])
            self.listaRenovables.SetReadOnly(i, 0)
            self.listaRenovables.ampliaDiccionarioTraduccion({_(self.parent.contribuciones[i][-1]): self.parent.contribuciones[i][-1]})
            self.listaRenovables.SetCellValue(i, 1, self.parent.contribuciones[i][-1])
            self.listaRenovables.SetReadOnly(i, 1)
            self.listaRenovables.SetCellValue(i, 2, self.parent.contribuciones[i][2][0])
            self.listaRenovables.SetCellValue(i, 3, self.parent.contribuciones[i][2][1])
            self.listaRenovables.SetCellValue(i, 4, self.parent.contribuciones[i][2][2])
            self.listaRenovables.SetCellValue(i, 5, self.parent.contribuciones[i][3][0])
            self.listaRenovables.SetCellValue(i, 6, self.parent.contribuciones[i][3][1])
            self.listaRenovables.SetCellValue(i, 7, self.parent.contribuciones[i][3][2])
            self.listaRenovables.SetCellValue(i, 8, self.parent.contribuciones[i][3][3])
            self.listaRenovables.SetCellValue(i, 9, self.parent.contribuciones[i][3][4])
            self.listaRenovables.SetCellEditor(i, 10, opcionesTipoCombustible)
            if self.parent.contribuciones[i][3][5] != '':
                combustible = getTraduccion(listado=listadoCombustibles, elemento=self.parent.contribuciones[i][3][5])
                self.listaRenovables.SetCellValue(i, 10, combustible)

        self.listaRenovables.AutoSizeColumns()

    def cargaVista(self):
        """
        Metodo: cargaVista
        
        
        """
        self.cargarListaIluminacion()
        self.cargarListaAirePrimario()
        self.cargarListaGT()
        self.cargarListaACS()
        self.cargarListaCalefaccion()
        self.cargarListaRefrigeracion()
        self.cargarListaRenovables()

    def confirmacionUsuario(self):
        """
        Metodo: confirmacionUsuario
        
        
        """
        deseaReemplazar = dialogoConfirma.Dialog1(self, _(u'\xbfDesea guardar los cambios?'))
        deseaReemplazar.ShowModal()
        if deseaReemplazar.dev == True:
            return True
        else:
            self.cambios = False
            return False

    def onGuardarBoton(self, event):
        """
        Metodo: onGuardarBoton
        
            ARGUMENTOS:
                    event:
        
        """
        if self.confirmacionUsuario():
            self.realizaCambios()
        else:
            self.cargaVista()

    def realizaCambios(self):
        """
        Metodo: realizaCambios
        
        """
        listaErrores = u''
        if self.listaACS.IsShown():
            for i in range(self.listaACS.GetNumberRows()):
                listaErrores += Comprueba(self.listaACS.GetCellValue(i, 0), 1, listaErrores, u'nombre %s' % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaACS.GetCellValue(i, 1), 1, listaErrores, u'tipo de equipo %s' % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaACS.GetCellValue(i, 2), 1, listaErrores, u'definici\xf3n %s' % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaACS.GetCellValue(i, 3), 1, listaErrores, u'tipo generador %s' % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaACS.GetCellValue(i, 4), 1, listaErrores, u'tipo combustible %s' % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaACS.GetCellValue(i, 5), 2, listaErrores, u'rendimiento estacional %s' % (i + 1), 0).ErrorDevuelto
                listaErrores += Comprueba2(self.listaACS.GetCellValue(i, 6), 2, listaErrores, u'm2 cubiertos %s' % (i + 1), 0).ErrorDevuelto
                listaErrores += Comprueba2(self.listaACS.GetCellValue(i, 7), 2, listaErrores, u'demanda cubierta %s' % (i + 1), 0).ErrorDevuelto

            if listaErrores != u'':
                wx.MessageBox(_(u'Revise los siguientes campos:\n') + listaErrores, _(u'Aviso'))
                return False
            self.actualizaACS()
        elif self.listaCalefaccion.IsShown():
            for i in range(self.listaCalefaccion.GetNumberRows()):
                listaErrores += Comprueba(self.listaCalefaccion.GetCellValue(i, 0), 1, listaErrores, u'nombre %s' % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaCalefaccion.GetCellValue(i, 1), 1, listaErrores, u'tipo de equipo %s' % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaCalefaccion.GetCellValue(i, 2), 1, listaErrores, u'definici\xf3n %s' % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaCalefaccion.GetCellValue(i, 3), 1, listaErrores, u'tipo generador %s' % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaCalefaccion.GetCellValue(i, 4), 1, listaErrores, u'tipo combustible %s' % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaCalefaccion.GetCellValue(i, 5), 2, listaErrores, u'rendimiento estacional %s' % (i + 1), 0).ErrorDevuelto
                listaErrores += Comprueba2(self.listaCalefaccion.GetCellValue(i, 6), 2, listaErrores, u'm2 cubiertos %s' % (i + 1), 0).ErrorDevuelto
                listaErrores += Comprueba2(self.listaCalefaccion.GetCellValue(i, 7), 2, listaErrores, u'demanda cubierta %s' % (i + 1), 0).ErrorDevuelto

            if listaErrores != u'':
                wx.MessageBox(_(u'Revise los siguientes campos:\n') + listaErrores, _(u'Aviso'))
                return False
            self.actualizaCalefaccion()
        elif self.listaRefrigeracion.IsShown():
            for i in range(self.listaRefrigeracion.GetNumberRows()):
                listaErrores += Comprueba(self.listaRefrigeracion.GetCellValue(i, 0), 1, listaErrores, _(u'nombre %s') % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaRefrigeracion.GetCellValue(i, 1), 1, listaErrores, _(u'tipo de equipo %s') % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaRefrigeracion.GetCellValue(i, 2), 1, listaErrores, _(u'definici\xf3n %s') % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaRefrigeracion.GetCellValue(i, 3), 1, listaErrores, _(u'tipo generador %s') % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaRefrigeracion.GetCellValue(i, 4), 1, listaErrores, _(u'tipo combustible %s') % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaRefrigeracion.GetCellValue(i, 5), 2, listaErrores, _(u'rendimiento estacional %s') % (i + 1), 0).ErrorDevuelto
                listaErrores += Comprueba2(self.listaRefrigeracion.GetCellValue(i, 6), 2, listaErrores, _(u'm2 cubiertos %s') % (i + 1), 0).ErrorDevuelto
                listaErrores += Comprueba2(self.listaRefrigeracion.GetCellValue(i, 7), 2, listaErrores, _(u'demanda cubierta %s') % (i + 1), 0).ErrorDevuelto

            if listaErrores != u'':
                wx.MessageBox(_(u'Revise los siguientes campos:\n') + listaErrores, _(u'Aviso'))
                return False
            self.actualizaRefrigeracion()
        elif self.listaRenovables.IsShown():
            self.actualizaRenovables()
        elif self.listaIluminacion.IsShown():
            for i in range(self.listaIluminacion.GetNumberRows()):
                listaErrores += Comprueba(self.listaIluminacion.GetCellValue(i, 0), 1, listaErrores, _(u'nombre %s') % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaIluminacion.GetCellValue(i, 1), 1, listaErrores, _(u'zona %s') % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaIluminacion.GetCellValue(i, 2), 2, listaErrores, _(u'superficie %s') % (i + 1), 0).ErrorDevuelto
                listaErrores += Comprueba(self.listaIluminacion.GetCellValue(i, 3), 1, listaErrores, _(u'zona representaci\xf3n %s') % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaIluminacion.GetCellValue(i, 4), 1, listaErrores, _(u'actividad %s') % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaIluminacion.GetCellValue(i, 5), 1, listaErrores, _(u'definici\xf3n %s') % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaIluminacion.GetCellValue(i, 6), 2, listaErrores, _(u'potencia %s') % (i + 1), 0).ErrorDevuelto
                listaErrores += Comprueba(self.listaIluminacion.GetCellValue(i, 7), 2, listaErrores, _(u'iluminancia %s') % (i + 1), 0).ErrorDevuelto

            if listaErrores != u'':
                wx.MessageBox(_(u'Revise los siguientes campos:\n') + listaErrores, _(u'Aviso'))
                return False
            self.actualizaIluminacion()
        elif self.listaAirePrimario.IsShown():
            for i in range(self.listaAirePrimario.GetNumberRows()):
                listaErrores += Comprueba(self.listaAirePrimario.GetCellValue(i, 0), 1, listaErrores, _(u'nombre %s') % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaAirePrimario.GetCellValue(i, 1), 1, listaErrores, _(u'zona %s') % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaAirePrimario.GetCellValue(i, 2), 2, listaErrores, _(u'caudal de ventilaci\xf3n %s') % (i + 1), 0).ErrorDevuelto
                listaErrores += Comprueba(self.listaAirePrimario.GetCellValue(i, 3), 1, listaErrores, _(u'recuperaci\xf3n de calor %s') % (i + 1)).ErrorDevuelto
                if self.listaAirePrimario.GetCellValue(i, 3) == True:
                    listaErrores += Comprueba(self.listaAirePrimario.GetCellValue(i, 4), 2, listaErrores, _(u'rendimiento del recuperador %s') % (i + 1), 0).ErrorDevuelto

            if listaErrores != u'':
                wx.MessageBox(_(u'Revise los siguientes campos:\n') + listaErrores, _(u'Aviso'))
                return False
            self.actualizaAirePrimario()
        elif self.listaGT.IsShown():
            for i in range(self.listaGT.GetNumberRows()):
                listaErrores += Comprueba(self.listaGT.GetCellValue(i, 0), 1, listaErrores, _(u'nombre %s') % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaGT.GetCellValue(i, 1), 1, listaErrores, _(u'zona %s') % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaGT.GetCellValue(i, 2), 1, listaErrores, _(u'tipo de equipo %s') % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaGT.GetCellValue(i, 3), 1, listaErrores, _(u'servicio %s') % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaGT.GetCellValue(i, 4), 1, listaErrores, _(u'definici\xf3n %s') % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaGT.GetCellValue(i, 5), 2, listaErrores, _(u'consumo anual %s') % (i + 1), 0).ErrorDevuelto

            if listaErrores != u'':
                wx.MessageBox(_(u'Revise los siguientes campos:\n') + listaErrores, _(u'Aviso'))
                return False
            self.actualizaGT()
        self.cambios = False
        return True

    def actualizaGT(self):
        """
        Metodo: actualizaGT
        
        """
        cnt = 0
        for i in range(len(self.parent.ventiladores)):
            if self.parent.ventiladores[i][6] == 0:
                self.parent.ventiladores[i][2] = self.listaGT.GetCellValue(i, 5)
            cnt += 1

        for i in range(len(self.parent.bombas)):
            if self.parent.bombas[i][6] == 0:
                self.parent.bombas[i][2] = self.listaGT.GetCellValue(cnt, 5)
            cnt += 1

        for i in range(len(self.parent.torresRefrigeracion)):
            if self.parent.torresRefrigeracion[i][6] == 0:
                self.parent.torresRefrigeracion[i][2] = self.listaGT.GetCellValue(cnt, 5)
            cnt += 1

    def actualizaAirePrimario(self):
        """
        Metodo: actualizaAirePrimario
        
        """
        for i in range(len(self.parent.ventilacion)):
            self.parent.ventilacion[i][2] = self.listaAirePrimario.GetCellValue(i, 2)
            self.parent.ventilacion[i][3] = self.listaAirePrimario.GetCellValue(i, 3)
            self.parent.ventilacion[i][4] = self.listaAirePrimario.GetCellValue(i, 4)

    def actualizaIluminacion(self):
        """
        Metodo: actualizaIluminacion
        
        """
        for i in range(len(self.parent.iluminacion)):
            self.parent.iluminacion[i][7] = self.listaIluminacion.GetCellValue(i, 4)
            if u'Conocido' in self.listaIluminacion.GetCellValue(i, 5):
                potencia = self.listaIluminacion.GetCellValue(i, 6)
                self.parent.iluminacion[i][2] = float(potencia)
                self.parent.iluminacion[i][9][0] = potencia
            iluminancia = self.listaIluminacion.GetCellValue(i, 7)
            self.parent.iluminacion[i][9][1] = iluminancia

    def actualizaRenovables(self):
        """
        Metodo: actualizaRenovables
        
        
        """
        for i in range(len(self.parent.contribuciones)):
            datosRenovable = []
            datosRenovable.append(self.listaRenovables.GetCellValue(i, 2))
            datosRenovable.append(self.listaRenovables.GetCellValue(i, 3))
            datosRenovable.append(self.listaRenovables.GetCellValue(i, 4))
            reno = False
            for j in datosRenovable:
                if j != '':
                    reno = True
                    break

            datosRenovable.append(False)
            datosElectricidad = []
            datosElectricidad.append(self.listaRenovables.GetCellValue(i, 5))
            datosElectricidad.append(self.listaRenovables.GetCellValue(i, 6))
            datosElectricidad.append(self.listaRenovables.GetCellValue(i, 7))
            datosElectricidad.append(self.listaRenovables.GetCellValue(i, 8))
            datosElectricidad.append(self.listaRenovables.GetCellValue(i, 9))
            datosElectricidad.append(self.listaRenovables.GetCellValue(i, 10))
            elec = False
            for j in datosElectricidad:
                if j != '':
                    elec = True
                    break

            self.parent.contribuciones[i][2] = datosRenovable
            self.parent.contribuciones[i][3] = datosElectricidad
            self.parent.contribuciones[i][4] = [reno, elec]

    def actualizaRefrigeracion(self):
        """
        Metodo: actualizaRefrigeracion
        
        """
        cnt = 0
        for i in range(len(self.parent.refrigeracion)):
            if self.listaRefrigeracion.GetCellValue(i, 2) == 'Conocido':
                if 'Conocido' in self.parent.refrigeracion[i][6]:
                    self.parent.refrigeracion[i][3] = self.listaRefrigeracion.GetCellValue(i, 3)
                    self.parent.refrigeracion[i][4] = self.listaRefrigeracion.GetCellValue(i, 4)
                    self.parent.refrigeracion[i][7][2] = self.listaRefrigeracion.GetCellValue(i, 5)
                    self.parent.refrigeracion[i][2][2] = self.listaRefrigeracion.GetCellValue(i, 5)
                    self.parent.refrigeracion[i][5][2][0] = self.listaRefrigeracion.GetCellValue(i, 6)
                    self.parent.refrigeracion[i][5][2][1] = self.listaRefrigeracion.GetCellValue(i, 7)
                else:
                    nuevo = []
                    nuevo.append(self.listaRefrigeracion.GetCellValue(i, 0))
                    nuevo.append('refrigeracion')
                    nuevo.append(['', '', float(self.listaRefrigeracion.GetCellValue(i, 5))])
                    nuevo.append(self.listaRefrigeracion.GetCellValue(i, 3))
                    nuevo.append(self.listaRefrigeracion.GetCellValue(i, 4))
                    nuevo.append([['', ''], ['', ''], [self.listaRefrigeracion.GetCellValue(i, 6), self.listaRefrigeracion.GetCellValue(i, 7)]])
                    nuevo.append(u'Conocido (Ensayado/justificado)')
                    datosConcretos = []
                    datosConcretos.append('')
                    datosConcretos.append('')
                    datosConcretos.append(self.listaRefrigeracion.GetCellValue(i, 5))
                    nuevo.append(datosConcretos)
                    nuevo.append(self.parent.refrigeracion[i][-1])
                    self.parent.refrigeracion[i] = nuevo
            else:
                self.parent.refrigeracion[i][3] = self.listaRefrigeracion.GetCellValue(i, 3)
                self.parent.refrigeracion[i][4] = self.listaRefrigeracion.GetCellValue(i, 4)
                self.parent.refrigeracion[i][5][2][0] = self.listaRefrigeracion.GetCellValue(i, 6)
                self.parent.refrigeracion[i][5][2][1] = self.listaRefrigeracion.GetCellValue(i, 7)
            cnt += 1

        for i in range(len(self.parent.climatizacion)):
            if self.listaRefrigeracion.GetCellValue(i, 2) == 'Conocido':
                if 'Conocido' in self.parent.climatizacion[i][6]:
                    self.parent.climatizacion[i][3] = self.listaRefrigeracion.GetCellValue(cnt, 3)
                    self.parent.climatizacion[i][4] = self.listaRefrigeracion.GetCellValue(cnt, 4)
                    self.parent.climatizacion[i][7][2] = self.listaRefrigeracion.GetCellValue(cnt, 5)
                    self.parent.climatizacion[i][2][2] = self.listaRefrigeracion.GetCellValue(cnt, 5)
                    self.parent.climatizacion[i][5][2][0] = self.listaRefrigeracion.GetCellValue(cnt, 6)
                    self.parent.climatizacion[i][5][2][1] = self.listaRefrigeracion.GetCellValue(cnt, 7)
                else:
                    nuevo = []
                    nuevo.append(self.listaRefrigeracion.GetCellValue(cnt, 0))
                    nuevo.append('climatizacion')
                    nuevo.append([self.parent.climatizacion[i][2][0], self.parent.climatizacion[i][2][1], float(self.listaRefrigeracion.GetCellValue(cnt, 5))])
                    nuevo.append(self.listaRefrigeracion.GetCellValue(cnt, 3))
                    nuevo.append(self.listaRefrigeracion.GetCellValue(cnt, 4))
                    nuevo.append([[self.parent.climatizacion[i][5][0][0], self.parent.climatizacion[i][5][0][1]], [self.parent.climatizacion[i][5][1][0], self.parent.climatizacion[i][5][1][1]], [self.listaRefrigeracion.GetCellValue(cnt, 6), self.listaRefrigeracion.GetCellValue(cnt, 7)]])
                    nuevo.append(u'Conocido (Ensayado/justificado)')
                    datosConcretos = []
                    datosConcretos.append(str(self.parent.climatizacion[i][2][0]))
                    datosConcretos.append(str(self.parent.climatizacion[i][2][1]))
                    datosConcretos.append(self.listaRefrigeracion.GetCellValue(cnt, 5))
                    nuevo.append(datosConcretos)
                    nuevo.append(self.parent.climatizacion[i][8])
                    nuevo.append(self.parent.climatizacion[i][-1])
                    self.parent.climatizacion[i] = nuevo
            else:
                self.parent.climatizacion[i][3] = self.listaRefrigeracion.GetCellValue(cnt, 3)
                self.parent.climatizacion[i][4] = self.listaRefrigeracion.GetCellValue(cnt, 4)
                self.parent.climatizacion[i][5][2][0] = self.listaRefrigeracion.GetCellValue(cnt, 6)
                self.parent.climatizacion[i][5][2][1] = self.listaRefrigeracion.GetCellValue(cnt, 7)
            cnt += 1

        for i in range(len(self.parent.mixto3)):
            if self.listaRefrigeracion.GetCellValue(cnt, 2) == 'Conocido':
                if 'Conocido' in self.parent.mixto3[i][6]:
                    self.parent.mixto3[i][3] = self.listaRefrigeracion.GetCellValue(cnt, 3)
                    self.parent.mixto3[i][4] = self.listaRefrigeracion.GetCellValue(cnt, 4)
                    self.parent.mixto3[i][7][2] = self.listaRefrigeracion.GetCellValue(cnt, 5)
                    self.parent.mixto3[i][2][2] = self.listaRefrigeracion.GetCellValue(cnt, 5)
                    self.parent.mixto3[i][5][2][0] = self.listaRefrigeracion.GetCellValue(cnt, 6)
                    self.parent.mixto3[i][5][2][1] = self.listaRefrigeracion.GetCellValue(cnt, 7)
                else:
                    nuevo = []
                    nuevo.append(self.listaRefrigeracion.GetCellValue(cnt, 0))
                    nuevo.append('mixto3')
                    nuevo.append([self.parent.mixto3[i][2][0], self.parent.mixto3[i][2][1], float(self.listaRefrigeracion.GetCellValue(cnt, 5))])
                    nuevo.append(self.listaRefrigeracion.GetCellValue(cnt, 3))
                    nuevo.append(self.listaRefrigeracion.GetCellValue(cnt, 4))
                    nuevo.append([[self.parent.mixto3[i][5][0][0], self.parent.mixto3[i][5][0][1]], [self.parent.mixto3[i][5][1][0], self.parent.mixto3[i][5][1][1]], [self.listaRefrigeracion.GetCellValue(cnt, 6), self.listaRefrigeracion.GetCellValue(cnt, 7)]])
                    nuevo.append(u'Conocido (Ensayado/justificado)')
                    datosConcretos = []
                    datosConcretos.append(str(self.parent.mixto3[i][2][0]))
                    datosConcretos.append(str(self.parent.mixto3[i][2][1]))
                    datosConcretos.append(self.listaRefrigeracion.GetCellValue(cnt, 5))
                    nuevo.append(datosConcretos)
                    nuevo.append(self.parent.mixto3[i][8])
                    nuevo.append(self.parent.mixto3[i][-1])
                    self.parent.mixto3[i] = nuevo
            else:
                self.parent.mixto3[i][3] = self.listaRefrigeracion.GetCellValue(cnt, 3)
                self.parent.mixto3[i][4] = self.listaRefrigeracion.GetCellValue(cnt, 4)
                self.parent.mixto3[i][5][2][0] = self.listaRefrigeracion.GetCellValue(cnt, 6)
                self.parent.mixto3[i][5][2][1] = self.listaRefrigeracion.GetCellValue(cnt, 7)
            cnt += 1

    def actualizaCalefaccion(self):
        """
        Metodo: actualizaCalefaccion
        
        """
        cnt = 0
        for i in range(len(self.parent.calefaccion)):
            if self.listaCalefaccion.GetCellValue(i, 2) == 'Conocido':
                if 'Conocido' in self.parent.calefaccion[i][6]:
                    self.parent.calefaccion[i][3] = self.listaCalefaccion.GetCellValue(i, 3)
                    self.parent.calefaccion[i][4] = self.listaCalefaccion.GetCellValue(i, 4)
                    self.parent.calefaccion[i][2][1] = self.listaCalefaccion.GetCellValue(i, 5)
                    self.parent.calefaccion[i][5][1][0] = self.listaCalefaccion.GetCellValue(i, 6)
                    self.parent.calefaccion[i][5][1][1] = self.listaCalefaccion.GetCellValue(i, 7)
                    if self.listaCalefaccion.GetCellValue(i, 3) in (u'Caldera Est\xe1ndar', u'Caldera Condensaci\xf3n', u'Caldera Baja Temperatura') and self.listaCalefaccion.GetCellValue(i, 4) != u'Electricidad':
                        self.parent.calefaccion[i][7] = [self.listaCalefaccion.GetCellValue(i, 5)]
                    else:
                        self.parent.calefaccion[i][7] = ['', self.listaCalefaccion.GetCellValue(i, 5), '']
                else:
                    nuevo = []
                    nuevo.append(self.listaCalefaccion.GetCellValue(i, 0))
                    nuevo.append('calefaccion')
                    nuevo.append(['', float(self.listaCalefaccion.GetCellValue(i, 5)), ''])
                    nuevo.append(self.listaCalefaccion.GetCellValue(i, 3))
                    nuevo.append(self.listaCalefaccion.GetCellValue(i, 4))
                    nuevo.append([['', ''], [self.listaCalefaccion.GetCellValue(i, 6), self.listaCalefaccion.GetCellValue(i, 7)], ['', '']])
                    nuevo.append(u'Conocido (Ensayado/justificado)')
                    datosConcretos = []
                    if self.listaCalefaccion.GetCellValue(i, 3) in (u'Caldera Est\xe1ndar', u'Caldera Condensaci\xf3n', u'Caldera Baja Temperatura') and self.listaCalefaccion.GetCellValue(i, 4) != u'Electricidad':
                        datosConcretos = [self.listaCalefaccion.GetCellValue(i, 5)]
                    else:
                        datosConcretos = ['', self.listaCalefaccion.GetCellValue(i, 5), '']
                    datosConcretos.append(self.listaCalefaccion.GetCellValue(i, 5))
                    nuevo.append(datosConcretos)
                    nuevo.append(self.parent.calefaccion[i][-1])
                    self.parent.calefaccion[i] = nuevo
            else:
                self.parent.calefaccion[i][5][1][0] = self.listaCalefaccion.GetCellValue(i, 6)
                self.parent.calefaccion[i][5][1][1] = self.listaCalefaccion.GetCellValue(i, 7)
            cnt += 1

        for i in range(len(self.parent.climatizacion)):
            if self.listaCalefaccion.GetCellValue(i, 2) == 'Conocido':
                if 'Conocido' in self.parent.climatizacion[i][6]:
                    self.parent.climatizacion[i][3] = self.listaCalefaccion.GetCellValue(cnt, 3)
                    self.parent.climatizacion[i][4] = self.listaCalefaccion.GetCellValue(cnt, 4)
                    self.parent.climatizacion[i][7][1] = self.listaCalefaccion.GetCellValue(cnt, 5)
                    self.parent.climatizacion[i][2][1] = self.listaCalefaccion.GetCellValue(cnt, 5)
                    self.parent.climatizacion[i][5][1][0] = self.listaCalefaccion.GetCellValue(cnt, 6)
                    self.parent.climatizacion[i][5][1][1] = self.listaCalefaccion.GetCellValue(cnt, 7)
                else:
                    nuevo = []
                    nuevo.append(self.listaCalefaccion.GetCellValue(cnt, 0))
                    nuevo.append('climatizacion')
                    nuevo.append([self.parent.climatizacion[i][2][0], float(self.listaCalefaccion.GetCellValue(cnt, 5)), self.parent.climatizacion[i][2][2]])
                    nuevo.append(self.listaCalefaccion.GetCellValue(cnt, 3))
                    nuevo.append(self.listaCalefaccion.GetCellValue(cnt, 4))
                    nuevo.append([[self.parent.climatizacion[i][5][0][0], self.parent.climatizacion[i][5][0][1]], [self.listaCalefaccion.GetCellValue(cnt, 6), self.listaCalefaccion.GetCellValue(cnt, 7)], [self.parent.climatizacion[i][5][2][0], self.parent.climatizacion[i][5][2][1]]])
                    nuevo.append(u'Conocido (Ensayado/justificado)')
                    datosConcretos = []
                    datosConcretos.append(str(self.parent.climatizacion[i][2][0]))
                    datosConcretos.append(self.listaCalefaccion.GetCellValue(cnt, 5))
                    datosConcretos.append(str(self.parent.climatizacion[i][2][2]))
                    nuevo.append(datosConcretos)
                    nuevo.append(self.parent.climatizacion[i][8])
                    nuevo.append(self.parent.climatizacion[i][-1])
                    self.parent.climatizacion[i] = nuevo
            else:
                self.parent.climatizacion[i][5][1][0] = self.listaCalefaccion.GetCellValue(cnt, 6)
                self.parent.climatizacion[i][5][1][1] = self.listaCalefaccion.GetCellValue(cnt, 7)
            cnt += 1

        for i in range(len(self.parent.mixto2)):
            if self.listaCalefaccion.GetCellValue(cnt, 2) == 'Conocido':
                if 'Conocido' in self.parent.mixto2[i][6]:
                    self.parent.mixto2[i][3] = self.listaCalefaccion.GetCellValue(cnt, 3)
                    self.parent.mixto2[i][4] = self.listaCalefaccion.GetCellValue(cnt, 4)
                    self.parent.mixto2[i][2][1] = self.listaCalefaccion.GetCellValue(cnt, 5)
                    self.parent.mixto2[i][5][1][0] = self.listaCalefaccion.GetCellValue(cnt, 6)
                    self.parent.mixto2[i][5][1][1] = self.listaCalefaccion.GetCellValue(cnt, 7)
                    self.parent.mixto2[i][7] = [str(self.parent.mixto2[i][2][0]), self.listaCalefaccion.GetCellValue(cnt, 5), '']
                else:
                    nuevo = []
                    nuevo.append(self.listaCalefaccion.GetCellValue(cnt, 0))
                    nuevo.append('mixto2')
                    nuevo.append([self.parent.mixto2[i][2][0], float(self.listaCalefaccion.GetCellValue(cnt, 5)), self.parent.mixto2[i][2][2]])
                    nuevo.append(self.listaCalefaccion.GetCellValue(cnt, 3))
                    nuevo.append(self.listaCalefaccion.GetCellValue(cnt, 4))
                    nuevo.append([[self.parent.mixto2[i][5][0][0], self.parent.mixto2[i][5][0][1]], [self.listaCalefaccion.GetCellValue(cnt, 6), self.listaCalefaccion.GetCellValue(cnt, 7)], [self.parent.mixto2[i][5][2][0], self.parent.mixto2[i][5][2][1]]])
                    nuevo.append(u'Conocido (Ensayado/justificado)')
                    datosConcretos = []
                    datosConcretos = [str(self.parent.mixto2[i][2][0]), self.listaCalefaccion.GetCellValue(cnt, 5), '']
                    nuevo.append(datosConcretos)
                    nuevo.append(self.parent.mixto2[i][8])
                    nuevo.append(self.parent.mixto2[i][-1])
                    self.parent.mixto2[i] = nuevo
            else:
                self.parent.mixto2[i][5][1][0] = self.listaCalefaccion.GetCellValue(cnt, 6)
                self.parent.mixto2[i][5][1][1] = self.listaCalefaccion.GetCellValue(cnt, 7)
            cnt += 1

        for i in range(len(self.parent.mixto3)):
            if self.listaCalefaccion.GetCellValue(cnt, 2) == 'Conocido':
                if 'Conocido' in self.parent.mixto3[i][6]:
                    self.parent.mixto3[i][3] = self.listaCalefaccion.GetCellValue(cnt, 3)
                    self.parent.mixto3[i][4] = self.listaCalefaccion.GetCellValue(cnt, 4)
                    self.parent.mixto3[i][7][1] = self.listaCalefaccion.GetCellValue(cnt, 5)
                    self.parent.mixto3[i][2][1] = self.listaCalefaccion.GetCellValue(cnt, 5)
                    self.parent.mixto3[i][5][1][0] = self.listaCalefaccion.GetCellValue(cnt, 6)
                    self.parent.mixto3[i][5][1][1] = self.listaCalefaccion.GetCellValue(cnt, 7)
                else:
                    nuevo = []
                    nuevo.append(self.listaCalefaccion.GetCellValue(cnt, 0))
                    nuevo.append('mixto3')
                    nuevo.append([self.parent.mixto3[i][2][0], float(self.listaCalefaccion.GetCellValue(cnt, 5)), self.parent.mixto3[i][2][2]])
                    nuevo.append(self.listaCalefaccion.GetCellValue(cnt, 3))
                    nuevo.append(self.listaCalefaccion.GetCellValue(cnt, 4))
                    nuevo.append([[self.parent.mixto3[i][5][0][0], self.parent.mixto3[i][5][0][1]], [self.listaCalefaccion.GetCellValue(cnt, 6), self.listaCalefaccion.GetCellValue(cnt, 7)], [self.parent.mixto3[i][5][2][0], self.parent.mixto3[i][5][2][1]]])
                    nuevo.append(u'Conocido (Ensayado/justificado)')
                    datosConcretos = []
                    datosConcretos.append(str(self.parent.mixto3[i][2][0]))
                    datosConcretos.append(self.listaCalefaccion.GetCellValue(cnt, 5))
                    datosConcretos.append(str(self.parent.mixto3[i][2][2]))
                    nuevo.append(datosConcretos)
                    nuevo.append(self.parent.mixto3[i][8])
                    nuevo.append(self.parent.mixto3[i][-1])
                    self.parent.mixto3[i] = nuevo
            else:
                self.parent.mixto3[i][5][1][0] = self.listaCalefaccion.GetCellValue(cnt, 6)
                self.parent.mixto3[i][5][1][1] = self.listaCalefaccion.GetCellValue(cnt, 7)
            cnt += 1

    def actualizaACS(self):
        """
        Metodo: actualizaACS
        
        """
        cnt = 0
        for i in range(len(self.parent.ACS)):
            if self.listaACS.GetCellValue(i, 2) == 'Conocido':
                if 'Conocido' in self.parent.ACS[i][6]:
                    self.parent.ACS[i][3] = self.listaACS.GetCellValue(i, 3)
                    self.parent.ACS[i][4] = self.listaACS.GetCellValue(i, 4)
                    self.parent.ACS[i][2][0] = self.listaACS.GetCellValue(i, 5)
                    self.parent.ACS[i][5][0][0] = self.listaACS.GetCellValue(i, 6)
                    self.parent.ACS[i][5][0][1] = self.listaACS.GetCellValue(i, 7)
                    if self.listaACS.GetCellValue(i, 3) in (u'Caldera Est\xe1ndar', u'Caldera Condensaci\xf3n', u'Caldera Baja Temperatura') and self.listaACS.GetCellValue(i, 4) != u'Electricidad':
                        self.parent.ACS[i][7] = [self.listaACS.GetCellValue(i, 5)]
                    else:
                        self.parent.ACS[i][7] = [self.listaACS.GetCellValue(i, 5), '', '']
                else:
                    nuevo = []
                    nuevo.append(self.listaACS.GetCellValue(i, 0))
                    nuevo.append('ACS')
                    nuevo.append([float(self.listaACS.GetCellValue(i, 5)), '', ''])
                    nuevo.append(self.listaACS.GetCellValue(i, 3))
                    nuevo.append(self.listaACS.GetCellValue(i, 4))
                    nuevo.append([[self.listaACS.GetCellValue(i, 6), self.listaACS.GetCellValue(i, 7)], ['', ''], ['', '']])
                    nuevo.append(u'Conocido (Ensayado/justificado)')
                    datosConcretos = []
                    if self.listaACS.GetCellValue(i, 3) in (u'Caldera Est\xe1ndar', u'Caldera Condensaci\xf3n', u'Caldera Baja Temperatura') and self.listaACS.GetCellValue(i, 4) != u'Electricidad':
                        datosConcretos = [self.listaACS.GetCellValue(i, 5)]
                    else:
                        datosConcretos = [self.listaACS.GetCellValue(i, 5), '', '']
                    datosConcretos.append(self.listaACS.GetCellValue(i, 5))
                    nuevo.append(datosConcretos)
                    nuevo.append(self.parent.ACS[i][8])
                    nuevo.append(self.parent.ACS[i][-1])
                    self.parent.ACS[i] = nuevo
            else:
                self.parent.ACS[i][3] = self.listaACS.GetCellValue(i, 3)
                self.parent.ACS[i][4] = self.listaACS.GetCellValue(i, 4)
                self.parent.ACS[i][5][0][0] = self.listaACS.GetCellValue(i, 6)
                self.parent.ACS[i][5][0][1] = self.listaACS.GetCellValue(i, 7)
            cnt += 1

        for i in range(len(self.parent.mixto2)):
            if self.listaACS.GetCellValue(cnt, 2) == 'Conocido':
                if 'Conocido' in self.parent.mixto2[i][6]:
                    self.parent.mixto2[i][3] = self.listaACS.GetCellValue(cnt, 3)
                    self.parent.mixto2[i][4] = self.listaACS.GetCellValue(cnt, 4)
                    self.parent.mixto2[i][2][0] = self.listaACS.GetCellValue(cnt, 5)
                    self.parent.mixto2[i][5][0][0] = self.listaACS.GetCellValue(cnt, 6)
                    self.parent.mixto2[i][5][0][1] = self.listaACS.GetCellValue(cnt, 7)
                    self.parent.mixto2[i][7] = [self.listaACS.GetCellValue(cnt, 5), str(self.parent.mixto2[i][2][1]), '']
                else:
                    nuevo = []
                    nuevo.append(self.listaACS.GetCellValue(cnt, 0))
                    nuevo.append('mixto2')
                    nuevo.append([float(self.listaACS.GetCellValue(cnt, 5)), self.parent.mixto2[i][2][1], self.parent.mixto2[i][2][2]])
                    nuevo.append(self.listaACS.GetCellValue(cnt, 3))
                    nuevo.append(self.listaACS.GetCellValue(cnt, 4))
                    nuevo.append([[self.listaACS.GetCellValue(cnt, 6), self.listaACS.GetCellValue(cnt, 7)], [self.parent.mixto2[i][5][1][0], self.parent.mixto2[i][5][1][1]], [self.parent.mixto2[i][5][2][0], self.parent.mixto2[i][5][2][1]]])
                    nuevo.append(u'Conocido (Ensayado/justificado)')
                    datosConcretos = []
                    datosConcretos = [self.listaACS.GetCellValue(cnt, 5), str(self.parent.mixto2[i][2][1]), '']
                    nuevo.append(datosConcretos)
                    nuevo.append(self.parent.mixto2[i][8])
                    nuevo.append(self.parent.mixto2[i][-1])
                    self.parent.mixto2[i] = nuevo
            else:
                self.parent.mixto2[i][5][0][0] = self.listaACS.GetCellValue(cnt, 6)
                self.parent.mixto2[i][5][0][1] = self.listaACS.GetCellValue(cnt, 7)
            cnt += 1

        for i in range(len(self.parent.mixto3)):
            if self.listaACS.GetCellValue(cnt, 2) == 'Conocido':
                if 'Conocido' in self.parent.mixto3[i][6]:
                    self.parent.mixto3[i][3] = self.listaACS.GetCellValue(cnt, 3)
                    self.parent.mixto3[i][4] = self.listaACS.GetCellValue(cnt, 4)
                    self.parent.mixto3[i][7][0] = self.listaACS.GetCellValue(cnt, 5)
                    self.parent.mixto3[i][2][0] = self.listaACS.GetCellValue(cnt, 5)
                    self.parent.mixto3[i][5][0][0] = self.listaACS.GetCellValue(cnt, 6)
                    self.parent.mixto3[i][5][0][1] = self.listaACS.GetCellValue(cnt, 7)
                else:
                    nuevo = []
                    nuevo.append(self.listaACS.GetCellValue(cnt, 0))
                    nuevo.append('mixto3')
                    nuevo.append([float(self.listaACS.GetCellValue(cnt, 5)), self.parent.mixto3[i][2][1], self.parent.mixto3[i][2][2]])
                    nuevo.append(self.listaACS.GetCellValue(cnt, 3))
                    nuevo.append(self.listaACS.GetCellValue(cnt, 4))
                    nuevo.append([[self.listaACS.GetCellValue(cnt, 6), self.listaACS.GetCellValue(cnt, 7)], [self.parent.mixto3[i][5][1][0], self.parent.mixto3[i][5][1][1]], [self.parent.mixto3[i][5][2][0], self.parent.mixto3[i][5][2][1]]])
                    nuevo.append(u'Conocido (Ensayado/justificado)')
                    datosConcretos = []
                    datosConcretos.append(self.listaACS.GetCellValue(cnt, 5))
                    datosConcretos.append(str(self.parent.mixto3[i][2][1]))
                    datosConcretos.append(str(self.parent.mixto3[i][2][2]))
                    nuevo.append(datosConcretos)
                    nuevo.append(self.parent.mixto3[i][8])
                    nuevo.append(self.parent.mixto3[i][-1])
                    self.parent.mixto3[i] = nuevo
            else:
                self.parent.mixto3[i][5][0][0] = self.listaACS.GetCellValue(cnt, 6)
                self.parent.mixto3[i][5][0][1] = self.listaACS.GetCellValue(cnt, 7)
            cnt += 1