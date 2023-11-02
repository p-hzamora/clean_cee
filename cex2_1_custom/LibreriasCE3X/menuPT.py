# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: LibreriasCE3X\menuPT.pyc
# Compiled at: 2015-02-19 13:18:34
"""
Modulo: menuPT.py

"""
import wx, os, logging, ElementosConstructivos.Aviso_borrar_material as Aviso_borrar_material, ElementosConstructivos.cargaBD as cargaBD, directorios
Directorio = directorios.BuscaDirectorios().Directorio

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return Frame1(parent)


wxID_VENTANA, wxID_DESCRIPCIONTEXT, wxID_DESCRIPCION, wxID_GRUPO_MATERIAL_EXISTENTES_TEXT, wxID_GRUPO_MATERIAL_EXISTENTES, wxID_GRUPOMATERIALTEXT, wxID_GRUPOMATERIAL, wxID_ESPESORTEXT, wxID_ESPESOR, wxID_ESPESORUNIDADES, wxID_CONDUCTIVIDADTEXT, wxID_CONDUCTIVIDAD, wxID_CONDUCTIVIDADUNIDADES, wxID_DENSIDADTEXT, wxID_DENSIDAD, wxID_DENSIDADUNIDADES, wxID_CALORTEXT, wxID_CALOR, wxID_CALORUNIDADES, wxID_WXGUARDAR, wxID_WXBORRAR, wxID_FRAME1FICUADRO = [ wx.NewId() for _init_ctrls in range(22) ]
wxID_FRAME1, wxID_FRAME1BORRARMATERIAL, wxID_FRAME1FICUADRO, wxID_FRAME1CALORTEXT, wxID_FRAME1CALORUNIDADES, wxID_WXCARGARPT, wxID_FRAME1CONDUCTIVIDAD, wxID_FRAME1CONDUCTIVIDADTEXT, wxID_FRAME1CONDUCTIVIDADUNIDADES, wxID_FRAME1DENSIDAD, wxID_FRAME1DENSIDADTEXT, wxID_FRAME1DENSIDADUNIDADES, wxID_FRAME1DESCRIPCION, wxID_FRAME1DESCRIPCIONTEXT, wxID_FRAME1ESPESOR, wxID_FRAME1ESPESORTEXT, wxID_FRAME1ESPESORUNIDADES, wxID_FRAME1GRUPOMATERIAL, wxID_FRAME1GRUPOMATERIALTEXT, wxID_FRAME1GUARDAR, wxID_FRAME1STATICTEXT1, wxID_FRAME1VISTAMATERIALES, wxID_FRAME1BOTON_MODIFICAR, wxID_FRAME1FOTOMATERIAL, wxID_FRAME1CARGARIMAGEN, wxID_FRAME1FACTORVAPORTEXT, wxID_FRAME1FACTORVAPOR, wxID_TIPOFACHADA, wxID_PANEL1STATICBITMAP1 = [ wx.NewId() for _init_ctrls in range(29) ]

