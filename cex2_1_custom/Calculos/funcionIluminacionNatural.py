# Embedded file name: Calculos\funcionIluminacionNatural.pyc
"""
Modulo: funcionIluminacionNatural.py

"""

def calculoRadiacionSolarHuecosParaIluminacion(listadoHuecos = [], areaInst = 0.0, zonaInst = ''):
    """
    Metodo: calculo_ventanas_iluminacion
    areaInst: area de la zona cubierta por la instalacion de iluminacion
    zonaInst: zona cubierta por la instalacion de iluminaci\xf3n
    Calculo del gvis, en funcion de la radiacion solar que entra por los huecos de la zona
    
    """
    g_vis_suma = 0
    for fila in listadoHuecos:
        if zonaInst == '' or zonaInst == fila.subgrupo:
            tipo = fila.tipo
            A = float(fila.superficie)
            FS = float(fila.Gvidrio)
            orientacion = fila.orientacion
            porcMarco = float(fila.porcMarco) / 100
            corrFS = float(fila.correctorFSCTE)
            g_vis = 0
            if tipo == 'Lucernario':
                orientacion = tipo
            K_orientacion = factorConversionPorOrientacion(orientacion)
            g_vis = FS * K_orientacion * A * (1 - porcMarco) * corrFS
            g_vis_suma += g_vis

    if areaInst > 0:
        g_vis_iluminacion = g_vis_suma / areaInst
    else:
        g_vis_iluminacion = 0.0
    return g_vis_iluminacion


