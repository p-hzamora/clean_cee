# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: LibreriasCE3X\menuCerramientos.pyc
# Compiled at: 2015-05-29 09:04:55
"""
Modulo: menuCerramientos.py

"""
import wx, os, logging, ElementosConstructivos.BDcerramientos as BDcerramientos, ElementosConstructivos.cargaBD as cargaBD, directorios
Directorio = directorios.BuscaDirectorios().Directorio
DirectorioBD = directorios.BuscaDirectorios().DirectorioDoc
import Envolvente.dialogoConfirma as confirmacion, Envolvente.apendiceE as apendiceE
wxID_VENTANA, wxID_DESCRIPCIONTEXT, wxID_WXLISTCTRL1, wxID_LISTACERRAMIENTOSCREADOSTEXTO, wxID_LISTACERRAMIENTOSCREADOS, wxID_GRUPO_MATERIAL_TEXTO, wxID_GRUPO_MATERIAL, wxID_MATERIAL_TEXTO, wxID_MATERIAL, wxID_ESPESORTEXT, wxID_ESPESOR, wxID_ESPESORUNIDADES, wxID_CONDUCTIVIDADTEXT, wxID_CONDUCTIVIDAD, wxID_CONDUCTIVIDADUNIDADES, wxID_DENSIDADTEXT, wxID_DENSIDAD, wxID_DENSIDADUNIDADES, wxID_CALORTEXT, wxID_CALOR, wxID_CALORUNIDADES, wxID_WXANADIR, wxID_WXMODIFICAR, wxID_WXBORRAR, wxID_WXSUBIR, wxID_WXBAJAR, wxID_TRANSMITANCIATEXT, wxID_TRANSMITANCIA, wxID_TRANSMITANCIAUNIDADES, wxID_WXGUARDAR, wxID_WXLIMPIAR, wxID_FRAME1FACTORVAPORTEXT, wxID_FRAME1FACTORVAPOR, wxID_FRAME1PANEL1, wxID_FRAME1ESPESOR, wxID_EXPLICACION_TEXTO, wxID_CAPATEXT, wxID_CERRAMIENTOTEXT, wxID_WXMODIFICARCERRA, wxID_WXBORRARCERRA, wxID_PANEL1TREECTRL1, wxID_WXCARGARCERRA, wxID_FRAME1STATICTEXT1, wxID_CAMARAUNIDADES = [ wx.NewId() for _init_ctrls in range(44) ]

def getPosicionAislamiento(aislamientoCheck, posicionAislamientoChoice):
    if aislamientoCheck == False:
        casoAislamiento = 'Ninguno'
    elif posicionAislamientoChoice == 'La partición':
        casoAislamiento = 'AisladoParticion'
    elif posicionAislamientoChoice == 'El cerramiento':
        casoAislamiento = 'AisladoCerramiento'
    elif posicionAislamientoChoice == 'Ambos':
        casoAislamiento = 'Ambos'
    else:
        casoAislamiento = 'Ninguno'
    return casoAislamiento


def getGradoVentilacion(gradoVentilacion):
    nivelesVentilacion = [
     'Ligeramente Ventilado', 'Ventilado']
    return nivelesVentilacion.index(gradoVentilacion)


class composicionCerramiento:
    """
    Clase: composicionCerramiento del modulo menuCerramientos.py

    """

    def __init__(self, nombre, transmitancia, peso, materiales):
        """
        Constructor de la clase

        ARGUMENTOS:
                nombre:
                transmitancia:
                peso:
                materiales:
        """
        self.nombre = nombre
        self.transmitancia = transmitancia
        self.peso = peso
        self.materiales = materiales


def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return Dialog1(parent)


