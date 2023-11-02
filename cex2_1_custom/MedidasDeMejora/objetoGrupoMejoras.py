# File: o (Python 2.7)

'''
Modulo: objetoGrupoMejoras.py

'''
from Calculos.listados import getVersionGuardada, versionArchivoCoincideConVersionPrograma
import ElementosConstructivos.BDcerramientos as BDcerramientos
import ElementosConstructivos.cargaBD as cargaBD
import Envolvente.tablasValores as tablasValores
import StringIO
import copy
import datosEdificio
import pickle
import tempfile
import wx
import logging

class mejoraEdificioCompleto:
    '''
    Clase: mejoraEdificioCompleto del modulo objetoGrupoMejoras.py


    '''
    
    def __init__(self, fileName, nombre = '', datosEdificioOriginal = None, caracteristicas = '', otrosDatos = ''):
        '''
        Constructor de la clase


        ARGUMENTOS:
    \t\tfileName:
    \t\tprograma:
    \t\tnombre:
    \t\tdatosEdificioOriginal:
        '''
        self.mejoras = fileName
        self.nombre = self.getNombreConjunto()
        self.datosEdificioOriginal = datosEdificioOriginal
        self.caracteristicas = caracteristicas
        self.otrosDatos = otrosDatos
        self.ahorro = []
        self.datosNuevoEdificio = None
        self.analisisEconomico = AnalisisEconomicoConjuntoMM()

    
    def calculoInversionInicial(self):
        """
        Metodo: calculoInversionInicial
        Devuelve el coste total de la inversi\xf3n = suma de los costes de cada medida
        Si no se han definido los costes de todas las medidas o alguno no es correcto, devuelve '-'
        """
        numeroMedidasConjuntoMM = self.getNumeroMedidasConjunto()
        if len(self.analisisEconomico.inversionInicial) != numeroMedidasConjuntoMM:
            costeInversion = '-'
        else:
            
            try:
                costeInversion = sum(self.analisisEconomico.inversionInicial)
            except:
                logging.info(u'Excepcion en: %s' % __name__)
                costeInversion = '-'

        return costeInversion

    
    def getNumeroMedidasConjunto(self):
        return 1

    
    def getNombreConjunto(self):
        nombre = self.mejoras.split('\\')[-1]
        return nombre

    
    def calificacion(self):
        
        try:
            f1 = open(self.mejoras, 'r')
            version = pickle.load(f1)
            versionArchivoCoincide = versionArchivoCoincideConVersionPrograma(versionGuardada = version, programa = self.datosEdificioOriginal.programa)
            if versionArchivoCoincide == False:
                f1.close()
                return _(u'El conjunto de mejoras se grab\xc3\xb3 con una versi\xc3\xb3n de CE3X diferente a la actual. Grabe el archivo del conjunto de medidas de mejora con la versi\xc3\xb3n actual y vuelva a cargarlo.')
            None.load(f1)
            datosGen = pickle.load(f1)
            datosEnvolvente = pickle.load(f1)
            datosInstalaciones = pickle.load(f1)
            pickle.load(f1)
            pickle.load(f1)
            pickle.load(f1)
            pickle.load(f1)
            datosSombras = pickle.load(f1)
            pickle.load(f1)
            pickle.load(f1)
            f1.close()
        except:
            f1.close()
            return _(u'Error en la lectura del fichero')

        datosGen[6] = float(datosGen[6])
        datosGen[7] = float(datosGen[7])
        datosGen[8] = float(datosGen[8])
        datosGen[9] = datosGen[9]
        envolvente = [
            datosEnvolvente[0],
            datosEnvolvente[1],
            datosEnvolvente[2]]
        subgrupos = datosEnvolvente[3]
        zonaCalificacion = ''
        if self.datosEdificioOriginal.programa == 'Residencial':
            self.datosNuevoEdificio = datosEdificio.datosEdificio(datosGenerales = datosGen, datosEnvolvente = envolvente, datosInstalaciones = datosInstalaciones, programa = self.datosEdificioOriginal.programa, subgrupos = subgrupos, datosSombras = datosSombras, escala = self.datosEdificioOriginal.escala, esEdificioExistente = self.datosEdificioOriginal.esEdificioExistente)
            self.datosNuevoEdificio.calificacion()
        else:
            self.datosNuevoEdificio = datosEdificio.datosEdificioTerciario(datosGenerales = datosGen, datosEnvolvente = envolvente, datosInstalaciones = datosInstalaciones, programa = self.datosEdificioOriginal.programa, subgrupos = subgrupos, datosSombras = datosSombras, escala = self.datosEdificioOriginal.escala, esEdificioExistente = self.datosEdificioOriginal.esEdificioExistente)
            self.datosNuevoEdificio.calificacion()
        if self.datosNuevoEdificio.casoValido == False:
            return None
        None.calcularAhorros()

    
    def calcularAhorros(self):
        '''
        Metodo: calcularAhorros


        ARGUMENTOS:
    \t\tdatosEdificioOriginal:
        '''
        
        try:
            ahorro0 = round(((self.datosEdificioOriginal.datosResultados.ddaBrutaCal - self.datosNuevoEdificio.datosResultados.ddaBrutaCal) / self.datosEdificioOriginal.datosResultados.ddaBrutaCal) * 100, 1)
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            if self.datosNuevoEdificio.datosResultados.ddaBrutaCal == 0:
                ahorro0 = 0
            else:
                ahorro0 = -100

        
        try:
            ahorro1 = round(((self.datosEdificioOriginal.datosResultados.ddaBrutaRef - self.datosNuevoEdificio.datosResultados.ddaBrutaRef) / self.datosEdificioOriginal.datosResultados.ddaBrutaRef) * 100, 1)
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            if self.datosNuevoEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
                ahorro1 = 0
            elif self.datosNuevoEdificio.datosResultados.ddaBrutaRef == 0:
                ahorro1 = 0
            else:
                ahorro1 = -100

        
        try:
            ahorro2 = round(((self.datosEdificioOriginal.datosResultados.emisionesCal - self.datosNuevoEdificio.datosResultados.emisionesCal) / self.datosEdificioOriginal.datosResultados.emisionesCal) * 100, 1)
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            if self.datosNuevoEdificio.datosResultados.emisionesCal == 0:
                ahorro2 = 0
            else:
                ahorro2 = -100

        
        try:
            ahorro3 = round(((self.datosEdificioOriginal.datosResultados.emisionesRef - self.datosNuevoEdificio.datosResultados.emisionesRef) / self.datosEdificioOriginal.datosResultados.emisionesRef) * 100, 1)
        except:
            if self.datosNuevoEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
                ahorro3 = 0
            elif self.datosNuevoEdificio.datosResultados.emisionesRef == 0:
                ahorro3 = 0
            else:
                ahorro3 = -100

        
        try:
            ahorro4 = round(((self.datosEdificioOriginal.datosResultados.emisionesACS - self.datosNuevoEdificio.datosResultados.emisionesACS) / self.datosEdificioOriginal.datosResultados.emisionesACS) * 100, 1)
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            if self.datosNuevoEdificio.datosResultados.emisionesACS == 0:
                ahorro4 = 0
            else:
                ahorro4 = -100

        
        try:
            ahorro5 = round(((self.datosEdificioOriginal.datosResultados.emisionesMostrar - self.datosNuevoEdificio.datosResultados.emisionesMostrar) / self.datosEdificioOriginal.datosResultados.emisionesMostrar) * 100, 1)
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            if self.datosNuevoEdificio.datosResultados.emisionesMostrar == 0:
                ahorro5 = 0
            else:
                ahorro5 = -100

        if self.datosEdificioOriginal.programa == 'Residencial':
            self.ahorro = [
                ahorro0,
                ahorro1,
                ahorro2,
                ahorro3,
                ahorro4,
                ahorro5]
        else:
            
            try:
                ahorroIluminacion = round(((self.datosEdificioOriginal.datosResultados.emisionesIlum - self.datosNuevoEdificio.datosResultados.emisionesIlum) / self.datosEdificioOriginal.datosResultados.emisionesIlum) * 100, 1)
            except:
                logging.info(u'Excepcion en: %s' % __name__)
                if self.datosNuevoEdificio.datosResultados.emisionesIlum == 0:
                    ahorroIluminacion = 0
                else:
                    ahorroIluminacion = -100

            self.ahorro = [
                ahorro0,
                ahorro1,
                ahorro2,
                ahorro3,
                ahorro4,
                ahorroIluminacion,
                ahorro5]



