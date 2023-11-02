# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\apendiceE.pyc
# Compiled at: 2015-02-04 13:05:01
"""
Modulo: apendiceE.py

"""

def murosEnContactoConElTerreno(Rm, z):
    """
    Metodo: murosEnContactoConElTerreno

    ARGUMENTOS:
                Rm:
                z):
    """
    tablaE5 = [
     [
      3.05, 2.2, 1.48, 1.15, 0.95, 0.71],
     [
      1.17, 0.99, 0.77, 0.64, 0.55, 0.44],
     [
      0.74, 0.65, 0.54, 0.47, 0.42, 0.34],
     [
      0.54, 0.49, 0.42, 0.37, 0.34, 0.28],
     [
      0.42, 0.39, 0.35, 0.31, 0.28, 0.24]]
    valores_Rm = [
     0.0, 0.5, 1.0, 1.5, 2.0]
    valores_z = [0.5, 1.0, 2.0, 3.0, 4.0, 6.0]
    fila_Rm = []
    if Rm < 0:
        Rm = 0.0
        fila_Rm = tablaE5[0]
    else:
        if Rm >= 2:
            Rm = 2.0
            fila_Rm = tablaE5[-1]
        else:
            for v, t in zip(valores_Rm, tablaE5):
                if v <= Rm:
                    fila_anterior = t
                    valor_Rm_anterior = v
                else:
                    fila_actual = t
                    valor_Rm_actual = v
                    break

            factor = (float(Rm) - valor_Rm_anterior) / (valor_Rm_actual - valor_Rm_anterior)
            fila_Rm = [ fila_anterior[i] + (fila_actual[i] - fila_anterior[i]) * factor for i in range(len(fila_actual)) ]
        if z < 0.5:
            Um = fila_Rm[0]
        else:
            if z >= 6:
                Um = fila_Rm[-1]
            else:
                for v, t in zip(valores_z, fila_Rm):
                    if v <= z:
                        fila_anterior = t
                        valor_z_anterior = v
                    else:
                        fila_actual = t
                        valor_z_actual = v
                        break

            factor = (float(z) - valor_z_anterior) / (valor_z_actual - valor_z_anterior)
            Um = fila_anterior + (fila_actual - fila_anterior) * factor
    return Um


def particionesInterioresCaso1(Api, Ae, casoAislamiento, gradoVentilacion):
    """
    Metodo: particionesInterioresCaso1

    ARGUMENTOS:
                Api:
                Ae:
                casoAislamiento:
                gradoVentilacion:
    """
    tablaB = [
     [
      [
       0.99, 1.0], [0.94, 0.97], [0.91, 0.96]],
     [
      [
       0.97, 0.99], [0.85, 0.92], [0.77, 0.9]],
     [
      [
       0.96, 0.98], [0.77, 0.87], [0.67, 0.84]],
     [
      [
       0.94, 0.97], [0.7, 0.83], [0.59, 0.79]],
     [
      [
       0.92, 0.96], [0.65, 0.79], [0.53, 0.74]],
     [
      [
       0.89, 0.95], [0.56, 0.73], [0.44, 0.67]],
     [
      [
       0.86, 0.93], [0.48, 0.66], [0.36, 0.59]],
     [
      [
       0.83, 0.91], [0.43, 0.61], [0.32, 0.54]],
     [
      [
       0.81, 0.9], [0.39, 0.57], [0.28, 0.5]]]
    try:
        cociente = float(Api) / float(Ae)
    except ZeroDivisionError:
        cociente = 100.0

    if cociente < 0.25:
        contador = 0
    elif cociente <= 0.5:
        contador = 1
    elif cociente <= 0.75:
        contador = 2
    elif cociente <= 1.0:
        contador = 3
    elif cociente <= 1.25:
        contador = 4
    elif cociente <= 2.0:
        contador = 5
    elif cociente <= 2.5:
        contador = 6
    elif cociente <= 3.0:
        contador = 7
    else:
        contador = 8
    if casoAislamiento == 'AisladoParticion':
        aislamiento = 0
    elif casoAislamiento == 'AisladoCerramiento':
        aislamiento = 2
    elif casoAislamiento == 'Ambos':
        aislamiento = 0
    elif casoAislamiento == 'Ninguno':
        aislamiento = 1
    b = float(tablaB[contador][aislamiento][gradoVentilacion])
    return b


