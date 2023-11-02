# Embedded file name: Calculos\funcionesCalculo.pyc
from Escala.escalaCalificacion import getDiccionarioTemperaturasAguaRedACS
import logging
diccTempAguaRed = getDiccionarioTemperaturasAguaRedACS()
tempUtilizacionACS = 60.0
calorEspecificoACS = 4.18
densidadACS = 1
tempExteriorAcumulacion = 26.8
rendCalRefer = 92.0
combCalRefer = u'Gas Natural'
rendRefRefer = 200.0
combRefRefer = u'Electricidad'
rendCalEdifRef = 70.0
combCalEdifRef = u'Gas\xf3leo-C'
rendRefEdifRef = 170.0
combRefEdifRef = u'Electricidad'
rendACSEdifRef = 100.0
combACSEdifRef = u'Electricidad'
rendCombustionDefecto = 90.0
betaCombDefecto = 0.2
rendNominalJoule = 100.0
diccCOPNominalDefecto = {0: 270.0,
 1: 220.0,
 2: 200.0}
diccEERNominalDefecto = {0: 250.0,
 1: 200.0,
 2: 180.0}
diccLuminarias = {u'Incandescente': [10.0, 0.6],
 u'Incandescentes hal\xf3genas': [18.0, 0.74],
 u'Fluorescencia lineal de 26 mm': [90.0, 0.73],
 u'Fluorescencia lineal de 16 mm': [100.0, 0.79],
 u'Fluorescencia compacta': [80.0, 0.7],
 u'Sodio Blanco': [75.0, 0.69],
 u'Vapor de Mercurio': [60.0, 0.74],
 u'Halogenuros met\xe1licos': [88.0, 0.74],
 u'Inducci\xf3n': [70.0, 0.82],
 u'LED': [60.0, 0.95],
 u'LED Tube (lineal)': [85.0, 0.95]}

def coeficienteDePasoEmisiones(combustible = None, provincia = None, extrapeninsular = False):
    """
    Metodo: CoeficienteDePasoEmisiones
    """
    if combustible == u'Gas Natural':
        K = 0.252
    elif combustible == u'Gas\xf3leo-C':
        K = 0.311
    elif combustible == u'Electricidad':
        if extrapeninsular == False:
            K = 0.331
        elif provincia in (u'Ceuta', u'Melilla'):
            K = 0.721
        elif provincia in (u'Illes Balears',):
            K = 0.932
        elif provincia in (u'Las Palmas', u'Santa Cruz de Tenerife'):
            K = 0.776
        else:
            K = 0.833
    elif combustible == u'GLP':
        K = 0.254
    elif combustible == u'Carb\xf3n':
        K = 0.472
    elif combustible == u'Biocarburante':
        K = 0.018
    elif combustible == u'Biomasa/Renovable':
        K = 0.018
    elif combustible == u'BiomasaDens':
        K = 0.018
    return K


def coeficienteDePasoEnergiaPrimaria(combustible = None, provincia = None, extrapeninsular = False):
    """
    Metodo: coeficienteDePasoEnergiaPrimaria
    """
    if combustible == u'Gas Natural':
        KenPrim = 1.195
        KenPrimRen = 0.005
        KenPrimNoRen = 1.19
    elif combustible == u'Gas\xf3leo-C':
        KenPrim = 1.182
        KenPrimRen = 0.003
        KenPrimNoRen = 1.179
    elif combustible == u'Electricidad':
        if extrapeninsular == False:
            KenPrim = 2.368
            KenPrimRen = 0.414
            KenPrimNoRen = 1.954
        elif provincia in (u'Ceuta', u'Melilla'):
            KenPrim = 2.79
            KenPrimRen = 0.072
            KenPrimNoRen = 2.718
        elif provincia in (u'Illes Balears',):
            KenPrim = 3.049
            KenPrimRen = 0.082
            KenPrimNoRen = 2.968
        elif provincia in (u'Las Palmas', u'Santa Cruz de Tenerife'):
            KenPrim = 2.994
            KenPrimRen = 0.07
            KenPrimNoRen = 2.924
        else:
            KenPrim = 3.011
            KenPrimRen = 0.075
            KenPrimNoRen = 2.937
    elif combustible == u'GLP':
        KenPrim = 1.204
        KenPrimRen = 0.003
        KenPrimNoRen = 1.201
    elif combustible == u'Carb\xf3n':
        KenPrim = 1.084
        KenPrimRen = 0.002
        KenPrimNoRen = 1.082
    elif combustible == u'Biocarburante':
        KenPrim = 1.113
        KenPrimRen = 1.028
        KenPrimNoRen = 0.085
    elif combustible == u'Biomasa/Renovable':
        KenPrim = 1.037
        KenPrimRen = 1.003
        KenPrimNoRen = 0.034
    elif combustible == u'BiomasaDens':
        KenPrim = 1.113
        KenPrimRen = 1.028
        KenPrimNoRen = 0.085
    return (KenPrim, KenPrimRen, KenPrimNoRen)