def fraccionamientoConsumo(calendario, iluminacion, gVis):
    """
    Metodo: fraccionamientoConsumo
    
    
    ARGUMENTOS:
                calendario:
                iluminacion:
                gVis):
    """
    valoresGVisTabla = [0,
     0.0024,
     0.012,
     0.024,
     0.048,
     0.072,
     0.096,
     0.12,
     0.144,
     0.168,
     0.192,
     0.216]
    valoresIluminacionTabla = [100,
     300,
     500,
     700,
     1000,
     2000]
    if '8h' in calendario:
        tabla = [[1.0,
          0.83,
          0.51,
          0.41,
          0.37,
          0.36,
          0.36,
          0.35,
          0.35,
          0.35,
          0.35,
          0.35],
         [1.0,
          0.92,
          0.74,
          0.59,
          0.45,
          0.41,
          0.39,
          0.38,
          0.37,
          0.37,
          0.36,
          0.36],
         [1.0,
          0.95,
          0.82,
          0.7,
          0.54,
          0.47,
          0.43,
          0.41,
          0.39,
          0.38,
          0.38,
          0.37],
         [1.0,
          0.96,
          0.85,
          0.76,
          0.61,
          0.52,
          0.47,
          0.44,
          0.42,
          0.4,
          0.39,
          0.39],
         [1.0,
          0.97,
          0.88,
          0.81,
          0.69,
          0.6,
          0.53,
          0.49,
          0.46,
          0.44,
          0.42,
          0.41],
         [1.0,
          0.99,
          0.93,
          0.88,
          0.81,
          0.74,
          0.68,
          0.63,
          0.59,
          0.55,
          0.52,
          0.5]]
    elif '12h' in calendario:
        tabla = [[1.0,
          0.87,
          0.63,
          0.54,
          0.48,
          0.46,
          0.45,
          0.45,
          0.44,
          0.44,
          0.44,
          0.43],
         [1.0,
          0.94,
          0.81,
          0.69,
          0.58,
          0.53,
          0.51,
          0.49,
          0.48,
          0.47,
          0.46,
          0.46],
         [1.0,
          0.96,
          0.86,
          0.77,
          0.65,
          0.59,
          0.55,
          0.53,
          0.51,
          0.5,
          0.49,
          0.48],
         [1.0,
          0.97,
          0.89,
          0.82,
          0.71,
          0.64,
          0.59,
          0.56,
          0.54,
          0.53,
          0.51,
          0.5],
         [1.0,
          0.98,
          0.92,
          0.86,
          0.77,
          0.7,
          0.65,
          0.61,
          0.58,
          0.56,
          0.55,
          0.53],
         [1.0,
          0.99,
          0.95,
          0.91,
          0.86,
          0.81,
          0.76,
          0.72,
          0.69,
          0.66,
          0.64,
          0.62]]
    elif '16h' in calendario:
        tabla = [[1.0,
          0.89,
          0.66,
          0.57,
          0.52,
          0.51,
          0.5,
          0.49,
          0.49,
          0.49,
          0.49,
          0.48],
         [1.0,
          0.95,
          0.82,
          0.72,
          0.61,
          0.57,
          0.54,
          0.53,
          0.52,
          0.51,
          0.51,
          0.5],
         [1.0,
          0.97,
          0.88,
          0.8,
          0.68,
          0.62,
          0.59,
          0.56,
          0.55,
          0.54,
          0.53,
          0.52],
         [1.0,
          0.98,
          0.9,
          0.84,
          0.74,
          0.67,
          0.63,
          0.6,
          0.58,
          0.56,
          0.55,
          0.54],
         [1.0,
          0.98,
          0.92,
          0.87,
          0.79,
          0.73,
          0.68,
          0.64,
          0.62,
          0.6,
          0.58,
          0.57],
         [1.0,
          0.99,
          0.95,
          0.92,
          0.87,
          0.83,
          0.78,
          0.75,
          0.72,
          0.69,
          0.67,
          0.65]]
    elif '24h' in calendario:
        tabla = [[1.0,
          0.92,
          0.77,
          0.7,
          0.67,
          0.65,
          0.65,
          0.64,
          0.64,
          0.64,
          0.64,
          0.64],
         [1.0,
          0.96,
          0.88,
          0.8,
          0.73,
          0.7,
          0.68,
          0.67,
          0.66,
          0.66,
          0.66,
          0.65],
         [1.0,
          0.98,
          0.92,
          0.86,
          0.78,
          0.74,
          0.71,
          0.7,
          0.69,
          0.68,
          0.67,
          0.67],
         [1.0,
          0.98,
          0.93,
          0.89,
          0.82,
          0.77,
          0.74,
          0.72,
          0.71,
          0.7,
          0.69,
          0.68],
         [1.0,
          0.99,
          0.95,
          0.91,
          0.85,
          0.81,
          0.78,
          0.75,
          0.74,
          0.72,
          0.71,
          0.7],
         [1.0,
          0.99,
          0.97,
          0.95,
          0.91,
          0.88,
          0.85,
          0.83,
          0.81,
          0.79,
          0.77,
          0.76]]
    else:
        return -1
    fila_Iluminacion = []
    if iluminacion <= 100.0:
        iluminacion = 100.0
        fila_Iluminacion = tabla[0]
    else:
        if iluminacion > 2000.0:
            return 1.0
        for v, t in zip(valoresIluminacionTabla, tabla):
            if v < iluminacion:
                fila_anterior = t
                valor_Iluminacion_anterior = v
            else:
                fila_actual = t
                valor_Iluminacion_actual = v
                break

        factor = (float(iluminacion) - valor_Iluminacion_anterior) / (valor_Iluminacion_actual - valor_Iluminacion_anterior)
        fila_Iluminacion = [ x + (y - x) * factor for x, y in zip(fila_anterior, fila_actual) ]
    if gVis < 0.0:
        fraccionamiento = 1
    elif gVis >= 0.216:
        fraccionamiento = fila_Iluminacion[-1]
    else:
        for v, t in zip(valoresGVisTabla, fila_Iluminacion):
            if v <= gVis:
                fila_anterior = t
                valor_Iluminacion_anterior = v
            else:
                fila_actual = t
                valor_Iluminacion_actual = v
                break

        factor = (float(gVis) - valor_Iluminacion_anterior) / (valor_Iluminacion_actual - valor_Iluminacion_anterior)
        fraccionamiento = fila_anterior + (fila_actual - fila_anterior) * factor
    return fraccionamiento


def factorConversionPorOrientacion(orientacion):
    """
    Metodo: factorConversionPorOrientacion
    
    
    ARGUMENTOS:
                orientacion:
    """
    if orientacion == 'Norte':
        return 0.36
    elif orientacion == 'Sur':
        return 1.0
    elif orientacion == 'Este':
        return 0.78
    elif orientacion == 'Oeste':
        return 0.78
    elif orientacion == 'SE':
        return 0.95
    elif orientacion == 'SO':
        return 0.95
    elif orientacion == 'NE':
        return 0.51
    elif orientacion == 'NO':
        return 0.51
    elif orientacion == 'Lucernario':
        return 1.33
    else:
        return -1.0