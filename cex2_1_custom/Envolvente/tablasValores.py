# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\tablasValores.pyc
# Compiled at: 2015-05-29 10:09:47
"""
Modulo: tablasValores.py

"""
import math, wx, Calculos.funcionFactorSombra as funcionFactorSombra, logging

class tablasValores():
    """
    Clase: tablasValores del modulo tablasValores.py

    """

    def __init__(self, tipoCerramiento, posicion, datos, tipoIndicacion):
        """
        Constructor de la clase

        ARGUMENTOS:
                tipoCerramiento:
                posicion:
                datos:
                tipoIndicacion:
        """
        self.tipoCerramiento = tipoCerramiento
        self.posicion = posicion
        self.datos = datos
        self.tipoIndicacion = tipoIndicacion
        self.UCerramiento = ''
        self.densidadCerramiento = ''
        self.FSHueco = ''
        self.UMarco = ''
        self.fi = ''
        if tipoCerramiento == 'Hueco':
            self.obtenerDatosHuecos()
        elif tipoCerramiento == 'PT':
            self.obtenerPT()
        elif tipoCerramiento == 'PTMedidasMejora':
            self.obtenerPTMedidasMejora()
        elif tipoCerramiento == 'Cubierta' and posicion == 'terreno':
            self.obtenerDatosCubiertaTerreno()
        elif tipoCerramiento == 'Cubierta' and posicion == 'aire':
            self.obtenerDatosCubiertaAire()
        elif tipoCerramiento == 'Fachada' and posicion == 'terreno':
            self.obtenerDatosFachadaTerreno()
        elif tipoCerramiento == 'Fachada' and posicion == 'aire':
            self.obtenerDatosFachadaAire()
        elif tipoCerramiento == 'Suelo' and posicion == 'terreno':
            self.obtenerDatosSueloTerreno()
        elif tipoCerramiento == 'Suelo' and posicion == 'aire':
            self.obtenerDatosSueloAire()
        elif tipoCerramiento == 'Particion' and posicion == 'Vertical':
            self.obtenerDatosParticionVertical()
        elif tipoCerramiento == 'Particion' and posicion == 'HorizontalSuperiorBajoCubierta':
            self.obtenerDatosParticionHorizontalBajoCubierta()
        elif tipoCerramiento == 'Particion' and posicion == 'HorizontalSuperiorOtro':
            self.obtenerDatosParticionHorizontalOtro()
        elif tipoCerramiento == 'Particion' and posicion == 'HorizontalInferior':
            self.obtenerDatosParticionHorizontalInferior()
        elif tipoCerramiento == 'Particion' and posicion == 'CamaraSanitaria':
            self.obtenerDatosCamaraSanitaria()

    def obtenerDatosHuecos(self):
        """
        Metodo: obtenerDatosHuecos

        """
        diccTipoVidrio = {'Simple': [5.7, 0.82], 'Doble': [
                   3.3, 0.75], 
           'Doble bajo emisivo': [
                                2.7, 0.65]}
        diccTipoMarco = {'Metálico sin RPT': 5.7, 'Metálico con RPT': 4.0, 
           'PVC': 2.2, 
           'Madera': 2.2}
        tipoVidrio = self.datos[0]
        tipoMarco = self.datos[1]
        try:
            self.UCerramiento = diccTipoVidrio[tipoVidrio][0]
        except:
            logging.info('Excepcion en: %s' % __name__)
            self.UCerramiento = ''

        try:
            self.FSHueco = diccTipoVidrio[tipoVidrio][1]
        except:
            logging.info('Excepcion en: %s' % __name__)
            self.FSHueco = ''

        try:
            self.UMarco = diccTipoMarco[tipoMarco]
        except:
            logging.info('Excepcion en: %s' % __name__)
            self.UMarco = ''

    def obtenerPT(self):
        """
        Metodo: obtenerPT

        """
        tipoPT = self.datos[0]
        norma = self.datos[1]
        cerramiento = self.datos[2]
        diccDefecto = {'Pilar integrado en fachada': [1.05, 1.05, 1.05, 1.05], 'Pilar en Esquina': [
                              0.78, 0.78, 0.54, 0.54], 
           'Contorno de hueco': [
                               0.55, 0.55, 0.17, 0.17], 
           'Caja de Persiana': [
                              1.49, 1.49, 0.39, 0.39], 
           'Encuentro de fachada con forjado': [
                                              1.58, 1.58, 1.31, 1.31], 
           'Encuentro de fachada con cubierta': [
                                               0.49, 1.04, 0.82, 0.82], 
           'Encuentro de fachada con suelo en contacto con el aire': [
                                                                    0.37, 0.97, 0.66, 0.66], 
           'Encuentro de fachada con solera': [
                                             0.14, 0.14, 0.14, 0.14]}
        diccEstimado_anterior = {'Pilar integrado en fachada': ['False', 0.81, 0.81, 1.05, 'False', 0.01], 'Pilar en Esquina': [
                              'False', 
                              0.6, 0.6, 0.78, 'False', 
                              0.16], 
           'Contorno de hueco': [
                               0.72, 
                               0.33, 0.33, 0.55, 
                               0.49, 0.02], 
           'Caja de Persiana': [
                              0.67, 
                              1.69, 1.69, 1.49, 
                              0.4, 0.65], 
           'Encuentro de fachada con forjado': [
                                              0.98, 
                                              1.51, 
                                              1.51, 
                                              1.58, 
                                              1.17, 
                                              0.16], 
           'Encuentro de fachada con cubierta': [
                                               0.49], 
           'Encuentro de fachada con suelo en contacto con el aire': [
                                                                    0.37], 
           'Encuentro de fachada con solera': [
                                             0.14]}
        diccEstimado_nbe = {'Pilar integrado en fachada': ['False', 1.05, 1.05, 1.05, 'False', 0.01], 'Pilar en Esquina': [
                              'False', 
                              0.78, 0.78, 0.78, 
                              'False', 0.16], 
           'Contorno de hueco': [
                               1.07, 
                               0.55, 0.55, 0.55, 
                               0.72, 0.02], 
           'Caja de Persiana': [
                              0.25, 
                              1.49, 1.49, 1.49, 
                              0.67, 0.65], 
           'Encuentro de fachada con forjado': [
                                              1.21, 
                                              1.58, 
                                              1.58, 
                                              1.58, 
                                              1.28, 
                                              0.16], 
           'Encuentro de fachada con cubierta': [
                                               1.04], 
           'Encuentro de fachada con suelo en contacto con el aire': [
                                                                    0.97], 
           'Encuentro de fachada con solera': [
                                             0.14]}
        diccEstimado_cte = {'Pilar integrado en fachada': ['False', 0.96, 1.05, 1.05, 'False', 0.01], 'Pilar en Esquina': [
                              'False', 
                              0.43, 0.54, 0.54, 
                              'False', 0.16], 
           'Contorno de hueco': [
                               0.02, 
                               0.02, 0.17, 0.17, 
                               0.02, 0.02], 
           'Caja de Persiana': [
                              0.25, 
                              0.53, 0.39, 0.39, 
                              0.24, 0.65], 
           'Encuentro de fachada con forjado': [
                                              1.2, 
                                              1.3, 
                                              1.31, 
                                              1.31, 
                                              1.19, 
                                              0.16], 
           'Encuentro de fachada con cubierta': [
                                               0.82], 
           'Encuentro de fachada con suelo en contacto con el aire': [
                                                                    0.66], 
           'Encuentro de fachada con solera': [
                                             0.14]}
        if 'Por defecto' in cerramiento[8] or 'Conocidas' in cerramiento[8]:
            if cerramiento[1] == 'Suelo' and (cerramiento[-1] == 'aire' and tipoPT != 'Encuentro de fachada con suelo en contacto con el aire' or cerramiento[-1] == 'terreno' and tipoPT != 'Encuentro de fachada con solera'):
                self.fi = ''
            elif cerramiento[1] == 'Cubierta' and (cerramiento[-1] != 'aire' or tipoPT not in ('Encuentro de fachada con cubierta',
                                                                                               'Contorno de hueco')):
                self.fi = ''
            else:
                if cerramiento[1] == 'Fachada' and (cerramiento[-1] != 'aire' or tipoPT not in ('Pilar integrado en fachada',
                                                                                                'Pilar en Esquina',
                                                                                                'Contorno de hueco',
                                                                                                'Caja de Persiana',
                                                                                                'Encuentro de fachada con forjado')):
                    self.fi = ''
                else:
                    try:
                        self.fi = diccDefecto[tipoPT][norma]
                    except:
                        logging.info('Excepcion en: %s' % __name__)
                        self.fi = ''

        elif 'Estimadas' in cerramiento[8]:
            if cerramiento[1] == 'Suelo' and (cerramiento[-1] == 'aire' and tipoPT != 'Encuentro de fachada con suelo en contacto con el aire' or cerramiento[-1] == 'terreno' and tipoPT != 'Encuentro de fachada con solera'):
                self.fi = ''
            elif cerramiento[1] == 'Cubierta' and (cerramiento[-1] != 'aire' or tipoPT not in ('Encuentro de fachada con cubierta',
                                                                                               'Contorno de hueco')):
                self.fi = ''
            elif cerramiento[1] == 'Fachada' and (cerramiento[-1] != 'aire' or tipoPT not in ('Pilar integrado en fachada',
                                                                                              'Pilar en Esquina',
                                                                                              'Contorno de hueco',
                                                                                              'Caja de Persiana',
                                                                                              'Encuentro de fachada con forjado')):
                self.fi = ''
            elif cerramiento[1] != 'Fachada':
                contador = 0
            else:
                if cerramiento[9][0] == 'Una hoja':
                    if cerramiento[9][2] == True and cerramiento[9][9] == 'Por el exterior':
                        contador = 5
                    else:
                        if cerramiento[9][8] == 'Muro de piedra' or cerramiento[9][8] == 'Muro de adobe/tapial':
                            contador = 0
                        else:
                            if cerramiento[9][8] == 'Fábrica de bloques de picón' or cerramiento[9][8] == 'Fábrica de bloques de hormigón' or cerramiento[9][8] == '1/2 pie de fábrica de ladrillo':
                                contador = 1
                            elif cerramiento[9][8] == '1 pie de fábrica de ladrillo':
                                contador = 4
                elif cerramiento[9][0] == 'Doble hoja con cámara':
                    if cerramiento[9][1] == 'No ventilada' or cerramiento[9][1] == 'Ligeramente ventilada':
                        contador = 2
                    else:
                        if cerramiento[9][1] == 'Rellena de Aislamiento':
                            contador = 3
                        else:
                            contador = 5
                else:
                    contador = 5
                try:
                    if norma == 0:
                        dicc = diccEstimado_anterior
                    elif norma == 1:
                        dicc = diccEstimado_nbe
                    else:
                        dicc = diccEstimado_cte
                    self.fi = dicc[tipoPT][contador]
                except:
                    logging.info('Excepcion en: %s' % __name__)
                    self.fi = ''

    def obtenerPTMedidasMejora(self):
        """
        Metodo: obtenerPTMedidasMejora

                self):   ###Cuando tengo aislamiento por el exteri:
        """
        diccAislamientoExterior = {'Pilar integrado en fachada': [0.01], 'Pilar en Esquina': [
                              0.16], 
           'Contorno de hueco': [
                               0.02], 
           'Caja de Persiana': [
                              0.65], 
           'Encuentro de fachada con forjado': [
                                              0.16], 
           'Encuentro de fachada con cubierta': [
                                               0.26], 
           'Encuentro de fachada con suelo en contacto con el aire': [
                                                                    0.22]}
        tipoPT = self.datos[0]
        self.fi = diccAislamientoExterior[tipoPT][0]

    def obtenerDatosCubiertaTerreno(self):
        """
        Metodo: obtenerDatosCubiertaTerreno

        """
        if self.tipoIndicacion == 'Estimado':
            datosAislamiento = self.datos[0]
            Rais = ''
            if len(datosAislamiento) == 1:
                if datosAislamiento[0] == 'SinAislamiento':
                    Rais = 0.03
                else:
                    Rais = float(datosAislamiento[0])
            else:
                if datosAislamiento[0] == 'EPS':
                    conduct = 0.046
                    espesor = float(datosAislamiento[1])
                elif datosAislamiento[0] == 'XPS':
                    conduct = 0.039
                    espesor = float(datosAislamiento[1])
                elif datosAislamiento[0] == 'MW':
                    conduct = 0.05
                    espesor = float(datosAislamiento[1])
                elif datosAislamiento[0] == 'PUR':
                    conduct = 0.04
                    espesor = float(datosAislamiento[1])
                elif datosAislamiento[0] == 'Otro':
                    conduct = float(datosAislamiento[2])
                    espesor = float(datosAislamiento[1])
                Rais = espesor / conduct
            Rtotal = Rais
            try:
                self.UCerramiento = 1.0 / Rtotal
            except ZeroDivisionError:
                self.UCerramiento = 100000000.0

            self.densidadCerramiento = 400.0
        elif self.tipoIndicacion == 'Por defecto':
            norma = self.datos[0]
            HE1 = self.datos[1]
            diccCubiertaTerrenoPorDefecto = {0: 1.0, 1: 1.0, 
               2: {'alpha': 0.94, 'A': 0.94, 'B': 0.82, 'C': 0.73, 'D': 0.66, 'E': 0.57}, 3: {'alpha': 0.94, 'A': 0.5, 'B': 0.38, 'C': 0.29, 'D': 0.27, 'E': 0.25}}
            if norma == 0 or norma == 1:
                self.UCerramiento = diccCubiertaTerrenoPorDefecto[norma]
            elif norma == 2 or norma == 3:
                zonaAux = HE1[0:-1]
                self.UCerramiento = diccCubiertaTerrenoPorDefecto[norma][zonaAux]
            self.densidadCerramiento = 400

    def obtenerDatosCubiertaAire(self):
        """
        Metodo: obtenerDatosCubiertaAire

        """
        if self.tipoIndicacion == 'Estimado':
            tipoCubierta = self.datos[0]
            tipoForjado = self.datos[1]
            tipoCamara = self.datos[2]
            tieneAislamiento = self.datos[3]
            if tipoCubierta == 'Cubierta plana':
                if tipoForjado == 'Unidireccional':
                    Rcerr = 0.3
                    self.densidadCerramiento = 360
                else:
                    if tipoForjado == 'Reticular':
                        Rcerr = 0.24
                        self.densidadCerramiento = 375
                    else:
                        if tipoForjado == 'Losa':
                            Rcerr = 0.17
                            self.densidadCerramiento = 500
                        elif tipoForjado == 'Casetones recuperables':
                            Rcerr = 0.17
                            self.densidadCerramiento = 344
            elif tipoCubierta == 'Cubierta plana ventilada':
                if tipoCamara == 'Ligeramente ventilada':
                    if tipoForjado == 'Unidireccional':
                        Rcerr = 0.54
                        self.densidadCerramiento = 360
                    else:
                        if tipoForjado == 'Reticular':
                            Rcerr = 0.48
                            self.densidadCerramiento = 375
                        else:
                            if tipoForjado == 'Losa':
                                Rcerr = 0.41
                                self.densidadCerramiento = 500
                            elif tipoForjado == 'Casetones recuperables':
                                Rcerr = 0.41
                                self.densidadCerramiento = 344
                elif tipoCamara == 'Ventilada':
                    if tipoForjado == 'Unidireccional':
                        Rcerr = 0.41
                        self.densidadCerramiento = 360
                    else:
                        if tipoForjado == 'Reticular':
                            Rcerr = 0.34
                            self.densidadCerramiento = 375
                        else:
                            if tipoForjado == 'Losa':
                                Rcerr = 0.27
                                self.densidadCerramiento = 500
                            elif tipoForjado == 'Casetones recuperables':
                                Rcerr = 0.27
                                self.densidadCerramiento = 344
            elif tipoCubierta == 'Cubierta ajardinada':
                Rcerr = 0.74
                self.densidadCerramiento = 400
            elif tipoCubierta == 'Cubierta inclinada':
                if tipoForjado == 'Unidireccional':
                    Rcerr = 0.25
                    self.densidadCerramiento = 360
                elif tipoForjado == 'Losa':
                    Rcerr = 0.1
                    self.densidadCerramiento = 500
                else:
                    Rcerr = 0.23
                    self.densidadCerramiento = 180
            elif tipoCubierta == 'Cubierta inclinada ventilada':
                if tipoCamara == 'Ligeramente ventilada':
                    if tipoForjado == 'Unidireccional':
                        Rcerr = 0.33
                        self.densidadCerramiento = 360
                    elif tipoForjado == 'Losa':
                        Rcerr = 0.22
                        self.densidadCerramiento = 500
                elif tipoCamara == 'Ventilada':
                    if tipoForjado == 'Unidireccional':
                        Rcerr = 0.24
                        self.densidadCerramiento = 360
                    elif tipoForjado == 'Losa':
                        Rcerr = 0.12
                        self.densidadCerramiento = 500
            if tieneAislamiento == False:
                Rais = 0
            else:
                datosAislamiento = self.datos[4]
                Rais = ''
                if len(datosAislamiento) == 1:
                    Rais = float(datosAislamiento[0])
                else:
                    if datosAislamiento[0] == 'EPS':
                        conduct = 0.046
                        espesor = float(datosAislamiento[1])
                    elif datosAislamiento[0] == 'XPS':
                        conduct = 0.039
                        espesor = float(datosAislamiento[1])
                    elif datosAislamiento[0] == 'MW':
                        conduct = 0.05
                        espesor = float(datosAislamiento[1])
                    elif datosAislamiento[0] == 'PUR':
                        conduct = 0.04
                        espesor = float(datosAislamiento[1])
                    elif datosAislamiento[0] == 'Otro':
                        conduct = float(datosAislamiento[2])
                        espesor = float(datosAislamiento[1])
                    else:
                        conduct = 0.05
                        espesor = 0.01
                    Rais = espesor / conduct
            Rtotal = Rcerr + Rais
            self.UCerramiento = 1.0 / Rtotal
        if self.tipoIndicacion == 'Por defecto':
            norma = self.datos[0]
            HE1 = self.datos[1]
            NBE = self.datos[2]
            posicionCubierta = self.datos[3]
            if norma == 0:
                if posicionCubierta == 'Cubierta plana':
                    self.densidadCerramiento = 344
                else:
                    self.densidadCerramiento = 180
            else:
                self.densidadCerramiento = 344
            diccCubiertaAirePorDefecto = {0: {'Cubierta plana': 2.17, 'Cubierta inclinada': 2.63}, 1: {'V': 1.4, 'W': 1.4, 'X': 1.2, 'Y': 0.9, 'Z': 0.7}, 2: {'alpha': 0.5, 'A': 0.5, 'B': 0.45, 'C': 0.41, 'D': 0.38, 'E': 0.35}, 3: {'alpha': 0.5, 'A': 0.47, 'B': 0.33, 'C': 0.23, 'D': 0.22, 'E': 0.19}}
            if norma == 0:
                self.UCerramiento = diccCubiertaAirePorDefecto[norma][posicionCubierta]
            else:
                if norma == 1:
                    self.UCerramiento = diccCubiertaAirePorDefecto[norma][NBE]
                elif norma == 2 or norma == 3:
                    zonaAux = HE1[0:-1]
                    self.UCerramiento = diccCubiertaAirePorDefecto[norma][zonaAux]

    def obtenerDatosFachadaTerreno(self):
        """
        Metodo: obtenerDatosFachadaTerreno

        """
        if self.tipoIndicacion == 'Estimado':
            tieneAislamiento = self.datos[0]
            if tieneAislamiento == False:
                Rais = 0.12
            else:
                Rais = ''
                datosAislamiento = self.datos[1]
                if len(datosAislamiento) == 1:
                    Rais = float(datosAislamiento[0])
                else:
                    if datosAislamiento[0] == 'EPS':
                        conduct = 0.046
                        espesor = float(datosAislamiento[1])
                    elif datosAislamiento[0] == 'XPS':
                        conduct = 0.039
                        espesor = float(datosAislamiento[1])
                    elif datosAislamiento[0] == 'MW':
                        conduct = 0.05
                        espesor = float(datosAislamiento[1])
                    elif datosAislamiento[0] == 'PUR':
                        conduct = 0.04
                        espesor = float(datosAislamiento[1])
                    elif datosAislamiento[0] == 'Otro':
                        conduct = float(datosAislamiento[2])
                        espesor = float(datosAislamiento[1])
                    Rais = espesor / conduct
            Rtotal = Rais
            try:
                self.UCerramiento = 1.0 / Rtotal
            except ZeroDivisionError:
                self.UCerramiento = 100000000.0

            self.densidadCerramiento = 200
        if self.tipoIndicacion == 'Por defecto':
            norma = self.datos[0]
            HE1 = self.datos[1]
            diccFachadaTerrenoPorDefecto = {0: 2.0, 1: 2.0, 
               2: {'alpha': 0.94, 'A': 0.94, 'B': 0.82, 'C': 0.73, 'D': 0.66, 'E': 0.57}, 3: {'alpha': 0.94, 'A': 0.5, 'B': 0.38, 'C': 0.29, 'D': 0.27, 'E': 0.25}}
            if norma == 0 or norma == 1:
                self.UCerramiento = diccFachadaTerrenoPorDefecto[norma]
            elif norma == 2 or norma == 3:
                zonaAux = HE1[0:-1]
                self.UCerramiento = diccFachadaTerrenoPorDefecto[norma][zonaAux]
            self.densidadCerramiento = 200.0

    def obtenerDatosFachadaAire(self):
        """
        Metodo: obtenerDatosFachadaAire

        """
        if self.tipoIndicacion == 'Estimado':
            tipoFachada = self.datos[0]
            datos = self.datos[1]
            tieneAislamiento = self.datos[2]
            if tipoFachada == 'Doble hoja con cámara':
                if datos == 'No ventilada':
                    Rcerr = 0.42
                elif datos == 'Ligeramente ventilada':
                    Rcerr = 0.33
                elif datos == 'Ventilada':
                    Rcerr = 0.15
                else:
                    Rcerr = 0.25
                self.densidadCerramiento = 200
            elif tipoFachada == 'Una hoja':
                if datos == '1/2 pie de fábrica de ladrillo':
                    Rcerr = 0.25
                    self.densidadCerramiento = 191
                elif datos == '1 pie de fábrica de ladrillo':
                    Rcerr = 0.42
                    self.densidadCerramiento = 343
                elif datos == 'Fábrica de bloques de hormigón':
                    Rcerr = 0.22
                    self.densidadCerramiento = 168
                elif datos == 'Fábrica de bloques de picón':
                    Rcerr = 0.42
                    self.densidadCerramiento = 180
                elif datos == 'Muro de piedra':
                    Rcerr = 0.17
                    self.densidadCerramiento = 920
                else:
                    Rcerr = 0.36
                    self.densidadCerramiento = 680
            else:
                Rcerr = 0.21
                self.densidadCerramiento = 200
            if tieneAislamiento == False:
                Rais = 0
            else:
                datosAislamiento = self.datos[3]
                Rais = ''
                if len(datosAislamiento) == 1:
                    Rais = float(datosAislamiento[0])
                else:
                    if datosAislamiento[0] == 'EPS':
                        conduct = 0.046
                        espesor = float(datosAislamiento[1])
                    elif datosAislamiento[0] == 'XPS':
                        conduct = 0.039
                        espesor = float(datosAislamiento[1])
                    elif datosAislamiento[0] == 'MW':
                        conduct = 0.05
                        espesor = float(datosAislamiento[1])
                    elif datosAislamiento[0] == 'PUR':
                        conduct = 0.04
                        espesor = float(datosAislamiento[1])
                    else:
                        conduct = float(datosAislamiento[2])
                        espesor = float(datosAislamiento[1])
                    Rais = espesor / conduct
            Rtotal = Rcerr + Rais
            self.UCerramiento = 1.0 / Rtotal
        if self.tipoIndicacion == 'Por defecto':
            norma = self.datos[0]
            HE1 = self.datos[1]
            NBE = self.datos[2]
            if norma == 0:
                self.densidadCerramiento = 168.0
            else:
                self.densidadCerramiento = 200.0
            diccFachadaAirePorDefecto = {0: 2.38, 1: {'V': 1.8, 'W': 1.8, 'X': 1.6, 'Y': 1.4, 'Z': 1.4}, 2: {'alpha': 0.94, 'A': 0.94, 'B': 0.82, 'C': 0.73, 'D': 0.66, 'E': 0.57}, 3: {'alpha': 0.94, 'A': 0.5, 'B': 0.38, 'C': 0.29, 'D': 0.27, 'E': 0.25}}
            if norma == 0:
                self.UCerramiento = diccFachadaAirePorDefecto[norma]
            else:
                if norma == 1:
                    self.UCerramiento = diccFachadaAirePorDefecto[norma][NBE]
                elif norma == 2 or norma == 3:
                    zonaAux = HE1[0:-1]
                    self.UCerramiento = diccFachadaAirePorDefecto[norma][zonaAux]

    def obtenerDatosSueloAire(self):
        """
        Metodo: obtenerDatosSueloAire

        """
        if self.tipoIndicacion == 'Estimado':
            tipoForjado = self.datos[0]
            entreVigado = self.datos[1]
            tieneAislamiento = self.datos[2]
            if tipoForjado == 'Unidireccional':
                if entreVigado == 'Cerámicas':
                    Rcerr = 0.32
                    self.densidadCerramiento = 333
                else:
                    Rcerr = 0.21
                    self.densidadCerramiento = 372
            elif tipoForjado == 'Reticular':
                if entreVigado == 'Cerámicas':
                    Rcerr = 0.18
                    self.densidadCerramiento = 365
                elif entreVigado == 'De Hormigón':
                    Rcerr = 0.15
                    self.densidadCerramiento = 385
                else:
                    Rcerr = 0.07
                    self.densidadCerramiento = 344
            elif tipoForjado == 'Losa':
                Rcerr = 0.12
                self.densidadCerramiento = 750
            elif tipoForjado == 'De Madera':
                Rcerr = 0.26
                self.densidadCerramiento = 34.2
            if tieneAislamiento == False:
                Rais = 0
            else:
                datosAislamiento = self.datos[3]
                Rais = ''
                if len(datosAislamiento) == 1:
                    Rais = float(datosAislamiento[0])
                else:
                    if datosAislamiento[0] == 'EPS':
                        conduct = 0.046
                        espesor = float(datosAislamiento[1])
                    elif datosAislamiento[0] == 'XPS':
                        conduct = 0.039
                        espesor = float(datosAislamiento[1])
                    elif datosAislamiento[0] == 'MW':
                        conduct = 0.05
                        espesor = float(datosAislamiento[1])
                    elif datosAislamiento[0] == 'PUR':
                        conduct = 0.04
                        espesor = float(datosAislamiento[1])
                    elif datosAislamiento[0] == 'Otro':
                        conduct = float(datosAislamiento[2])
                        espesor = float(datosAislamiento[1])
                    else:
                        conduct = 0.05
                        espesor = 0.01
                    Rais = espesor / conduct
            Rtotal = Rcerr + Rais
            self.UCerramiento = 1.0 / Rtotal
        if self.tipoIndicacion == 'Por defecto':
            norma = self.datos[0]
            HE1 = self.datos[1]
            NBE = self.datos[2]
            if norma == 0:
                self.densidadCerramiento = 50
            else:
                self.densidadCerramiento = 333
            diccSueloAirePorDefecto = {0: 2.5, 1: {'V': 1.0, 'W': 1.0, 'X': 0.9, 'Y': 0.8, 'Z': 0.7}, 2: {'alpha': 0.53, 'A': 0.53, 'B': 0.52, 'C': 0.5, 'D': 0.49, 'E': 0.48}, 3: {'alpha': 0.53, 'A': 0.53, 'B': 0.46, 'C': 0.36, 'D': 0.34, 'E': 0.31}}
            if norma == 0:
                self.UCerramiento = diccSueloAirePorDefecto[norma]
            else:
                if norma == 1:
                    self.UCerramiento = diccSueloAirePorDefecto[norma][NBE]
                elif norma == 2 or norma == 3:
                    zonaAux = HE1[0:-1]
                    self.UCerramiento = diccSueloAirePorDefecto[norma][zonaAux]

    def obtenerDatosSueloTerreno(self):
        """
        Metodo: obtenerDatosSueloTerreno

        """
        if self.tipoIndicacion == 'Por defecto':
            norma = self.datos[0]
            HE1 = self.datos[1]
            profundidad = self.datos[2]
            diccSueloTerrenoMenos05PorDefecto = {0: 1.0, 1: 1.0, 
               2: {'alpha': 0.94, 'A': 0.94, 'B': 0.82, 'C': 0.73, 'D': 0.66, 'E': 0.57}, 3: {'alpha': 0.94, 'A': 0.5, 'B': 0.38, 'C': 0.29, 'D': 0.27, 'E': 0.25}}
            diccSueloTerrenoMas05PorDefecto = {0: 1.0, 1: 1.0, 
               2: {'alpha': 0.94, 'A': 0.94, 'B': 0.82, 'C': 0.73, 'D': 0.66, 'E': 0.57}, 3: {'alpha': 0.94, 'A': 0.5, 'B': 0.38, 'C': 0.29, 'D': 0.27, 'E': 0.25}}
            if profundidad == '-0.5':
                dicc = diccSueloTerrenoMenos05PorDefecto
            else:
                dicc = diccSueloTerrenoMas05PorDefecto
            if norma == 0:
                self.UCerramiento = dicc[norma]
            elif norma == 1:
                self.UCerramiento = dicc[norma]
            elif norma == 2 or norma == 3:
                zonaAux = HE1[0:-1]
                self.UCerramiento = dicc[norma][zonaAux]
            self.densidadCerramiento = 750

    def obtenerDatosParticionVertical(self):
        """
        Metodo: obtenerDatosParticionVertical

        """
        if self.tipoIndicacion == 'Estimado':
            norma = self.datos[0]
            HE1 = self.datos[1]
            NBE = self.datos[2]
            tieneAislamiento = self.datos[3]
            if tieneAislamiento == True:
                if norma == 0:
                    self.UCerramiento = 1.2
                else:
                    if norma == 1:
                        self.UCerramiento = 1.2
                    else:
                        if 'A' in HE1 or 'alpha' in HE1:
                            self.UCerramiento = 1.2
                        else:
                            if 'B' in HE1:
                                self.UCerramiento = 1.17
                            else:
                                if 'C' in HE1:
                                    self.UCerramiento = 1.04
                                else:
                                    if 'D' in HE1:
                                        self.UCerramiento = 0.94
                                    elif 'E' in HE1:
                                        self.UCerramiento = 0.81
            elif norma == 0:
                self.UCerramiento = 2.5
            elif norma == 1:
                if NBE == 'V' or NBE == 'W':
                    self.UCerramiento = 2.0
                elif NBE == 'X':
                    self.UCerramiento = 1.8
                else:
                    if NBE == 'Y':
                        self.UCerramiento = 1.6
                    else:
                        self.UCerramiento = 1.6
            elif 'A' in HE1 or 'alpha' in HE1:
                self.UCerramiento = 1.34
            elif 'B' in HE1:
                self.UCerramiento = 1.17
            elif 'C' in HE1:
                self.UCerramiento = 1.04
            elif 'D' in HE1:
                self.UCerramiento = 0.94
            elif 'E' in HE1:
                self.UCerramiento = 0.81
            self.densidadCerramiento = 60
        if self.tipoIndicacion == 'Por defecto':
            norma = self.datos[0]
            HE1 = self.datos[1]
            NBE = self.datos[2]
            diccParticionVerticalPorDefecto = {0: 2.25, 1: {'V': 1.8, 'W': 1.8, 'X': 1.62, 'Y': 1.44, 'Z': 1.44}, 2: {'alpha': 0.94, 'A': 0.94, 'B': 0.82, 'C': 0.73, 'D': 0.66, 'E': 0.57}, 3: {'alpha': 0.94, 'A': 0.94, 'B': 0.82, 'C': 0.73, 'D': 0.66, 'E': 0.57}}
            if norma == 0:
                self.UCerramiento = diccParticionVerticalPorDefecto[norma]
            elif norma == 1:
                self.UCerramiento = diccParticionVerticalPorDefecto[norma][NBE]
            elif norma == 2 or norma == 3:
                zonaAux = HE1[0:-1]
                self.UCerramiento = diccParticionVerticalPorDefecto[norma][zonaAux]
            self.densidadCerramiento = 60

    def obtenerDatosParticionHorizontalBajoCubierta(self):
        """
        Metodo: obtenerDatosParticionHorizontalBajoCubierta

        """
        if self.tipoIndicacion == 'Estimado':
            norma = self.datos[0]
            HE1 = self.datos[1]
            NBE = self.datos[2]
            tieneAislamiento = self.datos[3]
            if tieneAislamiento == True:
                if norma == 0:
                    self.UCerramiento = 1.12
                    self.densidadCerramiento = 120
                elif norma == 1:
                    if NBE == 'V' or NBE == 'W':
                        self.UCerramiento = 1.12
                    elif NBE == 'X':
                        self.UCerramiento = 1.12
                    elif NBE == 'Y':
                        self.UCerramiento = 1.12
                    else:
                        self.UCerramiento = 1.12
                    self.densidadCerramiento = 400
                else:
                    if 'A' in HE1 or 'alpha' in HE1:
                        self.UCerramiento = 0.71
                    elif 'B' in HE1:
                        self.UCerramiento = 0.64
                    elif 'C' in HE1:
                        self.UCerramiento = 0.59
                    elif 'D' in HE1:
                        self.UCerramiento = 0.54
                    elif 'E' in HE1:
                        self.UCerramiento = 0.5
                    self.densidadCerramiento = 400
            elif norma == 0:
                self.UCerramiento = 1.7
                self.densidadCerramiento = 120
            elif norma == 1:
                if NBE == 'V' or NBE == 'W':
                    self.UCerramiento = 1.7
                elif NBE == 'X':
                    self.UCerramiento = 1.4
                elif NBE == 'Y':
                    self.UCerramiento = 1.2
                else:
                    self.UCerramiento = 1.2
                self.densidadCerramiento = 400
            else:
                if 'A' in HE1 or 'alpha' in HE1:
                    self.UCerramiento = 0.71
                elif 'B' in HE1:
                    self.UCerramiento = 0.64
                elif 'C' in HE1:
                    self.UCerramiento = 0.59
                elif 'D' in HE1:
                    self.UCerramiento = 0.54
                elif 'E' in HE1:
                    self.UCerramiento = 0.5
                self.densidadCerramiento = 400
        if self.tipoIndicacion == 'Por defecto':
            norma = self.datos[0]
            HE1 = self.datos[1]
            NBE = self.datos[2]
            if norma == 0:
                self.densidadCerramiento = 120.0
            else:
                self.densidadCerramiento = 400.0
            diccPHBajoCubiertaPorDefecto = {0: 1.36, 1: {'V': 1.36, 'W': 1.36, 'X': 1.12, 'Y': 0.96, 'Z': 0.96}, 2: {'alpha': 0.5, 'A': 0.5, 'B': 0.45, 'C': 0.41, 'D': 0.38, 'E': 0.35}, 3: {'alpha': 0.5, 'A': 0.5, 'B': 0.45, 'C': 0.41, 'D': 0.38, 'E': 0.35}}
            if norma == 0:
                self.UCerramiento = diccPHBajoCubiertaPorDefecto[norma]
            else:
                if norma == 1:
                    self.UCerramiento = diccPHBajoCubiertaPorDefecto[norma][NBE]
                elif norma == 2 or norma == 3:
                    zonaAux = HE1[0:-1]
                    self.UCerramiento = diccPHBajoCubiertaPorDefecto[norma][zonaAux]

    def obtenerDatosParticionHorizontalOtro(self):
        """
        Metodo: obtenerDatosParticionHorizontalOtro

        """
        if self.tipoIndicacion == 'Por defecto':
            norma = self.datos[0]
            HE1 = self.datos[1]
            NBE = self.datos[2]
            if norma == 0:
                self.densidadCerramiento = 220
            else:
                self.densidadCerramiento = 500
            diccPHOtroPorDefecto = {0: 1.7, 1: {'V': 1.7, 'W': 1.7, 'X': 1.4, 'Y': 1.2, 'Z': 1.2}, 2: {'alpha': 0.5, 'A': 0.5, 'B': 0.45, 'C': 0.41, 'D': 0.38, 'E': 0.35}, 3: {'alpha': 0.5, 'A': 0.5, 'B': 0.45, 'C': 0.41, 'D': 0.38, 'E': 0.35}}
            if norma == 0:
                self.UCerramiento = diccPHOtroPorDefecto[norma]
            else:
                if norma == 1:
                    self.UCerramiento = diccPHOtroPorDefecto[norma][NBE]
                elif norma == 2 or norma == 3:
                    zonaAux = HE1[0:-1]
                    self.UCerramiento = diccPHOtroPorDefecto[norma][zonaAux]

    def obtenerDatosParticionHorizontalInferior(self):
        """
        Metodo: obtenerDatosParticionHorizontalInferior

        """
        if self.tipoIndicacion == 'Estimado':
            norma = self.datos[0]
            HE1 = self.datos[1]
            NBE = self.datos[2]
            if norma == 0:
                self.UCerramiento = 2.17
                self.densidadCerramiento = 50.0
            elif norma == 1:
                if NBE == 'V' or NBE == 'W':
                    self.UCerramiento = 2.17
                elif NBE == 'X':
                    self.UCerramiento = 1.4
                elif NBE == 'Y':
                    self.UCerramiento = 1.2
                else:
                    self.UCerramiento = 1.2
                self.densidadCerramiento = 333.0
            else:
                if 'A' in HE1 or 'alpha' in HE1:
                    self.UCerramiento = 0.59
                elif 'B' in HE1:
                    self.UCerramiento = 0.58
                elif 'C' in HE1:
                    self.UCerramiento = 0.56
                elif 'D' in HE1:
                    self.UCerramiento = 0.54
                elif 'E' in HE1:
                    self.UCerramiento = 0.53
                self.densidadCerramiento = 333.0
        elif self.tipoIndicacion == 'Por defecto':
            norma = self.datos[0]
            HE1 = self.datos[1]
            NBE = self.datos[2]
            if norma == 0:
                self.densidadCerramiento = 50.0
            else:
                self.densidadCerramiento = 333.0
            diccPHInferiorPorDefecto = {0: 2.17, 1: {'V': 2.17, 'W': 2.17, 'X': 1.4, 'Y': 1.2, 'Z': 1.2}, 2: {'alpha': 0.53, 'A': 0.53, 'B': 0.52, 'C': 0.5, 'D': 0.49, 'E': 0.48}, 3: {'alpha': 0.53, 'A': 0.53, 'B': 0.52, 'C': 0.5, 'D': 0.49, 'E': 0.48}}
            if norma == 0:
                self.UCerramiento = diccPHInferiorPorDefecto[norma]
            else:
                if norma == 1:
                    self.UCerramiento = diccPHInferiorPorDefecto[norma][NBE]
                elif norma == 2 or norma == 3:
                    zonaAux = HE1[0:-1]
                    self.UCerramiento = diccPHInferiorPorDefecto[norma][zonaAux]

    def obtenerDatosCamaraSanitaria(self):
        """
        Metodo: obtenerDatosCamaraSanitaria

        """
        if self.tipoIndicacion == 'Estimado':
            norma = self.datos[0]
            HE1 = self.datos[1]
            NBE = self.datos[2]
            B = float(self.datos[3])
            if norma == 0:
                Rf = 0.3
                self.densidadCerramiento = 333.0
            elif norma == 1:
                if NBE == 'V' or NBE == 'W':
                    Rf = 0.3
                elif NBE == 'X':
                    Rf = 0.51
                elif NBE == 'Y':
                    Rf = 0.63
                else:
                    Rf = 0.63
                self.densidadCerramiento = 333.0
            else:
                if 'A' in HE1 or 'B' in HE1 or 'alpha' in HE1:
                    if B < 18.0:
                        Rf = 1.5
                    else:
                        Rf = 1.0
                elif 'C' in HE1:
                    if B < 22.0:
                        Rf = 1.5
                    else:
                        Rf = 1.0
                elif 'D' in HE1:
                    if B < 24.0:
                        Rf = 1.5
                    else:
                        Rf = 1.0
                elif 'E' in HE1:
                    if B < 22.0:
                        Rf = 1.5
                    else:
                        Rf = 1.0
                self.densidadCerramiento = 333.0
            self.UCerramiento = 1.0 / Rf
        if self.tipoIndicacion == 'Por defecto':
            norma = self.datos[0]
            HE1 = self.datos[1]
            NBE = self.datos[2]
            diccCamaraSanitariaPorDefecto = {0: 2.0, 1: {'V': 2.0, 'W': 2.0, 'X': 1.4, 'Y': 1.2, 'Z': 1.2}, 2: {'alpha': 0.53, 'A': 0.53, 'B': 0.52, 'C': 0.5, 'D': 0.49, 'E': 0.48}, 3: {'alpha': 0.53, 'A': 0.53, 'B': 0.52, 'C': 0.5, 'D': 0.49, 'E': 0.48}}
            if norma == 0:
                self.UCerramiento = diccCamaraSanitariaPorDefecto[norma]
            elif norma == 1:
                self.UCerramiento = diccCamaraSanitariaPorDefecto[norma][NBE]
            elif norma == 2 or norma == 3:
                zonaAux = HE1[0:-1]
                self.UCerramiento = diccCamaraSanitariaPorDefecto[norma][zonaAux]
            self.densidadCerramiento = 333.0