def calculoContribucionSolarMinimaEdificioReferencia(zonaHE4 = 'I', Q_ACS = 0.0):
    """
    M\xe9todo: calculoContribucionSolarMinimaEdificioReferencia
    C\xe1lculo de la contribucion solar minma para el edificio de referencia
    Segun DBHE4-CTE2013
    QACS en l/dia
    """
    dicc50_5000 = {'I': 30.0,
     'II': 30.0,
     'III': 40.0,
     'IV': 50.0,
     'V': 60.0}
    dicc5000_10000 = {'I': 30.0,
     'II': 40.0,
     'III': 50.0,
     'IV': 60.0,
     'V': 70.0}
    diccMas10000 = {'I': 30.0,
     'II': 50.0,
     'III': 60.0,
     'IV': 70.0,
     'V': 70.0}
    if Q_ACS <= 50.0:
        porcSolar = 0.0
    else:
        if Q_ACS <= 5000.0:
            dicc = dicc50_5000
        elif Q_ACS <= 10000.0:
            dicc = dicc5000_10000
        else:
            dicc = diccMas10000
        porcSolar = dicc[zonaHE4]
    return porcSolar


def calculoVEEIIluminacionLimite(actividad = '', esEdificioReferencia = True, esZonaRepresentacion = False):
    diccVEEIRef = {u'Administrativo en general': [3.5, 6, 3.0],
     u'Pabellones de exposici\xf3n o ferias': [3.5, 0.0, 3.0],
     u'Salas de diagn\xf3stico': [3.5, 0.0, 3.5],
     u'Aulas y laboratorios': [4.0, 0.0, 3.5],
     u'Habitaciones de hospital': [4.5, 0.0, 4.0],
     u'Zonas comunes': [4.5, 10.0, 6.0],
     u'Almacenes,  archivos,  salas t\xe9cnicas y cocinas': [5.0, 0.0, 4.0],
     u'Espacios deportivos': [5.0, 0.0, 4.0],
     u'Estaciones de transporte': [0.0, 6.0, 5.0],
     u'Supermercados,  hipermercados y grandes almacenes': [0.0, 6.0, 5.0],
     u'Bibliotecas,  museos y galer\xedas de arte': [0.0, 6.0, 5.0],
     u'Zonas comunes en edificios residenciales': [0.0, 7.5, 4.0],
     u'Centros comerciales (excluidas tiendas)': [0.0, 8.0, 6.0],
     u'Hosteler\xeda y restauraci\xf3n': [0.0, 10.0, 8.0],
     u'Religioso en general': [0.0, 10.0, 8.0],
     u'Auditorios,  salas de actos,  usos m\xfaltiples,  convenciones,  espect\xe1culos...': [0.0, 10.0, 8.0],
     u'Tiendas y peque\xf1o comercio': [0.0, 10.0, 8.0],
     u'Habitaciones de hoteles,  hostales...': [0.0, 12.0, 10.0],
     u'Otros': [4.5, 10.0, 4.0],
     u'Locales con nivel de iluminaci\xf3n superior a 600 lux': [4.5, 10.0, 2.5]}
    if esEdificioReferencia == True:
        if esZonaRepresentacion == False:
            contador = 0
        else:
            contador = 1
    elif esEdificioReferencia == False:
        contador = 2
    VEEIRef = diccVEEIRef[actividad][contador]
    return VEEIRef


