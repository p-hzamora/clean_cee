# Embedded file name: ventanaSubgrupo.pyc
"""
Modulo: ventanaSubgrupo.py

"""
from Instalaciones.comprobarCampos import Comprueba
from MedidasDeMejora.funcionActualizarMMInstalacionesAlCambiarSuperficie import actualizarNombreSubgrupoDeConjuntosMM, existenInstalacionesColgandoDeZonaModificadaOEliminadaEnConjuntosMM, actualizarCoberturaDeConjuntosMM, actualizarSuperficieIluminacionDeConjuntosMM
from miChoice import MiChoice
from undo import eventoUndo
import Calculos.calculoSuperficies as calculoSuperficies
import copy
import wx
import logging

def create(parent, id, pos, size, style, name, panelEnvolvente, panelInstalaciones, modo, item):
    """
    Metodo: create
    
    
    ARGUMENTOS:
                parent:
                 id:
                 pos:
                 size:
                 style:
                 name:
                 panelEnvolvente:
                panelInstalaciones:
                modo:
                item:
    """
    return ventanaSubgrupo(parent, id, pos, size, style, name, panelEnvolvente, panelInstalaciones, modo, item)


wxID_PANEL1, wxID_PANEL1NOMBRESUBGRUPO, wxID_PANEL1NOMBRESUBGRUPOTEXT, wxID_PANEL1RAIZCHOICE, wxID_PANEL1RAIZTEXT, wxID_PANEL1SUPERFICIETEXT, wxID_PANEL1SUPERSUBGRUPO, wxID_PANEL1UNIDADESSUPERFICIETEXT, wxID_DIALOG1BOTONACEPTAR, wxID_DIALOG1BOTONCANCELAR, wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICBOX1 = [ wx.NewId() for _init_ctrls in range(12) ]

