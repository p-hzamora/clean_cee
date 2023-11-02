# File: a (Python 2.7)

'''
Modulo: analisisFinanciero.py
M\xf3dulo que implementa las funciones necesarias para realizar el c\xe1lculo financiero de las medidas de mejora
'''
import logging

def payBack(inversionInicial, ahorroEconomicoAnual, costesMantenimientoAnual, vidaUtil):
    '''
    Metodo: payBack
    Calculo del pay back por la instalaci\xf3n de un conjunto de medidas de mejora

    ARGUMENTOS:
\t\tinversionInicial: inversi\xf3n iicial del conjunto de medidas de mejora
\t\tahorroEconomicoAnual: ahorro economico que supone en las facturas anuales la instalacion del conjunto de mejoras
\t\tcostesMantenimientoAnual: gastos de mantenimiento que supone el nuevo conjunto de medidas
\t\tvidaUtil: vida util estimada

    '''
    vidaMasLongeva = max(vidaUtil)
    inversionTotal = 0
    for (i, v) in zip(inversionInicial, vidaUtil):
        inversionTotal += i * vidaMasLongeva / float(v)
    
    
    try:
        pB = inversionTotal / (ahorroEconomicoAnual - costesMantenimientoAnual)
    except:
        aux = '-'
        pB = aux
        logging.info(u'No hay ahorro econ\xc3\xb3mico')

    return pB


def van(inversionInicial, ahorroEconomicoAnual, tasaIncrementoPrecioEnergia, costesMantenimientoAnual, tasaRetornoInversion, vidaUtil):
    '''
    Metodo: van
    Calculo del Valor Anual Neto por la instalaci\xf3n de un conjunto de medidas de mejora

    ARGUMENTOS:
\t\tinversionInicial: inversi\xf3n iicial del conjunto de medidas de mejora
\t\tahorroEconomicoAnual: ahorro economico que supone en las facturas anuales la instalacion del conjunto de mejoras
\t\ttasaIncrementoPrecioEnergia: tasa conocida del incremento de cada combustible
\t\ttasaRetornoInversion: tasa conocida
\t\tcostesMantenimientoAnual: gastos de mantenimiento que supone el nuevo conjunto de medidas
\t\tvidaUtil: vida util estimada
    '''
    vidaMasLongeva = max(vidaUtil)
    inversionTotal = 0
    for (i, v) in zip(inversionInicial, vidaUtil):
        inversionTotal += i * vidaMasLongeva / float(v)
    
    ahorrosFuturos = 0
    for i in range(1, int(vidaMasLongeva + 1)):
        ahorrosFuturos += ahorroEconomicoAnual * (1 + tasaIncrementoPrecioEnergia) ** i / (1 + tasaRetornoInversion) ** i
    
    valor_actual_neto = -inversionTotal + ahorrosFuturos - costesMantenimientoAnual * vidaMasLongeva
    return valor_actual_neto

