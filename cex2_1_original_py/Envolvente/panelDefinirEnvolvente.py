# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\panelDefinirEnvolvente.pyc
# Compiled at: 2014-12-09 14:58:47
"""
Modulo: panelDefinirEnvolvente.py

"""
import wx, Envolvente.panelFachadaConAire as panelFachadaConAire, Envolvente.panelFachadaConTerreno as panelFachadaConTerreno, Envolvente.panelFachadaConEdificio as panelFachadaConEdificio, Envolvente.panelCubiertaConAire as panelCubiertaConAire, Envolvente.panelCubiertaConTerreno as panelCubiertaConTerreno, Envolvente.panelSueloConTerreno as panelSueloConTerreno, Envolvente.panelSueloConAire as panelSueloConAire, Envolvente.panelHuecos as panelHuecos, Envolvente.panelPuentesTermicos as panelPuentesTermicos, Envolvente.panelPuentesTermicosPorDefecto as panelPuentesTermicosPorDefecto, Envolvente.panelParticionVertical as panelParticionVertical, Envolvente.panelParticionHorizontalInferior as panelParticionHorizontalInferior, Envolvente.panelParticionHorizontalSuperior as panelParticionHorizontalSuperior, tips, nuevoUndo, copy, directorios
Directorio = directorios.BuscaDirectorios().Directorio
wxID_PANEL1, wxID_PANEL1DEFINIRCUBIERTA, wxID_PANEL1DEFINIRELEMENTOTEXT, wxID_PANEL1DEFINIRFACHADA, wxID_PANEL1DEFINIRHUECO, wxID_PANEL1DEFINIRPARTICIONINTERIOR, wxID_PANEL1DEFINIRPUENTETERMICO, wxID_PANEL1DEFINIRSUELO, wxID_PANEL1STATICBITMAP1, wxID_PANEL1CONTACTOSUELO, wxID_PANEL1CONTACTOAIRE, wxID_PANEL1CONTACTOEDIFICIO, wxID_PANEL1DEFINIR, wxID_PANEL1TEXTOINFORMACIONTEXT, wxID_PANEL1PTDEFECTOBOTON, wxID_PANEL1VERTICAL, wxID_PANEL1HORIZONTALSUP, wxID_PANEL1HORIZONTALINF, wxID_WXPANEL1STATICLINE, wxID_PANEL1PTUSUARIO = [ wx.NewId() for _init_ctrls in range(20) ]

