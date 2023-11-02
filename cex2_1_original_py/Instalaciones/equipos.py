# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Instalaciones\equipos.pyc
# Compiled at: 2015-02-09 18:39:49
"""
Modulo: equipos.py

"""
import math, perfilesTerciario

class EQ_ED_AireAire_BDC:
    """
    Clase: EQ_ED_AireAire_BDC del modulo equipos.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Equipo de expansion directa aire-aire bomba de calor'

    def conCal_FCP(self, fcp_cal):
        """
        Metodo: conCal_FCP

        ARGUMENTOS:
                fcp_cal:
        """
        mod = 0.08565215 + 0.93881371 * fcp_cal - 0.1834361 * fcp_cal ** 2 + 0.15897022 * fcp_cal ** 3
        return mod

    def conCal_T(self, Th_ext):
        """
        Metodo: conCal_T

        ARGUMENTOS:
                Th_ext:
        """
        mod = 1.201222828 - 0.040063338 * Th_ext + 0.0010877 * Th_ext ** 2
        return mod

    def conRef_FCP(self, fcp_ref):
        """
        Metodo: conRef_FCP

        ARGUMENTOS:
                fcp_ref:
        """
        mod = 0.20123007 - 0.0312175 * fcp_ref + 1.9504979 * fcp_ref ** 2 - 1.1205104 * fcp_ref ** 3
        return mod

    def conRef_T(self, Th_int, T_ext):
        """
        Metodo: conRef_T

        ARGUMENTOS:
                Th_int:
                T_ext:
        """
        mod = 0.1117801 + 0.028493334 * Th_int - 0.000411156 * Th_int ** 2 + 0.021414276 * T_ext + 0.000161125 * T_ext ** 2 - 0.000679104 * Th_int * T_ext
        return mod


class EQ_ED_AireAgua_BDC:
    """
    Clase: EQ_ED_AireAgua_BDC del modulo equipos.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Equipo de expansion directa bomba de calor aire-agua'

    def conCal_FCP(self, fcp):
        """
        Metodo: conCal_FCP

        ARGUMENTOS:
                fcp:
        """
        mod = 0.08565216 + 0.93881381 * fcp - 0.18343613 * fcp ** 2 + 0.15897022 * fcp ** 3
        return mod

    def conCal_T(self, Th_ext):
        """
        Metodo: conCal_T

        ARGUMENTOS:
                Th_ext:
        """
        mod = 0.9496 + 0.009 * Th_ext - 0.0001 * Th_ext ** 2
        return mod


class EQ_ED_UnidadExterior:
    """
    Clase: EQ_ED_UnidadExterior del modulo equipos.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Equipo unidad exterior en expansion directa'

    def conCal_T(self, Th_ext):
        """
        Metodo: conCal_T

        ARGUMENTOS:
                Th_ext:
        """
        mod = 1.201222828 - 0.040063338 * Th_ext + 0.0010877 * Th_ext ** 2
        return mod

    def conCal_FCP(self, fcp):
        """
        Metodo: conCal_FCP

        ARGUMENTOS:
                fcp:
        """
        mod = 0.08565216 + 0.93881381 * fcp - 0.18343613 * fcp ** 2 + 0.15897022 * fcp ** 3
        return mod

    def conRef_FCP(self, fcp_ref):
        """
        Metodo: conRef_FCP

        ARGUMENTOS:
                fcp_ref:
        """
        mod = 0.20123007 - 0.0312175 * fcp_ref + 1.9504979 * fcp_ref ** 2 - 1.1205104 * fcp_ref ** 3
        return mod

    def conRef_T(self, Th_int, T_ext):
        """
        Metodo: conRef_T

        ARGUMENTOS:
                Th_int:
                T_ext:
        """
        mod = 0.1117801 + 0.028493334 * Th_int - 0.000411156 * Th_int ** 2 + 0.021414276 * T_ext + 0.000161125 * T_ext ** 2 - 0.000679104 * Th_int * T_ext
        return mod


class bombaCaudalVariable:
    """
    Clase: bombaCaudalVariable  del modulo equipos.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Bomba de Caudal Variable: Definida por curva'
        self.potenciaElectricaNominal = 0.1
        self.nombre = ''
        self.c1 = 0.6
        self.c2 = 0.4
        self.c3 = 0.0
        self.c4 = 0.0

    def potFCP(self, fcp):
        """
        Metodo: potFCP

        ARGUMENTOS:
                fcp:
        """
        potenciaConsumida = self.potenciaElectricaNominal * (self.c1 + self.c2 * fcp + self.c3 * fcp ** 2 + self.c4 * fcp ** 3)
        return potenciaConsumida


class bombaCaudalVariable2:
    """
    Clase: bombaCaudalVariable2  del modulo equipos.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Bomba de Caudal Variable: Definida por escalones'
        self.potenciaElectricaNominal = 0.1
        self.nombre = ''
        self.fcp = []
        self.escalonesPotencia = []

    def potFCP(self, fcp):
        """
        Metodo: potFCP

        ARGUMENTOS:
                fcp:
        """
        for f, escalonesPotencia in zip(self.fcp, self.escalonesPotencia):
            fraccionPotenciaConsumida = escalonesPotencia
            if f >= fcp:
                return fraccionPotenciaConsumida * self.potenciaElectricaNominal

        return fraccionPotenciaConsumida * self.potenciaElectricaNominal


class ventiladorCaudalConstante:
    """
    Clase: ventiladorCaudalConstante  del modulo equipos.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Ventilador de Caudal Constante'
        self.potenciaElectricaNominal = 0.1
        self.nombre = ''

    def pot(self):
        """
        Metodo: pot

        """
        potenciaConsumida = self.potenciaElectricaNominal
        return potenciaConsumida


class ventiladorCaudalVariable:
    """
    Clase: ventiladorCaudalVariable  del modulo equipos.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Ventilador de Caudal Variable: Definida por curva'
        self.potenciaElectricaNominal = 0.1
        self.nombre = ''
        self.c1 = 0.199
        self.c2 = -0.4144
        self.c3 = 0.81118
        self.c4 = 0.45420048
        self.c5 = 0.0

    def potFCP(self, fcp):
        """
        Metodo: potFCP

        ARGUMENTOS:
                fcp:
        """
        potenciaConsumida = self.potenciaElectricaNominal * (self.c1 + self.c2 * fcp + self.c3 * fcp ** 2 + self.c4 * fcp ** 3 + self.c5 * fcp ** 4)
        return potenciaConsumida


class ventiladorCaudalVariable2:
    """
    Clase: ventiladorCaudalVariable2 del modulo equipos.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Ventilador de Caudal Variable: Definido por escalones'
        self.potenciaElectricaNominal = 0.1
        self.nombre = ''
        self.fcp = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        self.escalonesPotencia = [0.15, 0.15, 0.16, 0.2, 0.25, 0.34, 0.45, 0.62, 0.83, 1.0]

    def potFCP(self, fcp):
        """
        Metodo: potFCP

        ARGUMENTOS:
                fcp:
        """
        for f, escalonesPotencia in zip(self.fcp, self.escalonesPotencia):
            fraccionPotenciaConsumida = escalonesPotencia
            if f >= fcp:
                return fraccionPotenciaConsumida * self.potenciaElectricaNominal

        return fraccionPotenciaConsumida * self.potenciaElectricaNominal


