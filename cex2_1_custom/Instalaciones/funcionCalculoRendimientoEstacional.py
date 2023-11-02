# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\funcionCalculoRendimientoEstacional.pyc
# Compiled at: 2015-02-19 13:18:33
from Instalaciones import tablasValoresInstalaciones, perfilesTerciario, equipos
from Instalaciones.equipos import estimacionRendimientoEstacionalBDCACS, estimacionRendimientoEstacionalBDCCalefaccion, estimacionRendimientoEstacionalBDCRefrigeracion, estimacionRendimientoEstacionalBDCRefrigeracionCondensadaAgua
import logging
degradacionAntiguedad = 1.0
fcpSistema = [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]

def calculoRendimientoMedioEstacional(zonaHE1, programa, tipoEdificio, tipoInstalacion, modoDefinicion, tipoEquipo, combustible, **kwargs):
    for key in kwargs:
        if isinstance(kwargs[key], str) or isinstance(kwargs[key], unicode):
            exec '%s = "%s"' % (key, kwargs[key])
        else:
            exec '%s = %s' % (key, kwargs[key])

    if 'rendEstACS' not in kwargs:
        rendEstACS = ''
    if 'rendEstCal' not in kwargs:
        rendEstCal = ''
    if 'rendEstRef' not in kwargs:
        rendEstRef = ''
    if 'rendNominalACS' not in kwargs:
        rendNominalACS = ''
    if 'rendNominalCal' not in kwargs:
        rendNominalCal = ''
    if 'rendNominalRef' not in kwargs:
        rendNominalRef = ''
    if 'variosGeneradoresCheck' not in kwargs:
        variosGeneradoresCheck = False
    if 'fraccionPotencia' not in kwargs or variosGeneradoresCheck == False:
        fraccionPotencia = 1.0
    if 'fraccionPotenciaEntrada' not in kwargs or variosGeneradoresCheck == False:
        fraccionPotenciaEntrada = 0.0
    if 'tipoBdC' not in kwargs:
        tipoBdC = ''
    if programa == 'Residencial':
        usoEdificio = 'Residencial'
    else:
        usoEdificio = tipoEdificio
    if modoDefinicion == 'Conocido (Ensayado/justificado)':
        resultado = calculoRendEstEquipoConocido(tipoInstalacion, rendEstACS, rendEstCal, rendEstRef)
        return resultado
    if modoDefinicion == 'Estimado según Instalación':
        if tipoEquipo in ('Caldera Estándar', 'Caldera Condensación', 'Caldera Baja Temperatura') and combustible != 'Electricidad':
            resultado = calculoRendEstCalderaEstimada(tipoInstalacion, tipoEquipo, combustible, aislanteCaldera, rendCombCaldera, potenciaCaldera, cargaMediaCaldera)
            return resultado
        else:
            if tipoEquipo == 'Efecto Joule' or tipoEquipo in ('Caldera Estándar', 'Caldera Condensación',
                                                              'Caldera Baja Temperatura') and combustible == 'Electricidad':
                resultado = calculoRendEstEfectoJoule(rendNominal)
                return resultado
            resultado = calculoRendEstBdCEstimada(tipoInstalacion, tipoEquipo, zonaHE1, usoEdificio, rendNominalACS, rendNominalCal, rendNominalRef, variosGeneradoresCheck, fraccionPotencia, fraccionPotenciaEntrada, tipoBdC)
            return resultado

    else:
        if tipoEquipo in ('Caldera Estándar', 'Caldera Condensación', 'Caldera Baja Temperatura') and combustible != 'Electricidad':
            resultado = calculoRendEstCalderaEstimadaSgCurva(tipoInstalacion, tipoEquipo, zonaHE1, usoEdificio, curvaRendimiento, rendNominalPG, factorCargaMinimo, factorCargaMaximo, potNominal, temperaturas)
            return resultado
        else:
            resultado = calculoRendEstBdCEstimadaSgCurva(tipoInstalacion, tipoEquipo, zonaHE1, usoEdificio, curvaRendimiento, rendNominalPG, factorCargaMinimo, factorCargaMaximo, potNominal, temperaturaAmbienteInt, tipoBdC)
            return resultado


