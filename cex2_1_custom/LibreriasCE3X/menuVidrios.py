# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: LibreriasCE3X\menuVidrios.pyc
# Compiled at: 2015-02-19 13:18:34
"""
Modulo: menuVidrios.py

"""
import wx, Envolvente.dialogoConfirma as dialogoConfirma, logging, ElementosConstructivos.Aviso_borrar_material as Aviso_borrar_material, ElementosConstructivos.cargaBD as cargaBD

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return Frame1(parent)


wxID_FRAME1, wxID_FRAME1ABSORTIVIDAD, wxID_FRAME1ABSORTIVIDADTEXT, wxID_FRAME1ARBOLMARCOS, wxID_FRAME1ARBOLVIDRIOS, wxID_FRAME1BORRARMARCO, wxID_FRAME1BORRARVIDRIO, wxID_FRAME1CARGARMARCO, wxID_FRAME1CARGARVIDRIO, wxID_FRAME1GRUPOMARCO, wxID_FRAME1GRUPOMARCOTEXT, wxID_FRAME1GRUPOVIDRIO, wxID_FRAME1GRUPOVIDRIOTEXT, wxID_FRAME1GUARDARMARCO, wxID_FRAME1GUARDARVIDRIO, wxID_FRAME1GVIDRIO, wxID_FRAME1GVIDRIOTEXT, wxID_FRAME1MARCOSTITULOTEXT, wxID_FRAME1MODIFICARMARCO, wxID_FRAME1MODIFICARVIDRIO, wxID_FRAME1NOMBREMARCO, wxID_FRAME1NOMBREMARCOTEXT, wxID_FRAME1NOMBREVIDRIO, wxID_FRAME1NOMBREVIDRIOTEXT, wxID_FRAME1SELECCIONARGRUPOMARCOCHOICE, wxID_FRAME1SELECCIONARGRUPOMARCOTEXT, wxID_FRAME1SELECCIONARGRUPOVIDRIOCHOICE, wxID_FRAME1SELECCIONARGRUPOVIDRIOTEXT, wxID_FRAME1STATICLINE1, wxID_FRAME1UMARCO, wxID_FRAME1UMARCOTEXT, wxID_FRAME1UMARCOUNIDADESTEXT, wxID_FRAME1UVIDRIO, wxID_FRAME1UVIDRIOTEXT, wxID_FRAME1UVIDRIOUNIDADESTEXT, wxID_FRAME1VIDRIOSTITULOTEXT, wxID_FRAME1TREECTRL1, wxID_FRAME1TREECTRL2 = [ wx.NewId() for _init_ctrls in range(38) ]