class definirEnvolvente(wx.Panel, nuevoUndo.VistaUndo):
    """
    Clase: definirEnvolvente del modulo panelDefinirEnvolvente.py

    """

    def _init_ctrls(self, prnt, id, posi, siz, styles, named):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
                id:
                posi:
                siz:
                styles:
                named:
        """
        wx.Panel.__init__(self, id=wxID_PANEL1, name='panelDefinirEnvolvente', parent=prnt, pos=posi, size=siz, style=styles)
        self.SetBackgroundColour('white')
        self.definirText = wx.StaticText(id=wxID_PANEL1DEFINIR, label=_('Envolvente térmica del edificio'), name='definirText', parent=self, pos=wx.Point(0, 0), size=wx.Size(167, 18), style=0)
        self.definirText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.definirText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.definirCubierta = wx.RadioButton(id=wxID_PANEL1DEFINIRCUBIERTA, label=_('Cubierta'), name='definirCubierta', parent=self, pos=wx.Point(20, 30), size=wx.Size(130, 18), style=wx.RB_GROUP)
        self.definirCubierta.Bind(wx.EVT_RADIOBUTTON, self.OndefinirCubierta, id=wxID_PANEL1DEFINIRCUBIERTA)
        self.definirFachada = wx.RadioButton(id=wxID_PANEL1DEFINIRFACHADA, label=_('Muro'), name='definirFachada', parent=self, pos=wx.Point(20, 60), size=wx.Size(130, 18), style=0)
        self.definirFachada.SetValue(True)
        self.definirFachada.Bind(wx.EVT_RADIOBUTTON, self.OndefinirFachada, id=wxID_PANEL1DEFINIRFACHADA)
        self.definirSuelo = wx.RadioButton(id=wxID_PANEL1DEFINIRSUELO, label=_('Suelo'), name='definirSuelo', parent=self, pos=wx.Point(20, 90), size=wx.Size(130, 18), style=0)
        self.definirSuelo.Bind(wx.EVT_RADIOBUTTON, self.OndefinirSuelo, id=wxID_PANEL1DEFINIRSUELO)
        self.definirParticionInterior = wx.RadioButton(id=wxID_PANEL1DEFINIRPARTICIONINTERIOR, label=_('Partición interior'), name='definirParticionInterior', parent=self, pos=wx.Point(20, 120), size=wx.Size(130, 18), style=0)
        self.definirParticionInterior.Bind(wx.EVT_RADIOBUTTON, self.OndefinirParticionInterior, id=wxID_PANEL1DEFINIRPARTICIONINTERIOR)
        self.definirHueco = wx.RadioButton(id=wxID_PANEL1DEFINIRHUECO, label=_('Hueco/Lucernario'), name='definirHueco', parent=self, pos=wx.Point(20, 150), size=wx.Size(130, 18), style=0)
        self.definirHueco.Bind(wx.EVT_RADIOBUTTON, self.OndefinirHueco, id=wxID_PANEL1DEFINIRHUECO)
        self.definirPuenteTermico = wx.RadioButton(id=wxID_PANEL1DEFINIRPUENTETERMICO, label=_('Puente térmico'), name='definirPuenteTermico', parent=self, pos=wx.Point(20, 180), size=wx.Size(130, 18), style=0)
        self.definirPuenteTermico.Bind(wx.EVT_RADIOBUTTON, self.OnpuentesTermicosDefectoBoton, id=wxID_PANEL1DEFINIRPUENTETERMICO)
        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(Directorio + '/Imagenes/muroFachada.jpg', wx.BITMAP_TYPE_JPEG), id=wxID_PANEL1STATICBITMAP1, name='staticBitmap1', parent=self, pos=wx.Point(500, 0), size=wx.Size(200, 200), style=0)
        self.contactoSuelo = wx.RadioButton(id=wxID_PANEL1CONTACTOSUELO, label=_('En contacto con el terreno'), name='contactoSuelo', parent=self, pos=wx.Point(150, 60), size=wx.Size(168, 18), style=wx.RB_GROUP)
        self.contactoSuelo.SetValue(False)
        self.contactoSuelo.Bind(wx.EVT_RADIOBUTTON, self.OncontactoSuelo, id=wxID_PANEL1CONTACTOSUELO)
        self.contactoAire = wx.RadioButton(id=wxID_PANEL1CONTACTOAIRE, label=_('De fachada'), name='contactoAire', parent=self, pos=wx.Point(150, 78), size=wx.Size(168, 18), style=0)
        self.contactoAire.SetValue(True)
        self.contactoAire.Bind(wx.EVT_RADIOBUTTON, self.OnContactoAire, id=wxID_PANEL1CONTACTOAIRE)
        self.contactoEdificio = wx.RadioButton(id=wxID_PANEL1CONTACTOEDIFICIO, label=_('Medianería'), name='contactoEdificio', parent=self, pos=wx.Point(150, 96), size=wx.Size(168, 18), style=0)
        self.contactoEdificio.Bind(wx.EVT_RADIOBUTTON, self.OnContactoEdificio, id=wxID_PANEL1CONTACTOEDIFICIO)
        self.contactoEdificio.Show(True)
        self.vertical = wx.RadioButton(id=wxID_PANEL1VERTICAL, label=_('Vertical'), name='vertical', parent=self, pos=wx.Point(150, 120), size=wx.Size(250, 18), style=wx.RB_GROUP)
        self.vertical.SetValue(True)
        self.vertical.Bind(wx.EVT_RADIOBUTTON, self.OnVerticalRadio, id=wxID_PANEL1VERTICAL)
        self.vertical.Show(False)
        self.horizontalSuperior = wx.RadioButton(id=wxID_PANEL1HORIZONTALSUP, label=_('Horizontal en contacto con espacio NH superior'), name='horizontalSuperior', parent=self, pos=wx.Point(150, 138), size=wx.Size(250, 18), style=0)
        self.horizontalSuperior.Bind(wx.EVT_RADIOBUTTON, self.OnHorizontalSuperior, id=wxID_PANEL1HORIZONTALSUP)
        self.horizontalSuperior.Show(False)
        self.horizontalInferior = wx.RadioButton(id=wxID_PANEL1HORIZONTALINF, label=_('Horizontal en contacto con espacio NH inferior'), name='horizontalInferior', parent=self, pos=wx.Point(150, 156), size=wx.Size(250, 18), style=0)
        self.horizontalInferior.Bind(wx.EVT_RADIOBUTTON, self.OnHorizontalInferior, id=wxID_PANEL1HORIZONTALINF)
        self.horizontalInferior.Show(False)
        self.puentesTermicosDefecto = wx.Button(id=wxID_PANEL1PTDEFECTOBOTON, label=_('Por defecto'), name='puentesTermicosDefecto', parent=self, pos=wx.Point(150, 180), size=wx.Size(140, 18), style=0)
        self.puentesTermicosDefecto.Show(False)
        self.puentesTermicosDefecto.Bind(wx.EVT_BUTTON, self.OnpuentesTermicosDefectoBoton, id=wxID_PANEL1PTDEFECTOBOTON)
        self.puentesTermicosUsuario = wx.Button(id=wxID_PANEL1PTUSUARIO, label=_('Definidos por usuario'), name='puentesTermicosUsuario', parent=self, pos=wx.Point(150, 180), size=wx.Size(140, 18), style=0)
        self.puentesTermicosUsuario.Show(False)
        self.puentesTermicosUsuario.Bind(wx.EVT_BUTTON, self.OndefinirPuenteTermico, id=wxID_PANEL1PTUSUARIO)
        self.staticLine = wx.StaticLine(id=wxID_WXPANEL1STATICLINE, name='staticLine', parent=self, pos=wx.Point(0, 202), size=wx.Size(710, 3), style=0)
        self.staticLine.SetBackgroundColour(wx.Colour(0, 64, 128))
        colorSombra = wx.Color(240, 240, 240)
        colorNormal = wx.Color(255, 255, 255)
        self.contactoSuelo.SetBackgroundColour(colorSombra)
        self.contactoAire.SetBackgroundColour(colorSombra)
        self.contactoEdificio.SetBackgroundColour(colorSombra)
        self.horizontalSuperior.SetBackgroundColour(colorSombra)
        self.horizontalInferior.SetBackgroundColour(colorSombra)
        self.vertical.SetBackgroundColour(colorSombra)
        self.definirSuelo.SetBackgroundColour(colorNormal)
        self.definirCubierta.SetBackgroundColour(colorNormal)
        self.definirFachada.SetBackgroundColour(colorSombra)
        self.definirParticionInterior.SetBackgroundColour(colorNormal)
        self.definirHueco.SetBackgroundColour(colorNormal)
        self.definirPuenteTermico.SetBackgroundColour(colorNormal)
        self.definirCubierta.Bind(wx.EVT_SET_FOCUS, self.manejadorElegirObjeto, id=wxID_PANEL1DEFINIRCUBIERTA)
        self.definirFachada.Bind(wx.EVT_SET_FOCUS, self.manejadorElegirObjeto, id=wxID_PANEL1DEFINIRFACHADA)
        self.definirSuelo.Bind(wx.EVT_SET_FOCUS, self.manejadorElegirObjeto, id=wxID_PANEL1DEFINIRSUELO)
        self.definirParticionInterior.Bind(wx.EVT_SET_FOCUS, self.manejadorElegirObjeto, id=wxID_PANEL1DEFINIRPARTICIONINTERIOR)
        self.definirHueco.Bind(wx.EVT_SET_FOCUS, self.manejadorElegirObjeto, id=wxID_PANEL1DEFINIRHUECO)
        self.definirPuenteTermico.Bind(wx.EVT_SET_FOCUS, self.manejadorElegirObjeto, id=wxID_PANEL1DEFINIRPUENTETERMICO)
        self.contactoSuelo.Bind(wx.EVT_SET_FOCUS, self.manejadorElegirObjeto, id=wxID_PANEL1CONTACTOSUELO)
        self.contactoAire.Bind(wx.EVT_SET_FOCUS, self.manejadorElegirObjeto, id=wxID_PANEL1CONTACTOAIRE)
        self.contactoEdificio.Bind(wx.EVT_SET_FOCUS, self.manejadorElegirObjeto, id=wxID_PANEL1CONTACTOEDIFICIO)
        self.vertical.Bind(wx.EVT_SET_FOCUS, self.manejadorElegirObjeto, id=wxID_PANEL1VERTICAL)
        self.horizontalSuperior.Bind(wx.EVT_SET_FOCUS, self.manejadorElegirObjeto, id=wxID_PANEL1HORIZONTALSUP)
        self.horizontalInferior.Bind(wx.EVT_SET_FOCUS, self.manejadorElegirObjeto, id=wxID_PANEL1HORIZONTALINF)

    def actualizaDiccionario(self):
        self.diccionario = {}
        lista = self.GetRadioValues()
        lista.pop(-1)
        self.diccionario['panelDefinirEnvolvente.radios'] = lista

    def GetRadioValues(self):
        if self.definirCubierta.GetValue() == True:
            obj = self.definirCubierta
        elif self.definirFachada.GetValue() == True:
            obj = self.definirFachada
        elif self.definirSuelo.GetValue() == True:
            obj = self.definirSuelo
        elif self.definirParticionInterior.GetValue() == True:
            obj = self.definirParticionInterior
        elif self.definirHueco.GetValue() == True:
            obj = self.definirHueco
        elif self.definirPuenteTermico.GetValue() == True:
            obj = self.definirPuenteTermico
        return [
         self.definirCubierta.GetValue(),
         self.definirFachada.GetValue(),
         self.definirSuelo.GetValue(),
         self.definirParticionInterior.GetValue(),
         self.definirHueco.GetValue(),
         self.definirPuenteTermico.GetValue(),
         self.contactoSuelo.GetValue(),
         self.contactoAire.GetValue(),
         self.contactoEdificio.GetValue(),
         self.vertical.GetValue(),
         self.horizontalSuperior.GetValue(),
         self.horizontalInferior.GetValue(),
         obj]

    def SetRadioValues(self, lista):
        self.definirCubierta.SetValue(lista[0])
        self.definirFachada.SetValue(lista[1])
        self.definirSuelo.SetValue(lista[2])
        self.definirParticionInterior.SetValue(lista[3])
        self.definirHueco.SetValue(lista[4])
        self.definirPuenteTermico.SetValue(lista[5])
        self.contactoSuelo.SetValue(lista[6])
        self.contactoAire.SetValue(lista[7])
        self.contactoEdificio.SetValue(lista[8])
        self.vertical.SetValue(lista[9])
        self.horizontalSuperior.SetValue(lista[10])
        self.horizontalInferior.SetValue(lista[11])

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
        self.actualizaDiccionario()

    def OnVerticalRadio(self, event):
        """
        Metodo: OnVerticalRadio

        ARGUMENTOS:
                event:
        """
        self.puentesTermicosDefecto.Show(False)
        self.puentesTermicosUsuario.Show(False)
        self.mostrarOpcionesContactoParticion()
        self.parent.panelRecuadro.titulo.SetLabel(_('Partición interior vertical'))
        self.parent.panel2.Destroy()
        self.parent.panel2 = panelParticionVertical.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
        self.parent.panel2.SetSize(wx.Size(770, 350))
        imagen = wx.Image(Directorio + '/Imagenes/PI_Vertical.jpg', wx.BITMAP_TYPE_JPEG)
        self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
        tips.tipsOnVertical(self.parent.parent.parent)

    def OnHorizontalSuperior(self, event):
        """
        Metodo: OnHorizontalSuperior

        ARGUMENTOS:
                event:
        """
        self.puentesTermicosDefecto.Show(False)
        self.puentesTermicosUsuario.Show(False)
        self.mostrarOpcionesContactoParticion()
        self.parent.panelRecuadro.titulo.SetLabel(_('Partición interior horizontal en contacto con espacio NH superior'))
        self.parent.panel2.Destroy()
        self.parent.panel2 = panelParticionHorizontalSuperior.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
        self.parent.panel2.SetSize(wx.Size(770, 350))
        imagen = wx.Image(Directorio + '/Imagenes/PI_Horizontal_Superior.jpg', wx.BITMAP_TYPE_JPEG)
        self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
        tips.tipsOnHorizontalSuperior(self.parent.parent.parent)

    def OnHorizontalInferior(self, event):
        """
        Metodo: OnHorizontalInferior

        ARGUMENTOS:
                event:
        """
        self.puentesTermicosDefecto.Show(False)
        self.puentesTermicosUsuario.Show(False)
        self.mostrarOpcionesContactoParticion()
        self.parent.panelRecuadro.titulo.SetLabel(_('Partición interior horizontal en contacto con espacio NH inferior'))
        self.parent.panel2.Destroy()
        self.parent.panel2 = panelParticionHorizontalInferior.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
        self.parent.panel2.SetSize(wx.Size(770, 350))
        imagen = wx.Image(Directorio + '/Imagenes/PI_Horizontal_Inferior.jpg', wx.BITMAP_TYPE_JPEG)
        self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
        tips.tipsOnHorizontalInferior(self.parent.parent.parent)

    def OndefinirParticionInterior(self, event):
        """
        Metodo: OndefinirParticionInterior

        ARGUMENTOS:
                event:
        """
        self.puentesTermicosDefecto.Show(False)
        self.puentesTermicosUsuario.Show(False)
        colorSombra = wx.Color(240, 240, 240)
        colorNormal = wx.Color(255, 255, 255)
        self.definirSuelo.SetBackgroundColour(colorNormal)
        self.definirCubierta.SetBackgroundColour(colorNormal)
        self.definirFachada.SetBackgroundColour(colorNormal)
        self.definirParticionInterior.SetBackgroundColour(colorSombra)
        self.definirHueco.SetBackgroundColour(colorNormal)
        self.definirPuenteTermico.SetBackgroundColour(colorNormal)
        self.mostrarOpcionesContactoParticion()
        if self.vertical.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Partición interior vertical'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelParticionVertical.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            imagen = wx.Image(Directorio + '/Imagenes/PI_Vertical.jpg', wx.BITMAP_TYPE_JPEG)
            self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
            tips.tipsOnVertical(self.parent.parent.parent)
        elif self.horizontalSuperior.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Partición interior horizontal en contacto con espacio NH superior'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelParticionHorizontalSuperior.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            imagen = wx.Image(Directorio + '/Imagenes/PI_Horizontal_Superior.jpg', wx.BITMAP_TYPE_JPEG)
            self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
            tips.tipsOnHorizontalSuperior(self.parent.parent.parent)
        elif self.horizontalInferior.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Partición interior horizontal en contacto con espacio NH inferior'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelParticionHorizontalInferior.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            imagen = wx.Image(Directorio + '/Imagenes/PI_Horizontal_Inferior.jpg', wx.BITMAP_TYPE_JPEG)
            self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
            tips.tipsOnHorizontalInferior(self.parent.parent.parent)

    def OnpuentesTermicosDefectoBoton(self, event):
        """
        Metodo: OnpuentesTermicosDefectoBoton

        ARGUMENTOS:
                event:
        """
        self.noMostrarOpcionesContacto()
        colorSombra = wx.Color(240, 240, 240)
        colorNormal = wx.Color(255, 255, 255)
        self.definirSuelo.SetBackgroundColour(colorNormal)
        self.definirCubierta.SetBackgroundColour(colorNormal)
        self.definirFachada.SetBackgroundColour(colorNormal)
        self.definirParticionInterior.SetBackgroundColour(colorNormal)
        self.definirHueco.SetBackgroundColour(colorNormal)
        self.definirPuenteTermico.SetBackgroundColour(colorSombra)
        self.puentesTermicosDefecto.Show(False)
        self.puentesTermicosUsuario.Show(True)
        self.parent.panelRecuadro.titulo.SetLabel(_('Puente térmico por defecto'))
        self.parent.panel2.Destroy()
        self.parent.panel2 = panelPuentesTermicosPorDefecto.panelPuentesTermicosPorDefecto(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
        self.parent.panel2.SetSize(wx.Size(770, 350))
        self.parent.panelBotones.anadirBoton.Show(False)
        self.parent.panelBotones.modificarBoton.Show(False)
        self.parent.panelBotones.borrarBoton.Show(False)
        imagen = wx.Image(Directorio + '/Imagenes/puenteTermico.jpg', wx.BITMAP_TYPE_JPEG)
        self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
        tips.tipsOnpuentesTermicosDefectoBoton(self.parent.parent.parent)

    def OndefinirFachada(self, event):
        """
        Metodo: OndefinirFachada

        ARGUMENTOS:
                event:
        """
        self.puentesTermicosDefecto.Show(False)
        self.puentesTermicosUsuario.Show(False)
        colorSombra = wx.Color(240, 240, 240)
        colorNormal = wx.Color(255, 255, 255)
        self.definirSuelo.SetBackgroundColour(colorNormal)
        self.definirCubierta.SetBackgroundColour(colorNormal)
        self.definirFachada.SetBackgroundColour(colorSombra)
        self.definirParticionInterior.SetBackgroundColour(colorNormal)
        self.definirHueco.SetBackgroundColour(colorNormal)
        self.definirPuenteTermico.SetBackgroundColour(colorNormal)
        self.mostrarOpcionesContacto()
        if self.contactoAire.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Muro de fachada'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelFachadaConAire.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            imagen = wx.Image(Directorio + '/Imagenes/muroFachada.jpg', wx.BITMAP_TYPE_JPEG)
            self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
            tips.tipsOnFachadaConAire(self.parent.parent.parent)
        elif self.contactoSuelo.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Muro en contacto con el terreno'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelFachadaConTerreno.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            imagen = wx.Image(Directorio + '/Imagenes/muroTerreno.jpg', wx.BITMAP_TYPE_JPEG)
            self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
            tips.tipsOnFachadaConTerreno(self.parent.parent.parent)
        elif self.contactoEdificio.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Medianería'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelFachadaConEdificio.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            imagen = wx.Image(Directorio + '/Imagenes/Medianeria.jpg', wx.BITMAP_TYPE_JPEG)
            self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
            tips.tipsOnFachadaConEdificio(self.parent.parent.parent)

    def OndefinirCubierta(self, event):
        """
        Metodo: OndefinirCubierta

        ARGUMENTOS:
                event:
        """
        self.puentesTermicosDefecto.Show(False)
        self.puentesTermicosUsuario.Show(False)
        colorSombra = wx.Color(240, 240, 240)
        colorNormal = wx.Color(255, 255, 255)
        self.definirSuelo.SetBackgroundColour(colorNormal)
        self.definirCubierta.SetBackgroundColour(colorSombra)
        self.definirFachada.SetBackgroundColour(colorNormal)
        self.definirParticionInterior.SetBackgroundColour(colorNormal)
        self.definirHueco.SetBackgroundColour(colorNormal)
        self.definirPuenteTermico.SetBackgroundColour(colorNormal)
        self.mostrarOpcionesContactoCubierta()
        if self.contactoAire.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Cubierta en contacto con el aire'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelCubiertaConAire.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            imagen = wx.Image(Directorio + '/Imagenes/cubiertaAire.jpg', wx.BITMAP_TYPE_JPEG)
            self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
            tips.tipsOndefinirCubiertaConAire(self.parent.parent.parent)
        elif self.contactoSuelo.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Cubierta enterrada'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelCubiertaConTerreno.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            imagen = wx.Image(Directorio + '/Imagenes/cubiertaTerreno.jpg', wx.BITMAP_TYPE_JPEG)
            self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
            tips.tipsOndefinirCubiertaTerreno(self.parent.parent.parent)

    def OndefinirSuelo(self, event):
        """
        Metodo: OndefinirSuelo

        ARGUMENTOS:
                event:
        """
        self.puentesTermicosDefecto.Show(False)
        self.puentesTermicosUsuario.Show(False)
        colorSombra = wx.Color(240, 240, 240)
        colorNormal = wx.Color(255, 255, 255)
        self.definirSuelo.SetBackgroundColour(colorSombra)
        self.definirCubierta.SetBackgroundColour(colorNormal)
        self.definirFachada.SetBackgroundColour(colorNormal)
        self.definirParticionInterior.SetBackgroundColour(colorNormal)
        self.definirHueco.SetBackgroundColour(colorNormal)
        self.definirPuenteTermico.SetBackgroundColour(colorNormal)
        self.mostrarOpcionesContactoCubierta()
        if self.contactoAire.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Suelo en contacto con el aire exterior'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelSueloConAire.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            imagen = wx.Image(Directorio + '/Imagenes/sueloAire.jpg', wx.BITMAP_TYPE_JPEG)
            self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
            tips.tipsOnSueloConAire(self.parent.parent.parent)
        elif self.contactoSuelo.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Suelo en contacto con el terreno'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelSueloConTerreno.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            imagen = wx.Image(Directorio + '/Imagenes/sueloTerreno.jpg', wx.BITMAP_TYPE_JPEG)
            self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
            tips.tipsOndefinirSueloTerreno(self.parent.parent.parent)

    def OndefinirHueco(self, event):
        """
        Metodo: OndefinirHueco

        ARGUMENTOS:
                event:
        """
        self.puentesTermicosDefecto.Show(False)
        self.puentesTermicosUsuario.Show(False)
        colorSombra = wx.Color(240, 240, 240)
        colorNormal = wx.Color(255, 255, 255)
        self.definirSuelo.SetBackgroundColour(colorNormal)
        self.definirCubierta.SetBackgroundColour(colorNormal)
        self.definirFachada.SetBackgroundColour(colorNormal)
        self.definirParticionInterior.SetBackgroundColour(colorNormal)
        self.definirHueco.SetBackgroundColour(colorSombra)
        self.definirPuenteTermico.SetBackgroundColour(colorNormal)
        self.noMostrarOpcionesContacto()
        self.parent.panelRecuadro.titulo.SetLabel(_('Hueco/Lucernario'))
        self.parent.panel2.Destroy()
        self.parent.panel2 = panelHuecos.panelHuecos(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
        self.parent.panel2.SetSize(wx.Size(770, 350))
        imagen = wx.Image(Directorio + '/Imagenes/huecoLucernario.jpg', wx.BITMAP_TYPE_JPEG)
        self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
        tips.tipsOndefinirHueco(self.parent.parent.parent)

    def OndefinirPuenteTermico(self, event):
        """
        Metodo: OndefinirPuenteTermico

        ARGUMENTOS:
                event:
        """
        self.puentesTermicosDefecto.Show(True)
        self.puentesTermicosUsuario.Show(False)
        self.noMostrarOpcionesContacto()
        colorSombra = wx.Color(240, 240, 240)
        colorNormal = wx.Color(255, 255, 255)
        self.definirSuelo.SetBackgroundColour(colorNormal)
        self.definirCubierta.SetBackgroundColour(colorNormal)
        self.definirFachada.SetBackgroundColour(colorNormal)
        self.definirParticionInterior.SetBackgroundColour(colorNormal)
        self.definirHueco.SetBackgroundColour(colorNormal)
        self.definirPuenteTermico.SetBackgroundColour(colorSombra)
        self.parent.panelRecuadro.titulo.SetLabel(_('Puente térmico'))
        self.parent.panel2.Destroy()
        self.parent.panel2 = panelPuentesTermicos.panelPuentesTermicos(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
        self.parent.panel2.SetSize(wx.Size(770, 350))
        imagen = wx.Image(Directorio + '/Imagenes/puenteTermico.jpg', wx.BITMAP_TYPE_JPEG)
        self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
        tips.tipsOnpuentesTermicosBoton(self.parent.parent.parent)

    def OnContactoAire(self, event):
        """
        Metodo: OnContactoAire

        ARGUMENTOS:
                event:
        """
        if self.definirCubierta.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Cubierta en contacto con el aire'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelCubiertaConAire.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            imagen = wx.Image(Directorio + '/Imagenes/cubiertaAire.jpg', wx.BITMAP_TYPE_JPEG)
            self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
            tips.tipsOndefinirCubiertaConAire(self.parent.parent.parent)
        elif self.definirFachada.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Muro de fachada'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelFachadaConAire.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            imagen = wx.Image(Directorio + '/Imagenes/muroFachada.jpg', wx.BITMAP_TYPE_JPEG)
            self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
            tips.tipsOnFachadaConAire(self.parent.parent.parent)
        elif self.definirSuelo.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Suelo en contacto con el aire exterior'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelSueloConAire.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            imagen = wx.Image(Directorio + '/Imagenes/sueloAire.jpg', wx.BITMAP_TYPE_JPEG)
            self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
            tips.tipsOnSueloConAire(self.parent.parent.parent)

    def OncontactoSuelo(self, event):
        """
        Metodo: OncontactoSuelo

        ARGUMENTOS:
                event:
        """
        if self.definirCubierta.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Cubierta enterrada'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelCubiertaConTerreno.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            imagen = wx.Image(Directorio + '/Imagenes/cubiertaTerreno.jpg', wx.BITMAP_TYPE_JPEG)
            self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
            tips.tipsOndefinirCubiertaTerreno(self.parent.parent.parent)
        elif self.definirFachada.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Muro en contacto con el terreno'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelFachadaConTerreno.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            imagen = wx.Image(Directorio + '/Imagenes/muroTerreno.jpg', wx.BITMAP_TYPE_JPEG)
            self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
            tips.tipsOnFachadaConTerreno(self.parent.parent.parent)
        elif self.definirSuelo.GetValue() == True:
            self.parent.panelRecuadro.titulo.SetLabel(_('Suelo en contacto con el terreno'))
            self.parent.panel2.Destroy()
            self.parent.panel2 = panelSueloConTerreno.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
            self.parent.panel2.SetSize(wx.Size(770, 350))
            imagen = wx.Image(Directorio + '/Imagenes/sueloTerreno.jpg', wx.BITMAP_TYPE_JPEG)
            self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
            tips.tipsOndefinirSueloTerreno(self.parent.parent.parent)

    def OnContactoEdificio(self, event):
        """
        Metodo: OnContactoEdificio

        ARGUMENTOS:
                event:
        """
        self.parent.panelRecuadro.titulo.SetLabel(_('Medianería'))
        self.parent.panel2.Destroy()
        self.parent.panel2 = panelFachadaConEdificio.Panel1(parent=self.parent, id=-1, pos=wx.Point(230, 250), size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL, name='')
        self.parent.panel2.SetSize(wx.Size(770, 350))
        imagen = wx.Image(Directorio + '/Imagenes/Medianeria.jpg', wx.BITMAP_TYPE_JPEG)
        self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagen))
        tips.tipsOnFachadaConEdificio(self.parent.parent.parent)

    def ponerEtiquetasSituacionCerramientos(self):
        """
        Metodo: ponerEtiquetasSituacionCerramientos

        """
        if self.definirCubierta.GetValue() == True:
            self.contactoAire.SetLabel(_('En contacto con el aire'))
            self.contactoAire.Move(wx.Point(150, 48))
            self.contactoSuelo.SetLabel(_('Enterrada'))
            self.contactoSuelo.Move(wx.Point(150, 30))
        elif self.definirFachada.GetValue() == True:
            self.contactoAire.SetLabel(_('De fachada'))
            self.contactoAire.Move(wx.Point(150, 78))
            self.contactoSuelo.SetLabel(_('En contacto con el terreno'))
            self.contactoSuelo.Move(wx.Point(150, 60))
            self.contactoEdificio.SetLabel(_('Medianería'))
            self.contactoEdificio.Move(wx.Point(150, 96))
        elif self.definirSuelo.GetValue() == True:
            self.contactoAire.SetLabel(_('En contacto con el aire exterior'))
            self.contactoAire.Move(wx.Point(150, 108))
            self.contactoSuelo.SetLabel(_('En contacto con el terreno'))
            self.contactoSuelo.Move(wx.Point(150, 90))

    def mostrarOpcionesContactoCubierta(self):
        """
        Metodo: mostrarOpcionesContactoCubierta

        """
        self.ponerEtiquetasSituacionCerramientos()
        self.contactoSuelo.Show(True)
        if self.contactoAire.GetValue() == False and self.contactoSuelo.GetValue() == False:
            self.contactoAire.SetValue(True)
        self.contactoAire.Show(True)
        self.contactoEdificio.Show(False)
        self.vertical.Show(False)
        self.horizontalSuperior.Show(False)
        self.horizontalInferior.Show(False)
        self.parent.panelBotones.anadirBoton.Show(True)
        self.parent.panelBotones.modificarBoton.Show(True)
        self.parent.panelBotones.borrarBoton.Show(True)

    def mostrarOpcionesContacto(self):
        """
        Metodo: mostrarOpcionesContacto

        """
        self.ponerEtiquetasSituacionCerramientos()
        self.contactoSuelo.Show(True)
        self.contactoAire.Show(True)
        self.contactoEdificio.Show(True)
        self.vertical.Show(False)
        self.horizontalSuperior.Show(False)
        self.horizontalInferior.Show(False)
        self.parent.panelBotones.anadirBoton.Show(True)
        self.parent.panelBotones.modificarBoton.Show(True)
        self.parent.panelBotones.borrarBoton.Show(True)

    def noMostrarOpcionesContacto(self):
        """
        Metodo: noMostrarOpcionesContacto

        """
        self.contactoSuelo.Show(False)
        self.contactoAire.Show(False)
        self.contactoEdificio.Show(False)
        self.vertical.Show(False)
        self.horizontalSuperior.Show(False)
        self.horizontalInferior.Show(False)
        self.parent.panelBotones.anadirBoton.Show(True)
        self.parent.panelBotones.modificarBoton.Show(True)
        self.parent.panelBotones.borrarBoton.Show(True)

    def mostrarOpcionesContactoParticion(self):
        """
        Metodo: mostrarOpcionesContactoParticion

        """
        self.contactoSuelo.Show(False)
        self.contactoAire.Show(False)
        self.contactoEdificio.Show(False)
        self.vertical.Show(True)
        self.horizontalSuperior.Show(True)
        self.horizontalInferior.Show(True)
        self.parent.panelBotones.anadirBoton.Show(True)
        self.parent.panelBotones.modificarBoton.Show(True)
        self.parent.panelBotones.borrarBoton.Show(True)