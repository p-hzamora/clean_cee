# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: MedidasDeMejora\panelDefinirMedidasMejora.pyc
# Compiled at: 2015-05-28 16:57:29
"""
Modulo: panelDefinirMedidasMejora.py

"""
import wx, wx.glcanvas, MedidasDeMejora.ventanaAislamiento as ventanaAislamiento, MedidasDeMejora.ventanaHuecos as ventanaHuecos, MedidasDeMejora.ventanaPT as ventanaPT, MedidasDeMejora.anadirMedida as anadirMedida
from MedidasDeMejora.objetoGrupoMejoras import grupoMedidasMejora
import MedidasDeMejora.definicionInstalaciones as definicionInstalaciones, copy, logging, directorios
Directorio = directorios.BuscaDirectorios().Directorio
wxID_PANELDEFINIRMEDIDASMEJORAANADIR, wxID_PANELDEFINIRMEDIDASMEJORABORRAR, wxID_PANELDEFINIRMEDIDASMEJORADEFINIRMEDIDAMEJORA, wxID_PANELDEFINIRMEDIDASMEJORADEFINIRNUEVASMEDIDASTEXT, wxID_PANELDEFINIRMEDIDASMEJORADESCRIPCIONCUADRO, wxID_PANELDEFINIRMEDIDASMEJORADESCRIPCIONTEXT, wxID_PANELDEFINIRMEDIDASMEJORAMEJORAENVOLVENTECHOICE, wxID_PANELDEFINIRMEDIDASMEJORAMEJORAENVOLVENTETEXT, wxID_PANELDEFINIRMEDIDASMEJORAMEJORAINSTALACIONESCHOICE, wxID_PANELDEFINIRMEDIDASMEJORAMEJORAINSTALACIONESTEXT, wxID_PANELDEFINIRMEDIDASMEJORAMODIFICAR, wxID_PANELDEFINIRMEDIDASMEJORATABLAMEDIDASMEJORA, wxID_PANELDEFINIRMEDIDASMEJORATABLARESULTADOS, wxID_PANELDEFINIRMEDIDASMEJORAGUARDARCONJUNTOBUTTON, wxID_PANELDEFINIRMEDIDASMEJORAMODIFICARCONJUNTOBUTTON, wxID_PANELDEFINIRMEDIDASMEJORAELIMINARCONJUNTOBUTTON, wxID_PANELDEFINIRMEDIDASMEJORADEFINIRMEDIDAMEJORA2, wxID_LISTADOMEDIDASTEXT, wxID_RESULTADOMEDIDASTEXT, wxID_PANELDEFINIRMEDIDASMEJORAANADIR, wxID_wxPANEL6ETIQUETA, wxID_WXPANEL6EMISA, wxID_WXPANEL6NOTAA, wxID_WXPANEL6EMISB, wxID_WXPANEL6NOTAB, wxID_WXPANEL6EMISC, wxID_WXPANEL6NOTAC, wxID_WXPANEL6EMISD, wxID_WXPANEL6NOTAD, wxID_WXPANEL6EMISE, wxID_WXPANEL6NOTAE, wxID_WXPANEL6EMISF, wxID_WXPANEL6NOTAF, wxID_WXPANEL6EMISG, wxID_WXPANEL6NOTAG, wxID_PANELDEFINIRMEDIDASMEJORACARACTERISTICASTEXT, wxID_PANELDEFINIRMEDIDASMEJORACARACTERISTICASCUADRO, wxID_PANELDEFINIRMEDIDASMEJORAOTROSDATOSTEXT, wxID_PANELDEFINIRMEDIDASMEJORAOTROSDATOSCUADRO = [ wx.NewId() for _init_ctrls in range(39) ]

