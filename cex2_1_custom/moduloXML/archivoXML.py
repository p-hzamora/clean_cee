# File: a (Python 2.7)

from Calculos.listados import versionXML, versionDatosEnergeticosXML
from lxml import etree
import codecs

class ArchivoXML:
    
    def __init__(self, versionXML = '%s' % versionXML, versionDatosEnergeticosXML = '%s' % versionDatosEnergeticosXML, encoding = 'utf-8'):
        self.versionXML = versionXML
        self.versionDatosEnergeticosXML = versionDatosEnergeticosXML
        self.encoding = encoding
        self.xml = etree.Element('DatosEnergeticosDelEdificio')
        self.xml.set('version', self.versionDatosEnergeticosXML)
        self.logErrores = []

    
    def DatosDelCertificador(self, **kwargs):
        datos = etree.SubElement(self.xml, 'DatosDelCertificador')
        for clave in kwargs.keys():
            elemento = etree.SubElement(datos, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def IdentificacionEdificio(self, **kwargs):
        datos = etree.SubElement(self.xml, 'IdentificacionEdificio')
        for clave in kwargs.keys():
            if clave == 'ReferenciaCatastral':
                listadoRefCatast = ''
                for rc in kwargs[clave]:
                    if listadoRefCatast != '':
                        listadoRefCatast += ', '
                    listadoRefCatast += '%s' % rc
                
                elemento = etree.SubElement(datos, clave)
                elemento.text = unicode(listadoRefCatast)
                continue
            elemento = etree.SubElement(datos, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def DatosGeneralesyGeometria(self, **kwargs):
        datos = etree.SubElement(self.xml, 'DatosGeneralesyGeometria')
        for clave in kwargs.keys():
            elemento = etree.SubElement(datos, clave)
            elemento.text = unicode(kwargs[clave])
        
        elemento = etree.SubElement(datos, 'PorcentajeSuperficieAcristalada')

    
    def PorcentajeSuperficieAcristalada(self, **kwargs):
        d1 = self.xml.find('DatosGeneralesyGeometria')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'DatosGeneralesyGeometria')
        d2 = d1.find('PorcentajeSuperficieAcristalada')
        if d2 == None:
            d2 = etree.SubElement(d1, 'PorcentajeSuperficieAcristalada')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d2, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def CerramientoOpaco(self, **kwargs):
        '''
        Dentro de cerramiento Opaco est\xe1n Capas. Dentro hay Capa para cada una de las capas del cerramiento
        Pasamos un listado de capas. Cada elemento de la lista en un diccionario con los datos de cada capa.
        '''
        d1 = self.xml.find('DatosEnvolventeTermica')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'DatosEnvolventeTermica')
        d2 = d1.find('CerramientosOpacos')
        if d2 == None:
            d2 = etree.SubElement(d1, 'CerramientosOpacos')
        d3 = etree.SubElement(d2, 'Elemento')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d3, clave)
            contenido = kwargs[clave]
            if type(contenido) != list:
                elemento.text = unicode(contenido)
                continue
            d4 = d3.find('Capas')
            if d4 == None:
                d4 = etree.SubElement(d1, 'Capas')
            for capaDict in contenido:
                d5 = etree.SubElement(d4, 'Capa')
                for key in capaDict.keys():
                    elementoSegundoNivel = etree.SubElement(d5, key)
                    elementoSegundoNivel.text = unicode(capaDict[key])
                
            
        

    
    def Hueco(self, **kwargs):
        d1 = self.xml.find('DatosEnvolventeTermica')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'DatosEnvolventeTermica')
        d2 = d1.find('HuecosyLucernarios')
        if d2 == None:
            d2 = etree.SubElement(d1, 'HuecosyLucernarios')
        d3 = etree.SubElement(d2, 'Elemento')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d3, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def PuenteTermico(self, **kwargs):
        d1 = self.xml.find('DatosEnvolventeTermica')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'DatosEnvolventeTermica')
        d2 = d1.find('PuentesTermicos')
        if d2 == None:
            d2 = etree.SubElement(d1, 'PuentesTermicos')
        d3 = etree.SubElement(d2, 'Elemento')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d3, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def GeneradorDeCalefaccion(self, **kwargs):
        d1 = self.xml.find('InstalacionesTermicas')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'InstalacionesTermicas')
        d2 = d1.find('GeneradoresDeCalefaccion')
        if d2 == None:
            d2 = etree.SubElement(d1, 'GeneradoresDeCalefaccion')
        d3 = etree.SubElement(d2, 'Generador')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d3, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def GeneradorDeRefrigeracion(self, **kwargs):
        d1 = self.xml.find('InstalacionesTermicas')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'InstalacionesTermicas')
        d2 = d1.find('GeneradoresDeRefrigeracion')
        if d2 == None:
            d2 = etree.SubElement(d1, 'GeneradoresDeRefrigeracion')
        d3 = etree.SubElement(d2, 'Generador')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d3, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def InstalacionACS(self, **kwargs):
        d1 = self.xml.find('InstalacionesTermicas')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'InstalacionesTermicas')
        d2 = d1.find('InstalacionesACS')
        if d2 == None:
            d2 = etree.SubElement(d1, 'InstalacionesACS')
        d3 = etree.SubElement(d2, 'Instalacion')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d3, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def SistemasSecundarios(self, **kwargs):
        d1 = self.xml.find('InstalacionesTermicas')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'InstalacionesTermicas')
        d2 = self.xml.find('SistemasSecundariosCalefaccionRefrigeracion')
        if d2 == None:
            d2 = etree.SubElement(d1, 'SistemasSecundariosCalefaccionRefrigeracion')

    
    def TorreRefrigeracion(self, **kwargs):
        d1 = self.xml.find('InstalacionesTermicas')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'InstalacionesTermicas')
        d2 = d1.find('TorresyRefrigeracion')
        if d2 == None:
            d2 = etree.SubElement(d1, 'TorresyRefrigeracion')
        d3 = etree.SubElement(d2, 'Sistema')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d3, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def VentilacionYBombeo(self, **kwargs):
        d1 = self.xml.find('InstalacionesTermicas')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'InstalacionesTermicas')
        d2 = d1.find('VentilacionyBombeo')
        if d2 == None:
            d2 = etree.SubElement(d1, 'VentilacionyBombeo')
        d3 = etree.SubElement(d2, 'Sistema')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d3, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def EquipoDeAirePrimario(self, **kwargs):
        d1 = self.xml.find('InstalacionesTermicas')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'InstalacionesTermicas')
        d2 = d1.find('EquiposDeAirePrimario')
        if d2 == None:
            d2 = etree.SubElement(d1, 'EquiposDeAirePrimario')
        d3 = etree.SubElement(d2, 'EquipoAirePrimario')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d3, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def PotenciaTotalInstaladaIluminacion(self, **kwargs):
        d1 = self.xml.find('InstalacionesIluminacion')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'InstalacionesIluminacion')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d1, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def InstalacionIluminacion(self, **kwargs):
        d1 = self.xml.find('InstalacionesIluminacion')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'InstalacionesIluminacion')
            potenciaTotalInstalada = etree.SubElement(d1, 'PotenciaTotalInstalada')
        d2 = etree.SubElement(d1, 'Espacio')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d2, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def CondicionesFuncionamientoyOcupacion(self, **kwargs):
        d1 = self.xml.find('CondicionesFuncionamientoyOcupacion')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'CondicionesFuncionamientoyOcupacion')
        d2 = etree.SubElement(d1, 'Espacio')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d2, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def EnergiaRenovable(self, **kwargs):
        d1 = self.xml.find('EnergiasRenovables')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'EnergiasRenovables')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d1, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def EnergiaRenovableTermica(self, **kwargs):
        d1 = self.xml.find('EnergiasRenovables')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'EnergiasRenovables')
        d2 = d1.find('Termica')
        if d2 == None:
            d2 = etree.SubElement(d1, 'Termica')
        d3 = etree.SubElement(d2, 'Sistema')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d3, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def EnergiaRenovableElectrica(self, **kwargs):
        d1 = self.xml.find('EnergiasRenovables')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'EnergiasRenovables')
        d2 = d1.find('Electrica')
        if d2 == None:
            d2 = etree.SubElement(d1, 'Electrica')
        d3 = etree.SubElement(d2, 'Sistema')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d3, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def DemandaEdificioObjeto(self, **kwargs):
        d1 = self.xml.find('Demanda')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'Demanda')
        d2 = etree.SubElement(d1, 'EdificioObjeto')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d2, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def DemandaEdificioDeReferencia(self, **kwargs):
        d1 = self.xml.find('Demanda')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'Demanda')
        d2 = etree.SubElement(d1, 'EdificioDeReferencia')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d2, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def DemandaExigencias(self, **kwargs):
        d1 = self.xml.find('Demanda')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'Demanda')
        d2 = etree.SubElement(d1, 'Exigencias')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d2, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def ConsumoFactoresdePasoFinalAPrimariaNoRenovable(self, **kwargs):
        d1 = self.xml.find('Consumo')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'Consumo')
        d2 = d1.find('FactoresdePaso')
        if d2 == None:
            d2 = etree.SubElement(d1, 'FactoresdePaso')
        d3 = d2.find('FinalAPrimariaNoRenovable')
        if d3 == None:
            d3 = etree.SubElement(d2, 'FinalAPrimariaNoRenovable')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d3, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def ConsumoFactoresdePasoFinalAEmisiones(self, **kwargs):
        d1 = self.xml.find('Consumo')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'Consumo')
        d2 = d1.find('FactoresdePaso')
        if d2 == None:
            d2 = etree.SubElement(d1, 'FactoresdePaso')
        d3 = d2.find('FinalAEmisiones')
        if d3 == None:
            d3 = etree.SubElement(d2, 'FinalAEmisiones')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d3, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def ConsumoEnergiaPrimariaNoRenovable(self, **kwargs):
        d1 = self.xml.find('Consumo')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'Consumo')
        d2 = d1.find('EnergiaPrimariaNoRenovable')
        if d2 == None:
            d2 = etree.SubElement(d1, 'EnergiaPrimariaNoRenovable')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d2, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def ConsumoEnergiaFinal(self, **kwargs):
        d1 = self.xml.find('Consumo')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'Consumo')
        d2 = d1.find('EnergiaFinalVectores')
        if d2 == None:
            d2 = etree.SubElement(d1, 'EnergiaFinalVectores')
        d3 = d2.find(kwargs['Combustible'])
        if d3 == None:
            d3 = etree.SubElement(d2, kwargs['Combustible'])
        for clave in kwargs.keys():
            if clave != 'Combustible':
                elemento = etree.SubElement(d3, clave)
                elemento.text = unicode(kwargs[clave])
                continue

    
    def ConsumoExigencias(self, **kwargs):
        d1 = self.xml.find('Consumo')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'Consumo')
        d2 = d1.find('Exigencias')
        if d2 == None:
            d2 = etree.SubElement(d1, 'Exigencias')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d2, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def EmisionesCO2(self, **kwargs):
        d1 = self.xml.find('EmisionesCO2')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'EmisionesCO2')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d1, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def CalificacionEmisionesCO2(self, **kwargs):
        d1 = self.xml.find('Calificacion')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'Calificacion')
        d2 = d1.find('EmisionesCO2')
        if d2 == None:
            d2 = etree.SubElement(d1, 'EmisionesCO2')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d2, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def CalificacionDemanda(self, **kwargs):
        d1 = self.xml.find('Calificacion')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'Calificacion')
        d2 = d1.find('Demanda')
        if d2 == None:
            d2 = etree.SubElement(d1, 'Demanda')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d2, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def CalificacionEnergiaPrimariaNoRenovable(self, **kwargs):
        d1 = self.xml.find('Calificacion')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'Calificacion')
        d2 = d1.find('EnergiaPrimariaNoRenovable')
        if d2 == None:
            d2 = etree.SubElement(d1, 'EnergiaPrimariaNoRenovable')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d2, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def EscalaDemandaCalefaccion(self, **kwargs):
        d1 = self.xml.find('Calificacion')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'Calificacion')
        d2 = d1.find('Demanda')
        if d2 == None:
            d2 = etree.SubElement(d1, 'Demanda')
        d3 = d2.find('EscalaCalefaccion')
        if d3 == None:
            d3 = etree.SubElement(d2, 'EscalaCalefaccion')
        lista = kwargs.keys()
        lista.sort()
        for clave in lista:
            elemento = etree.SubElement(d3, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def EscalaDemandaRefrigeracion(self, **kwargs):
        d1 = self.xml.find('Calificacion')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'Calificacion')
        d2 = d1.find('Demanda')
        if d2 == None:
            d2 = etree.SubElement(d1, 'Demanda')
        d3 = d2.find('EscalaRefrigeracion')
        if d3 == None:
            d3 = etree.SubElement(d2, 'EscalaRefrigeracion')
        lista = kwargs.keys()
        lista.sort()
        for clave in lista:
            elemento = etree.SubElement(d3, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def EscalaEnPrimNoRen(self, **kwargs):
        d1 = self.xml.find('Calificacion')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'Calificacion')
        d2 = d1.find('EnergiaPrimariaNoRenovable')
        if d2 == None:
            d2 = etree.SubElement(d1, 'EnergiaPrimariaNoRenovable')
        d3 = d2.find('EscalaGlobal')
        if d3 == None:
            d3 = etree.SubElement(d2, 'EscalaGlobal')
        lista = kwargs.keys()
        lista.sort()
        for clave in lista:
            elemento = etree.SubElement(d3, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def EscalaEmisiones(self, **kwargs):
        d1 = self.xml.find('Calificacion')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'Calificacion')
        d2 = d1.find('EmisionesCO2')
        if d2 == None:
            d2 = etree.SubElement(d1, 'EmisionesCO2')
        d3 = d2.find('EscalaGlobal')
        if d3 == None:
            d3 = etree.SubElement(d2, 'EscalaGlobal')
        lista = kwargs.keys()
        lista.sort()
        for clave in lista:
            elemento = etree.SubElement(d3, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def MedidaDeMejora(self, **kwargs):
        """En los campos Demanda, CalificacionDemanda,EnergiaPrimariaNoRenovable, ...
           hay que pasar un diccionario con los campos del siguiente nivel
           ejemplo:

           xml.MedidaDeMejora(Descripcion = u'La mejor medida del mundo', Demanda={'Global':183.10,'GlobalDiferenciaSituacionInicial':34.00})
           """
        d1 = self.xml.find('MedidasDeMejora')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'MedidasDeMejora')
        d2 = etree.SubElement(d1, 'Medida')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d2, clave)
            contenido = kwargs[clave]
            if type(contenido) != dict:
                elemento.text = unicode(contenido)
                continue
            for clave2 in contenido.keys():
                elementoSegundoNivel = etree.SubElement(elemento, clave2)
                elementoSegundoNivel.text = unicode(contenido[clave2])
            
        

    
    def PruebasComprobacionesInspecciones(self, **kwargs):
        d1 = self.xml.find('PruebasComprobacionesInspecciones')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'PruebasComprobacionesInspecciones')
        d2 = self.xml.find('Visita')
        if d2 == None:
            d2 = etree.SubElement(d1, 'Visita')
        for clave in kwargs.keys():
            elemento = etree.SubElement(d2, clave)
            elemento.text = unicode(kwargs[clave])
        

    
    def DatosPersonalizados(self, **kwargs):
        '''Le llega un diccionario. La key ser\xe1 la <clave> y el otro elemento sera el contenido. Adem\xe1s el segundo elemento a la vez puede ser un diccionario.
           '''
        d1 = self.xml.find('DatosPersonalizados')
        if d1 == None:
            d1 = etree.SubElement(self.xml, 'DatosPersonalizados')
        for clave in kwargs:
            elemento = etree.SubElement(d1, clave)
            contenido = kwargs[clave]
            if type(contenido) != dict:
                elemento.text = unicode(contenido)
                continue
            for clave2 in contenido.keys():
                elementoSegundoNivel = etree.SubElement(elemento, clave2)
                elementoSegundoNivel.text = unicode(contenido[clave2])
            
        

    
    def SacarLosErrores(self, nombreArchivo):
        if self.logErrores != []:
            print 'En el archivo %s se han producido las siguientes incidencias:' % nombreArchivo
            for i in self.logErrores:
                print '\t- %s' % i
            

    
    def imprime(self):
        aux = etree.tostring(self.xml, pretty_print = True, encoding = self.encoding)
        return aux

    imprime = property(imprime)
    
    def grabaArchivo(self, ruta):
        f1 = open(ruta, 'w')
        f1.write('<?xml version="%s" encoding="%s" ?>\n' % (self.versionXML, self.encoding.upper()))
        f1.write(self.imprime)
        f1.close()


if __name__ == '__main__':
    xml = ArchivoXML(encoding = 'UTF-8')
    xml.DatosDelCertificador(nombre = u'Miguel \xc3\x81ngel', vehiculo = u'cami\xc3\xb3n')
    print xml.imprime
    xml.grabaArchivo('c:\\temp\\xml.xml')
