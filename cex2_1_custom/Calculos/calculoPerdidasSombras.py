# Embedded file name: Calculos\calculoPerdidasSombras.pyc
"""
Modulo: calculoPerdidasSombras.py

En este modulo se encuentran las funciones para calcular
el porcentaje de p\xe9rdidas de radacion por las sombras que afecten a la
ventana o panel
"""
import Image
import Polygon
import copy
from Calculos.calculoPoligonosPatronesSombra import compruebaPuntos

def tablaA(alfa, beta, porcentajes):
    """
    Metodo: tablaA
    Devuelve el porcentaje de perdidas paras las casillas A,
    en una tupla para diferenciar invierno y verano
    Necesita los datos de orientacion inclicancion y
    porcentajes de sombreamiento de cada casilla
    
    ARGUMENTOS:
                alfa:
                beta:
                porcentajes:
    
    
    """
    res = []
    for i in range(0, 10):
        res.append(float(porcentajes[i]))

    sumaVerano = 0
    sumaInvierno = 0
    if alfa == 'SO':
        perInvierno = [0.0572,
         0.0754,
         0.0275,
         0.0912,
         0.0074,
         0.0994,
         0,
         0.0809,
         0,
         0.0424]
        perVerano = [0.0007,
         0.0001,
         0.0013,
         0.0014,
         0,
         0.005,
         0,
         0.0011,
         0,
         0.0121]
    elif alfa == 'Sur':
        perInvierno = [0.0835,
         0.0723,
         0.0663,
         0.0628,
         0.0597,
         0.051,
         0.0387,
         0.0294,
         0.0144,
         0.0121]
        perVerano = [0.0005,
         0.0002,
         0.0022,
         0.0021,
         0.0041,
         0.004,
         0,
         0,
         0.0075,
         0.0075]
    elif alfa == 'Este':
        perInvierno = [0.0061,
         0,
         0.048,
         0,
         0.0867,
         0,
         0.1059,
         0,
         0.0742,
         0]
        perVerano = [0,
         0,
         0.0008,
         0,
         0.0023,
         0,
         0.004,
         0,
         0.0091,
         0]
    elif alfa == 'SE':
        perInvierno = [0.0765,
         0.0457,
         0.0872,
         0.0251,
         0.104,
         0.0062,
         0.0908,
         0,
         0.0478,
         0]
        perVerano = [0.0007,
         0.0004,
         0.0009,
         0.0012,
         0.0047,
         0,
         0.0009,
         0,
         0.0116,
         0]
    elif alfa == 'Oeste':
        perInvierno = [0,
         0.0073,
         0,
         0.0483,
         0,
         0.0873,
         0,
         0.101,
         0,
         0.0609]
        perVerano = [0,
         0,
         0,
         0.001,
         0,
         0.0024,
         0,
         0.0044,
         0,
         0.0104]
    elif alfa == 'Techo' or alfa == 'Lucernario':
        perInvierno = [0.0616,
         0.0549,
         0.0531,
         0.0486,
         0.0356,
         0.0309,
         0.0172,
         0.0142,
         0.0042,
         0.0036]
        perVerano = [0.0007,
         0.0006,
         0.0008,
         0.0007,
         0.0002,
         0.0001,
         0,
         0,
         0.0004,
         0.0004]
    else:
        perInvierno = [0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0]
        perVerano = [0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0]
    for i in range(len(res)):
        sumaVerano = sumaVerano + res[i] * perVerano[i]
        sumaInvierno = sumaInvierno + res[i] * perInvierno[i]

    return (sumaVerano, sumaInvierno)