class Frame1(wx.Dialog):
    """
    Clase: Frame1 del modulo menuVidrios.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
        """
        wx.Dialog.__init__(self, id=wxID_FRAME1, name='', parent=prnt, pos=wx.Point(0, 0), size=wx.Size(778, 521), style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN | wx.TAB_TRAVERSAL, title=_('Vidrios'))
        self.SetClientSize(wx.Size(770, 487))
        self.SetBackgroundColour('white')
        self.arbolVidrios = wx.TreeCtrl(id=wxID_FRAME1TREECTRL1, name='arbolVidrios', parent=self, pos=wx.Point(8, 15), size=wx.Size(200, 450), style=wx.TR_HAS_BUTTONS)
        self.arbolVidrios.Bind(wx.EVT_TREE_SEL_CHANGED, self.onArbolVidrios, id=wxID_FRAME1TREECTRL1)
        self.vidriosTituloText = wx.StaticText(id=wxID_FRAME1VIDRIOSTITULOTEXT, label=_('Librería de vidrios'), name='vidriosTituloText', parent=self, pos=wx.Point(220, 22), size=wx.Size(61, 18), style=0)
        self.vidriosTituloText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.vidriosTituloText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.nombreVidrioText = wx.StaticText(id=wxID_FRAME1NOMBREVIDRIOTEXT, label=_('Nombre'), name='nombreVidrioText', parent=self, pos=wx.Point(235, 86), size=wx.Size(66, 13), style=0)
        self.grupoVidrioText = wx.StaticText(id=wxID_FRAME1GRUPOVIDRIOTEXT, label=_('Grupo'), name='grupoVidrioText', parent=self, pos=wx.Point(235, 116), size=wx.Size(58, 13), style=0)
        self.seleccionarGrupoVidrioText = wx.StaticText(id=wxID_FRAME1SELECCIONARGRUPOVIDRIOTEXT, label=_('Seleccionar grupo existente'), name='seleccionarGrupoVidrioText', parent=self, pos=wx.Point(235, 146), size=wx.Size(134, 13), style=0)
        self.nombreVidrio = wx.TextCtrl(id=wxID_FRAME1NOMBREVIDRIO, name='nombreVidrio', parent=self, pos=wx.Point(304, 84), size=wx.Size(440, 21), style=0, value='')
        self.grupoVidrio = wx.TextCtrl(id=wxID_FRAME1GRUPOVIDRIO, name='grupoVidrio', parent=self, pos=wx.Point(304, 114), size=wx.Size(440, 21), style=0, value='')
        grupos1 = cargaBD.cargarGrupoVidrioCal()
        grupos2 = cargaBD.cargarGrupoVidrioUser()
        for i in grupos2:
            grupos1.append(i)

        self.seleccionarGrupoVidrioChoice = wx.Choice(choices=grupos1, id=wxID_FRAME1SELECCIONARGRUPOVIDRIOCHOICE, name='seleccionarGrupoVidrioChoice', parent=self, pos=wx.Point(404, 144), size=wx.Size(340, 21), style=0)
        self.seleccionarGrupoVidrioChoice.Bind(wx.EVT_CHOICE, self.onSeleccionarGrupoVidrioChoice, id=wxID_FRAME1SELECCIONARGRUPOVIDRIOCHOICE)
        self.PropiedadesLinea = wx.StaticBox(id=-1, label=_('Propiedades'), name='PropiedadesLinea', parent=self, pos=wx.Point(220, 176), size=wx.Size(524, 176), style=0)
        self.PropiedadesLinea.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.PropiedadesLinea.SetForegroundColour(wx.Colour(0, 64, 128))
        self.uVidrioText = wx.StaticText(id=wxID_FRAME1UVIDRIOTEXT, label=_('U'), name='uVidrioText', parent=self, pos=wx.Point(235, 206), size=wx.Size(36, 13), style=0)
        self.gVidrioText = wx.StaticText(id=wxID_FRAME1GVIDRIOTEXT, label=_('Factor solar'), name='gVidrioText', parent=self, pos=wx.Point(235, 236), size=wx.Size(60, 13), style=0)
        self.uVidrio = wx.TextCtrl(id=wxID_FRAME1UVIDRIO, name='uVidrio', parent=self, pos=wx.Point(304, 204), size=wx.Size(56, 21), style=0, value='')
        self.gVidrio = wx.TextCtrl(id=wxID_FRAME1GVIDRIO, name='gVidrio', parent=self, pos=wx.Point(304, 234), size=wx.Size(56, 21), style=0, value='')
        self.uVidrioUnidadesText = wx.StaticText(id=wxID_FRAME1UVIDRIOUNIDADESTEXT, label=_('W/m2K'), name='uVidrioUnidadesText', parent=self, pos=wx.Point(365, 206), size=wx.Size(34, 13), style=0)
        self.cargarVidrio = wx.Button(id=wxID_FRAME1CARGARVIDRIO, label=_('Cargar al proyecto'), name='cargarVidrio', parent=self, pos=wx.Point(220, 417), size=wx.Size(165, 21), style=0)
        self.cargarVidrio.Bind(wx.EVT_BUTTON, self.OnCargarVidrio, id=wxID_FRAME1CARGARVIDRIO)
        self.guardarVidrio = wx.Button(id=wxID_FRAME1GUARDARVIDRIO, label=_('Guardar'), name='guardarVidrio', parent=self, pos=wx.Point(220, 443), size=wx.Size(75, 23), style=0)
        self.guardarVidrio.Bind(wx.EVT_BUTTON, self.OnGuardarVidrio, id=wxID_FRAME1GUARDARVIDRIO)
        self.guardarVidrio.SetForegroundColour(wx.Colour(0, 64, 128))
        self.guardarVidrio.SetBackgroundColour('white')
        self.modificarVidrio = wx.Button(id=wxID_FRAME1MODIFICARVIDRIO, label=_('Modificar'), name='modificarVidrio', parent=self, pos=wx.Point(310, 443), size=wx.Size(75, 23), style=0)
        self.modificarVidrio.Bind(wx.EVT_BUTTON, self.OnModificarVidrio, id=wxID_FRAME1MODIFICARVIDRIO)
        self.modificarVidrio.SetForegroundColour(wx.Colour(0, 64, 128))
        self.modificarVidrio.SetBackgroundColour('white')
        self.borrarVidrio = wx.Button(id=wxID_FRAME1BORRARVIDRIO, label=_('Borrar'), name='borrarVidrio', parent=self, pos=wx.Point(445, 443), size=wx.Size(75, 23), style=0)
        self.borrarVidrio.Bind(wx.EVT_BUTTON, self.OnBorrarVidrio, id=wxID_FRAME1BORRARVIDRIO)
        self.borrarVidrio.SetForegroundColour(wx.Colour(0, 64, 128))
        self.borrarVidrio.SetBackgroundColour('white')

    def __init__(self, parent):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
        """
        self.elementosArbol = []
        self._init_ctrls(parent)
        self.cargarArbolVidrios(self.arbolVidrios)
        self.parent = parent
        self.dev = False

    def OnCargarVidrio(self, event):
        """
        Metodo: OnCargarVidrio

        ARGUMENTOS:
                event:
        """
        if self.arbolVidrios.GetChildrenCount(self.arbolVidrios.GetSelection()) == 0:
            vidrio = []
            prob = self.arbolVidrios.GetItemText(self.arbolVidrios.GetSelection())
            vidrio = cargaBD.cargarVidrio(prob)
            self.dev = vidrio
            self.Close()

    def onArbolVidrios(self, event):
        """
        Metodo: onArbolVidrios

        ARGUMENTOS:
                event:
        """
        if self.arbolVidrios.GetChildrenCount(self.arbolVidrios.GetSelection()) == 0:
            vidrio = []
            prob = self.arbolVidrios.GetItemText(self.arbolVidrios.GetSelection())
            vidrio = cargaBD.cargarVidrio(prob)
            self.nombreVidrio.SetValue(str(vidrio[0]))
            self.grupoVidrio.SetValue(str(vidrio[1]))
            self.uVidrio.SetValue(str(vidrio[3]))
            self.gVidrio.SetValue(str(vidrio[2]))
        else:
            self.nombreVidrio.SetValue('')
            self.grupoVidrio.SetValue('')
            self.uVidrio.SetValue('')
            self.gVidrio.SetValue('')
            self.seleccionarGrupoVidrioChoice.SetSelection(-1)

    def OnGuardarVidrio(self, event):
        """
        Metodo: OnGuardarVidrio

        ARGUMENTOS:
                event:
        """
        if cargaBD.compruebaVidrio(self.nombreVidrio.GetValue()) == False:
            nombreVidrio = self.nombreVidrio.GetValue()
            nombreVidrio = str(nombreVidrio.encode('cp1252'))
            nombre_grupo = self.grupoVidrio.GetValue()
            nombre_grupo = str(nombre_grupo.encode('cp1252'))
            uVidrio = self.uVidrio.GetValue()
            gVidrio = self.gVidrio.GetValue()
            if ',' in uVidrio:
                uVidrio = uVidrio.replace(',', '.')
            if ',' in gVidrio:
                gVidrio = gVidrio.replace(',', '.')
            try:
                float(uVidrio)
                if float(uVidrio) <= 0:
                    uVidrio = ''
            except:
                logging.info('Excepcion en: %s' % __name__)
                uVidrio = ''

            try:
                float(gVidrio)
                if float(gVidrio) <= 0 or float(gVidrio) > 1:
                    gVidrio = ''
            except:
                logging.info('Excepcion en: %s' % __name__)
                gVidrio = ''

            lista_errores = ''
            if nombreVidrio == '':
                lista_errores += 'nombre'
            if nombre_grupo == '':
                if lista_errores != '':
                    lista_errores += ', '
                lista_errores += 'grupo'
            if uVidrio == '':
                if lista_errores != '':
                    lista_errores += ', '
                lista_errores += 'U'
            if gVidrio == '':
                if lista_errores != '':
                    lista_errores += ', '
                lista_errores += 'factor solar'
            if lista_errores != '':
                wx.MessageBox(_('Revise los siguientes campos:\n') + lista_errores, _('Aviso'))
                return
            nuevoVidrio = []
            nuevoVidrio.append(unicode(self.nombreVidrio.GetValue()))
            nuevoVidrio.append(unicode(self.grupoVidrio.GetValue()))
            nuevoVidrio.append(gVidrio)
            nuevoVidrio.append(uVidrio)
            nuevoVidrio.append('U')
            cargaBD.nuevoVidrio(nuevoVidrio)
            self.cargarArbolVidrios(self.arbolVidrios)
            self.seleccionarGrupoVidrioChoice.Clear()
            grupos1 = cargaBD.cargarGrupoVidrioCal()
            grupos2 = cargaBD.cargarGrupoVidrioUser()
            for i in grupos2:
                grupos1.append(i)

            self.seleccionarGrupoVidrioChoice.AppendItems(grupos1)
            self.nombreVidrio.SetValue('')
            self.grupoVidrio.SetValue('')
            self.uVidrio.SetValue('')
            self.gVidrio.SetValue('')
            self.seleccionarGrupoVidrioChoice.SetSelection(-1)
        else:
            wx.MessageBox(_('El nombre del vidrio ya existe, cámbielo para continuar'), _('Aviso'))

    def OnModificarVidrio(self, event):
        """
        Metodo: OnModificarVidrio

        ARGUMENTOS:
                event:
        """
        try:
            nobreViejo = self.arbolVidrios.GetItemText(self.arbolVidrios.GetSelection())
        except:
            wx.MessageBox(_('Debe seleccionar un elemento en el árbol'), _('Aviso'))
            return

        if self.arbolVidrios.GetChildrenCount(self.arbolVidrios.GetSelection()) > 0:
            if self.arbolVidrios.GetItemTextColour(self.arbolVidrios.GetSelection()) == 'Dark green':
                wx.MessageBox(_('No se puede modificar un grupo de vidrios por defecto (en verde)'), _('Aviso'))
                return
        elif self.arbolVidrios.GetItemTextColour(self.arbolVidrios.GetSelection()) == wx.Colour(100, 200, 0):
            wx.MessageBox(_('No se puede modificar un vidrio por defecto (en verde)'), _('Aviso'))
            return
        nombreVidrio = self.nombreVidrio.GetValue()
        nombreVidrio = str(nombreVidrio.encode('cp1252'))
        nombre_grupo = self.grupoVidrio.GetValue()
        nombre_grupo = str(nombre_grupo.encode('cp1252'))
        uVidrio = self.uVidrio.GetValue()
        gVidrio = self.gVidrio.GetValue()
        if nobreViejo != nombreVidrio:
            if cargaBD.compruebaVidrio(self.nombreVidrio.GetValue()) == True:
                wx.MessageBox(_('El nombre del vidrio ya existe, cámbielo para continuar'), _('Aviso'))
                return
        if ',' in uVidrio:
            uVidrio = uVidrio.replace(',', '.')
        if ',' in gVidrio:
            gVidrio = gVidrio.replace(',', '.')
        try:
            float(uVidrio)
            if float(uVidrio) <= 0:
                uVidrio = ''
        except:
            logging.info('Excepcion en: %s' % __name__)
            uVidrio = ''

        try:
            float(gVidrio)
            if float(gVidrio) <= 0 or float(gVidrio) > 1:
                gVidrio = ''
        except:
            logging.info('Excepcion en: %s' % __name__)
            gVidrio = ''

        lista_errores = ''
        if nombreVidrio == '':
            lista_errores += 'nombre'
        if nombre_grupo == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'grupo'
        if uVidrio == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'U'
        if gVidrio == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'factor solar'
        if lista_errores != '':
            wx.MessageBox(_('Revise los siguientes campos:\n') + lista_errores, _('Aviso'))
            return
        else:
            booleano = False
            for i in self.parent.panelEnvolvente.ventanas:
                try:
                    if i.vidrioSeleccionado == nobreViejo:
                        booleano = True
                        break
                except:
                    logging.info('Excepcion en: %s' % __name__)

            hola = Aviso_borrar_material.create(self, 2)
            hola.ShowModal()
            if hola.borrar == True:
                if booleano == True:
                    dlg = dialogoConfirma.Dialog2(self, _('El vidrio que está tratando de modificar ha sido asignado a huecos que componen la envolvente térmica del edificio y se verán afectados por esa modificación. ¿Desea continuar?'))
                    dlg.ShowModal()
                    if dlg.dev == False:
                        return
                    for i in self.parent.panelEnvolvente.ventanas:
                        try:
                            if i.vidrioSeleccionado == nobreViejo:
                                i.vidrioSeleccionado = nombreVidrio
                                i.UvidrioConocido = uVidrio
                                i.GvidrioConocido = gVidrio
                        except:
                            logging.info('Excepcion en: %s' % __name__)

                nuevoVidrio = []
                nuevoVidrio.append(unicode(self.nombreVidrio.GetValue()))
                nuevoVidrio.append(unicode(self.grupoVidrio.GetValue()))
                nuevoVidrio.append(gVidrio)
                nuevoVidrio.append(uVidrio)
                nuevoVidrio.append('U')
                cargaBD.modificaVidrio(nuevoVidrio, nobreViejo)
                self.cargarArbolVidrios(self.arbolVidrios)
                try:
                    self.parent.panelEnvolvente.OnArbolCerramientos(None)
                except:
                    logging.info('Excepcion en: %s' % __name__)

            return

    def OnBorrarVidrio(self, event):
        """
        Metodo: OnBorrarVidrio

        ARGUMENTOS:
                event:
        """
        try:
            self.arbolVidrios.GetItemText(self.arbolVidrios.GetSelection())
        except:
            wx.MessageBox(_('Debe seleccionar un elemento en el árbol'), _('Aviso'))
            return

        if self.arbolVidrios.GetChildrenCount(self.arbolVidrios.GetSelection()) > 0:
            if self.arbolVidrios.GetItemTextColour(self.arbolVidrios.GetSelection()) == 'Dark green':
                wx.MessageBox(_('No se puede eliminar un grupo de vidrios por defecto (en verde)'), _('Aviso'))
                return
            hola = Aviso_borrar_material.create(self, 1)
            hola.ShowModal()
            if hola.borrar == True:
                cargaBD.borraGrupoVidrioUser(self.arbolVidrios.GetItemText(self.arbolVidrios.GetSelection()))
                self.seleccionarGrupoVidrioChoice.Clear()
                grupos1 = cargaBD.cargarGrupoVidrioCal()
                grupos2 = cargaBD.cargarGrupoVidrioUser()
                for i in grupos2:
                    grupos1.append(i)

                self.seleccionarGrupoVidrioChoice.AppendItems(grupos1)
                self.cargarArbolVidrios(self.arbolVidrios)
        elif self.arbolVidrios.GetItemTextColour(self.arbolVidrios.GetSelection()) == wx.Colour(100, 200, 0):
            wx.MessageBox(_('No se puede eliminar un vidrio por defecto (en verde)'), _('Aviso'))
            return
        hola = Aviso_borrar_material.create(self, 0)
        hola.ShowModal()
        if hola.borrar == True:
            cargaBD.borraVidrioUser(self.arbolVidrios.GetItemText(self.arbolVidrios.GetSelection()))
            self.seleccionarGrupoVidrioChoice.Clear()
            grupos1 = cargaBD.cargarGrupoVidrioCal()
            grupos2 = cargaBD.cargarGrupoVidrioUser()
            for i in grupos2:
                grupos1.append(i)

            self.seleccionarGrupoVidrioChoice.AppendItems(grupos1)
            self.cargarArbolVidrios(self.arbolVidrios)
        self.cargarArbolVidrios(self.arbolVidrios)

    def onSeleccionarGrupoVidrioChoice(self, event):
        """
        Metodo: onSeleccionarGrupoVidrioChoice

        ARGUMENTOS:
                event:
        """
        self.grupoVidrio.SetValue(self.seleccionarGrupoVidrioChoice.GetStringSelection())

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

    def cargarArbolVidrios(self, arbol):
        """
        Metodo: cargarArbolVidrios

        ARGUMENTOS:
                arbol:
        """
        elementosExpandidos = self.expandidosEnArbol(arbol)
        arbol.DeleteAllItems()
        self.elementosArbol = []
        root = arbol.AddRoot('Vidrios')
        gruposCal = []
        gruposCal = cargaBD.cargarGrupoVidrioCal()
        mat = []
        for i in gruposCal:
            idTree = arbol.AppendItem(root, i)
            self.elementosArbol.append(idTree)
            arbol.SetItemTextColour(idTree, 'Dark green')
            mat = cargaBD.cargarVidriosCal(i)
            for j in mat:
                it = arbol.AppendItem(idTree, j)
                arbol.SetItemTextColour(it, wx.Colour(100, 200, 0))

            mat = cargaBD.cargarVidriosUser(i)
            for j in mat:
                it = arbol.AppendItem(idTree, j)
                arbol.SetItemTextColour(it, 'grey')

        gruposUser = []
        gruposUser = cargaBD.cargarGrupoVidrioUser()
        for i in gruposUser:
            idTree = arbol.AppendItem(root, i)
            self.elementosArbol.append(idTree)
            arbol.SetItemTextColour(idTree, 'Black')
            mat = cargaBD.cargarVidriosUser(i)
            for j in mat:
                it = arbol.AppendItem(idTree, j)
                arbol.SetItemTextColour(it, 'grey')

        arbol.Expand(root)
        self.expandirAnteriores(elementosExpandidos, arbol)