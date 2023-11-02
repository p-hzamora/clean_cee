# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Calculos\limitesCTEyEdifRef.pyc
# Compiled at: 2014-12-18 13:20:16
"""
Modulo: limitesCTEyEdifRef.py

"""

def Calculo_parametros_maximos(cerramientos, ventanas):
    """
    Metodo: Calculo_parametros_maximos

    ARGUMENTOS:
                cerramientos:
                ventanas:
    """
    cerr_ext_max = -1000
    CT_max = -1000
    no_habit_max = -1000
    suelo_ext_max = -1000
    cub_max = -1000
    medianera_max = -1000
    no_calefac_max = -1000
    vidrios_max = -1000
    marcos_max = -1000
    for cerr in cerramientos:
        U_cerr = float(cerr[3])
        if cerr[1] == 'Muro Exterior' and cerr[5] != 'Suelo' and cerr[5] != 'Techo':
            if cerr_ext_max < U_cerr:
                cerr_ext_max = U_cerr
        elif cerr[1] == 'Cerramiento en Contacto Terreno' and cerr[5] != 'Techo':
            if CT_max < U_cerr:
                CT_max = U_cerr
        elif cerr[1] == 'Pared Interior contacto espac. no habit.' and cerr[5] != 'Suelo' and cerr[5] != 'Techo':
            if no_habit_max < U_cerr:
                no_habit_max = U_cerr
        elif cerr[1] == 'Suelo al Exterior' or cerr[1] == 'Muro Exterior' and cerr[5] == 'Suelo' or cerr[1] == 'Pared Interior contacto espac. no habit.' and cerr[5] == 'Suelo':
            if suelo_ext_max < U_cerr:
                suelo_ext_max = U_cerr
        elif cerr[1] == 'Cubierta' or cerr[1] == 'Muro Exterior' and cerr[5] == 'Techo' or cerr[1] == 'Pared Interior contacto espac. no habit.' and cerr[5] == 'Techo':
            if cub_max < U_cerr:
                cub_max = U_cerr
        elif cerr[1] == 'Medianera':
            if medianera_max < U_cerr:
                medianera_max = U_cerr
        elif cerr[1] == 'Pared Interior con espac. habit. no calefac.':
            if no_calefac_max < U_cerr:
                no_calefac_max = U_cerr

    for vent in ventanas:
        U = float(vent.Uvidrio)
        U_marco = float(vent.Umarco)
        porc_marco = float(vent.porcMarco)
        valor_U_vidrio = U * (100 - porc_marco) / 100 + U_marco * porc_marco / 100
        if vidrios_max < valor_U_vidrio:
            vidrios_max = valor_U_vidrio

    if cerr_ext_max != -1000:
        cerr_ext_max = str(round(cerr_ext_max, 2))
    else:
        cerr_ext_max = 'No def.'
    if CT_max != -1000:
        CT_max = str(round(CT_max, 2))
    else:
        CT_max = 'No def.'
    if no_habit_max != -1000:
        no_habit_max = str(round(no_habit_max, 2))
    else:
        no_habit_max = 'No def.'
    if suelo_ext_max != -1000:
        suelo_ext_max = str(round(suelo_ext_max, 2))
    else:
        suelo_ext_max = 'No def.'
    if cub_max != -1000:
        cub_max = str(round(cub_max, 2))
    else:
        cub_max = 'No def.'
    if medianera_max != -1000:
        medianera_max = str(round(medianera_max, 2))
    else:
        medianera_max = 'No def.'
    if no_calefac_max != -1000:
        no_calefac_max = str(round(no_calefac_max, 2))
    else:
        no_calefac_max = 'No def.'
    if vidrios_max != -1000:
        vidrios_max = str(round(vidrios_max, 2))
    else:
        vidrios_max = 'No def.'
    if marcos_max != -1000:
        marcos_max = str(round(marcos_max, 2))
    else:
        marcos_max = 'No def.'
    valores_max_proyecto = [cerr_ext_max, CT_max, no_habit_max, suelo_ext_max, cub_max, 
     vidrios_max, 
     medianera_max, no_calefac_max]
    return valores_max_proyecto


