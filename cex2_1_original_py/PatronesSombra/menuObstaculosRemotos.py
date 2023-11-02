# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: PatronesSombra\menuObstaculosRemotos.pyc
# Compiled at: 2015-02-17 10:48:36
"""
Modulo: menuObstaculosRemotos.py

"""
import wx, Envolvente.dialogoConfirma as dialogoConfirma, Calculos.calculoPerdidasSombras as calculoPerdidasSombras, PatronesSombra.ayudaObstaculos as ayudaObstaculos, PatronesSombra.ayudaModificarObstaculos as ayudaModificarObstaculos, directorios
Directorio = directorios.BuscaDirectorios().Directorio
wxID_PANEL1, wxID_PANEL1ACIMUT1SELEC, wxID_PANEL1ACIMUT1TEXT, wxID_PANEL1ACIMUT2SELEC, wxID_PANEL1ACIMUT2TEXT, wxID_PANEL1BOTANADIR, wxID_PANEL1BOTBORRAR, wxID_PANEL1BOTCALCULAR, wxID_PANEL1BOTGUARDARPATRON, wxID_PANEL1BOTMODIFICAR, wxID_PANEL1CARGARPATRONTEXT, wxID_PANEL1DEFINIRTEXT, wxID_PANEL1ELEVACIO1SELEC, wxID_PANEL1ELEVACION1TEXT, wxID_PANEL1ELEVACION2SELEC, wxID_PANEL1ELEVACION2TEXT, wxID_PANEL1LISTAOBSTACULOS, wxID_PANEL1NOMBRESOMBRA, wxID_PANEL1NOMBRESOMBRATEXT, wxID_PANEL1PANEL1, wxID_PANEL1SELECCIONASOMBRA, wxID_PANEL1STATICBITMAP1, wxID_PANEL1STATICBITMAP2, wxID_PANEL1STATICBITMAP3, wxID_PANEL1ACIMUT3TEXT, wxID_PANEL1ACIMUT4TEXT, wxID_PANEL1ELEVACION4TEXT, wxID_PANEL1ELEVACION3TEXT, wxID_PANEL1ACIMUT3SELEC, wxID_PANEL1ELEVACION3SELEC, wxID_PANEL1ACIMUT4SELEC, wxID_PANEL1ELEVACION4SELEC, wxID_PANEL1NOTA, wxID_PANEL1ELEVACIONTEXT, wxID_PANEL1AYUDAOBSTACULOSBUTTON, wxID_PANEL1INTRODUCCIONSIMPLIFICADATEXT, wxID_PANEL1CREARNUEVOBUTTON, wxID_PANEL1ACIMUT1TEXTGRADOS, wxID_PANEL1ACIMUT2TEXTGRADOS, wxID_PANEL1ACIMUT3TEXTGRADOS, wxID_PANEL1ACIMUT4TEXTGRADOS, wxID_PANEL1ELEVACION1TEXTGRADOS, wxID_PANEL1ELEVACION2TEXTGRADOS, wxID_PANEL1ELEVACION3TEXTGRADOS, wxID_PANEL1ELEVACION4TEXTGRADOS, wxID_PANEL1PATRONTEXT, wxID_PANEL1BOTMODIFICARPATRON, wxID_PANEL1BOTBORRARPATRON = [ wx.NewId() for _init_ctrls in range(48) ]

def create(app, provincia):
    """
    Metodo: create

    ARGUMENTOS:
                app:
                provincia:
    """
    return Panel1(id=-1, name='panel1', parent=app, pos=wx.Point(0, 0), size=wx.Size(914, 688), style=wx.TAB_TRAVERSAL, prov=provincia)


