# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Informes\chequeoInforme.pyc
# Compiled at: 2015-02-05 13:20:59
"""
Modulo: chequeoInforme.py

"""
import wx, wx.grid, datetime
wxID_PANEL2, wxID_PANEL2CANCELARBOTON, wxID_PANEL2COMENTARIOSCTRL, wxID_PANEL2CONFIGURACIONINFORMETEXT, wxID_PANEL2CONJUNTOSINCLUIRLISTCTRL, wxID_PANEL2DOCUMENTACIONCTRL, wxID_PANEL2GENERARINFORMEBOTON, wxID_PANEL2OPCION1CHOICE, wxID_PANEL2OPCION1TEXT, wxID_PANEL2OPCION2CHOICE, wxID_PANEL2OPCION2TEXT, wxID_PANEL2OPCION3CHOICE, wxID_PANEL2OPCION3TEXT, wxID_DIALOG1, wxID_DIALOG1STATICBOX1, wxID_DIALOG1STATICBOX2, wxID_DIALOG1STATICBOX3, wxID_DIALOG1STATICBOX4, wxID_PANEL2FECHATEXT, wxID_PANEL2FECHAINFORMECTRL_DIA, wxID_PANEL2FECHAINFORMECTRL_MES, wxID_PANEL2FECHAINFORMECTRL_ANNO, wxID_PANEL2BARRAFECHA1TEXT, wxID_PANEL2BARRAFECHA2TEXT, wxID_PANEL2FECHAVISITATEXT, wxID_PANEL2FECHAVISITACTRL_DIA, wxID_PANEL2FECHAVISITACTRL_MES, wxID_PANEL2FECHAVISITACTRL_ANNO, wxID_PANEL2BARRAFECHAVISITA1TEXT, wxID_PANEL2BARRAFECHAVISITA2TEXT = [ wx.NewId() for _init_ctrls in range(30) ]

