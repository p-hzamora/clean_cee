# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: wxFrameGt.pyc
# Compiled at: 2014-12-09 15:08:48
"""
Modulo: wxFrameGt.py

"""
from Escala.escalaCalificacion import escalaTerciario
import datosEdificio, directorios, idioma, Calculos.listadosWeb as listadosWeb, wx, wxFramePt
idioma.ini()
Directorio = directorios.BuscaDirectorios().Directorio

def create(parent):
    """
    Metodo: create

    ARGUMENTOS:
                parent:
    """
    return wxFrameGt(parent)


class wxFrameGt(wxFramePt.wxFramePt):
    """
    Clase: wxFrameGt del modulo wxFrameGt.py

    """

    def __init__(self, parent=None):
        """
        Constructor de la clase

        """
        wxFramePt.wxFramePt.__init__(self, parent=None)
        self.escala = escalaTerciario()
        self.SetTitle(_('CE3X - GT: Certificación energética simplificada de edificios existentes - Gran terciario'))
        self.programa = 'GranTerciario'
        self.panelInstalaciones.panelElegirObjeto.ventiladores.Show(True)
        self.panelInstalaciones.panelElegirObjeto.bombas.Show(True)
        self.panelInstalaciones.panelElegirObjeto.torresRefrigeracion.Show(True)
        self.panelInstalaciones.vistaClasica.definirEquposGT.Show(True)
        self.panelInstalaciones.listadoOpcionesInstalaciones = listadosWeb.listadoOpcionesInstalacionesTerciario
        self.panelInstalaciones.panel2.rendimientoChoice.SetItems(listadosWeb.listadoOpcionesInstalacionesTerciario)
        self.panelInstalaciones.panel2.rendimientoChoice.SetSelection(1)
        return

    def OnMenuFileOpenNuevo(self, event):
        """
        Metodo: OnMenuFileOpenNuevo

        ARGUMENTOS:
                event:
        """
        wxFramePt.wxFramePt.OnMenuFileOpenNuevo(self, event)
        self.SetTitle(_('CE3X - GT: Certificación Energética Simplificada de Edificios Existentes - Gran Terciario'))

    def OnMenuFileSaveasMenu(self, event):
        """
        Metodo: OnMenuFileSaveasMenu

        ARGUMENTOS:
                event:
        """
        wxFramePt.wxFramePt.OnMenuFileSaveasMenu(self, event)
        self.SetTitle(_('CE3X - GT: %s') % self.filename)

    def OnMenuFileSaveMenu(self, event):
        """
        Metodo: OnMenuFileSaveMenu

        ARGUMENTOS:
                event:
        """
        wxFramePt.wxFramePt.OnMenuFileSaveMenu(self, event)
        self.SetTitle(_('CE3X - GT: %s') % self.filename)

    def OnMenuFileOpenMenu(self, event):
        """
        Metodo: OnMenuFileOpenMenu

        ARGUMENTOS:
                event:
        """
        wxFramePt.wxFramePt.OnMenuFileOpenMenu(self, event)
        self.SetTitle(_('CE3X - GT: %s') % self.filename)

    def abreArchivoDirecto(self, fichero):
        """
        Metodo: abreArchivoDirecto

        ARGUMENTOS:
                event:
        """
        wxFramePt.wxFramePt.abreArchivoDirecto(self, fichero)
        self.SetTitle(_('CE3X - GT: %s') % self.filename)