def calculoDdaBrutaACS(Q_ACS = 0.0, instalacionACS = None, zonaHE1PeninsularOExtrapeninsular = None, area = None):
    """
    Metodo: calculoDemandaACSBruta
    instalacionACS es un listado de objetos con los datos de las instalaciones de ACS
    
    zonaHE1PeninsularOExtrapeninsular = 'D1_peninsular' o 'D1_extrapeninsular'
    
    """
    tempAguaRed = diccTempAguaRed[zonaHE1PeninsularOExtrapeninsular]
    ddaACSBruta_sinAcumulacion = 360.0 * densidadACS * calorEspecificoACS * Q_ACS * (tempUtilizacionACS - tempAguaRed) / 3600 / area
    ddaACSBruta_acumulacion = calculoDdaACSAcumulacion(instalacionACS=instalacionACS, area=area)
    ddaACSBruta = ddaACSBruta_sinAcumulacion + ddaACSBruta_acumulacion
    return (ddaACSBruta, ddaACSBruta_sinAcumulacion, ddaACSBruta_acumulacion)


def calculoDdaACSAcumulacion(instalacionACS = None, area = None):
    """
    Metodo: calculoPerdidasAcumulacion
    """
    perdidas_dda = 0
    for i in instalacionACS.listado:
        acumulacion = i.acumulacion
        if acumulacion != [False]:
            Talta = float(acumulacion[2])
            Tbaja = float(acumulacion[3])
            UA = float(acumulacion[4])
            perdidas_dda += UA * ((Talta + Tbaja) / 2 - tempExteriorAcumulacion) * 8760.0 / 1000.0 / area

    return perdidas_dda


def calculoDdaNeta(ddaBruta = 0.0, porcTermica = 0.0, contribGeneracion = 0.0):
    """
    M\xe9todo: calculoDdaNeta
        Argumentos:
        ddaBruta: dda bruta para el servicio
        porcTermica: porc energ\xeda solar t\xe9rmica para el servicio. En %
        contribGenracion: contribuci\xf3n energ\xe9tica por cogeneraci\xf3n. En kWh/m2
    
    """
    contribTermica = porcTermica / 100.0
    ddaNeta = ddaBruta * (1 - contribTermica) - contribGeneracion
    if ddaNeta < 0.0:
        ddaNeta = 0.0
    return ddaNeta


def calculoDdaBruta(ddaNeta = 0.0, porcTermica = 0.0, contribGeneracion = 0.0):
    """
    M\xe9todo: calculoDdaBruta
    Argumentos:
        ddaNeta: dda neta para el servicio
        porcTermica: porc energ\xeda solar t\xe9rmica para el servicio. En %
        contribGenracion: contribuci\xf3n energ\xe9tica por cogeneraci\xf3n. En kWh/m2
    Calcula la demanda bruta a partir de las demandas netas y las contribuciones energ\xe9ticas asociadas
    Se utiliza en el an\xe1lisis econ\xf3mico para estimar las demandas brutas asociadas a los consumos reflejados en las facturas
    """
    contribTermica = porcTermica / 100.0
    ddaBruta = (ddaNeta + contribGeneracion) / (1 - contribTermica)
    return ddaBruta


def calculoNumeroHorasOcupacionEdificio(tipoUso):
    """
    Metodo: calculoNumeroHoras
    
    """
    if tipoUso in ('Intensidad Baja - 8h', 'Intensidad Media - 8h', 'Intensidad Alta - 8h'):
        numero_horas = 2504.0
    elif tipoUso in ('Intensidad Baja - 12h', 'Intensidad Media - 12h', 'Intensidad Alta - 12h'):
        numero_horas = 3548.0
    elif tipoUso in ('Intensidad Baja - 16h', 'Intensidad Media - 16h', 'Intensidad Alta - 16h'):
        numero_horas = 4592.0
    elif tipoUso in ('Intensidad Baja - 24h', 'Intensidad Media - 24h', 'Intensidad Alta - 24h'):
        numero_horas = 6680.0
    else:
        numero_horas = 8760.0
    return numero_horas


