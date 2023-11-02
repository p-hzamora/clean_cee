# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\panelPuentesTermicos.pyc
# Compiled at: 2015-02-19 13:18:33
"""
Modulo: panelPuentesTermicos.py

"""
from miChoice import MiChoice
import Envolvente.tablasValores as tablasValores, directorios, Calculos.listadosWeb as listadosWeb, LibreriasCE3X.menuPT as menuPT, nuevoUndo, wx, logging
Directorio = directorios.BuscaDirectorios().Directorio
wxID_PANEL1, wxID_PANEL1CERRAMIENTOCHOICE, wxID_PANEL1CERRAMIENTOTEXT, wxID_PANEL1FIPUENTE, wxID_PANEL1FITEXT, wxID_PANEL1FIUNIDADESTEXT, wxID_PANEL1LONGITUDPUENTE, wxID_PANEL1LONGITUDTEXT, wxID_PANEL1LONGITUDUNIDADESTEXT, wxID_PANEL1NOMBREPUENTETERMICO, wxID_PANEL1NOMBREPUENTETEXT, wxID_PANEL1TIPOPUENTECHOICE, wxID_PANEL1TIPOPUENTETEXT, wxID_PANEL1NOMBREMUROTEXT, wxID_PANEL1NOMBREMURO, wxID_FRAME1CARGARPT = [ wx.NewId() for _init_ctrls in range(16) ]

