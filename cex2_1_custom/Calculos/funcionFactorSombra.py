# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Calculos\funcionFactorSombra.pyc
# Compiled at: 2014-02-18 15:21:03
"""
Modulo: funcion_factor_Sombra.py

"""
import unittest

def Factor_Sombra_Voladizos(L, H, D, Orientacion):
    """
    Metodo: Factor_Sombra_Voladizos

    ARGUMENTOS:
                L:
                H:
                D:
                Orientacion:
    """
    L = float(L)
    H = float(H)
    D = float(D)
    if L < 0 or D < 0 or H <= 0:
        FS = 1
        return FS
    else:
        D_H = float(D) / float(H)
        L_H = float(L) / float(H)
        if Orientacion != 'Norte' and Orientacion != 'NO' and Orientacion != 'NE' and L_H >= 0.2 and D_H >= 0:
            if Orientacion == 'Sur':
                contador_O = 0
            elif Orientacion == 'SE' or Orientacion == 'SO':
                contador_O = 1
            elif Orientacion == 'Este' or Orientacion == 'Oeste':
                contador_O = 2
            if D_H >= 0 and D_H <= 0.2:
                contador_limite1 = 0
            elif D_H > 0.2 and D_H <= 0.5:
                contador_limite1 = 1
            elif D_H > 0.5:
                contador_limite1 = 2
            if L_H >= 0.2 and L_H <= 0.5:
                contador_limite2 = 0
            elif L_H > 0.5 and L_H <= 1:
                contador_limite2 = 1
            elif L_H > 1 and L_H <= 2:
                contador_limite2 = 2
            elif L_H > 2:
                contador_limite2 = 3
            factor_sombra = [[[0.82, 0.5, 0.28, 0.16], [0.87, 0.64, 0.39, 0.22], [0.93, 0.82, 0.6, 0.39]],
             [
              [
               0.9, 0.71, 0.43, 0.16], [0.94, 0.82, 0.6, 0.27], [0.98, 0.93, 0.84, 0.65]],
             [
              [
               0.92, 0.77, 0.55, 0.22], [0.96, 0.86, 0.7, 0.43], [0.99, 0.96, 0.89, 0.75]]]
            FS = factor_sombra[contador_O][contador_limite1][contador_limite2]
            return FS
        FS = 1
        return FS


def Factor_Sombra_Retranqueo(R, H, W, Orientacion):
    """
    Metodo: Factor_Sombra_Retranqueo

    ARGUMENTOS:
                R:
                H:
                W:
                Orientacion:
    """
    R = float(R)
    H = float(H)
    W = float(W)
    if R < 0 or W <= 0 or H <= 0:
        FS = 1
        return FS
    else:
        if Orientacion != 'Norte' and Orientacion != 'NO' and Orientacion != 'NE' and R / H > 0.05 and R / W > 0.05:
            if Orientacion == 'Sur':
                contador_O = 0
            elif Orientacion == 'SE' or Orientacion == 'SO':
                contador_O = 1
            elif Orientacion == 'Este' or Orientacion == 'Oeste':
                contador_O = 2
            if R / H > 0.05 and R / H <= 0.1:
                contador_limite1 = 0
            elif R / H > 0.1 and R / H <= 0.2:
                contador_limite1 = 1
            elif R / H > 0.2 and R / H <= 0.5:
                contador_limite1 = 2
            elif R / H > 0.5:
                contador_limite1 = 3
            if R / W > 0.05 and R / W <= 0.1:
                contador_limite2 = 0
            elif R / W > 0.1 and R / W <= 0.2:
                contador_limite2 = 1
            elif R / W > 0.2 and R / W <= 0.5:
                contador_limite2 = 2
            elif R / W > 0.5:
                contador_limite2 = 3
            factor_sombra = [
             [[0.82, 0.74, 0.62, 0.39], [0.76, 0.67, 0.56, 0.35],
              [
               0.56, 0.51, 0.39, 0.27], [0.35, 0.32, 0.27, 0.17]],
             [
              [
               0.86, 0.81, 0.72, 0.51], [0.79, 0.74, 0.66, 0.47],
              [
               0.59, 0.56, 0.47, 0.36], [0.38, 0.36, 0.32, 0.23]],
             [
              [
               0.91, 0.87, 0.81, 0.65], [0.86, 0.82, 0.76, 0.61],
              [
               0.71, 0.68, 0.61, 0.51], [0.53, 0.51, 0.48, 0.39]]]
            FS = factor_sombra[contador_O][contador_limite1][contador_limite2]
            return FS
        FS = 1
        return FS


