# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\dialogoEscalones.pyc
# Compiled at: 2015-02-19 13:18:33
from Instalaciones.comprobarCampos import Comprueba2
import logging

def create(parent):
    return Dialog1(parent)



class Dialog1(wx.Dialog):

    def _init_coll_potFcp_Columns(self, parent, a):
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
        parent.SetRowLabelValue(0, 'Fracción\npotencia')
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
        self.potenciaFcp = wx.grid.Grid(id=wxID_POTENCIAFCPGRID1, name='', parent=self, pos=wx.Point(15, 55), size=wx.Size(420, 85), style=wx.RAISED_BORDER)
        self._init_coll_potFcp_Columns(self.potenciaFcp, a)
        self.dev = False

    def __init__(self, parent, a):
        self._init_ctrls(parent, a)

    def OnBotonAceptarButton(self, event):
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
            raise Exception('Revise los valores de la tabla')

    def OnBotonCancelarButton(self, event):
        self.dev = False
        self.Close()