# Embedded file name: miChoiceGrid.pyc
from wx import Choice
import wx
import wx.grid

class MiChoiceGrid(wx.grid.GridCellChoiceEditor):
    """Redefinimos Choice para recibir una lista de tuplas
    La lista de tuplas la convertimos en un diccionario que es un atributo 
    de esta nueva clase
    
    Se muestra el segundo elemento de la tupla
    Los m\xe9todos get devuelven el primer elemento de la tupla
    """
    traduccion = dict()

    def __init__(self, *args, **kwargs):
        for c in kwargs['choices']:
            self.traduccion[c[1]] = c[0]

        listaOpciones = [ x[1] for x in kwargs['choices'] ]
        super(MiChoiceGrid, self).__init__(listaOpciones)

    def GetCellAttr(self):
        stringTraducida = super(MiChoiceGrid, self).GetCellAttr()
        if stringTraducida == u'':
            string = u''
        else:
            string = self.traduccion[stringTraducida]
        return string

    def SetCellAttr(self, seleccion):
        """Seleccion me llega en castellano,
        tengo que elegir entre las opciones que est\xe1n traducidas         
        """
        if seleccion == u'':
            seleccionTraducida = u''
        else:
            traduccionInversa = dict(((v, k) for k, v in self.traduccion.iteritems()))
            seleccionTraducida = traduccionInversa[seleccion]
        super(MiChoiceGrid, self).SetCellAttr(seleccionTraducida)