def Factor_Sombra_Lamas_Horizontales(Beta, Orientacion):
    """
    Metodo: Factor_Sombra_Lamas_Horizontales

    ARGUMENTOS:
                Beta:
                Orientacion:
    """
    Beta = float(Beta)
    if Beta < 0 or Beta > 90:
        FS = 1
        return FS
    else:
        if Orientacion != 'Norte' and Orientacion != 'NO' and Orientacion != 'NE':
            if Orientacion == 'Sur':
                contador_O = 0
            elif Orientacion == 'SE' or Orientacion == 'SO':
                contador_O = 1
            elif Orientacion == 'Este' or Orientacion == 'Oeste':
                contador_O = 2
            if Beta > 60:
                Beta = 60
            factor_sombra = [[0.49, 0.42, 0.26], [0.54, 0.44, 0.26], [0.57, 0.45, 0.27]]
            if Beta >= 0 and Beta <= 30:
                contador_Beta = 0
                limite_Beta1 = 0
                limite_Beta2 = 30
            elif Beta > 30 and Beta <= 60:
                contador_Beta = 1
                limite_Beta1 = 30
                limite_Beta2 = 60
            FS_limite1 = factor_sombra[contador_O][contador_Beta]
            FS_limite2 = factor_sombra[contador_O][contador_Beta + 1]
            FS = (FS_limite1 - FS_limite2) / (limite_Beta1 - limite_Beta2) * (Beta - limite_Beta2) + FS_limite2
            return FS
        FS = 1
        return FS


def Factor_Sombra_Lamas_Verticales(Beta, Orientacion):
    """
    Metodo: Factor_Sombra_Lamas_Verticales

    ARGUMENTOS:
                Beta:
                Orientacion:
    """
    Beta = float(Beta)
    if Beta < -90 or Beta > 90:
        FS = 1
        return FS
    else:
        if Beta < -60:
            Beta = -60
        if Beta > 60:
            Beta = 60
        if Orientacion != 'Norte' and Orientacion != 'NO' and Orientacion != 'NE':
            if Orientacion == 'Sur':
                contador_O = 0
            elif Orientacion == 'SE':
                contador_O = 1
            elif Orientacion == 'Este':
                contador_O = 2
            elif Orientacion == 'Oeste':
                contador_O = 3
            elif Orientacion == 'SO':
                contador_O = 4
            factor_sombra = [
             [
              0.37, 0.44, 0.49, 0.53, 0.47, 0.41, 
              0.32],
             [
              0.46, 0.53, 0.56, 0.56, 0.47, 0.4, 
              0.3],
             [
              0.39, 0.47, 0.54, 0.63, 0.55, 0.45, 
              0.32],
             [
              0.44, 0.52, 0.58, 0.63, 0.5, 0.41, 
              0.29],
             [
              0.38, 0.44, 0.5, 0.56, 0.53, 0.48, 
              0.38]]
            if Beta >= -60 and Beta <= -45:
                contador_Beta = 0
                limite_Beta1 = -60
                limite_Beta2 = -45
            elif Beta > -45 and Beta <= -30:
                contador_Beta = 1
                limite_Beta1 = -45
                limite_Beta2 = -30
            elif Beta > -30 and Beta <= 0:
                contador_Beta = 2
                limite_Beta1 = -30
                limite_Beta2 = 0
            elif Beta > 0 and Beta <= 30:
                contador_Beta = 3
                limite_Beta1 = 0
                limite_Beta2 = 30
            elif Beta > 30 and Beta <= 45:
                contador_Beta = 4
                limite_Beta1 = 30
                limite_Beta2 = 45
            elif Beta > 45 and Beta <= 60:
                contador_Beta = 5
                limite_Beta1 = 45
                limite_Beta2 = 60
            FS_limite1 = factor_sombra[contador_O][contador_Beta]
            FS_limite2 = factor_sombra[contador_O][contador_Beta + 1]
            FS = (FS_limite1 - FS_limite2) / (limite_Beta1 - limite_Beta2) * (Beta - limite_Beta2) + FS_limite2
            return FS
        FS = 1
        return FS


