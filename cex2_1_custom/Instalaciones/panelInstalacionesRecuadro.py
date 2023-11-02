# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\panelInstalacionesRecuadro.pyc
# Compiled at: 2014-02-18 15:21:02
"""
Modulo: panelInstalacionesRecuadro.py

"""
import wx
wxID_PANEL1, wxID_PANEL1RECUADRO = [ wx.NewId() for _init_ctrls in range(2) ]

class panelRecuadro(wx.Panel):
    """
    Clase: panelRecuadro del modulo panelInstalacionesRecuadro.py

    """

    def _init_ctrls(self, prnt, ide, posi, siz, styl, nam):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
                ide:
                posi:
                siz:
                styl:
                nam:
        """
        wx.Panel.__init__(self, id=ide, name=nam, parent=prnt, pos=posi, size=siz, style=styl)
        self.SetBackgroundColour('white')
        self.titulo = wx.StaticText(id=wxID_PANEL1RECUADRO, label=_('Equipo de ACS'), name='datosGeneralesText', parent=self, pos=wx.Point(0, 8), size=wx.Size(770, 20), style=0)
        self.titulo.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.titulo.SetForegroundColour(wx.Colour(0, 64, 128))

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
        self.parent = parent