def particionesInterioresCaso2(Aint, Uint, Aext, nivel_estanqueidad, volumen_no_habitable):
    """
    Metodo: particionesInterioresCaso2

    ARGUMENTOS:
                Aint:
                Uint:
                AextVertical:
                nivel_estanqueidad:
                volumen_no_habitable:
    """
    AextVertical = Aext - Aint
    if AextVertical < 0.0:
        Aext = Aint
        AextVertical = Aext - Aint
    UextRs = (0.32 * Aint + 1.3 * AextVertical) / Aext
    if nivel_estanqueidad == 0:
        infilt = 1.0
    else:
        infilt = 10.0
    Hint = Uint * Aint + 0.34 * volumen_no_habitable * 0.5
    Hext = UextRs * Aext + 0.34 * volumen_no_habitable * infilt
    b = Hext / (Hint + Hext)
    return b


def camaraSanitaria(B, Rf):
    """
    Metodo: camaraSanitaria

    ARGUMENTOS:
                B:
                Rf):
    """
    tablaE9 = [
     [
      2.63, 1.14, 0.72, 0.53, 0.42, 0.35],
     [
      2.3, 1.07, 0.7, 0.52, 0.41, 0.34],
     [
      2.06, 1.01, 0.67, 0.5, 0.4, 0.33],
     [
      1.87, 0.97, 0.65, 0.49, 0.39, 0.33],
     [
      1.73, 0.93, 0.63, 0.48, 0.39, 0.32],
     [
      1.61, 0.89, 0.62, 0.47, 0.38, 0.32],
     [
      1.43, 0.83, 0.59, 0.45, 0.37, 0.31],
     [
      1.3, 0.79, 0.57, 0.44, 0.36, 0.31],
     [
      1.2, 0.75, 0.55, 0.43, 0.35, 0.3],
     [
      1.12, 0.72, 0.53, 0.42, 0.35, 0.29],
     [
      1.06, 0.69, 0.51, 0.41, 0.34, 0.29],
     [
      1.0, 0.67, 0.5, 0.4, 0.33, 0.29],
     [
      0.96, 0.65, 0.49, 0.39, 0.33, 0.28],
     [
      0.92, 0.63, 0.48, 0.39, 0.32, 0.28],
     [
      0.89, 0.61, 0.47, 0.38, 0.32, 0.28],
     [
      0.86, 0.6, 0.46, 0.38, 0.32, 0.27],
     [
      0.83, 0.59, 0.45, 0.37, 0.31, 0.27],
     [
      0.81, 0.58, 0.45, 0.37, 0.31, 0.27],
     [
      0.79, 0.57, 0.44, 0.36, 0.31, 0.27]]
    valores_Rf = [
     0.0, 0.5, 1.0, 1.5, 2.0, 2.5]
    valores_B = [5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 
     34, 36]
    fila_B = []
    if B < 5.0:
        B = 5.0
        fila_B = tablaE9[0]
    else:
        if B >= 36.0:
            B = 36.0
            fila_B = tablaE9[-1]
        else:
            for v, t in zip(valores_B, tablaE9):
                if v <= B:
                    fila_anterior = t
                    valor_B_anterior = v
                else:
                    fila_actual = t
                    valor_B_actual = v
                    break

            factor = (float(B) - valor_B_anterior) / (valor_B_actual - valor_B_anterior)
            fila_B = [ fila_anterior[i] + (fila_actual[i] - fila_anterior[i]) * factor for i in range(len(fila_actual)) ]
        if Rf < 0.0:
            Us = fila_B[0]
        else:
            if Rf >= 2.5:
                Us = fila_B[-1]
            else:
                for v, t in zip(valores_Rf, fila_B):
                    if v <= Rf:
                        fila_anterior = t
                        valor_Rf_anterior = v
                    else:
                        fila_actual = t
                        valor_Rf_actual = v
                        break

            factor = (float(Rf) - valor_Rf_anterior) / (valor_Rf_actual - valor_Rf_anterior)
            Us = fila_anterior + (fila_actual - fila_anterior) * factor
    return Us