def Factor_Sombra_Toldos_A(tipo_tejido, Orientacion, angulo):
    """
    Metodo: Factor_Sombra_Toldos_A

    ARGUMENTOS:
                tipo_tejido:
                Orientacion:
                angulo:
    """
    angulo = float(angulo)
    if angulo < 30:
        angulo = 30
    if angulo > 60:
        angulo = 60
    if tipo_tejido == 'Opaco':
        contador_tejido = 0
    else:
        contador_tejido = 1
    if Orientacion == 'Sur' or Orientacion == 'SE' or Orientacion == 'SO':
        contador_Orientacion = 0
    else:
        if Orientacion == 'Este' or Orientacion == 'Oeste':
            contador_Orientacion = 1
        else:
            FS = 1
            return FS
        angulos = [30, 45, 60]
        for contador in range(len(angulos)):
            if angulo <= angulos[contador] and angulo >= angulos[contador - 1]:
                limite_1 = angulos[contador - 1]
                limite_2 = angulos[contador]
                contador_1 = contador - 1
                contador_2 = contador
                break

    matriz = [[[0.02, 0.05, 0.22], [0.04, 0.08, 0.28]],
     [
      [
       0.22, 0.25, 0.42], [0.24, 0.28, 0.48]]]
    valor_1 = matriz[contador_tejido][contador_Orientacion][contador_1]
    valor_2 = matriz[contador_tejido][contador_Orientacion][contador_2]
    FS = (valor_2 - valor_1) * (angulo - limite_1) / (limite_2 - limite_1) + valor_1
    return FS


def Factor_Sombra_Toldos_B(tipo_tejido, Orientacion, angulo):
    """
    Metodo: Factor_Sombra_Toldos_B

    ARGUMENTOS:
                tipo_tejido:
                Orientacion:
                angulo:
    """
    angulo = float(angulo)
    if angulo < 30:
        angulo = 30
    if angulo > 60:
        angulo = 60
    if tipo_tejido == 'Opaco':
        contador_tejido = 0
    else:
        contador_tejido = 1
    if Orientacion == 'Sur':
        contador_Orientacion = 0
    else:
        if Orientacion == 'SE' or Orientacion == 'SO':
            contador_Orientacion = 1
        elif Orientacion == 'Este' or Orientacion == 'Oeste':
            contador_Orientacion = 2
        else:
            FS = 1
            return FS
        angulos = [30, 45, 60]
        for contador in range(len(angulos)):
            if angulo <= angulos[contador] and angulo >= angulos[contador - 1]:
                limite_1 = angulos[contador - 1]
                limite_2 = angulos[contador]
                contador_1 = contador - 1
                contador_2 = contador
                break

    matriz = [
     [
      [
       0.43, 0.2, 0.14], [0.61, 0.3, 0.39], [0.67, 0.4, 0.28]],
     [
      [
       0.63, 0.4, 0.34], [0.81, 0.5, 0.42], [0.87, 0.6, 0.48]]]
    valor_1 = matriz[contador_tejido][contador_Orientacion][contador_1]
    valor_2 = matriz[contador_tejido][contador_Orientacion][contador_2]
    FS = (valor_2 - valor_1) * (angulo - limite_1) / (limite_2 - limite_1) + valor_1
    return FS