class TorreRefrigeracionVelocidadConstante:
    """
    Clase: TorreRefrigeracionVelocidadConstante  del modulo equipos.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Ventilador de Caudal Constante'
        self.potenciaElectricaNominal = 0.1
        self.nombre = ''

    def pot(self):
        """
        Metodo: pot

        """
        potenciaConsumida = self.potenciaElectricaNominal
        return potenciaConsumida


class TorreRefrigeracionVelocidadVariable:
    """
    Clase: TorreRefrigeracionVelocidadVariable  del modulo equipos.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Ventilador de Caudal Variable: Definida por curva'
        self.potenciaElectricaNominal = 0.1
        self.nombre = ''
        self.c1 = 0.331629
        self.c2 = -0.885676
        self.c3 = 0.6055
        self.c4 = 0.9484

    def potFCP(self, fcp):
        """
        Metodo: potFCP

        ARGUMENTOS:
                fcp:
        """
        potenciaConsumida = self.potenciaElectricaNominal * (self.c1 + self.c2 * fcp + self.c3 * fcp ** 2 + self.c4 * fcp ** 3)
        return potenciaConsumida


class TorreRefrigeracionVelocidadVariable2:
    """
    Clase: TorreRefrigeracionVelocidadVariable2 del modulo equipos.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Ventilador de Caudal Variable: Definido por escalones'
        self.potenciaElectricaNominal = 0.1
        self.nombre = ''
        self.fcp = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        self.escalonesPotencia = [0.15, 0.15, 0.16, 0.2, 0.25, 0.34, 0.45, 0.62, 0.83, 1.0]

    def potFCP(self, fcp):
        """
        Metodo: potFCP

        ARGUMENTOS:
                fcp:
        """
        for f, escalonesPotencia in zip(self.fcp, self.escalonesPotencia):
            fraccionPotenciaConsumida = escalonesPotencia
            if f >= fcp:
                return fraccionPotenciaConsumida * self.potenciaElectricaNominal

        return fraccionPotenciaConsumida * self.potenciaElectricaNominal


class CalderaCondensacion:
    """
    Clase: CalderaCondensacion del modulo equipos.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Caldera de condensacion definida mediante una curva bicuadratica'
        self.potenciaNominal = 100.0
        self.nombre = 'Caldera de Condensacion'
        self.c1 = 1.12
        self.c2 = 0.014
        self.c3 = -0.02599
        self.c4 = 0
        self.c5 = -1.4e-06
        self.c6 = -0.001536
        self.rendimientoNominalPlenaCarga = 0.9
        self.fcpMin = 0.1
        self.fcpMax = 1.0
        self.tempMin = 20.0
        self.tempMax = 85.0

    def rendimientoNominal(self):
        """
        Metodo: rendimientoNominal

        """
        rendimiento = 91.0 + math.log(self.potenciaNominal, 10)
        self.rendimientoNominalPlenaCarga = rendimiento / 100.0
        return rendimiento

    def potFcpT(self, fcp, t):
        """
        Metodo: potFcpT

        ARGUMENTOS:
                fcp:
                t:
        """
        if fcp < self.fcpMin:
            fcp = self.fcpMin
        elif fcp > self.fcpMax:
            fcp = self.fcpMax
        if t < self.tempMin:
            t = self.tempMin
        elif t > self.tempMax:
            t = self.tempMax
        normalizedBoilerEfficiencyCurveOutput = self.c1 + self.c2 * fcp + self.c3 * fcp ** 2 + self.c4 * t + self.c5 * t ** 2 + self.c6 * fcp * t
        potenciaConsumidaCargaParcial = self.potenciaNominal * fcp / (self.rendimientoNominalPlenaCarga * normalizedBoilerEfficiencyCurveOutput)
        return potenciaConsumidaCargaParcial


class CalderaBajaTemperatura:
    """
    Clase: CalderaBajaTemperatura del modulo equipos.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Caldera de baja temperatura definida mediante una curva bicubica'
        self.potenciaNominal = 100.0
        self.nombre = 'Caldera de Baja Temperatura'
        self.c1 = 1.1117
        self.c2 = 0.0786
        self.c3 = -0.40042
        self.c4 = 0
        self.c5 = -0.000156783
        self.c6 = 0.009384599
        self.c7 = 0.234257955
        self.c8 = 1.32927e-06
        self.c9 = -0.004446701
        self.c10 = -1.22498e-05
        self.rendimientoNominalPlenaCarga = 0.875
        self.fcpMin = 0.1
        self.fcpMax = 1.0
        self.tempMin = 20.0
        self.tempMax = 85.0

    def rendimientoNominal(self):
        """
        Metodo: rendimientoNominal

        """
        rendimiento = 87.5 + 1.5 * math.log(self.potenciaNominal, 10)
        self.rendimientoNominalPlenaCarga = rendimiento / 100.0
        return rendimiento

    def potFcpT(self, fcp, t):
        """
        Metodo: potFcpT

        ARGUMENTOS:
                fcp:
                t:
        """
        if fcp < self.fcpMin:
            fcp = self.fcpMin
        elif fcp > self.fcpMax:
            fcp = self.fcpMax
        if t < self.tempMin:
            t = self.tempMin
        elif t > self.tempMax:
            t = self.tempMax
        normalizedBoilerEfficiencyCurveOutput = self.c1 + self.c2 * fcp + self.c3 * fcp ** 2 + self.c4 * t + self.c5 * t ** 2 + self.c6 * fcp * t + self.c7 * fcp ** 3 + self.c8 * t ** 3 + self.c9 * fcp ** 2 * t + self.c10 * fcp * t ** 2
        potenciaConsumidaCargaParcial = self.potenciaNominal * fcp / (self.rendimientoNominalPlenaCarga * normalizedBoilerEfficiencyCurveOutput)
        return potenciaConsumidaCargaParcial


class CalderaConvencional:
    """
    Clase: CalderaConvencional del modulo equipos.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Caldera Convencional. Definida por una curva cÃºbica.'
        self.potenciaNominal = 100.0
        self.nombre = 'Caldera convencional - típica año 1983'
        self.c1 = 0.751522818 / 0.8415236398079999
        self.c2 = 0.384597789 / 0.8415236398079999
        self.c3 = -0.51156047 / 0.8415236398079999
        self.c4 = 0.200944063 / 0.8415236398079999
        self.rendimientoNominalPlenaCarga = 0.84
        self.fcpMin = 0.1
        self.fcpMax = 1.0

    def rendimientoNominal(self):
        """
        Metodo: rendimientoNominal

        """
        rendimiento = 84.0 + 2.0 * math.log(self.potenciaNominal, 10)
        self.rendimientoNominalPlenaCarga = rendimiento / 100.0
        return rendimiento

    def potFcp(self, fcp):
        """
        Metodo: potFcp
        Nos devuelve la potencia consumida en función del fcp
        
        ARGUMENTOS:
                fcp:
        """
        if fcp < self.fcpMin:
            fcp = self.fcpMin
        elif fcp > self.fcpMax:
            fcp = self.fcpMax
        normalizedBoilerEfficiencyCurveOutput = self.c1 + self.c2 * fcp + self.c3 * fcp ** 2 + self.c4 * fcp ** 3
        potenciaConsumidaCargaParcial = self.potenciaNominal * fcp / (self.rendimientoNominalPlenaCarga * normalizedBoilerEfficiencyCurveOutput)
        return potenciaConsumidaCargaParcial


