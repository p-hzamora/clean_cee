# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: moduloXML\funcionesXML.pyc
# Compiled at: 2015-05-27 14:02:59


def calculoUhueco(Uvidrio, Umarco, porcMarco):
    Uhueco = Uvidrio * (100.0 - porcMarco) / 100.0 + Umarco * porcMarco / 100.0
    return round(Uhueco, 2)


def calculoVolumenEspacioHabitable(superficie, altura):
    volumenEspacioHabitable = superficie * altura
    return volumenEspacioHabitable


def calculoPorcentajeCubiertoInstalacion(listadoInstalaciones, superficie):
    """
    Calcula el porcentaje cubierto por una instalacion
    listadoInstalaciones: obj ListadoEquipoGeneracion de datosEdificio
    """
    porcentajeCubierto = listadoInstalaciones.coberturaM2 / superficie * 100.0
    return porcentajeCubierto


def calculoCompacidad(listadoCerramientos, volumenEspacioHabitable):
    """
    listadoCerramientos: array con objetos de tipo Cerramiento de datosEdificio
    """
    superficieTotalCerr = 0.0
    for cerr in listadoCerramientos:
        if cerr.enContactoCon != 'edificio':
            superficieTotalCerr += cerr.superficieBruta

    compacidad = volumenEspacioHabitable / superficieTotalCerr
    return compacidad


def calculoSuperficieAcristalada(listadoCerramientos, orientacion):
    """
    listadoCerramientos: array con objetos de tipo Cerramiento de datosEdificio
    """
    superficieBrutaTotal = 0.0
    superficieNetaTotal = 0.0
    for cerr in listadoCerramientos:
        if cerr.orientacion == orientacion:
            superficieBrutaTotal += cerr.superficieBruta
            superficieNetaTotal += cerr.superficieNeta

    superficieHuecos = superficieBrutaTotal - superficieNetaTotal
    if superficieBrutaTotal > 0.0:
        porcentajeHuecos = superficieHuecos / superficieBrutaTotal * 100.0
    else:
        porcentajeHuecos = 0.0
    return porcentajeHuecos


def getValorVariable(variable):
    if variable != '':
        try:
            if float(variable) > 0.0:
                nuevaVariable = float(variable)
            else:
                nuevaVariable = 0.0
        except:
            nuevaVariable = 0.0

    else:
        nuevaVariable = 0.0
    return nuevaVariable


def calculoDemandaConjunta(extrapeninsular, ddaCal, ddaRef):
    if extrapeninsular == False:
        coefPonderacion = 0.7
    else:
        coefPonderacion = 0.85
    ddaConjunta = ddaCal + coefPonderacion * ddaRef
    return ddaConjunta