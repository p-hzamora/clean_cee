# File: a (Python 2.7)

__doc__ = '\nModulo: ayudaReferenciasCatastrales.py\n\n\nModulo que contiene la clase Dialog1, que muestra la ventana de ayuda\n'
import wx
import LibreriasPython.ultimatelistctrl as ULC

def create(parent):
    '''
    Metodo: create
    devuelve una instancia de la clase Dialog1()
    
    ARGUMENTOS:
\t\tparent:
    
    '''
    return Dialog1(parent)

continue
(wxID_DIALOG1, wxID_DIALOG1ACEPTAR, wxID_DIALOG1STATICTEXT1, wxID_DIALOG1ANADIR, wx_subdialog_aceptar, wx_subdialog_cancelar) = [ wx.NewId() for _init_ctrls in range(6) ]

class Dialog1(wx.Dialog):
    '''
    Clase: Dialog1 del modulo ayudaDatosGenerales.py

    Ventana de ayuda para saber la normativa vigente en el a\xf1o de construcii\xf3n del edificio
    '''
    
    def __init__(self, parent, listadoRefCat = []):
        '''
        Constructor de la clase


        ARGUMENTOS:
            parent:
            annoConstr:

        '''
        self.listadoRefCat = listadoRefCat
        self.parent = parent
        self._init_ctrls()

    
    def _init_ctrls(self):
        '''
        Metodo: _init_ctrls
        Iniciaci\xf3n de elementos gr\xe1ficos. LLamado desde __init__
        '''
        wx.Dialog.__init__(self, id = wxID_DIALOG1, name = '', parent = self.parent, pos = wx.Point(428, 302), size = wx.Size(515, 300), style = wx.DEFAULT_DIALOG_STYLE, title = _(u'Listado de referencias catastrales del inmueble'))
        self.SetClientSize(wx.Size(515, 300))
        self.SetBackgroundColour('white')
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add((-1, 10))
        self.staticText1 = wx.StaticText(id = wxID_DIALOG1STATICTEXT1, label = _(u'Listado referencias catastrales del inmueble'), name = 'datosGeneralesText', parent = self, pos = wx.Point(15, 30), size = wx.Size(250, 21), style = 0)
        self.staticText1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticText1.SetForegroundColour(wx.Colour(0, 64, 128))
        self.vbox.Add(self.staticText1, flag = wx.LEFT, border = 25)
        self.vbox.Add((-1, 10))
        self.list_ctrl = ULC.UltimateListCtrl(self, -1, pos = wx.Point(25, 50), size = wx.Size(465, 150), agwStyle = ULC.ULC_REPORT | ULC.ULC_HAS_VARIABLE_ROW_HEIGHT | ULC.ULC_HRULES | ULC.ULC_BORDER_SELECT)
        titulo = ULC.UltimateListItem()
        titulo._format = wx.LIST_FORMAT_LEFT
        titulo._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT | ULC.ULC_MASK_FONT
        titulo._image = []
        titulo._text = u''
        self.list_ctrl.InsertColumnInfo(0, titulo)
        titulo = ULC.UltimateListItem()
        titulo._format = wx.LIST_FORMAT_LEFT
        titulo._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT | ULC.ULC_MASK_FONT
        titulo._image = []
        titulo._text = _(u'Referencia catastral')
        self.list_ctrl.InsertColumnInfo(1, titulo)
        titulo = ULC.UltimateListItem()
        titulo._format = wx.LIST_FORMAT_CENTRE
        titulo._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT | ULC.ULC_MASK_FONT
        titulo._image = []
        titulo._text = u''
        self.list_ctrl.InsertColumnInfo(2, titulo)
        titulo = ULC.UltimateListItem()
        titulo._format = wx.LIST_FORMAT_CENTRE
        titulo._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT | ULC.ULC_MASK_FONT
        titulo._image = []
        titulo._text = u''
        self.list_ctrl.InsertColumnInfo(3, titulo)
        self.list_ctrl.SetColumnWidth(0, 20)
        self.list_ctrl.SetColumnWidth(1, 280)
        self.list_ctrl.SetColumnWidth(2, 80)
        self.list_ctrl.SetColumnWidth(3, 80)
        self.vbox.Add(self.list_ctrl, proportion = 1, flag = wx.LEFT | wx.RIGHT | wx.EXPAND, border = 25)
        self.vbox.Add((-1, 10))
        self.anadir = wx.Button(id = wxID_DIALOG1ANADIR, label = _(u'A\xc3\xb1adir nueva'), name = u'anadir', parent = self, pos = wx.Point(410, 210), size = wx.Size(75, 23), style = 0)
        self.anadir.Bind(wx.EVT_BUTTON, self.onAnadirButton, id = wxID_DIALOG1ANADIR)
        self.anadir.SetToolTip(wx.ToolTip(_(u'A\xc3\xb1adir nueva referencia catastral a la lista.')))
        self.vbox.Add(self.anadir, flag = wx.LEFT, border = 410)
        self.vbox.Add((-1, 10))
        self.aceptar = wx.Button(id = wxID_DIALOG1ACEPTAR, label = _(u'Aceptar'), name = u'aceptar', parent = self, pos = wx.Point(410, 260), size = wx.Size(75, 23), style = 0)
        self.aceptar.Bind(wx.EVT_BUTTON, self.onAceptarButton, id = wxID_DIALOG1ACEPTAR)
        self.aceptar.SetToolTip(wx.ToolTip(_(u'Salir de la pantalla de configuraci\xc3\xb3n de las referencias catastrales.')))
        self.vbox.Add(self.aceptar, flag = wx.LEFT, border = 410)
        self.vbox.Add((-1, 10))
        self.cargarDatos()
        self.SetSizer(self.vbox)

    
    def cargarDatos(self):
        '''
        Metodo: cargarDatos


        ARGUMENTOS:
            datos:
        '''
        self.list_ctrl.DeleteAllItems()
        for i in range(0, len(self.listadoRefCat)):
            fila = self.list_ctrl.InsertStringItem(i, str(i + 1))
            self.list_ctrl.SetStringItem(fila, 1, self.listadoRefCat[i])
            buttonEditar = wx.Button(id = i, label = _(u'Editar'), name = u'buttonEditar', parent = self.list_ctrl)
            buttonEditar.Bind(wx.EVT_BUTTON, self.onButtonEditar)
            buttonEditar.SetToolTip(wx.ToolTip(_(u'Modificar la referencia catastral definida.')))
            self.list_ctrl.SetItemWindow(fila, col = 2, wnd = buttonEditar, expand = False)
            buttonEliminar = wx.Button(id = i + 10000, label = _(u'Eliminar'), name = u'buttonEliminar', parent = self.list_ctrl)
            buttonEliminar.Bind(wx.EVT_BUTTON, self.onButtonEliminar)
            buttonEliminar.SetToolTip(wx.ToolTip(_(u'Eliminar la referencia catastral definida.')))
            self.list_ctrl.SetItemWindow(fila, col = 3, wnd = buttonEliminar, expand = False)
        

    
    def onButtonEditar(self, event):
        posSelect = event.Id
        subDialog = SubDialog(self, referencia = self.listadoRefCat[posSelect])
        subDialog.ShowModal()
        if subDialog.referencia != '':
            self.listadoRefCat[posSelect] = subDialog.referencia
            self.cargarDatos()
            self.Refresh()

    
    def onButtonEliminar(self, event):
        posSelect = event.Id - 10000
        self.listadoRefCat.pop(posSelect)
        self.cargarDatos()
        self.Destroy()
        self.parent.onReferenciaCatastralButton(None)

    
    def onAceptarButton(self, event):
        '''
        Metodo: onAceptarButton
        Evento que gestiona la accion de que el usuario presione el boton aceptar

        ARGUMENTOS:
    \t\tevent:

        
        '''
        self.parent.listadoRefCat = self.listadoRefCat
        self.Close()

    
    def onAnadirButton(self, event):
        subDialog = SubDialog(self, referencia = '')
        subDialog.ShowModal()
        if subDialog.referencia != '':
            self.listadoRefCat.append(subDialog.referencia)
            self.cargarDatos()
            self.Refresh()