def tablaB(alfa, beta, porcentajes):
    """
    Metodo: tablaB
    
    Devuelve el porcentaje de perdidas paras las casillas B,
    en una tupla para diferenciar invierno y verano
    Necesita los datos de orientacion inclicancion y
    porcentajes de sombreamiento de cada casilla
    
    ARGUMENTOS:
                alfa:
                beta:
                porcentajes:
    """
    res = []
    for i in range(10, 22):
        res.append(float(porcentajes[i]))

    sumaVerano = 0
    sumaInvierno = 0
    if alfa == 'SO':
        perInvierno = [0.0134,
         0.0164,
         0.0056,
         0.0266,
         0.0006,
         0.0249,
         0,
         0.0241,
         0,
         0.0091,
         0,
         0.0035]
        perVerano = [0.0018,
         0.0022,
         0.0009,
         0.0052,
         0,
         0.0014,
         0,
         0.005,
         0,
         0,
         0,
         0.0015]
    elif alfa == 'Sur':
        perInvierno = [0.0179,
         0.0151,
         0.015,
         0.0156,
         0.012,
         0.0127,
         0.01,
         0.0088,
         0.0031,
         0.0025,
         0.0001,
         0.0004]
        perVerano = [0.0051,
         0.0041,
         0.0038,
         0.0038,
         0.002,
         0.0024,
         0.003,
         0.003,
         0.0002,
         0.0005,
         0,
         0]
    elif alfa == 'Este':
        perInvierno = [0.0038,
         0,
         0.0267,
         0,
         0.045,
         0,
         0.0664,
         0,
         0.0232,
         0,
         0.0181,
         0]
        perVerano = [0,
         0,
         0.0024,
         0,
         0,
         0,
         0.0066,
         0,
         0,
         0,
         0.011,
         0]
    elif alfa == 'SE':
        perInvierno = [0.0195,
         0.0105,
         0.0237,
         0.0057,
         0.0238,
         0.0006,
         0.026,
         0,
         0.0117,
         0,
         0.004,
         0]
        perVerano = [0.0025,
         0.0017,
         0.0056,
         0.0009,
         0.0009,
         0,
         0.005,
         0,
         0,
         0,
         0.0041,
         0]
    elif alfa == 'Oeste':
        perInvierno = [0,
         0.0035,
         0,
         0.0291,
         0,
         0.0443,
         0,
         0.0588,
         0,
         0.0181,
         0,
         0.0186]
        perVerano = [0,
         0,
         0,
         0.0025,
         0,
         0,
         0,
         0.007,
         0,
         0,
         0,
         0.0096]
    elif alfa == 'Techo' or alfa == 'Lucernario':
        perInvierno = [0.0411,
         0.0335,
         0.0297,
         0.0305,
         0.0233,
         0.0199,
         0.0123,
         0.0102,
         0.0022,
         0.0017,
         0.0001,
         0.0002]
        perVerano = [0.0019,
         0.0017,
         0.0015,
         0.0015,
         0.0008,
         0.0007,
         0.0011,
         0.0011,
         0,
         0.0001,
         0,
         0]
    else:
        perInvierno = [0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0]
        perVerano = [0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0]
    for i in range(len(res)):
        sumaVerano = sumaVerano + res[i] * perVerano[i]
        sumaInvierno = sumaInvierno + res[i] * perInvierno[i]

    return (sumaVerano, sumaInvierno)


def tablaC(alfa, beta, porcentajes):
    """
    Metodo: tablaC
    
    Devuelve el porcentaje de perdidas paras las casillas C,
    en una tupla para diferenciar invierno y verano
    Necesita los datos de orientacion inclicancion y
    porcentajes de sombreamiento de cada casilla
    
    
    ARGUMENTOS:
                alfa:
                beta:
                porcentajes:
    
    """
    res = []
    for i in range(22, 34):
        res.append(float(porcentajes[i]))

    sumaVerano = 0
    sumaInvierno = 0
    if alfa == 'SO':
        perInvierno = [0.0013,
         0.0041,
         0.0002,
         0.0027,
         0,
         0.001,
         0,
         0.0007,
         0,
         0.0052,
         0,
         0]
        perVerano = [0.0016,
         0.0043,
         0.0003,
         0.0034,
         0,
         0.0018,
         0,
         0.0014,
         0,
         0.0048,
         0,
         0]
    elif alfa == 'Sur':
        perInvierno = [0.0026,
         0.0025,
         0.0023,
         0.0021,
         0.0016,
         0.0015,
         0,
         0,
         0.0012,
         0.0012,
         0,
         0]
        perVerano = [0.0048,
         0.0047,
         0.0044,
         0.0039,
         0.0027,
         0.0026,
         0.0003,
         0.0003,
         0.0016,
         0.0016,
         0,
         0]
    elif alfa == 'Este':
        perInvierno = [0.0011,
         0,
         0.0021,
         0,
         0.0042,
         0,
         0.006,
         0,
         0.0094,
         0,
         0,
         0]
        perVerano = [0.0005,
         0,
         0.0011,
         0,
         0.0023,
         0,
         0.0034,
         0,
         0.0051,
         0,
         0,
         0]
    elif alfa == 'SE':
        perInvierno = [0.0038,
         0.0013,
         0.0027,
         0,
         0.0009,
         0,
         0.001,
         0,
         0.0048,
         0,
         0,
         0]
        perVerano = [0.0041,
         0.0016,
         0.0036,
         0.0001,
         0.002,
         0,
         0.0016,
         0,
         0.0046,
         0,
         0,
         0]
    elif alfa == 'Oeste':
        perInvierno = [0,
         0.0012,
         0,
         0.0023,
         0,
         0.0046,
         0,
         0.0061,
         0,
         0.0103,
         0,
         0]
        perVerano = [0,
         0.0006,
         0,
         0.0011,
         0,
         0.0025,
         0,
         0.0037,
         0,
         0.0055,
         0,
         0]
    elif alfa == 'Techo' or alfa == 'Lucernario':
        perInvierno = [0.0052,
         0.0049,
         0.0038,
         0.0036,
         0.0066,
         0.0065,
         0,
         0,
         0.0028,
         0.0028,
         0,
         0]
        perVerano = [0.0025,
         0.0024,
         0.0019,
         0.0018,
         0.0029,
         0.0029,
         0.0002,
         0.0003,
         0.0012,
         0.0013,
         0,
         0]
    else:
        perInvierno = [0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0]
        perVerano = [0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0]
    for i in range(len(res)):
        sumaVerano = sumaVerano + res[i] * perVerano[i]
        sumaInvierno = sumaInvierno + res[i] * perInvierno[i]

    return (sumaVerano, sumaInvierno)