def calculoPropiedadesTermicasBDCEstimada_ACS(tipoEquipo, zonaHE1, usoEdificio, rendNominal, fraccionPotencia, fraccionPotenciaEntrada):
    fraccionEnergia, rendEst = estimacionRendimientoEstacionalBDCACS(zonaHE1, usoEdificio, tipoEquipo, rendNominal, fraccionPotenciaEntrada, fraccionPotencia)
    rendEst = round(degradacionAntiguedad * rendEst, 1)
    return (fraccionEnergia, rendEst)


def calculoPropiedadesTermicasBDCEstimada_Cal(tipoEquipo, zonaHE1, usoEdificio, rendNominal, fraccionPotencia, fraccionPotenciaEntrada):
    fraccionEnergia, rendEst = estimacionRendimientoEstacionalBDCCalefaccion(zonaHE1, usoEdificio, tipoEquipo, rendNominal, fraccionPotenciaEntrada, fraccionPotencia)
    rendEst = round(degradacionAntiguedad * rendEst, 1)
    return (
     fraccionEnergia, rendEst)


def calculoPropiedadesTermicasBDCEstimada_Ref(tipoEquipo, zonaHE1, usoEdificio, rendNominal, fraccionPotencia, fraccionPotenciaEntrada, tipoBdC):
    if tipoBdC in ('Aire-Aire', 'Aire-Agua', ''):
        fraccionEnergia, rendEst = estimacionRendimientoEstacionalBDCRefrigeracion(zonaHE1, usoEdificio, tipoEquipo, rendNominal, fraccionPotenciaEntrada, fraccionPotencia)
    else:
        fraccionEnergia, rendEst = estimacionRendimientoEstacionalBDCRefrigeracionCondensadaAgua(zonaHE1, usoEdificio, tipoEquipo, rendNominal, fraccionPotenciaEntrada, fraccionPotencia)
    rendEst = round(degradacionAntiguedad * rendEst, 1)
    return (
     fraccionEnergia, rendEst)


def calculoRendEstEquipoConocido(tipoInstalacion, rendEstACS, rendEstCal, rendEstRef):
    if tipoInstalacion == 'ACS':
        return rendEstACS
    if tipoInstalacion == 'calefaccion':
        return rendEstCal
    if tipoInstalacion in 'refrigeracion':
        return rendEstRef
    if tipoInstalacion == 'climatizacion':
        return (rendEstCal, rendEstRef)
    if tipoInstalacion == 'mixto2':
        return (rendEstACS, rendEstCal)
    if tipoInstalacion == 'mixto3':
        return (rendEstACS, rendEstCal, rendEstRef)


def calculoRendEstEfectoJoule(rendNominal):
    rendEst = rendNominal
    try:
        rendEst = round(float(rendNominal), 1)
    except:
        logging.info('Excepcion en: %s' % __name__)
        rendEst = ''

    return rendEst


def calculoRendEstCalderaEstimada(tipoInstalacion, tipoEquipo, combustible, aislanteCaldera, rendCombCaldera, potenciaCaldera, cargaMediaCaldera):
    vectorTipoCaldera = [
     False, False, True, False, False, True, False]
    objRendimientos = tablasValoresInstalaciones.tablasValores(tipoInstalacion, [
     tipoEquipo, combustible, aislanteCaldera, rendCombCaldera, potenciaCaldera, 
     cargaMediaCaldera, vectorTipoCaldera], 'Caldera', 'Estimado')
    if tipoInstalacion == 'ACS':
        rendEstacional = objRendimientos.rendimientoEstacionalACS
    else:
        rendEstacional = objRendimientos.rendimientoEstacionalCal
    try:
        rendEstacional = round(float(rendEstacional), 1)
    except:
        logging.info('Excepcion en: %s' % __name__)

    return rendEstacional


