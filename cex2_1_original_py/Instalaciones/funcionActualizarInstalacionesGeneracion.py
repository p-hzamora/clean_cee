# Embedded file name: Instalaciones\funcionActualizarInstalacionesGeneracion.pyc
from Calculos.listadosWeb import listadoOpcionesBdC
from Instalaciones.funcionCalculoRendimientoEstacional import calculoRendimientoMedioEstacional
from MedidasDeMejora.objetoGrupoMejoras import grupoMedidasMejora

def actualizarInstalacionesGeneracion(instACS, instCal, instRef, instClima, instMixto2, instMixto3, zonaHE1, programa, tipoEdificio):
    """
    M\xe9todo: actualizarInstalacionesGeneracion
    Argumentos:
                instACS, instCal... :array con datos de instalaciones
                zonaHE1, 
                programa: Residencial, Peque\xf1oTerciario, GranTerciario
                uso: Residencial o Intensidad Media - 12 h....
    Devuelve los array actualizados: instACS, instCal...
    """
    instACS = actualizarInstalacionesGeneracionSegunTipo(instalacionesGeneracion=instACS, zonaHE1=zonaHE1, programa=programa, tipoEdificio=tipoEdificio)
    instCal = actualizarInstalacionesGeneracionSegunTipo(instalacionesGeneracion=instCal, zonaHE1=zonaHE1, programa=programa, tipoEdificio=tipoEdificio)
    instRef = actualizarInstalacionesGeneracionSegunTipo(instalacionesGeneracion=instRef, zonaHE1=zonaHE1, programa=programa, tipoEdificio=tipoEdificio)
    instClima = actualizarInstalacionesGeneracionSegunTipo(instalacionesGeneracion=instClima, zonaHE1=zonaHE1, programa=programa, tipoEdificio=tipoEdificio)
    instMixto2 = actualizarInstalacionesGeneracionSegunTipo(instalacionesGeneracion=instMixto2, zonaHE1=zonaHE1, programa=programa, tipoEdificio=tipoEdificio)
    instMixto3 = actualizarInstalacionesGeneracionSegunTipo(instalacionesGeneracion=instMixto3, zonaHE1=zonaHE1, programa=programa, tipoEdificio=tipoEdificio)
    return (instACS,
     instCal,
     instRef,
     instClima,
     instMixto2,
     instMixto3)