def calculoCargasEdificio(tipoUso = '', potenciaIluminacion = 0.0, area = 0.0):
    """
    Metodo: calculoCargasEdificio
    ARGUMENTOS:
        tipoUso: 'Intensidad Baja - 8h'....
        potenciaIluminacion potencia total en W
        area: en m2
    """
    if potenciaIluminacion > 0.0:
        cargaIluminacion = potenciaIluminacion / area
    else:
        cargaIluminacion = 0.0
    if tipoUso in ('Intensidad Baja - 8h', 'Intensidad Baja - 12h', 'Intensidad Baja - 16h', 'Intensidad Baja - 24h', 'Intensidad Baja', 'IB'):
        cargaOcupSensible = 2.0
        cargaOcupLatente = 1.26
        cargaEquipos = 1.5
    elif tipoUso in ('Intensidad Media - 8h', 'Intensidad Media - 12h', 'Intensidad Media - 16h', 'Intensidad Media - 24h', 'Intensidad Media', 'IM'):
        cargaOcupSensible = 6.0
        cargaOcupLatente = 3.79
        cargaEquipos = 4.5
    elif tipoUso in ('Intensidad Alta - 8h', 'Intensidad Alta - 12h', 'Intensidad Alta - 16h', 'Intensidad Alta - 24h', 'Intensidad Alta', 'IA'):
        cargaOcupSensible = 10.0
        cargaOcupLatente = 6.31
        cargaEquipos = 7.5
    else:
        cargaOcupSensible = 0.0
        cargaOcupLatente = 0.0
        cargaEquipos = 0.0
    if '8h' in tipoUso:
        nHorasLaboral = 8.0
        nHorasSabado = 8.0
        nHorasFestivo = 0.0
    elif '12h' in tipoUso:
        nHorasLaboral = 12.0
        nHorasSabado = 8.0
        nHorasFestivo = 0.0
    elif '16h' in tipoUso:
        nHorasLaboral = 16.0
        nHorasSabado = 8.0
        nHorasFestivo = 0.0
    elif '24h' in tipoUso:
        nHorasLaboral = 24.0
        nHorasSabado = 8.0
        nHorasFestivo = 0.0
    else:
        nHorasLaboral = 0.0
        nHorasSabado = 0.0
        nHorasFestivo = 0.0
    nHorasEdificioOcupado = nHorasLaboral * 5.0 + nHorasSabado + nHorasFestivo
    cargasInternas = (cargaOcupSensible + cargaOcupLatente + cargaEquipos + cargaIluminacion) * nHorasEdificioOcupado / 168.0
    return cargasInternas


def getValorDdaACSVersionesAnteriores(versionArchivoGuardado = 0.0, programa = 'Residencial', tipoEdificio = 'Unifamiliar', superficie = None):
    """
    Si el archivo es de versiones anteriores a la 1.9 y el edificio es de residencial, 
    se pone el valor de consumo de ACS con el que se hizo el c\xe1lculo
    """
    consumoACS = ''
    if versionArchivoGuardado < 1.9 and programa == 'Residencial':
        try:
            if tipoEdificio == 'Unifamiliar':
                caudalDiarioPorPersona = 30.0
            else:
                caudalDiarioPorPersona = 22.0
            superficie = float(superficie)
            consumoACS = round(caudalDiarioPorPersona * 0.03 * superficie, 2)
        except:
            consumoACS = ''
            logging.info(u'Excepcion en: %s' % __name__)

    return consumoACS


def getValorVentilacionNoGuardado(versionArchivoGuardado = 0.0, programa = 'Residencial', altura = None):
    """
    Si el archivo es de versiones anteriores a la 1.9, se pone el valor de ventilacion con el qeu se hizo el calculo
    Si el archivo es de versiones posteriores y no se ha indicado ning\xfan valor, se pone el valor por defecto,
    es decir, 0.63 xa residencial y 0.8 xa terciario
    """
    if versionArchivoGuardado < 1.9:
        try:
            altura = float(altura)
            if programa == 'Residencial':
                valorVentilacion = round(2.16 / altura, 2)
            else:
                valorVentilacion = round(2.8800000000000003 / altura, 2)
        except:
            valorVentilacion = getValorDefectoVentilacion(programa)
            logging.info(u'Excepcion en: %s' % __name__)

    else:
        valorVentilacion = getValorDefectoVentilacion(programa)
    return valorVentilacion


def getValorDefectoVentilacion(programa):
    if programa == 'Residencial':
        valorDefectoVentilacion = 0.63
    else:
        valorDefectoVentilacion = 0.8
    return valorDefectoVentilacion


