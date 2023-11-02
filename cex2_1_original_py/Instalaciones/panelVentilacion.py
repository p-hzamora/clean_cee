# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\panelVentilacion.pyc
# Compiled at: 2015-02-19 13:18:33
"""
Modulo: panelVentilacion.py

"""
from Instalaciones.comprobarCampos import Comprueba
from miChoice import MiChoice
import wx, logging
wxID_PANEL1, wxID_PANEL1EQUIPOVENTILACION, wxID_PANEL1EQUIPOVENTILACIONTEXT, wxID_PANEL1EQUIPOVENTILACIONUNIDADESTEXT, wxID_PANEL1NOMBREINSTALACION, wxID_PANEL1NOMBREINSTALACIONTEXT, wxID_PANEL1RECUPERADORCHECK, wxID_PANEL1RENDIMIENTO, wxID_PANEL1RENDIMIENTOTEXT, wxID_PANEL1RENDIMIENTOUNIDADESTEXT, wxID_PANEL1SUBGRUPOCHOICE, wxID_PANEL1SUBGRUPOTEXT, wxID_CARACTERISTICASLINEATEXT = [ wx.NewId() for _init_ctrls in range(13) ]

class Panel1(wx.Panel):
    """
    Clase: Panel1 del modulo panelVentilacion.py

    """

    def _init_ctrls(self, prnt, id, posi, siz, styles, named):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
                id:
                 posi:
                 siz:
                 styles:
                 named:
        """
        wx.Panel.__init__(self, id=id, name=named, parent=prnt, pos=posi, size=siz, style=styles)
        self.SetBackgroundColour('white')
        self.nombreInstalacionText = wx.StaticText(id=wxID_PANEL1NOMBREINSTALACIONTEXT, label=_('Nombre'), name='nombreInstalacionText', parent=self, pos=wx.Point(15, 2), size=wx.Size(102, 13), style=0)
        self.nombreInstalacion = wx.TextCtrl(id=wxID_PANEL1NOMBREINSTALACION, name='nombreInstalacion', parent=self, pos=wx.Point(170, 0), size=wx.Size(230, 21), style=0, value=_('Aire primario'))
        self.nombreInstalacion.SetForegroundColour(wx.Colour(100, 200, 0))
        self.nombreInstalacion.Bind(wx.EVT_TEXT, self.OnNombreInstalacion, id=wxID_PANEL1NOMBREINSTALACION)
        self.subgrupoText = wx.StaticText(id=wxID_PANEL1SUBGRUPOTEXT, label=_('Zona'), name='subgrupoText', parent=self, pos=wx.Point(435, 2), size=wx.Size(50, 13), style=0)
        self.subgrupoChoice = MiChoice(choices=[], id=wxID_PANEL1SUBGRUPOCHOICE, name='subgrupoChoice', parent=self, pos=wx.Point(496, 0), size=wx.Size(214, 21), style=0)
        self.CaracteristicasLineaText = wx.StaticBox(id=wxID_CARACTERISTICASLINEATEXT, label=_('Características'), name='CaracteristicasLineaText', parent=self, pos=wx.Point(0, 26), size=wx.Size(710, 108), style=0)
        self.CaracteristicasLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.CaracteristicasLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.equipoVentilacionText = wx.StaticText(id=wxID_PANEL1EQUIPOVENTILACIONTEXT, label=_('Caudal de ventilación'), name='equipoVentilacionText', parent=self, pos=wx.Point(15, 46), size=wx.Size(150, 13), style=0)
        self.equipoVentilacion = wx.TextCtrl(id=wxID_PANEL1EQUIPOVENTILACION, name='equipoVentilacion', parent=self, pos=wx.Point(170, 44), size=wx.Size(60, 21), style=0, value='')
        self.equipoVentilacionUnidadesText = wx.StaticText(id=wxID_PANEL1EQUIPOVENTILACIONUNIDADESTEXT, label=_('m3/h'), name='equipoVentilacionUnidadesText', parent=self, pos=wx.Point(235, 46), size=wx.Size(24, 13), style=0)
        self.recuperadorCheck = wx.CheckBox(id=wxID_PANEL1RECUPERADORCHECK, label=_('¿Tiene recuperador de calor?'), name='recuperadorCheck', parent=self, pos=wx.Point(15, 76), size=wx.Size(168, 13), style=0)
        self.recuperadorCheck.SetValue(False)
        self.recuperadorCheck.Bind(wx.EVT_CHECKBOX, self.OnRecuperadorCheck, id=wxID_PANEL1RECUPERADORCHECK)
        self.rendimientoText = wx.StaticText(id=wxID_PANEL1RENDIMIENTOTEXT, label=_('Rendimiento estacional'), name='rendimientoText', parent=self, pos=wx.Point(15, 106), size=wx.Size(120, 13), style=0)
        self.rendimientoText.Show(False)
        self.rendimiento = wx.TextCtrl(id=wxID_PANEL1RENDIMIENTO, name='rendimiento', parent=self, pos=wx.Point(170, 104), size=wx.Size(60, 21), style=0, value='')
        self.rendimiento.Show(False)
        self.rendimientoUnidadesText = wx.StaticText(id=wxID_PANEL1RENDIMIENTOUNIDADESTEXT, label=_('%'), name='rendimientoUnidadesText', parent=self, pos=wx.Point(235, 106), size=wx.Size(15, 13), style=0)
        self.rendimientoUnidadesText.Show(False)

    def OnNombreInstalacion(self, event):
        """
        Metodo: OnNombreInstalacion

        ARGUMENTOS:
                event:
        """
        if self.nombreInstalacion.GetValue() == _('Aire primario'):
            self.nombreInstalacion.SetForegroundColour(wx.Colour(100, 200, 0))
        else:
            self.nombreInstalacion.SetForegroundColour(wx.Colour(0, 0, 0))

    def __init__(self, parent, id, pos, size, style, name, real_parent=None):
        """
        Constructor de la clase

        ARGUMENTOS:
                 parent:
                 id:
                 pos:
                 size:
                 style:
                 name:
                real_parent = None:
        """
        if real_parent == None:
            self.parent = parent
        else:
            self.parent = real_parent
        self.tipoSistema = 'ventilacion'
        self._init_ctrls(parent, id, pos, size, style, name)
        self.subgrupoChoice.SetItems(self.cargarRaices())
        self.elegirRaiz()
        return

    def elegirRaiz(self):
        """
        Metodo: elegirRaiz

        """
        try:
            sel = self.parent.arbolInstalaciones.GetSelection()
            self.subgrupoChoice.SetStringSelection('Edificio Objeto')
            raiz = self.parent.arbolInstalaciones.GetRootItem()
            while sel != raiz:
                for i in range(len(self.parent.parent.subgrupos)):
                    if self.parent.arbolInstalaciones.GetItemText(sel) == '%s' % self.parent.parent.subgrupos[i].nombre:
                        self.subgrupoChoice.SetStringSelection(self.parent.arbolInstalaciones.GetItemText(sel))
                        return

                sel = self.parent.arbolInstalaciones.GetItemParent(sel)

        except:
            logging.info('Excepcion en: %s' % __name__)
            self.subgrupoChoice.SetStringSelection('Edificio Objeto')

    def cargarRaices(self):
        """
        Metodo: cargarRaices

        """
        raices = []
        raices.append(('Edificio Objeto', _('Edificio Objeto')))
        for i in range(len(self.parent.parent.subgrupos)):
            if self.parent.parent.subgrupos[i].nombre != 'Edificio Objeto':
                raices.append((self.parent.parent.subgrupos[i].nombre, self.parent.parent.subgrupos[i].nombre))

        return raices

    def OnRecuperadorCheck(self, event):
        """
        Metodo: OnRecuperadorCheck

        ARGUMENTOS:
                 event:
        """
        if self.recuperadorCheck.GetValue() == True:
            self.rendimientoText.Show(True)
            self.rendimiento.Show(True)
            self.rendimientoUnidadesText.Show(True)
        else:
            self.rendimientoText.Show(False)
            self.rendimiento.Show(False)
            self.rendimientoUnidadesText.Show(False)

    def comprobarDatos(self):
        """
        Metodo: comprobarDatos

        """
        caudal = self.equipoVentilacion.GetValue()
        if ',' in caudal:
            caudal = caudal.replace(',', '.')
            self.equipoVentilacion.SetValue(caudal)
        rendimiento = self.rendimiento.GetValue()
        if ',' in rendimiento:
            rendimiento = rendimiento.replace(',', '.')
            self.rendimiento.SetValue(rendimiento)
        self.listaErrores = ''
        self.listaErrores += Comprueba(self.nombreInstalacion.GetValue(), 1, self.listaErrores, _('nombre')).ErrorDevuelto
        self.listaErrores += Comprueba(self.subgrupoChoice.GetStringSelection(), 0, self.listaErrores, _('zona')).ErrorDevuelto
        self.listaErrores += Comprueba(self.equipoVentilacion.GetValue(), 2, self.listaErrores, _('caudal de ventilación'), 0).ErrorDevuelto
        if self.recuperadorCheck.GetValue() == True:
            self.listaErrores += Comprueba(self.rendimiento.GetValue(), 2, self.listaErrores, _('rendimiento estacional'), 0, 100).ErrorDevuelto

    def cogerDatos(self):
        """
        Metodo: cogerDatos

        """
        self.comprobarDatos()
        if self.listaErrores != '':
            return self.listaErrores
        datos = []
        datos.append(self.nombreInstalacion.GetValue())
        datos.append('ventilacion')
        datos.append(self.equipoVentilacion.GetValue())
        datos.append(self.recuperadorCheck.GetValue())
        if self.recuperadorCheck.GetValue() == True:
            datos.append(self.rendimiento.GetValue())
        else:
            datos.append(0)
        datos.append(self.subgrupoChoice.GetStringSelection())
        return datos

    def cargarDatos(self, datos):
        """
        Metodo: cargarDatos

        ARGUMENTOS:
                datos:
        """
        self.nombreInstalacion.SetValue(datos[0])
        self.equipoVentilacion.SetValue(datos[2])
        self.recuperadorCheck.SetValue(datos[3])
        if self.recuperadorCheck.GetValue() == True:
            self.rendimiento.SetValue(str(datos[4]))
        else:
            self.rendimiento.SetValue('')
        self.OnRecuperadorCheck(None)
        self.subgrupoChoice.SetStringSelection(datos[5])
        return