# Embedded file name: ElementosConstructivos\BDcerramientos.pyc
"""
Modulo: BDcerramientos.py
Modulo con las funciones necesarias para manejar la base de datos de cerramientos del programa
"""
import sqlite3 as dbapi
import os
import wx
import logging

def evitaInj(dato):
    """
    Metodo: evitaInj
    metodo implementado para evitar el SQL inyection en la apliaccio
    Devuelve un estring en el que se han filtrado todas las comillas dobles, siendo sustituidas por dos comillas simples
    
    ARGUMENTOS:
                dato: string de entrada que se debe filtrar
    """
    if '"' in dato:
        dato = dato.replace('"', "''")
    return dato


def borrarCerramiento(cerramiento, filename):
    """
    Metodo: borrarCerramiento
    metodo que borra el cerramiento indicado de la base de datos
    
    ARGUMENTOS:
                cerramiento: string con el nombre del cerramiento(PK) que se desea borrar
                filename: ruta del fichero de BD
    """
    try:
        bbdd = dbapi.connect(filename)
        bbdd.text_factory = str
        c = bbdd.cursor()
        cerramiento = cerramiento.encode('iso-8859-15')
        cerramiento = evitaInj(cerramiento)
        c.execute('delete from compone where NAME_CERR= "%s" ' % cerramiento)
        c.execute('delete from cerramiento where NAME= "%s" ' % cerramiento)
    except:
        wx.MessageBox(_(u'Error de conexi\xf3n a la base de datos'), _(u'Aviso'))
    finally:
        try:
            bbdd.commit()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            c.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            bbdd.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)


def guardar(cerramiento, materiales, filename):
    """
    Metodo: guardar
    
    
    ARGUMENTOS:
                cerramiento:
                materiales:
                filename: ruta del fichero de BD
    """
    if os.path.exists(filename):
        bol = guardaDatos(cerramiento, materiales, filename)
        return bol


def cargaCerramientos(filename):
    """
    Metodo: cargaCerramientos
    Devuelve una lista con los nombres de los cerramientos almacenados en la BD
    
    ARGUMENTOS:
                filename): ruta del fichero de BD
    """
    listaCerramientos = []
    try:
        bbdd = dbapi.connect(filename)
        bbdd.text_factory = str
        c = bbdd.cursor()
        c.execute('select NAME from cerramiento order by NAME')
        for i in c.fetchall():
            listaCerramientos.append('%s' % i)

    except:
        wx.MessageBox(_(u'Error de conexi\xf3n a la base de datos'), _(u'Aviso'))
    finally:
        try:
            bbdd.commit()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            c.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            bbdd.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

    return listaCerramientos


def cargaCerramiento(nombre, filename):
    """
    Metodo: cargaCerramiento
    Devuelve una lista con los datos del cerramiento indicado
    ###Carga lista materiales que componen el cerramiento
    ARGUMENTOS:
                nombre: string que indica el cerramiento a cargar
                filename): ruta del fichero de BD  
    """
    listaCerramiento = []
    try:
        bbdd = dbapi.connect(filename)
        bbdd.text_factory = str
        c = bbdd.cursor()
        nombre = nombre.encode('iso-8859-15')
        c.execute('select * from cerramiento where NAME="%s" ' % nombre)
        listaCerramiento.append(c.fetchall())
        c.execute('select * from compone where NAME_CERR="%s" order by ORDEN' % nombre)
        listaCerramiento.append(c.fetchall())
    except:
        wx.MessageBox(_(u'Error de conexi\xf3n a la base de datos'), _(u'Aviso'))
    finally:
        try:
            bbdd.commit()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            c.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            bbdd.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

    return listaCerramiento


def cargaMaterial(nombre, filename):
    """
    Metodo: cargaMaterial
    Carga caracter\xedsticas del material que compone el cerramiento
    
    ARGUMENTOS:
                nombre:
                filename): ruta del fichero de BD
    """
    listaMaterial = []
    try:
        bbdd = dbapi.connect(filename)
        bbdd.text_factory = str
        c = bbdd.cursor()
        c.execute('select * from material where NAME="%s" ' % nombre)
        for i in c.fetchall():
            for j in i:
                listaMaterial.append(j)

    except:
        wx.MessageBox(_(u'Error de conexi\xf3n a la base de datos'), _(u'Aviso'))
    finally:
        try:
            bbdd.commit()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            c.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            bbdd.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

    return listaMaterial