class Dialog(wx.Dialog):
    """
    Clase: Dialog del modulo chequeoInforme.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(475, 40), size=wx.Size(698, 680), style=wx.DEFAULT_DIALOG_STYLE, title=_('Opciones del Informe'))
        self.SetClientSize(wx.Size(698, 680))
        self.SetBackgroundColour('white')
        self.configuracionInformeText = wx.StaticText(id=wxID_PANEL2CONFIGURACIONINFORMETEXT, label=_('Configuración del informe de certificación energética'), name='configuracionInformeText', parent=self, pos=wx.Point(15, 15), size=wx.Size(437, 18), style=0)
        self.configuracionInformeText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.configuracionInformeText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticBox1 = wx.StaticBox(id=wxID_DIALOG1STATICBOX1, label=_('¿Qué conjuntos desea incluir en el informe?'), name='staticText1', parent=self, pos=wx.Point(15, 45), size=wx.Size(668, 163), style=0)
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticBox1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticBox2 = wx.StaticBox(id=wxID_DIALOG1STATICBOX2, label=_('Pruebas, comprobaciones e inspecciones realizadas por el técnico certificador'), name='staticText1', parent=self, pos=wx.Point(15, 218), size=wx.Size(668, 200), style=0)
        self.staticBox2.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticBox2.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticBox3 = wx.StaticBox(id=wxID_DIALOG1STATICBOX3, label=_('Documentación'), name='staticText1', parent=self, pos=wx.Point(15, 428), size=wx.Size(668, 128), style=0)
        self.staticBox3.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticBox3.SetForegroundColour(wx.Colour(0, 64, 128))
        self.staticBox4 = wx.StaticBox(id=wxID_DIALOG1STATICBOX4, label=_('Configuración del informe'), name='staticText1', parent=self, pos=wx.Point(15, 566), size=wx.Size(668, 61), style=0)
        self.staticBox4.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticBox4.SetForegroundColour(wx.Colour(0, 64, 128))
        self.conjuntosIncluirlistCtrl = wx.ListCtrl(id=wxID_PANEL2CONJUNTOSINCLUIRLISTCTRL, name='conjuntosIncluirlistCtrl', parent=self, pos=wx.Point(30, 70), size=wx.Size(378, 123), style=wx.LC_REPORT)
        self._init_coll_conjuntosIncluirlistCtrl_Columns(self.conjuntosIncluirlistCtrl)
        self.opcion1Text = wx.StaticText(id=wxID_PANEL2OPCION1TEXT, label=_('Opción 1'), name='opcion1Text', parent=self, pos=wx.Point(434, 70), size=wx.Size(48, 13), style=0)
        self.opcion2Text = wx.StaticText(id=wxID_PANEL2OPCION2TEXT, label=_('Opción 2'), name='opcion2Text', parent=self, pos=wx.Point(434, 113), size=wx.Size(48, 13), style=0)
        self.opcion3Text = wx.StaticText(id=wxID_PANEL2OPCION3TEXT, label=_('Opción 3'), name='opcion3Text', parent=self, pos=wx.Point(434, 156), size=wx.Size(48, 13), style=0)
        self.opcion1Choice = wx.Choice(choices=self.listaMedidas, id=wxID_PANEL2OPCION1CHOICE, name='opcion1Choice', parent=self, pos=wx.Point(434, 86), size=wx.Size(234, 21), style=0)
        self.opcion1Choice.Bind(wx.EVT_CHOICE, self.onOpcion1Choice, id=wxID_PANEL2OPCION1CHOICE)
        self.opcion2Choice = wx.Choice(choices=[], id=wxID_PANEL2OPCION2CHOICE, name='opcion2Choice', parent=self, pos=wx.Point(434, 129), size=wx.Size(234, 21), style=0)
        self.opcion2Choice.Bind(wx.EVT_CHOICE, self.onOpcion2Choice, id=wxID_PANEL2OPCION2CHOICE)
        self.opcion3Choice = wx.Choice(choices=[], id=wxID_PANEL2OPCION3CHOICE, name='opcion3Choice', parent=self, pos=wx.Point(434, 172), size=wx.Size(234, 21), style=0)
        self.comentariosCtrl = wx.TextCtrl(id=wxID_PANEL2COMENTARIOSCTRL, name='comentariosCtrl', parent=self, pos=wx.Point(30, 242), size=wx.Size(638, 160), style=wx.TE_MULTILINE, value='')
        self.documentacionCtrl = wx.TextCtrl(id=wxID_PANEL2DOCUMENTACIONCTRL, name='documentacionCtrl', parent=self, pos=wx.Point(30, 452), size=wx.Size(638, 89), style=wx.TE_MULTILINE, value='')
        fecha = datetime.date.today()
        dia = fecha.day
        mes = fecha.month
        anno = fecha.year
        self.fechaText = wx.StaticText(id=wxID_PANEL2FECHATEXT, label=_('Fecha elaboración certificado'), name='fechaText', parent=self, pos=wx.Point(30, 595), size=wx.Size(155, 13), style=0)
        self.fechaInformeCtrl_dia = wx.TextCtrl(id=wxID_PANEL2FECHAINFORMECTRL_DIA, name='fechaInformeCtrl_dia', parent=self, pos=wx.Point(190, 591), size=wx.Size(25, 21), style=0, value=unicode(dia))
        self.fechaInformeCtrl_mes = wx.TextCtrl(id=wxID_PANEL2FECHAINFORMECTRL_MES, name='fechaInformeCtrl_mes', parent=self, pos=wx.Point(228, 591), size=wx.Size(25, 21), style=0, value=unicode(mes))
        self.fechaInformeCtrl_anno = wx.TextCtrl(id=wxID_PANEL2FECHAINFORMECTRL_ANNO, name='fechaInformeCtrl_anno', parent=self, pos=wx.Point(266, 591), size=wx.Size(40, 21), style=0, value=unicode(anno))
        self.barraFecha1Text = wx.StaticText(id=wxID_PANEL2BARRAFECHA1TEXT, label=_('/'), name='fechaText', parent=self, pos=wx.Point(219, 595), size=wx.Size(5, 13), style=0)
        self.barraFecha2Text = wx.StaticText(id=wxID_PANEL2BARRAFECHA2TEXT, label=_('/'), name='fechaText', parent=self, pos=wx.Point(257, 595), size=wx.Size(5, 13), style=0)
        self.fechaVisitaText = wx.StaticText(id=wxID_PANEL2FECHAVISITATEXT, label=_('Fecha visita inmueble'), name='fechaVisitaText', parent=self, pos=wx.Point(420, 595), size=wx.Size(120, 13), style=0)
        self.fechaVisitaCtrl_dia = wx.TextCtrl(id=wxID_PANEL2FECHAVISITACTRL_DIA, name='fechaVisitaCtrl_dia', parent=self, pos=wx.Point(552, 591), size=wx.Size(25, 21), style=0, value=unicode(dia))
        self.fechaVisitaCtrl_mes = wx.TextCtrl(id=wxID_PANEL2FECHAVISITACTRL_MES, name='fechaVisitaCtrl_mes', parent=self, pos=wx.Point(590, 591), size=wx.Size(25, 21), style=0, value=unicode(mes))
        self.fechaVisitaCtrl_anno = wx.TextCtrl(id=wxID_PANEL2FECHAVISITACTRL_ANNO, name='fechaVisitaCtrl_anno', parent=self, pos=wx.Point(628, 591), size=wx.Size(40, 21), style=0, value=unicode(anno))
        self.barraFechaVisita1Text = wx.StaticText(id=wxID_PANEL2BARRAFECHAVISITA1TEXT, label=_('/'), name='barraFechaVisita1Text', parent=self, pos=wx.Point(581, 595), size=wx.Size(5, 13), style=0)
        self.barraFechaVisita2Text = wx.StaticText(id=wxID_PANEL2BARRAFECHAVISITA2TEXT, label=_('/'), name='barraFechaVisita2Text', parent=self, pos=wx.Point(619, 595), size=wx.Size(5, 13), style=0)
        self.generarInformeBoton = wx.Button(id=wxID_PANEL2GENERARINFORMEBOTON, label=_('Generar informes'), name='generarInformeBoton', parent=self, pos=wx.Point(15, 642), size=wx.Size(125, 23), style=0)
        self.generarInformeBoton.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Verdana'))
        self.generarInformeBoton.Bind(wx.EVT_BUTTON, self.OnGenerarInformeBotonButton, id=wxID_PANEL2GENERARINFORMEBOTON)
        self.cancelarBoton = wx.Button(id=wxID_PANEL2CANCELARBOTON, label=_('Cancelar'), name='cancelarBoton', parent=self, pos=wx.Point(155, 642), size=wx.Size(125, 23), style=0)
        self.cancelarBoton.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Verdana'))
        self.cancelarBoton.Bind(wx.EVT_BUTTON, self.OnCancelarBotonButton, id=wxID_PANEL2CANCELARBOTON)
        self.conjuntosIncluirlistCtrl.SetToolTip(wx.ToolTip(_('Conjuntos de medidas de mejora ya incluidos en el informe.')))
        self.opcion1Choice.SetToolTip(wx.ToolTip(_('Seleccione el conjunto de medidas de mejora que aparecerá en posición 1.')))
        self.opcion2Choice.SetToolTip(wx.ToolTip(_('Seleccione el conjunto de medidas de mejora que aparecerá en posición 2.')))
        self.opcion3Choice.SetToolTip(wx.ToolTip(_('Seleccione el conjunto de medidas de mejora que aparecerá en posición 3.')))
        self.comentariosCtrl.SetToolTip(wx.ToolTip(_('Se describen a continuación las pruebas, comprobaciones e inspecciones llevadas a cabo por el técnico certificador durante el proceso de toma de datos y de calificación de la eficiencia energética del edificio, con la finalidad de establecer la conformidad de la información de partida contenida en el certificado de eficiencia energética.')))
        self.documentacionCtrl.SetToolTip(wx.ToolTip(_('Documentación aportada para justificar la calificación energética.')))
        self.fechaInformeCtrl_dia.SetToolTip(wx.ToolTip(_('Fecha de elaboración el certificado de eficiencia energética (Día)')))
        self.fechaInformeCtrl_mes.SetToolTip(wx.ToolTip(_('Fecha de elaboración el certificado de eficiencia energética (Mes)')))
        self.fechaInformeCtrl_anno.SetToolTip(wx.ToolTip(_('Fecha de elaboración el certificado de eficiencia energética (Año)')))
        self.fechaVisitaCtrl_dia.SetToolTip(wx.ToolTip(_('Fecha de la visita al inmueble (Día)')))
        self.fechaVisitaCtrl_mes.SetToolTip(wx.ToolTip(_('Fecha de la visita al inmueble (Mes)')))
        self.fechaVisitaCtrl_anno.SetToolTip(wx.ToolTip(_('Fecha de la visita al inmueble (Año)')))
        self.generarInformeBoton.SetToolTip(wx.ToolTip(_('Generar informe de certificación y de medidas de mejora')))

    def onOpcion2Choice(self, event):
        """
        Metodo: onOpcion2Choice

        ARGUMENTOS:
                event:
        """
        texto = self.opcion2Choice.GetStringSelection()
        if texto == '':
            self.opcion3Choice.SetItems([])
        else:
            nuevo = []
            for i in self.listaMedidas:
                if i == texto or i == self.opcion1Choice.GetStringSelection():
                    pass
                else:
                    nuevo.append(i)

            self.opcion3Choice.SetItems(nuevo)

    def onOpcion1Choice(self, event):
        """
        Metodo: onOpcion1Choice

        ARGUMENTOS:
                event:
        """
        texto = self.opcion1Choice.GetStringSelection()
        if texto == '':
            self.opcion2Choice.SetItems([])
            self.opcion3Choice.SetItems([])
        else:
            nuevo = []
            for i in self.listaMedidas:
                if i == texto:
                    pass
                else:
                    nuevo.append(i)

            self.opcion2Choice.SetItems(nuevo)
            self.opcion3Choice.SetItems([])

    def _init_coll_conjuntosIncluirlistCtrl_Columns(self, a):
        """
        Metodo: _init_coll_conjuntosIncluirlistCtrl_Columns

        ARGUMENTOS:
                a:
        """
        a.InsertColumn(col=0, format=wx.LIST_FORMAT_CENTER, heading=_('Conjuntos de medidas'), width=234)
        a.InsertColumn(col=1, format=wx.LIST_FORMAT_CENTER, heading=_('Calificación'), width=140)
        self.listaMedidas = [
         '']
        for i in self.parent.listadoConjuntosMMUsuario:
            if i.datosNuevoEdificio.casoValido == True:
                if self.parent.programa == 'Residencial':
                    cali = str(round(i.datosNuevoEdificio.datosResultados.emisionesMostrar, 1)) + ' ' + i.datosNuevoEdificio.datosResultados.emisiones_nota
                else:
                    try:
                        cali = str(round(i.datosNuevoEdificio.datosResultados.emisionesMostrar, 1)) + ' ' + i.datosNuevoEdificio.datosResultados.emisiones_nota
                    except:
                        wx.MessageBox(_('El conjunto de medidas %s no es válido.' % i.nombre), _('Aviso'))
                        return

                a.Append([i.nombre, cali])
                self.listaMedidas.append(i.nombre)

    def __init__(self, a):
        """
        Constructor de la clase

        ARGUMENTOS:
                a:
        """
        self.parent = a
        self.dev = False
        self._init_ctrls(a)

    def OnGenerarInformeBotonButton(self, event):
        """
        Metodo: OnGenerarInformeBotonButton

        ARGUMENTOS:
                event:
        """
        if self.parent.objEdificio.esEdificioExistente == True and self.opcion1Choice.GetStringSelection() == '':
            wx.MessageBox(_('No ha seleccionado ningún conjunto de mejoras para su edificio. INFORME INCOMPLETO'), _('Aviso'))
        datos = []
        datos.append(self.opcion1Choice.GetStringSelection())
        datos.append(self.opcion2Choice.GetStringSelection())
        datos.append(self.opcion3Choice.GetStringSelection())
        datos.append(self.comentariosCtrl.GetValue())
        datos.append(self.documentacionCtrl.GetValue())
        fecha = [self.fechaInformeCtrl_dia.GetValue(), self.fechaInformeCtrl_mes.GetValue(), self.fechaInformeCtrl_anno.GetValue()]
        datos.append(fecha)
        fechaVisita = fecha = [self.fechaVisitaCtrl_dia.GetValue(), self.fechaVisitaCtrl_mes.GetValue(), self.fechaVisitaCtrl_anno.GetValue()]
        datos.append(fechaVisita)
        self.dev = datos
        self.Close()

    def cargarDatos(self, datos):
        """
        Metodo: cargarDatos

        ARGUMENTOS:
                datos:
        """
        self.opcion1Choice.SetStringSelection(datos[0])
        self.onOpcion1Choice(None)
        self.opcion2Choice.SetStringSelection(datos[1])
        self.onOpcion2Choice(None)
        self.opcion3Choice.SetStringSelection(datos[2])
        self.comentariosCtrl.SetValue(datos[3])
        self.documentacionCtrl.SetValue(datos[4])
        if len(datos) <= 5:
            fechaInforme = [
             '', '', '']
        else:
            fechaInforme = datos[5]
        if len(datos) <= 6:
            fechaVisita = [
             '', '', '']
        else:
            fechaVisita = datos[6]
        if fechaInforme != ['', '', '']:
            self.fechaInformeCtrl_dia.SetValue(fechaInforme[0])
            self.fechaInformeCtrl_mes.SetValue(fechaInforme[1])
            self.fechaInformeCtrl_anno.SetValue(fechaInforme[2])
        else:
            fechaInforme = datetime.date.today()
            dia = fechaInforme.day
            mes = fechaInforme.month
            anno = fechaInforme.year
            self.fechaInformeCtrl_dia.SetValue(unicode(dia))
            self.fechaInformeCtrl_mes.SetValue(unicode(mes))
            self.fechaInformeCtrl_anno.SetValue(unicode(anno))
        self.fechaVisitaCtrl_dia.SetValue(fechaVisita[0])
        self.fechaVisitaCtrl_mes.SetValue(fechaVisita[1])
        self.fechaVisitaCtrl_anno.SetValue(fechaVisita[2])
        return

    def OnCancelarBotonButton(self, event):
        """
        Metodo: OnCancelarBotonButton

        ARGUMENTOS:
                event:
        """
        self.Close()
        self.onOpcion1Choice(None)
        return