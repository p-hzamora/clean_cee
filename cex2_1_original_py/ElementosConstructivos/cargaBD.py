# Embedded file name: ElementosConstructivos\cargaBD.pyc
"""
Modulo: cargaBD.py
Modulo con las funciones necesarias para manejar la base de datos de las librer\xedas
"""
import sqlite3 as dbapi
import wx
import logging
import directorios
Directorio = directorios.BuscaDirectorios().DirectorioDoc

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


def cargarGrupoPTCal():
    """
    Metodo: cargarGrupoPTCal
    
    
    """
    listaGrupos = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        c.execute('select Name from grupoPT')
        for i in c.fetchall():
            listaGrupos.append('%s' % i)

    except:
        wx.MessageBox(_(u'Error de conexi\xf3n a la base de datos'), _(u'Aviso'))
    finally:
        try:
            c.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            bbdd.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

    return listaGrupos


def cargarPTCal(grupo):
    """
    Metodo: cargarPTCal
    
    
    ARGUMENTOS:
                grupo:
    """
    listaMateriales = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = (grupo,)
        c.execute("select NAME from puenteTermico where TYPE='C' and grupo=?", clave)
        for i in c.fetchall():
            listaMateriales.append('%s' % i)

    except:
        wx.MessageBox(_(u'Error de conexi\xf3n a la base de datos'), _(u'Aviso'))
    finally:
        try:
            c.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            bbdd.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

    return listaMateriales


def nuevoPT(material):
    """
    Metodo: nuevoPT
    
    
    ARGUMENTOS:
                material:
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        nombre = material[0].encode('iso-8859-15')
        nombre = evitaInj(nombre)
        fachada = material[1].encode('iso-8859-15')
        fachada = evitaInj(fachada)
        grupo = material[-1].encode('iso-8859-15')
        grupo = evitaInj(grupo)
        material.pop(1)
        material.pop(0)
        material.pop(-1)
        c.execute('select * from tipoFachada where NAME="%s"  ' % fachada)
        if c.fetchone() == None:
            c.execute('insert into tipoFachada values("%s", \'U\')' % fachada)
        c.execute('select * from fachadaGrupo where FACHADA="%s" and GRUPO = "%s"  ' % (fachada, grupo))
        if c.fetchone() == None:
            c.execute('insert into fachadaGrupo values("%s", "%s")' % (fachada, grupo))
        c.execute('insert into puenteTermico values("%s", "%s", ?, ?, ?, "%s")' % (nombre, fachada, grupo), material)
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

    return


def modificaPT(material, nombreViejo):
    """
    Metodo: modificaPT
    
    
    ARGUMENTOS:
                material:
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        nombre = material[0].encode('iso-8859-15')
        fachada = material[1].encode('iso-8859-15')
        grupo = material[-1].encode('iso-8859-15')
        nombreViejo = nombreViejo.encode('iso-8859-15')
        nombreViejo = evitaInj(nombreViejo)
        nombre = evitaInj(nombre)
        grupo = evitaInj(grupo)
        fachada = evitaInj(fachada)
        material.pop(-1)
        material.pop(1)
        material.pop(0)
        c.execute('update puenteTermico SET FI=?, \n                                    IMAGE=?, \n                                    TYPE=?,\n                                    NAME="%s"\n                                    where NAME="%s" and FACHADA= "%s" and GRUPO="%s" ' % (nombre,
         nombreViejo,
         fachada,
         grupo), material)
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


def cargarGrupoPTUser():
    """
    Metodo: cargarGrupoPTUser
    
    
                :
    """
    listaGrupos = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        c.execute("select NAME from grupoPT where TYPE='U'")
        for i in c.fetchall():
            listaGrupos.append('%s' % i)

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

    return listaGrupos