class ventanaSubgrupo(wx.Dialog):
    """
    Clase: ventanaSubgrupo del modulo ventanaSubgrupo.py
    
    
    """

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
        wx.Dialog.__init__(self, id=ide, name=nam, parent=prnt, pos=posi, size=siz, style=styl, title=_(u'Definir zonas del edificio'))
        self.SetBackgroundColour('white')
        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=_(u'Definir zonas del edificio'), name='staticText1', parent=self, pos=wx.Point(15, 15), size=wx.Size(350, 20), style=0)
        self.staticText1.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, u''))
        self.staticText1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticBox1 = wx.StaticBox(id=wxID_DIALOG1STATICBOX1, label=_(u'Definici\xf3n de una zona'), name='staticText1', parent=self, pos=wx.Point(15, 45), size=wx.Size(414, 120), style=0)
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticBox1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.nombreSubgrupoText = wx.StaticText(id=wxID_PANEL1NOMBRESUBGRUPOTEXT, label=_(u'Nombre de la zona'), name=u'nombreSubgrupoText', parent=self, pos=wx.Point(30, 70), size=wx.Size(135, 13), style=0)
        self.nombreSubgrupo = wx.TextCtrl(id=wxID_PANEL1NOMBRESUBGRUPO, name=u'nombreSubgrupo', parent=self, pos=wx.Point(190, 68), size=wx.Size(224, 21), style=0, value=u'')
        self.raizText = wx.StaticText(id=wxID_PANEL1RAIZTEXT, label=_(u'Elemento ra\xedz'), name=u'raizText', parent=self, pos=wx.Point(30, 100), size=wx.Size(67, 13), style=0)
        self.raizchoice = MiChoice(choices=[(u'Edificio Objeto', _(u'Edificio Objeto'))], id=wxID_PANEL1RAIZCHOICE, name=u'raizchoice', parent=self, pos=wx.Point(190, 98), size=wx.Size(224, 21), style=0)
        self.raizchoice.Bind(wx.EVT_CHOICE, self.OnRaizChoice, id=wxID_PANEL1RAIZCHOICE)
        self.superficieSubgrupoText = wx.StaticText(id=wxID_PANEL1SUPERFICIETEXT, label=_(u'Superficie habitable asociada'), name=u'superficieSubgrupoText', parent=self, pos=wx.Point(30, 130), size=wx.Size(150, 13), style=0)
        self.superficieSubgrupo = wx.TextCtrl(id=wxID_PANEL1SUPERSUBGRUPO, name=u'superficieSubgrupo', parent=self, pos=wx.Point(190, 128), size=wx.Size(80, 21), style=0, value=u'')
        self.unidadesSuperficieSubgrupoText = wx.StaticText(id=wxID_PANEL1UNIDADESSUPERFICIETEXT, label=_(u'm2'), name=u'superficieSubgrupoText', parent=self, pos=wx.Point(275, 130), size=wx.Size(15, 13), style=0)
        self.botonAceptar = wx.Button(id=wxID_DIALOG1BOTONACEPTAR, label=_(u'Aceptar'), name=u'botonAceptar', parent=self, pos=wx.Point(15, 180), size=wx.Size(75, 23), style=0)
        self.botonAceptar.Bind(wx.EVT_BUTTON, self.OnBotonAceptarButton, id=wxID_DIALOG1BOTONACEPTAR)
        self.botonCancelar = wx.Button(id=wxID_DIALOG1BOTONCANCELAR, label=_(u'Cancelar'), name=u'botonCancelar', parent=self, pos=wx.Point(105, 180), size=wx.Size(75, 23), style=0)
        self.botonCancelar.Bind(wx.EVT_BUTTON, self.OnBotonCancelarButton, id=wxID_DIALOG1BOTONCANCELAR)

    def __init__(self, parent, id, pos, size, style, name, panelEnvolvente, panelInstalaciones, modo, item):
        """
        Constructor de la clase
        
        
        ARGUMENTOS:
                 parent:
                 id:
                 pos:
                 size:
                 style:
                 name:
                 panelEnvolvente:
                panelInstalaciones:
                modo:
                item:
        """
        self.parent = parent
        self._init_ctrls(parent, id, pos, size, style, name)
        self.bol = True
        self.raizchoice.SetItems(self.cargarRaices())
        self.panelEnvolvente = panelEnvolvente
        self.panelInstalaciones = panelInstalaciones
        self.modo = modo
        self.itemAntiguo = item
        self.elegirRaiz()

    def OnRaizChoice(self, event):
        """
        Metodo: OnRaizChoice
        
        
        ARGUMENTOS:
                 event:
        """
        event.Skip()

    def elegirRaiz(self):
        """
        Metodo: elegirRaiz
        
        
        """
        try:
            sel = self.parent.arbolCerramientos.GetSelection()
            try:
                self.raizchoice.SetSelection(0)
                for i in range(len(self.parent.parent.subgrupos)):
                    if self.parent.arbolCerramientos.GetItemText(sel) == self.parent.parent.subgrupos[i].nombre:
                        self.raizchoice.SetStringSelection(self.parent.arbolCerramientos.GetItemText(sel))
                        break
                    else:
                        self.raizchoice.SetSelection(0)

            except:
                logging.info(u'Excepcion en: %s' % __name__)
                self.raizchoice.SetSelection(0)

        except:
            logging.info(u'Excepcion en: %s' % __name__)
            sel = self.parent.arbolInstalaciones.GetSelection()
            try:
                self.raizchoice.SetSelection(0)
                for i in range(len(self.parent.parent.subgrupos)):
                    if self.parent.arbolInstalaciones.GetItemText(sel) == self.parent.parent.subgrupos[i].nombre:
                        self.raizchoice.SetStringSelection(self.parent.arbolInstalaciones.GetItemText(sel))
                        break
                    else:
                        self.raizchoice.SetSelection(0)

            except:
                logging.info(u'Excepcion en: %s' % __name__)
                self.raizchoice.SetSelection(0)

    def cargarRaices(self):
        """
        Metodo: cargarRaices
        
        
        """
        raices = [(u'Edificio Objeto', _(u'Edificio Objeto'))]
        for sub in self.parent.parent.subgrupos:
            raices.append((sub.nombre, sub.nombre))

        return raices

    def cogerDatos(self):
        """
        Metodo: cogerDatos
        
        
        """
        descripcion = self.nombreSubgrupo.GetValue()
        raiz = self.raizchoice.GetStringSelection()
        superSub = self.superficieSubgrupo.GetValue()
        self.listaErrores = ''
        self.listaErrores += Comprueba(self.nombreSubgrupo.GetValue(), 1, self.listaErrores, _(u'Nombre')).ErrorDevuelto
        self.listaErrores += Comprueba(self.raizchoice.GetStringSelection(), 0, self.listaErrores, _(u'Elemento ra\xedz')).ErrorDevuelto
        if ',' in superSub:
            superSub = superSub.replace(',', '.')
            self.superficieSubgrupo.SetValue(superSub)
        self.listaErrores += Comprueba(self.superficieSubgrupo.GetValue(), 2, self.listaErrores, _(u'Superficie'), 0).ErrorDevuelto
        if self.listaErrores != '':
            return self.listaErrores
        zona = claseZona(descripcion, raiz, superSub)
        return zona

    def cargarDatos(self, datos):
        """
        Metodo: cargarDatos
        
        
        ARGUMENTOS:
                datos:
        """
        self.nombreSubgrupo.SetValue(datos.nombre)
        self.raizchoice.SetStringSelection(datos.raiz)
        self.superficieSubgrupo.SetValue(datos.superficie)

    def compruebaNombres(self, nombre):
        """
        Metodo: compruebaNombres
        
        
        ARGUMENTOS:
                nombre:
        """
        for i in range(len(self.parent.parent.subgrupos)):
            if nombre == self.parent.parent.subgrupos[i].nombre:
                return nombre

        return 'elemento no encontrado'

    def onComprobarSuperficies(self):
        """
        Metodo: onComprobarSuperficies
        
        
        """
        superficieEdificioObjeto = self.parent.parent.parent.panelDatosGenerales.superficie.GetValue()
        superficieNuevaZona = float(self.superficieSubgrupo.GetValue())
        totalZona = 0
        superficieZonaPpal = 0
        for sub in self.parent.parent.subgrupos:
            if self.raizchoice.GetStringSelection() == sub.raiz and self.itemAntiguo != sub.nombre:
                totalZona += float(sub.superficie)
            if self.raizchoice.GetStringSelection() == sub.nombre:
                superficieZonaPpal = float(sub.superficie)

        totalZona = totalZona + superficieNuevaZona
        if self.raizchoice.GetStringSelection() != u'Edificio Objeto':
            if totalZona > superficieZonaPpal:
                wx.MessageBox(_(u'La superficie de las subzonas definidas son superiores a la superficie de la zona ' + unicode(self.raizchoice.GetStringSelection())), _(u'Aviso'))
                return False
        else:
            if float(totalZona) > float(superficieEdificioObjeto):
                wx.MessageBox(_(u'La superficie de las zonas definidas son superiores a la superficie total del edificio'), _(u'Aviso'))
                return False
            return True

    def avisoModificacionZona(self, boolExistenInstColgandoDeZonaElimOModifEnConjuntosMM):
        """
        M\xe9todo: avisoModificacionZona
        Argumentos: 
            boolExistenInstColgandoDeZonaElimOModifEnConjuntosMM: True si existen en conjuntosMM instalaciones qeu cuelgan de esta zona, False, en caso contrario
        Saca mensaje de aviso al modificar superficie o nombre de una zona
        """
        if boolExistenInstColgandoDeZonaElimOModifEnConjuntosMM == False:
            wx.MessageBox(_(u'Al modificar la superficie de una zona se actualizan las superficies cubiertas por las instalaciones que cuelgan de dicha zona.\nRevise los valores.'), _(u'Aviso'))
        else:
            wx.MessageBox(_(u'Al modificar la superficie de una zona se actualizan las superficies cubiertas por las instalaciones que cuelgan de dicha zona.\nRevise las instalaciones del edificio y las medidas de mejora de instalaciones definidas.'), _(u'Aviso'))

    def actualizarSuperficiesInstalaciones(self, superficieZonaModificada, nombreZonaNuevo):
        """
        Metodo: actualizarSuperficiesInstalaciones
        
        
        ARGUMENTOS:
                 superficieZonaModificada:
                 zonaModificada:
        """
        if self.parent.parent.parent.panelInstalaciones.ACS != [] or self.parent.parent.parent.panelInstalaciones.calefaccion != [] or self.parent.parent.parent.panelInstalaciones.refrigeracion != [] or self.parent.parent.parent.panelInstalaciones.climatizacion != [] or self.parent.parent.parent.panelInstalaciones.mixto2 != [] or self.parent.parent.parent.panelInstalaciones.mixto3 != []:
            listadoInstalacionesSuperficiesInicial = [self.parent.parent.parent.panelInstalaciones.ACS,
             self.parent.parent.parent.panelInstalaciones.calefaccion,
             self.parent.parent.parent.panelInstalaciones.refrigeracion,
             self.parent.parent.parent.panelInstalaciones.climatizacion,
             self.parent.parent.parent.panelInstalaciones.mixto2,
             self.parent.parent.parent.panelInstalaciones.mixto3]
            listadoInstalacionesSuperficies = calculoSuperficies.actualizarSuperficiesInstalaciones(listadoInstalaciones=listadoInstalacionesSuperficiesInicial, superficieCambiada=superficieZonaModificada, zonaCambiada=nombreZonaNuevo)
            self.parent.parent.parent.panelInstalaciones.ACS = listadoInstalacionesSuperficies[0]
            self.parent.parent.parent.panelInstalaciones.calefaccion = listadoInstalacionesSuperficies[1]
            self.parent.parent.parent.panelInstalaciones.refrigeracion = listadoInstalacionesSuperficies[2]
            self.parent.parent.parent.panelInstalaciones.climatizacion = listadoInstalacionesSuperficies[3]
            self.parent.parent.parent.panelInstalaciones.mixto2 = listadoInstalacionesSuperficies[4]
            self.parent.parent.parent.panelInstalaciones.mixto3 = listadoInstalacionesSuperficies[5]
            if self.parent.parent.parent.panelInstalaciones.panel2.tipoSistema not in 'iluminacion':
                zonaAntigua = self.panelInstalaciones.panel2.subgrupoChoice.GetSelection()
                self.panelInstalaciones.panel2.subgrupoChoice.SetItems(self.panelInstalaciones.panel2.cargarRaices())
                self.panelInstalaciones.panel2.subgrupoChoice.SetSelection(zonaAntigua)
                if self.parent.parent.parent.panelInstalaciones.panel2.tipoSistema == 'ACS':
                    self.parent.parent.parent.panelInstalaciones.panel2.OnCoberturaPorcentaje(None)
                elif self.parent.parent.parent.panelInstalaciones.panel2.tipoSistema == 'calefaccion':
                    self.parent.parent.parent.panelInstalaciones.panel2.OnCoberturaPorcentaje(None)
                elif self.parent.parent.parent.panelInstalaciones.panel2.tipoSistema == 'refrigeracion':
                    self.parent.parent.parent.panelInstalaciones.panel2.OnCoberturaPorcentaje(None)
                elif self.parent.parent.parent.panelInstalaciones.panel2.tipoSistema == 'climatizacion':
                    self.parent.parent.parent.panelInstalaciones.panel2.OnCoberturaPorcentaje(None)
                    self.parent.parent.parent.panelInstalaciones.panel2.OnCoberturaPorcentaje2(None)
                elif self.parent.parent.parent.panelInstalaciones.panel2.tipoSistema == 'mixto2':
                    self.parent.parent.parent.panelInstalaciones.panel2.OnCoberturaPorcentaje(None)
                    self.parent.parent.parent.panelInstalaciones.panel2.OnCoberturaPorcentaje2(None)
                elif self.parent.parent.parent.panelInstalaciones.panel2.tipoSistema == 'mixto3':
                    self.parent.parent.parent.panelInstalaciones.panel2.OnCoberturaPorcentaje(None)
                    self.parent.parent.parent.panelInstalaciones.panel2.OnCoberturaPorcentaje2(None)
                    self.parent.parent.parent.panelInstalaciones.panel2.OnCoberturaPorcentaje3(None)
        return

    def onComprobarSuperficiesInferiores(self, zonaAntigua):
        """
        Metodo: onComprobarSuperficiesInferiores
        
        
        ARGUMENTOS:
                 zonaAntigua:
        """
        superficieSuperZona = float(self.superficieSubgrupo.GetValue())
        totalZona = 0
        for sub in self.parent.parent.subgrupos:
            if zonaAntigua == sub.raiz:
                totalZona += float(sub.superficie)

        if totalZona > superficieSuperZona:
            wx.MessageBox(_(u'La superficies de las subzonas definidas son superiores a la superficie de la zona ' + unicode(self.nombreSubgrupo.GetStringSelection())), _(u'Aviso'))
            return False

    def OnBotonAceptarButton(self, event):
        """
        Metodo: OnBotonAceptarButton
        
        
        ARGUMENTOS:
                 event:
        """
        zonaPanel = self.cogerDatos()
        if type(zonaPanel) == type(u'hola'):
            wx.MessageBox(_(u'Revise los siguientes campos:\n' + zonaPanel), _(u'Aviso'))
            return
        else:
            aux = self.onComprobarSuperficies()
            if aux == False:
                return
            accionesUndo = []
            datosUndo = []
            if self.modo == u'a\xf1adir':
                repetido = False
                for subgrupo in self.parent.parent.subgrupos:
                    if subgrupo.nombre == zonaPanel.nombre:
                        repetido = True
                        break

                if repetido == True:
                    wx.MessageBox(_(u'Ya existe una zona con este nombre, indique otro'), _(u'Aviso'))
                    return
                self.parent.parent.subgrupos.append(zonaPanel)
                datosUndo.append(zonaPanel.nombre)
                accionesUndo.append('anadir zona')
                if self.parent.parent.parent.programa == 'GranTerciario':
                    self.panelInstalaciones.iluminacion = calculoSuperficies.actualizarSuperficiesIluminacion(self.parent.parent.subgrupos, self.parent.parent.parent.panelDatosGenerales.superficie.GetValue(), self.panelInstalaciones.iluminacion)
                    try:
                        if self.panelInstalaciones.panelElegirObjeto.iluminacion.GetValue() == True:
                            self.panelInstalaciones.panel2.onSeleccionarSubgrupo(None)
                    except:
                        logging.info(u'Excepcion en: %s' % __name__)

                self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, accionesUndo, datosUndo))
            elif self.modo == u'modificar':
                aux = self.onComprobarSuperficiesInferiores(self.itemAntiguo)
                if aux == False:
                    return
                if zonaPanel.nombre == self.itemAntiguo:
                    for i in range(len(self.parent.parent.subgrupos)):
                        if self.parent.parent.subgrupos[i].nombre == zonaPanel.nombre:
                            datosUndo.append([copy.deepcopy(self.parent.parent.subgrupos[i]), zonaPanel.nombre])
                            accionesUndo.append('modificar zona')
                            if float(self.parent.parent.subgrupos[i].superficie) != float(zonaPanel.superficie):
                                self.parent.parent.subgrupos[i] = zonaPanel
                                self.actualizarSuperficiesInstalaciones(zonaPanel.superficie, zonaPanel.nombre)
                                boolExistenInstColgandoDeZonaElimOModifEnConjuntosMM = existenInstalacionesColgandoDeZonaModificadaOEliminadaEnConjuntosMM(listadoConjuntosMM=self.parent.parent.parent.listadoConjuntosMMUsuario, subgrupoModifOElim=zonaPanel.nombre)
                                self.avisoModificacionZona(boolExistenInstColgandoDeZonaElimOModifEnConjuntosMM=boolExistenInstColgandoDeZonaElimOModifEnConjuntosMM)
                                if boolExistenInstColgandoDeZonaElimOModifEnConjuntosMM == True:
                                    self.parent.parent.parent.listadoConjuntosMMUsuario = actualizarCoberturaDeConjuntosMM(listadoConjuntosMM=self.parent.parent.parent.listadoConjuntosMMUsuario, superficieCambiada=zonaPanel.superficie, zonaCambiada=zonaPanel.nombre)
                                if self.parent.parent.parent.programa == 'GranTerciario':
                                    self.panelInstalaciones.iluminacion = calculoSuperficies.actualizarSuperficiesIluminacion(self.parent.parent.subgrupos, self.parent.parent.parent.panelDatosGenerales.superficie.GetValue(), self.panelInstalaciones.iluminacion)
                                    if boolExistenInstColgandoDeZonaElimOModifEnConjuntosMM == True:
                                        self.parent.parent.parent.listadoConjuntosMMUsuario = actualizarSuperficieIluminacionDeConjuntosMM(listadoConjuntosMM=self.parent.parent.parent.listadoConjuntosMMUsuario, listadoSubgrupos=self.parent.parent.subgrupos, superficieHabitable=self.parent.parent.parent.panelDatosGenerales.superficie.GetValue())
                                    try:
                                        if self.panelInstalaciones.panelElegirObjeto.iluminacion.GetValue() == True:
                                            nombreInstalacion = self.panelInstalaciones.panel2.nombreInstalacion.GetValue()
                                            encontrado = False
                                            for inst in self.panelInstalaciones.iluminacion:
                                                if inst[0] == nombreInstalacion:
                                                    self.panelInstalaciones.panel2.cargarDatos(inst)
                                                    encontrado = True
                                                    break

                                            if encontrado == False:
                                                self.panelInstalaciones.panel2.onSeleccionarSubgrupo(None)
                                    except:
                                        logging.info(u'Excepcion en: %s' % __name__)

                            else:
                                self.parent.parent.subgrupos[i] = zonaPanel
                            break

                    self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, accionesUndo, datosUndo))
                elif self.compruebaNombres(zonaPanel.nombre) == 'elemento no encontrado':
                    for i in range(len(self.parent.parent.subgrupos)):
                        if self.parent.parent.subgrupos[i].nombre == self.itemAntiguo:
                            datosUndo.append([copy.deepcopy(self.parent.parent.subgrupos[i]), zonaPanel.nombre])
                            accionesUndo.append('modificar zona')
                            cambios = self.ModificarRaizElemento(self.itemAntiguo, zonaPanel.nombre)
                            boolExistenInstColgandoDeZonaElimOModifEnConjuntosMM = existenInstalacionesColgandoDeZonaModificadaOEliminadaEnConjuntosMM(listadoConjuntosMM=self.parent.parent.parent.listadoConjuntosMMUsuario, subgrupoModifOElim=self.itemAntiguo)
                            if boolExistenInstColgandoDeZonaElimOModifEnConjuntosMM == True:
                                self.parent.parent.parent.listadoConjuntosMMUsuario = actualizarNombreSubgrupoDeConjuntosMM(listadoConjuntosMM=self.parent.parent.parent.listadoConjuntosMMUsuario, nombreNuevoSubgrupo=zonaPanel.nombre, nombreAntiguoSubgrupo=self.itemAntiguo)
                            if float(self.parent.parent.subgrupos[i].superficie) != float(zonaPanel.superficie):
                                self.parent.parent.subgrupos[i] = zonaPanel
                                self.actualizarSuperficiesInstalaciones(zonaPanel.superficie, zonaPanel.nombre)
                                if boolExistenInstColgandoDeZonaElimOModifEnConjuntosMM == True:
                                    self.parent.parent.parent.listadoConjuntosMMUsuario = actualizarCoberturaDeConjuntosMM(listadoConjuntosMM=self.parent.parent.parent.listadoConjuntosMMUsuario, superficieCambiada=zonaPanel.superficie, zonaCambiada=zonaPanel.nombre)
                                self.avisoModificacionZona(boolExistenInstColgandoDeZonaElimOModifEnConjuntosMM=boolExistenInstColgandoDeZonaElimOModifEnConjuntosMM)
                                if self.parent.parent.parent.programa == 'GranTerciario':
                                    self.panelInstalaciones.iluminacion = calculoSuperficies.actualizarSuperficiesIluminacion(self.parent.parent.subgrupos, self.parent.parent.parent.panelDatosGenerales.superficie.GetValue(), self.panelInstalaciones.iluminacion)
                                    if boolExistenInstColgandoDeZonaElimOModifEnConjuntosMM == True:
                                        self.parent.parent.parent.listadoConjuntosMMUsuario = actualizarSuperficieIluminacionDeConjuntosMM(listadoConjuntosMM=self.parent.parent.parent.listadoConjuntosMMUsuario, listadoSubgrupos=self.parent.parent.subgrupos, superficieHabitable=self.parent.parent.parent.panelDatosGenerales.superficie.GetValue())
                                    try:
                                        if self.panelInstalaciones.panelElegirObjeto.iluminacion.GetValue() == True:
                                            nombreInstalacion = self.panelInstalaciones.panel2.nombreInstalacion.GetValue()
                                            encontrado = False
                                            for inst in self.panelInstalaciones.iluminacion:
                                                if inst[0] == nombreInstalacion:
                                                    self.panelInstalaciones.panel2.cargarDatos(inst)
                                                    encontrado = True
                                                    break

                                            if encontrado == False:
                                                self.panelInstalaciones.panel2.onSeleccionarSubgrupo(None)
                                    except:
                                        logging.info(u'Excepcion en: %s' % __name__)

                            else:
                                self.parent.parent.subgrupos[i] = zonaPanel
                            for i in range(len(cambios[0])):
                                datosUndo.append(cambios[0][i])
                                accionesUndo.append(cambios[1][i])

                            break

                    self.parent.parent.parent.pilaUndo.apilar(eventoUndo(self.parent, accionesUndo, datosUndo))
                else:
                    wx.MessageBox(_(u'El nombre de la zona modificada ya existe, indique otro'), _(u'Aviso'))
            try:
                self.panelEnvolvente.cargarArbol(self.panelEnvolvente.arbolCerramientos)
                if self.parent.parent.parent.programa == 'GranTerciario' and self.panelInstalaciones.panelElegirObjeto.iluminacion.GetValue() == True:
                    zonaAntigua = self.panelInstalaciones.panel2.subgrupoChoice.GetStringSelection()
                    listaRaices = self.panelInstalaciones.panel2.cargarRaices(self.panelInstalaciones.iluminacion)
                    nombreInstalacion = self.panelInstalaciones.panel2.nombreInstalacion.GetValue()
                    for inst in self.panelInstalaciones.iluminacion:
                        if inst[0] == nombreInstalacion:
                            zonaSeleccionada = inst[-1]
                            listaRaices.append((inst[-1], inst[-1]))
                            break

                    self.panelInstalaciones.panel2.subgrupoChoice.SetItems(listaRaices)
                    self.panelInstalaciones.panel2.subgrupoChoice.SetStringSelection(zonaSeleccionada)
                else:
                    zonaAntigua = self.panelInstalaciones.panel2.subgrupoChoice.GetSelection()
                    if self.panelInstalaciones.panelElegirObjeto.iluminacion.GetValue() == True:
                        self.panelInstalaciones.panel2.subgrupoChoice.SetItems(self.panelInstalaciones.panel2.cargarRaices(self.panelInstalaciones.iluminacion))
                    else:
                        self.panelInstalaciones.panel2.subgrupoChoice.SetItems(self.panelInstalaciones.panel2.cargarRaices())
                    self.panelInstalaciones.panel2.subgrupoChoice.SetSelection(zonaAntigua)
                zonaAntigua = self.panelEnvolvente.panel2.subgrupoChoice.GetSelection()
                self.panelEnvolvente.panel2.subgrupoChoice.SetItems(self.panelEnvolvente.panel2.cargarRaices())
                self.panelEnvolvente.panel2.subgrupoChoice.SetSelection(zonaAntigua)
            except:
                logging.info(u'Excepcion en: %s' % __name__)

            try:
                self.parent.parent.parent.panelInstalaciones.vistaClasica.cargaVista()
            except:
                logging.info(u'Excepcion en: %s' % __name__)

            self.Close()
            return

    def ModificarRaizElemento(self, nombreViejo, nombreNuevo):
        """
        Metodo: ModificarRaizElemento
        
        
        ARGUMENTOS:
                 nombreViejo:
                 nombreNuevo:
        """
        accionesUndo = []
        datosUndo = []
        for i in range(len(self.parent.parent.subgrupos)):
            if nombreViejo == self.parent.parent.subgrupos[i].raiz:
                datosUndo.append([copy.deepcopy(self.parent.parent.subgrupos[i]), self.parent.parent.subgrupos[i].nombre])
                accionesUndo.append('modificar zona')
                self.parent.parent.subgrupos[i].raiz = nombreNuevo

        for i in range(len(self.panelEnvolvente.cerramientos)):
            if nombreViejo == self.panelEnvolvente.cerramientos[i][-2]:
                datosUndo.append([copy.deepcopy(self.panelEnvolvente.cerramientos[i]), self.panelEnvolvente.cerramientos[i][0]])
                accionesUndo.append('modificar cerramiento')
                self.panelEnvolvente.cerramientos[i][-2] = nombreNuevo

        for i in range(len(self.panelInstalaciones.ACS)):
            if nombreViejo == self.panelInstalaciones.ACS[i][-1]:
                datosUndo.append([copy.deepcopy(self.panelInstalaciones.ACS[i]), self.panelInstalaciones.ACS[i][0]])
                accionesUndo.append('modificar ACS')
                self.panelInstalaciones.ACS[i][-1] = nombreNuevo

        for i in range(len(self.panelInstalaciones.calefaccion)):
            if nombreViejo == self.panelInstalaciones.calefaccion[i][-1]:
                datosUndo.append([copy.deepcopy(self.panelInstalaciones.calefaccion[i]), self.panelInstalaciones.calefaccion[i][0]])
                accionesUndo.append('modificar Calefaccion')
                self.panelInstalaciones.calefaccion[i][-1] = nombreNuevo

        for i in range(len(self.panelInstalaciones.refrigeracion)):
            if nombreViejo == self.panelInstalaciones.refrigeracion[i][-1]:
                datosUndo.append([copy.deepcopy(self.panelInstalaciones.refrigeracion[i]), self.panelInstalaciones.refrigeracion[i][0]])
                accionesUndo.append('modificar Refrigeracion')
                self.panelInstalaciones.refrigeracion[i][-1] = nombreNuevo

        for i in range(len(self.panelInstalaciones.climatizacion)):
            if nombreViejo == self.panelInstalaciones.climatizacion[i][-1]:
                datosUndo.append([copy.deepcopy(self.panelInstalaciones.climatizacion[i]), self.panelInstalaciones.climatizacion[i][0]])
                accionesUndo.append('modificar Climatizacion')
                self.panelInstalaciones.climatizacion[i][-1] = nombreNuevo

        for i in range(len(self.panelInstalaciones.mixto2)):
            if nombreViejo == self.panelInstalaciones.mixto2[i][-1]:
                datosUndo.append([copy.deepcopy(self.panelInstalaciones.mixto2[i]), self.panelInstalaciones.mixto2[i][0]])
                accionesUndo.append('modificar Mixto2')
                self.panelInstalaciones.mixto2[i][-1] = nombreNuevo

        for i in range(len(self.panelInstalaciones.mixto3)):
            if nombreViejo == self.panelInstalaciones.mixto3[i][-1]:
                datosUndo.append([copy.deepcopy(self.panelInstalaciones.mixto3[i]), self.panelInstalaciones.mixto3[i][0]])
                accionesUndo.append('modificar Mixto3')
                self.panelInstalaciones.mixto3[i][-1] = nombreNuevo

        for i in range(len(self.panelInstalaciones.contribuciones)):
            if nombreViejo == self.panelInstalaciones.contribuciones[i][-1]:
                datosUndo.append([copy.deepcopy(self.panelInstalaciones.contribuciones[i]), self.panelInstalaciones.contribuciones[i][0]])
                accionesUndo.append('modificar Contribuciones')
                self.panelInstalaciones.contribuciones[i][-1] = nombreNuevo

        for i in range(len(self.panelInstalaciones.iluminacion)):
            if nombreViejo == self.panelInstalaciones.iluminacion[i][-1]:
                datosUndo.append([copy.deepcopy(self.panelInstalaciones.iluminacion[i]), self.panelInstalaciones.iluminacion[i][0]])
                accionesUndo.append('modificar Iluminacion')
                self.panelInstalaciones.iluminacion[i][-1] = nombreNuevo

        for i in range(len(self.panelInstalaciones.ventilacion)):
            if nombreViejo == self.panelInstalaciones.ventilacion[i][-1]:
                datosUndo.append([copy.deepcopy(self.panelInstalaciones.ventilacion[i]), self.panelInstalaciones.ventilacion[i][0]])
                accionesUndo.append('modificar Ventilacion')
                self.panelInstalaciones.ventilacion[i][-1] = nombreNuevo

        for i in range(len(self.panelInstalaciones.ventiladores)):
            if nombreViejo == self.panelInstalaciones.ventiladores[i][-1]:
                datosUndo.append([copy.deepcopy(self.panelInstalaciones.ventiladores[i]), self.panelInstalaciones.ventiladores[i][0]])
                accionesUndo.append('modificar Ventiladores')
                self.panelInstalaciones.ventiladores[i][-1] = nombreNuevo

        for i in range(len(self.panelInstalaciones.bombas)):
            if nombreViejo == self.panelInstalaciones.bombas[i][-1]:
                datosUndo.append([copy.deepcopy(self.panelInstalaciones.bombas[i]), self.panelInstalaciones.bombas[i][0]])
                accionesUndo.append('modificar Bombas')
                self.panelInstalaciones.bombas[i][-1] = nombreNuevo

        for i in range(len(self.panelInstalaciones.torresRefrigeracion)):
            if nombreViejo == self.panelInstalaciones.torresRefrigeracion[i][-1]:
                datosUndo.append([copy.deepcopy(self.panelInstalaciones.torresRefrigeracion[i]), self.panelInstalaciones.torresRefrigeracion[i][0]])
                accionesUndo.append('modificar Torres')
                self.panelInstalaciones.torresRefrigeracion[i][-1] = nombreNuevo

        return [datosUndo, accionesUndo]

    def OnBotonCancelarButton(self, event):
        """
        Metodo: OnBotonCancelarButton
        
        
        ARGUMENTOS:
                 event:
        """
        self.Close()


class claseZona():
    """
    Clase: claseZona del modulo ventanaSubgrupo.py
    
    
    """

    def __init__(self, nombre, raiz, superficie):
        """
        Constructor de la clase
        
        
        ARGUMENTOS:
                 nombre:
                 raiz:
                 superficie:
        """
        self.nombre = nombre
        self.raiz = raiz
        self.superficie = superficie
        self.tipo = 'Subgrupo'