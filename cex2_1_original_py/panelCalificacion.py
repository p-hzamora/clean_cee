# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: panelCalificacion.pyc
# Compiled at: 2014-02-25 15:39:24
"""
Modulo: panelCalificacion.py

"""
import wx, wx.lib.throbber, wx.lib.buttons, directorios
Directorio = directorios.BuscaDirectorios().Directorio

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return panelCalificacion(parent)


wxID_WXPANEL6, wxID_wxPANEL6IMAGENMIYABI, wxID_wxPANEL6ETIQUETA, wxID_WXPANEL6NOTAA, wxID_WXPANEL6NOTAB, wxID_WXPANEL6NOTAC, wxID_WXPANEL6NOTAD, wxID_WXPANEL6NOTAE, wxID_WXPANEL6TITULO, wxID_WXPANEL6INDICADOR, wxID_WXPANEL6LINEAA, wxID_WXPANEL6LINEAB, wxID_WXPANEL6LINEAC, wxID_WXPANEL6LINEAD, wxID_WXPANEL6LINEAE, wxID_WXPANEL6EMISA, wxID_WXPANEL6EMISB, wxID_WXPANEL6EMISC, wxID_WXPANEL6EMISD, wxID_WXPANEL6EMISE, wxID_WXPANEL6EDIFOBJETO, wxID_WXPANEL6DDACAL, wxID_WXPANEL6DDAREF, wxID_WXPANEL6EMISCAL, wxID_WXPANEL6EMISREF, wxID_WXPANEL6EMISACS, wxID_WXPANEL6UNIDADES1, wxID_WXPANEL6UNIDADES2, wxID_WXPANEL6UNIDADES3, wxID_WXPANEL6UNIDADES4, wxID_WXPANEL6UNIDADES5, wxID_WXPANEL6VALORDDACAL, wxID_WXPANEL6VALORDDAREF, wxID_WXPANEL6VALOREMISCAL, wxID_WXPANEL6VALOREMISREF, wxID_WXPANEL6VALOREMISACS, wxID_WXPANEL6NOTADDACAL, wxID_WXPANEL6NOTADDAREF, wxID_WXPANEL6NOTAEMISCAL, wxID_WXPANEL6NOTAEMISREF, wxID_WXPANEL6NOTAEMISACS, wxID_WXPANEL6LIMITEA, wxID_WXPANEL6LIMITEB, wxID_WXPANEL6LIMITEC, wxID_WXPANEL6LIMITED, wxID_WXPANEL6LIMITEE, wxID_WXPANEL6CERRAR, wxID_WXPANEL6VALOREMISILUMINACION, wxID_WXPANEL6UNIDADES6, wxID_WXPANEL6EMISILUMINACION, wxID_WXPANEL6NOTAEMISILUMINACION, wxID_WXPANEL6BALANCECONTRIBUCIONES, wxID_WXPANEL6BALANCECONTRIBUCIONES6, wxID_WXPANEL6VALORBALANCECONTRIBUCIONES, wxID_WXPANEL6NOTAF, wxID_WXPANEL6EMISF, wxID_WXPANEL6LIMITEF, wxID_WXPANEL6NOTAG, wxID_WXPANEL6EMISG, wxID_WXPANEL6LIMITEG = [ wx.NewId() for _init_ctrls in range(60) ]

