# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: MedidasDeMejora\medidasMejoraDefecto.pyc
# Compiled at: 2015-01-25 00:56:33
from Envolvente.tablasValores import tablasValores
from Calculos.limitesCTEyEdifRef import getValoresLimiteCerr
from Calculos.funcionesCalculo import calculoContribucionSolarMinimaEdificioReferencia
from copy import deepcopy
from objetoGrupoMejoras import grupoMedidasMejora

def getMedidasPorDefecto(objEdificio=None):
    listadoConjuntosMMPorDefecto = []
    norma = objEdificio.datosIniciales.normativaVigente
    zonaHE1 = objEdificio.datosIniciales.zonaHE1
    superficieTotalHabitable = objEdificio.datosIniciales.area
    medidaAislamiento = [
     '', 'Adición de Aislamiento Térmico',
     [
      False, False, False, False, False, False, '', '', '', '',
      False, ['', '', '', '', '', '', ''], [False, False, False, False]]]
    sinSombras = [
     '', '', '', '', '', '', ['', 0, 0], ['', 0, 0], '',
     False, False, '', False, False, '', '', '', False, False,
     False, False, False, False, False, ['', '']]
    medidaHuecos = [
     '', 'Sustitución/mejora de Huecos',
     [
      [
       True, True, True, True, True, True, True, True, True],
      False, False, '', '', '', False, False, '', '', '', False, '', False, False, '', '',
      False, '', False, sinSombras]]
    medidaPT = [
     '', 'Mejora de Puentes Térmicos',
     ['False', '', 'False', '', 'False', '', 'False', 
      '', 'False', 
      '', 'False', '', 'False', '', 'False', 
      '', 'False', 
      '', 'False', '']]
    valoresMejoraFachada = {'alpha1': 0.94, 'alpha2': 0.94, 'alpha3': 0.94, 'alpha4': 0.94, 'A1': 0.5, 
       'A2': 0.5, 'A3': 0.5, 'A4': 0.5, 'B1': 0.38, 
       'B2': 0.38, 'B3': 0.38, 'B4': 0.38, 'C1': 0.29, 
       'C2': 0.29, 'C3': 0.29, 'C4': 0.29, 'D1': 0.27, 
       'D2': 0.27, 'D3': 0.27, 'E1': 0.25}
    valoresMejoraCubierta = {'alpha1': 0.5, 'alpha2': 0.5, 'alpha3': 0.5, 'alpha4': 0.5, 'A1': 0.47, 
       'A2': 0.47, 'A3': 0.47, 'A4': 0.47, 'B1': 0.33, 
       'B2': 0.33, 'B3': 0.33, 'B4': 0.33, 'C1': 0.23, 
       'C2': 0.23, 'C3': 0.23, 'C4': 0.23, 'D1': 0.22, 
       'D2': 0.22, 'D3': 0.22, 'E1': 0.19}
    valoresMejoraSuelo = {'alpha1': 0.53, 'alpha2': 0.53, 'alpha3': 0.53, 'alpha4': 0.53, 'A1': 0.53, 
       'A2': 0.53, 'A3': 0.53, 'A4': 0.53, 'B1': 0.46, 
       'B2': 0.46, 'B3': 0.46, 'B4': 0.46, 'C1': 0.36, 
       'C2': 0.36, 'C3': 0.36, 'C4': 0.36, 'D1': 0.34, 
       'D2': 0.34, 'D3': 0.34, 'E1': 0.31}
    medida = deepcopy(medidaAislamiento)
    nombreMedida = _('Adición de aislamiento térmico en fachada por el exterior')
    medida[0] = nombreMedida
    nuevaU = valoresMejoraFachada[zonaHE1]
    nuevosPT = [
     '', '', '', '', '', '', '']
    nuevosPT[0] = str(tablasValores('PTMedidasMejora', None, [
     'Pilar integrado en fachada'], None).fi)
    nuevosPT[1] = str(tablasValores('PTMedidasMejora', None, [
     'Pilar en Esquina'], None).fi)
    nuevosPT[2] = str(tablasValores('PTMedidasMejora', None, [
     'Contorno de hueco'], None).fi)
    nuevosPT[3] = str(tablasValores('PTMedidasMejora', None, [
     'Caja de Persiana'], None).fi)
    nuevosPT[4] = str(tablasValores('PTMedidasMejora', None, [
     'Encuentro de fachada con forjado'], None).fi)
    nuevosPT[5] = str(tablasValores('PTMedidasMejora', None, [
     'Encuentro de fachada con cubierta'], None).fi)
    nuevosPT[6] = str(tablasValores('PTMedidasMejora', None, [
     'Encuentro de fachada con suelo en contacto con el aire'], None).fi)
    medida[2] = [
     True, False, False, True, False, False, nuevaU, '', '', '', True, nuevosPT, [False, False, False, False]]
    conjuntoMejoras = [
     [
      medida], ['', [], False]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD1', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    medida = deepcopy(medidaAislamiento)
    nombreMedida = _('Adición de aislamiento térmico en fachada por el interior o relleno de cámara de aire')
    medida[0] = nombreMedida
    nuevaU = valoresMejoraFachada[zonaHE1]
    medida[2] = [
     True, False, False, True, False, False, nuevaU, '', '', '',
     False, ['', '', '', '', '', '', ''], [False, False, False, False]]
    conjuntoMejoras = [
     [
      medida], ['', [], False]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD2', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    medida = deepcopy(medidaAislamiento)
    nombreMedida = _('Adición de aislamiento térmico en cubierta')
    medida[0] = nombreMedida
    nuevaU = valoresMejoraCubierta[zonaHE1]
    medida[2] = [
     False, True, False, True, False, False, nuevaU, '', '', '',
     False, ['', '', '', '', '', '', ''], [False, False, False, False]]
    conjuntoMejoras = [
     [
      medida], ['', [], False]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD3', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    medida = deepcopy(medidaAislamiento)
    nombreMedida = _('Adición de aislamiento térmico en suelo')
    medida[0] = nombreMedida
    nuevaU = valoresMejoraSuelo[zonaHE1]
    medida[2] = [
     False, False, True, True, False, False, nuevaU, '', '', '', False,
     [
      '', '', '', '', '', '', ''], [False, False, False, False]]
    conjuntoMejoras = [
     [
      medida], ['', [], False]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD4', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    medida = deepcopy(medidaPT)
    nombreMedida = _('Trasdosado interior de pilares integrados en fachada')
    medida[0] = nombreMedida
    nuevaFiPilarIntegradoFachada = 0.2
    nuevaFiPilarEnEsquina = 0.03
    medida[2] = [
     'True', 'nuevaFiPilarIntegradoFachada', 'True', 'nuevaFiPilarEnEsquina', 
     'False', '', 'False', '', 
     'False', '', 'False', '', 
     'False', '', 'False', '', 'False', '', 'False', '']
    conjuntoMejoras = [
     [
      medida], ['', [], False]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD5', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    medida = deepcopy(medidaPT)
    nombreMedida = _('Adición de aislamiento en cajas de persiana')
    medida[0] = nombreMedida
    nuevaFi = 0
    medida[2] = [
     'False', '', 'False', '', 'False', '', 'True', 'nuevaFi', 'False', 
     '', 'False', '', 'False', 
     '', 'False', '', 'False', 
     '', 'False', '']
    conjuntoMejoras = [
     [
      medida], ['', [], False]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD6', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    medida = deepcopy(medidaHuecos)
    nombreMedida = _('Sustitución de vidrios por otros más aislantes')
    medida[0] = nombreMedida
    medida[2][1] = True
    medida[2][2] = True
    medida[2][3] = 1.8
    medida[2][4] = 0.62
    conjuntoMejoras = [
     [
      medida], ['', [], False]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD7', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    medida = deepcopy(medidaHuecos)
    nombreMedida = _('Sustitución de vidrios con control solar')
    medida[0] = nombreMedida
    medida[2][0] = [
     False, False, False, True, True, True, True, True, True]
    medida[2][1] = True
    medida[2][2] = True
    medida[2][3] = 3.3
    medida[2][4] = 0.45
    conjuntoMejoras = [
     [
      medida], ['', [], False]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD8', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    medida = deepcopy(medidaHuecos)
    nombreMedida = _('Sustitución de ventanas')
    medida[0] = nombreMedida
    medida[2][1] = True
    medida[2][2] = True
    medida[2][3] = 1.8
    medida[2][4] = 0.62
    medida[2][15] = 1.6
    if 'alpha' in zonaHE1 or 'A' in zonaHE1 or 'B' in zonaHE1:
        medida[2][10] = 27
    else:
        medida[2][10] = 9
    medida[2][6] = True
    medida[2][9] = 'Valor conocido'
    medida[2][11] = True
    medida[2][12] = 30
    medida[2][13] = True
    medida[2][14] = True
    conjuntoMejoras = [
     [
      medida], ['', [], False]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD9', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    medida = deepcopy(medidaHuecos)
    nombreMedida = _('Mejora Estanqueidad Ventanas')
    medida[0] = nombreMedida
    medida[2][6] = True
    medida[2][9] = 'Valor conocido'
    if 'alpha' in zonaHE1 or 'A' in zonaHE1 or 'B' in zonaHE1:
        medida[2][10] = 27
    else:
        medida[2][10] = 9
    conjuntoMejoras = [[medida], ['', [], False]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD10', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    medida = deepcopy(medidaHuecos)
    nombreMedida = _('Incorporación de doble ventana')
    medida[0] = nombreMedida
    medida[2][17] = True
    medida[2][18] = 'Vidrio Simple'
    conjuntoMejoras = [
     [
      medida], ['', [], False]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD10', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    sistemasACS = objEdificio.datosIniciales.sistemasACS
    sistemasCalefaccion = objEdificio.datosIniciales.sistemasCalefaccion
    sistemasRefrigeracion = objEdificio.datosIniciales.sistemasRefrigeracion
    sistemasClimatizacion = objEdificio.datosIniciales.sistemasClimatizacion
    sistemasMixto2 = objEdificio.datosIniciales.sistemasMixto2
    sistemasMixto3 = objEdificio.datosIniciales.sistemasMixto3
    sistemasContribuciones = objEdificio.datosIniciales.sistemasContribuciones
    if objEdificio.programa == 'Residencial':
        sistemasIluminacion = []
        sistemasVentilacion = []
        sistemasVentiladores = []
        sistemasBombas = []
        sistemasTorresRefrigeracion = []
    else:
        sistemasIluminacion = objEdificio.datosIniciales.sistemasIluminacion
        sistemasVentilacion = objEdificio.datosIniciales.sistemasVentilacion
        sistemasVentiladores = objEdificio.datosIniciales.sistemasVentiladores
        sistemasBombas = objEdificio.datosIniciales.sistemasBombas
        sistemasTorresRefrigeracion = objEdificio.datosIniciales.sistemasTorresRefrigeracion
    nombreMedida = _('Incorporación/mejora de sistema de energía solar térmica para ACS')
    nuevoSistemasContribuciones = deepcopy(sistemasContribuciones)
    contribSolarMinima = calculoContribucionSolarMinimaEdificioReferencia(zonaHE4=objEdificio.datosIniciales.zonaHE4, Q_ACS=objEdificio.datosIniciales.Q_ACS)
    nuevoSistemasContribuciones.append(['Incorporación de sistema de energía solar térmica para ACS', 'renovable',
     [
      str(contribSolarMinima), '', '', False],
     [
      '', '', '', '', '', ''], [True, False], 'Edificio Objeto'])
    conjuntoMejoras = [[],
     [nombreMedida,
      [sistemasACS, sistemasCalefaccion, sistemasRefrigeracion, 
       sistemasClimatizacion, 
       sistemasMixto2, sistemasMixto3, 
       nuevoSistemasContribuciones, 
       sistemasIluminacion, sistemasVentilacion, 
       sistemasVentiladores, 
       sistemasBombas, sistemasTorresRefrigeracion],
      True]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD12', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    nombreMedida = _('Incorporación/mejora de sistema de energía solar térmica para calefacción')
    nuevoSistemasContribuciones = deepcopy(sistemasContribuciones)
    nuevoSistemasContribuciones.append(['Incorporación de sistema de energía solar térmica para calefacción',
     'renovable',
     [
      '', '20', '', False], ['', '', '', '', '', ''],
     [
      True, False], 'Edificio Objeto'])
    conjuntoMejoras = [[],
     [nombreMedida,
      [sistemasACS, sistemasCalefaccion, sistemasRefrigeracion, 
       sistemasClimatizacion, 
       sistemasMixto2, sistemasMixto3, 
       nuevoSistemasContribuciones, 
       sistemasIluminacion, 
       sistemasVentilacion, sistemasVentiladores, 
       sistemasBombas, 
       sistemasTorresRefrigeracion],
      True]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD13', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    nombreMedida = _('Incorporación/mejora de sistema de energía solar térmica para refrigeración')
    nuevoSistemasContribuciones = deepcopy(sistemasContribuciones)
    nuevoSistemasContribuciones.append(['Incorporación de sistema de energía solar térmica para refrigeración',
     'renovable',
     [
      '', '', '20', False], ['', '', '', '', '', ''],
     [
      True, False], 'Edificio Objeto'])
    conjuntoMejoras = [[],
     [nombreMedida,
      [sistemasACS, sistemasCalefaccion, sistemasRefrigeracion, 
       sistemasClimatizacion, 
       sistemasMixto2, sistemasMixto3, 
       nuevoSistemasContribuciones, 
       sistemasIluminacion, 
       sistemasVentilacion, sistemasVentiladores, 
       sistemasBombas, 
       sistemasTorresRefrigeracion],
      True]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD14', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    nombreMedida = _('Incorporación/mejora de sistema fotovoltaico')
    nuevoSistemasContribuciones = deepcopy(sistemasContribuciones)
    valorFotovoltaica = objEdificio.datosIniciales.area * 4.2
    nuevoSistemasContribuciones.append(['Incorporación/mejora de sistema fotovoltaico', 'renovable',
     [
      '', '', '', False],
     [str(valorFotovoltaica),
      '', '', '', '', ''],
     [
      False, True], 'Edificio Objeto'])
    conjuntoMejoras = [[],
     [nombreMedida,
      [sistemasACS, sistemasCalefaccion, sistemasRefrigeracion, 
       sistemasClimatizacion, 
       sistemasMixto2, sistemasMixto3, 
       nuevoSistemasContribuciones, 
       sistemasIluminacion, 
       sistemasVentilacion, sistemasVentiladores, 
       sistemasBombas, 
       sistemasTorresRefrigeracion],
      True]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD15', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    nombreMedida = _('Incorporación de un sistema de cogeneración para ACS')
    nuevoSistemasContribuciones = deepcopy(sistemasContribuciones)
    calorACS = round(objEdificio.datosResultados.ddaNetaACS * objEdificio.datosIniciales.area, 2)
    energiaConsumida = round(calorACS / 0.64, 2)
    energiaGenerada = round(energiaConsumida * 0.32, 2)
    combustible = 'Gas Natural'
    nuevoSistemasContribuciones.append(['Producción de ACS mediante cogeneración', 'renovable',
     [
      '', '', '', False],
     [str(energiaGenerada), str(calorACS),
      '', '', str(energiaConsumida),
      combustible], [False, True], 'Edificio Objeto'])
    conjuntoMejoras = [[],
     [nombreMedida,
      [sistemasACS, sistemasCalefaccion, sistemasRefrigeracion, 
       sistemasClimatizacion, 
       sistemasMixto2, sistemasMixto3, 
       nuevoSistemasContribuciones, 
       sistemasIluminacion, 
       sistemasVentilacion, sistemasVentiladores, 
       sistemasBombas, 
       sistemasTorresRefrigeracion],
      True]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD16', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    nombreMedida = _('Sustitución de equipos de generación para ACS por caldera de alta eficiencia energética')
    nuevoSistemasACS = [
     [
      'Nueva instalación ACS', 'ACS',
      [
       95.0, '', ''], 'Caldera Condensación', 'Gas Natural',
      [
       [
        str(superficieTotalHabitable), '100.0'], ['', ''], ['', '']],
      'Conocido (Ensayado/justificado)', ['95'], [False], 'Edificio Objeto']]
    nuevoSistemasMixto2 = deepcopy(sistemasMixto2)
    nuevoSistemasMixto3 = deepcopy(sistemasMixto3)
    for eq in nuevoSistemasMixto2:
        eq[5][0] = [
         '0', '0']

    for eq in nuevoSistemasMixto3:
        eq[5][0] = [
         '0', '0']

    conjuntoMejoras = [[],
     [nombreMedida,
      [
       nuevoSistemasACS, sistemasCalefaccion, sistemasRefrigeracion, 
       sistemasClimatizacion, 
       nuevoSistemasMixto2, nuevoSistemasMixto3, 
       sistemasContribuciones, 
       sistemasIluminacion, 
       sistemasVentilacion, sistemasVentiladores, 
       sistemasBombas, 
       sistemasTorresRefrigeracion],
      True]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD17', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    nombreMedida = _('Sustitución de equipos de generación para calefacción por caldera de alta eficiencia energética')
    nuevoSistemasCalefaccion = [
     [
      'Nueva instalación calefacción', 'calefaccion', ['', 95.0, ''],
      'Caldera Condensación', 'Gas Natural',
      [
       [
        '', ''], [str(superficieTotalHabitable), '100.0'], ['', '']],
      'Conocido (Ensayado/justificado)', ['95'], 'Edificio Objeto']]
    nuevoSistemasClimatizacion = deepcopy(sistemasClimatizacion)
    nuevoSistemasMixto2 = deepcopy(sistemasMixto2)
    nuevoSistemasMixto3 = deepcopy(sistemasMixto3)
    for eq in nuevoSistemasClimatizacion:
        eq[5][1] = ['0', '0']

    for eq in nuevoSistemasMixto2:
        eq[5][1] = [
         '0', '0']

    for eq in nuevoSistemasMixto3:
        eq[5][1] = [
         '0', '0']

    conjuntoMejoras = [[],
     [nombreMedida,
      [
       sistemasACS, nuevoSistemasCalefaccion, sistemasRefrigeracion, 
       nuevoSistemasClimatizacion, 
       nuevoSistemasMixto2, nuevoSistemasMixto3, 
       sistemasContribuciones, 
       sistemasIluminacion, 
       sistemasVentilacion, sistemasVentiladores, 
       sistemasBombas, 
       sistemasTorresRefrigeracion],
      True]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD18', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    nombreMedida = _('Sustitución de calderas de combustión por otras de mayor eficiencia energética')
    nuevoSistemasACS = deepcopy(sistemasACS)
    nuevoSistemasCalefaccion = deepcopy(sistemasCalefaccion)
    nuevoSistemasMixto2 = deepcopy(sistemasMixto2)
    for sist in nuevoSistemasACS:
        if sist[3] in ('Caldera Estándar', 'Caldera Condensación', 'Caldera Baja Temperatura') and sist[4] != 'Electricidad':
            if sist[2][0] < 95.0:
                sist[0] = sist[0] + ' Mejorado'
                sist[2] = [95.0, '', '']
                sist[6] = 'Conocido (Ensayado/justificado)'
                sist[7] = ['95.0']

    for sist in nuevoSistemasCalefaccion:
        if sist[3] in ('Caldera Estándar', 'Caldera Condensación', 'Caldera Baja Temperatura') and sist[4] != 'Electricidad':
            if sist[2][1] < 95.0:
                sist[0] = sist[0] + ' Mejorado'
                sist[2] = ['', 95.0, '']
                sist[6] = 'Conocido (Ensayado/justificado)'
                sist[7] = ['95.0']

    for sist in nuevoSistemasMixto2:
        if sist[3] in ('Caldera Estándar', 'Caldera Condensación', 'Caldera Baja Temperatura') and sist[4] != 'Electricidad':
            if sist[2][0] < 95.0:
                sist[0] = sist[0] + ' Mejorado'
                sist[2] = [95.0, 95.0, '']
                sist[6] = 'Conocido (Ensayado/justificado)'
                sist[7] = ['95.0']

    conjuntoMejoras = [[],
     [nombreMedida,
      [
       nuevoSistemasACS, nuevoSistemasCalefaccion, sistemasRefrigeracion, 
       sistemasClimatizacion, 
       nuevoSistemasMixto2, sistemasMixto3, 
       sistemasContribuciones, 
       sistemasIluminacion, 
       sistemasVentilacion, sistemasVentiladores, 
       sistemasBombas, 
       sistemasTorresRefrigeracion],
      True]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD23', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    nombreMedida = _('Sustitución de equipos de generación para ACS por caldera de biomasa')
    nuevoSistemasACS = [
     [
      'Nueva instalación ACS', 'ACS', [80.0, '', ''],
      'Caldera Estándar', 'Biomasa/Renovable',
      [[str(superficieTotalHabitable), '100.0'],
       [
        '', ''], ['', '']],
      'Conocido (Ensayado/justificado)', ['80'], [False], 'Edificio Objeto']]
    nuevoSistemasMixto2 = deepcopy(sistemasMixto2)
    nuevoSistemasMixto3 = deepcopy(sistemasMixto3)
    for eq in nuevoSistemasMixto2:
        eq[5][0] = ['0', '0']

    for eq in nuevoSistemasMixto3:
        eq[5][0] = [
         '0', '0']

    conjuntoMejoras = [[],
     [nombreMedida,
      [
       nuevoSistemasACS, sistemasCalefaccion, sistemasRefrigeracion, 
       sistemasClimatizacion, 
       nuevoSistemasMixto2, nuevoSistemasMixto3, 
       sistemasContribuciones, 
       sistemasIluminacion, sistemasVentilacion, 
       sistemasVentiladores, 
       sistemasBombas, sistemasTorresRefrigeracion],
      True]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD24', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    nombreMedida = _('Sustitución de equipos de generación para calefacción por caldera de biomasa')
    nuevoSistemasCalefaccion = [
     [
      'Nueva instalación calefacción', 'calefaccion', ['', 80.0, ''],
      'Caldera Estándar', 'Biomasa/Renovable',
      [
       [
        '', ''], [str(superficieTotalHabitable), '100.0'], ['', '']],
      'Conocido (Ensayado/justificado)', ['80'], 'Edificio Objeto']]
    nuevoSistemasClimatizacion = deepcopy(sistemasClimatizacion)
    nuevoSistemasMixto2 = deepcopy(sistemasMixto2)
    nuevoSistemasMixto3 = deepcopy(sistemasMixto3)
    for eq in nuevoSistemasClimatizacion:
        eq[5][1] = ['0', '0']

    for eq in nuevoSistemasMixto2:
        eq[5][1] = [
         '0', '0']

    for eq in nuevoSistemasMixto3:
        eq[5][1] = [
         '0', '0']

    conjuntoMejoras = [[],
     [nombreMedida,
      [
       sistemasACS, nuevoSistemasCalefaccion, sistemasRefrigeracion, 
       nuevoSistemasClimatizacion, 
       nuevoSistemasMixto2, nuevoSistemasMixto3, 
       sistemasContribuciones, 
       sistemasIluminacion, 
       sistemasVentilacion, sistemasVentiladores, 
       sistemasBombas, 
       sistemasTorresRefrigeracion],
      True]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD25', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    nombreMedida = _('Sustitución de equipos de generación para calefacción por bomba de calor de alta eficiencia energética')
    nuevoSistemasCalefaccion = [
     [
      'Nueva instalación calefacción', 'calefaccion', ['', 420.0, ''],
      'Bomba de Calor', 'Electricidad',
      [
       [
        '', ''], [str(superficieTotalHabitable), '100.0'], ['', '']],
      'Conocido (Ensayado/justificado)', ['', '420', ''], 'Edificio Objeto']]
    nuevoSistemasClimatizacion = deepcopy(sistemasClimatizacion)
    nuevoSistemasMixto2 = deepcopy(sistemasMixto2)
    nuevoSistemasMixto3 = deepcopy(sistemasMixto3)
    for eq in nuevoSistemasClimatizacion:
        eq[5][1] = ['0', '0']

    for eq in nuevoSistemasMixto2:
        eq[5][1] = [
         '0', '0']

    for eq in nuevoSistemasMixto3:
        eq[5][1] = [
         '0', '0']

    conjuntoMejoras = [[],
     [nombreMedida,
      [
       sistemasACS, nuevoSistemasCalefaccion, sistemasRefrigeracion, 
       nuevoSistemasClimatizacion, 
       nuevoSistemasMixto2, nuevoSistemasMixto3, 
       sistemasContribuciones, 
       sistemasIluminacion, 
       sistemasVentilacion, sistemasVentiladores, 
       sistemasBombas, 
       sistemasTorresRefrigeracion],
      True]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD19', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    nombreMedida = _('Sustitución de equipos de generación para refrigeración por bomba de calor de alta eficiencia energética')
    nuevoSistemasRefrigeracion = [
     [
      'Nueva instalación refrigeración', 'refrigeracion',
      [
       '', '', 400], 'Maquina frigorífica', 'Electricidad',
      [
       [
        '', ''], ['', ''], [str(superficieTotalHabitable), '100.0']],
      'Conocido (Ensayado/justificado)', ['', '', '400'], 'Edificio Objeto']]
    nuevoSistemasClimatizacion = deepcopy(sistemasClimatizacion)
    nuevoSistemasMixto3 = deepcopy(sistemasMixto3)
    for eq in nuevoSistemasClimatizacion:
        eq[5][2] = ['0', '0']

    for eq in nuevoSistemasMixto3:
        eq[5][2] = [
         '0', '0']

    conjuntoMejoras = [[],
     [nombreMedida,
      [
       sistemasACS, sistemasCalefaccion, nuevoSistemasRefrigeracion, 
       nuevoSistemasClimatizacion, 
       sistemasMixto2, nuevoSistemasMixto3, 
       sistemasContribuciones, 
       sistemasIluminacion, 
       sistemasVentilacion, sistemasVentiladores, 
       sistemasBombas, 
       sistemasTorresRefrigeracion],
      True]]
    objetoGrupoMedidas = grupoMedidasMejora(nombre='MD20', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
    listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    if objEdificio.programa != 'Residencial':
        nombreMedida = _('Mejora de la eficiencia de la iluminación')
        nuevoSistemasIluminacion = deepcopy(sistemasIluminacion)
        for eq in nuevoSistemasIluminacion:
            eq[3] = 3.0
            iluminancia = float(eq[9][1])
            superf = float(eq[5])
            nuevaPotencia = 3.0 * superf * iluminancia / 100.0
            eq[2] = nuevaPotencia
            eq[8] = 'Conocido(ensayado/justificado)'
            eq[9] = [str(nuevaPotencia), str(iluminancia)]

        conjuntoMejoras = [[],
         [nombreMedida,
          [
           sistemasACS, sistemasCalefaccion, sistemasRefrigeracion, 
           sistemasClimatizacion, 
           sistemasMixto2, 
           sistemasMixto3, sistemasContribuciones, 
           nuevoSistemasIluminacion, 
           sistemasVentilacion, sistemasVentiladores, 
           sistemasBombas, 
           sistemasTorresRefrigeracion],
          True]]
        objetoGrupoMedidas = grupoMedidasMejora(nombre='MD21', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
        listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
        nombreMedida = _('Incorporación/mejora de equipos de recuperación de calor')
        nuevoSistemasVentilacion = deepcopy(sistemasVentilacion)
        for eq in nuevoSistemasVentilacion:
            eq[3] = True
            if float(eq[4]) < 70:
                eq[4] = 70

        conjuntoMejoras = [[],
         [nombreMedida,
          [
           sistemasACS, sistemasCalefaccion, sistemasRefrigeracion, 
           sistemasClimatizacion, 
           sistemasMixto2, 
           sistemasMixto3, sistemasContribuciones, 
           sistemasIluminacion, 
           nuevoSistemasVentilacion, sistemasVentiladores, 
           sistemasBombas, 
           sistemasTorresRefrigeracion],
          True]]
        objetoGrupoMedidas = grupoMedidasMejora(nombre='MD22', datosEdificioOriginal=objEdificio, mejoras=conjuntoMejoras)
        listadoConjuntosMMPorDefecto.append(objetoGrupoMedidas)
    return listadoConjuntosMMPorDefecto