def calculoRendEstBdCEstimada(tipoInstalacion, tipoEquipo, zonaHE1, usoEdificio, rendNominalACS, rendNominalCal, rendNominalRef, variosGeneradoresCheck, fraccionPotencia, fraccionPotenciaEntrada, tipoBdC):
    fraccionEnergia = ''
    rendEstACS = ''
    rendEstCal = ''
    rendEstRef = ''
    if variosGeneradoresCheck == False:
        fraccionPotencia = 1.0
        fraccionPotenciaEntrada = 0.0
    if tipoInstalacion == 'ACS':
        try:
            aux, rendEstACS = calculoPropiedadesTermicasBDCEstimada_ACS(tipoEquipo, zonaHE1, usoEdificio, float(rendNominalACS), float(fraccionPotencia), float(fraccionPotenciaEntrada))
        except:
            logging.info('Excepcion en: %s' % __name__)

        return rendEstACS
    if tipoInstalacion == 'calefaccion':
        try:
            fraccionEnergia, rendEstCal = calculoPropiedadesTermicasBDCEstimada_Cal(tipoEquipo, zonaHE1, usoEdificio, float(rendNominalCal), float(fraccionPotencia), float(fraccionPotenciaEntrada))
        except:
            logging.info('Excepcion en: %s' % __name__)

        return (
         rendEstCal, fraccionEnergia)
    if tipoInstalacion in 'refrigeracion':
        try:
            fraccionEnergia, rendEstRef = calculoPropiedadesTermicasBDCEstimada_Ref(tipoEquipo, zonaHE1, usoEdificio, float(rendNominalRef), float(fraccionPotencia), float(fraccionPotenciaEntrada), tipoBdC)
        except:
            logging.info('Excepcion en: %s' % __name__)

        return (
         rendEstRef, fraccionEnergia)
    if tipoInstalacion == 'climatizacion':
        try:
            aux, rendEstCal = calculoPropiedadesTermicasBDCEstimada_Cal(tipoEquipo, zonaHE1, usoEdificio, float(rendNominalCal), float(fraccionPotencia), float(fraccionPotenciaEntrada))
        except:
            logging.info('Excepcion en: %s' % __name__)

        try:
            aux, rendEstRef = calculoPropiedadesTermicasBDCEstimada_Ref(tipoEquipo, zonaHE1, usoEdificio, float(rendNominalRef), float(fraccionPotencia), float(fraccionPotenciaEntrada), tipoBdC)
        except:
            logging.info('Excepcion en: %s' % __name__)

        return (
         rendEstCal, rendEstRef)
    if tipoInstalacion == 'mixto2':
        try:
            aux, rendEstACS = calculoPropiedadesTermicasBDCEstimada_ACS(tipoEquipo, zonaHE1, usoEdificio, float(rendNominalACS), float(fraccionPotencia), float(fraccionPotenciaEntrada))
        except:
            logging.info('Excepcion en: %s' % __name__)

        try:
            aux, rendEstCal = calculoPropiedadesTermicasBDCEstimada_Cal(tipoEquipo, zonaHE1, usoEdificio, float(rendNominalCal), float(fraccionPotencia), float(fraccionPotenciaEntrada))
        except:
            logging.info('Excepcion en: %s' % __name__)

        return (
         rendEstACS, rendEstCal)
    if tipoInstalacion == 'mixto3':
        try:
            aux, rendEstACS = calculoPropiedadesTermicasBDCEstimada_ACS(tipoEquipo, zonaHE1, usoEdificio, float(rendNominalACS), float(fraccionPotencia), float(fraccionPotenciaEntrada))
        except:
            logging.info('Excepcion en: %s' % __name__)

        try:
            aux, rendEstCal = calculoPropiedadesTermicasBDCEstimada_Cal(tipoEquipo, zonaHE1, usoEdificio, float(rendNominalCal), float(fraccionPotencia), float(fraccionPotenciaEntrada))
        except:
            logging.info('Excepcion en: %s' % __name__)

        try:
            aux, rendEstRef = calculoPropiedadesTermicasBDCEstimada_Ref(tipoEquipo, zonaHE1, usoEdificio, float(rendNominalRef), float(fraccionPotencia), float(fraccionPotenciaEntrada), tipoBdC)
        except:
            logging.info('Excepcion en: %s' % __name__)

        return (
         rendEstACS, rendEstCal, rendEstRef)