class Panel1(wx.Frame):
    """
    Clase: Panel1 del modulo menuObstaculosRemotos.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
        """
        self.listaPuntos = []
        wx.Frame.__init__(self, id=wxID_PANEL1, name='', parent=prnt, pos=wx.Point(0, 0), size=wx.Size(914, 743), style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN | wx.TAB_TRAVERSAL, title=_('Patrones de sombra'))
        self.SetBackgroundColour('white')
        self.nombreSombraText = wx.StaticText(id=wxID_PANEL1NOMBRESOMBRATEXT, label=_('Nombre del patrón de sombras'), name='nombreSombraText', parent=self, pos=wx.Point(30, 15), size=wx.Size(152, 13), style=0)
        self.nombreSombra = wx.TextCtrl(id=wxID_PANEL1NOMBRESOMBRA, name='nombreSombra', parent=self, pos=wx.Point(240, 13), size=wx.Size(400, 21), style=0, value='')
        self.crearNuevoButton = wx.Button(id=wxID_PANEL1CREARNUEVOBUTTON, label=_('Crear nuevo'), name='crearNuevoButton', parent=self, pos=wx.Point(660, 13), size=wx.Size(75, 23), style=0)
        self.crearNuevoButton.Bind(wx.EVT_BUTTON, self.OnCrearNuevo, id=wxID_PANEL1CREARNUEVOBUTTON)
        self.seleccionarPatronText = wx.StaticText(id=wxID_PANEL1CARGARPATRONTEXT, label=_('Patrones de sombra definidos'), name='seleccionarPatronText', parent=self, pos=wx.Point(30, 40), size=wx.Size(150, 13), style=0)
        self.seleccionaSombra = wx.Choice(choices=[], id=wxID_PANEL1SELECCIONASOMBRA, name='seleccionaSombra', parent=self, pos=wx.Point(240, 38), size=wx.Size(400, 21), style=0)
        self.seleccionaSombra.Bind(wx.EVT_CHOICE, self.OnSelecionaSombraChoice, id=wxID_PANEL1SELECCIONASOMBRA)
        self.patronText = wx.StaticBox(id=wxID_PANEL1PATRONTEXT, label=_(''), name='PropiedadesLinea', parent=self, pos=wx.Point(15, 70), size=wx.Size(860, 420), style=0)
        self.patronText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.patronText.SetForegroundColour(wx.Colour(0, 64, 128))
        if self.provincia in ('Las Palmas', 'Santa Cruz de Tenerife'):
            self.patronText.SetLabel(_('Trayectoria solar para Canarias'))
        else:
            self.patronText.SetLabel(_('Trayectoria solar para la Península Ibérica y Baleares'))
        self.elevacionText = wx.StaticText(id=wxID_PANEL1ELEVACIONTEXT, label=_('Elevación β (º)'), name='nombreSombraText', parent=self, pos=wx.Point(30, 90), size=wx.Size(200, 13), style=0)
        self.panel1 = wx.Panel(id=wxID_PANEL1PANEL1, name='panel1', parent=self, pos=wx.Point(20, 104), size=wx.Size(850, 370), style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(252, 245, 201))
        self.panel1.Bind(wx.EVT_PAINT, self.onPaint)
        self.AcimutText = wx.StaticText(id=wxID_PANEL1DEFINIRTEXT, label=_('Acimut α (º)'), name='acimutText', parent=self, pos=wx.Point(790, 472), size=wx.Size(80, 13), style=0)
        self.definirPoligonoLinea = wx.StaticBox(id=-1, label=_('Definir polígonos'), name='PropiedadesLinea', parent=self, pos=wx.Point(15, 495), size=wx.Size(860, 165), style=0)
        self.definirPoligonoLinea.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.definirPoligonoLinea.SetForegroundColour(wx.Colour(0, 64, 128))
        self.nota = wx.StaticText(id=wxID_PANEL1NOTA, label=_('Sitúese en el centro del elemento sombreado mirando al sur; Ángulos al este negativos'), name='definirText', parent=self, pos=wx.Point(395, 640), size=wx.Size(475, 13), style=0)
        self.listaObstaculos = wx.ListCtrl(id=wxID_PANEL1LISTAOBSTACULOS, name='listaObstaculos', parent=self, pos=wx.Point(370, 520), size=wx.Size(496, 120), style=wx.LC_REPORT)
        self._init_coll_listCtrl1_Columns(self.listaObstaculos)
        self.listaObstaculos.Bind(wx.EVT_LIST_ITEM_SELECTED, self.pinchar_listaObstaculos, id=wxID_PANEL1LISTAOBSTACULOS)
        self.Acimut1Text = wx.StaticText(id=wxID_PANEL1ACIMUT1TEXT, label=_('α 1'), name='Acimut1Text', parent=self, pos=wx.Point(30, 520), size=wx.Size(25, 13), style=0)
        self.acimut2Text = wx.StaticText(id=wxID_PANEL1ACIMUT2TEXT, label=_('α 2'), name='acimut2Text', parent=self, pos=wx.Point(30, 542), size=wx.Size(25, 13), style=0)
        self.acimut3Text = wx.StaticText(id=wxID_PANEL1ACIMUT3TEXT, label=_('α 3'), name='acimut2Text', parent=self, pos=wx.Point(30, 564), size=wx.Size(25, 13), style=0)
        self.acimut4Text = wx.StaticText(id=wxID_PANEL1ACIMUT4TEXT, label=_('α 4'), name='acimut2Text', parent=self, pos=wx.Point(30, 586), size=wx.Size(25, 13), style=0)
        self.elevacion1Text = wx.StaticText(id=wxID_PANEL1ELEVACION1TEXT, label=_('β 1'), name='elevacion1Text', parent=self, pos=wx.Point(160, 520), size=wx.Size(25, 13), style=0)
        self.elevacion2Text = wx.StaticText(id=wxID_PANEL1ELEVACION2TEXT, label=_('β 2'), name='elevacion2Text', parent=self, pos=wx.Point(160, 542), size=wx.Size(25, 13), style=0)
        self.elevacion3Text = wx.StaticText(id=wxID_PANEL1ELEVACION3TEXT, label=_('β 3'), name='elevacion2Text', parent=self, pos=wx.Point(160, 564), size=wx.Size(25, 13), style=0)
        self.elevacion4Text = wx.StaticText(id=wxID_PANEL1ELEVACION4TEXT, label=_('β 4'), name='elevacion2Text', parent=self, pos=wx.Point(160, 586), size=wx.Size(25, 13), style=0)
        self.acimut1Selec = wx.TextCtrl(id=wxID_PANEL1ACIMUT1SELEC, name='acimut1Selec', parent=self, pos=wx.Point(59, 516), size=wx.Size(56, 21), style=0, value='')
        self.acimut1Selec.Bind(wx.EVT_TEXT, self.OnAcimut1Text, id=wxID_PANEL1ACIMUT1SELEC)
        self.elevacion1Selec = wx.TextCtrl(id=wxID_PANEL1ELEVACIO1SELEC, name='elevacio1Selec', parent=self, pos=wx.Point(189, 516), size=wx.Size(56, 21), style=0, value='')
        self.acimut2Selec = wx.TextCtrl(id=wxID_PANEL1ACIMUT2SELEC, name='acimut2Selec', parent=self, pos=wx.Point(59, 538), size=wx.Size(56, 21), style=0, value='')
        self.acimut2Selec.Bind(wx.EVT_TEXT, self.OnAcimut2Text, id=wxID_PANEL1ACIMUT2SELEC)
        self.elevacion2Selec = wx.TextCtrl(id=wxID_PANEL1ELEVACION2SELEC, name='elevacion2Selec', parent=self, pos=wx.Point(189, 538), size=wx.Size(56, 21), style=0, value='')
        self.acimut3Selec = wx.TextCtrl(id=wxID_PANEL1ACIMUT3SELEC, name='acimut3Selec', parent=self, pos=wx.Point(59, 560), size=wx.Size(56, 21), style=0, value='')
        self.elevacion3Selec = wx.TextCtrl(id=wxID_PANEL1ELEVACION3SELEC, name='elevacion3Selec', parent=self, pos=wx.Point(189, 560), size=wx.Size(56, 21), style=0, value='0')
        self.acimut4Selec = wx.TextCtrl(id=wxID_PANEL1ACIMUT4SELEC, name='acimut4Selec', parent=self, pos=wx.Point(59, 582), size=wx.Size(56, 21), style=0, value='')
        self.elevacion4Selec = wx.TextCtrl(id=wxID_PANEL1ELEVACION4SELEC, name='elevacion4Selec', parent=self, pos=wx.Point(189, 582), size=wx.Size(56, 21), style=0, value='0')
        self.Acimut1TextGrados = wx.StaticText(id=wxID_PANEL1ACIMUT1TEXTGRADOS, label=_('º'), name='Acimut1Text', parent=self, pos=wx.Point(118, 520), size=wx.Size(25, 13), style=0)
        self.acimut2TextGrados = wx.StaticText(id=wxID_PANEL1ACIMUT2TEXTGRADOS, label=_('º'), name='acimut2Text', parent=self, pos=wx.Point(118, 542), size=wx.Size(25, 13), style=0)
        self.acimut3TextGrados = wx.StaticText(id=wxID_PANEL1ACIMUT3TEXTGRADOS, label=_('º'), name='acimut2Text', parent=self, pos=wx.Point(118, 564), size=wx.Size(25, 13), style=0)
        self.acimut4TextGrados = wx.StaticText(id=wxID_PANEL1ACIMUT4TEXTGRADOS, label=_('º'), name='acimut2Text', parent=self, pos=wx.Point(118, 586), size=wx.Size(25, 13), style=0)
        self.elevacion1TextGrados = wx.StaticText(id=wxID_PANEL1ELEVACION1TEXTGRADOS, label=_('º'), name='elevacion1Text', parent=self, pos=wx.Point(249, 520), size=wx.Size(10, 13), style=0)
        self.elevacion2TextGrados = wx.StaticText(id=wxID_PANEL1ELEVACION2TEXTGRADOS, label=_('º'), name='elevacion2Text', parent=self, pos=wx.Point(249, 542), size=wx.Size(10, 13), style=0)
        self.elevacion3TextGrados = wx.StaticText(id=wxID_PANEL1ELEVACION3TEXTGRADOS, label=_('º'), name='elevacion2Text', parent=self, pos=wx.Point(249, 564), size=wx.Size(10, 13), style=0)
        self.elevacion4TextGrados = wx.StaticText(id=wxID_PANEL1ELEVACION4TEXTGRADOS, label=_('º'), name='elevacion2Text', parent=self, pos=wx.Point(249, 586), size=wx.Size(10, 13), style=0)
        self.botAnadir = wx.Button(id=wxID_PANEL1BOTANADIR, label=_('Añadir'), name='botAnadir', parent=self, pos=wx.Point(275, 520), size=wx.Size(75, 21), style=0)
        self.botAnadir.Bind(wx.EVT_BUTTON, self.OnAnadirButton, id=wxID_PANEL1BOTANADIR)
        self.botModificar = wx.Button(id=wxID_PANEL1BOTMODIFICAR, label=_('Modificar'), name='botModificar', parent=self, pos=wx.Point(275, 545), size=wx.Size(75, 21), style=0)
        self.botModificar.Bind(wx.EVT_BUTTON, self.OnModificarButton, id=wxID_PANEL1BOTMODIFICAR)
        self.botModificar.Enable(False)
        self.botBorrar = wx.Button(id=wxID_PANEL1BOTBORRAR, label=_('Borrar'), name='botBorrar', parent=self, pos=wx.Point(275, 571), size=wx.Size(75, 21), style=0)
        self.botBorrar.Bind(wx.EVT_BUTTON, self.OnBorrarButton, id=wxID_PANEL1BOTBORRAR)
        self.botBorrar.Enable(False)
        self.introduccionSimplificadaText = wx.StaticText(id=wxID_PANEL1INTRODUCCIONSIMPLIFICADATEXT, label=_('Introducción simplificada'), name='introduccionSimplificadaText', parent=self, pos=wx.Point(30, 619), size=wx.Size(136, 13), style=0)
        self.ayudaObstaculosButton = wx.Button(id=wxID_PANEL1AYUDAOBSTACULOSBUTTON, label=_('Obstáculos rectangulares'), name='ayudaObstaculosButton', parent=self, pos=wx.Point(188, 617), size=wx.Size(162, 21), style=0)
        self.ayudaObstaculosButton.Bind(wx.EVT_BUTTON, self.OnAyudaObstaculosButton, id=wxID_PANEL1AYUDAOBSTACULOSBUTTON)
        self.GuardarPatronBoton = wx.Button(id=wxID_PANEL1BOTGUARDARPATRON, label=_('Guardar patrón'), name='botGuardar', parent=self, pos=wx.Point(15, 677), size=wx.Size(100, 23), style=0)
        self.GuardarPatronBoton.Bind(wx.EVT_BUTTON, self.OnGuardarPatronBotonButton, id=wxID_PANEL1BOTGUARDARPATRON)
        self.GuardarPatronBoton.SetForegroundColour(wx.Colour(0, 64, 128))
        self.GuardarPatronBoton.SetBackgroundColour('white')
        self.seleccionaSombra.SetItems(self.sombrasGuardadas())
        self.ModificarPatronBoton = wx.Button(id=wxID_PANEL1BOTMODIFICARPATRON, label=_('Modificar patrón'), name='ModificarPatronBoton', parent=self, pos=wx.Point(130, 677), size=wx.Size(100, 23), style=0)
        self.ModificarPatronBoton.Bind(wx.EVT_BUTTON, self.OnModificarPatronBotonButton, id=wxID_PANEL1BOTMODIFICARPATRON)
        self.ModificarPatronBoton.SetForegroundColour(wx.Colour(0, 64, 128))
        self.ModificarPatronBoton.SetBackgroundColour('white')
        self.BorrarPatronBoton = wx.Button(id=wxID_PANEL1BOTBORRARPATRON, label=_('Borrar patrón'), name='BorrarPatronBoton', parent=self, pos=wx.Point(290, 677), size=wx.Size(100, 23), style=0)
        self.BorrarPatronBoton.Bind(wx.EVT_BUTTON, self.OnBorrarPatronBotonButton, id=wxID_PANEL1BOTBORRARPATRON)
        self.BorrarPatronBoton.SetForegroundColour(wx.Colour(0, 64, 128))
        self.BorrarPatronBoton.SetBackgroundColour('white')
        self.nombreSombra.SetToolTip(wx.ToolTip(_('Nombre único con el que se identica este patrón de sombras')))
        self.crearNuevoButton.SetToolTip(wx.ToolTip(_('Graba el patrón de sombras que está editando.')))
        self.seleccionaSombra.SetToolTip(wx.ToolTip(_('Seleccione un patrón de sombras existente para editarlo o visualizarlo.')))
        self.listaObstaculos.SetToolTip(wx.ToolTip(_('Lista de polígonos que conforman el patrón de sombreamiento.')))
        self.acimut1Selec.SetToolTip(wx.ToolTip(_('Coordenada azimutal de una de las esquinas del elemento de sombreamiento.\nSur: 0º\nÁngulos al este: negativos')))
        self.acimut2Selec.SetToolTip(wx.ToolTip(_('Coordenada azimutal de una de las esquinas del elemento de sombreamiento.\nSur: 0º\nÁngulos al este: negativos')))
        self.acimut3Selec.SetToolTip(wx.ToolTip(_('Coordenada azimutal de una de las esquinas del elemento de sombreamiento.\nSur: 0º\nÁngulos al este: negativos')))
        self.acimut4Selec.SetToolTip(wx.ToolTip(_('Coordenada azimutal de una de las esquinas del elemento de sombreamiento.\nSur: 0º\nÁngulos al este: negativos')))
        self.elevacion1Selec.SetToolTip(wx.ToolTip(_('Ángulo de elevación de una de las esquinas del elemento de sombreamiento.')))
        self.elevacion2Selec.SetToolTip(wx.ToolTip(_('Ángulo de elevación de una de las esquinas del elemento de sombreamiento.')))
        self.elevacion3Selec.SetToolTip(wx.ToolTip(_('Ángulo de elevación de una de las esquinas del elemento de sombreamiento.')))
        self.elevacion4Selec.SetToolTip(wx.ToolTip(_('Ángulo de elevación de una de las esquinas del elemento de sombreamiento.')))
        self.botAnadir.SetToolTip(wx.ToolTip(_('Añade un polígono nuevo al patrón de sombras.')))
        self.botModificar.SetToolTip(wx.ToolTip(_('Modifique el polígono seleccionado.')))
        self.botBorrar.SetToolTip(wx.ToolTip(_('Elimina el polígono seleccionado.')))
        self.ayudaObstaculosButton.SetToolTip(wx.ToolTip(_('Ayuda para la generación de los polígonos para los elementos \nde sombreamiento con sección rectangular.')))
        self.GuardarPatronBoton.SetToolTip(wx.ToolTip(_('Añade un nuevo patrón de sombras.')))
        self.ModificarPatronBoton.SetToolTip(wx.ToolTip(_('Guarda las modificaciones que ha realizado en el patrón de sombras.')))
        self.BorrarPatronBoton.SetToolTip(wx.ToolTip(_('Elimina este patrón de sombras.')))

    def OnCrearNuevo(self, event):
        """
        Metodo: OnCrearNuevo

        ARGUMENTOS:
                event): #funcion para limpiar todos los camp:
        """
        self.listaPuntos = []
        self.panel1.Refresh()
        self.nombreSombra.SetValue('')
        self.seleccionaSombra.SetSelection(-1)
        self.listaObstaculos.DeleteAllItems()
        self.acimut1Selec.SetValue('')
        self.elevacion1Selec.SetValue('')
        self.acimut2Selec.SetValue('')
        self.elevacion2Selec.SetValue('')
        self.acimut3Selec.SetValue('')
        self.elevacion3Selec.SetValue('0')
        self.acimut4Selec.SetValue('')
        self.elevacion4Selec.SetValue('0')
        self.botModificar.Enable(False)
        self.botBorrar.Enable(False)

    def OnAyudaObstaculosButton(self, event):
        """
        Metodo: OnAyudaObstaculosButton

        ARGUMENTOS:
                event:
        """
        ayuda = ayudaObstaculos.Dialog1(self)
        ayuda.ShowModal()
        if ayuda.dev != False:
            poligono1 = ayuda.dev[0]
            self.acimut1Selec.SetValue(poligono1[0][0])
            self.elevacion1Selec.SetValue(poligono1[0][1])
            self.acimut2Selec.SetValue(poligono1[1][0])
            self.elevacion2Selec.SetValue(poligono1[1][1])
            self.acimut3Selec.SetValue(poligono1[2][0])
            self.elevacion3Selec.SetValue(poligono1[2][1])
            self.acimut4Selec.SetValue(poligono1[3][0])
            self.elevacion4Selec.SetValue(poligono1[3][1])
            self.OnAnadirButton(None)
            if len(ayuda.dev) == 2:
                poligono2 = ayuda.dev[1]
                self.acimut1Selec.SetValue(poligono2[0][0])
                self.elevacion1Selec.SetValue(poligono2[0][1])
                self.acimut2Selec.SetValue(poligono2[1][0])
                self.elevacion2Selec.SetValue(poligono2[1][1])
                self.acimut3Selec.SetValue(poligono2[2][0])
                self.elevacion3Selec.SetValue(poligono2[2][1])
                self.acimut4Selec.SetValue(poligono2[3][0])
                self.elevacion4Selec.SetValue(poligono2[3][1])
                self.OnAnadirButton(None)
        else:
            return
        return

    def OnModificarPatronBotonButton(self, event):
        """
        Metodo: OnModificarPatronBotonButton

        ARGUMENTOS:
                event:
        """
        nombre = self.nombreSombra.GetValue()
        if self.nombreSombra.GetValue() == 'Sin patrón':
            wx.MessageBox(_('El nombre escogido para el patrón de sombras es incorrecto. Debe introducir otro nombre.'), _('Aviso'))
            return
        if self.seleccionaSombra.GetStringSelection() != '':
            if nombre == self.seleccionaSombra.GetStringSelection():
                utilizadoCerr, utilizadoVent = self.comprobacionUtilizacionPatron(nombre)
                if utilizadoCerr == True or utilizadoVent == True:
                    if utilizadoCerr == True and utilizadoVent == True:
                        mensaje = 'cerramientos opacos y huecos'
                    else:
                        if utilizadoCerr == True:
                            mensaje = 'cerramientos opacos'
                        else:
                            if utilizadoVent == True:
                                mensaje = 'huecos'
                            mensaje1 = 'El patrón de sombras seleccionado ha sido asignado a algún elemento de tipo '
                            dlg = ayudaModificarObstaculos.Dialog1(self, mensaje, mensaje1)
                            dlg.ShowModal()
                            if dlg.dev == False:
                                return
                        for i in self.parent.datosSombras:
                            if nombre == i[0]:
                                i[0] = self.nombreSombra.GetValue()
                                i[1] = self.listaPuntos
                                i[2] = calculoPerdidasSombras.calculoPorcentajesSombras(self.listaPuntos, self.provincia)
                                break

                    self.seleccionaSombra.SetItems(self.sombrasGuardadas())
                    self.seleccionaSombra.SetStringSelection(nombre)
                else:
                    for i in self.parent.datosSombras:
                        if nombre == i[0]:
                            i[0] = self.nombreSombra.GetValue()
                            i[1] = self.listaPuntos
                            i[2] = calculoPerdidasSombras.calculoPorcentajesSombras(self.listaPuntos, self.provincia)
                            break

                    self.seleccionaSombra.SetItems(self.sombrasGuardadas())
                    self.seleccionaSombra.SetStringSelection(nombre)
            else:
                nombreAntiguo = self.seleccionaSombra.GetStringSelection()
                utilizadoCerr, utilizadoVent = self.comprobacionUtilizacionPatron(nombreAntiguo)
                if utilizadoCerr == True or utilizadoVent == True:
                    if utilizadoCerr == True and utilizadoVent == True:
                        mensaje = 'cerramientos opacos y huecos'
                    else:
                        if utilizadoCerr == True:
                            mensaje = 'cerramientos opacos'
                        else:
                            if utilizadoVent == True:
                                mensaje = 'huecos'
                            mensaje1 = 'El patrón de sombras seleccionado ha sido asignado a algún elemento de tipo '
                            dlg = ayudaModificarObstaculos.Dialog1(self, mensaje, mensaje1)
                            dlg.ShowModal()
                            if dlg.dev == False:
                                return
                        for i in self.parent.datosSombras:
                            if nombreAntiguo == i[0]:
                                i[0] = self.nombreSombra.GetValue()
                                i[1] = self.listaPuntos
                                i[2] = calculoPerdidasSombras.calculoPorcentajesSombras(self.listaPuntos, self.provincia)
                                break

                    nombreNuevo = self.nombreSombra.GetValue()
                    self.seleccionaSombra.SetItems(self.sombrasGuardadas())
                    self.seleccionaSombra.SetStringSelection(nombreNuevo)
                    self.actualizarNombreSombras(nombreNuevo, nombreAntiguo)
                else:
                    for i in self.parent.datosSombras:
                        if nombreAntiguo == i[0]:
                            i[0] = self.nombreSombra.GetValue()
                            i[1] = self.listaPuntos
                            i[2] = calculoPerdidasSombras.calculoPorcentajesSombras(self.listaPuntos, self.provincia)
                            break

                    self.seleccionaSombra.SetItems(self.sombrasGuardadas())
                    self.seleccionaSombra.SetStringSelection(nombre)
        else:
            wx.MessageBox(_('Es necesario seleccionar un patrón de sombras existente para modificarlo'), _('Aviso'))

    def OnBorrarPatronBotonButton(self, event):
        """
        Metodo: OnBorrarPatronBotonButton

        ARGUMENTOS:
                event:
        """
        nombre = self.nombreSombra.GetValue()
        utilizadoCerr, utilizadoVent = self.comprobacionUtilizacionPatron(nombre)
        if utilizadoCerr == True and utilizadoVent == True:
            wx.MessageBox(_('El patrón de sombras no puede ser eliminado porque ha sido asignado algún elemento de tipo cerramientos opacos o huecos'), _('Aviso'))
            return
        if utilizadoCerr == True:
            wx.MessageBox(_('El patrón de sombras no puede ser eliminado porque ha sido asignado algún elemento de tipo cerramientos opacos'), _('Aviso'))
            return
        if utilizadoVent == True:
            wx.MessageBox(_('El patrón de sombras no puede ser eliminado porque ha sido asignado algún hueco'), _('Aviso'))
            return
        for i in range(len(self.parent.datosSombras)):
            if self.parent.datosSombras[i][0] == nombre:
                self.parent.datosSombras.pop(i)
                self.seleccionaSombra.SetItems(self.sombrasGuardadas())
                self.seleccionaSombra.SetSelection(-1)
                self.nombreSombra.SetValue('')
                self.listaPuntos = []
                self.refrescarLista()
                self.panel1.Refresh()
                return

        wx.MessageBox(_('No se ha guardado el patrón de sombras "') + nombre + _('"'), _('Aviso'))

    def OnSelecionaSombraChoice(self, event):
        """
        Metodo: OnSelecionaSombraChoice

        ARGUMENTOS:
                event:
        """
        nombre = self.seleccionaSombra.GetStringSelection()
        self.listaObstaculos.DeleteAllItems()
        for i in self.parent.datosSombras:
            if i[0] == nombre:
                self.listaPuntos = []
                for j in i[1]:
                    self.listaPuntos.append(j)

        self.refrescarLista()
        self.panel1.Refresh()
        self.nombreSombra.SetValue(self.seleccionaSombra.GetStringSelection())

    def refrescarLista(self):
        """
        Metodo: refrescarLista

        """
        self.listaObstaculos.DeleteAllItems()
        for i in self.listaPuntos:
            self.listaObstaculos.Append(i)

    def compruebaSombra(self, nombre):
        """
        Metodo: compruebaSombra

        ARGUMENTOS:
                nombre):  ###Comprueba que la sombra no esta ya guarda:
        """
        for i in self.parent.datosSombras:
            if i[0] == nombre:
                return True

        return False

    def OnGuardarPatronBotonButton(self, event):
        """
        Metodo: OnGuardarPatronBotonButton

        ARGUMENTOS:
                event:
        """
        if self.nombreSombra.GetValue() == '':
            wx.MessageBox(_('Debe introducir un nombre para la sombra.'), _('Aviso'))
            return
        if self.nombreSombra.GetValue() == 'Sin patrón':
            wx.MessageBox(_('El nombre escogido para el patrón de sombras es incorrecto. Debe introducir otro nombre.'), _('Aviso'))
            return
        if self.compruebaSombra(self.nombreSombra.GetValue()) == True:
            nombre = self.nombreSombra.GetValue()
            utilizadoCerr, utilizadoVent = self.comprobacionUtilizacionPatron(nombre)
            if utilizadoCerr == True or utilizadoVent == True:
                if utilizadoCerr == True and utilizadoVent == True:
                    mensaje = 'cerramientos opacos y huecos'
                else:
                    if utilizadoCerr == True:
                        mensaje = 'cerramientos opacos'
                    else:
                        if utilizadoVent == True:
                            mensaje = 'huecos'
                        mensaje1 = 'El patrón de sombras ya existe y ha sido asignado a algún elemento de tipo '
                        dlg = ayudaModificarObstaculos.Dialog1(self, mensaje, mensaje1)
                        dlg.ShowModal()
                        if dlg.dev == False:
                            return
                    for i in self.parent.datosSombras:
                        if self.nombreSombra.GetValue() == i[0]:
                            i[0] = self.nombreSombra.GetValue()
                            i[1] = self.listaPuntos
                            i[2] = calculoPerdidasSombras.calculoPorcentajesSombras(self.listaPuntos, self.provincia)
                            break

                self.seleccionaSombra.SetItems(self.sombrasGuardadas())
                self.seleccionaSombra.SetStringSelection(self.nombreSombra.GetValue())
            else:
                mix = dialogoConfirma.Dialog1(self, _('La sombra que ha elegido ya existe, ¿desea reemplazarla?'))
                mix.ShowModal()
                if mix.dev == False:
                    return
                for i in self.parent.datosSombras:
                    if self.nombreSombra.GetValue() == i[0]:
                        i[0] = self.nombreSombra.GetValue()
                        i[1] = self.listaPuntos
                        i[2] = calculoPerdidasSombras.calculoPorcentajesSombras(self.listaPuntos, self.provincia)
                        break

                self.seleccionaSombra.SetItems(self.sombrasGuardadas())
                self.seleccionaSombra.SetStringSelection(self.nombreSombra.GetValue())
        else:
            self.parent.datosSombras.append([self.nombreSombra.GetValue(), self.listaPuntos,
             calculoPerdidasSombras.calculoPorcentajesSombras(self.listaPuntos, self.provincia), False])
            self.seleccionaSombra.SetItems(self.sombrasGuardadas())
            self.seleccionaSombra.SetStringSelection(self.nombreSombra.GetValue())

    def sombrasGuardadas(self):
        """
        Metodo: sombrasGuardadas

        """
        nombres = []
        for i in self.parent.datosSombras:
            nombres.append(i[0])

        return nombres

    def OnAcimut1Text(self, event):
        """
        Metodo: OnAcimut1Text

        ARGUMENTOS:
                event:
        """
        self.acimut4Selec.SetValue(self.acimut1Selec.GetValue())

    def OnAcimut2Text(self, event):
        """
        Metodo: OnAcimut2Text

        ARGUMENTOS:
                event:
        """
        self.acimut3Selec.SetValue(self.acimut2Selec.GetValue())

    def pinchar_listaObstaculos(self, event):
        """
        Metodo: pinchar_listaObstaculos

        ARGUMENTOS:
                event:
        """
        self.pos_selec = int(event.GetIndex())
        fila = self.listaPuntos[self.pos_selec]
        self.acimut1Selec.SetValue(str(fila[0]))
        self.elevacion1Selec.SetValue(str(fila[1]))
        self.acimut2Selec.SetValue(str(fila[2]))
        self.elevacion2Selec.SetValue(str(fila[3]))
        self.acimut3Selec.SetValue(str(fila[4]))
        self.elevacion3Selec.SetValue(str(fila[5]))
        self.acimut4Selec.SetValue(str(fila[6]))
        self.elevacion4Selec.SetValue(str(fila[7]))
        self.botModificar.Enable(True)
        self.botBorrar.Enable(True)

    def OnModificarButton(self, event):
        """
        Metodo: OnModificarButton

        ARGUMENTOS:
                event:
        """
        fila = []
        aci1 = self.acimut1Selec.GetValue()
        ele1 = self.elevacion1Selec.GetValue()
        aci2 = self.acimut2Selec.GetValue()
        ele2 = self.elevacion2Selec.GetValue()
        aci3 = self.acimut3Selec.GetValue()
        ele3 = self.elevacion3Selec.GetValue()
        aci4 = self.acimut4Selec.GetValue()
        ele4 = self.elevacion4Selec.GetValue()
        if ',' in aci1:
            aci1 = aci1.replace(',', '.')
        if ',' in ele1:
            ele1 = ele1.replace(',', '.')
        if ',' in aci2:
            aci2 = aci2.replace(',', '.')
        if ',' in ele2:
            ele2 = ele2.replace(',', '.')
        if ',' in aci3:
            aci3 = aci3.replace(',', '.')
        if ',' in ele3:
            ele3 = ele3.replace(',', '.')
        if ',' in aci4:
            aci4 = aci4.replace(',', '.')
        if ',' in ele2:
            ele4 = ele4.replace(',', '.')
        listaErrores = ''
        try:
            aci1 = float(aci1)
        except (ValueError, TypeError):
            listaErrores += 'α1'

        try:
            ele1 = float(ele1)
        except (ValueError, TypeError):
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'β1'

        try:
            aci2 = float(aci2)
        except (ValueError, TypeError):
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'α2'

        try:
            ele2 = float(ele2)
        except (ValueError, TypeError):
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'β2'

        try:
            aci3 = float(aci3)
        except (ValueError, TypeError):
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'α3'

        try:
            ele3 = float(ele3)
        except (ValueError, TypeError):
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'β3'

        try:
            aci4 = float(aci4)
        except (ValueError, TypeError):
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'α4'

        try:
            ele4 = float(ele4)
        except (ValueError, TypeError):
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'β4'

        if listaErrores != '':
            wx.MessageBox(_('Revise los siguientes campos:\n') + listaErrores, _('Aviso'))
            return
        if aci1 < -180 or aci1 > 180 or aci2 < -180 or aci2 > 180 or aci3 < -180 or aci3 > 180 or aci4 < -180 or aci4 > 180:
            wx.MessageBox(_('Los valores de acimut deben estar en el rango (-180, 180) grados'), _('Aviso'))
            return
        if ele1 < 0 or ele2 < 0 or ele3 < 0 or ele4 < 0 or ele1 > 90 or ele2 > 90 or ele3 > 90 or ele4 > 90:
            wx.MessageBox(_('Los valores de elevación deben estar en el rango (0, 90) grados'), _('Aviso'))
            return
        self.listaObstaculos.DeleteItem(self.pos_selec)
        self.listaPuntos.pop(self.pos_selec)
        fila.append(round(float(aci1), 2))
        fila.append(round(float(ele1), 2))
        fila.append(round(float(aci2), 2))
        fila.append(round(float(ele2), 2))
        fila.append(round(float(aci3), 2))
        fila.append(round(float(ele3), 2))
        fila.append(round(float(aci4), 2))
        fila.append(round(float(ele4), 2))
        self.listaPuntos.append(fila)
        self.listaObstaculos.Append(fila)
        self.panel1.Refresh()
        self.acimut1Selec.SetValue('')
        self.elevacion1Selec.SetValue('')
        self.acimut2Selec.SetValue('')
        self.elevacion2Selec.SetValue('')
        self.acimut3Selec.SetValue('')
        self.elevacion3Selec.SetValue('0')
        self.acimut4Selec.SetValue('')
        self.elevacion4Selec.SetValue('0')
        self.panel1.Refresh()

    def OnBorrarButton(self, event):
        """
        Metodo: OnBorrarButton

        ARGUMENTOS:
                event:
        """
        seleccionado = self.listaObstaculos.GetFocusedItem()
        self.listaObstaculos.DeleteItem(seleccionado)
        del self.listaPuntos[seleccionado]
        self.acimut1Selec.SetValue('')
        self.elevacion1Selec.SetValue('')
        self.acimut2Selec.SetValue('')
        self.elevacion2Selec.SetValue('')
        self.acimut3Selec.SetValue('')
        self.elevacion3Selec.SetValue('0')
        self.acimut4Selec.SetValue('')
        self.elevacion4Selec.SetValue('0')
        self.panel1.Refresh()

    def OnAnadirButton(self, event):
        """
        Metodo: OnAnadirButton

        ARGUMENTOS:
                event:
        """
        fila = []
        aci1 = self.acimut1Selec.GetValue()
        ele1 = self.elevacion1Selec.GetValue()
        aci2 = self.acimut2Selec.GetValue()
        ele2 = self.elevacion2Selec.GetValue()
        aci3 = self.acimut3Selec.GetValue()
        ele3 = self.elevacion3Selec.GetValue()
        aci4 = self.acimut4Selec.GetValue()
        ele4 = self.elevacion4Selec.GetValue()
        if ',' in aci1:
            aci1 = aci1.replace(',', '.')
        if ',' in ele1:
            ele1 = ele1.replace(',', '.')
        if ',' in aci2:
            aci2 = aci2.replace(',', '.')
        if ',' in ele2:
            ele2 = ele2.replace(',', '.')
        if ',' in aci3:
            aci3 = aci3.replace(',', '.')
        if ',' in ele3:
            ele3 = ele3.replace(',', '.')
        if ',' in aci4:
            aci4 = aci4.replace(',', '.')
        if ',' in ele2:
            ele4 = ele4.replace(',', '.')
        listaErrores = ''
        try:
            aci1 = float(aci1)
        except (ValueError, TypeError):
            listaErrores += 'α1'

        try:
            ele1 = float(ele1)
        except (ValueError, TypeError):
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'β1'

        try:
            aci2 = float(aci2)
        except (ValueError, TypeError):
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'α2'

        try:
            ele2 = float(ele2)
        except (ValueError, TypeError):
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'β2'

        try:
            aci3 = float(aci3)
        except (ValueError, TypeError):
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'α3'

        try:
            ele3 = float(ele3)
        except (ValueError, TypeError):
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'β3'

        try:
            aci4 = float(aci4)
        except (ValueError, TypeError):
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'α4'

        try:
            ele4 = float(ele4)
        except (ValueError, TypeError):
            if listaErrores != '':
                listaErrores += ', '
            listaErrores += 'β4'

        if listaErrores != '':
            wx.MessageBox(_('Revise los siguientes campos:\n') + listaErrores, _('Aviso'))
            return
        if aci1 < -180 or aci1 > 180 or aci2 < -180 or aci2 > 180 or aci3 < -180 or aci3 > 180 or aci4 < -180 or aci4 > 180:
            wx.MessageBox(_('Los valores de acimut deben estar en el rango (-180, 180) grados'), _('Aviso'))
            return
        if ele1 < 0 or ele2 < 0 or ele3 < 0 or ele4 < 0 or ele1 > 90 or ele2 > 90 or ele3 > 90 or ele4 > 90:
            wx.MessageBox(_('Los valores de elevación deben estar en el rango (0, 90) grados'), _('Aviso'))
            return
        fila.append(round(float(aci1), 2))
        fila.append(round(float(ele1), 2))
        fila.append(round(float(aci2), 2))
        fila.append(round(float(ele2), 2))
        fila.append(round(float(aci3), 2))
        fila.append(round(float(ele3), 2))
        fila.append(round(float(aci4), 2))
        fila.append(round(float(ele4), 2))
        self.listaPuntos.append(fila)
        self.listaObstaculos.Append(fila)
        self.panel1.Refresh()
        self.acimut1Selec.SetValue('')
        self.elevacion1Selec.SetValue('')
        self.acimut2Selec.SetValue('')
        self.elevacion2Selec.SetValue('')
        self.acimut3Selec.SetValue('')
        self.elevacion3Selec.SetValue('0')
        self.acimut4Selec.SetValue('')
        self.elevacion4Selec.SetValue('0')

    def _init_coll_listCtrl1_Columns(self, parent):
        """
        Metodo: _init_coll_listCtrl1_Columns

        ARGUMENTOS:
                parent:
        """
        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='α 1', width=62)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='β 1', width=62)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='α 2', width=62)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT, heading='β 2', width=62)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT, heading='α 3', width=62)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_LEFT, heading='β 3', width=62)
        parent.InsertColumn(col=6, format=wx.LIST_FORMAT_LEFT, heading='α 4', width=62)
        parent.InsertColumn(col=7, format=wx.LIST_FORMAT_LEFT, heading='β 4', width=62)

    def __init__(self, parent, id, pos, size, style, name, prov):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
                id:
                pos:
                size:
                style:
                name:
                prov:
        """
        self.listaPuntos = []
        self.parent = parent
        self.provincia = prov
        self._init_ctrls(parent)

    def onPaint(self, event=None):
        """
        Metodo: onPaint

        ARGUMENTOS:
                event=None:
        """
        pintor = wx.PaintDC(self.panel1)
        pintor.Clear()
        if self.provincia in ('Las Palmas', 'Santa Cruz de Tenerife'):
            im = wx.Image(Directorio + '/Imagenes/cartaSolarCanarias.jpg', wx.BITMAP_TYPE_JPEG)
            bitmap = wx.BitmapFromImage(im)
            pintor.DrawBitmap(bitmap, 0, 0, False)
        else:
            im = wx.Image(Directorio + '/Imagenes/cartaSolarPeninsula.jpg', wx.BITMAP_TYPE_JPEG)
            bitmap = wx.BitmapFromImage(im)
            pintor.DrawBitmap(bitmap, 0, 0, False)
        boli = wx.Pen((0, 0, 0), 2, 1)
        pintor.SetPen(boli)
        for i in range(len(self.listaPuntos)):
            pintor.DrawLine(int(float(self.listaPuntos[i][0]) * 728 / 360) + 434, 348 - int(float(self.listaPuntos[i][1]) * 300 / 80), int(float(self.listaPuntos[i][2]) * 728 / 360) + 434, 348 - int(float(self.listaPuntos[i][3]) * 300 / 80))
            pintor.DrawLine(int(float(self.listaPuntos[i][2]) * 728 / 360) + 434, 348 - int(float(self.listaPuntos[i][3]) * 300 / 80), int(float(self.listaPuntos[i][4]) * 728 / 360) + 434, 348 - int(float(self.listaPuntos[i][5]) * 300 / 80))
            pintor.DrawLine(int(float(self.listaPuntos[i][4]) * 728 / 360) + 434, 348 - int(float(self.listaPuntos[i][5]) * 300 / 80), int(float(self.listaPuntos[i][6]) * 728 / 360) + 434, 348 - int(float(self.listaPuntos[i][7]) * 300 / 80))
            pintor.DrawLine(int(float(self.listaPuntos[i][6]) * 728 / 360) + 434, 348 - int(float(self.listaPuntos[i][7]) * 300 / 80), int(float(self.listaPuntos[i][0]) * 728 / 360) + 434, 348 - int(float(self.listaPuntos[i][1]) * 300 / 80))

    def comprobacionUtilizacionPatron(self, patronObjeto):
        """
        Metodo: comprobacionUtilizacionPatron

        ARGUMENTOS:
                patronObjeto:
        """
        utilizadoCerr = False
        utilizadoVent = False
        for cerr in self.parent.panelEnvolvente.cerramientos:
            if cerr[7] == patronObjeto:
                utilizadoCerr = True
                break

        for vent in self.parent.panelEnvolvente.ventanas:
            if vent.patronSombras == patronObjeto:
                utilizadoVent = True
                break

        return (
         utilizadoCerr, utilizadoVent)

    def actualizarNombreSombras(self, nombreNuevo, nombreAntiguo):
        """
        Metodo: actualizarNombreSombras

        ARGUMENTOS:
                nombreNuevo:
                nombreAntiguo:
        """
        for cerr in self.parent.panelEnvolvente.cerramientos:
            if (cerr[1] == 'Cubierta' or cerr[1] == 'Fachada') and cerr[-1] == 'aire':
                if cerr[7] == nombreAntiguo:
                    cerr[7] = nombreNuevo

        for vent in self.parent.panelEnvolvente.ventanas:
            if vent.patronSombras == nombreAntiguo:
                vent.patronSombras = nombreNuevo