class SubDialog(wx.Dialog):
    '''
    Clase: SubDialog del modulo ayudaDatosCatastrales.py

    Ventana para definir una nueva referencia catastral o editarla 
    '''
    
    def __init__(self, parent, referencia = ''):
        self.referencia = referencia
        self.parent = parent
        self._init_ctrls()

    
    def _init_ctrls(self):
        '''
        Metodo: _init_ctrls
        Iniciaci\xf3n de elementos gr\xe1ficos. LLamado desde __init__
        '''
        wx.Dialog.__init__(self, id = -1, name = '', parent = self.parent, pos = wx.Point(428, 302), size = wx.Size(315, 100), style = wx.DEFAULT_DIALOG_STYLE, title = _(u'Definir referencia catastral'))
        self.SetClientSize(wx.Size(315, 100))
        self.SetBackgroundColour('white')
        self.referenciaText = wx.StaticText(id = -1, label = _(u'Referencia catastral'), name = u'referenciaText', parent = self, pos = wx.Point(15, 30), size = wx.Size(100, 13), style = 0)
        self.referenciaCuadro = wx.TextCtrl(id = -1, name = u'referenciaCuadro', parent = self, pos = wx.Point(130, 26), size = wx.Size(160, 21), style = 0, value = u'')
        self.referenciaCuadro.SetToolTip(wx.ToolTip(_(u'Definir referencia catastral del inmueble.')))
        self.aceptar = wx.Button(id = wx_subdialog_aceptar, label = _(u'Aceptar'), name = u'aceptar', parent = self, pos = wx.Point(125, 65), size = wx.Size(75, 23), style = 0)
        self.aceptar.Bind(wx.EVT_BUTTON, self.onAceptarButton, id = wx_subdialog_aceptar)
        self.aceptar.SetToolTip(wx.ToolTip(_(u'Guardar cambios en referencia catastral y salir de la pantalla de edici\xc3\xb3n.')))
        self.cancelar = wx.Button(id = wx_subdialog_cancelar, label = _(u'Cancelar'), name = u'cancelar', parent = self, pos = wx.Point(215, 65), size = wx.Size(75, 23), style = 0)
        self.cancelar.Bind(wx.EVT_BUTTON, self.onCancelarButton, id = wx_subdialog_cancelar)
        self.cancelar.SetToolTip(wx.ToolTip(_(u'No guardar cambios en referencia catastral y salir de la pantalla de edici\xc3\xb3n.')))
        self.cargarDatos()

    
    def cargarDatos(self):
        self.referenciaCuadro.SetValue(self.referencia)

    
    def onAceptarButton(self, event):
        self.referencia = self.referenciaCuadro.GetValue()
        if self.referencia == '':
            wx.MessageBox(_(u'No se ha indicado una referencia catastral v\xc3\xa1lida'), _(u'Aviso'))
        else:
            self.Close()

    
    def onCancelarButton(self, event):
        self.referencia = ''
        self.Close()