def borraGrupoPTUser(grupo, padre):
    """
    Metodo: borraGrupoPTUser
    
    
    ARGUMENTOS:
                grupo:
                padre:
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = grupo.encode('iso-8859-15')
        padre = padre.encode('iso-8859-15')
        clave = evitaInj(clave)
        padre = evitaInj(padre)
        c.execute('delete from puenteTermico where FACHADA="%s" and GRUPO = "%s" ' % (clave, padre))
        c.execute('delete from fachadaGrupo where FACHADA="%s" and GRUPO = "%s" ' % (clave, padre))
        bbdd.commit()
        c.execute('select * from puenteTermico where FACHADA="%s" ' % clave)
        if c.fetchone() == None:
            c.execute('delete from tipoFachada where NAME="%s" ' % clave)
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

    return


def borraPTUser(material, padre, abuelo):
    """
    Metodo: borraPTUser
    
    
    ARGUMENTOS:
                material:
                padre:
                abuelo:
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = material.encode('iso-8859-15')
        padre = padre.encode('iso-8859-15')
        abuelo = abuelo.encode('iso-8859-15')
        clave = evitaInj(clave)
        padre = evitaInj(padre)
        abuelo = evitaInj(abuelo)
        c.execute('select FACHADA from puenteTermico where NAME="%s" ' % clave)
        grupo = c.fetchone()
        c.execute('delete from puenteTermico where NAME="%s" and FACHADA = "%s" and GRUPO = "%s" ' % (clave, padre, abuelo))
        bbdd.commit()
        c.execute('select * from puenteTermico where FACHADA=? and GRUPO = "%s" ' % abuelo, grupo)
        if c.fetchone() == None:
            c.execute('delete from tipoFachada where NAME=?', grupo)
            c.execute(' delete from fachadaGrupo where FACHADA=? and GRUPO="%s" ' % abuelo, grupo)
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

    return


def compruebaPT(material, padre, abuelo):
    """
    Metodo: compruebaPT
    
    
    ARGUMENTOS:
                material:
                padre:
                abuelo:
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = material.encode('iso-8859-15')
        padre = padre.encode('iso-8859-15')
        abuelo = abuelo.encode('iso-8859-15')
        clave = evitaInj(clave)
        padre = evitaInj(padre)
        abuelo = evitaInj(abuelo)
        c.execute('select * from puenteTermico where NAME="%s" and FACHADA = "%s" and GRUPO = "%s" ' % (clave, padre, abuelo))
    except:
        wx.MessageBox(_(u'Error de conexi\xf3n a la base de datos'), _(u'Aviso'))
    finally:
        if c.fetchone() == None:
            try:
                c.close()
            except:
                logging.info(u'Excepcion en: %s' % __name__)

            try:
                bbdd.close()
            except:
                logging.info(u'Excepcion en: %s' % __name__)

            return False
        try:
            c.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            bbdd.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        return True

    return


def cargarPT(material, padre, abuelo):
    """
    Metodo: cargarPT
    
    
    ARGUMENTOS:
                material:
                padre:
                abuelo):###Llamo a esta funcion:
                le doy nombre del material y me devuelve caracteristic:
    """
    listaMaterial = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        material = material.encode('iso-8859-15')
        padre = padre.encode('iso-8859-15')
        abuelo = abuelo.encode('iso-8859-15')
        material = evitaInj(material)
        padre = evitaInj(padre)
        abuelo = evitaInj(abuelo)
        c.execute('select * from puenteTermico where NAME ="%s" and FACHADA="%s" and GRUPO = "%s" ' % (material, padre, abuelo))
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


def obtenerFachadas():
    """
    Metodo: obtenerFachadas
    
    
                :
    """
    listaMateriales = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        c.execute('select NAME from tipoFachada')
        for i in c.fetchall():
            listaMateriales.append('%s' % i)

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

    return listaMateriales


def cargarOpcionesCerramientoCal(grupo):
    """
    Metodo: cargarOpcionesCerramientoCal
    
    
    ARGUMENTOS:
                grupo:
    """
    r = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        c.execute('select FACHADA from fachadaGrupo, \n    tipoFachada  where fachadaGrupo.GRUPO="%s" \n    and tipoFachada.TYPE = "C" and tipoFachada.NAME=fachadaGrupo.FACHADA ' % grupo)
        for i in c.fetchall():
            r.append('%s' % i)

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

    return r


def cargarOpcionesCerramientoUser(grupo):
    """
    Metodo: cargarOpcionesCerramientoUser
    
    
    ARGUMENTOS:
                grupo:
    """
    r = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        c.execute('select fachadaGrupo.FACHADA from fachadaGrupo, tipoFachada  \nwhere fachadaGrupo.GRUPO="%s" and tipoFachada.TYPE = "U" and tipoFachada.NAME=fachadaGrupo.FACHADA ' % grupo)
        for i in c.fetchall():
            r.append('%s' % i)

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

    return r


def cargaPTCal(grupo, fachada):
    """
    Metodo: cargaPTCal
    
    
    ARGUMENTOS:
                grupo:
                fachada:
    """
    lista = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        c.execute('select Name from puenteTermico \nwhere GRUPO="%s" and FACHADA="%s" and TYPE= "C" ' % (grupo, fachada))
        for i in c.fetchall():
            lista.append('%s' % i)

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

    return lista


def cargaPTUser(grupo, fachada):
    """
    Metodo: cargaPTUser
    
    
    ARGUMENTOS:
                grupo:
                fachada:
    """
    lista = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        c.execute('select Name from puenteTermico \nwhere GRUPO="%s" and FACHADA="%s" and TYPE= "U" ' % (grupo, fachada))
        for i in c.fetchall():
            lista.append('%s' % i)

    except:
        logging.info(u'Excepcion en: %s' % __name__)
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

    return lista


def nuevoMaterial(material):
    """
    Metodo: nuevoMaterial
    
    
    ARGUMENTOS:
                material:
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        nombre = material[0].encode('iso-8859-15')
        grupo = material[8].encode('iso-8859-15')
        nombre = evitaInj(nombre)
        grupo = evitaInj(grupo)
        material.pop(8)
        material.pop(0)
        c.execute('select * from grupo where NAME="%s"  ' % grupo)
        if c.fetchone() == None:
            foto = material[6].encode('iso-8859-15')
            c.execute('insert into grupo values("%s", \'U\', "%s")' % (grupo, foto))
        c.execute('insert into material values("%s", ?, ?, ?, ?, ?, ?, ?, "%s")' % (nombre, grupo), material)
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

    return


