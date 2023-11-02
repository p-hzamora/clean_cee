# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: directorios.pyc
# Compiled at: 2015-02-17 16:12:15
"""
Modulo: directorios.py

"""
import os, registro

class BuscaDirectorios:
    """
    Clase: BuscaDirectorios del modulo directorios.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        if os.name == 'nt':
            self.Directorio = registro.leerDirectorio()
            self.DirectorioDoc = registro.leerDirectorioDoc()
        else:
            self.Directorio = os.path.dirname(os.path.realpath(__file__))
            self.DirectorioDoc = os.path.dirname(os.path.realpath(__file__))