# Embedded file name: PatronesSombra\ayudaObstaculos.pyc
"""
Modulo: ayudaObstaculos.py

Modulo para facilitar la introducci\xf3n de
Obst\xe1culos remotos de forma simplificada
"""
from Instalaciones.comprobarCampos import Comprueba
from miChoice import MiChoice
import directorios
import Calculos.listadosWeb as listadosWeb
import math
import wx
Directorio = directorios.BuscaDirectorios().Directorio

def create(parent):
    """
    Metodo: create
    Devuelve una instancia de la clase Dialog1()
    
    ARGUMENTOS:
                parent:
    
    
    """
    return Dialog1(parent)


wxID_DIALOG1, wxID_DIALOG1ACEPTARBOTON, wxID_DIALOG1ACIMUT1TEXT, wxID_DIALOG1ACIMUT1TEXTCTRL, wxID_DIALOG1ACIMUT2TEXT, wxID_DIALOG1ACIMUT2TEXTCTRL, wxID_DIALOG1ACIMUT3TEXT, wxID_DIALOG1ACIMUT3TEXTCTRL, wxID_DIALOG1ACIMUT4TEXT, wxID_DIALOG1ACIMUT4TEXTCTRL, wxID_DIALOG1AYUDAOBSTACULOSTEXT, wxID_DIALOG1CANCELARBOTON, wxID_DIALOG1D1TEXT, wxID_DIALOG1D1TEXTCTRL, wxID_DIALOG1D2TEXT, wxID_DIALOG1D2TEXTCTRL, wxID_DIALOG1DTEXT, wxID_DIALOG1DTEXTCTRL, wxID_DIALOG1ELEVACION1TEXT, wxID_DIALOG1ELEVACION1TEXTCTRL, wxID_DIALOG1ELEVACION2TEXT, wxID_DIALOG1ELEVACION2TEXTCTRL, wxID_DIALOG1ELEVACION3TEXT, wxID_DIALOG1ELEVACION3TEXTCTRL, wxID_DIALOG1ELEVACION4TEXT, wxID_DIALOG1ELEVACION4TEXTCTRL, wxID_DIALOG1ELEVACIOND1TEXT, wxID_DIALOG1ELEVACIOND2TEXT, wxID_DIALOG1ELEVACIONDTEXT, wxID_DIALOG1GRADOSD1TEXT, wxID_DIALOG1GRADOSD2TEXT, wxID_DIALOG1GRADOSDTEXT, wxID_DIALOG1MD1TEXT, wxID_DIALOG1MD2TEXT, wxID_DIALOG1MTEXT, wxID_DIALOG1ORIENTACIONCHOICE, wxID_DIALOG1ORIENTACIONTEXT, wxID_DIALOG1TEXTCTRL4, wxID_DIALOG1TEXTCTRL5, wxID_DIALOG1TEXTCTRL6, wxID_PANELIMAGEN, wxID_DIALOG1OBSTACULOREMOTOTEXT, wxID_DIALOG1EDIFICIOOBJETOTEXT, wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICTEXT2, wxID_PANEL1ACIMUT1TEXTUNIDADES, wxID_PANEL1ACIMUT2TEXTUNIDADES, wxID_PANEL1ACIMUT3TEXTUNIDADES, wxID_PANEL1ACIMUT4TEXTUNIDADES, wxID_PANEL1ELEVACION1TEXTUNIDADES, wxID_PANEL1ELEVACION2TEXTUNIDADES, wxID_PANEL1ELEVACION3TEXTUNIDADES, wxID_PANEL1ELEVACION4TEXTUNIDADES = [ wx.NewId() for _init_ctrls in range(53) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo ayudaObstaculos.py
    
    Ventana de ayuda para introducir obst\xe1culos rectangulares
    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls
        Iniciaci\xf3n de elementos gr\xe1ficos
        
        ARGUMENTOS:
                prnt:
        
        
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(521, 144), size=wx.Size(690, 555), style=wx.DEFAULT_DIALOG_STYLE, title=_(u'Ayuda para la definici\xf3n de obst\xe1culos rectangulares'))
        self.SetClientSize(wx.Size(674, 519))
        self.SetBackgroundColour('white')
        self.ayudaObstaculosText = wx.StaticText(id=wxID_DIALOG1AYUDAOBSTACULOSTEXT, label=_(u'Obst\xe1culos rectangulares'), name=u'ayudaObstaculosText', parent=self, pos=wx.Point(15, 10), size=wx.Size(178, 16), style=0)
        self.ayudaObstaculosText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, u''))
        self.ayudaObstaculosText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticText1 = wx.StaticBox(id=wxID_DIALOG1STATICTEXT1, label=_(u'Definici\xf3n del obst\xe1culo rectangular'), name='datosGeneralesText', parent=self, pos=wx.Point(15, 41), size=wx.Size(644, 273), style=0)
        self.staticText1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticText1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.imagen = wx.StaticBitmap(bitmap=wx.Bitmap(Directorio + '/Imagenes/ayudaSombras.jpg', wx.BITMAP_TYPE_JPEG), id=wxID_PANELIMAGEN, name='imagen', parent=self, pos=wx.Point(20, 66), size=wx.Size(353, 223), style=0)
        self.obstaculoRemotoParaleloText = wx.StaticText(id=wxID_DIALOG1OBSTACULOREMOTOTEXT, label=_(u'Obst\xe1culos rectangulares'), name=u'obstaculoRemotoParaleloText', parent=self, pos=wx.Point(77, 289), size=wx.Size(126, 13), style=0)
        self.obstaculoRemotoParaleloText.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Tahoma'))
        self.edificioObjetoText = wx.StaticText(id=wxID_DIALOG1EDIFICIOOBJETOTEXT, label=_(u'Edificio objeto'), name=u'edificioObjetoText', parent=self, pos=wx.Point(266, 289), size=wx.Size(96, 13), style=0)
        self.edificioObjetoText.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Tahoma'))
        self.orientacionText = wx.StaticText(id=wxID_DIALOG1ORIENTACIONTEXT, label=_(u'Orientaci\xf3n'), name=u'orientacionText', parent=self, pos=wx.Point(475, 98), size=wx.Size(56, 13), style=0)
        self.orientacionChoice = MiChoice(choices=listadosWeb.listadoOpcionesOrientacionSombras, id=wxID_DIALOG1ORIENTACIONCHOICE, name=u'orientacionChoice', parent=self, pos=wx.Point(543, 96), size=wx.Size(56, 21), style=0)
        self.orientacionChoice.Bind(wx.EVT_CHOICE, self.OnCalculoAngulos, id=wxID_DIALOG1ORIENTACIONCHOICE)
        self.dText = wx.StaticText(id=wxID_DIALOG1DTEXT, label=_(u'd'), name=u'dText', parent=self, pos=wx.Point(475, 128), size=wx.Size(7, 13), style=0)
        self.d1Text = wx.StaticText(id=wxID_DIALOG1D1TEXT, label=_(u'd1'), name=u'd1Text', parent=self, pos=wx.Point(475, 158), size=wx.Size(14, 13), style=0)
        self.d2Text = wx.StaticText(id=wxID_DIALOG1D2TEXT, label=_(u'd2'), name=u'd2Text', parent=self, pos=wx.Point(475, 188), size=wx.Size(14, 13), style=0)
        self.dTextCtrl = wx.TextCtrl(id=wxID_DIALOG1DTEXTCTRL, name=u'dTextCtrl', parent=self, pos=wx.Point(543, 126), size=wx.Size(56, 21), style=0, value=u'')
        self.dTextCtrl.Bind(wx.EVT_TEXT, self.OnCalculoAngulos, id=wxID_DIALOG1DTEXTCTRL)
        self.d1TextCtrl = wx.TextCtrl(id=wxID_DIALOG1D1TEXTCTRL, name=u'd1TextCtrl', parent=self, pos=wx.Point(543, 156), size=wx.Size(56, 21), style=0, value=u'')
        self.d1TextCtrl.Bind(wx.EVT_TEXT, self.OnCalculoAngulos, id=wxID_DIALOG1D1TEXTCTRL)
        self.d2TextCtrl = wx.TextCtrl(id=wxID_DIALOG1D2TEXTCTRL, name=u'D2TextCtrl', parent=self, pos=wx.Point(543, 186), size=wx.Size(56, 21), style=0, value=u'')
        self.d2TextCtrl.Bind(wx.EVT_TEXT, self.OnCalculoAngulos, id=wxID_DIALOG1D2TEXTCTRL)
        self.mText = wx.StaticText(id=wxID_DIALOG1MTEXT, label=_(u'm'), name=u'mText', parent=self, pos=wx.Point(606, 128), size=wx.Size(9, 13), style=0)
        self.mD1Text = wx.StaticText(id=wxID_DIALOG1MD1TEXT, label=_(u'm'), name=u'mD1Text', parent=self, pos=wx.Point(606, 158), size=wx.Size(9, 13), style=0)
        self.mD2Text = wx.StaticText(id=wxID_DIALOG1MD2TEXT, label=_(u'm'), name=u'mD2Text', parent=self, pos=wx.Point(606, 188), size=wx.Size(9, 13), style=0)
        self.elevacionDText = wx.StaticText(id=wxID_DIALOG1ELEVACIONDTEXT, label=_(u'Elevaci\xf3n'), name=u'elevacionDText', parent=self, pos=wx.Point(475, 218), size=wx.Size(54, 13), style=0)
        self.elevacionDTextCtrl = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL4, name='textCtrl4', parent=self, pos=wx.Point(543, 216), size=wx.Size(56, 21), style=0, value=u'')
        self.elevacionDTextCtrl.Bind(wx.EVT_TEXT, self.OnCalculoAngulos, id=wxID_DIALOG1TEXTCTRL4)
        self.elevacionDUnidades = wx.StaticText(id=wxID_DIALOG1GRADOSDTEXT, label=_(u'm'), name=u'elevacionDUnidades', parent=self, pos=wx.Point(606, 218), size=wx.Size(15, 13), style=0)
        self.staticText2 = wx.StaticBox(id=wxID_DIALOG1STATICTEXT2, label=_(u'Pol\xedgono definido'), name='datosGeneralesText', parent=self, pos=wx.Point(15, 329), size=wx.Size(644, 125), style=0)
        self.staticText2.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticText2.SetForegroundColour(wx.Colour(0, 64, 128))
        self.acimut1Text = wx.StaticText(id=wxID_DIALOG1ACIMUT1TEXT, label=_(u'Acimut 1'), name=u'acimut1Text', parent=self, pos=wx.Point(30, 354), size=wx.Size(42, 13), style=0)
        self.acimut2Text = wx.StaticText(id=wxID_DIALOG1ACIMUT2TEXT, label=_(u'Acimut 2'), name=u'acimut2Text', parent=self, pos=wx.Point(30, 379), size=wx.Size(42, 13), style=0)
        self.acimut3Text = wx.StaticText(id=wxID_DIALOG1ACIMUT3TEXT, label=_(u'Acimut 3'), name=u'acimut3Text', parent=self, pos=wx.Point(30, 404), size=wx.Size(42, 13), style=0)
        self.acimut4Text = wx.StaticText(id=wxID_DIALOG1ACIMUT4TEXT, label=_(u'Acimut 4'), name=u'acimut4Text', parent=self, pos=wx.Point(30, 429), size=wx.Size(42, 13), style=0)
        self.acimut1TextCtrl = wx.TextCtrl(id=wxID_DIALOG1ACIMUT1TEXTCTRL, name=u'acimut1TextCtrl', parent=self, pos=wx.Point(80, 352), size=wx.Size(56, 21), style=0, value=u'')
        self.acimut1TextCtrl.Enable(False)
        self.acimut2TextCtrl = wx.TextCtrl(id=wxID_DIALOG1ACIMUT2TEXTCTRL, name=u'acimut2TextCtrl', parent=self, pos=wx.Point(80, 377), size=wx.Size(56, 21), style=0, value=u'')
        self.acimut2TextCtrl.Enable(False)
        self.acimut3TextCtrl = wx.TextCtrl(id=wxID_DIALOG1ACIMUT3TEXTCTRL, name=u'acimut3TextCtrl', parent=self, pos=wx.Point(80, 402), size=wx.Size(56, 21), style=0, value=u'')
        self.acimut3TextCtrl.Enable(False)
        self.acimut4TextCtrl = wx.TextCtrl(id=wxID_DIALOG1ACIMUT4TEXTCTRL, name=u'acimut4TextCtrl', parent=self, pos=wx.Point(80, 427), size=wx.Size(56, 21), style=0, value=u'')
        self.acimut4TextCtrl.Enable(False)
        self.elevacion1Text = wx.StaticText(id=wxID_DIALOG1ELEVACION1TEXT, label=_(u'Elevaci\xf3n 1'), name=u'elevacion1Text', parent=self, pos=wx.Point(240, 354), size=wx.Size(55, 13), style=0)
        self.elevacion2Text = wx.StaticText(id=wxID_DIALOG1ELEVACION2TEXT, label=_(u'Elevaci\xf3n 2'), name=u'elevacion2Text', parent=self, pos=wx.Point(240, 379), size=wx.Size(55, 13), style=0)
        self.elevacion3Text = wx.StaticText(id=wxID_DIALOG1ELEVACION3TEXT, label=_(u'Elevaci\xf3n 3'), name=u'elevacion3Text', parent=self, pos=wx.Point(240, 404), size=wx.Size(55, 13), style=0)
        self.elevacion4Text = wx.StaticText(id=wxID_DIALOG1ELEVACION4TEXT, label=_(u'Elevaci\xf3n 4'), name=u'elevacion4Text', parent=self, pos=wx.Point(240, 429), size=wx.Size(55, 13), style=0)
        self.elevacion1TextCtrl = wx.TextCtrl(id=wxID_DIALOG1ELEVACION1TEXTCTRL, name=u'elevacion1TextCtrl', parent=self, pos=wx.Point(306, 352), size=wx.Size(56, 21), style=0, value=u'')
        self.elevacion1TextCtrl.Enable(False)
        self.elevacion2TextCtrl = wx.TextCtrl(id=wxID_DIALOG1ELEVACION2TEXTCTRL, name=u'elevacion2TextCtrl', parent=self, pos=wx.Point(306, 377), size=wx.Size(56, 21), style=0, value=u'')
        self.elevacion2TextCtrl.Enable(False)
        self.elevacion3TextCtrl = wx.TextCtrl(id=wxID_DIALOG1ELEVACION3TEXTCTRL, name=u'elevacion3TextCtrl', parent=self, pos=wx.Point(306, 402), size=wx.Size(56, 21), style=0, value=u'')
        self.elevacion3TextCtrl.Enable(False)
        self.elevacion4TextCtrl = wx.TextCtrl(id=wxID_DIALOG1ELEVACION4TEXTCTRL, name=u'elevacion4TextCtrl', parent=self, pos=wx.Point(306, 427), size=wx.Size(56, 21), style=0, value=u'')
        self.elevacion4TextCtrl.Enable(False)
        self.aceptarBoton = wx.Button(id=wxID_DIALOG1ACEPTARBOTON, label=_(u'Aceptar'), name=u'aceptarBoton', parent=self, pos=wx.Point(15, 479), size=wx.Size(75, 24), style=0)
        self.aceptarBoton.Bind(wx.EVT_BUTTON, self.OnAceptarButton, id=wxID_DIALOG1ACEPTARBOTON)
        self.cancelarBoton = wx.Button(id=wxID_DIALOG1CANCELARBOTON, label=_(u'Cancelar'), name=u'cancelarBoton', parent=self, pos=wx.Point(105, 479), size=wx.Size(75, 24), style=0)
        self.cancelarBoton.Bind(wx.EVT_BUTTON, self.OnCancelarButton, id=wxID_DIALOG1CANCELARBOTON)
        self.Acimut1TextUnidades = wx.StaticText(id=wxID_PANEL1ACIMUT1TEXTUNIDADES, label=u'\xba', name=u'Acimut1Text', parent=self, pos=wx.Point(141, 354), size=wx.Size(25, 13), style=0)
        self.acimut2TextUnidades = wx.StaticText(id=wxID_PANEL1ACIMUT2TEXTUNIDADES, label=u'\xba', name=u'acimut2Text', parent=self, pos=wx.Point(141, 379), size=wx.Size(25, 13), style=0)
        self.acimut3TextUnidades = wx.StaticText(id=wxID_PANEL1ACIMUT3TEXTUNIDADES, label=u'\xba', name=u'acimut2Text', parent=self, pos=wx.Point(141, 404), size=wx.Size(25, 13), style=0)
        self.acimut4TextUnidades = wx.StaticText(id=wxID_PANEL1ACIMUT4TEXTUNIDADES, label=u'\xba', name=u'acimut2Text', parent=self, pos=wx.Point(141, 429), size=wx.Size(25, 13), style=0)
        self.elevacion1TextUnidades = wx.StaticText(id=wxID_PANEL1ELEVACION1TEXTUNIDADES, label=u'\xba', name=u'elevacion1Text', parent=self, pos=wx.Point(367, 354), size=wx.Size(25, 13), style=0)
        self.elevacion2TextUnidades = wx.StaticText(id=wxID_PANEL1ELEVACION2TEXTUNIDADES, label=u'\xba', name=u'elevacion2Text', parent=self, pos=wx.Point(367, 379), size=wx.Size(25, 13), style=0)
        self.elevacion3TextUnidades = wx.StaticText(id=wxID_PANEL1ELEVACION3TEXTUNIDADES, label=u'\xba', name=u'elevacion2Text', parent=self, pos=wx.Point(367, 404), size=wx.Size(25, 13), style=0)
        self.elevacion4TextUnidades = wx.StaticText(id=wxID_PANEL1ELEVACION4TEXTUNIDADES, label=u'\xba', name=u'elevacion2Text', parent=self, pos=wx.Point(367, 429), size=wx.Size(25, 13), style=0)
        self.orientacionChoice.SetToolTip(wx.ToolTip(_(u'Indique la orientaci\xf3n del obst\xe1culo, visto desde el centro del elemento sombreado.')))
        self.dTextCtrl.SetToolTip(wx.ToolTip(_(u'M\xednima distancia entre el centro del elemento sombreado y el obst\xe1culo.')))
        self.d1TextCtrl.SetToolTip(wx.ToolTip(_(u'Dimensi\xf3n horizontal del obst\xe1culo a la izquierda de la l\xednea de m\xednima distancia.')))
        self.d2TextCtrl.SetToolTip(wx.ToolTip(_(u'Dimensi\xf3n horizontal del obst\xe1culo a la derecha de la l\xednea de m\xednima distancia.')))
        self.elevacionDTextCtrl.SetToolTip(wx.ToolTip(_(u'Dimensi\xf3n vertical del obst\xe1culo medida desde la l\xednea de m\xednima distancia.')))

    def __init__(self, parent):
        """
        Constructor de la clase
        
        
        ARGUMENTOS:
                parent:
        """
        self._init_ctrls(parent)
        self.dev = False
        self.eCentro = 0
        self.aCentro = 0

    def OnAceptarButton(self, event):
        """
        Metodo: OnAceptarButton
        Evento que gestiona la acci\xf3n de hacer click sobre el boton aceptar
        
        ARGUMENTOS:
                event:
        
        
        """
        listaErrores = self.OnComprobarCampos()
        if listaErrores != '':
            wx.MessageBox(_(u'Revise los siguientes campos:\n') + listaErrores, _(u'Aviso'))
            return
        else:
            self.OnCalculoAngulos(None)
            d1 = float(self.d1TextCtrl.GetValue())
            d2 = float(self.d2TextCtrl.GetValue())
            if d1 >= 0 and d2 <= 0 or d1 <= 0 and d2 >= 0:
                self.dev = [[[self.acimut1TextCtrl.GetValue(), self.elevacion1TextCtrl.GetValue()],
                  [self.acimut2TextCtrl.GetValue(), self.elevacion2TextCtrl.GetValue()],
                  [self.acimut3TextCtrl.GetValue(), self.elevacion3TextCtrl.GetValue()],
                  [self.acimut4TextCtrl.GetValue(), self.elevacion4TextCtrl.GetValue()]]]
            else:
                self.dev = [[[self.acimut1TextCtrl.GetValue(), self.elevacion1TextCtrl.GetValue()],
                  [str(self.aCentro), str(self.eCentro)],
                  [str(self.aCentro), '0'],
                  [self.acimut1TextCtrl.GetValue(), '0']], [[str(self.aCentro), str(self.eCentro)],
                  [self.acimut2TextCtrl.GetValue(), self.elevacion2TextCtrl.GetValue()],
                  [self.acimut2TextCtrl.GetValue(), '0'],
                  [str(self.aCentro), '0']]]
            self.Close()
            return

    def OnCancelarButton(self, event):
        """
        Metodo: OnCancelarButton
        Evento que gestiona la acci\xf3n de hacer click sobre el boton cancelar
        
        ARGUMENTOS:
                event:
        
        
        """
        self.dev = False
        self.Close()

    def OnCalculoAngulos(self, event):
        """
        Metodo: OnCalculoAngulos
        Evento  recalcula los valores de los \xe1ngulos de acimut y elevaci\xf3n cada vez que el usuario edita un campo editable
        
        
        ARGUMENTOS:
                event:
        
        """
        a1 = ''
        a2 = ''
        elevacionD = ''
        e1 = ''
        e2 = ''
        try:
            d = float(self.dTextCtrl.GetValue())
            d1 = float(self.d1TextCtrl.GetValue())
            d2 = float(self.d2TextCtrl.GetValue())
            elevacionD = float(self.elevacionDTextCtrl.GetValue())
        except (ValueError, TypeError):
            return

        if self.orientacionChoice.GetStringSelection() == u'Sur':
            d = float(self.dTextCtrl.GetValue())
            d1 = float(self.d1TextCtrl.GetValue())
            d2 = float(self.d2TextCtrl.GetValue())
            a1 = math.atan(-d1 / d) * 180.0 / math.pi
            a2 = math.atan(d2 / d) * 180.0 / math.pi
            self.aCentro = 0
            elevacionD = float(self.elevacionDTextCtrl.GetValue())
            x1 = math.sqrt(d1 ** 2 + d ** 2)
            x2 = math.sqrt(d2 ** 2 + d ** 2)
            e1 = math.atan(elevacionD / x1) * 180.0 / math.pi
            e2 = math.atan(elevacionD / x2) * 180.0 / math.pi
            self.eCentro = math.atan(elevacionD / d) * 180.0 / math.pi
            a1 = round(a1, 1)
            a2 = round(a2, 1)
            e1 = round(e1, 1)
            e2 = round(e2, 1)
            self.eCentro = round(self.eCentro, 1)
        if self.orientacionChoice.GetStringSelection() == u'SE':
            d = float(self.dTextCtrl.GetValue())
            d1 = float(self.d1TextCtrl.GetValue())
            d2 = float(self.d2TextCtrl.GetValue())
            a1 = math.atan(-d1 / d) * 180.0 / math.pi - 45.0
            a2 = math.atan(d2 / d) * 180.0 / math.pi - 45.0
            self.aCentro = -45.0
            elevacionD = float(self.elevacionDTextCtrl.GetValue())
            x1 = math.sqrt(d1 ** 2 + d ** 2)
            x2 = math.sqrt(d2 ** 2 + d ** 2)
            e1 = math.atan(elevacionD / x1) * 180.0 / math.pi
            e2 = math.atan(elevacionD / x2) * 180.0 / math.pi
            self.eCentro = math.atan(elevacionD / d) * 180.0 / math.pi
            a1 = round(a1, 1)
            a2 = round(a2, 1)
            e1 = round(e1, 1)
            e2 = round(e2, 1)
            self.eCentro = round(self.eCentro, 1)
        if self.orientacionChoice.GetStringSelection() == u'Este':
            d = float(self.dTextCtrl.GetValue())
            d1 = float(self.d1TextCtrl.GetValue())
            d2 = float(self.d2TextCtrl.GetValue())
            a1 = math.atan(-d1 / d) * 180.0 / math.pi - 90.0
            a2 = math.atan(d2 / d) * 180.0 / math.pi - 90.0
            self.aCentro = -90.0
            elevacionD = float(self.elevacionDTextCtrl.GetValue())
            x1 = math.sqrt(d1 ** 2 + d ** 2)
            x2 = math.sqrt(d2 ** 2 + d ** 2)
            e1 = math.atan(elevacionD / x1) * 180.0 / math.pi
            e2 = math.atan(elevacionD / x2) * 180.0 / math.pi
            self.eCentro = math.atan(elevacionD / d) * 180.0 / math.pi
            a1 = round(a1, 1)
            a2 = round(a2, 1)
            e1 = round(e1, 1)
            e2 = round(e2, 1)
            self.eCentro = round(self.eCentro, 1)
        if self.orientacionChoice.GetStringSelection() == u'NE':
            d = float(self.dTextCtrl.GetValue())
            d1 = float(self.d1TextCtrl.GetValue())
            d2 = float(self.d2TextCtrl.GetValue())
            a1 = math.atan(-d1 / d) * 180.0 / math.pi - 135.0
            a2 = math.atan(d2 / d) * 180.0 / math.pi - 135.0
            self.aCentro = -135.0
            elevacionD = float(self.elevacionDTextCtrl.GetValue())
            x1 = math.sqrt(d1 ** 2 + d ** 2)
            x2 = math.sqrt(d2 ** 2 + d ** 2)
            e1 = math.atan(elevacionD / x1) * 180.0 / math.pi
            e2 = math.atan(elevacionD / x2) * 180.0 / math.pi
            self.eCentro = math.atan(elevacionD / d) * 180.0 / math.pi
            a1 = round(a1, 1)
            a2 = round(a2, 1)
            e1 = round(e1, 1)
            e2 = round(e2, 1)
            self.eCentro = round(self.eCentro, 1)
        if self.orientacionChoice.GetStringSelection() == u'NO':
            d = float(self.dTextCtrl.GetValue())
            d1 = float(self.d1TextCtrl.GetValue())
            d2 = float(self.d2TextCtrl.GetValue())
            a1 = math.atan(-d1 / d) * 180.0 / math.pi + 135.0
            a2 = math.atan(d2 / d) * 180.0 / math.pi + 135.0
            self.aCentro = 135.0
            elevacionD = float(self.elevacionDTextCtrl.GetValue())
            x1 = math.sqrt(d1 ** 2 + d ** 2)
            x2 = math.sqrt(d2 ** 2 + d ** 2)
            e1 = math.atan(elevacionD / x1) * 180.0 / math.pi
            e2 = math.atan(elevacionD / x2) * 180.0 / math.pi
            self.eCentro = math.atan(elevacionD / d) * 180.0 / math.pi
            a1 = round(a1, 1)
            a2 = round(a2, 1)
            e1 = round(e1, 1)
            e2 = round(e2, 1)
            self.eCentro = round(self.eCentro, 1)
        if self.orientacionChoice.GetStringSelection() == u'Oeste':
            d = float(self.dTextCtrl.GetValue())
            d1 = float(self.d1TextCtrl.GetValue())
            d2 = float(self.d2TextCtrl.GetValue())
            a1 = math.atan(-d1 / d) * 180.0 / math.pi + 90.0
            a2 = math.atan(d2 / d) * 180.0 / math.pi + 90.0
            self.aCentro = 90.0
            elevacionD = float(self.elevacionDTextCtrl.GetValue())
            x1 = math.sqrt(d1 ** 2 + d ** 2)
            x2 = math.sqrt(d2 ** 2 + d ** 2)
            e1 = math.atan(elevacionD / x1) * 180.0 / math.pi
            e2 = math.atan(elevacionD / x2) * 180.0 / math.pi
            self.eCentro = math.atan(elevacionD / d) * 180.0 / math.pi
            a1 = round(a1, 1)
            a2 = round(a2, 1)
            e1 = round(e1, 1)
            e2 = round(e2, 1)
            self.eCentro = round(self.eCentro, 1)
        if self.orientacionChoice.GetStringSelection() == u'SO':
            d = float(self.dTextCtrl.GetValue())
            d1 = float(self.d1TextCtrl.GetValue())
            d2 = float(self.d2TextCtrl.GetValue())
            a1 = math.atan(-d1 / d) * 180.0 / math.pi + 45.0
            a2 = math.atan(d2 / d) * 180.0 / math.pi + 45.0
            self.aCentro = 45.0
            elevacionD = float(self.elevacionDTextCtrl.GetValue())
            x1 = math.sqrt(d1 ** 2 + d ** 2)
            x2 = math.sqrt(d2 ** 2 + d ** 2)
            e1 = math.atan(elevacionD / x1) * 180.0 / math.pi
            e2 = math.atan(elevacionD / x2) * 180.0 / math.pi
            self.eCentro = math.atan(elevacionD / d) * 180.0 / math.pi
            a1 = round(a1, 1)
            a2 = round(a2, 1)
            e1 = round(e1, 1)
            e2 = round(e2, 1)
            self.eCentro = round(self.eCentro, 1)
        self.acimut1TextCtrl.SetValue(str(a1))
        self.acimut2TextCtrl.SetValue(str(a2))
        self.acimut3TextCtrl.SetValue(str(a2))
        self.acimut4TextCtrl.SetValue(str(a1))
        self.elevacion1TextCtrl.SetValue(str(e1))
        self.elevacion2TextCtrl.SetValue(str(e2))
        self.elevacion3TextCtrl.SetValue('0')
        self.elevacion4TextCtrl.SetValue('0')

    def OnComprobarCampos(self):
        """
        Metodo: OnComprobarCampos
        
        Funcon que realiza la cmprobaci\xf3n de que todos los campos tengan campos correctos
        cuando el usuario quiere incorporar el nuevo obstaculo
        """
        listaErrores = u''
        orientacion = self.orientacionChoice.GetStringSelection()
        d = self.dTextCtrl.GetValue()
        d1 = self.d1TextCtrl.GetValue()
        d2 = self.d2TextCtrl.GetValue()
        e = self.elevacionDTextCtrl.GetValue()
        if ',' in d:
            d = d.replace(',', '.')
            self.dTextCtrl.SetValue(d)
        if ',' in d1:
            d1 = d1.replace(',', '.')
            self.d1TextCtrl.SetValue(d1)
        if ',' in d2:
            d2 = d2.replace(',', '.')
            self.d2TextCtrl.SetValue(d2)
        if ',' in e:
            e = e.replace(',', '.')
            self.elevacionDTextCtrl.SetValue(e)
        listaErrores += Comprueba(orientacion, 0, listaErrores, _(u'orientaci\xf3n')).ErrorDevuelto
        listaErrores += Comprueba(d, 2, listaErrores, u'd', 0).ErrorDevuelto
        listaErrores += Comprueba(d1, 2, listaErrores, u'd1').ErrorDevuelto
        listaErrores += Comprueba(d2, 2, listaErrores, u'd2').ErrorDevuelto
        listaErrores += Comprueba(e, 2, listaErrores, _(u'elevaci\xf3n'), 0).ErrorDevuelto
        return listaErrores