def nuevoVidrio(material):
    """
    Metodo: nuevoVidrio
    
    
    ARGUMENTOS:
                material:
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        nombre = material[0].encode('iso-8859-15')
        grupo = material[1].encode('iso-8859-15')
        nombre = evitaInj(nombre)
        grupo = evitaInj(grupo)
        material.pop(1)
        material.pop(0)
        c.execute('select * from grupoVidrio where NAME="%s"  ' % grupo)
        if c.fetchone() == None:
            c.execute('insert into grupoVidrio values("%s", \'U\')' % grupo)
        c.execute('insert into vidrio values("%s", "%s", ?, ?, ?)' % (nombre, grupo), material)
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

    return


def nuevoMarco(material):
    """
    Metodo: nuevoMarco
    
    
    ARGUMENTOS:
                material:
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        nombre = material[0].encode('iso-8859-15')
        grupo = material[1].encode('iso-8859-15')
        nombre = evitaInj(nombre)
        grupo = evitaInj(grupo)
        material.pop(1)
        material.pop(0)
        c.execute('select * from grupoMarco where NAME="%s"  ' % grupo)
        if c.fetchone() == None:
            c.execute('insert into grupoMarco values("%s", \'U\')' % grupo)
        c.execute('insert into marco values("%s", "%s", ?, ?, ?)' % (nombre, grupo), material)
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

    return


def modificaMaterial(material, nombreViejo):
    """
    Metodo: modificaMaterial
    
    
    ARGUMENTOS:
                material:
                nombreViejo:
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        nombre = material[8].encode('iso-8859-15')
        grupo = material[7].encode('iso-8859-15')
        nombre = evitaInj(nombre)
        grupo = evitaInj(grupo)
        nombreViejo = nombreViejo.encode('iso-8859-15')
        material.pop(8)
        material.pop(7)
        c.execute('update material SET THICKNESS=?, \n                                    CONDUCTIVITY=?, \n                                    DENSITY=?, \n                                    SPECIFIC_HEAT=?, \n                                    VAPOUR_DF=?, \n                                    IMAGE=?, \n                                    TYPE=?, \n                                    GRUPO="%s", \n                                    NAME="%s"\n                                    where NAME="%s" ' % (grupo, nombre, nombreViejo), material)
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


def modificaVidrio(material, nombreViejo):
    """
    Metodo: modificaVidrio
    
    
    ARGUMENTOS:
                material:
    
    
    
    
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        nombre = material[0].encode('iso-8859-15')
        grupo = material[1].encode('iso-8859-15')
        nombre = evitaInj(nombre)
        grupo = evitaInj(grupo)
        nombreViejo = nombreViejo.encode('iso-8859-15')
        nombreViejo = evitaInj(nombreViejo)
        material.pop(1)
        material.pop(0)
        c.execute('update vidrio SET FACTORSOLAR=?, \n                                    UVIDRIO=?, \n                                    TYPE=?, \n                                    GRUPO="%s",\n                                    NAME="%s"\n                                    where NAME="%s" ' % (grupo, nombre, nombreViejo), material)
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