def Factor_Sombra_Lucernarios(x, y, z):
    """
    Metodo: Factor_Sombra_Lucernarios

    ARGUMENTOS:
                x:
                y:
                z:
    """
    x = float(x)
    y = float(y)
    z = float(z)
    coeficientes = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
    coeficiente_fila = float(x) / float(z)
    coeficiente_columna = float(y) / float(z)
    if coeficiente_fila < 0.1:
        coeficiente_fila = 0.1
    if coeficiente_fila > 10:
        coeficiente_fila = 10
    if coeficiente_columna < 0.1:
        coeficiente_columna = 0.1
    if coeficiente_columna > 10:
        coeficiente_columna = 10
    for contador in range(len(coeficientes)):
        if coeficiente_fila <= coeficientes[contador] and coeficiente_fila >= coeficientes[contador - 1]:
            limite_1_fila = coeficientes[contador - 1]
            limite_2_fila = coeficientes[contador]
            contador_1_fila = contador - 1
            contador_2_fila = contador
            break

    for contador in range(len(coeficientes)):
        if coeficiente_columna <= coeficientes[contador] and coeficiente_columna >= coeficientes[contador - 1]:
            limite_1_columna = coeficientes[contador - 1]
            limite_2_columna = coeficientes[contador]
            contador_1_columna = contador - 1
            contador_2_columna = contador
            break

    matriz_factores = [
     [
      0.42, 0.43, 0.43, 0.43, 0.44, 0.44],
     [
      0.43, 0.46, 0.48, 0.5, 0.51, 0.52],
     [
      0.43, 0.48, 0.52, 0.55, 0.58, 0.59],
     [
      0.43, 0.5, 0.55, 0.6, 0.66, 0.68],
     [
      0.44, 0.51, 0.58, 0.66, 0.75, 0.79],
     [
      0.44, 0.52, 0.59, 0.68, 0.79, 0.85]]
    valor_1_1 = matriz_factores[contador_1_fila][contador_1_columna]
    valor_2_1 = matriz_factores[contador_2_fila][contador_1_columna]
    valor_1_2 = matriz_factores[contador_1_fila][contador_2_columna]
    valor_2_2 = matriz_factores[contador_2_fila][contador_2_columna]
    valor_1 = (valor_2_1 - valor_1_1) * (coeficiente_fila - limite_1_fila) / (limite_2_fila - limite_1_fila) + valor_1_1
    valor_2 = (valor_2_2 - valor_1_2) * (coeficiente_fila - limite_1_fila) / (limite_2_fila - limite_1_fila) + valor_1_2
    FS = (valor_2 - valor_1) * (coeficiente_columna - limite_1_columna) / (limite_2_columna - limite_1_columna) + valor_1
    return FS


def Factor_Sombra_Voladizos_Calculos(L, H, D, Orientacion):
    """
    Metodo: Factor_Sombra_Voladizos_Calculos

    ARGUMENTOS:
                L:
                H:
                D:
                Orientacion:
    """
    L = float(L)
    H = float(H)
    D = float(D)
    if L < 0 or D < 0 or H <= 0:
        FS = 1
        return FS
    else:
        D_H = float(D) / float(H)
        L_H = float(L) / float(H)
        if Orientacion != 'Norte' and Orientacion != 'NO' and Orientacion != 'NE' and L_H >= 0.2 and D_H >= 0:
            if Orientacion == 'Sur':
                contador_O = 0
            elif Orientacion == 'SE' or Orientacion == 'SO':
                contador_O = 1
            elif Orientacion == 'Este' or Orientacion == 'Oeste':
                contador_O = 2
            if D_H >= 0 and D_H <= 0.2:
                contador_limite1 = 0
            elif D_H > 0.2 and D_H <= 0.5:
                contador_limite1 = 1
            elif D_H > 0.5:
                contador_limite1 = 2
            if L_H >= 0.2 and L_H <= 0.5:
                contador_limite2 = 0
            elif L_H > 0.5 and L_H <= 1:
                contador_limite2 = 1
            elif L_H > 1 and L_H <= 2:
                contador_limite2 = 2
            elif L_H > 2:
                contador_limite2 = 3
            factor_sombra_invierno = [
             [
              [
               0.92, 0.79, 0.64, 0.58], [0.99, 0.95, 0.79, 0.68], [1.0, 0.98, 0.88, 0.74]],
             [
              [
               0.91, 0.81, 0.69, 0.59], [0.99, 0.94, 0.84, 0.74], [0.99, 0.98, 0.92, 0.82]],
             [
              [
               0.91, 0.85, 0.81, 0.8], [0.98, 0.94, 0.91, 0.89], [0.99, 0.97, 0.94, 0.93]]]
            factor_sombra_verano = [
             [
              [
               0.65, 0.56, 0.54, 0.53], [0.79, 0.64, 0.62, 0.61], [0.88, 0.7, 0.68, 0.67]],
             [
              [
               0.77, 0.6, 0.56, 0.55], [0.89, 0.71, 0.64, 0.63], [0.94, 0.78, 0.68, 0.67]],
             [
              [
               0.86, 0.7, 0.55, 0.47], [0.95, 0.83, 0.67, 0.56], [0.98, 0.9, 0.75, 0.61]]]
            FS_invierno = factor_sombra_invierno[contador_O][contador_limite1][contador_limite2]
            FS_verano = factor_sombra_verano[contador_O][contador_limite1][contador_limite2]
            FS = [
             FS_invierno, FS_verano]
            return FS
        FS = [
         1, 1]
        return FS