def sueloTerrenoCaso1(D, Ra, B):
    """
    Metodo: sueloTerrenoCaso1

    ARGUMENTOS:
                D:
                Ra:
                B:
    """
    valores_B = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20]
    tablaE3 = [
     [
      [
       2.35], [1.57, 1.3, 1.16, 1.07, 1.01],
      [
       1.39, 1.01, 0.8, 0.66, 0.57],
      [
       1.39, 1.01, 0.8, 0.66, 0.57]],
     [
      [
       1.56], [1.17, 1.04, 0.97, 0.92, 0.89],
      [
       1.08, 0.89, 0.79, 0.72, 0.67],
      [
       1.04, 0.83, 0.7, 0.61, 0.55]],
     [
      [
       1.2], [0.94, 0.85, 0.8, 0.78, 0.76],
      [
       0.88, 0.76, 0.69, 0.64, 0.61],
      [
       0.85, 0.71, 0.63, 0.57, 0.53]],
     [
      [
       0.99], [0.79, 0.73, 0.69, 0.67, 0.65],
      [
       0.75, 0.65, 0.6, 0.57, 0.54],
      [
       0.73, 0.62, 0.56, 0.51, 0.48]],
     [
      [
       0.85], [0.69, 0.64, 0.61, 0.59, 0.58],
      [
       0.65, 0.58, 0.54, 0.51, 0.49],
      [
       0.64, 0.55, 0.5, 0.47, 0.44]],
     [
      [
       0.74], [0.61, 0.57, 0.54, 0.53, 0.52],
      [
       0.58, 0.52, 0.48, 0.46, 0.44],
      [
       0.57, 0.5, 0.45, 0.43, 0.41]],
     [
      [
       0.66], [0.55, 0.51, 0.49, 0.48, 0.47],
      [
       0.53, 0.47, 0.44, 0.42, 0.41],
      [
       0.51, 0.45, 0.42, 0.39, 0.37]],
     [
      [
       0.6], [0.5, 0.47, 0.45, 0.44, 0.43],
      [
       0.48, 0.43, 0.41, 0.39, 0.38],
      [
       0.47, 0.42, 0.38, 0.36, 0.35]],
     [
      [
       0.55], [0.46, 0.43, 0.42, 0.41, 0.4],
      [
       0.44, 0.4, 0.38, 0.36, 0.35],
      [
       0.43, 0.39, 0.36, 0.34, 0.33]],
     [
      [
       0.51], [0.43, 0.4, 0.39, 0.38, 0.37],
      [
       0.41, 0.37, 0.35, 0.34, 0.33],
      [
       0.4, 0.36, 0.34, 0.32, 0.31]],
     [
      [
       0.44], [0.38, 0.36, 0.34, 0.34, 0.33],
      [
       0.36, 0.33, 0.31, 0.3, 0.29],
      [
       0.36, 0.32, 0.3, 0.28, 0.27]],
     [
      [
       0.39], [0.34, 0.32, 0.31, 0.3, 0.3],
      [
       0.32, 0.3, 0.28, 0.27, 0.27],
      [
       0.32, 0.29, 0.27, 0.26, 0.25]],
     [
      [
       0.35], [0.31, 0.29, 0.28, 0.27, 0.27],
      [
       0.29, 0.27, 0.26, 0.25, 0.24],
      [
       0.29, 0.26, 0.25, 0.24, 0.23]],
     [
      [
       0.32], [0.28, 0.27, 0.26, 0.25, 0.25],
      [
       0.27, 0.25, 0.24, 0.23, 0.22],
      [
       0.27, 0.24, 0.23, 0.22, 0.21]],
     [
      [
       0.3], [0.26, 0.25, 0.24, 0.23, 0.23],
      [
       0.25, 0.23, 0.22, 0.21, 0.21],
      [
       0.25, 0.22, 0.21, 0.2, 0.2]]]
    fila_B = []
    aux = []
    if B <= 1.0:
        fila_B = tablaE3[0]
    else:
        if B >= 20.0:
            fila_B = tablaE3[-1]
        else:
            for v, t in zip(valores_B, tablaE3):
                if v <= B:
                    fila_anterior = t
                    valor_B_anterior = v
                else:
                    fila_actual = t
                    valor_B_actual = v
                    break

            factor = (float(B) - valor_B_anterior) / (valor_B_actual - valor_B_anterior)
            for a, b in zip(fila_anterior, fila_actual):
                aux = [ a[i] + (b[i] - a[i]) * factor for i in range(len(a)) ]
                fila_B += [aux]

        array_Ra = []
        if Ra <= 0:
            D = 0
        if D <= 0:
            return fila_B[0][0]
    if D <= 0.5:
        factor = float(D) / 0.5
        array_Ra = [ fila_B[0][0] + factor * (x - fila_B[0][0]) for x in fila_B[1] ]
    elif D <= 1.0:
        factor = (float(D) - 0.5) / 0.5
        array_Ra = [ fila_B[1][i] + factor * (fila_B[2][i] - fila_B[1][i]) for i in range(len(fila_B[1])) ]
    elif D <= 1.5:
        factor = (float(D) - 1.0) / 0.5
        array_Ra = [ fila_B[2][i] + factor * (fila_B[3][i] - fila_B[2][i]) for i in range(len(fila_B[1])) ]
    else:
        array_Ra = fila_B[3]
    if Ra <= 0.5:
        factor = Ra / 0.5
        U = fila_B[0][0] + (array_Ra[0] - fila_B[0][0]) * factor
    elif Ra <= 1.0:
        factor = (Ra - 0.5) / 0.5
        U = array_Ra[0] + (array_Ra[1] - array_Ra[0]) * factor
    elif Ra <= 1.5:
        factor = (Ra - 1.0) / 0.5
        U = array_Ra[1] + (array_Ra[2] - array_Ra[1]) * factor
    elif Ra <= 2.0:
        factor = (Ra - 1.5) / 0.5
        U = array_Ra[2] + (array_Ra[3] - array_Ra[2]) * factor
    elif Ra <= 2.5:
        factor = (Ra - 2.0) / 0.5
        U = array_Ra[3] + (array_Ra[4] - array_Ra[3]) * factor
    else:
        U = array_Ra[4]
    return U


