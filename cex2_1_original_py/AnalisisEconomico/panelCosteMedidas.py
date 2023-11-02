# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: AnalisisEconomico\panelCosteMedidas.pyc
# Compiled at: 2015-02-23 10:37:31
"""
Modulo: panelCosteMedidas.py

"""
import wx
from AnalisisEconomico.miGridAnalisisEconomico import MyGrid
from Envolvente.comprobarCampos import Comprueba
wxID_PANEL1, wxID_PANEL1GRID1, wxID_PANEL1TITULOTEXT, wxID_PANEL1STATICTEXT1 = [ wx.NewId() for _init_ctrls in range(4) ]

class Panel1(wx.Panel):
    """
    Clase: Panel1 del modulo panelCosteMedidas.py

    """

    def _init_coll_listaMedidas_Columns(self, parent):
        """
        Metodo: _init_coll_listaMedidas_Columns

        ARGUMENTOS:
                parent:
        """
        parent.CreateGrid(0, 6)
        parent.SetColLabelValue(0, _('Medida de mejora'))
        parent.SetColLabelValue(1, _('Conjunto'))
        parent.SetColLabelValue(2, _('Tipo de medida'))
        parent.SetColLabelValue(3, _('Vida útil (años)'))
        parent.SetColLabelValue(4, _('Coste de medida (€)'))
        parent.SetColLabelValue(5, _('Incremento coste\nmantenimiento anual (€)'))
        parent.AutoSizeColumns()

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
        wx.Panel.__init__(self, id=id_prnt, name=name_prnt, parent=prnt, pos=pos_prnt, size=size_prnt, style=style_prnt | wx.TAB_TRAVERSAL)
        self.SetBackgroundColour('white')
        self.tituloText = wx.StaticText(id=wxID_PANEL1STATICTEXT1, label=_('Valoración económica de las medidas de mejora de eficiencia energética'), name='tituloText', parent=self, pos=wx.Point(15, 24), size=wx.Size(608, 18), style=0)
        self.tituloText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.tituloText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.listaMedidas = MyGrid(id=wxID_PANEL1GRID1, parent=self, pos=wx.Point(15, 70), size=wx.Size(695, 400), style=wx.RAISED_BORDER | wx.TAB_TRAVERSAL)
        self.listaMedidas.Bind(wx.grid.EVT_GRID_CELL_CHANGE, self.OnListaMedidas, id=wxID_PANEL1GRID1)
        self._init_coll_listaMedidas_Columns(self.listaMedidas)
        self.datosCostes = []
        self.incluirMedidas()

    def comprobarDatos(self):
        """
        Metodo: comprobarDatos

        """
        self.datosCostes = []
        for i in range(self.listaMedidas.GetNumberRows()):
            datos = []
            for j in range(self.listaMedidas.GetNumberCols()):
                datos.append(self.listaMedidas.GetCellValue(i, j))
                if j == 3 or j == 4 or j == 5:
                    if Comprueba(self.listaMedidas.GetCellValue(i, j), 2, '', _('mal definido'), 0).ErrorDevuelto != '':
                        return str(i + 1) + ';' + self.listaMedidas.GetColLabelValue(j)

            self.datosCostes.append(datos)

        return self.datosCostes

    def cogerDatos(self):
        """
        Metodo: cogerDatos
        """
        for i in range(self.listaMedidas.GetNumberRows()):
            for j in range(self.listaMedidas.GetNumberCols()):
                if j in (3, 4, 5):
                    dato = self.listaMedidas.GetCellValue(i, j)
                    if ',' in dato:
                        dato = dato.replace(',', '.')
                        self.listaMedidas.SetCellValue(i, j, dato)

        self.datosCostes = []
        for i in range(self.listaMedidas.GetNumberRows()):
            datos = []
            for j in range(self.listaMedidas.GetNumberCols()):
                datos.append(self.listaMedidas.GetCellValue(i, j))

            self.datosCostes.append(datos)

        return self.datosCostes

    def cargarDatos(self, datos):
        """
        Metodo: cargarDatos

        ARGUMENTOS:
                datos:
        """
        self.datosCostes = []
        for i in datos:
            self.datosCostes.append(i)

        self.incluirMedidas()

    def compruebaDatosMedida(self, nombre, grupo):
        """
        Metodo: compruebaDatosMedida

        ARGUMENTOS:
                nombre:
                grupo): #carga los costes asociados a cada medi:
        """
        for i in self.datosCostes:
            if i[0] == nombre and i[1] == grupo:
                return i

        return False

    def OnListaMedidas(self, event):
        """
        Metodo: OnListaMedidas

        ARGUMENTOS:
                event:
        """
        pass

    def incluirMedidas(self):
        """
        Metodo: incluirMedidas

                self):    #carga de listado de medidas en la tab:
        """
        if self.listaMedidas.GetNumberRows() != 0:
            self.listaMedidas.DeleteRows(0, self.listaMedidas.GetNumberRows())
        listado = self.parent.parent.parent.listadoConjuntosMMUsuario
        cont = 0
        for i in range(len(listado)):
            if type(listado[i].mejoras) == type('edificio completo'):
                self.listaMedidas.AppendRows(1)
                self.listaMedidas.SetCellValue(cont, 0, 'Nuevo Edificio Definido por el Usuario')
                self.listaMedidas.SetCellValue(cont, 1, listado[i].nombre)
                self.listaMedidas.SetReadOnly(cont, 1)
                self.listaMedidas.SetCellValue(cont, 2, 'Definido por el Usuario')
                self.listaMedidas.SetReadOnly(cont, 2)
                arrayMedida = self.compruebaDatosMedida('Nuevo Edificio Definido por el Usuario', listado[i].nombre)
                if arrayMedida != False:
                    self.listaMedidas.SetCellValue(cont, 3, arrayMedida[3])
                    self.listaMedidas.SetCellValue(cont, 4, arrayMedida[4])
                    if arrayMedida[5] == '':
                        arrayMedida[5] = str(0.0)
                    self.listaMedidas.SetCellValue(cont, 5, arrayMedida[5])
                else:
                    self.listaMedidas.SetCellValue(cont, 5, '0.0')
                cont = cont + 1
            else:
                if listado[i].mejoras[1][2] == True:
                    self.listaMedidas.AppendRows(1)
                    self.listaMedidas.SetCellValue(cont, 0, 'Nuevas Instalaciones')
                    self.listaMedidas.SetReadOnly(cont, 0)
                    self.listaMedidas.SetCellValue(cont, 1, listado[i].nombre)
                    self.listaMedidas.SetReadOnly(cont, 1)
                    self.listaMedidas.SetCellValue(cont, 2, 'Instalaciones')
                    self.listaMedidas.SetReadOnly(cont, 2)
                    arrayMedida = self.compruebaDatosMedida('Nuevas Instalaciones', listado[i].nombre)
                    if arrayMedida != False:
                        self.listaMedidas.SetCellValue(cont, 3, arrayMedida[3])
                        self.listaMedidas.SetCellValue(cont, 4, arrayMedida[4])
                        if arrayMedida[5] == '':
                            arrayMedida[5] = str(0.0)
                        self.listaMedidas.SetCellValue(cont, 5, arrayMedida[5])
                    else:
                        self.listaMedidas.SetCellValue(cont, 5, '0.0')
                    cont = cont + 1
                if listado[i].mejoras[0] != []:
                    for j in range(len(listado[i].mejoras[0])):
                        self.listaMedidas.AppendRows(1)
                        self.listaMedidas.SetCellValue(cont, 0, listado[i].mejoras[0][j][0])
                        self.listaMedidas.SetReadOnly(cont, 0)
                        self.listaMedidas.SetCellValue(cont, 1, listado[i].nombre)
                        self.listaMedidas.SetReadOnly(cont, 1)
                        self.listaMedidas.SetCellValue(cont, 2, listado[i].mejoras[0][j][1])
                        self.listaMedidas.SetReadOnly(cont, 2)
                        arrayMedida = self.compruebaDatosMedida(listado[i].mejoras[0][j][0], listado[i].nombre)
                        if arrayMedida != False:
                            self.listaMedidas.SetCellValue(cont, 3, arrayMedida[3])
                            self.listaMedidas.SetCellValue(cont, 4, arrayMedida[4])
                            if arrayMedida[5] == '':
                                arrayMedida[5] = str(0.0)
                            self.listaMedidas.SetCellValue(cont, 5, arrayMedida[5])
                        else:
                            self.listaMedidas.SetCellValue(cont, 5, '0.0')
                        cont = cont + 1

        self.listaMedidas.AutoSizeColumns()

    def __init__(self, parent, id, pos, size, style, name, real_parent):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
                id:
                pos:
                size:
                style:
                name:
                real_parent:
        """
        self.parent = real_parent
        self._init_ctrls(parent, id, pos, size, style, name)