def Factor_Sombra_Retranqueo_Calculos(R, H, W, Orientacion):
    """
    Metodo: Factor_Sombra_Retranqueo_Calculos

    ARGUMENTOS:
                R:
                H:
                W:
                Orientacion:
    """
    R = float(R)
    H = float(H)
    W = float(W)
    if R < 0 or W <= 0 or H <= 0:
        FS = 1
        return FS
    else:
        if Orientacion != 'Norte' and Orientacion != 'NO' and Orientacion != 'NE' and R / H > 0.05 and R / W > 0.05:
            if Orientacion == 'Sur':
                contador_O = 0
            elif Orientacion == 'SE' or Orientacion == 'SO':
                contador_O = 1
            elif Orientacion == 'Este' or Orientacion == 'Oeste':
                contador_O = 2
            if R / H > 0.05 and R / H <= 0.1:
                contador_limite1 = 0
            elif R / H > 0.1 and R / H <= 0.2:
                contador_limite1 = 1
            elif R / H > 0.2 and R / H <= 0.5:
                contador_limite1 = 2
            elif R / H > 0.5:
                contador_limite1 = 3
            if R / W > 0.05 and R / W <= 0.1:
                contador_limite2 = 0
            elif R / W > 0.1 and R / W <= 0.2:
                contador_limite2 = 1
            elif R / W > 0.2 and R / W <= 0.5:
                contador_limite2 = 2
            elif R / W > 0.5:
                contador_limite2 = 3
            factor_sombra_invierno = [
             [[0.92, 0.87, 0.76, 0.62], [0.88, 0.84, 0.73, 0.59],
              [
               0.78, 0.74, 0.65, 0.53], [0.66, 0.63, 0.54, 0.44]],
             [
              [
               0.9, 0.85, 0.74, 0.62], [0.86, 0.82, 0.71, 0.6],
              [
               0.75, 0.72, 0.63, 0.55], [0.62, 0.6, 0.54, 0.48]],
             [
              [
               0.87, 0.8, 0.63, 0.47], [0.83, 0.77, 0.61, 0.46],
              [
               0.72, 0.68, 0.56, 0.43], [0.61, 0.58, 0.49, 0.39]]]
            factor_sombra_verano = [
             [
              [
               0.81, 0.75, 0.62, 0.51], [0.7, 0.66, 0.56, 0.47],
              [
               0.44, 0.43, 0.39, 0.36], [0.35, 0.35, 0.33, 0.31]],
             [
              [
               0.87, 0.83, 0.71, 0.59], [0.8, 0.76, 0.66, 0.54],
              [
               0.62, 0.59, 0.52, 0.43], [0.46, 0.44, 0.38, 0.32]],
             [
              [
               0.91, 0.89, 0.82, 0.75], [0.86, 0.84, 0.78, 0.71],
              [
               0.73, 0.71, 0.67, 0.62], [0.6, 0.58, 0.56, 0.52]]]
            FS_invierno = factor_sombra_invierno[contador_O][contador_limite1][contador_limite2]
            FS_verano = factor_sombra_verano[contador_O][contador_limite1][contador_limite2]
            FS = [
             FS_invierno, FS_verano]
            return FS
        FS = [
         1, 1]
        return FS


