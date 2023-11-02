# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\comprobarCampos.pyc
# Compiled at: 2014-02-18 15:21:02
"""
Modulo: comprobarCampos.py

"""

class Comprueba:
    """
    Clase: Comprueba del modulo comprobarCampos.py

    """

    def __init__(self, dato, tipoObjeto, listaErrores, msgError, valorMin=None, valorMax=None):
        """
        Constructor de la clase

        ARGUMENTOS:
                dato:
                tipoObjeto:
                listaErrores:
                msgError:
                valorMin=None:
                valorMax=None:
        """
        self.dato = dato
        self.tipoObjeto = tipoObjeto
        self.listaErrores = listaErrores
        self.valorMin = valorMin
        self.valorMax = valorMax
        self.msgError = msgError
        self.ErrorDevuelto = self.realizaComprobacion()

    def realizaComprobacion(self):
        """
        Metodo: realizaComprobacion

        """
        if self.tipoObjeto == 0 or self.tipoObjeto == 1:
            if self.dato == '':
                if self.listaErrores != '':
                    return ', ' + self.msgError
                else:
                    return self.msgError

            else:
                return ''
        elif self.tipoObjeto == 2:
            if ',' in self.dato:
                self.dato = self.dato.replace(',', '.')
            if self.valorMin != None:
                try:
                    if float(self.dato) < self.valorMin:
                        self.dato = ''
                except (ValueError, TypeError):
                    self.dato = ''

            if self.valorMax != None:
                try:
                    if float(self.dato) > self.valorMax:
                        self.dato = ''
                except (ValueError, TypeError):
                    self.dato = ''

            try:
                float(self.dato)
            except (ValueError, TypeError):
                self.dato = ''

            if self.dato == '':
                if self.listaErrores != '':
                    return ', ' + self.msgError
                else:
                    return self.msgError

            else:
                return ''
        return