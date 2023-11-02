# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\panelFachadaConEdificio.pyc
# Compiled at: 2015-02-23 10:42:15
"""
Modulo: panelFachadaConEdificio.py

"""
from Envolvente.comprobarCampos import Comprueba
from miChoice import MiChoice
import Calculos.listadosWeb as listadosWeb, nuevoUndo, wx, logging
wxID_PANEL1, wxID_PANEL1INERCIACHOICE, wxID_PANEL1INERCIATEXT, wxID_PANEL1NOMBREMURO, wxID_PANEL1NOMBREMUROTEXT, wxID_PANEL1SUPERFICIEMURO, wxID_PANEL1SUPERFICIETEXT, wxID_PANEL1LONGIMUROTEXT, wxID_PANEL1ALTURAMUROTEXT, wxID_PANEL1MULTIMUROTEXT, wxID_PANEL1LONGIMURO, wxID_PANEL1ALTURAMURO, wxID_PANEL1MULTIMURO, wxID_PANEL1LONGITUDUNIDADESTEXT, wxID_PANEL1ALTURAUNIDADESTEXT, wxID_PANEL1SUPERFICIEUNIDADESTEXT, wxID_PANEL1SUBGRUPOTEXT, wxID_PANEL1SUBGRUPOCHOICE, wxID_PANEL1UNIDADESINERCIATEXT, wxID_DIMENSIONESLINEATEXT, wxID_CARACTERISTICASLINEATEXT = [ wx.NewId() for _init_ctrls in range(21) ]