def getMasaM2CerrReferencia(tipo='', enContactoCon=''):
    """
    Metodo: cerramientosEdificioReferencia

    ARGUMENTOS:
        tipo: Fachada, Cubierta, Suelo
        enContactoCon: aire, terreno, edificio
    Devuelve la masa por m2 para los cerramientos indicados
    """
    if tipo == 'Fachada' and enContactoCon == 'edificio':
        Peso_ref = 163.2
    elif tipo == 'Fachada' and enContactoCon == 'aire':
        Peso_ref = 185.3
    elif tipo == 'Cubierta' and enContactoCon == 'aire':
        Peso_ref = 585.5
    elif tipo == 'Suelo' and enContactoCon == 'aire':
        Peso_ref = 558.5
    return Peso_ref


def getValoresLimiteCerr(zonaHE1='', tipo='', enContactoCon=''):
    """
    Metodo: getValoresLimiteCerr

    ARGUMENTOS:
                zonaHE1:
                tipo: Fachada, Cubierta, Suelo
                enContactoCon: aire, terreno, edificio
        Devuelve el valor limite del CTE
    """
    diccUopacosReferencia = {'alpha1': [0.94, 0.53, 0.5, 0.29], 'alpha2': [
                0.94, 0.53, 0.5, 0.29], 
       'alpha3': [
                0.94, 0.53, 0.5, 0.29], 
       'alpha4': [
                0.94, 0.53, 0.5, 0.29], 
       'A1': [
            0.94, 0.53, 0.5, 0.29], 
       'A2': [
            0.94, 0.53, 0.5, 0.29], 
       'A3': [
            0.94, 0.53, 0.5, 0.29], 
       'A4': [
            0.94, 0.53, 0.5, 0.29], 
       'B1': [
            0.82, 0.52, 0.45, 0.32], 
       'B2': [
            0.82, 0.52, 0.45, 0.32], 
       'B3': [
            0.82, 0.52, 0.45, 0.3], 
       'B4': [
            0.82, 0.52, 0.45, 0.28], 
       'C1': [
            0.73, 0.5, 0.41, 0.37], 
       'C2': [
            0.73, 0.5, 0.41, 0.32], 
       'C3': [
            0.73, 0.5, 0.41, 0.28], 
       'C4': [
            0.73, 0.5, 0.41, 0.27], 
       'D1': [
            0.66, 0.49, 0.38, 0.36], 
       'D2': [
            0.66, 0.49, 0.38, 0.31], 
       'D3': [
            0.66, 0.49, 0.38, 0.28], 
       'E1': [
            0.57, 0.48, 0.35, 0.36]}
    UmurosfachadaCerrTerreno = diccUopacosReferencia[zonaHE1][0]
    Usuelo = diccUopacosReferencia[zonaHE1][1]
    Ucubierta = diccUopacosReferencia[zonaHE1][2]
    FSlucernario = diccUopacosReferencia[zonaHE1][3]
    if tipo == 'Fachada' and enContactoCon == 'edificio':
        valor = 0.0
    elif tipo == 'Fachada' and enContactoCon == 'aire':
        valor = UmurosfachadaCerrTerreno
    elif tipo == 'Cubierta' and enContactoCon == 'aire':
        valor = Ucubierta
    elif tipo == 'Suelo' and enContactoCon == 'aire':
        valor = Usuelo
    elif tipo == 'Lucernario':
        valor = FSlucernario
    return valor


def getPermeabilidadLimiteHuecos(zonaHE1=''):
    """
    Metodo: getPermeabilidadLimiteHuecos
    Argumentos: zonaHE1
    Devuelve la permeabilidad que le corresponde
    """
    if 'alpha' in zonaHE1 or 'A' in zonaHE1 or 'B' in zonaHE1:
        permeabilidad = 50.0
    else:
        permeabilidad = 27.0
    return permeabilidad