class ExpansionDirectaAireAguaBombaDeCalorModoCalor:
    """
    Clase: ExpansionDirectaAireAguaBombaDeCalorModoCalor del modulo equipos.py
    Equipo de expansion directa aire-agua bomba de calor
    datos calener VYP 
    con_FCP-EQ_ED_AireAguaBDC-ACS-Defecto = 0.0856522 + 0.938814 VI1 - 0.183436 VI1² + 0.15897 VI1³
    conCal_T-EQ_ED_AireAire_BDC-Defecto = 1.20122 + 0 VI1 + 0 VI1² - 0.0400633 VI2 + 0.0010877 VI2² + 0 VI1 VI2

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Expansión directa aire-aire bomba de calor'
        self.potenciaNominal = 100.0
        self.nombre = 'Expansion directa aire-aire bomba de calor'
        self.c1 = 0.0856522
        self.c2 = 0.938814
        self.c3 = -0.183436
        self.c4 = 0.15897
        self.d1 = 0.9496
        self.d2 = 0.0
        self.d3 = 0.0
        self.d4 = 0.009
        self.d5 = -0.0001
        self.d6 = 0
        self.e1 = 0.8232
        self.e2 = 0.0
        self.e3 = 0.0
        self.e4 = 0.0281
        self.e5 = 0.0002
        self.e6 = 0
        self.rendimientoNominalPlenaCarga = 2.5
        self.fcpMin = 0.0
        self.fcpMax = 1.0
        self.tIntMin = 10.0
        self.tIntMax = 30.0
        self.tHExtMin = -15.0
        self.tHExtMax = 30.0

    def capDisponibleTIntTHExt(self, tInt, tHExt):
        if tInt < self.tIntMin:
            tInt = self.tIntMin
        elif tInt > self.tIntMax:
            tInt = self.tIntMax
        if tHExt < self.tHExtMin:
            tHExt = self.tHExtMin
        elif tHExt > self.tHExtMax:
            tHExt = self.tHExtMax
        capCal_T = self.e1 + self.e2 * tInt + self.e3 * tInt ** 2 + self.e4 * tHExt + self.e5 * tHExt ** 2 + self.e6 * tInt * tHExt
        capacidad = self.potenciaNominal * capCal_T
        return capacidad

    def potFcpTIntTHExt(self, fcp, tInt, tHExt):
        """
        Metodo: potFcpTIntTHExt
        Devuelve la potencia consumida en funcion de:
        fcp : factor de carga parcial
        tInt: temperatura Interior
        tHext: temperatura humeda exterior

        ARGUMENTOS:
            fcp:
            tInt:
            tHExt:
        """
        if fcp < self.fcpMin:
            fcp = self.fcpMin
        elif fcp > self.fcpMax:
            fcp = self.fcpMax
        if tInt < self.tIntMin:
            tInt = self.tIntMin
        elif tInt > self.tIntMax:
            tInt = self.tIntMax
        if tHExt < self.tHExtMin:
            tHExt = self.tHExtMin
        elif tHExt > self.tHExtMax:
            tHExt = self.tHExtMax
        conCal_FCP = self.c1 + self.c2 * fcp + self.c3 * fcp ** 2 + self.c4 * fcp ** 3
        conCal_T = self.d1 + self.d2 * tInt + self.d3 * tInt ** 2 + self.d4 * tHExt + self.d5 * tHExt ** 2 + self.d6 * tInt * tHExt
        potenciaConsumidaCargaParcial = self.potenciaNominal / self.rendimientoNominalPlenaCarga * conCal_FCP * conCal_T
        return potenciaConsumidaCargaParcial


class ExpansionDirectaAireAireBombaDeCalorModoCalor:
    """
    Clase: ExpansionDirectaAireAireBombaDeCalorModoCalor del modulo equipos.py
    Equipo de expansion directa aire-agua bomba de calor
    datos calener VYP 
    con_FCP-EQ_ED_AireAguaBDC-ACS-Defecto = 0.0856522 + 0.938814 VI1 - 0.183436 VI1² + 0.15897 VI1³
    conCal_T-EQ_ED_AireAire_BDC-Defecto = 1.20122 + 0 VI1 + 0 VI1² - 0.0400633 VI2 + 0.0010877 VI2² + 0 VI1 VI2

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Expansión directa aire-aire bomba de calor'
        self.potenciaNominal = 100.0
        self.nombre = 'Expansion directa aire-aire bomba de calor'
        self.c1 = 0.0856522
        self.c2 = 0.938814
        self.c3 = -0.183436
        self.c4 = 0.15897
        self.d1 = 1.20122
        self.d2 = 0.0
        self.d3 = 0.0
        self.d4 = -0.0400633
        self.d5 = 0.0010877
        self.d6 = 0
        self.e1 = 0.814741
        self.e2 = 0.0
        self.e3 = 0.0
        self.e4 = 0.0306826
        self.e5 = 3.23028e-05
        self.e6 = 0
        self.rendimientoNominalPlenaCarga = 2.5
        self.fcpMin = 0.0
        self.fcpMax = 1.0
        self.tIntMin = 10.0
        self.tIntMax = 30.0
        self.tHExtMin = -15.0
        self.tHExtMax = 30.0

    def capDisponibleTIntTHExt(self, tInt, tHExt):
        if tInt < self.tIntMin:
            tInt = self.tIntMin
        elif tInt > self.tIntMax:
            tInt = self.tIntMax
        if tHExt < self.tHExtMin:
            tHExt = self.tHExtMin
        elif tHExt > self.tHExtMax:
            tHExt = self.tHExtMax
        capCal_T = self.e1 + self.e2 * tInt + self.e3 * tInt ** 2 + self.e4 * tHExt + self.e5 * tHExt ** 2 + self.e6 * tInt * tHExt
        capacidad = self.potenciaNominal * capCal_T
        return capacidad

    def potFcpTIntTHExt(self, fcp, tInt, tHExt):
        """
        Metodo: potFcpTIntTHExt
        Devuelve la potencia consumida en funcion de:
        fcp : factor de carga parcial
        tInt: temperatura Interior
        tHext: temperatura humeda exterior

        ARGUMENTOS:
            fcp:
            tInt:
            tHExt:
        """
        if fcp < self.fcpMin:
            fcp = self.fcpMin
        elif fcp > self.fcpMax:
            fcp = self.fcpMax
        if tInt < self.tIntMin:
            tInt = self.tIntMin
        elif tInt > self.tIntMax:
            tInt = self.tIntMax
        if tHExt < self.tHExtMin:
            tHExt = self.tHExtMin
        elif tHExt > self.tHExtMax:
            tHExt = self.tHExtMax
        conCal_FCP = self.c1 + self.c2 * fcp + self.c3 * fcp ** 2 + self.c4 * fcp ** 3
        conCal_T = self.d1 + self.d2 * tInt + self.d3 * tInt ** 2 + self.d4 * tHExt + self.d5 * tHExt ** 2 + self.d6 * tInt * tHExt
        potenciaConsumidaCargaParcial = self.potenciaNominal / self.rendimientoNominalPlenaCarga * conCal_FCP * conCal_T
        return potenciaConsumidaCargaParcial