def actualizarInstalacionesGeneracionSegunTipo(instalacionesGeneracion, zonaHE1, programa, tipoEdificio):
    """
    Argumentos: instalacionesGeneracion: array con datos instalaciones de generacion:
                                         acs, cal, ref, mixto2, clima, mixto3 (le llega de un tipo)
                zonaHE1
                programa: Residencial, peque\xf1oTerciario, GranTerciario
                tipoEdificio: Intensidad Media - 12 h
    
    Devuelve el nuevo array con los equipos
                
    """
    for equipo in instalacionesGeneracion:
        nombre = equipo[0]
        tipoInstalacion = equipo[1]
        rendEstACS_antiguo, rendEstCal_antiguo, rendEstRef_antiguo = equipo[2]
        tipoEquipo = equipo[3]
        combustible = equipo[4]
        cobertura = equipo[5]
        modoDefinicion = equipo[6]
        datosEquipo = equipo[7]
        kwargs = {}
        if modoDefinicion == u'Conocido (Ensayado/justificado)':
            pass
        else:
            if modoDefinicion == u'Estimado seg\xfan Instalaci\xf3n':
                if tipoEquipo in (u'Caldera Est\xe1ndar', u'Caldera Condensaci\xf3n', u'Caldera Baja Temperatura') and combustible != u'Electricidad':
                    kwargsCalderaEst = getkwargsCalderaEst(datosEquipo, tipoInstalacion)
                    kwargs.update(kwargsCalderaEst)
                elif tipoEquipo == u'Efecto Joule' or tipoEquipo in (u'Caldera Est\xe1ndar', u'Caldera Condensaci\xf3n', u'Caldera Baja Temperatura') and combustible == u'Electricidad':
                    kwargsJouleEst = getkwargsJouleEst(datosEquipo, tipoInstalacion)
                    kwargs.update(kwargsJouleEst)
                else:
                    kwargsBdCEst = getkwargsBdCEst(datosEquipo, tipoInstalacion)
                    kwargs.update(kwargsBdCEst)
            elif tipoEquipo in (u'Caldera Est\xe1ndar', u'Caldera Condensaci\xf3n', u'Caldera Baja Temperatura') and combustible != u'Electricidad':
                kwargsCalderaSgCurva = getkwargsCalderaEstSgCurva(datosEquipo, tipoInstalacion)
                kwargs.update(kwargsCalderaSgCurva)
            else:
                kwargsBdCSgCurva = getkwargsBdCEstSgCurva(datosEquipo, tipoInstalacion)
                kwargs.update(kwargsBdCSgCurva)
            resultado = calculoRendimientoMedioEstacional(zonaHE1=zonaHE1, programa=programa, tipoEdificio=tipoEdificio, tipoInstalacion=tipoInstalacion, modoDefinicion=modoDefinicion, tipoEquipo=tipoEquipo, combustible=combustible, **kwargs)
            rendEstACS = ''
            rendEstCal = ''
            rendEstRef = ''
            if tipoInstalacion == 'ACS':
                rendEstACS = resultado
            elif tipoInstalacion == 'calefaccion':
                if modoDefinicion == u'Estimado seg\xfan Instalaci\xf3n' and tipoEquipo not in (u'Caldera Est\xe1ndar', u'Caldera Condensaci\xf3n', u'Caldera Baja Temperatura', u'Efecto Joule', u'Equipo de Rendimiento Constante'):
                    rendEstCal, fraccionEnergia = resultado
                else:
                    rendEstCal = resultado
            elif tipoInstalacion == 'refrigeracion':
                if modoDefinicion == u'Estimado seg\xfan Instalaci\xf3n':
                    rendEstRef, fraccionEnergia = resultado
                else:
                    rendEstRef = resultado
            elif tipoInstalacion == 'climatizacion':
                rendEstCal, rendEstRef = resultado
            elif tipoInstalacion == 'mixto2':
                if modoDefinicion == u'Estimado seg\xfan Instalaci\xf3n' and tipoEquipo in (u'Caldera Est\xe1ndar', u'Caldera Condensaci\xf3n', u'Caldera Baja Temperatura', u'Efecto Joule'):
                    rendEstACS = resultado
                    rendEstCal = resultado
                else:
                    rendEstACS, rendEstCal = resultado
            elif tipoInstalacion == 'mixto3':
                rendEstACS, rendEstCal, rendEstRef = resultado
            equipo[2] = [rendEstACS, rendEstCal, rendEstRef]

    return instalacionesGeneracion


def getkwargsCalderaEst(datosEquipo, tipoInstalacion):
    aislanteCaldera = datosEquipo[0]
    rendCombCaldera = datosEquipo[1]
    cargaMediaCaldera = datosEquipo[2]
    potenciaCaldera = datosEquipo[3]
    kwargsCalderaEst = {'aislanteCaldera': aislanteCaldera,
     'rendCombCaldera': rendCombCaldera,
     'potenciaCaldera': potenciaCaldera,
     'cargaMediaCaldera': cargaMediaCaldera}
    return kwargsCalderaEst


def getkwargsJouleEst(datosEquipo, tipoInstalacion):
    arrayRendimientoNominal = datosEquipo[0]
    array_antiguedad = datosEquipo[1]
    array_variosGeneradores = datosEquipo[2]
    if tipoInstalacion in ('ACS', 'mixto2'):
        rendNominal = arrayRendimientoNominal[0]
    elif tipoInstalacion == 'calefaccion':
        rendNominal = arrayRendimientoNominal[1]
    kwargsJouleEst = {'rendNominal': rendNominal}
    return kwargsJouleEst


