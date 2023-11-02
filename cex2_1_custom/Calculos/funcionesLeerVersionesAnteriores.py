# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Calculos\funcionesLeerVersionesAnteriores.pyc
# Compiled at: 2015-02-04 16:48:36
from Calculos.listadosWeb import getPosicionKeyEnListado, normativaVigente
from Envolvente.funcionActualizarEnvolvente import actualizarEnvolvente
from Instalaciones.funcionActualizarInstalacionesGeneracion import actualizarInstalacionesGeneracion, actualizarRendimientoConjuntosMM
from MedidasDeMejora.objetoGrupoMejoras import AnalisisEconomicoConjuntoMM, grupoMedidasMejora

def adaptarVersionesAnterioresArchivo(datosArchivo, versionArchivoGuardado):
    diccionarioCadenasARemplazar = {'(imenuCerramientos': '(iLibreriasCE3X.menuCerramientos', '(idatosEdificio\ndatosEdificioInicialesTerciario': '(idatosEdificio\ndatosEdificioIniciales', 
       '(idatosEdificio\ndatosEdificioResultadosTerciario': '(idatosEdificio\ndatosEdificioResultados'}
    for k in diccionarioCadenasARemplazar:
        datosArchivo = datosArchivo.replace(k, diccionarioCadenasARemplazar[k])

    return datosArchivo


def adaptarVersionesAnterioresEnvolvente(datosEnvolvente, datosGenerales, versionArchivoGuardado):
    zonaHE1 = datosGenerales[4]
    zonaNBE = datosGenerales[15]
    normVig = datosGenerales[0]
    posicionNormativaVigente = getPosicionKeyEnListado(listado=normativaVigente, elemento=normVig)
    listadoCerramientos = datosEnvolvente[0]
    if versionArchivoGuardado < 2.0:
        listadoCerramientos = actualizarEnvolvente(listadoCerramientos=listadoCerramientos, normativaVigente=posicionNormativaVigente, zonaHE1=zonaHE1, zonaNBE=zonaNBE)
    datosEnvolvente[0] = listadoCerramientos
    return datosEnvolvente


def adaptarVersionesAnterioresInstalaciones(datosInstalaciones, datosGenerales, versionArchivoGuardado, programa):
    zonaHE1 = datosGenerales[4]
    tipoEdificio = datosGenerales[1]
    if zonaHE1 == '' or tipoEdificio == '':
        return datosInstalaciones
    if versionArchivoGuardado < 2.0:
        instalacionACS, instalacionCalefaccion, instalacionRefrigeracion, instalacionClimatizacion, instalacionMixto2, instalacionMixto3 = actualizarInstalacionesGeneracion(instACS=datosInstalaciones[0], instCal=datosInstalaciones[1], instRef=datosInstalaciones[2], instClima=datosInstalaciones[3], instMixto2=datosInstalaciones[4], instMixto3=datosInstalaciones[5], zonaHE1=zonaHE1, programa=programa, tipoEdificio=tipoEdificio)
        datosInstalaciones[0] = instalacionACS
        datosInstalaciones[1] = instalacionCalefaccion
        datosInstalaciones[2] = instalacionRefrigeracion
        datosInstalaciones[3] = instalacionClimatizacion
        datosInstalaciones[4] = instalacionMixto2
        datosInstalaciones[5] = instalacionMixto3
    return datosInstalaciones


def adaptarVersionesAnterioresInstalacionesConjuntosMM(datosMM, datosGenerales, versionArchivoGuardado, programa):
    mensajeAviso = ''
    zonaHE1 = datosGenerales[4]
    tipoEdificio = datosGenerales[1]
    if zonaHE1 == '' or tipoEdificio == '':
        return (datosMM, mensajeAviso)
    listadoConjuntosMM = []
    if versionArchivoGuardado < 2.0:
        for conjuntoMM in datosMM:
            if isinstance(conjuntoMM, grupoMedidasMejora):
                listadoConjuntosMM.append(conjuntoMM)
            else:
                mensajeAviso += '    - %s\n' % conjuntoMM.nombre

        listadoConjuntosMM = actualizarRendimientoConjuntosMM(listadoConjuntosMM=listadoConjuntosMM, zonaHE1=zonaHE1, programa=programa, tipoEdificio=tipoEdificio)
    else:
        listadoConjuntosMM = datosMM
    return (
     listadoConjuntosMM, mensajeAviso)


def adaptarVersionesAnterioresMM(datosMM, versionArchivoGuardado):
    if versionArchivoGuardado <= 2.0:
        for conjuntoMM in datosMM:
            if hasattr(conjuntoMM, 'caracteristicas') == False:
                setattr(conjuntoMM, 'caracteristicas', '')
            if hasattr(conjuntoMM, 'otrosDatos') == False:
                setattr(conjuntoMM, 'otrosDatos', '')
            if hasattr(conjuntoMM, 'datosEdificioOriginal') == False:
                setattr(conjuntoMM, 'datosEdificioOriginal', None)
            if hasattr(conjuntoMM, 'inversionInicial') == False:
                setattr(conjuntoMM, 'inversionInicial', None)
            if hasattr(conjuntoMM, 'costeMantenimientoAnual') == False:
                setattr(conjuntoMM, 'costeMantenimientoAnual', None)
            if hasattr(conjuntoMM, 'analisisEconomico') == False:
                atributoAnalisisEconomico = AnalisisEconomicoConjuntoMM()
                setattr(conjuntoMM, 'analisisEconomico', atributoAnalisisEconomico)

    return datosMM