class Panel1(wx.Panel, nuevoUndo.VistaUndo):
    """
    Clase: Panel1 del modulo panelFachadaConEdificio.py

    """

    def OnNombreMuro(self, event):
        """
        Metodo: OnNombreMuro

        ARGUMENTOS:
                event:
        """
        if self.nombreMuro.GetValue() == _('Medianería'):
            self.nombreMuro.SetForegroundColour(wx.Colour(100, 200, 0))
        else:
            self.nombreMuro.SetForegroundColour(wx.Colour(0, 0, 0))

    def _init_ctrls(self, prnt, ide, posi, siz, styl, named):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
                ide:
                posi:
                siz:
                styl:
                named:
        """
        wx.Panel.__init__(self, id=ide, name='panelFachadaConEdificio', parent=prnt, pos=posi, size=siz, style=styl)
        self.SetBackgroundColour('white')
        self.nombreMuroText = wx.StaticText(id=wxID_PANEL1NOMBREMUROTEXT, label=_('Nombre'), name='nombreMuroText', parent=self, pos=wx.Point(15, 2), size=wx.Size(102, 13), style=0)
        self.nombreMuro = wx.TextCtrl(id=wxID_PANEL1NOMBREMURO, name='nombreMuro', parent=self, pos=wx.Point(151, 0), size=wx.Size(210, 21), style=0, value=_('Medianería'))
        self.nombreMuro.SetForegroundColour(wx.Colour(100, 200, 0))
        self.nombreMuro.Bind(wx.EVT_TEXT, self.OnNombreMuro, id=wxID_PANEL1NOMBREMURO)
        self.subgrupoText = wx.StaticText(id=wxID_PANEL1SUBGRUPOTEXT, label=_('Zona'), name='subgrupoText', parent=self, pos=wx.Point(388, 2), size=wx.Size(50, 13), style=0)
        self.subgrupoChoice = MiChoice(choices=[], id=wxID_PANEL1SUBGRUPOCHOICE, name='subgrupoChoice', parent=self, pos=wx.Point(496, 0), size=wx.Size(214, 21), style=0)
        self.DimensionesLineaText = wx.StaticBox(id=wxID_DIMENSIONESLINEATEXT, label=_('Dimensiones'), name='LineaText', parent=self, pos=wx.Point(0, 26), size=wx.Size(361, 77), style=0)
        self.DimensionesLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.DimensionesLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.CaracteristicasLineaText = wx.StaticBox(id=wxID_CARACTERISTICASLINEATEXT, label=_('Características'), name='LineaText', parent=self, pos=wx.Point(373, 26), size=wx.Size(337, 77), style=0)
        self.CaracteristicasLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.superficieText = wx.StaticText(id=wxID_PANEL1SUPERFICIETEXT, label=_('Superficie'), name='superficieText', parent=self, pos=wx.Point(15, 46), size=wx.Size(51, 13), style=0)
        self.superficieMuro = wx.TextCtrl(id=wxID_PANEL1SUPERFICIEMURO, name='superficieMuro', parent=self, pos=wx.Point(151, 44), size=wx.Size(80, 21), style=0, value='')
        self.superficieMuro.Bind(wx.EVT_TEXT, self.OnCambioSuperficie, id=wxID_PANEL1SUPERFICIEMURO)
        self.superficieUnidadesText = wx.StaticText(id=wxID_PANEL1SUPERFICIEUNIDADESTEXT, label=_('m2'), name='superficieUnidadesText', parent=self, pos=wx.Point(236, 46), size=wx.Size(14, 13), style=0)
        self.longitudMuroText = wx.StaticText(id=wxID_PANEL1LONGIMUROTEXT, label=_('Longitud'), name='longitudMuroText', parent=self, pos=wx.Point(151, 69), size=wx.Size(28, 13), style=0)
        self.longitudMuro = wx.TextCtrl(id=wxID_PANEL1LONGIMURO, name='longitudMuro', parent=self, pos=wx.Point(191, 67), size=wx.Size(40, 15), style=0, value='')
        self.longitudMuro.Bind(wx.EVT_TEXT, self.OnCambioLAMText, id=wxID_PANEL1LONGIMURO)
        self.LongitudUnidadesText = wx.StaticText(id=wxID_PANEL1LONGITUDUNIDADESTEXT, label=_('m'), name='profundidadUnidadesText', parent=self, pos=wx.Point(236, 69), size=wx.Size(14, 13), style=0)
        self.alturaMuroText = wx.StaticText(id=wxID_PANEL1ALTURAMUROTEXT, label=_('Altura'), name='alturaMuroText', parent=self, pos=wx.Point(151, 85), size=wx.Size(28, 13), style=0)
        self.alturaMuro = wx.TextCtrl(id=wxID_PANEL1ALTURAMURO, name='alturaMuro', parent=self, pos=wx.Point(191, 83), size=wx.Size(40, 15), style=0, value='')
        self.alturaMuro.Bind(wx.EVT_TEXT, self.OnCambioLAMText, id=wxID_PANEL1ALTURAMURO)
        self.alturaMuroUnidades = wx.StaticText(id=wxID_PANEL1ALTURAUNIDADESTEXT, label=_('m'), name='alturaMuroUnidades', parent=self, pos=wx.Point(236, 85), size=wx.Size(14, 13), style=0)
        self.multiMuroText = wx.StaticText(id=wxID_PANEL1MULTIMUROTEXT, label=_('Multiplicador'), name='multiMuroText', parent=self, pos=wx.Point(0, 94), size=wx.Size(80, 13), style=0)
        self.multiMuroText.Show(False)
        self.multiMuro = wx.TextCtrl(id=wxID_PANEL1MULTIMURO, name='multiMuro', parent=self, pos=wx.Point(120, 94), size=wx.Size(80, 21), style=0, value='1')
        self.multiMuro.Show(False)
        self.multiMuro.Bind(wx.EVT_TEXT, self.OnCambioLAMText, id=wxID_PANEL1MULTIMURO)
        self.longitudMuroText.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.LongitudUnidadesText.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.alturaMuroText.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.alturaMuroUnidades.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.inerciaText = wx.StaticText(id=wxID_PANEL1INERCIATEXT, label=_('Tipo de muro'), name='inerciaText', parent=self, pos=wx.Point(388, 46), size=wx.Size(75, 13), style=0)
        self.inerciaChoice = MiChoice(choices=listadosWeb.listadoOpcionesInercia, id=wxID_PANEL1INERCIACHOICE, name='inerciaChoice', parent=self, pos=wx.Point(496, 44), size=wx.Size(160, 21), style=0)
        self.inerciaChoice.SetSelection(0)
        self.inerciaChoice.Bind(wx.EVT_CHOICE, self.obtenerInercia, id=wxID_PANEL1INERCIACHOICE)
        self.unidadesInerciaText = wx.StaticText(id=wxID_PANEL1UNIDADESINERCIATEXT, label=_('kg/m2'), name='inerciaText', parent=self, pos=wx.Point(662, 46), size=wx.Size(30, 13), style=0)
        self.nombreMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1NOMBREMURO)
        self.superficieMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1SUPERFICIEMURO)
        self.longitudMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1LONGIMURO)
        self.alturaMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1ALTURAMURO)
        self.multiMuro.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1MULTIMURO)
        self.subgrupoChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1SUBGRUPOCHOICE)
        self.inerciaChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1INERCIACHOICE)

    def actualizaDiccionario(self):
        self.diccionario = {}
        self.diccionario['panelFachadaConEdificio.nombreMuro'] = self.nombreMuro.GetValue()
        self.diccionario['panelFachadaConEdificio.superficieMuro'] = self.superficieMuro.GetValue()
        self.diccionario['panelFachadaConEdificio.longitudMuro'] = self.longitudMuro.GetValue()
        self.diccionario['panelFachadaConEdificio.alturaMuro'] = self.alturaMuro.GetValue()
        self.diccionario['panelFachadaConEdificio.multiMuro'] = self.multiMuro.GetValue()
        self.diccionario['panelFachadaConEdificio.subgrupoChoice'] = self.subgrupoChoice.GetSelection()
        self.diccionario['panelFachadaConEdificio.inerciaChoice'] = self.inerciaChoice.GetSelection()

    def cogeValoresDiccionario(self):
        self.nombreMuro.SetValue(self.diccionario['panelFachadaConEdificio.nombreMuro'])
        self.superficieMuro.SetValue(self.diccionario['panelFachadaConEdificio.superficieMuro'])
        self.longitudMuro.SetValue(self.diccionario['panelFachadaConEdificio.longitudMuro'])
        self.alturaMuro.SetValue(self.diccionario['panelFachadaConEdificio.alturaMuro'])
        self.multiMuro.SetValue(self.diccionario['panelFachadaConEdificio.multiMuro'])
        self.subgrupoChoice.SetSelection(self.diccionario['panelFachadaConEdificio.subgrupoChoice'])
        self.inerciaChoice.SetSelection(self.diccionario['panelFachadaConEdificio.inerciaChoice'])

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
        self.bol = True
        self.subgrupoChoice.SetItems(self.cargarRaices())
        self.elegirRaiz()
        self.obtenerInercia(None)
        self.actualizaDiccionario()
        return

    def elegirRaiz(self):
        """
        Metodo: elegirRaiz

        """
        try:
            sel = self.parent.arbolCerramientos.GetSelection()
            self.subgrupoChoice.SetStringSelection('Edificio Objeto')
            raiz = self.parent.arbolCerramientos.GetRootItem()
            while sel != raiz:
                for i in range(len(self.parent.parent.subgrupos)):
                    if self.parent.arbolCerramientos.GetItemText(sel) == self.parent.parent.subgrupos[i].nombre:
                        self.subgrupoChoice.SetStringSelection(self.parent.arbolCerramientos.GetItemText(sel))
                        return

                sel = self.parent.arbolCerramientos.GetItemParent(sel)

        except:
            logging.info('Excepcion en: %s' % __name__)
            self.subgrupoChoice.SetStringSelection('Edificio Objeto')

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

    def OnCambioSuperficie(self, event):
        """
        Metodo: OnCambioSuperficie

        ARGUMENTOS:
                event:
        """
        if self.bol == True:
            self.longitudMuro.SetValue('')
            self.alturaMuro.SetValue('')
            self.multiMuro.SetValue('1')

    def OnCambioLAMText(self, event):
        """
        Metodo: OnCambioLAMText

        ARGUMENTOS:
                event:
        """
        longitud = self.longitudMuro.GetValue()
        altura = self.alturaMuro.GetValue()
        multiplicador = self.multiMuro.GetValue()
        if ',' in longitud:
            longitud = longitud.replace(',', '.')
            self.longitudMuro.SetValue(longitud)
            self.longitudMuro.SetInsertionPointEnd()
        if ',' in altura:
            altura = altura.replace(',', '.')
            self.alturaMuro.SetValue(altura)
            self.alturaMuro.SetInsertionPointEnd()
        if ',' in multiplicador:
            multiplicador = multiplicador.replace(',', '.')
            self.multiMuro.SetValue(multiplicador)
            self.multiMuro.SetInsertionPointEnd()
        try:
            lon = float(self.longitudMuro.GetValue())
            alt = float(self.alturaMuro.GetValue())
            mul = float(self.multiMuro.GetValue())
            self.bol = False
            superficieTotal = round(lon * alt * mul, 2)
            self.superficieMuro.SetValue(str(superficieTotal))
            self.bol = True
        except (ValueError, TypeError):
            pass

    def obtenerInercia(self, event):
        """
        Metodo: obtenerInercia

        ARGUMENTOS:
                event:
        """
        if self.inerciaChoice.GetSelection() == int(0):
            densidadCerramiento = '200'
        elif self.inerciaChoice.GetSelection() == int(1):
            densidadCerramiento = '50'
        return densidadCerramiento

    def comprobarDatos(self):
        """
        Metodo: comprobarDatos

                self):
        """
        listaErrores = ''
        dato = self.superficieMuro.GetValue()
        if ',' in dato:
            dato = dato.replace(',', '.')
            self.superficieMuro.SetValue(dato)
        listaErrores += Comprueba(self.nombreMuro.GetValue(), 1, listaErrores, _('nombre')).ErrorDevuelto
        listaErrores += Comprueba(self.subgrupoChoice.GetStringSelection(), 0, listaErrores, _('zona')).ErrorDevuelto
        listaErrores += Comprueba(self.superficieMuro.GetValue(), 2, listaErrores, _('superficie'), 0).ErrorDevuelto
        return listaErrores

    def cogerDatos(self):
        """
        Metodo: cogerDatos

        """
        listaErrores = self.comprobarDatos()
        if listaErrores != '':
            return listaErrores
        else:
            densidadCerramiento = self.obtenerInercia(None)
            datos = []
            datos.append(self.nombreMuro.GetValue())
            datos.append('Fachada')
            datos.append(self.superficieMuro.GetValue())
            datos.append(0)
            datos.append(densidadCerramiento)
            datos.append('')
            datos.append('')
            datos.append('Sin patrón')
            datos.append(self.longitudMuro.GetValue())
            datos.append(self.alturaMuro.GetValue())
            datos.append(self.multiMuro.GetValue())
            datos.append(self.subgrupoChoice.GetStringSelection())
            datos.append('edificio')
            return datos

    def cargarDatos(self, datos):
        """
        Metodo: cargarDatos

        ARGUMENTOS:
                datos:
        """
        self.nombreMuro.SetValue(datos[0])
        self.superficieMuro.SetValue(datos[2])
        if datos[4] == '50':
            self.inerciaChoice.SetSelection(1)
        elif datos[4] == '200':
            self.inerciaChoice.SetSelection(0)
        self.longitudMuro.SetValue(datos[8])
        self.alturaMuro.SetValue(datos[9])
        self.multiMuro.SetValue(datos[10])
        self.subgrupoChoice.SetStringSelection(datos[11])
        self.parent.panelElegirObjeto.definirFachada.SetValue(True)
        self.parent.panelElegirObjeto.mostrarOpcionesContacto()
        self.parent.panelElegirObjeto.contactoEdificio.SetValue(True)
        colorSombra = wx.Color(240, 240, 240)
        colorNormal = wx.Color(255, 255, 255)
        self.parent.panelElegirObjeto.definirSuelo.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirCubierta.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirFachada.SetBackgroundColour(colorSombra)
        self.parent.panelElegirObjeto.definirParticionInterior.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirHueco.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirPuenteTermico.SetBackgroundColour(colorNormal)
        self.actualizaDiccionario()