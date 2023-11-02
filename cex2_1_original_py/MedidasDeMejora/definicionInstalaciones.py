# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: MedidasDeMejora\definicionInstalaciones.pyc
# Compiled at: 2014-12-23 16:19:43
"""
Modulo: definicionInstalaciones.py

"""
import wx, MedidasDeMejora.ventanaACS as ventanaACS, MedidasDeMejora.ventanaCalefaccion as ventanaCalefaccion, MedidasDeMejora.ventanaRefrigeracion as ventanaRefrigeracion, MedidasDeMejora.ventanaClimatizacion as ventanaClimatizacion, MedidasDeMejora.ventanaMixto2 as ventanaMixto2, MedidasDeMejora.ventanaMixto3 as ventanaMixto3, MedidasDeMejora.ventanaContribuciones as ventanaContribuciones, MedidasDeMejora.ventanaIluminacion as ventanaIluminacion, MedidasDeMejora.ventanaVentilacion as ventanaVentilacion, MedidasDeMejora.ventanaUniversal as ventanaUniversal, MedidasDeMejora.ventanaVentiladores as ventanaVentiladores, MedidasDeMejora.ventanaBombas as ventanaBombas, MedidasDeMejora.ventanaTorresRefrigeracion as ventanaTorresRefrigeracion
wxID_PANEL1, wxID_PANEL1BOTONANADIR, wxID_PANEL1BOTONBORRAR, wxID_PANEL1BOTONMODIFICAR, wxID_PANEL1INSTALACIONESTEXT, wxID_PANEL1LISTCTRL1, wxID_PANEL1TIPOINSTALACIONCHOICE, wxID_DIALOG1ACEPTARBOTON, wxID_DIALOG1CANCELARBOTON, wxID_STATICBOX1 = [ wx.NewId() for _init_ctrls in range(10) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo definicionInstalaciones.py

    """

    def _init_listCtrl1_Columns(self, parent):
        """
        Metodo: _init_listCtrl1_Columns

        ARGUMENTOS:
                parent:
        """
        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading=_('Nombre'), width=300)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading=_('Tipo de Medida'), width=300)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='', width=0)

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
        """
        wx.Dialog.__init__(self, id=wxID_PANEL1, name='', parent=prnt, pos=wx.Point(0, 0), size=wx.Size(770, 394), style=wx.DEFAULT_DIALOG_STYLE, title=_('Medidas de mejora de las instalaciones'))
        self.SetClientSize(wx.Size(770, 394))
        self.SetBackgroundColour('white')
        self.instalacionesText = wx.StaticText(id=wxID_PANEL1INSTALACIONESTEXT, label=_('Definir instalaciones del edificio con medidas de mejora incorporadas'), name='instalacionesText', parent=self, pos=wx.Point(15, 15), size=wx.Size(700, 16), style=0)
        self.instalacionesText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.instalacionesText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticBox1 = wx.StaticBox(id=wxID_STATICBOX1, label=_('Instalaciones definidas en el edificio mejorado'), name='staticBox1', parent=self, pos=wx.Point(15, 45), size=wx.Size(740, 296), style=0)
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.staticBox1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.listCtrl1 = wx.ListCtrl(id=wxID_PANEL1LISTCTRL1, name='listCtrl1', parent=self, pos=wx.Point(30, 70), size=wx.Size(605, 256), style=wx.LC_REPORT)
        self._init_listCtrl1_Columns(self.listCtrl1)
        self.botonAnadir = wx.Button(id=wxID_PANEL1BOTONANADIR, label=_('Añadir nueva'), name='botonAnadir', parent=self, pos=wx.Point(640, 100), size=wx.Size(100, 23), style=0)
        self.botonAnadir.Bind(wx.EVT_BUTTON, self.OnBotonAnadir, id=wxID_PANEL1BOTONANADIR)
        self.botonModificar = wx.Button(id=wxID_PANEL1BOTONMODIFICAR, label=_('Modificar'), name='botonModificar', parent=self, pos=wx.Point(640, 200), size=wx.Size(100, 23), style=0)
        self.botonModificar.Bind(wx.EVT_BUTTON, self.OnBotonModificar, id=wxID_PANEL1BOTONMODIFICAR)
        self.botonBorrar = wx.Button(id=wxID_PANEL1BOTONBORRAR, label=_('Borrar'), name='botonBorrar', parent=self, pos=wx.Point(640, 300), size=wx.Size(100, 23), style=0)
        self.botonBorrar.Bind(wx.EVT_BUTTON, self.OnBotonBorrar, id=wxID_PANEL1BOTONBORRAR)
        self.aceptarBoton = wx.Button(id=wxID_DIALOG1ACEPTARBOTON, label=_('Aceptar'), name='aceptarBoton', parent=self, pos=wx.Point(15, 356), size=wx.Size(75, 23), style=0)
        self.aceptarBoton.Bind(wx.EVT_BUTTON, self.onAceptarBoton, id=wxID_DIALOG1ACEPTARBOTON)
        self.cancelarBoton = wx.Button(id=wxID_DIALOG1CANCELARBOTON, label=_('Cancelar'), name='cancelarBoton', parent=self, pos=wx.Point(105, 356), size=wx.Size(75, 23), style=0)
        self.cancelarBoton.Bind(wx.EVT_BUTTON, self.onCancelarBoton, id=wxID_DIALOG1CANCELARBOTON)

    def __init__(self, parent, listadoInstalaciones):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
                listadoInstalaciones:
        """
        self.parent = parent
        self._init_ctrls(parent)
        self.dev = False
        self.cambios = False
        self.sistemasACSMM = listadoInstalaciones[0]
        self.sistemasCalefaccionMM = listadoInstalaciones[1]
        self.sistemasRefrigeracionMM = listadoInstalaciones[2]
        self.sistemasClimatizacionMM = listadoInstalaciones[3]
        self.sistemasMixto2MM = listadoInstalaciones[4]
        self.sistemasMixto3MM = listadoInstalaciones[5]
        self.sistemasContribucionesMM = listadoInstalaciones[6]
        self.sistemasIluminacionMM = listadoInstalaciones[7]
        self.sistemasVentilacionMM = listadoInstalaciones[8]
        self.sistemasVentiladoresMM = listadoInstalaciones[9]
        self.sistemasBombasMM = listadoInstalaciones[10]
        self.sistemasTorresRefrigeracionMM = listadoInstalaciones[11]
        self.cargarTabla()

    def onAceptarBoton(self, event):
        """
        Metodo: onAceptarBoton

        ARGUMENTOS:
                event:
        """
        if self.cambios == True:
            self.dev = [
             self.sistemasACSMM, self.sistemasCalefaccionMM, self.sistemasRefrigeracionMM,
             self.sistemasClimatizacionMM, self.sistemasMixto2MM, self.sistemasMixto3MM,
             self.sistemasContribucionesMM, self.sistemasIluminacionMM, self.sistemasVentilacionMM,
             self.sistemasVentiladoresMM, self.sistemasBombasMM, self.sistemasTorresRefrigeracionMM]
        else:
            self.dev = False
        self.Close()

    def onCancelarBoton(self, event):
        """
        Metodo: onCancelarBoton

        ARGUMENTOS:
                event:
        """
        self.dev = False
        self.Close()

    def OnBotonAnadir(self, event):
        """
        Metodo: OnBotonAnadir

        ARGUMENTOS:
                event:
        """
        dlg = ventanaUniversal.create(self)
        dlg.ShowModal()
        if dlg.dev != False:
            self.cambios = True
            if dlg.dev[1] == 'ACS':
                self.sistemasACSMM.append(dlg.dev)
            if dlg.dev[1] == 'calefaccion':
                self.sistemasCalefaccionMM.append(dlg.dev)
            if dlg.dev[1] == 'refrigeracion':
                self.sistemasRefrigeracionMM.append(dlg.dev)
            if dlg.dev[1] == 'climatizacion':
                self.sistemasClimatizacionMM.append(dlg.dev)
            if dlg.dev[1] == 'mixto2':
                self.sistemasMixto2MM.append(dlg.dev)
            if dlg.dev[1] == 'mixto3':
                self.sistemasMixto3MM.append(dlg.dev)
            if dlg.dev[1] == 'renovable':
                self.sistemasContribucionesMM.append(dlg.dev)
            if dlg.dev[1] == 'iluminacion':
                self.sistemasIluminacionMM.append(dlg.dev)
            if dlg.dev[1] == 'ventilacion':
                self.sistemasVentilacionMM.append(dlg.dev)
            if dlg.dev[1] == 'ventiladores':
                self.sistemasVentiladoresMM.append(dlg.dev)
            if dlg.dev[1] == 'bombas':
                self.sistemasBombasMM.append(dlg.dev)
            if dlg.dev[1] == 'torresRefrigeracion':
                self.sistemasTorresRefrigeracionMM.append(dlg.dev)
        self.cargarTabla()

    def OnBotonModificar(self, event):
        """
        Metodo: OnBotonModificar

        ARGUMENTOS:
                event:
        """
        seleccionado = self.listCtrl1.GetFocusedItem()
        if seleccionado == -1:
            wx.MessageBox(_('Seleccione una instalación de la lista'), _('Aviso'))
            return
        texto = self.listCtrl1.GetItemText(seleccionado)
        for i in range(len(self.sistemasACSMM)):
            if self.sistemasACSMM[i][0] == texto:
                dlg = ventanaACS.create(self)
                dlg.panel.parent.cargarDatosAlPanel(self.sistemasACSMM[i], dlg.panel)
                dlg.ShowModal()
                comp = True
                if dlg.dev != False:
                    if texto != dlg.dev[0]:
                        comp = self.comprobarNombres(dlg.dev[0], dlg.dev[1], i)
                    if comp == True:
                        self.sistemasACSMM[i] = dlg.dev
                        self.cargarTabla()
                        self.cambios = True
                        return
                    wx.MessageBox(_('El nombre de la instalación ya existe'), _('Aviso'))
                    return

        for i in range(len(self.sistemasCalefaccionMM)):
            if self.sistemasCalefaccionMM[i][0] == texto:
                dlg = ventanaCalefaccion.create(self)
                dlg.panel.parent.cargarDatosAlPanel(self.sistemasCalefaccionMM[i], dlg.panel)
                dlg.ShowModal()
                comp = True
                if dlg.dev != False:
                    if texto != dlg.dev[0]:
                        comp = self.comprobarNombres(dlg.dev[0], dlg.dev[1], i)
                    if comp == True:
                        self.sistemasCalefaccionMM[i] = dlg.dev
                        self.cargarTabla()
                        self.cambios = True
                        return
                    wx.MessageBox(_('El nombre de la instalación ya existe'), _('Aviso'))
                    return

        for i in range(len(self.sistemasRefrigeracionMM)):
            if self.sistemasRefrigeracionMM[i][0] == texto:
                dlg = ventanaRefrigeracion.create(self)
                dlg.panel.parent.cargarDatosAlPanel(self.sistemasRefrigeracionMM[i], dlg.panel)
                dlg.ShowModal()
                comp = True
                if dlg.dev != False:
                    if texto != dlg.dev[0]:
                        comp = self.comprobarNombres(dlg.dev[0], dlg.dev[1], i)
                    if comp == True:
                        self.sistemasRefrigeracionMM[i] = dlg.dev
                        self.cargarTabla()
                        self.cambios = True
                        return
                    wx.MessageBox(_('El nombre de la instalación ya existe'), _('Aviso'))
                    return

        for i in range(len(self.sistemasClimatizacionMM)):
            if self.sistemasClimatizacionMM[i][0] == texto:
                dlg = ventanaClimatizacion.create(self)
                dlg.panel.parent.cargarDatosAlPanel(self.sistemasClimatizacionMM[i], dlg.panel)
                dlg.ShowModal()
                comp = True
                if dlg.dev != False:
                    if texto != dlg.dev[0]:
                        comp = self.comprobarNombres(dlg.dev[0], dlg.dev[1], i)
                    if comp == True:
                        self.sistemasClimatizacionMM[i] = dlg.dev
                        self.cargarTabla()
                        self.cambios = True
                        return
                    wx.MessageBox(_('El nombre de la instalación ya existe'), _('Aviso'))
                    return

        for i in range(len(self.sistemasMixto2MM)):
            if self.sistemasMixto2MM[i][0] == texto:
                dlg = ventanaMixto2.create(self)
                dlg.panel.parent.cargarDatosAlPanel(self.sistemasMixto2MM[i], dlg.panel)
                dlg.ShowModal()
                comp = True
                if dlg.dev != False:
                    if texto != dlg.dev[0]:
                        comp = self.comprobarNombres(dlg.dev[0], dlg.dev[1], i)
                    if comp == True:
                        self.sistemasMixto2MM[i] = dlg.dev
                        self.cargarTabla()
                        self.cambios = True
                        return
                    wx.MessageBox(_('El nombre de la instalación ya existe'), _('Aviso'))
                    return

        for i in range(len(self.sistemasMixto3MM)):
            if self.sistemasMixto3MM[i][0] == texto:
                dlg = ventanaMixto3.create(self)
                dlg.panel.parent.cargarDatosAlPanel(self.sistemasMixto3MM[i], dlg.panel)
                dlg.ShowModal()
                comp = True
                if dlg.dev != False:
                    if texto != dlg.dev[0]:
                        comp = self.comprobarNombres(dlg.dev[0], dlg.dev[1], i)
                    if comp == True:
                        self.sistemasMixto3MM[i] = dlg.dev
                        self.cargarTabla()
                        self.cambios = True
                        return
                    wx.MessageBox(_('El nombre de la instalación ya existe'), _('Aviso'))
                    return

        for i in range(len(self.sistemasContribucionesMM)):
            if self.sistemasContribucionesMM[i][0] == texto:
                dlg = ventanaContribuciones.create(self)
                dlg.panel.cargarDatos(self.sistemasContribucionesMM[i])
                dlg.ShowModal()
                comp = True
                if dlg.dev != False:
                    if texto != dlg.dev[0]:
                        comp = self.comprobarNombres(dlg.dev[0], dlg.dev[1], i)
                    if comp == True:
                        self.sistemasContribucionesMM[i] = dlg.dev
                        self.cargarTabla()
                        self.cambios = True
                        return
                    wx.MessageBox(_('El nombre de la instalación ya existe'), _('Aviso'))
                    return

        for i in range(len(self.sistemasIluminacionMM)):
            if self.sistemasIluminacionMM[i][0] == texto:
                dlg = ventanaIluminacion.create(self, self.sistemasIluminacionMM)
                dlg.panel.cargarDatos(self.sistemasIluminacionMM[i])
                dlg.ShowModal()
                comp = True
                if dlg.dev != False:
                    if texto != dlg.dev[0]:
                        comp = self.comprobarNombres(dlg.dev[0], dlg.dev[1], i)
                    if comp == True:
                        self.sistemasIluminacionMM[i] = dlg.dev
                        self.cargarTabla()
                        self.cambios = True
                        return
                    wx.MessageBox(_('El nombre de la instalación ya existe'), _('Aviso'))
                    return

        for i in range(len(self.sistemasVentilacionMM)):
            if self.sistemasVentilacionMM[i][0] == texto:
                dlg = ventanaVentilacion.create(self)
                dlg.panel.cargarDatos(self.sistemasVentilacionMM[i])
                dlg.ShowModal()
                comp = True
                if dlg.dev != False:
                    if texto != dlg.dev[0]:
                        comp = self.comprobarNombres(dlg.dev[0], dlg.dev[1], i)
                    if comp == True:
                        self.sistemasVentilacionMM[i] = dlg.dev
                        self.cargarTabla()
                        self.cambios = True
                        return
                    wx.MessageBox(_('El nombre de la instalación ya existe'), _('Aviso'))
                    return

        for i in range(len(self.sistemasVentiladoresMM)):
            if self.sistemasVentiladoresMM[i][0] == texto:
                dlg = ventanaVentiladores.create(self)
                dlg.panel.cargarDatos(self.sistemasVentiladoresMM[i])
                dlg.ShowModal()
                comp = True
                if dlg.dev != False:
                    if texto != dlg.dev[0]:
                        comp = self.comprobarNombres(dlg.dev[0], dlg.dev[1], i)
                    if comp == True:
                        self.sistemasVentiladoresMM[i] = dlg.dev
                        self.cargarTabla()
                        self.cambios = True
                        return
                    wx.MessageBox(_('El nombre de la instalación ya existe'), _('Aviso'))
                    return

        for i in range(len(self.sistemasBombasMM)):
            if self.sistemasBombasMM[i][0] == texto:
                dlg = ventanaBombas.create(self)
                dlg.panel.cargarDatos(self.sistemasBombasMM[i])
                dlg.ShowModal()
                comp = True
                if dlg.dev != False:
                    if texto != dlg.dev[0]:
                        comp = self.comprobarNombres(dlg.dev[0], dlg.dev[1], i)
                    if comp == True:
                        self.sistemasBombasMM[i] = dlg.dev
                        self.cargarTabla()
                        self.cambios = True
                        return
                    wx.MessageBox(_('El nombre de la instalación ya existe'), _('Aviso'))
                    return

        for i in range(len(self.sistemasTorresRefrigeracionMM)):
            if self.sistemasTorresRefrigeracionMM[i][0] == texto:
                dlg = ventanaTorresRefrigeracion.create(self)
                dlg.panel.cargarDatos(self.sistemasTorresRefrigeracionMM[i])
                dlg.ShowModal()
                comp = True
                if dlg.dev != False:
                    if texto != dlg.dev[0]:
                        comp = self.comprobarNombres(dlg.dev[0], dlg.dev[1], i)
                    if comp == True:
                        self.sistemasTorresRefrigeracionMM[i] = dlg.dev
                        self.cargarTabla()
                        self.cambios = True
                        return
                    wx.MessageBox(_('El nombre de la instalación ya existe'), _('Aviso'))
                    return

    def comprobarNombres(self, nombre, tipo, pos):
        """
        Metodo: comprobarNombres

        ARGUMENTOS:
                nombre:
                tipo:
                pos:
        """
        for i in range(len(self.sistemasACSMM)):
            if self.sistemasACSMM[i][0] == nombre:
                return False

        for i in range(len(self.sistemasCalefaccionMM)):
            if self.sistemasCalefaccionMM[i][0] == nombre:
                return False

        for i in range(len(self.sistemasRefrigeracionMM)):
            if self.sistemasRefrigeracionMM[i][0] == nombre:
                return False

        for i in range(len(self.sistemasClimatizacionMM)):
            if self.sistemasClimatizacionMM[i][0] == nombre:
                return False

        for i in range(len(self.sistemasMixto2MM)):
            if self.sistemasMixto2MM[i][0] == nombre:
                return False

        for i in range(len(self.sistemasMixto3MM)):
            if self.sistemasMixto3MM[i][0] == nombre:
                return False

        for i in range(len(self.sistemasContribucionesMM)):
            if self.sistemasContribucionesMM[i][0] == nombre:
                return False

        if self.parent.parent.parent.parent.objEdificio.programa != 'Residencial':
            for i in range(len(self.sistemasIluminacionMM)):
                if self.sistemasIluminacionMM[i][0] == nombre:
                    return False

            for i in range(len(self.sistemasVentilacionMM)):
                if self.sistemasVentilacionMM[i][0] == nombre:
                    return False

            for i in range(len(self.sistemasVentiladoresMM)):
                if self.sistemasVentiladoresMM[i][0] == nombre:
                    return False

            for i in range(len(self.sistemasBombasMM)):
                if self.sistemasBombasMM[i][0] == nombre:
                    return False

            for i in range(len(self.sistemasTorresRefrigeracionMM)):
                if self.sistemasTorresRefrigeracionMM[i][0] == nombre:
                    return False

        return True

    def OnBotonBorrar(self, event):
        """
        Metodo: OnBotonBorrar

        ARGUMENTOS:
                event:
        """
        seleccionado = self.listCtrl1.GetFocusedItem()
        if seleccionado == -1:
            wx.MessageBox(_('Seleccione una instalación de la lista'), _('Aviso'))
            return
        texto = self.listCtrl1.GetItemText(seleccionado)
        for i in range(len(self.sistemasACSMM)):
            if self.sistemasACSMM[i][0] == texto:
                self.sistemasACSMM.pop(i)
                self.cargarTabla()
                self.cambios = True
                return

        for i in range(len(self.sistemasCalefaccionMM)):
            if self.sistemasCalefaccionMM[i][0] == texto:
                self.sistemasCalefaccionMM.pop(i)
                self.cargarTabla()
                self.cambios = True
                return

        for i in range(len(self.sistemasRefrigeracionMM)):
            if self.sistemasRefrigeracionMM[i][0] == texto:
                self.sistemasRefrigeracionMM.pop(i)
                self.cargarTabla()
                self.cambios = True
                return

        for i in range(len(self.sistemasClimatizacionMM)):
            if self.sistemasClimatizacionMM[i][0] == texto:
                self.sistemasClimatizacionMM.pop(i)
                self.cargarTabla()
                self.cambios = True
                return

        for i in range(len(self.sistemasMixto2MM)):
            if self.sistemasMixto2MM[i][0] == texto:
                self.sistemasMixto2MM.pop(i)
                self.cargarTabla()
                self.cambios = True
                return

        for i in range(len(self.sistemasMixto3MM)):
            if self.sistemasMixto3MM[i][0] == texto:
                self.sistemasMixto3MM.pop(i)
                self.cargarTabla()
                self.cambios = True
                return

        for i in range(len(self.sistemasContribucionesMM)):
            if self.sistemasContribucionesMM[i][0] == texto:
                self.sistemasContribucionesMM.pop(i)
                self.cargarTabla()
                self.cambios = True
                return

        for i in range(len(self.sistemasIluminacionMM)):
            if self.sistemasIluminacionMM[i][0] == texto:
                self.sistemasIluminacionMM.pop(i)
                self.cargarTabla()
                self.cambios = True
                return

        for i in range(len(self.sistemasVentilacionMM)):
            if self.sistemasVentilacionMM[i][0] == texto:
                self.sistemasVentilacionMM.pop(i)
                self.cargarTabla()
                self.cambios = True
                return

        for i in range(len(self.sistemasVentiladoresMM)):
            if self.sistemasVentiladoresMM[i][0] == texto:
                self.sistemasVentiladoresMM.pop(i)
                self.cargarTabla()
                self.cambios = True
                return

        for i in range(len(self.sistemasBombasMM)):
            if self.sistemasBombasMM[i][0] == texto:
                self.sistemasBombasMM.pop(i)
                self.cargarTabla()
                self.cambios = True
                return

        for i in range(len(self.sistemasTorresRefrigeracionMM)):
            if self.sistemasTorresRefrigeracionMM[i][0] == texto:
                self.sistemasTorresRefrigeracionMM.pop(i)
                self.cargarTabla()
                self.cambios = True
                return

    def cargarTabla(self):
        """
        Metodo: cargarTabla

        """
        self.listCtrl1.DeleteAllItems()
        for i in self.sistemasACSMM:
            self.listCtrl1.Append([i[0], 'Equipo de ACS', ''])

        for i in self.sistemasCalefaccionMM:
            self.listCtrl1.Append([i[0], 'Equipo de sólo calefacción', ''])

        for i in self.sistemasRefrigeracionMM:
            self.listCtrl1.Append([i[0], 'Equipo de sólo refrigeración', ''])

        for i in self.sistemasClimatizacionMM:
            self.listCtrl1.Append([i[0], 'Equipo de calefacción y refrigeración', ''])

        for i in self.sistemasMixto2MM:
            self.listCtrl1.Append([i[0], 'Equipo mixto de calefacción y ACS'])

        for i in self.sistemasMixto3MM:
            self.listCtrl1.Append([i[0], 'Equipo mixto de calefacción,  refrigeración y ACS', ''])

        for i in self.sistemasContribucionesMM:
            self.listCtrl1.Append([i[0], 'Contribuciones energéticas', ''])

        for i in self.sistemasIluminacionMM:
            self.listCtrl1.Append([i[0], 'Equipo de iluminación', ''])

        for i in self.sistemasVentilacionMM:
            self.listCtrl1.Append([i[0], 'Equipo de aire primario', ''])

        for i in self.sistemasVentiladoresMM:
            self.listCtrl1.Append([i[0], 'Ventiladores', ''])

        for i in self.sistemasBombasMM:
            self.listCtrl1.Append([i[0], 'Equipo de bombeo', ''])

        for i in self.sistemasTorresRefrigeracionMM:
            self.listCtrl1.Append([i[0], 'Torres de refrigeración', ''])


def create(parent, listadoInstalaciones):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
                listadoInstalaciones:
    """
    return Dialog1(parent, listadoInstalaciones)