def sueloTerrenoCaso2(z, Rf, B):
    """
    Metodo: sueloTerrenoCaso2

    ARGUMENTOS:
                z:
                Rf:
                B:
    """
    valores_B = [
     5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20]
    tablaE4 = [
     [
      [
       0.64, 0.52, 0.44, 0.39],
      [
       0.54, 0.45, 0.4, 0.36],
      [
       0.42, 0.37, 0.34, 0.31],
      [
       0.35, 0.32, 0.29, 0.27]],
     [
      [
       0.57, 0.46, 0.4, 0.35],
      [
       0.48, 0.41, 0.36, 0.33],
      [
       0.38, 0.34, 0.31, 0.28],
      [
       0.32, 0.29, 0.27, 0.25]],
     [
      [
       0.52, 0.42, 0.37, 0.33],
      [
       0.44, 0.38, 0.33, 0.3],
      [
       0.35, 0.31, 0.29, 0.26],
      [
       0.3, 0.27, 0.25, 0.24]],
     [
      [
       0.47, 0.39, 0.34, 0.3],
      [
       0.4, 0.35, 0.31, 0.28],
      [
       0.33, 0.29, 0.27, 0.25],
      [
       0.28, 0.26, 0.24, 0.22]],
     [
      [
       0.43, 0.36, 0.32, 0.28],
      [
       0.37, 0.32, 0.29, 0.26],
      [
       0.3, 0.27, 0.25, 0.23],
      [
       0.26, 0.24, 0.22, 0.21]],
     [
      [
       0.4, 0.34, 0.3, 0.27],
      [
       0.35, 0.3, 0.27, 0.25],
      [
       0.29, 0.26, 0.24, 0.22],
      [
       0.25, 0.23, 0.21, 0.2]],
     [
      [
       0.36, 0.3, 0.27, 0.24],
      [
       0.31, 0.27, 0.24, 0.22],
      [
       0.26, 0.23, 0.21, 0.2],
      [
       0.22, 0.21, 0.19, 0.18]],
     [
      [
       0.32, 0.27, 0.24, 0.22],
      [
       0.28, 0.25, 0.22, 0.2],
      [
       0.23, 0.21, 0.2, 0.18],
      [
       0.2, 0.19, 0.18, 0.17]],
     [
      [
       0.29, 0.25, 0.22, 0.2],
      [
       0.25, 0.23, 0.2, 0.19],
      [
       0.21, 0.2, 0.18, 0.17],
      [
       0.19, 0.17, 0.16, 0.16]],
     [
      [
       0.26, 0.23, 0.2, 0.19],
      [
       0.23, 0.21, 0.19, 0.18],
      [
       0.2, 0.18, 0.17, 0.16],
      [
       0.17, 0.16, 0.15, 0.15]],
     [
      [
       0.24, 0.21, 0.19, 0.17],
      [
       0.22, 0.19, 0.18, 0.16],
      [
       0.18, 0.17, 0.16, 0.15],
      [
       0.16, 0.15, 0.14, 0.14]]]
    fila_B = []
    aux = []
    if B <= 5.0:
        fila_B = tablaE4[0]
    else:
        if B >= 20.0:
            fila_B = tablaE4[-1]
        else:
            for v, t in zip(valores_B, tablaE4):
                if v <= B:
                    fila_anterior = t
                    valor_B_anterior = v
                else:
                    fila_actual = t
                    valor_B_actual = v
                    break

            factor = (float(B) - valor_B_anterior) / (valor_B_actual - valor_B_anterior)
            for a, b in zip(fila_anterior, fila_actual):
                aux = [ a[i] + (b[i] - a[i]) * factor for i in range(len(a)) ]
                fila_B += [aux]

        array_Rf = []
        if z < 0.5:
            return -1
    if z <= 1.0:
        array_Rf = fila_B[0]
    elif z <= 2.0:
        array_Rf = fila_B[1]
    elif z <= 3.0:
        array_Rf = fila_B[2]
    else:
        array_Rf = fila_B[3]
    if Rf <= 0.0:
        U = array_Rf[0]
    elif Rf <= 0.5:
        factor = (Rf - 0.0) / 0.5
        U = array_Rf[0] + (array_Rf[1] - array_Rf[0]) * factor
    elif Rf <= 1.0:
        factor = (Rf - 0.5) / 0.5
        U = array_Rf[1] + (array_Rf[2] - array_Rf[1]) * factor
    elif Rf <= 1.5:
        factor = (Rf - 1.0) / 0.5
        U = array_Rf[2] + (array_Rf[3] - array_Rf[2]) * factor
    else:
        U = array_Rf[3]
    return U


