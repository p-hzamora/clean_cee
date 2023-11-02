# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: LibreriasCE3X\menuMarcos.pyc
# Compiled at: 2015-02-19 13:18:33
"""
Modulo: menuMarcos.py

"""
import wx, logging, ElementosConstructivos.Aviso_borrar_material as Aviso_borrar_material, ElementosConstructivos.cargaBD as cargaBD, Envolvente.dialogoConfirma as dialogoConfirma

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return Frame1(parent)


wxID_FRAME1, wxID_FRAME1ABSORTIVIDAD, wxID_FRAME1ABSORTIVIDADTEXT, wxID_FRAME1ARBOLMARCOS, wxID_FRAME1ARBOLVIDRIOS, wxID_FRAME1BORRARMARCO, wxID_FRAME1BORRARVIDRIO, wxID_FRAME1CARGARMARCO, wxID_FRAME1CARGARVIDRIO, wxID_FRAME1GRUPOMARCO, wxID_FRAME1GRUPOMARCOTEXT, wxID_FRAME1GRUPOVIDRIO, wxID_FRAME1GRUPOVIDRIOTEXT, wxID_FRAME1GUARDARMARCO, wxID_FRAME1GUARDARVIDRIO, wxID_FRAME1GVIDRIO, wxID_FRAME1GVIDRIOTEXT, wxID_FRAME1MARCOSTITULOTEXT, wxID_FRAME1MODIFICARARCO, wxID_FRAME1MODIFICARVIDRIO, wxID_FRAME1NOMBREMARCO, wxID_FRAME1NOMBREMARCOTEXT, wxID_FRAME1NOMBREVIDRIO, wxID_FRAME1NOMBREVIDRIOTEXT, wxID_FRAME1SELECCIONARGRUPOMARCOCHOICE, wxID_FRAME1SELECCIONARGRUPOMARCOTEXT, wxID_FRAME1SELECCIONARGRUPOVIDRIOCHOICE, wxID_FRAME1SELECCIONARGRUPOVIDRIOTEXT, wxID_FRAME1STATICLINE1, wxID_FRAME1UMARCO, wxID_FRAME1UMARCOTEXT, wxID_FRAME1UMARCOUNIDADESTEXT, wxID_FRAME1UVIDRIO, wxID_FRAME1UVIDRIOTEXT, wxID_FRAME1UVIDRIOUNIDADESTEXT, wxID_FRAME1VIDRIOSTITULOTEXT, wxID_FRAME1TREECTRL1, wxID_FRAME1TREECTRL2, wxID_FRAME1MODIFICARMARCO = [ wx.NewId() for _init_ctrls in range(39) ]

