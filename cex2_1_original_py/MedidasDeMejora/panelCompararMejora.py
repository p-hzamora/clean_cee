# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: MedidasDeMejora\panelCompararMejora.pyc
# Compiled at: 2015-02-11 10:07:39
"""
Modulo: panelCompararMejora.py

"""
import wx
wxID_PANELCOMPARARMEJORA, wxID_wxID_PANELCOMPARARMEJORATEXT, wxID_TABLAMEDIDASMEJORA, wxID_LISTADOMEDIDASTEXT = [ wx.NewId() for _init_ctrls in range(4) ]

class panelCompararMejora(wx.Panel):
    """
    Clase: panelCompararMejora del modulo panelCompararMejora.py

    """

    def _init_coll_TablaMedidas_Columns(self, parent):
        """
        Metodo: _init_coll_TablaMedidas_Columns

        ARGUMENTOS:
                parent:
        """
        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading=_('Medidas de Mejora'), width=200)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_CENTER, heading=_('Dda Cal.'), width=70)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_CENTER, heading=_('Dda Ref.'), width=70)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_CENTER, heading=_('Emis. Cal.'), width=70)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_CENTER, heading=_('Emis. Ref.'), width=70)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_CENTER, heading=_('Emis. ACS'), width=70)
        parent.InsertColumn(col=6, format=wx.LIST_FORMAT_CENTER, heading=_('Emis. Globales'), width=74)
        parent.InsertColumn(col=7, format=wx.LIST_FORMAT_CENTER, heading=_('Ahorro'), width=70)

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
        self.SetBackgroundColour('white')
        self.MedidasMejoraText = wx.StaticText(id=wxID_wxID_PANELCOMPARARMEJORATEXT, label=_('Comparación de los conjuntos de medidas de mejora definidas'), name='MedidasMejora', parent=self, pos=wx.Point(0, 0), size=wx.Size(400, 14), style=0)
        self.MedidasMejoraText.Enable(True)
        self.MedidasMejoraText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.MedidasMejoraText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.ListadoMedidasText = wx.StaticBox(id=wxID_LISTADOMEDIDASTEXT, label=_('Listado comparativo de conjuntos de medidas de mejora'), name='ListadoMedidasText', parent=self, pos=wx.Point(0, 89), size=wx.Size(710, 360), style=0)
        self.ListadoMedidasText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.ListadoMedidasText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.TablaMedidas = wx.ListCtrl(id=wxID_TABLAMEDIDASMEJORA, name='TablaMedidas', parent=self, pos=wx.Point(15, 114), size=wx.Size(680, 320), style=wx.LC_REPORT)
        self._init_coll_TablaMedidas_Columns(self.TablaMedidas)
        self.CargarDatos()

    def CargarDatos(self):
        """
        Metodo: CargarDatos

        """
        self.TablaMedidas.DeleteAllItems()
        self.TablaMedidas.Append(['CASO BASE',
         str(round(self.parent.parent.parent.objEdificio.datosResultados.ddaBrutaCal, 1)) + ' ' + str(self.parent.parent.parent.objEdificio.datosResultados.ddaBrutaCal_nota),
         str(round(self.parent.parent.parent.objEdificio.datosResultados.ddaBrutaRef, 1)) + ' ' + str(self.parent.parent.parent.objEdificio.datosResultados.ddaBrutaRef_nota),
         str(round(self.parent.parent.parent.objEdificio.datosResultados.emisionesCal, 1)) + ' ' + str(self.parent.parent.parent.objEdificio.datosResultados.emisionesCal_nota),
         str(round(self.parent.parent.parent.objEdificio.datosResultados.emisionesRef, 1)) + ' ' + str(self.parent.parent.parent.objEdificio.datosResultados.emisionesRef_nota),
         str(round(self.parent.parent.parent.objEdificio.datosResultados.emisionesACS, 1)) + ' ' + str(self.parent.parent.parent.objEdificio.datosResultados.emisionesACS_nota),
         str(round(self.parent.parent.parent.objEdificio.datosResultados.emisionesMostrar, 1)) + ' ' + str(self.parent.parent.parent.objEdificio.datosResultados.emisiones_nota),
         '-'])
        for i in self.parent.parent.parent.listadoConjuntosMMUsuario:
            if i.datosNuevoEdificio.casoValido == True:
                self.TablaMedidas.Append([i.nombre,
                 str(round(i.datosNuevoEdificio.datosResultados.ddaBrutaCal, 1)) + ' ' + str(i.datosNuevoEdificio.datosResultados.ddaBrutaCal_nota),
                 str(round(i.datosNuevoEdificio.datosResultados.ddaBrutaRef, 1)) + ' ' + str(i.datosNuevoEdificio.datosResultados.ddaBrutaRef_nota),
                 str(round(i.datosNuevoEdificio.datosResultados.emisionesCal, 1)) + ' ' + str(i.datosNuevoEdificio.datosResultados.emisionesCal_nota),
                 str(round(i.datosNuevoEdificio.datosResultados.emisionesRef, 1)) + ' ' + str(i.datosNuevoEdificio.datosResultados.emisionesRef_nota),
                 str(round(i.datosNuevoEdificio.datosResultados.emisionesACS, 1)) + ' ' + str(i.datosNuevoEdificio.datosResultados.emisionesACS_nota),
                 str(round(i.datosNuevoEdificio.datosResultados.emisionesMostrar, 1)) + ' ' + str(i.datosNuevoEdificio.datosResultados.emisiones_nota),
                 str(round(i.ahorro[-1], 1)) + '%'])

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
        self.parent = parent
        self._init_ctrls(parent, id, pos, size, style, name)


