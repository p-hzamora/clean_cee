# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: wxFrame1.pyc
# Compiled at: 2015-05-29 14:01:48
"""
Modulo: wxFrame1.py

"""
from Calculos.funcionesCalculo import compararDosConjuntosObjEdificio
from Calculos.funcionesLeerVersionesAnteriores import adaptarVersionesAnterioresArchivo, adaptarVersionesAnterioresMM, adaptarVersionesAnterioresInstalaciones, adaptarVersionesAnterioresInstalacionesConjuntosMM, adaptarVersionesAnterioresEnvolvente
from Calculos.listados import versionCEX, getVersionGuardada, programaVersion, programaVersionExe
from Escala.escalaCalificacion import escalaResidencial
from Informes.creaMMPDF import BorradoInformeMM
from Informes.creaPDF import FuenteAusente, BorradoInformeCertificacion
from MedidasDeMejora.medidasMejoraDefecto import getMedidasPorDefecto
from moduloXML.escribirXML import escribirXML
from panelCalificacion import panelCalificacion
from panelDatosAdministrativos import panelDatosAdministrativos
from panelDatosGenerales import panelDatosGenerales
from panelEnvolvente import panelEnvolvente
from panelInstalaciones import panelInstalaciones
from panelMedidasMejora import panelMedidasMejora
from undo import eventoUndo
from wxNotebook1 import wxNotebook1
import Calculos.calculoPerdidasSombras as calculoPerdidasSombras, ElementosConstructivos.BDcerramientos as BDcerramientos, Envolvente.dialogoConfirma as dialogoConfirma, Envolvente.objetosEnvolvente as objetosEnvolvente, Informes.chequeoInforme as chequeoInforme, Informes.creaMMPDF as creaMMPDF, Informes.creaPDF as creaPDF, LibreriasCE3X.menuCerramientos as menuCerramientos, LibreriasCE3X.menuMarcos as menuMarcos, LibreriasCE3X.menuMateriales as menuMateriales, LibreriasCE3X.menuPT as menuPT, LibreriasCE3X.menuVidrios as menuVidrios, Menus.acercaDe as acercaDe, Menus.asistenciaIdae as asistenciaIdae, PatronesSombra.menuObstaculosRemotos as menuObstaculosRemotos, StringIO, copy, datosEdificio, decoradores, dialogoConfirmaGuardarCambios, directorios, fpformat, idioma, matplotlib, os, panelAnalisisEconomico, pickle, registro, sys, tempfile, tips, undo, ventanaSubgrupo, webbrowser, wx
from reportlab.platypus.doctemplate import LayoutError
idioma.ini()
import logging
Directorio = directorios.BuscaDirectorios().Directorio
DirectorioDoc = directorios.BuscaDirectorios().DirectorioDoc

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return wxFrame1(parent)


wxID_WXFRAME1, wxID_WXFRAME1NOTEBOOK1, wxID_WXFRAME1PANEL1, wxID_WXFRAME1PANEL2, wxID_WXFRAME1PANEL3, wxID_WXFRAME1PANEL4, wxID_WXFRAME1PANEL5 = [ wx.NewId() for _init_ctrls in range(7) ]
wxID_WXFRAME1PANEL6, = [ wx.NewId() for _init_ctrls_panel6 in range(1) ]
wxID_WXFRAME1PANEL7, = [ wx.NewId() for _init_ctrls_panel7 in range(1) ]
wxID_FRAME1MENUFILECLOSE, wxID_FRAME1MENUFILEEXIT, wxID_FRAME1MENUFILEOPEN, wxID_FRAME1MENUFILESAVE, wxID_FRAME1MENUFILESAVEAS, wxID_FRAME1MENUFILENUEVO = [ wx.NewId() for _init_coll_menuFile_Items in range(6) ]
wxID_FRAME1MENUHELPAYUDA, wxID_FRAME1MANUALUSUARIO, wxID_FRAME1MANUALCASOSPRACTICOS, wxID_FRAME1GUIAMEDIDAS, wxID_FRAME1FICHASTOMADATOS, wxID_FRAME1MANUALOBTENCIONDATOS, wxID_FRAME1MENUASISTENCIA, wxID_FRAME1MANUALES = [ wx.NewId() for _init_coll_menuHelp_Items in range(8) ]
wxID_FRAME1MENUHELPABOUT, = [ wx.NewId() for _init_coll_menuAcercaDe_Items in range(1) ]
wxID_FRAME1CALIFICAR, wxID_FRAME1INFORME, wxID_FRAME1MEDIDASDEMEJORA, wxID_FRAME1PRESUPUESTO, wxID_FRAME1ANALISISECONOMICO, wxID_FRAME1ARCHIVOXML = [ wx.NewId() for _init_coll_menuCalificar_Items in range(6) ]
wxID_FRAME1DEFINIRNUEVOSMATERIALES, wxID_FRAME1DEFINIRCERRAMIENTOS, wxID_FRAME1DEFINIRVENTANAS, wxID_FRAME1DEFINIRPT, wxID_FRAME1MARCOS = [ wx.NewId() for _init_coll_menuLibrerias_Items in range(5) ]
wxID_FRAME1DEFINIROBSTACULOS, = [ wx.NewId() for _init_coll_menuObstaculosRemotos_Items in range(1) ]
ID_TOOLBAR = wx.NewId()
ID_BOTON_ABRIR = wx.NewId()
ID_BOTON_NUEVO = wx.NewId()
ID_BOTON_GUARDAR = wx.NewId()
ID_BOTON_EJECUTAR = wx.NewId()
ID_BOTON_INFORME = wx.NewId()
ID_BOTON_ARCHIVOXML = wx.NewId()
ID_BOTON_MEJORA = wx.NewId()
ID_BOTON_ECONOMICO = wx.NewId()
ID_BOTON_SOMBRAS = wx.NewId()
ID_BOTON_UNDO = wx.NewId()
ID_BOTON_REDO = wx.NewId()