def modificaMarco(material, nombreViejo):
    """
    Metodo: modificaMarco
    
    
    ARGUMENTOS:
                material:
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        nombre = material[0].encode('iso-8859-15')
        grupo = material[1].encode('iso-8859-15')
        nombreViejo = nombreViejo.encode('iso-8859-15')
        nombreViejo = evitaInj(nombreViejo)
        nombre = evitaInj(nombre)
        grupo = evitaInj(grupo)
        material.pop(1)
        material.pop(0)
        c.execute('update marco SET ABSORTIVIDAD=?, \n                                    UMARCO=?, \n                                    TYPE=?, \n                                    GRUPO="%s",\n                                    NAME="%s"\n                                    where NAME="%s" ' % (grupo, nombre, nombreViejo), material)
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


def cargarGrupoCal():
    """
    Metodo: cargarGrupoCal
    
    
                :
    """
    listaGrupos = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        c.execute("select NAME from grupo where TYPE='C'")
        for i in c.fetchall():
            listaGrupos.append('%s' % i)

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

    return listaGrupos


def cargarGrupoUser():
    """
    Metodo: cargarGrupoUser
    
    
                :
    """
    listaGrupos = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        c.execute("select NAME from grupo where TYPE='U'")
        for i in c.fetchall():
            listaGrupos.append('%s' % i)

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

    return listaGrupos


def cargarGrupoVidrioCal():
    """
    Metodo: cargarGrupoVidrioCal
    
    
                :
    """
    listaGrupos = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        c.execute("select NAME from grupoVidrio where TYPE='C'")
        for i in c.fetchall():
            listaGrupos.append('%s' % i)

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

    return listaGrupos


def cargarGrupoVidrioUser():
    """
    Metodo: cargarGrupoVidrioUser
    
    
                :
    """
    listaGrupos = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        c.execute("select NAME from grupoVidrio where TYPE='U'")
        for i in c.fetchall():
            listaGrupos.append('%s' % i)

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

    return listaGrupos


def cargarGrupoMarcoCal():
    """
    Metodo: cargarGrupoMarcoCal
    
    
                :
    """
    listaGrupos = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        c.execute("select NAME from grupoMarco where TYPE='C'")
        for i in c.fetchall():
            listaGrupos.append('%s' % i)

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

    return listaGrupos


def cargarGrupoMarcoUser():
    """
    Metodo: cargarGrupoMarcoUser
    
    
                :
    """
    listaGrupos = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        c.execute("select NAME from grupoMarco where TYPE='U'")
        for i in c.fetchall():
            listaGrupos.append('%s' % i)

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

    return listaGrupos


def cargarMaterialesCal(grupo):
    """
    Metodo: cargarMaterialesCal
    
    
    ARGUMENTOS:
                grupo:
    """
    listaMateriales = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = (grupo,)
        c.execute("select NAME from material where TYPE='C' and grupo=?", clave)
        for i in c.fetchall():
            listaMateriales.append('%s' % i)

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

    return listaMateriales


def cargarMaterialesUser(grupo):
    """
    Metodo: cargarMaterialesUser
    
    
    ARGUMENTOS:
                grupo:
    """
    listaMateriales = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = (grupo,)
        c.execute("select NAME from material where TYPE='U' and grupo=?", clave)
        for i in c.fetchall():
            listaMateriales.append('%s' % i)

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

    return listaMateriales


def cargarVidriosCal(grupo):
    """
    Metodo: cargarVidriosCal
    
    
    ARGUMENTOS:
                grupo:
    """
    listaVidrios = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = (grupo,)
        c.execute("select NAME from vidrio where TYPE='C' and grupo=?", clave)
        for i in c.fetchall():
            listaVidrios.append('%s' % i)

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

    return listaVidrios


def cargarVidriosUser(grupo):
    """
    Metodo: cargarVidriosUser
    
    
    ARGUMENTOS:
                grupo:
    """
    listaVidrios = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = (grupo,)
        c.execute("select NAME from vidrio where TYPE='U' and grupo=?", clave)
        for i in c.fetchall():
            listaVidrios.append('%s' % i)

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

    return listaVidrios


def cargarMarcosCal(grupo):
    """
    Metodo: cargarMarcosCal
    
    
    ARGUMENTOS:
                grupo:
    """
    listaMarcos = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = (grupo,)
        c.execute("select NAME from marco where TYPE='C' and grupo=?", clave)
        for i in c.fetchall():
            listaMarcos.append('%s' % i)

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

    return listaMarcos


def cargarMarcosUser(grupo):
    """
    Metodo: cargarMarcosUser
    
    
    ARGUMENTOS:
                grupo:
    """
    listaMarcos = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = (grupo,)
        c.execute("select NAME from marco where TYPE='U' and grupo=?", clave)
        for i in c.fetchall():
            listaMarcos.append('%s' % i)

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

    return listaMarcos


def borraGrupoUser(grupo):
    """
    Metodo: borraGrupoUser
    
    
    ARGUMENTOS:
                grupo:
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = grupo.encode('iso-8859-15')
        clave = evitaInj(clave)
        c.execute('delete from material where GRUPO="%s" ' % clave)
        c.execute('delete from grupo where NAME="%s" ' % clave)
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


