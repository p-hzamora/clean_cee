# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: panelInstalaciones.pyc
# Compiled at: 2015-02-19 13:18:34
"""
Modulo: panelInstalaciones.py

"""
import Instalaciones.panelACS as panelACS, Instalaciones.panelBombas as panelBombas, Instalaciones.panelCalefaccion as panelCalefaccion, Instalaciones.panelClimatizacion as panelClimatizacion, Instalaciones.panelDefinirInstalaciones as panelDefinirInstalaciones, Instalaciones.panelIluminacion as panelIluminacion, Instalaciones.panelInstalacionesBotones as panelInstalacionesBotones, Instalaciones.panelInstalacionesRecuadro as panelInstalacionesRecuadro, Instalaciones.panelMixto2 as panelMixto2, Instalaciones.panelMixto3 as panelMixto3, Instalaciones.panelRefrigeracion as panelRefrigeracion, Instalaciones.panelRenovables as panelRenovables, Instalaciones.panelTorresRefrigeracion as panelTorresRefrigeracion, Instalaciones.panelVentilacion as panelVentilacion, Instalaciones.panelVentiladores as panelVentiladores, Instalaciones.panelVistaClasicaInstalaciones as panelVistaClasicaInstalaciones, directorios, Calculos.listadosWeb as listadosWeb, tips, ventanaSubgrupo, wx, logging
Directorio = directorios.BuscaDirectorios().Directorio
wxID_PANEL1, wxID_PANEL1TREECTRL1, wxID_PANEL1NUEVOSUB, wxID_PANEL1NUEVOELE = [ wx.NewId() for _init_ctrls in range(4) ]