def cerramientosExteriores(U, tipo):
    """
    Metodo: cerramientosExteriores

    ARGUMENTOS:
                U:
                tipo:
    """
    if tipo == 'Vertical':
        Rsuperficial = 0.17
    elif tipo == 'HorizontalFlujoAscendente':
        Rsuperficial = 0.14
    elif tipo == 'HorizontalFlujoDescendente':
        Rsuperficial = 0.21000000000000002
    Rtotal = 1.0 / float(U) + Rsuperficial
    U = 1.0 / Rtotal
    return U


def fachadaVentilada(U):
    """
    Metodo: fachadaVentilada

    ARGUMENTOS:
                U:
    """
    Rsuperficial = 0.26
    Rtotal = 1.0 / float(U) + Rsuperficial
    U = 1.0 / Rtotal
    return U


def cubiertaTerreno(U, profundidad):
    """
    Metodo: cubiertaTerreno

    ARGUMENTOS:
                U:
                profundidad:
    """
    Rtotal = 1 / float(U) + 0.14 + float(profundidad) / 2.0
    U = 1 / Rtotal
    return U


def particionesInterioresResistencias(U, tipo):
    """
    Metodo: particionesInterioresResistencias

    ARGUMENTOS:
                U:
                tipo:
    """
    if tipo == 'Vertical':
        Rsuperficial = 0.26
    elif tipo == 'HorizontalSuperior':
        Rsuperficial = 0.2
    elif tipo == 'HorizontalInferior':
        Rsuperficial = 0.34
    Rtotal = 1.0 / float(U) + Rsuperficial
    U = 1 / Rtotal
    return U