def borraGrupoVidrioUser(grupo):
    """
    Metodo: borraGrupoVidrioUser
    
    
    ARGUMENTOS:
                grupo:
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = grupo.encode('iso-8859-15')
        clave = evitaInj(clave)
        c.execute('delete from vidrio where GRUPO="%s" ' % clave)
        c.execute('delete from grupoVidrio where NAME="%s" ' % clave)
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


def borraGrupoMarcoUser(grupo):
    """
    Metodo: borraGrupoMarcoUser
    
    
    ARGUMENTOS:
                grupo:
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = grupo.encode('iso-8859-15')
        clave = evitaInj(clave)
        c.execute('delete from marco where GRUPO="%s" ' % clave)
        c.execute('delete from grupoMarco where NAME="%s" ' % clave)
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


def borraMaterialUser(material):
    """
    Metodo: borraMaterialUser
    
    
    ARGUMENTOS:
                material:
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = material.encode('iso-8859-15')
        clave = evitaInj(clave)
        c.execute('select GRUPO from material where NAME="%s" ' % clave)
        grupo = c.fetchone()
        c.execute('delete from material where NAME="%s" ' % clave)
        bbdd.commit()
        c.execute('select * from material where GRUPO=?', grupo)
        if c.fetchone() == None:
            c.execute('delete from grupo where NAME=?', grupo)
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

    return


def borraVidrioUser(material):
    """
    Metodo: borraVidrioUser
    
    
    ARGUMENTOS:
                material:
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = material.encode('iso-8859-15')
        clave = evitaInj(clave)
        c.execute('select GRUPO from vidrio where NAME="%s" ' % clave)
        grupo = c.fetchone()
        c.execute('delete from vidrio where NAME="%s" ' % clave)
        bbdd.commit()
        c.execute('select * from vidrio where GRUPO=?', grupo)
        if c.fetchone() == None:
            c.execute('delete from grupoVidrio where NAME=?', grupo)
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

    return


def borraMarcoUser(material):
    """
    Metodo: borraMarcoUser
    
    
    ARGUMENTOS:
                material:
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = material.encode('iso-8859-15')
        clave = evitaInj(clave)
        c.execute('select GRUPO from marco where NAME="%s" ' % clave)
        grupo = c.fetchone()
        c.execute('delete from marco where NAME="%s" ' % clave)
        bbdd.commit()
        c.execute('select * from marco where GRUPO=?', grupo)
        if c.fetchone() == None:
            c.execute('delete from grupoMarco where NAME=?', grupo)
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

    return


def cmpMaterialEnCerra(material):
    """
    Metodo: cmpMaterialEnCerra
    
    
    ARGUMENTOS:
                material:
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = material.encode('iso-8859-15')
        clave = evitaInj(clave)
        c.execute('select * from compone where NAME_MAT="%s" ' % clave)
    except:
        wx.MessageBox(_(u'Error de conexi\xf3n a la base de datos'), _(u'Aviso'))
    finally:
        if c.fetchone() == None:
            try:
                c.close()
            except:
                logging.info(u'Excepcion en: %s' % __name__)

            try:
                bbdd.close()
            except:
                logging.info(u'Excepcion en: %s' % __name__)

            return False
        try:
            c.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            bbdd.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        return True

    return