class Frame1(wx.Dialog):
    """
    Clase: Frame1 del modulo menuPT.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
        """
        wx.Dialog.__init__(self, id=-1, name='', parent=None, pos=wx.Point(0, 0), size=wx.Size(155, 13), style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN | wx.TAB_TRAVERSAL, title=_('Puentes Térmicos'))
        self.SetClientSize(wx.Size(770, 487))
        self.SetBackgroundColour('white')
        self.DescripcionText = wx.StaticText(id=wxID_DESCRIPCIONTEXT, label=_('Nombre'), name='DescripcionText', parent=self, pos=wx.Point(235, 86), size=wx.Size(65, 13), style=0)
        self.Descripcion = wx.TextCtrl(id=wxID_DESCRIPCION, name='Descripcion', parent=self, pos=wx.Point(304, 84), size=wx.Size(440, 21), style=0, value='')
        self.PuenteTermicoText = wx.StaticText(id=wxID_GRUPOMATERIALTEXT, label=_('Tipo'), name='GrupoText', parent=self, pos=wx.Point(235, 116), size=wx.Size(65, 13), style=0)
        grupos1 = cargaBD.cargarGrupoPTCal()
        grupos2 = cargaBD.cargarGrupoPTUser()
        for i in grupos2:
            grupos1.append(i)

        self.grupoPTChoice = wx.Choice(choices=grupos1, id=wxID_GRUPO_MATERIAL_EXISTENTES, name='grupoPTChoice', parent=self, pos=wx.Point(304, 114), size=wx.Size(440, 21), style=0)
        self.grupoPTChoice.Bind(wx.EVT_CHOICE, self.onGrupoPTChoice, id=wxID_GRUPO_MATERIAL_EXISTENTES)
        self.caracText = wx.StaticText(id=wxID_DESCRIPCIONTEXT, label=_('Características del cerramiento asociado'), name='DescripcionText', parent=self, pos=wx.Point(235, 146), size=wx.Size(195, 13), style=0)
        self.tipoFachada = wx.TextCtrl(id=wxID_DESCRIPCION, name='tipoFachada', parent=self, pos=wx.Point(468, 144), size=wx.Size(276, 21), style=0, value='')
        self.GrupoMaterialTexto_Existente = wx.StaticText(id=wxID_GRUPO_MATERIAL_EXISTENTES_TEXT, label=_('Seleccionar características ya definidas'), name='Grupo Material Text', parent=self, pos=wx.Point(235, 176), size=wx.Size(210, 13), style=0)
        self.tipoFachadaChoice = wx.Choice(choices=self.cargarFachadas(), id=wxID_TIPOFACHADA, name='tipoFachadaChoice', parent=self, pos=wx.Point(468, 174), size=wx.Size(276, 21), style=0)
        self.tipoFachadaChoice.Bind(wx.EVT_CHOICE, self.onTipoFachadaChoice, id=wxID_TIPOFACHADA)
        self.PropiedadesLinea = wx.StaticBox(id=-1, label=_('Propiedades'), name='PropiedadesLinea', parent=self, pos=wx.Point(220, 206), size=wx.Size(524, 176), style=0)
        self.PropiedadesLinea.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.PropiedadesLinea.SetForegroundColour(wx.Colour(0, 64, 128))
        self.fiText = wx.StaticText(id=wxID_CALORTEXT, label=_('φ'), name='fiText', parent=self, pos=wx.Point(235, 236), size=wx.Size(20, 41), style=0)
        self.fiCuadro = wx.TextCtrl(id=wxID_FRAME1FICUADRO, name='fiCuadro', parent=self, pos=wx.Point(304, 234), size=wx.Size(56, 21), style=0, value='')
        self.fiUnidades = wx.StaticText(id=wxID_CALORUNIDADES, label=_('W/mK'), name='fiUnidades', parent=self, pos=wx.Point(365, 236), size=wx.Size(30, 13), style=0)
        self.fotoMaterial = wx.StaticBitmap(bitmap=wx.Bitmap(Directorio + '/Imagenes/Fotos_Materiales/blanco.bmp'), id=wxID_PANEL1STATICBITMAP1, name='staticBitmap1', parent=self, pos=wx.Point(583, 220), size=wx.Size(125, 125), style=0)
        self.cargarImagen = wx.Button(id=wxID_FRAME1CARGARIMAGEN, label=_('Cargar Imagen'), name='cargarImagen', parent=self, pos=wx.Point(583, 352), size=wx.Size(125, 23), style=0)
        self.cargarImagen.Bind(wx.EVT_BUTTON, self.OnCargarImagenButton, id=wxID_FRAME1CARGARIMAGEN)
        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1, label=_('Librería de puentes térmicos'), name='staticText1', parent=self, pos=wx.Point(220, 22), size=wx.Size(106, 13), style=0)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.staticText1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.vistaMateriales = wx.TreeCtrl(id=wxID_FRAME1VISTAMATERIALES, name='vistaMateriales', parent=self, pos=wx.Point(8, 15), size=wx.Size(200, 450), style=wx.TR_HAS_BUTTONS)
        self.vistaMateriales.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnVistaMaterialesTreeSelChanged, id=wxID_FRAME1VISTAMATERIALES)
        self.cargarArbol(self.vistaMateriales)
        self.CargarPT = wx.Button(id=wxID_WXCARGARPT, label=_('Cargar al proyecto'), name=_('Cargar Puente Térmico'), parent=self, pos=wx.Point(220, 417), size=wx.Size(165, 21), style=0)
        self.CargarPT.Bind(wx.EVT_BUTTON, self.OnCargarButton, id=wxID_WXCARGARPT)
        self.guardarBoton = wx.Button(id=wxID_WXGUARDAR, label=_('Guardar'), name='Guardar', parent=self, pos=wx.Point(220, 443), size=wx.Size(75, 23), style=0)
        self.guardarBoton.Bind(wx.EVT_BUTTON, self.OnGuardarButton, id=wxID_WXGUARDAR)
        self.guardarBoton.SetForegroundColour(wx.Colour(0, 64, 128))
        self.guardarBoton.SetBackgroundColour('white')
        self.modificarBoton = wx.Button(id=wxID_FRAME1BOTON_MODIFICAR, label=_('Modificar'), name='boton_modificar', parent=self, pos=wx.Point(310, 443), size=wx.Size(75, 23), style=0)
        self.modificarBoton.Bind(wx.EVT_BUTTON, self.OnBoton_modificarButton, id=wxID_FRAME1BOTON_MODIFICAR)
        self.modificarBoton.Enable(False)
        self.modificarBoton.SetForegroundColour(wx.Colour(0, 64, 128))
        self.modificarBoton.SetBackgroundColour('white')
        self.borrarBoton = wx.Button(id=wxID_FRAME1BORRARMATERIAL, label=_('Borrar'), name='borrarPuenteTérmico', parent=self, pos=wx.Point(445, 443), size=wx.Size(75, 23), style=0)
        self.borrarBoton.Enable(False)
        self.borrarBoton.Bind(wx.EVT_BUTTON, self.OnBorrarMaterialButton, id=wxID_FRAME1BORRARMATERIAL)
        self.borrarBoton.SetForegroundColour(wx.Colour(0, 64, 128))
        self.borrarBoton.SetBackgroundColour('white')
        return

    def cargarFachadas(self):
        """
        Metodo: cargarFachadas

        """
        tipos = cargaBD.obtenerFachadas()
        return tipos

    def __init__(self, parent):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
        """
        self.elementosArbol = []
        self._init_ctrls(parent)
        self.imageFile = ''
        self.dev = False

    def onTipoFachadaChoice(self, event):
        """
        Metodo: onTipoFachadaChoice

        ARGUMENTOS:
                event:
        """
        grupo_seleccionado = self.tipoFachadaChoice.GetStringSelection()
        self.tipoFachada.SetValue(grupo_seleccionado)

    def onGrupoPTChoice(self, event):
        """
        Metodo: onGrupoPTChoice

        ARGUMENTOS:
                event:
        """
        event.Skip()

    def OnCargarButton(self, event):
        """
        Metodo: OnCargarButton

        ARGUMENTOS:
                event:
        """
        nombre_cerramiento = self.Descripcion.GetValue()
        nombre_cerramiento = str(nombre_cerramiento.encode('cp1252'))
        nombre_grupo = self.grupoPTChoice.GetStringSelection()
        nombre_grupo = str(nombre_grupo.encode('cp1252'))
        nombre_fachada = self.tipoFachada.GetValue()
        nombre_fachada = str(nombre_fachada.encode('cp1252'))
        fiCuadro = self.fiCuadro.GetValue()
        if ',' in fiCuadro:
            fiCuadro = fiCuadro.replace(',', '.')
        try:
            float(fiCuadro)
            if float(fiCuadro) <= 0:
                fiCuadro = ''
        except:
            logging.info('Excepcion en: %s' % __name__)
            fiCuadro = ''

        if nombre_cerramiento == '' and nombre_grupo == '' and nombre_fachada == '' and fiCuadro == '':
            wx.MessageBox(_('Indique el puente térmico que desea cargar'), _('Aviso'))
            return
        lista_errores = ''
        if nombre_cerramiento == '':
            lista_errores += 'nombre'
        if nombre_grupo == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'tipo'
        if nombre_fachada == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'características del cerramiento asociado'
        if fiCuadro == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'φ'
        if lista_errores != '':
            wx.MessageBox(_('Revise los siguientes campos:\n') + str(lista_errores), _('Aviso'))
            return
        self.dev = [
         nombre_cerramiento, nombre_grupo, nombre_fachada, fiCuadro]
        self.Close()

    def OnGuardarButton(self, event):
        """
        Metodo: OnGuardarButton

        ARGUMENTOS:
                event:
        """
        nombre_cerramiento = self.Descripcion.GetValue()
        nombre_cerramiento = str(nombre_cerramiento.encode('cp1252'))
        nombre_grupo = self.grupoPTChoice.GetStringSelection()
        nombre_grupo = str(nombre_grupo.encode('cp1252'))
        nombre_fachada = self.tipoFachada.GetValue()
        nombre_fachada = str(nombre_fachada.encode('cp1252'))
        fiCuadro = self.fiCuadro.GetValue()
        if ',' in fiCuadro:
            fiCuadro = fiCuadro.replace(',', '.')
        try:
            float(fiCuadro)
            if float(fiCuadro) <= 0:
                fiCuadro = ''
        except (ValueError, TypeError):
            fiCuadro = ''

        lista_errores = ''
        if nombre_cerramiento == '':
            lista_errores += 'nombre'
        if nombre_grupo == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'tipo'
        if nombre_fachada == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'características del cerramiento asociado'
        if fiCuadro == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'φ'
        if lista_errores != '':
            wx.MessageBox(_('Revise los siguientes campos:\n') + lista_errores, _('Aviso'))
            return
        if cargaBD.compruebaPT(self.Descripcion.GetValue(), nombre_fachada, nombre_grupo) == False:
            nuevoMaterial = []
            nuevoMaterial.append(self.Descripcion.GetValue())
            nuevoMaterial.append(self.tipoFachada.GetValue())
            nuevoMaterial.append(fiCuadro)
            nuevoMaterial.append(self.imageFile)
            nuevoMaterial.append('U')
            nuevoMaterial.append(nombre_grupo)
            cargaBD.nuevoPT(nuevoMaterial)
            self.cargarArbol(self.vistaMateriales)
            self.tipoFachadaChoice.SetItems(self.cargarFachadas())
            self.modificarBoton.Enable(False)
            self.Descripcion.SetValue('')
            self.fiCuadro.SetValue(' ')
            self.tipoFachada.SetValue(' ')
            bmp = wx.Image(Directorio + '/Imagenes/Fotos_Materiales/blanco.bmp')
            bmp = bmp.Scale(125, 125, wx.IMAGE_QUALITY_HIGH)
            self.fotoMaterial.SetBitmap(wx.BitmapFromImage(bmp))
            self.fotoMaterial.SetBitmap(wx.BitmapFromImage(bmp))
        else:
            wx.MessageBox(_('El nombre del puente térmico ya existe, cámbielo para continuar'), _('Aviso'))

    def OnVistaMaterialesTreeSelChanged(self, event):
        """
        Metodo: OnVistaMaterialesTreeSelChanged

        ARGUMENTOS:
                event:
        """
        if self.vistaMateriales.GetItemTextColour(self.vistaMateriales.GetSelection()) == 'grey':
            self.modificarBoton.Enable(True)
            self.borrarBoton.Enable(True)
        else:
            self.modificarBoton.Enable(False)
            self.borrarBoton.Enable(False)
        if self.vistaMateriales.GetItemTextColour(self.vistaMateriales.GetSelection()) == 'Black':
            self.modificarBoton.Enable(True)
            self.borrarBoton.Enable(True)
        if self.vistaMateriales.GetChildrenCount(self.vistaMateriales.GetSelection()) == 0:
            try:
                material = []
                prob = self.vistaMateriales.GetItemText(self.vistaMateriales.GetSelection())
                papa = self.vistaMateriales.GetItemParent(self.vistaMateriales.GetSelection())
                padre = self.vistaMateriales.GetItemText(papa)
                abuelo = self.vistaMateriales.GetItemText(self.vistaMateriales.GetItemParent(self.vistaMateriales.GetItemParent(self.vistaMateriales.GetSelection())))
                material = cargaBD.cargarPT(prob, padre, abuelo)
                self.Descripcion.SetValue(str(material[0]))
                self.grupoPTChoice.SetStringSelection(str(material[-1]))
                self.tipoFachada.SetValue(str(material[1]))
                self.tipoFachadaChoice.SetStringSelection(str(material[1]))
                self.fiCuadro.SetValue(str(material[2]))
                self.imageFile = material[3]
                try:
                    if os.path.exists(self.imageFile.decode('iso-8859-15')) == True:
                        bmp = wx.Image(material[3].decode('iso-8859-15'))
                    elif os.path.exists(Directorio + '/Imagenes/' + material[3].decode('iso-8859-15')) == True and '.' in material[3]:
                        bmp = wx.Image(Directorio + '/Imagenes/' + material[3].decode('iso-8859-15'))
                    bmp = bmp.Scale(125, 125, wx.IMAGE_QUALITY_HIGH)
                    self.fotoMaterial.SetBitmap(wx.BitmapFromImage(bmp))
                    self.fotoMaterial.SetBitmap(wx.BitmapFromImage(bmp))
                except:
                    logging.info('Excepcion en: %s' % __name__)

            except:
                logging.info('Excepcion en: %s' % __name__)

        else:
            self.imageFile = ''
            self.Descripcion.SetValue('')
            self.fiCuadro.SetValue(' ')
            self.modificarBoton.Enable(False)
            bmp = wx.Image(Directorio + '/Imagenes/Fotos_Materiales/blanco.bmp')
            bmp = bmp.Scale(125, 125, wx.IMAGE_QUALITY_HIGH)
            self.fotoMaterial.SetBitmap(wx.BitmapFromImage(bmp))
            self.fotoMaterial.SetBitmap(wx.BitmapFromImage(bmp))
            if self.vistaMateriales.GetItemText(self.vistaMateriales.GetSelection()) == 'Puentes Térmicos':
                self.grupoPTChoice.SetStringSelection('')
                self.tipoFachada.SetValue(' ')
                self.tipoFachadaChoice.SetStringSelection('')
                return
            papa = self.vistaMateriales.GetItemParent(self.vistaMateriales.GetSelection())
            if self.vistaMateriales.GetItemText(papa) == 'Puentes Térmicos':
                self.grupoPTChoice.SetStringSelection(self.vistaMateriales.GetItemText(self.vistaMateriales.GetSelection()))
                self.tipoFachada.SetValue(' ')
                self.tipoFachadaChoice.SetStringSelection('')
            else:
                self.grupoPTChoice.SetStringSelection(self.vistaMateriales.GetItemText(papa))
                self.tipoFachada.SetValue(self.vistaMateriales.GetItemText(self.vistaMateriales.GetSelection()))
                self.tipoFachadaChoice.SetStringSelection(self.vistaMateriales.GetItemText(self.vistaMateriales.GetSelection()))

    def OnBorrarMaterialButton(self, event):
        """
        Metodo: OnBorrarMaterialButton

        ARGUMENTOS:
                event:
        """
        if self.vistaMateriales.GetChildrenCount(self.vistaMateriales.GetSelection()) > 0:
            if self.vistaMateriales.GetItemTextColour(self.vistaMateriales.GetSelection()) == 'Dark green':
                wx.MessageBox(_('No se puede eliminar un grupo puentes térmicos por defecto'), _('Aviso'))
            else:
                papa = self.vistaMateriales.GetItemParent(self.vistaMateriales.GetSelection())
                padre = self.vistaMateriales.GetItemText(papa)
                hola = Aviso_borrar_material.create(self, 1)
                hola.ShowModal()
                if hola.borrar == True:
                    cargaBD.borraGrupoPTUser(self.vistaMateriales.GetItemText(self.vistaMateriales.GetSelection()), padre)
                    self.cargarArbol(self.vistaMateriales)
        elif self.vistaMateriales.GetItemTextColour(self.vistaMateriales.GetSelection()) == wx.Colour(100, 200, 0):
            wx.MessageBox(_('No se puede eliminar un puente térmico por defecto'), _('Aviso'))
        else:
            hola = Aviso_borrar_material.create(self, 0)
            hola.ShowModal()
            if hola.borrar == True:
                papa = self.vistaMateriales.GetItemParent(self.vistaMateriales.GetSelection())
                padre = self.vistaMateriales.GetItemText(papa)
                abuelo = self.vistaMateriales.GetItemText(self.vistaMateriales.GetItemParent(self.vistaMateriales.GetItemParent(self.vistaMateriales.GetSelection())))
                cargaBD.borraPTUser(self.vistaMateriales.GetItemText(self.vistaMateriales.GetSelection()), padre, abuelo)
        self.cargarArbol(self.vistaMateriales)
        self.Descripcion.SetValue('')
        self.fiCuadro.SetValue(' ')
        self.tipoFachada.SetValue(' ')
        self.modificarBoton.Enable(False)
        self.tipoFachadaChoice.SetItems(self.cargarFachadas())
        self.imageFile = ''
        bmp = wx.Image(Directorio + '/Imagenes/Fotos_Materiales/blanco.bmp')
        bmp = bmp.Scale(125, 125, wx.IMAGE_QUALITY_HIGH)
        self.fotoMaterial.SetBitmap(wx.BitmapFromImage(bmp))
        self.fotoMaterial.SetBitmap(wx.BitmapFromImage(bmp))

    def OnBoton_modificarButton(self, event):
        """
        Metodo: OnBoton_modificarButton

        ARGUMENTOS:
                event:
        """
        try:
            nombreViejo = self.vistaMateriales.GetItemText(self.vistaMateriales.GetSelection())
        except:
            wx.MessageBox(_('Debe seleccionar un elemento en el árbol'), _('Aviso'))
            return

        nombre_cerramiento = self.Descripcion.GetValue()
        nombre_cerramiento = str(nombre_cerramiento.encode('cp1252'))
        nombre_grupo = self.grupoPTChoice.GetStringSelection()
        nombre_grupo = str(nombre_grupo.encode('cp1252'))
        nombre_fachada = self.tipoFachada.GetValue()
        nombre_fachada = str(nombre_fachada.encode('cp1252'))
        fiCuadro = self.fiCuadro.GetValue()
        if nombreViejo != nombre_cerramiento:
            if cargaBD.compruebaPT(self.Descripcion.GetValue(), nombre_fachada, nombre_grupo) == True:
                wx.MessageBox(_('El nombre del puente térmico ya existe, cámbielo para continuar'), _('Aviso'))
                return
        if ',' in fiCuadro:
            fiCuadro = fiCuadro.replace(',', '.')
        try:
            float(fiCuadro)
            if float(fiCuadro) <= 0:
                fiCuadro = ''
        except (ValueError, TypeError):
            fiCuadro = ''

        lista_errores = ''
        if nombre_cerramiento == '':
            lista_errores += 'nombre'
        if nombre_grupo == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'tipo'
        if nombre_fachada == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'características del cerramiento asociado'
        if fiCuadro == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'φ'
        if lista_errores != '':
            wx.MessageBox(_('Revise los siguientes campos:\n') + lista_errores, _('Aviso'))
            return
        hola = Aviso_borrar_material.create(self, 2)
        hola.ShowModal()
        if hola.borrar == True:
            nuevoMaterial = []
            nuevoMaterial.append(self.Descripcion.GetValue())
            nuevoMaterial.append(self.tipoFachada.GetValue())
            nuevoMaterial.append(fiCuadro)
            nuevoMaterial.append(self.imageFile)
            nuevoMaterial.append('U')
            nuevoMaterial.append(nombre_grupo)
            cargaBD.modificaPT(nuevoMaterial, nombreViejo)
            self.cargarArbol(self.vistaMateriales)

    def OnCargarImagenButton(self, event):
        """
        Metodo: OnCargarImagenButton

        ARGUMENTOS:
                event:
        """
        tipoArchivo = 'All files (*.*)|*.*'
        dlg = wx.FileDialog(self, message='Seleccione una foto para el material', defaultDir=Directorio + '/Imagenes/PuentesTermicos', style=wx.OPEN, wildcard=tipoArchivo)
        if dlg.ShowModal() == wx.ID_OK:
            self.imageFile = dlg.GetPath()
            bmp = wx.Image(dlg.GetPath())
            bmp = bmp.Scale(125, 125, wx.IMAGE_QUALITY_HIGH)
            self.fotoMaterial.SetBitmap(wx.BitmapFromImage(bmp))

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
                arbol:
        """
        elementosExpandidos = self.expandidosEnArbol(arbol)
        arbol.DeleteAllItems()
        self.elementosArbol = []
        root = arbol.AddRoot('Puentes Térmicos')
        gruposCal = []
        gruposCal = cargaBD.cargarGrupoPTCal()
        mat = []
        for i in gruposCal:
            idTree = arbol.AppendItem(root, i)
            self.elementosArbol.append(idTree)
            arbol.SetItemTextColour(idTree, 'Dark green')
            mat = cargaBD.cargarOpcionesCerramientoCal(i)
            for j in mat:
                it = arbol.AppendItem(idTree, j)
                self.elementosArbol.append(it)
                arbol.SetItemTextColour(it, wx.Colour(100, 200, 100))
                mat2 = cargaBD.cargaPTCal(i, j)
                for k in mat2:
                    it2 = arbol.AppendItem(it, k)
                    self.elementosArbol.append(it2)
                    arbol.SetItemTextColour(it2, wx.Colour(100, 200, 0))

                mat2 = cargaBD.cargaPTUser(i, j)
                for k in mat2:
                    it2 = arbol.AppendItem(it, k)
                    self.elementosArbol.append(it2)
                    arbol.SetItemTextColour(it2, 'grey')

            mat = cargaBD.cargarOpcionesCerramientoUser(i)
            for j in mat:
                it = arbol.AppendItem(idTree, j)
                self.elementosArbol.append(it)
                arbol.SetItemTextColour(it, 'Black')
                mat2 = cargaBD.cargaPTUser(i, j)
                for k in mat2:
                    it2 = arbol.AppendItem(it, k)
                    self.elementosArbol.append(it2)
                    arbol.SetItemTextColour(it2, 'grey')

        arbol.Expand(root)
        self.expandirAnteriores(elementosExpandidos, arbol)