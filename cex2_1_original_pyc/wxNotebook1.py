# Embedded file name: wxNotebook1.pyc
"""
Modulo: wxNotebook1.py

"""
from MedidasDeMejora.panelCompararMejora import panelCompararMejora, panelCompararMejoraTerciario
from MedidasDeMejora.panelDefinirMedidasMejora import panelDefinirMedidasMejora
import wx
import logging

def create(parent):
    """
    Metodo: create
    
    
    ARGUMENTOS:
                parent:
    """
    return wxNotebook1(parent)


wxID_NOTEBOOK1 = wx.NewId()

class wxNotebook1(wx.Notebook):
    """
    Clase: wxNotebook1 del modulo wxNotebook1.py
    
    
    """

    def _init_ctrls(self, prnt, id_prnt, pos_prnt, size_prnt, style_prnt, name_prnt):
        """
        Metodo: _init_ctrls
        
        
        ARGUMENTOS:
                prnt:
                id_prnt:
                pos_prnt:
                size_prnt:
                style_prnt:
                name_prnt:
        """
        wx.Notebook.__init__(self, id=id_prnt, name=name_prnt, parent=prnt, pos=pos_prnt, size=size_prnt, style=style_prnt)

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
        self.parent = parent
        self._init_ctrls(parent, id, pos, size, style, name)
        self.subgrupos = []
        self.envolvente = ''
        self.instalaciones = ''
        wx.EVT_LEFT_DOWN(self, self.OnLeftDown)

    def OnLeftDown(self, event):
        nPestanaSelec = self.HitTest(event.GetPosition())[0]
        self.SetSelection(nPestanaSelec)
        pestanaSelec = self.GetPage(nPestanaSelec)
        if pestanaSelec.GetName() == 'panelMedidasMejora':
            self.recalcularMedidasDeMejora()
        elif pestanaSelec.GetName() == 'panelAnalisisEconomico':
            self.recalcularAnalisisEconomico()

    def recalcularMedidasDeMejora(self):
        self.parent.calculoMedidasUsuario()
        if self.parent.objEdificio.casoValido == True:
            if isinstance(self.parent.panelMedidasMejora.PanelVacio, panelDefinirMedidasMejora):
                try:
                    conjuntoCargadoEnPanel = self.parent.panelMedidasMejora.PanelVacio.conjuntoMM
                    conjuntoMMARecargar = ''
                    for conjuntoMM in self.parent.listadoConjuntosMMUsuario:
                        if conjuntoMM.nombre == conjuntoCargadoEnPanel.nombre:
                            conjuntoMMARecargar = conjuntoMM
                            break

                    if conjuntoMMARecargar != '':
                        self.parent.panelMedidasMejora.PanelVacio.Destroy()
                        self.parent.panelMedidasMejora.PanelVacio = panelDefinirMedidasMejora(parent=self.parent.panelMedidasMejora, pos=wx.Point(230, 8), size=wx.Size(770, 584), style=wx.TAB_TRAVERSAL, name='PanelVacio', id=-1, conjuntoMM=conjuntoMMARecargar)
                except:
                    logging.info(u'Excepcion en: %s' % __name__)

            elif isinstance(self.parent.panelMedidasMejora.PanelVacio, panelCompararMejora):
                try:
                    self.parent.panelMedidasMejora.PanelVacio.CargarDatos()
                except:
                    logging.info(u'Excepcion en: %s' % __name__)

            elif isinstance(self.parent.panelMedidasMejora.PanelVacio, panelCompararMejoraTerciario):
                try:
                    self.parent.panelMedidasMejora.PanelVacio.CargarDatos()
                except:
                    logging.info(u'Excepcion en: %s' % __name__)

        else:
            if self.parent.panelMedidasMejora in self.parent.paneles:
                self.parent.panelMedidasMejora.OnCerrarButton(None)
            if self.parent.panelAnalisisEconomico in self.parent.paneles:
                self.parent.panelAnalisisEconomico.OnCerrarButton(None)
        return

    def recalcularAnalisisEconomico(self):
        self.parent.calculoAnalisisEconomico()
        if self.parent.objEdificio.casoValido == False:
            if self.parent.panelMedidasMejora in self.parent.paneles:
                self.parent.panelMedidasMejora.OnCerrarButton(None)
            if self.parent.panelAnalisisEconomico in self.parent.paneles:
                self.parent.panelAnalisisEconomico.OnCerrarButton(None)
        return

    def iniciaPaneles(self, paneles, notebook):
        """
        Metodo: iniciaPaneles
        
        
        ARGUMENTOS:
                paneles:
                notebook):   ####Funcion que carga los paneles que estan en el array panel:
        """
        for i in range(len(paneles)):
            notebook.AddPage(imageId=-1, page=paneles[i], select=False, text=paneles[i].nombre)
            if paneles[i].nombre == _(u'Envolvente t\xe9rmica'):
                self.envolvente = paneles[i]
            if paneles[i].nombre == _(u'Instalaciones'):
                self.instalaciones = paneles[i]