# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: MedidasDeMejora\ventanaUniversal.pyc
# Compiled at: 2015-02-17 10:46:53
"""
Modulo: ventanaUniversal.py

"""
from miChoice import MiChoice
import Instalaciones.panelACS as panelACS, Instalaciones.panelBombas as panelBombas, Instalaciones.panelCalefaccion as panelCalefaccion, Instalaciones.panelClimatizacion as panelClimatizacion, Instalaciones.panelIluminacion as panelIluminacion, Instalaciones.panelMixto2 as panelMixto2, Instalaciones.panelMixto3 as panelMixto3, Instalaciones.panelRefrigeracion as panelRefrigeracion, Instalaciones.panelRenovables as panelRenovables, Instalaciones.panelTorresRefrigeracion as panelTorresRefrigeracion, Instalaciones.panelVentilacion as panelVentilacion, Instalaciones.panelVentiladores as panelVentiladores, Calculos.listadosWeb as listadosWeb, wx

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return Dialog1(parent)


wxID_DIALOG1, wxID_DIALOG1ACEPTARBOTON, wxID_DIALOG1AISLANTERADIO, wxID_DIALOG1CANCELARBOTON, wxID_DIALOG1CERRAMIENTOSMEJORADOSTEXT, wxID_DIALOG1CHOICE1, wxID_DIALOG1CUBIERTACHECK, wxID_DIALOG1DESCRIPCION, wxID_DIALOG1DESCRIPCIONTEXT, wxID_DIALOG1ESPESORAISLANTE, wxID_DIALOG1ESPESORTEXT, wxID_DIALOG1ESPESORUNIDADESTEXT, wxID_DIALOG1FACHADACHECK, wxID_DIALOG1LANDAAISLANTE, wxID_DIALOG1LANDAAISLANTETEXT, wxID_DIALOG1LANDAAISLANTEUNIDADES, wxID_DIALOG1LIBRERIARADIO, wxID_DIALOG1NUEVATRANSMITEXT, wxID_DIALOG1SUELOCHECK, wxID_DIALOG1TITULOTEXT, wxID_DIALOG1URADIO, wxID_DIALOG1VALORU, wxID_DIALOG1VALURUNIDADESTEXT, wxID_DIALOG1TITULOTEXT, wxID_PANELDEFINIRMEDIDASMEJORAMEJORAENVOLVENTECHOICE = [ wx.NewId() for _init_ctrls in range(25) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo ventanaUniversal.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                 prnt:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(0, 0), size=wx.Size(770, 420), style=wx.DEFAULT_DIALOG_STYLE, title=_('Definir nueva instalación'))
        self.SetClientSize(wx.Size(770, 440))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tituloText = wx.StaticText(id=wxID_DIALOG1TITULOTEXT, label=_('Seleccione el tipo de equipo a añadir'), name='tituloText', parent=self, pos=wx.Point(15, 4), size=wx.Size(165, 30), style=0)
        self.tituloText.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.tituloText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.tituloText.SetSize(wx.Size(165, 34))
        self.tipoInstalacionChoice = MiChoice(choices=listadosWeb.listadoOpcionesMMInstalaciones, id=wxID_PANELDEFINIRMEDIDASMEJORAMEJORAENVOLVENTECHOICE, name='tipoInstalacionChoice', parent=self, pos=wx.Point(185, 10), size=wx.Size(250, 21), style=0)
        self.tipoInstalacionChoice.SetSelection(0)
        self.tipoInstalacionChoice.Bind(wx.EVT_CHOICE, self.OnTipoInstalacionChoice, id=wxID_PANELDEFINIRMEDIDASMEJORAMEJORAENVOLVENTECHOICE)
        self.panel = panelACS.Panel1(parent=self, id=-1, pos=wx.Point(15, 60), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='panelACS', real_parent=prnt.parent.parent.parent.parent.panelInstalaciones)
        self.aceptarBoton = wx.Button(id=wxID_DIALOG1ACEPTARBOTON, label=_('Aceptar'), name='aceptarBoton', parent=self, pos=wx.Point(15, 412), size=wx.Size(75, 23), style=0)
        self.aceptarBoton.Bind(wx.EVT_BUTTON, self.onAceptarBoton, id=wxID_DIALOG1ACEPTARBOTON)
        self.cancelarBoton = wx.Button(id=wxID_DIALOG1CANCELARBOTON, label=_('Cancelar'), name='cancelarBoton', parent=self, pos=wx.Point(105, 412), size=wx.Size(75, 23), style=0)
        self.cancelarBoton.Bind(wx.EVT_BUTTON, self.onCancelarBoton, id=wxID_DIALOG1CANCELARBOTON)

    def __init__(self, parent):
        """
        Constructor de la clase

        ARGUMENTOS:
                 parent:
        """
        self._init_ctrls(parent)
        self.parent = parent
        self.dev = False
        self.panel.Destroy()
        self.panel = panelACS.Panel1(parent=self, id=-1, pos=wx.Point(15, 60), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='panelACS', real_parent=self.parent.parent.parent.parent.parent.panelInstalaciones)
        self.panel.aislanteCaldera.SetSelection(0)
        self.panel.definirAntiguedadChoice.SetSelection(0)
        self.panel.SetSize(wx.Size(770, 370))
        if self.parent.parent.parent.parent.parent.programa == b'Peque\xf1oTerciario':
            a = listadosWeb.listadoOpcionesMMInstalacionePT
            self.tipoInstalacionChoice.SetItems(a)
        elif self.parent.parent.parent.parent.parent.programa == 'GranTerciario':
            a = listadosWeb.listadoOpcionesMMInstalacioneGT
            self.tipoInstalacionChoice.SetItems(a)

    def OnTipoInstalacionChoice(self, event):
        """
        Metodo: OnTipoInstalacionChoice

        ARGUMENTOS:
                event:
        """
        if 'Equipo de ACS' in self.tipoInstalacionChoice.GetStringSelection():
            self.panel.Destroy()
            self.panel = panelACS.Panel1(parent=self, id=-1, pos=wx.Point(15, 60), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='panelACS', real_parent=self.parent.parent.parent.parent.parent.panelInstalaciones)
            self.panel.aislanteCaldera.SetSelection(0)
            self.panel.definirAntiguedadChoice.SetSelection(0)
            self.panel.SetSize(wx.Size(770, 370))
        if 'Equipo de sólo calefacción' in self.tipoInstalacionChoice.GetStringSelection():
            self.panel.Destroy()
            self.panel = panelCalefaccion.Panel1(parent=self, id=-1, pos=wx.Point(15, 60), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='panelCalefaccion', real_parent=self.parent.parent.parent.parent.parent.panelInstalaciones)
            self.panel.aislanteCaldera.SetSelection(0)
            self.panel.definirAntiguedadChoice.SetSelection(0)
            self.panel.SetSize(wx.Size(770, 370))
        if 'Equipo de sólo refrigeración' in self.tipoInstalacionChoice.GetStringSelection():
            self.panel.Destroy()
            self.panel = panelRefrigeracion.Panel1(parent=self, id=-1, pos=wx.Point(15, 60), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='panelRefrigeracion', real_parent=self.parent.parent.parent.parent.parent.panelInstalaciones)
            self.panel.definirAntiguedadChoice.SetSelection(0)
            self.panel.SetSize(wx.Size(770, 370))
        if 'Equipo de calefacción y refrigeración' in self.tipoInstalacionChoice.GetStringSelection():
            self.panel.Destroy()
            self.panel = panelClimatizacion.Panel1(parent=self, id=-1, pos=wx.Point(15, 60), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='panelClimatizacion', real_parent=self.parent.parent.parent.parent.parent.panelInstalaciones)
            self.panel.definirAntiguedadChoice.SetSelection(0)
            self.panel.SetSize(wx.Size(770, 370))
        if 'Equipo mixto de calefacción y ACS' in self.tipoInstalacionChoice.GetStringSelection():
            self.panel.Destroy()
            self.panel = panelMixto2.Panel1(parent=self, id=-1, pos=wx.Point(15, 60), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='panelMixto2', real_parent=self.parent.parent.parent.parent.parent.panelInstalaciones)
            self.panel.aislanteCaldera.SetSelection(0)
            self.panel.definirAntiguedadChoice.SetSelection(0)
            self.panel.SetSize(wx.Size(770, 370))
        if 'Equipo mixto de calefacción,  refrigeración y ACS' in self.tipoInstalacionChoice.GetStringSelection():
            self.panel.Destroy()
            self.panel = panelMixto3.Panel1(parent=self, id=-1, pos=wx.Point(15, 60), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='panelMixto3', real_parent=self.parent.parent.parent.parent.parent.panelInstalaciones)
            self.panel.definirAntiguedadChoice.SetSelection(0)
            self.panel.SetSize(wx.Size(770, 370))
        if 'Contribuciones energéticas' in self.tipoInstalacionChoice.GetStringSelection():
            self.panel.Destroy()
            self.panel = panelRenovables.Panel1(parent=self, id=-1, pos=wx.Point(15, 60), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='panelRenovables', real_parent=self.parent.parent.parent.parent.parent.panelInstalaciones)
            self.panel.SetSize(wx.Size(770, 370))
        if 'Equipo de iluminación' in self.tipoInstalacionChoice.GetStringSelection():
            self.panel.Destroy()
            self.panel = panelIluminacion.Panel1(parent=self, id=-1, pos=wx.Point(15, 60), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='panelIluminacion', real_parent=self.parent.parent.parent.parent.parent.panelInstalaciones, instalacionIluminacion=self.parent.sistemasIluminacionMM)
            self.panel.SetSize(wx.Size(770, 370))
        if 'Equipo de aire primario' in self.tipoInstalacionChoice.GetStringSelection():
            self.panel.Destroy()
            self.panel = panelVentilacion.Panel1(parent=self, id=-1, pos=wx.Point(15, 60), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='panelVentilacion', real_parent=self.parent.parent.parent.parent.parent.panelInstalaciones)
            self.panel.SetSize(wx.Size(770, 370))
        if 'Ventiladores' in self.tipoInstalacionChoice.GetStringSelection():
            self.panel.Destroy()
            self.panel = panelVentiladores.Panel1(parent=self, id=-1, pos=wx.Point(15, 60), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='panelVentiladores', real_parent=self.parent.parent.parent.parent.parent.panelInstalaciones)
            self.panel.SetSize(wx.Size(770, 370))
        if 'Equipo de bombeo' in self.tipoInstalacionChoice.GetStringSelection():
            self.panel.Destroy()
            self.panel = panelBombas.Panel1(parent=self, id=-1, pos=wx.Point(15, 60), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='panelBombas', real_parent=self.parent.parent.parent.parent.parent.panelInstalaciones)
            self.panel.SetSize(wx.Size(770, 370))
        if 'Torres de refrigeración' in self.tipoInstalacionChoice.GetStringSelection():
            self.panel.Destroy()
            self.panel = panelTorresRefrigeracion.Panel1(parent=self, id=-1, pos=wx.Point(15, 60), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='panelTorresRefrigeracion', real_parent=self.parent.parent.parent.parent.parent.panelInstalaciones)
            self.panel.SetSize(wx.Size(770, 370))

    def onAceptarBoton(self, event):
        """
        Metodo: onAceptarBoton

        ARGUMENTOS:
                event:
        """
        a = self.panel.GetName()
        if a == 'panelRenovables' or a == 'panelVentilacion' or a == 'panelVentiladores' or a == 'panelBombas' or a == 'panelTorresRefrigeracion':
            self.dev = self.panel.cogerDatos()
        else:
            if a == 'panelIluminacion':
                self.dev = self.panel.cogerDatosMM()
            else:
                self.dev = self.panel.parent.cogerDatosDelPanel(self.panel)
            if type(self.dev) == type('hola'):
                wx.MessageBox(_('Revise los siguientes campos:\n') + self.dev, _('Aviso'))
                return
        comp = self.comprobarNombres(self.dev[0])
        if comp == True:
            self.Close()
        else:
            wx.MessageBox(_('La instalación: "') + self.dev[0] + _('" ya está definida'), _('Aviso'))
            return

    def comprobarNombres(self, nombre):
        """
        Metodo: comprobarNombres

        ARGUMENTOS:
                nombre:
        """
        for i in self.parent.sistemasACSMM:
            if i[0] == nombre:
                return False

        for i in self.parent.sistemasCalefaccionMM:
            if i[0] == nombre:
                return False

        for i in self.parent.sistemasRefrigeracionMM:
            if i[0] == nombre:
                return False

        for i in self.parent.sistemasClimatizacionMM:
            if i[0] == nombre:
                return False

        for i in self.parent.sistemasMixto2MM:
            if i[0] == nombre:
                return False

        for i in self.parent.sistemasMixto3MM:
            if i[0] == nombre:
                return False

        for i in self.parent.sistemasContribucionesMM:
            if i[0] == nombre:
                return False

        for i in self.parent.sistemasIluminacionMM:
            if i[0] == nombre:
                return False

        for i in self.parent.sistemasVentilacionMM:
            if i[0] == nombre:
                return False

        for i in self.parent.sistemasVentiladoresMM:
            if i[0] == nombre:
                return False

        for i in self.parent.sistemasBombasMM:
            if i[0] == nombre:
                return False

        for i in self.parent.sistemasTorresRefrigeracionMM:
            if i[0] == nombre:
                return False

        return True

    def onCancelarBoton(self, event):
        """
        Metodo: onCancelarBoton

        ARGUMENTOS:
                event:
        """
        self.dev = False
        self.Close()