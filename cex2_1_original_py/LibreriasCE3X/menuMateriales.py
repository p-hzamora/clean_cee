# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: LibreriasCE3X\menuMateriales.pyc
# Compiled at: 2015-05-25 19:33:25
"""
Modulo: menuMateriales.py

"""
import wx, os, logging, ElementosConstructivos.cargaBD as cargaBD, Envolvente.dialogoConfirma as dialogoConfirma, directorios
Directorio = directorios.BuscaDirectorios().Directorio

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return Frame1(parent)


wxID_VENTANA, wxID_DESCRIPCIONTEXT, wxID_DESCRIPCION, wxID_GRUPO_MATERIAL_EXISTENTES_TEXT, wxID_GRUPO_MATERIAL_EXISTENTES, wxID_GRUPOMATERIALTEXT, wxID_GRUPOMATERIAL, wxID_ESPESORTEXT, wxID_ESPESOR, wxID_ESPESORUNIDADES, wxID_CONDUCTIVIDADTEXT, wxID_CONDUCTIVIDAD, wxID_CONDUCTIVIDADUNIDADES, wxID_DENSIDADTEXT, wxID_DENSIDAD, wxID_DENSIDADUNIDADES, wxID_CALORTEXT, wxID_CALOR, wxID_CALORUNIDADES, wxID_WXGUARDAR, wxID_WXBORRAR, wxID_FACTORDIFUSIONVAPORTEXT, wxID_FACTORDIFUSIONVAPOR, wxID_FACTORDIFUSIONVAPORUNIDADES = [ wx.NewId() for _init_ctrls in range(24) ]
wxID_FRAME1, wxID_FRAME1BORRARMATERIAL, wxID_FRAME1CALOR, wxID_FRAME1CALORTEXT, wxID_FRAME1CALORUNIDADES, wxID_FRAME1CERRAR, wxID_FRAME1CONDUCTIVIDAD, wxID_FRAME1CONDUCTIVIDADTEXT, wxID_FRAME1CONDUCTIVIDADUNIDADES, wxID_FRAME1DENSIDAD, wxID_FRAME1DENSIDADTEXT, wxID_FRAME1DENSIDADUNIDADES, wxID_FRAME1DESCRIPCION, wxID_FRAME1DESCRIPCIONTEXT, wxID_FRAME1ESPESOR, wxID_FRAME1ESPESORTEXT, wxID_FRAME1ESPESORUNIDADES, wxID_FRAME1GRUPOMATERIAL, wxID_FRAME1GRUPOMATERIALTEXT, wxID_FRAME1GUARDAR, wxID_FRAME1STATICTEXT1, wxID_FRAME1VISTAMATERIALES, wxID_FRAME1BOTON_MODIFICAR, wxID_FRAME1FOTOMATERIAL, wxID_FRAME1CARGARIMAGEN, wxID_FRAME1FACTORVAPORTEXT, wxID_FRAME1FACTORVAPOR, wxID_CAMARAUNIDADES = [ wx.NewId() for _init_ctrls in range(28) ]

