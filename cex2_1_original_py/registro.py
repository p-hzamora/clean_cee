# Embedded file name: registro.pyc
"""
Modulo: registro.py

"""
from Calculos.listados import versionCEX, esRC
import os.path
import sys
import logging
try:
    import _winreg as d
except:
    logging.info(u'Excepcion en: %s' % __name__)

version = 'CEX' + str(versionCEX) + esRC

def compruebaCodigoFuente():
    """Devuelve True si se ejecuta desde c\xf3digo fuente """
    archivo, extension = os.path.splitext(__file__)
    if archivo == 'C:\\Users\\MiguelAngel\\workspace\\CEX\\registro' or archivo == 'C:\\Users\\EdurneZubiri\\workspace\\CEX\\registro':
        return True
    else:
        return False


def compruebaLinux():
    """Devuelve True si se ejecuta desde linux"""
    if sys.platform == 'linux2':
        return True
    else:
        return False


def leerDirectorio():
    """
    Metodo: leerDirectorio
    
    
    """
    if compruebaCodigoFuente() or compruebaLinux():
        ruta, archivo = os.path.split(__file__)
        if ruta == '':
            ruta = './'
        return ruta
    else:
        try:
            a = d.OpenKey(d.HKEY_CURRENT_USER, 'Software\\%s\\directorio' % version)
            b = d.EnumValue(a, 0)
            return b[1]
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            try:
                a = d.OpenKey(d.HKEY_USERS, '.DEFAULT\\Software\\%s\\directorio' % version)
                b = d.EnumValue(a, 0)
                return b[1]
            except:
                logging.info(u'Excepcion en: %s' % __name__)
                return None

        return None


def leerDirectorioDoc():
    """
    Metodo: leerDirectorioDoc
    
    
    """
    if compruebaCodigoFuente() or compruebaLinux():
        ruta, archivo = os.path.split(__file__)
        if ruta == '':
            ruta = './'
        return ruta
    else:
        try:
            a = d.OpenKey(d.HKEY_CURRENT_USER, 'Software\\%s\\directorioDoc' % version)
            b = d.EnumValue(a, 0)
            return b[1]
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            try:
                a = d.OpenKey(d.HKEY_USERS, '.DEFAULT\\Software\\%s\\directorioDoc' % version)
                b = d.EnumValue(a, 0)
                return b[1]
            except:
                logging.info(u'Excepcion en: %s' % __name__)
                return None

        return None


def leerIdioma():
    """
    Metodo: leerIdioma
    
    
                :
    """
    try:
        a = d.OpenKey(d.HKEY_CURRENT_USER, 'Software\\%s\\idioma' % version)
        b = d.EnumValue(a, 0)
        return b[1]
    except:
        logging.info(u'Excepcion en: %s' % __name__)
        try:
            a = d.OpenKey(d.HKEY_USERS, '.DEFAULT\\Software\\%s\\idioma' % version)
            b = d.EnumValue(a, 0)
            return b[1]
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            return 'es'


def editarIdioma(idioma):
    """
    Metodo: editarIdioma
    
    
    ARGUMENTOS:
                idioma:
    """
    try:
        a = d.OpenKey(d.HKEY_CURRENT_USER, 'Software\\%s' % version)
        d.SetValue(a, 'idioma', d.REG_SZ, idioma)
        a.Close()
    except:
        logging.info(u'Excepcion en: %s' % __name__)
        try:
            a = d.OpenKey(d.HKEY_USERS, '.DEFAULT\\Software\\%s' % version)
            d.SetValue(a, 'idioma', d.REG_SZ, idioma)
            a.Close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)


def editarFicherosRecientes(files):
    """
    Metodo: editarFicherosRecientes
    
    
    ARGUMENTOS:
                files:
    """
    try:
        a = d.OpenKey(d.HKEY_CURRENT_USER, 'Software\\%s' % version)
    except:
        logging.info(u'Excepcion en: %s' % __name__)
        try:
            a = d.OpenKey(d.HKEY_USERS, 'Software\\%s' % version)
        except:
            logging.info(u'Excepcion en: %s' % __name__)

    try:
        d.SetValue(a, 'file0', d.REG_SZ, files[0])
        d.SetValue(a, 'file1', d.REG_SZ, files[1])
        d.SetValue(a, 'file2', d.REG_SZ, files[2])
        d.SetValue(a, 'file3', d.REG_SZ, files[3])
        d.SetValue(a, 'file4', d.REG_SZ, files[4])
    except:
        logging.info(u'Excepcion en: %s' % __name__)

    try:
        a.Close()
    except:
        logging.info(u'Excepcion en: %s' % __name__)


def leerFicherosRecientes():
    """
    Metodo: leerFicherosRecientes
    
    
                :
    """
    try:
        a = d.OpenKey(d.HKEY_CURRENT_USER, 'Software\\%s' % version)
        files = []
        for i in range(6):
            if 'file' in d.EnumKey(a, i):
                b = d.OpenKey(d.HKEY_CURRENT_USER, 'Software\\%s\\' % version + d.EnumKey(a, i))
                c = d.EnumValue(b, 0)
                if c[1] != '':
                    files.append(c[1])

        a.Close()
        return files
    except:
        logging.info(u'Excepcion en: %s' % __name__)
        try:
            a = d.OpenKey(d.HKEY_USERS, '.DEFAULT\\Software\\%s' % version)
            files = []
            for i in range(6):
                if 'file' in d.EnumKey(a, i):
                    b = d.OpenKey(d.HKEY_USERS, '.DEFAULT\\Software\\%s\\' % version + d.EnumKey(a, i))
                    c = d.EnumValue(b, 0)
                    if c[1] != '':
                        files.append(c[1])

            a.Close()
            return files
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            return []