def Factor_Sombra_Lamas_Horizontales_Calculos(Beta, Orientacion):
    """
    Metodo: Factor_Sombra_Lamas_Horizontales_Calculos

    ARGUMENTOS:
                Beta:
                Orientacion:
    """
    Beta = float(Beta)
    if Beta < 0 or Beta > 90:
        FS = [
         1, 1]
        return FS
    else:
        if Orientacion != 'Norte' and Orientacion != 'NO' and Orientacion != 'NE':
            if Orientacion == 'Sur':
                contador_O = 0
            elif Orientacion == 'SE' or Orientacion == 'SO':
                contador_O = 1
            elif Orientacion == 'Este' or Orientacion == 'Oeste':
                contador_O = 2
            if Beta > 60:
                Beta = 60
            factor_sombra_invierno = [[0.529, 0.167, 0.08], [0.503, 0.207, 0.102], [0.551, 0.295, 0.178]]
            factor_sombra_verano = [
             [
              0.354, 0.277, 0.234], [0.375, 0.245, 0.195], [0.49, 0.272, 0.189]]
            if Beta >= 0 and Beta <= 30:
                contador_Beta = 0
                limite_Beta1 = 0
                limite_Beta2 = 30
            elif Beta > 30 and Beta <= 60:
                contador_Beta = 1
                limite_Beta1 = 30
                limite_Beta2 = 60
            FS_limite1_invierno = factor_sombra_invierno[contador_O][contador_Beta]
            FS_limite2_invierno = factor_sombra_invierno[contador_O][contador_Beta + 1]
            FS_limite1_verano = factor_sombra_verano[contador_O][contador_Beta]
            FS_limite2_verano = factor_sombra_verano[contador_O][contador_Beta + 1]
            FS_invierno = (FS_limite1_invierno - FS_limite2_invierno) / (limite_Beta1 - limite_Beta2) * (Beta - limite_Beta2) + FS_limite2_invierno
            FS_verano = (FS_limite1_verano - FS_limite2_verano) / (limite_Beta1 - limite_Beta2) * (Beta - limite_Beta2) + FS_limite2_verano
            return [
             FS_invierno, FS_verano]
        FS = [
         1, 1]
        return FS


def Factor_Sombra_Lamas_Verticales_Calculos(Beta, Orientacion):
    """
    Metodo: Factor_Sombra_Lamas_Verticales_Calculos

    ARGUMENTOS:
                Beta:
                Orientacion:
    """
    Beta = float(Beta)
    if Beta < -90 or Beta > 90:
        FS = [1, 1]
        return FS
    else:
        if Beta < -60:
            Beta = -60
        if Beta > 60:
            Beta = 60
        if Orientacion != 'Norte' and Orientacion != 'NO' and Orientacion != 'NE':
            if Orientacion == 'Sur':
                contador_O = 2
            elif Orientacion == 'SE':
                contador_O = 3
            elif Orientacion == 'Este':
                contador_O = 4
            elif Orientacion == 'Oeste':
                contador_O = 0
            elif Orientacion == 'SO':
                contador_O = 1
            factor_sombra_invierno = [[0.526, 0.591, 0.517, 0.365, 0.289, 0.27, 0.23],
             [
              0.373, 0.504, 0.558, 0.541, 0.338, 
              0.255, 0.166],
             [
              0.277, 0.409, 0.463, 0.505, 0.444, 
              0.382, 0.254],
             [
              0.165, 0.262, 0.354, 0.563, 0.554, 
              0.491, 0.354],
             [
              0.211, 0.247, 0.265, 0.353, 0.533, 
              0.606, 0.527]]
            factor_sombra_verano = [
             [
              0.362, 0.505, 0.608, 0.706, 0.509, 
              0.4, 0.284],
             [
              0.301, 0.367, 0.411, 0.522, 0.6, 0.592, 
              0.467],
             [
              0.422, 0.471, 0.482, 0.498, 0.48, 0.467, 
              0.416],
             [
              0.469, 0.599, 0.602, 0.514, 0.399, 
              0.355, 0.29],
             [
              0.275, 0.394, 0.506, 0.711, 0.606, 
              0.499, 0.352]]
            if Beta >= -60 and Beta <= -45:
                contador_Beta = 0
                limite_Beta1 = -60
                limite_Beta2 = -45
            elif Beta > -45 and Beta <= -30:
                contador_Beta = 1
                limite_Beta1 = -45
                limite_Beta2 = -30
            elif Beta > -30 and Beta <= 0:
                contador_Beta = 2
                limite_Beta1 = -30
                limite_Beta2 = 0
            elif Beta > 0 and Beta <= 30:
                contador_Beta = 3
                limite_Beta1 = 0
                limite_Beta2 = 30
            elif Beta > 30 and Beta <= 45:
                contador_Beta = 4
                limite_Beta1 = 30
                limite_Beta2 = 45
            elif Beta > 45 and Beta <= 60:
                contador_Beta = 5
                limite_Beta1 = 45
                limite_Beta2 = 60
            FS_limite1_invierno = factor_sombra_invierno[contador_O][contador_Beta]
            FS_limite2_invierno = factor_sombra_invierno[contador_O][contador_Beta + 1]
            FS_limite1_verano = factor_sombra_verano[contador_O][contador_Beta]
            FS_limite2_verano = factor_sombra_verano[contador_O][contador_Beta + 1]
            FS_invierno = (FS_limite1_invierno - FS_limite2_invierno) / (limite_Beta1 - limite_Beta2) * (Beta - limite_Beta2) + FS_limite2_invierno
            FS_verano = (FS_limite1_verano - FS_limite2_verano) / (limite_Beta1 - limite_Beta2) * (Beta - limite_Beta2) + FS_limite2_verano
            return [
             FS_invierno, FS_verano]
        FS = [
         1, 1]
        return FS