class panelInstalaciones(wx.Panel):
    """
    Clase: panelInstalaciones del modulo panelInstalaciones.py

    """

    def _init_ctrls(self, prnt, id_prnt, pos_prnt, size_prnt, style_prnt, name_prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
                id_prnt:
                pos_prnt:
                size_prnt:
                style_prnt:
                name_prnt:
        """
        wx.Panel.__init__(self, id=id_prnt, name=name_prnt, parent=prnt, pos=pos_prnt, size=size_prnt, style=style_prnt)
        self.SetBackgroundColour('white')
        if self.parent.parent.programa == 'GranTerciario':
            self.listadoOpcionesInstalaciones = listadosWeb.listadoOpcionesInstalacionesTerciario
            self.listadoOpcionesInstalacionesMixtos = listadosWeb.listadoOpcionesInstalacionesTerciario[0:2]
        else:
            self.listadoOpcionesInstalaciones = listadosWeb.listadoOpcionesInstalaciones
            self.listadoOpcionesInstalacionesMixtos = self.listadoOpcionesInstalaciones
        self.listadoCombustibles = [
         'Gas Natural', 'Gasóleo-C', 
         'Electricidad', 
         'GLP', 'Carbón', 'Biocarburante', 'Biomasa/Renovable']
        self.listadoOpcionesAcumulacion = [
         'Conocido',
         'Estimado', 'Por defecto']
        self.listadoInstalaciones = [
         'Caldera Estándar', 
         'Caldera Condensación', 
         'Caldera Baja Temperatura', 
         'Bomba de Calor', 
         'Bomba de Calor - Caudal Ref. Variable', 'Efecto Joule', 
         'Equipo de Rendimiento Constante']
        self.listadoInstalacionesElectrico = [
         'Maquina frigorífica',
         'Máquina frigorífica - Caudal Ref. Variable',
         'Equipo de Rendimiento Constante']
        self.listadoInstalacionesClimatizacion = ['Bomba de Calor',
         'Bomba de Calor - Caudal Ref. Variable',
         'Equipo de Rendimiento Constante']
        self.arbolInstalaciones = wx.TreeCtrl(id=wxID_PANEL1TREECTRL1, name='arbolInstalaciones', parent=self, pos=wx.Point(0, 8), size=wx.Size(216, 584), style=wx.TR_HAS_BUTTONS)
        self.arbolInstalaciones.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnArbolInstalaciones, id=wxID_PANEL1TREECTRL1)
        self.arbolInstalaciones.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.OnArbolItemRightClick, id=wxID_PANEL1TREECTRL1)
        self.nuevoSubgrupo = wx.Button(id=wxID_PANEL1NUEVOSUB, label=_('Zonas'), name='nuevoSubgrupo', parent=self, pos=wx.Point(0, 591), size=wx.Size(50, 20), style=0)
        self.nuevoSubgrupo.Bind(wx.EVT_BUTTON, self.OnNuevoSubgrupo, id=wxID_PANEL1NUEVOSUB)
        self.nuevoSubgrupo.Show(True)
        self.panelElegirObjeto = panelDefinirInstalaciones.Panel1(parent=self, id=-1, pos=wx.Point(230, 8), size=wx.Size(770, 206), style=wx.TAB_TRAVERSAL, name='')
        self.panelRecuadro = panelInstalacionesRecuadro.panelRecuadro(id=-1, name='panelRecuadro', parent=self, pos=wx.Point(230, 214), size=wx.Size(770, 36), style=0)
        self.panelBotones = panelInstalacionesBotones.panelBotones(id=-1, name='panelBotones', parent=self, pos=wx.Point(230, 600), size=wx.Size(770, 100), style=wx.TAB_TRAVERSAL)
        self.panel2 = panelACS.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(770, 350), style=wx.TAB_TRAVERSAL, name='')
        self.vistaClasica = panelVistaClasicaInstalaciones.Panel1(parent=self, id=-1, pos=wx.Point(230, 8), size=wx.Size(770, 580), style=wx.TAB_TRAVERSAL, name='')
        self.vistaClasica.Show(False)

    def OnArbolItemRightClick(self, event):
        """
        Metodo: OnArbolItemRightClick

        ARGUMENTOS:
                event:
        """
        elemento = self.arbolInstalaciones.GetItemText(event.GetItem())
        for i in self.parent.subgrupos:
            if i.nombre == elemento:
                self.submenu = wx.Menu()
                modificar = ['Modificar', wx.NewId()]
                borrar = ['Borrar', wx.NewId()]
                self.submenu.Append(modificar[1], modificar[0])
                self.submenu.Append(borrar[1], borrar[0])
                self.Bind(wx.EVT_MENU, self.onPopMenu, id=modificar[1])
                self.Bind(wx.EVT_MENU, self.onPopMenu, id=borrar[1])
                self.PopupMenu(self.submenu, event.GetPoint())
                break

    def onPopMenu(self, event):
        """
        Metodo: onPopMenu

        ARGUMENTOS:
                event:
        """
        it = self.submenu.GetLabel(event.GetId())
        if 'Modificar' == it:
            self.panelBotones.OnmodificarBoton(event)
        else:
            self.panelBotones.OnBorrarBotonButton(event)

    def OnArbolInstalaciones(self, event):
        """
        Metodo: OnArbolInstalaciones

        ARGUMENTOS:
                event):   ###Cuando pincho en el arb:
        """
        if self.vistaNormal == True:
            nombre = self.arbolInstalaciones.GetItemText(self.arbolInstalaciones.GetSelection())
            for i in self.ACS:
                if nombre == '%s' % i[0]:
                    self.panelRecuadro.titulo.SetLabel(_('Equipo de ACS'))
                    self.panel2.Destroy()
                    self.panel2 = panelACS.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                    self.cargarDatosAlPanel(i, self.panel2)
                    self.panel2.SetSize(wx.Size(770, 350))
                    self.panelElegirObjeto.definirACS.SetValue(True)
                    tips.Acs(self.parent.parent)
                    break

            for i in self.calefaccion:
                if nombre == '%s' % i[0]:
                    self.panelRecuadro.titulo.SetLabel(_('Equipo de sólo calefacción'))
                    self.panel2.Destroy()
                    self.panel2 = panelCalefaccion.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                    tips.Calefaccion(self.parent.parent)
                    self.cargarDatosAlPanel(i, self.panel2)
                    self.panel2.SetSize(wx.Size(770, 350))
                    self.panelElegirObjeto.definirCalefaccion.SetValue(True)
                    break

            for i in self.refrigeracion:
                if nombre == '%s' % i[0]:
                    self.panelRecuadro.titulo.SetLabel(_('Equipo de sólo refrigeración'))
                    self.panel2.Destroy()
                    self.panel2 = panelRefrigeracion.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                    tips.Refrigeracion(self.parent.parent)
                    self.cargarDatosAlPanel(i, self.panel2)
                    self.panel2.SetSize(wx.Size(770, 350))
                    self.panelElegirObjeto.definirRefrigeracion.SetValue(True)
                    break

            for i in self.climatizacion:
                if nombre == '%s' % i[0]:
                    self.panelRecuadro.titulo.SetLabel(_('Equipo de calefacción y refrigeración'))
                    self.panel2.Destroy()
                    self.panel2 = panelClimatizacion.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                    tips.Climatizacion(self.parent.parent)
                    self.cargarDatosAlPanel(i, self.panel2)
                    self.panel2.SetSize(wx.Size(770, 350))
                    self.panelElegirObjeto.definirCaleYRefri.SetValue(True)
                    break

            for i in self.mixto2:
                if nombre == '%s' % i[0]:
                    self.panelRecuadro.titulo.SetLabel(_('Equipo mixto de calefacción y ACS'))
                    self.panel2.Destroy()
                    self.panel2 = panelMixto2.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                    tips.MixtosCaleyAcs(self.parent.parent)
                    self.cargarDatosAlPanel(i, self.panel2)
                    self.panel2.SetSize(wx.Size(770, 350))
                    self.panelElegirObjeto.definirSistemasMixtosCaleyACS.SetValue(True)
                    break

            for i in self.mixto3:
                if nombre == '%s' % i[0]:
                    self.panelRecuadro.titulo.SetLabel(_('Equipo mixto de calefacción, refrigeración y ACS'))
                    self.panel2.Destroy()
                    self.panel2 = panelMixto3.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                    tips.MixtosClimayAcs(self.parent.parent)
                    self.cargarDatosAlPanel(i, self.panel2)
                    self.panel2.SetSize(wx.Size(770, 350))
                    self.panelElegirObjeto.definirSistemasMixtosClimayACS.SetValue(True)
                    break

            for i in self.contribuciones:
                if nombre == '%s' % i[0]:
                    self.panelRecuadro.titulo.SetLabel(_('Contribuciones energéticas'))
                    self.panel2.Destroy()
                    self.panel2 = panelRenovables.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                    tips.Renovables(self.parent.parent)
                    self.panel2.cargarDatos(i)
                    self.panel2.SetSize(wx.Size(770, 350))
                    self.panelElegirObjeto.contribucionesEnergeticas.SetValue(True)
                    break

            for i in self.iluminacion:
                if nombre == '%s' % i[0]:
                    self.panelRecuadro.titulo.SetLabel(_('Equipos de iluminación'))
                    self.panel2.Destroy()
                    self.panel2 = panelIluminacion.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='', instalacionIluminacion=self.iluminacion)
                    tips.Iluminacion(self.parent.parent)
                    self.panel2.cargarDatos(datos=i, instalacionIluminacion=self.iluminacion)
                    self.panel2.SetSize(wx.Size(770, 350))
                    self.panelElegirObjeto.iluminacion.SetValue(True)
                    break

            for i in self.ventilacion:
                if nombre == '%s' % i[0]:
                    self.panelRecuadro.titulo.SetLabel(_('Equipos de aire primario'))
                    self.panel2.Destroy()
                    self.panel2 = panelVentilacion.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                    tips.Ventilacion(self.parent.parent)
                    self.panel2.cargarDatos(i)
                    self.panel2.SetSize(wx.Size(770, 350))
                    self.panelElegirObjeto.ventilacion.SetValue(True)
                    break

            for i in self.ventiladores:
                if nombre == '%s' % i[0]:
                    self.panelRecuadro.titulo.SetLabel(_('Ventiladores'))
                    self.panel2.Destroy()
                    self.panel2 = panelVentiladores.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                    tips.ventiladores(self.parent.parent)
                    self.panel2.cargarDatos(i)
                    self.panel2.SetSize(wx.Size(770, 350))
                    self.panelElegirObjeto.ventiladores.SetValue(True)
                    break

            for i in self.bombas:
                if nombre == '%s' % i[0]:
                    self.panelRecuadro.titulo.SetLabel(_('Equipos de bombeo'))
                    self.panel2.Destroy()
                    self.panel2 = panelBombas.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                    tips.bombas(self.parent.parent)
                    self.panel2.cargarDatos(i)
                    self.panel2.SetSize(wx.Size(770, 350))
                    self.panelElegirObjeto.bombas.SetValue(True)
                    break

            for i in self.torresRefrigeracion:
                if nombre == '%s' % i[0]:
                    self.panelRecuadro.titulo.SetLabel(_('Torres de refrigeración'))
                    self.panel2.Destroy()
                    self.panel2 = panelTorresRefrigeracion.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                    tips.TorresRefrigeracion(self.parent.parent)
                    self.panel2.cargarDatos(i)
                    self.panel2.SetSize(wx.Size(770, 350))
                    self.panelElegirObjeto.torresRefrigeracion.SetValue(True)
                    break

        else:
            nombre = self.arbolInstalaciones.GetItemText(self.arbolInstalaciones.GetSelection())
            for i in range(len(self.ACS)):
                if nombre == self.ACS[i][0]:
                    self.panelElegirObjeto.definirACS.SetValue(True)
                    self.vistaClasica.seleccionCorrecta('ACS', nombre)
                    self.vistaClasica.definirACS.SetValue(True)
                    return

            for i in range(len(self.calefaccion)):
                if nombre == self.calefaccion[i][0]:
                    self.panelElegirObjeto.definirCalefaccion.SetValue(True)
                    self.vistaClasica.seleccionCorrecta('calefaccion', nombre)
                    self.vistaClasica.definirCalefaccion.SetValue(True)
                    return

            for i in range(len(self.refrigeracion)):
                if nombre == self.refrigeracion[i][0]:
                    self.panelElegirObjeto.definirRefrigeracion.SetValue(True)
                    self.vistaClasica.seleccionCorrecta('refrigeracion', nombre)
                    self.vistaClasica.definirRefrigeracion.SetValue(True)
                    return

            for i in range(len(self.climatizacion)):
                if nombre == self.climatizacion[i][0]:
                    self.panelElegirObjeto.definirCaleYRefri.SetValue(True)
                    self.vistaClasica.seleccionCorrecta('calefaccion', nombre)
                    self.vistaClasica.definirCalefaccion.SetValue(True)
                    return

            for i in range(len(self.mixto2)):
                if nombre == self.mixto2[i][0]:
                    self.panelElegirObjeto.definirSistemasMixtosCaleyACS.SetValue(True)
                    self.vistaClasica.seleccionCorrecta('calefaccion', nombre)
                    self.vistaClasica.definirCalefaccion.SetValue(True)
                    return

            for i in range(len(self.mixto3)):
                if nombre == self.mixto3[i][0]:
                    self.panelElegirObjeto.definirSistemasMixtosClimayACS.SetValue(True)
                    self.vistaClasica.seleccionCorrecta('calefaccion', nombre)
                    self.vistaClasica.definirCalefaccion.SetValue(True)
                    return

            for i in range(len(self.contribuciones)):
                if nombre == self.contribuciones[i][0]:
                    self.panelElegirObjeto.contribucionesEnergeticas.SetValue(True)
                    self.vistaClasica.seleccionCorrecta('renovables', nombre)
                    self.vistaClasica.contribucionesEnergeticas.SetValue(True)
                    return

            for i in range(len(self.iluminacion)):
                if nombre == self.iluminacion[i][0]:
                    self.panelElegirObjeto.iluminacion.SetValue(True)
                    self.vistaClasica.seleccionCorrecta('iluminacion', nombre)
                    self.vistaClasica.definirIluminacion.SetValue(True)
                    return

            for i in range(len(self.ventilacion)):
                if nombre == self.ventilacion[i][0]:
                    self.panelElegirObjeto.ventilacion.SetValue(True)
                    self.vistaClasica.seleccionCorrecta('ventilacion', nombre)
                    self.vistaClasica.definirVentilacion.SetValue(True)
                    return

            for i in range(len(self.ventiladores)):
                if nombre == self.ventiladores[i][0]:
                    self.panelElegirObjeto.ventiladores.SetValue(True)
                    self.vistaClasica.seleccionCorrecta('GT', nombre)
                    self.vistaClasica.definirEquposGT.SetValue(True)
                    return

            for i in range(len(self.bombas)):
                if nombre == self.bombas[i][0]:
                    self.panelElegirObjeto.bombas.SetValue(True)
                    self.vistaClasica.seleccionCorrecta('GT', nombre)
                    self.vistaClasica.definirEquposGT.SetValue(True)
                    return

            for i in range(len(self.torresRefrigeracion)):
                if nombre == self.torresRefrigeracion[i][0]:
                    self.panelElegirObjeto.torresRefrigeracion.SetValue(True)
                    self.vistaClasica.seleccionCorrecta('GT', nombre)
                    self.vistaClasica.definirEquposGT.SetValue(True)
                    return

    def OnNuevoSubgrupo(self, event):
        """
        Metodo: OnNuevoSubgrupo

        ARGUMENTOS:
                event:
        """
        superficie = self.parent.parent.panelDatosGenerales.superficie.GetValue()
        try:
            if ',' in superficie:
                superficie = superficie.replace(',', '.')
                self.parent.parent.panelDatosGenerales.superficie.SetValue(superficie)
            float(superficie)
        except (ValueError, TypeError):
            wx.MessageBox(_('Revise la superficie del edificio en el panel de datos generales'), _('Aviso'))
            return

        dlg = ventanaSubgrupo.create(self, -1, wx.Point(200, 200), wx.Size(448, 240), wx.DEFAULT_DIALOG_STYLE, 'ventanaZonas', self.parent.parent.panelEnvolvente, self, 'añadir', None)
        dlg.ShowModal()
        return

    def raizEnArbol(self, metidos, valor):
        """
        Metodo: raizEnArbol

        ARGUMENTOS:
                metidos:
                valor:
        """
        for i in metidos:
            if i[0] == valor:
                return [True, i[1]]

        return [
         False, '']

    def expandidosEnArbol(self, arbol):
        """
        Metodo: expandidosEnArbol

        ARGUMENTOS:
                arbol:
        """
        elem = []
        for i in self.elementosArbol:
            if arbol.IsExpanded(i):
                elem.append(arbol.GetItemText(i))

        return elem

    def expandirAnteriores(self, elementos, arbol):
        """
        Metodo: expandirAnteriores

        ARGUMENTOS:
                elementos:
                arbol:
        """
        for i in elementos:
            for j in self.elementosArbol:
                arbol.GetItemText(j)
                if i == arbol.GetItemText(j):
                    arbol.Expand(j)
                    break

    def cargarArbol(self, arbol):
        """
        Metodo: cargarArbol

        ARGUMENTOS:
                arbol): #funcion para cargar el arb:
        """
        elementosExpandidos = self.expandidosEnArbol(arbol)
        arbol.DeleteAllItems()
        self.elementosArbol = []
        root = arbol.AddRoot(_('Edificio Objeto'))
        arbol.SetItemTextColour(root, 'black')
        arbol.SetItemBold(root)
        arbol.SetItemImage(root, 13, wx.TreeItemIcon_Normal)
        try:
            self.parent.envolvente.recargaArbol(self.parent.envolvente.arbolCerramientos)
        except:
            logging.info('Excepcion en: %s' % __name__)

        datos = []
        for i in self.parent.subgrupos:
            datos.append(i)

        metidos = []
        metidos.append(['Edificio Objeto', root])
        while datos != []:
            for i in range(len(datos)):
                resultado = self.raizEnArbol(metidos, datos[i].raiz)
                if resultado[0] == True:
                    nuevo = arbol.AppendItem(resultado[1], '%s' % datos[i].nombre)
                    self.elementosArbol.append(nuevo)
                    arbol.SetItemTextColour(nuevo, 'grey')
                    arbol.SetItemBold(nuevo)
                    arbol.SetItemImage(nuevo, 12, wx.TreeItemIcon_Normal)
                    metidos.append(['%s' % datos[i].nombre, nuevo])
                    datos.pop(i)
                    break

        for j in self.ACS:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 0, wx.TreeItemIcon_Normal)

        for j in self.calefaccion:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 4, wx.TreeItemIcon_Normal)

        for j in self.refrigeracion:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 3, wx.TreeItemIcon_Normal)

        for j in self.climatizacion:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 5, wx.TreeItemIcon_Normal)

        for j in self.mixto2:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 2, wx.TreeItemIcon_Normal)

        for j in self.mixto3:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 1, wx.TreeItemIcon_Normal)

        for j in self.contribuciones:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 11, wx.TreeItemIcon_Normal)

        for j in self.iluminacion:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 8, wx.TreeItemIcon_Normal)

        for j in self.ventilacion:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 7, wx.TreeItemIcon_Normal)

        for j in self.ventiladores:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 6, wx.TreeItemIcon_Normal)

        for j in self.bombas:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 9, wx.TreeItemIcon_Normal)

        for j in self.torresRefrigeracion:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 10, wx.TreeItemIcon_Normal)

        arbol.Expand(root)
        self.expandirAnteriores(elementosExpandidos, arbol)

    def recargaArbol(self, arbol):
        """
        Metodo: recargaArbol

        ARGUMENTOS:
                arbol): #funcion para cargar el arb:
        """
        arbol.DeleteAllItems()
        self.elementosArbol = []
        root = arbol.AddRoot(_('Edificio Objeto'))
        arbol.SetItemTextColour(root, 'black')
        arbol.SetItemBold(root)
        arbol.SetItemImage(root, 13, wx.TreeItemIcon_Normal)
        datos = []
        for i in self.parent.subgrupos:
            datos.append(i)

        metidos = []
        metidos.append(['Edificio Objeto', root])
        while datos != []:
            for i in range(len(datos)):
                resultado = self.raizEnArbol(metidos, datos[i].raiz)
                if resultado[0] == True:
                    nuevo = arbol.AppendItem(resultado[1], '%s' % datos[i].nombre)
                    self.elementosArbol.append(nuevo)
                    arbol.SetItemTextColour(nuevo, 'grey')
                    arbol.SetItemBold(nuevo)
                    arbol.SetItemImage(nuevo, 12, wx.TreeItemIcon_Normal)
                    metidos.append(['%s' % datos[i].nombre, nuevo])
                    datos.pop(i)
                    break

        for j in self.ACS:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 0, wx.TreeItemIcon_Normal)

        for j in self.calefaccion:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 4, wx.TreeItemIcon_Normal)

        for j in self.refrigeracion:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 3, wx.TreeItemIcon_Normal)

        for j in self.climatizacion:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 5, wx.TreeItemIcon_Normal)

        for j in self.mixto2:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 2, wx.TreeItemIcon_Normal)

        for j in self.mixto3:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 1, wx.TreeItemIcon_Normal)

        for j in self.contribuciones:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 11, wx.TreeItemIcon_Normal)

        for j in self.iluminacion:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 8, wx.TreeItemIcon_Normal)

        for j in self.ventilacion:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 7, wx.TreeItemIcon_Normal)

        for j in self.ventiladores:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 6, wx.TreeItemIcon_Normal)

        for j in self.bombas:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 9, wx.TreeItemIcon_Normal)

        for j in self.torresRefrigeracion:
            resultado = self.raizEnArbol(metidos, j[-1])
            nuevo = arbol.AppendItem(resultado[1], '%s' % j[0])
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 10, wx.TreeItemIcon_Normal)

        arbol.Expand(root)
        try:
            self.panel2.raizchoice.SetItems(self.panel2.cargarRaices())
        except:
            logging.info('Excepcion en: %s' % __name__)

        arbol.Expand(root)

    def iniciaIconosArbol(self):
        """
        Metodo: iniciaIconosArbol

        """
        self.iconosArbol = wx.ImageList(14, 14, True, 1)
        aguaCaliente = wx.Bitmap(Directorio + '/Imagenes/aguaCaliente.ico')
        calefaccionRefrigeracionAguaCaliente = wx.Bitmap(Directorio + '/Imagenes/calefaccionRefrigeracionAguaCaliente.ico')
        calefaccionAguaCaliente = wx.Bitmap(Directorio + '/Imagenes/calefaccionAguaCaliente.ico')
        refrigeracion = wx.Bitmap(Directorio + '/Imagenes/refrigeracion.ico')
        calefaccion = wx.Bitmap(Directorio + '/Imagenes/calefaccion.ico')
        calefaccionRefrigeracion = wx.Bitmap(Directorio + '/Imagenes/calefaccionRefrigeracion.ico')
        ventiladores = wx.Bitmap(Directorio + '/Imagenes/ventiladores.ico')
        ventilacion = wx.Bitmap(Directorio + '/Imagenes/ventilacion.ico')
        iluminacion = wx.Bitmap(Directorio + '/Imagenes/iluminacion.ico')
        bombeo = wx.Bitmap(Directorio + '/Imagenes/bombeo.ico')
        torreRefrigeracion = wx.Bitmap(Directorio + '/Imagenes/torreRefrigeracion.ico')
        contribuciones = wx.Bitmap(Directorio + '/Imagenes/contribuciones.ico')
        zona = wx.Bitmap(Directorio + '/Imagenes/zona.ico')
        edificioObjeto = wx.Bitmap(Directorio + '/Imagenes/edificioObjeto.ico')
        self.iconosArbol.Add(aguaCaliente)
        self.iconosArbol.Add(calefaccionRefrigeracionAguaCaliente)
        self.iconosArbol.Add(calefaccionAguaCaliente)
        self.iconosArbol.Add(refrigeracion)
        self.iconosArbol.Add(calefaccion)
        self.iconosArbol.Add(calefaccionRefrigeracion)
        self.iconosArbol.Add(ventiladores)
        self.iconosArbol.Add(ventilacion)
        self.iconosArbol.Add(iluminacion)
        self.iconosArbol.Add(bombeo)
        self.iconosArbol.Add(torreRefrigeracion)
        self.iconosArbol.Add(contribuciones)
        self.iconosArbol.Add(zona)
        self.iconosArbol.Add(edificioObjeto)
        self.arbolInstalaciones.SetImageList(self.iconosArbol)

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
        self.init_vectors()
        self.parent = parent
        self._init_ctrls(parent, id, pos, size, style, name)
        self.nombre = _('Instalaciones')
        self.iniciaIconosArbol()
        self.elementosArbol = []
        self.cargarArbol(self.arbolInstalaciones)
        self.vistaNormal = True

    def init_vectors(self):
        """
        Metodo: init_vectors

        """
        self.ACS = []
        self.calefaccion = []
        self.refrigeracion = []
        self.climatizacion = []
        self.mixto2 = []
        self.mixto3 = []
        self.contribuciones = []
        self.iluminacion = []
        self.ventilacion = []
        self.ventiladores = []
        self.bombas = []
        self.torresRefrigeracion = []

    def cogerDatos(self):
        """
        Metodo: cogerDatos

                self):   ###Coge los datos para guardarlos en el archivo .c:
        """
        datos = []
        datos.append(self.ACS)
        datos.append(self.calefaccion)
        datos.append(self.refrigeracion)
        datos.append(self.climatizacion)
        datos.append(self.mixto2)
        datos.append(self.mixto3)
        datos.append(self.contribuciones)
        datos.append(self.iluminacion)
        datos.append(self.ventilacion)
        datos.append(self.ventiladores)
        datos.append(self.bombas)
        datos.append(self.torresRefrigeracion)
        return datos

    def exportarDatos(self):
        """
        Metodo: exportarDatos

                self):  ###Carga datos al abrir un nuevo archi:
        """
        instalaciones = [
         self.ACS, self.calefaccion, self.refrigeracion, self.climatizacion,
         self.mixto2, self.mixto3, self.contribuciones, self.iluminacion,
         self.ventilacion, self.ventiladores, self.bombas, self.torresRefrigeracion]
        return instalaciones

    def cargarDatos(self, datos):
        """
        Metodo: cargarDatos

        ARGUMENTOS:
                datos:
        """
        self.ACS = []
        for i in datos[0]:
            self.ACS.append(i)

        self.calefaccion = []
        for i in datos[1]:
            self.calefaccion.append(i)

        self.refrigeracion = []
        for i in datos[2]:
            self.refrigeracion.append(i)

        self.climatizacion = []
        for i in datos[3]:
            self.climatizacion.append(i)

        self.mixto2 = []
        for i in datos[4]:
            self.mixto2.append(i)

        self.mixto3 = []
        for i in datos[5]:
            self.mixto3.append(i)

        self.contribuciones = []
        for i in datos[6]:
            self.contribuciones.append(i)

        self.iluminacion = []
        for i in datos[7]:
            self.iluminacion.append(i)

        self.ventilacion = []
        for i in datos[8]:
            self.ventilacion.append(i)

        self.ventiladores = []
        for i in datos[9]:
            self.ventiladores.append(i)

        self.bombas = []
        for i in datos[10]:
            self.bombas.append(i)

        self.torresRefrigeracion = []
        for i in datos[11]:
            self.torresRefrigeracion.append(i)

        self.cargarArbol(self.arbolInstalaciones)
        self.panelElegirObjeto.definirACS.SetValue(True)
        self.panelElegirObjeto.OntipoInstalacion(None)
        return

    def cogerDatosDelPanel(self, panelObjeto):
        """
        Metodo: cogerDatosDelPanel

        ARGUMENTOS:
                panelObjeto):   ###Recoge datos de los panel:
        """
        panelObjeto.comprobarDatos()
        if panelObjeto.listaErrores != '':
            return panelObjeto.listaErrores
        datos = []
        datos.append(panelObjeto.nombreInstalacion.GetValue())
        datos.append(panelObjeto.tipoSistema)
        arrayRendimientosEstacionales = [
         '', '', '']
        if panelObjeto.tipoSistema == 'ACS':
            arrayRendimientosEstacionales[0] = panelObjeto.rendimientoEstacionalACS
        elif panelObjeto.tipoSistema == 'calefaccion':
            arrayRendimientosEstacionales[1] = panelObjeto.rendimientoEstacionalCal
        elif panelObjeto.tipoSistema == 'refrigeracion':
            arrayRendimientosEstacionales[2] = panelObjeto.rendimientoEstacionalRef
        elif panelObjeto.tipoSistema == 'climatizacion':
            arrayRendimientosEstacionales[1] = panelObjeto.rendimientoEstacionalCal
            arrayRendimientosEstacionales[2] = panelObjeto.rendimientoEstacionalRef
        elif panelObjeto.tipoSistema == 'mixto2':
            arrayRendimientosEstacionales[0] = panelObjeto.rendimientoEstacionalACS
            arrayRendimientosEstacionales[1] = panelObjeto.rendimientoEstacionalCal
        elif panelObjeto.tipoSistema == 'mixto3':
            arrayRendimientosEstacionales[0] = panelObjeto.rendimientoEstacionalACS
            arrayRendimientosEstacionales[1] = panelObjeto.rendimientoEstacionalCal
            arrayRendimientosEstacionales[2] = panelObjeto.rendimientoEstacionalRef
        datos.append(arrayRendimientosEstacionales)
        datos.append(panelObjeto.generadorChoice.GetStringSelection())
        datos.append(panelObjeto.combustibleChoice.GetStringSelection())
        arrayCobertura = [
         [
          '', ''], ['', ''], ['', '']]
        if panelObjeto.tipoSistema == 'ACS':
            arrayCobertura[0][0] = panelObjeto.coberturaMetros.GetValue()
            arrayCobertura[0][1] = panelObjeto.coberturaPorcentaje.GetValue()
        elif panelObjeto.tipoSistema == 'calefaccion':
            arrayCobertura[1][0] = panelObjeto.coberturaMetros.GetValue()
            arrayCobertura[1][1] = panelObjeto.coberturaPorcentaje.GetValue()
        elif panelObjeto.tipoSistema == 'refrigeracion':
            arrayCobertura[2][0] = panelObjeto.coberturaMetros.GetValue()
            arrayCobertura[2][1] = panelObjeto.coberturaPorcentaje.GetValue()
        elif panelObjeto.tipoSistema == 'climatizacion':
            arrayCobertura[1][0] = panelObjeto.coberturaMetros.GetValue()
            arrayCobertura[1][1] = panelObjeto.coberturaPorcentaje.GetValue()
            arrayCobertura[2][0] = panelObjeto.coberturaMetros2.GetValue()
            arrayCobertura[2][1] = panelObjeto.coberturaPorcentaje2.GetValue()
        elif panelObjeto.tipoSistema == 'mixto2':
            arrayCobertura[0][0] = panelObjeto.coberturaMetros.GetValue()
            arrayCobertura[0][1] = panelObjeto.coberturaPorcentaje.GetValue()
            arrayCobertura[1][0] = panelObjeto.coberturaMetros2.GetValue()
            arrayCobertura[1][1] = panelObjeto.coberturaPorcentaje2.GetValue()
        elif panelObjeto.tipoSistema == 'mixto3':
            arrayCobertura[0][0] = panelObjeto.coberturaMetros3.GetValue()
            arrayCobertura[0][1] = panelObjeto.coberturaPorcentaje3.GetValue()
            arrayCobertura[1][0] = panelObjeto.coberturaMetros.GetValue()
            arrayCobertura[1][1] = panelObjeto.coberturaPorcentaje.GetValue()
            arrayCobertura[2][0] = panelObjeto.coberturaMetros2.GetValue()
            arrayCobertura[2][1] = panelObjeto.coberturaPorcentaje2.GetValue()
        datos.append(arrayCobertura)
        datos.append(panelObjeto.rendimientoChoice.GetStringSelection())
        datosEquipoGenerador = []
        if panelObjeto.generadorChoice.GetStringSelection() == 'Equipo de Rendimiento Constante':
            rendimiento = [
             '', '', '']
            if panelObjeto.tipoSistema == 'ACS':
                rendimiento[0] = panelObjeto.rendimietoMedio.GetValue()
            elif panelObjeto.tipoSistema == 'calefaccion':
                rendimiento[1] = panelObjeto.rendimietoMedio.GetValue()
            elif panelObjeto.tipoSistema == 'refrigeracion':
                rendimiento[2] = panelObjeto.rendimietoMedio.GetValue()
            elif panelObjeto.tipoSistema == 'climatizacion':
                rendimiento[1] = panelObjeto.rendimietoMedio.GetValue()
                rendimiento[2] = panelObjeto.rendimietoMedio2.GetValue()
            elif panelObjeto.tipoSistema == 'mixto2':
                rendimiento[0] = panelObjeto.rendimietoMedio.GetValue()
                rendimiento[1] = panelObjeto.rendimietoMedio2.GetValue()
            elif panelObjeto.tipoSistema == 'mixto3':
                rendimiento[0] = panelObjeto.rendimietoMedio3.GetValue()
                rendimiento[1] = panelObjeto.rendimietoMedio.GetValue()
                rendimiento[2] = panelObjeto.rendimietoMedio2.GetValue()
            datosEquipoGenerador = rendimiento
        elif panelObjeto.generadorChoice.GetStringSelection() in ('Caldera Estándar',
                                                                  'Caldera Condensación',
                                                                  'Caldera Baja Temperatura') and panelObjeto.combustibleChoice.GetStringSelection() != 'Electricidad':
            if 'Conocido' in panelObjeto.rendimientoChoice.GetStringSelection():
                if panelObjeto.tipoSistema == 'ACS' or panelObjeto.tipoSistema == 'calefaccion':
                    datosEquipoGenerador = [
                     panelObjeto.rendimietoMedio.GetValue()]
                elif panelObjeto.tipoSistema == 'mixto2':
                    datosEquipoGenerador = [
                     panelObjeto.rendimietoMedio.GetValue(), panelObjeto.rendimietoMedio2.GetValue()]
            else:
                if 'Estimado según Instalación' in panelObjeto.rendimientoChoice.GetStringSelection():
                    datosEquipoGenerador = [
                     panelObjeto.aislanteCaldera.GetStringSelection(),
                     panelObjeto.rendimientoCombustion.GetValue(),
                     panelObjeto.cargaMedia.GetValue(),
                     panelObjeto.potenciaNominal.GetValue(),
                     panelObjeto.vectorTipoCaldera,
                     panelObjeto.arrayAyudaCalefaccion]
                else:
                    datosEquipoGenerador = [
                     panelObjeto.potNominal.GetValue(), panelObjeto.rendNominalPG.GetValue(),
                     panelObjeto.factorCargaMinimo.GetValue(),
                     panelObjeto.factorCargaMaximo.GetValue(),
                     panelObjeto.temperaturaAmbienteInt.GetValue(), panelObjeto.temperaturas,
                     panelObjeto.curvaRendimiento]
        elif 'Conocido' in panelObjeto.rendimientoChoice.GetStringSelection():
            rendimientoMedio = [
             '', '', '']
            if panelObjeto.tipoSistema == 'ACS':
                rendimientoMedio = [
                 panelObjeto.rendimietoMedio.GetValue(), '', '']
            elif panelObjeto.tipoSistema == 'calefaccion':
                rendimientoMedio = [
                 '', panelObjeto.rendimietoMedio.GetValue(), '']
            elif panelObjeto.tipoSistema == 'refrigeracion':
                rendimientoMedio = [
                 '', '', panelObjeto.rendimietoMedio.GetValue()]
            if panelObjeto.tipoSistema == 'climatizacion':
                rendimientoMedio = [
                 '', panelObjeto.rendimietoMedio.GetValue(),
                 panelObjeto.rendimietoMedio2.GetValue()]
            elif panelObjeto.tipoSistema == 'mixto2':
                rendimientoMedio = [
                 panelObjeto.rendimietoMedio.GetValue(),
                 panelObjeto.rendimietoMedio2.GetValue(), '']
            elif panelObjeto.tipoSistema == 'mixto3':
                rendimientoMedio = [
                 panelObjeto.rendimietoMedio3.GetValue(), panelObjeto.rendimietoMedio.GetValue(),
                 panelObjeto.rendimietoMedio2.GetValue()]
            datosEquipoGenerador = rendimientoMedio
        elif 'Estimado según Instalación' in panelObjeto.rendimientoChoice.GetStringSelection():
            if panelObjeto.definirAntiguedadChoice.GetSelection() == 0:
                array_antiguedad = [
                 True, False, False]
            elif panelObjeto.definirAntiguedadChoice.GetSelection() == 1:
                array_antiguedad = [
                 False, True, False]
            else:
                array_antiguedad = [
                 False, False, True]
            rendimientoNominal = [
             '', '', '']
            if panelObjeto.tipoSistema == 'ACS' or panelObjeto.tipoSistema == 'calefaccion' or panelObjeto.tipoSistema == 'refrigeracion':
                array_variosGeneradores = [
                 panelObjeto.VariosGeneradoresCheck.GetValue(),
                 panelObjeto.FraccionPotencia.GetValue(),
                 panelObjeto.fraccionPotenciaEntrada.GetValue()]
            else:
                array_variosGeneradores = []
            if panelObjeto.tipoSistema == 'ACS':
                rendimientoNominal = [
                 panelObjeto.rendimientoNominal.GetValue(), '', '']
            elif panelObjeto.tipoSistema == 'calefaccion':
                rendimientoNominal = [
                 '', panelObjeto.rendimientoNominal.GetValue(), '']
            elif panelObjeto.tipoSistema == 'refrigeracion':
                rendimientoNominal = [
                 '', '', panelObjeto.rendimientoNominal.GetValue()]
            elif panelObjeto.tipoSistema == 'climatizacion':
                rendimientoNominal = [
                 '', panelObjeto.rendimientoNominal.GetValue(),
                 panelObjeto.rendimientoNominal2.GetValue()]
            elif panelObjeto.tipoSistema == 'mixto2':
                rendimientoNominal = [
                 panelObjeto.rendimientoNominal.GetValue(),
                 panelObjeto.rendimientoNominal.GetValue(), '']
            elif panelObjeto.tipoSistema == 'mixto3':
                rendimientoNominal = [
                 panelObjeto.rendimientoNominal3.GetValue(),
                 panelObjeto.rendimientoNominal.GetValue(),
                 panelObjeto.rendimientoNominal2.GetValue()]
            if panelObjeto.tipoSistema == 'refrigeracion':
                datosEquipoGenerador = [
                 rendimientoNominal, array_antiguedad, array_variosGeneradores,
                 panelObjeto.caracteristicasBDCChoice.GetSelection()]
            else:
                datosEquipoGenerador = [
                 rendimientoNominal, array_antiguedad, array_variosGeneradores]
        elif panelObjeto.tipoSistema == 'ACS' or panelObjeto.tipoSistema == 'calefaccion':
            datosEquipoGenerador = [
             panelObjeto.potNominal.GetValue(), panelObjeto.rendNominalPG.GetValue(),
             panelObjeto.factorCargaMinimo.GetValue(),
             panelObjeto.factorCargaMaximo.GetValue(),
             panelObjeto.temperaturaAmbienteInt.GetValue(),
             panelObjeto.temperaturas, panelObjeto.curvaRendimiento]
        elif panelObjeto.tipoSistema == 'refrigeracion':
            datosEquipoGenerador = [
             panelObjeto.potNominal.GetValue(), panelObjeto.rendNominalPG.GetValue(),
             panelObjeto.factorCargaMinimo.GetValue(),
             panelObjeto.factorCargaMaximo.GetValue(),
             panelObjeto.temperaturaAmbienteInt.GetValue(),
             panelObjeto.temperaturas, panelObjeto.curvaRendimiento,
             panelObjeto.caracteristicasBDCChoice.GetSelection()]
        datos.append(datosEquipoGenerador)
        datosEquipoACS = []
        if panelObjeto.tipoSistema == 'ACS' or panelObjeto.tipoSistema == 'mixto2' or panelObjeto.tipoSistema == 'mixto3':
            if panelObjeto.acumulacionCheck.GetValue() == False:
                datosEquipoACS = [
                 panelObjeto.acumulacionCheck.GetValue()]
            else:
                datosEquipoACS.append(panelObjeto.acumulacionCheck.GetValue())
                datosEquipoACS.append(panelObjeto.volumen.GetValue())
                datosEquipoACS.append(panelObjeto.temperaturaAlta.GetValue())
                datosEquipoACS.append(panelObjeto.temperaturaBaja.GetValue())
                valorUAAcumulacion = panelObjeto.UAvalor.GetValue()
                datosEquipoACS.append(valorUAAcumulacion)
                datosEquipoACS.append(panelObjeto.valorUAChoice.GetStringSelection())
                if 'Conocido' not in panelObjeto.valorUAChoice.GetStringSelection():
                    if 'Estimado' in panelObjeto.valorUAChoice.GetStringSelection():
                        datosEquipoACS.append(panelObjeto.espesorAislamiento.GetValue())
                        datosEquipoACS.append(panelObjeto.aislamientoAcumulacionChoice.GetStringSelection())
                    datosEquipoACS.append(panelObjeto.multiplicador.GetValue())
            datos.append(datosEquipoACS)
        datos.append(panelObjeto.subgrupoChoice.GetStringSelection())
        return datos

    def cargarDatosAlPanel(self, datos, panelObjeto):
        """
        Metodo: cargarDatosAlPanel

        ARGUMENTOS:
                datos:
                panelObjeto):   ###carga datos al panel que ha:
        """
        panelObjeto.nombreInstalacion.SetValue(datos[0])
        panelObjeto.tipoSistema = datos[1]
        arrayRendimientosEstacionales = datos[2]
        if panelObjeto.tipoSistema == 'ACS':
            self.panelElegirObjeto.definirACS.SetValue(True)
            panelObjeto.rendimientoEstacionalACS = arrayRendimientosEstacionales[0]
        elif panelObjeto.tipoSistema == 'calefaccion':
            self.panelElegirObjeto.definirCalefaccion.SetValue(True)
            panelObjeto.rendimientoEstacionalCal = arrayRendimientosEstacionales[1]
        elif panelObjeto.tipoSistema == 'refrigeracion':
            self.panelElegirObjeto.definirRefrigeracion.SetValue(True)
            panelObjeto.rendimientoEstacionalRef = arrayRendimientosEstacionales[2]
        elif panelObjeto.tipoSistema == 'climatizacion':
            self.panelElegirObjeto.definirCaleYRefri.SetValue(True)
            panelObjeto.rendimientoEstacionalCal = arrayRendimientosEstacionales[1]
            panelObjeto.rendimientoEstacionalRef = arrayRendimientosEstacionales[2]
        elif panelObjeto.tipoSistema == 'mixto2':
            self.panelElegirObjeto.definirSistemasMixtosCaleyACS.SetValue(True)
            panelObjeto.rendimientoEstacionalACS = arrayRendimientosEstacionales[0]
            panelObjeto.rendimientoEstacionalCal = arrayRendimientosEstacionales[1]
        elif panelObjeto.tipoSistema == 'mixto3':
            self.panelElegirObjeto.definirSistemasMixtosClimayACS.SetValue(True)
            panelObjeto.rendimientoEstacionalACS = arrayRendimientosEstacionales[0]
            panelObjeto.rendimientoEstacionalCal = arrayRendimientosEstacionales[1]
            panelObjeto.rendimientoEstacionalRef = arrayRendimientosEstacionales[2]
        panelObjeto.generadorChoice.SetStringSelection(datos[3])
        tipoGenerador = datos[3]
        panelObjeto.OngeneradorChoice(None)
        combustible = datos[4]
        panelObjeto.combustibleChoice.SetStringSelection(datos[4])
        if panelObjeto.tipoSistema in ('ACS', 'calefaccion'):
            panelObjeto.cargaModoObtencion()
        arrayCobertura = datos[5]
        if panelObjeto.tipoSistema == 'ACS':
            panelObjeto.coberturaMetros.SetValue(arrayCobertura[0][0])
            panelObjeto.coberturaPorcentaje.SetValue(arrayCobertura[0][1])
        else:
            if panelObjeto.tipoSistema == 'calefaccion':
                panelObjeto.coberturaMetros.SetValue(arrayCobertura[1][0])
                panelObjeto.coberturaPorcentaje.SetValue(arrayCobertura[1][1])
            if panelObjeto.tipoSistema == 'refrigeracion':
                panelObjeto.coberturaMetros.SetValue(arrayCobertura[2][0])
                panelObjeto.coberturaPorcentaje.SetValue(arrayCobertura[2][1])
            elif panelObjeto.tipoSistema == 'climatizacion':
                panelObjeto.coberturaMetros.SetValue(arrayCobertura[1][0])
                panelObjeto.coberturaPorcentaje.SetValue(arrayCobertura[1][1])
                panelObjeto.coberturaMetros2.SetValue(arrayCobertura[2][0])
                panelObjeto.coberturaPorcentaje2.SetValue(arrayCobertura[2][1])
            elif panelObjeto.tipoSistema == 'mixto2':
                panelObjeto.coberturaMetros.SetValue(arrayCobertura[0][0])
                panelObjeto.coberturaPorcentaje.SetValue(arrayCobertura[0][1])
                panelObjeto.coberturaMetros2.SetValue(arrayCobertura[1][0])
                panelObjeto.coberturaPorcentaje2.SetValue(arrayCobertura[1][1])
            elif panelObjeto.tipoSistema == 'mixto3':
                panelObjeto.coberturaMetros.SetValue(arrayCobertura[1][0])
                panelObjeto.coberturaPorcentaje.SetValue(arrayCobertura[1][1])
                panelObjeto.coberturaMetros2.SetValue(arrayCobertura[2][0])
                panelObjeto.coberturaPorcentaje2.SetValue(arrayCobertura[2][1])
                panelObjeto.coberturaMetros3.SetValue(arrayCobertura[0][0])
                panelObjeto.coberturaPorcentaje3.SetValue(arrayCobertura[0][1])
            try:
                panelObjeto.rendimientoChoice.SetStringSelection(datos[6])
                definicionInstalacion = datos[6]
                datosEquipoGenerador = datos[7]
                if tipoGenerador == 'Equipo de Rendimiento Constante':
                    rendimiento = datosEquipoGenerador
                    if panelObjeto.tipoSistema == 'ACS':
                        panelObjeto.rendimietoMedio.SetValue(rendimiento[0])
                    else:
                        if panelObjeto.tipoSistema == 'calefaccion':
                            panelObjeto.rendimietoMedio.SetValue(rendimiento[1])
                        elif panelObjeto.tipoSistema == 'refrigeracion':
                            panelObjeto.rendimietoMedio.SetValue(rendimiento[2])
                    if panelObjeto.tipoSistema == 'climatizacion':
                        panelObjeto.rendimietoMedio.SetValue(rendimiento[1])
                        panelObjeto.rendimietoMedio2.SetValue(rendimiento[2])
                    else:
                        if panelObjeto.tipoSistema == 'mixto2':
                            panelObjeto.rendimietoMedio.SetValue(rendimiento[0])
                            panelObjeto.rendimietoMedio2.SetValue(rendimiento[1])
                        elif panelObjeto.tipoSistema == 'mixto3':
                            panelObjeto.rendimietoMedio3.SetValue(rendimiento[0])
                            panelObjeto.rendimietoMedio.SetValue(rendimiento[1])
                            panelObjeto.rendimietoMedio2.SetValue(rendimiento[2])
                elif tipoGenerador in ('Caldera Estándar', 'Caldera Condensación',
                                       'Caldera Baja Temperatura') and combustible != 'Electricidad':
                    if 'Conocido' in definicionInstalacion:
                        panelObjeto.rendimietoMedio.SetValue(datosEquipoGenerador[0])
                        if panelObjeto.tipoSistema == 'mixto2':
                            try:
                                panelObjeto.rendimietoMedio2.SetValue(datosEquipoGenerador[1])
                            except:
                                logging.info('Excepcion en: %s' % __name__)
                                panelObjeto.rendimietoMedio2.SetValue(datosEquipoGenerador[0])

                    elif 'Estimado según Instalación' in definicionInstalacion:
                        panelObjeto.aislanteCaldera.SetStringSelection(datosEquipoGenerador[0])
                        panelObjeto.rendimientoCombustion.SetValue(datosEquipoGenerador[1])
                        panelObjeto.cargaMedia.SetValue(datosEquipoGenerador[2])
                        panelObjeto.potenciaNominal.SetValue(datosEquipoGenerador[3])
                        panelObjeto.vectorTipoCaldera = datosEquipoGenerador[4]
                        panelObjeto.arrayAyudaCalefaccion = datosEquipoGenerador[5]
                    else:
                        panelObjeto.potNominal.SetValue(datosEquipoGenerador[0])
                        panelObjeto.rendNominalPG.SetValue(datosEquipoGenerador[1])
                        panelObjeto.factorCargaMinimo.SetValue(datosEquipoGenerador[2])
                        panelObjeto.factorCargaMaximo.SetValue(datosEquipoGenerador[3])
                        panelObjeto.temperaturaAmbienteInt.SetValue(datosEquipoGenerador[4])
                        panelObjeto.temperaturas = datosEquipoGenerador[5]
                        panelObjeto.curvaRendimiento = datosEquipoGenerador[6]
                elif 'Conocido' in definicionInstalacion:
                    rendimientoMedio = datosEquipoGenerador
                    if panelObjeto.tipoSistema == 'ACS':
                        panelObjeto.rendimietoMedio.SetValue(rendimientoMedio[0])
                    else:
                        if panelObjeto.tipoSistema == 'calefaccion':
                            panelObjeto.rendimietoMedio.SetValue(rendimientoMedio[1])
                        elif panelObjeto.tipoSistema == 'refrigeracion':
                            panelObjeto.rendimietoMedio.SetValue(rendimientoMedio[2])
                    if panelObjeto.tipoSistema == 'climatizacion':
                        panelObjeto.rendimietoMedio.SetValue(rendimientoMedio[1])
                        panelObjeto.rendimietoMedio2.SetValue(rendimientoMedio[2])
                    else:
                        if panelObjeto.tipoSistema == 'mixto2':
                            panelObjeto.rendimietoMedio.SetValue(rendimientoMedio[0])
                            panelObjeto.rendimietoMedio2.SetValue(rendimientoMedio[1])
                        elif panelObjeto.tipoSistema == 'mixto3':
                            panelObjeto.rendimietoMedio3.SetValue(rendimientoMedio[0])
                            panelObjeto.rendimietoMedio.SetValue(rendimientoMedio[1])
                            panelObjeto.rendimietoMedio2.SetValue(rendimientoMedio[2])
                elif 'Estimado según Instalación' in definicionInstalacion:
                    rendimientoNominal = datosEquipoGenerador[0]
                    array_antiguedad = datosEquipoGenerador[1]
                    if array_antiguedad[0] == True:
                        panelObjeto.definirAntiguedadChoice.SetSelection(0)
                    elif array_antiguedad[1] == True:
                        panelObjeto.definirAntiguedadChoice.SetSelection(1)
                    else:
                        panelObjeto.definirAntiguedadChoice.SetSelection(2)
                    if panelObjeto.tipoSistema == 'ACS' or panelObjeto.tipoSistema == 'calefaccion' or panelObjeto.tipoSistema == 'refrigeracion':
                        array_variosGeneradores = datosEquipoGenerador[2]
                        panelObjeto.VariosGeneradoresCheck.SetValue(array_variosGeneradores[0])
                        panelObjeto.FraccionPotencia.SetValue(array_variosGeneradores[1])
                        panelObjeto.fraccionPotenciaEntrada.SetValue(array_variosGeneradores[2])
                    if panelObjeto.tipoSistema == 'ACS':
                        panelObjeto.rendimientoNominal.SetValue(rendimientoNominal[0])
                    else:
                        if panelObjeto.tipoSistema == 'calefaccion':
                            panelObjeto.rendimientoNominal.SetValue(rendimientoNominal[1])
                        elif panelObjeto.tipoSistema == 'refrigeracion':
                            panelObjeto.rendimientoNominal.SetValue(rendimientoNominal[2])
                            panelObjeto.caracteristicasBDCChoice.SetSelection(datosEquipoGenerador[3])
                    if panelObjeto.tipoSistema == 'climatizacion':
                        panelObjeto.rendimientoNominal.SetValue(rendimientoNominal[1])
                        panelObjeto.rendimientoNominal2.SetValue(rendimientoNominal[2])
                    else:
                        if panelObjeto.tipoSistema == 'mixto2':
                            panelObjeto.rendimientoNominal.SetValue(rendimientoNominal[0])
                        elif panelObjeto.tipoSistema == 'mixto3':
                            panelObjeto.rendimientoNominal3.SetValue(rendimientoNominal[0])
                            panelObjeto.rendimientoNominal.SetValue(rendimientoNominal[1])
                            panelObjeto.rendimientoNominal2.SetValue(rendimientoNominal[2])
                else:
                    panelObjeto.potNominal.SetValue(datosEquipoGenerador[0])
                    panelObjeto.rendNominalPG.SetValue(datosEquipoGenerador[1])
                    panelObjeto.factorCargaMinimo.SetValue(datosEquipoGenerador[2])
                    panelObjeto.factorCargaMaximo.SetValue(datosEquipoGenerador[3])
                    panelObjeto.temperaturaAmbienteInt.SetValue(datosEquipoGenerador[4])
                    panelObjeto.temperaturas = datosEquipoGenerador[5]
                    panelObjeto.curvaRendimiento = datosEquipoGenerador[6]
                    if panelObjeto.tipoSistema == 'refrigeracion':
                        panelObjeto.caracteristicasBDCChoice.SetSelection(datosEquipoGenerador[7])
                        if datosEquipoGenerador[7] == 0 or datosEquipoGenerador[7] == 2:
                            panelObjeto.temperaturaAmbienteIntText.SetLabel(_('Temperatura ambiente interior'))
                        else:
                            panelObjeto.temperaturaAmbienteIntText.SetLabel(_('Temperatura impulsión agua'))
            except:
                logging.info('Excepcion en: %s' % __name__)
                panelObjeto.rendimientoChoice.SetStringSelection('Estimado según Instalación')

            if panelObjeto.tipoSistema == 'ACS' or panelObjeto.tipoSistema == 'mixto2' or panelObjeto.tipoSistema == 'mixto3':
                datosEquipoACS = datos[8]
                panelObjeto.acumulacionCheck.SetValue(datosEquipoACS[0])
                if datosEquipoACS[0] == True:
                    panelObjeto.volumen.SetValue(datosEquipoACS[1])
                    panelObjeto.temperaturaAlta.SetValue(datosEquipoACS[2])
                    panelObjeto.temperaturaBaja.SetValue(datosEquipoACS[3])
                    panelObjeto.valorUAChoice.SetStringSelection(datosEquipoACS[5])
                    panelObjeto.UAvalor.SetValue(datosEquipoACS[4])
                    if 'Estimado' in panelObjeto.valorUAChoice.GetStringSelection():
                        panelObjeto.espesorAislamiento.SetValue(datosEquipoACS[6])
                        panelObjeto.aislamientoAcumulacionChoice.SetStringSelection(datosEquipoACS[7])
                        if len(datosEquipoACS) < 8:
                            panelObjeto.multiplicador.SetValue('1')
                        else:
                            panelObjeto.multiplicador.SetValue(datosEquipoACS[8])
                    elif 'Por defecto' in panelObjeto.valorUAChoice.GetStringSelection():
                        if len(datosEquipoACS) < 6:
                            panelObjeto.multiplicador.SetValue('1')
                        else:
                            panelObjeto.multiplicador.SetValue(datosEquipoACS[6])
            panelObjeto.subgrupoChoice.SetStringSelection(datos[-1])
            if panelObjeto.tipoSistema in ('ACS', 'calefaccion', 'refrigeracion'):
                panelObjeto.OnCoberturaPorcentaje(None)
            elif panelObjeto.tipoSistema in ('climatizacion', 'mixto2'):
                panelObjeto.OnCoberturaPorcentaje(None)
                panelObjeto.OnCoberturaPorcentaje2(None)
            else:
                panelObjeto.OnCoberturaPorcentaje(None)
                panelObjeto.OnCoberturaPorcentaje2(None)
                panelObjeto.OnCoberturaPorcentaje3(None)
            try:
                panelObjeto.OnrendimientoChoice(None)
            except (AttributeError, NameError):
                pass

            if panelObjeto.tipoSistema == 'ACS' or panelObjeto.tipoSistema == 'mixto2' or panelObjeto.tipoSistema == 'mixto3':
                panelObjeto.OnAcumulacionCheck(None)
            try:
                panelObjeto.OnVariosGeneradoresCheck(None)
            except (AttributeError, NameError):
                pass

        return