def getUlimiteHuecos(zonaHE1='', porc_huecos=0.0, orientacion=''):
    """
    Metodo: getUlimiteHuecos
    ARGUMENTOS:
                zonaHE1:
                porc_huecos: tanto por uno de porcentaje de huecos en orientacion
                orientacion
        Devuelve el valor de transmitancia termica limite del hueco
    """
    Transmit_lim_cerr = []
    contador_porc_huecos = 0
    if porc_huecos <= 0.1:
        contador_porc_huecos = 0
    elif porc_huecos <= 0.2:
        contador_porc_huecos = 1
    elif porc_huecos <= 0.3:
        contador_porc_huecos = 2
    elif porc_huecos <= 0.4:
        contador_porc_huecos = 3
    elif porc_huecos <= 0.5:
        contador_porc_huecos = 4
    else:
        contador_porc_huecos = 5
    if orientacion == 'Norte' or orientacion == 'NO' or orientacion == 'NE':
        contador_orientacion = 0
    elif orientacion == 'Este' or orientacion == 'Oeste':
        contador_orientacion = 1
    elif orientacion == 'Sur':
        contador_orientacion = 2
    elif orientacion == 'SE' or orientacion == 'SO':
        contador_orientacion = 3
    if zonaHE1 in ('alpha1', 'alpha2', 'alpha3', 'alpha4', 'A1', 'A2', 'A3', 'A4'):
        Transmit_lim_cerr = [
         [
          5.7, 5.7, 5.7, 5.7],
         [
          4.7, 5.7, 5.7, 5.7],
         [
          4.1, 5.5, 5.7, 5.7],
         [
          3.8, 5.2, 5.7, 5.7],
         [
          3.5, 5.0, 5.7, 5.7],
         [
          3.4, 4.8, 5.7, 5.7]]
    elif zonaHE1 in ('B1', 'B2', 'B3', 'B4'):
        Transmit_lim_cerr = [
         [
          5.4, 5.7, 5.7, 5.7],
         [
          3.8, 4.9, 5.7, 5.7],
         [
          3.3, 4.3, 5.7, 5.7],
         [
          3.0, 4.0, 5.6, 5.6],
         [
          2.8, 3.7, 5.4, 5.4],
         [
          2.7, 3.6, 5.2, 5.2]]
    elif zonaHE1 in ('C1', 'C2', 'C3', 'C4'):
        Transmit_lim_cerr = [
         [
          4.4, 4.4, 4.4, 4.4],
         [
          3.4, 3.9, 4.4, 4.4],
         [
          2.9, 3.3, 4.3, 4.3],
         [
          2.6, 3.0, 3.9, 3.9],
         [
          2.4, 2.8, 3.6, 3.6],
         [
          2.2, 2.7, 3.5, 3.5]]
    elif zonaHE1 in ('D1', 'D2', 'D3'):
        Transmit_lim_cerr = [
         [
          3.5, 3.5, 3.5, 3.5],
         [
          3.0, 3.5, 3.5, 3.5],
         [
          2.5, 2.9, 3.5, 3.5],
         [
          2.2, 2.6, 3.4, 3.4],
         [
          2.1, 2.5, 3.2, 3.2],
         [
          1.9, 2.3, 3.0, 3.0]]
    elif zonaHE1 in ('E1', ):
        Transmit_lim_cerr = [
         [
          3.1, 3.1, 3.1, 3.1],
         [
          3.1, 3.1, 3.1, 3.1],
         [
          2.6, 3.0, 3.1, 3.1],
         [
          2.2, 2.7, 3.1, 3.1],
         [
          2.0, 2.4, 3.1, 3.1],
         [
          1.9, 2.3, 3.0, 3.0]]
    Ulimite = Transmit_lim_cerr[contador_porc_huecos][contador_orientacion]
    return Ulimite