class pruebasUnitarias(unittest.TestCase):
    """
    Clase: pruebasUnitarias del modulo funcion_factor_Sombra.py

    """

    def conocidosFactor_Sombra_Voladizos(self):
        """
        Metodo: conocidosFactor_Sombra_Voladizos

        """
        return (
         (
          [
           1, 1, 1, 'Sur'], 0.82),
         (
          [
           1, 1, 1, 'Norte'], 1),
         (
          [
           1, 1, 1, 'NO'], 1),
         (
          [
           1, 1, 1, 'NE'], 1),
         (
          [
           1, 0, 1, 'Cualquier cosa'], 1),
         (
          [
           1, 1, 1, 'Este'], 0.96),
         (
          [
           1, 1, 1, 'SO'], 0.93))

    def conocidosFactor_Sombra_Retranqueo(self):
        """
        Metodo: conocidosFactor_Sombra_Retranqueo

        """
        return (
         (
          [
           1, 1, 1, 'Sur'], 0.17),
         (
          [
           1, 1, 1, 'Norte'], 1),
         (
          [
           1, 1, 1, 'NO'], 1),
         (
          [
           1, 1, 1, 'NE'], 1),
         (
          [
           1, 0, 1, 'Cualquier cosa'], 1),
         (
          [
           1, 1, 1, 'Este'], 0.39),
         (
          [
           1, 1, 1, 'SO'], 0.23))

    def testFactor_Sombra_Voladizos(self):
        """
        Metodo: testFactor_Sombra_Voladizos

                self):                         :
        Comprobamos el funcionamiento correcto de la funcion con valores conocidos
        """
        for argumentos, resultado in self.conocidosFactor_Sombra_Voladizos():
            result = Factor_Sombra_Voladizos(argumentos[0], argumentos[1], argumentos[2], argumentos[3])
            self.assertEqual(resultado, result)

    def testFactor_Sombra_Retranqueo(self):
        """
        Metodo: testFactor_Sombra_Retranqueo

        Comprobamos el funcionamiento correcto de la funcion con valores conocidos
        """
        for argumentos, resultado in self.conocidosFactor_Sombra_Retranqueo():
            result = Factor_Sombra_Retranqueo(argumentos[0], argumentos[1], argumentos[2], argumentos[3])
            self.assertEqual(resultado, result)