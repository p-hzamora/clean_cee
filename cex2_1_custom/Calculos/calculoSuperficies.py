# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Calculos\calculoSuperficies.pyc
# Compiled at: 2015-02-19 13:18:33
"""
Modulo: calculrSuperficies.py

"""
import logging

def calcularSuperficieSegunPorcentajeCubierto(nuevaSuperficie, porcentajeCubierto):
    """
    Funcion: calcularSuperficieSegunPorcentajeCubierto

    ARGUMENTOS:
                nuevaSuperficie:
                porcentajeCubierto:
    """
    nuevaSuperficie = float(nuevaSuperficie)
    porcentajeCubierto = float(porcentajeCubierto)
    m2Cubiertos = nuevaSuperficie * porcentajeCubierto / 100.0
    m2Cubiertos = round(m2Cubiertos, 2)
    return m2Cubiertos


def actualizarSuperficiesInstalaciones(listadoInstalaciones, superficieCambiada, zonaCambiada):
    """
    Funcion: actualizarSuperficiesInstalaciones

    ARGUMENTOS:
                listadoInstalaciones:
                superficieCambiada: nueva superficie
                zonaCambiada: zona que ha cambiado. Puede ser el Edificio Objeto
    """
    for tipoInst in listadoInstalaciones:
        for inst in tipoInst:
            porcCubiertoACS = inst[5][0][1]
            porcCubiertoCal = inst[5][1][1]
            porcCubiertoRef = inst[5][2][1]
            zonaSeleccionada = inst[-1]
            if zonaSeleccionada == zonaCambiada:
                if porcCubiertoACS != '':
                    m2CubiertosACS = calcularSuperficieSegunPorcentajeCubierto(superficieCambiada, porcCubiertoACS)
                    inst[5][0][0] = str(m2CubiertosACS)
                if porcCubiertoCal != '':
                    m2CubiertosCal = calcularSuperficieSegunPorcentajeCubierto(superficieCambiada, porcCubiertoCal)
                    inst[5][1][0] = str(m2CubiertosCal)
                if porcCubiertoRef != '':
                    m2CubiertosRef = calcularSuperficieSegunPorcentajeCubierto(superficieCambiada, porcCubiertoRef)
                    inst[5][2][0] = str(m2CubiertosRef)

    return listadoInstalaciones


def actualizarSuperficiesIluminacion(subgrupos, superficieHabitable, arrayIluminacion):
    """
    Metodo: ActualizarSuperficiesIluminacion

    ARGUMENTOS:
                subgrupos:
                 superficieHabitable:
                 arrayIluminacion:
        Por ejemplo, si edificio = 100 m2 y tengo dos subzonas de 30m2 y 20m2, a edificio solo puedo asignar iluminacion de 50 m2. En GT
    """
    try:
        float(superficieHabitable)
    except:
        logging.info('Excepcion en: %s' % __name__)
        return arrayIluminacion

    dicc = {}
    areaTotalZonas = 0
    for sub1 in subgrupos:
        area = float(sub1.superficie)
        if sub1.raiz == 'Edificio Objeto':
            areaTotalZonas += area
        areaSubzonas = 0
        for sub2 in subgrupos:
            if sub2.raiz == sub1.nombre:
                areaSubzonas += float(sub2.superficie)

        area = area - areaSubzonas
        dicc[sub1.nombre] = area

    dicc['Edificio Objeto'] = float(superficieHabitable) - areaTotalZonas
    for inst in arrayIluminacion:
        areaIluminada = dicc[inst[-1]]
        inst[5] = str(areaIluminada)
        control = inst[10]
        if control[0] == True:
            if float(control[1]) > areaIluminada:
                inst[10][1] = str(areaIluminada)

    return arrayIluminacion