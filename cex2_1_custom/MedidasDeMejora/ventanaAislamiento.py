# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: MedidasDeMejora\ventanaAislamiento.pyc
# Compiled at: 2015-02-23 10:53:17
"""
Modulo: ventanaAislamiento.py

"""
import wx
from Instalaciones.comprobarCampos import Comprueba
import Envolvente.tablasValores as tablasValores

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return Dialog1(parent)


wxID_DIALOG1, wxID_DIALOG1ACEPTARBOTON, wxID_DIALOG1AISLANTERADIO, wxID_DIALOG1CANCELARBOTON, wxID_DIALOG1CHOICE1, wxID_DIALOG1CUBIERTACHECK, wxID_DIALOG1DESCRIPCION, wxID_DIALOG1DESCRIPCIONTEXT, wxID_DIALOG1ESPESORAISLANTE, wxID_DIALOG1ESPESORTEXT, wxID_DIALOG1ESPESORUNIDADESTEXT, wxID_DIALOG1FACHADACHECK, wxID_DIALOG1LANDAAISLANTE, wxID_DIALOG1LANDAAISLANTETEXT, wxID_DIALOG1LANDAAISLANTEUNIDADES, wxID_DIALOG1LIBRERIARADIO, wxID_DIALOG1SUELOCHECK, wxID_DIALOG1TITULOTEXT, wxID_DIALOG1URADIO, wxID_DIALOG1VALORU, wxID_DIALOG1VALURUNIDADESTEXT, wxID_PANEL1STATICTEXT2, wxID_PANEL1STATICTEXT3, wxID_PANEL1STATICTEXT4, wxID_PANEL1STATICTEXT5, wxID_PANEL1STATICTEXT6, wxID_PANEL1STATICTEXT7, wxID_PANEL1STATICTEXT8, wxID_PANEL1TEXTCTRL1, wxID_PANEL1TEXTCTRL2, wxID_PANEL1TEXTCTRL3, wxID_PANEL1TEXTCTRL4, wxID_PANEL1TEXTCTRL5, wxID_PANEL1TEXTCTRL6, wxID_PANEL1TEXTCTRL7, wxID_DIALOG1EXTERIORRADIO, wxID_DIALOG1INTERIORRADIO, wxID_PANEL1STATICTEXT2FI, wxID_PANEL1STATICTEXT3FI, wxID_PANEL1STATICTEXT4FI, wxID_PANEL1STATICTEXT5FI, wxID_PANEL1STATICTEXT6FI, wxID_PANEL1STATICTEXT7FI, wxID_PANEL1STATICTEXT8FI, wxID_PANEL1STATICTEXT2UNID, wxID_PANEL1STATICTEXT3UNID, wxID_PANEL1STATICTEXT4UNID, wxID_PANEL1STATICTEXT5UNID, wxID_PANEL1STATICTEXT6UNID, wxID_PANEL1STATICTEXT7UNID, wxID_PANEL1STATICTEXT8UNID, wxID_DIALOG1UTEXT, wxID_STATICBOX1, wxID_STATICBOX2, wxID_STATICBOX3, wxID_DIALOG1PARTICIONINTERIORCHECK, wxID_PIVERTICALCHECK, wxID_PIHORIZONTALSUPERIORCHECK, wxID_PIHORIZONTALINFERIORCHECK = [ wx.NewId() for _init_ctrls in range(59) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo ventanaAislamiento.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                 prnt:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(0, 0), size=wx.Size(572, 570), style=wx.DEFAULT_DIALOG_STYLE, title=_('Medida de mejora en el aislamiento térmico'))
        self.SetClientSize(wx.Size(572, 570))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tituloText = wx.StaticText(id=wxID_DIALOG1TITULOTEXT, label=_('Medida de mejora en el aislamiento térmico'), name='tituloText', parent=self, pos=wx.Point(15, 15), size=wx.Size(270, 18), style=0)
        self.tituloText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.tituloText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.descripcionText = wx.StaticText(id=wxID_DIALOG1DESCRIPCIONTEXT, label=_('Nombre'), name='descripcionText', parent=self, pos=wx.Point(30, 50), size=wx.Size(68, 13), style=0)
        self.descripcion = wx.TextCtrl(id=wxID_DIALOG1DESCRIPCION, name='descripcion', parent=self, pos=wx.Point(150, 48), size=wx.Size(407, 21), style=0, value='')
        self.staticBox1 = wx.StaticBox(id=wxID_STATICBOX1, label=_('Seleccionar elementos de la envolvente donde se mejora el aislamiento térmico'), name='staticBox1', parent=self, pos=wx.Point(15, 80), size=wx.Size(542, 128), style=0)
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.staticBox1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticBox2 = wx.StaticBox(id=wxID_STATICBOX2, label=_('Definición de las nuevas características de los cerramientos'), name='staticBox1', parent=self, pos=wx.Point(15, 213), size=wx.Size(542, 90), style=0)
        self.staticBox2.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.staticBox2.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticBox3 = wx.StaticBox(id=wxID_STATICBOX3, label=_('Definición del nuevo valor de φ de los puentes térmicos'), name='staticBox1', parent=self, pos=wx.Point(15, 308), size=wx.Size(542, 209), style=0)
        self.staticBox3.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.staticBox3.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticBox3.Show(False)
        self.fachadaCheck = wx.CheckBox(id=wxID_DIALOG1FACHADACHECK, label=_('Fachada'), name='fachadaCheck', parent=self, pos=wx.Point(30, 105), size=wx.Size(70, 13), style=0)
        self.fachadaCheck.SetValue(False)
        self.fachadaCheck.Bind(wx.EVT_CHECKBOX, self.onFachadaCheck, id=wxID_DIALOG1FACHADACHECK)
        self.cubiertaCheck = wx.CheckBox(id=wxID_DIALOG1CUBIERTACHECK, label=_('Cubierta'), name='cubiertaCheck', parent=self, pos=wx.Point(30, 130), size=wx.Size(70, 13), style=0)
        self.cubiertaCheck.SetValue(False)
        self.cubiertaCheck.Bind(wx.EVT_CHECKBOX, self.onMostrarOpcionCaracteristicasAislamientoAnadido, id=wxID_DIALOG1CUBIERTACHECK)
        self.sueloCheck = wx.CheckBox(id=wxID_DIALOG1SUELOCHECK, label=_('Suelo'), name='sueloCheck', parent=self, pos=wx.Point(30, 155), size=wx.Size(70, 13), style=0)
        self.sueloCheck.SetValue(False)
        self.sueloCheck.Bind(wx.EVT_CHECKBOX, self.onMostrarOpcionCaracteristicasAislamientoAnadido, id=wxID_DIALOG1SUELOCHECK)
        self.particionInteriorCheck = wx.CheckBox(id=wxID_DIALOG1PARTICIONINTERIORCHECK, label=_('Partición interior'), name='particionInteriorCheck', parent=self, pos=wx.Point(30, 180), size=wx.Size(118, 13), style=0)
        self.particionInteriorCheck.SetValue(False)
        self.particionInteriorCheck.Bind(wx.EVT_CHECKBOX, self.onParticionInteriorCheck, id=wxID_DIALOG1PARTICIONINTERIORCHECK)
        self.exteriorRadio = wx.RadioButton(id=wxID_DIALOG1EXTERIORRADIO, label=_('por el exterior'), name='exteriorRadio', parent=self, pos=wx.Point(150, 98), size=wx.Size(150, 13), style=wx.RB_GROUP)
        self.exteriorRadio.Show(False)
        self.exteriorRadio.SetValue(True)
        self.exteriorRadio.Bind(wx.EVT_RADIOBUTTON, self.onExteriorRadio, id=wxID_DIALOG1EXTERIORRADIO)
        self.interiorRadio = wx.RadioButton(id=wxID_DIALOG1INTERIORRADIO, label=_('por el interior'), name='interiorRadio', parent=self, pos=wx.Point(150, 114), size=wx.Size(150, 13), style=0)
        self.interiorRadio.Show(False)
        self.interiorRadio.Bind(wx.EVT_RADIOBUTTON, self.onExteriorRadio, id=wxID_DIALOG1INTERIORRADIO)
        self.PIVerticalCheck = wx.CheckBox(id=wxID_PIVERTICALCHECK, label=_('Vertical'), name='verticalRadio', parent=self, pos=wx.Point(150, 168), size=wx.Size(150, 13), style=0)
        self.PIVerticalCheck.Show(False)
        self.PIVerticalCheck.SetValue(False)
        self.PIHorizontalSuperiorCheck = wx.CheckBox(id=wxID_PIHORIZONTALSUPERIORCHECK, label=_('Horizontal en contacto con espacio NH superior'), name='PIHorizontalSuperiorCheck', parent=self, pos=wx.Point(150, 180), size=wx.Size(300, 13), style=0)
        self.PIHorizontalSuperiorCheck.Show(False)
        self.PIHorizontalSuperiorCheck.SetValue(False)
        self.PIHorizontalInferiorCheck = wx.CheckBox(id=wxID_PIHORIZONTALINFERIORCHECK, label=_('Horizontal en contacto con espacio NH inferior'), name='PIHorizontalInferiorCheck', parent=self, pos=wx.Point(150, 192), size=wx.Size(300, 13), style=0)
        self.PIHorizontalInferiorCheck.Show(False)
        self.PIHorizontalInferiorCheck.SetValue(False)
        self.Uradio = wx.RadioButton(id=wxID_DIALOG1URADIO, label=_('Nuevo valor de transmitancia térmica'), name='Uradio', parent=self, pos=wx.Point(30, 238), size=wx.Size(210, 13), style=wx.RB_GROUP)
        self.Uradio.SetValue(True)
        self.Uradio.Bind(wx.EVT_RADIOBUTTON, self.OnRadioButton, id=wxID_DIALOG1URADIO)
        self.aislanteRadio = wx.RadioButton(id=wxID_DIALOG1AISLANTERADIO, label=_('Características del aislamiento añadido'), name='aislanteRadio', parent=self, pos=wx.Point(30, 268), size=wx.Size(210, 13), style=0)
        self.aislanteRadio.Bind(wx.EVT_RADIOBUTTON, self.OnRadioButton, id=wxID_DIALOG1AISLANTERADIO)
        self.libreriaRadio = wx.RadioButton(id=wxID_DIALOG1LIBRERIARADIO, label=_('Librería de materiales'), name='libreriaRadio', parent=self, pos=wx.Point(30, 292), size=wx.Size(128, 13), style=0)
        self.libreriaRadio.Show(False)
        self.libreriaRadio.Bind(wx.EVT_RADIOBUTTON, self.OnRadioButton, id=wxID_DIALOG1LIBRERIARADIO)
        self.UText = wx.StaticText(id=wxID_DIALOG1UTEXT, label=_('U'), name='UText', parent=self, pos=wx.Point(312, 238), size=wx.Size(14, 13), style=0)
        self.valorU = wx.TextCtrl(id=wxID_DIALOG1VALORU, name='valorU', parent=self, pos=wx.Point(326, 236), size=wx.Size(50, 21), style=0, value='0.57')
        self.valorU.SetForegroundColour(wx.Colour(100, 200, 0))
        self.valorU.Bind(wx.EVT_TEXT, self.OnColorValorU, id=wxID_DIALOG1VALORU)
        self.valurUnidadesText = wx.StaticText(id=wxID_DIALOG1VALURUNIDADESTEXT, label=_('W/m2K'), name='valurUnidadesText', parent=self, pos=wx.Point(381, 238), size=wx.Size(34, 13), style=0)
        self.landaAislanteText = wx.StaticText(id=wxID_DIALOG1LANDAAISLANTETEXT, label=_('λ'), name='landaAislanteText', parent=self, pos=wx.Point(312, 268), size=wx.Size(12, 13), style=0)
        self.landaAislanteText.Show(True)
        self.landaAislante = wx.TextCtrl(id=wxID_DIALOG1LANDAAISLANTE, name='landaAislante', parent=self, pos=wx.Point(326, 266), size=wx.Size(50, 21), style=0, value='')
        self.landaAislante.Show(True)
        self.landaAislante.Enable(False)
        self.landaAislanteUnidades = wx.StaticText(id=wxID_DIALOG1LANDAAISLANTEUNIDADES, label=_('W/mK'), name='landaAislanteUnidades', parent=self, pos=wx.Point(381, 268), size=wx.Size(27, 13), style=0)
        self.landaAislanteUnidades.Show(True)
        self.espesorText = wx.StaticText(id=wxID_DIALOG1ESPESORTEXT, label=_('Espesor'), name='espesorText', parent=self, pos=wx.Point(431, 268), size=wx.Size(38, 13), style=0)
        self.espesorText.Show(True)
        self.espesorAislante = wx.TextCtrl(id=wxID_DIALOG1ESPESORAISLANTE, name='espesorAislante', parent=self, pos=wx.Point(474, 266), size=wx.Size(50, 21), style=0, value='')
        self.espesorAislante.Enable(False)
        self.espesorAislante.Show(True)
        self.espesorUnidadesText = wx.StaticText(id=wxID_DIALOG1ESPESORUNIDADESTEXT, label=_('m'), name='espesorUnidadesText', parent=self, pos=wx.Point(529, 268), size=wx.Size(13, 13), style=0)
        self.espesorUnidadesText.Show(True)
        self.choice1 = wx.Choice(choices=self.parent.parent.parent.parent.listadoCerramientos, id=wxID_DIALOG1CHOICE1, name='choice1', parent=self, pos=wx.Point(248, 272), size=wx.Size(168, 21), style=0)
        self.choice1.Enable(False)
        self.choice1.Show(False)
        self.staticText2 = wx.StaticText(id=wxID_PANEL1STATICTEXT2, label=_('Pilar integrado en fachada'), name='staticText2', parent=self, pos=wx.Point(30, 333), size=wx.Size(126, 13), style=0)
        self.staticText2.Show(False)
        self.staticText3 = wx.StaticText(id=wxID_PANEL1STATICTEXT3, label=_('Pilar en esquina'), name='staticText3', parent=self, pos=wx.Point(30, 358), size=wx.Size(75, 13), style=0)
        self.staticText3.Show(False)
        self.staticText4 = wx.StaticText(id=wxID_PANEL1STATICTEXT4, label=_('Contorno de hueco'), name='staticText4', parent=self, pos=wx.Point(30, 383), size=wx.Size(92, 13), style=0)
        self.staticText4.Show(False)
        self.staticText5 = wx.StaticText(id=wxID_PANEL1STATICTEXT5, label=_('Caja de persiana'), name='staticText5', parent=self, pos=wx.Point(30, 408), size=wx.Size(81, 13), style=0)
        self.staticText5.Show(False)
        self.staticText6 = wx.StaticText(id=wxID_PANEL1STATICTEXT6, label=_('Encuentro de fachada con forjado'), name='staticText6', parent=self, pos=wx.Point(30, 433), size=wx.Size(164, 13), style=0)
        self.staticText6.Show(False)
        self.staticText7 = wx.StaticText(id=wxID_PANEL1STATICTEXT7, label=_('Encuentro de fachada con cubierta'), name='staticText7', parent=self, pos=wx.Point(30, 458), size=wx.Size(168, 13), style=0)
        self.staticText7.Show(False)
        self.staticText8 = wx.StaticText(id=wxID_PANEL1STATICTEXT8, label=_('Encuentro de fachada con suelo en contacto con el aire'), name='staticText8', parent=self, pos=wx.Point(30, 483), size=wx.Size(266, 13), style=0)
        self.staticText8.Show(False)
        self.textCtrl1 = wx.TextCtrl(id=wxID_PANEL1TEXTCTRL1, name='textCtrl1', parent=self, pos=wx.Point(326, 331), size=wx.Size(50, 21), style=0, value='')
        self.textCtrl1.Show(False)
        self.textCtrl2 = wx.TextCtrl(id=wxID_PANEL1TEXTCTRL2, name='textCtrl2', parent=self, pos=wx.Point(326, 356), size=wx.Size(50, 21), style=0, value='')
        self.textCtrl2.Show(False)
        self.textCtrl3 = wx.TextCtrl(id=wxID_PANEL1TEXTCTRL3, name='textCtrl3', parent=self, pos=wx.Point(326, 381), size=wx.Size(50, 21), style=0, value='')
        self.textCtrl3.Show(False)
        self.textCtrl4 = wx.TextCtrl(id=wxID_PANEL1TEXTCTRL4, name='textCtrl4', parent=self, pos=wx.Point(326, 406), size=wx.Size(50, 21), style=0, value='')
        self.textCtrl4.Show(False)
        self.textCtrl5 = wx.TextCtrl(id=wxID_PANEL1TEXTCTRL5, name='textCtrl5', parent=self, pos=wx.Point(326, 431), size=wx.Size(50, 21), style=0, value='')
        self.textCtrl5.Show(False)
        self.textCtrl6 = wx.TextCtrl(id=wxID_PANEL1TEXTCTRL6, name='textCtrl6', parent=self, pos=wx.Point(326, 456), size=wx.Size(50, 21), style=0, value='')
        self.textCtrl6.Show(False)
        self.textCtrl7 = wx.TextCtrl(id=wxID_PANEL1TEXTCTRL7, name='textCtrl7', parent=self, pos=wx.Point(326, 481), size=wx.Size(50, 21), style=0, value='')
        self.textCtrl7.Show(False)
        self.staticText2FI = wx.StaticText(id=wxID_PANEL1STATICTEXT2FI, label=_('φ'), name='staticText2', parent=self, pos=wx.Point(312, 333), size=wx.Size(12, 13), style=0)
        self.staticText2FI.Show(False)
        self.staticText3FI = wx.StaticText(id=wxID_PANEL1STATICTEXT3FI, label=_('φ'), name='staticText3', parent=self, pos=wx.Point(312, 358), size=wx.Size(12, 13), style=0)
        self.staticText3FI.Show(False)
        self.staticText4FI = wx.StaticText(id=wxID_PANEL1STATICTEXT4FI, label=_('φ'), name='staticText4', parent=self, pos=wx.Point(312, 383), size=wx.Size(12, 13), style=0)
        self.staticText4FI.Show(False)
        self.staticText5FI = wx.StaticText(id=wxID_PANEL1STATICTEXT5FI, label=_('φ'), name='staticText5', parent=self, pos=wx.Point(312, 408), size=wx.Size(12, 13), style=0)
        self.staticText5FI.Show(False)
        self.staticText6FI = wx.StaticText(id=wxID_PANEL1STATICTEXT6FI, label=_('φ'), name='staticText6', parent=self, pos=wx.Point(312, 433), size=wx.Size(12, 13), style=0)
        self.staticText6FI.Show(False)
        self.staticText7FI = wx.StaticText(id=wxID_PANEL1STATICTEXT7FI, label=_('φ'), name='staticText7', parent=self, pos=wx.Point(312, 458), size=wx.Size(12, 13), style=0)
        self.staticText7FI.Show(False)
        self.staticText8FI = wx.StaticText(id=wxID_PANEL1STATICTEXT8FI, label=_('φ'), name='staticText8', parent=self, pos=wx.Point(312, 483), size=wx.Size(12, 13), style=0)
        self.staticText8FI.Show(False)
        self.staticText2UNID = wx.StaticText(id=wxID_PANEL1STATICTEXT2UNID, label=_('W/mK'), name='staticText2', parent=self, pos=wx.Point(381, 333), size=wx.Size(30, 13), style=0)
        self.staticText2UNID.Show(False)
        self.staticText3UNID = wx.StaticText(id=wxID_PANEL1STATICTEXT3UNID, label=_('W/mK'), name='staticText3', parent=self, pos=wx.Point(381, 358), size=wx.Size(30, 13), style=0)
        self.staticText3UNID.Show(False)
        self.staticText4UNID = wx.StaticText(id=wxID_PANEL1STATICTEXT4UNID, label=_('W/mK'), name='staticText4', parent=self, pos=wx.Point(381, 383), size=wx.Size(30, 13), style=0)
        self.staticText4UNID.Show(False)
        self.staticText5UNID = wx.StaticText(id=wxID_PANEL1STATICTEXT5UNID, label=_('W/mK'), name='staticText5', parent=self, pos=wx.Point(381, 408), size=wx.Size(30, 13), style=0)
        self.staticText5UNID.Show(False)
        self.staticText6UNID = wx.StaticText(id=wxID_PANEL1STATICTEXT6UNID, label=_('W/mK'), name='staticText6', parent=self, pos=wx.Point(381, 433), size=wx.Size(30, 13), style=0)
        self.staticText6UNID.Show(False)
        self.staticText7UNID = wx.StaticText(id=wxID_PANEL1STATICTEXT7UNID, label=_('W/mK'), name='staticText7', parent=self, pos=wx.Point(381, 458), size=wx.Size(30, 13), style=0)
        self.staticText7UNID.Show(False)
        self.staticText8UNID = wx.StaticText(id=wxID_PANEL1STATICTEXT8UNID, label=_('W/mK'), name='staticText8', parent=self, pos=wx.Point(381, 483), size=wx.Size(30, 13), style=0)
        self.staticText8UNID.Show(False)
        self.aceptarBoton = wx.Button(id=wxID_DIALOG1ACEPTARBOTON, label=_('Aceptar'), name='aceptarBoton', parent=self, pos=wx.Point(15, 532), size=wx.Size(75, 23), style=0)
        self.aceptarBoton.Bind(wx.EVT_BUTTON, self.onAceptarBoton, id=wxID_DIALOG1ACEPTARBOTON)
        self.cancelarBoton = wx.Button(id=wxID_DIALOG1CANCELARBOTON, label=_('Cancelar'), name='cancelarBoton', parent=self, pos=wx.Point(105, 532), size=wx.Size(75, 23), style=0)
        self.cancelarBoton.Bind(wx.EVT_BUTTON, self.onCancelarBoton, id=wxID_DIALOG1CANCELARBOTON)

    def __init__(self, parent):
        """
        Constructor de la clase

        ARGUMENTOS:
                 parent:
        """
        self.parent = parent
        self._init_ctrls(parent)
        self.dev = False
        self.iniciaPTDefecto()

    def iniciaPTDefecto(self):
        """
        Metodo: iniciaPTDefecto

        """
        self.textCtrl1.SetValue(str(tablasValores.tablasValores('PTMedidasMejora', None, ['Pilar integrado en fachada'], None).fi))
        self.textCtrl2.SetValue(str(tablasValores.tablasValores('PTMedidasMejora', None, ['Pilar en Esquina'], None).fi))
        self.textCtrl3.SetValue(str(tablasValores.tablasValores('PTMedidasMejora', None, ['Contorno de hueco'], None).fi))
        self.textCtrl4.SetValue(str(tablasValores.tablasValores('PTMedidasMejora', None, ['Caja de Persiana'], None).fi))
        self.textCtrl5.SetValue(str(tablasValores.tablasValores('PTMedidasMejora', None, ['Encuentro de fachada con forjado'], None).fi))
        self.textCtrl6.SetValue(str(tablasValores.tablasValores('PTMedidasMejora', None, ['Encuentro de fachada con cubierta'], None).fi))
        self.textCtrl7.SetValue(str(tablasValores.tablasValores('PTMedidasMejora', None, ['Encuentro de fachada con suelo en contacto con el aire'], None).fi))
        return

    def onExteriorRadio(self, event):
        """
        Metodo: onExteriorRadio

        ARGUMENTOS:
                event:
        """
        if self.exteriorRadio.GetValue() == True and self.fachadaCheck.GetValue() == True:
            self.staticBox3.Show(True)
            self.staticText2.Show(True)
            self.staticText3.Show(True)
            self.staticText4.Show(True)
            self.staticText5.Show(True)
            self.staticText6.Show(True)
            self.staticText7.Show(True)
            self.staticText8.Show(True)
            self.textCtrl1.Show(True)
            self.textCtrl2.Show(True)
            self.textCtrl3.Show(True)
            self.textCtrl4.Show(True)
            self.textCtrl5.Show(True)
            self.textCtrl6.Show(True)
            self.textCtrl7.Show(True)
            self.staticText2FI.Show(True)
            self.staticText3FI.Show(True)
            self.staticText4FI.Show(True)
            self.staticText5FI.Show(True)
            self.staticText6FI.Show(True)
            self.staticText7FI.Show(True)
            self.staticText8FI.Show(True)
            self.staticText2UNID.Show(True)
            self.staticText3UNID.Show(True)
            self.staticText4UNID.Show(True)
            self.staticText5UNID.Show(True)
            self.staticText6UNID.Show(True)
            self.staticText7UNID.Show(True)
            self.staticText8UNID.Show(True)
        else:
            self.staticBox3.Show(False)
            self.staticText2.Show(False)
            self.staticText3.Show(False)
            self.staticText4.Show(False)
            self.staticText5.Show(False)
            self.staticText6.Show(False)
            self.staticText7.Show(False)
            self.staticText8.Show(False)
            self.textCtrl1.Show(False)
            self.textCtrl2.Show(False)
            self.textCtrl3.Show(False)
            self.textCtrl4.Show(False)
            self.textCtrl5.Show(False)
            self.textCtrl6.Show(False)
            self.textCtrl7.Show(False)
            self.staticText2FI.Show(False)
            self.staticText3FI.Show(False)
            self.staticText4FI.Show(False)
            self.staticText5FI.Show(False)
            self.staticText6FI.Show(False)
            self.staticText7FI.Show(False)
            self.staticText8FI.Show(False)
            self.staticText2UNID.Show(False)
            self.staticText3UNID.Show(False)
            self.staticText4UNID.Show(False)
            self.staticText5UNID.Show(False)
            self.staticText6UNID.Show(False)
            self.staticText7UNID.Show(False)
            self.staticText8UNID.Show(False)

    def onMostrarOpcionCaracteristicasAislamientoAnadido(self, event):
        if (self.fachadaCheck.GetValue() == True or self.cubiertaCheck.GetValue() == True) and self.sueloCheck.GetValue() == False and self.particionInteriorCheck.GetValue() == False:
            self.aislanteRadio.Show(True)
            self.landaAislanteText.Show(True)
            self.landaAislante.Show(True)
            self.landaAislanteUnidades.Show(True)
            self.espesorText.Show(True)
            self.espesorAislante.Show(True)
            self.espesorUnidadesText.Show(True)
        else:
            self.aislanteRadio.Show(False)
            self.landaAislanteText.Show(False)
            self.landaAislante.Show(False)
            self.landaAislanteUnidades.Show(False)
            self.espesorText.Show(False)
            self.espesorAislante.Show(False)
            self.espesorUnidadesText.Show(False)
            self.Uradio.SetValue(True)
            self.OnRadioButton(None)
        return

    def onFachadaCheck(self, event):
        """
        Metodo: onFachadaCheck

        ARGUMENTOS:
                event:
        """
        if self.fachadaCheck.GetValue() == True:
            self.exteriorRadio.Show(True)
            self.interiorRadio.Show(True)
            self.exteriorRadio.SetValue(True)
            self.onExteriorRadio(None)
        else:
            self.exteriorRadio.Show(False)
            self.interiorRadio.Show(False)
            self.staticBox3.Show(False)
            self.staticText2.Show(False)
            self.staticText3.Show(False)
            self.staticText4.Show(False)
            self.staticText5.Show(False)
            self.staticText6.Show(False)
            self.staticText7.Show(False)
            self.staticText8.Show(False)
            self.textCtrl1.Show(False)
            self.textCtrl2.Show(False)
            self.textCtrl3.Show(False)
            self.textCtrl4.Show(False)
            self.textCtrl5.Show(False)
            self.textCtrl6.Show(False)
            self.textCtrl7.Show(False)
            self.staticText2FI.Show(False)
            self.staticText3FI.Show(False)
            self.staticText4FI.Show(False)
            self.staticText5FI.Show(False)
            self.staticText6FI.Show(False)
            self.staticText7FI.Show(False)
            self.staticText8FI.Show(False)
            self.staticText2UNID.Show(False)
            self.staticText3UNID.Show(False)
            self.staticText4UNID.Show(False)
            self.staticText5UNID.Show(False)
            self.staticText6UNID.Show(False)
            self.staticText7UNID.Show(False)
            self.staticText8UNID.Show(False)
        self.onMostrarOpcionCaracteristicasAislamientoAnadido(None)
        return

    def onParticionInteriorCheck(self, event):
        """
        Metodo: onFachadaCheck. Si he seleccionado que se aisla la particion interior

        ARGUMENTOS:
                event:
        """
        if self.particionInteriorCheck.GetValue() == True:
            self.PIVerticalCheck.Show(True)
            self.PIHorizontalSuperiorCheck.Show(True)
            self.PIHorizontalInferiorCheck.Show(True)
        else:
            self.PIVerticalCheck.Show(False)
            self.PIHorizontalSuperiorCheck.Show(False)
            self.PIHorizontalInferiorCheck.Show(False)
        self.onMostrarOpcionCaracteristicasAislamientoAnadido(None)
        return

    def OnColorValorU(self, event):
        self.valorU.SetForegroundColour(wx.Colour(0, 0, 0))

    def OnRadioButton(self, event):
        """
        Metodo: OnRadioButton

        ARGUMENTOS:
                event:
        """
        if self.Uradio.GetValue() == True:
            self.valorU.Enable(True)
            self.choice1.Enable(False)
            self.espesorAislante.Enable(False)
            self.landaAislante.Enable(False)
        elif self.aislanteRadio.GetValue() == True:
            self.valorU.Enable(False)
            self.choice1.Enable(False)
            self.espesorAislante.Enable(True)
            self.landaAislante.Enable(True)
        elif self.libreriaRadio.GetValue() == True:
            self.valorU.Enable(False)
            self.choice1.Enable(True)
            self.espesorAislante.Enable(False)
            self.landaAislante.Enable(False)

    def onAceptarBoton(self, event):
        """
        Metodo: onAceptarBoton

        ARGUMENTOS:
                event:
        """
        valorU = self.valorU.GetValue()
        landaAislante = self.landaAislante.GetValue()
        espesorAislante = self.espesorAislante.GetValue()
        textCtrl1 = self.textCtrl1.GetValue()
        textCtrl2 = self.textCtrl2.GetValue()
        textCtrl3 = self.textCtrl3.GetValue()
        textCtrl4 = self.textCtrl4.GetValue()
        textCtrl5 = self.textCtrl5.GetValue()
        textCtrl6 = self.textCtrl6.GetValue()
        textCtrl7 = self.textCtrl7.GetValue()
        if ',' in valorU:
            valorU = valorU.replace(',', '.')
            self.valorU.SetValue(valorU)
        if ',' in landaAislante:
            landaAislante = landaAislante.replace(',', '.')
            self.landaAislante.SetValue(landaAislante)
        if ',' in espesorAislante:
            espesorAislante = espesorAislante.replace(',', '.')
            self.espesorAislante.SetValue(espesorAislante)
        if ',' in textCtrl1:
            textCtrl1 = textCtrl1.replace(',', '.')
            self.textCtrl1.SetValue(textCtrl1)
        if ',' in textCtrl2:
            textCtrl2 = textCtrl2.replace(',', '.')
            self.textCtrl2.SetValue(textCtrl2)
        if ',' in textCtrl3:
            textCtrl3 = textCtrl3.replace(',', '.')
            self.textCtrl3.SetValue(textCtrl3)
        if ',' in textCtrl4:
            textCtrl4 = textCtrl4.replace(',', '.')
            self.textCtrl4.SetValue(textCtrl4)
        if ',' in textCtrl5:
            textCtrl5 = textCtrl5.replace(',', '.')
            self.textCtrl5.SetValue(textCtrl5)
        if ',' in textCtrl6:
            textCtrl6 = textCtrl6.replace(',', '.')
            self.textCtrl6.SetValue(textCtrl6)
        if ',' in textCtrl7:
            textCtrl7 = textCtrl7.replace(',', '.')
            self.textCtrl7.SetValue(textCtrl7)
        error = ''
        error += Comprueba(self.descripcion.GetValue(), 0, error, _('nombre')).ErrorDevuelto
        if self.fachadaCheck.GetValue() == False and self.cubiertaCheck.GetValue() == False and self.sueloCheck.GetValue() == False and self.particionInteriorCheck.GetValue() == False and self.particionInteriorCheck.GetValue() == False:
            if error != '':
                error += ', '
            error += _('elementos de la envolvente donde se mejora el aislamiento térmico')
        if self.Uradio.GetValue() == True:
            error += Comprueba(self.valorU.GetValue(), 2, error, 'U', 0).ErrorDevuelto
        if self.aislanteRadio.GetValue() == True:
            error += Comprueba(self.landaAislante.GetValue(), 2, error, 'λ', 0.0).ErrorDevuelto
            error += Comprueba(self.espesorAislante.GetValue(), 2, error, _('espesor'), 0.0).ErrorDevuelto
        if self.libreriaRadio.GetValue() == True:
            error += Comprueba(self.choice1.GetStringSelection(), 0, error, _('cerramiento')).ErrorDevuelto
        if self.fachadaCheck.GetValue() == True and self.exteriorRadio.GetValue() == True:
            if self.textCtrl1.GetValue() != '':
                error += Comprueba(self.textCtrl1.GetValue(), 2, error, _('φ de pilar integrado en fachada')).ErrorDevuelto
            if self.textCtrl2.GetValue() != '':
                error += Comprueba(self.textCtrl2.GetValue(), 2, error, _('φ de pilar en esquina')).ErrorDevuelto
            if self.textCtrl3.GetValue() != '':
                error += Comprueba(self.textCtrl3.GetValue(), 2, error, _('φ de contorno de Hueco')).ErrorDevuelto
            if self.textCtrl4.GetValue() != '':
                error += Comprueba(self.textCtrl4.GetValue(), 2, error, _('φ de caja de Persiana')).ErrorDevuelto
            if self.textCtrl5.GetValue() != '':
                error += Comprueba(self.textCtrl5.GetValue(), 2, error, _('φ de encuentro de fachada con forjado')).ErrorDevuelto
            if self.textCtrl6.GetValue() != '':
                error += Comprueba(self.textCtrl6.GetValue(), 2, error, _('φ de encuentro de fachada con cubierta')).ErrorDevuelto
            if self.textCtrl7.GetValue() != '':
                error += Comprueba(self.textCtrl7.GetValue(), 2, error, _('φ de encuentro de fachada con suelo en contacto con el aire')).ErrorDevuelto
        if self.particionInteriorCheck.GetValue() == True and self.PIVerticalCheck.GetValue() == False and self.PIHorizontalSuperiorCheck.GetValue() == False and self.PIHorizontalInferiorCheck.GetValue() == False:
            if error != '':
                error += ', '
            error += _('tipo de partición interior donde se mejora el aislamiento')
        if error != '':
            wx.MessageBox(_('Revise los siguientes campos:\n') + error + _('.'), _('Aviso'))
            return
        datos = []
        datos.append(self.descripcion.GetValue())
        datos.append('Adición de Aislamiento Térmico')
        datosConcretos = []
        datosConcretos.append(self.fachadaCheck.GetValue())
        datosConcretos.append(self.cubiertaCheck.GetValue())
        datosConcretos.append(self.sueloCheck.GetValue())
        datosConcretos.append(self.Uradio.GetValue())
        datosConcretos.append(self.aislanteRadio.GetValue())
        datosConcretos.append(self.libreriaRadio.GetValue())
        datosConcretos.append(self.valorU.GetValue())
        datosConcretos.append(self.landaAislante.GetValue())
        datosConcretos.append(self.espesorAislante.GetValue())
        datosConcretos.append(self.choice1.GetStringSelection())
        datosConcretos.append(self.exteriorRadio.GetValue())
        if self.fachadaCheck.GetValue() == True and self.exteriorRadio.GetValue() == True:
            datosConcretos.append([self.textCtrl1.GetValue(), self.textCtrl2.GetValue(),
             self.textCtrl3.GetValue(), self.textCtrl4.GetValue(),
             self.textCtrl5.GetValue(), self.textCtrl6.GetValue(), self.textCtrl7.GetValue()])
        else:
            datosConcretos.append(['', '', '', '', '', '', ''])
        datosConcretos.append([self.particionInteriorCheck.GetValue(), self.PIVerticalCheck.GetValue(),
         self.PIHorizontalSuperiorCheck.GetValue(), self.PIHorizontalInferiorCheck.GetValue()])
        datos.append(datosConcretos)
        self.dev = datos
        self.Close()

    def cargarDatos(self, datos):
        """
        Metodo: cargarDatos

        ARGUMENTOS:
                datos:
        """
        self.descripcion.SetValue(datos[0])
        datos.append('Adición de Aislamiento Térmico')
        datosConcretos = datos[2]
        self.fachadaCheck.SetValue(datosConcretos[0])
        self.cubiertaCheck.SetValue(datosConcretos[1])
        self.sueloCheck.SetValue(datosConcretos[2])
        self.Uradio.SetValue(datosConcretos[3])
        self.aislanteRadio.SetValue(datosConcretos[4])
        self.libreriaRadio.SetValue(datosConcretos[5])
        self.valorU.SetValue(str(datosConcretos[6]))
        self.landaAislante.SetValue(str(datosConcretos[7]))
        self.espesorAislante.SetValue(str(datosConcretos[8]))
        self.choice1.SetStringSelection(str(datosConcretos[9]))
        valoresPT = datosConcretos[11]
        self.textCtrl1.SetValue(str(valoresPT[0]))
        self.textCtrl2.SetValue(str(valoresPT[1]))
        self.textCtrl3.SetValue(str(valoresPT[2]))
        self.textCtrl4.SetValue(str(valoresPT[3]))
        self.textCtrl5.SetValue(str(valoresPT[4]))
        self.textCtrl6.SetValue(str(valoresPT[5]))
        self.textCtrl7.SetValue(str(valoresPT[6]))
        self.onFachadaCheck(None)
        self.exteriorRadio.SetValue(datosConcretos[10])
        self.interiorRadio.SetValue(not datosConcretos[10])
        self.onExteriorRadio(None)
        self.OnRadioButton(None)
        if len(datosConcretos) == 13:
            self.particionInteriorCheck.SetValue(datosConcretos[12][0])
            self.PIVerticalCheck.SetValue(datosConcretos[12][1])
            self.PIHorizontalSuperiorCheck.SetValue(datosConcretos[12][2])
            self.PIHorizontalInferiorCheck.SetValue(datosConcretos[12][3])
            self.onParticionInteriorCheck(None)
        if self.interiorRadio.GetValue() == True:
            self.iniciaPTDefecto()
        self.onMostrarOpcionCaracteristicasAislamientoAnadido(None)
        return

    def onCancelarBoton(self, event):
        """
        Metodo: onCancelarBoton

        ARGUMENTOS:
                event:
        """
        self.dev = False
        self.Close()