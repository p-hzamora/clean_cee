# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\ayudaNumeroHoras.pyc
# Compiled at: 2014-12-09 12:32:30
"""
Modulo: ayudaNumeroHoras.py

"""
import wx, Instalaciones.escalonamientoEquipos as escalonamientoEquipos, Instalaciones.perfilesTerciario as perfilesTerciario
from Instalaciones.comprobarCampos import Comprueba

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return Dialog1(parent)


wxID_DIALOG1, wxID_DIALOG1BETACOMB, wxID_DIALOG1BUTTON1, wxID_ACEPTARBUTTON, wxID_CANCELARBUTTON, wxID_DIALOG1DEMANDA, wxID_DIALOG1FRACCIONES, wxID_DIALOG1HOLA, wxID_DIALOG1POTENCIA, wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICTEXT2, wxID_DIALOG1STATICTEXT3, wxID_DIALOG1STATICTEXT4, wxID_DIALOG1STATICTEXT5, wxID_DIALOG1STATICTEXT6, wxID_DIALOG1STATICTEXT7, wxID_DIALOG1STATICTEXT8, wxID_DIALOG1TEXTCTRL1, wxID_DIALOG1TGNR, wxID_DIALOG1TON, wxID_DIALOG1STATICBOX1, wxID_POTENCIAMAXIMAINSTALACIONESUNIDADES, wxID_DEMANDAUNIDADES, wxID_NUMEROHORAS = [ wx.NewId() for _init_ctrls in range(24) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo ayudaNumeroHoras.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(716, 97), size=wx.Size(306, 218), style=wx.DEFAULT_DIALOG_STYLE, title=_('Estimación del número de horas demanda'))
        self.SetClientSize(wx.Size(306, 218))
        self.SetBackgroundColour('white')
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=_('Número de horas de demanda'), name='staticText1', parent=self, pos=wx.Point(15, 15), size=wx.Size(350, 20), style=0)
        self.staticText1.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.staticText1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticBox1 = wx.StaticBox(id=wxID_DIALOG1STATICBOX1, label=_('Estimación del número de horas de demanda'), name='staticText1', parent=self, pos=wx.Point(15, 45), size=wx.Size(276, 120), style=0)
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticBox1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.potenciaMaximaInstalacionText = wx.StaticText(id=wxID_DIALOG1STATICTEXT3, label=_('Potencia máxima instalación'), name='potenciaMaximaInstalacionText', parent=self, pos=wx.Point(30, 70), size=wx.Size(164, 13), style=0)
        self.potencia = wx.TextCtrl(id=wxID_DIALOG1POTENCIA, name='potencia', parent=self, pos=wx.Point(200, 68), size=wx.Size(56, 21), style=0, value='')
        self.potencia.Bind(wx.EVT_TEXT, self.calculoTiempoFuncionamiento, id=wxID_DIALOG1POTENCIA)
        self.potenciaMaximaInstalacionUnidades = wx.StaticText(id=wxID_POTENCIAMAXIMAINSTALACIONESUNIDADES, label=_('kW'), name='potenciaMaximaInstalacionUnidades', parent=self, pos=wx.Point(261, 70), size=wx.Size(15, 13), style=0)
        self.demandaEnergiaAnualText = wx.StaticText(id=wxID_DIALOG1STATICTEXT8, label=_('Demanda energía anual'), name='demandaEnergiaAnualText', parent=self, pos=wx.Point(30, 100), size=wx.Size(151, 13), style=0)
        self.demanda = wx.TextCtrl(id=wxID_DIALOG1DEMANDA, name='demanda', parent=self, pos=wx.Point(200, 98), size=wx.Size(56, 21), style=0, value='')
        self.demanda.Bind(wx.EVT_TEXT, self.calculoTiempoFuncionamiento, id=wxID_DIALOG1DEMANDA)
        self.demandaUnidades = wx.StaticText(id=wxID_DEMANDAUNIDADES, label=_('kWh'), name='demandaUnidades', parent=self, pos=wx.Point(261, 100), size=wx.Size(20, 13), style=0)
        self.numeroDeHorasDeDeamandaText = wx.StaticText(id=wxID_DIALOG1STATICTEXT6, label=_('Número de horas de demanda'), name='numeroDeHorasDeDeamandaText', parent=self, pos=wx.Point(30, 130), size=wx.Size(164, 13), style=0)
        self.tgnr = wx.TextCtrl(id=wxID_DIALOG1TGNR, name='tgnr', parent=self, pos=wx.Point(200, 128), size=wx.Size(56, 21), style=0, value='')
        self.tgnr.SetEditable(False)
        self.tgnr.Enable(False)
        self.numeroHorasUnidades = wx.StaticText(id=wxID_NUMEROHORAS, label=_('h'), name='numeroHorasUnidades', parent=self, pos=wx.Point(261, 130), size=wx.Size(15, 13), style=0)
        self.aceptarButton = wx.Button(id=wxID_ACEPTARBUTTON, label=_('Aceptar'), name='cerrarButton', parent=self, pos=wx.Point(15, 180), size=wx.Size(75, 23), style=0)
        self.aceptarButton.Bind(wx.EVT_BUTTON, self.OnAceptarButton, id=wxID_ACEPTARBUTTON)
        self.cancelarButton = wx.Button(id=wxID_CANCELARBUTTON, label=_('Cancelar'), name='cerrarButton', parent=self, pos=wx.Point(105, 180), size=wx.Size(75, 23), style=0)
        self.cancelarButton.Bind(wx.EVT_BUTTON, self.OnCancelarButton, id=wxID_CANCELARBUTTON)
        self.potencia.SetToolTip(wx.ToolTip(_('Potencia máxima demanda por la instalación (kW)')))
        self.demanda.SetToolTip(wx.ToolTip(_('Demanda térmica anual (kWh). \nSi previamente ya ha realizado una calificación, en este campo, le aparecerá la demanda\ncalculada de calefacción o refrigeración, dependiendo del servicio seleccionado.')))

    def __init__(self, parent, zona, perfilUso, servicio):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
                zona:
                perfilUso:
                servicio:
        """
        self.parent = parent
        self._init_ctrls(parent)
        self.dev = []
        self.zona = zona
        self.perfilUso = perfilUso
        self.servicio = servicio
        self.calculoDemandaCalefaccion()

    def calculoDemandaCalefaccion(self):
        """
        Metodo: iniciaValores

        """
        if self.parent.parent.parent.parent.objEdificio.casoValido == True:
            if self.servicio == 'Calefacción':
                dda = self.parent.parent.parent.parent.objEdificio.datosResultados.ddaBrutaCal
                dda = round(dda * self.parent.parent.parent.parent.objEdificio.datosIniciales.area, 1)
            elif self.servicio == 'Refrigeración':
                dda = self.parent.parent.parent.parent.objEdificio.datosResultados.ddaBrutaRef
                dda = round(dda * self.parent.parent.parent.parent.objEdificio.datosIniciales.area, 1)
            else:
                dda = self.parent.parent.parent.parent.objEdificio.datosResultados.ddaBrutaACS
                dda = round(dda * self.parent.parent.parent.parent.objEdificio.datosIniciales.area, 1)
            self.demanda.SetValue(str(dda))

    def OnAceptarButton(self, event):
        """
        Metodo: OnAceptarButton

        ARGUMENTOS:
                event:
        """
        listaErrores = ''
        listaErrores += Comprueba(self.potencia.GetValue(), 2, listaErrores, _('potencia máxima de la instalación'), 0.0).ErrorDevuelto
        listaErrores += Comprueba(self.demanda.GetValue(), 2, listaErrores, _('demanda de energía anual'), 0.0).ErrorDevuelto
        if listaErrores == '':
            self.dev = [
             self.tgnr.GetValue()]
            self.Close()
        else:
            wx.MessageBox(_('Revise los siguientes campos:\n') + listaErrores, _('Aviso'))

    def OnCancelarButton(self, event):
        """
        Metodo: OnCancelarButton

        ARGUMENTOS:
                event:
        """
        self.Close()

    def calculoTiempoFuncionamiento(self, event):
        """
        Metodo: calculoTiempoFuncionamiento

        ARGUMENTOS:
                event:
        """
        try:
            dato = self.potencia.GetValue()
            if ',' in dato:
                dato = dato.replace(',', '.')
                self.potencia.SetValue(dato)
                self.potencia.SetInsertionPointEnd()
            dato = self.demanda.GetValue()
            if ',' in dato:
                dato = dato.replace(',', '.')
                self.demanda.SetValue(dato)
                self.demanda.SetInsertionPointEnd()
            fcpSistema = [0.05, 
             0.15, 
             0.25, 
             0.35, 
             0.45, 
             0.55, 
             0.65, 
             0.75, 
             0.85, 
             0.95]
            if self.servicio == 'Calefacción':
                distribucionFraccionEnergia = perfilesTerciario.PerfilDemandaCalefaccion(self.zona, self.perfilUso)
            elif self.servicio == 'Refrigeración':
                distribucionFraccionEnergia = perfilesTerciario.PerfilDemandaRefrigeracion(self.zona, self.perfilUso)
            elif self.servicio == 'ACS':
                distribucionFraccionEnergia = [
                 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                 0.0, 0.0, 0.0, 1.0]
            listaFracciones = [
             1.0]
            if self.zona != '':
                porcentajeEnergiaEquipos, betaComb = escalonamientoEquipos.porcentajeEnergiaEquipos(listaFracciones, fcpSistema, distribucionFraccionEnergia)
                if self.demanda != '':
                    energiaAnualEquipos = [ float(x) * float(self.demanda.GetValue()) / 100.0 for x in porcentajeEnergiaEquipos ]
                    tgnr = [ round(float(energiaAnualEquipos[i]) / (float(self.potencia.GetValue()) * float(betaComb[i])), 1) for i in range(len(betaComb))
                           ]
                    aux = str(tgnr).replace('[', '').replace(']', '').replace("'", '')
                    aux = str(round(float(aux), 1))
                    self.tgnr.SetValue(aux)
        except:
            self.tgnr.SetValue('')