def tablaD(alfa, beta, porcentajes):
    """
    Metodo: tablaD
    
    Devuelve el porcentaje de perdidas paras las casillas D,
    en una tupla para diferenciar invierno y verano
    Necesita los datos de orientacion inclicancion y
    porcentajes de sombreamiento de cada casilla
    
    
    ARGUMENTOS:
                alfa:
                beta:
                porcentajes:
    """
    res = []
    for i in range(34, 48):
        res.append(float(porcentajes[i]))

    sumaVerano = 0
    sumaInvierno = 0
    if alfa == 'SO':
        perInvierno = [0.0008,
         0.0025,
         0,
         0.0003,
         0,
         0.0026,
         0,
         0.0038,
         0,
         0,
         0,
         0,
         0,
         0.0162]
        perVerano = [0.0268,
         0.0586,
         0.0017,
         0.0862,
         0,
         0.0929,
         0,
         0.1014,
         0,
         0,
         0,
         0.0005,
         0,
         0.0108]
    elif alfa == 'Sur':
        perInvierno = [0.0017,
         0.0014,
         0,
         0,
         0.001,
         0.001,
         0.0009,
         0.0009,
         0,
         0,
         0,
         0,
         0.0045,
         0.0033]
        perVerano = [0.0962,
         0.0898,
         0.0811,
         0.0797,
         0.0575,
         0.0568,
         0.0318,
         0.0293,
         0,
         0,
         0.0001,
         0.0001,
         0.0039,
         0.0039]
    elif alfa == 'Este':
        perInvierno = [0.0012,
         0,
         0.0026,
         0,
         0.0036,
         0,
         0.0069,
         0,
         0,
         0,
         0,
         0,
         0.0359,
         0]
        perVerano = [0.0086,
         0,
         0.0387,
         0,
         0.0726,
         0,
         0.1223,
         0,
         0,
         0,
         0.0004,
         0,
         0.0113,
         0]
    elif alfa == 'SE':
        perInvierno = [0.0024,
         0.0007,
         0.0002,
         0,
         0.0023,
         0,
         0.0036,
         0,
         0,
         0,
         0,
         0,
         0.0159,
         0]
        perVerano = [0.0608,
         0.0233,
         0.0917,
         0.0018,
         0.1159,
         0,
         0.1172,
         0,
         0,
         0,
         0.0004,
         0,
         0.0104,
         0]
    elif alfa == 'Oeste':
        perInvierno = [0,
         0.0013,
         0,
         0.003,
         0,
         0.004,
         0,
         0.0076,
         0,
         0,
         0,
         0,
         0,
         0.0359]
        perVerano = [0,
         0.0115,
         0,
         0.0453,
         0,
         0.0782,
         0,
         0.1155,
         0,
         0,
         0,
         0.0006,
         0,
         0.0119]
    elif alfa == 'Techo' or alfa == 'Lucernario':
        perInvierno = [0.0066,
         0.0056,
         0.0025,
         0.0026,
         0.0038,
         0.0038,
         0.0038,
         0.0038,
         0,
         0,
         0,
         0,
         0.0021,
         0.0018]
        perVerano = [0.081,
         0.0764,
         0.0692,
         0.0762,
         0.0607,
         0.074,
         0.0575,
         0.0619,
         0,
         0,
         0.0001,
         0.0001,
         0.0004,
         0.0004]
    else:
        perInvierno = [0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0]
        perVerano = [0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0]
    for i in range(len(res)):
        sumaVerano = sumaVerano + res[i] * perVerano[i]
        sumaInvierno = sumaInvierno + res[i] * perInvierno[i]

    return (sumaVerano, sumaInvierno)