def calcularLongitudPT(cerr, tipoPuenteSeleccionado, alturaPlanta, numeroPlantas):
    """
    Metodo: calcularLongitudPT

    ARGUMENTOS:
                cerr:
                tipoPuenteSeleccionado:
                alturaPlanta:
                numeroPlantas:
    """
    longitudPT = 0
    alturaPlanta = float(alturaPlanta)
    numeroPlantas = float(numeroPlantas)
    if tipoPuenteSeleccionado != 'Contorno de hueco' and tipoPuenteSeleccionado != 'Caja de Persiana':
        superficie = float(cerr[2])
        if cerr[1] == 'Fachada':
            try:
                longitud = float(cerr[-5])
                altura = float(cerr[-4])
                multip = 1.0
            except (ValueError, TypeError):
                try:
                    altura = float(alturaPlanta)
                    longitud = superficie / (alturaPlanta * numeroPlantas)
                    multip = numeroPlantas
                except (ValueError, TypeError):
                    longitudPT = ''
                    return longitudPT
                except ZeroDivisionError:
                    longitudPT = ''
                    return longitudPT

            if tipoPuenteSeleccionado == 'Pilar integrado en fachada':
                longitudPT = round((math.ceil(longitud / 5.0) + 1.0) * altura * multip, 2)
            elif tipoPuenteSeleccionado == 'Pilar en Esquina':
                longitudPT = round(altura * multip * 1.0, 2)
            else:
                if tipoPuenteSeleccionado == 'Encuentro de fachada con forjado' or tipoPuenteSeleccionado == 'Encuentro de fachada con voladizo':
                    if numeroPlantas <= 1.0:
                        longitudPT = round(longitud * numeroPlantas, 2)
                    else:
                        longitudPT = round(longitud * (numeroPlantas - 1.0), 2)
                else:
                    longitudPT = ''
        else:
            if cerr[1] == 'Suelo':
                try:
                    longitud = float(cerr[-5])
                    altura = float(cerr[-4])
                except (ValueError, TypeError):
                    altura = superficie / 7.0
                    longitud = 7.0

                if tipoPuenteSeleccionado == 'Encuentro de fachada con suelo en contacto con el aire' or tipoPuenteSeleccionado == 'Encuentro de fachada con solera':
                    longitudPT = round(altura * 2.0 + longitud * 2.0, 2)
                else:
                    longitudPT = ''
            elif cerr[1] == 'Cubierta':
                try:
                    longitud = float(cerr[-5])
                    altura = float(cerr[-4])
                except (ValueError, TypeError):
                    altura = superficie / 7.0
                    longitud = 7.0

                if tipoPuenteSeleccionado == 'Encuentro de fachada con cubierta':
                    longitudPT = round(altura * 2.0 + longitud * 2.0, 2)
                else:
                    longitudPT = ''
    else:
        superficie = float(cerr.superficie)
        try:
            longitud = float(cerr.longitud)
            altura = float(cerr.altura)
            multip = float(cerr.multiplicador)
        except (ValueError, TypeError):
            altura = 1.0
            longitud = superficie / 1.0
            multip = 1.0

        if tipoPuenteSeleccionado == 'Contorno de hueco':
            longitudPT = round((2.0 * longitud + 2.0 * altura) * multip, 2)
        elif tipoPuenteSeleccionado == 'Caja de Persiana':
            longitudPT = round(longitud * multip, 2)
        else:
            longitudPT = ''
    return longitudPT