class panelCalificacion(wx.Panel):
    """
    Clase: panelCalificacion del modulo panelCalificacion.py

    """

    def _init_ctrls(self, prnt, id_prnt, pos_prnt, size_prnt, style_prnt, name_prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
                id_prnt:
                pos_prnt:
                size_prnt:
                style_prnt:
                name_prnt:
        """
        wx.Panel.__init__(self, id=id_prnt, name=name_prnt, parent=prnt, pos=pos_prnt, size=size_prnt, style=style_prnt)
        self.SetBackgroundStyle(wx.BG_STYLE_SYSTEM)
        self.SetBackgroundColour('white')
        self.parent = prnt
        self.Etiqueta = wx.StaticBitmap(bitmap=wx.Bitmap(Directorio + '/Imagenes/etiqueta_transparente.gif', wx.BITMAP_TYPE_GIF), id=wxID_wxPANEL6ETIQUETA, name='Etiqueta', parent=self, pos=wx.Point(45, 90), size=wx.Size(280, 290), style=0)
        self.NotaA = wx.StaticText(id=wxID_WXPANEL6NOTAA, label=_('A'), name='NotaA', parent=self, pos=wx.Point(255, 86), size=wx.Size(30, 30), style=wx.NO_3D | 0)
        self.NotaA.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'MS Shell Dlg 2'))
        self.NotaA.SetForegroundColour(wx.Colour(0, 159, 60))
        self.NotaA.Show(False)
        self.EmisA = wx.StaticText(id=wxID_WXPANEL6EMISA, label='', name='EmisA', parent=self, pos=wx.Point(190, 91), size=wx.Size(30, 20), style=wx.NO_3D | 0)
        self.EmisA.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.EmisA.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.EmisA.Show(False)
        self.LimiteA = wx.StaticText(id=wxID_WXPANEL6LIMITEA, label='', name='LimiteA', parent=self, pos=wx.Point(2, 101), size=wx.Size(30, 20), style=wx.NO_3D | 0)
        self.LimiteA.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.LimiteA.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.LimiteA.Show(True)
        self.NotaB = wx.StaticText(id=wxID_WXPANEL6NOTAB, label=_('B'), name='NotaB', parent=self, pos=wx.Point(270, 130), size=wx.Size(30, 30), style=wx.NO_3D | 0)
        self.NotaB.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'MS Shell Dlg 2'))
        self.NotaB.SetForegroundColour(wx.Colour(43, 180, 49))
        self.NotaB.Show(False)
        self.EmisB = wx.StaticText(id=wxID_WXPANEL6EMISB, label='', name='EmisB', parent=self, pos=wx.Point(205, 135), size=wx.Size(30, 20), style=wx.NO_3D | 0)
        self.EmisB.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.EmisB.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.EmisB.Show(False)
        self.LimiteB = wx.StaticText(id=wxID_WXPANEL6LIMITEB, label='', name='LimiteB', parent=self, pos=wx.Point(2, 145), size=wx.Size(30, 20), style=wx.NO_3D | 0)
        self.LimiteB.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.LimiteB.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.LimiteB.Show(True)
        self.NotaC = wx.StaticText(id=wxID_WXPANEL6NOTAC, label=_('C'), name='NotaC', parent=self, pos=wx.Point(300, 175), size=wx.Size(30, 30), style=wx.NO_3D | 0)
        self.NotaC.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'MS Shell Dlg 2'))
        self.NotaC.SetForegroundColour(wx.Colour(179, 216, 0))
        self.NotaC.Show(False)
        self.EmisC = wx.StaticText(id=wxID_WXPANEL6EMISC, label='', name='EmisC', parent=self, pos=wx.Point(235, 180), size=wx.Size(30, 20), style=wx.NO_3D | 0)
        self.EmisC.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.EmisC.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.EmisC.Show(False)
        self.LimiteC = wx.StaticText(id=wxID_WXPANEL6LIMITEC, label='', name='LimiteC', parent=self, pos=wx.Point(2, 190), size=wx.Size(30, 20), style=wx.NO_3D | 0)
        self.LimiteC.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.LimiteC.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.LimiteC.Show(True)
        self.NotaD = wx.StaticText(id=wxID_WXPANEL6NOTAD, label=_('D'), name='NotaD', parent=self, pos=wx.Point(330, 218), size=wx.Size(30, 30), style=wx.NO_3D | 0)
        self.NotaD.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'MS Shell Dlg 2'))
        self.NotaD.SetForegroundColour(wx.Colour(248, 244, 0))
        self.NotaD.Show(False)
        self.EmisD = wx.StaticText(id=wxID_WXPANEL6EMISD, label='', name='EmisD', parent=self, pos=wx.Point(265, 223), size=wx.Size(30, 20), style=wx.NO_3D | 0)
        self.EmisD.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.EmisD.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.EmisD.Show(False)
        self.LimiteD = wx.StaticText(id=wxID_WXPANEL6LIMITED, label='', name='LimiteD', parent=self, pos=wx.Point(2, 233), size=wx.Size(30, 20), style=wx.NO_3D | 0)
        self.LimiteD.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.LimiteD.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.LimiteD.Show(True)
        self.NotaE = wx.StaticText(id=wxID_WXPANEL6NOTAE, label=_('E'), name='NotaE', parent=self, pos=wx.Point(350, 263), size=wx.Size(30, 30), style=wx.NO_3D | 0)
        self.NotaE.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'MS Shell Dlg 2'))
        self.NotaE.SetForegroundColour(wx.Colour(244, 193, 0))
        self.NotaE.Show(False)
        self.EmisE = wx.StaticText(id=wxID_WXPANEL6EMISE, label='', name='EmisE', parent=self, pos=wx.Point(285, 268), size=wx.Size(30, 20), style=wx.NO_3D | 0)
        self.EmisE.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.EmisE.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.EmisE.Show(False)
        self.LimiteE = wx.StaticText(id=wxID_WXPANEL6LIMITEE, label='', name='LimiteE', parent=self, pos=wx.Point(2, 278), size=wx.Size(30, 20), style=wx.NO_3D | 0)
        self.LimiteE.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.LimiteE.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.LimiteE.Show(True)
        self.NotaF = wx.StaticText(id=wxID_WXPANEL6NOTAF, label=_('F'), name='NotaF', parent=self, pos=wx.Point(370, 308), size=wx.Size(30, 30), style=wx.NO_3D | 0)
        self.NotaF.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'MS Shell Dlg 2'))
        self.NotaF.SetForegroundColour(wx.Colour(233, 113, 24))
        self.NotaF.Show(False)
        self.EmisF = wx.StaticText(id=wxID_WXPANEL6EMISF, label='', name='EmisF', parent=self, pos=wx.Point(305, 313), size=wx.Size(30, 20), style=wx.NO_3D | 0)
        self.EmisF.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.EmisF.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.EmisF.Show(False)
        self.LimiteF = wx.StaticText(id=wxID_WXPANEL6LIMITEF, label='', name='LimiteF', parent=self, pos=wx.Point(2, 320), size=wx.Size(30, 20), style=wx.NO_3D | 0)
        self.LimiteF.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.LimiteF.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.LimiteF.Show(True)
        self.NotaG = wx.StaticText(id=wxID_WXPANEL6NOTAG, label=_('G'), name='NotaG', parent=self, pos=wx.Point(400, 353), size=wx.Size(30, 30), style=wx.NO_3D | 0)
        self.NotaG.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'MS Shell Dlg 2'))
        self.NotaG.SetForegroundColour(wx.Colour(223, 0, 36))
        self.NotaG.Show(False)
        self.EmisG = wx.StaticText(id=wxID_WXPANEL6EMISG, label='', name='EmisG', parent=self, pos=wx.Point(335, 358), size=wx.Size(30, 20), style=wx.NO_3D | 0)
        self.EmisG.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.EmisG.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.EmisG.Show(False)
        self.LimiteG = wx.StaticText(id=wxID_WXPANEL6LIMITEG, label='', name='LimiteG', parent=self, pos=wx.Point(2, 364), size=wx.Size(30, 20), style=wx.NO_3D | 0)
        self.LimiteG.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.LimiteG.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.LimiteG.Show(True)
        self.Titulo = wx.StaticText(id=wxID_WXPANEL6TITULO, label=_('Calificación energética de edificios'), name='Titulo', parent=self, pos=wx.Point(15, 20), size=wx.Size(50, 20), style=0)
        self.Titulo.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Titulo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.Indicador = wx.StaticText(id=wxID_WXPANEL6INDICADOR, label=_('Indicador kgCO2/m2'), name='Titulo', parent=self, pos=wx.Point(15, 50), size=wx.Size(50, 20), style=0)
        self.Indicador.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Indicador.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.EdifObjeto = wx.StaticText(id=wxID_WXPANEL6EDIFOBJETO, label=_('Edificio objeto'), name='EdifObj', parent=self, pos=wx.Point(580, 75), size=wx.Size(50, 20), style=0)
        self.EdifObjeto.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.EdifObjeto.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.DdaCal = wx.StaticText(id=wxID_WXPANEL6DDACAL, label=_('Demanda de calefacción'), name='DdaCal', parent=self, pos=wx.Point(500, 125), size=wx.Size(50, 20), style=0)
        self.DdaCal.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.DdaCal.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.Unidades1 = wx.StaticText(id=wxID_WXPANEL6UNIDADES1, label=_('(kWh/m2)'), name='Unidades1', parent=self, pos=wx.Point(550, 140), size=wx.Size(50, 15), style=0)
        self.Unidades1.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Unidades1.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.DdaRef = wx.StaticText(id=wxID_WXPANEL6DDAREF, label=_('Demanda de refrigeración'), name='DdaRef', parent=self, pos=wx.Point(500, 165), size=wx.Size(50, 20), style=0)
        self.DdaRef.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.DdaRef.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.Unidades2 = wx.StaticText(id=wxID_WXPANEL6UNIDADES2, label=_('(kWh/m2)'), name='Unidades2', parent=self, pos=wx.Point(550, 180), size=wx.Size(50, 15), style=0)
        self.Unidades2.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Unidades2.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.EmisCal = wx.StaticText(id=wxID_WXPANEL6EMISCAL, label=_('Emisiones de calefacción'), name='EmisCal', parent=self, pos=wx.Point(500, 205), size=wx.Size(50, 20), style=0)
        self.EmisCal.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.EmisCal.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.Unidades3 = wx.StaticText(id=wxID_WXPANEL6UNIDADES3, label=_('(kg CO2/m2)'), name='Unidades3', parent=self, pos=wx.Point(550, 220), size=wx.Size(50, 15), style=0)
        self.Unidades3.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Unidades3.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.EmisRef = wx.StaticText(id=wxID_WXPANEL6EMISREF, label=_('Emisiones de refrigeración'), name='EmisRef', parent=self, pos=wx.Point(500, 245), size=wx.Size(50, 20), style=0)
        self.EmisRef.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.EmisRef.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.Unidades4 = wx.StaticText(id=wxID_WXPANEL6UNIDADES4, label=_('(kg CO2/m2)'), name='Unidades4', parent=self, pos=wx.Point(550, 260), size=wx.Size(50, 15), style=0)
        self.Unidades4.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Unidades4.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.EmisACS = wx.StaticText(id=wxID_WXPANEL6EMISACS, label=_('Emisiones de ACS'), name='EmisACS', parent=self, pos=wx.Point(500, 285), size=wx.Size(50, 20), style=0)
        self.EmisACS.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.EmisACS.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.Unidades5 = wx.StaticText(id=wxID_WXPANEL6UNIDADES5, label=_('(kg CO2/m2)'), name='Unidades5', parent=self, pos=wx.Point(550, 300), size=wx.Size(50, 15), style=0)
        self.Unidades5.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Unidades5.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.EmisIluminacion = wx.StaticText(id=wxID_WXPANEL6EMISILUMINACION, label=_('Emisiones de iluminación'), name='EmisIluminacion', parent=self, pos=wx.Point(500, 325), size=wx.Size(50, 20), style=0)
        self.EmisIluminacion.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.EmisIluminacion.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.EmisIluminacion.Show(False)
        self.Unidades6 = wx.StaticText(id=wxID_WXPANEL6UNIDADES6, label=_('(kg CO2/m2)'), name='Unidades6', parent=self, pos=wx.Point(550, 340), size=wx.Size(50, 15), style=0)
        self.Unidades6.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Unidades6.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.Unidades6.Show(False)
        self.balanceContribuciones = wx.StaticText(id=wxID_WXPANEL6BALANCECONTRIBUCIONES, label=_('Balance contribuciones'), name='balanceContribuciones', parent=self, pos=wx.Point(500, 380), size=wx.Size(50, 20), style=0)
        self.balanceContribuciones.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.balanceContribuciones.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.balanceContribuciones.Show(False)
        self.balanceContribucionesUnidades = wx.StaticText(id=wxID_WXPANEL6BALANCECONTRIBUCIONES6, label=_('(kg CO2/m2)'), name='balanceContribuciones', parent=self, pos=wx.Point(550, 395), size=wx.Size(50, 15), style=0)
        self.balanceContribucionesUnidades.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.balanceContribucionesUnidades.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.balanceContribucionesUnidades.Show(False)
        self.ValorDdaCal = wx.StaticText(id=wxID_WXPANEL6VALORDDACAL, label='', name='ValorDdaCal', parent=self, pos=wx.Point(725, 125), size=wx.Size(50, 20), style=0)
        self.ValorDdaCal.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.ValorDdaCal.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.ValorDdaCal.Show(True)
        self.ValorDdaRef = wx.StaticText(id=wxID_WXPANEL6VALORDDAREF, label='', name='ValorDdaRef', parent=self, pos=wx.Point(725, 165), size=wx.Size(50, 20), style=0)
        self.ValorDdaRef.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.ValorDdaRef.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.ValorDdaRef.Show(True)
        self.ValorEmisCal = wx.StaticText(id=wxID_WXPANEL6VALOREMISCAL, label='', name='ValorEmisCal', parent=self, pos=wx.Point(725, 205), size=wx.Size(50, 20), style=0)
        self.ValorEmisCal.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.ValorEmisCal.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.ValorEmisCal.Show(True)
        self.ValorEmisRef = wx.StaticText(id=wxID_WXPANEL6VALOREMISREF, label='', name='ValorEmisRef', parent=self, pos=wx.Point(725, 245), size=wx.Size(50, 20), style=0)
        self.ValorEmisRef.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.ValorEmisRef.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.ValorEmisRef.Show(True)
        self.ValorEmisACS = wx.StaticText(id=wxID_WXPANEL6VALOREMISACS, label='', name='ValorEmisACS', parent=self, pos=wx.Point(725, 285), size=wx.Size(50, 20), style=0)
        self.ValorEmisACS.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.ValorEmisACS.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.ValorEmisACS.Show(True)
        self.ValorEmisIluminacion = wx.StaticText(id=wxID_WXPANEL6VALOREMISILUMINACION, label='', name='ValorEmisIluminacion', parent=self, pos=wx.Point(725, 325), size=wx.Size(50, 20), style=0)
        self.ValorEmisIluminacion.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.ValorEmisIluminacion.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.ValorEmisIluminacion.Show(False)
        self.valorBalanceContribuciones = wx.StaticText(id=wxID_WXPANEL6VALORBALANCECONTRIBUCIONES, label='', name='valorBalanceContribuciones', parent=self, pos=wx.Point(725, 380), size=wx.Size(50, 20), style=0)
        self.valorBalanceContribuciones.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.valorBalanceContribuciones.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))
        self.valorBalanceContribuciones.Show(False)
        self.NotaDdaCal = wx.StaticText(id=wxID_WXPANEL6NOTADDACAL, label='', name='NotaDdaCal', parent=self, pos=wx.Point(780, 125), size=wx.Size(50, 20), style=0)
        self.NotaDdaCal.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.NotaDdaCal.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.NotaDdaCal.Show(True)
        self.NotaDdaRef = wx.StaticText(id=wxID_WXPANEL6NOTADDAREF, label='', name='NotaDdaRef', parent=self, pos=wx.Point(780, 165), size=wx.Size(50, 20), style=0)
        self.NotaDdaRef.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.NotaDdaRef.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.NotaEmisCal = wx.StaticText(id=wxID_WXPANEL6NOTAEMISCAL, label='', name='NotaEmisCal', parent=self, pos=wx.Point(780, 205), size=wx.Size(50, 20), style=0)
        self.NotaEmisCal.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.NotaEmisCal.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.NotaEmisCal.Show(True)
        self.NotaEmisRef = wx.StaticText(id=wxID_WXPANEL6NOTAEMISREF, label='', name='NotaEmisRef', parent=self, pos=wx.Point(780, 245), size=wx.Size(50, 20), style=0)
        self.NotaEmisRef.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.NotaEmisRef.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.NotaEmisACS = wx.StaticText(id=wxID_WXPANEL6NOTAEMISACS, label='', name='NotaEmisACS', parent=self, pos=wx.Point(780, 285), size=wx.Size(50, 20), style=0)
        self.NotaEmisACS.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.NotaEmisACS.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.NotaEmisACS.Show(True)
        self.NotaEmisIluminacion = wx.StaticText(id=wxID_WXPANEL6NOTAEMISILUMINACION, label='', name='NotaEmisACS', parent=self, pos=wx.Point(780, 325), size=wx.Size(50, 20), style=0)
        self.NotaEmisIluminacion.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.NotaEmisIluminacion.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.NotaEmisIluminacion.Show(False)
        self.Cerrar = wx.Button(id=wxID_WXPANEL6CERRAR, label=_('Cerrar'), name='Cerrar', parent=self, pos=wx.Point(860, 600), size=wx.Size(80, 23), style=0)
        self.Cerrar.Bind(wx.EVT_BUTTON, self.OnCerrarButton, id=wxID_WXPANEL6CERRAR)
        self.Cerrar.SetBackgroundColour(wx.Color(240, 240, 240))

    def OnCerrarButton(self, event):
        """
        Metodo: OnCerrarButton

        ARGUMENTOS:
                event:
        """
        identificador = self.GetId()
        for i in range(len(self.parent.parent.paneles)):
            if self.parent.parent.paneles[i].GetId() == identificador:
                self.parent.parent.paneles.pop(i)
                break

        pagina = self.parent.GetSelection()
        self.parent.DeletePage(pagina)

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
        self.nombre = _('Calificación Energética')