class panelDefinirMedidasMejora(wx.Panel):
    """
    Clase: panelDefinirMedidasMejora del modulo panelDefinirMedidasMejora.py

    """

    def _init_coll_TablaMedidasMejora_Columns(self, parent):
        """
        Metodo: _init_coll_TablaMedidasMejora_Columns

        ARGUMENTOS:
                parent:
        """
        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading=_('Medidas mejora'), width=430)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading=_('Tipo de medida'), width=245)

    def _init_coll_TablaResultados_Columns(self, parent):
        """
        Metodo: _init_coll_TablaResultados_Columns

        ARGUMENTOS:
                parent:
        """
        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_CENTER, heading=_('RESULTADOS'), width=175)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_CENTER, heading=_('Medidas mejora'), width=95)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_CENTER, heading=_('Caso base'), width=95)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_CENTER, heading=_('Ahorro'), width=95)

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
        self.DefinirNuevasMedidasText = wx.StaticText(id=wxID_PANELDEFINIRMEDIDASMEJORADEFINIRNUEVASMEDIDASTEXT, label=_('Conjunto de medidas de mejora'), name='DefinirNuevasMedidasText', parent=self, pos=wx.Point(0, 0), size=wx.Size(284, 14), style=0)
        self.DefinirNuevasMedidasText.Enable(True)
        self.DefinirNuevasMedidasText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.DefinirNuevasMedidasText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.DescripcionText = wx.StaticText(id=wxID_PANELDEFINIRMEDIDASMEJORADESCRIPCIONTEXT, label=_('Nombre conjunto medidas mejora'), name='DescripcionText', parent=self, pos=wx.Point(15, 40), size=wx.Size(210, 13), style=0)
        self.DescripcionCuadro = wx.TextCtrl(id=wxID_PANELDEFINIRMEDIDASMEJORADESCRIPCIONCUADRO, name='DescripcionCuadro', parent=self, pos=wx.Point(230, 38), size=wx.Size(480, 21), style=0, value=self.conjuntoMM.nombre)
        self.DescripcionCuadro.SetToolTip(wx.ToolTip(_('Indique el nombre del conjunto de medidas de mejora.')))
        self.caracteristicasText = wx.StaticText(id=wxID_PANELDEFINIRMEDIDASMEJORACARACTERISTICASTEXT, label=_('Características'), name='CaracteristicasText', parent=self, pos=wx.Point(15, 71), size=wx.Size(100, 13), style=0)
        self.caracteristicasCuadro = wx.TextCtrl(id=wxID_PANELDEFINIRMEDIDASMEJORACARACTERISTICASCUADRO, name='CaracteristicasCuadro', parent=self, pos=wx.Point(130, 69), size=wx.Size(580, 48), style=wx.TE_MULTILINE, value=self.conjuntoMM.caracteristicas)
        self.caracteristicasCuadro.SetToolTip(wx.ToolTip(_('Indique las características técnicas de la medida (modelo de equipos, materiales, parámetros característicos)')))
        self.otrosDatosText = wx.StaticText(id=wxID_PANELDEFINIRMEDIDASMEJORAOTROSDATOSTEXT, label=_('Otros datos'), name='otrosDatosText', parent=self, pos=wx.Point(15, 129), size=wx.Size(100, 13), style=0)
        self.otrosDatosCuadro = wx.TextCtrl(id=wxID_PANELDEFINIRMEDIDASMEJORAOTROSDATOSCUADRO, name='otrosDatosCuadro', parent=self, pos=wx.Point(130, 127), size=wx.Size(580, 48), style=wx.TE_MULTILINE, value=self.conjuntoMM.otrosDatos)
        self.otrosDatosCuadro.SetToolTip(wx.ToolTip(_('Indique otros datos de interés del conjunto de medidas de mejora.')))
        self.ListadoMedidasText = wx.StaticBox(id=wxID_LISTADOMEDIDASTEXT, label=_('Listado medidas mejora incluidas en el conjunto'), name='ListadoMedidasText', parent=self, pos=wx.Point(0, 184), size=wx.Size(710, 190), style=0)
        self.ListadoMedidasText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.ListadoMedidasText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.ListadoMedidasText.SetToolTip(wx.ToolTip(_('Listado de medidas de mejora que conforman el conjunto.')))
        self.TablaMedidasMejora = wx.ListCtrl(id=wxID_PANELDEFINIRMEDIDASMEJORATABLAMEDIDASMEJORA, name='TablaMedidasMejora', parent=self, pos=wx.Point(15, 203), size=wx.Size(680, 125), style=wx.LC_REPORT)
        self._init_coll_TablaMedidasMejora_Columns(self.TablaMedidasMejora)
        self.TablaMedidasMejora.Bind(wx.EVT_LIST_ITEM_SELECTED, self.Pinchar_TablaMedidasMejora, id=wxID_PANELDEFINIRMEDIDASMEJORATABLAMEDIDASMEJORA)
        self.TablaMedidasMejora.SetToolTip(wx.ToolTip(_('Listado de medidas de mejora que conforman el conjunto.')))
        self.Anadir = wx.Button(id=wxID_PANELDEFINIRMEDIDASMEJORAANADIR, label=_('Añadir medida'), name=_('Añadir'), parent=self, pos=wx.Point(15, 338), size=wx.Size(100, 21), style=0)
        self.Anadir.Bind(wx.EVT_BUTTON, self.OnAnadirButton, id=wxID_PANELDEFINIRMEDIDASMEJORAANADIR)
        self.Anadir.SetToolTip(wx.ToolTip(_('Añadir una nueva medida de mejora al conjunto')))
        self.Modificar = wx.Button(id=wxID_PANELDEFINIRMEDIDASMEJORAMODIFICAR, label=_('Modificar medida'), name=_('Modificar'), parent=self, pos=wx.Point(130, 338), size=wx.Size(100, 21), style=0)
        self.Modificar.Bind(wx.EVT_BUTTON, self.OnModificarButton, id=wxID_PANELDEFINIRMEDIDASMEJORAMODIFICAR)
        self.Modificar.SetToolTip(wx.ToolTip(_('Modificar la medida de mejora seleccionada.')))
        self.Borrar = wx.Button(id=wxID_PANELDEFINIRMEDIDASMEJORABORRAR, label=_('Borrar medida'), name=_('Borrar'), parent=self, pos=wx.Point(290, 338), size=wx.Size(100, 21), style=0)
        self.Borrar.Bind(wx.EVT_BUTTON, self.OnBorrarButton, id=wxID_PANELDEFINIRMEDIDASMEJORABORRAR)
        self.Borrar.SetToolTip(wx.ToolTip(_('Eliminar la medida de mejora seleccionada.')))
        self.ResultadosMedidasText = wx.StaticBox(id=wxID_RESULTADOMEDIDASTEXT, label=_('Calificación energética del edificio con el conjunto de medidas de mejora'), name='ResultadosMedidasText', parent=self, pos=wx.Point(0, 384), size=wx.Size(710, 200), style=0)
        self.ResultadosMedidasText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.ResultadosMedidasText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.ResultadosMedidasText.Show(False)
        self.ResultadosMedidasText.SetToolTip(wx.ToolTip(_('Resultados al implementar las medidas de mejora definidas.')))
        self.TablaResultados = wx.ListCtrl(id=wxID_PANELDEFINIRMEDIDASMEJORATABLARESULTADOS, name='TablaResultados', parent=self, pos=wx.Point(15, 414), size=wx.Size(465, 155), style=wx.LC_REPORT)
        self.TablaResultados.Enable(False)
        self.TablaResultados.Show(False)
        self.TablaResultados.SetHelpText('')
        self._init_coll_TablaResultados_Columns(self.TablaResultados)
        self.TablaResultados.SetToolTip(wx.ToolTip(_('Resultados al implementar las medidas de mejora definidas.')))
        self.Etiqueta = wx.StaticBitmap(bitmap=wx.Bitmap(Directorio + '/Imagenes/etiqueta_transparente_peque.gif', wx.BITMAP_TYPE_GIF), id=wxID_wxPANEL6ETIQUETA, name='Etiqueta', parent=self, pos=wx.Point(484, 418), size=wx.Size(138, 147), style=0)
        self.Etiqueta.Show(False)
        self.Etiqueta.SetToolTip(wx.ToolTip(_('Resultados al implementar las medidas de mejora definidas.')))
        self.NotaA = wx.StaticText(id=wxID_WXPANEL6NOTAA, label=_('A'), name='NotaA', parent=self, pos=wx.Point(610, 415), size=wx.Size(15, 15), style=wx.NO_3D | 0)
        self.NotaA.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'MS Shell Dlg 2'))
        self.NotaA.SetForegroundColour(wx.Colour(0, 159, 60))
        self.NotaA.Show(False)
        self.EmisA = wx.StaticText(id=wxID_WXPANEL6EMISA, label='', name='EmisA', parent=self, pos=wx.Point(555, 416), size=wx.Size(15, 15), style=wx.NO_3D | 0)
        self.EmisA.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.EmisA.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.EmisA.Show(False)
        self.NotaB = wx.StaticText(id=wxID_WXPANEL6NOTAB, label=_('B'), name='NotaB', parent=self, pos=wx.Point(630, 437), size=wx.Size(15, 15), style=wx.NO_3D | 0)
        self.NotaB.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'MS Shell Dlg 2'))
        self.NotaB.SetForegroundColour(wx.Colour(43, 180, 49))
        self.NotaB.Show(False)
        self.EmisB = wx.StaticText(id=wxID_WXPANEL6EMISB, label='', name='EmisB', parent=self, pos=wx.Point(575, 438), size=wx.Size(15, 15), style=wx.NO_3D | 0)
        self.EmisB.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.EmisB.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.EmisB.Show(False)
        self.NotaC = wx.StaticText(id=wxID_WXPANEL6NOTAC, label=_('C'), name='NotaC', parent=self, pos=wx.Point(650, 460), size=wx.Size(15, 15), style=wx.NO_3D | 0)
        self.NotaC.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'MS Shell Dlg 2'))
        self.NotaC.SetForegroundColour(wx.Colour(179, 216, 0))
        self.NotaC.Show(False)
        self.EmisC = wx.StaticText(id=wxID_WXPANEL6EMISC, label='', name='EmisC', parent=self, pos=wx.Point(595, 461), size=wx.Size(15, 15), style=wx.NO_3D | 0)
        self.EmisC.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.EmisC.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.EmisC.Show(False)
        self.NotaD = wx.StaticText(id=wxID_WXPANEL6NOTAD, label=_('D'), name='NotaD', parent=self, pos=wx.Point(660, 482), size=wx.Size(15, 15), style=wx.NO_3D | 0)
        self.NotaD.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'MS Shell Dlg 2'))
        self.NotaD.SetForegroundColour(wx.Colour(248, 244, 0))
        self.NotaD.Show(False)
        self.EmisD = wx.StaticText(id=wxID_WXPANEL6EMISD, label='', name='EmisD', parent=self, pos=wx.Point(605, 483), size=wx.Size(15, 15), style=wx.NO_3D | 0)
        self.EmisD.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.EmisD.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.EmisD.Show(False)
        self.NotaE = wx.StaticText(id=wxID_WXPANEL6NOTAE, label=_('E'), name='NotaE', parent=self, pos=wx.Point(670, 506), size=wx.Size(15, 15), style=wx.NO_3D | 0)
        self.NotaE.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'MS Shell Dlg 2'))
        self.NotaE.SetForegroundColour(wx.Colour(244, 193, 0))
        self.NotaE.Show(False)
        self.EmisE = wx.StaticText(id=wxID_WXPANEL6EMISE, label='', name='EmisE', parent=self, pos=wx.Point(615, 507), size=wx.Size(15, 15), style=wx.NO_3D | 0)
        self.EmisE.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.EmisE.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.EmisE.Show(False)
        self.NotaF = wx.StaticText(id=wxID_WXPANEL6NOTAF, label=_('F'), name='NotaF', parent=self, pos=wx.Point(680, 528), size=wx.Size(15, 15), style=wx.NO_3D | 0)
        self.NotaF.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'MS Shell Dlg 2'))
        self.NotaF.SetForegroundColour(wx.Colour(233, 113, 24))
        self.NotaF.Show(False)
        self.EmisF = wx.StaticText(id=wxID_WXPANEL6EMISF, label='', name='EmisF', parent=self, pos=wx.Point(625, 529), size=wx.Size(15, 15), style=wx.NO_3D | 0)
        self.EmisF.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.EmisF.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.EmisF.Show(False)
        self.NotaG = wx.StaticText(id=wxID_WXPANEL6NOTAG, label=_('G'), name='NotaG', parent=self, pos=wx.Point(690, 550), size=wx.Size(30, 30), style=wx.NO_3D | 0)
        self.NotaG.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'MS Shell Dlg 2'))
        self.NotaG.SetForegroundColour(wx.Colour(223, 0, 36))
        self.NotaG.Show(False)
        self.EmisG = wx.StaticText(id=wxID_WXPANEL6EMISG, label='', name='EmisG', parent=self, pos=wx.Point(635, 551), size=wx.Size(15, 15), style=wx.NO_3D | 0)
        self.EmisG.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.EmisG.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.EmisG.Show(False)

    def comprobarAislamiento(self, elemento):
        """
        Metodo: comprobarAislamiento

        ARGUMENTOS:
                elemento:
        """
        if elemento[2][0] == False and elemento[2][1] == False and elemento[2][2] == False and elemento[2][12][0] == False:
            return False
        fachada = False
        cubierta = False
        suelo = False
        piVertical = False
        piHorizontalSuperior = False
        piHorizontalInferior = False
        for i in self.conjuntoMedidasEnvolvente:
            if i[0] != elemento[0]:
                if i[1] == 'Adición de Aislamiento Térmico':
                    if i[2][0] == True:
                        fachada = True
                    if i[2][1] == True:
                        cubierta = True
                    if i[2][2] == True:
                        suelo = True
                    if i[2][12][0] == True:
                        if i[2][12][1] == True:
                            piVertical = True
                        if i[2][12][2] == True:
                            piHorizontalSuperior = True
                        if i[2][12][3] == True:
                            piHorizontalInferior = True

        error = ''
        if elemento[2][0] == True and fachada == True:
            error += 'fachadas'
        if elemento[2][1] == True and cubierta == True:
            if error != '':
                error += ', '
            error += 'cubiertas'
        if elemento[2][2] == True and suelo == True:
            if error != '':
                error += ', '
            error += 'suelos'
        if elemento[2][12][1] == True and piVertical == True:
            if error != '':
                error += ', '
            error += 'partición interior vertical'
        if elemento[2][12][2] == True and piHorizontalSuperior == True:
            if error != '':
                error += ', '
            error += 'partición interior horizontal en contacto con espacio no habitable superior'
        if elemento[2][12][3] == True and piHorizontalInferior == True:
            if error != '':
                error += ', '
            error += 'partición interior horizontal en contacto con espacio no habitable inferior'
        if error != '':
            return error
        if elemento[2][0] == True and elemento[2][10] == True:
            p1 = False
            p2 = False
            p3 = False
            p4 = False
            p5 = False
            p6 = False
            p7 = False
            p8 = False
            p9 = False
            p10 = False
            for i in self.conjuntoMedidasEnvolvente:
                if i[0] != elemento[0]:
                    if i[1] == 'Mejora de Puentes Térmicos':
                        if i[2][0] == True:
                            p1 = True
                        if i[2][2] == True:
                            p2 = True
                        if i[2][4] == True:
                            p3 = True
                        if i[2][6] == True:
                            p4 = True
                        if i[2][8] == True:
                            p5 = True
                        if i[2][10] == True:
                            p6 = True
                        if i[2][12] == True:
                            p7 = True
                        if i[2][14] == True:
                            p8 = True
                        if i[2][16] == True:
                            p9 = True
                        if i[2][18] == True:
                            p10 = True

            listadoPTenMedida = elemento[2][11]
            if listadoPTenMedida[0] != '':
                pilarIntegrado = True
            else:
                pilarIntegrado = False
            if listadoPTenMedida[1] != '':
                pilarEsquina = True
            else:
                pilarEsquina = False
            if listadoPTenMedida[2] != '':
                contornoHueco = True
            else:
                contornoHueco = False
            if listadoPTenMedida[3] != '':
                cajaPersiana = True
            else:
                cajaPersiana = False
            if listadoPTenMedida[4] != '':
                fachadaForjado = True
            else:
                fachadaForjado = False
            if listadoPTenMedida[5] != '':
                fachadaCubierta = True
            else:
                fachadaCubierta = False
            if listadoPTenMedida[6] != '':
                fachadaSueloAire = True
            else:
                fachadaSueloAire = False
            if p1 == True and pilarIntegrado == True:
                error += 'puente térmico de pilar integrado en fachada'
            if p2 == True and pilarEsquina == True:
                if error != '':
                    error += ', '
                error += 'puente térmico de pilar en esquina'
            if p3 == True and contornoHueco == True:
                if error != '':
                    error += ', '
                error += 'puente térmico de contorno de hueco'
            if p4 == True and cajaPersiana == True:
                if error != '':
                    error += ', '
                error += 'puente térmico de caja de persiana'
            if p5 == True and fachadaForjado == True:
                if error != '':
                    error += ', '
                error += 'puente térmico de encuentro de fachada con forjado'
            if p7 == True and fachadaCubierta == True:
                if error != '':
                    error += ', '
                error += 'puente térmico de encuentro de fachada con cubierta'
            if p8 == True and fachadaSueloAire == True:
                if error != '':
                    error += ', '
                error += 'puente térmico de encuentro de fachada con suelo en contacto con el aire'
            if error != '':
                return error
        return True

    def comprobarHuecos(self, elemento):
        """
        Metodo: comprobarHuecos

        ARGUMENTOS:
                elemento:
        """
        if elemento[2][0][0] == False and elemento[2][0][1] == False and elemento[2][0][2] == False and elemento[2][0][3] == False and elemento[2][0][4] == False and elemento[2][0][5] == False and elemento[2][0][6] == False and elemento[2][0][7] == False and elemento[2][0][8] == False:
            return False
        norte = False
        norOeste = False
        norEste = False
        sur = False
        surOeste = False
        surEste = False
        lucernario = False
        oeste = False
        este = False
        for i in self.conjuntoMedidasEnvolvente:
            if i[0] != elemento[0]:
                if i[1] == 'Sustitución/mejora de Huecos':
                    if i[2][0][0] == True:
                        norte = True
                    if i[2][0][1] == True:
                        norOeste = True
                    if i[2][0][2] == True:
                        norEste = True
                    if i[2][0][3] == True:
                        sur = True
                    if i[2][0][4] == True:
                        surOeste = True
                    if i[2][0][5] == True:
                        surEste = True
                    if i[2][0][6] == True:
                        lucernario = True
                    if i[2][0][7] == True:
                        oeste = True
                    if i[2][0][8] == True:
                        este = True

        error = ''
        if elemento[2][0][0] == True and norte == True:
            error += 'huecos a norte'
        if elemento[2][0][1] == True and norOeste == True:
            if error != '':
                error += ', '
            error += 'huecos a NO'
        if elemento[2][0][2] == True and norEste == True:
            if error != '':
                error += ', '
            error += 'huecos a NE'
        if elemento[2][0][3] == True and sur == True:
            if error != '':
                error += ', '
            error += 'huecos a sur'
        if elemento[2][0][4] == True and surOeste == True:
            if error != '':
                error += ', '
            error += 'huecos a SO'
        if elemento[2][0][5] == True and surEste == True:
            if error != '':
                error += ', '
            error += 'huecos a SE'
        if elemento[2][0][6] == True and lucernario == True:
            if error != '':
                error += ', '
            error += 'lucernarios'
        if elemento[2][0][7] == True and oeste == True:
            if error != '':
                error += ', '
            error += 'huecos a oeste'
        if elemento[2][0][8] == True and este == True:
            if error != '':
                error += ', '
            error += 'huecos a este'
        if error != '':
            return error
        return True

    def comprobarPT(self, elemento):
        """
        Metodo: comprobarPT

        ARGUMENTOS:
                elemento:
        """
        p1 = False
        p2 = False
        p3 = False
        p4 = False
        p5 = False
        p6 = False
        p7 = False
        p8 = False
        p9 = False
        p10 = False
        for i in self.conjuntoMedidasEnvolvente:
            if i[0] != elemento[0]:
                if i[1] == 'Mejora de Puentes Térmicos':
                    if i[2][0] == True:
                        p1 = True
                    if i[2][2] == True:
                        p2 = True
                    if i[2][4] == True:
                        p3 = True
                    if i[2][6] == True:
                        p4 = True
                    if i[2][8] == True:
                        p5 = True
                    if i[2][10] == True:
                        p6 = True
                    if i[2][12] == True:
                        p7 = True
                    if i[2][14] == True:
                        p8 = True
                    if i[2][16] == True:
                        p9 = True
                    if i[2][18] == True:
                        p10 = True

        error = ''
        if elemento[2][0] == True and p1 == True:
            error += 'puente térmico de pilar integrado en fachada'
        if elemento[2][2] == True and p2 == True:
            if error != '':
                error += ', '
            error += 'puente térmico de pilar en esquina'
        if elemento[2][4] == True and p3 == True:
            if error != '':
                error += ', '
            error += 'puente térmico de contorno de hueco'
        if elemento[2][6] == True and p4 == True:
            if error != '':
                error += ', '
            error += 'puente térmico de caja de persiana'
        if elemento[2][8] == True and p5 == True:
            if error != '':
                error += ', '
            error += 'puente térmico de encuentro de fachada con forjado'
        if elemento[2][10] == True and p6 == True:
            if error != '':
                error += ', '
            error += 'puente térmico de encuentro de fachada con voladizo'
        if elemento[2][12] == True and p7 == True:
            if error != '':
                error += ', '
            error += 'puente térmico de encuentro de fachada con cubierta'
        if elemento[2][14] == True and p8 == True:
            if error != '':
                error += ', '
            error += 'puente térmico de encuentro de fachada con suelo en contacto con el aire'
        if elemento[2][16] == True and p9 == True:
            if error != '':
                error += ', '
            error += 'puente térmico de encuentro de fachada con solera'
        if error != '':
            return error
        pilarIntegrado = False
        pilarEsquina = False
        contornoHueco = False
        cajaPersiana = False
        fachadaForjado = False
        fachadaCubierta = False
        fachadaSueloAire = False
        for i in self.conjuntoMedidasEnvolvente:
            if i[0] != elemento[0]:
                if i[1] == 'Adición de Aislamiento Térmico' and i[2][0] == True and i[2][10] == True:
                    listadoPTModificados = i[2][11]
                    if listadoPTModificados[0] != '':
                        pilarIntegrado = True
                    else:
                        pilarIntegrado = False
                    if listadoPTModificados[1] != '':
                        pilarEsquina = True
                    else:
                        pilarEsquina = False
                    if listadoPTModificados[2] != '':
                        contornoHueco = True
                    else:
                        contornoHueco = False
                    if listadoPTModificados[3] != '':
                        cajaPersiana = True
                    else:
                        cajaPersiana = False
                    if listadoPTModificados[4] != '':
                        fachadaForjado = True
                    else:
                        fachadaForjado = False
                    if listadoPTModificados[5] != '':
                        fachadaCubierta = True
                    else:
                        fachadaCubierta = False
                    if listadoPTModificados[6] != '':
                        fachadaSueloAire = True
                    else:
                        fachadaSueloAire = False

        if elemento[2][0] == True and pilarIntegrado == True:
            error += 'puente térmico de pilar integrado en fachada'
        if elemento[2][2] == True and pilarEsquina == True:
            if error != '':
                error += ', '
            error += 'puente térmico de pilar en esquina'
        if elemento[2][4] == True and contornoHueco == True:
            if error != '':
                error += ', '
            error += 'puente térmico de contorno de hueco'
        if elemento[2][6] == True and cajaPersiana == True:
            if error != '':
                error += ', '
            error += 'puente térmico de caja de persiana'
        if elemento[2][8] == True and fachadaForjado == True:
            if error != '':
                error += ', '
            error += 'puente térmico de encuentro de fachada con forjado'
        if elemento[2][12] == True and fachadaCubierta == True:
            if error != '':
                error += ', '
            error += 'puente térmico de encuentro de fachada con cubierta'
        if elemento[2][14] == True and fachadaSueloAire == True:
            if error != '':
                error += ', '
            error += 'puente térmico de encuentro de fachada con suelo en contacto con el aire'
        if error != '':
            return error
        return True

    def recargarLista(self):
        """
        Metodo: recargarLista

        """
        self.TablaMedidasMejora.DeleteAllItems()
        if self.conjuntoMedidasInstalaciones == True:
            self.TablaMedidasMejora.Append(['Nueva definición de las instalaciones', 'Instalaciones'])
        if type(self.conjuntoMedidasEnvolvente) == type('edificio completo'):
            ruta = self.conjuntoMedidasEnvolvente.split('/')
            filename = ruta[-1]
            self.TablaMedidasMejora.Append(['Nuevo Edificio Definido por el Usuario', 'Desde Fichero: ' + filename])
        else:
            for i in self.conjuntoMedidasEnvolvente:
                if i[1] == 'ACS':
                    var = 'Equipo de ACS'
                elif i[1] == 'calefaccion':
                    var = 'Equipo de sólo calefacción'
                elif i[1] == 'refrigeracion':
                    var = 'Equipo de sólo refrigeración'
                elif i[1] == 'climatizacion':
                    var = 'Equipo de calefacción y refrigeración'
                elif i[1] == 'mixto2':
                    var = 'Equipo mixto de calefacción y ACS'
                elif i[1] == 'mixto3':
                    var = 'Equipo mixto de calefacción,  refrigeración y ACS'
                elif i[1] == 'iluminacion':
                    var = 'Equipo de iluminación'
                elif i[1] == 'ventilacion':
                    var = 'Equipo de aire primario'
                else:
                    var = i[1]
                self.TablaMedidasMejora.Append([i[0], var])

    def compruebaNombres(self, nombre, tipoMedida):
        """
        Metodo: compruebaNombres

        ARGUMENTOS:
                nombre:
                tipoMedida:
        """
        if nombre == 'Nueva definición de las instalaciones':
            return 'nombre de instalaciones no posible'
        for i in range(len(self.conjuntoMedidasEnvolvente)):
            if nombre == self.conjuntoMedidasEnvolvente[i][0]:
                return self.conjuntoMedidasEnvolvente[i][0]

        return 'elemento no encontrado'

    def Pinchar_TablaMedidasMejora(self, event):
        """
        Metodo: Pinchar_TablaMedidasMejora

        ARGUMENTOS:
                event:
        """
        event.Skip()

    def OnAnadirButton(self, event):
        """
        Metodo: OnAnadirButton

        ARGUMENTOS:
                event:
        """
        elemento = None
        dlg = anadirMedida.create(self, self.parent.parent)
        dlg.ShowModal()
        if dlg.dev != False:
            if dlg.dev[1] == 'defecto':
                for i in self.parent.parent.parent.listadoConjuntosMMPorDefecto:
                    for j in i.mejoras:
                        try:
                            if dlg.dev[0] == j[0][0]:
                                elemento = copy.deepcopy(i)
                                break
                        except:
                            logging.info('Excepcion en: %s' % __name__)
                            break

                    if i.mejoras[1][2] == True:
                        if i.mejoras[1][0] == dlg.dev[0]:
                            elemento = copy.deepcopy(i)
                    if elemento != None:
                        break

        if elemento != None:
            if elemento.mejoras[0] != []:
                if self.compruebaNombres(elemento.mejoras[0][0][0], elemento.mejoras[0][0][1]) == 'elemento no encontrado':
                    i = elemento.mejoras[0][0]
                    if i[1] == 'Adición de Aislamiento Térmico':
                        if self.comprobarAislamiento(i) == True:
                            self.conjuntoMedidasEnvolvente.append(i)
                        else:
                            if self.comprobarAislamiento(i) == False:
                                wx.MessageBox(_('Debe indicar dónde colocar el aislamiento.'), _('Aviso'))
                                return
                            else:
                                wx.MessageBox(_('Imposible duplicar aislamiento en ') + self.comprobarAislamiento(i) + _('.'), _('Aviso'))
                                return

                    else:
                        if i[1] == 'Sustitución/mejora de Huecos':
                            if self.comprobarHuecos(i) == True:
                                self.conjuntoMedidasEnvolvente.append(i)
                            else:
                                wx.MessageBox(_('Ya ha definido una mejora para ') + self.comprobarHuecos(i) + _(' en este grupo.'), _('Aviso'))
                                return
                        elif i[1] == 'Mejora de Puentes Térmicos':
                            if self.comprobarPT(i) == True:
                                self.conjuntoMedidasEnvolvente.append(i)
                            else:
                                wx.MessageBox(_('Ya ha definido una mejora para "') + self.comprobarPT(i) + _('" en este grupo.'), _('Aviso'))
                                return
                else:
                    if self.compruebaNombres(elemento.mejoras[0][0][0], elemento.mejoras[0][0][1]) == 'nombre de instalaciones no posible':
                        wx.MessageBox(_('El nombre de la medida de mejora seleccionado es incorrecto.'), _('Aviso'))
                        return
                    else:
                        wx.MessageBox(_('La medida de mejora seleccionada ya existe.'), _('Aviso'))
                        return

            elif elemento.mejoras[1][2] == True:
                if self.conjuntoMedidasInstalaciones == True:
                    wx.MessageBox(_('Ya ha definido una mejora de instalaciones  en este grupo.'), _('Aviso'))
                else:
                    self.conjuntoMedidasInstalaciones = True
                    self.sistemasACSMM = elemento.mejoras[1][1][0]
                    self.sistemasCalefaccionMM = elemento.mejoras[1][1][1]
                    self.sistemasRefrigeracionMM = elemento.mejoras[1][1][2]
                    self.sistemasClimatizacionMM = elemento.mejoras[1][1][3]
                    self.sistemasMixto2MM = elemento.mejoras[1][1][4]
                    self.sistemasMixto3MM = elemento.mejoras[1][1][5]
                    self.sistemasContribucionesMM = elemento.mejoras[1][1][6]
                    self.sistemasIluminacionMM = elemento.mejoras[1][1][7]
                    self.sistemasVentilacionMM = elemento.mejoras[1][1][8]
                    self.sistemasVentiladoresMM = elemento.mejoras[1][1][9]
                    self.sistemasBombasMM = elemento.mejoras[1][1][10]
                    self.sistemasTorresRefrigeracionMM = elemento.mejoras[1][1][11]
        if dlg.dev != False:
            if dlg.dev[1] == 'usuario':
                i = dlg.dev[0]
                if i[1] in ('Adición de Aislamiento Térmico', 'Sustitución/mejora de Huecos',
                            'Mejora de Puentes Térmicos'):
                    if self.compruebaNombres(dlg.dev[0][0], dlg.dev[0][1]) == 'elemento no encontrado':
                        if i[1] == 'Adición de Aislamiento Térmico':
                            if self.comprobarAislamiento(i) == True:
                                self.conjuntoMedidasEnvolvente.append(i)
                            else:
                                if self.comprobarAislamiento(i) == False:
                                    wx.MessageBox(_('Debe indicar dónde colocar el aislamiento.'), _('Aviso'))
                                    return
                                else:
                                    wx.MessageBox(_('Imposible duplicar aislamiento en ') + self.comprobarAislamiento(i) + _('.'), _('Aviso'))
                                    return

                        else:
                            if i[1] == 'Sustitución/mejora de Huecos':
                                if self.comprobarHuecos(i) == True:
                                    self.conjuntoMedidasEnvolvente.append(i)
                                else:
                                    wx.MessageBox(_('Ya ha definido una mejora para ') + self.comprobarHuecos(i) + _(' en este grupo.'), _('Aviso'))
                                    return
                            elif i[1] == 'Mejora de Puentes Térmicos':
                                if self.comprobarPT(i) == True:
                                    self.conjuntoMedidasEnvolvente.append(i)
                                else:
                                    wx.MessageBox(_('Ya ha definido una mejora para "') + self.comprobarPT(i) + _('" en este grupo.'), _('Aviso'))
                    else:
                        if self.compruebaNombres(dlg.dev[0][0], dlg.dev[0][1]) == 'nombre de instalaciones no posible':
                            wx.MessageBox(_('El nombre de la medida de mejora seleccionado es incorrecto.'), _('Aviso'))
                            return
                        else:
                            wx.MessageBox(_('El nombre elegido ya existe.'), _('Aviso'))
                            return

                elif self.conjuntoMedidasInstalaciones == True:
                    wx.MessageBox(_('Ya ha definido una mejora de instalaciones  en este grupo.'), _('Aviso'))
                else:
                    self.conjuntoMedidasInstalaciones = True
                    self.sistemasACSMM = i[0]
                    self.sistemasCalefaccionMM = i[1]
                    self.sistemasRefrigeracionMM = i[2]
                    self.sistemasClimatizacionMM = i[3]
                    self.sistemasMixto2MM = i[4]
                    self.sistemasMixto3MM = i[5]
                    self.sistemasContribucionesMM = i[6]
                    self.sistemasIluminacionMM = i[7]
                    self.sistemasVentilacionMM = i[8]
                    self.sistemasVentiladoresMM = i[9]
                    self.sistemasBombasMM = i[10]
                    self.sistemasTorresRefrigeracionMM = i[11]
        self.recargarLista()
        self.recargarComparativaMedidas(flagMensajeAvisoEnergiaElectricaGenerada=True)
        return

    def OnModificarButton(self, event):
        """
        Metodo: OnModificarButton

        ARGUMENTOS:
                event:
        """
        seleccionado = self.TablaMedidasMejora.GetFocusedItem()
        if seleccionado == -1:
            wx.MessageBox(_('Seleccione una medida de la lista'), _('Aviso'))
            return
        texto = self.TablaMedidasMejora.GetItemText(seleccionado)
        if texto != 'Nueva definición de las instalaciones':
            for i in range(len(self.conjuntoMedidasEnvolvente)):
                if texto == self.conjuntoMedidasEnvolvente[i][0]:
                    if self.conjuntoMedidasEnvolvente[i][1] == 'Adición de Aislamiento Térmico':
                        dlg = ventanaAislamiento.create(self)
                        dlg.cargarDatos(self.conjuntoMedidasEnvolvente[i])
                        dlg.ShowModal()
                        if dlg.dev != False:
                            if self.compruebaNombres(dlg.dev[0], texto) == 'elemento no encontrado' or self.compruebaNombres(dlg.dev[0], texto) == texto:
                                medidaModificada = dlg.dev
                                medidaModificadaNombreAnterior = copy.deepcopy(medidaModificada)
                                medidaModificadaNombreAnterior[0] = texto
                                if self.comprobarAislamiento(medidaModificadaNombreAnterior) == True:
                                    self.conjuntoMedidasEnvolvente[i] = dlg.dev
                                else:
                                    if self.comprobarAislamiento(medidaModificadaNombreAnterior) == False:
                                        wx.MessageBox(_('Debe indicar dónde colocar el aislamiento.'), _('Aviso'))
                                        return
                                    else:
                                        wx.MessageBox(_('Imposible duplicar aislamiento en ') + self.comprobarAislamiento(medidaModificadaNombreAnterior) + _('.'), _('Aviso'))
                                        return

                            else:
                                if self.compruebaNombres(dlg.dev[0], texto) == 'nombre de instalaciones no posible':
                                    wx.MessageBox(_('El nombre de la medida de mejora seleccionado es incorrecto.'), _('Aviso'))
                                    return
                                else:
                                    wx.MessageBox(_('El nombre elegido ya existe.'), _('Aviso'))
                                    return

                    else:
                        if self.conjuntoMedidasEnvolvente[i][1] == 'Sustitución/mejora de Huecos':
                            dlg = ventanaHuecos.create(self, self.parent.parent.parent.panelEnvolvente.ventanas)
                            dlg.cargarDatos(self.conjuntoMedidasEnvolvente[i])
                            dlg.ShowModal()
                            if dlg.dev != False:
                                if self.compruebaNombres(dlg.dev[0], texto) == 'elemento no encontrado' or self.compruebaNombres(dlg.dev[0], texto) == texto:
                                    medidaModificada = dlg.dev
                                    medidaModificadaNombreAnterior = copy.deepcopy(medidaModificada)
                                    medidaModificadaNombreAnterior[0] = texto
                                    if self.comprobarHuecos(medidaModificadaNombreAnterior) == True:
                                        self.conjuntoMedidasEnvolvente[i] = dlg.dev
                                    else:
                                        wx.MessageBox(_('Ya ha definido una mejora para ') + self.comprobarHuecos(medidaModificadaNombreAnterior) + _(' en este grupo.'), _('Aviso'))
                                        return
                                else:
                                    if self.compruebaNombres(dlg.dev[0], texto) == 'nombre de instalaciones no posible':
                                        wx.MessageBox(_('El nombre de la medida de mejora seleccionado es incorrecto.'), _('Aviso'))
                                        return
                                    else:
                                        wx.MessageBox(_('El nombre elegido ya existe.'), _('Aviso'))
                                        return

                        elif self.conjuntoMedidasEnvolvente[i][1] == 'Mejora de Puentes Térmicos':
                            dlg = ventanaPT.create(self)
                            dlg.cargarDatos(self.conjuntoMedidasEnvolvente[i])
                            dlg.ShowModal()
                            if dlg.dev != False:
                                if self.compruebaNombres(dlg.dev[0], texto) == 'elemento no encontrado' or self.compruebaNombres(dlg.dev[0], texto) == texto:
                                    medidaModificada = dlg.dev
                                    medidaModificadaNombreAnterior = copy.deepcopy(medidaModificada)
                                    medidaModificadaNombreAnterior[0] = texto
                                    if self.comprobarPT(medidaModificadaNombreAnterior) == True:
                                        self.conjuntoMedidasEnvolvente[i] = dlg.dev
                                    else:
                                        wx.MessageBox(_('Ya ha definido una mejora para "') + self.comprobarPT(medidaModificadaNombreAnterior) + _('" en este grupo.'), _('Aviso'))
                                else:
                                    if self.compruebaNombres(dlg.dev[0], texto) == 'nombre de instalaciones no posible':
                                        wx.MessageBox(_('El nombre de la medida de mejora seleccionado es incorrecto.'), _('Aviso'))
                                        return
                                    else:
                                        wx.MessageBox(_('El nombre elegido ya existe.'), _('Aviso'))
                                        return

        elif texto == 'Nueva definición de las instalaciones':
            listadoInstalaciones = [self.sistemasACSMM, self.sistemasCalefaccionMM, self.sistemasRefrigeracionMM,
             self.sistemasClimatizacionMM, self.sistemasMixto2MM, self.sistemasMixto3MM,
             self.sistemasContribucionesMM, self.sistemasIluminacionMM,
             self.sistemasVentilacionMM, self.sistemasVentiladoresMM,
             self.sistemasBombasMM, self.sistemasTorresRefrigeracionMM]
            dlg = definicionInstalaciones.create(self, listadoInstalaciones)
            dlg.ShowModal()
            if dlg.dev != False:
                self.conjuntoMedidasInstalaciones = True
                self.sistemasACSMM = dlg.dev[0]
                self.sistemasCalefaccionMM = dlg.dev[1]
                self.sistemasRefrigeracionMM = dlg.dev[2]
                self.sistemasClimatizacionMM = dlg.dev[3]
                self.sistemasMixto2MM = dlg.dev[4]
                self.sistemasMixto3MM = dlg.dev[5]
                self.sistemasContribucionesMM = dlg.dev[6]
                self.sistemasIluminacionMM = dlg.dev[7]
                self.sistemasVentilacionMM = dlg.dev[8]
                self.sistemasVentiladoresMM = dlg.dev[9]
                self.sistemasBombasMM = dlg.dev[10]
                self.sistemasTorresRefrigeracionMM = dlg.dev[11]
        self.recargarLista()
        self.recargarComparativaMedidas(flagMensajeAvisoEnergiaElectricaGenerada=True)

    def OnBorrarButton(self, event):
        """
        Metodo: OnBorrarButton

        ARGUMENTOS:
                event:
        """
        try:
            seleccionado = self.TablaMedidasMejora.GetFocusedItem()
            texto = self.TablaMedidasMejora.GetItemText(seleccionado)
            for i in range(len(self.conjuntoMedidasEnvolvente)):
                if self.conjuntoMedidasEnvolvente[i][0] == texto:
                    del self.conjuntoMedidasEnvolvente[i]
                    break

            if self.conjuntoMedidasInstalaciones == True and texto == 'Nueva definición de las instalaciones':
                self.conjuntoMedidasInstalaciones = False
                self.sistemasACSMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasACS)
                self.sistemasCalefaccionMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasCalefaccion)
                self.sistemasRefrigeracionMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasRefrigeracion)
                self.sistemasClimatizacionMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasClimatizacion)
                self.sistemasMixto2MM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasMixto2)
                self.sistemasMixto3MM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasMixto3)
                self.sistemasContribucionesMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasContribuciones)
                if self.parent.parent.parent.objEdificio.programa != 'Residencial':
                    self.sistemasIluminacionMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasIluminacion)
                    self.sistemasVentilacionMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasVentilacion)
                    self.sistemasVentiladoresMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasVentiladores)
                    self.sistemasBombasMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasBombas)
                    self.sistemasTorresRefrigeracionMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasTorresRefrigeracion)
            self.recargarComparativaMedidas(flagMensajeAvisoEnergiaElectricaGenerada=True)
            self.TablaMedidasMejora.DeleteItem(seleccionado)
        except:
            self.recargarComparativaMedidas(flagMensajeAvisoEnergiaElectricaGenerada=True)
            self.TablaMedidasMejora.DeleteItem(seleccionado)

    def recargarComparativaMedidas(self, flagMensaje=True, flagMensajeAvisoEnergiaElectricaGenerada=False):
        """
        Metodo: recargarComparativaMedidas
        Atributos: 
        flagMensaje: si se quiere que se saque el mns de error en caso de que no se haya podido calcular el conjunto de mm
        flagMensajeAvisoEnergiaElectricaGenerada: si quieres que saque el error si la energia electrica generada es mayor que la consumida
        """
        if self.conjuntoMedidasEnvolvente == [] and self.conjuntoMedidasInstalaciones == False:
            self.TablaResultados.Show(False)
            self.ResultadosMedidasText.Show(False)
            self.Etiqueta.Show(False)
            self.NotaA.Show(False)
            self.EmisA.Show(False)
            self.NotaB.Show(False)
            self.EmisB.Show(False)
            self.NotaC.Show(False)
            self.EmisC.Show(False)
            self.NotaD.Show(False)
            self.EmisD.Show(False)
            self.NotaE.Show(False)
            self.EmisE.Show(False)
            self.NotaF.Show(False)
            self.EmisF.Show(False)
            self.NotaG.Show(False)
            self.EmisG.Show(False)
        else:
            if type(self.conjuntoMedidasEnvolvente) == type('edificio completo'):
                self.conjuntoMM.datosEdificioOriginal = self.parent.parent.parent.objEdificio
                self.conjuntoMM.calificacion()
                if self.conjuntoMM.datosNuevoEdificio.casoValido == False and flagMensaje == True:
                    wx.MessageBox(_('Revise el conjunto de medidas de mejora. \n%s' % self.conjuntoMM.datosNuevoEdificio.mensajeAviso), _('Aviso'))
            else:
                listadoInstalaciones = [
                 self.sistemasACSMM, self.sistemasCalefaccionMM, self.sistemasRefrigeracionMM,
                 self.sistemasClimatizacionMM, self.sistemasMixto2MM, self.sistemasMixto3MM,
                 self.sistemasContribucionesMM, self.sistemasIluminacionMM,
                 self.sistemasVentilacionMM, self.sistemasVentiladoresMM,
                 self.sistemasBombasMM, self.sistemasTorresRefrigeracionMM]
                self.listadoMedidas = [
                 self.conjuntoMedidasEnvolvente,
                 [
                  '', listadoInstalaciones, self.conjuntoMedidasInstalaciones]]
                self.conjuntoMM.mejoras = self.listadoMedidas
                self.conjuntoMM.datosEdificioOriginal = self.parent.parent.parent.objEdificio
                self.conjuntoMM.calificacion()
                if self.conjuntoMM.datosNuevoEdificio.casoValido == False and flagMensaje == True:
                    wx.MessageBox(_('Revise el conjunto de medidas de mejora. \n%s' % self.conjuntoMM.datosNuevoEdificio.mensajeAviso), _('Aviso'))
                elif self.conjuntoMM.datosNuevoEdificio.casoValido == True and self.conjuntoMM.datosNuevoEdificio.mensajeAviso != '' and flagMensajeAvisoEnergiaElectricaGenerada == True:
                    wx.MessageBox(self.conjuntoMM.datosNuevoEdificio.mensajeAviso, _('Aviso'))
                if self.conjuntoMM.datosNuevoEdificio.casoValido == False:
                    self.TablaResultados.DeleteAllItems()
                    self.TablaResultados.Show(False)
                    self.ResultadosMedidasText.Show(False)
                    self.Etiqueta.Show(False)
                    self.NotaA.Show(False)
                    self.EmisA.Show(False)
                    self.NotaB.Show(False)
                    self.EmisB.Show(False)
                    self.NotaC.Show(False)
                    self.EmisC.Show(False)
                    self.NotaD.Show(False)
                    self.EmisD.Show(False)
                    self.NotaE.Show(False)
                    self.EmisE.Show(False)
                    self.NotaF.Show(False)
                    self.EmisF.Show(False)
                    self.NotaG.Show(False)
                    self.EmisG.Show(False)
                    return
            self.TablaResultados.DeleteAllItems()
            self.TablaResultados.Append([_('Demanda de calefacción'),
             str(round(self.conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaCal, 1)) + ' ' + self.conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaCal_nota,
             str(round(self.parent.parent.parent.objEdificio.datosResultados.ddaBrutaCal, 1)) + ' ' + self.parent.parent.parent.objEdificio.datosResultados.ddaBrutaCal_nota,
             str(self.conjuntoMM.ahorro[0]) + ' %'])
            if self.parent.parent.parent.objEdificio.datosIniciales.zonaHE1 in ('alpha1',
                                                                                'A1',
                                                                                'B1',
                                                                                'C1',
                                                                                'D1',
                                                                                'E1') and self.parent.parent.parent.objEdificio == 'Residencial':
                self.TablaResultados.Append([_('Demanda de refrigeración'),
                 _('No calificable'),
                 _('No calificable'), '-'])
            else:
                self.TablaResultados.Append([_('Demanda de refrigeración'),
                 str(round(self.conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaRef, 1)) + ' ' + self.conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaRef_nota,
                 str(round(self.parent.parent.parent.objEdificio.datosResultados.ddaBrutaRef, 1)) + ' ' + self.parent.parent.parent.objEdificio.datosResultados.ddaBrutaRef_nota,
                 str(self.conjuntoMM.ahorro[1]) + ' %'])
            self.TablaResultados.Append([_('Emisiones de calefacción'),
             str(round(self.conjuntoMM.datosNuevoEdificio.datosResultados.emisionesCal, 1)) + ' ' + self.conjuntoMM.datosNuevoEdificio.datosResultados.emisionesCal_nota,
             str(round(self.parent.parent.parent.objEdificio.datosResultados.emisionesCal, 1)) + ' ' + self.parent.parent.parent.objEdificio.datosResultados.emisionesCal_nota,
             str(self.conjuntoMM.ahorro[2]) + ' %'])
            if self.parent.parent.parent.objEdificio.datosIniciales.zonaHE1 in ('alpha1',
                                                                                'A1',
                                                                                'B1',
                                                                                'C1',
                                                                                'D1',
                                                                                'E1') and self.parent.parent.parent.objEdificio == 'Residencial':
                self.TablaResultados.Append([_('Emisiones de refrigeración'),
                 _('No calificable'),
                 _('No calificable'),
                 '-'])
            else:
                self.TablaResultados.Append([_('Emisiones de refrigeración'),
                 str(round(self.conjuntoMM.datosNuevoEdificio.datosResultados.emisionesRef, 1)) + ' ' + self.conjuntoMM.datosNuevoEdificio.datosResultados.emisionesRef_nota,
                 str(round(self.parent.parent.parent.objEdificio.datosResultados.emisionesRef, 1)) + ' ' + self.parent.parent.parent.objEdificio.datosResultados.emisionesRef_nota,
                 str(self.conjuntoMM.ahorro[3]) + ' %'])
            self.TablaResultados.Append([_('Emisiones de ACS'),
             str(round(self.conjuntoMM.datosNuevoEdificio.datosResultados.emisionesACS, 1)) + ' ' + self.conjuntoMM.datosNuevoEdificio.datosResultados.emisionesACS_nota,
             str(round(self.parent.parent.parent.objEdificio.datosResultados.emisionesACS, 1)) + ' ' + self.parent.parent.parent.objEdificio.datosResultados.emisionesACS_nota,
             str(self.conjuntoMM.ahorro[4]) + ' %'])
            if self.parent.parent.parent.objEdificio.programa != 'Residencial':
                self.TablaResultados.Append([_('Emisiones de iluminación'),
                 str(round(self.conjuntoMM.datosNuevoEdificio.datosResultados.emisionesIlum, 1)) + ' ' + self.conjuntoMM.datosNuevoEdificio.datosResultados.emisionesIlum_nota,
                 str(round(self.parent.parent.parent.objEdificio.datosResultados.emisionesIlum, 1)) + ' ' + self.parent.parent.parent.objEdificio.datosResultados.emisionesIlum_nota,
                 str(self.conjuntoMM.ahorro[5]) + ' %'])
            self.TablaResultados.Append([_('EMISIONES GLOBALES'),
             str(round(self.conjuntoMM.datosNuevoEdificio.datosResultados.emisionesMostrar, 1)) + ' ' + self.conjuntoMM.datosNuevoEdificio.datosResultados.emisiones_nota,
             str(round(self.parent.parent.parent.objEdificio.datosResultados.emisionesMostrar, 1)) + ' ' + self.parent.parent.parent.objEdificio.datosResultados.emisiones_nota,
             str(self.conjuntoMM.ahorro[-1]) + ' %'])
            self.TablaResultados.Show(True)
            self.ResultadosMedidasText.Show(True)
            self.Etiqueta.Show(True)
            self.NotaA.Show(False)
            self.EmisA.Show(False)
            self.NotaB.Show(False)
            self.EmisB.Show(False)
            self.NotaC.Show(False)
            self.EmisC.Show(False)
            self.NotaD.Show(False)
            self.EmisD.Show(False)
            self.NotaE.Show(False)
            self.EmisE.Show(False)
            self.NotaF.Show(False)
            self.EmisF.Show(False)
            self.NotaG.Show(False)
            self.EmisG.Show(False)
            if self.conjuntoMM.datosNuevoEdificio.datosResultados.emisiones_nota == 'A':
                self.EmisA.SetLabel(str(round(self.conjuntoMM.datosNuevoEdificio.datosResultados.emisionesMostrar, 1)))
                self.NotaA.Show(True)
                self.EmisA.Show(True)
            elif self.conjuntoMM.datosNuevoEdificio.datosResultados.emisiones_nota == 'B':
                self.EmisB.SetLabel(str(round(self.conjuntoMM.datosNuevoEdificio.datosResultados.emisionesMostrar, 1)))
                self.NotaB.Show(True)
                self.EmisB.Show(True)
            elif self.conjuntoMM.datosNuevoEdificio.datosResultados.emisiones_nota == 'C':
                self.EmisC.SetLabel(str(round(self.conjuntoMM.datosNuevoEdificio.datosResultados.emisionesMostrar, 1)))
                self.NotaC.Show(True)
                self.EmisC.Show(True)
            elif self.conjuntoMM.datosNuevoEdificio.datosResultados.emisiones_nota == 'D':
                self.EmisD.SetLabel(str(round(self.conjuntoMM.datosNuevoEdificio.datosResultados.emisionesMostrar, 1)))
                self.NotaD.Show(True)
                self.EmisD.Show(True)
            elif self.conjuntoMM.datosNuevoEdificio.datosResultados.emisiones_nota == 'E':
                self.EmisE.SetLabel(str(round(self.conjuntoMM.datosNuevoEdificio.datosResultados.emisionesMostrar, 1)))
                self.NotaE.Show(True)
                self.EmisE.Show(True)
            elif self.conjuntoMM.datosNuevoEdificio.datosResultados.emisiones_nota == 'F':
                self.EmisF.SetLabel(str(round(self.conjuntoMM.datosNuevoEdificio.datosResultados.emisionesMostrar, 1)))
                self.NotaF.Show(True)
                self.EmisF.Show(True)
            elif self.conjuntoMM.datosNuevoEdificio.datosResultados.emisiones_nota == 'G':
                self.EmisG.SetLabel(str(round(self.conjuntoMM.datosNuevoEdificio.datosResultados.emisionesMostrar, 1)))
                self.NotaG.Show(True)
                self.EmisG.Show(True)

    def __init__(self, parent, id, pos, size, style, name, conjuntoMM=None):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
                id:
                pos:
                size:
                style:
                name:
                medidas=None:
        """
        self.parent = parent
        if conjuntoMM == None:
            conjuntoMMcargado = grupoMedidasMejora(nombre='', datosEdificioOriginal=self.parent.parent.parent.objEdificio)
        else:
            conjuntoMMcargado = copy.deepcopy(conjuntoMM)
        self.conjuntoMM = conjuntoMMcargado
        medidas = self.conjuntoMM.mejoras
        self._init_ctrls(parent, id, pos, wx.Size(0, 0), style, name)
        if medidas == []:
            self.conjuntoMedidasEnvolvente = []
            self.conjuntoMedidasInstalaciones = False
            self.sistemasACSMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasACS)
            self.sistemasCalefaccionMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasCalefaccion)
            self.sistemasRefrigeracionMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasRefrigeracion)
            self.sistemasClimatizacionMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasClimatizacion)
            self.sistemasMixto2MM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasMixto2)
            self.sistemasMixto3MM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasMixto3)
            self.sistemasContribucionesMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasContribuciones)
            if self.parent.parent.parent.objEdificio.programa != 'Residencial':
                self.sistemasIluminacionMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasIluminacion)
                self.sistemasVentilacionMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasVentilacion)
                self.sistemasVentiladoresMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasVentiladores)
                self.sistemasBombasMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasBombas)
                self.sistemasTorresRefrigeracionMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasTorresRefrigeracion)
            else:
                self.sistemasIluminacionMM = []
                self.sistemasVentilacionMM = []
                self.sistemasVentiladoresMM = []
                self.sistemasBombasMM = []
                self.sistemasTorresRefrigeracionMM = []
            self.DescripcionCuadro.Enable(True)
            self.Anadir.Enable(True)
            self.Modificar.Enable(True)
            self.Borrar.Enable(True)
            self.parent.panelBotones.guardarBoton.Show(True)
            self.parent.panelBotones.modificarBoton.Show(True)
            self.parent.panelBotones.borrarBoton.Show(True)
        elif type(medidas) == type('edificio completo'):
            self.conjuntoMedidasEnvolvente = medidas
            self.conjuntoMedidasInstalaciones = False
            self.sistemasACSMM = []
            self.sistemasCalefaccionMM = []
            self.sistemasRefrigeracionMM = []
            self.sistemasClimatizacionMM = []
            self.sistemasMixto2MM = []
            self.sistemasMixto3MM = []
            self.sistemasContribucionesMM = []
            self.sistemasIluminacionMM = []
            self.sistemasVentilacionMM = []
            self.sistemasVentiladoresMM = []
            self.sistemasBombasMM = []
            self.sistemasTorresRefrigeracionMM = []
            self.recargarLista()
            self.recargarComparativaMedidas()
            self.DescripcionCuadro.Enable(False)
            self.Anadir.Enable(False)
            self.Modificar.Enable(False)
            self.Borrar.Enable(False)
            self.parent.panelBotones.guardarBoton.Show(False)
            self.parent.panelBotones.modificarBoton.Show(True)
            self.parent.panelBotones.borrarBoton.Show(True)
        else:
            self.conjuntoMedidasEnvolvente = []
            for i in medidas[0]:
                self.conjuntoMedidasEnvolvente.append(copy.deepcopy(i))

            self.conjuntoMedidasInstalaciones = copy.deepcopy(medidas[1][1])
            if medidas[1][2] == False:
                self.conjuntoMedidasInstalaciones = False
                self.sistemasACSMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasACS)
                self.sistemasCalefaccionMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasCalefaccion)
                self.sistemasRefrigeracionMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasRefrigeracion)
                self.sistemasClimatizacionMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasClimatizacion)
                self.sistemasMixto2MM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasMixto2)
                self.sistemasMixto3MM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasMixto3)
                self.sistemasContribucionesMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasContribuciones)
                if self.parent.parent.parent.objEdificio.programa != 'Residencial':
                    self.sistemasIluminacionMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasIluminacion)
                    self.sistemasVentilacionMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasVentilacion)
                    self.sistemasVentiladoresMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasVentiladores)
                    self.sistemasBombasMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasBombas)
                    self.sistemasTorresRefrigeracionMM = copy.deepcopy(self.parent.parent.parent.objEdificio.datosIniciales.sistemasTorresRefrigeracion)
                else:
                    self.sistemasIluminacionMM = []
                    self.sistemasVentilacionMM = []
                    self.sistemasVentiladoresMM = []
                    self.sistemasBombasMM = []
                    self.sistemasTorresRefrigeracionMM = []
            else:
                self.conjuntoMedidasInstalaciones = True
                self.sistemasACSMM = copy.deepcopy(medidas[1][1][0])
                self.sistemasCalefaccionMM = copy.deepcopy(medidas[1][1][1])
                self.sistemasRefrigeracionMM = copy.deepcopy(medidas[1][1][2])
                self.sistemasClimatizacionMM = copy.deepcopy(medidas[1][1][3])
                self.sistemasMixto2MM = copy.deepcopy(medidas[1][1][4])
                self.sistemasMixto3MM = copy.deepcopy(medidas[1][1][5])
                self.sistemasContribucionesMM = copy.deepcopy(medidas[1][1][6])
                self.sistemasIluminacionMM = copy.deepcopy(medidas[1][1][7])
                self.sistemasVentilacionMM = copy.deepcopy(medidas[1][1][8])
                self.sistemasVentiladoresMM = copy.deepcopy(medidas[1][1][9])
                self.sistemasBombasMM = copy.deepcopy(medidas[1][1][10])
                self.sistemasTorresRefrigeracionMM = copy.deepcopy(medidas[1][1][11])
            self.DescripcionCuadro.Enable(True)
            self.Anadir.Enable(True)
            self.Modificar.Enable(True)
            self.Borrar.Enable(True)
            self.parent.panelBotones.guardarBoton.Show(True)
            self.parent.panelBotones.modificarBoton.Show(True)
            self.parent.panelBotones.borrarBoton.Show(True)
            self.recargarLista()
            self.recargarComparativaMedidas()
        listadoInstalaciones = [
         self.sistemasACSMM, self.sistemasCalefaccionMM, self.sistemasRefrigeracionMM,
         self.sistemasClimatizacionMM, self.sistemasMixto2MM, self.sistemasMixto3MM,
         self.sistemasContribucionesMM, self.sistemasIluminacionMM,
         self.sistemasVentilacionMM, self.sistemasVentiladoresMM,
         self.sistemasBombasMM, self.sistemasTorresRefrigeracionMM]
        self.listadoMedidas = [
         self.conjuntoMedidasEnvolvente,
         [
          '', listadoInstalaciones, self.conjuntoMedidasInstalaciones]]
        self.SetSize(size)
        return