# Embedded file name: Instalaciones\panelIluminacion.pyc
"""
Modulo: panelIluminacion.py

"""
from Instalaciones.comprobarCampos import Comprueba
from miChoice import MiChoice
import Calculos.listadosWeb as listadosWeb
from Calculos.funcionesCalculo import diccLuminarias
import wx
import logging
wxID_PANEL1, wxID_PANEL1CHOICE1, wxID_PANEL1CHOICE2, wxID_PANEL1DEFINIRSEGUNCHOICE, wxID_PANEL1DEFINIRSEGUNTEXT, wxID_PANEL1NOMBREINSTALACION, wxID_PANEL1NOMBREINSTALACIONTEXT, wxID_PANEL1SUBGRUPOCHOICE, wxID_PANEL1SUBGRUPOTEXT, wxID_PANEL1SUPERFICIEMURO, wxID_PANEL1SUPERFICIETEXT, wxID_PANEL1SUPERFICIEUNIDADESTEXT, wxID_PANEL1TIPOLOCALTEXT, wxID_PANEL1USOTEXT, wxID_PANEL1ZONAREPRESENTACIONCHECK, wxID_PANEL1DEFINIRTEXT, wxID_PANEL1DEFINIRCHOICE, wxID_PANEL1POTENCIAINSTALDATEXT, wxID_PANEL1POTENCIAINSTALDA, wxID_PANEL1POTENCIAUNIDDESTEXT, wxID_PANEL1ILUMINANCIATEXT, wxID_PANEL1ILUMINANCIA, wxID_PANEL1ILUMINANCIAUNIDDESTEXT, wxID_PANEL1TIPOEQUIPOTEXT, wxID_PANEL1TIPOEQUIPOTEXT, wxID_PANEL1DEFINIRCHOICE, wxID_PANEL1ILUMIHELPBOTON, wxID_PANEL1SINCONTROL, wxID_PANEL1CONCONTROL, wxID_PANEL1SUPERFICIECONTROLTEXT, wxID_PANEL1SUPERFICIECONTROL, wxID_PANEL1SUPERFICIECONTROLUNIDADES, wxID_CARACTERISTICASLINEATEXT, wxID_DEMANDALINEATEXT = [ wx.NewId() for _init_ctrls in range(34) ]