class VRVModoCalor:
    """
    Clase: VRVModoCalor del modulo equipos.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Expansión directa aire-aire bomba de calor'
        self.potenciaNominal = 100.0
        self.nombre = 'Expansion directa aire-aire bomba de calor'
        self.c1 = 0.85
        self.c2 = 0.15
        self.c3 = 0.0
        self.c4 = 0.0
        self.d1 = 1.20122
        self.d2 = 0.0
        self.d3 = 0.0
        self.d4 = -0.0400633
        self.d5 = 0.0010877
        self.d6 = 0
        self.e1 = 0.814741
        self.e2 = 0.0
        self.e3 = 0.0
        self.e4 = 0.0306826
        self.e5 = 3.23028e-05
        self.e6 = 0
        self.rendimientoNominalPlenaCarga = 2.5
        self.fcpMin = 0.01
        self.fcpMax = 1.0
        self.tIntMin = 10.0
        self.tIntMax = 30.0
        self.tHExtMin = -15.0
        self.tHExtMax = 30.0

    def capDisponibleTIntTHExt(self, tInt, tHExt):
        if tInt < self.tIntMin:
            tInt = self.tIntMin
        elif tInt > self.tIntMax:
            tInt = self.tIntMax
        if tHExt < self.tHExtMin:
            tHExt = self.tHExtMin
        elif tHExt > self.tHExtMax:
            tHExt = self.tHExtMax
        capCal_T = self.e1 + self.e2 * tInt + self.e3 * tInt ** 2 + self.e4 * tHExt + self.e5 * tHExt ** 2 + self.e6 * tInt * tHExt
        capacidad = self.potenciaNominal * capCal_T
        return capacidad

    def potFcpTIntTHExt(self, fcp, tInt, tHExt):
        """
        Metodo: potFcpTIntTHExt

        ARGUMENTOS:
                fcp:
                tInt:
                tHExt:
        """
        if fcp < self.fcpMin:
            fcp = self.fcpMin
        elif fcp > self.fcpMax:
            fcp = self.fcpMax
        if tInt < self.tIntMin:
            tInt = self.tIntMin
        elif tInt > self.tIntMax:
            tInt = self.tIntMax
        if tHExt < self.tHExtMin:
            tHExt = self.tHExtMin
        elif tHExt > self.tHExtMax:
            tHExt = self.tHExtMax
        plf_FCP = self.c1 + self.c2 * fcp + self.c3 * fcp ** 2 + self.c4 * fcp ** 3
        conCal_T = self.d1 + self.d2 * tInt + self.d3 * tInt ** 2 + self.d4 * tHExt + self.d5 * tHExt ** 2 + self.d6 * tInt * tHExt
        potenciaConsumidaCargaParcial = self.potenciaNominal * fcp / self.rendimientoNominalPlenaCarga / plf_FCP * conCal_T
        return potenciaConsumidaCargaParcial


class EquiposRefrigeracionDefinidosPorCurva:

    def getCurva(self):
        curva = [
         '%s' % self.c1,
         '%s' % self.c2,
         '%s' % self.c3,
         '%s' % self.c4,
         '%s' % self.d1,
         '%s' % self.d2,
         '%s' % self.d3,
         '%s' % self.d4,
         '%s' % self.d5,
         '%s' % self.d6]
        return curva


class ExpansionDirectaAireAireBombaDeCalorModoFrio(EquiposRefrigeracionDefinidosPorCurva):
    """
    Clase: ExpansionDirectaAireAireBombaDeCalorModoFrio del modulo equipos.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Expansión directa aire-aire bomba de calor'
        self.potenciaNominal = 100.0
        self.nombre = 'Expansion directa aire-aire bomba de calor'
        self.c1 = 0.20123
        self.c2 = -0.0312175
        self.c3 = 1.9505
        self.c4 = -1.12051
        self.d1 = 0.11178
        self.d2 = 0.0284933
        self.d3 = -0.000411156
        self.d4 = 0.0214143
        self.d5 = 0.000161125
        self.d6 = -0.000679104
        self.e1 = 0.880785
        self.e2 = 0.0142476
        self.e3 = 0.000554364
        self.e4 = -0.00755806
        self.e5 = 3.29832e-05
        self.e6 = -0.000191711
        self.rendimientoNominalPlenaCarga = 2.5
        self.fcpMin = 0.0
        self.fcpMax = 1.0
        self.tHIntMin = 5.0
        self.tHIntMax = 30.0
        self.tExtMin = 5.0
        self.tExtMax = 50.0

    def capDisponibleTHIntTExt(self, tHInt, tExt):
        if tHInt < self.tHIntMin:
            tHInt = self.tHIntMin
        elif tHInt > self.tHIntMax:
            tHInt = self.tHIntMax
        if tExt < self.tExtMin:
            tExt = self.tExtMin
        elif tExt > self.tExtMax:
            tExt = self.tExtMax
        capCal_T = self.e1 + self.e2 * tHInt + self.e3 * tHInt ** 2 + self.e4 * tExt + self.e5 * tExt ** 2 + self.e6 * tHInt * tExt
        capacidad = self.potenciaNominal * capCal_T
        return capacidad

    def potFcpTHIntTExt(self, fcp, tHInt, tExt):
        """
        Metodo: potFcpTHIntTExt

        ARGUMENTOS:
            fcp:
            tHInt:
            tExt:
        """
        if fcp < self.fcpMin:
            fcp = self.fcpMin
        elif fcp > self.fcpMax:
            fcp = self.fcpMax
        if tHInt < self.tHIntMin:
            tHInt = self.tHIntMin
        elif tHInt > self.tHIntMax:
            tHInt = self.tHIntMax
        if tExt < self.tExtMin:
            tExt = self.tExtMin
        elif tExt > self.tExtMax:
            tExt = self.tExtMax
        conRef_FCP = self.c1 + self.c2 * fcp + self.c3 * fcp ** 2 + self.c4 * fcp ** 3
        conRef_T = self.d1 + self.d2 * tHInt + self.d3 * tHInt ** 2 + self.d4 * tExt + self.d5 * tExt ** 2 + self.d6 * tHInt * tExt
        potenciaConsumidaCargaParcial = self.potenciaNominal / self.rendimientoNominalPlenaCarga * conRef_FCP * conRef_T / 0.65
        return potenciaConsumidaCargaParcial