class panelCompararMejoraTerciario(panelCompararMejora):
    """
    Clase: panelCompararMejoraTerciario del modulo panelCompararMejora.py

    """

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
        panelCompararMejora.__init__(self, parent, id, pos, size, style, name)

    def _init_coll_TablaMedidas_Columns(self, parent):
        """
        Metodo: _init_coll_TablaMedidas_Columns

        ARGUMENTOS:
                parent:
        """
        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading=_('Medidas de Mejora'), width=200)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_CENTER, heading=_('Dda Cal.'), width=60)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_CENTER, heading=_('Dda Ref.'), width=60)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_CENTER, heading=_('Emis. Cal.'), width=60)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_CENTER, heading=_('Emis. Ref.'), width=60)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_CENTER, heading=_('Emis. ACS'), width=60)
        parent.InsertColumn(col=6, format=wx.LIST_FORMAT_CENTER, heading=_('Emis. Iluminación'), width=100)
        parent.InsertColumn(col=7, format=wx.LIST_FORMAT_CENTER, heading=_('Emis. Globales'), width=60)
        parent.InsertColumn(col=8, format=wx.LIST_FORMAT_CENTER, heading=_('Ahorro'), width=60)

    def CargarDatos(self):
        """
        Metodo: CargarDatos

        """
        self.TablaMedidas.DeleteAllItems()
        self.TablaMedidas.Append(['CASO BASE',
         str(round(self.parent.parent.parent.objEdificio.datosResultados.ddaBrutaCal, 1)) + ' ' + str(self.parent.parent.parent.objEdificio.datosResultados.ddaBrutaCal_nota),
         str(round(self.parent.parent.parent.objEdificio.datosResultados.ddaBrutaRef, 1)) + ' ' + str(self.parent.parent.parent.objEdificio.datosResultados.ddaBrutaRef_nota),
         str(round(self.parent.parent.parent.objEdificio.datosResultados.emisionesCal, 1)) + ' ' + str(self.parent.parent.parent.objEdificio.datosResultados.emisionesCal_nota),
         str(round(self.parent.parent.parent.objEdificio.datosResultados.emisionesRef, 1)) + ' ' + str(self.parent.parent.parent.objEdificio.datosResultados.emisionesRef_nota),
         str(round(self.parent.parent.parent.objEdificio.datosResultados.emisionesACS, 1)) + ' ' + str(self.parent.parent.parent.objEdificio.datosResultados.emisionesACS_nota),
         str(round(self.parent.parent.parent.objEdificio.datosResultados.emisionesIlum, 1)) + ' ' + str(self.parent.parent.parent.objEdificio.datosResultados.emisionesIlum_nota),
         str(round(self.parent.parent.parent.objEdificio.datosResultados.emisionesMostrar, 1)) + ' ' + str(self.parent.parent.parent.objEdificio.datosResultados.emisiones_nota),
         '-'])
        for i in self.parent.parent.parent.listadoConjuntosMMUsuario:
            if i.datosNuevoEdificio.casoValido == True:
                self.TablaMedidas.Append([i.nombre,
                 str(round(i.datosNuevoEdificio.datosResultados.ddaBrutaCal, 1)) + ' ' + str(i.datosNuevoEdificio.datosResultados.ddaBrutaCal_nota),
                 str(round(i.datosNuevoEdificio.datosResultados.ddaBrutaRef, 1)) + ' ' + str(i.datosNuevoEdificio.datosResultados.ddaBrutaRef_nota),
                 str(round(i.datosNuevoEdificio.datosResultados.emisionesCal, 1)) + ' ' + str(i.datosNuevoEdificio.datosResultados.emisionesCal_nota),
                 str(round(i.datosNuevoEdificio.datosResultados.emisionesRef, 1)) + ' ' + str(i.datosNuevoEdificio.datosResultados.emisionesRef_nota),
                 str(round(i.datosNuevoEdificio.datosResultados.emisionesACS, 1)) + ' ' + str(i.datosNuevoEdificio.datosResultados.emisionesACS_nota),
                 str(round(i.datosNuevoEdificio.datosResultados.emisionesIlum, 1)) + ' ' + str(i.datosNuevoEdificio.datosResultados.emisionesIlum_nota),
                 str(round(i.datosNuevoEdificio.datosResultados.emisionesMostrar, 1)) + ' ' + str(i.datosNuevoEdificio.datosResultados.emisiones_nota),
                 str(round(i.ahorro[-1], 1)) + '%'])