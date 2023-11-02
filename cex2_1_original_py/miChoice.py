# Embedded file name: miChoice.pyc
from wx import Choice
import wx

class MiChoice(Choice):
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

        kwargs['choices'] = [ x[1] for x in kwargs['choices'] ]
        super(MiChoice, self).__init__(*args, **kwargs)

    def GetString(self, n):
        stringTraducida = super(MiChoice, self).GetString(n)
        string = self.traduccion[stringTraducida]
        return string

    def GetStringSelection(self):
        stringTraducida = super(MiChoice, self).GetStringSelection()
        if stringTraducida == u'':
            string = u''
        else:
            string = self.traduccion[stringTraducida]
        return string

    def Insert(self):
        """No creo que lo use, pero por si acaso fuerzo un error"""
        raise

    def SetItems(self, choices):
        self.traduccion = dict()
        for c in choices:
            self.traduccion[c[1]] = c[0]

        choices = [ x[1] for x in choices ]
        super(MiChoice, self).SetItems(choices)

    def SetStringSelection(self, seleccion):
        """Seleccion me llega en castellano,
        tengo que elegir entre las opciones que est\xe1n traducidas 
        
        
        """
        if seleccion == u'':
            seleccionTraducida = u''
        else:
            traduccionInversa = dict(((v, k) for k, v in self.traduccion.iteritems()))
            seleccionTraducida = traduccionInversa[seleccion]
        super(MiChoice, self).SetStringSelection(seleccionTraducida)

    def SetString(self):
        """No creo que lo use, pero por si acaso fuerzo un error"""
        raise