def getkwargsBdCEst(datosEquipo, tipoInstalacion):
    arrayRendimientoNominal = datosEquipo[0]
    array_antiguedad = datosEquipo[1]
    array_variosGeneradores = datosEquipo[2]
    rendNominalACS = arrayRendimientoNominal[0]
    rendNominalCal = arrayRendimientoNominal[1]
    rendNominalRef = arrayRendimientoNominal[2]
    if tipoInstalacion in ('ACS', 'calefaccion', 'refrigeracion'):
        variosGeneradoresCheck = array_variosGeneradores[0]
        fraccionPotencia = array_variosGeneradores[1]
        fraccionPotenciaEntrada = array_variosGeneradores[2]
    else:
        variosGeneradoresCheck = False
        fraccionPotencia = ''
        fraccionPotenciaEntrada = ''
    if tipoInstalacion == 'refrigeracion':
        tipoBdC = listadoOpcionesBdC[datosEquipo[3]][0]
    else:
        tipoBdC = ''
    kwargsBdCEst = {'rendNominalACS': rendNominalACS,
     'rendNominalCal': rendNominalCal,
     'rendNominalRef': rendNominalRef,
     'variosGeneradoresCheck': variosGeneradoresCheck,
     'fraccionPotencia': fraccionPotencia,
     'fraccionPotenciaEntrada': fraccionPotenciaEntrada,
     'tipoBdC': tipoBdC}
    return kwargsBdCEst


def getkwargsCalderaEstSgCurva(datosEquipo, tipoInstalacion):
    potNominal = datosEquipo[0]
    rendNominalPG = datosEquipo[1]
    factorCargaMinimo = datosEquipo[2]
    factorCargaMaximo = datosEquipo[3]
    temperaturaAmbienteInt = datosEquipo[4]
    temperaturas = datosEquipo[5]
    curvaRendimiento = datosEquipo[6]
    kwargsCalderaSgCurva = {'curvaRendimiento': curvaRendimiento,
     'rendNominalPG': rendNominalPG,
     'factorCargaMinimo': factorCargaMinimo,
     'factorCargaMaximo': factorCargaMaximo,
     'potNominal': potNominal,
     'temperaturas': temperaturas}
    return kwargsCalderaSgCurva


def getkwargsBdCEstSgCurva(datosEquipo, tipoInstalacion):
    potNominal = datosEquipo[0]
    rendNominalPG = datosEquipo[1]
    factorCargaMinimo = datosEquipo[2]
    factorCargaMaximo = datosEquipo[3]
    temperaturaAmbienteInt = datosEquipo[4]
    temperaturas = datosEquipo[5]
    curvaRendimiento = datosEquipo[6]
    if tipoInstalacion == 'refrigeracion':
        tipoBdC = listadoOpcionesBdC[datosEquipo[7]][0]
    else:
        tipoBdC = ''
    kwargsBdCSgCurva = {'curvaRendimiento': curvaRendimiento,
     'rendNominalPG': rendNominalPG,
     'factorCargaMinimo': factorCargaMinimo,
     'factorCargaMaximo': factorCargaMaximo,
     'potNominal': potNominal,
     'temperaturaAmbienteInt': temperaturaAmbienteInt,
     'tipoBdC': tipoBdC}
    return kwargsBdCSgCurva


def actualizarRendimientoConjuntosMM(listadoConjuntosMM, zonaHE1, programa, tipoEdificio):
    """
    M\xe9todo: actualizarRendimientoConjuntosMM
    Argumentos: listadoConjuntosMM, zonaHE1, programa, tipoEdificio
    Devuelve el listado de conjuntos de medidas de mejora con los rendimientos actualizados
    
    """
    for conjuntoMM in listadoConjuntosMM:
        if isinstance(conjuntoMM, grupoMedidasMejora):
            if conjuntoMM.mejoras[1][2] == True:
                instalacionACS, instalacionCalefaccion, instalacionRefrigeracion, instalacionClimatizacion, instalacionMixto2, instalacionMixto3 = actualizarInstalacionesGeneracion(instACS=conjuntoMM.mejoras[1][1][0], instCal=conjuntoMM.mejoras[1][1][1], instRef=conjuntoMM.mejoras[1][1][2], instClima=conjuntoMM.mejoras[1][1][3], instMixto2=conjuntoMM.mejoras[1][1][4], instMixto3=conjuntoMM.mejoras[1][1][5], zonaHE1=zonaHE1, programa=programa, tipoEdificio=tipoEdificio)
                conjuntoMM.mejoras[1][1][0] = instalacionACS
                conjuntoMM.mejoras[1][1][1] = instalacionCalefaccion
                conjuntoMM.mejoras[1][1][2] = instalacionRefrigeracion
                conjuntoMM.mejoras[1][1][3] = instalacionClimatizacion
                conjuntoMM.mejoras[1][1][4] = instalacionMixto2
                conjuntoMM.mejoras[1][1][5] = instalacionMixto3

    return listadoConjuntosMM