class ExpansionDirectaAguaAireBombaDeCalorModoFrio(EquiposRefrigeracionDefinidosPorCurva):
    """
    Clase: ExpansionDirectaAireAireBombaDeCalorModoFrio del modulo equipos.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Expansión directa aire-aire bomba de calor'
        self.potenciaNominal = 100.0
        self.nombre = 'Expansion directa aire-aire bomba de calor'
        self.temperaturaAproximacion = 3.0
        self.c1 = 0.088065
        self.c2 = 1.137742
        self.c3 = -0.225806
        self.c4 = 0.0
        self.d1 = 0.612022
        self.d2 = -0.0162828
        self.d3 = 0.00040824
        self.d4 = 0.0030978
        self.d5 = 0.00059292
        self.d6 = -0.00066744
        self.e1 = 0.966736
        self.e2 = 0.040518
        self.e3 = 0.00058968
        self.e4 = -0.0080352
        self.e5 = 6.804e-05
        self.e6 = -0.0004536
        self.rendimientoNominalPlenaCarga = 2.5
        self.fcpMin = 0.0
        self.fcpMax = 1.0
        self.tHIntMin = 5
        self.tHIntMax = 50
        self.tExtMin = 5
        self.tExtMax = 50

    def capDisponibleTHIntTExt(self, tHInt, tExt):
        tExt = tExt + self.temperaturaAproximacion
        if tHInt < self.tHIntMin:
            tHInt = self.tHIntMin
        elif tHInt > self.tHIntMax:
            tHInt = self.tHIntMax
        if tExt < self.tExtMin:
            tExt = self.tExtMin
        elif tExt > self.tExtMax:
            tExt = self.tExtMax
        capCal_T = self.e1 + self.e2 * tHInt + self.e3 * tHInt ** 2 + self.e4 * tExt + self.e5 * tExt ** 2 + self.e6 * tHInt * tExt
        capacidad = self.potenciaNominal * capCal_T
        return capacidad

    def potFcpTHIntTExt(self, fcp, tHInt, tExt):
        """
        Metodo: potFcpTHIntTExt

        ARGUMENTOS:
                fcp:
                tHInt:
                tExt:
        """
        tExt = tExt + self.temperaturaAproximacion
        if fcp < self.fcpMin:
            fcp = self.fcpMin
        elif fcp > self.fcpMax:
            fcp = self.fcpMax
        if tHInt < self.tHIntMin:
            tHInt = self.tHIntMin
        elif tHInt > self.tHIntMax:
            tHInt = self.tHIntMax
        if tExt < self.tExtMin:
            tExt = self.tExtMin
        elif tExt > self.tExtMax:
            tExt = self.tExtMax
        conRef_FCP = self.c1 + self.c2 * fcp + self.c3 * fcp ** 2 + self.c4 * fcp ** 3
        conRef_T = self.d1 + self.d2 * tHInt + self.d3 * tHInt ** 2 + self.d4 * tExt + self.d5 * tExt ** 2 + self.d6 * tHInt * tExt
        potenciaConsumidaCargaParcial = self.potenciaNominal / self.rendimientoNominalPlenaCarga * conRef_FCP * conRef_T / 0.65
        return potenciaConsumidaCargaParcial


class ExpansionDirectaAguaAireBombaDeCalorModoFrioVRV(EquiposRefrigeracionDefinidosPorCurva):
    """
    Clase: ExpansionDirectaAireAireBombaDeCalorModoFrio del modulo equipos.py
    Derivada a partir de la condensada por agua del calener GT,
    pero con la degradación de rendimiento de la del energyPlus

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Expansión directa aire-aire bomba de calor'
        self.potenciaNominal = 100.0
        self.nombre = 'Expansion directa aire-aire bomba de calor'
        self.temperaturaAproximacion = 3.0
        self.c1 = 0.1
        self.c2 = 0.9
        self.c3 = 0.0
        self.c4 = 0.0
        self.d1 = 0.612022
        self.d2 = -0.0162828
        self.d3 = 0.00040824
        self.d4 = 0.0030978
        self.d5 = 0.00059292
        self.d6 = -0.00066744
        self.e1 = 0.966736
        self.e2 = 0.040518
        self.e3 = 0.00058968
        self.e4 = -0.0080352
        self.e5 = 6.804e-05
        self.e6 = -0.0004536
        self.rendimientoNominalPlenaCarga = 2.5
        self.fcpMin = 0.0
        self.fcpMax = 1.0
        self.tHIntMin = 5
        self.tHIntMax = 50
        self.tExtMin = 5
        self.tExtMax = 50

    def capDisponibleTHIntTExt(self, tHInt, tExt):
        tExt = tExt + self.temperaturaAproximacion
        if tHInt < self.tHIntMin:
            tHInt = self.tHIntMin
        elif tHInt > self.tHIntMax:
            tHInt = self.tHIntMax
        if tExt < self.tExtMin:
            tExt = self.tExtMin
        elif tExt > self.tExtMax:
            tExt = self.tExtMax
        capCal_T = self.e1 + self.e2 * tHInt + self.e3 * tHInt ** 2 + self.e4 * tExt + self.e5 * tExt ** 2 + self.e6 * tHInt * tExt
        capacidad = self.potenciaNominal * capCal_T
        return capacidad

    def potFcpTHIntTExt(self, fcp, tHInt, tExt):
        """
        Metodo: potFcpTHIntTExt

        ARGUMENTOS:
                fcp:
                tHInt:
                tExt:
        """
        tExt = tExt + self.temperaturaAproximacion
        if fcp < self.fcpMin:
            fcp = self.fcpMin
        elif fcp > self.fcpMax:
            fcp = self.fcpMax
        if tHInt < self.tHIntMin:
            tHInt = self.tHIntMin
        elif tHInt > self.tHIntMax:
            tHInt = self.tHIntMax
        if tExt < self.tExtMin:
            tExt = self.tExtMin
        elif tExt > self.tExtMax:
            tExt = self.tExtMax
        conRef_FCP = self.c1 + self.c2 * fcp + self.c3 * fcp ** 2 + self.c4 * fcp ** 3
        conRef_T = self.d1 + self.d2 * tHInt + self.d3 * tHInt ** 2 + self.d4 * tExt + self.d5 * tExt ** 2 + self.d6 * tHInt * tExt
        potenciaConsumidaCargaParcial = self.potenciaNominal / self.rendimientoNominalPlenaCarga * conRef_FCP * conRef_T / 0.65
        return potenciaConsumidaCargaParcial


