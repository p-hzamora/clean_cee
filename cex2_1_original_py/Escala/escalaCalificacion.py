# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Escala\escalaCalificacion.pyc
# Compiled at: 2014-12-09 16:53:03
"""
Modulo: escalaCalificacion.py
En residencial: Permite leer archivo xml Localidades.xml que cotiene la informacion de la escala
En terciario: Devuelve diccionario con limites IEE entre clases

"""
import xml.etree.ElementTree as etree, directorios
Directorio = directorios.BuscaDirectorios().Directorio

class Escala:
    pass


def firstLower(s):
    """cambia la primera letra a minuscula. Para los nombres de los atributos"""
    return s[0].lower() + s[1:]


def formatoDato(s):
    """Comprueba el formato del dato. Si puede lo pasa a float"""
    if s == 'None':
        pass
    try:
        return float(s)
    except ValueError:
        return s
    except TypeError:
        return s
    except Exception as e:
        return s


def escalaResidencial():
    xml = etree.parse(Directorio + '/Escala/Localidades.xml')
    root = xml.getroot()
    diccEscala = {}
    for zona in root:
        nombreZona = zona.attrib.get('nombre')
        obj1 = Escala()
        for dato in zona:
            if dato.tag != 'Tipo':
                setattr(obj1, firstLower(dato.tag), formatoDato(dato.text))
            else:
                obj2 = Escala()
                setattr(obj1, firstLower(dato.attrib.get('nombre')), obj2)
                for datosResultados in dato:
                    obj3 = Escala()
                    setattr(obj2, firstLower(datosResultados.attrib.get('nombre')), obj3)
                    for valores in datosResultados:
                        if '-' in valores.tag:
                            tag = valores.tag.replace('-', '')
                        else:
                            tag = valores.tag
                        setattr(obj3, tag, formatoDato(valores.text))

        diccEscala[nombreZona] = obj1

    return diccEscala


def escalaTerciario():
    diccLimitesEntreClases = {'AB': 0.4, 'BC': 0.65, 
       'CD': 1.0, 
       'DE': 1.3, 
       'EF': 1.6, 
       'FG': 2.0}
    return diccLimitesEntreClases


def getDiccionarioTemperaturasAguaRedACS():
    xml = etree.parse(Directorio + '/Escala/Localidades.xml')
    root = xml.getroot()
    diccTemperaturaAguaRed = {}
    for zona in root:
        nombreZona = zona.attrib.get('nombre')
        for dato in zona:
            if dato.tag == 'TemperaturaMediaAnual':
                diccTemperaturaAguaRed[nombreZona] = float(dato.text)

    return diccTemperaturaAguaRed


if __name__ == '__main__':
    escala = escalaResidencial()