def compruebaMaterial(material):
    """
    Metodo: compruebaMaterial
    
    
    ARGUMENTOS:
                material:
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = material.encode('iso-8859-15')
        clave = evitaInj(clave)
        c.execute('select * from material where NAME="%s" ' % clave)
    except:
        wx.MessageBox(_(u'Error de conexi\xf3n a la base de datos'), _(u'Aviso'))
    finally:
        if c.fetchone() == None:
            try:
                c.close()
            except:
                logging.info(u'Excepcion en: %s' % __name__)

            try:
                bbdd.close()
            except:
                logging.info(u'Excepcion en: %s' % __name__)

            return False
        try:
            c.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            bbdd.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        return True

    return


def compruebaVidrio(material):
    """
    Metodo: compruebaVidrio
    
    
    ARGUMENTOS:
                material:
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = material.encode('iso-8859-15')
        clave = evitaInj(clave)
        c.execute('select * from vidrio where NAME="%s" ' % clave)
    except:
        wx.MessageBox(_(u'Error de conexi\xf3n a la base de datos'), _(u'Aviso'))
    finally:
        if c.fetchone() == None:
            try:
                c.close()
            except:
                logging.info(u'Excepcion en: %s' % __name__)

            try:
                bbdd.close()
            except:
                logging.info(u'Excepcion en: %s' % __name__)

            return False
        try:
            c.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            bbdd.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        return True

    return


def compruebaMarco(material):
    """
    Metodo: compruebaMarco
    
    
    ARGUMENTOS:
                material:
    """
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = material.encode('iso-8859-15')
        clave = evitaInj(clave)
        c.execute('select * from marco where NAME="%s" ' % clave)
    except:
        wx.MessageBox(_(u'Error de conexi\xf3n a la base de datos'), _(u'Aviso'))
    finally:
        if c.fetchone() == None:
            try:
                c.close()
            except:
                logging.info(u'Excepcion en: %s' % __name__)

            try:
                bbdd.close()
            except:
                logging.info(u'Excepcion en: %s' % __name__)

            return False
        try:
            c.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        try:
            bbdd.close()
        except:
            logging.info(u'Excepcion en: %s' % __name__)

        return True

    return


def cargarMaterial(material):
    """
    Metodo: cargarMaterial
    
    
    ARGUMENTOS:
                material):   ###Llamo a esta funcion:
                le doy nombre del material y me devuelve caracteristic:
    """
    listaMaterial = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        material = material.encode('iso-8859-15')
        c.execute('select * from material where NAME ="%s" ' % material)
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


def cargarVidrio(material):
    """
    Metodo: cargarVidrio
    
    
    ARGUMENTOS:
                material):   ###Llamo a esta funcion:
                le doy nombre del vidrio y me devuelve caracteristic:
    """
    listaVidrio = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        material = material.encode('iso-8859-15')
        c.execute('select * from vidrio where NAME ="%s" ' % material)
        for i in c.fetchall():
            for j in i:
                listaVidrio.append(j)

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

    return listaVidrio


def cargarMarco(material):
    """
    Metodo: cargarMarco
    
    
    ARGUMENTOS:
                material):   ###Llamo a esta funcion:
                le doy nombre del vidrio y me devuelve caracteristic:
    """
    listaMarco = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        material = material.encode('iso-8859-15')
        c.execute('select * from marco where NAME ="%s" ' % material)
        for i in c.fetchall():
            for j in i:
                listaMarco.append(j)

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

    return listaMarco


def cargarMaterial_problemas_acentos(material):
    """
    Metodo: cargarMaterial_problemas_acentos
    
    
    ARGUMENTOS:
                material:
    """
    listaMaterial = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        c.execute('select * from material where NAME ="%s" ' % material)
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


def cargarMateriales(grupo):
    """
    Metodo: cargarMateriales
    
    
    ARGUMENTOS:
                grupo):   ###Me devuelve materiales que hay dentro de un grupo de material:
    """
    listaMateriales = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        clave = grupo.encode('iso-8859-15')
        c.execute('select NAME from material where GRUPO ="%s" ' % clave)
        for i in c.fetchall():
            listaMateriales.append('%s' % i)

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

    return listaMateriales


def probar():
    """
    Metodo: probar
    
    
                :
    """
    listaMateriales = []
    try:
        bbdd = dbapi.connect(Directorio + '/bbdd.dat')
        bbdd.text_factory = str
        c = bbdd.cursor()
        c.execute('select * from material')
        for i in c.fetchall():
            for j in i:
                listaMateriales.append(j)

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