def calculoRendEstCalderaEstimadaSgCurva(tipoInstalacion, tipoEquipo, zonaHE1, usoEdificio, curvaRendimiento, rendNominalPG, factorCargaMinimo, factorCargaMaximo, potNominal, temperaturas):
    rendEst = ''
    try:
        if tipoInstalacion == 'ACS':
            repartoEnergiaPorcentualCaracteristico = [
             0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
             0.0, 1.0]
        elif tipoInstalacion == 'calefaccion':
            repartoEnergiaPorcentualCaracteristico = perfilesTerciario.PerfilDemandaCalefaccion(zonaHE1, usoEdificio)
        if tipoEquipo == 'Caldera Estándar':
            caldera = equipos.CalderaConvencional()
            caldera.c1 = float(curvaRendimiento[0])
            caldera.c2 = float(curvaRendimiento[1])
            caldera.c3 = float(curvaRendimiento[2])
            caldera.c4 = float(curvaRendimiento[3])
            caldera.rendimientoNominalPlenaCarga = float(rendNominalPG)
            caldera.fcpMin = float(factorCargaMinimo)
            caldera.fcpMax = float(factorCargaMaximo)
            caldera.potenciaNominal = float(potNominal)
            potenciaEnCadaFcp = [ caldera.potFcp(x) for x in fcpSistema ]
        elif tipoEquipo == 'Caldera Condensación':
            caldera = equipos.CalderaCondensacion()
            caldera.c1 = float(curvaRendimiento[0])
            caldera.c2 = float(curvaRendimiento[1])
            caldera.c3 = float(curvaRendimiento[2])
            caldera.c4 = float(curvaRendimiento[3])
            caldera.c5 = float(curvaRendimiento[4])
            caldera.c6 = float(curvaRendimiento[5])
            caldera.rendimientoNominalPlenaCarga = float(rendNominalPG)
            caldera.fcpMin = float(factorCargaMinimo)
            caldera.fcpMax = float(factorCargaMaximo)
            caldera.tempMin = float(temperaturas[0])
            caldera.tempMax = float(temperaturas[1])
            caldera.potenciaNominal = float(potNominal)
            potenciaEnCadaFcp = [ caldera.potFcpT(x, float(temperaturas[2])) for x in fcpSistema ]
        elif tipoEquipo == 'Caldera Baja Temperatura':
            caldera = equipos.CalderaBajaTemperatura()
            caldera.c1 = float(curvaRendimiento[0])
            caldera.c2 = float(curvaRendimiento[1])
            caldera.c3 = float(curvaRendimiento[2])
            caldera.c4 = float(curvaRendimiento[3])
            caldera.c5 = float(curvaRendimiento[4])
            caldera.c6 = float(curvaRendimiento[5])
            caldera.c7 = float(curvaRendimiento[6])
            caldera.c8 = float(curvaRendimiento[7])
            caldera.c9 = float(curvaRendimiento[8])
            caldera.c10 = float(curvaRendimiento[9])
            caldera.rendimientoNominalPlenaCarga = float(rendNominalPG)
            caldera.fcpMin = float(factorCargaMinimo)
            caldera.fcpMax = float(factorCargaMaximo)
            caldera.tempMin = float(temperaturas[0])
            caldera.tempMax = float(temperaturas[1])
            caldera.potenciaNominal = float(potNominal)
            potenciaEnCadaFcp = [ caldera.potFcpT(x, float(temperaturas[2])) for x in fcpSistema ]
        rendEst = sum([ repartoEnergiaPorcentualCaracteristico[i] * fcpSistema[i] * float(potNominal) / potenciaEnCadaFcp[i] for i in range(len(potenciaEnCadaFcp))
                      ])
        rendEst = round(rendEst, 1)
    except:
        logging.info('Excepcion en: %s' % __name__)

    return rendEst