class grupoMedidasMejora:
    '''
    Clase: grupoMedidasMejora del modulo objetoGrupoMejoras.py


    '''
    
    def __init__(self, nombre, datosEdificioOriginal, mejoras = [
        [],
        [
            '',
            [],
            False]], caracteristicas = '', otrosDatos = ''):
        '''
        Constructor de la clase


        ARGUMENTOS:
    \t\tnombre:
    \t\tdatosEdificioOriginal:
    \t\tmejoras=None:
        '''
        if not mejoras:
            pass
        mejoras = []
        self.mejoras = mejoras
        self.nombre = nombre
        self.datosEdificioOriginal = datosEdificioOriginal
        self.caracteristicas = caracteristicas
        self.otrosDatos = otrosDatos
        self.cerramientosMejorados = []
        self.huecosMejorados = []
        self.puentesTermicosMejorados = []
        self.ahorro = []
        self.datosNuevoEdificio = None
        self.analisisEconomico = AnalisisEconomicoConjuntoMM()

    
    def calculoInversionInicial(self):
        """
        Metodo: calculoInversionInicial
        Devuelve el coste total de la inversi\xf3n = suma de los costes de cada medida
        Si no se han definido los costes de todas las medidas o alguno no es correcto, devuelve '-'
        """
        numeroMedidasConjuntoMM = self.getNumeroMedidasConjunto()
        if len(self.analisisEconomico.inversionInicial) != numeroMedidasConjuntoMM:
            costeInversion = '-'
        else:
            
            try:
                costeInversion = sum(self.analisisEconomico.inversionInicial)
            except:
                logging.info(u'Excepcion en: %s' % __name__)
                costeInversion = '-'

        return costeInversion

    
    def getNumeroMedidasConjunto(self):
        numeroMedidasConjuntoMM = 0
        if self.mejoras[1][2] == True:
            numeroMedidasConjuntoMM += 1
        numeroMedidasConjuntoMM += len(self.mejoras[0])
        return numeroMedidasConjuntoMM

    
    def obtenerEnvolvente(self, cerr, vent, pt):
        '''
        Metodo: obtenerEnvolvente


        ARGUMENTOS:
    \t\tcerr:
    \t\tvent:
    \t\tpt:
        '''
        self.cerramientosMejorados = copy.deepcopy(cerr)
        self.huecosMejorados = copy.deepcopy(vent)
        self.puentesTermicosMejorados = copy.deepcopy(pt)

    
    def obtenerInstalaciones(self, medidas, datosEdificioOriginal):
        '''
        Metodo: obtenerInstalaciones


        ARGUMENTOS:
    \t\tmedidas:
    \t\tdatosEdificioOriginal:
        '''
        if medidas == []:
            self.sistemasACSMM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasACS)
            self.sistemasCalefaccionMM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasCalefaccion)
            self.sistemasRefrigeracionMM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasRefrigeracion)
            self.sistemasClimatizacionMM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasClimatizacion)
            self.sistemasMixto2MM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasMixto2)
            self.sistemasMixto3MM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasMixto3)
            self.sistemasContribucionesMM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasContribuciones)
            if datosEdificioOriginal.programa != 'Residencial':
                self.sistemasIluminacionMM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasIluminacionMM)
                self.sistemasVentilacionMM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasVentilacionMM)
                self.sistemasVentiladoresMM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasVentiladoresMM)
                self.sistemasBombasMM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasBombasMM)
                self.sistemasTorresRefrigeracionMM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasTorresRefrigeracionMM)
            else:
                self.sistemasIluminacionMM = []
                self.sistemasVentilacionMM = []
                self.sistemasVentiladoresMM = []
                self.sistemasBombasMM = []
                self.sistemasTorresRefrigeracionMM = []
        elif medidas[1][2] == False:
            self.sistemasACSMM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasACS)
            self.sistemasCalefaccionMM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasCalefaccion)
            self.sistemasRefrigeracionMM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasRefrigeracion)
            self.sistemasClimatizacionMM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasClimatizacion)
            self.sistemasMixto2MM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasMixto2)
            self.sistemasMixto3MM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasMixto3)
            self.sistemasContribucionesMM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasContribuciones)
            if datosEdificioOriginal.programa != 'Residencial':
                self.sistemasIluminacionMM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasIluminacion)
                self.sistemasVentilacionMM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasVentilacion)
                self.sistemasVentiladoresMM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasVentiladores)
                self.sistemasBombasMM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasBombas)
                self.sistemasTorresRefrigeracionMM = copy.deepcopy(datosEdificioOriginal.datosIniciales.sistemasTorresRefrigeracion)
            else:
                self.sistemasIluminacionMM = []
                self.sistemasVentilacionMM = []
                self.sistemasVentiladoresMM = []
                self.sistemasBombasMM = []
                self.sistemasTorresRefrigeracionMM = []
        else:
            self.sistemasACSMM = medidas[1][1][0]
            self.sistemasCalefaccionMM = medidas[1][1][1]
            self.sistemasRefrigeracionMM = medidas[1][1][2]
            self.sistemasClimatizacionMM = medidas[1][1][3]
            self.sistemasMixto2MM = medidas[1][1][4]
            self.sistemasMixto3MM = medidas[1][1][5]
            self.sistemasContribucionesMM = medidas[1][1][6]
            if datosEdificioOriginal.programa != 'Residencial':
                self.sistemasIluminacionMM = medidas[1][1][7]
                self.sistemasVentilacionMM = medidas[1][1][8]
                self.sistemasVentiladoresMM = medidas[1][1][9]
                self.sistemasBombasMM = medidas[1][1][10]
                self.sistemasTorresRefrigeracionMM = medidas[1][1][11]
            else:
                self.sistemasIluminacionMM = []
                self.sistemasVentilacionMM = []
                self.sistemasVentiladoresMM = []
                self.sistemasBombasMM = []
                self.sistemasTorresRefrigeracionMM = []
        return [
            self.sistemasACSMM,
            self.sistemasCalefaccionMM,
            self.sistemasRefrigeracionMM,
            self.sistemasClimatizacionMM,
            self.sistemasMixto2MM,
            self.sistemasMixto3MM,
            self.sistemasContribucionesMM,
            self.sistemasIluminacionMM,
            self.sistemasVentilacionMM,
            self.sistemasVentiladoresMM,
            self.sistemasBombasMM,
            self.sistemasTorresRefrigeracionMM]

    
    def obtenerMedidas(self, mejoras):
        '''
        Metodo: obtenerMedidas


        ARGUMENTOS:
    \t\tmejoras):    ###A\xf1ado medidas de mejo:
        '''
        self.medidasMejoraEnvolvente = []
        for i in mejoras[0]:
            self.medidasMejoraEnvolvente.append(i)
        

    
    def incluirMedidas(self, cerramientosIniciales):
        '''
        Metodo: incluirMedidas


        ARGUMENTOS:
    \t\tcerramientosIniciales:
        '''
        orientaciones = [
            'Norte',
            'NO',
            'NE',
            'Sur',
            'SO',
            'SE',
            'Techo',
            'Oeste',
            'Este']
        for i in range(len(self.medidasMejoraEnvolvente)):
            if u'Adici\xc3\xb3n de Aislamiento T\xc3\xa9rmico' in self.medidasMejoraEnvolvente[i]:
                for j in range(len(self.cerramientosMejorados)):
                    if not self.medidasMejoraEnvolvente[i][2][0] == True and 'Fachada' == self.cerramientosMejorados[j][1] or self.cerramientosMejorados[j][-1] != 'edificio':
                        if not self.medidasMejoraEnvolvente[i][2][1] == True or 'Cubierta' == self.cerramientosMejorados[j][1]:
                            if not self.medidasMejoraEnvolvente[i][2][2] == True or 'Suelo' == self.cerramientosMejorados[j][1]:
                                if not self.medidasMejoraEnvolvente[i][2][12][0] == True and self.medidasMejoraEnvolvente[i][2][12][1] == True and u'Partici\xc3\xb3n Interior' == self.cerramientosMejorados[j][1] or self.cerramientosMejorados[j][-1] == 'vertical':
                                    if (self.medidasMejoraEnvolvente[i][2][12][0] == True and self.medidasMejoraEnvolvente[i][2][12][2] == True and u'Partici\xc3\xb3n Interior' == self.cerramientosMejorados[j][1] or self.cerramientosMejorados[j][-1] == 'horizontal superior' or self.medidasMejoraEnvolvente[i][2][12][0] == True) and self.medidasMejoraEnvolvente[i][2][12][3] == True and u'Partici\xc3\xb3n Interior' == self.cerramientosMejorados[j][1] and self.cerramientosMejorados[j][-1] == 'horizontal inferior':
                                        if self.medidasMejoraEnvolvente[i][2][3] == True:
                                            self.cerramientosMejorados[j][3] = float(self.medidasMejoraEnvolvente[i][2][6])
                                        elif self.medidasMejoraEnvolvente[i][2][4] == True:
                                            landa = self.medidasMejoraEnvolvente[i][2][7]
                                            espesor = self.medidasMejoraEnvolvente[i][2][8]
                                            if float(landa) != 0:
                                                rAislamiento = float(espesor) / float(landa)
                                            else:
                                                rAislamiento = 1000000
                                            if self.cerramientosMejorados[j][1] in ('Fachada', 'Cubierta'):
                                                rCerramiento = 1 / float(self.cerramientosMejorados[j][3])
                                                rNueva = rAislamiento + rCerramiento
                                                Unueva = 1 / rNueva
                                                self.cerramientosMejorados[j][3] = Unueva
                                            
                                        
                                    if self.medidasMejoraEnvolvente[i][2][0] == True and self.medidasMejoraEnvolvente[i][2][10] == True:
                                        for j in range(len(self.puentesTermicosMejorados)):
                                            if 'Pilar integrado en fachada' == self.puentesTermicosMejorados[j][2] or self.medidasMejoraEnvolvente[i][2][11][0] != '':
                                                self.puentesTermicosMejorados[j][3] = self.medidasMejoraEnvolvente[i][2][11][0]
                                            
                                            if 'Pilar en Esquina' == self.puentesTermicosMejorados[j][2] or self.medidasMejoraEnvolvente[i][2][11][1] != '':
                                                self.puentesTermicosMejorados[j][3] = self.medidasMejoraEnvolvente[i][2][11][1]
                                            
                                            if 'Contorno de hueco' == self.puentesTermicosMejorados[j][2] or self.medidasMejoraEnvolvente[i][2][11][2] != '':
                                                self.puentesTermicosMejorados[j][3] = self.medidasMejoraEnvolvente[i][2][11][2]
                                            
                                            if 'Caja de Persiana' == self.puentesTermicosMejorados[j][2] or self.medidasMejoraEnvolvente[i][2][11][3] != '':
                                                self.puentesTermicosMejorados[j][3] = self.medidasMejoraEnvolvente[i][2][11][3]
                                            
                                            if 'Encuentro de fachada con forjado' == self.puentesTermicosMejorados[j][2] or self.medidasMejoraEnvolvente[i][2][11][4] != '':
                                                self.puentesTermicosMejorados[j][3] = self.medidasMejoraEnvolvente[i][2][11][4]
                                            
                                            if 'Encuentro de fachada con cubierta' == self.puentesTermicosMejorados[j][2] or self.medidasMejoraEnvolvente[i][2][11][5] != '':
                                                self.puentesTermicosMejorados[j][3] = self.medidasMejoraEnvolvente[i][2][11][5]
                                            
                                            if 'Encuentro de fachada con suelo en contacto con el aire' == self.puentesTermicosMejorados[j][2] or self.medidasMejoraEnvolvente[i][2][11][6] != '':
                                                self.puentesTermicosMejorados[j][3] = self.medidasMejoraEnvolvente[i][2][11][6]
                                            
                                        
                                    continue
                                    if u'Sustituci\xc3\xb3n/mejora de Huecos' in self.medidasMejoraEnvolvente[i][1]:
                                        mejoraHuecos = self.medidasMejoraEnvolvente[i][2]
                                        nuevaUvidrio = False
                                        nuevaGvidrio = False
                                        nuevaPermeabilidad = False
                                        nuevoPorcMarco = False
                                        nuevaUMarco = False
                                        nuevaAbsortividadMarco = False
                                        nuevaUdobleVentana = False
                                        nuevaGdobleVentana = False
                                        nuevosEltosSombra = False
                                        nuevosCorrectoresSombra = False
                                        orientaciones = mejoraHuecos[0]
                                        if mejoraHuecos[1] == True:
                                            if mejoraHuecos[2] == True:
                                                nuevaUvidrio = mejoraHuecos[3]
                                                nuevaGvidrio = mejoraHuecos[4]
                                            else:
                                                datos = self.obtenerDatosLibreriaVidrios(mejoraHuecos[5])
                                                nuevaUvidrio = datos[0]
                                                nuevaGvidrio = datos[1]
                                        if mejoraHuecos[6] == True:
                                            if mejoraHuecos[7] == True:
                                                nuevaPermeabilidad = self.obtenerPermeabilidadClase(mejoraHuecos[8])
                                            else:
                                                nuevaPermeabilidad = mejoraHuecos[10]
                                        if mejoraHuecos[11] == True:
                                            nuevoPorcMarco = mejoraHuecos[12]
                                        if mejoraHuecos[13] == True:
                                            if mejoraHuecos[14] == True:
                                                nuevaUMarco = mejoraHuecos[15]
                                            else:
                                                datos = self.obtenerUmarcoLibreria(mejoraHuecos[16])
                                                nuevaUMarco = datos[0]
                                                nuevaAbsortividadMarco = datos[1]
                                        if mejoraHuecos[17] == True:
                                            datos = self.obtenerDatosDobleVentana(mejoraHuecos[18])
                                            nuevaUdobleVentana = datos[0]
                                            nuevaGdobleVentana = datos[1]
                                        if mejoraHuecos[19] == True:
                                            nuevosEltosSombra = mejoraHuecos[20]
                                        for vent in self.huecosMejorados:
                                            if float(vent.porcMarco) < 99.9:
                                                tipoVentana = vent.tipo
                                                orientacionVentana = vent.orientacion
                                                if orientacionVentana == 'Norte':
                                                    contador = 0
                                                elif orientacionVentana == 'NO':
                                                    contador = 1
                                                elif orientacionVentana == 'NE':
                                                    contador = 2
                                                elif orientacionVentana == 'Sur':
                                                    contador = 3
                                                elif orientacionVentana == 'SO':
                                                    contador = 4
                                                elif orientacionVentana == 'SE':
                                                    contador = 5
                                                elif orientacionVentana == 'Oeste':
                                                    contador = 7
                                                elif orientacionVentana == 'Este':
                                                    contador = 8
                                                if (tipoVentana == 'Lucernario' or orientaciones[6] == True or tipoVentana == 'Hueco') and orientaciones[contador] == True:
                                                    if nuevaPermeabilidad != False:
                                                        vent.permeabilidadValor = nuevaPermeabilidad
                                                    if nuevoPorcMarco != False:
                                                        vent.porcMarco = nuevoPorcMarco
                                                    if nuevaAbsortividadMarco != False:
                                                        vent.absortividadValor = nuevaAbsortividadMarco
                                                        vent.absortividadPosiciones = [
                                                            0,
                                                            0]
                                                    if nuevaUvidrio != False:
                                                        Uvidrio = float(nuevaUvidrio)
                                                    else:
                                                        Uanterior = vent.Uvidrio
                                                        if ('Estimadas' in vent.__tipo__ or vent.dobleVentana == True or 'Conocidas' in vent.__tipo__) and vent.dobleVentana == True:
                                                            RcontraventanaAnterior = 0.18
                                                            if float(Uanterior) == 0:
                                                                Uanterior = 1e-006
                                                            Uvidrio = 1 / (1 / Uanterior - RcontraventanaAnterior)
                                                        else:
                                                            Uvidrio = Uanterior
                                                    if nuevaUMarco != False:
                                                        Umarco = float(nuevaUMarco)
                                                    else:
                                                        UmarcoAnterior = vent.Umarco
                                                        if ('Estimadas' in vent.__tipo__ or vent.dobleVentana == True or 'Conocidas' in vent.__tipo__) and vent.dobleVentana == True:
                                                            RcontraventanaAnterior = 0.18
                                                            if float(UmarcoAnterior) == 0:
                                                                UmarcoAnterior = 1e-006
                                                            Umarco = 1 / (1 / UmarcoAnterior - RcontraventanaAnterior)
                                                        else:
                                                            Umarco = UmarcoAnterior
                                                    if nuevaGvidrio != False:
                                                        Gvidrio = float(nuevaGvidrio)
                                                    else:
                                                        Ganterior = vent.Gvidrio
                                                        if ('Estimadas' in vent.__tipo__ or vent.dobleVentana == True or 'Conocidas' in vent.__tipo__) and vent.dobleVentana == True:
                                                            GcontraventanaAnterior = 0.82
                                                            Gvidrio = Ganterior / GcontraventanaAnterior
                                                        else:
                                                            Gvidrio = Ganterior
                                                    if nuevaUdobleVentana != False:
                                                        UdobleVentana = nuevaUdobleVentana
                                                        GdobleVentana = nuevaGdobleVentana
                                                    elif ('Estimadas' in vent.__tipo__ or vent.dobleVentana == True or 'Conocidas' in vent.__tipo__) and vent.dobleVentana == True:
                                                        UdobleVentana = 1 / 0.18
                                                        GdobleVentana = 0.82
                                                    else:
                                                        UdobleVentana = ''
                                                        GdobleVentana = ''
                                                    if UdobleVentana != '' and GdobleVentana != '':
                                                        if float(Uvidrio) == 0:
                                                            Uvidrio = 1e-006
                                                        Ucambiar = 1 / (1 / Uvidrio + 1 / UdobleVentana)
                                                        Gcambiar = Gvidrio * GdobleVentana
                                                        if float(Umarco) == 0:
                                                            Umarco = 1e-006
                                                        UmarcoCambiar = 1 / (1 / Umarco + 1 / UdobleVentana)
                                                    else:
                                                        Ucambiar = Uvidrio
                                                        Gcambiar = Gvidrio
                                                        UmarcoCambiar = Umarco
                                                    vent.Uvidrio = Ucambiar
                                                    vent.Gvidrio = Gcambiar
                                                    vent.Umarco = UmarcoCambiar
                                                    if nuevosEltosSombra != False:
                                                        vent.elementosProteccionSolar = nuevosEltosSombra
                                                        Voladizo_L = nuevosEltosSombra[0]
                                                        Voladizo_D = nuevosEltosSombra[1]
                                                        Voladizo_H = nuevosEltosSombra[2]
                                                        Retranqueo_H = nuevosEltosSombra[3]
                                                        Retranqueo_W = nuevosEltosSombra[4]
                                                        Retranqueo_R = nuevosEltosSombra[5]
                                                        Lamas_Horizontales_BETA = nuevosEltosSombra[6]
                                                        Lamas_Verticales_BETA = nuevosEltosSombra[7]
                                                        Toldos_AnguloA = nuevosEltosSombra[8]
                                                        Toldos_OpacoA = nuevosEltosSombra[9]
                                                        Toldos_TranslucidoA = nuevosEltosSombra[10]
                                                        Toldos_AnguloB = nuevosEltosSombra[11]
                                                        Toldos_OpacoB = nuevosEltosSombra[12]
                                                        Toldos_TranslucidoB = nuevosEltosSombra[13]
                                                        Lucernarios_X = nuevosEltosSombra[14]
                                                        Lucernarios_Y = nuevosEltosSombra[15]
                                                        Lucernarios_Z = nuevosEltosSombra[16]
                                                        Voladizos_Si = nuevosEltosSombra[17]
                                                        Retranqueos_Si = nuevosEltosSombra[18]
                                                        Lamas_Horizontales_Si = nuevosEltosSombra[19]
                                                        Lamas_Verticales_Si = nuevosEltosSombra[20]
                                                        Toldos_Si = nuevosEltosSombra[21]
                                                        Lucernarios_Si = nuevosEltosSombra[22]
                                                        Otro_Si = nuevosEltosSombra[23]
                                                        OtroInvierno = nuevosEltosSombra[24][0]
                                                        OtroVerano = nuevosEltosSombra[24][1]
                                                        nuevosCorrectoresSombra = tablasValores.obtenerCorrectoresFactorSolar(orientacionVentana, Voladizo_L, Voladizo_D, Voladizo_H, Retranqueo_H, Retranqueo_W, Retranqueo_R, Lamas_Horizontales_BETA, Lamas_Verticales_BETA, Toldos_AnguloA, Toldos_OpacoA, Toldos_TranslucidoA, Toldos_AnguloB, Toldos_OpacoB, Toldos_TranslucidoB, Lucernarios_X, Lucernarios_Y, Lucernarios_Z, Voladizos_Si, Retranqueos_Si, Lamas_Horizontales_Si, Lamas_Verticales_Si, Lucernarios_Si, Toldos_Si, Otro_Si, OtroInvierno, OtroVerano)[0]
                                                        vent.correctorFSCTE = nuevosCorrectoresSombra[0]
                                                        vent.correctorFSInvierno = nuevosCorrectoresSombra[1]
                                                        vent.correctorFSVerano = nuevosCorrectoresSombra[2]
                                                    
                                                
                                            continue
                                            if u'Mejora de Puentes T\xc3\xa9rmicos' in self.medidasMejoraEnvolvente[i][1]:
                                                for j in range(len(self.puentesTermicosMejorados)):
                                                    if self.medidasMejoraEnvolvente[i][2][0] == True and 'Pilar integrado en fachada' == self.puentesTermicosMejorados[j][2] or self.medidasMejoraEnvolvente[i][2][1] != '':
                                                        self.puentesTermicosMejorados[j][3] = self.medidasMejoraEnvolvente[i][2][1]
                                                    
                                                    if self.medidasMejoraEnvolvente[i][2][2] == True and 'Pilar en Esquina' == self.puentesTermicosMejorados[j][2] or self.medidasMejoraEnvolvente[i][2][3] != '':
                                                        self.puentesTermicosMejorados[j][3] = self.medidasMejoraEnvolvente[i][2][3]
                                                    
                                                    if self.medidasMejoraEnvolvente[i][2][4] == True and 'Contorno de hueco' == self.puentesTermicosMejorados[j][2] or self.medidasMejoraEnvolvente[i][2][5] != '':
                                                        self.puentesTermicosMejorados[j][3] = self.medidasMejoraEnvolvente[i][2][5]
                                                    
                                                    if self.medidasMejoraEnvolvente[i][2][6] == True and 'Caja de Persiana' == self.puentesTermicosMejorados[j][2] or self.medidasMejoraEnvolvente[i][2][7] != '':
                                                        self.puentesTermicosMejorados[j][3] = self.medidasMejoraEnvolvente[i][2][7]
                                                    
                                                    if self.medidasMejoraEnvolvente[i][2][8] == True and 'Encuentro de fachada con forjado' == self.puentesTermicosMejorados[j][2] or self.medidasMejoraEnvolvente[i][2][9] != '':
                                                        self.puentesTermicosMejorados[j][3] = self.medidasMejoraEnvolvente[i][2][9]
                                                    
                                                    if self.medidasMejoraEnvolvente[i][2][10] == True and 'Encuentro de fachada con voladizo' == self.puentesTermicosMejorados[j][2] or self.medidasMejoraEnvolvente[i][2][11] != '':
                                                        self.puentesTermicosMejorados[j][3] = self.medidasMejoraEnvolvente[i][2][11]
                                                    
                                                    if self.medidasMejoraEnvolvente[i][2][12] == True and 'Encuentro de fachada con cubierta' == self.puentesTermicosMejorados[j][2] or self.medidasMejoraEnvolvente[i][2][13] != '':
                                                        self.puentesTermicosMejorados[j][3] = self.medidasMejoraEnvolvente[i][2][13]
                                                    
                                                    if self.medidasMejoraEnvolvente[i][2][14] == True and 'Encuentro de fachada con suelo en contacto con el aire' == self.puentesTermicosMejorados[j][2] or self.medidasMejoraEnvolvente[i][2][15] != '':
                                                        self.puentesTermicosMejorados[j][3] = self.medidasMejoraEnvolvente[i][2][15]
                                                    
                                                    if self.medidasMejoraEnvolvente[i][2][16] == True and 'Encuentro de fachada con solera' == self.puentesTermicosMejorados[j][2] or self.medidasMejoraEnvolvente[i][2][17] != '':
                                                        self.puentesTermicosMejorados[j][3] = self.medidasMejoraEnvolvente[i][2][17]
                                                    
                                                
                                            return None

    
    def obtenerDatosLibreriaVidrios(self, nombre):
        '''
        Metodo: obtenerDatosLibreriaVidrios


        ARGUMENTOS:
    \t\tnombre:
        '''
        datos = cargaBD.cargarVidrio(nombre)
        return [
            datos[3],
            datos[2]]

    
    def obtenerPermeabilidadClase(self, clase):
        '''
        Metodo: obtenerPermeabilidadClase


        ARGUMENTOS:
    \t\tclase:
        '''
        if clase == 'Clase 0 (no ensayada)':
            return 100
        if None == 'Clase 1':
            return 50
        if None == 'Clase 2':
            return 27
        if None == 'Clase 3':
            return 8
        if None == 'Clase 4':
            return 3

    
    def obtenerUmarcoLibreria(self, nombre):
        '''
        Metodo: obtenerUmarcoLibreria


        ARGUMENTOS:
    \t\tnombre:
        '''
        dato = cargaBD.cargarMarco(nombre)
        return [
            dato[3],
            dato[2]]

    
    def obtenerDatosDobleVentana(self, dobleVentana):
        '''
        Metodo: obtenerDatosDobleVentana


        ARGUMENTOS:
    \t\tdobleVentana:
        '''
        if dobleVentana == 'Vidrio Simple':
            return [
                5.7,
                0.82]
        if None == 'Vidrio Doble':
            return [
                3.3,
                0.75]
        return [
            None,
            '']

    
    def calificacion(self):
        '''
        Metodo: calcular
        '''
        self.obtenerEnvolvente(self.datosEdificioOriginal.datosIniciales.cerramientos, self.datosEdificioOriginal.datosIniciales.huecos, self.datosEdificioOriginal.datosIniciales.puentesTermicos)
        self.datosInstalaciones = self.obtenerInstalaciones(self.mejoras, self.datosEdificioOriginal)
        self.obtenerMedidas(self.mejoras)
        self.incluirMedidas(self.datosEdificioOriginal.datosIniciales.cerramientos)
        nuevaEnvolvente = [
            self.cerramientosMejorados,
            self.huecosMejorados,
            self.puentesTermicosMejorados]
        if self.datosEdificioOriginal.programa == 'Residencial':
            zonaCalificacion = ''
            self.datosNuevoEdificio = datosEdificio.datosEdificio(datosGenerales = self.datosEdificioOriginal.datosGenerales, datosEnvolvente = nuevaEnvolvente, datosInstalaciones = self.datosInstalaciones, programa = self.datosEdificioOriginal.programa, subgrupos = self.datosEdificioOriginal.subgrupos, datosSombras = self.datosEdificioOriginal.datosSombras, escala = self.datosEdificioOriginal.escala, esEdificioExistente = self.datosEdificioOriginal.esEdificioExistente)
            self.datosNuevoEdificio.calificacion()
        else:
            zonaCalificacion = ''
            self.datosNuevoEdificio = datosEdificio.datosEdificioTerciario(datosGenerales = self.datosEdificioOriginal.datosGenerales, datosEnvolvente = nuevaEnvolvente, datosInstalaciones = self.datosInstalaciones, programa = self.datosEdificioOriginal.programa, subgrupos = self.datosEdificioOriginal.subgrupos, datosSombras = self.datosEdificioOriginal.datosSombras, escala = self.datosEdificioOriginal.escala, esEdificioExistente = self.datosEdificioOriginal.esEdificioExistente)
            self.datosNuevoEdificio.calificacion()
        if self.datosNuevoEdificio.casoValido == True:
            self.calcularAhorros()

    
    def calcularAhorros(self):
        '''
        Metodo: calcularAhorros
        '''
        
        try:
            ahorro0 = round(((self.datosEdificioOriginal.datosResultados.ddaBrutaCal - self.datosNuevoEdificio.datosResultados.ddaBrutaCal) / self.datosEdificioOriginal.datosResultados.ddaBrutaCal) * 100, 1)
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            if self.datosNuevoEdificio.datosResultados.ddaBrutaCal == 0:
                ahorro0 = 0
            else:
                ahorro0 = -100

        
        try:
            ahorro1 = round(((self.datosEdificioOriginal.datosResultados.ddaBrutaRef - self.datosNuevoEdificio.datosResultados.ddaBrutaRef) / self.datosEdificioOriginal.datosResultados.ddaBrutaRef) * 100, 1)
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            if self.datosNuevoEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
                ahorro1 = 0
            elif self.datosNuevoEdificio.datosResultados.ddaBrutaRef == 0:
                ahorro1 = 0
            else:
                ahorro1 = -100

        
        try:
            ahorro2 = round(((self.datosEdificioOriginal.datosResultados.emisionesCal - self.datosNuevoEdificio.datosResultados.emisionesCal) / self.datosEdificioOriginal.datosResultados.emisionesCal) * 100, 1)
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            if self.datosNuevoEdificio.datosResultados.emisionesCal == 0:
                ahorro2 = 0
            else:
                ahorro2 = -100

        
        try:
            ahorro3 = round(((self.datosEdificioOriginal.datosResultados.emisionesRef - self.datosNuevoEdificio.datosResultados.emisionesRef) / self.datosEdificioOriginal.datosResultados.emisionesRef) * 100, 1)
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            if self.datosNuevoEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
                ahorro3 = 0
            elif self.datosNuevoEdificio.datosResultados.emisionesRef == 0:
                ahorro3 = 0
            else:
                ahorro3 = -100

        
        try:
            ahorro4 = round(((self.datosEdificioOriginal.datosResultados.emisionesACS - self.datosNuevoEdificio.datosResultados.emisionesACS) / self.datosEdificioOriginal.datosResultados.emisionesACS) * 100, 1)
        except:
            if self.datosNuevoEdificio.datosResultados.emisionesACS == 0:
                ahorro4 = 0
            else:
                ahorro4 = -100

        
        try:
            ahorro5 = round(((self.datosEdificioOriginal.datosResultados.emisionesMostrar - self.datosNuevoEdificio.datosResultados.emisionesMostrar) / self.datosEdificioOriginal.datosResultados.emisionesMostrar) * 100, 1)
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            if self.datosNuevoEdificio.datosResultados.emisionesMostrar == 0:
                ahorro5 = 0
            else:
                ahorro5 = -100

        if self.datosEdificioOriginal.programa == 'Residencial':
            self.ahorro = [
                ahorro0,
                ahorro1,
                ahorro2,
                ahorro3,
                ahorro4,
                ahorro5]
        else:
            
            try:
                ahorroIluminacion = round(((self.datosEdificioOriginal.datosResultados.emisionesIlum - self.datosNuevoEdificio.datosResultados.emisionesIlum) / self.datosEdificioOriginal.datosResultados.emisionesIlum) * 100, 1)
            except:
                logging.info(u'Excepcion en: %s' % __name__)
                if self.datosNuevoEdificio.datosResultados.emisionesIlum == 0:
                    ahorroIluminacion = 0
                else:
                    ahorroIluminacion = -100

            self.ahorro = [
                ahorro0,
                ahorro1,
                ahorro2,
                ahorro3,
                ahorro4,
                ahorroIluminacion,
                ahorro5]



