# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: idioma.pyc
# Compiled at: 2015-02-19 13:18:34
"""
Modulo: idioma.py

"""
import directorios, gettext, registro, wx, logging
Directorio = directorios.BuscaDirectorios().Directorio

def ini():
    """
    Metodo: ini

                :
    """
    try:
        idioma = registro.leerIdioma()
        lang = gettext.translation(idioma, Directorio + '/locale', languages=[idioma])
        lang.install(unicode=1)
    except:
        logging.info('Excepcion en: %s' % __name__)
        lang = gettext.translation('es', Directorio + '/locale', languages=['es'])
        lang.install(unicode=1)
        wx.MessageBox('No se ha podido cargar el paquete de idioma', 'Aviso')