class wxFrame1(wx.Frame):
    """
    Clase: wxFrame1 del modulo wxFrame1.py

    """

    def __init__(self, parent):
        """
        Constructor de la clase

        ARGUMENTOS:
             parent:
        """
        self.objEdificio = None
        self.listadoConjuntosMMUsuario = []
        self.listadoConjuntosMMPorDefecto = []
        self.diccInformacionExtra = {}
        self.esEdificioExistente = True
        self.programa = 'Residencial'
        self.version = versionCEX
        self.versionArchivoGuardado = ''
        idioma.ini()
        self._init_ctrls(parent)
        _icon = wx.Icon(Directorio + '/Imagenes/logoCex.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(_icon)
        self.filename = None
        self.libreriaVidriosMarcos = []
        self.datosSombras = []
        self.nuevoListadoSombras = [('Sin patrón', _('Sin patrón'))]
        self.configuracionInforme = []
        self.pilaUndo = undo.undoManaggement()
        self.pilaRedo = undo.undoManaggement()
        self.pilaUndo.pila = [undo.EventoInicial()]
        self.pilaRedo.pila = [undo.EventoInicial()]
        self.listadoComposicionesCerramientos = []
        self.escala = escalaResidencial()
        self._init_coll_menuComplementos_Items(self.menuComplementos)
        return

    def cogerPlugins(self):
        """
        Metodo: cogerPlugins

                self):   ###Funcion que coje los plugins que haya en la carpeta Plugi:
        """
        fich = []
        for i in os.listdir(Directorio + '\\Plugins'):
            nombre = i.split('.')
            try:
                if nombre[1] == 'py':
                    fich.append(str(nombre[0]))
            except:
                pass

            try:
                if nombre[1] == 'pyc' and nombre[0] not in fich:
                    fich.append(str(nombre[0]))
            except:
                pass

            try:
                if nombre[1] == 'pyd' and nombre[0] not in fich:
                    fich.append(str(nombre[0]))
            except:
                pass

        sys.path.append(Directorio + '\\Plugins')
        return fich

    def _init_coll_menuBar1_Menus(self, parent):
        """
        Metodo: _init_coll_menuBar1_Menus

        ARGUMENTOS:
                 parent:
        """
        parent.Append(menu=self.menuFile, title=_('Archivo'))
        parent.Append(menu=self.menuLibrerias, title=_('Librerías'))
        parent.Append(menu=self.menuObstaculosRemotos, title=_('Patrones de sombra'))
        parent.Append(menu=self.menuCalificar, title=_('Resultados'))
        parent.Append(menu=self.menuComplementos, title=_('Complementos'))
        parent.Append(menu=self.menuHelp, title=_('Ayuda'))
        parent.Append(menu=self.menuAcercaDe, title=_('Acerca de'))

    def _init_coll_menuHelp_Items(self, parent):
        """
        Metodo: _init_coll_menuHelp_Items

        ARGUMENTOS:
                 parent:
        """
        parent.Append(help=_('Asistencia técnica y consultas'), id=wxID_FRAME1MENUASISTENCIA, kind=wx.ITEM_NORMAL, text=_('Asistencia técnica y consultas'))
        self.Bind(wx.EVT_MENU, self.OnMenuHelpAsistenciaMenu, id=wxID_FRAME1MENUASISTENCIA)
        parent.AppendSeparator()
        parent.Append(help=_('Manual de usuario'), id=wxID_FRAME1MANUALUSUARIO, kind=wx.ITEM_NORMAL, text=_('Manual de usuario'))
        self.Bind(wx.EVT_MENU, self.OnManualUsuario, id=wxID_FRAME1MANUALUSUARIO)
        parent.Append(help=_('Manual de medidas de mejora'), id=wxID_FRAME1GUIAMEDIDAS, kind=wx.ITEM_NORMAL, text=_('Manual de medidas de mejora'))
        self.Bind(wx.EVT_MENU, self.OnGuiaMedidasMejora, id=wxID_FRAME1GUIAMEDIDAS)
        parent.Append(help=_('Manual de fundamentos técnicos'), id=wxID_FRAME1MANUALOBTENCIONDATOS, kind=wx.ITEM_NORMAL, text=_('Manual de fundamentos técnicos'))
        self.Bind(wx.EVT_MENU, self.OnManualObtencionDatos, id=wxID_FRAME1MANUALOBTENCIONDATOS)

    def _init_coll_menuAcercaDe_Items(self, parent):
        """
        Metodo: _init_coll_menuAcercaDe_Items
        ARGUMENTOS:
                 parent:
        """
        parent.Append(help=_('Muestra información general'), id=wxID_FRAME1MENUHELPABOUT, kind=wx.ITEM_NORMAL, text=_('Acerca de'))
        self.Bind(wx.EVT_MENU, self.OnMenuHelpAboutMenu, id=wxID_FRAME1MENUHELPABOUT)

    def _init_coll_menuFile_Items(self, parent):
        """
        Metodo: _init_coll_menuFile_Items

        ARGUMENTOS:
                 parent:
        """
        nuevo = wx.MenuItem(parent, wxID_FRAME1MENUFILENUEVO, _('&Nuevo\tCtrl+N'))
        nuevo.SetBitmap(wx.Bitmap(Directorio + '//Imagenes//nuevoPeque.png'))
        nuevo.SetHelp(_('Borra todos los campos para empezar un proyecto nuevo.'))
        parent.AppendItem(nuevo)
        abrir = wx.MenuItem(parent, wxID_FRAME1MENUFILEOPEN, _('&Abrir\tCtrl+A'))
        abrir.SetBitmap(wx.Bitmap(Directorio + '//Imagenes//AbrirPeque.png'))
        abrir.SetHelp(_('Cierra el proyecto actual y abre otro desde un archivo.'))
        parent.AppendItem(abrir)
        guardar = wx.MenuItem(parent, wxID_FRAME1MENUFILESAVE, _('&Guardar\tCtrl+G'))
        guardar.SetBitmap(wx.Bitmap(Directorio + '//Imagenes//GuardarPeque.png'))
        guardar.SetHelp(_('Guarda el proyecto actual en un archivo.'))
        parent.AppendItem(guardar)
        parent.Append(help=_('Guardar archivo como'), id=wxID_FRAME1MENUFILESAVEAS, kind=wx.ITEM_NORMAL, text=_('Guardar como'))
        self.submenuIdioma = wx.Menu()
        for i in os.listdir(Directorio + '/locale'):
            ide = wx.NewId()
            self.submenuIdioma.Append(ide, str(i))
            self.Bind(wx.EVT_MENU, self.idiomasMenu, id=ide)

        parent.AppendMenu(id=-1, submenu=self.submenuIdioma, text=_('Idioma'))
        parent.Append(help=_('Cierra el programa'), id=wxID_FRAME1MENUFILEEXIT, kind=wx.ITEM_NORMAL, text=_('Salir'))
        self.history = wx.FileHistory(8)
        a = registro.leerFicherosRecientes()
        a.reverse()
        for i in a:
            if i != '':
                self.history.AddFileToHistory(i)

        self.history.UseMenu(parent)
        self.history.AddFilesToMenu()
        self.Bind(wx.EVT_MENU, self.OnMenuFileOpenMenu, id=wxID_FRAME1MENUFILEOPEN)
        self.Bind(wx.EVT_MENU, self.OnMenuFileOpenNuevo, id=wxID_FRAME1MENUFILENUEVO)
        self.Bind(wx.EVT_MENU, self.OnMenuFileSaveMenu, id=wxID_FRAME1MENUFILESAVE)
        self.Bind(wx.EVT_MENU, self.OnMenuFileSaveasMenu, id=wxID_FRAME1MENUFILESAVEAS)
        self.Bind(wx.EVT_MENU_RANGE, self.on_file_history, id=wx.ID_FILE1, id2=wx.ID_FILE9)
        self.Bind(wx.EVT_MENU, self.OnMenuFileExitMenu, id=wxID_FRAME1MENUFILEEXIT)
        self.Bind(wx.EVT_CLOSE, self.OnMenuFileExitMenu)

    def idiomasMenu(self, event):
        """
        Metodo: idiomasMenu

        ARGUMENTOS:
                event:
        """
        it = self.submenuIdioma.GetLabel(event.GetId())
        if it != registro.leerIdioma():
            registro.editarIdioma(it)
            wx.MessageBox(_('Necesario reiniciar la aplicación para aplicar los cambios'))

    def on_file_history(self, event):
        """
        Metodo: on_file_history

        ARGUMENTOS:
                 event:
        """
        fileNum = event.GetId() - wx.ID_FILE1
        path = self.history.GetHistoryFile(fileNum)
        self.abreArchivoDirecto(path.replace('\n', ''))

    def _init_coll_menuLibrerias_Items(self, parent):
        """
        Metodo: _init_coll_menuLibrerias_Items

        ARGUMENTOS:
                parent:
        """
        materiales = wx.MenuItem(parent, wxID_FRAME1DEFINIRNUEVOSMATERIALES, _('Materiales'))
        materiales.SetBitmap(wx.Bitmap(Directorio + '/Imagenes/materiales.ico'))
        materiales.SetHelp(_('Librería de materiales'))
        parent.AppendItem(materiales)
        self.Bind(wx.EVT_MENU, self.DefinirNuevoMaterial, id=wxID_FRAME1DEFINIRNUEVOSMATERIALES)
        cerramientos = wx.MenuItem(parent, wxID_FRAME1DEFINIRCERRAMIENTOS, _('Cerramientos'))
        cerramientos.SetBitmap(wx.Bitmap(Directorio + '/Imagenes/cerramientos.ico'))
        cerramientos.SetHelp(_('Definir composición cerramientos'))
        parent.AppendItem(cerramientos)
        self.Bind(wx.EVT_MENU, self.DefinirComposicionCerramientos, id=wxID_FRAME1DEFINIRCERRAMIENTOS)
        vidrios = wx.MenuItem(parent, wxID_FRAME1DEFINIRVENTANAS, _('Vidrios'))
        vidrios.SetBitmap(wx.Bitmap(Directorio + '/Imagenes/ventana.ico'))
        vidrios.SetHelp(_('Librería de vidrios'))
        parent.AppendItem(vidrios)
        self.Bind(wx.EVT_MENU, self.DefinirVentanas, id=wxID_FRAME1DEFINIRVENTANAS)
        marcos = wx.MenuItem(parent, wxID_FRAME1MARCOS, _('Marcos'))
        marcos.SetBitmap(wx.Bitmap(Directorio + '/Imagenes/marco.ico'))
        marcos.SetHelp(_('Librería de  marcos'))
        parent.AppendItem(marcos)
        self.Bind(wx.EVT_MENU, self.DefinirMarcos, id=wxID_FRAME1MARCOS)
        puentes = wx.MenuItem(parent, wxID_FRAME1DEFINIRPT, _('Puentes térmicos'))
        puentes.SetBitmap(wx.Bitmap(Directorio + '/Imagenes/pt.ico'))
        puentes.SetHelp(_('Librería de Puentes Térmicos'))
        parent.AppendItem(puentes)
        self.Bind(wx.EVT_MENU, self.DefinirPT, id=wxID_FRAME1DEFINIRPT)

    def _init_coll_menuObstaculosRemotos_Items(self, parent):
        """
        Metodo: _init_coll_menuObstaculosRemotos_Items

        ARGUMENTOS:
                parent:
        """
        sombras = wx.MenuItem(parent, wxID_FRAME1DEFINIROBSTACULOS, _('&Patrones de sombra\tCtrl+O'))
        sombras.SetBitmap(wx.Bitmap(Directorio + '/Imagenes/sombrasPeque.png'))
        sombras.SetHelp(_('Definición de los perfiles de sombra.'))
        parent.AppendItem(sombras)
        self.Bind(wx.EVT_MENU, self.DefinirObstaculosRemotos, id=wxID_FRAME1DEFINIROBSTACULOS)

    def _init_coll_menuCalificar_Items(self, parent):
        """
        Metodo: _init_coll_menuCalificar_Items

        ARGUMENTOS:
                 parent:
        """
        calificar = wx.MenuItem(parent, wxID_FRAME1CALIFICAR, _('&Calificar\tCtrl+Q'))
        calificar.SetBitmap(wx.Bitmap(Directorio + '/Imagenes/calificarPeque.png'))
        calificar.SetHelp(_('Calificación del edificio.'))
        parent.AppendItem(calificar)
        self.Bind(wx.EVT_MENU, self.OnMenuCalificar, id=wxID_FRAME1CALIFICAR)
        mejora = wx.MenuItem(parent, wxID_FRAME1MEDIDASDEMEJORA, _('&Medidas de mejora\tCtrl+M'))
        mejora.SetBitmap(wx.Bitmap(Directorio + '/Imagenes/mejoraPeque.png'))
        mejora.SetHelp(_('Definición de las medidas de mejora.'))
        parent.AppendItem(mejora)
        self.Bind(wx.EVT_MENU, self.OnMedidasDeMejora, id=wxID_FRAME1MEDIDASDEMEJORA)
        economico = wx.MenuItem(parent, wxID_FRAME1ANALISISECONOMICO, _('Análisis &económico\tCtrl+E'))
        economico.SetBitmap(wx.Bitmap(Directorio + '/Imagenes/euroPeque.png'))
        economico.SetHelp(_('Análisis económico de las medidas de mejora.'))
        parent.AppendItem(economico)
        self.Bind(wx.EVT_MENU, self.OnAnalisisEconomico, id=wxID_FRAME1ANALISISECONOMICO)
        informe = wx.MenuItem(parent, wxID_FRAME1INFORME, _('&Informe\tCtrl+I'))
        informe.SetBitmap(wx.Bitmap(Directorio + '/Imagenes/informePeque.png'))
        informe.SetHelp(_('Generación del informe.'))
        parent.AppendItem(informe)
        self.Bind(wx.EVT_MENU, self.OnGenerarInforme, id=wxID_FRAME1INFORME)
        archivoXML = wx.MenuItem(parent, wxID_FRAME1ARCHIVOXML, _('&ArchivoXML para registro\tCtrl+J'))
        archivoXML.SetBitmap(wx.Bitmap(Directorio + '/Imagenes/archivoXMLPeque.png'))
        archivoXML.SetHelp(_('Generación archivo .xml para el registro en el órgano competente de la CCAA correspondiente.'))
        parent.AppendItem(archivoXML)
        self.Bind(wx.EVT_MENU, self.OnGenerarArchivoXML, id=wxID_FRAME1ARCHIVOXML)

    def _init_coll_menuComplementos_Items(self, parent):
        """
        Metodo: _init_coll_menuComplementos_Items

        ARGUMENTOS:
             parent:
        """
        plugs = []
        plugs = self.cogerPlugins()
        if plugs == []:
            vacio = wx.MenuItem(parent, -1, _('(vacio)'))
            vacio.Enable(False)
            parent.AppendItem(vacio)
        else:
            objetos = []
            nombres = []
            for i in range(len(plugs)):
                try:
                    objetos.append(__import__(plugs[i]))
                    nombres.append(plugs[i])
                except:
                    wx.MessageBox(_('Error al cargar el complemento: ') + plugs[i], _('Aviso'))

            if objetos == []:
                vacio = wx.MenuItem(parent, -1, _('(vacio)'))
                vacio.Enable(False)
                parent.AppendItem(vacio)
            else:
                for i in range(len(objetos)):
                    objetos[i] = objetos[i].create(self)

                for i in range(len(objetos)):
                    try:
                        parent.AppendMenu(id=-1, text=nombres[i], submenu=objetos[i].menuit)
                    except:
                        logging.info('No se han añadido complementos al menu.')

    def _init_coll_notebook1_Pages(self, parent):
        """
        Metodo: _init_coll_notebook1_Pages

        ARGUMENTOS:
                 parent:
        """
        self.panelDatosAdministrativos = panelDatosAdministrativos(parent=parent, id=-1, pos=self.posicion_defecto, size=self.tamano_defecto, style=0, name='panelDatosAdministrativos')
        self.panelDatosGenerales = panelDatosGenerales(parent=self.notebook1, id=-1, pos=self.posicion_defecto, size=self.tamano_defecto, style=0, name='panelDatosGenerales')
        self.panelEnvolvente = panelEnvolvente(parent=self.notebook1, id=-1, pos=self.posicion_defecto, size=self.tamano_defecto, style=0, name='panelEnvolvente')
        self.panelInstalaciones = panelInstalaciones(parent=self.notebook1, id=-1, pos=self.posicion_defecto, size=self.tamano_defecto, style=0, name='panelInstalaciones')
        self.panelMedidasMejora = panelMedidasMejora(parent=self.notebook1, id=wx.NewId(), pos=self.posicion_defecto, size=self.tamano_defecto, style=0, name='panelMedidasMejora')
        self.panelMedidasMejora.Show(False)
        self.panelAnalisisEconomico = panelAnalisisEconomico.Panel1(parent=self.notebook1, id=wx.NewId(), pos=self.posicion_defecto, size=self.tamano_defecto, style=0, name='panelAnalisisEconomico')
        self.panelAnalisisEconomico.Show(False)
        self.paneles = []
        self.paneles.append(self.panelDatosAdministrativos)
        self.paneles.append(self.panelDatosGenerales)
        self.paneles.append(self.panelEnvolvente)
        self.paneles.append(self.panelInstalaciones)
        self.notebook1.iniciaPaneles(self.paneles, self.notebook1)
        self.notebook1.SetSelection(0)

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                 prnt:
        """
        self.tamano_defecto = wx.Size(1000, 775)
        self.posicion_defecto = wx.Point(0, 0)
        self.datosSombras = []
        self.nuevoListadoSombras = [
         (
          'Sin patrón', _('Sin patrón'))]
        self.listadoCerramientos = []
        wx.Frame.__init__(self, id=wxID_WXFRAME1, name='', parent=prnt, pos=self.posicion_defecto, size=self.tamano_defecto, style=wx.DEFAULT_FRAME_STYLE, title=_('CE3X - RES: Certificación energética simplificada de edificios existentes - Residencial'))
        self._init_utils()
        self.SetMenuBar(self.menuBar1)
        self.notebook1 = wxNotebook1(id=wxID_WXFRAME1NOTEBOOK1, name='notebook1', parent=self, pos=self.posicion_defecto, size=self.tamano_defecto, style=0)
        self.paneles = []
        self._init_coll_notebook1_Pages(self.notebook1)
        tb = self.CreateToolBar(wx.TB_HORIZONTAL | wx.BORDER)
        self.ToolBar = tb
        tb.SetToolBitmapSize((32, 32))
        imageNuevo = Directorio + '/Imagenes/nuevo.png'
        imageNuevo1 = wx.Image(imageNuevo, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        botonNuevo = wx.BitmapButton(tb, ID_BOTON_NUEVO, imageNuevo1, wx.DefaultPosition, wx.Size(-1, -1), style=wx.BU_AUTODRAW)
        botonNuevo.SetToolTip(wx.ToolTip(_('Borra todos los campos para comenzar con un proyecto nuevo')))
        tb.AddControl(botonNuevo)
        wx.EVT_BUTTON(self, ID_BOTON_NUEVO, self.OnMenuFileOpenNuevo)
        imageAbrir = Directorio + '/Imagenes/abrir.png'
        imageAbrir1 = wx.Image(imageAbrir, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        botonAbrir = wx.BitmapButton(tb, ID_BOTON_ABRIR, imageAbrir1, wx.DefaultPosition, wx.Size(-1, -1), style=wx.BU_AUTODRAW)
        botonAbrir.SetToolTip(wx.ToolTip(_('Cargar un proyecto desde un archivo')))
        tb.AddControl(botonAbrir)
        wx.EVT_BUTTON(self, ID_BOTON_ABRIR, self.OnMenuFileOpenMenu)
        imageGuardar = Directorio + '/Imagenes/guardar.png'
        imageGuardar1 = wx.Image(imageGuardar, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        botonGuardar = wx.BitmapButton(tb, ID_BOTON_GUARDAR, imageGuardar1, wx.DefaultPosition, wx.Size(-1, -1), style=wx.BU_AUTODRAW)
        botonGuardar.SetToolTip(wx.ToolTip(_('Guarda en un archivo el proyecto actual')))
        tb.AddControl(botonGuardar)
        wx.EVT_BUTTON(self, ID_BOTON_GUARDAR, self.OnMenuFileSaveMenu)
        imageUndo = Directorio + '/Imagenes/Undo.png'
        imageUndo1 = wx.Image(imageUndo, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        botonUndo = wx.BitmapButton(tb, ID_BOTON_UNDO, imageUndo1, wx.DefaultPosition, wx.Size(-1, -1), style=wx.BU_AUTODRAW)
        botonUndo.SetToolTip(wx.ToolTip(_('Deshacer')))
        tb.AddControl(botonUndo)
        wx.EVT_BUTTON(self, ID_BOTON_UNDO, self.deshacerUltimoPaso)
        imageRedo = Directorio + '/Imagenes/Redo.png'
        imageRedo1 = wx.Image(imageRedo, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        botonRedo = wx.BitmapButton(tb, ID_BOTON_REDO, imageRedo1, wx.DefaultPosition, wx.Size(-1, -1), style=wx.BU_AUTODRAW)
        botonRedo.SetToolTip(wx.ToolTip(_('Rehacer')))
        tb.AddControl(botonRedo)
        wx.EVT_BUTTON(self, ID_BOTON_REDO, self.rehacerUltimoPaso)
        tb.AddSeparator()
        tb.AddSeparator()
        imageSombras = Directorio + '/Imagenes/sombras.png'
        imageSombras1 = wx.Image(imageSombras, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        botonSombras = wx.BitmapButton(tb, ID_BOTON_SOMBRAS, imageSombras1, wx.DefaultPosition, wx.Size(-1, -1), style=wx.BU_AUTODRAW)
        botonSombras.SetToolTip(wx.ToolTip(_('Definición sombras')))
        tb.AddControl(botonSombras)
        wx.EVT_BUTTON(self, ID_BOTON_SOMBRAS, self.DefinirObstaculosRemotos)
        tb.AddSeparator()
        tb.AddSeparator()
        imageEjecutar = Directorio + '/Imagenes/calificar.png'
        imageEjecutar1 = wx.Image(imageEjecutar, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        botonCalificar = wx.BitmapButton(tb, ID_BOTON_EJECUTAR, imageEjecutar1, wx.DefaultPosition, wx.Size(-1, -1), style=wx.BU_AUTODRAW)
        botonCalificar.SetToolTip(wx.ToolTip(_('Califica el proyecto')))
        tb.AddControl(botonCalificar)
        wx.EVT_BUTTON(self, ID_BOTON_EJECUTAR, self.OnMenuCalificar)
        imageMejora = Directorio + '/Imagenes/mejora.png'
        imageMejora1 = wx.Image(imageMejora, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.botonMejoras11 = wx.BitmapButton(tb, ID_BOTON_MEJORA, imageMejora1, wx.DefaultPosition, wx.Size(-1, -1), style=wx.BU_AUTODRAW)
        self.botonMejoras11.SetToolTip(wx.ToolTip(_('Medidas de mejora')))
        tb.AddControl(self.botonMejoras11)
        wx.EVT_BUTTON(self, ID_BOTON_MEJORA, self.OnMedidasDeMejora)
        imageEconomico = Directorio + '/Imagenes/euro.png'
        imageEconomico1 = wx.Image(imageEconomico, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.botonEconomico11 = wx.BitmapButton(tb, ID_BOTON_ECONOMICO, imageEconomico1, wx.DefaultPosition, wx.Size(-1, -1), style=wx.BU_AUTODRAW)
        self.botonEconomico11.SetToolTip(wx.ToolTip(_('Análisis Económico')))
        tb.AddControl(self.botonEconomico11)
        wx.EVT_BUTTON(self, ID_BOTON_ECONOMICO, self.OnAnalisisEconomico)
        imageInforme = Directorio + '/Imagenes/informe.png'
        imageInforme1 = wx.Image(imageInforme, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        botonInforme = wx.BitmapButton(tb, ID_BOTON_INFORME, imageInforme1, wx.DefaultPosition, wx.Size(-1, -1), style=wx.BU_AUTODRAW)
        botonInforme.SetToolTip(wx.ToolTip(_('Genera el informe del proyecto')))
        tb.AddControl(botonInforme)
        wx.EVT_BUTTON(self, ID_BOTON_INFORME, self.OnGenerarInforme)
        imageArchivoXML = Directorio + '/Imagenes/archivoXML.png'
        imageArchivoXML1 = wx.Image(imageArchivoXML, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        botonArchivoXML = wx.BitmapButton(tb, ID_BOTON_ARCHIVOXML, imageArchivoXML1, wx.DefaultPosition, wx.Size(-1, -1), style=wx.BU_AUTODRAW)
        botonArchivoXML.SetToolTip(wx.ToolTip(_('Genera el archivo .xml para el registro en el órgano competente de la CCAA correspondiente')))
        tb.AddControl(botonArchivoXML)
        wx.EVT_BUTTON(self, ID_BOTON_ARCHIVOXML, self.OnGenerarArchivoXML)
        tb.Realize()
        self.sb = self.CreateStatusBar()
        tips.tips(self)

    def _init_utils(self):
        """
        Metodo: _init_utils

        """
        self.menuFile = wx.Menu(title='')
        self.menuHelp = wx.Menu(title='')
        self.menuCalificar = wx.Menu(title='')
        self.menuLibrerias = wx.Menu(title='')
        self.menuObstaculosRemotos = wx.Menu(title='')
        self.menuComplementos = wx.Menu(title='')
        self.menuBar1 = wx.MenuBar()
        self.menuAcercaDe = wx.Menu(title='')
        self._init_coll_menuFile_Items(self.menuFile)
        self._init_coll_menuLibrerias_Items(self.menuLibrerias)
        self._init_coll_menuObstaculosRemotos_Items(self.menuObstaculosRemotos)
        self._init_coll_menuCalificar_Items(self.menuCalificar)
        self._init_coll_menuHelp_Items(self.menuHelp)
        self._init_coll_menuAcercaDe_Items(self.menuAcercaDe)
        self._init_coll_menuBar1_Menus(self.menuBar1)

    def OnManuales(self, event):
        """
        Metodo: OnManuales

        ARGUMENTOS:
                event:
        """
        webbrowser.open_new('http://www.minetur.gob.es/energia/desarrollo/EficienciaEnergetica/CertificacionEnergetica/DocumentosReconocidos/Paginas/Procedimientossimplificadosparaedificiosexistentes.aspx')

    def OnManualUsuario(self, event):
        """
        Metodo: OnManualUsuario

        ARGUMENTOS:
                event:
        """
        try:
            rutaArchivo = os.path.join(DirectorioDoc, 'Manuales', '1.- Manual de usuario CE³X_Enero2015.pdf')
            os.startfile(rutaArchivo)
        except:
            wx.MessageBox(_('El documento solicitado no puede abrirse. Es posible que no haya instalado los manuales de la aplicación.Reinstalando el programa se solucionará el problema'), _('Aviso'))

    def OnGuiaMedidasMejora(self, event):
        """
        Metodo: OnGuiaMedidasMejora

        ARGUMENTOS:
                event:
        """
        try:
            rutaArchivo = os.path.join(DirectorioDoc, 'Manuales', '3.- Manual medidas de mejora CE³X_Enero2015.pdf')
            os.startfile(rutaArchivo)
        except:
            wx.MessageBox(_('El documento solicitado no puede abrirse. Es posible que no haya instalado los manuales de la aplicación.Reinstalando el programa se solucionará el problema'), _('Aviso'))

    def OnManualObtencionDatos(self, event):
        """
        Metodo: OnManualObtencionDatos

        ARGUMENTOS:
                event:
        """
        try:
            rutaArchivo = os.path.join(DirectorioDoc, 'Manuales', '2.- Manual fundamentos técnicos CE³X_Enero2015.pdf')
            os.startfile(rutaArchivo)
        except:
            wx.MessageBox(_('El documento solicitado no puede abrirse. Es posible que no haya instalado los manuales de la aplicación.Reinstalando el programa se solucionará el problema'), _('Aviso'))

    def OnMenuHelpAboutMenu(self, event):
        dlg = acercaDe.create(self)
        dlg.ShowModal()

    def OnMenuHelpAsistenciaMenu(self, event):
        dlg = asistenciaIdae.create(self)
        dlg.ShowModal()

    def deshacerUltimoPaso(self, event):
        """
        Metodo: deshacerUltimoPaso

        ARGUMENTOS:
                event:
        """
        try:
            a = self.pilaUndo.desempilar()
        except:
            self.pilaUndo.pila = [
             undo.EventoInicial()]
            wx.MessageBox(_('No hay pasos que deshacer.'), _('Aviso'))
            return

        if a.miniEventos.pila == []:
            if a.accion == 'inicioPila':
                self.pilaUndo.apilar(a)
                wx.MessageBox(_('No hay pasos que deshacer.'), _('Aviso'))
            else:
                a.contraEvento(0)
        elif len(a.miniEventos.pila) == 1:
            if a.miniEventos.pila[0].accion == 'inicioPila':
                if a.accion == 'inicioPila':
                    self.pilaUndo.apilar(a)
                    wx.MessageBox(_('No hay pasos que deshacer.'), _('Aviso'))
                else:
                    a.contraEvento(0)
            else:
                miniEvt = a.miniEventos.desempilar()
                self.pilaUndo.apilar(a)
                miniEvt.contraEvento(0)
        else:
            miniEvt = a.miniEventos.desempilar()
            self.pilaUndo.apilar(a)
            miniEvt.contraEvento(0)

    def rehacerUltimoPaso(self, event):
        """
        Metodo: rehacerUltimoPaso

        ARGUMENTOS:
                event:
        """
        try:
            a = self.pilaRedo.desempilar()
        except:
            self.pilaRedo.pila = [
             undo.EventoInicial()]
            wx.MessageBox(_('No hay pasos que rehacer.'), _('Aviso'))
            return

        if a.miniEventos.pila == []:
            if a.accion == 'inicioPila':
                self.pilaRedo.apilar(a)
                wx.MessageBox(_('No hay pasos que rehacer.'), _('Aviso'))
            else:
                a.contraEvento(1)
        elif len(a.miniEventos.pila) == 1:
            if a.miniEventos.pila[0].accion == 'inicioPila':
                if a.accion == 'inicioPila':
                    self.pilaRedo.apilar(a)
                    wx.MessageBox(_('No hay pasos que rehacer.'), _('Aviso'))
                else:
                    a.contraEvento(1)
            else:
                miniEvt = a.miniEventos.desempilar()
                self.pilaRedo.apilar(a)
                miniEvt.contraEvento(1)
        else:
            miniEvt = a.miniEventos.desempilar()
            self.pilaRedo.apilar(a)
            miniEvt.contraEvento(1)

    def OnGenerarInforme(self, event):
        """
        Metodo: OnGenerarInforme
        """
        self.calculoAnalisisEconomico()
        if self.objEdificio.casoValido == True:
            estanTodosDatos, datosAdmin = self.comprobarDatosInforme()
            if estanTodosDatos == False:
                return
            dlg = chequeoInforme.Dialog(self)
            try:
                dlg.cargarDatos(self.configuracionInforme)
            except:
                logging.info('Excepcion en: %s' % __name__)

            dlg.ShowModal()
            if dlg.dev == False:
                return
            self.configuracionInforme = dlg.dev
            informeCorrecto = self.generarInformeCertificacion(datosAdmin)
            if informeCorrecto == True:
                try:
                    if self.filename == None or self.filename == '':
                        ficheroInforme = DirectorioDoc + '/informeCalificacion.pdf'
                    elif '.cex' in self.filename:
                        ficheroInforme = self.filename.replace('.cex', '.pdf')
                    elif '.CEX' in self.filename:
                        ficheroInforme = self.filename.replace('.CEX', '.pdf')
                    else:
                        ficheroInforme = DirectorioDoc + '/informeCalificacion.pdf'
                    os.startfile(ficheroInforme)
                except:
                    wx.MessageBox(_('El documento no se puede abrir. Si hay algún documento abierto con el mismo nombre debe cerrarlo.'), _('Aviso'))

            informeMMCorrecto = self.generarInformeMM(datosAdmin)
            if informeMMCorrecto == True:
                try:
                    if self.filename == None or self.filename == '':
                        ficheroInforme = DirectorioDoc + '/informeMedidasMejora.pdf'
                    elif '.cex' in self.filename:
                        ficheroInforme = self.filename.replace('.cex', '_informeMedidasMejora.pdf')
                    elif '.CEX' in self.filename:
                        ficheroInforme = self.filename.replace('.CEX', '_informeMedidasMejora.pdf')
                    else:
                        ficheroInforme = DirectorioDoc + '/informeMedidasMejora.pdf'
                    os.startfile(ficheroInforme)
                except:
                    wx.MessageBox(_('El documento no se puede abrir. Si hay algún documento abierto con el mismo nombre debe cerrarlo.'), _('Aviso'))

        elif self.objEdificio.mensajeAviso != '':
            wx.MessageBox(self.objEdificio.mensajeAviso, _('Aviso'))
        return

    def comprobarDatosInforme(self):
        datosAdmin = self.panelDatosAdministrativos.exportarDatos()
        if datosAdmin == []:
            return (False, [])
        aux = self.panelDatosGenerales.comprobarPlanoEIMagenEdificio()
        if aux != '':
            return (False, [])
        return (True, datosAdmin)

    def generarInformeCertificacion(self, datosAdmin):
        try:
            informe = creaPDF.GeneraInforme(filename=self.filename, objEdificio=self.objEdificio, datosAdmin=datosAdmin, listadoConjuntosMMUsuario=self.listadoConjuntosMMUsuario, datosEconomicos=self.panelAnalisisEconomico.cogerDatos(), datosConfiguracionInforme=self.configuracionInforme)
        except FuenteAusente:
            aux = FuenteAusente()
            wx.MessageBox(unicode(aux), _('Aviso'))
            return False
        except BorradoInformeCertificacion:
            aux = BorradoInformeCertificacion()
            wx.MessageBox(unicode(aux), _('Aviso'))
            return False
        except LayoutError:
            mensajeError = _('Los párrafos de los comentarios son muy largos.\nPor favor, introduzca algún salto de línea')
            wx.MessageBox(mensajeError, _('Aviso'))
            return False
        except:
            wx.MessageBox(_('No se ha podido generar el informe de certificación.'), _('Aviso'))
            return False

        return True

    def generarInformeMM(self, datosAdmin):
        try:
            informe = creaMMPDF.GeneraInforme(filename=self.filename, objEdificio=self.objEdificio, datosAdmin=datosAdmin, listadoConjuntosMMUsuario=self.listadoConjuntosMMUsuario, datosConfiguracionInforme=self.configuracionInforme)
            if informe.listadoConjuntosMMUsuario == []:
                return False
        except FuenteAusente:
            aux = FuenteAusente()
            wx.MessageBox(unicode(aux), _('Aviso'))
            return False
        except BorradoInformeMM:
            aux = BorradoInformeMM()
            wx.MessageBox(unicode(aux), _('Aviso'))
            return False
        except:
            wx.MessageBox(_('No se ha podido generar el informe de medidas de mejora.'), _('Aviso'))
            return False

        return True

    def OnGenerarArchivoXML(self, event):
        """
        Metodo: OnGenerarInforme
        """
        self.calculoAnalisisEconomico()
        if self.objEdificio.casoValido == True:
            estanTodosDatos, datosAdmin = self.comprobarDatosInforme()
            if estanTodosDatos == False:
                return
            xml = escribirXML(filename=self.filename, objEdificio=self.objEdificio, datosAdmin=datosAdmin, listadoConjuntosMMUsuario=self.listadoConjuntosMMUsuario, datosConfiguracionInforme=self.configuracionInforme, tipoProcedimiento='CertificacionExistente')
            if xml.logErrores == []:
                wx.MessageBox(_('Archivo .xml creado correctamente.\nHa sido guardado en la misma ubicación que el archivo .cex.'), _('Aviso'))
            else:
                aux = ''
                for i in xml.logErrores:
                    aux += '- %s\n' % i

                wx.MessageBox(aux, _('Aviso'))

    def calculoCalificacion(self):
        zonaCalificacion = ''
        self.objEdificio = datosEdificio.datosEdificio(datosGenerales=self.panelDatosGenerales.exportarDatos(), datosEnvolvente=self.panelEnvolvente.cogerDatos(), datosInstalaciones=self.panelInstalaciones.exportarDatos(), programa=self.programa, subgrupos=self.notebook1.subgrupos, zonaCalificacion=zonaCalificacion, datosSombras=self.datosSombras, escala=self.escala, esEdificioExistente=self.esEdificioExistente)
        self.objEdificio.calificacion()

    def calculoMedidasPorDefecto(self):
        """
        Metodo: onCalcularMedidasPorDefecto
        Se calculan las medidas de mejora por defecto
        """
        self.calculoCalificacion()
        if self.objEdificio.casoValido == False:
            if self.objEdificio.mensajeAviso != '':
                wx.MessageBox(self.objEdificio.mensajeAviso, _('Aviso'))
            return
        esIgual = True
        if len(self.listadoConjuntosMMPorDefecto) > 0:
            esIgual = compararDosConjuntosObjEdificio(self.objEdificio, self.listadoConjuntosMMPorDefecto[0].datosEdificioOriginal)
        if esIgual == False or self.listadoConjuntosMMPorDefecto == []:
            self.barraEstado = wx.ProgressDialog(_('Calculando...'), _('Espere mientras se recalculan las medidas de mejora por defecto...'))
            self.listadoConjuntosMMPorDefecto = []
            try:
                listadoConjuntosMMPorDefectoSinCalcular = getMedidasPorDefecto(self.objEdificio)
                contador = 0
                for conjunto in listadoConjuntosMMPorDefectoSinCalcular:
                    conjunto.datosEdificioOriginal = self.objEdificio
                    conjunto.calificacion()
                    if conjunto.datosNuevoEdificio.casoValido == True:
                        if conjunto.ahorro[-1] > 0.0:
                            self.listadoConjuntosMMPorDefecto.append(conjunto)
                    contador += 1
                    self.barraEstado.Update(int(contador * 100 / len(listadoConjuntosMMPorDefectoSinCalcular)))

            except:
                logging.info('Excepcion en: %s' % __name__)

            self.barraEstado.Update(100)
            self.barraEstado.Destroy()

    def calculoMedidasUsuario(self):
        """
        Metodo: calculoMedidasUsuario
        """
        self.calculoCalificacion()
        if self.objEdificio.casoValido == False:
            if self.objEdificio.mensajeAviso != '':
                wx.MessageBox(self.objEdificio.mensajeAviso, _('Aviso'))
            return
        esIgual = True
        if len(self.listadoConjuntosMMUsuario) > 0:
            esIgual = compararDosConjuntosObjEdificio(self.objEdificio, self.listadoConjuntosMMUsuario[0].datosEdificioOriginal)
        if esIgual == False:
            self.barraEstado = wx.ProgressDialog(_('Calculando...'), _('Espere mientras se recalculan las medidas de mejora...'))
            total = len(self.listadoConjuntosMMUsuario)
            listadoErrores = ''
            for i in range(len(self.listadoConjuntosMMUsuario)):
                conjunto = self.listadoConjuntosMMUsuario[i]
                try:
                    if type(conjunto.mejoras) == type('edificio completo'):
                        conjunto.datosEdificioOriginal = self.objEdificio
                        conjunto.calificacion()
                        conjuntoRecalculado = conjunto
                    else:
                        conjunto.datosEdificioOriginal = self.objEdificio
                        conjunto.calificacion()
                        conjuntoRecalculado = conjunto
                    if conjuntoRecalculado.datosNuevoEdificio.casoValido == True:
                        pass
                    else:
                        listadoErrores += '- %s: %s\n' % (conjuntoRecalculado.nombre, conjuntoRecalculado.datosNuevoEdificio.mensajeAviso)
                except:
                    logging.info('Excepcion en: %s' % __name__)
                    try:
                        listadoErrores += '- %s' % conjunto.nombre
                    except:
                        logging.info('Excepcion en: %s' % __name__)

                self.barraEstado.Update(int(i * 100 / total))

            self.barraEstado.Update(100)
            self.barraEstado.Destroy()
            if listadoErrores != '':
                wx.MessageBox(_('No se han podido calcular los siguientes conjuntos de medidas de mejora:\n%s' % listadoErrores), _('Aviso'))

    def calculoAnalisisEconomico(self, flag=0):
        self.calculoMedidasUsuario()
        if self.objEdificio.casoValido == False:
            for conjuntoMM in self.listadoConjuntosMMUsuario:
                self.panelAnalisisEconomico.panelResultado.recargaTablaResultados()

            return
        self.panelAnalisisEconomico.panelResultado.calculoAnalisisEconomico(flag=flag)
        self.panelAnalisisEconomico.panelResultado.recargaTablaResultados()

    def OnMenuCalificar(self, event):
        """
        Metodo: OnMenuCalificar
        """
        self.calculoCalificacion()
        if self.objEdificio.casoValido == True:
            if self.objEdificio.mensajeAviso != '':
                wx.MessageBox(self.objEdificio.mensajeAviso, _('Aviso'))
            self.PanelResultadosCalificacion(objEdificio=self.objEdificio)
        elif self.objEdificio.mensajeAviso != '':
            wx.MessageBox(self.objEdificio.mensajeAviso, _('Aviso'))

    def PanelResultadosCalificacion(self, objEdificio):
        """
        Metodo: PanelResultadosCalificacion

        ARGUMENTOS:
                lista_limites:
                 lista_calificaciones:
                 balanceContribuciones:
        """
        self.panelCalificacion = panelCalificacion(parent=self.notebook1, id=wx.NewId(), pos=self.posicion_defecto, size=(0,
                                                                                                                          0), style=0, name='')
        self.paneles.append(self.panelCalificacion)
        self.notebook1.iniciaPaneles([self.paneles[int(len(self.paneles) - 1)]], self.notebook1)
        self.notebook1.SetSelection(len(self.paneles) - 1)
        emisiones_limites = objEdificio.datosResultados.emisiones_limites
        limite_A = emisiones_limites[0]
        limite_B = emisiones_limites[1]
        limite_C = emisiones_limites[2]
        limite_D = emisiones_limites[3]
        limite_E = emisiones_limites[4]
        limite_F = emisiones_limites[5]
        self.panelCalificacion.ValorDdaCal.SetLabel(str(round(objEdificio.datosResultados.ddaBrutaCal, 1)))
        self.panelCalificacion.NotaDdaCal.SetLabel(objEdificio.datosResultados.ddaBrutaCal_nota)
        if objEdificio.datosResultados.ddaBrutaRef_nota != _('No calificable'):
            self.panelCalificacion.ValorDdaRef.SetLabel(str(round(objEdificio.datosResultados.ddaBrutaRef, 1)))
            self.panelCalificacion.NotaDdaRef.SetLabel(objEdificio.datosResultados.ddaBrutaRef_nota)
        else:
            self.panelCalificacion.ValorDdaRef.SetLabel(_('No calificable'))
            self.panelCalificacion.NotaDdaRef.SetLabel('')
        self.panelCalificacion.ValorEmisCal.SetLabel(str(round(objEdificio.datosResultados.emisionesCal, 1)))
        self.panelCalificacion.NotaEmisCal.SetLabel(objEdificio.datosResultados.emisionesCal_nota)
        if objEdificio.datosResultados.emisionesRef_nota != _('No calificable'):
            self.panelCalificacion.ValorEmisRef.SetLabel(str(round(objEdificio.datosResultados.emisionesRef, 1)))
            self.panelCalificacion.NotaEmisRef.SetLabel(objEdificio.datosResultados.emisionesRef_nota)
        else:
            self.panelCalificacion.ValorEmisRef.SetLabel(_('No calificable'))
            self.panelCalificacion.NotaEmisRef.SetLabel('')
        self.panelCalificacion.ValorEmisACS.SetLabel(str(round(objEdificio.datosResultados.emisionesACS, 1)))
        self.panelCalificacion.NotaEmisACS.SetLabel(objEdificio.datosResultados.emisionesACS_nota)
        self.panelCalificacion.LimiteA.SetLabel(_('< ') + str(limite_A))
        self.panelCalificacion.LimiteB.SetLabel(_('< ') + str(limite_B))
        self.panelCalificacion.LimiteC.SetLabel(_('< ') + str(limite_C))
        self.panelCalificacion.LimiteD.SetLabel(_('< ') + str(limite_D))
        self.panelCalificacion.LimiteE.SetLabel(_('< ') + str(limite_E))
        self.panelCalificacion.LimiteF.SetLabel(_('< ') + str(limite_F))
        self.panelCalificacion.LimiteG.SetLabel(_('>= ') + str(limite_F))
        self.panelCalificacion.NotaA.Show(False)
        self.panelCalificacion.NotaB.Show(False)
        self.panelCalificacion.NotaC.Show(False)
        self.panelCalificacion.NotaD.Show(False)
        self.panelCalificacion.NotaE.Show(False)
        self.panelCalificacion.NotaF.Show(False)
        self.panelCalificacion.NotaG.Show(False)
        self.panelCalificacion.EmisA.Show(False)
        self.panelCalificacion.EmisB.Show(False)
        self.panelCalificacion.EmisC.Show(False)
        self.panelCalificacion.EmisD.Show(False)
        self.panelCalificacion.EmisE.Show(False)
        self.panelCalificacion.EmisF.Show(False)
        self.panelCalificacion.EmisG.Show(False)
        emisionesGlobales = str(round(objEdificio.datosResultados.emisionesMostrar, 1))
        if objEdificio.datosResultados.emisiones_nota == 'A':
            self.panelCalificacion.NotaA.Show(True)
            self.panelCalificacion.EmisA.SetLabel(emisionesGlobales)
            self.panelCalificacion.EmisA.Show(True)
        if objEdificio.datosResultados.emisiones_nota == 'B':
            self.panelCalificacion.NotaB.Show(True)
            self.panelCalificacion.EmisB.SetLabel(emisionesGlobales)
            self.panelCalificacion.EmisB.Show(True)
        if objEdificio.datosResultados.emisiones_nota == 'C':
            self.panelCalificacion.NotaC.Show(True)
            self.panelCalificacion.EmisC.SetLabel(emisionesGlobales)
            self.panelCalificacion.EmisC.Show(True)
        if objEdificio.datosResultados.emisiones_nota == 'D':
            self.panelCalificacion.NotaD.Show(True)
            self.panelCalificacion.EmisD.SetLabel(emisionesGlobales)
            self.panelCalificacion.EmisD.Show(True)
        if objEdificio.datosResultados.emisiones_nota == 'E':
            self.panelCalificacion.NotaE.Show(True)
            self.panelCalificacion.EmisE.SetLabel(emisionesGlobales)
            self.panelCalificacion.EmisE.Show(True)
        if objEdificio.datosResultados.emisiones_nota == 'F':
            self.panelCalificacion.NotaF.Show(True)
            self.panelCalificacion.EmisF.SetLabel(emisionesGlobales)
            self.panelCalificacion.EmisF.Show(True)
        if objEdificio.datosResultados.emisiones_nota == 'G':
            self.panelCalificacion.NotaG.Show(True)
            self.panelCalificacion.EmisG.SetLabel(emisionesGlobales)
            self.panelCalificacion.EmisG.Show(True)
        if objEdificio.datosResultados.emisionesContrib != 0:
            self.panelCalificacion.balanceContribuciones.Show(True)
            self.panelCalificacion.balanceContribucionesUnidades.Show(True)
            self.panelCalificacion.valorBalanceContribuciones.SetLabel(str(round(objEdificio.datosResultados.emisionesContrib, 1)))
            self.panelCalificacion.valorBalanceContribuciones.Show(True)
        else:
            self.panelCalificacion.balanceContribuciones.Show(False)
            self.panelCalificacion.balanceContribucionesUnidades.Show(False)
            self.panelCalificacion.valorBalanceContribuciones.Show(False)
        self.panelCalificacion.SetSize(self.tamano_defecto)

    def OnMedidasDeMejora(self, event):
        """
        Metodo: OnMedidasDeMejora

        ARGUMENTOS:
                event:
        """
        self.calculoCalificacion()
        if self.objEdificio.casoValido == False:
            if self.objEdificio.mensajeAviso != '':
                wx.MessageBox(self.objEdificio.mensajeAviso, _('Aviso'))
            return
        self.calculoMedidasPorDefecto()
        self.calculoMedidasUsuario()
        self.panelMedidasMejora.abrirPanelMedidasMejora()
        self.paneles.append(self.panelMedidasMejora)
        self.notebook1.iniciaPaneles([self.paneles[int(len(self.paneles) - 1)]], self.notebook1)
        self.notebook1.SetSelection(len(self.paneles) - 1)
        items = self.menuCalificar.GetMenuItems()
        items[1].Enable(False)
        self.botonMejoras11.Enable(False)

    def OnAnalisisEconomico(self, event):
        """
        Metodo: OnAnalisisEconomico

        ARGUMENTOS:
                event:
        """
        self.calculoCalificacion()
        if self.objEdificio.casoValido == False:
            if self.objEdificio.mensajeAviso != '':
                wx.MessageBox(self.objEdificio.mensajeAviso, _('Aviso'))
            return
        self.paneles.append(self.panelAnalisisEconomico)
        self.notebook1.iniciaPaneles([self.paneles[int(len(self.paneles) - 1)]], self.notebook1)
        self.notebook1.SetSelection(len(self.paneles) - 1)
        items = self.menuCalificar.GetMenuItems()
        items[2].Enable(False)
        self.botonEconomico11.Enable(False)

    def DefinirObstaculosRemotos(self, event):
        """
        Metodo: DefinirObstaculosRemotos

        ARGUMENTOS:
                event:
        """
        provincia = ''
        provincia = self.panelDatosGenerales.provinciaChoice.GetStringSelection()
        if provincia == '':
            wx.MessageBox(_('Debe indicar primero la provincia/ciudad autónoma en la que se ubica el edificio'), _('Aviso'))
            return
        self.ventanaSombras = menuObstaculosRemotos.create(self, provincia)
        self.ventanaSombras.Bind(wx.EVT_CLOSE, self.OnSombrasClose)
        self.ventanaSombras.MakeModal(True)
        self.ventanaSombras.Show()

    def OnSombrasClose(self, event):
        """
        Metodo: OnSombrasClose

        ARGUMENTOS:
                event:
        """
        self.ventanaSombras.MakeModal(False)
        self.ventanaSombras.Destroy()
        self.nuevoListadoSombras = [
         (
          'Sin patrón', _('Sin patrón'))]
        for elemento in self.datosSombras:
            self.nuevoListadoSombras.append((elemento[0], elemento[0]))

        try:
            if (self.panelEnvolvente.panelElegirObjeto.definirFachada.GetValue() == True or self.panelEnvolvente.panelElegirObjeto.definirCubierta.GetValue() == True) and self.panelEnvolvente.panelElegirObjeto.contactoAire.GetValue() == True:
                self.panelEnvolvente.panel2.obstaculoRemotoChoice.SetItems(self.nuevoListadoSombras)
                self.panelEnvolvente.panel2.obstaculoRemotoChoice.SetSelection(0)
                nombreCerramiento = self.panelEnvolvente.panel2.nombreMuro.GetValue()
                for cerr in self.panelEnvolvente.cerramientos:
                    if cerr[0] == nombreCerramiento:
                        self.panelEnvolvente.panel2.obstaculoRemotoChoice.SetStringSelection(cerr[7])
                        break

            elif self.panelEnvolvente.panelElegirObjeto.definirHueco.GetValue() == True:
                self.panelEnvolvente.panel2.obstaculosRemotosChoice.SetItems(self.nuevoListadoSombras)
                self.panelEnvolvente.panel2.obstaculosRemotosChoice.SetSelection(0)
                nombreVidrio = self.panelEnvolvente.panel2.decripcionHueco.GetValue()
                for vent in self.panelEnvolvente.ventanas:
                    if vent.descripcion == nombreVidrio:
                        self.panelEnvolvente.panel2.obstaculosRemotosChoice.SetStringSelection(vent.patronSombras)
                        break

        except:
            logging.info('Excepcion en: %s' % __name__)

        try:
            self.panelEnvolvente.vistaClasica.cargaCerramientos()
            self.panelEnvolvente.vistaClasica.cargaHuecos()
        except:
            logging.info('Excepcion en: %s' % __name__)

    def DefinirVentanas(self, event):
        """
        Metodo: DefinirVentanas

        ARGUMENTOS:
                event:
        """
        dlg = menuVidrios.create(self)
        dlg.cargarVidrio.Show(False)
        dlg.ShowModal()
        dlg.Destroy()

    def DefinirMarcos(self, event):
        """
        Metodo: DefinirMarcos

        ARGUMENTOS:
                 event:
        """
        dlg = menuMarcos.create(self)
        dlg.cargarMarco.Show(False)
        dlg.ShowModal()
        dlg.Destroy()

    def DefinirNuevoMaterial(self, event):
        """
        Metodo: DefinirNuevoMaterial

        ARGUMENTOS:
                event:
        """
        dlg = menuMateriales.create(self)
        dlg.ShowModal()
        dlg.Destroy()

    def DefinirComposicionCerramientos(self, event):
        """
        Metodo: DefinirComposicionCerramientos

        ARGUMENTOS:
                event:
        """
        self.dlg = menuCerramientos.create(self)
        self.dlg.ShowModal()
        self.listadoCerramientos = []
        for i in self.listadoComposicionesCerramientos:
            self.listadoCerramientos.append(i.nombre)

        try:
            self.panelEnvolvente.panel2.cerramientosChoice.SetItems(self.listadoCerramientos)
        except:
            logging.info('Excepcion en: %s' % __name__)

        self.dlg.Destroy()

    def DefinirPT(self, event):
        """
        Metodo: DefinirPT

        ARGUMENTOS:
                event:
        """
        self.dlg = menuPT.create(self)
        self.dlg.CargarPT.Show(False)
        self.dlg.ShowModal()
        self.dlg.Destroy()

    def OnMenuFileOpenNuevo(self, event):
        """
        Metodo: OnMenuFileOpenNuevo

        ARGUMENTOS:
                event):      :
        """
        self.versionArchivoGuardado = versionCEX
        if self.OnMenuFileExitMenu(None) == 'cancelar':
            return
        else:
            self.filename = None
            self.SetTitle(_('CE3X - res: Certificación Energética Simplificada de Edificios Existentes - Residencial'))
            self.listadoCerramientos = []
            self.listadoComposicionesCerramientos = []
            self.nuevoListadoSombras = [
             (
              'Sin patrón', _('Sin patrón'))]
            self.datosSombras = []
            datosAdmin = [
             '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', [], '', '', '', '', '', '', '', '', '', '']
            datosGen = ['', '', '', '', '', '', '', '', '', '', '',
             False, '', [False, '', ''], False, '', '', '', '', '', '']
            datosEnvolvente = [[], [], [], []]
            datosInstalacion = [[], [], [], [], [], [], [], [], [], [], [], []]
            datosMejoras = []
            datosAnalisis = [[], ['', '', '', '', '', '', '', '', '', ''], []]
            self.configuracionInforme = ['', '', '', '', '', ['', '', ''], ['', '', '']]
            self.diccInformacionExtra = {}
            self.esEdificioExistente = True
            self.panelDatosAdministrativos.cargarDatos(datosAdmin)
            self.panelDatosGenerales.cargarDatos(datosGen)
            self.panelEnvolvente.panelBotones.OnVistaNormalBoton(None)
            self.panelEnvolvente.cargarDatos(datosEnvolvente)
            self.panelInstalaciones.panelBotones.OnVistaNormalBoton(None)
            self.panelInstalaciones.cargarDatos(datosInstalacion)
            self.listadoConjuntosMMUsuario = datosMejoras
            self.panelAnalisisEconomico.cargarDatos(datosAnalisis)
            self.notebook1.subgrupos = []
            self.libreriaVidriosMarcos = []
            self.panelDatosGenerales.localidadChoice.SetItems([_('')])
            self.panelDatosGenerales.otroCuadro.SetValue('')
            self.panelDatosGenerales.otroCuadro.Show(False)
            items = self.menuCalificar.GetMenuItems()
            items[2].Enable(True)
            items[3].Enable(True)
            self.botonMejoras11.Enable(True)
            self.botonEconomico11.Enable(True)
            bol = True
            while bol != False:
                bol = False
                for i in range(len(self.paneles)):
                    if i > 3:
                        self.notebook1.RemovePage(i)
                        self.paneles[i].Show(False)
                        self.paneles.pop(i)
                        bol = True
                        break

            self.pilaUndo = undo.undoManaggement()
            self.pilaRedo = undo.undoManaggement()
            self.pilaUndo.pila = [undo.EventoInicial()]
            self.pilaRedo.pila = [undo.EventoInicial()]
            return

    def OnMenuFileSaveasMenu(self, event):
        """
        Metodo: OnMenuFileSaveasMenu

        ARGUMENTOS:
                event:
        """
        dlg = wx.FileDialog(self, 'Guardar', DirectorioDoc, '', '*.cex', wx.SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            try:
                f1 = open(self.filename, 'w')
                pickle.dump('%s ' % programaVersion + self.programa, f1)
                pickle.dump(self.panelDatosAdministrativos.cogerDatos(), f1)
                pickle.dump(self.panelDatosGenerales.cogerDatos(), f1)
                pickle.dump(self.panelEnvolvente.cogerDatos(), f1)
                pickle.dump(self.panelInstalaciones.cogerDatos(), f1)
                pickle.dump(self.listadoConjuntosMMUsuario, f1)
                pickle.dump(self.panelAnalisisEconomico.cogerDatos(), f1)
                pickle.dump(self.libreriaVidriosMarcos, f1)
                pickle.dump(self.listadoComposicionesCerramientos, f1)
                pickle.dump(self.datosSombras, f1)
                pickle.dump([ x[0] for x in self.nuevoListadoSombras ], f1)
                pickle.dump(self.configuracionInforme, f1)
                pickle.dump(self.diccInformacionExtra, f1)
                pickle.dump(self.esEdificioExistente, f1)
                f1.flush()
                self.versionArchivoGuardado = versionCEX
                f1.close()
            except:
                wx.MessageBox(_('Error al guardar el fichero'), _('Aviso'))

            self.SetTitle(_('CE3X - res: %s') % self.filename)
            self.pilaUndo.apilar(eventoUndo(self, 'guardar', 'guardar'))
            self.refrescaRecentFiles()

    def OnMenuFileSaveMenu(self, event):
        """
        Metodo: OnMenuFileSaveMenu

        ARGUMENTOS:
                event:
        """
        if self.filename == None:
            return self.OnMenuFileSaveasMenu(event)
        else:
            try:
                f1 = open(self.filename, 'w')
                pickle.dump('%s ' % programaVersion + self.programa, f1)
                pickle.dump(self.panelDatosAdministrativos.cogerDatos(), f1)
                pickle.dump(self.panelDatosGenerales.cogerDatos(), f1)
                pickle.dump(self.panelEnvolvente.cogerDatos(), f1)
                pickle.dump(self.panelInstalaciones.cogerDatos(), f1)
                pickle.dump(self.listadoConjuntosMMUsuario, f1)
                pickle.dump(self.panelAnalisisEconomico.cogerDatos(), f1)
                pickle.dump(self.libreriaVidriosMarcos, f1)
                pickle.dump(self.listadoComposicionesCerramientos, f1)
                pickle.dump(self.datosSombras, f1)
                pickle.dump([ x[0] for x in self.nuevoListadoSombras ], f1)
                pickle.dump(self.configuracionInforme, f1)
                pickle.dump(self.diccInformacionExtra, f1)
                pickle.dump(self.esEdificioExistente, f1)
                f1.flush()
                self.versionArchivoGuardado = versionCEX
                f1.close()
            except:
                wx.MessageBox(_('Error al guardar el fichero'), _('Aviso'))

            self.SetTitle(_('CE3X - res: %s') % self.filename)
            self.pilaUndo.apilar(eventoUndo(self, 'guardar', 'guardar'))
            self.refrescaRecentFiles()
            return

    def OnMenuFileExitMenu(self, event):
        """
        Metodo: OnMenuFileExitMenu

        ARGUMENTOS:
                 event): #cierro fiche:
        """
        if len(self.pilaUndo.pila) > 1:
            if self.pilaUndo.pila[0].accion != 'guardar':
                dlg = dialogoConfirmaGuardarCambios.Dialog1(self, _('El proyecto ha sido modificado. ¿Desea guardar los cambios?'))
                dlg.ShowModal()
                if dlg.dev == 'guardar':
                    self.OnMenuFileSaveMenu(None)
                elif dlg.dev == 'cancelar':
                    return 'cancelar'
        if event != None:
            self.Destroy()
        return 'no cancelar'

    def OnMenuFileOpenMenu(self, event):
        """
        Metodo: OnMenuFileOpenMenu

        ARGUMENTOS:
                 event:
        """
        if self.OnMenuFileExitMenu(None) == 'cancelar':
            return
        else:
            dlg = wx.FileDialog(self, _('Seleccione un archivo'), DirectorioDoc, '', '*.cex', wx.OPEN)
            if dlg.ShowModal() == wx.ID_OK:
                self.filename = dlg.GetPath()
                dlg.Destroy()
                self.abreArchivoCEX(filename=self.filename)
            return

    def refrescaRecentFiles(self):
        """
        Metodo: refrescaRecentFiles

        """
        a = registro.leerFicherosRecientes()
        for i in range(len(a)):
            if self.filename == a[i]:
                a.pop(i)
                break

        a.insert(0, self.filename)
        registro.editarFicherosRecientes(a)
        for i in range(self.history.GetCount()):
            try:
                self.history.RemoveFileFromHistory(i)
            except:
                logging.info('Excepcion en: %s' % __name__)

        a = registro.leerFicherosRecientes()
        a.reverse()
        for i in a:
            if i != '':
                self.history.AddFileToHistory(i)

    def abreArchivoDirecto(self, filename):
        """
        Metodo: abreArchivoDirecto
    

        ARGUMENTOS:
                filename:
        Cuando se abre un archivo de los recientes
        """
        self.filename = filename
        self.abreArchivoCEX(filename=self.filename)

    def abreArchivoCEX(self, filename, barraProgreso=True):
        """
        barraProgreso: es un flag. Si esta a True: se muestra la barra de estado. Si  es False no se muestra. Por defecto es True
        """
        if barraProgreso:
            self.barraEstado = wx.ProgressDialog(_('Abriendo...'), _('Espere mientras se abre el archivo...'))
        try:
            if barraProgreso:
                self.barraEstado.Update(int(1.0 / 40.0 * 100.0))
            f1 = open(filename, 'r')
            auxString = f1.read()
            f1.close()
            if barraProgreso:
                self.barraEstado.Update(int(2.0 / 40.0 * 100.0))
            version = pickle.loads(auxString)
            if barraProgreso:
                self.barraEstado.Update(int(3.0 / 40.0 * 100.0))
            self.versionArchivoGuardado = getVersionGuardada(version)
            if barraProgreso:
                self.barraEstado.Update(int(4.0 / 40.0 * 100.0))
            datosArchivoAdaptado = adaptarVersionesAnterioresArchivo(datosArchivo=auxString, versionArchivoGuardado=self.versionArchivoGuardado)
            if barraProgreso:
                self.barraEstado.Update(int(5.0 / 40.0 * 100.0))
            f1 = StringIO.StringIO()
            f1.write(datosArchivoAdaptado)
            if barraProgreso:
                self.barraEstado.Update(int(6.0 / 40.0 * 100.0))
            f1.seek(0)
            version = pickle.load(f1)
            if barraProgreso:
                self.barraEstado.Update(int(7.0 / 40.0 * 100.0))
            datosAdmin = pickle.load(f1)
            if barraProgreso:
                self.barraEstado.Update(int(8.0 / 40.0 * 100.0))
            datosGen = pickle.load(f1)
            if barraProgreso:
                self.barraEstado.Update(int(9.0 / 40.0 * 100.0))
            if self.programa not in version:
                if 'Residencial' in version:
                    prog = _('"residencial"')
                elif b'Peque\xf1oTerciario' in version:
                    prog = _('"pequeño terciario"')
                elif 'GranTerciario' in version:
                    prog = _('"gran terciario"')
                else:
                    prog = ''
                if prog != '':
                    dlg = dialogoConfirma.Dialog1(self, _('El fichero que está abriendo fue creado con la versión ') + prog + _(' de la aplicación. ¿Desea iniciar ahora dicha versión?'))
                    dlg.ShowModal()
                    if dlg.dev == True:
                        if barraProgreso:
                            self.barraEstado.Update(100)
                            self.barraEstado.Destroy()
                        try:
                            f1.close()
                        except:
                            logging.info('Excepcion en: %s' % __name__)

                        ruta = '%s\\%s' % (Directorio, programaVersionExe)
                        nombreExe = programaVersionExe
                        filenameConRuta = self.filename
                        os.spawnl(os.P_NOWAIT, ruta, '\\%s' % nombreExe, '"%s"' % filenameConRuta)
                        self.OnMenuFileExitMenu(1)
                        return
            if barraProgreso:
                self.barraEstado.Update(int(10.0 / 40.0 * 100.0))
            datosEnvolvente = pickle.load(f1)
            if barraProgreso:
                self.barraEstado.Update(int(11.0 / 40.0 * 100.0))
            datosInstalaciones = pickle.load(f1)
            if barraProgreso:
                self.barraEstado.Update(int(12.0 / 40.0 * 100.0))
            datosMMArchivo = pickle.load(f1)
            if barraProgreso:
                self.barraEstado.Update(int(13.0 / 40.0 * 100.0))
            datosMM = adaptarVersionesAnterioresMM(datosMM=datosMMArchivo, versionArchivoGuardado=self.versionArchivoGuardado)
            if barraProgreso:
                self.barraEstado.Update(int(14.0 / 40.0 * 100.0))
            datosAnalisis = pickle.load(f1)
            if barraProgreso:
                self.barraEstado.Update(int(15.0 / 40.0 * 100.0))
            self.libreriaVidriosMarcos = pickle.load(f1)
            if barraProgreso:
                self.barraEstado.Update(int(16.0 / 40.0 * 100.0))
            cerramientos = pickle.load(f1)
            if barraProgreso:
                self.barraEstado.Update(int(17.0 / 40.0 * 100.0))
            self.datosSombras = pickle.load(f1)
            if barraProgreso:
                self.barraEstado.Update(int(18.0 / 40.0 * 100.0))
            auxListadoSombras = pickle.load(f1)
            if barraProgreso:
                self.barraEstado.Update(int(19.0 / 40.0 * 100.0))
            self.nuevoListadoSombras = [('Sin patrón', _('Sin patrón'))]
            if barraProgreso:
                self.barraEstado.Update(int(20.0 / 40.0 * 100.0))
            for sombra in auxListadoSombras[1:]:
                self.nuevoListadoSombras.append((sombra, sombra))

            if barraProgreso:
                self.barraEstado.Update(int(21.0 / 40.0 * 100.0))
            self.configuracionInforme = pickle.load(f1)
            if barraProgreso:
                self.barraEstado.Update(int(22.0 / 40.0 * 100.0))
            try:
                self.diccInformacionExtra = pickle.load(f1)
            except:
                logging.info('Excepcion en: %s' % __name__)
                self.diccInformacionExtra = {}

            if barraProgreso:
                self.barraEstado.Update(int(23.0 / 40.0 * 100.0))
            try:
                self.esEdificioExistente = pickle.load(f1)
            except:
                logging.info('Excepcion en: %s' % __name__)
                self.esEdificioExistente = True

            if barraProgreso:
                self.barraEstado.Update(int(24.0 / 40.0 * 100.0))
            datosEnvolvente = adaptarVersionesAnterioresEnvolvente(datosEnvolvente=datosEnvolvente, datosGenerales=datosGen, versionArchivoGuardado=self.versionArchivoGuardado)
            if barraProgreso:
                self.barraEstado.Update(int(25.0 / 40.0 * 100.0))
            datosInstalaciones = adaptarVersionesAnterioresInstalaciones(datosInstalaciones=datosInstalaciones, datosGenerales=datosGen, versionArchivoGuardado=self.versionArchivoGuardado, programa=self.programa)
            if barraProgreso:
                self.barraEstado.Update(int(26.0 / 40.0 * 100.0))
            datosMM, mensajeAviso = adaptarVersionesAnterioresInstalacionesConjuntosMM(datosMM=datosMM, datosGenerales=datosGen, versionArchivoGuardado=self.versionArchivoGuardado, programa=self.programa)
            if barraProgreso:
                self.barraEstado.Update(int(27.0 / 40.0 * 100.0))
            if mensajeAviso != '':
                wx.MessageBox(_('Se ha detectado que existe un conjunto de medidas de mejora cargado desde archivo y que fue creado con una versión anterior de CE3X. Dicho conjunto no puede ser cargado y deberá ser previamente guardado con la versión actual de CE3X y después añadido como conjunto de medidas de mejora.'), _('Aviso'))
            self.listadoComposicionesCerramientos = cerramientos
            self.listadoCerramientos = []
            for i in self.listadoComposicionesCerramientos:
                self.listadoCerramientos.append(i.nombre)

            if barraProgreso:
                self.barraEstado.Update(int(28.0 / 40.0 * 100.0))
            self.panelDatosAdministrativos.cargarDatos(datosAdmin)
            if barraProgreso:
                self.barraEstado.Update(int(29.0 / 40.0 * 100.0))
            self.panelDatosGenerales.cargarDatos(datosGen)
            if barraProgreso:
                self.barraEstado.Update(int(30.0 / 40.0 * 100.0))
            self.panelEnvolvente.panelBotones.OnVistaNormalBoton(None)
            if barraProgreso:
                self.barraEstado.Update(int(31.0 / 40.0 * 100.0))
            self.panelEnvolvente.cargarDatos(datosEnvolvente)
            if barraProgreso:
                self.barraEstado.Update(int(32.0 / 40.0 * 100.0))
            self.panelInstalaciones.panelBotones.OnVistaNormalBoton(None)
            if barraProgreso:
                self.barraEstado.Update(int(33.0 / 40.0 * 100.0))
            self.panelInstalaciones.cargarDatos(datosInstalaciones)
            if barraProgreso:
                self.barraEstado.Update(int(34.0 / 40.0 * 100.0))
            self.listadoConjuntosMMUsuario = datosMM
            if barraProgreso:
                self.barraEstado.Update(int(35.0 / 40.0 * 100.0))
            self.panelAnalisisEconomico.cargarDatos(datosAnalisis)
            if barraProgreso:
                self.barraEstado.Update(int(36.0 / 40.0 * 100.0))
            f1.close()
        except Exception as e:
            if barraProgreso:
                self.barraEstado.Update(100)
                self.barraEstado.Destroy()
            if 'workspace' in __file__:
                print 'Error al abrir el fichero'
                print e
                print type(e)
                print e.args
            else:
                wx.MessageBox(_('Error al abrir el fichero'), _('Aviso'))
                f1.close()
                return

        if barraProgreso:
            self.barraEstado.Update(int(37.0 / 40.0 * 100.0))
        bol = True
        while bol != False:
            bol = False
            for i in range(len(self.paneles)):
                if i > 3:
                    self.notebook1.RemovePage(i)
                    self.paneles[i].Show(False)
                    self.paneles.pop(i)
                    bol = True
                    break

        if barraProgreso:
            self.barraEstado.Update(int(38.0 / 40.0 * 100.0))
        items = self.menuCalificar.GetMenuItems()
        items[2].Enable(True)
        items[3].Enable(True)
        self.botonMejoras11.Enable(True)
        self.botonEconomico11.Enable(True)
        if barraProgreso:
            self.barraEstado.Update(int(39.0 / 40.0 * 100.0))
        try:
            self.SetTitle(_('CE3X - res: %s') % self.filename)
        except:
            logging.info('Excepcion en: %s' % __name__)
            self.SetTitle(_('CE3X - res:'))

        self.pilaUndo = undo.undoManaggement()
        self.pilaRedo = undo.undoManaggement()
        self.pilaUndo.pila = [undo.EventoInicial()]
        self.pilaRedo.pila = [undo.EventoInicial()]
        self.refrescaRecentFiles()
        self.barraEstado.Update(int(40.0 / 40.0 * 100.0))
        self.barraEstado.Update(100)
        self.barraEstado.Destroy()
        return

    @decoradores.deco(1)
    def funcion(self, filename):
        pass