class Frame1(wx.Dialog):
    """
    Clase: Frame1 del modulo menuMateriales.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
        """
        wx.Dialog.__init__(self, id=wxID_VENTANA, name='', parent=None, pos=wx.Point(0, 0), size=wx.Size(155, 13), style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN | wx.TAB_TRAVERSAL, title=_('Materiales'))
        self.SetClientSize(wx.Size(770, 487))
        self.SetBackgroundColour('white')
        self.DescripcionText = wx.StaticText(id=wxID_DESCRIPCIONTEXT, label=_('Nombre'), name='DescripcionText', parent=self, pos=wx.Point(235, 86), size=wx.Size(65, 13), style=0)
        self.Descripcion = wx.TextCtrl(id=wxID_DESCRIPCION, name='Nombre', parent=self, pos=wx.Point(304, 82), size=wx.Size(440, 21), style=0, value='')
        self.GrupoMaterialText = wx.StaticText(id=wxID_GRUPOMATERIALTEXT, label=_('Grupo'), name='GrupoText', parent=self, pos=wx.Point(235, 116), size=wx.Size(65, 13), style=0)
        self.GrupoMaterial = wx.TextCtrl(id=wxID_GRUPOMATERIAL, name='GrupoMaterial', parent=self, pos=wx.Point(304, 112), size=wx.Size(440, 21), style=0, value='')
        self.GrupoMaterial.Bind(wx.EVT_TEXT, self.escribiendoGrupoMaterial, id=wxID_GRUPOMATERIAL)
        self.GrupoMaterialTexto_Existente = wx.StaticText(id=wxID_GRUPO_MATERIAL_EXISTENTES_TEXT, label=_('Seleccionar un grupo de materiales existente'), name='Grupo Material Text', parent=self, pos=wx.Point(235, 146), size=wx.Size(240, 13), style=0)
        grupos1 = cargaBD.cargarGrupoCal()
        grupos2 = cargaBD.cargarGrupoUser()
        for i in grupos2:
            grupos1.append(i)

        self.GrupoMaterial_Existente = wx.Choice(choices=grupos1, id=wxID_GRUPO_MATERIAL_EXISTENTES, name='GrupoMaterial', parent=self, pos=wx.Point(480, 144), size=wx.Size(264, 21), style=0)
        self.GrupoMaterial_Existente.Bind(wx.EVT_CHOICE, self.SeleccionarGrupoMaterial, id=wxID_GRUPO_MATERIAL_EXISTENTES)
        self.PropiedadesLinea = wx.StaticBox(id=-1, label=_('Propiedades'), name='PropiedadesLinea', parent=self, pos=wx.Point(220, 176), size=wx.Size(524, 176), style=0)
        self.PropiedadesLinea.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.PropiedadesLinea.SetForegroundColour(wx.Colour(0, 64, 128))
        self.EspesorText = wx.StaticText(id=wxID_ESPESORTEXT, label=_('Espesor'), name='EspesorText', parent=self, pos=wx.Point(235, 206), size=wx.Size(60, 13), style=0)
        self.Espesor = wx.TextCtrl(id=wxID_ESPESOR, name='Espesor', parent=self, pos=wx.Point(304, 204), size=wx.Size(56, 21), style=0, value='')
        self.EspesorUnidades = wx.StaticText(id=wxID_ESPESORUNIDADES, label=_('m'), name='EspesorUnidades', parent=self, pos=wx.Point(365, 206), size=wx.Size(40, 13), style=0)
        self.ConductividadText = wx.StaticText(id=wxID_CONDUCTIVIDADTEXT, label=_('λ'), name='ConductividadText', parent=self, pos=wx.Point(235, 236), size=wx.Size(40, 13), style=0)
        self.Conductividad = wx.TextCtrl(id=wxID_CONDUCTIVIDAD, name='Conductividad', parent=self, pos=wx.Point(304, 234), size=wx.Size(56, 21), style=0, value='')
        self.ConductividadUnidades = wx.StaticText(id=wxID_CONDUCTIVIDADUNIDADES, label=_('W/mK'), name='Densidad', parent=self, pos=wx.Point(365, 236), size=wx.Size(35, 13), style=0)
        self.DensidadText = wx.StaticText(id=wxID_DENSIDADTEXT, label=_('ρ'), name='Unidades', parent=self, pos=wx.Point(235, 266), size=wx.Size(60, 13), style=0)
        self.Densidad = wx.TextCtrl(id=wxID_DENSIDAD, name='Densidad', parent=self, pos=wx.Point(304, 264), size=wx.Size(56, 21), style=0, value='')
        self.DensidadUnidades = wx.StaticText(id=wxID_DENSIDADUNIDADES, label=_('kg/m3'), name='DensidadUnidades', parent=self, pos=wx.Point(365, 266), size=wx.Size(40, 13), style=0)
        self.CalorText = wx.StaticText(id=wxID_CALORTEXT, label=_('Calor específico'), name='CalorText', parent=self, pos=wx.Point(235, 294), size=wx.Size(50, 41), style=0)
        self.Calor = wx.TextCtrl(id=wxID_CALOR, name='Calor', parent=self, pos=wx.Point(304, 294), size=wx.Size(56, 21), style=0, value='')
        self.CalorUnidades = wx.StaticText(id=wxID_CALORUNIDADES, label=_('J/kgK'), name='CalorUnidades', parent=self, pos=wx.Point(365, 296), size=wx.Size(30, 13), style=0)
        self.FactorDifusionVaporText = wx.StaticText(id=wxID_FACTORDIFUSIONVAPORTEXT, label=_('μ'), name='FactorDifusionVaporText', parent=self, pos=wx.Point(235, 326), size=wx.Size(50, 41), style=0)
        self.FactorDifusionVapor = wx.TextCtrl(id=wxID_FACTORDIFUSIONVAPOR, name='FactorDifusionVapor', parent=self, pos=wx.Point(304, 326), size=wx.Size(56, 21), style=0, value='')
        self.FactorDifusionVaporUnidades = wx.StaticText(id=wxID_FACTORDIFUSIONVAPORUNIDADES, label='', name='', parent=self, pos=wx.Point(365, 326), size=wx.Size(30, 13), style=0)
        self.resistenciaCamaraText = wx.StaticText(id=wxID_FRAME1FACTORVAPORTEXT, label=_('R'), name='resistenciaCamaraText', parent=self, pos=wx.Point(235, 206), size=wx.Size(15, 26), style=0)
        self.resistenciaCamara = wx.TextCtrl(id=wxID_FRAME1FACTORVAPOR, name='resistenciaCamara', parent=self, pos=wx.Point(304, 204), size=wx.Size(56, 21), style=0, value='')
        self.resistenciaCamara.SetToolTipString('')
        self.resistenciaCamaraUnidades = wx.StaticText(id=wxID_CAMARAUNIDADES, label=_('m2K/W'), name='CalorUnidades', parent=self, pos=wx.Point(365, 206), size=wx.Size(40, 13), style=0)
        self.resistenciaCamara.Show(False)
        self.resistenciaCamaraText.Show(False)
        self.resistenciaCamaraUnidades.Show(False)
        self.fotoMaterial = wx.Panel(id=wxID_FRAME1FOTOMATERIAL, name='fotoMaterial', parent=self, pos=wx.Point(570, 200), size=wx.Size(152, 100), style=wx.TAB_TRAVERSAL)
        self.fotoMaterial.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.cargarImagen = wx.Button(id=wxID_FRAME1CARGARIMAGEN, label=_('Cargar imagen'), name='cargarImagen', parent=self, pos=wx.Point(583, 322), size=wx.Size(125, 23), style=0)
        self.cargarImagen.Bind(wx.EVT_BUTTON, self.OnCargarImagenButton, id=wxID_FRAME1CARGARIMAGEN)
        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1, label=_('Librería de materiales'), name='staticText1', parent=self, pos=wx.Point(220, 22), size=wx.Size(106, 13), style=0)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.staticText1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.vistaMateriales = wx.TreeCtrl(id=wxID_FRAME1VISTAMATERIALES, name='vistaMateriales', parent=self, pos=wx.Point(8, 15), size=wx.Size(200, 450), style=wx.TR_HAS_BUTTONS)
        self.vistaMateriales.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnVistaMaterialesTreeSelChanged, id=wxID_FRAME1VISTAMATERIALES)
        self.cargarArbol(self.vistaMateriales)
        self.Guardar = wx.Button(id=wxID_WXGUARDAR, label=_('Guardar'), name='Guardar', parent=self, pos=wx.Point(220, 443), size=wx.Size(75, 23), style=0)
        self.Guardar.Bind(wx.EVT_BUTTON, self.OnGuardarButton, id=wxID_WXGUARDAR)
        self.Guardar.SetForegroundColour(wx.Colour(0, 64, 128))
        self.Guardar.SetBackgroundColour('white')
        self.boton_modificar = wx.Button(id=wxID_FRAME1BOTON_MODIFICAR, label=_('Modificar'), name='boton_modificar', parent=self, pos=wx.Point(310, 443), size=wx.Size(75, 23), style=0)
        self.boton_modificar.Bind(wx.EVT_BUTTON, self.OnBoton_modificarButton, id=wxID_FRAME1BOTON_MODIFICAR)
        self.boton_modificar.Enable(False)
        self.boton_modificar.SetForegroundColour(wx.Colour(0, 64, 128))
        self.boton_modificar.SetBackgroundColour('white')
        self.borrarMaterial = wx.Button(id=wxID_FRAME1BORRARMATERIAL, label=_('Borrar'), name='borrarMaterial', parent=self, pos=wx.Point(445, 443), size=wx.Size(75, 23), style=0)
        self.borrarMaterial.Enable(False)
        self.borrarMaterial.Bind(wx.EVT_BUTTON, self.OnBorrarMaterialButton, id=wxID_FRAME1BORRARMATERIAL)
        self.borrarMaterial.SetForegroundColour(wx.Colour(0, 64, 128))
        self.borrarMaterial.SetBackgroundColour('white')
        return

    def __init__(self, parent):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
        """
        self.elementosArbol = []
        self._init_ctrls(parent)
        self.parent = parent
        self.imageFile = ''

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
            self.FactorDifusionVaporText.Show(False)
            self.FactorDifusionVapor.Show(False)
            self.FactorDifusionVaporUnidades.Show(False)
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
            self.FactorDifusionVaporText.Show(True)
            self.FactorDifusionVapor.Show(True)
            self.FactorDifusionVaporUnidades.Show(True)

    def escribiendoGrupoMaterial(self, event):
        """
        Metodo: escribiendoGrupoMaterial

                self,event:
        """
        self.opcionesDeGrupo(self.GrupoMaterial.GetValue())
        self.GrupoMaterial_Existente.SetSelection(-1)

    def SeleccionarGrupoMaterial(self, event):
        """
        Metodo: SeleccionarGrupoMaterial

        ARGUMENTOS:
                event:
        """
        grupo_seleccionado = self.GrupoMaterial_Existente.GetStringSelection()
        self.GrupoMaterial.SetValue(grupo_seleccionado)
        self.GrupoMaterial_Existente.SetStringSelection(grupo_seleccionado)
        self.opcionesDeGrupo(grupo_seleccionado)

    def compruebaDatosEntrada(self, nombre_grupo, resCam, Espesor, Conductividad, Densidad, Calor, FactorDifusionVapor, nombre_cerramiento):
        lista_errores = ''
        if nombre_grupo == 'Cámaras de aire':
            if ',' in resCam:
                resCam = resCam.replace(',', '.')
            try:
                float(resCam)
                if float(resCam) <= 0:
                    resCam = ''
            except (ValueError, TypeError):
                resCam = ''

            if resCam == '':
                if lista_errores != '':
                    lista_errores += ', '
                lista_errores += 'R'
        else:
            if ',' in Espesor:
                Espesor = Espesor.replace(',', '.')
            if ',' in Conductividad:
                Conductividad = Conductividad.replace(',', '.')
            if ',' in Densidad:
                Densidad = Densidad.replace(',', '.')
            if ',' in Calor:
                Calor = Calor.replace(',', '.')
            if ',' in FactorDifusionVapor:
                FactorDifusionVapor = FactorDifusionVapor.replace(',', '.')
            try:
                float(Espesor)
                if float(Espesor) <= 0:
                    Espesor = ''
            except (ValueError, TypeError):
                Espesor = ''

            try:
                float(Conductividad)
                if float(Conductividad) <= 0:
                    Conductividad = ''
            except (ValueError, TypeError):
                Conductividad = ''

            try:
                float(Densidad)
                if float(Densidad) <= 0:
                    Densidad = ''
            except (ValueError, TypeError):
                Densidad = ''

            try:
                float(Calor)
                if float(Calor) <= 0:
                    Calor = ''
            except (ValueError, TypeError):
                Calor = ''

            try:
                float(FactorDifusionVapor)
                if float(FactorDifusionVapor) <= 0:
                    FactorDifusionVapor = ''
            except (ValueError, TypeError):
                FactorDifusionVapor = ''

        if nombre_cerramiento == '':
            lista_errores += 'nombre'
        if nombre_grupo == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'grupo'
        if Espesor == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'espesor'
        if Conductividad == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'λ'
        if Densidad == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'ρ'
        if Calor == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'calor especifico'
        if FactorDifusionVapor == '':
            if lista_errores != '':
                lista_errores += ', '
            lista_errores += 'μ'
        return (nombre_grupo,
         resCam,
         Espesor,
         Conductividad,
         Densidad,
         Calor,
         FactorDifusionVapor,
         nombre_cerramiento,
         lista_errores)

    def OnGuardarButton(self, event):
        """
        Metodo: OnGuardarButton

        ARGUMENTOS:
                event:
        """
        if cargaBD.compruebaMaterial(self.Descripcion.GetValue()) == False:
            nombre_cerramiento = self.Descripcion.GetValue()
            nombre_cerramiento = str(nombre_cerramiento.encode('cp1252'))
            nombre_grupo = self.GrupoMaterial.GetValue()
            Espesor = self.Espesor.GetValue()
            Conductividad = self.Conductividad.GetValue()
            Densidad = self.Densidad.GetValue()
            Calor = self.Calor.GetValue()
            FactorDifusionVapor = self.FactorDifusionVapor.GetValue()
            resCam = self.resistenciaCamara.GetValue()
            imagen = self.imageFile
            nombre_grupo, resCam, Espesor, Conductividad, Densidad, Calor, FactorDifusionVapor, nombre_cerramiento, lista_errores = self.compruebaDatosEntrada(nombre_grupo, resCam, Espesor, Conductividad, Densidad, Calor, FactorDifusionVapor, nombre_cerramiento)
            if imagen == '':
                imagen = Directorio + '/Imagenes/Fotos_Materiales/asfalto.bmp'
            if lista_errores != '':
                wx.MessageBox(_('Revise los siguientes campos:\n') + lista_errores, _('Aviso'))
                return
            if nombre_grupo == 'Cámaras de aire':
                nuevoMaterial = []
                nuevoMaterial.append(self.Descripcion.GetValue())
                nuevoMaterial.append(str(float(resCam) / 100))
                nuevoMaterial.append(str(round(float(resCam) / 100 / float(resCam), 2)))
                nuevoMaterial.append('1')
                nuevoMaterial.append('1')
                nuevoMaterial.append('1')
                nuevoMaterial.append(imagen)
                nuevoMaterial.append('U')
                nuevoMaterial.append(unicode(self.GrupoMaterial.GetValue()))
            else:
                nuevoMaterial = []
                nuevoMaterial.append(self.Descripcion.GetValue())
                nuevoMaterial.append(Espesor)
                nuevoMaterial.append(Conductividad)
                nuevoMaterial.append(Densidad)
                nuevoMaterial.append(Calor)
                nuevoMaterial.append(FactorDifusionVapor)
                nuevoMaterial.append(imagen)
                nuevoMaterial.append('U')
                nuevoMaterial.append(unicode(self.GrupoMaterial.GetValue()))
            cargaBD.nuevoMaterial(nuevoMaterial)
            self.cargarArbol(self.vistaMateriales)
            self.GrupoMaterial_Existente.Clear()
            grupos1 = cargaBD.cargarGrupoCal()
            grupos2 = cargaBD.cargarGrupoUser()
            for i in grupos2:
                grupos1.append(i)

            self.GrupoMaterial_Existente.AppendItems(grupos1)
            self.boton_modificar.Enable(False)
            self.Descripcion.SetValue('')
            self.GrupoMaterial.SetValue('')
            self.Espesor.SetValue('')
            self.Conductividad.SetValue('')
            self.Densidad.SetValue('')
            self.Calor.SetValue('')
            self.FactorDifusionVapor.SetValue('')
            self.resistenciaCamara.SetValue('')
            bmp = wx.Bitmap(Directorio + '/Imagenes/Fotos_Materiales/blanco.bmp')
            wx.StaticBitmap(parent=self.fotoMaterial, id=-1, bitmap=bmp, size=(500,
                                                                               500), pos=(0,
                                                                                          0))
        else:
            wx.MessageBox(_('El nombre del material ya existe, cámbielo para continuar'), _('Aviso'))

    def OnCerrarButton(self, event):
        """
        Metodo: OnCerrarButton

        ARGUMENTOS:
                event:
        """
        self.Close()

    def OnVistaMaterialesTreeSelChanged(self, event):
        """
        Metodo: OnVistaMaterialesTreeSelChanged

        ARGUMENTOS:
                event:
        """
        if self.vistaMateriales.GetItemTextColour(self.vistaMateriales.GetSelection()) == 'grey':
            self.boton_modificar.Enable(True)
            self.borrarMaterial.Enable(True)
        else:
            self.boton_modificar.Enable(False)
            self.borrarMaterial.Enable(False)
        if self.vistaMateriales.GetItemTextColour(self.vistaMateriales.GetSelection()) == 'Black':
            self.boton_modificar.Enable(True)
            self.borrarMaterial.Enable(True)
        if self.vistaMateriales.GetChildrenCount(self.vistaMateriales.GetSelection()) == 0:
            material = []
            prob = self.vistaMateriales.GetItemText(self.vistaMateriales.GetSelection())
            material = cargaBD.cargarMaterial(prob)
            self.opcionesDeGrupo(str(material[8]))
            if material[8] == b'C\xe1maras de aire':
                dato = str(round(float(material[1]) / float(material[2]), 2))
                self.resistenciaCamara.SetValue(dato)
            else:
                self.Espesor.SetValue(str(material[1]))
                self.Conductividad.SetValue(str(material[2]))
                self.Densidad.SetValue(str(material[3]))
                self.Calor.SetValue(str(material[4]))
                self.FactorDifusionVapor.SetValue(str(material[5]))
            self.Descripcion.SetValue(str(material[0]))
            self.GrupoMaterial.SetValue(str(material[8]))
            try:
                if str(material[7]) == 'U':
                    self.imageFile = str(material[6])
                else:
                    self.imageFile = Directorio + '/Imagenes/Fotos_Materiales/' + str(material[6])
                bmp = wx.Bitmap(self.imageFile)
                wx.StaticBitmap(parent=self.fotoMaterial, id=-1, bitmap=bmp, size=(76,
                                                                                   100), pos=(50,
                                                                                              0))
            except:
                wx.MessageBox(_('No se encuentra la imagen del material.'), _('Aviso'))

        else:
            self.boton_modificar.Enable(False)
            self.Descripcion.SetValue('')
            self.GrupoMaterial.SetValue('')
            self.Espesor.SetValue('')
            self.Conductividad.SetValue('')
            self.Densidad.SetValue('')
            self.Calor.SetValue('')
            self.FactorDifusionVapor.SetValue('')
            self.resistenciaCamara.SetValue('')
            bmp = wx.Bitmap(Directorio + '/Imagenes/Fotos_Materiales/blanco.bmp')
            wx.StaticBitmap(parent=self.fotoMaterial, id=-1, bitmap=bmp, size=(500,
                                                                               500), pos=(0,
                                                                                          0))

    def OnBorrarMaterialButton(self, event):
        """
        Metodo: OnBorrarMaterialButton

        ARGUMENTOS:
                event:
        """
        if self.vistaMateriales.GetChildrenCount(self.vistaMateriales.GetSelection()) > 0:
            if self.vistaMateriales.GetItemTextColour(self.vistaMateriales.GetSelection()) == 'Dark green':
                wx.MessageBox(_('No se puede eliminar un grupo de materiales por defecto'), _('Aviso'))
            else:
                borrar = dialogoConfirma.Dialog1(self, '¿Desea borrar el grupo seleccionado?')
                borrar.ShowModal()
                if borrar.dev == False:
                    return
                cargaBD.borraGrupoUser(self.vistaMateriales.GetItemText(self.vistaMateriales.GetSelection()))
                self.vistaMateriales.DeleteChildren(self.vistaMateriales.GetSelection())
                self.vistaMateriales.Delete(self.vistaMateriales.GetSelection())
                self.GrupoMaterial_Existente.Clear()
                grupos1 = cargaBD.cargarGrupoCal()
                grupos2 = cargaBD.cargarGrupoUser()
                for i in grupos2:
                    grupos1.append(i)

                self.GrupoMaterial_Existente.AppendItems(grupos1)
                self.cargarArbol(self.vistaMateriales)
        elif self.vistaMateriales.GetItemTextColour(self.vistaMateriales.GetSelection()) == wx.Colour(100, 200, 0):
            wx.MessageBox(_('No se puede eliminar un material por defecto'), _('Aviso'))
        else:
            borrar = dialogoConfirma.Dialog1(self, '¿Desea borrar el elemento seleccionado?')
            borrar.ShowModal()
            if borrar.dev == False:
                return
            cargaBD.borraMaterialUser(self.vistaMateriales.GetItemText(self.vistaMateriales.GetSelection()))
            self.GrupoMaterial_Existente.Clear()
            grupos1 = cargaBD.cargarGrupoCal()
            grupos2 = cargaBD.cargarGrupoUser()
            for i in grupos2:
                grupos1.append(i)

            self.GrupoMaterial_Existente.AppendItems(grupos1)
            self.cargarArbol(self.vistaMateriales)
        self.boton_modificar.Enable(False)
        self.Descripcion.SetValue('')
        self.GrupoMaterial.SetValue('')
        self.Espesor.SetValue('')
        self.Conductividad.SetValue('')
        self.Densidad.SetValue('')
        self.Calor.SetValue('')
        self.FactorDifusionVapor.SetValue('')
        self.resistenciaCamara.SetValue('')
        bmp = wx.Bitmap(Directorio + '/Imagenes/Fotos_Materiales/blanco.bmp')
        wx.StaticBitmap(parent=self.fotoMaterial, id=-1, bitmap=bmp, size=(500, 500), pos=(0,
                                                                                           0))

    def OnBoton_modificarButton(self, event):
        """
        Metodo: OnBoton_modificarButton

        ARGUMENTOS:
                event:
        """
        nombre_cerramiento = self.Descripcion.GetValue()
        nombre_cerramiento = str(nombre_cerramiento.encode('cp1252'))
        nombre_grupo = self.GrupoMaterial.GetValue()
        Espesor = self.Espesor.GetValue()
        Conductividad = self.Conductividad.GetValue()
        Densidad = self.Densidad.GetValue()
        Calor = self.Calor.GetValue()
        FactorDifusionVapor = self.FactorDifusionVapor.GetValue()
        resCam = self.resistenciaCamara.GetValue()
        imagen = self.imageFile
        nombre_grupo, resCam, Espesor, Conductividad, Densidad, Calor, FactorDifusionVapor, nombre_cerramiento, lista_errores = self.compruebaDatosEntrada(nombre_grupo, resCam, Espesor, Conductividad, Densidad, Calor, FactorDifusionVapor, nombre_cerramiento)
        imagen = ''
        if imagen == '':
            imagen = Directorio + '/Imagenes/Fotos_Materiales/asfalto.bmp'
        if lista_errores != '':
            wx.MessageBox(_('Revise los siguientes campos:\n') + lista_errores, _('Aviso'))
        if lista_errores != '':
            return
        if cargaBD.compruebaMaterial(self.Descripcion.GetValue()) == True and self.Descripcion.GetValue() != self.vistaMateriales.GetItemText(self.vistaMateriales.GetSelection()):
            wx.MessageBox(_('Ya existe un material con el nombre definido.'), _('Aviso'))
            return
        booleano2 = cargaBD.cmpMaterialEnCerra(self.vistaMateriales.GetItemText(self.vistaMateriales.GetSelection()))
        booleano = False
        for i in self.parent.listadoComposicionesCerramientos:
            for j in i.materiales:
                if j[0] == self.vistaMateriales.GetItemText(self.vistaMateriales.GetSelection()):
                    booleano = True
                    break

        if booleano == True and booleano2 == True:
            a = dialogoConfirma.Dialog2(self, 'El material que desea modificar se ha asignado a alguna composición de cerramiento del proyecto y de la base de datos. Esta modificación afectará únicamente a las composiciones de cerramientos de la base de datos. ¿Desea continuar?')
            a.ShowModal()
            if a.dev == False:
                return
        elif booleano == True:
            a = dialogoConfirma.Dialog2(self, 'El material que desea modificar se ha asignado a alguna composición de cerramiento del proyecto. La composición del cerramiento del proyecto no va a ser modificada debiendo ser acutializadamanualmente. ¿Desea continuar?')
            a.ShowModal()
            if a.dev == False:
                return
        elif booleano2 == True:
            a = dialogoConfirma.Dialog2(self, 'El material que desea modificar se ha asignado a alguna composición de cerramiento de la base de datos. La composición del cerramiento de la base de datos va a ser modificada. ¿Desea continuar?')
            a.ShowModal()
            if a.dev == False:
                return
        if nombre_grupo == 'Cámaras de aire':
            nuevoMaterial = []
            nuevoMaterial.append(str(float(resCam) / 100))
            nuevoMaterial.append(str(round(float(resCam) / 100 / float(resCam), 2)))
            nuevoMaterial.append('1')
            nuevoMaterial.append('1')
            nuevoMaterial.append('1')
            nuevoMaterial.append(imagen)
            nuevoMaterial.append('U')
            nuevoMaterial.append(unicode(self.GrupoMaterial.GetValue()))
            nuevoMaterial.append(self.Descripcion.GetValue())
        else:
            nuevoMaterial = []
            nuevoMaterial.append(Espesor)
            nuevoMaterial.append(Conductividad)
            nuevoMaterial.append(Densidad)
            nuevoMaterial.append(Calor)
            nuevoMaterial.append(FactorDifusionVapor)
            nuevoMaterial.append(imagen)
            nuevoMaterial.append('U')
            nuevoMaterial.append(unicode(self.GrupoMaterial.GetValue()))
            nuevoMaterial.append(self.Descripcion.GetValue())
        cargaBD.modificaMaterial(nuevoMaterial, self.vistaMateriales.GetItemText(self.vistaMateriales.GetSelection()))
        if booleano == True:
            for i in range(len(self.parent.listadoComposicionesCerramientos)):
                for j in range(len(self.parent.listadoComposicionesCerramientos[i].materiales)):
                    if self.parent.listadoComposicionesCerramientos[i].materiales[j][0] == self.vistaMateriales.GetItemText(self.vistaMateriales.GetSelection()):
                        self.parent.listadoComposicionesCerramientos[i].materiales[j] = cargaBD.cargarMaterial(self.Descripcion.GetValue())

        self.cargarArbol(self.vistaMateriales)

    def OnCargarImagenButton(self, event):
        """
        Metodo: OnCargarImagenButton

        ARGUMENTOS:
                event:
        """
        tipoArchivo = 'BMP files (*.bmp)|*.bmp|GIF files (*.gif)|*.gif |JPG files (*.jpg)|*.jpg '
        dlg = wx.FileDialog(self, message='Seleccione una foto para el material', defaultDir=Directorio + '/Imagenes/Fotos_Materiales', style=wx.OPEN, wildcard=tipoArchivo)
        if dlg.ShowModal() == wx.ID_OK:
            self.imageFile = dlg.GetPath()
            bmp = wx.Bitmap(self.imageFile)
            wx.StaticBitmap(parent=self.fotoMaterial, id=-1, bitmap=bmp, size=(76,
                                                                               100), pos=(50,
                                                                                          0))

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
        root = arbol.AddRoot('Materiales')
        gruposCal = []
        gruposCal = cargaBD.cargarGrupoCal()
        mat = []
        for i in gruposCal:
            idTree = arbol.AppendItem(root, i)
            self.elementosArbol.append(idTree)
            arbol.SetItemTextColour(idTree, 'Dark green')
            mat = cargaBD.cargarMaterialesCal(i)
            for j in mat:
                it = arbol.AppendItem(idTree, j)
                arbol.SetItemTextColour(it, wx.Colour(100, 200, 0))

            mat = cargaBD.cargarMaterialesUser(i)
            for j in mat:
                it = arbol.AppendItem(idTree, j)
                arbol.SetItemTextColour(it, 'grey')

        gruposUser = []
        gruposUser = cargaBD.cargarGrupoUser()
        for i in gruposUser:
            idTree = arbol.AppendItem(root, i)
            self.elementosArbol.append(idTree)
            arbol.SetItemTextColour(idTree, 'Black')
            mat = cargaBD.cargarMaterialesUser(i)
            for j in mat:
                it = arbol.AppendItem(idTree, j)
                arbol.SetItemTextColour(it, 'grey')

        arbol.Expand(root)
        self.expandirAnteriores(elementosExpandidos, arbol)