class VRVModoFrio(EquiposRefrigeracionDefinidosPorCurva):
    """
    Clase: VRVModoFrio del modulo equipos.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Expansión directa aire-aire bomba de calor'
        self.potenciaNominal = 100.0
        self.nombre = 'Expansion directa aire-aire bomba de calor'
        self.c1 = 0.85
        self.c2 = 0.15
        self.c3 = 0.0
        self.c4 = 0.0
        self.d1 = 0.11178
        self.d2 = 0.0284933
        self.d3 = -0.000411156
        self.d4 = 0.0214143
        self.d5 = 0.000161125
        self.d6 = -0.000679104
        self.rendimientoNominalPlenaCarga = 2.5
        self.fcpMin = 0.0
        self.fcpMax = 1.0
        self.tHIntMin = 5.0
        self.tHIntMax = 30.0
        self.tExtMin = 5.0
        self.tExtMax = 50.0
        self.e1 = 0.880785
        self.e2 = 0.0142476
        self.e3 = 0.000554364
        self.e4 = -0.00755806
        self.e5 = 3.29832e-05
        self.e6 = -0.000191711

    def capDisponibleTHIntTExt(self, tHInt, tExt):
        if tHInt < self.tHIntMin:
            tHInt = self.tHIntMin
        elif tHInt > self.tHIntMax:
            tHInt = self.tHIntMax
        if tExt < self.tExtMin:
            tExt = self.tExtMin
        elif tExt > self.tExtMax:
            tExt = self.tExtMax
        capCal_T = self.e1 + self.e2 * tHInt + self.e3 * tHInt ** 2 + self.e4 * tExt + self.e5 * tExt ** 2 + self.e6 * tHInt * tExt
        capacidad = self.potenciaNominal * capCal_T
        return capacidad

    def potFcpTHIntTExt(self, fcp, tHInt, tExt):
        """
        Metodo: potFcpTHIntTExt

        ARGUMENTOS:
            fcp:
            tHInt:
            tExt:
        """
        if fcp < self.fcpMin:
            fcp = self.fcpMin
        elif fcp > self.fcpMax:
            fcp = self.fcpMax
        if tHInt < self.tHIntMin:
            tHInt = self.tHIntMin
        elif tHInt > self.tHIntMax:
            tHInt = self.tHIntMax
        if tExt < self.tExtMin:
            tExt = self.tExtMin
        elif tExt > self.tExtMax:
            tExt = self.tExtMax
        plf_FCP = self.c1 + self.c2 * fcp + self.c3 * fcp ** 2 + self.c4 * fcp ** 3
        conRef_T = self.d1 + self.d2 * tHInt + self.d3 * tHInt ** 2 + self.d4 * tExt + self.d5 * tExt ** 2 + self.d6 * tHInt * tExt
        potenciaConsumidaCargaParcial = self.potenciaNominal / self.rendimientoNominalPlenaCarga * fcp * conRef_T / plf_FCP / 0.65
        if potenciaConsumidaCargaParcial == 0.0:
            potenciaConsumidaCargaParcial = 1e-06
        return potenciaConsumidaCargaParcial


class VRVModoFrioAireAgua:
    """
    Clase: VRVModoFrio del modulo equipos.py

    """

    def __init__(self):
        """
        Constructor de la clase

        """
        self.descripcion = 'Expansión directa aire-agua bomba de calor'
        self.potenciaNominal = 100.0
        self.nombre = 'Expansion directa aire-agua bomba de calor'
        self.c1 = 0.85
        self.c2 = 0.15
        self.c3 = 0.0
        self.c4 = 0.0
        self.d1 = 0.11178
        self.d2 = 0.0284933
        self.d3 = -0.000411156
        self.d4 = 0.0214143
        self.d5 = 0.000161125
        self.d6 = -0.000679104
        self.rendimientoNominalPlenaCarga = 2.5
        self.fcpMin = 0.0
        self.fcpMax = 1.0
        self.tHIntMin = 5.0
        self.tHIntMax = 30.0
        self.tExtMin = 5.0
        self.tExtMax = 50.0

    def potFcpTHIntTExt(self, fcp, tHInt, tExt):
        """
        Metodo: potFcpTHIntTExt

        ARGUMENTOS:
                fcp:
                tHInt:
                tExt:
        """
        if fcp < self.fcpMin:
            fcp = self.fcpMin
        elif fcp > self.fcpMax:
            fcp = self.fcpMax
        if tHInt < self.tHIntMin:
            tHInt = self.tHIntMin
        elif tHInt > self.tHIntMax:
            tHInt = self.tHIntMax
        if tExt < self.tExtMin:
            tExt = self.tExtMin
        elif tExt > self.tExtMax:
            tExt = self.tExtMax
        plf_FCP = self.c1 + self.c2 * fcp + self.c3 * fcp ** 2 + self.c4 * fcp ** 3
        conRef_T = self.d1 + self.d2 * tHInt + self.d3 * tHInt ** 2 + self.d4 * tExt + self.d5 * tExt ** 2 + self.d6 * tHInt * tExt
        potenciaConsumidaCargaParcial = self.potenciaNominal / self.rendimientoNominalPlenaCarga * fcp * conRef_T / plf_FCP / 0.65
        if potenciaConsumidaCargaParcial == 0.0:
            potenciaConsumidaCargaParcial = 1e-06
        return potenciaConsumidaCargaParcial


def estimacionCargaEscalonadaCalefaccion(zona, uso, porcentajeDesde, porcentajeDeLaPotenciaTotalAportadoPorEsteGenerador):
    """
    Metodo: estimacionCargaEscalonadaCalefaccion

    ARGUMENTOS:
                zona:
                uso:
                porcentajeDesd:
    """
    perfil = perfilesTerciario.PerfilDemandaCalefaccion(zona, uso)
    fcpSistema = map((lambda x: x / 10.0 + 0.05), range(10))
    aux = map((lambda x, y: x / y), perfil, fcpSistema)
    total = sum(aux)
    perfilRepartoTiempoPorcentualCaracteristico = map((lambda x: x / total), aux)
    porcentajeHasta = porcentajeDesde + porcentajeDeLaPotenciaTotalAportadoPorEsteGenerador
    fcpGeneradoresAnteriores = []
    fcpGenerador = []
    fcpGeneradoresSiguientes = []
    for fcp in fcpSistema:
        if fcp <= porcentajeDesde:
            fcpGeneradoresAnteriores.append(fcp)
        else:
            fcpGeneradoresAnteriores.append(porcentajeDesde)
        if fcp <= porcentajeDesde:
            fcpGenerador.append(0)
        elif fcp <= porcentajeHasta:
            fcpGenerador.append(fcp - porcentajeDesde)
        else:
            fcpGenerador.append(porcentajeHasta - porcentajeDesde)
        if fcp <= porcentajeHasta:
            fcpGeneradoresSiguientes.append(0)
        else:
            fcpGeneradoresSiguientes.append(fcp - porcentajeHasta)

    porcentajeEnergiaGenerador = map((lambda x, y, z, w: y / (x + y + z) * w), fcpGeneradoresAnteriores, fcpGenerador, fcpGeneradoresSiguientes, perfil)
    nivelDeCargaDelGenerador = map((lambda x: x / porcentajeDeLaPotenciaTotalAportadoPorEsteGenerador), fcpGenerador)
    porcentajeTiempoAcumulado = 0
    for n, t in zip(nivelDeCargaDelGenerador, perfilRepartoTiempoPorcentualCaracteristico):
        if n > 0:
            porcentajeTiempoAcumulado += t

    betaComb = sum(map((lambda x, y: x * y), nivelDeCargaDelGenerador, perfilRepartoTiempoPorcentualCaracteristico)) / porcentajeTiempoAcumulado
    return (
     porcentajeEnergiaGenerador, betaComb)


def estimacionRendimientoEstacionalBDCCalefaccion(zona, uso, tipoGenerador, rendNominal, porcentajeDesde, porcentajeDeLaPotenciaTotalAportadoPorEsteGenerador):
    """
    Metodo: estimacionRendimientoEstacionalBDCCalefaccion

    ARGUMENTOS:
                zona:
                uso:
                tipoGenerador:
                rendNominal:
                porcentajeDesd:
    """
    perfil = perfilesTerciario.PerfilDemandaCalefaccion(zona, uso)
    perfilTempHumExt = perfilesTerciario.PerfilTemperaturaHumedaCalefaccion(zona, uso)
    fcpSistema = map((lambda x: x / 10.0 + 0.05), range(10))
    porcentajeHasta = porcentajeDesde + porcentajeDeLaPotenciaTotalAportadoPorEsteGenerador
    fcpGeneradoresAnteriores = []
    fcpGenerador = []
    fcpGeneradoresSiguientes = []
    for fcp in fcpSistema:
        if fcp <= porcentajeDesde:
            fcpGeneradoresAnteriores.append(fcp)
        else:
            fcpGeneradoresAnteriores.append(porcentajeDesde)
        if fcp <= porcentajeDesde:
            fcpGenerador.append(0)
        elif fcp <= porcentajeHasta:
            fcpGenerador.append(fcp - porcentajeDesde)
        else:
            fcpGenerador.append(porcentajeHasta - porcentajeDesde)
        if fcp <= porcentajeHasta:
            fcpGeneradoresSiguientes.append(0)
        else:
            fcpGeneradoresSiguientes.append(fcp - porcentajeHasta)

    porcentajeEnergiaGenerador = map((lambda x, y, z, w: y / (x + y + z) * w), fcpGeneradoresAnteriores, fcpGenerador, fcpGeneradoresSiguientes, perfil)
    nivelDeCargaDelGenerador = map((lambda x: x / porcentajeDeLaPotenciaTotalAportadoPorEsteGenerador), fcpGenerador)
    porcentajeDeLaEnergiaTotalAportadoPorEsteGenerador = sum(porcentajeEnergiaGenerador)
    factorPonderacion = map((lambda x: x / porcentajeDeLaEnergiaTotalAportadoPorEsteGenerador), porcentajeEnergiaGenerador)
    if tipoGenerador == 'Bomba de Calor - Caudal Ref. Variable':
        bDC = VRVModoCalor()
    else:
        bDC = ExpansionDirectaAireAireBombaDeCalorModoCalor()
    bDC.rendimientoNominalPlenaCarga = rendNominal / 100.0
    fcpMod = [ x / bDC.capDisponibleTIntTHExt(20.0, y) * bDC.potenciaNominal for x, y in zip(nivelDeCargaDelGenerador, perfilTempHumExt) ]
    eir = []
    for x, y in zip(fcpMod, perfilTempHumExt):
        if x != 0:
            eir.append(bDC.potFcpTIntTHExt(x, 20.0, y) / (x * bDC.capDisponibleTIntTHExt(20.0, y)))
        else:
            eir.append(0)

    eirEstacional = sum([ x * y for x, y in zip(factorPonderacion, eir) ])
    rendimientoEstacional = 1.0 / eirEstacional * 100.0
    return (
     porcentajeEnergiaGenerador, rendimientoEstacional)


def estimacionRendimientoEstacionalBDCACS(zona, uso, tipoGenerador, rendNominal, porcentajeDesde, porcentajeDeLaPotenciaTotalAportadoPorEsteGenerador):
    """
    Metodo: estimacionRendimientoEstacionalBDCACS

    ARGUMENTOS: (mantenemos los mismos argumentos en estimacionRendimientoEstacionalBDCCalefaccion
                aunque algunos no hacen falta):
                zona:
                uso:
                tipoGenerador:
                rendNominal:
                porcentajeDesd:
    """
    perfil = [
     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
    perfilTemperaturaHumedaCalefaccion = perfilesTerciario.PerfilTemperaturaHumedaCalefaccion(zona, uso)
    tempMedia = sum(perfilTemperaturaHumedaCalefaccion) / len(perfilTemperaturaHumedaCalefaccion)
    perfilTempHumExt = [tempMedia, tempMedia, tempMedia, tempMedia, tempMedia, tempMedia, tempMedia, 
     tempMedia, tempMedia, tempMedia]
    fcpSistema = map((lambda x: x / 10.0 + 0.05), range(10))
    porcentajeHasta = porcentajeDesde + porcentajeDeLaPotenciaTotalAportadoPorEsteGenerador
    fcpGeneradoresAnteriores = []
    fcpGenerador = []
    fcpGeneradoresSiguientes = []
    for fcp in fcpSistema:
        if fcp <= porcentajeDesde:
            fcpGeneradoresAnteriores.append(fcp)
        else:
            fcpGeneradoresAnteriores.append(porcentajeDesde)
        if fcp <= porcentajeDesde:
            fcpGenerador.append(0)
        elif fcp <= porcentajeHasta:
            fcpGenerador.append(fcp - porcentajeDesde)
        else:
            fcpGenerador.append(porcentajeHasta - porcentajeDesde)
        if fcp <= porcentajeHasta:
            fcpGeneradoresSiguientes.append(0)
        else:
            fcpGeneradoresSiguientes.append(fcp - porcentajeHasta)

    porcentajeEnergiaGenerador = map((lambda x, y, z, w: y / (x + y + z) * w), fcpGeneradoresAnteriores, fcpGenerador, fcpGeneradoresSiguientes, perfil)
    nivelDeCargaDelGenerador = map((lambda x: x / porcentajeDeLaPotenciaTotalAportadoPorEsteGenerador), fcpGenerador)
    porcentajeDeLaEnergiaTotalAportadoPorEsteGenerador = sum(porcentajeEnergiaGenerador)
    factorPonderacion = map((lambda x: x / porcentajeDeLaEnergiaTotalAportadoPorEsteGenerador), porcentajeEnergiaGenerador)
    if tipoGenerador == 'Bomba de Calor - Caudal Ref. Variable':
        bDC = ExpansionDirectaAireAguaBombaDeCalorModoCalor()
    else:
        bDC = ExpansionDirectaAireAguaBombaDeCalorModoCalor()
    bDC.rendimientoNominalPlenaCarga = rendNominal / 100.0
    rendimientos = map((lambda x, y: x * bDC.potenciaNominal / bDC.potFcpTIntTHExt(x, 50.0, y)), nivelDeCargaDelGenerador, perfilTempHumExt)
    rendimientoEstacional = sum(map((lambda x, y: x * y), factorPonderacion, rendimientos)) * 100.0
    return (
     porcentajeEnergiaGenerador, rendimientoEstacional)


def estimacionRendimientoEstacionalBDCRefrigeracion(zona, uso, tipoGenerador, rendNominal, porcentajeDesde, porcentajeDeLaPotenciaTotalAportadoPorEsteGenerador):
    """
    Metodo: estimacionRendimientoEstacionalBDCRefrigeracion

    ARGUMENTOS:
                zona:
                uso:
                tipoGenerador:
                rendNominal:
                porcentajeDesd:
    """
    perfil = perfilesTerciario.PerfilDemandaRefrigeracion(zona, uso)
    perfilTempSecExt = perfilesTerciario.PerfilTemperaturaSecaRefrigeracion(zona, uso)
    fcpSistema = map((lambda x: x / 10.0 + 0.05), range(10))
    porcentajeHasta = porcentajeDesde + porcentajeDeLaPotenciaTotalAportadoPorEsteGenerador
    fcpGeneradoresAnteriores = []
    fcpGenerador = []
    fcpGeneradoresSiguientes = []
    for fcp in fcpSistema:
        if fcp <= porcentajeDesde:
            fcpGeneradoresAnteriores.append(fcp)
        else:
            fcpGeneradoresAnteriores.append(porcentajeDesde)
        if fcp <= porcentajeDesde:
            fcpGenerador.append(0)
        elif fcp <= porcentajeHasta:
            fcpGenerador.append(fcp - porcentajeDesde)
        else:
            fcpGenerador.append(porcentajeHasta - porcentajeDesde)
        if fcp <= porcentajeHasta:
            fcpGeneradoresSiguientes.append(0)
        else:
            fcpGeneradoresSiguientes.append(fcp - porcentajeHasta)

    porcentajeEnergiaGenerador = map((lambda x, y, z, w: y / (x + y + z) * w), fcpGeneradoresAnteriores, fcpGenerador, fcpGeneradoresSiguientes, perfil)
    nivelDeCargaDelGenerador = map((lambda x: x / porcentajeDeLaPotenciaTotalAportadoPorEsteGenerador), fcpGenerador)
    porcentajeDeLaEnergiaTotalAportadoPorEsteGenerador = sum(porcentajeEnergiaGenerador)
    factorPonderacion = map((lambda x: x / porcentajeDeLaEnergiaTotalAportadoPorEsteGenerador), porcentajeEnergiaGenerador)
    if tipoGenerador == 'Máquina frigorífica - Caudal Ref. Variable' or tipoGenerador == 'Bomba de Calor - Caudal Ref. Variable':
        bDC = VRVModoFrio()
    else:
        bDC = ExpansionDirectaAireAireBombaDeCalorModoFrio()
    bDC.rendimientoNominalPlenaCarga = rendNominal / 100.0
    fcpMod = [ x / bDC.capDisponibleTHIntTExt(17.8, y) * bDC.potenciaNominal for x, y in zip(nivelDeCargaDelGenerador, perfilTempSecExt) ]
    eir = []
    for x, y in zip(fcpMod, perfilTempSecExt):
        if x != 0:
            eir.append(bDC.potFcpTHIntTExt(x, 17.8, y) / (x * bDC.capDisponibleTHIntTExt(17.8, y)))
        else:
            eir.append(0)

    eirEstacional = sum(map((lambda x, y: x * y), factorPonderacion, eir))
    rendimientoEstacional = 1.0 / eirEstacional * 100
    return (
     porcentajeEnergiaGenerador, rendimientoEstacional)


def estimacionRendimientoEstacionalBDCRefrigeracionCondensadaAgua(zona, uso, tipoGenerador, rendNominal, porcentajeDesde, porcentajeDeLaPotenciaTotalAportadoPorEsteGenerador):
    """
    Metodo: estimacionRendimientoEstacionalBDCRefrigeracion

    ARGUMENTOS:
                zona:
                uso:
                tipoGenerador:
                rendNominal:
                porcentajeDesd:
    """
    perfil = perfilesTerciario.PerfilDemandaRefrigeracion(zona, uso)
    perfilTempHumExt = perfilesTerciario.PerfilTemperaturaHumedaRefrigeracion(zona, uso)
    fcpSistema = map((lambda x: x / 10.0 + 0.05), range(10))
    porcentajeHasta = porcentajeDesde + porcentajeDeLaPotenciaTotalAportadoPorEsteGenerador
    fcpGeneradoresAnteriores = []
    fcpGenerador = []
    fcpGeneradoresSiguientes = []
    for fcp in fcpSistema:
        if fcp <= porcentajeDesde:
            fcpGeneradoresAnteriores.append(fcp)
        else:
            fcpGeneradoresAnteriores.append(porcentajeDesde)
        if fcp <= porcentajeDesde:
            fcpGenerador.append(0)
        elif fcp <= porcentajeHasta:
            fcpGenerador.append(fcp - porcentajeDesde)
        else:
            fcpGenerador.append(porcentajeHasta - porcentajeDesde)
        if fcp <= porcentajeHasta:
            fcpGeneradoresSiguientes.append(0)
        else:
            fcpGeneradoresSiguientes.append(fcp - porcentajeHasta)

    porcentajeEnergiaGenerador = map((lambda x, y, z, w: y / (x + y + z) * w), fcpGeneradoresAnteriores, fcpGenerador, fcpGeneradoresSiguientes, perfil)
    nivelDeCargaDelGenerador = map((lambda x: x / porcentajeDeLaPotenciaTotalAportadoPorEsteGenerador), fcpGenerador)
    porcentajeDeLaEnergiaTotalAportadoPorEsteGenerador = sum(porcentajeEnergiaGenerador)
    factorPonderacion = map((lambda x: x / porcentajeDeLaEnergiaTotalAportadoPorEsteGenerador), porcentajeEnergiaGenerador)
    if tipoGenerador == 'Máquina frigorífica - Caudal Ref. Variable' or tipoGenerador == 'Bomba de Calor - Caudal Ref. Variable':
        bDC = VRVModoFrioAireAgua()
        bDC.rendimientoNominalPlenaCarga = rendNominal / 100.0
        rendimientos = map((lambda x, y: x * bDC.potenciaNominal / bDC.potFcpTHIntTExt(x, 17.8, y)), nivelDeCargaDelGenerador, perfilTempHumExt)
        rendimientoEstacional = sum(map((lambda x, y: x * y), factorPonderacion, rendimientos)) * 100.0
    else:
        bDC = ExpansionDirectaAguaAireBombaDeCalorModoFrio()
        fcpMod = [ x / bDC.capDisponibleTHIntTExt(20.0, y) * bDC.potenciaNominal for x, y in zip(nivelDeCargaDelGenerador, perfilTempHumExt) ]
        bDC.rendimientoNominalPlenaCarga = rendNominal / 100.0
        rendimientos = map((lambda x, y: x * bDC.potenciaNominal / bDC.potFcpTHIntTExt(x, 17.8, y)), fcpMod, perfilTempHumExt)
        rendimientoEstacional = sum(map((lambda x, y: x * y), factorPonderacion, rendimientos)) * 100.0
    return (
     porcentajeEnergiaGenerador, rendimientoEstacional)


if __name__ == '__main__':
    fcp = [
     0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]
    th = [8.511957625499825, 11.69508508121823, 12.573468086319114, 12.880752118936172, 
     12.907728168163771, 13.373972081576763, 13.77225983397445, 14.368949076634822, 
     14.309414881253838, 14.584647391852933]
    ti = 7.0
    bDC = ExpansionDirectaAguaAireBombaDeCalorModoFrio()
    fcpMod = [ x / bDC.capDisponibleTHIntTExt(ti, y) * bDC.potenciaNominal for x, y in zip(fcp, th) ]
    p = [ 1.625 / 100.0 * bDC.potFcpTHIntTExt(fcpMod[i], ti, th[i]) for i in range(10) ]