def obtenerCorrectoresFactorSolar(orientacionHueco, Voladizo_L, Voladizo_D, Voladizo_H, Retranqueo_H, Retranqueo_W, Retranqueo_R, Lamas_Horizontales_BETA, Lamas_Verticales_BETA, Toldos_AnguloA, Toldos_OpacoA, Toldos_TranslucidoA, Toldos_AnguloB, Toldos_OpacoB, Toldos_TranslucidoB, Lucernarios_X, Lucernarios_Y, Lucernarios_Z, Voladizos_Si, Retranqueos_Si, Lamas_Horizontales_Si, Lamas_Verticales_Si, Lucernarios_Si, Toldos_Si, Otro_Si, OtroInvierno, OtroVerano):
    """
    Metodo: obtenerCorrectoresFactorSolar

    ARGUMENTOS:
                orientacionHueco:
    """
    if Voladizo_L != '' and Voladizo_D != '' and Voladizo_H != '':
        try:
            FS_VOLADIZOS = float(funcionFactorSombra.Factor_Sombra_Voladizos(Voladizo_L, Voladizo_H, Voladizo_D, orientacionHueco))
            FS_VOLADIZOS_calculos = funcionFactorSombra.Factor_Sombra_Voladizos_Calculos(Voladizo_L, Voladizo_H, Voladizo_D, orientacionHueco)
            FS_VOLADIZOS_invierno = FS_VOLADIZOS_calculos[0]
            FS_VOLADIZOS_verano = FS_VOLADIZOS_calculos[1]
        except:
            wx.MessageBox(_('Voladizo mal definido'), _('Aviso'))
            return

        Voladizos_Si = False
    else:
        FS_VOLADIZOS = 1.0
        FS_VOLADIZOS_invierno = 1.0
        FS_VOLADIZOS_verano = 1.0
    if Retranqueo_H != '' and Retranqueo_W != '' and Retranqueo_R != '':
        try:
            FS_RETRANQUEOS = float(funcionFactorSombra.Factor_Sombra_Retranqueo(Retranqueo_R, Retranqueo_H, Retranqueo_W, orientacionHueco))
            FS_RETRANQUEOS_calculos = funcionFactorSombra.Factor_Sombra_Retranqueo_Calculos(Retranqueo_R, Retranqueo_H, Retranqueo_W, orientacionHueco)
            FS_RETRANQUEOS_invierno = FS_RETRANQUEOS_calculos[0]
            FS_RETRANQUEOS_verano = FS_RETRANQUEOS_calculos[1]
        except:
            wx.MessageBox(_('Retranqueo mal definido'), _('Aviso'))
            return

        Retranqueos_Si = False
    else:
        FS_RETRANQUEOS = 1.0
        FS_RETRANQUEOS_invierno = 1.0
        FS_RETRANQUEOS_verano = 1.0
    if Lamas_Horizontales_BETA[0] != '':
        try:
            FS_LAMAS_HORIZONTALES = float(funcionFactorSombra.Factor_Sombra_Lamas_Horizontales(Lamas_Horizontales_BETA[0], orientacionHueco))
            FS_LAMAS_HORIZONTALES_calculos = funcionFactorSombra.Factor_Sombra_Lamas_Horizontales_Calculos(Lamas_Horizontales_BETA[0], orientacionHueco)
            trans = float(Lamas_Horizontales_BETA[1])
            refle = float(Lamas_Horizontales_BETA[2])
            FS_LAMAS_HORIZONTALES_invierno = FS_LAMAS_HORIZONTALES_calculos[0] + (1 - FS_LAMAS_HORIZONTALES_calculos[0]) * (trans + refle)
            FS_LAMAS_HORIZONTALES_verano = FS_LAMAS_HORIZONTALES_calculos[1] + (1 - FS_LAMAS_HORIZONTALES_calculos[1]) * (trans + refle)
        except:
            wx.MessageBox(_('Lamas horizontales mal definidas'), _('Aviso'))
            return

        Lamas_Horizontales_Si = False
    else:
        FS_LAMAS_HORIZONTALES = 1.0
        FS_LAMAS_HORIZONTALES_invierno = 1.0
        FS_LAMAS_HORIZONTALES_verano = 1.0
    if Lamas_Verticales_BETA[0] != '':
        try:
            FS_LAMAS_VERTICALES = float(funcionFactorSombra.Factor_Sombra_Lamas_Verticales(Lamas_Verticales_BETA[0], orientacionHueco))
            trans = float(Lamas_Verticales_BETA[1])
            refle = float(Lamas_Verticales_BETA[2])
            FS_LAMAS_VERTICALES_calculos = funcionFactorSombra.Factor_Sombra_Lamas_Verticales_Calculos(Lamas_Verticales_BETA[0], orientacionHueco)
            FS_LAMAS_VERTICALES_invierno = FS_LAMAS_VERTICALES_calculos[0] + (1 - FS_LAMAS_VERTICALES_calculos[0]) * (trans + refle)
            FS_LAMAS_VERTICALES_verano = FS_LAMAS_VERTICALES_calculos[1] + (1 - FS_LAMAS_VERTICALES_calculos[1]) * (trans + refle)
        except:
            wx.MessageBox(_('Lamas verticales mal definidas'), _('Aviso'))
            return

        Lamas_Verticales_Si = False
    else:
        FS_LAMAS_VERTICALES = 1.0
        FS_LAMAS_VERTICALES_invierno = 1.0
        FS_LAMAS_VERTICALES_verano = 1.0
    if Toldos_AnguloA != '' and (Toldos_OpacoA == True or Toldos_TranslucidoA == True) or Toldos_AnguloB != '' and (Toldos_OpacoB == True or Toldos_TranslucidoB == True):
        if Toldos_AnguloA != '' and (Toldos_OpacoA == True or Toldos_TranslucidoA == True):
            if Toldos_OpacoA == True:
                tipo_tejido = 'Opaco'
            else:
                if Toldos_TranslucidoA == True:
                    tipo_tejido = 'Translucido'
                try:
                    FS_TOLDOS = float(funcionFactorSombra.Factor_Sombra_Toldos_A(tipo_tejido, orientacionHueco, Toldos_AnguloA))
                except:
                    wx.MessageBox(_('Toldo mal definido'), _('Aviso'))
                    return

            Toldos_Si = False
        else:
            if Toldos_AnguloB != '' and (Toldos_OpacoB == True or Toldos_TranslucidoB == True):
                if Toldos_OpacoB == True:
                    tipo_tejido = 'Opaco'
                else:
                    if Toldos_TranslucidoB == True:
                        tipo_tejido = 'Translucido'
                    try:
                        FS_TOLDOS = float(funcionFactorSombra.Factor_Sombra_Toldos_B(tipo_tejido, orientacionHueco, Toldos_AnguloB))
                    except:
                        wx.MessageBox(_('Toldo mal definido'), _('Aviso'))
                        return

                Toldos_Si = False
            else:
                FS_TOLDOS = 1.0
    else:
        FS_TOLDOS = 1.0
    if Lucernarios_X != '' and Lucernarios_Y != '' and Lucernarios_Z != '':
        try:
            FS_LUCERNARIOS = float(funcionFactorSombra.Factor_Sombra_Lucernarios(Lucernarios_X, Lucernarios_Y, Lucernarios_Z))
        except:
            wx.MessageBox(_('Lucernario mal definido'), _('Aviso'))
            return

        Lucernarios_Si = False
    else:
        FS_LUCERNARIOS = 1.0
    if Otro_Si == True:
        try:
            FS_OTRO_invierno = float(OtroInvierno)
            FS_OTRO_verano = float(OtroVerano)
        except:
            logging.info('Excepcion en: %s' % __name__)
            FS_OTRO_invierno = 1.0
            FS_OTRO_verano = 1.0

    else:
        FS_OTRO_invierno = 1.0
        FS_OTRO_verano = 1.0
    corrector_FS_sombras = FS_VOLADIZOS * FS_RETRANQUEOS * FS_LAMAS_HORIZONTALES * FS_LAMAS_VERTICALES * FS_TOLDOS * FS_LUCERNARIOS
    corrector_FS_invierno = FS_VOLADIZOS_invierno * FS_RETRANQUEOS_invierno * FS_LAMAS_HORIZONTALES_invierno * FS_LAMAS_VERTICALES_invierno * FS_LUCERNARIOS * FS_OTRO_invierno
    corrector_FS_verano = min(FS_VOLADIZOS_verano, FS_RETRANQUEOS_verano, FS_LAMAS_HORIZONTALES_verano, FS_LAMAS_VERTICALES_verano, FS_TOLDOS, FS_LUCERNARIOS, FS_OTRO_verano)
    return [
     [
      corrector_FS_sombras, corrector_FS_invierno, corrector_FS_verano],
     [
      Voladizos_Si, Retranqueos_Si, Lamas_Horizontales_Si, Lamas_Verticales_Si, 
      Lucernarios_Si, Toldos_Si, Otro_Si]]