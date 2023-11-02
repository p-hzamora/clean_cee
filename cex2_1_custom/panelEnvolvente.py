# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: panelEnvolvente.pyc
# Compiled at: 2015-02-19 13:18:34
"""
Modulo: panelEnvolvente.py

"""
import wx, directorios
Directorio = directorios.BuscaDirectorios().Directorio
import Envolvente.panelDefinirEnvolvente as panelDefinirEnvolvente
from Envolvente.panelBotones import panelBotones
import Envolvente.panelFachadaConAire as panelFachadaConAire, Envolvente.panelFachadaConTerreno as panelFachadaConTerreno, Envolvente.panelFachadaConEdificio as panelFachadaConEdificio, Envolvente.panelCubiertaConTerreno as panelCubiertaConTerreno, Envolvente.panelCubiertaConAire as panelCubiertaConAire, Envolvente.panelVistaClasicaEnvolvente as panelVistaClasicaEnvolvente, Envolvente.panelSueloConTerreno as panelSueloConTerreno, Envolvente.panelSueloConAire as panelSueloConAire, Envolvente.panelHuecos as panelHuecos, Envolvente.panelPuentesTermicos as panelPuentesTermicos, Envolvente.panelParticionVertical as panelParticionVertical, Envolvente.panelParticionHorizontalInferior as panelParticionHorizontalInferior, Envolvente.panelParticionHorizontalSuperior as panelParticionHorizontalSuperior, ventanaSubgrupo, tips, Envolvente.panelEnvolventeRecuadro as panelEnvolventeRecuadro, nuevoUndo, logging
wxID_PANEL1, wxID_PANEL1PANEL2, wxID_PANEL1TREECTRL1, wxID_PANEL1PANELBOTONES, wxID_PANEL1NUEVOSUB, wxID_PANEL1NUEVOELE = [ wx.NewId() for _init_ctrls in range(6) ]