def getGradosHora(programa = '', tipoEdificio = '', zonaHE1PeninsularOExtrapeninsular = ''):
    diccGH = {'A3_peninsular': {'8h': [5624.3, 1668.8],
                       '12h': [8038.3, 2687.3],
                       '16h': [8038.3, 3802.2],
                       '24h': [16203.5, 3419.1]},
     'A4_peninsular': {'8h': [5567.4, 2394.6],
                       '12h': [7949.4, 3906.0],
                       '16h': [7949.4, 5463.8],
                       '24h': [16021.1, 4985.6]},
     'B3_peninsular': {'8h': [8129.4, 1651.7],
                       '12h': [11642.5, 2675.8],
                       '16h': [11642.5, 3769.5],
                       '24h': [23507.5, 3422.2]},
     'B4_peninsular': {'8h': [8133.8, 2329.0],
                       '12h': [11623.1, 3798.6],
                       '16h': [11623.1, 5292.1],
                       '24h': [23495.5, 4835.1]},
     'C1_peninsular': {'8h': [13539.0, 283.7],
                       '12h': [19479.5, 423.6],
                       '16h': [19479.5, 666.2],
                       '24h': [39484.0, 593.5]},
     'C2_peninsular': {'8h': [12999.0, 632.2],
                       '12h': [18682.7, 1040.2],
                       '16h': [18682.7, 1529.2],
                       '24h': [37842.0, 1381.6]},
     'C3_peninsular': {'8h': [12551.7, 1504.4],
                       '12h': [18065.3, 2473.5],
                       '16h': [18065.3, 3485.7],
                       '24h': [36354.8, 3150.9]},
     'C4_peninsular': {'8h': [12508.8, 2223.7],
                       '12h': [18019.5, 3674.1],
                       '16h': [18019.5, 5134.4],
                       '24h': [36176.7, 4706.2]},
     'D1_peninsular': {'8h': [17979.7, 260.3],
                       '12h': [26016.7, 399.2],
                       '16h': [26016.7, 629.2],
                       '24h': [51889.4, 564.7]},
     'D2_peninsular': {'8h': [17343.8, 634.1],
                       '12h': [25154.1, 1054.5],
                       '16h': [25154.1, 1548.1],
                       '24h': [49765.9, 1356.4]},
     'D3_peninsular': {'8h': [16920.4, 1535.1],
                       '12h': [24564.3, 2489.7],
                       '16h': [24564.3, 3488.5],
                       '24h': [48616.3, 3158.3]},
     'E1_peninsular': {'8h': [21630.4, 251.9],
                       '12h': [31708.6, 388.0],
                       '16h': [31708.6, 611.3],
                       '24h': [61780.9, 529.4]},
     'A1_extrapeninsular': {'8h': [5498.2, 9.8],
                            '12h': [7978.5, 11.7],
                            '16h': [7978.5, 19.8],
                            '24h': [15644.7, 14.4]},
     'A2_extrapeninsular': {'8h': [5376.9, 67.6],
                            '12h': [7812.2, 102.9],
                            '16h': [7812.2, 171.3],
                            '24h': [15253.0, 127.1]},
     'A3_extrapeninsular': {'8h': [5377.2, 453.8],
                            '12h': [7811.5, 715.6],
                            '16h': [7811.5, 1035.1],
                            '24h': [15241.0, 910.8]},
     'A4_extrapeninsular': {'8h': [5383.6, 1075.2],
                            '12h': [7831.5, 1738.6],
                            '16h': [7831.5, 2424.9],
                            '24h': [15255.1, 2225.9]},
     'B1_extrapeninsular': {'8h': [8021.5, 14.6],
                            '12h': [11760.7, 20.8],
                            '16h': [11760.7, 31.3],
                            '24h': [22903.6, 15.2]},
     'B2_extrapeninsular': {'8h': [7913.3, 64.0],
                            '12h': [11595.5, 93.5],
                            '16h': [11595.5, 153.1],
                            '24h': [22614.3, 118.9]},
     'B3_extrapeninsular': {'8h': [7884.2, 455.0],
                            '12h': [11549.3, 711.8],
                            '16h': [11549.3, 1024.1],
                            '24h': [22510.3, 891.8]},
     'B4_extrapeninsular': {'8h': [7872.1, 1078.1],
                            '12h': [11557.6, 1748.5],
                            '16h': [11557.6, 2442.7],
                            '24h': [22492.8, 2252.7]},
     'C1_extrapeninsular': {'8h': [12112.0, 12.4],
                            '12h': [17978.4, 14.5],
                            '16h': [17978.4, 21.6],
                            '24h': [34327.4, 17.0]},
     'C2_extrapeninsular': {'8h': [12116.1, 75.8],
                            '12h': [17819.8, 108.3],
                            '16h': [17819.8, 167.5],
                            '24h': [34135.3, 132.3]},
     'C3_extrapeninsular': {'8h': [12146.0, 439.4],
                            '12h': [17826.9, 693.0],
                            '16h': [17826.9, 1002.7],
                            '24h': [34130.5, 890.1]},
     'C4_extrapeninsular': {'8h': [12169.1, 1082.5],
                            '12h': [17819.9, 1753.3],
                            '16h': [17819.9, 2447.7],
                            '24h': [34143.3, 2231.5]},
     'D1_extrapeninsular': {'8h': [16976.7, 24.1],
                            '12h': [25232.5, 31.3],
                            '16h': [25232.5, 45.0],
                            '24h': [47767.6, 26.2]},
     'D2_extrapeninsular': {'8h': [17187.8, 73.2],
                            '12h': [25253.7, 107.4],
                            '16h': [25253.7, 169.8],
                            '24h': [47931.2, 121.2]},
     'D3_extrapeninsular': {'8h': [17138.2, 444.3],
                            '12h': [25200.9, 702.4],
                            '16h': [25200.9, 1012.9],
                            '24h': [47906.8, 899.2]},
     'E1_extrapeninsular': {'8h': [21448.6, 6.1],
                            '12h': [31639.1, 7.4],
                            '16h': [31639.1, 12.6],
                            '24h': [59669.2, 6.1]},
     'alpha1_extrapeninsular': {'8h': [206.6, 63.2],
                                '12h': [286.4, 80.9],
                                '16h': [286.4, 128.5],
                                '24h': [551.8, 106.8]},
     'alpha2_extrapeninsular': {'8h': [42.4, 124.1],
                                '12h': [61.8, 174.3],
                                '16h': [61.8, 283.2],
                                '24h': [127.9, 219.2]},
     'alpha3_extrapeninsular': {'8h': [42.4, 430.5],
                                '12h': [61.8, 696.0],
                                '16h': [61.8, 1027.9],
                                '24h': [127.9, 894.0]},
     'alpha4_extrapeninsular': {'8h': [42.4, 825.6],
                                '12h': [61.8, 1413.6],
                                '16h': [61.8, 2004.5],
                                '24h': [127.9, 1907.6]}}
    if programa != 'Residencial':
        if '8h' in tipoEdificio:
            horasUso = '8h'
        elif '12h' in tipoEdificio:
            horasUso = '12h'
        elif '16h' in tipoEdificio:
            horasUso = '16h'
        elif '24h' in tipoEdificio:
            horasUso = '24h'
        GH_invierno = diccGH[zonaHE1PeninsularOExtrapeninsular][horasUso][0]
        GH_verano = diccGH[zonaHE1PeninsularOExtrapeninsular][horasUso][1]
    else:
        GH_invierno = 0.0
        GH_verano = 0.0
    return (GH_invierno, GH_verano)


def compararDosConjuntosObjEdificio(objEdificio1 = None, objEdificio2 = None):
    """
    M\xe9todo: compararDosConjuntosObjEdificio
    Atributos: dos obj tipo datosEdificio a comparar
    
    Funcion para comparar dos objetos de tipo datos Edificio entre si
    Devuelve True si los obj son iguales, False si son diferentes
    """
    try:
        for key in objEdificio1.datosResultados.__dict__:
            if key not in ('dI', 'dG', 'parent', 'expFinal'):
                if objEdificio1.datosResultados.__dict__[key] != objEdificio2.datosResultados.__dict__[key]:
                    return False

        if objEdificio1.datosIniciales.tasaVentilacion != objEdificio2.datosIniciales.tasaVentilacion:
            return False
    except:
        logging.info(u'Excepcion en: %s' % __name__)
        return False

    return True