def crea(filename):
    """
    Metodo: crea
    
    Genera las tablas de la base de datos
    ARGUMENTOS:
                filename: ruta del fichero de BD
    """
    try:
        bbdd = dbapi.connect(filename)
        bbdd.text_factory = str
        c = bbdd.cursor()
        c.execute('create table cerramiento(\n                    NAME            text, \n                    TRANS_TERMICA   NUMBER(5, 5), \n                    PESOM2          NUMBER(5, 5), \n                    CONSTRAINT PK_cerramiento PRIMARY KEY (NAME)\n                    )')
        c.execute('create table material(\n                    NAME            text, \n                    THICKNESS       NUMBER(5, 5), \n                    CONDUCTIVITY    NUMBER(5, 5), \n                    DENSITY         NUMBER(5, 5), \n                    SPECIFIC_HEAT   NUMBER(5, 5), \n                    VAPOUR_DF       NUMBER(5, 5), \n                    IMAGE           text, \n                    TYPE            text, \n                    GRUPO           text, \n                    CONSTRAINT PK_material PRIMARY KEY (NAME), \n                    CONSTRAINT FK_material FOREIGN KEY (GRUPO) references grupo(NAME)\n                    )')
        c.execute('create table compone(\n                    NAME_CERR       text, \n                    NAME_MAT        text, \n                    ORDEN           NUMBER(5), \n                    THICKNESS       NUMBER(5, 5), \n                    CONSTRAINT PK_compone PRIMARY KEY (NAME_CERR, NAME_MAT, ORDEN), \n                    CONSTRAINT FK_compone_cerr FOREIGN KEY (NAME_CERR) references cerramiento(NAME), \n                    CONSTRAINT FK_compone_mat FOREIGN KEY (NAME_MAT) references material(NAME)\n                    )')
    except:
        wx.MessageBox(_(u'Error de conexi\xf3n a la base de datos'), _(u'Aviso'))
    finally:
        try:
            bbdd.commit()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            c.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            bbdd.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)


def existeCerra(cerramiento, filename):
    """
    Metodo: existeCerra
    Comprueba si el nombre de cerramiento(PK) ya existe
    Si existe devuelve True, en caso contrario False
    
    ARGUMENTOS:
                cerramiento:
                filename: ruta del fichero de BD
    """
    try:
        bbdd = dbapi.connect(filename)
        bbdd.text_factory = str
        c = bbdd.cursor()
        cerramiento = evitaInj(cerramiento)
        c.execute('select * from cerramiento where NAME="%s" ' % cerramiento)
    except:
        wx.MessageBox(_(u'Error de conexi\xf3n a la base de datos'), _(u'Aviso'))
    finally:
        if c.fetchone() != None:
            try:
                c.close()
            except:
                logging.info(u'Excepcion en: %s' % __name__)

            try:
                bbdd.close()
            except:
                logging.info(u'Excepcion en: %s' % __name__)

            return True
        try:
            c.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            bbdd.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        return False

    return


def guardaDatos(cerramiento, materiales, filename):
    """
    Metodo: guardaDatos
    Guarda una composicion de cerramiento en la BD
    
    ARGUMENTOS:
                cerramiento: lista de datos del cerramiento
                materiales: lista de materiales que componen el cerramiento
                filename: ruta del fichero de BD
    """
    try:
        bbdd = dbapi.connect(filename)
        bbdd.text_factory = str
        c = bbdd.cursor()
        nCerramiento = cerramiento[0]
        cerramiento.pop(0)
        nCerramiento = evitaInj(nCerramiento)
        c.execute('select * from cerramiento where NAME="%s" ' % nCerramiento)
        if c.fetchone() != None:
            return False
        c.execute('insert into cerramiento values("%s", ?, ?)' % nCerramiento, cerramiento)
        cont = 1
        for i in materiales:
            nameMaterial = i[0]
            c.execute('select * from material where NAME="%s" ' % i[0])
            if c.fetchone() == None:
                c.execute('insert into material values(?, ?, ?, ?, ?, ?, ?, ?, ?)', i)
            compo = []
            compo.append(nameMaterial)
            compo.append(cont)
            compo.append(i[1])
            c.execute('insert into compone values("%s", ?, ?, ?)' % nCerramiento, compo)
            cont = cont + 1

    except:
        wx.MessageBox(_(u'Error de conexi\xf3n a la base de datos'), _(u'Aviso'))
    finally:
        try:
            bbdd.commit()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            c.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            bbdd.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

    return True


def cerramientoCompleto(nombre, filename):
    """
    Metodo: cerramientoCompleto
    Selecciona de la base de datos todos los datos del cerramiento indicado
    
    ARGUMENTOS:
                nombre: string con el nombre del cerraiento
                filename: ruta del fichero de BD
    """
    try:
        bbdd = dbapi.connect(filename)
        bbdd.text_factory = str
        c = bbdd.cursor()
        retorno = []
        c.execute('select * from cerramiento where NAME="%s" ' % nombre)
        cerramiento = c.fetchall()
        nCerramiento = cerramiento[0][0]
        nCerramiento = evitaInj(nCerramiento)
        c.execute('select * from compone where NAME_CERR="%s" order by ORDEN' % nCerramiento)
        nombreMateriales = []
        nombreMateriales.append(c.fetchall())
        nombreMateriales = nombreMateriales[0]
        material = []
        for i in nombreMateriales:
            material.append(cargaMaterial(i[1], filename))

        retorno.append(cerramiento)
        retorno.append(material)
    except:
        wx.MessageBox(_(u'Error de conexi\xf3n a la base de datos'), _(u'Aviso'))
    finally:
        try:
            bbdd.commit()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            c.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            bbdd.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

    return retorno