class panelPuentesTermicos(wx.Panel, nuevoUndo.VistaUndo):
    """
    Clase: panelPuentesTermicos del modulo panelPuentesTermicos.py

    """

    def OnNombrePuenteTermico(self, event):
        """
        Metodo: OnNombrePuenteTermico

        ARGUMENTOS:
                event:
        """
        if self.nombrePuenteTermico.GetValue() == 'Puente térmico':
            self.nombrePuenteTermico.SetForegroundColour(wx.Colour(100, 200, 0))
        else:
            self.nombrePuenteTermico.SetForegroundColour(wx.Colour(0, 0, 0))

    def _init_ctrls(self, prnt, ide, posi, siz, styl, nam):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
                ide:
                posi:
                siz:
                styl:
                nam:
        """
        wx.Panel.__init__(self, id=ide, name='panelPuentesTermicos', parent=prnt, pos=posi, size=siz, style=styl)
        self.SetBackgroundColour('white')
        self.nombrePuenteText = wx.StaticText(id=wxID_PANEL1NOMBREMUROTEXT, label=_('Nombre'), name='nombrePuenteText', parent=self, pos=wx.Point(15, 2), size=wx.Size(102, 13), style=0)
        self.nombrePuenteTermico = wx.TextCtrl(id=wxID_PANEL1NOMBREMURO, name='nombrePuenteTermico', parent=self, pos=wx.Point(138, 0), size=wx.Size(304, 21), style=0, value=_('Puente termico'))
        self.nombrePuenteTermico.SetForegroundColour(wx.Colour(100, 200, 0))
        self.nombrePuenteTermico.Bind(wx.EVT_TEXT, self.OnNombrePuenteTermico, id=wxID_PANEL1NOMBREMURO)
        self.CaracteristicasLineaText = wx.StaticBox(id=-1, label=_('Parámetros generales'), name='LineaText', parent=self, pos=wx.Point(0, 26), size=wx.Size(710, 316), style=0)
        self.CaracteristicasLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.tipoPuenteText = wx.StaticText(id=wxID_PANEL1TIPOPUENTETEXT, label=_('Tipo de puente térmico'), name='tipoPuenteText', parent=self, pos=wx.Point(15, 46), size=wx.Size(112, 13), style=0)
        self.tipoPuenteChoice = MiChoice(choices=listadosWeb.listadoOpcionesPuentesTermicos, id=wxID_PANEL1TIPOPUENTECHOICE, name='tipoPuenteChoice', parent=self, pos=wx.Point(138, 44), size=wx.Size(304, 21), style=0)
        self.tipoPuenteChoice.Bind(wx.EVT_CHOICE, self.OnCambioTipoPT, id=wxID_PANEL1TIPOPUENTECHOICE)
        self.cerramientoText = wx.StaticText(id=wxID_PANEL1CERRAMIENTOTEXT, label=_('Cerramiento asociado'), name='cerramientoText', parent=self, pos=wx.Point(15, 76), size=wx.Size(105, 13), style=0)
        self.cerramientoChoice = wx.Choice(choices=[], id=wxID_PANEL1CERRAMIENTOCHOICE, name='cerramientoChoice', parent=self, pos=wx.Point(138, 74), size=wx.Size(304, 21), style=0)
        self.cerramientoChoice.Bind(wx.EVT_CHOICE, self.OnCambioCerramientoAsociado, id=wxID_PANEL1CERRAMIENTOCHOICE)
        self.fiText = wx.StaticText(id=wxID_PANEL1FITEXT, label=_('φ'), name='fiText', parent=self, pos=wx.Point(15, 106), size=wx.Size(10, 13), style=0)
        self.fiPuente = wx.TextCtrl(id=wxID_PANEL1FIPUENTE, name='fiPuente', parent=self, pos=wx.Point(138, 104), size=wx.Size(56, 21), style=0, value='')
        self.fiPuente.Bind(wx.EVT_TEXT, self.OnCambiofi, id=wxID_PANEL1FIPUENTE)
        self.fiUnidadesText = wx.StaticText(id=wxID_PANEL1FIUNIDADESTEXT, label=_('W/mK'), name='fiUnidadesText', parent=self, pos=wx.Point(199, 106), size=wx.Size(35, 13), style=0)
        self.cargarPT = wx.BitmapButton(id=wxID_FRAME1CARGARPT, bitmap=wx.Bitmap(Directorio + '/Imagenes/pt.ico', wx.BITMAP_TYPE_ANY), parent=self, pos=wx.Point(240, 103), size=wx.Size(23, 21), style=wx.BU_AUTODRAW)
        self.cargarPT.Bind(wx.EVT_BUTTON, self.OnCargarPT, id=wxID_FRAME1CARGARPT)
        self.longitudText = wx.StaticText(id=wxID_PANEL1LONGITUDTEXT, label=_('Longitud'), name='longitudText', parent=self, pos=wx.Point(15, 136), size=wx.Size(41, 13), style=0)
        self.longitudPuente = wx.TextCtrl(id=wxID_PANEL1LONGITUDPUENTE, name='longitudPuente', parent=self, pos=wx.Point(138, 134), size=wx.Size(56, 21), style=0, value='')
        self.longitudPuente.Bind(wx.EVT_TEXT, self.OnCambioLongitud, id=wxID_PANEL1LONGITUDPUENTE)
        self.longitudUnidadesText = wx.StaticText(id=wxID_PANEL1LONGITUDUNIDADESTEXT, label=_('m'), name='longitudUnidadesText', parent=self, pos=wx.Point(199, 136), size=wx.Size(8, 13), style=0)
        self.nombrePuenteTermico.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1NOMBREMURO)
        self.fiPuente.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1FIPUENTE)
        self.longitudPuente.Bind(wx.EVT_KILL_FOCUS, self.manejador, id=wxID_PANEL1LONGITUDPUENTE)
        self.tipoPuenteChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1TIPOPUENTECHOICE)
        self.cerramientoChoice.Bind(wx.EVT_KILL_FOCUS, self.manejadorChoice, id=wxID_PANEL1CERRAMIENTOCHOICE)

    def actualizaDiccionario(self):
        self.diccionario = {}
        self.diccionario['panelPuentesTermicos.nombrePuenteTermico'] = self.nombrePuenteTermico.GetValue()
        self.diccionario['panelPuentesTermicos.fiPuente'] = self.fiPuente.GetValue()
        self.diccionario['panelPuentesTermicos.longitudPuente'] = self.longitudPuente.GetValue()
        self.diccionario['panelPuentesTermicos.tipoPuenteChoice'] = self.tipoPuenteChoice.GetSelection()
        self.diccionario['panelPuentesTermicos.cerramientoChoice'] = self.cerramientoChoice.GetSelection()

    def cogeValoresDiccionario(self):
        self.nombrePuenteTermico.SetValue(self.diccionario['panelPuentesTermicos.nombrePuenteTermico'])
        self.fiPuente.SetValue(self.diccionario['panelPuentesTermicos.fiPuente'])
        self.longitudPuente.SetValue(self.diccionario['panelPuentesTermicos.longitudPuente'])
        self.tipoPuenteChoice.SetSelection(self.diccionario['panelPuentesTermicos.tipoPuenteChoice'])
        self.cerramientoChoice.SetSelection(self.diccionario['panelPuentesTermicos.cerramientoChoice'])

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
        self.valorDefectoFi = True
        self.valorDefectoLongitud = True
        cerramientos = self.cargarCerramientos()
        self.elegirCerramientoSeleccionado(cerramientos)
        self.actualizaDiccionario()
        self.boleano = True

    def OnCargarPT(self, event):
        """
        Metodo: OnCargarPT

        ARGUMENTOS:
                event:
        """
        dlg = menuPT.create(self)
        dlg.ShowModal()
        if dlg.dev != False:
            nombreCerramiento = dlg.dev[0]
            nombreGrupo = dlg.dev[1]
            fiCuadro = dlg.dev[3]
            self.fiPuente.SetValue(fiCuadro)
            self.tipoPuenteChoice.SetStringSelection(nombreGrupo)

    def cargarCerramientos(self):
        """
        Metodo: cargarCerramientos

        """
        cerramientos = []
        for i in self.parent.cerramientos:
            cerramientos.append(i[0])

        self.cerramientoChoice.AppendItems(cerramientos)
        return cerramientos

    def elegirCerramientoSeleccionado(self, cerramientos):
        """
        Metodo: elegirCerramientoSeleccionado

        ARGUMENTOS:
                cerramientos:
        """
        sel = self.parent.arbolCerramientos.GetSelection()
        self.cerramientoChoice.SetSelection(-1)
        try:
            seleccionArbol = self.parent.arbolCerramientos.GetItemText(sel)
            if 'Hueco' in seleccionArbol or 'PT' in seleccionArbol:
                sel = self.parent.arbolCerramientos.GetItemParent(sel)
                seleccionArbol = self.parent.arbolCerramientos.GetItemText(sel)
            for cerr in cerramientos:
                if self.parent.arbolCerramientos.GetItemText(sel) == cerr:
                    self.cerramientoChoice.SetStringSelection(cerr)
                    self.calcularLongitud()

        except:
            logging.info('Excepcion en: %s' % __name__)
            self.cerramientoChoice.SetSelection(-1)

    def OnCambioCerramientoAsociado(self, event):
        self.calcularFi()
        self.calcularLongitud()

    def calcularLongitud(self):
        """
        Metodo: calcularLongitud

        ARGUMENTOS:
                event:
        """
        longitudPT = ''
        if self.valorDefectoLongitud == True:
            cerramientoEscogido = self.cerramientoChoice.GetStringSelection()
            tipoPuenteSeleccionado = self.tipoPuenteChoice.GetStringSelection()
            alturaPlanta = self.parent.parent.parent.panelDatosGenerales.alturaMediaLibre.GetValue()
            numeroPlantas = self.parent.parent.parent.panelDatosGenerales.numeroPlantas.GetValue()
            if ',' in alturaPlanta:
                alturaPlanta = alturaPlanta.replace(',', '.')
                self.parent.parent.parent.panelDatosGenerales.alturaMediaLibre.SetValue(alturaPlanta)
            if ',' in numeroPlantas:
                numeroPlantas = numeroPlantas.replace(',', '.')
                self.parent.parent.parent.panelDatosGenerales.numeroPlantas.SetValue(numeroPlantas)
            if tipoPuenteSeleccionado != 'Contorno de hueco' and tipoPuenteSeleccionado != 'Caja de Persiana':
                for cerr in self.parent.cerramientos:
                    if cerr[0] == cerramientoEscogido:
                        longitudPT = tablasValores.calcularLongitudPT(cerr, tipoPuenteSeleccionado, alturaPlanta, numeroPlantas)
                        break

            else:
                longitudContorno = 0
                longitudPersiana = 0
                for v in self.parent.ventanas:
                    if v.cerramientoAsociado == cerramientoEscogido:
                        superficie_v = float(v.superficie)
                        try:
                            longitud_v = float(v.longitud)
                            altura_v = float(v.altura)
                            multip_v = float(v.multiplicador)
                        except (ValueError, TypeError):
                            altura_v = 1.0
                            longitud_v = superficie_v / altura_v
                            multip_v = 1

                        longitudContorno += (2 * longitud_v + 2 * altura_v) * multip_v
                        longitudPersiana += longitud_v * multip_v

                if tipoPuenteSeleccionado == 'Contorno de hueco':
                    if longitudContorno != 0:
                        longitudPT = longitudContorno
                    else:
                        longitudPT = ''
                elif longitudPersiana != 0:
                    longitudPT = longitudPersiana
                else:
                    longitudPT = ''
            self.boleano = False
            self.longitudPuente.SetValue(str(longitudPT))
            self.boleano = True

    def OnCambioTipoPT(self, event):
        """
        Metodo: OnCambioTipoPT

        ARGUMENTOS:
                event:
        """
        self.calcularFi()
        self.calcularLongitud()

    def calcularFi(self):
        if self.valorDefectoFi == True:
            try:
                for cerr in self.parent.cerramientos:
                    if cerr[0] == self.cerramientoChoice.GetStringSelection():
                        fi = tablasValores.tablasValores('PT', None, [self.tipoPuenteChoice.GetStringSelection(),
                         self.parent.parent.parent.panelDatosGenerales.anoConstruccionChoice.GetSelection(), cerr], None).fi
                        break

                if fi == False:
                    fi = ''
                self.boleano = False
                self.fiPuente.SetValue(str(fi))
                self.boleano = True
            except:
                logging.info('Excepcion en: %s' % __name__)

        return

    def OnCambioLongitud(self, event):
        """
        Metodo: OnCambioLongitud

        ARGUMENTOS:
                event:
        """
        if self.boleano == True:
            self.valorDefectoLongitud = False
            try:
                self.longitudPuente.SetForegroundColour(wx.Colour(0, 0, 0))
            except:
                logging.info('Excepcion en: %s' % __name__)

            try:
                float(self.longitudPuente.GetValue())
            except (ValueError, TypeError):
                logging.info('Excepcion en: %s' % __name__)
                self.valorDefectoLongitud = True

        else:
            self.valorDefectoLongitud = True
            try:
                self.longitudPuente.SetForegroundColour(wx.Colour(100, 200, 0))
            except:
                logging.info('Excepcion en: %s' % __name__)

    def OnCambiofi(self, event):
        """
        Metodo: OnCambiofi

        ARGUMENTOS:
                event:
        """
        if self.boleano == True:
            self.valorDefectoFi = False
            try:
                self.fiPuente.SetForegroundColour(wx.Colour(0, 0, 0))
            except:
                logging.info('Excepcion en: %s' % __name__)

            try:
                float(self.fiPuente.GetValue())
            except (ValueError, TypeError):
                self.valorDefectoFi = True

        else:
            self.valorDefectoFi = True
            try:
                self.fiPuente.SetForegroundColour(wx.Colour(100, 200, 0))
            except:
                logging.info('Excepcion en: %s' % __name__)

    def comprobarDatos(self):
        """
        Metodo: comprobarDatos

        """
        listaErrores = ''
        descripcion = self.nombrePuenteTermico.GetValue()
        tipo = self.tipoPuenteChoice.GetStringSelection()
        cerrAsociado = self.cerramientoChoice.GetStringSelection()
        transm = self.fiPuente.GetValue()
        longitud = self.longitudPuente.GetValue()
        if ',' in transm:
            transm = transm.replace(',', '.')
            self.fiPuente.SetValue(transm)
        if ',' in longitud:
            longitud = longitud.replace(',', '.')
            self.longitudPuente.SetValue(longitud)
        try:
            float(transm)
        except (ValueError, TypeError):
            logging.info('Excepcion en: %s' % __name__)
            transm = ''

        try:
            float(longitud)
            if float(longitud) < 0:
                longitud = ''
        except (ValueError, TypeError):
            logging.info('Excepcion en: %s' % __name__)
            longitud = ''

        if descripcion == '':
            listaErrores += 'nombre'
        if tipo == '':
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'tipo de puente térmico'
        if cerrAsociado == '':
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'cerramiento asociado'
        if transm == '':
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'φ'
        if longitud == '':
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'longitud'
        return listaErrores

    def cogerDatos(self):
        """
        Metodo: cogerDatos

        """
        listaErrores = self.comprobarDatos()
        if listaErrores != '':
            return listaErrores
        datos = []
        datos.append(self.nombrePuenteTermico.GetValue())
        datos.append('PT')
        datos.append(self.tipoPuenteChoice.GetStringSelection())
        datos.append(self.fiPuente.GetValue())
        datos.append(self.longitudPuente.GetValue())
        datos.append('usuario_fi')
        datos.append('usuario')
        datos.append(self.cerramientoChoice.GetStringSelection())
        subgrupo = self.subgrupoAlquePertenece(self.cerramientoChoice.GetStringSelection())
        datos.append(subgrupo)
        return datos

    def subgrupoAlquePertenece(self, cerramiento):
        """
        Metodo: subgrupoAlquePertenece

        ARGUMENTOS:
                cerramiento:
        """
        for i in self.parent.cerramientos:
            if i[0] == cerramiento:
                subgrupo = i[-2]
                break

        return subgrupo

    def cargarDatos(self, datos):
        """
        Metodo: cargarDatos

        ARGUMENTOS:
                datos:
        """
        self.nombrePuenteTermico.SetValue(datos[0])
        self.tipoPuenteChoice.SetStringSelection(datos[2])
        self.fiPuente.SetValue(str(datos[3]))
        self.longitudPuente.SetValue(str(datos[4]))
        self.cerramientoChoice.SetStringSelection(datos[7])
        self.parent.panelElegirObjeto.definirPuenteTermico.SetValue(True)
        self.parent.panelElegirObjeto.noMostrarOpcionesContacto()
        colorSombra = wx.Color(240, 240, 240)
        colorNormal = wx.Color(255, 255, 255)
        self.parent.panelElegirObjeto.definirSuelo.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirCubierta.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirFachada.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirParticionInterior.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirHueco.SetBackgroundColour(colorNormal)
        self.parent.panelElegirObjeto.definirPuenteTermico.SetBackgroundColour(colorSombra)
        self.actualizaDiccionario()