def getFSHuecosInviernoReferencia(Uvidrio=0.0):
    """
    Metodo: FSinviernoReferencia

    ARGUMENTOS:
        Uvidrio
        
    Devuelve el FS de invierno para el edificio de referencia
    """
    matriz_FS_invierno = [
     [
      5.7, 0.85],
     [
      5.5, 0.85],
     [
      5.3, 0.84],
     [
      5.1, 0.83],
     [
      4.9, 0.83],
     [
      4.7, 0.82],
     [
      4.5, 0.81],
     [
      4.3, 0.8],
     [
      4.1, 0.79],
     [
      3.9, 0.78],
     [
      3.7, 0.77],
     [
      3.5, 0.76],
     [
      3.3, 0.74],
     [
      3.1, 0.73],
     [
      2.9, 0.72],
     [
      2.7, 0.7],
     [
      2.5, 0.68],
     [
      2.3, 0.67],
     [
      2.1, 0.65],
     [
      1.9, 0.63]]
    contador = 0
    FS_invierno = 0.0
    if Uvidrio >= 5.7:
        FS_invierno = 0.85
    elif Uvidrio <= 1.9:
        FS_invierno = 0.63
    else:
        for i in matriz_FS_invierno:
            if Uvidrio > i[0]:
                U_1 = matriz_FS_invierno[contador - 1][0]
                U_2 = matriz_FS_invierno[contador][0]
                FS_1 = matriz_FS_invierno[contador - 1][1]
                FS_2 = matriz_FS_invierno[contador][1]
                FS_invierno = (FS_2 - FS_1) / (U_2 - U_1) * (Uvidrio - U_1) + FS_1
                break
            else:
                contador += 1

    return FS_invierno