class Frame1(wx.Dialog):
    """
    Clase: Frame1 del modulo menuMarcos.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
        """
        wx.Dialog.__init__(self, id=wxID_FRAME1, name='', parent=prnt, pos=wx.Point(0, 0), size=wx.Size(778, 521), style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN | wx.TAB_TRAVERSAL, title=_('Marcos'))
        self.SetClientSize(wx.Size(770, 487))
        self.SetBackgroundColour('white')
        self.arbolMarcos = wx.TreeCtrl(id=wxID_FRAME1TREECTRL2, name='arbolMarcos', parent=self, pos=wx.Point(8, 15), size=wx.Size(200, 450), style=wx.TR_HAS_BUTTONS)
        self.arbolMarcos.Bind(wx.EVT_TREE_SEL_CHANGED, self.onArbolMarcos, id=wxID_FRAME1TREECTRL2)
        self.marcosTituloText = wx.StaticText(id=wxID_FRAME1MARCOSTITULOTEXT, label=_('Librería de marcos'), name='marcosTituloText', parent=self, pos=wx.Point(220, 22), size=wx.Size(61, 18), style=0)
        self.marcosTituloText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.marcosTituloText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.nombreMarcoText = wx.StaticText(id=wxID_FRAME1NOMBREMARCOTEXT, label=_('Nombre'), name='nombreMarcoText', parent=self, pos=wx.Point(235, 86), size=wx.Size(66, 13), style=0)
        self.grupoMarcoText = wx.StaticText(id=wxID_FRAME1GRUPOMARCOTEXT, label=_('Grupo'), name='grupoMarcoText', parent=self, pos=wx.Point(235, 116), size=wx.Size(58, 13), style=0)
        self.seleccionarGrupoMarcoText = wx.StaticText(id=wxID_FRAME1SELECCIONARGRUPOMARCOTEXT, label=_('Seleccionar Grupo Existente'), name='seleccionarGrupoMarcoText', parent=self, pos=wx.Point(235, 146), size=wx.Size(134, 13), style=0)
        self.nombreMarco = wx.TextCtrl(id=wxID_FRAME1NOMBREMARCO, name='nombreMarco', parent=self, pos=wx.Point(304, 84), size=wx.Size(440, 21), style=0, value='')
        self.grupoMarco = wx.TextCtrl(id=wxID_FRAME1GRUPOMARCO, name='grupoMarco', parent=self, pos=wx.Point(304, 114), size=wx.Size(440, 21), style=0, value='')
        grupos1 = cargaBD.cargarGrupoMarcoCal()
        grupos2 = cargaBD.cargarGrupoMarcoUser()
        for i in grupos2:
            grupos1.append(i)

        self.seleccionarGrupoMarcoChoice = wx.Choice(choices=grupos1, id=wxID_FRAME1SELECCIONARGRUPOMARCOCHOICE, name='seleccionarGrupoMarcoChoice', parent=self, pos=wx.Point(404, 144), size=wx.Size(340, 21), style=0)
        self.seleccionarGrupoMarcoChoice.Bind(wx.EVT_CHOICE, self.onSeleccionarGrupoMarcoChoice, id=wxID_FRAME1SELECCIONARGRUPOMARCOCHOICE)
        self.PropiedadesLinea = wx.StaticBox(id=-1, label=_('Propiedades'), name='PropiedadesLinea', parent=self, pos=wx.Point(220, 176), size=wx.Size(524, 176), style=0)
        self.PropiedadesLinea.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.PropiedadesLinea.SetForegroundColour(wx.Colour(0, 64, 128))
        self.uMarcoText = wx.StaticText(id=wxID_FRAME1UMARCOTEXT, label=_('U'), name='uMarcoText', parent=self, pos=wx.Point(235, 206), size=wx.Size(36, 13), style=0)
        self.uMarco = wx.TextCtrl(id=wxID_FRAME1UMARCO, name='uMarco', parent=self, pos=wx.Point(304, 204), size=wx.Size(56, 21), style=0, value='')
        self.uMarcoUnidadesText = wx.StaticText(id=wxID_FRAME1UMARCOUNIDADESTEXT, label=_('W/m2K'), name='uMarcoUnidadesText', parent=self, pos=wx.Point(365, 206), size=wx.Size(34, 13), style=0)
        self.absortividadText = wx.StaticText(id=wxID_FRAME1ABSORTIVIDADTEXT, label=_('Absortividad'), name='absortividadText', parent=self, pos=wx.Point(235, 236), size=wx.Size(60, 13), style=0)
        self.absortividad = wx.TextCtrl(id=wxID_FRAME1ABSORTIVIDAD, name='absortividad', parent=self, pos=wx.Point(304, 234), size=wx.Size(56, 21), style=0, value='')
        self.cargarMarco = wx.Button(id=wxID_FRAME1CARGARMARCO, label=_('Cargar al proyecto'), name='cargarMarco', parent=self, pos=wx.Point(220, 417), size=wx.Size(165, 21), style=0)
        self.cargarMarco.Bind(wx.EVT_BUTTON, self.OnCargarMarco, id=wxID_FRAME1CARGARMARCO)
        self.guardarMarco = wx.Button(id=wxID_FRAME1GUARDARMARCO, label=_('Guardar'), name='guardarMarco', parent=self, pos=wx.Point(220, 443), size=wx.Size(75, 23), style=0)
        self.guardarMarco.Bind(wx.EVT_BUTTON, self.OnGuardarMarco, id=wxID_FRAME1GUARDARMARCO)
        self.guardarMarco.SetForegroundColour(wx.Colour(0, 64, 128))
        self.guardarMarco.SetBackgroundColour('white')
        self.modificarMarco = wx.Button(id=wxID_FRAME1MODIFICARMARCO, label=_('Modificar'), name='modificarMarco', parent=self, pos=wx.Point(310, 443), size=wx.Size(75, 23), style=0)
        self.modificarMarco.Bind(wx.EVT_BUTTON, self.OnModificarMarco, id=wxID_FRAME1MODIFICARMARCO)
        self.modificarMarco.SetForegroundColour(wx.Colour(0, 64, 128))
        self.modificarMarco.SetBackgroundColour('white')
        self.borrarMarco = wx.Button(id=wxID_FRAME1BORRARMARCO, label=_('Borrar'), name='borrarMarco', parent=self, pos=wx.Point(445, 443), size=wx.Size(75, 23), style=0)
        self.borrarMarco.Bind(wx.EVT_BUTTON, self.OnBorrarMarco, id=wxID_FRAME1BORRARMARCO)
        self.borrarMarco.SetForegroundColour(wx.Colour(0, 64, 128))
        self.borrarMarco.SetBackgroundColour('white')

    def __init__(self, parent):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
        """
        self._init_ctrls(parent)
        self.elementosArbol = []
        self.cargarArbolMarcos(self.arbolMarcos)
        self.parent = parent
        self.dev = False

    def OnCargarMarco(self, event):
        """
        Metodo: OnCargarMarco

        ARGUMENTOS:
                event:
        """
        if self.arbolMarcos.GetChildrenCount(self.arbolMarcos.GetSelection()) == 0:
            marco = []
            prob = self.arbolMarcos.GetItemText(self.arbolMarcos.GetSelection())
            marco = cargaBD.cargarMarco(prob)
            self.dev = marco
            self.Close()

    def onArbolMarcos(self, event):
        """
        Metodo: onArbolMarcos

        ARGUMENTOS:
                event:
        """
        if self.arbolMarcos.GetChildrenCount(self.arbolMarcos.GetSelection()) == 0:
            marco = []
            prob = self.arbolMarcos.GetItemText(self.arbolMarcos.GetSelection())
            marco = cargaBD.cargarMarco(prob)
            self.nombreMarco.SetValue(str(marco[0]))
            self.grupoMarco.SetValue(str(marco[1]))
            self.uMarco.SetValue(str(marco[3]))
            self.absortividad.SetValue(str(marco[2]))
        else:
            self.nombreMarco.SetValue('')
            self.grupoMarco.SetValue('')
            self.uMarco.SetValue('')
            self.absortividad.SetValue('')
            self.seleccionarGrupoMarcoChoice.SetSelection(-1)

    def OnGuardarMarco(self, event):
        """
        Metodo: OnGuardarMarco

        ARGUMENTOS:
                event:
        """
        if cargaBD.compruebaMarco(self.nombreMarco.GetValue()) == False:
            nombreMarco = self.nombreMarco.GetValue()
            nombreMarco = str(nombreMarco.encode('cp1252'))
            nombre_grupo = self.grupoMarco.GetValue()
            nombre_grupo = str(nombre_grupo.encode('cp1252'))
            uMarco = self.uMarco.GetValue()
            absor = self.absortividad.GetValue()
            if ',' in uMarco:
                uMarco = uMarco.replace(',', '.')
            if ',' in absor:
                absor = absor.replace(',', '.')
            try:
                float(uMarco)
                if float(uMarco) <= 0:
                    uMarco = ''
            except:
                logging.info('Excepcion en: %s' % __name__)
                uMarco = ''

            try:
                float(absor)
                if float(absor) <= 0 or float(absor) > 1:
                    absor = ''
            except:
                logging.info('Excepcion en: %s' % __name__)
                absor = ''

            lista_errores = ''
            if nombreMarco == '':
                lista_errores += 'nombre'
            if nombre_grupo == '':
                if lista_errores != '':
                    lista_errores += ', '
                lista_errores += 'grupo'
            if uMarco == '':
                if lista_errores != '':
                    lista_errores += ', '
                lista_errores += 'U'
            if absor == '':
                if lista_errores != '':
                    lista_errores += ', '
                lista_errores += 'absortividad'
            if lista_errores != '':
                wx.MessageBox(_('Revise los siguientes campos:\n') + lista_errores, _('Aviso'))
                return
            nuevoMarco = []
            nuevoMarco.append(unicode(self.nombreMarco.GetValue()))
            nuevoMarco.append(unicode(self.grupoMarco.GetValue()))
            nuevoMarco.append(absor)
            nuevoMarco.append(uMarco)
            nuevoMarco.append('U')
            cargaBD.nuevoMarco(nuevoMarco)
            self.cargarArbolMarcos(self.arbolMarcos)
            self.seleccionarGrupoMarcoChoice.Clear()
            grupos1 = cargaBD.cargarGrupoMarcoCal()
            grupos2 = cargaBD.cargarGrupoMarcoUser()
            for i in grupos2:
                grupos1.append(i)

            self.seleccionarGrupoMarcoChoice.AppendItems(grupos1)
            self.nombreMarco.SetValue('')
            self.grupoMarco.SetValue('')
            self.uMarco.SetValue('')
            self.absortividad.SetValue('')
            self.seleccionarGrupoMarcoChoice.SetSelection(-1)
        else:
            wx.MessageBox(_('El nombre del marco ya existe, cámbielo para continuar'), _('Aviso'))

    def OnModificarMarco(self, event):
        """
        Metodo: OnModificarMarco

        ARGUMENTOS:
                event:
        """
        try:
            nombreViejo = self.arbolMarcos.GetItemText(self.arbolMarcos.GetSelection())
        except:
            wx.MessageBox(_('Debe seleccionar un elemento en el árbol'), _('Aviso'))
            return

        if self.arbolMarcos.GetChildrenCount(self.arbolMarcos.GetSelection()) > 0:
            if self.arbolMarcos.GetItemTextColour(self.arbolMarcos.GetSelection()) == 'Dark green':
                wx.MessageBox(_('No se puede modificar un grupo de marcos por defecto (en verde)'), _('Aviso'))
                return
        elif self.arbolMarcos.GetItemTextColour(self.arbolMarcos.GetSelection()) == 'green':
            wx.MessageBox(_('No se puede modificar un marco por defecto (en verde)'), _('Aviso'))
            return
        nombreMarco = self.nombreMarco.GetValue()
        nombreMarco = str(nombreMarco.encode('cp1252'))
        nombre_grupo = self.grupoMarco.GetValue()
        nombre_grupo = str(nombre_grupo.encode('cp1252'))
        uMarco = self.uMarco.GetValue()
        absor = self.absortividad.GetValue()
        if nombreViejo != nombreMarco:
            if cargaBD.compruebaMarco(self.nombreMarco.GetValue()) == True:
                wx.MessageBox(_('El nombre del marco ya existe, cámbielo para continuar'), _('Aviso'))
                return
        if ',' in uMarco:
            uMarco = uMarco.replace(',', '.')
        if ',' in absor:
            absor = absor.replace(',', '.')
        try:
            float(uMarco)
            if float(uMarco) <= 0:
                uMarco = ''
        except:
            logging.info('Excepcion en: %s' % __name__)
            uMarco = ''

        try:
            float(absor)
            if float(absor) <= 0 or float(absor) > 1:
                absor = ''
        except:
            logging.info('Excepcion en: %s' % __name__)
            absor = ''

        lista_errores = ''
        if nombreMarco == '':
            lista_errores += 'nombre'
        if nombre_grupo == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'grupo'
        if uMarco == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'U'
        if absor == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'absortividad'
        if lista_errores != '':
            wx.MessageBox(_('Revise los siguientes campos:\n') + lista_errores, _('Aviso'))
            return
        else:
            booleano = False
            for i in self.parent.panelEnvolvente.ventanas:
                try:
                    if i.marcoSeleccionado == nombreViejo.encode('cp1252'):
                        booleano = True
                        break
                except:
                    logging.info('Excepcion en: %s' % __name__)

            hola = Aviso_borrar_material.create(self, 2)
            hola.ShowModal()
            if hola.borrar == True:
                if booleano == True:
                    dlg = dialogoConfirma.Dialog2(self, b'El marco que est\xe1 tratando de modificar ha sido asignado a huecos que componen la envolvente t\xe9rmica del edificio y se ver\xe1n afectados por esa modificaci\xf3n. \xbfDesea continuar?')
                    dlg.ShowModal()
                    if dlg.dev == False:
                        return
                    for i in self.parent.panelEnvolvente.ventanas:
                        try:
                            if i.marcoSeleccionado == nombreViejo.encode('cp1252'):
                                i.marcoSeleccionado = nombreMarco
                                i.UmarcoConocido = uMarco
                                i.absortividadMarco = absor
                        except:
                            logging.info('Excepcion en: %s' % __name__)

                nuevoMarco = []
                nuevoMarco.append(unicode(self.nombreMarco.GetValue()))
                nuevoMarco.append(unicode(self.grupoMarco.GetValue()))
                nuevoMarco.append(absor)
                nuevoMarco.append(uMarco)
                nuevoMarco.append('U')
                cargaBD.modificaMarco(nuevoMarco, nombreViejo)
                self.cargarArbolMarcos(self.arbolMarcos)
                try:
                    self.parent.panelEnvolvente.OnArbolCerramientos(None)
                except:
                    logging.info('Excepcion en: %s' % __name__)

            return

    def OnBorrarMarco(self, event):
        """
        Metodo: OnBorrarMarco

        ARGUMENTOS:
                event:
        """
        try:
            self.arbolMarcos.GetItemText(self.arbolMarcos.GetSelection())
        except:
            logging.info('Excepcion en: %s' % __name__)
            wx.MessageBox(_('Debe seleccionar un elemento en el árbol'), _('Aviso'))
            return

        if self.arbolMarcos.GetChildrenCount(self.arbolMarcos.GetSelection()) > 0:
            if self.arbolMarcos.GetItemTextColour(self.arbolMarcos.GetSelection()) == 'Dark green':
                wx.MessageBox(_('No se puede eliminar un grupo de marcos por defecto (en verde)'), _('Aviso'))
                return
            hola = Aviso_borrar_material.create(self, 1)
            hola.ShowModal()
            if hola.borrar == True:
                cargaBD.borraGrupoMarcoUser(self.arbolMarcos.GetItemText(self.arbolMarcos.GetSelection()))
                self.seleccionarGrupoMarcoChoice.Clear()
                grupos1 = cargaBD.cargarGrupoMarcoCal()
                grupos2 = cargaBD.cargarGrupoMarcoUser()
                for i in grupos2:
                    grupos1.append(i)

                self.seleccionarGrupoMarcoChoice.AppendItems(grupos1)
                self.cargarArbolMarcos(self.arbolMarcos)
        elif self.arbolMarcos.GetItemTextColour(self.arbolMarcos.GetSelection()) == 'green':
            wx.MessageBox(_('No se puede eliminar un marco por defecto (en verde)'), _('Aviso'))
            return
        hola = Aviso_borrar_material.create(self, 0)
        hola.ShowModal()
        if hola.borrar == True:
            cargaBD.borraMarcoUser(self.arbolMarcos.GetItemText(self.arbolMarcos.GetSelection()))
            self.seleccionarGrupoMarcoChoice.Clear()
            grupos1 = cargaBD.cargarGrupoMarcoCal()
            grupos2 = cargaBD.cargarGrupoMarcoUser()
            for i in grupos2:
                grupos1.append(i)

            self.seleccionarGrupoMarcoChoice.AppendItems(grupos1)
            self.cargarArbolMarcos(self.arbolMarcos)
        self.cargarArbolMarcos(self.arbolMarcos)

    def onSeleccionarGrupoMarcoChoice(self, event):
        """
        Metodo: onSeleccionarGrupoMarcoChoice

        ARGUMENTOS:
                event:
        """
        self.grupoMarco.SetValue(self.seleccionarGrupoMarcoChoice.GetStringSelection())

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

    def cargarArbolMarcos(self, arbol):
        """
        Metodo: cargarArbolMarcos

        ARGUMENTOS:
                arbol:
        """
        elementosExpandidos = self.expandidosEnArbol(arbol)
        arbol.DeleteAllItems()
        self.elementosArbol = []
        root = arbol.AddRoot('Marcos')
        gruposCal = []
        gruposCal = cargaBD.cargarGrupoMarcoCal()
        mat = []
        for i in gruposCal:
            idTree = arbol.AppendItem(root, i)
            self.elementosArbol.append(idTree)
            arbol.SetItemTextColour(idTree, 'Dark green')
            mat = cargaBD.cargarMarcosCal(i)
            for j in mat:
                it = arbol.AppendItem(idTree, j)
                self.elementosArbol.append(it)
                arbol.SetItemTextColour(it, 'green')

            mat = cargaBD.cargarMarcosUser(i)
            for j in mat:
                it = arbol.AppendItem(idTree, j)
                self.elementosArbol.append(it)
                arbol.SetItemTextColour(it, 'grey')

        gruposUser = []
        gruposUser = cargaBD.cargarGrupoMarcoUser()
        for i in gruposUser:
            idTree = arbol.AppendItem(root, i)
            self.elementosArbol.append(idTree)
            arbol.SetItemTextColour(idTree, 'Black')
            mat = cargaBD.cargarMarcosUser(i)
            for j in mat:
                it = arbol.AppendItem(idTree, j)
                self.elementosArbol.append(it)
                arbol.SetItemTextColour(it, 'grey')

        arbol.Expand(root)
        self.expandirAnteriores(elementosExpandidos, arbol)