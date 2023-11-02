# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\dialogoEscalones.pyc
# Compiled at: 2015-02-19 13:18:33
"""
Modulo: dialogoEscalones.py

"""
import wx
from Instalaciones.comprobarCampos import Comprueba2
import logging

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return Dialog1(parent)


wxID_DIALOG1, wxID_DIALOG1BOTONACEPTAR, wxID_DIALOG1BOTONCANCELAR, wxID_POTENCIAFCPGRID1, wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICTEXT2 = [ wx.NewId() for _init_ctrls in range(6) ]

class Dialog1(wx.Dialog):
    """
    Clase: Dialog1 del modulo dialogoEscalones.py

    """

    def _init_coll_potFcp_Columns(self, parent, a):
        """
        Metodo: _init_coll_potFcp_Columns

        ARGUMENTOS:
                parent:
                a:
        """
        parent.CreateGrid(0, 10)
        parent.SetColLabelValue(0, '0.1')
        parent.SetColLabelValue(1, '0.2')
        parent.SetColLabelValue(2, '0.3')
        parent.SetColLabelValue(3, '0.4')
        parent.SetColLabelValue(4, '0.5')
        parent.SetColLabelValue(5, '0.6')
        parent.SetColLabelValue(6, '0.7')
        parent.SetColLabelValue(7, '0.8')
        parent.SetColLabelValue(8, '0.9')
        parent.SetColLabelValue(9, '1.0')
        parent.AppendRows(1)
        parent.SetRowLabelValue(0, _('Fracción\npotencia'))
        parent.SetCellValue(0, 0, a[0])
        parent.SetCellValue(0, 1, a[1])
        parent.SetCellValue(0, 2, a[2])
        parent.SetCellValue(0, 3, a[3])
        parent.SetCellValue(0, 4, a[4])
        parent.SetCellValue(0, 5, a[5])
        parent.SetCellValue(0, 6, a[6])
        parent.SetCellValue(0, 7, a[7])
        parent.SetCellValue(0, 8, a[8])
        parent.SetCellValue(0, 9, a[9])
        parent.AutoSizeColumns()
        parent.AutoSizeRows()
        parent.SetDefaultCellAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

    def _init_ctrls(self, prnt, a):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
                a:
        """
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt, pos=wx.Point(475, 379), size=wx.Size(450, 193), style=wx.DEFAULT_DIALOG_STYLE, title=_('Definir consumo por escalones'))
        self.SetClientSize(wx.Size(450, 193))
        self.SetBackgroundColour('white')
        self.potenciaFcpText = wx.StaticText(id=wxID_DIALOG1STATICTEXT1, label=_('Definir la fracción de la potencia en cada punto'), name='potenciaFcpText', parent=self, pos=wx.Point(15, 15), size=wx.Size(200, 13), style=0)
        self.potenciaFcpText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.potenciaFcpText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.fraccionCaudalText = wx.StaticText(id=wxID_DIALOG1STATICTEXT2, label=_('Fracción del caudal'), name='fraccionCaudalText', parent=self, pos=wx.Point(15, 40), size=wx.Size(420, 13), style=wx.ALIGN_CENTRE)
        self.potenciaFcp = wx.grid.Grid(id=wxID_POTENCIAFCPGRID1, name='', parent=self, pos=wx.Point(15, 55), size=wx.Size(420, 85), style=wx.RAISED_BORDER)
        self._init_coll_potFcp_Columns(self.potenciaFcp, a)
        self.botonAceptar = wx.Button(id=wxID_DIALOG1BOTONACEPTAR, label=_('Aceptar'), name='botonAceptar', parent=self, pos=wx.Point(15, 155), size=wx.Size(75, 23), style=0)
        self.botonAceptar.Bind(wx.EVT_BUTTON, self.OnBotonAceptarButton, id=wxID_DIALOG1BOTONACEPTAR)
        self.botonCancelar = wx.Button(id=wxID_DIALOG1BOTONCANCELAR, label=_('Cancelar'), name='botonCancelar', parent=self, pos=wx.Point(105, 155), size=wx.Size(75, 23), style=0)
        self.botonCancelar.Bind(wx.EVT_BUTTON, self.OnBotonCancelarButton, id=wxID_DIALOG1BOTONCANCELAR)
        self.dev = False

    def __init__(self, parent, a):
        """
        Constructor de la clase

        ARGUMENTOS:
                parent:
                a:
        """
        self._init_ctrls(parent, a)

    def OnBotonAceptarButton(self, event):
        """
        Metodo: OnBotonAceptarButton

        ARGUMENTOS:
                event:
        """
        anterior = 0
        bueno = True
        for i in range(10):
            if Comprueba2(self.potenciaFcp.GetCellValue(0, i), 2, '', 'fail', 0.0, 1.0).ErrorDevuelto != '':
                bueno = False
                break
            else:
                try:
                    if float(self.potenciaFcp.GetCellValue(0, i)) < anterior:
                        bueno = False
                        break
                except:
                    logging.info('Excepcion en: %s' % __name__)
                    bueno = False
                    break

            anterior = float(self.potenciaFcp.GetCellValue(0, i))

        if bueno:
            self.dev = True
            self.Close()
        else:
            wx.MessageBox(_('Revise los valores de la tabla'), _('Aviso'))

    def OnBotonCancelarButton(self, event):
        """
        Metodo: OnBotonCancelarButton

        ARGUMENTOS:
                event:
        """
        self.dev = False
        self.Close()