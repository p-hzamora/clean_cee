# Embedded file name: DatosGenerales\ayudaNormativaVigente.pyc
"""
Modulo: ayudaDatosGenerales.py


Modulo que contiene la clase Dialog1, que muestra la ventana de ayuda
"""
import wx
import logging

def create(parent):
    """
    Metodo: create
    devuelve una instancia de la clase Dialog1()
    
    ARGUMENTOS:
                parent:
    
    """
    return Dialog1(parent)


wxID_DIALOG1, wxID_DIALOG1ACEPTAR, wxID_DIALOG1CANCELAR, wxID_DIALOG1RADIOBUTTON1, wxID_DIALOG1RADIOBUTTON2, wxID_DIALOG1RADIOBUTTON3, wxID_DIALOG1RADIOBUTTON4, wxID_DIALOG1STATICTEXT1 = [ wx.NewId() for _init_ctrls in range(8) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo ayudaDatosGenerales.py
    
    Ventana de ayuda para saber la normativa vigente en el a\xf1o de construcii\xf3n del edificio
    """

    def __init__(self, parent, annoConstr):
        """
        Constructor de la clase
        
        
        ARGUMENTOS:
            parent:
            annoConstr:
        
        """
        anosButton = self.seleccionarPeriodoTemporal(annoConstr)
        self._init_ctrls(parent, anosButton)
        self.dev = False

    def _init_ctrls(self, prnt, anosButton):
        """
        Metodo: _init_ctrls
        Iniciaci\xf3n de elementos gr\xe1ficos. LLamado desde __init__
        
        ARGUMENTOS:
                prnt:
                anosButton:
        
        
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(428, 302), size=wx.Size(315, 250), style=wx.DEFAULT_DIALOG_STYLE, title=_(u'A\xf1o de visado del proyecto del edificio'))
        self.SetClientSize(wx.Size(315, 250))
        self.SetBackgroundColour('white')
        self.staticText1 = wx.StaticBox(id=wxID_DIALOG1STATICTEXT1, label=_(u'\xbfCu\xe1ndo se vis\xf3 el proyecto del edificio?'), name='datosGeneralesText', parent=self, pos=wx.Point(15, 30), size=wx.Size(285, 150), style=0)
        self.staticText1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticText1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.radioButton1 = wx.RadioButton(id=wxID_DIALOG1RADIOBUTTON1, label=_(u'Antes de 1981'), name='radioButton1', parent=self, pos=wx.Point(30, 55), size=wx.Size(104, 13), style=0)
        self.radioButton1.SetValue(anosButton[0])
        self.radioButton2 = wx.RadioButton(id=wxID_DIALOG1RADIOBUTTON2, label=_(u'Entre 1981 y 2007'), name='radioButton2', parent=self, pos=wx.Point(30, 85), size=wx.Size(120, 13), style=0)
        self.radioButton2.SetValue(anosButton[1])
        self.radioButton3 = wx.RadioButton(id=wxID_DIALOG1RADIOBUTTON3, label=_(u'Entre 2007 y 2014'), name='radioButton3', parent=self, pos=wx.Point(30, 115), size=wx.Size(112, 13), style=0)
        self.radioButton3.SetValue(anosButton[2])
        self.radioButton4 = wx.RadioButton(id=wxID_DIALOG1RADIOBUTTON4, label=_(u'Despu\xe9s de 2014'), name='radioButton4', parent=self, pos=wx.Point(30, 145), size=wx.Size(112, 13), style=0)
        self.radioButton4.SetValue(anosButton[3])
        self.aceptar = wx.Button(id=wxID_DIALOG1ACEPTAR, label=_(u'Aceptar'), name=u'aceptar', parent=self, pos=wx.Point(15, 195), size=wx.Size(75, 23), style=0)
        self.aceptar.Bind(wx.EVT_BUTTON, self.OnAceptarButton, id=wxID_DIALOG1ACEPTAR)
        self.cancelar = wx.Button(id=wxID_DIALOG1CANCELAR, label=_(u'Cancelar'), name=u'cancelar', parent=self, pos=wx.Point(105, 195), size=wx.Size(75, 23), style=0)
        self.cancelar.Bind(wx.EVT_BUTTON, self.OnCancelarButton, id=wxID_DIALOG1CANCELAR)

    def OnAceptarButton(self, event):
        """
        Metodo: OnAceptarButton
        Evento que gestiona la accion de que el usuario presione el boton aceptar
        
        ARGUMENTOS:
                event:
        
        
        """
        self.dev = [self.radioButton1.GetValue(),
         self.radioButton2.GetValue(),
         self.radioButton3.GetValue(),
         self.radioButton4.GetValue()]
        self.Close()

    def OnCancelarButton(self, event):
        """
        Metodo: OnCancelarButton
        Evento que gestiona la accion de que el usuario presione el boton aceptar
        
        ARGUMENTOS:
                event:
        
        
        """
        self.dev = False
        self.Close()

    def seleccionarPeriodoTemporal(self, annoConstr):
        try:
            annoConstr = float(annoConstr)
            if annoConstr < 100.0:
                anosButton = [True,
                 False,
                 False,
                 False]
            elif annoConstr < 1981.0:
                anosButton = [True,
                 False,
                 False,
                 False]
            elif annoConstr < 2007.0:
                anosButton = [False,
                 True,
                 False,
                 False]
            elif annoConstr < 2014.0:
                anosButton = [False,
                 False,
                 True,
                 False]
            else:
                anosButton = [False,
                 False,
                 False,
                 True]
        except:
            anosButton = [True,
             False,
             False,
             False]
            logging.info(u'Excepcion en: %s' % __name__)

        return anosButton