class AnalisisEconomicoConjuntoMM:
    
    def __init__(self, vidaUtil = [], inversionInicial = [], costeMantenimiento = []):
        '''
        VidaUtil, inversionInicial y costeMantenimiento son arrays de longitud el numero de medidas del conjunto
        '''
        self.vidaUtil = vidaUtil
        self.inversionInicial = inversionInicial
        self.costeMantenimiento = costeMantenimiento
        self.analisisTeorico = ResultadoAnalisisEconomicoConjuntoMM()
        self.analisisFacturas = ResultadoAnalisisEconomicoConjuntoMM()

    
    def inicializar(self):
        self.inicializarAnalisisTeorico()
        self.inicializarAnalisisFacturas()

    
    def inicializarAnalisisTeorico(self):
        self.analisisTeorico = ResultadoAnalisisEconomicoConjuntoMM()

    
    def inicializarAnalisisFacturas(self):
        self.analisisFacturas = ResultadoAnalisisEconomicoConjuntoMM()



class ResultadoAnalisisEconomicoConjuntoMM:
    
    def __init__(self, van = '', payBack = '', precioAnual_CB = '', precioAnual_CM = '', ahorroEconomico = ''):
        '''
        resultadosCB y resultadosCM son atributos que contienen un objeto, para poder
        almacenar informaci\xf3n del c\xe1lculo del an\xe1lisis seg\xfan facturas 
        '''
        self.van = van
        self.payBack = payBack
        self.precioAnual_CB = precioAnual_CB
        self.precioAnual_CM = precioAnual_CM
        self.ahorroEconomico = ahorroEconomico
        self.resultadosCB = ResultadoDemandasyConsumosAnalisisEconomicoConjuntoMM()
        self.resultadosCM = ResultadoDemandasyConsumosAnalisisEconomicoConjuntoMM()

    
    def guardarResultados(self, van = '', payBack = '', precioAnual_CB = '', precioAnual_CM = '', ahorroEconomico = ''):
        self.van = van
        self.payBack = payBack
        self.precioAnual_CB = precioAnual_CB
        self.precioAnual_CM = precioAnual_CM
        self.ahorroEconomico = ahorroEconomico