class panelEnvolvente(wx.Panel, nuevoUndo.VistaUndo):
    """
    Clase: panelEnvolvente del modulo panelEnvolvente.py

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
        self.arbolCerramientos = wx.TreeCtrl(id=wxID_PANEL1TREECTRL1, name='treeCtrl1', parent=self, pos=wx.Point(0, 8), size=wx.Size(216, 584), style=wx.TR_HAS_BUTTONS)
        self.arbolCerramientos.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnArbolCerramientos, id=wxID_PANEL1TREECTRL1)
        self.arbolCerramientos.Bind(wx.EVT_TREE_SEL_CHANGING, self.manejadorArbol, id=wxID_PANEL1TREECTRL1)
        self.arbolCerramientos.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.OnArbolItemRightClick, id=wxID_PANEL1TREECTRL1)
        self.nuevoSubgrupo = wx.Button(id=wxID_PANEL1NUEVOSUB, label=_('Zonas'), name='nuevoSubgrupo', parent=self, pos=wx.Point(0, 591), size=wx.Size(50, 20), style=0)
        self.nuevoSubgrupo.Bind(wx.EVT_BUTTON, self.OnNuevoSubgrupo, id=wxID_PANEL1NUEVOSUB)
        self.nuevoSubgrupo.Show(True)
        self.panelElegirObjeto = panelDefinirEnvolvente.definirEnvolvente(parent=self, id=-1, pos=wx.Point(230, 8), size=wx.Size(770, 206), style=wx.TAB_TRAVERSAL, name='')
        self.panelRecuadro = panelEnvolventeRecuadro.panelRecuadro(id=-1, name='panelRecuadro', parent=self, pos=wx.Point(230, 214), size=wx.Size(770, 36), style=0)
        self.panel2 = panelFachadaConAire.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(770, 350), style=wx.TAB_TRAVERSAL, name='')
        self.panelBotones = panelBotones(id=-1, name='panelBotones', parent=self, pos=wx.Point(230, 600), size=wx.Size(770, 100), style=wx.TAB_TRAVERSAL)
        self.vistaClasica = panelVistaClasicaEnvolvente.Panel1(parent=self, id=-1, pos=wx.Point(230, 8), size=wx.Size(770, 580), style=wx.TAB_TRAVERSAL, name='')
        self.vistaClasica.Show(False)

    def init_vectors(self):
        """
        Metodo: init_vectors

        """
        self.cerramientos = []
        self.ventanas = []
        self.puentesTermicos = []

    def OnArbolItemRightClick(self, event):
        """
        Metodo: OnArbolItemRightClick

        ARGUMENTOS:
                event:
        """
        elemento = self.arbolCerramientos.GetItemText(event.GetItem())
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

        dlg = ventanaSubgrupo.create(self, -1, wx.Point(200, 200), wx.Size(448, 240), wx.DEFAULT_DIALOG_STYLE, 'ventanaZonas', self, self.parent.parent.panelInstalaciones, 'añadir', None)
        dlg.ShowModal()
        return

    def OnArbolCerramientos(self, event):
        """
        Metodo: OnArbolCerramientos

        ARGUMENTOS:
                event:
        """
        if self.vistaNormal == True:
            nombre = self.arbolCerramientos.GetItemText(self.arbolCerramientos.GetSelection())
            for i in self.cerramientos:
                if nombre == i[0]:
                    if i[1] == 'Fachada':
                        if i[len(i) - 1] == 'aire':
                            self.panelRecuadro.titulo.SetLabel(_('Muro de fachada'))
                            self.panel2.Destroy()
                            self.panel2 = panelFachadaConAire.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                            tips.tipsOnFachadaConAire(self.parent.parent)
                            self.panel2.cargarDatos(i)
                            self.panel2.SetSize(wx.Size(770, 350))
                            imagen = wx.Image(Directorio + '/Imagenes/muroFachada.jpg', wx.BITMAP_TYPE_JPEG)
                            self.panelElegirObjeto.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
                        if i[len(i) - 1] == 'terreno':
                            self.panelRecuadro.titulo.SetLabel(_('Muro en contacto con el terreno'))
                            self.panel2.Destroy()
                            self.panel2 = panelFachadaConTerreno.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                            tips.tipsOnFachadaConTerreno(self.parent.parent)
                            self.panel2.cargarDatos(i)
                            self.panel2.SetSize(wx.Size(770, 350))
                            imagen = wx.Image(Directorio + '/Imagenes/muroTerreno.jpg', wx.BITMAP_TYPE_JPEG)
                            self.panelElegirObjeto.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
                        if i[len(i) - 1] == 'edificio':
                            self.panelRecuadro.titulo.SetLabel(_('Medianería'))
                            self.panel2.Destroy()
                            self.panel2 = panelFachadaConEdificio.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                            tips.tipsOnFachadaConEdificio(self.parent.parent)
                            self.panel2.cargarDatos(i)
                            self.panel2.SetSize(wx.Size(770, 350))
                            imagen = wx.Image(Directorio + '/Imagenes/Medianeria.jpg', wx.BITMAP_TYPE_JPEG)
                            self.panelElegirObjeto.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
                        self.panelElegirObjeto.puentesTermicosDefecto.Show(False)
                        self.panelElegirObjeto.puentesTermicosUsuario.Show(False)
                    elif i[1] == 'Cubierta':
                        if i[len(i) - 1] == 'aire':
                            self.panelRecuadro.titulo.SetLabel(_('Cubierta en contacto con el aire'))
                            self.panel2.Destroy()
                            self.panel2 = panelCubiertaConAire.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                            tips.tipsOndefinirCubiertaConAire(self.parent.parent)
                            self.panel2.cargarDatos(i)
                            self.panel2.SetSize(wx.Size(770, 350))
                            imagen = wx.Image(Directorio + '/Imagenes/cubiertaAire.jpg', wx.BITMAP_TYPE_JPEG)
                            self.panelElegirObjeto.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
                        if i[len(i) - 1] == 'terreno':
                            self.panelRecuadro.titulo.SetLabel(_('Cubierta enterrada'))
                            self.panel2.Destroy()
                            self.panel2 = panelCubiertaConTerreno.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                            tips.tipsOndefinirCubiertaTerreno(self.parent.parent)
                            self.panel2.cargarDatos(i)
                            self.panel2.SetSize(wx.Size(770, 350))
                            imagen = wx.Image(Directorio + '/Imagenes/cubiertaTerreno.jpg', wx.BITMAP_TYPE_JPEG)
                            self.panelElegirObjeto.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
                        self.panelElegirObjeto.puentesTermicosDefecto.Show(False)
                        self.panelElegirObjeto.puentesTermicosUsuario.Show(False)
                    elif i[1] == 'Suelo':
                        if i[len(i) - 1] == 'aire':
                            self.panelRecuadro.titulo.SetLabel(_('Suelo en contacto con el aire exterior'))
                            self.panel2.Destroy()
                            self.panel2 = panelSueloConAire.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                            tips.tipsOnSueloConAire(self.parent.parent)
                            self.panel2.cargarDatos(i)
                            self.panel2.SetSize(wx.Size(770, 350))
                            imagen = wx.Image(Directorio + '/Imagenes/sueloAire.jpg', wx.BITMAP_TYPE_JPEG)
                            self.panelElegirObjeto.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
                        if i[len(i) - 1] == 'terreno':
                            self.panelRecuadro.titulo.SetLabel(_('Suelo en contacto con el terreno'))
                            self.panel2.Destroy()
                            self.panel2 = panelSueloConTerreno.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                            tips.tipsOndefinirSueloTerreno(self.parent.parent)
                            self.panel2.cargarDatos(i)
                            self.panel2.SetSize(wx.Size(770, 350))
                            imagen = wx.Image(Directorio + '/Imagenes/sueloTerreno.jpg', wx.BITMAP_TYPE_JPEG)
                            self.panelElegirObjeto.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
                        self.panelElegirObjeto.puentesTermicosDefecto.Show(False)
                        self.panelElegirObjeto.puentesTermicosUsuario.Show(False)
                    elif i[1] == 'Partición Interior':
                        if i[len(i) - 1] == 'vertical':
                            self.panelRecuadro.titulo.SetLabel(_('Partición interior vertical'))
                            self.panel2.Destroy()
                            self.panel2 = panelParticionVertical.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                            tips.tipsOnVertical(self.parent.parent)
                            self.panel2.cargarDatos(i)
                            self.panel2.SetSize(wx.Size(770, 350))
                            imagen = wx.Image(Directorio + '/Imagenes/PI_Vertical.jpg', wx.BITMAP_TYPE_JPEG)
                            self.panelElegirObjeto.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
                        if i[len(i) - 1] == 'horizontal superior':
                            self.panelRecuadro.titulo.SetLabel(_('Partición interior horizontal en contacto con espacio NH superior'))
                            self.panel2.Destroy()
                            self.panel2 = panelParticionHorizontalSuperior.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                            tips.tipsOnHorizontalSuperior(self.parent.parent)
                            self.panel2.cargarDatos(i)
                            self.panel2.SetSize(wx.Size(770, 350))
                            imagen = wx.Image(Directorio + '/Imagenes/PI_Horizontal_Superior.jpg', wx.BITMAP_TYPE_JPEG)
                            self.panelElegirObjeto.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
                        if i[len(i) - 1] == 'horizontal inferior':
                            self.panelRecuadro.titulo.SetLabel(_('Partición interior horizontal en contacto con espacio NH inferior'))
                            self.panel2.Destroy()
                            self.panel2 = panelParticionHorizontalInferior.Panel1(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                            tips.tipsOnHorizontalInferior(self.parent.parent)
                            self.panel2.cargarDatos(i)
                            self.panel2.SetSize(wx.Size(770, 350))
                            imagen = wx.Image(Directorio + '/Imagenes/PI_Horizontal_Inferior.jpg', wx.BITMAP_TYPE_JPEG)
                            self.panelElegirObjeto.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
                        self.panelElegirObjeto.puentesTermicosDefecto.Show(False)
                        self.panelElegirObjeto.puentesTermicosUsuario.Show(False)
                    break

            for j in self.ventanas:
                if nombre == j.descripcion:
                    if j.tipo == 'Hueco' or j.tipo == 'Lucernario':
                        self.panelRecuadro.titulo.SetLabel(_('Hueco/Lucernario'))
                        self.panel2.Destroy()
                        self.panel2 = panelHuecos.panelHuecos(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                        tips.tipsOndefinirHueco(self.parent.parent)
                        self.panel2.cargarDatos(j)
                        self.panel2.SetSize(wx.Size(770, 350))
                        self.panelElegirObjeto.puentesTermicosDefecto.Show(False)
                        self.panelElegirObjeto.puentesTermicosUsuario.Show(False)
                        imagen = wx.Image(Directorio + '/Imagenes/huecoLucernario.jpg', wx.BITMAP_TYPE_JPEG)
                        self.panelElegirObjeto.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
                        break

            for i in self.puentesTermicos:
                if nombre == i[0]:
                    self.panelRecuadro.titulo.SetLabel(_('Puente térmico'))
                    self.panel2.Destroy()
                    self.panel2 = panelPuentesTermicos.panelPuentesTermicos(parent=self, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
                    tips.tipsOnpuentesTermicosBoton(self.parent.parent)
                    self.panel2.cargarDatos(i)
                    self.panel2.SetSize(wx.Size(770, 350))
                    self.panelElegirObjeto.puentesTermicosDefecto.Show(True)
                    self.panelElegirObjeto.puentesTermicosUsuario.Show(False)
                    imagen = wx.Image(Directorio + '/Imagenes/puenteTermico.jpg', wx.BITMAP_TYPE_JPEG)
                    self.panelElegirObjeto.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
                    break

        else:
            nombre = self.arbolCerramientos.GetItemText(self.arbolCerramientos.GetSelection())
            for i in range(len(self.cerramientos)):
                if nombre == self.cerramientos[i][0]:
                    self.vistaClasica.cerramiestosRadio.SetValue(True)
                    self.vistaClasica.OnCerramiestosRadioRadiobutton(None)
                    self.vistaClasica.listaCerramientos.SelectRow(i)
                    return

            for i in range(len(self.ventanas)):
                if nombre == self.ventanas[i].descripcion:
                    self.vistaClasica.huecosRadio.SetValue(True)
                    self.vistaClasica.OnHuecosRadioRadiobutton(None)
                    self.vistaClasica.listaHuecos.SelectRow(i)
                    return

            for i in range(len(self.puentesTermicos)):
                if nombre == self.puentesTermicos[i][0]:
                    self.vistaClasica.pTermicosRadio.SetValue(True)
                    self.vistaClasica.OnPTermicosRadioRadiobutton(None)
                    self.vistaClasica.listaPuentesTermicos.SelectRow(i)
                    return

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
                if i == arbol.GetItemText(j):
                    arbol.Expand(j)
                    break

    def cargarArbol(self, arbol):
        """
        Metodo: cargarArbol

        ARGUMENTOS:
                arbol): #funcion para cargar el arb:
        """
        elementosExpandidos = self.expandidosEnArbol(self.arbolCerramientos)
        arbol.DeleteAllItems()
        self.elementosArbol = []
        root = arbol.AddRoot(_('Edificio Objeto'))
        arbol.SetItemTextColour(root, 'black')
        arbol.SetItemBold(root)
        arbol.SetItemImage(root, 7, wx.TreeItemIcon_Normal)
        try:
            self.parent.instalaciones.recargaArbol(self.parent.instalaciones.arbolInstalaciones)
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
                    nuevo = arbol.AppendItem(resultado[1], datos[i].nombre)
                    self.elementosArbol.append(nuevo)
                    arbol.SetItemTextColour(nuevo, 'grey')
                    arbol.SetItemBold(nuevo)
                    arbol.SetItemImage(nuevo, 6, wx.TreeItemIcon_Normal)
                    metidos.append([datos[i].nombre, nuevo])
                    datos.pop(i)
                    break

        for i in self.cerramientos:
            resultado = self.raizEnArbol(metidos, i[len(i) - 2])
            if resultado[0] == True:
                nuevo = arbol.AppendItem(resultado[1], i[0])
                self.elementosArbol.append(nuevo)
                metidos.append([i[0], nuevo])
                arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
                arbol.SetItemBold(nuevo)
                if i[1] == 'Cubierta':
                    arbol.SetItemImage(nuevo, 5, wx.TreeItemIcon_Normal)
                elif i[len(i) - 1] == 'aire':
                    arbol.SetItemImage(nuevo, 2, wx.TreeItemIcon_Normal)
                if i[len(i) - 1] == 'terreno':
                    arbol.SetItemImage(nuevo, 1, wx.TreeItemIcon_Normal)
                else:
                    if i[len(i) - 1] == 'edificio':
                        arbol.SetItemImage(nuevo, 0, wx.TreeItemIcon_Normal)
                    else:
                        arbol.SetItemImage(nuevo, 0, wx.TreeItemIcon_Normal)

        for j in self.ventanas:
            resultado = self.raizEnArbol(metidos, j.cerramientoAsociado)
            nuevo = arbol.AppendItem(resultado[1], j.descripcion)
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(63, 197, 254))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 3, wx.TreeItemIcon_Normal)

        for j in self.puentesTermicos:
            resultado = self.raizEnArbol(metidos, j[7])
            nuevo = arbol.AppendItem(resultado[1], j[0])
            self.elementosArbol.append(nuevo)
            if j[5] == 'defecto_fi':
                arbol.SetItemTextColour(nuevo, wx.Colour(243, 169, 71))
            else:
                arbol.SetItemTextColour(nuevo, wx.Colour(169, 101, 11))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 4, wx.TreeItemIcon_Normal)

        arbol.Expand(root)
        self.expandirAnteriores(elementosExpandidos, self.arbolCerramientos)

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
        arbol.SetItemImage(root, 7, wx.TreeItemIcon_Normal)
        datos = []
        for i in self.parent.subgrupos:
            datos.append(i)

        metidos = []
        metidos.append(['Edificio Objeto', root])
        while datos != []:
            for i in range(len(datos)):
                resultado = self.raizEnArbol(metidos, datos[i].raiz)
                if resultado[0] == True:
                    nuevo = arbol.AppendItem(resultado[1], datos[i].nombre)
                    self.elementosArbol.append(nuevo)
                    arbol.SetItemTextColour(nuevo, 'grey')
                    arbol.SetItemBold(nuevo)
                    arbol.SetItemImage(nuevo, 6, wx.TreeItemIcon_Normal)
                    metidos.append([datos[i].nombre, nuevo])
                    datos.pop(i)
                    break

        for i in self.cerramientos:
            resultado = self.raizEnArbol(metidos, i[len(i) - 2])
            if resultado[0] == True:
                nuevo = arbol.AppendItem(resultado[1], i[0])
                self.elementosArbol.append(nuevo)
                metidos.append([i[0], nuevo])
                arbol.SetItemTextColour(nuevo, wx.Colour(0, 64, 128))
                arbol.SetItemBold(nuevo)
                if i[1] == 'Cubierta':
                    arbol.SetItemImage(nuevo, 5, wx.TreeItemIcon_Normal)
                elif i[len(i) - 1] == 'aire':
                    arbol.SetItemImage(nuevo, 2, wx.TreeItemIcon_Normal)
                if i[len(i) - 1] == 'terreno':
                    arbol.SetItemImage(nuevo, 1, wx.TreeItemIcon_Normal)
                else:
                    if i[len(i) - 1] == 'edificio':
                        arbol.SetItemImage(nuevo, 0, wx.TreeItemIcon_Normal)
                    else:
                        arbol.SetItemImage(nuevo, 0, wx.TreeItemIcon_Normal)

        for j in self.ventanas:
            resultado = self.raizEnArbol(metidos, j.cerramientoAsociado)
            nuevo = arbol.AppendItem(resultado[1], j.descripcion)
            self.elementosArbol.append(nuevo)
            arbol.SetItemTextColour(nuevo, wx.Colour(63, 197, 254))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 3, wx.TreeItemIcon_Normal)

        for j in self.puentesTermicos:
            resultado = self.raizEnArbol(metidos, j[7])
            nuevo = arbol.AppendItem(resultado[1], j[0])
            self.elementosArbol.append(nuevo)
            if j[5] == 'defecto_fi':
                arbol.SetItemTextColour(nuevo, wx.Colour(243, 169, 71))
            else:
                arbol.SetItemTextColour(nuevo, wx.Colour(169, 101, 11))
            arbol.SetItemBold(nuevo)
            arbol.SetItemImage(nuevo, 4, wx.TreeItemIcon_Normal)

        arbol.Expand(root)
        try:
            self.panel2.raizchoice.SetItems(self.panel2.cargarRaices())
        except:
            logging.info('Excepcion en: %s' % __name__)

    def iniciaIconosArbol(self):
        """
        Metodo: iniciaIconosArbol

        """
        self.iconosArbol = wx.ImageList(14, 14, True, 1)
        cerramientoEdificio = wx.Bitmap(Directorio + '/Imagenes/cerramientoEdificio.ico')
        cerramientoTerreno = wx.Bitmap(Directorio + '/Imagenes/cerramientoTerreno.ico')
        cerramientoAire = wx.Bitmap(Directorio + '/Imagenes/cerramientoAire.ico')
        hueco = wx.Bitmap(Directorio + '/Imagenes/hueco.ico')
        pt = wx.Bitmap(Directorio + '/Imagenes/pt.ico')
        cubierta = wx.Bitmap(Directorio + '/Imagenes/cubierta.ico')
        zona = wx.Bitmap(Directorio + '/Imagenes/zona.ico')
        edificioObjeto = wx.Bitmap(Directorio + '/Imagenes/edificioObjeto.ico')
        self.iconosArbol.Add(cerramientoEdificio)
        self.iconosArbol.Add(cerramientoTerreno)
        self.iconosArbol.Add(cerramientoAire)
        self.iconosArbol.Add(hueco)
        self.iconosArbol.Add(pt)
        self.iconosArbol.Add(cubierta)
        self.iconosArbol.Add(zona)
        self.iconosArbol.Add(edificioObjeto)
        self.arbolCerramientos.SetImageList(self.iconosArbol)

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
        self.nombre = _('Envolvente térmica')
        self.iniciaIconosArbol()
        self.elementosArbol = []
        self.cargarArbol(self.arbolCerramientos)
        self.vistaNormal = True

    def cogerDatos(self):
        """
        Metodo: cogerDatos

        """
        datos = []
        datos.append(self.cerramientos)
        datos.append(self.ventanas)
        datos.append(self.puentesTermicos)
        datos.append(self.parent.subgrupos)
        return datos

    def cargarDatos(self, datos):
        """
        Metodo: cargarDatos

        ARGUMENTOS:
                datos:
        """
        self.cerramientos = []
        for i in datos[0]:
            self.cerramientos.append(i)

        self.ventanas = []
        for i in datos[1]:
            self.ventanas.append(i)

        self.puentesTermicos = []
        for i in datos[2]:
            self.puentesTermicos.append(i)

        self.parent.subgrupos = []
        for i in datos[3]:
            self.parent.subgrupos.append(i)

        self.cargarArbol(self.arbolCerramientos)
        self.panelElegirObjeto.definirFachada.SetValue(True)
        self.panelElegirObjeto.contactoAire.SetValue(True)
        self.panelElegirObjeto.OndefinirFachada(None)
        return