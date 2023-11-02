# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\absortividad_cuadro.pyc
# Compiled at: 2014-02-25 15:39:24
"""
Modulo: absortividad_cuadro.py

"""
import wx

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return Dialog1(parent)


wxID_DIALOG1, wxID_DIALOG1STATICTEXT1, wxID_COLOR, wxID_CLARO, wxID_MEDIO, wxID_OSCURO, wxID_BLANCO, wxID_BLANCO1, wxID_BLANCO2, wxID_BLANCO3, wxID_AMARILLO, wxID_AMARILLO1, wxID_AMARILLO2, wxID_AMARILLO3, wxID_BEIGE, wxID_BEIGE1, wxID_BEIGE2, wxID_BEIGE3, wxID_MARRON, wxID_MARRON1, wxID_MARRON2, wxID_MARRON3, wxID_ROJO, wxID_ROJO1, wxID_ROJO2, wxID_ROJO3, wxID_VERDE, wxID_VERDE1, wxID_VERDE2, wxID_VERDE3, wxID_AZUL, wxID_AZUL1, wxID_AZUL2, wxID_AZUL3, wxID_GRIS, wxID_GRIS1, wxID_GRIS2, wxID_GRIS3, wxID_NEGRO, wxID_NEGRO1, wxID_NEGRO2, wxID_NEGRO3, wxID_WXELTOSSOMBRASACEPTAR = [ wx.NewId() for _init_ctrls in range(43) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo absortividad_cuadro.py

    """

    def _init_ctrls(self, prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(465, 202), size=wx.Size(345, 365), style=wx.DEFAULT_DIALOG_STYLE, title=_('Absortividad Marco'))
        self.SetClientSize(wx.Size(345, 365))
        self.SetBackgroundColour('white')
        self.parent = prnt
        self.staticText1 = wx.StaticBox(id=wxID_DIALOG1STATICTEXT1, label=_('Absortividad del marco para radiación solar α'), name='datosGeneralesText', parent=self, pos=wx.Point(15, 30), size=wx.Size(315, 290), style=0)
        self.staticText1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, ''))
        self.staticText1.SetForegroundColour(wx.Colour(0, 64, 128))
        Blanco1 = 0.2
        Blanco2 = 0.3
        Amarillo1 = 0.3
        Amarillo2 = 0.5
        Amarillo3 = 0.7
        Beige1 = 0.35
        Beige2 = 0.55
        Beige3 = 0.75
        Marron1 = 0.5
        Marron2 = 0.75
        Marron3 = 0.92
        Rojo1 = 0.65
        Rojo2 = 0.8
        Rojo3 = 0.9
        Verde1 = 0.4
        Verde2 = 0.7
        Verde3 = 0.88
        Azul1 = 0.5
        Azul2 = 0.8
        Azul3 = 0.95
        Gris1 = 0.4
        Gris2 = 0.65
        Negro2 = 0.96
        self.matriz_absortividad_valores = [
         [
          Blanco1, Blanco2],
         [
          Amarillo1, Amarillo2, Amarillo3],
         [
          Beige1, Beige2, Beige3],
         [
          Marron1, Marron2, Marron3],
         [
          Rojo1, Rojo2, Rojo3],
         [
          Verde1, Verde2, Verde3],
         [
          Azul1, Azul2, Azul3],
         [
          Gris1, Gris2, ''],
         [
          '', Negro2, '']]
        contador_fila = self.parent.contador_fila_absortividad
        contador_col = self.parent.contador_col_absortividad
        matriz_absortividad_activos = [
         [
          False, False, False],
         [
          False, False, False],
         [
          False, False, False],
         [
          False, False, False],
         [
          False, False, False],
         [
          False, False, False],
         [
          False, False, False],
         [
          False, False, False],
         [
          False, False, False]]
        matriz_absortividad_activos[contador_fila][contador_col] = True
        Blanco1_activo = matriz_absortividad_activos[0][0]
        Blanco2_activo = matriz_absortividad_activos[0][1]
        Amarillo1_activo = matriz_absortividad_activos[1][0]
        Amarillo2_activo = matriz_absortividad_activos[1][1]
        Amarillo3_activo = matriz_absortividad_activos[1][2]
        Beige1_activo = matriz_absortividad_activos[2][0]
        Beige2_activo = matriz_absortividad_activos[2][1]
        Beige3_activo = matriz_absortividad_activos[2][2]
        Marron1_activo = matriz_absortividad_activos[3][0]
        Marron2_activo = matriz_absortividad_activos[3][1]
        Marron3_activo = matriz_absortividad_activos[3][2]
        Rojo1_activo = matriz_absortividad_activos[4][0]
        Rojo2_activo = matriz_absortividad_activos[4][1]
        Rojo3_activo = matriz_absortividad_activos[4][2]
        Verde1_activo = matriz_absortividad_activos[5][0]
        Verde2_activo = matriz_absortividad_activos[5][1]
        Verde3_activo = matriz_absortividad_activos[5][2]
        Azul1_activo = matriz_absortividad_activos[6][0]
        Azul2_activo = matriz_absortividad_activos[6][1]
        Azul3_activo = matriz_absortividad_activos[6][2]
        Gris1_activo = matriz_absortividad_activos[7][0]
        Gris2_activo = matriz_absortividad_activos[7][1]
        Negro2_activo = matriz_absortividad_activos[8][1]
        self.Color = wx.StaticText(id=wxID_COLOR, label=_('Color'), name=_('Color'), parent=self, pos=wx.Point(30, 60), size=wx.Size(60, 75), style=0)
        self.Color.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Color.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.Claro = wx.StaticText(id=wxID_CLARO, label=_('Claro'), name=_('Claro'), parent=self, pos=wx.Point(105, 60), size=wx.Size(60, 75), style=0)
        self.Claro.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Claro.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.Medio = wx.StaticText(id=wxID_MEDIO, label=_('Medio'), name=_('Medio'), parent=self, pos=wx.Point(180, 60), size=wx.Size(60, 75), style=0)
        self.Medio.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Medio.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.Oscuro = wx.StaticText(id=wxID_OSCURO, label=_('Oscuro'), name=_('Oscuro'), parent=self, pos=wx.Point(255, 60), size=wx.Size(60, 75), style=0)
        self.Oscuro.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Oscuro.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.Blanco = wx.StaticText(id=wxID_BLANCO, label=_('Blanco'), name=_('Blanco'), parent=self, pos=wx.Point(30, 85), size=wx.Size(60, 75), style=0)
        self.Blanco.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Blanco.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.Blanco1 = wx.RadioButton(id=wxID_BLANCO1, label=str(Blanco1), name='Blanco1', parent=self, pos=wx.Point(105, 85), size=wx.Size(50, 13), style=wx.RB_GROUP)
        self.Blanco1.SetValue(Blanco1_activo)
        self.Blanco2 = wx.RadioButton(id=wxID_BLANCO2, label=str(Blanco2), name='Blanco2', parent=self, pos=wx.Point(180, 85), size=wx.Size(50, 13), style=0)
        self.Blanco2.SetValue(Blanco2_activo)
        self.Blanco3 = wx.StaticText(id=wxID_BLANCO3, label=_('    ---'), name='Blanco3', parent=self, pos=wx.Point(255, 85), size=wx.Size(50, 13), style=0)
        self.Amarillo = wx.StaticText(id=wxID_AMARILLO, label=_('Amarillo'), name=_('Amarillo'), parent=self, pos=wx.Point(30, 110), size=wx.Size(60, 75), style=0)
        self.Amarillo.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Amarillo.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.Amarillo1 = wx.RadioButton(id=wxID_AMARILLO1, label=str(Amarillo1), name='Amarillo1', parent=self, pos=wx.Point(105, 110), size=wx.Size(50, 13), style=0)
        self.Amarillo1.SetValue(Amarillo1_activo)
        self.Amarillo2 = wx.RadioButton(id=wxID_AMARILLO2, label=str(Amarillo2), name='Amarillo2', parent=self, pos=wx.Point(180, 110), size=wx.Size(50, 13), style=0)
        self.Amarillo2.SetValue(Amarillo2_activo)
        self.Amarillo3 = wx.RadioButton(id=wxID_AMARILLO3, label=str(Amarillo3), name='Amarillo3', parent=self, pos=wx.Point(255, 110), size=wx.Size(50, 13), style=0)
        self.Amarillo3.SetValue(Amarillo3_activo)
        self.Beige = wx.StaticText(id=wxID_BEIGE, label=_('Beige'), name=_('Beige'), parent=self, pos=wx.Point(30, 135), size=wx.Size(60, 75), style=0)
        self.Beige.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Beige.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.Beige1 = wx.RadioButton(id=wxID_BEIGE1, label=str(Beige1), name='Beige1', parent=self, pos=wx.Point(105, 135), size=wx.Size(50, 13), style=0)
        self.Beige1.SetValue(Beige1_activo)
        self.Beige2 = wx.RadioButton(id=wxID_BEIGE2, label=str(Beige2), name='Beige2', parent=self, pos=wx.Point(180, 135), size=wx.Size(50, 13), style=0)
        self.Beige2.SetValue(Beige2_activo)
        self.Beige3 = wx.RadioButton(id=wxID_BEIGE3, label=str(Beige3), name='Beige3', parent=self, pos=wx.Point(255, 135), size=wx.Size(50, 13), style=0)
        self.Beige3.SetValue(Beige3_activo)
        self.Marron = wx.StaticText(id=wxID_MARRON, label=_('Marron'), name=_('Marron'), parent=self, pos=wx.Point(30, 160), size=wx.Size(60, 75), style=0)
        self.Marron.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Marron.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.Marron1 = wx.RadioButton(id=wxID_MARRON1, label=str(Marron1), name='Marron1', parent=self, pos=wx.Point(105, 160), size=wx.Size(50, 13), style=0)
        self.Marron1.SetValue(Marron1_activo)
        self.Marron2 = wx.RadioButton(id=wxID_MARRON2, label=str(Marron2), name='Marron2', parent=self, pos=wx.Point(180, 160), size=wx.Size(50, 13), style=0)
        self.Marron2.SetValue(Marron2_activo)
        self.Marron3 = wx.RadioButton(id=wxID_MARRON3, label=str(Marron3), name='Marron3', parent=self, pos=wx.Point(255, 160), size=wx.Size(50, 13), style=0)
        self.Marron3.SetValue(Marron3_activo)
        self.Rojo = wx.StaticText(id=wxID_ROJO, label=_('Rojo'), name=_('Rojo'), parent=self, pos=wx.Point(30, 185), size=wx.Size(60, 75), style=0)
        self.Rojo.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Rojo.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.Rojo1 = wx.RadioButton(id=wxID_ROJO1, label=str(Rojo1), name='Rojo1', parent=self, pos=wx.Point(105, 185), size=wx.Size(50, 13), style=0)
        self.Rojo1.SetValue(Rojo1_activo)
        self.Rojo2 = wx.RadioButton(id=wxID_ROJO2, label=str(Rojo2), name='Rojo2', parent=self, pos=wx.Point(180, 185), size=wx.Size(50, 13), style=0)
        self.Rojo2.SetValue(Rojo2_activo)
        self.Rojo3 = wx.RadioButton(id=wxID_ROJO3, label=str(Rojo3), name='Rojo3', parent=self, pos=wx.Point(255, 185), size=wx.Size(50, 13), style=0)
        self.Rojo3.SetValue(Rojo3_activo)
        self.Verde = wx.StaticText(id=wxID_VERDE, label=_('Verde'), name=_('Verde'), parent=self, pos=wx.Point(30, 210), size=wx.Size(60, 75), style=0)
        self.Verde.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Verde.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.Verde1 = wx.RadioButton(id=wxID_VERDE1, label=str(Verde1), name='Verde1', parent=self, pos=wx.Point(105, 210), size=wx.Size(50, 13), style=0)
        self.Verde1.SetValue(Verde1_activo)
        self.Verde2 = wx.RadioButton(id=wxID_VERDE2, label=str(Verde2), name='Verde2', parent=self, pos=wx.Point(180, 210), size=wx.Size(50, 13), style=0)
        self.Verde2.SetValue(Verde2_activo)
        self.Verde3 = wx.RadioButton(id=wxID_VERDE3, label=str(Verde3), name='Verde3', parent=self, pos=wx.Point(255, 210), size=wx.Size(50, 13), style=0)
        self.Verde3.SetValue(Verde3_activo)
        self.Azul = wx.StaticText(id=wxID_AZUL, label=_('Azul'), name=_('Azul'), parent=self, pos=wx.Point(30, 235), size=wx.Size(60, 75), style=0)
        self.Azul.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Azul.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.Azul1 = wx.RadioButton(id=wxID_AZUL1, label=str(Azul1), name='Azul1', parent=self, pos=wx.Point(105, 235), size=wx.Size(50, 13), style=0)
        self.Azul1.SetValue(Azul1_activo)
        self.Azul2 = wx.RadioButton(id=wxID_AZUL2, label=str(Azul2), name='Azul2', parent=self, pos=wx.Point(180, 235), size=wx.Size(50, 13), style=0)
        self.Azul2.SetValue(Azul2_activo)
        self.Azul3 = wx.RadioButton(id=wxID_AZUL3, label=str(Azul3), name='Azul3', parent=self, pos=wx.Point(255, 235), size=wx.Size(50, 13), style=0)
        self.Azul3.SetValue(Azul3_activo)
        self.Gris = wx.StaticText(id=wxID_GRIS, label=_('Gris'), name=_('Gris'), parent=self, pos=wx.Point(30, 260), size=wx.Size(60, 75), style=0)
        self.Gris.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Gris.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.Gris1 = wx.RadioButton(id=wxID_GRIS1, label=str(Gris1), name='Gris1', parent=self, pos=wx.Point(105, 260), size=wx.Size(50, 13), style=0)
        self.Gris1.SetValue(Gris1_activo)
        self.Gris2 = wx.RadioButton(id=wxID_GRIS2, label=str(Gris2), name='Gris2', parent=self, pos=wx.Point(180, 260), size=wx.Size(50, 13), style=0)
        self.Gris2.SetValue(Gris2_activo)
        self.Gris3 = wx.StaticText(id=wxID_GRIS3, label=_('    ---'), name='Gris3', parent=self, pos=wx.Point(255, 260), size=wx.Size(50, 13), style=0)
        self.Negro = wx.StaticText(id=wxID_NEGRO, label=_('Negro'), name=_('Negro'), parent=self, pos=wx.Point(30, 285), size=wx.Size(60, 75), style=0)
        self.Negro.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.Negro.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Tahoma'))
        self.Negro1 = wx.StaticText(id=wxID_NEGRO1, label=_('    ---'), name='Negro1', parent=self, pos=wx.Point(105, 285), size=wx.Size(50, 13), style=0)
        self.Negro2 = wx.RadioButton(id=wxID_NEGRO2, label=str(Negro2), name='Negro2', parent=self, pos=wx.Point(180, 285), size=wx.Size(50, 13), style=0)
        self.Negro2.SetValue(Negro2_activo)
        self.Negro3 = wx.StaticText(id=wxID_NEGRO3, label=_('    ---'), name='Negro3', parent=self, pos=wx.Point(255, 285), size=wx.Size(50, 13), style=0)
        self.aceptar = wx.Button(id=wxID_WXELTOSSOMBRASACEPTAR, label=_('Aceptar'), name='aceptar', parent=self, pos=wx.Point(15, 335), size=wx.Size(75, 23), style=0)
        self.aceptar.Bind(wx.EVT_BUTTON, self.OnAceptarButton, id=wxID_WXELTOSSOMBRASACEPTAR)
        self.Blanco1.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Blanco2.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Amarillo1.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Amarillo2.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Amarillo3.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Beige1.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Beige2.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Beige3.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Marron1.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Marron2.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Marron3.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Rojo1.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Rojo2.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Rojo3.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Verde1.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Verde2.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Verde3.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Azul1.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Azul2.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Azul3.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Gris1.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Gris2.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))
        self.Negro2.SetToolTip(wx.ToolTip(_('Tabla E.10 del CTE-HE')))

    def OnAceptarButton(self, event):
        """
        Metodo: OnAceptarButton

        ARGUMENTOS:
                event:
        """
        contador_fila = ''
        contador_col = ''
        if self.Blanco1.GetValue() == True:
            contador_fila = 0
            contador_col = 0
        elif self.Blanco2.GetValue() == True:
            contador_fila = 0
            contador_col = 1
        elif self.Amarillo1.GetValue() == True:
            contador_fila = 1
            contador_col = 0
        elif self.Amarillo2.GetValue() == True:
            contador_fila = 1
            contador_col = 1
        elif self.Amarillo3.GetValue() == True:
            contador_fila = 1
            contador_col = 2
        elif self.Beige1.GetValue() == True:
            contador_fila = 2
            contador_col = 0
        elif self.Beige2.GetValue() == True:
            contador_fila = 2
            contador_col = 1
        elif self.Beige3.GetValue() == True:
            contador_fila = 2
            contador_col = 2
        elif self.Marron1.GetValue() == True:
            contador_fila = 3
            contador_col = 0
        elif self.Marron2.GetValue() == True:
            contador_fila = 3
            contador_col = 1
        elif self.Marron3.GetValue() == True:
            contador_fila = 3
            contador_col = 2
        elif self.Rojo1.GetValue() == True:
            contador_fila = 4
            contador_col = 0
        elif self.Rojo2.GetValue() == True:
            contador_fila = 4
            contador_col = 1
        elif self.Rojo3.GetValue() == True:
            contador_fila = 4
            contador_col = 2
        elif self.Verde1.GetValue() == True:
            contador_fila = 5
            contador_col = 0
        elif self.Verde2.GetValue() == True:
            contador_fila = 5
            contador_col = 1
        elif self.Verde3.GetValue() == True:
            contador_fila = 5
            contador_col = 2
        elif self.Azul1.GetValue() == True:
            contador_fila = 6
            contador_col = 0
        elif self.Azul2.GetValue() == True:
            contador_fila = 6
            contador_col = 1
        elif self.Azul3.GetValue() == True:
            contador_fila = 6
            contador_col = 2
        elif self.Gris1.GetValue() == True:
            contador_fila = 7
            contador_col = 0
        elif self.Gris2.GetValue() == True:
            contador_fila = 7
            contador_col = 1
        elif self.Negro2.GetValue() == True:
            contador_fila = 8
            contador_col = 1
        self.dev = self.matriz_absortividad_valores[contador_fila][contador_col]
        self.parent.contador_fila_absortividad = contador_fila
        self.parent.contador_col_absortividad = contador_col
        self.Close()

    def __init__(self, parent):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
        """
        self.parent = parent
        self._init_ctrls(parent)
        self.dev = False