def leerCasillas(nombrePatron, datosSombras):
    """
    Metodo: leerCasillas
    
    
    ARGUMENTOS:
                nombrePatron:
                datosSombras:
    """
    for somb in datosSombras:
        if somb[0] == nombrePatron:
            porcentajes = somb[2]
            return porcentajes


def sombrasGuardadas(obj):
    """
    Metodo: sombrasGuardadas
    
    
    ARGUMENTOS:
                obj):   ####Me devuelve una lista con los nombres de los patrones de sombras guardados en temp.t:
    """
    nombres = []
    for i in obj.datosSombras:
        nombres.append(i[0])

    return nombres


def calculoPorcentajesSombras(listaPuntos, provincia):
    """
    Metodo: calculoPorcentajesSombras
    
    
    ARGUMENTOS:
                listaPuntos:
                provincia:
    """
    import directorios
    Directorio = directorios.BuscaDirectorios().Directorio
    im = Image.open(Directorio + '/Imagenes/prob2.bmp')
    if provincia in (u'Las Palmas', u'Santa Cruz de Tenerife'):
        a = copy.deepcopy(listaPuntos)
        for poligono in a:
            poligono[1] = poligono[1] - 12.0
            poligono[3] = poligono[3] - 12.0
            poligono[5] = poligono[5] - 12.0
            poligono[7] = poligono[7] - 12.0
            if poligono[1] < 0.0:
                poligono[1] = 0.0
            if poligono[3] < 0.0:
                poligono[3] = 0.0
            if poligono[5] < 0.0:
                poligono[5] = 0.0
            if poligono[7] < 0.0:
                poligono[7] = 0.0

    listaPuntosParaCalculos = []
    for i in listaPuntos:
        comp = compruebaPuntos(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
        a = comp.devuelvePuntos()
        if type(a) == str:
            pass
        else:
            for j in range(len(a)):
                fila = []
                fila.append(round(float(a[j][0][0]), 2))
                fila.append(round(float(a[j][0][1]), 2))
                fila.append(round(float(a[j][1][0]), 2))
                fila.append(round(float(a[j][1][1]), 2))
                fila.append(round(float(a[j][2][0]), 2))
                fila.append(round(float(a[j][2][1]), 2))
                fila.append(round(float(a[j][3][0]), 2))
                fila.append(round(float(a[j][3][1]), 2))
                listaPuntosParaCalculos.append(fila)

    mascara = Image.new('1', im.size, 0)
    for i in range(len(listaPuntosParaCalculos)):
        x1 = (int(listaPuntosParaCalculos[i][0] * 720 / 240) + 360, int(listaPuntosParaCalculos[i][1] * 321 / 80))
        x2 = (int(listaPuntosParaCalculos[i][2] * 720 / 240) + 360, int(listaPuntosParaCalculos[i][3] * 321 / 80))
        x3 = (int(listaPuntosParaCalculos[i][4] * 720 / 240) + 360, int(listaPuntosParaCalculos[i][5] * 321 / 80))
        x4 = (int(listaPuntosParaCalculos[i][6] * 720 / 240) + 360, int(listaPuntosParaCalculos[i][7] * 321 / 80))
        pun = []
        pun.append(x1)
        pun.append(x2)
        pun.append(x3)
        pun.append(x4)
        p = Polygon.Polygon(pun)
        for x in range(720):
            for y in range(321):
                if p.isInside(x, y):
                    mascara.putpixel((x, 320 - y), 1)

    hist = im.histogram()
    histSombra = im.histogram(mascara)
    porcentajes = []
    for i in range(1, 11):
        porcentajes.append(histSombra[i] * 100 / hist[i])

    for i in range(20, 32):
        porcentajes.append(histSombra[i] * 100 / hist[i])

    for i in range(40, 52):
        porcentajes.append(histSombra[i] * 100 / hist[i])

    for i in range(60, 74):
        porcentajes.append(histSombra[i] * 100 / hist[i])

    return porcentajes