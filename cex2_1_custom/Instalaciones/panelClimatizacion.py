# Embedded file name: Instalaciones\panelClimatizacion.pyc
"""
Modulo: panelClimatizacion.py

"""
from Calculos.funcionesCalculo import diccCOPNominalDefecto, diccEERNominalDefecto
from Instalaciones.comprobarCampos import Comprueba, Comprueba2
from Instalaciones.funcionCalculoRendimientoEstacional import calculoRendimientoMedioEstacional
from miChoice import MiChoice
import Calculos.listadosWeb as listadosWeb
import Instalaciones.equipos as equipos
import wx
import logging
wxID_PANEL1, wxID_PANEL1COBERTURA, wxID_PANEL1COMBUSTIBLECHOICE, wxID_PANEL1DEFINIRDEMANDARADIO, wxID_PANEL1DEFINIRMETROS2RADIO, wxID_PANEL1DEFINIRTEXT, wxID_PANEL1GENERADORCHOICE, wxID_PANEL1METROSUNIDADESTEXT, wxID_PANEL1NOMBREINSTALACION, wxID_PANEL1NOMBREINSTALACIONTEXT, wxID_PANEL1PORCENTAJEUNIDADESTEXT, wxID_PANEL1RENDIMIENTOCHOICE, wxID_PANEL1RENDIMIENTOTEXT, wxID_PANEL1SUBGRUPOCHOICE, wxID_PANEL1SUBGRUPOTEXT, wxID_PANEL1TIPOCOMBUSTIBLETEXT, wxID_PANEL1TIPOGENERADORTEXT, wxID_PANEL1CALEFACTEXT, wxID_PANEL1CHOICE1, wxID_PANEL1RADIOBUTTON1, wxID_PANEL1ANTIEQUIPOTEXT, wxID_PANEL1MENOS5ANOSRADIO, wxID_PANEL1ENTRE515RADIO, wxID_PANEL1AISLANTEMALORADIO, wxID_PANEL1RENDIMIENTOCHOICE, wxID_PANEL1RENDIMIENTOMEDIOTEXT, wxID_PANEL1RENDIMIENTOMEDIOUNIDADESTEXT, wxID_PANEL1RENDIMIENTONOMINAL, wxID_PANEL1RENDIMIENTONOMINALTEXT, wxID_PANEL1RENDIMIENTONOMINALUNIDADESTEXT, wxID_PANEL1RENDIMIENTOTEXT, wxID_PANEL1RENDIMIETOMEDIO, wxID_PANEL1RENDNOMINALTEXT, wxID_PANEL1RENDNOMINALUNITEXT, wxID_PANEL1RENDIMIENTOMEDIO, wxID_PANEL1RENDIMIENTOMEDIOTEXT2, wxID_PANEL1RENDIMIENTOMEDIOUNIDADESTEXT2, wxID_PANEL1RENDIMIENTONOMINAL2, wxID_PANEL1RENDIMIENTONOMINALTEXT2, wxID_PANEL1RENDIMIENTONOMINALUNIDADESTEXT2, wxID_PANEL1RENDIMIENTOTEXT2, wxID_PANEL1RENDIMIETOMEDIO2, wxID_PANEL1RENDNOMINALTEXT2, wxID_PANEL1RENDNOMINALUNITEXT2, wxID_PANEL1RENDIMIENTOMEDIO2, wxID_PANEL1PORCENTAJEUNIDADESTEXT2, wxID_PANEL1DEFINIRTEXT2, wxID_PANEL1DEFINIRMETROS2RADIO2, wxID_PANEL1RADIOBUTTON12, wxID_PANEL1COBERTURA2, wxID_PANEL1METROSUNIDADESTEXT2, wxID_PANEL1PORCENTAJEUNIDADESTEXT2, wxID_PANEL1RENDGLOBALTEXTCAL, wxID_PANEL1RENDIMIENTOGLOBALCAL, wxID_PANEL1RENDGLOBALUNITEXTCAL, wxID_PANEL1RENDGLOBALTEXTREF, wxID_PANEL1RENDIMIENTOGLOBALREF, wxID_PANEL1RENDGLOBALUNITEXTREF, wxID_CARACTERISTICASLINEATEXT, wxID_DEMANDALINEATEXT, wxID_PANEL1COBERTURAPORCEN, wxID_PANEL1COBERTURAPORCEN2, wxID_EFICIENCIALINEATEXT, wxID_PANEL1ANTIGUEDADCHOICE = [ wx.NewId() for _init_ctrls in range(64) ]