class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo menuCerramientos.py

    """
    lista_materiales_seleccionar = []
    transmitancia_global = 0.0
    lista_materiales = []

    def OnEspesorText(self, event):
        """
        Metodo: OnEspesorText

        ARGUMENTOS:
                event:
        """
        self.Espesor.SetForegroundColour(wx.Colour('black'))

    def _init_coll_listCtrl1_Columns(self, parent):
        """
        Metodo: _init_coll_listCtrl1_Columns

        ARGUMENTOS:
                parent:
        """
        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading=_('Material'), width=125)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading=_('Grupo'), width=125)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading=_('R (m2 K/W)'), width=62)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT, heading=_('Espesor (m)'), width=62)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT, heading='λ (W/mK)', width=62)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_LEFT, heading='ρ (kg/m3)', width=62)
        parent.InsertColumn(col=6, format=wx.LIST_FORMAT_LEFT, heading='Cp (J/kgK)', width=62)

    def __init__(self, parent):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
        """
        self.parent = parent
        wx.Dialog.__init__(self, id=wxID_VENTANA, name='', parent=parent, pos=wx.Point(0, 0), size=wx.Size(850, 600), style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN, title=_('Cerramientos'))
        self.SetClientSize(wx.Size(850, 600))
        self.SetBackgroundColour('white')
        self.arbol = wx.TreeCtrl(id=wxID_PANEL1TREECTRL1, name='treeCtrl1', parent=self, pos=wx.Point(8, 15), size=wx.Size(200, 565), style=wx.TR_HAS_BUTTONS)
        self.arbol.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnArbol, id=wxID_PANEL1TREECTRL1)
        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1, label=_('Librería de cerramientos'), name='staticText1', parent=self, pos=wx.Point(220, 22), size=wx.Size(106, 13), style=0)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.staticText1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.DescripcionText = wx.StaticText(id=wxID_DESCRIPCIONTEXT, label=_('Nombre'), name='DescripcionText', parent=self, pos=wx.Point(235, 60), size=wx.Size(65, 13), style=0)
        self.Descripcion = wx.TextCtrl(id=wxID_DESCRIPCIONTEXT, name='Descripcion', parent=self, pos=wx.Point(350, 58), size=wx.Size(450, 21), style=0, value='')
        self.CaracteristicasCerramientoLinea = wx.StaticBox(id=-1, label=_('Características del cerramiento'), name='PropiedadesLinea', parent=self, pos=wx.Point(220, 90), size=wx.Size(620, 290), style=0)
        self.CaracteristicasCerramientoLinea.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasCerramientoLinea.SetForegroundColour(wx.Colour(0, 64, 128))
        self.Explicaciontexto = wx.StaticText(id=wxID_EXPLICACION_TEXTO, label=_('Verticales (Materiales ordenados de exterior a interior);  Horizontales (Materiales ordenados de arriba a abajo)'), name='Grupo Material Text', parent=self, pos=wx.Point(250, 110), size=wx.Size(560, 15), style=0)
        self.listCtrl1 = wx.ListCtrl(id=wxID_WXLISTCTRL1, name='listCtrl1', parent=self, pos=wx.Point(235, 130), size=wx.Size(565, 145), style=wx.LC_REPORT)
        self._init_coll_listCtrl1_Columns(self.listCtrl1)
        self.listCtrl1.Bind(wx.EVT_LIST_ITEM_SELECTED, self.pinchar_listCtrl1, id=wxID_WXLISTCTRL1)
        self.Subir = wx.BitmapButton(bitmap=wx.Bitmap(Directorio + '/Imagenes/botonUp.ico', wx.BITMAP_TYPE_ANY), id=wxID_WXSUBIR, name='Subir', parent=self, pos=wx.Point(805, 155), size=wx.Size(30, 40), style=wx.BU_AUTODRAW)
        self.Subir.Bind(wx.EVT_BUTTON, self.OnSubirButton, id=wxID_WXSUBIR)
        self.Bajar = wx.BitmapButton(bitmap=wx.Bitmap(Directorio + '/Imagenes/botonDown.ico', wx.BITMAP_TYPE_ANY), id=wxID_WXBAJAR, name='Bajar', parent=self, pos=wx.Point(805, 200), size=wx.Size(30, 40), style=wx.BU_AUTODRAW)
        self.Bajar.Bind(wx.EVT_BUTTON, self.OnBajarButton, id=wxID_WXBAJAR)
        self.fotoCerramiento = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self, pos=wx.Point(355, 285), size=wx.Size(140, 85), style=wx.TAB_TRAVERSAL)
        self.fotoCerramiento.Refresh()
        self.TransmitanciaText = wx.StaticBox(id=wxID_TRANSMITANCIATEXT, label=_('R1+....+Rn'), name='TransmitanciaText', parent=self, pos=wx.Point(660, 305), size=wx.Size(140, 40), style=0)
        self.TransmitanciaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.TransmitanciaText.SetForegroundColour(wx.Colour(0, 0, 100))
        try:
            valorInicializado = str(round(1.0 / float(self.transmitancia_global)), 2)
        except (NameError, ZeroDivisionError):
            valorInicializado = '0.0'
        except (ValueError, TypeError):
            valorInicializado = '0.0'

        self.Transmitancia = wx.StaticText(id=wxID_TRANSMITANCIA, label=valorInicializado, name='Transmitancia', parent=self, pos=wx.Point(705, 325), size=wx.Size(30, 13), style=0)
        self.TransmitanciaUnidades = wx.StaticText(id=wxID_TRANSMITANCIAUNIDADES, label=_('m2K/W'), name='TransmitanciaUnidades', parent=self, pos=wx.Point(740, 325), size=wx.Size(40, 13), style=0)
        self.CaracteristicasMaterialLinea = wx.StaticBox(id=-1, label=_('Características del material'), name='PropiedadesLinea', parent=self, pos=wx.Point(220, 390), size=wx.Size(620, 124), style=0)
        self.CaracteristicasMaterialLinea.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasMaterialLinea.SetForegroundColour(wx.Colour(0, 64, 128))
        self.GrupoMaterialTexto = wx.StaticText(id=wxID_GRUPO_MATERIAL_TEXTO, label=_('Grupo de materiales'), name='Grupo Material Text', parent=self, pos=wx.Point(235, 410), size=wx.Size(110, 13), style=0)
        grupos1 = cargaBD.cargarGrupoCal()
        grupos2 = cargaBD.cargarGrupoUser()
        for i in grupos2:
            grupos1.append(i)

        self.GrupoMaterial = wx.Choice(choices=grupos1, id=wxID_GRUPO_MATERIAL, name='GrupoMaterial', parent=self, pos=wx.Point(350, 408), size=wx.Size(380, 21), style=0)
        self.GrupoMaterial.Bind(wx.EVT_CHOICE, self.SeleccionarGrupoMaterial, id=wxID_GRUPO_MATERIAL)
        self.MaterialTexto = wx.StaticText(id=wxID_MATERIAL_TEXTO, label=_('Material'), name='Material Text', parent=self, pos=wx.Point(235, 435), size=wx.Size(95, 13), style=0)
        self.Material = wx.Choice(choices=self.lista_materiales_seleccionar, id=wxID_MATERIAL, name='Material', parent=self, pos=wx.Point(350, 433), size=wx.Size(380, 21), style=0)
        self.Material.Bind(wx.EVT_CHOICE, self.SeleccionarMaterial, id=wxID_MATERIAL)
        self.EspesorText = wx.StaticText(id=wxID_ESPESORTEXT, label=_('Espesor'), name='EspesorText', parent=self, pos=wx.Point(235, 460), size=wx.Size(40, 13), style=0)
        self.Espesor = wx.TextCtrl(id=wxID_ESPESOR, name='Espesor', parent=self, pos=wx.Point(350, 458), size=wx.Size(56, 21), style=0, value='')
        self.Espesor.SetForegroundColour(wx.Colour(100, 200, 0))
        self.Espesor.Bind(wx.EVT_TEXT, self.OnEspesorText, id=wxID_FRAME1ESPESOR)
        self.EspesorUnidades = wx.StaticText(id=wxID_ESPESORUNIDADES, label=_('m'), name='EspesorUnidades', parent=self, pos=wx.Point(411, 460), size=wx.Size(40, 13), style=0)
        self.ConductividadText = wx.StaticText(id=wxID_CONDUCTIVIDADTEXT, label=_('λ'), name='ConductividadText', parent=self, pos=wx.Point(495, 460), size=wx.Size(10, 13), style=0)
        self.Conductividad = wx.TextCtrl(id=wxID_CONDUCTIVIDAD, name='Conductividad', parent=self, pos=wx.Point(580, 458), size=wx.Size(56, 21), style=0, value='')
        self.Conductividad.SetEditable(False)
        self.ConductividadUnidades = wx.StaticText(id=wxID_CONDUCTIVIDADUNIDADES, label=_('W/mK'), name='ConductividadUnidades', parent=self, pos=wx.Point(641, 460), size=wx.Size(30, 13), style=0)
        self.DensidadText = wx.StaticText(id=wxID_DENSIDADTEXT, label=_('ρ'), name='Densidad', parent=self, pos=wx.Point(235, 485), size=wx.Size(10, 13), style=0)
        self.Densidad = wx.TextCtrl(id=wxID_DENSIDAD, name='Densidad', parent=self, pos=wx.Point(350, 483), size=wx.Size(56, 21), style=0, value='')
        self.Densidad.SetEditable(False)
        self.DensidadUnidades = wx.StaticText(id=wxID_DENSIDADUNIDADES, label=_('kg/m3'), name='DensidadUnidades', parent=self, pos=wx.Point(411, 485), size=wx.Size(40, 13), style=0)
        self.CalorText = wx.StaticText(id=wxID_CALORTEXT, label=_('Calor específico'), name='CalorText', parent=self, pos=wx.Point(495, 485), size=wx.Size(83, 25), style=0)
        self.Calor = wx.TextCtrl(id=wxID_CALOR, name='Calor', parent=self, pos=wx.Point(580, 483), size=wx.Size(56, 21), style=0, value='')
        self.Calor.SetEditable(False)
        self.CalorUnidades = wx.StaticText(id=wxID_CALORUNIDADES, label=_('J/kgK'), name='CalorUnidades', parent=self, pos=wx.Point(641, 485), size=wx.Size(30, 13), style=0)
        self.resistenciaCamaraText = wx.StaticText(id=wxID_FRAME1FACTORVAPORTEXT, label=_('R'), name='resistenciaCamaraText', parent=self, pos=wx.Point(235, 460), size=wx.Size(40, 13), style=0)
        self.resistenciaCamara = wx.TextCtrl(id=wxID_FRAME1FACTORVAPOR, name='resistenciaCamara', parent=self, pos=wx.Point(350, 458), size=wx.Size(56, 21), style=0, value='')
        self.resistenciaCamara.SetToolTipString('')
        self.resistenciaCamaraUnidades = wx.StaticText(id=wxID_CAMARAUNIDADES, label=_('m2K/W'), name='CalorUnidades', parent=self, pos=wx.Point(411, 460), size=wx.Size(40, 13), style=0)
        self.resistenciaCamara.Show(False)
        self.resistenciaCamara.SetEditable(False)
        self.resistenciaCamaraText.Show(False)
        self.resistenciaCamaraUnidades.Show(False)
        self.anadir = wx.Button(id=wxID_WXANADIR, label=_('Añadir'), name='anadir', parent=self, pos=wx.Point(735, 410), size=wx.Size(100, 21), style=0)
        self.anadir.Bind(wx.EVT_BUTTON, self.OnAnadirButton, id=wxID_WXANADIR)
        self.Modificar = wx.Button(id=wxID_WXMODIFICAR, label=_('Modificar'), name='Modificar', parent=self, pos=wx.Point(735, 435), size=wx.Size(100, 21), style=0)
        self.Modificar.Bind(wx.EVT_BUTTON, self.OnModificarButton, id=wxID_WXMODIFICAR)
        self.Borrar = wx.Button(id=wxID_WXBORRAR, label=_('Borrar'), name='Borrar', parent=self, pos=wx.Point(735, 460), size=wx.Size(100, 21), style=0)
        self.Borrar.Bind(wx.EVT_BUTTON, self.OnBorrarButton, id=wxID_WXBORRAR)
        self.limpiar = wx.Button(id=wxID_WXLIMPIAR, label=_('Limpiar campos'), name='limpiar', parent=self, pos=wx.Point(735, 485), size=wx.Size(100, 21), style=0)
        self.limpiar.Bind(wx.EVT_BUTTON, self.OnLimpiarButton, id=wxID_WXLIMPIAR)
        self.CargarCerramiento = wx.Button(id=wxID_WXCARGARCERRA, label=_('Cargar al proyecto'), name='CargarCerramiento', parent=self, pos=wx.Point(220, 531), size=wx.Size(125, 21), style=0)
        self.CargarCerramiento.Bind(wx.EVT_BUTTON, self.onCargarCerramiento, id=wxID_WXCARGARCERRA)
        self.Guardar = wx.Button(id=wxID_WXGUARDAR, label=_('Guardar cerramiento'), name='Guardar', parent=self, pos=wx.Point(220, 557), size=wx.Size(125, 23), style=0)
        self.Guardar.Bind(wx.EVT_BUTTON, self.OnGuardarButton, id=wxID_WXGUARDAR)
        self.Guardar.SetForegroundColour(wx.Colour(0, 64, 128))
        self.Guardar.SetBackgroundColour('white')
        self.ModificarCerramiento = wx.Button(id=wxID_WXMODIFICARCERRA, label=_('Modificar cerramiento'), name='ModificarCerramiento', parent=self, pos=wx.Point(360, 557), size=wx.Size(125, 23), style=0)
        self.ModificarCerramiento.Bind(wx.EVT_BUTTON, self.OnModificarCerramientoButton, id=wxID_WXMODIFICARCERRA)
        self.ModificarCerramiento.SetForegroundColour(wx.Colour(0, 64, 128))
        self.ModificarCerramiento.SetBackgroundColour('white')
        self.BorrarCerramiento = wx.Button(id=wxID_WXBORRARCERRA, label=_('Borrar cerramiento'), name='BorrarCerramiento', parent=self, pos=wx.Point(545, 557), size=wx.Size(125, 23), style=0)
        self.BorrarCerramiento.Bind(wx.EVT_BUTTON, self.OnBorrarCerramientoButton, id=wxID_WXBORRARCERRA)
        self.BorrarCerramiento.SetForegroundColour(wx.Colour(0, 64, 128))
        self.BorrarCerramiento.SetBackgroundColour('white')
        self.pos_selec = 0
        self.longitud_listCtrl = 0
        self.lista_materiales = []
        self.peso_m2 = ()
        self.cargarArbol(self.arbol)

    def opcionesDeGrupo(self, grupo_seleccionado):
        """
        Metodo: opcionesDeGrupo

        ARGUMENTOS:
                grupo_seleccionado:
        """
        if grupo_seleccionado == 'Cámaras de aire':
            self.resistenciaCamara.Show(True)
            self.resistenciaCamaraText.Show(True)
            self.resistenciaCamaraUnidades.Show(True)
            self.EspesorText.Show(False)
            self.Espesor.Show(False)
            self.EspesorUnidades.Show(False)
            self.ConductividadText.Show(False)
            self.Conductividad.Show(False)
            self.ConductividadUnidades.Show(False)
            self.DensidadText.Show(False)
            self.Densidad.Show(False)
            self.DensidadUnidades.Show(False)
            self.CalorText.Show(False)
            self.Calor.Show(False)
            self.CalorUnidades.Show(False)
        else:
            self.resistenciaCamara.Show(False)
            self.resistenciaCamaraText.Show(False)
            self.resistenciaCamaraUnidades.Show(False)
            self.EspesorText.Show(True)
            self.Espesor.Show(True)
            self.EspesorUnidades.Show(True)
            self.ConductividadText.Show(True)
            self.Conductividad.Show(True)
            self.ConductividadUnidades.Show(True)
            self.DensidadText.Show(True)
            self.Densidad.Show(True)
            self.DensidadUnidades.Show(True)
            self.CalorText.Show(True)
            self.Calor.Show(True)
            self.CalorUnidades.Show(True)

    def onCargarCerramiento(self, event):
        """
        Metodo: onCargarCerramiento

        ARGUMENTOS:
                event:
        """
        nombre_cerramiento = str(self.Descripcion.GetValue().encode('iso-8859-15'))
        if nombre_cerramiento == '':
            wx.MessageBox(_('Indique el nombre del cerramiento'), _('Aviso'))
            return
        if self.listCtrl1.GetItemCount() == 0:
            wx.MessageBox(_('No puede crear una composición de cerramiento sin ningún material.'), _('Aviso'))
            return
        for i in self.parent.listadoComposicionesCerramientos:
            if i.nombre == nombre_cerramiento:
                wx.MessageBox(_('Ya ha cargado una composición de cerramiento con ese nombre al proyecto actual.'), _('Aviso'))
                return

        materiales = []
        for i in self.lista_materiales:
            mat = cargaBD.cargarMaterial(i[0])
            material = []
            material.append(mat[0])
            material.append(i[3])
            material.append(i[4])
            material.append(i[5])
            material.append(i[6])
            material.append(mat[6])
            material.append(mat[7])
            material.append(mat[8])
            material.append(mat[5])
            materiales.append(material)

        self.parent.listadoComposicionesCerramientos.append(composicionCerramiento(nombre_cerramiento, self.transmitancia_global, self.peso_m2, materiales))
        self.cargarArbol(self.arbol)

    def cargarArbol(self, arbol):
        """
        Metodo: cargarArbol

        ARGUMENTOS:
                arbol:
        """
        arbol.DeleteAllItems()
        root = arbol.AddRoot('Cerramientos')
        arbol.SetItemTextColour(root, 'black')
        arbol.SetItemBold(root)
        it1 = arbol.AppendItem(root, 'BD cerramientos')
        arbol.SetItemTextColour(it1, wx.Colour(0, 64, 128))
        arbol.SetItemBold(it1)
        it2 = arbol.AppendItem(root, 'Cerramientos del Proyecto')
        arbol.SetItemTextColour(it2, wx.Colour(0, 64, 128))
        arbol.SetItemBold(it2)
        cerra = BDcerramientos.cargaCerramientos(DirectorioBD + '/bbdd.dat')
        for i in cerra:
            arbol.AppendItem(it1, i)

        for i in self.parent.listadoComposicionesCerramientos:
            arbol.AppendItem(it2, i.nombre)

        arbol.Expand(root)
        arbol.Expand(it1)
        arbol.Expand(it2)

    def OnArbol(self, event):
        """
        Metodo: OnArbol

        ARGUMENTOS:
                event:
        """
        Cerramiento_Seleccionado = self.arbol.GetItemText(self.arbol.GetSelection())
        if Cerramiento_Seleccionado == 'Cerramientos' or Cerramiento_Seleccionado == 'Cerramientos del Proyecto' or Cerramiento_Seleccionado == 'BD cerramientos':
            return
        padre = self.arbol.GetItemText(self.arbol.GetItemParent(self.arbol.GetSelection()))
        imagenes = []
        if padre == 'BD cerramientos':
            self.Guardar.Enable(True)
            cerra = BDcerramientos.cargaCerramiento(Cerramiento_Seleccionado, DirectorioBD + '/bbdd.dat')
            self.lista_materiales = []
            self.listCtrl1.DeleteAllItems()
            for i in cerra[1]:
                fila_cerr = []
                mat = BDcerramientos.cargaMaterial(i[1], DirectorioBD + '/bbdd.dat')
                fila_cerr.append(unicode(i[1], 'cp1252'))
                fila_cerr.append(unicode(mat[8], 'cp1252'))
                fila_cerr.append(unicode(round(float(i[3]) / float(mat[2]), 3)))
                fila_cerr.append(i[3])
                fila_cerr.append(mat[2])
                fila_cerr.append(mat[3])
                fila_cerr.append(mat[4])
                self.lista_materiales.append(fila_cerr)
                if mat[7] == 'U':
                    if os.path.exists(mat[6]):
                        imagenes.append(mat[6])
                    else:
                        imagenes.append(str(Directorio + '/Imagenes/Fotos_Materiales/defecto.bmp'))
                else:
                    imagenes.append(str(Directorio + '/Imagenes/Fotos_Materiales/' + str(mat[6])))

        else:
            if padre == 'Cerramientos del Proyecto':
                self.Guardar.Enable(False)
                self.lista_materiales = []
                self.listCtrl1.DeleteAllItems()
                for i in self.parent.listadoComposicionesCerramientos:
                    if i.nombre == str(Cerramiento_Seleccionado.encode('iso-8859-15')):
                        for mat in i.materiales:
                            fila_cerr = []
                            fila_cerr.append(unicode(mat[0], 'cp1252'))
                            fila_cerr.append(unicode(mat[7], 'cp1252'))
                            fila_cerr.append(unicode(round(float(mat[1]) / float(mat[2]), 3)))
                            fila_cerr.append(mat[1])
                            fila_cerr.append(mat[2])
                            fila_cerr.append(mat[3])
                            fila_cerr.append(mat[4])
                            self.lista_materiales.append(fila_cerr)
                            if mat[6] == 'U':
                                imagenes.append(str(Directorio + '/Imagenes/Fotos_Materiales/defecto.bmp'))
                            else:
                                imagenes.append(str(Directorio + '/Imagenes/Fotos_Materiales/' + str(mat[5])))

                        break

            for i in self.lista_materiales:
                if 'Cámaras de aire' not in i[1]:
                    self.listCtrl1.Append(i)
                else:
                    self.listCtrl1.Append([i[0], i[1], i[2], '-', '-', '-', '-'])

            self.Descripcion.SetValue(Cerramiento_Seleccionado)
            self.cambiar_transmitancia_global()
            try:
                self.Transmitancia.SetLabel(str(round(1.0 / float(self.transmitancia_global), 2)))
            except (NameError, ZeroDivisionError):
                self.Transmitancia.SetLabel('')
            except (ValueError, TypeError):
                self.Transmitancia.SetLabel('')

            self.Espesor.SetValue('')
            self.Conductividad.SetValue('')
            self.Densidad.SetValue('')
            self.Calor.SetValue('')
            grupos1 = cargaBD.cargarGrupoCal()
            grupos2 = cargaBD.cargarGrupoUser()
            for i in grupos2:
                grupos1.append(i)

            self.GrupoMaterial.SetItems(grupos1)
            self.Material.Clear()
            materiales = []
            espesores = []
            for i in self.lista_materiales:
                materiales.append(i[0])
                espesores.append(float(i[3]))

        self.cargaFotoCerramiento(espesores, imagenes)

    def OnBorrarCerramientoButton(self, event):
        """
        Metodo: OnBorrarCerramientoButton

        ARGUMENTOS:
                event:
        """
        try:
            Cerramiento_Seleccionado = self.arbol.GetItemText(self.arbol.GetSelection())
        except:
            wx.MessageBox(_('Debe seleccionar el cerramiento del árbol que desea borrar.'), _('Aviso'))

        if Cerramiento_Seleccionado == 'Cerramientos' or Cerramiento_Seleccionado == 'Cerramientos del Proyecto' or Cerramiento_Seleccionado == 'BD cerramientos':
            wx.MessageBox(_('No puede eliminar este elemento.'), _('Aviso'))
            return
        else:
            padre = self.arbol.GetItemText(self.arbol.GetItemParent(self.arbol.GetSelection()))
            if event != None:
                borrar = confirmacion.Dialog1(self, '¿Desea borrar el elemento seleccionado?')
                borrar.ShowModal()
                if borrar.dev == False:
                    return
            if padre == 'BD cerramientos':
                BDcerramientos.borrarCerramiento(Cerramiento_Seleccionado, DirectorioBD + '/bbdd.dat')
            else:
                for i in self.parent.panelEnvolvente.cerramientos:
                    if 'Conocidas' in i[8] and i[6] == Cerramiento_Seleccionado.encode('iso-8859-15'):
                        wx.MessageBox(_('No puede eliminar este elemento por que ya está asignado a un cerramiento de la envolvente térmica.'), _('Aviso'))
                        return
                    if i[1] == 'Partición Interior' and 'Estimadas' in i[8] and i[9][4] == 'Conocida' and i[9][7] == Cerramiento_Seleccionado.encode('iso-8859-15'):
                        wx.MessageBox(_('No puede eliminar este elemento por que ya está asignado a un cerramiento de la envolvente térmica.'), _('Aviso'))
                        return

                for i in range(len(self.parent.listadoComposicionesCerramientos)):
                    if self.parent.listadoComposicionesCerramientos[i].nombre == Cerramiento_Seleccionado.encode('iso-8859-15'):
                        self.parent.listadoComposicionesCerramientos.pop(i)
                        break

            self.cargarArbol(self.arbol)
            return

    def OnModificarCerramientoButton(self, event):
        """
        Metodo: OnModificarCerramientoButton

        ARGUMENTOS:
                event:
        """
        try:
            Cerramiento_Seleccionado = self.arbol.GetItemText(self.arbol.GetSelection())
        except:
            wx.MessageBox(_('Debe seleccionar el cerramiento del árbol que desea borrar.'), _('Aviso'))
            return

        if Cerramiento_Seleccionado == 'Cerramientos' or Cerramiento_Seleccionado == 'Cerramientos del Proyecto' or Cerramiento_Seleccionado == 'BD cerramientos':
            wx.MessageBox(_('No puede modificar este elemento.'), _('Aviso'))
            return
        else:
            if self.listCtrl1.GetItemCount() == 0:
                wx.MessageBox(_('No puede crear una composición de cerramiento sin ningún material.'), _('Aviso'))
                return
            nuevo = self.Descripcion.GetValue().encode('iso-8859-15')
            padre = self.arbol.GetItemText(self.arbol.GetItemParent(self.arbol.GetSelection()))
            if padre == 'BD cerramientos':
                if nuevo == '':
                    wx.MessageBox(_('Indique el nombre del cerramiento'), _('Aviso'))
                    return
                if BDcerramientos.existeCerra(nuevo, DirectorioBD + '/bbdd.dat') == True and nuevo != self.arbol.GetItemText(self.arbol.GetSelection()).encode('iso-8859-15'):
                    wx.MessageBox(_('Ya existe un cerramiento con el nombre definido.'), _('Aviso'))
                    return
                self.OnBorrarCerramientoButton(None)
                self.OnGuardarButton(event)
            else:
                materiales = []
                for i in self.lista_materiales:
                    mat = cargaBD.cargarMaterial(i[0])
                    material = []
                    material.append(str(i[0].encode('cp1252')))
                    material.append(i[3])
                    material.append(i[4])
                    material.append(i[5])
                    material.append(i[6])
                    if mat != []:
                        material.append(mat[6])
                        material.append(mat[7])
                        material.append(mat[8])
                        material.append(mat[5])
                    else:
                        material.append('')
                        material.append('U')
                        material.append(str(i[1].encode('cp1252')))
                        material.append('')
                    materiales.append(material)

                if nuevo == Cerramiento_Seleccionado.encode('iso-8859-15'):
                    uso = False
                    for i in self.parent.panelEnvolvente.cerramientos:
                        if 'Conocidas' in i[8] and i[6] == Cerramiento_Seleccionado.encode('iso-8859-15'):
                            uso = True
                            break

                    if uso == True:
                        dlg = confirmacion.Dialog1(self, 'El cerramiento seleccionado ha sido asignado a algún elemento de tipo cerramientos opacos.¿Desea continuar?')
                        dlg.ShowModal()
                        if dlg.dev == False:
                            return
                        for i in range(len(self.parent.listadoComposicionesCerramientos)):
                            if self.parent.listadoComposicionesCerramientos[i].nombre == Cerramiento_Seleccionado.encode('iso-8859-15'):
                                self.parent.listadoComposicionesCerramientos[i] = composicionCerramiento(Cerramiento_Seleccionado.encode('iso-8859-15'), self.transmitancia_global, self.peso_m2, materiales)
                                break

                        for j in self.parent.panelEnvolvente.cerramientos:
                            if 'Conocidas' in j[8] and j[6] == Cerramiento_Seleccionado.encode('iso-8859-15'):
                                if j[1] == 'Cubierta' and j[-1] == 'aire':
                                    j[6] = nuevo
                                    UCerramiento = apendiceE.cerramientosExteriores(self.transmitancia_global, 'HorizontalFlujoAscendente')
                                    j[3] = str(round(UCerramiento, 2))
                                    j[4] = float(self.peso_m2)
                                else:
                                    if j[1] == 'Cubierta' and j[-1] == 'terreno':
                                        j[6] = nuevo
                                        profundidad = j[10]
                                        UCerramiento = apendiceE.cubiertaTerreno(self.transmitancia_global, profundidad)
                                        j[3] = str(round(UCerramiento, 2))
                                        j[4] = float(self.peso_m2) + 1800 * float(profundidad)
                                    else:
                                        if j[1] == 'Fachada' and j[-1] == 'aire':
                                            j[6] = nuevo
                                            UCerramiento = apendiceE.cerramientosExteriores(self.transmitancia_global, 'Vertical')
                                            j[3] = str(round(UCerramiento, 2))
                                            j[4] = float(self.peso_m2)
                                        elif j[1] == 'Suelo' and j[-1] == 'aire':
                                            j[6] = nuevo
                                            UCerramiento = apendiceE.cerramientosExteriores(self.transmitancia_global, 'HorizontalFlujoDescendente')
                                            j[3] = str(round(UCerramiento, 2))
                                            j[4] = float(self.peso_m2)
                            elif j[1] == 'Partición Interior' and 'Estimadas' in j[8] and j[9][4] == 'Conocida' and j[9][7] == Cerramiento_Seleccionado.encode('iso-8859-15'):
                                if j[1] == 'Partición Interior' and j[-1] == 'horizontal inferior':
                                    if j[5] == 'Garaje/espacio enterrado':
                                        j[9][7] = nuevo
                                        Up_sinRs = float(self.transmitancia_global)
                                        Uparticion = apendiceE.particionesInterioresResistencias(Up_sinRs, 'HorizontalInferior')
                                        Api = float(j[2])
                                        Ae = float(j[9][2])
                                        volumenNH = float(j[9][3])
                                        gradoVentilacion = getGradoVentilacion(j[9][1])
                                        b = apendiceE.particionesInterioresCaso2(Api, Uparticion, Ae, gradoVentilacion, volumenNH)
                                        UCerramiento = float(b) * float(Uparticion)
                                        j[3] = str(round(UCerramiento, 2))
                                        j[4] = float(self.peso_m2)
                                    elif j[5] == 'Cámara Sanitaria':
                                        j[9][7] = nuevo
                                        Aparticion = float(j[2])
                                        perimetro = float(j[9][0])
                                        B = Aparticion / (0.5 * perimetro)
                                        Uparticion = float(self.transmitancia_global)
                                        Rparticion = 1.0 / Uparticion
                                        UCerramiento = apendiceE.camaraSanitaria(B, Rparticion)
                                        j[3] = str(round(UCerramiento, 2))
                                        j[4] = float(self.peso_m2)
                                else:
                                    if j[1] == 'Partición Interior' and j[-1] == 'horizontal superior':
                                        j[9][7] = nuevo
                                        Up_sinRs = float(self.transmitancia_global)
                                        Uparticion = apendiceE.particionesInterioresResistencias(Up_sinRs, 'HorizontalSuperior')
                                        Api = float(j[2])
                                        Ae = float(j[9][1])
                                        gradoVentilacion = getGradoVentilacion(j[9][0])
                                        posicionAislamiento = getPosicionAislamiento(j[9][2], j[9][3])
                                        b = apendiceE.particionesInterioresCaso1(Api, Ae, posicionAislamiento, gradoVentilacion)
                                        UCerramiento = float(b) * float(Uparticion)
                                        j[3] = str(round(UCerramiento, 2))
                                        j[4] = float(self.peso_m2)
                                    elif j[1] == 'Partición Interior' and j[-1] == 'vertical':
                                        j[9][7] = nuevo
                                        Up_sinRs = float(self.transmitancia_global)
                                        Uparticion = apendiceE.particionesInterioresResistencias(Up_sinRs, 'Vertical')
                                        Api = float(j[2])
                                        Ae = float(j[9][1])
                                        gradoVentilacion = getGradoVentilacion(j[9][0])
                                        posicionAislamiento = getPosicionAislamiento(j[9][2], j[9][3])
                                        b = apendiceE.particionesInterioresCaso1(Api, Ae, posicionAislamiento, gradoVentilacion)
                                        UCerramiento = float(b) * float(Uparticion)
                                        j[3] = str(round(UCerramiento, 2))
                                        j[4] = float(self.peso_m2)

                    else:
                        for i in range(len(self.parent.listadoComposicionesCerramientos)):
                            if self.parent.listadoComposicionesCerramientos[i].nombre == Cerramiento_Seleccionado.encode('iso-8859-15'):
                                self.parent.listadoComposicionesCerramientos[i] = composicionCerramiento(Cerramiento_Seleccionado.encode('iso-8859-15'), self.transmitancia_global, self.peso_m2, materiales)

                else:
                    for i in self.parent.listadoComposicionesCerramientos:
                        if i.nombre == nuevo:
                            wx.MessageBox(_('Ya existe una composición de cerramientos con ese nombre en este proyecto'), _('Aviso'))
                            return

                    uso = False
                    for i in self.parent.panelEnvolvente.cerramientos:
                        if 'Conocidas' in i[8] and i[6] == Cerramiento_Seleccionado.encode('iso-8859-15'):
                            uso = True
                            break

                    if uso == True:
                        dlg = confirmacion.Dialog1(self, 'El cerramiento seleccionado ha sido asignado a algún elemento de tipo cerramientos opacos.¿Desea continuar?')
                        dlg.ShowModal()
                        if dlg.dev == False:
                            return
                        for i in range(len(self.parent.listadoComposicionesCerramientos)):
                            if self.parent.listadoComposicionesCerramientos[i].nombre == Cerramiento_Seleccionado.encode('iso-8859-15'):
                                self.parent.listadoComposicionesCerramientos[i] = composicionCerramiento(nuevo, self.transmitancia_global, self.peso_m2, materiales)
                                break

                        for j in self.parent.panelEnvolvente.cerramientos:
                            if 'Conocidas' in j[8] and j[6] == Cerramiento_Seleccionado.encode('iso-8859-15'):
                                if j[1] == 'Cubierta' and j[-1] == 'aire':
                                    j[6] = nuevo
                                    UCerramiento = apendiceE.cerramientosExteriores(self.transmitancia_global, 'HorizontalFlujoAscendente')
                                    j[3] = str(round(UCerramiento, 2))
                                    j[4] = float(self.peso_m2)
                                else:
                                    if j[1] == 'Cubierta' and j[-1] == 'terreno':
                                        j[6] = nuevo
                                        profundidad = j[10]
                                        UCerramiento = apendiceE.cubiertaTerreno(self.transmitancia_global, profundidad)
                                        j[3] = str(round(UCerramiento, 2))
                                        j[4] = float(self.peso_m2) + 1800 * float(profundidad)
                                    else:
                                        if j[1] == 'Fachada' and j[-1] == 'aire':
                                            j[6] = nuevo
                                            UCerramiento = apendiceE.cerramientosExteriores(self.transmitancia_global, 'Vertical')
                                            j[3] = str(round(UCerramiento, 2))
                                            j[4] = float(self.peso_m2)
                                        elif j[1] == 'Suelo' and j[-1] == 'aire':
                                            j[6] = nuevo
                                            UCerramiento = apendiceE.cerramientosExteriores(self.transmitancia_global, 'HorizontalFlujoDescendente')
                                            j[3] = str(round(UCerramiento, 2))
                                            j[4] = float(self.peso_m2)
                            elif j[1] == 'Partición Interior' and 'Estimadas' in j[8] and j[9][4] == 'Conocida' and j[9][7] == Cerramiento_Seleccionado.encode('iso-8859-15'):
                                if j[1] == 'Partición Interior' and j[-1] == 'horizontal inferior':
                                    if j[5] == 'Garaje/espacio enterrado':
                                        j[9][7] = nuevo
                                        Up_sinRs = float(self.transmitancia_global)
                                        Uparticion = apendiceE.particionesInterioresResistencias(Up_sinRs, 'HorizontalInferior')
                                        Api = float(j[2])
                                        Ae = float(j[9][2])
                                        volumenNH = float(j[9][3])
                                        gradoVentilacion = getGradoVentilacion(j[9][1])
                                        b = apendiceE.particionesInterioresCaso2(Api, Uparticion, Ae, gradoVentilacion, volumenNH)
                                        UCerramiento = float(b) * float(Uparticion)
                                        j[3] = str(round(UCerramiento, 2))
                                        j[4] = float(self.peso_m2)
                                    elif j[5] == 'Cámara Sanitaria':
                                        j[9][7] = nuevo
                                        Aparticion = float(j[2])
                                        perimetro = float(j[9][0])
                                        B = Aparticion / (0.5 * perimetro)
                                        Uparticion = float(self.transmitancia_global)
                                        Rparticion = 1.0 / Uparticion
                                        UCerramiento = apendiceE.camaraSanitaria(B, Rparticion)
                                        j[3] = str(round(UCerramiento, 2))
                                        j[4] = float(self.peso_m2)
                                else:
                                    if j[1] == 'Partición Interior' and j[-1] == 'horizontal superior':
                                        j[9][7] = nuevo
                                        Up_sinRs = float(self.transmitancia_global)
                                        Uparticion = apendiceE.particionesInterioresResistencias(Up_sinRs, 'HorizontalSuperior')
                                        Api = float(j[2])
                                        Ae = float(j[9][1])
                                        gradoVentilacion = getGradoVentilacion(j[9][0])
                                        posicionAislamiento = getPosicionAislamiento(j[9][2], j[9][3])
                                        b = apendiceE.particionesInterioresCaso1(Api, Ae, posicionAislamiento, gradoVentilacion)
                                        UCerramiento = float(b) * float(Uparticion)
                                        j[3] = str(round(UCerramiento, 2))
                                        j[4] = float(self.peso_m2)
                                    elif j[1] == 'Partición Interior' and j[-1] == 'vertical':
                                        j[9][7] = nuevo
                                        Up_sinRs = float(self.transmitancia_global)
                                        Uparticion = apendiceE.particionesInterioresResistencias(Up_sinRs, 'Vertical')
                                        Api = float(j[2])
                                        Ae = float(j[9][1])
                                        gradoVentilacion = getGradoVentilacion(j[9][0])
                                        posicionAislamiento = getPosicionAislamiento(j[9][2], j[9][3])
                                        b = apendiceE.particionesInterioresCaso1(Api, Ae, posicionAislamiento, gradoVentilacion)
                                        UCerramiento = float(b) * float(Uparticion)
                                        j[3] = str(round(UCerramiento, 2))
                                        j[4] = float(self.peso_m2)

                    else:
                        for i in range(len(self.parent.listadoComposicionesCerramientos)):
                            if self.parent.listadoComposicionesCerramientos[i].nombre == Cerramiento_Seleccionado.encode('iso-8859-15'):
                                self.parent.listadoComposicionesCerramientos[i] = composicionCerramiento(nuevo, self.transmitancia_global, self.peso_m2, materiales)

            self.cargarArbol(self.arbol)
            try:
                self.parent.panelEnvolvente.OnArbolCerramientos(None)
            except:
                logging.info('Excepcion en: %s' % __name__)

            return

    def cargaFotoCerramiento(self, a, imageFile):
        """
        Metodo: cargaFotoCerramiento

        ARGUMENTOS:
                a:
                imageFile:
        """
        if a != []:
            anchura = 0
            x = []
            for i in a:
                anchura = anchura + i
                x.append(i)

            suma = 0
            for i in range(len(a)):
                x[i] = int(a[i] * self.fotoCerramiento.Size[0] / anchura)
                suma = suma + x[i]

            if suma < self.fotoCerramiento.Size[0]:
                x[len(x) - 1] = x[len(x) - 1] + (self.fotoCerramiento.Size[0] - suma)
            posi = 0
            for i in range(len(a)):
                bmp = wx.Bitmap(imageFile[i])
                size = bmp.GetWidth()
                size = bmp.GetWidth()
                size = bmp.GetWidth()
                while x[i] > size:
                    wx.StaticBitmap(parent=self.fotoCerramiento, id=-1, bitmap=bmp, size=(size, 85), pos=(posi, 0))
                    x[i] = x[i] - size
                    posi = posi + size

                wx.StaticBitmap(parent=self.fotoCerramiento, id=-1, bitmap=bmp, size=(x[i], 85), pos=(posi, 0))
                posi = posi + x[i]

            self.fotoCerramiento.Refresh()
        else:
            self.fotoCerramiento = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self, pos=wx.Point(355, 285), size=wx.Size(140, 85), style=wx.TAB_TRAVERSAL)
            self.fotoCerramiento.Refresh()

    def OnLimpiarButton(self, event):
        """
        Metodo: OnLimpiarButton

        ARGUMENTOS:
                event:
        """
        self.opcionesDeGrupo('')
        self.lista_materiales = []
        self.transmitancia_global = ()
        self.peso_m2 = ()
        self.listCtrl1.DeleteAllItems()
        self.Transmitancia.SetLabel(_('0.0'))
        grupos1 = cargaBD.cargarGrupoCal()
        grupos2 = cargaBD.cargarGrupoUser()
        for i in grupos2:
            grupos1.append(i)

        self.GrupoMaterial.SetItems(grupos1)
        self.Material.Clear()
        self.Descripcion.SetValue('')
        self.Espesor.SetValue('')
        self.Conductividad.SetValue('')
        self.Densidad.SetValue('')
        self.Calor.SetValue('')
        self.resistenciaCamara.SetValue('')
        self.fotoCerramiento = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self, pos=wx.Point(355, 285), size=wx.Size(140, 85), style=wx.TAB_TRAVERSAL)
        self.fotoCerramiento.Refresh()

    def SeleccionarGrupoMaterial(self, parent):
        """
        Metodo: SeleccionarGrupoMaterial

        ARGUMENTOS:
                parent:
        """
        grupo = self.GrupoMaterial.GetString(self.GrupoMaterial.GetCurrentSelection())
        mat1 = cargaBD.cargarMateriales(grupo)
        self.opcionesDeGrupo(grupo)
        self.Material.Clear()
        self.Material.AppendItems(mat1)
        self.Material.SetSelection(-1)
        self.Espesor.SetValue('')
        self.Conductividad.SetValue('')
        self.Densidad.SetValue('')
        self.Calor.SetValue('')
        self.resistenciaCamara.SetValue('')

    def SeleccionarMaterial(self, parent):
        """
        Metodo: SeleccionarMaterial

        ARGUMENTOS:
                parent:
        """
        mat = self.Material.GetString(self.Material.GetCurrentSelection())
        mat1 = cargaBD.cargarMaterial(mat)
        THICKNESS = str(mat1[1])
        CONDUCTIVITY = str(mat1[2])
        DENSITY = str(mat1[3])
        SPECIFIC_HEAT = str(mat1[4])
        R = str(float(mat1[1]) / float(mat1[2]))
        self.Espesor.SetValue(THICKNESS)
        self.Conductividad.SetValue(CONDUCTIVITY)
        self.Densidad.SetValue(DENSITY)
        self.Calor.SetValue(SPECIFIC_HEAT)
        self.resistenciaCamara.SetValue(str(round(float(R), 3)))

    def OnSubirButton(self, event):
        """
        Metodo: OnSubirButton

        ARGUMENTOS:
                event:
        """
        posicion = self.pos_selec
        if posicion != 0:
            posicion_anterior = posicion - 1
        else:
            posicion_anterior = self.longitud_listCtrl - 1
        try:
            fila_1 = self.lista_materiales[posicion_anterior]
            fila_2 = self.lista_materiales[posicion]
        except IndexError:
            return

        self.lista_materiales[posicion_anterior] = fila_2
        self.lista_materiales[posicion] = fila_1
        self.listCtrl1.SetStringItem(posicion_anterior, 0, fila_2[0])
        self.listCtrl1.SetStringItem(posicion_anterior, 1, fila_2[1])
        if 'Cámaras de aire' not in fila_2[1]:
            self.listCtrl1.SetStringItem(posicion_anterior, 6, str(fila_2[2]))
            self.listCtrl1.SetStringItem(posicion_anterior, 3, str(fila_2[3]))
            self.listCtrl1.SetStringItem(posicion_anterior, 4, str(fila_2[4]))
            self.listCtrl1.SetStringItem(posicion_anterior, 5, str(fila_2[5]))
        else:
            self.listCtrl1.SetStringItem(posicion_anterior, 6, '-')
            self.listCtrl1.SetStringItem(posicion_anterior, 3, '-')
            self.listCtrl1.SetStringItem(posicion_anterior, 4, '-')
            self.listCtrl1.SetStringItem(posicion_anterior, 5, '-')
        self.listCtrl1.SetStringItem(posicion_anterior, 2, str(round(float(fila_2[3]) / float(fila_2[4]), 3)))
        self.listCtrl1.SetStringItem(posicion, 0, fila_1[0])
        self.listCtrl1.SetStringItem(posicion, 1, fila_1[1])
        if 'Cámaras de aire' not in fila_1[1]:
            self.listCtrl1.SetStringItem(posicion, 6, str(fila_1[2]))
            self.listCtrl1.SetStringItem(posicion, 3, str(fila_1[3]))
            self.listCtrl1.SetStringItem(posicion, 4, str(fila_1[4]))
            self.listCtrl1.SetStringItem(posicion, 5, str(fila_1[5]))
        else:
            self.listCtrl1.SetStringItem(posicion, 6, '-')
            self.listCtrl1.SetStringItem(posicion, 3, '-')
            self.listCtrl1.SetStringItem(posicion, 4, '-')
            self.listCtrl1.SetStringItem(posicion, 5, '-')
        self.listCtrl1.SetStringItem(posicion, 2, str(round(float(fila_1[3]) / float(fila_1[4]), 3)))
        materiales = []
        espesores = []
        for i in self.lista_materiales:
            materiales.append(i[0])
            espesores.append(float(i[3]))

        imagenes = []
        for i in materiales:
            mat = cargaBD.cargarMaterial(i)
            if mat != []:
                if str(mat[7]) == 'U':
                    imagenes.append(mat[6])
                else:
                    imagenes.append(str(Directorio + '/Imagenes/Fotos_Materiales/' + str(mat[6])))
            else:
                imagenes.append(str(Directorio + '/Imagenes/Fotos_Materiales/defecto.bmp'))

        self.cargaFotoCerramiento(espesores, imagenes)
        self.listCtrl1.SetItemState(posicion, 0, wx.LIST_STATE_SELECTED | wx.LIST_STATE_FOCUSED)
        self.listCtrl1.SetItemState(posicion_anterior, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)

    def OnBajarButton(self, event):
        """
        Metodo: OnBajarButton

        ARGUMENTOS:
                event:
        """
        posicion = self.pos_selec
        if posicion != self.longitud_listCtrl - 1:
            posicion_siguiente = posicion + 1
        else:
            posicion_siguiente = 0
        try:
            fila_1 = self.lista_materiales[posicion]
            fila_2 = self.lista_materiales[posicion_siguiente]
            self.lista_materiales[posicion] = fila_2
            self.lista_materiales[posicion_siguiente] = fila_1
        except IndexError:
            return

        self.listCtrl1.SetStringItem(posicion, 0, fila_2[0])
        self.listCtrl1.SetStringItem(posicion, 1, fila_2[1])
        if 'Cámaras de aire' not in fila_2[1]:
            self.listCtrl1.SetStringItem(posicion, 6, str(fila_2[2]))
            self.listCtrl1.SetStringItem(posicion, 3, str(fila_2[3]))
            self.listCtrl1.SetStringItem(posicion, 4, str(fila_2[4]))
            self.listCtrl1.SetStringItem(posicion, 5, str(fila_2[5]))
        else:
            self.listCtrl1.SetStringItem(posicion, 6, '-')
            self.listCtrl1.SetStringItem(posicion, 3, '-')
            self.listCtrl1.SetStringItem(posicion, 4, '-')
            self.listCtrl1.SetStringItem(posicion, 5, '-')
        self.listCtrl1.SetStringItem(posicion, 2, str(round(float(fila_2[3]) / float(fila_2[4]), 3)))
        self.listCtrl1.SetStringItem(posicion_siguiente, 0, fila_1[0])
        self.listCtrl1.SetStringItem(posicion_siguiente, 1, fila_1[1])
        if 'Cámaras de aire' not in fila_1[1]:
            self.listCtrl1.SetStringItem(posicion_siguiente, 6, str(fila_1[2]))
            self.listCtrl1.SetStringItem(posicion_siguiente, 3, str(fila_1[3]))
            self.listCtrl1.SetStringItem(posicion_siguiente, 4, str(fila_1[4]))
            self.listCtrl1.SetStringItem(posicion_siguiente, 5, str(fila_1[5]))
        else:
            self.listCtrl1.SetStringItem(posicion_siguiente, 6, '-')
            self.listCtrl1.SetStringItem(posicion_siguiente, 3, '-')
            self.listCtrl1.SetStringItem(posicion_siguiente, 4, '-')
            self.listCtrl1.SetStringItem(posicion_siguiente, 5, '-')
        self.listCtrl1.SetStringItem(posicion_siguiente, 2, str(round(float(fila_1[3]) / float(fila_1[4]), 3)))
        materiales = []
        espesores = []
        for i in self.lista_materiales:
            materiales.append(i[0])
            espesores.append(float(i[3]))

        imagenes = []
        for i in materiales:
            mat = cargaBD.cargarMaterial(i)
            if mat != []:
                if str(mat[7]) == 'U':
                    imagenes.append(mat[6])
                else:
                    imagenes.append(str(Directorio + '/Imagenes/Fotos_Materiales/' + str(mat[6])))
            else:
                imagenes.append(str(Directorio + '/Imagenes/Fotos_Materiales/defecto.bmp'))

        self.cargaFotoCerramiento(espesores, imagenes)
        self.listCtrl1.SetItemState(posicion, 0, wx.LIST_STATE_SELECTED | wx.LIST_STATE_FOCUSED)
        self.listCtrl1.SetItemState(posicion_siguiente, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)

    def OnGuardarButton(self, event):
        """
        Metodo: OnGuardarButton

        ARGUMENTOS:
                event:
        """
        nombre_cerramiento = str(self.Descripcion.GetValue().encode('iso-8859-15'))
        if nombre_cerramiento == '':
            wx.MessageBox(_('Indique el nombre del cerramiento'), _('Aviso'))
            return
        if self.listCtrl1.GetItemCount() == 0:
            wx.MessageBox(_('No puede crear una composición de cerramiento sin ningún material.'), _('Aviso'))
            return
        cerramiento = []
        cerramiento.append(nombre_cerramiento)
        cerramiento.append(self.transmitancia_global)
        cerramiento.append(self.peso_m2)
        materiales = []
        for i in self.lista_materiales:
            mat = cargaBD.cargarMaterial(i[0])
            material = []
            material.append(str(i[0].encode('cp1252')))
            material.append(i[3])
            material.append(i[4])
            material.append(i[5])
            material.append(i[6])
            if mat != []:
                material.append(mat[6])
                material.append(mat[7])
                material.append(mat[8])
            else:
                material.append('')
                material.append('U')
                material.append(str(i[1].encode('cp1252')))
            materiales.append(material)

        guarda = BDcerramientos.guardar(cerramiento, materiales, DirectorioBD + '/bbdd.dat')
        if guarda:
            pass
        else:
            wx.MessageBox(_('El cerramiento ya existe.'), _('Aviso'))
        self.cargarArbol(self.arbol)

    def OnCerrarButton(self, event):
        """
        Metodo: OnCerrarButton

        ARGUMENTOS:
                event:
        """
        self.Close()

    def OnAnadirButton(self, event):
        """
        Metodo: OnAnadirButton

        ARGUMENTOS:
                event:
        """
        fila_cerr = []
        Grupo = self.GrupoMaterial.GetStringSelection()
        Material = self.Material.GetStringSelection()
        Espesor = self.Espesor.GetValue()
        Conductividad = self.Conductividad.GetValue()
        Densidad = self.Densidad.GetValue()
        Calor = self.Calor.GetValue()
        if ',' in Espesor:
            Espesor = Espesor.replace(',', '.')
        if ',' in Conductividad:
            Conductividad = Conductividad.replace(',', '.')
        if ',' in Densidad:
            Densidad = Densidad.replace(',', '.')
        if ',' in Calor:
            Calor = Calor.replace(',', '.')
        try:
            float(Espesor)
        except (ValueError, TypeError):
            Espesor = ''

        try:
            float(Conductividad)
        except (ValueError, TypeError):
            Conductividad = ''

        try:
            float(Densidad)
        except (ValueError, TypeError):
            Densidad = ''

        try:
            float(Calor)
        except (ValueError, TypeError):
            Calor = ''

        if Espesor != '' and Conductividad != '' and Densidad != '' and Calor != '' and float(Espesor) >= 0 and float(Conductividad) >= 0 and float(Densidad) >= 0 and float(Calor) >= 0 and Grupo != '' and Material != '':
            if 'Cámaras de aire' not in Grupo:
                self.listCtrl1.Append([Material, Grupo, unicode(round(float(Espesor) / float(Conductividad), 3)),
                 Espesor, Conductividad, Densidad, Calor])
            else:
                self.listCtrl1.Append([Material, Grupo, unicode(round(float(Espesor) / float(Conductividad), 3)),
                 '-', '-', '-', '-'])
            fila_cerr.append(Material)
            fila_cerr.append(Grupo)
            try:
                fila_cerr.append(Espesor / Conductividad)
            except:
                logging.info('Excepcion en: %s' % __name__)
                fila_cerr.append('')

            fila_cerr.append(Espesor)
            fila_cerr.append(Conductividad)
            fila_cerr.append(Densidad)
            fila_cerr.append(Calor)
            self.lista_materiales.append(fila_cerr)
        else:
            lista_errores = ''
            if Grupo == '':
                lista_errores = lista_errores + 'grupo de materiales'
            if Material == '':
                if lista_errores != '':
                    lista_errores = lista_errores + ', '
                lista_errores = lista_errores + 'material'
            if Espesor == '' or float(Espesor) < 0:
                if lista_errores != '':
                    lista_errores = lista_errores + ', '
                lista_errores = lista_errores + 'espesor'
            if Conductividad == '' or float(Conductividad) < 0:
                if lista_errores != '':
                    lista_errores = lista_errores + ', '
                lista_errores = lista_errores + 'λ'
            if Densidad == '' or float(Densidad) < 0:
                if lista_errores != '':
                    lista_errores = lista_errores + ', '
                lista_errores = lista_errores + 'ρ'
            if Calor == '' or float(Calor) < 0:
                if lista_errores != '':
                    lista_errores = lista_errores + ', '
                lista_errores = lista_errores + b'calor espec\xedfico'
            wx.MessageBox(_('Revise los siguientes campos:\n') + lista_errores, _('Aviso'))
        self.cambiar_transmitancia_global()
        materiales = []
        espesores = []
        for i in self.lista_materiales:
            materiales.append(i[0])
            espesores.append(float(i[3]))

        imagenes = []
        for i in materiales:
            mat = cargaBD.cargarMaterial(i)
            if mat != []:
                if str(mat[7]) == 'U':
                    imagenes.append(mat[6])
                else:
                    imagenes.append(str(Directorio + '/Imagenes/Fotos_Materiales/' + str(mat[6])))
            else:
                imagenes.append(str(Directorio + '/Imagenes/Fotos_Materiales/defecto.bmp'))

        self.cargaFotoCerramiento(espesores, imagenes)

    def pinchar_listCtrl1(self, event):
        """
        Metodo: pinchar_listCtrl1

        ARGUMENTOS:
                event:
        """
        self.pos_selec = int(event.GetIndex())
        self.longitud_listCtrl = int(self.listCtrl1.GetItemCount())
        fila_cerr = self.lista_materiales[self.pos_selec]
        if fila_cerr[1] not in self.GrupoMaterial.GetItems():
            self.GrupoMaterial.Insert(fila_cerr[1], self.GrupoMaterial.Count - 1)
        self.GrupoMaterial.SetStringSelection(fila_cerr[1])
        grupo = fila_cerr[1]
        mat1 = cargaBD.cargarMateriales(grupo)
        self.opcionesDeGrupo(grupo)
        self.Material.Clear()
        if fila_cerr[0] in mat1:
            self.Material.AppendItems(mat1)
        else:
            self.Material.AppendItems(mat1 + [fila_cerr[0]])
        self.Material.SetStringSelection(fila_cerr[0])
        self.Espesor.SetValue(str(fila_cerr[3]))
        self.Conductividad.SetValue(str(fila_cerr[4]))
        self.Densidad.SetValue(str(fila_cerr[5]))
        self.Calor.SetValue(str(fila_cerr[6]))
        self.resistenciaCamara.SetValue(str(round(float(fila_cerr[3]) / float(fila_cerr[4]), 3)))

    def OnModificarButton(self, event):
        """
        Metodo: OnModificarButton

        ARGUMENTOS:
                event:
        """
        fila_cerr = []
        Grupo = self.GrupoMaterial.GetStringSelection()
        Material = self.Material.GetStringSelection()
        Espesor = self.Espesor.GetValue()
        Conductividad = self.Conductividad.GetValue()
        Densidad = self.Densidad.GetValue()
        Calor = self.Calor.GetValue()
        if ',' in Espesor:
            Espesor = Espesor.replace(',', '.')
        if ',' in Conductividad:
            Conductividad = Conductividad.replace(',', '.')
        if ',' in Densidad:
            Densidad = Densidad.replace(',', '.')
        if ',' in Calor:
            Calor = Calor.replace(',', '.')
        try:
            float(Espesor)
        except (ValueError, TypeError):
            Espesor = ''

        try:
            float(Conductividad)
        except (ValueError, TypeError):
            Conductividad = ''

        try:
            float(Densidad)
        except (ValueError, TypeError):
            Densidad = ''

        try:
            float(Calor)
        except (ValueError, TypeError):
            Calor = ''

        if Espesor != '' and Conductividad != '' and Densidad != '' and Calor != '' and float(Espesor) >= 0 and float(Conductividad) >= 0 and float(Densidad) >= 0 and float(Calor) >= 0 and Grupo != '' and Material != '':
            if 'Cámaras de aire' not in Grupo:
                self.listCtrl1.SetStringItem(self.pos_selec, 0, Material)
                self.listCtrl1.SetStringItem(self.pos_selec, 1, Grupo)
                self.listCtrl1.SetStringItem(self.pos_selec, 2, unicode(round(float(Espesor) / float(Conductividad), 3)))
                self.listCtrl1.SetStringItem(self.pos_selec, 3, Espesor)
                self.listCtrl1.SetStringItem(self.pos_selec, 4, Conductividad)
                self.listCtrl1.SetStringItem(self.pos_selec, 5, Densidad)
                self.listCtrl1.SetStringItem(self.pos_selec, 6, Calor)
            else:
                self.listCtrl1.SetStringItem(self.pos_selec, 0, Material)
                self.listCtrl1.SetStringItem(self.pos_selec, 1, Grupo)
                self.listCtrl1.SetStringItem(self.pos_selec, 2, unicode(round(float(Espesor) / float(Conductividad), 3)))
                self.listCtrl1.SetStringItem(self.pos_selec, 3, '-')
                self.listCtrl1.SetStringItem(self.pos_selec, 4, '-')
                self.listCtrl1.SetStringItem(self.pos_selec, 5, '-')
                self.listCtrl1.SetStringItem(self.pos_selec, 6, '-')
            fila_cerr.append(Material)
            fila_cerr.append(Grupo)
            try:
                fila_cerr.append(Espesor / Conductividad)
            except:
                logging.info('Excepcion en: %s' % __name__)
                fila_cerr.append('')

            fila_cerr.append(Espesor)
            fila_cerr.append(Conductividad)
            fila_cerr.append(Densidad)
            fila_cerr.append(Calor)
            self.lista_materiales[self.pos_selec] = fila_cerr
        else:
            lista_errores = ''
            if Grupo == '':
                lista_errores = lista_errores + 'grupo de material'
            if Material == '':
                if lista_errores != '':
                    lista_errores = lista_errores + ', '
                lista_errores = lista_errores + 'naterial'
            if Espesor == '' or float(Espesor < 0):
                if lista_errores != '':
                    lista_errores = lista_errores + ', '
                lista_errores = lista_errores + 'espesor'
            if Conductividad == '' or float(Conductividad) < 0:
                if lista_errores != '':
                    lista_errores = lista_errores + ', '
                lista_errores = lista_errores + 'λ'
            if Densidad == '' or float(Densidad) < 0:
                if lista_errores != '':
                    lista_errores = lista_errores + ', '
                lista_errores = lista_errores + 'ρ'
            if Calor == '' or float(Calor) < 0:
                if lista_errores != '':
                    lista_errores = lista_errores + ', '
                lista_errores = lista_errores + b'calor espec\xedfico'
            wx.MessageBox(_('Revise los siguientes campos:\n') + lista_errores, _('Aviso'))
        self.cambiar_transmitancia_global()
        materiales = []
        espesores = []
        for i in self.lista_materiales:
            materiales.append(i[0])
            espesores.append(float(i[3]))

        imagenes = []
        for i in materiales:
            mat = cargaBD.cargarMaterial(i)
            if mat != []:
                if str(mat[7]) == 'U':
                    imagenes.append(mat[6])
                else:
                    imagenes.append(str(Directorio + '/Imagenes/Fotos_Materiales/' + str(mat[6])))
            else:
                imagenes.append(str(Directorio + '/Imagenes/Fotos_Materiales/defecto.bmp'))

        self.cargaFotoCerramiento(espesores, imagenes)

    def OnBorrarButton(self, event):
        """
        Metodo: OnBorrarButton

        ARGUMENTOS:
                event:
        """
        try:
            seleccionado = self.listCtrl1.GetFocusedItem()
            if seleccionado == -1:
                wx.MessageBox(_('Seleccione el material de la lista que desea eliminar'), _('Aviso'))
                return
            self.listCtrl1.DeleteItem(seleccionado)
            del self.lista_materiales[seleccionado]
        except:
            wx.MessageBox(_('No hay materiales para eliminar'), _('Aviso'))
            return

        self.cambiar_transmitancia_global()
        materiales = []
        espesores = []
        for i in self.lista_materiales:
            materiales.append(i[0])
            espesores.append(float(i[3]))

        imagenes = []
        for i in materiales:
            mat = cargaBD.cargarMaterial(i)
            if mat != []:
                if str(mat[7]) == 'U':
                    imagenes.append(mat[6])
                else:
                    imagenes.append(str(Directorio + '/Imagenes/Fotos_Materiales/' + str(mat[6])))
            else:
                imagenes.append(str(Directorio + '/Imagenes/Fotos_Materiales/defecto.bmp'))

        self.cargaFotoCerramiento(espesores, imagenes)

    def cambiar_transmitancia_global(self):
        """
        Metodo: cambiar_transmitancia_global

        """
        self.caracteristicas_cerramiento_compuesto = 0
        if self.lista_materiales != []:
            self.caracteristicas_cerramiento_compuesto = self.calculo_cerramiento_compuesto(self.lista_materiales)
            self.transmitancia_global = self.caracteristicas_cerramiento_compuesto[0]
            self.peso_m2 = self.caracteristicas_cerramiento_compuesto[1]
            try:
                self.Transmitancia.SetLabel(str(round(1.0 / float(self.transmitancia_global), 2)))
            except (ValueError, TypeError):
                self.Transmitancia.SetLabel(_('0.0'))

        else:
            self.transmitancia_global = '0.0'
            self.Transmitancia.SetLabel(_('0.0'))

    def calculo_cerramiento_compuesto(self, lista_materiales):
        """
        Metodo: calculo_cerramiento_compuesto

        ARGUMENTOS:
                lista_materiales:
        """
        R = 0
        Peso_m2 = 0
        for i in lista_materiales:
            espesor = float(i[3])
            conductividad = float(i[4])
            densidad = float(i[5])
            R += espesor / conductividad
            if i[1] != 'Cámaras de aire':
                Peso_m2 += densidad * espesor

        Transmitancia = 1 / R
        caracteristicas_cerramiento_compuesto = [
         Transmitancia, Peso_m2]
        return caracteristicas_cerramiento_compuesto