class ResultadoDemandasyConsumosAnalisisEconomicoConjuntoMM:
    '''
    Se utiliza solo para almacenar los datos a partir de las facturas
    En el an\xe1lisis te\xf3rico no se utiliza pq los datos est\xe1n en datosEdificio
    '''
    
    def __init__(self, diccCal = { }, diccRef = { }, diccACS = { }, diccIlum = { }, diccVentiladores = { }, diccBombas = { }, diccTorresRef = { }, diccContribuciones = { }, ddaBrutaCal = 0, ddaBrutaRef = 0, ddaBrutaACS = 0, ddaNetaCal = 0, ddaNetaRef = 0, ddaNetaACS = 0):
        self.diccCal = diccCal
        self.diccRef = diccRef
        self.diccACS = diccACS
        self.diccIlum = diccIlum
        self.diccVentiladores = diccVentiladores
        self.diccBombas = diccBombas
        self.diccTorresRef = diccTorresRef
        self.diccContribuciones = diccContribuciones
        self.ddaBrutaCal = ddaBrutaCal
        self.ddaBrutaRef = ddaBrutaRef
        self.ddaBrutaACS = ddaBrutaACS
        self.ddaNetaCal = ddaNetaCal
        self.ddaNetaRef = ddaNetaRef
        self.ddaNetaACS = ddaNetaACS