class Panel1(wx.Panel):
    """
    Clase: Panel1 del modulo panelClimatizacion.py
    
    
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
        self.nombreInstalacionText = wx.StaticText(id=wxID_PANEL1NOMBREINSTALACIONTEXT, label=_(u'Nombre'), name=u'nombreInstalacionText', parent=self, pos=wx.Point(15, 2), size=wx.Size(102, 13), style=0)
        self.nombreInstalacion = wx.TextCtrl(id=wxID_PANEL1NOMBREINSTALACION, name=u'nombreInstalacion', parent=self, pos=wx.Point(170, 0), size=wx.Size(230, 21), style=0, value=_(u'Calefacci\xf3n y refrigeraci\xf3n'))
        self.nombreInstalacion.SetForegroundColour(wx.Colour(100, 200, 0))
        self.nombreInstalacion.Bind(wx.EVT_TEXT, self.OnNombreInstalacion, id=wxID_PANEL1NOMBREINSTALACION)
        self.subgrupoText = wx.StaticText(id=wxID_PANEL1SUBGRUPOTEXT, label=_(u'Zona'), name=u'subgrupoText', parent=self, pos=wx.Point(435, 2), size=wx.Size(60, 13), style=0)
        self.subgrupoChoice = MiChoice(choices=[], id=wxID_PANEL1SUBGRUPOCHOICE, name=u'subgrupoChoice', parent=self, pos=wx.Point(496, 0), size=wx.Size(200, 21), style=0)
        self.subgrupoChoice.Bind(wx.EVT_CHOICE, self.OnsubgrupoChoice, id=wxID_PANEL1SUBGRUPOCHOICE)
        self.tipoGeneradorText = wx.StaticText(id=wxID_PANEL1TIPOGENERADORTEXT, label=_(u'Tipo de generador'), name=u'tipoGeneradorText', parent=self, pos=wx.Point(15, 46), size=wx.Size(89, 13), style=0)
        self.CaracteristicasLineaText = wx.StaticBox(id=wxID_CARACTERISTICASLINEATEXT, label=_(u'Caracter\xedsticas'), name='CaracteristicasLineaText', parent=self, pos=wx.Point(0, 26), size=wx.Size(400, 77), style=0)
        self.CaracteristicasLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.generadorChoice = MiChoice(choices=listadosWeb.listadoInstalacionesClimatizacion, id=wxID_PANEL1GENERADORCHOICE, name=u'generadorChoice', parent=self, pos=wx.Point(170, 44), size=wx.Size(220, 21), style=0)
        self.generadorChoice.SetSelection(0)
        self.generadorChoice.Bind(wx.EVT_CHOICE, self.OngeneradorChoice, id=wxID_PANEL1GENERADORCHOICE)
        self.tipoCombustibleText = wx.StaticText(id=wxID_PANEL1TIPOCOMBUSTIBLETEXT, label=_(u'Tipo de combustible'), name=u'tipoCombustibleText', parent=self, pos=wx.Point(15, 71), size=wx.Size(96, 13), style=0)
        self.combustibleChoice = MiChoice(choices=listadosWeb.listadoCombustibles, id=wxID_PANEL1COMBUSTIBLECHOICE, name=u'combustibleChoice', parent=self, pos=wx.Point(170, 69), size=wx.Size(220, 21), style=0)
        self.combustibleChoice.SetSelection(2)
        self.combustibleChoice.Bind(wx.EVT_CHOICE, self.obtenerRendimientoEstacional, id=wxID_PANEL1COMBUSTIBLECHOICE)
        self.DemandaLineaText = wx.StaticBox(id=wxID_DEMANDALINEATEXT, label=_(u'Demanda cubierta'), name='DemandaLineaText', parent=self, pos=wx.Point(425, 26), size=wx.Size(285, 77), style=0)
        self.DemandaLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.DemandaLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.calefaccionText = wx.StaticText(id=wxID_PANEL1CALEFACTEXT, label=_(u'Calefacci\xf3n'), name=u'calefaccionText', parent=self, pos=wx.Point(542, 39), size=wx.Size(60, 13), style=0)
        self.refrigeracionText = wx.StaticText(id=wxID_PANEL1CALEFACTEXT, label=_(u'Refrigeraci\xf3n'), name=u'refrigeracionText2', parent=self, pos=wx.Point(620, 39), size=wx.Size(70, 13), style=0)
        self.definirMetros2Radio = wx.StaticText(id=wxID_PANEL1DEFINIRMETROS2RADIO, label=_(u'Superficie (m2)'), name=u'definirMetros2Radio', parent=self, pos=wx.Point(435, 58), size=wx.Size(81, 13), style=wx.RB_GROUP)
        self.definirDemandaRadio = wx.StaticText(id=wxID_PANEL1RADIOBUTTON1, label=_(u'Porcentaje (%)'), name='definirDemandaRadio', parent=self, pos=wx.Point(435, 80), size=wx.Size(100, 13), style=0)
        self.coberturaMetros = wx.TextCtrl(id=wxID_PANEL1COBERTURA, name=u'cobertura', parent=self, pos=wx.Point(540, 55), size=wx.Size(60, 21), style=0, value=u'')
        self.coberturaMetros.Bind(wx.EVT_TEXT, self.OnCobertura, id=wxID_PANEL1COBERTURA)
        self.coberturaMetros.SetForegroundColour(wx.Colour(100, 200, 0))
        self.coberturaPorcentaje = wx.TextCtrl(id=wxID_PANEL1COBERTURAPORCEN, name=u'coberturaPorcentaje', parent=self, pos=wx.Point(540, 77), size=wx.Size(60, 21), style=0, value=u'')
        self.coberturaPorcentaje.SetForegroundColour(wx.Colour(100, 200, 0))
        self.coberturaPorcentaje.Bind(wx.EVT_TEXT, self.OnCoberturaPorcentaje, id=wxID_PANEL1COBERTURAPORCEN)
        self.coberturaMetros2 = wx.TextCtrl(id=wxID_PANEL1COBERTURA2, name=u'coberturaMetros2', parent=self, pos=wx.Point(622, 55), size=wx.Size(60, 21), style=0, value=u'')
        self.coberturaMetros2.SetForegroundColour(wx.Colour(100, 200, 0))
        self.coberturaMetros2.Bind(wx.EVT_TEXT, self.OnCobertura2, id=wxID_PANEL1COBERTURA2)
        self.coberturaPorcentaje2 = wx.TextCtrl(id=wxID_PANEL1COBERTURAPORCEN2, name=u'coberturaPorcentaje2', parent=self, pos=wx.Point(622, 77), size=wx.Size(60, 21), style=0, value=u'')
        self.coberturaPorcentaje2.SetForegroundColour(wx.Colour(100, 200, 0))
        self.coberturaPorcentaje2.Bind(wx.EVT_TEXT, self.OnCoberturaPorcentaje2, id=wxID_PANEL1COBERTURAPORCEN2)
        self.EficienciaLineaText = wx.StaticBox(id=wxID_EFICIENCIALINEATEXT, label=_(u'Rendimiento medio estacional'), name='EficienciaLineaText', parent=self, pos=wx.Point(0, 107), size=wx.Size(710, 135), style=0)
        self.EficienciaLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.EficienciaLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.rendimientoText = wx.StaticText(id=wxID_PANEL1RENDIMIENTOTEXT, label=_(u'Rendimiento estacional'), name=u'rendimientoText', parent=self, pos=wx.Point(15, 130), size=wx.Size(150, 25), style=0)
        self.rendimientoText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.rendimientoChoice = MiChoice(choices=self.parent.listadoOpcionesInstalacionesMixtos, id=wxID_PANEL1CHOICE1, name='rendimientoChoice', parent=self, pos=wx.Point(170, 128), size=wx.Size(220, 21), style=0)
        self.rendimientoChoice.SetSelection(1)
        self.rendimientoChoice.Bind(wx.EVT_CHOICE, self.OnrendimientoChoice, id=wxID_PANEL1CHOICE1)
        self.calefaccionText = wx.StaticText(id=wxID_PANEL1CALEFACTEXT, label=_(u'Calefacci\xf3n'), name=u'calefaccionText', parent=self, pos=wx.Point(15, 180), size=wx.Size(100, 13), style=0)
        self.calefaccionText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, u''))
        self.calefaccionText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.refrigeracionText = wx.StaticText(id=wxID_PANEL1CALEFACTEXT, label=_(u'Refrigeraci\xf3n'), name=u'refrigeracionText2', parent=self, pos=wx.Point(15, 205), size=wx.Size(100, 13), style=0)
        self.refrigeracionText.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, u''))
        self.refrigeracionText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.definirAntiguedadText = wx.StaticText(id=wxID_PANEL1ANTIEQUIPOTEXT, label=_(u'Antig\xfcedad del equipo'), name=u'definirAntiguedadText', parent=self, pos=wx.Point(15, 155), size=wx.Size(120, 13), style=0)
        self.definirAntiguedadText.Show(False)
        self.definirAntiguedadChoice = MiChoice(choices=listadosWeb.listadoOpcionesAntiguedad, id=wxID_PANEL1ANTIGUEDADCHOICE, name=u'antiguedadChoice', parent=self, pos=wx.Point(170, 153), size=wx.Size(135, 21), style=0)
        self.definirAntiguedadChoice.SetSelection(2)
        self.definirAntiguedadChoice.Bind(wx.EVT_CHOICE, self.OnAntiguedadChoice, id=wxID_PANEL1ANTIGUEDADCHOICE)
        self.definirAntiguedadChoice.Show(False)
        self.rendimientoNominalText = wx.StaticText(id=wxID_PANEL1RENDNOMINALTEXT, label=_(u'Rendimiento nominal'), name=u'rendimientoNominalText', parent=self, pos=wx.Point(170, 180), size=wx.Size(100, 13), style=0)
        self.rendimientoNominal = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTONOMINAL, name=u'rendimientoNominal', parent=self, pos=wx.Point(275, 178), size=wx.Size(80, 21), style=0)
        copNominalDefecto = diccCOPNominalDefecto[self.definirAntiguedadChoice.GetSelection()]
        self.rendimientoNominal.SetValue('%s' % copNominalDefecto)
        self.rendimientoNominal.SetForegroundColour(wx.Colour(100, 200, 0))
        self.rendimientoNominal.Show(True)
        self.rendimientoNominal.Bind(wx.EVT_TEXT, self.OnRendimientoNominal, id=wxID_PANEL1RENDIMIENTONOMINAL)
        self.rendimientoNominalUnidadesText = wx.StaticText(id=wxID_PANEL1RENDNOMINALUNITEXT, label=_(u'%'), name=u'rendimientoNominalUnidadesText', parent=self, pos=wx.Point(360, 180), size=wx.Size(15, 13), style=0)
        self.rendimientoMedioText = wx.StaticText(id=wxID_PANEL1RENDIMIENTOMEDIOTEXT, label=_(u'Rendimiento medio estacional'), name=u'rendimientoMedioText', parent=self, pos=wx.Point(170, 180), size=wx.Size(200, 13), style=0)
        self.rendimientoMedioText.Show(False)
        self.rendimietoMedio = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTOMEDIO, name=u'rendimietoMedio', parent=self, pos=wx.Point(375, 178), size=wx.Size(80, 21), style=0)
        self.rendimietoMedio.Show(False)
        self.rendimietoMedio.Bind(wx.EVT_TEXT, self.obtenerRendimientoEstacional, id=wxID_PANEL1RENDIMIENTOMEDIO)
        self.rendimientoMedioUnidadesText = wx.StaticText(id=wxID_PANEL1RENDIMIENTOMEDIOTEXT, label=_(u'%'), name=u'rendimientoMedioUnidadesText', parent=self, pos=wx.Point(460, 180), size=wx.Size(15, 13), style=0)
        self.rendimientoMedioUnidadesText.Show(False)
        self.rendimientoNominalText2 = wx.StaticText(id=wxID_PANEL1RENDNOMINALTEXT2, label=_(u'Rendimiento nominal'), name=u'rendimientoNominalText2', parent=self, pos=wx.Point(170, 205), size=wx.Size(100, 13), style=0)
        self.rendimientoNominal2 = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTONOMINAL2, name=u'rendimientoNominal2', parent=self, pos=wx.Point(275, 203), size=wx.Size(80, 21), style=0)
        eerNominalDefecto = diccEERNominalDefecto[self.definirAntiguedadChoice.GetSelection()]
        self.rendimientoNominal2.SetValue('%s' % eerNominalDefecto)
        self.rendimientoNominal2.Show(True)
        self.rendimientoNominal2.SetForegroundColour(wx.Colour(100, 200, 0))
        self.rendimientoNominal2.Bind(wx.EVT_TEXT, self.OnRendimientoNominal2, id=wxID_PANEL1RENDIMIENTONOMINAL2)
        self.rendimientoNominalUnidadesText2 = wx.StaticText(id=wxID_PANEL1RENDNOMINALUNITEXT2, label=_(u'%'), name=u'rendimientoNominalUnidadesText2', parent=self, pos=wx.Point(360, 205), size=wx.Size(15, 13), style=0)
        self.rendimientoMedioText2 = wx.StaticText(id=wxID_PANEL1RENDIMIENTOMEDIOTEXT2, label=_(u'Rendimiento medio estacional'), name=u'rendimientoMedioText2', parent=self, pos=wx.Point(170, 205), size=wx.Size(200, 13), style=0)
        self.rendimientoMedioText2.Show(False)
        self.rendimietoMedio2 = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTOMEDIO2, name=u'rendimietoMedio2', parent=self, pos=wx.Point(375, 203), size=wx.Size(80, 21), style=0)
        self.rendimietoMedio2.Show(False)
        self.rendimietoMedio2.Bind(wx.EVT_TEXT, self.obtenerRendimientoEstacional, id=wxID_PANEL1RENDIMIENTOMEDIO2)
        self.rendimientoMedioUnidadesText2 = wx.StaticText(id=wxID_PANEL1RENDIMIENTOMEDIOTEXT2, label=_(u'%'), name=u'rendimientoMedioUnidadesText2', parent=self, pos=wx.Point(460, 205), size=wx.Size(15, 13), style=0)
        self.rendimientoMedioUnidadesText2.Show(False)
        self.rendimientoGlobalTextCal = wx.StaticText(id=wxID_PANEL1RENDGLOBALTEXTCAL, label=_(u'Rendimiento medio estacional'), name=u'rendimientoGlobalTextCal', parent=self, pos=wx.Point(435, 180), size=wx.Size(150, 13), style=0)
        self.rendimientoGlobalTextCal.Show(True)
        self.rendimientoGlobalTextCal.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.rendimientoGlobalCal = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTOGLOBALCAL, name=u'rendimientoGlobalCal', parent=self, pos=wx.Point(617, 178), size=wx.Size(60, 21), style=0)
        self.rendimientoGlobalCal.Show(True)
        self.rendimientoGlobalCal.Enable(False)
        self.rendimientoGlobalUnidadesTextCal = wx.StaticText(id=wxID_PANEL1RENDGLOBALUNITEXTCAL, label=_(u'%'), name=u'rendimientoGlobalUnidadesText', parent=self, pos=wx.Point(682, 180), size=wx.Size(15, 13), style=0)
        self.rendimientoGlobalUnidadesTextCal.Show(True)
        self.rendimientoGlobalUnidadesTextCal.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.rendimientoGlobalTextRef = wx.StaticText(id=wxID_PANEL1RENDGLOBALTEXTREF, label=_(u'Rendimiento medio estacional'), name=u'rendimientoGlobalTextRef', parent=self, pos=wx.Point(435, 205), size=wx.Size(150, 13), style=0)
        self.rendimientoGlobalTextRef.Show(True)
        self.rendimientoGlobalTextRef.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.rendimientoGlobalRef = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTOGLOBALREF, name=u'rendimientoGlobalRef', parent=self, pos=wx.Point(617, 203), size=wx.Size(60, 21), style=0)
        self.rendimientoGlobalRef.Show(True)
        self.rendimientoGlobalRef.Enable(False)
        self.rendimientoGlobalUnidadesTextRef = wx.StaticText(id=wxID_PANEL1RENDGLOBALUNITEXTREF, label=_(u'%'), name=u'rendimientoGlobalUnidadesText', parent=self, pos=wx.Point(682, 205), size=wx.Size(15, 13), style=0)
        self.rendimientoGlobalUnidadesTextRef.Show(True)
        self.rendimientoGlobalUnidadesTextRef.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.rendimientoGlobalTextCal.SetForegroundColour(wx.Colour(100, 100, 100))
        self.rendimientoGlobalUnidadesTextCal.SetForegroundColour(wx.Colour(100, 100, 100))
        self.rendimientoGlobalTextRef.SetForegroundColour(wx.Colour(100, 100, 100))
        self.rendimientoGlobalUnidadesTextRef.SetForegroundColour(wx.Colour(100, 100, 100))

    def OnsubgrupoChoice(self, event):
        """
        Metodo: OnsubgrupoChoice
        Al cambiar el subgrupo, pongo los porcentajes de cobertura al 100%, y se llama a OnCoberturaPorcentaje() y
        OnCoberturaPorcentaje2() por la acci\xf3n del SetValue()
        
        ARGUMENTOS:
                event:
        """
        self.coberturaPorcentaje.SetValue('100')
        self.coberturaPorcentaje2.SetValue('100')

    def OnNombreInstalacion(self, event):
        """
        Metodo: OnNombreInstalacion
        
        
        ARGUMENTOS:
                event:
        """
        if self.nombreInstalacion.GetValue() == _(u'Calefacci\xf3n y refrigeraci\xf3n'):
            self.nombreInstalacion.SetForegroundColour(wx.Colour(100, 200, 0))
        else:
            self.nombreInstalacion.SetForegroundColour(wx.Colour(0, 0, 0))

    def actualizarRendimientoNominalEquiposElectricos(self):
        """
        M\xe9todo: actualizarRendimientoNominalEquiposElectricos
        Si ha cambiado a equipo efecto joule o caldera, en rendimiento nominal se pone 100 %
        
        """
        try:
            float(self.rendimientoNominal.GetValue())
            valorValido = True
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            valorValido = False

        listadoValoresStr = [ str(x) for x in diccCOPNominalDefecto.values() ]
        if self.rendimientoNominal.GetValue() in listadoValoresStr or valorValido == False:
            rendNominalDefecto = diccCOPNominalDefecto[self.definirAntiguedadChoice.GetSelection()]
            self.rendimientoNominal.SetValue('%s' % rendNominalDefecto)
            self.rendimientoNominal.SetForegroundColour(wx.Colour(100, 200, 0))
        try:
            float(self.rendimientoNominal2.GetValue())
            valorValido = True
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            valorValido = False

        listadoValoresStr = [ str(x) for x in diccEERNominalDefecto.values() ]
        if self.rendimientoNominal2.GetValue() in listadoValoresStr or valorValido == False:
            rendNominalDefecto = diccEERNominalDefecto[self.definirAntiguedadChoice.GetSelection()]
            self.rendimientoNominal2.SetValue('%s' % rendNominalDefecto)
            self.rendimientoNominal2.SetForegroundColour(wx.Colour(100, 200, 0))

    def OnAntiguedadChoice(self, event):
        self.actualizarRendimientoNominalEquiposElectricos()
        self.obtenerRendimientoEstacional(None)
        return

    def OnRendimientoNominal(self, event):
        """
        Metodo: OnRendimientoNominal
        
        
        ARGUMENTOS:
                event:
        """
        try:
            copNominalDefecto = diccCOPNominalDefecto[self.definirAntiguedadChoice.GetSelection()]
            if float(self.rendimientoNominal.GetValue()) == copNominalDefecto:
                self.rendimientoNominal.SetForegroundColour(wx.Colour(100, 200, 0))
            else:
                self.rendimientoNominal.SetForegroundColour(wx.Colour(0, 0, 0))
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        self.obtenerRendimientoEstacional(None)
        return

    def OnRendimientoNominal2(self, event):
        """
        Metodo: OnRendimientoNominal2
        
        
        ARGUMENTOS:
                event:
        """
        eerNominalDefecto = diccEERNominalDefecto[self.definirAntiguedadChoice.GetSelection()]
        try:
            if float(self.rendimientoNominal2.GetValue()) == eerNominalDefecto:
                self.rendimientoNominal2.SetForegroundColour(wx.Colour(100, 200, 0))
            else:
                self.rendimientoNominal2.SetForegroundColour(wx.Colour(0, 0, 0))
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        self.obtenerRendimientoEstacional(None)
        return

    def OnCobertura(self, event):
        """
        Metodo: OnCobertura
        
        
        ARGUMENTOS:
                event:
        """
        if self.booleano == True:
            self.booleano = False
            if self.subgrupoChoice.GetStringSelection() == u'Edificio Objeto':
                try:
                    superficieTotal = float(self.parent.parent.parent.panelDatosGenerales.superficie.GetValue())
                    superficieActual = float(self.coberturaMetros.GetValue())
                    porcentaje = round(superficieActual * 100 / superficieTotal, 2)
                    self.coberturaPorcentaje.SetValue(str(porcentaje))
                except (ValueError, TypeError):
                    self.coberturaPorcentaje.SetValue('')
                except ZeroDivisionError:
                    self.coberturaPorcentaje.SetValue('')

            else:
                for i in self.parent.parent.subgrupos:
                    if i.nombre == self.subgrupoChoice.GetStringSelection():
                        mTotales = float(i.superficie)
                        break

                try:
                    mActuales = float(self.coberturaMetros.GetValue())
                    porcentaje = round(mActuales * 100 / mTotales, 2)
                    self.coberturaPorcentaje.SetValue(str(porcentaje))
                except (ValueError, TypeError):
                    self.coberturaPorcentaje.SetValue('')
                except ZeroDivisionError:
                    self.coberturaPorcentaje.SetValue('')

            self.booleano = True

    def OnCoberturaPorcentaje(self, event):
        """
        Metodo: OnCoberturaPorcentaje
        
        
        ARGUMENTOS:
                event:
        """
        if self.booleano == True:
            self.booleano = False
            if self.subgrupoChoice.GetStringSelection() == u'Edificio Objeto':
                try:
                    superficieTotal = float(self.parent.parent.parent.panelDatosGenerales.superficie.GetValue())
                    porcentajeActual = float(self.coberturaPorcentaje.GetValue())
                    mAcuales = round(porcentajeActual * superficieTotal / 100.0, 2)
                    self.coberturaMetros.SetValue(str(mAcuales))
                except (ValueError, TypeError):
                    self.coberturaMetros.SetValue('')
                except ZeroDivisionError:
                    self.coberturaMetros.SetValue('')

            else:
                for i in self.parent.parent.subgrupos:
                    if i.nombre == self.subgrupoChoice.GetStringSelection():
                        mTotales = float(i.superficie)
                        break

                try:
                    porcentaje = float(self.coberturaPorcentaje.GetValue())
                    mAcuales = round(porcentaje * mTotales / 100.0, 2)
                    self.coberturaMetros.SetValue(str(mAcuales))
                except (ValueError, TypeError):
                    self.coberturaMetros.SetValue('')
                except ZeroDivisionError:
                    self.coberturaMetros.SetValue('')

            self.booleano = True

    def OnCobertura2(self, event):
        """
        Metodo: OnCobertura2
        
        
        ARGUMENTOS:
                event:
        """
        if self.booleano == True:
            self.booleano = False
            if self.subgrupoChoice.GetStringSelection() == u'Edificio Objeto':
                try:
                    superficieTotal = float(self.parent.parent.parent.panelDatosGenerales.superficie.GetValue())
                    superficieActual = float(self.coberturaMetros2.GetValue())
                    porcentaje = round(superficieActual * 100 / superficieTotal, 2)
                    self.coberturaPorcentaje2.SetValue(str(porcentaje))
                except (ValueError, TypeError):
                    self.coberturaPorcentaje2.SetValue('')
                except ZeroDivisionError:
                    self.coberturaPorcentaje2.SetValue('')

            else:
                for i in self.parent.parent.subgrupos:
                    if i.nombre == self.subgrupoChoice.GetStringSelection():
                        mTotales = float(i.superficie)
                        break

                try:
                    mActuales = float(self.coberturaMetros2.GetValue())
                    porcentaje = round(mActuales * 100 / mTotales, 2)
                    self.coberturaPorcentaje2.SetValue(str(porcentaje))
                except (ValueError, TypeError):
                    self.coberturaPorcentaje2.SetValue('')
                except ZeroDivisionError:
                    self.coberturaPorcentaje2.SetValue('')

            self.booleano = True

    def OnCoberturaPorcentaje2(self, event):
        """
        Metodo: OnCoberturaPorcentaje2
        
        
        ARGUMENTOS:
                event:
        """
        if self.booleano == True:
            self.booleano = False
            if self.subgrupoChoice.GetStringSelection() == u'Edificio Objeto':
                try:
                    superficieTotal = float(self.parent.parent.parent.panelDatosGenerales.superficie.GetValue())
                    porcentajeActual = float(self.coberturaPorcentaje2.GetValue())
                    mAcuales = round(porcentajeActual * superficieTotal / 100.0, 2)
                    self.coberturaMetros2.SetValue(str(mAcuales))
                except (ValueError, TypeError):
                    self.coberturaMetros2.SetValue('')
                except ZeroDivisionError:
                    self.coberturaMetros2.SetValue('')

            else:
                for i in self.parent.parent.subgrupos:
                    if i.nombre == self.subgrupoChoice.GetStringSelection():
                        mTotales = float(i.superficie)
                        break

                try:
                    porcentaje = float(self.coberturaPorcentaje2.GetValue())
                    mAcuales = round(porcentaje * mTotales / 100.0, 2)
                    self.coberturaMetros2.SetValue(str(mAcuales))
                except (ValueError, TypeError):
                    self.coberturaMetros2.SetValue('')
                except ZeroDivisionError:
                    self.coberturaMetros2.SetValue('')

            self.booleano = True

    def __init__(self, parent, id, pos, size, style, name, real_parent = None):
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
        self.booleano = True
        self._init_ctrls(parent, id, pos, size, style, name)
        self.tipoSistema = 'climatizacion'
        self.listaErrores = u''
        self.subgrupoChoice.SetItems(self.cargarRaices())
        self.OnrendimientoChoice(None)
        self.elegirRaiz()
        self.rendimientoEstacionalRef = ''
        self.rendimientoEstacionalCal = ''
        self.obtenerRendimientoEstacional(None)
        return

    def obtenerRendimientoEstacional(self, event):
        """
        Metodo: obtenerRendimientoEstacional
        
        
        ARGUMENTOS:
                event):  #funcion para otener el rendimiento medio estacion:
        """
        kwargsConocido = {'rendEstACS': '',
         'rendEstCal': self.rendimietoMedio.GetValue(),
         'rendEstRef': self.rendimietoMedio2.GetValue()}
        kwargsBdCEst = {'rendNominalACS': '',
         'rendNominalCal': self.rendimientoNominal.GetValue(),
         'rendNominalRef': self.rendimientoNominal2.GetValue(),
         'variosGeneradoresCheck': False,
         'fraccionPotencia': '',
         'fraccionPotenciaEntrada': ''}
        kwargs = {}
        kwargs.update(kwargsConocido)
        kwargs.update(kwargsBdCEst)
        zonaHE1 = self.parent.parent.parent.panelDatosGenerales.HE1.GetStringSelection()
        programa = self.parent.parent.parent.programa
        tipoEdificio = self.parent.parent.parent.panelDatosGenerales.tipoEdificioChoice.GetStringSelection()
        modoDefinicion = self.rendimientoChoice.GetStringSelection()
        tipoEquipo = self.generadorChoice.GetStringSelection()
        combustible = self.combustibleChoice.GetStringSelection()
        resultado = calculoRendimientoMedioEstacional(zonaHE1=zonaHE1, programa=programa, tipoEdificio=tipoEdificio, tipoInstalacion=self.tipoSistema, modoDefinicion=modoDefinicion, tipoEquipo=tipoEquipo, combustible=combustible, **kwargs)
        self.rendimientoEstacionalCal, self.rendimientoEstacionalRef = resultado
        self.escribirRendimientoGlobal()

    def escribirRendimientoGlobal(self):
        """
        Metodo: escribirRendimientoGlobal
        
        
        """
        self.rendimientoGlobalCal.SetValue(str(self.rendimientoEstacionalCal))
        self.rendimientoGlobalRef.SetValue(str(self.rendimientoEstacionalRef))

    def elegirRaiz(self):
        """
        Metodo: elegirRaiz
        
        
        """
        sel = self.parent.arbolInstalaciones.GetSelection()
        try:
            self.subgrupoChoice.SetStringSelection(u'Edificio Objeto')
            raiz = self.parent.arbolInstalaciones.GetRootItem()
            while sel != raiz:
                for i in range(len(self.parent.parent.subgrupos)):
                    if self.parent.arbolInstalaciones.GetItemText(sel) == self.parent.parent.subgrupos[i].nombre:
                        self.subgrupoChoice.SetStringSelection(self.parent.arbolInstalaciones.GetItemText(sel))
                        self.OnsubgrupoChoice(None)
                        return

                sel = self.parent.arbolInstalaciones.GetItemParent(sel)

        except:
            logging.info(u'Excepcion en: %s' % __name__)
            self.subgrupoChoice.SetStringSelection(u'Edificio Objeto')

        self.OnsubgrupoChoice(None)
        return

    def cargarRaices(self):
        """
        Metodo: cargarRaices
        
        
        """
        raices = []
        raices.append((u'Edificio Objeto', _(u'Edificio Objeto')))
        for i in range(len(self.parent.parent.subgrupos)):
            if self.parent.parent.subgrupos[i].nombre != u'Edificio Objeto':
                raices.append((self.parent.parent.subgrupos[i].nombre, self.parent.parent.subgrupos[i].nombre))

        return raices

    def OngeneradorChoice(self, event):
        """
        Metodo: OngeneradorChoice
        
        
        ARGUMENTOS:
                event:
        """
        antes = self.rendimientoChoice.GetStringSelection()
        if u'Equipo de Rendimiento Constante' == self.generadorChoice.GetStringSelection():
            self.rendimientoChoice.SetItems([self.parent.listadoOpcionesInstalacionesMixtos[0]])
            self.rendimientoChoice.SetSelection(0)
        else:
            self.rendimientoChoice.SetItems(self.parent.listadoOpcionesInstalacionesMixtos)
            self.rendimientoChoice.SetStringSelection(antes)
        self.OnrendimientoChoice(None)
        return

    def OnrendimientoChoice(self, event):
        """
        Metodo: OnrendimientoChoice
        
        
        ARGUMENTOS:
                event:
        Se llama al cambiar de tipo de equipo, o de modoDefini\xf3n
        """
        if 'Conocido' in self.rendimientoChoice.GetStringSelection():
            self.rendimientoMedioText.Show(True)
            self.rendimietoMedio.Show(True)
            self.rendimientoMedioUnidadesText.Show(True)
            self.rendimientoNominalText.Show(False)
            self.rendimientoNominal.Show(False)
            self.rendimientoNominalUnidadesText.Show(False)
            self.definirAntiguedadChoice.Show(False)
            self.definirAntiguedadText.Show(False)
            self.rendimientoMedioText2.Show(True)
            self.rendimietoMedio2.Show(True)
            self.rendimientoMedioUnidadesText2.Show(True)
            self.rendimientoNominalText2.Show(False)
            self.rendimientoNominal2.Show(False)
            self.rendimientoNominalUnidadesText2.Show(False)
            self.rendimientoGlobalTextCal.Show(False)
            self.rendimientoGlobalCal.Show(False)
            self.rendimientoGlobalUnidadesTextCal.Show(False)
            self.rendimientoGlobalTextRef.Show(False)
            self.rendimientoGlobalRef.Show(False)
            self.rendimientoGlobalUnidadesTextRef.Show(False)
        else:
            self.rendimientoMedioText.Show(False)
            self.rendimietoMedio.Show(False)
            self.rendimientoMedioUnidadesText.Show(False)
            self.rendimientoNominalText.Show(True)
            self.rendimientoNominal.Show(True)
            self.rendimientoNominalUnidadesText.Show(True)
            self.definirAntiguedadChoice.Show(True)
            self.definirAntiguedadText.Show(True)
            self.rendimientoMedioText2.Show(False)
            self.rendimietoMedio2.Show(False)
            self.rendimientoMedioUnidadesText2.Show(False)
            self.rendimientoNominalText2.Show(True)
            self.rendimientoNominal2.Show(True)
            self.rendimientoNominalUnidadesText2.Show(True)
            self.rendimientoGlobalTextCal.Show(True)
            self.rendimientoGlobalCal.Show(True)
            self.rendimientoGlobalUnidadesTextCal.Show(True)
            self.rendimientoGlobalTextRef.Show(True)
            self.rendimientoGlobalRef.Show(True)
            self.rendimientoGlobalUnidadesTextRef.Show(True)
            self.actualizarRendimientoNominalEquiposElectricos()
        self.obtenerRendimientoEstacional(None)
        return

    def comprobarDatos(self):
        """
        Metodo: comprobarDatos
        
        
        """
        dato = self.coberturaMetros.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.coberturaMetros.SetValue(dato)
        dato = self.coberturaPorcentaje.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.coberturaPorcentaje.SetValue(dato)
        dato = self.coberturaMetros2.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.coberturaMetros2.SetValue(dato)
        dato = self.coberturaPorcentaje2.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.coberturaPorcentaje2.SetValue(dato)
        dato = self.rendimietoMedio.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.rendimietoMedio.SetValue(dato)
        dato = self.rendimietoMedio2.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.rendimietoMedio2.SetValue(dato)
        dato = self.rendimientoNominal.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.rendimientoNominal.SetValue(dato)
        dato = self.rendimientoNominal2.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.rendimientoNominal2.SetValue(dato)
        self.listaErrores = u''
        self.listaErrores += Comprueba(self.nombreInstalacion.GetValue(), 1, self.listaErrores, _(u'nombre')).ErrorDevuelto
        self.listaErrores += Comprueba(self.subgrupoChoice.GetStringSelection(), 0, self.listaErrores, _(u'zona')).ErrorDevuelto
        self.listaErrores += Comprueba(self.generadorChoice.GetStringSelection(), 0, self.listaErrores, _(u'tipo de generador')).ErrorDevuelto
        self.listaErrores += Comprueba(self.combustibleChoice.GetStringSelection(), 0, self.listaErrores, _(u'tipo de combustible')).ErrorDevuelto
        self.listaErrores += Comprueba(self.rendimientoChoice.GetStringSelection(), 0, self.listaErrores, _(u'definir rendimiento')).ErrorDevuelto
        rendi = self.rendimientoChoice.GetStringSelection()
        if self.parent.parent.parent.panelDatosGenerales.superficie.GetValue() == '':
            self.listaErrores += Comprueba2(self.coberturaPorcentaje.GetValue(), 2, self.listaErrores, _(u'porcentaje de demanda (calefacci\xf3n) de la zona cubierto'), 0, 100).ErrorDevuelto
        else:
            self.listaErrores += Comprueba2(self.coberturaPorcentaje.GetValue(), 2, self.listaErrores, _(u'porcentaje de demanda de la zona cubierto o m2 cubiertos por el equipo (calefacci\xf3n)'), 0, 100).ErrorDevuelto
        if self.parent.parent.parent.panelDatosGenerales.superficie.GetValue() == '':
            self.listaErrores += Comprueba2(self.coberturaPorcentaje2.GetValue(), 2, self.listaErrores, _(u'porcentaje de demanda (refrigeraci\xf3n) de la zona cubierto'), 0, 100).ErrorDevuelto
        else:
            self.listaErrores += Comprueba2(self.coberturaPorcentaje2.GetValue(), 2, self.listaErrores, _(u'porcentaje de demanda de la zona cubierto o m2 cubiertos por el equipo (refrigeraci\xf3n)'), 0, 100).ErrorDevuelto
        if 'Conocido' in rendi:
            self.listaErrores += Comprueba(self.rendimietoMedio.GetValue(), 2, self.listaErrores, _(u'rendimiento medio estacional (calefacci\xf3n)'), 0).ErrorDevuelto
            self.listaErrores += Comprueba(self.rendimietoMedio2.GetValue(), 2, self.listaErrores, _(u'rendimiento medio estacional (refrigeraci\xf3n)'), 0).ErrorDevuelto
        else:
            self.listaErrores += Comprueba(self.rendimientoNominal.GetValue(), 2, self.listaErrores, _(u'rendimiento nominal (calefacci\xf3n)'), 0.09).ErrorDevuelto
            self.listaErrores += Comprueba(self.rendimientoNominal2.GetValue(), 2, self.listaErrores, _(u'rendimiento nominal (refrigeraci\xf3n)'), 0.09).ErrorDevuelto
        if u'Conocido' not in rendi and self.listaErrores == '':
            if self.rendimientoEstacionalCal != '':
                self.listaErrores += Comprueba(str(self.rendimientoEstacionalCal), 2, self.listaErrores, _(u'rendimiento medio estacional para calefacci\xf3n'), 0.0).ErrorDevuelto
            if self.rendimientoEstacionalRef != '':
                self.listaErrores += Comprueba(str(self.rendimientoEstacionalRef), 2, self.listaErrores, _(u'rendimiento medio estacional para refrigeraci\xf3n'), 0.0).ErrorDevuelto