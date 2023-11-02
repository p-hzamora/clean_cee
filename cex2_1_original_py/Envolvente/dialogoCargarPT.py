# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\dialogoCargarPT.pyc
# Compiled at: 2014-02-18 15:21:02
"""
Modulo: dialogoCargarPT.py

"""
import wx

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return Dialog1(parent)


wxID_DIALOG1, wxID_DIALOG1ACEPTARBOTON, wxID_DIALOG1CANCELARBOTON, wxID_DIALOG1CARGARCERRAMIENTOSRADIOBUTTON, wxID_DIALOG1CARGARFINOMODIFICADARADIOBUTTON, wxID_DIALOG1CARGARTODOS, wxID_DIALOG1QUEDESEATEXT = [ wx.NewId() for _init_ctrls in range(7) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo dialogoCargarPT.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(402, 199), size=wx.Size(700, 332), style=wx.DEFAULT_DIALOG_STYLE, title=_('Opciones cargar puentes térmicos por defecto'))
        self.SetClientSize(wx.Size(700, 332))
        self.SetBackgroundColour('white')
        self.queDeseaText = wx.StaticText(id=wxID_DIALOG1QUEDESEATEXT, label=_('¿Qué desea hacer?'), name='queDeseaText', parent=self, pos=wx.Point(40, 24), size=wx.Size(92, 13), style=0)
        self.queDeseaText.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.cargarTodosPTRadioButton = wx.RadioButton(id=wxID_DIALOG1CARGARTODOS, label=_('Cargar los puentes térmicos por defecto de nuevo'), name='cargarTodosPTRadioButton', parent=self, pos=wx.Point(80, 72), size=wx.Size(600, 13), style=0)
        self.cargarTodosPTRadioButton.SetValue(True)
        self.CargarFiNoModificadaRadioButton = wx.RadioButton(id=wxID_DIALOG1CARGARFINOMODIFICADARADIOBUTTON, label=_('Recargar valores de φ en puentes térmicos por defecto cuyo valor no ha sido modificado por el usuario'), name='CargarFiNoModificadaRadioButton', parent=self, pos=wx.Point(80, 128), size=wx.Size(600, 13), style=0)
        self.CargarFiNoModificadaRadioButton.SetValue(False)
        self.cargarCerramientosRadioButton = wx.RadioButton(id=wxID_DIALOG1CARGARCERRAMIENTOSRADIOBUTTON, label=_('Cargar los puentes térmicos por defecto en cerramientos que no tengan puentes térmicos por defecto definidos'), name='cargarCerramientosRadioButton', parent=self, pos=wx.Point(80, 184), size=wx.Size(600, 13), style=0)
        self.cargarCerramientosRadioButton.SetValue(False)
        self.aceptarBoton = wx.Button(id=wxID_DIALOG1ACEPTARBOTON, label=_('Aceptar'), name='aceptarBoton', parent=self, pos=wx.Point(228, 248), size=wx.Size(88, 23), style=0)
        self.aceptarBoton.Bind(wx.EVT_BUTTON, self.OnAceptarButton, id=wxID_DIALOG1ACEPTARBOTON)
        self.cancelarBoton = wx.Button(id=wxID_DIALOG1CANCELARBOTON, label=_('Cancelar'), name='cancelarBoton', parent=self, pos=wx.Point(412, 248), size=wx.Size(91, 23), style=0)
        self.cancelarBoton.Bind(wx.EVT_BUTTON, self.OnCancelarButton, id=wxID_DIALOG1CANCELARBOTON)
        self.cargarTodosPTRadioButton.SetToolTip(wx.ToolTip(_('Borra y vuelve a cargar todos los puentes térmicos que fueron definidos por defecto.\n Se perderá cualquier modificación que el usuario haya podido realizar sobre los puentes térmicos \n definidos por defecto previamente. Los puentes térmicos definidos manualmente no se modifican.')))
        self.CargarFiNoModificadaRadioButton.SetToolTip(wx.ToolTip(_('Borra y vuelve a cargar los puentes térmicos que fueron definidos por defecto y que el usuario no ha modificado.\n Los puentes térmicos que fueron definidos por defecto y cuyas características  \n han sido modificados por el usuario se mantienen.')))
        self.cargarCerramientosRadioButton.SetToolTip(wx.ToolTip(_('Se cargan los puentes térmicos, sólo en los cerramientos que no tienen puentes térmicos por defecto.')))

    def __init__(self, parent):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
        """
        self._init_ctrls(parent)
        self.dev = False

    def OnAceptarButton(self, event):
        """
        Metodo: OnAceptarButton

        ARGUMENTOS:
                event:
        """
        opcion1 = self.cargarTodosPTRadioButton.GetValue()
        opcion2 = self.CargarFiNoModificadaRadioButton.GetValue()
        opcion3 = self.cargarCerramientosRadioButton.GetValue()
        self.dev = [
         opcion1, opcion2, opcion3]
        self.Close()

    def OnCancelarButton(self, event):
        """
        Metodo: OnCancelarButton

        ARGUMENTOS:
                event:
        """
        self.dev = False
        self.Close()