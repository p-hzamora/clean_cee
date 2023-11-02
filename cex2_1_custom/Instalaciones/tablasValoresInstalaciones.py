# Embedded file name: Instalaciones\tablasValoresInstalaciones.pyc
"""
Modulo: tablasValoresInstalaciones.py

"""
import math
import logging

class tablasValores:
    """
    Clase: tablasValores del modulo tablasValoresInstalaciones.py
    
    
    """

    def __init__(self, tipoInstalacion, datos, tipoGenerador, tipoIndicacion):
        """
        Constructor de la clase
        
        
        ARGUMENTOS:
                tipoInstalacion:
                datos:
                tipoGenerador:
                tipoIndicacion:
        """
        self.tipoInstalacion = tipoInstalacion
        self.datos = datos
        self.zonaClimatica = datos[-1]
        self.tipoGenerador = tipoGenerador
        self.tipoIndicacion = tipoIndicacion
        self.rendimientoEstacionalACS = ''
        self.rendimientoEstacionalCal = ''
        self.rendimientoEstacionalRef = ''
        if tipoInstalacion == u'ACS':
            if tipoGenerador == u'Caldera':
                self.rendimientoEstacionalACS = self.obtenerDatosCaldera('ACS')
            else:
                self.rendimientoEstacionalACS = self.obtenerDatosJoule('ACS')
        elif tipoInstalacion == u'calefaccion':
            if tipoGenerador == u'Caldera':
                self.rendimientoEstacionalCal = self.obtenerDatosCaldera('calefaccion')
            else:
                self.rendimientoEstacionalCal = self.obtenerDatosJoule('calefaccion')
        elif tipoInstalacion == u'refrigeracion':
            self.rendimientoEstacionalRef = self.obtenerDatosJoule('refrigeracion')
        elif tipoInstalacion == u'climatizacion':
            self.rendimientoEstacionalCal = self.obtenerDatosJoule('calefaccion')
            self.rendimientoEstacionalRef = self.obtenerDatosJoule('refrigeracion')
        elif tipoInstalacion == 'mixto2':
            if tipoGenerador == u'Caldera':
                self.rendimientoEstacionalACS = self.obtenerDatosCaldera('ACS')
                self.rendimientoEstacionalCal = self.rendimientoEstacionalACS
            else:
                self.rendimientoEstacionalACS = self.obtenerDatosJoule('ACS')
                self.rendimientoEstacionalCal = self.obtenerDatosJoule('calefaccion')
        elif tipoInstalacion == 'mixto3':
            self.rendimientoEstacionalACS = self.obtenerDatosJoule('ACS')
            self.rendimientoEstacionalCal = self.obtenerDatosJoule('calefaccion')
            self.rendimientoEstacionalRef = self.obtenerDatosJoule('refrigeracion')

    def obtenerDatosCaldera(self, tipoInstalacion):
        """
        Metodo: obtenerDatosCaldera
        El procedimiento est\xe1 basado en la norma Europea
        EN 15738 - Septiembre 2007, anejo N.5
        C\xe1lculo de los factores de p\xe9rdida.
        
        ARGUMENTOS:
                tipoInstalacion:
        """
        try:
            if self.tipoIndicacion == 'Estimado':
                equipo = self.datos[0]
                aislanteCaldera = self.datos[2]
                rendComb = float(self.datos[3])
                potencia = float(self.datos[4])
                cargaMedia = float(self.datos[5])
                vectorTipoCaldera = self.datos[6]
                if aislanteCaldera == u'Bien aislada y mantenida':
                    if equipo == u'Caldera Condensaci\xf3n':
                        c1 = 1.72
                        c2 = 0.44
                    else:
                        c1 = 3.45
                        c2 = 0.88
                elif aislanteCaldera == u'Antigua con aislamiento medio':
                    c1 = 6.9
                    c2 = 1.76
                elif aislanteCaldera == u'Antigua con mal aislamiento':
                    c1 = 8.36
                    c2 = 2.2
                else:
                    c1 = 10.35
                    c2 = 2.64
                alphaCaldera = c1 - c2 * math.log10(potencia)
                if vectorTipoCaldera[0] == True:
                    alphaChimenea = 0.2
                elif vectorTipoCaldera[1] == True:
                    alphaChimenea = 0.2
                elif vectorTipoCaldera[2] == True:
                    alphaChimenea = 0.4
                elif vectorTipoCaldera[3] == True:
                    if vectorTipoCaldera[5] == True:
                        alphaChimenea = 1.0
                    else:
                        alphaChimenea = 1.2
                elif vectorTipoCaldera[4] == True:
                    if vectorTipoCaldera[5] == True:
                        alphaChimenea = 1.2
                    else:
                        alphaChimenea = 1.6
                rendimientoEstacional = rendComb - (1 / cargaMedia - 1) * alphaChimenea - 1 / cargaMedia * alphaCaldera
                if rendimientoEstacional < 0:
                    rendimientoEstacional = 0
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            rendimientoEstacional = ''

        return rendimientoEstacional

    def obtenerDatosJoule(self, tipoInstalacion):
        """
        Metodo: obtenerDatosJoule
        
        
        ARGUMENTOS:
                tipoInstalacion:
        """
        equipo = self.datos[0]
        rendNominal = self.datos[2]
        antiguedad = self.datos[3]
        tablaCalACS = [[0.79,
          0.75,
          0.75,
          0.68,
          0.68],
         [0.79,
          0.71,
          0.71,
          0.68,
          0.68],
         [0.6,
          0.62,
          0.62,
          0.58,
          0.58],
         [1,
          1,
          1,
          1,
          1]]
        tablaRef = [[0.9,
          0.9,
          0.8,
          0.88],
         [0.83,
          0.83,
          0.71,
          0.78],
         [0.54,
          0.54,
          0.66,
          0.75],
         [1,
          1,
          1,
          1]]
        if tipoInstalacion == 'ACS' or tipoInstalacion == 'calefaccion':
            if equipo == u'Bomba de Calor Bloque' or equipo == u'Centralizado Bloque':
                eq = 0
            elif equipo == u'Bomba de Calor Vivienda' or equipo == u'Centralizado Vivienda':
                eq = 1
            elif equipo == u'Bomba de Calor Equipo Individual' or equipo == u'Individual':
                eq = 2
            else:
                eq = 3
            if 'A' in self.zonaClimatica or 'alpha' in self.zonaClimatica:
                aux = 0
            elif 'B' in self.zonaClimatica:
                aux = 1
            elif 'C' in self.zonaClimatica:
                aux = 2
            elif 'D' in self.zonaClimatica:
                aux = 3
            else:
                aux = 4
            coefPaso = tablaCalACS[eq][aux]
        elif tipoInstalacion == 'refrigeracion':
            if equipo == u'Centralizado Bloque':
                eq = 0
            elif equipo == u'Centralizado Vivienda':
                eq = 1
            elif equipo == u'Individual':
                eq = 2
            else:
                eq = 3
            if '1' in self.zonaClimatica:
                aux = 0
            elif '2' in self.zonaClimatica:
                aux = 1
            elif '3' in self.zonaClimatica:
                aux = 2
            else:
                aux = 3
            coefPaso = tablaRef[eq][aux]
        if antiguedad == '-5':
            coefAntiguedad = 0
        elif antiguedad == '5-15':
            coefAntiguedad = 0.1
        else:
            coefAntiguedad = 0.15
        rendimientoEstacional = float(rendNominal) * coefPaso * (1 - coefAntiguedad)
        return rendimientoEstacional