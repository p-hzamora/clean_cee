# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\objetosEnvolvente.pyc
# Compiled at: 2014-12-21 23:41:37
"""
Modulo: objetosEnvolvente.py

"""
import Envolvente.tablasValores as tablasValores

class Hueco:
    """
    Clase: Hueco del modulo objetosEnvolvente.py

    """

    def __init__(self, datosHueco):
        """
        Constructor de la clase

        ARGUMENTOS:
                datosHueco:
        """
        self.descripcion = datosHueco[0]
        self.tipo = datosHueco[1]
        self.superficie = datosHueco[2]
        self.Uvidrio = 0.0
        self.Gvidrio = 0.0
        self.Umarco = 0.0
        self.orientacion = datosHueco[3]
        self.porcMarco = datosHueco[4]
        self.correctorFSCTE = datosHueco[5][0]
        self.correctorFSInvierno = datosHueco[5][1]
        self.correctorFSVerano = datosHueco[5][2]
        self.cerramientoAsociado = datosHueco[6]
        self.permeabilidadChoice = datosHueco[7]
        self.permeabilidadValor = datosHueco[8]
        self.absortividadValor = datosHueco[9]
        self.absortividadPosiciones = datosHueco[10]
        self.tieneProteccionSolar = datosHueco[11]
        self.elementosProteccionSolar = datosHueco[12]
        self.patronSombras = datosHueco[13]
        self.dobleVentana = datosHueco[14]
        self.longitud = datosHueco[15]
        self.altura = datosHueco[16]
        self.multiplicador = datosHueco[17]
        self.subgrupo = datosHueco[-1]

    def calculoUhueco(self):
        Uhueco = float(self.Uvidrio) * (1.0 - float(self.porcMarco) / 100.0) + float(self.Umarco) * float(self.porcMarco) / 100.0
        return Uhueco

    def calculoFShueco(self):
        FShueco = float(self.correctorFSCTE) * (float(self.Gvidrio) * (1.0 - float(self.porcMarco) / 100.0) + 0.04 * float(self.Umarco) * float(self.absortividadValor) * float(self.porcMarco) / 100.0)
        return FShueco


class HuecoConocidas(Hueco):
    """
    Clase: HuecoConocidas del modulo objetosEnvolvente.py

    """

    def __init__(self, datosHueco):
        """
        Constructor de la clase

        ARGUMENTOS:
                datosHueco:
        """
        Hueco.__init__(self, datosHueco)
        self.__tipo__ = 'HuecoConocidas'
        self.vidrioSeleccionado = datosHueco[18]
        self.marcoSeleccionado = datosHueco[19]
        self.UvidrioConocido = datosHueco[20]
        self.GvidrioConocido = datosHueco[21]
        self.UmarcoConocido = datosHueco[22]
        self.calculoPropiedadesTermicas()

    def calculoPropiedadesTermicas(self):
        """
        Metodo: calculoPropiedadesTermicas

                self):#CONOCI:
        """
        if float(self.porcMarco) < 100.0:
            self.Uvidrio = float(self.UvidrioConocido)
            self.Gvidrio = float(self.GvidrioConocido)
        self.Umarco = float(self.UmarcoConocido)
        if self.dobleVentana == True:
            if float(self.porcMarco) < 100.0:
                self.Uvidrio = 1.0 / (1.0 / float(self.UvidrioConocido) + 0.18)
                self.Gvidrio = float(self.GvidrioConocido) * 0.82
            self.Umarco = 1.0 / (1.0 / float(self.UmarcoConocido) + 0.18)


class HuecoEstimadas(Hueco):
    """
    Clase: HuecoEstimadas del modulo objetosEnvolvente.py

    """

    def __init__(self, datosHueco):
        """
        Constructor de la clase

        ARGUMENTOS:
                datosHueco:
        """
        Hueco.__init__(self, datosHueco)
        self.__tipo__ = 'HuecoEstimadas'
        self.tipoVidrio = datosHueco[23]
        self.tipoMarco = datosHueco[24]
        self.calculoPropiedadesTermicas()

    def calculoPropiedadesTermicas(self):
        """
        Metodo: calculoPropiedadesTermicas

                self):#ESTIMA:
        """
        caracteristicasHuecos = tablasValores.tablasValores('Hueco', None, [self.tipoVidrio, self.tipoMarco], None)
        if float(self.porcMarco) < 100.0:
            self.Uvidrio = caracteristicasHuecos.UCerramiento
            self.Gvidrio = caracteristicasHuecos.FSHueco
        else:
            self.Uvidrio = 0.0
            self.Gvidrio = 0.0
        self.Umarco = caracteristicasHuecos.UMarco
        if self.dobleVentana == True:
            if float(self.porcMarco) < 100.0:
                self.Uvidrio = 1.0 / (1.0 / self.Uvidrio + 0.18)
                self.Gvidrio = self.Gvidrio * 0.82
            self.Umarco = 1.0 / (1.0 / self.Umarco + 0.18)
        return