class Panel1(wx.Panel):
    """
    Clase: Panel1 del modulo panelIluminacion.py
    
    
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
        self.nombreInstalacion = wx.TextCtrl(id=wxID_PANEL1NOMBREINSTALACION, name=u'nombreInstalacion', parent=self, pos=wx.Point(170, 0), size=wx.Size(230, 21), style=0, value=_(u'Iluminaci\xf3n'))
        self.nombreInstalacion.SetForegroundColour(wx.Colour(100, 200, 0))
        self.nombreInstalacion.Bind(wx.EVT_TEXT, self.OnNombreInstalacion, id=wxID_PANEL1NOMBREINSTALACION)
        self.subgrupoText = wx.StaticText(id=wxID_PANEL1SUBGRUPOTEXT, label=_(u'Zona'), name=u'subgrupoText', parent=self, pos=wx.Point(435, 2), size=wx.Size(50, 13), style=0)
        self.subgrupoChoice = MiChoice(choices=[], id=wxID_PANEL1SUBGRUPOCHOICE, name=u'subgrupoChoice', parent=self, pos=wx.Point(496, 0), size=wx.Size(214, 21), style=0)
        self.subgrupoChoice.Bind(wx.EVT_CHOICE, self.onSeleccionarSubgrupo, id=wxID_PANEL1SUBGRUPOCHOICE)
        self.CaracteristicasLineaText = wx.StaticBox(id=wxID_CARACTERISTICASLINEATEXT, label=_(u'Caracter\xedsticas'), name='CaracteristicasLineaText', parent=self, pos=wx.Point(0, 26), size=wx.Size(710, 77), style=0)
        self.CaracteristicasLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.superficieText = wx.StaticText(id=wxID_PANEL1SUPERFICIETEXT, label=_(u'Superficie zona'), name=u'superficieText', parent=self, pos=wx.Point(15, 46), size=wx.Size(115, 13), style=0)
        self.superficieMuro = wx.TextCtrl(id=wxID_PANEL1SUPERFICIEMURO, name=u'superficieMuro', parent=self, pos=wx.Point(170, 44), size=wx.Size(60, 21), style=0, value=u'')
        self.superficieUnidadesText = wx.StaticText(id=wxID_PANEL1SUPERFICIEUNIDADESTEXT, label=_(u'm2'), name=u'superficieUnidadesText', parent=self, pos=wx.Point(235, 46), size=wx.Size(14, 13), style=0)
        self.sinControl = wx.RadioButton(id=wxID_PANEL1SINCONTROL, label=_(u'Sin control de la iluminaci\xf3n'), name=u'sinControl', parent=self, pos=wx.Point(435, 40), size=wx.Size(180, 13), style=0)
        self.sinControl.SetValue(True)
        self.sinControl.Show(False)
        self.sinControl.Bind(wx.EVT_RADIOBUTTON, self.onControlIluminacion, id=wxID_PANEL1SINCONTROL)
        self.conControl = wx.RadioButton(id=wxID_PANEL1CONCONTROL, label=_(u'Con control de la iluminaci\xf3n'), name=u'conControl', parent=self, pos=wx.Point(435, 60), size=wx.Size(180, 13), style=0)
        self.conControl.Show(False)
        self.conControl.Bind(wx.EVT_RADIOBUTTON, self.onControlIluminacion, id=wxID_PANEL1CONCONTROL)
        self.superficieControlText = wx.StaticText(id=wxID_PANEL1SUPERFICIECONTROLTEXT, label=_(u'Superficie con control luminaci\xf3n'), name=u'superficieControlText', parent=self, pos=wx.Point(445, 77), size=wx.Size(170, 13), style=0)
        self.superficieControl = wx.TextCtrl(id=wxID_PANEL1SUPERFICIECONTROL, name=u'superficieMuro', parent=self, pos=wx.Point(617, 79), size=wx.Size(60, 16), style=0, value=u'')
        self.superficieControlUnidades = wx.StaticText(id=wxID_PANEL1SUPERFICIECONTROLUNIDADES, label=_(u'm2'), name=u'superficieControlUnidades', parent=self, pos=wx.Point(682, 79), size=wx.Size(14, 13), style=0)
        self.eficienciaEnergeticaText = wx.StaticBox(id=wxID_DEMANDALINEATEXT, label=_(u'Eficiencia energ\xe9tica'), name='eficienciaEnergeticaText', parent=self, pos=wx.Point(0, 107), size=wx.Size(710, 135), style=0)
        self.eficienciaEnergeticaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.eficienciaEnergeticaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.zonaRepresentacionCheck = wx.CheckBox(id=wxID_PANEL1ZONAREPRESENTACIONCHECK, label=_(u'Zona de representaci\xf3n'), name=u'zonaRepresentacionCheck', parent=self, pos=wx.Point(15, 130), size=wx.Size(150, 13), style=0)
        self.zonaRepresentacionCheck.SetValue(False)
        self.zonaRepresentacionCheck.Bind(wx.EVT_CHECKBOX, self.onZonasRadio, id=wxID_PANEL1ZONAREPRESENTACIONCHECK)
        self.usoText = wx.StaticText(id=wxID_PANEL1USOTEXT, label=_(u'Actividad'), name=u'usoText', parent=self, pos=wx.Point(230, 127), size=wx.Size(70, 13), style=0)
        self.usoChoice = MiChoice(choices=listadosWeb.tablaZona1, id=wxID_PANEL1CHOICE1, name='usoChoice', parent=self, pos=wx.Point(304, 125), size=wx.Size(392, 21), style=0)
        self.usoChoice.SetSelection(0)
        self.usoChoice.Bind(wx.EVT_CHOICE, self.valoresPorDefectoIluminancia, id=wxID_PANEL1CHOICE1)
        self.definirSegunText = wx.StaticText(id=wxID_PANEL1DEFINIRTEXT, label=_(u'Definir caracter\xedsticas'), name=u'definirSegunText', parent=self, pos=wx.Point(15, 155), size=wx.Size(150, 13), style=0)
        self.definirSegunChoice = MiChoice(choices=listadosWeb.listadoOpcionesIluminacion, id=wxID_PANEL1DEFINIRCHOICE, name=u'definirSegunChoice', parent=self, pos=wx.Point(170, 153), size=wx.Size(220, 21), style=0)
        self.definirSegunChoice.SetSelection(0)
        self.definirSegunChoice.Bind(wx.EVT_CHOICE, self.onDefinirSegunChoice, id=wxID_PANEL1DEFINIRCHOICE)
        self.potenciaInstaladaText = wx.StaticText(id=wxID_PANEL1POTENCIAINSTALDATEXT, label=_(u'Potencia instalada'), name=u'potenciaInstaladaText', parent=self, pos=wx.Point(15, 180), size=wx.Size(150, 13), style=0)
        self.potenciaInstalada = wx.TextCtrl(id=wxID_PANEL1POTENCIAINSTALDA, name=u'potenciaInstalada', parent=self, pos=wx.Point(170, 178), size=wx.Size(60, 21), style=0, value=u'')
        self.potenciaInstaladaUnidadesText = wx.StaticText(id=wxID_PANEL1POTENCIAUNIDDESTEXT, label=_(u'W'), name=u'potenciaInstaladaUnidadesText', parent=self, pos=wx.Point(235, 180), size=wx.Size(14, 13), style=0)
        self.tipoEquipoText = wx.StaticText(id=wxID_PANEL1TIPOEQUIPOTEXT, label=_(u'Tipo de equipo'), name=u'tipoEquipoText', parent=self, pos=wx.Point(15, 180), size=wx.Size(150, 13), style=0)
        self.tipoEquipoText.Show(False)
        self.tipoEquipoChoice = MiChoice(choices=listadosWeb.listaTipoEquipo, id=wxID_PANEL1DEFINIRCHOICE, name=u'tipoEquipoChoice', parent=self, pos=wx.Point(170, 178), size=wx.Size(220, 21), style=0)
        self.tipoEquipoChoice.Show(False)
        self.iluminanciaText = wx.StaticText(id=wxID_PANEL1ILUMINANCIATEXT, label=_(u'Iluminancia media horizontal'), name=u'iluminanciaText', parent=self, pos=wx.Point(15, 205), size=wx.Size(150, 13), style=0)
        self.iluminancia = wx.TextCtrl(id=wxID_PANEL1ILUMINANCIA, name=u'iluminancia', parent=self, pos=wx.Point(170, 203), size=wx.Size(60, 21), style=0, value=u'')
        self.iluminancia.Bind(wx.EVT_TEXT, self.OnCambioIluminancia, id=wxID_PANEL1ILUMINANCIA)
        self.iluminanciaUnidadesText = wx.StaticText(id=wxID_PANEL1ILUMINANCIAUNIDDESTEXT, label=_(u'lux'), name=u'iluminanciaUnidadesText', parent=self, pos=wx.Point(235, 205), size=wx.Size(20, 13), style=0)

    def OnNombreInstalacion(self, event):
        """
        Metodo: OnNombreInstalacion
        
        
        ARGUMENTOS:
                event:
        """
        if self.nombreInstalacion.GetValue() == _(u'Iluminaci\xf3n'):
            self.nombreInstalacion.SetForegroundColour(wx.Colour(100, 200, 0))
        else:
            self.nombreInstalacion.SetForegroundColour(wx.Colour(0, 0, 0))

    def __init__(self, parent, id, pos, size, style, name, real_parent = None, instalacionIluminacion = None):
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
                 instalacionIluminacion = None:
        """
        if real_parent == None:
            self.parent = parent
        else:
            self.parent = real_parent
        if instalacionIluminacion != None:
            instalacionIluminacionAntigua = instalacionIluminacion
        self.potencia = 0
        self.veei = 0
        self.cambiandoIluminancia = False
        self._init_ctrls(parent, id, pos, size, style, name)
        self.tipoSistema = 'iluminacion'
        if self.parent.parent.parent.programa == 'GranTerciario':
            self.sinControl.Show(True)
            self.conControl.Show(True)
            self.onControlIluminacion(True)
            self.superficieMuro.Enable(False)
        else:
            self.sinControl.Show(False)
            self.conControl.Show(False)
            self.superficieControl.Show(False)
            self.superficieControlText.Show(False)
            self.superficieControl.Show(False)
            self.superficieControlUnidades.Show(False)
        self.subgrupoChoice.SetItems(self.cargarRaices(instalacionIluminacionAntigua))
        self.elegirRaiz()
        self.valoresPorDefectoIluminancia(None)
        self.onSeleccionarSubgrupo(None)
        return

    def elegirRaiz(self):
        """
        Metodo: elegirRaiz
        
        
        """
        try:
            sel = self.parent.arbolInstalaciones.GetSelection()
            aux = self.subgrupoChoice.GetItems()
            if aux == []:
                return
            self.subgrupoChoice.SetSelection(0)
            raiz = self.parent.arbolInstalaciones.GetRootItem()
            while sel != raiz:
                for i in range(len(self.parent.parent.subgrupos)):
                    if self.parent.arbolInstalaciones.GetItemText(sel) == '%s' % self.parent.parent.subgrupos[i].nombre:
                        self.subgrupoChoice.SetStringSelection(self.parent.arbolInstalaciones.GetItemText(sel))
                        return

                sel = self.parent.arbolInstalaciones.GetItemParent(sel)

        except:
            logging.info(u'Excepcion en: %s' % __name__)

    def onSeleccionarSubgrupo(self, event):
        """
        Metodo: onSeleccionarSubgrupo
        
        
        ARGUMENTOS:
                event:
        """
        seleccionado = self.subgrupoChoice.GetStringSelection()
        if seleccionado == '':
            seleccionado = u'Edificio Objeto'
        superficieSubZonas = 0
        for sub in self.parent.parent.subgrupos:
            if seleccionado == sub.raiz:
                superficieSubZonas += float(sub.superficie)
            if seleccionado == sub.nombre:
                superficieZona = float(sub.superficie)

        if seleccionado == u'Edificio Objeto':
            superficieZona = self.parent.parent.parent.panelDatosGenerales.superficie.GetValue()
            try:
                if ',' in superficieZona:
                    superficieZona = superficieZona.replace(',', '.')
                    self.parent.parent.parent.superficie.SetValue(superficieZona)
                superficieZona = float(self.parent.parent.parent.panelDatosGenerales.superficie.GetValue())
            except (ValueError, TypeError):
                wx.MessageBox(_(u'Revise la superficie del edificio en el panel de datos generales'), _(u'Aviso'))
                return

        superficie = superficieZona - superficieSubZonas
        if superficie < 0:
            wx.MessageBox(_(u'La superficie de las zonas del edificio es mayor que la superficie del edificio,  revise los valores'), _(u'Aviso'))
            return
        self.superficieMuro.SetValue(str(superficie))

    def cargarRaices(self, instalacionIluminacionAntigua):
        """
        Metodo: cargarRaices
        
        
        ARGUMENTOS:
                 instalacionIluminacionAntigua:
        """
        raices = []
        if self.parent.parent.parent.programa == 'GranTerciario':
            raicesUtilizadas = []
            for ilum in instalacionIluminacionAntigua:
                raicesUtilizadas.append((ilum[-1], ilum[-1]))

            if u'Edificio Objeto' not in raicesUtilizadas:
                raices.append((u'Edificio Objeto', _(u'Edificio Objeto')))
            for i in range(len(self.parent.parent.subgrupos)):
                tuplaRaiz = ('%s' % self.parent.parent.subgrupos[i].nombre, '%s' % self.parent.parent.subgrupos[i].nombre)
                if self.parent.parent.subgrupos[i].nombre != u'Edificio Objeto' and tuplaRaiz not in raicesUtilizadas:
                    raices.append(tuplaRaiz)

        else:
            raices.append((u'Edificio Objeto', _(u'Edificio Objeto')))
            for i in range(len(self.parent.parent.subgrupos)):
                if self.parent.parent.subgrupos[i].nombre != u'Edificio Objeto':
                    raices.append(('%s' % self.parent.parent.subgrupos[i].nombre, '%s' % self.parent.parent.subgrupos[i].nombre))

        return raices

    def onControlIluminacion(self, event):
        """
        Metodo: onControlIluminacion
        
        
        ARGUMENTOS:
                 event:
        """
        if self.sinControl.GetValue() == True and self.parent.parent.parent.programa == 'GranTerciario':
            self.superficieControlText.Show(False)
            self.superficieControl.Show(False)
            self.superficieControlUnidades.Show(False)
        elif self.sinControl.GetValue() == False and self.parent.parent.parent.programa == 'GranTerciario':
            self.superficieControlText.Show(True)
            self.superficieControl.Show(True)
            self.superficieControlUnidades.Show(True)

    def onDefinirSegunChoice(self, event):
        """
        Metodo: onDefinirSegunChoice
        
        
        ARGUMENTOS:
                event:
        """
        if 'Estimado' in self.definirSegunChoice.GetStringSelection():
            self.tipoEquipoText.Show(True)
            self.tipoEquipoChoice.Show(True)
            self.potenciaInstaladaText.Show(False)
            self.potenciaInstalada.Show(False)
            self.potenciaInstaladaUnidadesText.Show(False)
        else:
            self.tipoEquipoText.Show(False)
            self.tipoEquipoChoice.Show(False)
            self.potenciaInstaladaText.Show(True)
            self.potenciaInstalada.Show(True)
            self.potenciaInstaladaUnidadesText.Show(True)

    def onZonasRadio(self, event):
        """
        Metodo: onZonasRadio
        
        
        ARGUMENTOS:
                event:
        """
        antes = self.usoChoice.GetStringSelection()
        if self.zonaRepresentacionCheck.GetValue() == False:
            tabla = listadosWeb.tablaZona1
        else:
            tabla = listadosWeb.tablaZona2
        self.usoChoice.SetItems(tabla)
        if antes in tabla:
            self.usoChoice.SetStringSelection(antes)
        else:
            self.usoChoice.SetSelection(0)
        self.valoresPorDefectoIluminancia(None)
        return

    def comprobarDatos(self):
        """
        Metodo: comprobarDatos
        
        
        """
        superficie = self.superficieMuro.GetValue()
        iluminancia = self.iluminancia.GetValue()
        if ',' in superficie:
            superficie = superficie.replace(',', '.')
            self.superficieMuro.SetValue(superficie)
        if ',' in iluminancia:
            iluminancia = iluminancia.replace(',', '.')
            self.iluminancia.SetValue(iluminancia)
        self.listaErrores = u''
        self.listaErrores += Comprueba(self.nombreInstalacion.GetValue(), 1, self.listaErrores, _(u'nombre')).ErrorDevuelto
        self.listaErrores += Comprueba(self.subgrupoChoice.GetStringSelection(), 0, self.listaErrores, _(u'zona')).ErrorDevuelto
        self.listaErrores += Comprueba(self.superficieMuro.GetValue(), 2, self.listaErrores, _(u'superficie'), 0).ErrorDevuelto
        self.listaErrores += Comprueba(self.usoChoice.GetStringSelection(), 0, self.listaErrores, _(u'uso')).ErrorDevuelto
        self.listaErrores += Comprueba(self.definirSegunChoice.GetStringSelection(), 0, self.listaErrores, _(u'definir seg\xfan')).ErrorDevuelto
        if self.parent.parent.parent.programa == 'GranTerciario' and self.conControl.GetValue() == True:
            superficieControl = self.superficieControl.GetValue()
            if ',' in superficieControl:
                superficieControl = superficieControl.replace(',', '.')
                self.superficieControl.SetValue(superficieControl)
            self.listaErrores += Comprueba(self.superficieControl.GetValue(), 2, self.listaErrores, _(u'superficie con control de la iluminaci\xf3n'), 0.0).ErrorDevuelto
            try:
                if float(self.superficieMuro.GetValue()) < float(self.superficieControl.GetValue()):
                    if self.listaErrores != '':
                        self.listaErrores += ', '
                    self.listaErrores += _(u'la superficie con control de la iluminaci\xf3n es mayor que la superficie total de la zona')
            except (ValueError, TypeError):
                pass

        if 'Conocido' in self.definirSegunChoice.GetStringSelection():
            potencia = self.potenciaInstalada.GetValue()
            if ',' in potencia:
                potencia = potencia.replace(',', '.')
                self.potenciaInstalada.SetValue(potencia)
            self.listaErrores += Comprueba(self.potenciaInstalada.GetValue(), 2, self.listaErrores, _(u'potencia instalada'), 0).ErrorDevuelto
        elif 'Estimado' in self.definirSegunChoice.GetStringSelection():
            self.listaErrores += Comprueba(self.tipoEquipoChoice.GetStringSelection(), 0, self.listaErrores, _(u'tipo de equipo')).ErrorDevuelto
        self.listaErrores += Comprueba(self.iluminancia.GetValue(), 2, self.listaErrores, _(u'iluminancia media horizontal'), 0).ErrorDevuelto

    def valoresPorDefectoIluminancia(self, event):
        """
        Metodo: valoresPorDefectoIluminancia
        
        
        ARGUMENTOS:
                event:
        """
        if self.cambiandoIluminancia == False:
            iluminanciaZona1 = [500,
             500,
             300,
             500,
             100,
             100,
             300,
             700,
             500]
            iluminanciaZona2 = [500,
             300,
             200,
             200,
             100,
             200,
             200,
             200,
             300,
             300,
             100,
             200,
             500]
            if self.zonaRepresentacionCheck.GetValue() == False:
                tabla = iluminanciaZona1
            else:
                tabla = iluminanciaZona2
            valorPorDefecto = tabla[self.usoChoice.GetSelection()]
            antes = self.cambiandoIluminancia
            self.iluminancia.SetValue(str(valorPorDefecto))
            self.cambiandoIluminancia = antes
            self.iluminancia.SetForegroundColour(wx.Colour(100, 200, 0))

    def OnCambioIluminancia(self, event):
        """
        Metodo: OnCambioIluminancia
        
        
        ARGUMENTOS:
                event:
        """
        self.iluminancia.SetForegroundColour(wx.Colour(0, 0, 0))
        self.cambiandoIluminancia = True

    def obtenerValoresIluminacion(self):
        """
        Metodo: obtenerValoresIluminacion
        
        
        """
        S = float(self.superficieMuro.GetValue())
        Em = float(self.iluminancia.GetValue())
        if 'Estimado' in self.definirSegunChoice.GetStringSelection():
            datosLuminaria = diccLuminarias[self.tipoEquipoChoice.GetStringSelection()]
            lumen_Watio = datosLuminaria[0]
            rendimientoLuminaria = datosLuminaria[1]
            lumen_Watio = lumen_Watio * rendimientoLuminaria
            self.potencia = Em * S / lumen_Watio
        else:
            self.potencia = float(self.potenciaInstalada.GetValue())
        self.veei = self.potencia * 100 / S / Em

    def cogerDatos(self):
        """
        Metodo: cogerDatos
        
        
        """
        if self.parent.parent.parent.programa == 'GranTerciario':
            if self.subgrupoChoice.GetItems() == []:
                return []
            zonaElegida = self.subgrupoChoice.GetStringSelection()
            raicesUtilizadas = []
            for ilum in self.parent.iluminacion:
                raicesUtilizadas.append(ilum[-1])

            if zonaElegida in raicesUtilizadas:
                wx.MessageBox(_(u'La zona seleccionada ya tiene una instalaci\xf3n de iluminaci\xf3n'), _(u'Aviso'))
                return []
        self.comprobarDatos()
        if self.listaErrores != u'':
            return self.listaErrores
        self.obtenerValoresIluminacion()
        datos = self.cogerDatosDelPanel()
        return datos

    def cogerDatosMM(self):
        """
        Metodo: cogerDatosMM
        
        
        """
        self.comprobarDatos()
        if self.listaErrores != u'':
            return self.listaErrores
        self.obtenerValoresIluminacion()
        datos = self.cogerDatosDelPanel()
        return datos

    def cogerDatosDelPanel(self):
        """
        Metodo: cogerDatosDelPanel
        
        
        """
        datos = []
        datos.append(self.nombreInstalacion.GetValue())
        datos.append('iluminacion')
        datos.append(self.potencia)
        datos.append(self.veei)
        datos.append('')
        datos.append(self.superficieMuro.GetValue())
        datos.append(self.zonaRepresentacionCheck.GetValue())
        datos.append(self.usoChoice.GetStringSelection())
        datos.append(self.definirSegunChoice.GetStringSelection())
        if 'Estimado' in self.definirSegunChoice.GetStringSelection():
            aux = [self.tipoEquipoChoice.GetStringSelection(), self.iluminancia.GetValue()]
        else:
            aux = [self.potenciaInstalada.GetValue(), self.iluminancia.GetValue()]
        datos.append(aux)
        aux = [self.conControl.GetValue(), self.superficieControl.GetValue()]
        datos.append(aux)
        datos.append(self.subgrupoChoice.GetStringSelection())
        return datos

    def cargarDatos(self, datos = [], instalacionIluminacion = []):
        """
        Metodo: cargarDatos
        
        
        ARGUMENTOS:
                datos: listado con los datos de la instalaci\xf3n a cargar
                instalacionIluminacion = Listado con arrays de todas las instalaciones defindias
        """
        self.nombreInstalacion.SetValue(datos[0])
        self.superficieMuro.SetValue(datos[5])
        self.zonaRepresentacionCheck.SetValue(datos[6])
        self.onZonasRadio(None)
        self.usoChoice.SetStringSelection(datos[7])
        self.definirSegunChoice.SetStringSelection(datos[8])
        aux = datos[9]
        if 'Estimado' in datos[8]:
            self.tipoEquipoChoice.SetStringSelection(aux[0])
            self.iluminancia.SetValue(aux[1])
        else:
            self.potenciaInstalada.SetValue(aux[0])
            self.iluminancia.SetValue(aux[1])
        self.cambiandoIluminancia = False
        aux = datos[10]
        self.conControl.SetValue(aux[0])
        self.superficieControl.SetValue(aux[1])
        self.onControlIluminacion(None)
        if self.parent.parent.parent.programa == 'GranTerciario':
            tuplaZonas = self.cargarRaices(instalacionIluminacion)
            zonaElegida = datos[11]
            if zonaElegida != u'Edificio Objeto':
                tuplaRaizInstalacionCargada = (zonaElegida, zonaElegida)
                tuplaZonas.append(tuplaRaizInstalacionCargada)
                self.subgrupoChoice.SetItems(tuplaZonas)
                self.subgrupoChoice.SetStringSelection(zonaElegida)
        else:
            self.subgrupoChoice.SetStringSelection(datos[11])
        self.onDefinirSegunChoice(None)
        return