def getFSlimiteHuecos(zonaHE1='', porc_huecos=0.0, orientacion='', esBajaCarga=True):
    """
    Metodo: getFSlimiteHuecos

    ARGUMENTOS:
                zonaHE1:
                porc_huecos:
                orientacion:
                esBajaCarga: True si es baja carga, False si es altaCarga
    """
    if orientacion in ('Norte', 'NE', 'NO'):
        FShlim = '-'
    else:
        contador_porc_huecos = 0
        if porc_huecos <= 0.1:
            contador_porc_huecos = 0
        elif porc_huecos <= 0.2:
            contador_porc_huecos = 1
        elif porc_huecos <= 0.3:
            contador_porc_huecos = 2
        elif porc_huecos <= 0.4:
            contador_porc_huecos = 3
        elif porc_huecos <= 0.5:
            contador_porc_huecos = 4
        else:
            contador_porc_huecos = 5
        if orientacion == 'Este' or orientacion == 'Oeste':
            contador_orientacion = 0
        elif orientacion == 'Sur':
            contador_orientacion = 1
        elif orientacion == 'SE' or orientacion == 'SO':
            contador_orientacion = 2
        if zonaHE1 in ('alpha1', 'A1'):
            FS_lim_bajaCarga = [
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-']]
            FS_lim_altaCarga = [['-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.56, '-', 0.6],
             [
              0.47, '-', 0.52],
             [
              0.42, '-', 0.46]]
        elif zonaHE1 in ('alpha2', 'A2'):
            FS_lim_bajaCarga = [
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.59, '-', '-'],
             [
              0.51, '-', 0.55]]
            FS_lim_altaCarga = [['-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.6, '-', '-'],
             [
              0.47, '-', 0.51],
             [
              0.4, 0.58, 0.43],
             [
              0.35, 0.52, 0.38]]
        elif zonaHE1 in ('alpha3', 'A3'):
            FS_lim_bajaCarga = [
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.57, '-', 0.6],
             [
              0.5, '-', 0.54]]
            FS_lim_altaCarga = [['-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.6, '-', '-'],
             [
              0.48, '-', 0.51],
             [
              0.41, 0.57, 0.44],
             [
              0.36, 0.51, 0.39]]
        elif zonaHE1 in ('alpha4', 'A4'):
            FS_lim_bajaCarga = [
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.57, '-', 0.58],
             [
              0.47, '-', 0.48],
             [
              0.4, 0.55, 0.42]]
            FS_lim_altaCarga = [['-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.56, '-', 0.57],
             [
              0.43, 0.59, 0.44],
             [
              0.35, 0.49, 0.37],
             [
              0.3, 0.42, 0.32]]
        elif zonaHE1 == 'B1':
            FS_lim_bajaCarga = [
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-']]
            FS_lim_altaCarga = [['-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.56, '-', 0.6],
             [
              0.47, '-', 0.52],
             [
              0.42, '-', 0.46]]
        elif zonaHE1 == 'B2':
            FS_lim_bajaCarga = [
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.59, '-', '-'],
             [
              0.51, '-', 0.55]]
            FS_lim_altaCarga = [['-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.6, '-', '-'],
             [
              0.47, '-', 0.51],
             [
              0.4, 0.58, 0.43],
             [
              0.35, 0.52, 0.38]]
        elif zonaHE1 == 'B3':
            FS_lim_bajaCarga = [
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.53, '-', 0.59],
             [
              0.46, '-', 0.52]]
            FS_lim_altaCarga = [['-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.57, '-', '-'],
             [
              0.45, '-', 0.5],
             [
              0.38, 0.57, 0.43],
             [
              0.33, 0.51, 0.38]]
        elif zonaHE1 == 'B4':
            FS_lim_bajaCarga = [
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.55, '-', 0.58],
             [
              0.45, '-', 0.48],
             [
              0.39, 0.55, 0.41]]
            FS_lim_altaCarga = [['-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.55, '-', 0.57],
             [
              0.42, 0.59, 0.44],
             [
              0.34, 0.49, 0.36],
             [
              0.29, 0.42, 0.31]]
        elif zonaHE1 == 'C1':
            FS_lim_bajaCarga = [
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-']]
            FS_lim_altaCarga = [['-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.56, '-', 0.6],
             [
              0.47, '-', 0.52],
             [
              0.42, '-', 0.46]]
        elif zonaHE1 == 'C2':
            FS_lim_bajaCarga = [
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.59, '-', '-'],
             [
              0.51, '-', 0.55]]
            FS_lim_altaCarga = [['-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.6, '-', '-'],
             [
              0.47, '-', 0.51],
             [
              0.4, 0.58, 0.43],
             [
              0.35, 0.52, 0.38]]
        elif zonaHE1 == 'C3':
            FS_lim_bajaCarga = [
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.51, '-', 0.54],
             [
              0.43, '-', 0.47]]
            FS_lim_altaCarga = [['-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.55, '-', 0.59],
             [
              0.43, '-', 0.46],
             [
              0.35, 0.52, 0.39],
             [
              0.31, 0.46, 0.34]]
        elif zonaHE1 == 'C4':
            FS_lim_bajaCarga = [
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.54, '-', 0.56],
             [
              0.47, '-', 0.46],
             [
              0.38, 0.53, 0.39]]
            FS_lim_altaCarga = [
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.54, '-', 0.56],
             [
              0.41, 0.57, 0.43],
             [
              0.34, 0.47, 0.35],
             [
              0.29, 0.4, 0.3]]
        elif zonaHE1 == 'D1':
            FS_lim_bajaCarga = [
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-']]
            FS_lim_altaCarga = [['-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.54, '-', 0.58],
             [
              0.45, '-', 0.49],
             [
              0.4, 0.57, 0.44]]
        elif zonaHE1 == 'D2':
            FS_lim_bajaCarga = [
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', 0.61],
             [
              0.49, '-', 0.53]]
            FS_lim_altaCarga = [
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.58, '-', 0.61],
             [
              0.46, '-', 0.49],
             [
              0.38, 0.54, 0.41],
             [
              0.33, 0.48, 0.36]]
        elif zonaHE1 == 'D3':
            FS_lim_bajaCarga = [
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.5, '-', 0.53],
             [
              0.42, 0.61, 0.46]]
            FS_lim_altaCarga = [['-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.54, '-', 0.57],
             [
              0.42, 0.58, 0.45],
             [
              0.35, 0.49, 0.37],
             [
              0.3, 0.43, 0.32]]
        elif zonaHE1 == 'E1':
            FS_lim_bajaCarga = [
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-']]
            FS_lim_altaCarga = [
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              '-', '-', '-'],
             [
              0.54, '-', 0.56],
             [
              0.45, 0.6, 0.49],
             [
              0.4, 0.54, 0.43]]
        if esBajaCarga == True:
            FS_lim = FS_lim_bajaCarga
        else:
            FS_lim = FS_lim_altaCarga
        FShlim = FS_lim[contador_porc_huecos][contador_orientacion]
    return FShlim


def getFiPTReferencia(zonaHE1='', tipo=''):
    if 'A' in zonaHE1 or 'alpha' in zonaHE1:
        contador_j = 0
    elif 'B' in zonaHE1:
        contador_j = 1
    elif 'C' in zonaHE1:
        contador_j = 2
    elif 'D' in zonaHE1:
        contador_j = 3
    elif 'E' in zonaHE1:
        contador_j = 4
    matriz_PT = [
     [
      1.082, 0.996, 0.919, 0.848, 0.771],
     [
      0.45, 0.45, 0.45, 0.45, 0.45],
     [
      0.45, 0.45, 0.45, 0.45, 0.45],
     [
      0.15, 0.15, 0.15, 0.15, 0.15],
     [
      -0.1, -0.15, -0.15, -0.15, -0.15],
     [
      0.4, 0.4, 0.4, 0.4, 0.4],
     [
      0.85, 0.85, 0.8, 0.75, 0.7],
     [
      0.15, 0.15, 0.15, 0.15, 0.15]]
    if tipo in ('Encuentro de fachada con forjado', 'Encuentro de fachada con voladizo'):
        contador_i = 0
    elif tipo in ('Encuentro de fachada con cubierta', ):
        contador_i = 1
    elif tipo in ('Encuentro de fachada con suelo en contacto con el aire', ):
        contador_i = 2
    elif tipo in ('Esquina hacia el exterior', ):
        contador_i = 3
    elif tipo in ('Esquina hacia el interior', ):
        contador_i = 4
    elif tipo in ('Contorno de hueco', 'Caja de Persiana', 'Jamba', 'Dintel', 'Alfeizar'):
        contador_i = 5
    elif tipo in ('Pilar integrado en fachada', 'Pilar en Esquina'):
        contador_i = 6
    elif tipo in ('Encuentro de fachada con solera', ):
        contador_i = 7
    else:
        contador_i = 0
    fi = matriz_PT[contador_i][contador_j]
    return fi


def getValoresMaximosCerrCTE2006(zona):
    """
    Metodo: getValoresMaximosCerrCTE2006

    ARGUMENTOS:
                zona:
        Valores tabla 2.3 CTE 2006
    """
    if zona == 1 or zona == 2:
        contador = 0
    elif zona == 3 or zona == 4:
        contador = 1
    elif zona == 5 or zona == 6 or zona == 7 or zona == 8:
        contador = 2
    elif zona == 9 or zona == 10 or zona == 11:
        contador = 3
    elif zona == 12:
        contador = 4
    valores_max_matriz = [[1.22, 0.69, 0.65, 5.7, 1.22],
     [
      1.07, 0.68, 0.59, 5.7, 1.07],
     [
      0.95, 0.65, 0.53, 4.4, 1.0],
     [
      0.86, 0.64, 0.49, 3.5, 1.0],
     [
      0.74, 0.62, 0.46, 3.1, 1.0]]
    valores_max = valores_max_matriz[contador]
    return valores_max