def calculoRendEstBdCEstimadaSgCurva(tipoInstalacion, tipoEquipo, zonaHE1, usoEdificio, curvaRendimiento, rendNominalPG, factorCargaMinimo, factorCargaMaximo, potNominal, temperaturaAmbienteInt, tipoBdC):
    rendEst = ''
    try:
        if tipoInstalacion == 'ACS':
            repartoEnergiaPorcentualCaracteristico = [
             0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
             0.0, 1.0]
            perfilTemperaturaSeca = perfilesTerciario.PerfilTemperaturaSecaCalefaccion(zonaHE1, usoEdificio)
        elif tipoInstalacion == 'calefaccion':
            repartoEnergiaPorcentualCaracteristico = perfilesTerciario.PerfilDemandaCalefaccion(zonaHE1, usoEdificio)
            perfilTemperaturaSeca = perfilesTerciario.PerfilTemperaturaSecaCalefaccion(zonaHE1, usoEdificio)
        elif tipoInstalacion == 'refrigeracion':
            repartoEnergiaPorcentualCaracteristico = perfilesTerciario.PerfilDemandaRefrigeracion(zonaHE1, usoEdificio)
            perfilTemperaturaSeca = perfilesTerciario.PerfilTemperaturaSecaRefrigeracion(zonaHE1, usoEdificio)
            perfilTemperaturaHumedaExterior = perfilesTerciario.PerfilTemperaturaHumedaRefrigeracion(zonaHE1, usoEdificio)
        if tipoEquipo == 'Bomba de Calor' or tipoEquipo == 'Maquina frigorífica':
            if tipoInstalacion == 'calefaccion' or tipoInstalacion == 'ACS':
                bDC = equipos.ExpansionDirectaAireAguaBombaDeCalorModoCalor()
            elif tipoInstalacion == 'refrigeracion':
                if tipoBdC in ('Aire-Aire', 'Aire-Agua'):
                    bDC = equipos.ExpansionDirectaAireAireBombaDeCalorModoFrio()
                elif tipoBdC in ('Agua-Aire', 'Agua-Agua'):
                    bDC = equipos.ExpansionDirectaAguaAireBombaDeCalorModoFrio()
            bDC.c1 = float(curvaRendimiento[0])
            bDC.c2 = float(curvaRendimiento[1])
            bDC.c3 = float(curvaRendimiento[2])
            bDC.c4 = float(curvaRendimiento[3])
            bDC.d1 = float(curvaRendimiento[4])
            bDC.d2 = float(curvaRendimiento[5])
            bDC.d3 = float(curvaRendimiento[6])
            bDC.d4 = float(curvaRendimiento[7])
            bDC.d5 = float(curvaRendimiento[8])
            bDC.d6 = float(curvaRendimiento[9])
            bDC.rendimientoNominalPlenaCarga = float(rendNominalPG)
            bDC.fcpMin = float(factorCargaMinimo)
            bDC.fcpMax = float(factorCargaMaximo)
            bDC.potenciaNominal = float(potNominal)
            ti = float(temperaturaAmbienteInt)
            if tipoInstalacion == 'refrigeracion':
                if tipoBdC in ('Aire-Aire', 'Aire-Agua'):
                    consumoEnCadaFcp = [ bDC.potFcpTHIntTExt(fcpSistema[i], ti, perfilTemperaturaSeca[i]) for i in range(len(fcpSistema)) ]
                elif tipoBdC in ('Agua-Aire', 'Agua-Agua'):
                    fcpMod = [ x / bDC.capDisponibleTHIntTExt(ti, y) * bDC.potenciaNominal for x, y in zip(fcpSistema, perfilTemperaturaHumedaExterior) ]
                    consumoEnCadaFcp = [ bDC.potFcpTHIntTExt(fcpMod[i], ti, perfilTemperaturaHumedaExterior[i]) for i in range(len(fcpSistema))
                                       ]
            else:
                consumoEnCadaFcp = [ bDC.potFcpTIntTHExt(fcpSistema[i], ti, perfilTemperaturaSeca[i]) for i in range(len(fcpSistema)) ]
        elif tipoEquipo == 'Bomba de Calor - Caudal Ref. Variable' or tipoEquipo == 'Máquina frigorífica - Caudal Ref. Variable':
            if tipoInstalacion == 'ACS':
                vRV = equipos.ExpansionDirectaAireAguaBombaDeCalorModoCalor()
            elif tipoInstalacion == 'calefaccion':
                vRV = equipos.VRVModoCalor()
            elif tipoInstalacion == 'refrigeracion':
                if tipoBdC in ('Aire-Aire', 'Aire-Agua'):
                    vRV = equipos.VRVModoFrio()
                elif tipoBdC in ('Agua-Aire', 'Agua-Agua'):
                    vRV = equipos.ExpansionDirectaAguaAireBombaDeCalorModoFrioVRV()
            vRV.c1 = float(curvaRendimiento[0])
            vRV.c2 = float(curvaRendimiento[1])
            vRV.c3 = float(curvaRendimiento[2])
            vRV.c4 = float(curvaRendimiento[3])
            vRV.d1 = float(curvaRendimiento[4])
            vRV.d2 = float(curvaRendimiento[5])
            vRV.d3 = float(curvaRendimiento[6])
            vRV.d4 = float(curvaRendimiento[7])
            vRV.d5 = float(curvaRendimiento[8])
            vRV.d6 = float(curvaRendimiento[9])
            vRV.rendimientoNominalPlenaCarga = float(rendNominalPG)
            vRV.fcpMin = float(factorCargaMinimo)
            vRV.fcpMax = float(factorCargaMaximo)
            vRV.potenciaNominal = float(potNominal)
            ti = float(temperaturaAmbienteInt)
            if tipoInstalacion == 'refrigeracion':
                if tipoBdC in ('Aire-Aire', 'Aire-Agua'):
                    consumoEnCadaFcp = [ vRV.potFcpTHIntTExt(fcpSistema[i], ti, perfilTemperaturaSeca[i]) for i in range(len(fcpSistema)) ]
                elif tipoBdC in ('Agua-Aire', 'Agua-Agua'):
                    fcpMod = [ x / vRV.capDisponibleTHIntTExt(ti, y) * vRV.potenciaNominal for x, y in zip(fcpSistema, perfilTemperaturaHumedaExterior) ]
                    consumoEnCadaFcp = [ vRV.potFcpTHIntTExt(fcpMod[i], ti, perfilTemperaturaHumedaExterior[i]) for i in range(len(fcpSistema))
                                       ]
            else:
                consumoEnCadaFcp = [ vRV.potFcpTIntTHExt(fcpSistema[i], ti, perfilTemperaturaSeca[i]) for i in range(len(fcpSistema))
                                   ]
        rendimientoEnCadaFcp = [ float(potNominal) * fcpSistema[i] / consumoEnCadaFcp[i] for i in range(len(fcpSistema))
                               ]
        rendEst = sum([ repartoEnergiaPorcentualCaracteristico[i] * rendimientoEnCadaFcp[i] for i in range(len(rendimientoEnCadaFcp))
                      ])
        rendEst = round(rendEst, 1)
    except:
        logging.info('Excepcion en: %s' % __name__)

    return rendEst