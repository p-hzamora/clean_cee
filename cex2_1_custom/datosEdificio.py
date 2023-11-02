# Embedded file name: datosEdificio.pyc
"""
Modulo: datosEdificio.py

"""
from Calculos.factoresKHuecos import factorKHuecosResidencial, factorKHuecosTerciario
from Calculos.funcionesCalculo import *
from Calculos.ganaciasSolaresOpacos import calculoGananciaSolarOpacosResidencial, calculoGananciaSolarOpacosTerciario
from Calculos.limitesCTEyEdifRef import *
import BD.leerBDDesdeArchivo as leerBDDesdeArchivo
import Calculos.calculoInfiltraciones as calculoInfiltraciones
import Calculos.calculoPerdidasSombras as calculoPerdidasSombras
import Calculos.calculoSuperficies as calculoSuperficies
import Calculos.funcionFactorSombra as funcionFactorSombra
import Calculos.funcionIluminacionNatural as funcionIluminacionNatural
import copy
import directorios
import pickle
import logging
Directorio = directorios.BuscaDirectorios().Directorio

class datosEdificioIniciales():
    """
    Clase: datosEdificioIniciales del modulo datosEdificio.py
    
    
    """

    def __init__(self, parent):
        """
        Constructor de la clase
        
        """
        self.parent = parent
        self.normativaVigente = ''
        self.tipoEdificio = ''
        self.zonaHE1 = ''
        self.zonaHE4 = ''
        self.area = ''
        self.altura = ''
        self.inerciaParticionesInteriores = ''
        self.masaParticiones = ''
        self.extrapeninsular = False
        self.tasaVentilacion = 0.0
        self.BlowerDoorTest = []
        self.getDatosGenerales()
        if self.parent.casoValido == False:
            return
        self.cerramientos = self.parent.datosEnvolvente[0]
        self.huecos = self.parent.datosEnvolvente[1]
        self.puentesTermicos = self.parent.datosEnvolvente[2]
        self.listadoHuecos = copy.deepcopy(self.huecos)
        self.listadoCerramientos = self.getListadoCerramientos()
        self.listadoPT = self.getListadoPuentesTermicos()
        self.comprobarDatosEnvolvente()
        if self.parent.casoValido == False:
            return
        self.sistemasACS = self.parent.datosInstalaciones[0]
        self.sistemasCalefaccion = self.parent.datosInstalaciones[1]
        self.sistemasRefrigeracion = self.parent.datosInstalaciones[2]
        self.sistemasClimatizacion = self.parent.datosInstalaciones[3]
        self.sistemasMixto2 = self.parent.datosInstalaciones[4]
        self.sistemasMixto3 = self.parent.datosInstalaciones[5]
        self.sistemasContribuciones = self.parent.datosInstalaciones[6]
        if self.parent.programa != 'Residencial':
            self.sistemasIluminacion = self.parent.datosInstalaciones[7]
            self.sistemasVentilacion = self.parent.datosInstalaciones[8]
            if self.parent.programa == 'GranTerciario':
                self.sistemasIluminacion = calculoSuperficies.actualizarSuperficiesIluminacion(self.parent.subgrupos, self.area, self.sistemasIluminacion)
            self.potenciaIluminacion = self.calculoPotenciaIluminacion()
            self.numeroHoras = calculoNumeroHorasOcupacionEdificio(tipoUso=self.tipoEdificio)
            self.cargasInternas = calculoCargasEdificio(tipoUso=self.tipoEdificio, potenciaIluminacion=self.potenciaIluminacion, area=self.area)
        else:
            self.sistemasIluminacion = []
            self.sistemasVentilacion = []
            self.potenciaIluminacion = 0.0
            self.numeroHoras = 0.0
            self.cargasInternas = 0.0
        self.tasaEqVentilacionNeta, self.tasaEqVentilacionBruta = self.calculoEquiposVentilacion()
        if self.parent.programa == 'GranTerciario':
            self.sistemasVentiladores = self.parent.datosInstalaciones[9]
            self.sistemasBombas = self.parent.datosInstalaciones[10]
            self.sistemasTorresRefrigeracion = self.parent.datosInstalaciones[11]
        else:
            self.sistemasVentiladores = []
            self.sistemasBombas = []
            self.sistemasTorresRefrigeracion = []
        self.ACS, self.calefaccion, self.refrigeracion = self.getListadoInstalacionesGeneracion()
        self.comprobarDatosInstalaciones()
        if self.parent.casoValido == False:
            return
        self.contribuciones = self.getListadoContribuciones()

    def getDatosGenerales(self):
        """
        Metodo: getDatosGenerales
        
        """
        if self.parent.datosGenerales == []:
            self.parent.casoValido = False
            return
        self.normativaVigente = self.parent.datosGenerales[0]
        self.tipoEdificio = self.parent.datosGenerales[1]
        self.provincia = self.parent.datosGenerales[2]
        self.localidad = self.parent.datosGenerales[3]
        self.zonaHE1 = self.parent.datosGenerales[4]
        self.zonaHE4 = self.parent.datosGenerales[5]
        self.area = float(self.parent.datosGenerales[6])
        self.altura = float(self.parent.datosGenerales[7])
        self.numeroPlantas = float(self.parent.datosGenerales[8])
        self.Q_ACS = float(self.parent.datosGenerales[9])
        self.masaParticiones = self.parent.datosGenerales[10]
        if self.parent.programa == 'Residencial':
            if self.masaParticiones == 'Ligera':
                self.inerciaParticionesInteriores = 200.0 * self.area
            elif self.masaParticiones == 'Media':
                self.inerciaParticionesInteriores = 500.0 * self.area
            elif self.masaParticiones == 'Pesada':
                self.inerciaParticionesInteriores = 900.0 * self.area
        elif self.masaParticiones == 'Ligera':
            self.inerciaParticionesInteriores = 0 * self.area
        elif self.masaParticiones == 'Media':
            self.inerciaParticionesInteriores = 200.0 * self.area
        elif self.masaParticiones == 'Pesada':
            self.inerciaParticionesInteriores = 500.0 * self.area
        self.extrapeninsular = self.parent.datosGenerales[11]
        self.otroCuadro = self.parent.datosGenerales[12]
        self.BlowerDoorTest = self.parent.datosGenerales[13]
        self.tasaVentilacion = float(self.parent.datosGenerales[16])
        self.imagen = self.parent.datosGenerales[17]
        self.plano = self.parent.datosGenerales[18]
        self.annoConstruccion = self.parent.datosGenerales[19]
        self.tipoUsoTerciario = self.parent.datosGenerales[20]
        self.zonaHE1PeninsularOExtrapeninsular = self.getZonaHE1PeninsularOExtrapeninsular()
        superficieSubgrupos = 0
        for sub in self.parent.subgrupos:
            if sub.raiz == u'Edificio Objeto':
                superficieSubgrupos += float(sub.superficie)

        if superficieSubgrupos > self.area:
            self.parent.casoValido = False
            self.parent.mensajeAviso = _(u'La superficie de las zonas del edificio es mayor que la superficie del edificio')
            return

    def getZonaHE1PeninsularOExtrapeninsular(self):
        if self.extrapeninsular == True:
            zonaHE1PeninsularOExtrapeninsular = '%s%s' % (self.zonaHE1, '_extrapeninsular')
        else:
            zonaHE1PeninsularOExtrapeninsular = '%s%s' % (self.zonaHE1, '_peninsular')
        return zonaHE1PeninsularOExtrapeninsular

    def getListadoCerramientos(self):
        listadoCerramientos = []
        listadoMensajeAviso = []
        for i in self.cerramientos:
            nombreCerr = i[0]
            listadoHuecos = []
            for h in self.listadoHuecos:
                if h.cerramientoAsociado == nombreCerr:
                    listadoHuecos.append(h)

            cerr = Cerramiento(nombre=i[0], tipo=i[1], enContactoCon=i[-1], superficieBruta=i[2], superficieNeta=0.0, orientacion=i[5], patronSombras=u'Sin patr\xf3n', U=i[3], masaM2=i[4], subgrupo=i[-2], listadoHuecos=listadoHuecos, modoObtencion=i[8])
            if cerr.mensajeAviso != None:
                listadoMensajeAviso.append(cerr.mensajeAviso)
            listadoCerramientos.append(cerr)

        if len(listadoMensajeAviso) > 0.0:
            self.parent.casoValido = False
            listaErrores = ''
            for msn in listadoMensajeAviso:
                if listaErrores != '':
                    listaErrores += ', '
                listaErrores += unicode(msn)

            self.parent.mensajeAviso = _(u'La superficie de huecos en ') + listaErrores + _(u' es mayor que la superficie del cerramiento')
        return listadoCerramientos

    def getListadoPuentesTermicos(self):
        listadoPT = []
        for i in self.puentesTermicos:
            pt = PuenteTermico(nombre=i[0], tipo=i[2], fi=i[3], longitud=i[4], cerramientoAsociado=i[7], subgrupo=i[-1])
            listadoPT.append(pt)

        return listadoPT

    def comprobarDatosEnvolvente(self):
        """
        Metodo: valoresEnvolvente
        Se ha tomado la decisi\xf3n de permitir certificar con cualquier valor. 
        
        """
        return
        if self.listadoCerramientos == []:
            self.parent.casoValido = False
            self.parent.mensajeAviso = _(u'No se han indicado los cerramientos que componen la envolvente t\xe9rmica')
            return
        if self.listadoHuecos == []:
            self.parent.casoValido = False
            self.parent.mensajeAviso = _(u'No se han indicado los huecos que componen la envolvente t\xe9rmica')
            return
        superficieTotalHuecos = 0.0
        for h in self.listadoHuecos:
            superficieTotalHuecos += float(h.superficie)

        if superficieTotalHuecos == 0.0:
            self.parent.casoValido = False
            self.parent.mensajeAviso = _(u'La superficie de los huecos del edificio es cero, compruebe dicho valor')
            return
        if self.listadoPT == []:
            self.parent.casoValido = False
            self.parent.mensajeAviso = _(u'No se han indicado los puentes t\xe9rmicos')
            return

    def getListadoInstalacionesGeneracion(self):
        """
        Metodo: sacarListadoInstalaciones
        """
        listadoEquiposACS = ListadoEquipoGeneracion()
        listadoEquiposCal = ListadoEquipoGeneracion()
        listadoEquiposRef = ListadoEquipoGeneracion()
        for i in self.sistemasACS:
            obj = EquipoGeneracion(nombre=i[0], rendimiento=i[2][0], generador=i[3], combustible=i[4], coberturaM2=i[5][0][0], coberturaPorc=i[5][0][1], acumulacion=i[8], subgrupo=i[-1], modoObtencion=i[6], objListado=listadoEquiposACS)
            if obj.generador in (u'Caldera Est\xe1ndar', u'Caldera Condensaci\xf3n', u'Caldera Baja Temperatura') and obj.modoObtencion == u'Estimado seg\xfan Instalaci\xf3n' and obj.combustible != u'Electricidad':
                potencia = i[7][3]
                obj.potencia = potencia

        for i in self.sistemasCalefaccion:
            obj = EquipoGeneracion(nombre=i[0], rendimiento=i[2][1], generador=i[3], combustible=i[4], coberturaM2=i[5][1][0], coberturaPorc=i[5][1][1], subgrupo=i[-1], modoObtencion=i[6], objListado=listadoEquiposCal)
            if obj.generador in (u'Caldera Est\xe1ndar', u'Caldera Condensaci\xf3n', u'Caldera Baja Temperatura') and obj.modoObtencion == u'Estimado seg\xfan Instalaci\xf3n' and obj.combustible != u'Electricidad':
                potencia = i[7][3]
                obj.potencia = potencia

        for i in self.sistemasRefrigeracion:
            obj = EquipoGeneracion(nombre=i[0], rendimiento=i[2][2], generador=i[3], combustible=i[4], coberturaM2=i[5][2][0], coberturaPorc=i[5][2][1], subgrupo=i[-1], modoObtencion=i[6], objListado=listadoEquiposRef)

        for i in self.sistemasClimatizacion:
            objCal = EquipoGeneracion(nombre=i[0], rendimiento=i[2][1], generador=i[3], combustible=i[4], coberturaM2=i[5][1][0], coberturaPorc=i[5][1][1], subgrupo=i[-1], modoObtencion=i[6], objListado=listadoEquiposCal)
            objRef = EquipoGeneracion(nombre=i[0], rendimiento=i[2][2], generador=i[3], combustible=i[4], coberturaM2=i[5][2][0], coberturaPorc=i[5][2][1], subgrupo=i[-1], modoObtencion=i[6], objListado=listadoEquiposRef)

        for i in self.sistemasMixto2:
            objACS = EquipoGeneracion(nombre=i[0], rendimiento=i[2][0], generador=i[3], combustible=i[4], coberturaM2=i[5][0][0], coberturaPorc=i[5][0][1], acumulacion=i[8], subgrupo=i[-1], modoObtencion=i[6], objListado=listadoEquiposACS)
            objCal = EquipoGeneracion(nombre=i[0], rendimiento=i[2][1], generador=i[3], combustible=i[4], coberturaM2=i[5][1][0], coberturaPorc=i[5][1][1], subgrupo=i[-1], modoObtencion=i[6], objListado=listadoEquiposCal)
            if objACS.generador in (u'Caldera Est\xe1ndar', u'Caldera Condensaci\xf3n', u'Caldera Baja Temperatura') and objACS.modoObtencion == u'Estimado seg\xfan Instalaci\xf3n' and objACS.combustible != u'Electricidad':
                potencia = i[7][3]
                objACS.potencia = potencia
                objCal.potencia = potencia

        for i in self.sistemasMixto3:
            objACS = EquipoGeneracion(nombre=i[0], rendimiento=i[2][0], generador=i[3], combustible=i[4], coberturaM2=i[5][0][0], coberturaPorc=i[5][0][1], acumulacion=i[8], subgrupo=i[-1], modoObtencion=i[6], objListado=listadoEquiposACS)
            objCal = EquipoGeneracion(nombre=i[0], rendimiento=i[2][1], generador=i[3], combustible=i[4], coberturaM2=i[5][1][0], coberturaPorc=i[5][1][1], subgrupo=i[-1], modoObtencion=i[6], objListado=listadoEquiposCal)
            objRef = EquipoGeneracion(nombre=i[0], rendimiento=i[2][2], generador=i[3], combustible=i[4], coberturaM2=i[5][2][0], coberturaPorc=i[5][2][1], subgrupo=i[-1], modoObtencion=i[6], objListado=listadoEquiposRef)

        return (listadoEquiposACS, listadoEquiposCal, listadoEquiposRef)

    def comprobarDatosInstalaciones(self):
        """
        M\xe9todo: comprobarDatosInstalaciones
        Comprueba que no se cubre mas del 100 % de la dda de calefacci\xf3n y el 100 % de la dda de refrigeracion
        Comprueba que se cubre exactamente el 100 % de la dda de ACS
        """
        coberturaCal = self.calefaccion.coberturaM2 / self.area
        if coberturaCal >= 1.01:
            self.parent.casoValido = False
            self.parent.mensajeAviso = _(u'La instalaci\xf3n de calefacci\xf3n cubre una demanda superior al 100%')
            return
        coberturaRef = self.refrigeracion.coberturaM2 / self.area
        if coberturaRef >= 1.01:
            self.parent.casoValido = False
            self.parent.mensajeAviso = _(u'La instalaci\xf3n de refrigeraci\xf3n cubre una demanda superior al 100%')
            return
        if self.Q_ACS > 0.0:
            coberturaACS = self.ACS.coberturaM2 / self.area
            if coberturaACS <= 0.99 or coberturaACS >= 1.01:
                self.parent.casoValido = False
                self.parent.mensajeAviso = _(u'La instalaci\xf3n de ACS no est\xe1 bien definida. El porcentaje de demanda cubierta debe ser el 100 %.')
                return

    def calculoPotenciaIluminacion(self):
        """
        Metodo: calculoPotenciaIluminacion
        Calcula la potencia real de consumo de las lamparas en funcion de si hay control de la iluminacion o no
        """
        potenciaTotal = 0
        for inst in self.sistemasIluminacion:
            potencia = inst[2]
            zona = inst[-1]
            areaZona = float(inst[5])
            aux = inst[10]
            conControl = aux[0]
            if conControl == True:
                areaControl = float(aux[1])
                gVis = funcionIluminacionNatural.calculoRadiacionSolarHuecosParaIluminacion(listadoHuecos=self.listadoHuecos, areaInst=areaZona, zonaInst=zona)
                Em = float(inst[9][1])
                if gVis == 0.0:
                    fraccionamiento = 1.0
                else:
                    fraccionamiento = funcionIluminacionNatural.fraccionamientoConsumo(self.tipoEdificio, Em, gVis)
            else:
                areaControl = 0.0
                fraccionamiento = 1.0
            areaSinControl = areaZona - areaControl
            try:
                potencia = potencia * (areaSinControl + areaControl * fraccionamiento) / areaZona
            except ZeroDivisionError:
                potencia = 0.0

            potenciaTotal += potencia

        return potenciaTotal

    def getListadoContribuciones(self):
        listadoContribuciones = ListadoContribucionesEnergeticas()
        for i in self.sistemasContribuciones:
            obj = ContribucionesEnergeticas(nombre=i[0], porcACS=i[2][0], porcCal=i[2][1], porcRef=i[2][2], calorRecupACS=i[3][1], calorRecupCal=i[3][2], calorRecupRef=i[3][3], electricidadGen=i[3][0], enConsum=i[3][4], combustible=i[3][5], objListado=listadoContribuciones)

        return listadoContribuciones

    def calculoEquiposVentilacion(self):
        """
        Metodo: calculoEquiposVentilacion
        
        """
        caudalEqVentilacionNeta = 0.0
        caudalEqVentilacionBruta = 0.0
        for i in self.sistemasVentilacion:
            rend = float(i[4]) / 100
            caudalEqVentilacionNeta += float(i[2]) * (1 - rend)
            caudalEqVentilacionBruta += float(i[2])

        tasaEqVentilacionNeta = caudalEqVentilacionNeta / (self.altura * self.area)
        tasaEqVentilacionBruta = caudalEqVentilacionBruta / (self.altura * self.area)
        return (tasaEqVentilacionNeta, tasaEqVentilacionBruta)

    def crearEdificioReferencia(self):
        """
        Metodo: crearEdificioReferencia
        
        """
        self.sistemasACS = []
        self.sistemasCalefaccion = []
        self.sistemasRefrigeracion = []
        self.sistemasClimatizacion = []
        self.sistemasMixto2 = []
        self.sistemasMixto3 = []
        self.sistemasIluminacion = self.getListadoIluminacionReferencia()
        self.potenciaIluminacion = self.calculoPotenciaIluminacion()
        self.cargasInternas = calculoCargasEdificio(tipoUso=self.tipoEdificio, potenciaIluminacion=self.potenciaIluminacion, area=self.area)
        self.sistemasVentilacion = self.calculoSistemasVentilacionEdificioReferencia()
        self.sistemasVentiladores = []
        self.sistemasBombas = []
        self.sistemasTorresRefrigeracion = []
        self.sistemasContribuciones = []
        self.ACS, self.calefaccion, self.refrigeracion = self.getListadoInstalacionesGeneracionReferencia()
        self.tasaEqVentilacionNeta, self.tasaEqVentilacionBruta = self.calculoEquiposVentilacion()
        self.contribuciones = self.getListadoContribucionesReferencia()
        self.getEnvolventeReferencia()

    def calculoSistemasVentilacionEdificioReferencia(self):
        """
        Metodo: calculoSistemasVentilacionEdificioReferencia: devuelve lso sistemas de ventilacion del edificio de referencia, son
        iguales a los del edificio objeto pero sin recuperador de calor
        
        
        ARGUMENTOS:
            sistemasVentilacionObjeto: listado de sistemas de ventilacion del edificio objeto
        """
        sistemasVentilacionReferencia = []
        for sist in self.sistemasVentilacion:
            nombre = sist[0]
            tipoEquipo = sist[1]
            caudalVentilacion = sist[2]
            tieneRecuperador = False
            rendimientoRecuperador = 0.0
            subgrupo = sist[-1]
            nuevoSistema = [nombre,
             tipoEquipo,
             caudalVentilacion,
             tieneRecuperador,
             rendimientoRecuperador,
             subgrupo]
            sistemasVentilacionReferencia.append(nuevoSistema)

        return sistemasVentilacionReferencia

    def getListadoInstalacionesGeneracionReferencia(self):
        """
        Metodo: getListadoInstalacionesGeneracionReferencia
        Se crean objetos de tipo EquipoGeneracion, con las caracteristicas de la instalacion del edificio de referencia
        """
        listadoEquiposACS = ListadoEquipoGeneracion()
        listadoEquiposCal = ListadoEquipoGeneracion()
        listadoEquiposRef = ListadoEquipoGeneracion()
        obj = EquipoGeneracion(nombre=u'Equipo ACS edificio referencia', rendimiento=rendACSEdifRef, combustible=combACSEdifRef, coberturaM2=self.area, coberturaPorc=100.0, acumulacion=[False], objListado=listadoEquiposACS)
        obj = EquipoGeneracion(nombre=u'Equipo Cal edificio referencia', rendimiento=rendCalEdifRef, combustible=combCalEdifRef, coberturaM2=self.area, coberturaPorc=100.0, objListado=listadoEquiposCal)
        obj = EquipoGeneracion(nombre=u'Equipo Ref edificio referencia', rendimiento=rendRefEdifRef, combustible=combRefEdifRef, coberturaM2=self.area, coberturaPorc=100.0, objListado=listadoEquiposRef)
        return (listadoEquiposACS, listadoEquiposCal, listadoEquiposRef)

    def getListadoContribucionesReferencia(self):
        listadoContribuciones = ListadoContribucionesEnergeticas()
        porcACSEdificioReferencia = calculoContribucionSolarMinimaEdificioReferencia(zonaHE4=self.zonaHE4, Q_ACS=self.Q_ACS)
        obj = ContribucionesEnergeticas(porcACS=porcACSEdificioReferencia, objListado=listadoContribuciones)
        return listadoContribuciones

    def getListadoIluminacionReferencia(self):
        """
        Metodo: getListadoIluminacionReferencia
        Se modifica el array sistemasIluminacion indicando en potencia la que le corresponde al edificio de referencia en funcion del veeiRef
        """
        sistemasIluminacion = copy.deepcopy(self.sistemasIluminacion)
        for inst in sistemasIluminacion:
            Pobjeto = float(inst[2])
            actividad = inst[7]
            areaZona = float(inst[5])
            esZonaRepresentacion = inst[6]
            iluminancia = float(inst[9][1])
            control = [False, '']
            inst[10] = control
            VEEIRef = calculoVEEIIluminacionLimite(actividad=actividad, esEdificioReferencia=True, esZonaRepresentacion=esZonaRepresentacion)
            Preferencia = VEEIRef * areaZona * iluminancia / 100.0
            inst[2] = Preferencia

        return sistemasIluminacion

    def getEnvolventeReferencia(self):
        """
        Metodo: getEnvolventeReferencia
        """
        self.cambiarOrientacionNEyNOReferencia()
        self.getSuperficieListadoCerramientosYListadoHuecosReferencia()
        self.getHuecosReferencia()
        self.convertirCerrEnContactoTerrenoYParticionesInteriores()
        self.getCerramientosReferencia()
        self.getPTReferencia()

    def cambiarOrientacionNEyNOReferencia(self):
        """
        Metodo:cambiarOrientacionNEyNO
        Cambia en listadoCerramientos y listadoHuecos lo que tiene orientacion NO o NE a Norte
        """
        for cerr in self.listadoCerramientos:
            if cerr.orientacion in ('NO', 'NE'):
                cerr.orientacion = 'Norte'

        for h in self.listadoHuecos:
            if h.orientacion in ('NO', 'NE'):
                h.orientacion = 'Norte'

    def getSuperficiesCerramientosYHuecosEdificio(self, listadoCerramientos = [], listadoHuecos = []):
        """
        Metodo: getSuperficiesCerramientosYHuecosEdificio
        Devuelve en dicc la superficie total de cerr por orientacion, la 
        superficie total de huecos por orientacion y el porcentaje de huecos por orientacion
        Devuelve: diccPorcHuecos, diccSuperficieOpacos, diccSuperficieHuecos
        """
        diccPorcHuecos = {'Norte': 0.0,
         'NO': 0.0,
         'NE': 0.0,
         'Este': 0.0,
         'Oeste': 0.0,
         'Sur': 0.0,
         'SE': 0.0,
         'SO': 0.0,
         'Techo': 0.0}
        diccSuperficieOpacos = {'Norte': 0.0,
         'NO': 0.0,
         'NE': 0.0,
         'Este': 0.0,
         'Oeste': 0.0,
         'Sur': 0.0,
         'SE': 0.0,
         'SO': 0.0,
         'Techo': 0.0}
        diccSuperficieHuecos = {'Norte': 0.0,
         'NO': 0.0,
         'NE': 0.0,
         'Este': 0.0,
         'Oeste': 0.0,
         'Sur': 0.0,
         'SE': 0.0,
         'SO': 0.0,
         'Techo': 0.0}
        for cerr in listadoCerramientos:
            if cerr.tipo in ('Fachada', 'Cubierta') and cerr.enContactoCon == 'aire':
                diccSuperficieOpacos[cerr.orientacion] += cerr.superficieBruta

        for h in listadoHuecos:
            diccSuperficieHuecos[h.orientacion] += float(h.superficie)

        for orientacion in diccPorcHuecos.keys():
            if diccSuperficieOpacos[orientacion] > 0.0:
                diccPorcHuecos[orientacion] = diccSuperficieHuecos[orientacion] / diccSuperficieOpacos[orientacion]

        return (diccPorcHuecos, diccSuperficieOpacos, diccSuperficieHuecos)

    def getSuperficieListadoCerramientosYListadoHuecosReferencia(self):
        """
        Metodo: getSuperficieListadoCerramientosYListadoHuecosReferencia
        Modifica los arrays listadoHuecos y listadoCerramientos para calcular la nueva superficie, si 
        los huecos superan el 60% de la superficie acristalada o el 5 % en el caso de cubiertas
        """
        diccPorcHuecos, diccSuperficieOpacos, diccSuperficieHuecos = self.getSuperficiesCerramientosYHuecosEdificio(listadoCerramientos=self.listadoCerramientos, listadoHuecos=self.listadoHuecos)
        diccFactorAjusteHuecos = {'Norte': 1.0,
         'Este': 1.0,
         'Oeste': 1.0,
         'Sur': 1.0,
         'SE': 1.0,
         'SO': 1.0,
         'Techo': 1.0}
        for orientacion in diccFactorAjusteHuecos.keys():
            if orientacion not in ('Techo',):
                if diccPorcHuecos[orientacion] > 0.6:
                    diccFactorAjusteHuecos[orientacion] = 0.6 / diccPorcHuecos[orientacion]
            elif diccPorcHuecos[orientacion] > 0.05:
                diccFactorAjusteHuecos[orientacion] = 0.05 / diccPorcHuecos[orientacion]

        for h in self.listadoHuecos:
            h.superficie = unicode(diccFactorAjusteHuecos[h.orientacion] * float(h.superficie))

        for cerr in self.listadoCerramientos:
            cerr.calculoSuperficieNeta()

    def convertirCerrEnContactoTerrenoYParticionesInteriores(self):
        """
        Metodo: convertirCerrEnContactoTerrenoYParticionesInteriores
        En edificio de referencia, los cerramientos en contacto con el terreno  y las particiones interiores
        pasan a ser cerramientos en contacto con el exterior
        """
        for cerr in self.listadoCerramientos:
            if cerr.tipo == 'Fachada' and cerr.enContactoCon == 'terreno':
                cerr.orientacion = 'Norte'
                cerr.enContactoCon = 'aire'
            elif cerr.tipo == 'Cubierta' and cerr.enContactoCon == 'terreno':
                cerr.orientacion = 'Techo'
                cerr.enContactoCon = 'aire'
            elif cerr.tipo == 'Suelo' and cerr.enContactoCon == 'terreno':
                cerr.orientacion = 'Suelo'
                cerr.enContactoCon = 'aire'
            elif cerr.tipo == u'Partici\xf3n Interior' and cerr.enContactoCon == 'vertical':
                cerr.tipo = 'Fachada'
                cerr.enContactoCon = 'aire'
                cerr.orientacion = 'Norte'
            elif cerr.tipo == u'Partici\xf3n Interior' and cerr.enContactoCon == 'horizontal inferior':
                cerr.tipo = 'Suelo'
                cerr.enContactoCon = 'aire'
                cerr.orientacion = 'Suelo'
            elif cerr.tipo == u'Partici\xf3n Interior' and cerr.enContactoCon == 'horizontal superior':
                cerr.tipo = 'Cubierta'
                cerr.enContactoCon = 'aire'
                cerr.orientacion = 'Techo'

    def getCerramientosReferencia(self):
        """
        Metodo: getCerramientosReferencia
        Se asigna a cerramientos opacos los valores del edificio de referencia
        """
        for cerr in self.listadoCerramientos:
            U_ref = getValoresLimiteCerr(zonaHE1=self.zonaHE1, tipo=cerr.tipo, enContactoCon=cerr.enContactoCon)
            Peso_ref = getMasaM2CerrReferencia(tipo=cerr.tipo, enContactoCon=cerr.enContactoCon)
            cerr.U = U_ref
            cerr.MasaM2 = Peso_ref
            cerr.patronSombras = u'Sin patr\xf3n'

    def getHuecosReferencia(self):
        """
        Metodo: getHuecosReferencia
        diccPorcHuecos: Diccionario que contiene el tanto por uno de huecos qeu hay en cada orientacion
        """
        if self.cargasInternas < 6.0:
            esBajaCarga = True
        else:
            esBajaCarga = False
        diccPorcHuecos, diccSuperficieOpacos, diccSuperficieHuecos = self.getSuperficiesCerramientosYHuecosEdificio(listadoCerramientos=self.listadoCerramientos, listadoHuecos=self.listadoHuecos)
        for h in self.listadoHuecos:
            porc_marco = float(h.porcMarco)
            if porc_marco > 50.0:
                pass
            else:
                porc_huecos = diccPorcHuecos[h.orientacion]
                if h.tipo == 'Hueco':
                    h.Uvidrio = getUlimiteHuecos(zonaHE1=self.zonaHE1, porc_huecos=porc_huecos, orientacion=h.orientacion)
                    h.Gvidrio = getFSHuecosInviernoReferencia(Uvidrio=h.Uvidrio)
                    FS_refrig_limite = getFSlimiteHuecos(zonaHE1=self.zonaHE1, porc_huecos=porc_huecos, orientacion=h.orientacion, esBajaCarga=esBajaCarga)
                else:
                    h.Uvidrio = getValoresLimiteCerr(zonaHE1=self.zonaHE1, tipo='Cubierta', enContactoCon='aire')
                    h.Gvidrio = 0.7
                    FS_refrig_limite = getValoresLimiteCerr(zonaHE1=self.zonaHE1, tipo='Lucernario')
                h.permeabilidadValor = getPermeabilidadLimiteHuecos(zonaHE1=self.zonaHE1)
                h.dobleVentana = False
                h.Umarco = 0.0
                h.porcMarco = 0.0
                h.tieneProteccionSolar = False
                h.elementosProteccionSolar[0] = ''
                h.elementosProteccionSolar[1] = ''
                h.elementosProteccionSolar[2] = ''
                Retranqueo_H = h.elementosProteccionSolar[3]
                Retranqueo_W = h.elementosProteccionSolar[4]
                Retranqueo_R = h.elementosProteccionSolar[5]
                h.elementosProteccionSolar[6] = ['', 0, 0]
                h.elementosProteccionSolar[7] = ['', 0, 0]
                h.elementosProteccionSolar[8] = ''
                h.elementosProteccionSolar[9] = False
                h.elementosProteccionSolar[10] = False
                h.elementosProteccionSolar[11] = ''
                h.elementosProteccionSolar[12] = False
                h.elementosProteccionSolar[13] = False
                h.elementosProteccionSolar[14] = ''
                h.elementosProteccionSolar[15] = ''
                h.elementosProteccionSolar[16] = ''
                h.elementosProteccionSolar[17] = False
                h.elementosProteccionSolar[19] = False
                h.elementosProteccionSolar[20] = False
                h.elementosProteccionSolar[21] = False
                h.elementosProteccionSolar[22] = False
                h.elementosProteccionSolar[23] = ''
                h.patronSombras = u'Sin patr\xf3n'
                if Retranqueo_H != '' and Retranqueo_W != '' and Retranqueo_R != '':
                    FS_RETRANQUEOS = float(funcionFactorSombra.Factor_Sombra_Retranqueo(Retranqueo_R, Retranqueo_H, Retranqueo_W, h.orientacion))
                    FS_RETRANQUEOS_calculos = funcionFactorSombra.Factor_Sombra_Retranqueo_Calculos(Retranqueo_R, Retranqueo_H, Retranqueo_W, h.orientacion)
                    FS_RETRANQUEOS_invierno = FS_RETRANQUEOS_calculos[0]
                    FS_RETRANQUEOS_verano = FS_RETRANQUEOS_calculos[1]
                    corrector_FS_sombras = FS_RETRANQUEOS
                    corrector_FS_invierno = FS_RETRANQUEOS_invierno
                    corrector_FS_verano = FS_RETRANQUEOS_verano
                    h.correctorFSCTE = corrector_FS_sombras
                    h.correctorFSInvierno = corrector_FS_invierno
                else:
                    h.correctorFSCTE = 1.0
                    h.correctorFSInvierno = 1.0
                    corrector_FS_verano = 1.0
                if FS_refrig_limite != '-':
                    correctorFSVerano_paraConseguirGvidrio = float(FS_refrig_limite) / float(h.Gvidrio)
                    nuevoCorrectorVerano = correctorFSVerano_paraConseguirGvidrio
                    h.correctorFSVerano = nuevoCorrectorVerano
                else:
                    h.correctorFSVerano = corrector_FS_verano

    def getPTReferencia(self):
        for pt in self.listadoPT:
            fi = getFiPTReferencia(zonaHE1=self.zonaHE1, tipo=pt.tipo)
            pt.fi = fi


class datosEdificioGlobales():
    """
    Clase: datosEdificioGlobales  del modulo datosEdificio.py
    
    
    """

    def __init__(self, parent, datosIniciales):
        """
        Constructor de la clase
        
        
        ARGUMENTOS:
                datosIniciales:
                datosSombras:
        """
        self.parent = parent
        self.dI = datosIniciales
        self.UA = 0.0
        self.UA_cerr = 0.0
        self.UA_cerr_verano = 0.0
        self.inercia = 0.0
        self.UA_vid = 0.0
        self.g_cal = 0.0
        self.g_ref = 0.0
        self.UA_PT = 0.0
        self.calculoVariablesGlobales()

    def calculoVariablesGlobales(self):
        """
        Metodo: calculoVariablesGlobales
        
        """
        calculoVentilacion = self.calculoVariablesGlobalesVentilacion()
        self.renh = float(calculoVentilacion) * float(self.dI.altura)
        self.UA_cerr, self.UA_cerr_verano, self.inercia, self.g_cal_opacos, self.g_ref_opacos = self.calculoVariablesGlobalesCerramientos()
        self.UA_PT = self.calculoVariablesGlobalesPT()
        self.UA_vid, self.g_cal_huecos, self.g_ref_huecos = self.calculoVariablesGlobalesHuecos()
        self.g_cal = self.g_cal_huecos + self.g_cal_opacos
        self.g_ref = self.g_ref_huecos + self.g_ref_opacos
        if self.g_ref < 0:
            self.g_ref = 0
        self.UA = self.UA_cerr + self.UA_vid + self.UA_PT

    def calculoVariablesGlobalesVentilacion(self):
        """
        Metodo: calculoVariablesGlobalesVentilacion
        
        """
        volumen = self.dI.area * self.dI.altura
        tasaCalculo = self.dI.tasaVentilacion - self.dI.tasaEqVentilacionBruta
        if tasaCalculo <= 0.0:
            tasaCalculo = 0.0001
        if self.dI.BlowerDoorTest[0] == False:
            ren = calculoInfiltraciones.calculoTasaVentilacion(volumen=volumen, area=self.dI.area, listadoCerramientos=self.dI.listadoCerramientos, listadoHuecos=self.dI.listadoHuecos, tasaCalculo=tasaCalculo, esEdificioExistente=self.parent.esEdificioExistente, programa=self.parent.programa, tipoEdificio=self.dI.tipoEdificio)
        else:
            q50 = float(self.dI.BlowerDoorTest[1])
            n = float(self.dI.BlowerDoorTest[2])
            ren = calculoInfiltraciones.calculoTasaVentilacionBlowerDoorTest(q50=q50, n=n, volumen=volumen, area=self.dI.area, listadoCerramientos=self.dI.listadoCerramientos, listadoHuecos=self.dI.listadoHuecos, tasaCalculo=tasaCalculo, esEdificioExistente=self.parent.esEdificioExistente, programa=self.parent.programa, tipoEdificio=self.dI.tipoEdificio)
        return ren

    def calculoVariablesGlobalesCerramientos(self):
        UA_cerr_suma = 0.0
        UA_cerr_suma_verano = 0.0
        Peso_cerr_suma = self.dI.inerciaParticionesInteriores
        g_cal_opacos_suma = 0.0
        g_ref_opacos_suma = 0.0
        for cerr in self.dI.listadoCerramientos:
            if self.parent.zonaCalificacion == '' or self.parent.zonaCalificacion == cerr.subgrupo:
                if cerr.enContactoCon != 'terreno':
                    Peso_cerr_suma = Peso_cerr_suma + cerr.masaM2 * cerr.superficieNeta
                UA_cerr_suma += cerr.U * cerr.superficieNeta
                if cerr.enContactoCon == 'aire' and (cerr.tipo == 'Fachada' or cerr.tipo == 'Cubierta'):
                    if self.parent.programa == 'Residencial':
                        g_cal_cerr, g_ref_cerr = calculoGananciaSolarOpacosResidencial(u=cerr.U, inercia=cerr.masaM2, orientacion=cerr.orientacion, zonaClimatica=self.dI.zonaHE1, extrapeninsular=self.dI.extrapeninsular)
                    else:
                        g_cal_cerr, g_ref_cerr = calculoGananciaSolarOpacosTerciario(u=cerr.U, inercia=cerr.masaM2, orientacion=cerr.orientacion, zonaClimatica=self.dI.zonaHE1, extrapeninsular=self.dI.extrapeninsular)
                        if '8h' in self.dI.tipoEdificio:
                            g_ref_cerr = g_ref_cerr * 0.5
                    if cerr.patronSombras != u'Sin patr\xf3n' and cerr.patronSombras != '':
                        porcentajes = calculoPerdidasSombras.leerCasillas(cerr.patronSombras, self.parent.datosSombras)
                        perdidas_verano = (calculoPerdidasSombras.tablaA(cerr.orientacion, 90, porcentajes)[0] + calculoPerdidasSombras.tablaB(cerr.orientacion, 90, porcentajes)[0] + calculoPerdidasSombras.tablaC(cerr.orientacion, 90, porcentajes)[0] + calculoPerdidasSombras.tablaD(cerr.orientacion, 90, porcentajes)[0]) / 100
                        perdidas_invierno = (calculoPerdidasSombras.tablaA(cerr.orientacion, 90, porcentajes)[1] + calculoPerdidasSombras.tablaB(cerr.orientacion, 90, porcentajes)[1] + calculoPerdidasSombras.tablaC(cerr.orientacion, 90, porcentajes)[1] + calculoPerdidasSombras.tablaD(cerr.orientacion, 90, porcentajes)[1]) / 100
                    else:
                        perdidas_verano = 0
                        perdidas_invierno = 0
                    g_cal_opacos_suma += g_cal_cerr * cerr.superficieNeta * (1 - perdidas_invierno)
                    g_ref_opacos_suma += g_ref_cerr * cerr.superficieNeta * (1 - perdidas_verano)
                elif cerr.enContactoCon == 'terreno':
                    if self.parent.programa != 'Residencial':
                        g_ref_opacos_suma -= cerr.superficieNeta * 0.015 * 2.5

        UA_cerr = UA_cerr_suma / self.dI.area
        UA_cerr_verano = UA_cerr_suma / self.dI.area
        inercia = Peso_cerr_suma / self.dI.area
        g_cal_opacos = g_cal_opacos_suma / self.dI.area
        g_ref_opacos = g_ref_opacos_suma / self.dI.area
        return (UA_cerr,
         UA_cerr_verano,
         inercia,
         g_cal_opacos,
         g_ref_opacos)

    def calculoVariablesGlobalesHuecos(self):
        UA_total_suma = 0
        g_cal_suma = 0
        g_ref_suma = 0
        UA_vidrio = 0
        UA_marco = 0
        ren = self.renh / self.dI.altura
        for h in self.dI.listadoHuecos:
            if self.parent.zonaCalificacion == '' or self.parent.zonaCalificacion == h.subgrupo:
                if float(h.porcMarco) == 100.0:
                    h.Uvidrio = 0.0
                    h.Gvidrio = 0.0
                UA_vidrio = float(h.Uvidrio) * float(h.superficie) * (1.0 - float(h.porcMarco) / 100.0)
                UA_marco = float(h.Umarco) * float(h.superficie) * float(h.porcMarco) / 100.0
                UA_total_suma += UA_vidrio + UA_marco

        UA_vid = UA_total_suma / self.dI.area
        ua_aux = self.UA_cerr + self.UA_PT + UA_vid
        for h in self.dI.listadoHuecos:
            if self.parent.zonaCalificacion == '' or self.parent.zonaCalificacion == h.subgrupo:
                if self.parent.programa == 'Residencial':
                    K_cal, K_ref = factorKHuecosResidencial(orientacion=h.orientacion)
                else:
                    K_cal, K_ref = factorKHuecosTerciario(orientacion=h.orientacion, intensidadUso=self.dI.tipoEdificio, zonaClimatica=self.dI.zonaHE1)
                gInv = float(h.superficie) * ((1 - float(h.porcMarco) / 100.0) * float(h.Gvidrio) + 4.5 * float(h.porcMarco) / 100.0 * 0.04 * float(h.Umarco) * float(h.absortividadValor))
                gVer = float(h.superficie) * ((1 - float(h.porcMarco) / 100.0) * float(h.Gvidrio) + 9.0 * float(h.porcMarco) / 100.0 * 0.04 * float(h.Umarco) * float(h.absortividadValor))
                if h.patronSombras != u'Sin patr\xf3n' and h.patronSombras != '':
                    porcentajes = calculoPerdidasSombras.leerCasillas(h.patronSombras, self.parent.datosSombras)
                    perdidasSombrasTablaA = calculoPerdidasSombras.tablaA(h.orientacion, 90, porcentajes)
                    perdidasSombrasTablaB = calculoPerdidasSombras.tablaB(h.orientacion, 90, porcentajes)
                    perdidasSombrasTablaC = calculoPerdidasSombras.tablaC(h.orientacion, 90, porcentajes)
                    perdidasSombrasTablaD = calculoPerdidasSombras.tablaD(h.orientacion, 90, porcentajes)
                    perdidas_verano = (perdidasSombrasTablaA[0] + perdidasSombrasTablaB[0] + perdidasSombrasTablaC[0] + perdidasSombrasTablaD[0]) / 100.0
                    perdidas_invierno = (perdidasSombrasTablaA[1] + perdidasSombrasTablaB[1] + perdidasSombrasTablaC[1] + perdidasSombrasTablaD[1]) / 100.0
                else:
                    perdidas_verano = 0.0
                    perdidas_invierno = 0.0
                g_cal_suma += gInv * K_cal * h.correctorFSInvierno * (1 - perdidas_invierno)
                g_ref_suma += gVer * K_ref * min(h.correctorFSVerano, 1 - perdidas_verano)

        g_cal_huecos = g_cal_suma / self.dI.area
        g_ref_huecos = g_ref_suma / self.dI.area
        return (UA_vid, g_cal_huecos, g_ref_huecos)

    def calculoVariablesGlobalesPT(self):
        UA_PT_suma = 0
        longitud_suma = 0
        for pt in self.dI.listadoPT:
            if self.parent.zonaCalificacion == '' or self.parent.zonaCalificacion == pt.subgrupo:
                if self.parent.programa == 'Residencial':
                    diccFactorAjusteResidencial = {u'Encuentro de fachada con solera': 2.0,
                     u'Encuentro de fachada con forjado': 2.0,
                     u'Encuentro de fachada con cubierta': 0.44,
                     u'Contorno de hueco': 2.0,
                     u'Esquina hacia el exterior': 2.0,
                     u'Esquina hacia el interior': 1.0}
                    if pt.tipo in diccFactorAjusteResidencial.keys():
                        factorAjuste = diccFactorAjusteResidencial[pt.tipo]
                    else:
                        factorAjuste = 1.0
                else:
                    factorAjuste = 1.0
                UA_PT_suma = UA_PT_suma + pt.fi * pt.longitud * factorAjuste
                longitud_suma += pt.longitud

        UA_PT = UA_PT_suma / self.dI.area
        return UA_PT


class datosEdificioResultados():
    """
    Clase: datosEdificioResultados del modulo datosEdificio.py
    
    
    """

    def __init__(self, parent, datosIniciales, datosGlobales):
        """
        Constructor de la clase
        
        """
        self.parent = parent
        self.dI = datosIniciales
        self.dG = datosGlobales
        self.ddaBrutaACS = 0.0
        self.ddaBrutaACS_sinAcumulacion = 0.0
        self.ddaBrutaACS_acumulacion = 0.0
        self.ddaNetaACS = 0.0
        self.expFinal = None
        self.ddaBrutaCal = 0.0
        self.ddaBrutaCal_edificio = 0.0
        self.ddaBrutaCal_ventilacion = 0.0
        self.ddaNetaCal = 0.0
        self.ddaBrutaRef = 0.0
        self.ddaBrutaRef_edificio = 0.0
        self.ddaBrutaRef_ventilacion = 0.0
        self.ddaNetaRef = 0.0
        self.enFinalReal = 0.0
        self.enFinal = 0.0
        self.enFinalRen = 0.0
        self.enFinalNoRen = 0.0
        self.emisiones = 0.0
        self.enPrim = 0.0
        self.enPrimRen = 0.0
        self.enPrimNoRen = 0.0
        self.diccNombresCombustibles = {u'Gas Natural': u'GasNatural',
         u'Gas\xf3leo-C': u'Gasoil',
         u'Electricidad': u'Electricidad',
         u'GLP': u'GLP',
         u'Carb\xf3n': u'Carbon',
         u'Biocarburante': u'Biocarburante',
         u'Biomasa/Renovable': u'BiomasaNoDens',
         u'BiomasaDens': u'BiomasaDens'}
        self.listaNombresServicios = ['ACS',
         'Cal',
         'Ref',
         '',
         'Contrib',
         'Ilum',
         'Ventiladores',
         'Bombas',
         'TorresRef']
        self.listaNombresVariables = ['enFinalReal',
         'enFinal',
         'enFinalRen',
         'enFinalNoRen',
         'emisiones',
         'enPrim',
         'enPrimRen',
         'enPrimNoRen']
        self.inicializarAtributos()
        self.calculoIndicadoresEnergeticos()
        self.comprobacionConsumoEnergiaElectricaGenerada()
        return

    @property
    def emisionesMostrar(self):
        """
        Las emisiones podr\xedan ser negativas si la generaci\xf3n de electricidad es muy grande. Por lo tanto
        hacemos que sea cero.
        """
        if self.emisiones < 0.0:
            return 0.0
        else:
            return self.emisiones

    @property
    def emisionesMostrar_Electricidad(self):
        """
        Las emisiones asociadas a la electricidad podr\xedan ser negativas si la generaci\xf3n de electricidad es muy grande. Por lo tanto
        hacemos que sea cero.
        """
        if self.emisiones_Electricidad < 0.0:
            return 0.0
        else:
            return self.emisiones_Electricidad

    @property
    def enPrimMostrar(self):
        """
        La energ\xeda primaria podr\xeda ser negativa si la generaci\xf3n de electricidad es muy grande. Por lo tanto
        hacemos que sea cero.
        """
        if self.enPrim < 0.0:
            return 0.0
        else:
            return self.enPrim

    @property
    def enPrimNoRenMostrar(self):
        """
        La energ\xeda primaria no renovable podr\xeda ser negativa si la generaci\xf3n de electricidad es muy grande. Por lo tanto
        hacemos que sea cero.
        """
        if self.enPrimNoRen < 0.0:
            return 0.0
        else:
            return self.enPrimNoRen

    @property
    def enPrimRenMostrar(self):
        """
        La energia primaria renovable podr\xedan ser negativa si la generaci\xf3n de electricidad es muy grande. Por lo tanto
        hacemos que sea cero.
        """
        if self.enPrimRen < 0.0:
            return 0.0
        else:
            return self.enPrimRen

    @property
    def enFinalMostrar(self):
        """
        La energia final podr\xeda ser negativa si la generaci\xf3n de electricidad es muy grande. Por lo tanto
        hacemos que sea cero.
        """
        if self.enFinal < 0.0:
            return 0.0
        else:
            return self.enFinal

    def inicializarAtributos(self):
        """
        Inicializo los atributos de la clase de forma din\xe1mica porque hay muchos
        """
        for var in self.listaNombresVariables:
            for serv in self.listaNombresServicios:
                exec 'self.%s%s = 0.0' % (var, serv)
                for key in self.diccNombresCombustibles:
                    comb = self.diccNombresCombustibles[key]
                    exec 'self.%s%s_%s = 0.0' % (var, serv, comb)

    def calculoIndicadoresEnergeticos(self):
        """
        Metodo: calculoIndicadoresEnergeticosp
        Calculo demandas, emisiones, enFinal, enPrim,
        
        """
        self.ddaBrutaACS, self.ddaBrutaACS_sinAcumulacion, self.ddaBrutaACS_acumulacion = calculoDdaBrutaACS(Q_ACS=self.dI.Q_ACS, instalacionACS=self.dI.ACS, zonaHE1PeninsularOExtrapeninsular=self.dI.zonaHE1PeninsularOExtrapeninsular, area=self.dI.area)
        self.expFinal = self.calculoExperimentoFinal()
        if self.parent.casoValido == False:
            return
        if self.parent.programa == 'Residencial':
            self.ddaBrutaCal_edificio = self.expFinal.ddaCal
            self.ddaBrutaRef_edificio = self.expFinal.ddaRef
        else:
            if '8h' in self.dI.tipoEdificio:
                self.ddaBrutaCal_edificio = self.expFinal.ddaCal * 1.34
            elif '12h' in self.dI.tipoEdificio:
                self.ddaBrutaCal_edificio = self.expFinal.ddaCal * 1.29
            elif '16h' in self.dI.tipoEdificio:
                self.ddaBrutaCal_edificio = self.expFinal.ddaCal * 1.19
            elif '24h' in self.dI.tipoEdificio:
                self.ddaBrutaCal_edificio = self.expFinal.ddaCal * 1.15
            if '3c' in self.dI.zonaHE1:
                if self.expFinal.ddaRef < 15:
                    self.ddaBrutaRef_edificio = self.expFinal.ddaRef + 15.0 * self.expFinal.ddaRef / 15.0
                else:
                    self.ddaBrutaRef_edificio = self.expFinal.ddaRef + 15.0
            elif 'E' not in self.dI.zonaHE1:
                if self.expFinal.ddaRef < 7.0:
                    self.ddaBrutaRef_edificio = self.expFinal.ddaRef + 7.0 * self.expFinal.ddaRef / 7.0
                else:
                    self.ddaBrutaRef_edificio = self.expFinal.ddaRef + 7.0
            else:
                self.ddaBrutaRef_edificio = self.expFinal.ddaRef
            if '8h' in self.dI.tipoEdificio:
                self.ddaBrutaRef_edificio = self.ddaBrutaRef_edificio * 1.1
        self.ddaBrutaCal_ventilacion, self.ddaBrutaRef_ventilacion = self.calculoDdasBrutasPorVentilacion()
        self.ddaBrutaCal, self.ddaBrutaRef = self.calculoDdasBrutas()
        self.ddaNetaACS, self.ddaNetaCal, self.ddaNetaRef = self.calculoDdasNetas()
        self.calculoEquiposGeneracion(dda=self.ddaNetaACS, instalacion=self.dI.ACS, servicio='ACS')
        self.calculoEquiposGeneracion(dda=self.ddaNetaCal, instalacion=self.dI.calefaccion, servicio='Cal')
        self.calculoEquiposGeneracion(dda=self.ddaNetaRef, instalacion=self.dI.refrigeracion, servicio='Ref')
        if len(self.dI.sistemasIluminacion) > 0:
            self.calculoIluminacion(servicio='Ilum')
        if len(self.dI.sistemasVentiladores) > 0:
            self.calculoEquiposGT(instalacion=self.dI.sistemasVentiladores, servicio='Ventiladores')
        if len(self.dI.sistemasBombas) > 0:
            self.calculoEquiposGT(instalacion=self.dI.sistemasBombas, servicio='Bombas')
        if len(self.dI.sistemasTorresRefrigeracion) > 0:
            self.calculoEquiposGT(instalacion=self.dI.sistemasTorresRefrigeracion, servicio='TorresRef')
        self.calculoContribuciones()
        self.calculoResultadosGlobalesEdificio()

    def calculoExperimentoFinal(self):
        """
        Metodo: calculoExperimentoFinal
        Se obtiene un objeto que tiene como atributos las demandas y las variables globales
        """
        expFinal, casoValido, listadoMensajes = self.parent.bd.calculoExperimentoFinal(UA_inicial=self.dG.UA, g_cal_inicial=self.dG.g_cal, g_ref_inicial=self.dG.g_ref, inercia_inicial=self.dG.inercia, renh_inicial=self.dG.renh)
        if not casoValido:
            self.parent.casoValido = False
            listaErrores = ''
            for i in listadoMensajes:
                listaErrores += '%s\n' % i

            self.parent.mensajeAviso = _(u'Revise los siguientes par\xe1metros de su edificio:\n') + listaErrores + _(u'Con estas caracter\xedsticas el edificio est\xe1 fuera del m\xe9todo simplificado. Emplee el m\xe9todo general.')
        return expFinal

    def calculoDdasBrutasPorVentilacion(self):
        """
        M\xe9todo: calculoDdasBrutasPorVentilacion
        Estimaci\xf3n de la demanda de calefacci\xf3n y refrigeracion debida a la ventilaci\xf3n. en kWh/m2a\xf1o
        """
        GH_invierno, GH_verano = getGradosHora(programa=self.parent.programa, tipoEdificio=self.dI.tipoEdificio, zonaHE1PeninsularOExtrapeninsular=self.dI.zonaHE1PeninsularOExtrapeninsular)
        densidadAire = 1.21
        Cpaire = 1.004
        caudalEqVentilacionNeta = self.dI.tasaEqVentilacionNeta * self.dI.area * self.dI.altura
        dda_calefaccion_ventilacion = caudalEqVentilacionNeta * densidadAire * Cpaire / 3600.0 * GH_invierno
        dda_refrigeracion_ventilacion = caudalEqVentilacionNeta * densidadAire * Cpaire / 3600.0 * GH_verano
        ddaCalBruta_ventilacion = dda_calefaccion_ventilacion / self.dI.area
        ddaRefBruta_ventilacion = dda_refrigeracion_ventilacion / self.dI.area
        return (ddaCalBruta_ventilacion, ddaRefBruta_ventilacion)

    def calculoDdasBrutas(self):
        """
        Metodo: calculoDdasBrutas
        La demanda bruta total es la suma de la propia del edificio mas lo asociado a la ventilacion
        """
        ddaCalBruta = self.ddaBrutaCal_edificio + self.ddaBrutaCal_ventilacion
        ddaRefBruta = self.ddaBrutaRef_edificio + self.ddaBrutaRef_ventilacion
        return (ddaCalBruta, ddaRefBruta)

    def calculoDdasNetas(self):
        """
        Metodo: calculoDdasNetas
        A partir de demandas brutas y con contribuciones energeticas que tenga, calcula las demandas netas
        y asigna valor a atributo correspondiente
        """
        if len(self.dI.contribuciones.listado) > 0.0:
            porcContribTermicaACS = self.dI.contribuciones.porcACSTotal
            contribGeneracionACS = self.dI.contribuciones.calorRecupACSTotal / self.dI.area
            porcContribTermicaCal = self.dI.contribuciones.porcCalTotal
            contribGeneracionCal = self.dI.contribuciones.calorRecupCalTotal / self.dI.area
            porcContribTermicaRef = self.dI.contribuciones.porcRefTotal
            contribGeneracionRef = self.dI.contribuciones.calorRecupRefTotal / self.dI.area
        else:
            porcContribTermicaACS = 0.0
            contribGeneracionACS = 0.0
            porcContribTermicaCal = 0.0
            contribGeneracionCal = 0.0
            porcContribTermicaRef = 0.0
            contribGeneracionRef = 0.0
        ddaNetaACS = calculoDdaNeta(ddaBruta=self.ddaBrutaACS, porcTermica=porcContribTermicaACS, contribGeneracion=contribGeneracionACS)
        ddaNetaCal = calculoDdaNeta(ddaBruta=self.ddaBrutaCal, porcTermica=porcContribTermicaCal, contribGeneracion=contribGeneracionCal)
        ddaNetaRef = calculoDdaNeta(ddaBruta=self.ddaBrutaRef, porcTermica=porcContribTermicaRef, contribGeneracion=contribGeneracionRef)
        return (ddaNetaACS, ddaNetaCal, ddaNetaRef)

    def calculoEquiposGeneracion(self, dda = 0.0, instalacion = [], servicio = None):
        """
        M\xe9todo: calculoEquiposGeneracion
        Argumentos: 
            dda = demanda neta. Float
            instalacion = array con listado de objetos de instalaciones que cubren la demanda definida
            servicio = 'Cal', 'Ref', 'ACS'. Para distinguir si hay que meter instalacion de referencia o no. Y para asignar nombres atributos
         Calcula emisiones, enFinal, enPrim asociado al servicio que se haya indicado
        """
        diccEnFinalReal = {}
        diccEnFinal = {}
        diccEnFinalRen = {}
        diccEnFinalNoRen = {}
        diccEmisiones = {}
        diccEnPrim = {}
        diccEnPrimRen = {}
        diccEnPrimNoRen = {}
        if servicio == 'Cal' or servicio == 'Ref':
            instalacion = self.getInstalacionConReferencia(tipo=servicio, instalacionEdificio=instalacion)
        for equipo in instalacion.listado:
            rend = equipo.rendimiento / 100.0
            combustible = equipo.combustible
            cobertura = equipo.coberturaM2 / self.dI.area
            Kem = coeficienteDePasoEmisiones(combustible=combustible, provincia=self.dI.provincia, extrapeninsular=self.dI.extrapeninsular)
            Kenprim, KenprimRen, KenprimNoRen = coeficienteDePasoEnergiaPrimaria(combustible=combustible, provincia=self.dI.provincia, extrapeninsular=self.dI.extrapeninsular)
            KenfinalRen, KenfinalNoRen = (0.0, 1.0)
            if equipo.tipo != 'referencia':
                enFinalReal = dda / rend * cobertura
            else:
                enFinalReal = 0.0
            enFinal = dda / rend * cobertura
            enFinalRen = dda / rend * cobertura * KenfinalRen
            enFinalNoRen = dda / rend * cobertura * KenfinalNoRen
            emisiones = dda / rend * cobertura * Kem
            enPrim = dda / rend * cobertura * Kenprim
            enPrimRen = dda / rend * cobertura * KenprimRen
            enPrimNoRen = dda / rend * cobertura * KenprimNoRen
            diccEnFinalReal = self.anadirDatosADicc(diccEnFinalReal, combustible, enFinalReal)
            diccEnFinal = self.anadirDatosADicc(diccEnFinal, combustible, enFinal)
            diccEnFinalRen = self.anadirDatosADicc(diccEnFinalRen, combustible, enFinalRen)
            diccEnFinalNoRen = self.anadirDatosADicc(diccEnFinalNoRen, combustible, enFinalNoRen)
            diccEmisiones = self.anadirDatosADicc(diccEmisiones, combustible, emisiones)
            diccEnPrim = self.anadirDatosADicc(diccEnPrim, combustible, enPrim)
            diccEnPrimRen = self.anadirDatosADicc(diccEnPrimRen, combustible, enPrimRen)
            diccEnPrimNoRen = self.anadirDatosADicc(diccEnPrimNoRen, combustible, enPrimNoRen)

        self.calculoResultadosParcialesEdificio(diccEnFinalReal=diccEnFinalReal, diccEnFinal=diccEnFinal, diccEnFinalRen=diccEnFinalRen, diccEnFinalNoRen=diccEnFinalNoRen, diccEmisiones=diccEmisiones, diccEnPrim=diccEnPrim, diccEnPrimRen=diccEnPrimRen, diccEnPrimNoRen=diccEnPrimNoRen, tipo=servicio)

    def anadirDatosADicc(self, dicc = {}, key = None, valor = 0.0):
        """
        M\xe9todo: anadirDatosADicc
        Cuando tengo un diccionario y tengo que sumar el valor a lo que contiene una key determinada
        Si no existe la key, asigna el valor y sino lo suma
        """
        if dicc.has_key(key):
            dicc[key] += valor
        else:
            dicc[key] = valor
        return dicc

    def calculoContribuciones(self):
        """
        M\xe9todo: calculoContribuciones
        Calcula emisiones, enFinal, enPrim asociadas a las contribuciones energeticas
        """
        diccEnFinalReal = {}
        diccEnFinal = {}
        diccEnFinalRen = {}
        diccEnFinalNoRen = {}
        diccEmisiones = {}
        diccEnPrim = {}
        diccEnPrimRen = {}
        diccEnPrimNoRen = {}
        if len(self.dI.contribuciones.listado) > 0:
            if self.dI.contribuciones.electricidadGenTotal > 0.0:
                combustible = u'Electricidad'
                electricidadGenM2 = float(self.dI.contribuciones.electricidadGenTotal) / self.dI.area
                Kem = coeficienteDePasoEmisiones(combustible=combustible, provincia=self.dI.provincia, extrapeninsular=self.dI.extrapeninsular)
                Kenprim, KenprimRen, KenprimNoRen = coeficienteDePasoEnergiaPrimaria(combustible=combustible, provincia=self.dI.provincia, extrapeninsular=self.dI.extrapeninsular)
                KenfinalRen, KenfinalNoRen = (0.0, 1.0)
                enFinalReal = -electricidadGenM2
                enFinal = -electricidadGenM2
                enFinalRen = -electricidadGenM2 * KenfinalRen
                enFinalNoRen = -electricidadGenM2 * KenfinalNoRen
                emisiones = -electricidadGenM2 * Kem
                enPrim = -electricidadGenM2 * Kenprim
                enPrimRen = -electricidadGenM2 * KenprimRen
                enPrimNoRen = -electricidadGenM2 * KenprimNoRen
                diccEnFinalReal = self.anadirDatosADicc(diccEnFinalReal, combustible, enFinalReal)
                diccEnFinal = self.anadirDatosADicc(diccEnFinal, combustible, enFinal)
                diccEnFinalRen = self.anadirDatosADicc(diccEnFinalRen, combustible, enFinalRen)
                diccEnFinalNoRen = self.anadirDatosADicc(diccEnFinalNoRen, combustible, enFinalNoRen)
                diccEmisiones = self.anadirDatosADicc(diccEmisiones, combustible, emisiones)
                diccEnPrim = self.anadirDatosADicc(diccEnPrim, combustible, enPrim)
                diccEnPrimRen = self.anadirDatosADicc(diccEnPrimRen, combustible, enPrimRen)
                diccEnPrimNoRen = self.anadirDatosADicc(diccEnPrimNoRen, combustible, enPrimNoRen)
        for equipo in self.dI.contribuciones.listado:
            if equipo.enConsum != '' and equipo.enConsum > 0.0:
                combustible = equipo.combustible
                enConsumM2 = float(equipo.enConsum) / self.dI.area
                Kem = coeficienteDePasoEmisiones(combustible=combustible, provincia=self.dI.provincia, extrapeninsular=self.dI.extrapeninsular)
                Kenprim, KenprimRen, KenprimNoRen = coeficienteDePasoEnergiaPrimaria(combustible=combustible, provincia=self.dI.provincia, extrapeninsular=self.dI.extrapeninsular)
                KenfinalRen, KenfinalNoRen = (0.0, 1.0)
                enFinalReal = enConsumM2
                enFinal = enConsumM2
                enFinalRen = enConsumM2 * KenfinalRen
                enFinalNoRen = enConsumM2 * KenfinalNoRen
                emisiones = enConsumM2 * Kem
                enPrim = enConsumM2 * Kenprim
                enPrimRen = enConsumM2 * KenprimRen
                enPrimNoRen = enConsumM2 * KenprimNoRen
                diccEnFinalReal = self.anadirDatosADicc(diccEnFinalReal, combustible, enFinalReal)
                diccEnFinal = self.anadirDatosADicc(diccEnFinal, combustible, enFinal)
                diccEnFinalRen = self.anadirDatosADicc(diccEnFinalRen, combustible, enFinalRen)
                diccEnFinalNoRen = self.anadirDatosADicc(diccEnFinalNoRen, combustible, enFinalNoRen)
                diccEmisiones = self.anadirDatosADicc(diccEmisiones, combustible, emisiones)
                diccEnPrim = self.anadirDatosADicc(diccEnPrim, combustible, enPrim)
                diccEnPrimRen = self.anadirDatosADicc(diccEnPrimRen, combustible, enPrimRen)
                diccEnPrimNoRen = self.anadirDatosADicc(diccEnPrimNoRen, combustible, enPrimNoRen)

        self.calculoResultadosParcialesEdificio(diccEnFinalReal=diccEnFinalReal, diccEnFinal=diccEnFinal, diccEnFinalRen=diccEnFinalRen, diccEnFinalNoRen=diccEnFinalNoRen, diccEmisiones=diccEmisiones, diccEnPrim=diccEnPrim, diccEnPrimRen=diccEnPrimRen, diccEnPrimNoRen=diccEnPrimNoRen, tipo='Contrib')

    def calculoResultadosParcialesEdificio(self, diccEnFinalReal = {}, diccEnFinal = {}, diccEnFinalRen = {}, diccEnFinalNoRen = {}, diccEmisiones = {}, diccEnPrim = {}, diccEnPrimRen = {}, diccEnPrimNoRen = {}, tipo = ''):
        """
        M\xe9todo: calculoResultadosParcialesEdificio
        Funcion a la que le llegan en diccionarios los consumos, emisiones, etc y crea los atributos parciales correspondientes
        self.emisACS, self.enFinalRealACS... self.emisACS_GasNatural...
        """
        listaDicc = {'enFinalReal': diccEnFinalReal,
         'enFinal': diccEnFinal,
         'enFinalRen': diccEnFinalRen,
         'enFinalNoRen': diccEnFinalNoRen,
         'emisiones': diccEmisiones,
         'enPrim': diccEnPrim,
         'enPrimRen': diccEnPrimRen,
         'enPrimNoRen': diccEnPrimNoRen}
        for keyListaDicc in listaDicc:
            valorTotal = 0.0
            dicc = listaDicc[keyListaDicc]
            for key in dicc:
                exec 'self.%s%s_%s = %s' % (keyListaDicc,
                 tipo,
                 self.diccNombresCombustibles[key],
                 dicc[key])
                valorTotal += dicc[key]

            exec 'self.%s%s = %s' % (keyListaDicc, tipo, valorTotal)

    def calculoResultadosGlobalesEdificio(self):
        """
        M\xe9todo: calculoResultadosGlobalesEdificio
        funcion que calcula las variables globales del edificio a partir de atributos parciales: 
        self.emisiones, self.enFinalReal...
        """
        for var in self.listaNombresVariables:
            exec 'self.%s = self.%sACS + self.%sCal + self.%sRef + self.%sContrib + self.%sIlum + self.%sVentiladores + self.%sBombas + self.%sTorresRef' % (var,
             var,
             var,
             var,
             var,
             var,
             var,
             var,
             var)
            for key in self.diccNombresCombustibles:
                comb = self.diccNombresCombustibles[key]
                exec 'self.%s_%s = self.%sACS_%s + self.%sCal_%s + self.%sRef_%s + self.%sContrib_%s + self.%sIlum_%s + self.%sVentiladores_%s + self.%sBombas_%s + self.%sTorresRef_%s' % (var,
                 comb,
                 var,
                 comb,
                 var,
                 comb,
                 var,
                 comb,
                 var,
                 comb,
                 var,
                 comb,
                 var,
                 comb,
                 var,
                 comb,
                 var,
                 comb)

    def getInstalacionConReferencia(self, tipo = None, instalacionEdificio = []):
        """
        Cojo la instalacion y si no se cubre el 100%, le a\xf1ade un objeto mas que corresponde a la de referencia
        """
        instalacionCoberturaTotal = copy.deepcopy(instalacionEdificio)
        coberturaTotal = instalacionCoberturaTotal.coberturaM2 / self.dI.area
        if tipo == 'Cal':
            rendReferencia = rendCalRefer
            combReferencia = combCalRefer
        else:
            rendReferencia = rendRefRefer
            combReferencia = combRefRefer
        if coberturaTotal < 1.0:
            coberturaInstalacionReferencia = 1.0 - coberturaTotal
            coberturaInstalacionReferenciaM2 = coberturaInstalacionReferencia * self.dI.area
            objInstalacionReferencia = EquipoGeneracion(tipo='referencia', rendimiento=rendReferencia, combustible=combReferencia, coberturaM2=coberturaInstalacionReferenciaM2, coberturaPorc=coberturaInstalacionReferencia, objListado=instalacionCoberturaTotal)
        return instalacionCoberturaTotal

    def calculoIluminacion(self, servicio = 'Ilum'):
        """
        M\xe9todo: calculoIluminacion
        Argumentos: 
            servicio = 'Ilum'. Parra asignar nombres atributos
         Calcula emisiones, enFinal, enPrim asociado al servicio que se haya indicado
        """
        diccEnFinalReal = {}
        diccEnFinal = {}
        diccEnFinalRen = {}
        diccEnFinalNoRen = {}
        diccEmisiones = {}
        diccEnPrim = {}
        diccEnPrimRen = {}
        diccEnPrimNoRen = {}
        combustible = u'Electricidad'
        Kem = coeficienteDePasoEmisiones(combustible=combustible, provincia=self.dI.provincia, extrapeninsular=self.dI.extrapeninsular)
        Kenprim, KenprimRen, KenprimNoRen = coeficienteDePasoEnergiaPrimaria(combustible=combustible, provincia=self.dI.provincia, extrapeninsular=self.dI.extrapeninsular)
        KenfinalRen, KenfinalNoRen = (0.0, 1.0)
        potenciaTotalIluminacion = self.dI.potenciaIluminacion
        consumoTotal = potenciaTotalIluminacion / self.dI.area / 1000.0 * self.dI.numeroHoras
        enFinalReal = consumoTotal
        enFinal = consumoTotal
        enFinalRen = consumoTotal * KenfinalRen
        enFinalNoRen = consumoTotal * KenfinalNoRen
        emisiones = consumoTotal * Kem
        enPrim = consumoTotal * Kenprim
        enPrimRen = consumoTotal * KenprimRen
        enPrimNoRen = consumoTotal * KenprimNoRen
        diccEnFinalReal = self.anadirDatosADicc(diccEnFinalReal, combustible, enFinalReal)
        diccEnFinal = self.anadirDatosADicc(diccEnFinal, combustible, enFinal)
        diccEnFinalRen = self.anadirDatosADicc(diccEnFinalRen, combustible, enFinalRen)
        diccEnFinalNoRen = self.anadirDatosADicc(diccEnFinalNoRen, combustible, enFinalNoRen)
        diccEmisiones = self.anadirDatosADicc(diccEmisiones, combustible, emisiones)
        diccEnPrim = self.anadirDatosADicc(diccEnPrim, combustible, enPrim)
        diccEnPrimRen = self.anadirDatosADicc(diccEnPrimRen, combustible, enPrimRen)
        diccEnPrimNoRen = self.anadirDatosADicc(diccEnPrimNoRen, combustible, enPrimNoRen)
        self.calculoResultadosParcialesEdificio(diccEnFinalReal=diccEnFinalReal, diccEnFinal=diccEnFinal, diccEnFinalRen=diccEnFinalRen, diccEnFinalNoRen=diccEnFinalNoRen, diccEmisiones=diccEmisiones, diccEnPrim=diccEnPrim, diccEnPrimRen=diccEnPrimRen, diccEnPrimNoRen=diccEnPrimNoRen, tipo=servicio)

    def calculoEquiposGT(self, instalacion = [], servicio = None):
        diccEnFinalReal = {}
        diccEnFinal = {}
        diccEnFinalRen = {}
        diccEnFinalNoRen = {}
        diccEmisiones = {}
        diccEnPrim = {}
        diccEnPrimRen = {}
        diccEnPrimNoRen = {}
        combustible = u'Electricidad'
        Kem = coeficienteDePasoEmisiones(combustible=combustible, provincia=self.dI.provincia, extrapeninsular=self.dI.extrapeninsular)
        Kenprim, KenprimRen, KenprimNoRen = coeficienteDePasoEnergiaPrimaria(combustible=combustible, provincia=self.dI.provincia, extrapeninsular=self.dI.extrapeninsular)
        KenfinalRen, KenfinalNoRen = (0.0, 1.0)
        consumoTotal = 0.0
        for equipo in instalacion:
            consumoTotal += float(equipo[2]) / self.dI.area

        enFinalReal = consumoTotal
        enFinal = consumoTotal
        enFinalRen = consumoTotal * KenfinalRen
        enFinalNoRen = consumoTotal * KenfinalNoRen
        emisiones = consumoTotal * Kem
        enPrim = consumoTotal * Kenprim
        enPrimRen = consumoTotal * KenprimRen
        enPrimNoRen = consumoTotal * KenprimNoRen
        diccEnFinalReal = self.anadirDatosADicc(diccEnFinalReal, combustible, enFinalReal)
        diccEnFinal = self.anadirDatosADicc(diccEnFinal, combustible, enFinal)
        diccEnFinalRen = self.anadirDatosADicc(diccEnFinalRen, combustible, enFinalRen)
        diccEnFinalNoRen = self.anadirDatosADicc(diccEnFinalNoRen, combustible, enFinalNoRen)
        diccEmisiones = self.anadirDatosADicc(diccEmisiones, combustible, emisiones)
        diccEnPrim = self.anadirDatosADicc(diccEnPrim, combustible, enPrim)
        diccEnPrimRen = self.anadirDatosADicc(diccEnPrimRen, combustible, enPrimRen)
        diccEnPrimNoRen = self.anadirDatosADicc(diccEnPrimNoRen, combustible, enPrimNoRen)
        self.calculoResultadosParcialesEdificio(diccEnFinalReal=diccEnFinalReal, diccEnFinal=diccEnFinal, diccEnFinalRen=diccEnFinalRen, diccEnFinalNoRen=diccEnFinalNoRen, diccEmisiones=diccEmisiones, diccEnPrim=diccEnPrim, diccEnPrimRen=diccEnPrimRen, diccEnPrimNoRen=diccEnPrimNoRen, tipo=servicio)

    def calculoConsumoEnFinalSegunCombustible(self):
        """
        Devuelve un array con el consumo de cada combustible. 
        Se  utiliza en analisis eco. 
        Se tiene en cuenta tb lo de los equipos de sustitucion. Es decir es energ\xeda final real + energ\xeda equipos sustituci\xf3n
        Se tiene en cuenta tb el consumo de la generaci\xf3n y la electricidad generada
        En kWh/m2
        """
        consumoEnFinalSegunCombustible = {u'Gas Natural': self.enFinal_GasNatural,
         u'Gas\xf3leo-C': self.enFinal_Gasoil,
         u'Electricidad': self.enFinal_Electricidad,
         u'GLP': self.enFinal_GLP,
         u'Carb\xf3n': self.enFinal_Carbon,
         u'Biocarburante': self.enFinal_Biocarburante,
         u'Biomasa/Renovable': self.enFinal_BiomasaNoDens,
         u'BiomasaDens': self.enFinal_BiomasaDens}
        return consumoEnFinalSegunCombustible

    def getLimitesEmisiones(self):
        limitesEmisionesGlobales = [round(self.emisiones_limiteAB, 1),
         round(self.emisiones_limiteBC, 1),
         round(self.emisiones_limiteCD, 1),
         round(self.emisiones_limiteDE, 1),
         round(self.emisiones_limiteEF, 1),
         round(self.emisiones_limiteFG, 1)]
        return limitesEmisionesGlobales

    def comprobacionConsumoEnergiaElectricaGenerada(self):
        """
        comprobacionConsumoEnergiaElectricaGenerada
        Funcion para comprobar que la energia el\xe9ctrica generada no supera la energ\xeda el\xe9ctrica autoconsumida.
        Saca un mensaje de aviso
        """
        if self.enFinal_Electricidad < 0.0:
            if self.parent.programa == 'Residencial':
                self.parent.mensajeAviso = _(u'La energ\xeda el\xe9ctrica generada para autoconsumo supera la energ\xeda el\xe9ctrica consumida para cubrir los servicios de calefacci\xf3n, refrigeraci\xf3n y ACS del edificio.')
            else:
                self.parent.mensajeAviso = _(u'La energ\xeda el\xe9ctrica generada para autoconsumo supera la energ\xeda el\xe9ctrica consumida para cubrir los servicios de calefacci\xf3n, refrigeraci\xf3n, ACS e iluminaci\xf3n del edificio.')


class datosEdificio():
    """
    Clase: datosEdificio del modulo datosEdificio.py
    """

    def __init__(self, datosGenerales = [], datosEnvolvente = [], datosInstalaciones = [[],
 [],
 [],
 [],
 [],
 [],
 [],
 [],
 [],
 [],
 [],
 []], programa = 'Residencial', subgrupos = [], zonaCalificacion = '', datosSombras = [], escala = {}, esEdificioExistente = True):
        """
        Constructor de la clase
        
        
        ARGUMENTOS:
                datosGenerales = [], 
             datosEnvolvente = [], 
             datosInstalaciones = [], 
             programa = 'Residencial',
             subgrupos = [], 
             zonaCalificacion = '', 
             datosSombras = [], 
             escala = {}
        """
        self.casoValido = True
        self.mensajeAviso = ''
        self.esEdificioExistente = esEdificioExistente
        self.datosIniciales = None
        self.datosGlobales = None
        self.datosResultados = None
        self.datosGenerales = datosGenerales
        self.datosEnvolvente = datosEnvolvente
        self.datosInstalaciones = datosInstalaciones
        self.programa = programa
        self.subgrupos = subgrupos
        self.zonaCalificacion = zonaCalificacion
        self.datosSombras = datosSombras
        self.escala = escala
        self.bd = None
        return

    def recargarBD(self):
        """
        Si no se ha cargado nunca la bd, self.bd = None
        Si self.bd es None o self.bd.zona no es la zona que se est\xe1 calificando, se recarga la lectura de la base de datos
        """
        if self.bd == None:
            self.bd = leerBDDesdeArchivo.BD(zona=self.datosIniciales.zonaHE1, extrapeninsular=self.datosIniciales.extrapeninsular)
        elif self.bd.zona != self.datosIniciales.zonaHE1 or self.bd.extrapeninsular != self.datosIniciales.extrapeninsular:
            self.bd = leerBDDesdeArchivo.BD(zona=self.datosIniciales.zonaHE1, extrapeninsular=self.datosIniciales.extrapeninsular)
        return

    def calificacion(self):
        self.datosIniciales = datosEdificioIniciales(self)
        if self.casoValido == False:
            return
        self.recargarBD()
        self.datosGlobales = datosEdificioGlobales(self, datosIniciales=self.datosIniciales)
        if self.casoValido == False:
            return
        self.datosResultados = datosEdificioResultados(self, datosIniciales=self.datosIniciales, datosGlobales=self.datosGlobales)
        self.calculoNotasIndicadoresEnergeticos()

    def getEscalaCalificacionResidencial(self):
        """
        se obtiene objeto con los datos de la escala de calificacion de residencial
        """
        if self.datosIniciales.extrapeninsular == False:
            auxPen = 'peninsular'
        else:
            auxPen = 'extrapeninsular'
        datos = self.escala['%s_%s' % (self.datosIniciales.zonaHE1, auxPen)]
        if self.datosIniciales.tipoEdificio == 'Unifamiliar':
            datosEscala = datos.unifamiliar
        else:
            datosEscala = datos.bloque
        return datosEscala

    def calculoNotasIndicadoresEnergeticos(self):
        """
        Metodo: calculoNotasIndicadoresEnergeticos
        Permite calcular las notas de los indicadores energ\xe9ticos parciales y totales
        """
        self.escalaZonaClimatica = self.getEscalaCalificacionResidencial()
        diccNombresVariables = {'ddaBrutaCal': 'demandaCalefaccion',
         'ddaBrutaRef': 'demandaRefrigeracion',
         'emisionesCal': 'emisionesCalefaccion',
         'emisionesRef': 'emisionesRefrigeracion',
         'emisionesACS': 'emisionesACS',
         'emisiones': 'emisionesTotales',
         'enPrimNoRenCal': 'cEPcalefaccion',
         'enPrimNoRenRef': 'cEPrefrigeracion',
         'enPrimNoRenACS': 'cEPACS',
         'enPrimNoRen': 'cEPtotal'}
        listaAux = ['AB',
         'BC',
         'CD',
         'DE',
         'EF',
         'FG']
        for key in diccNombresVariables.keys():
            exec 'self.datosResultados.%s_limites = []' % key
            for i in listaAux:
                exec 'valorLimite=self.escalaZonaClimatica.%s.%s' % (diccNombresVariables[key], i)
                exec 'self.datosResultados.%s_limite%s = valorLimite' % (key, i)
                exec 'self.datosResultados.%s_limites.append(valorLimite)' % key

            exec 'limites = self.datosResultados.%s_limites' % key
            exec 'valorCalificar = self.datosResultados.%s' % key
            nota = self.calculoNotaCalificacion(limites=limites, valorCalificar=valorCalificar)
            exec 'self.datosResultados.%s_nota = nota' % key

        self.datosResultados.emisionesIlum_nota = '-'
        self.datosResultados.enPrimNoRenIlum_nota = '-'

    def calculoNotaCalificacion(self, limites = [], valorCalificar = None):
        """
        Met\xf3do: calculoNotaCalificacion
        Le llegan los limites y el valor de la variable y devuelve la nota correspondiente
        """
        dicc = {limites[0]: 'A',
         limites[1]: 'B',
         limites[2]: 'C',
         limites[3]: 'D',
         limites[4]: 'E',
         limites[5]: 'F'}
        if None in limites:
            nota = 'No calificable'
            return nota
        else:
            if valorCalificar == 0.0:
                nota = 'A'
            elif valorCalificar >= limites[-1]:
                nota = 'G'
            else:
                keyLimite = 0.0
                for lim in limites:
                    if valorCalificar < lim:
                        keyLimite = lim
                        break

                nota = dicc[keyLimite]
            return nota


class datosEdificioTerciario(datosEdificio):
    """
    Clase: datosEdificioTerciario del modulo datosEdificio.py
    
    
    """

    def __init__(self, datosGenerales = [], datosEnvolvente = [], datosInstalaciones = [[],
 [],
 [],
 [],
 [],
 [],
 [],
 [],
 [],
 [],
 [],
 []], programa = 'GranTerciario', subgrupos = [], zonaCalificacion = '', datosSombras = [], escala = {}, esEdificioExistente = True):
        """
        Constructor de la clase
        
        
        ARGUMENTOS:
                panelDatosgenerales:
                panelEnvolvente:
                panelInstalaciones:
                program:
        """
        self.datosInicialesEdifRef = None
        self.datosGlobalesEdifRef = None
        self.datosResultadosEdifRef = None
        datosEdificio.__init__(self, datosGenerales=datosGenerales, datosEnvolvente=datosEnvolvente, datosInstalaciones=datosInstalaciones, programa=programa, subgrupos=subgrupos, zonaCalificacion=zonaCalificacion, datosSombras=datosSombras, escala=escala, esEdificioExistente=esEdificioExistente)
        return

    def recargarBD(self, datosIniciales = None):
        """
        Si no se ha cargado nunca la bd, self.bd = None
        Si self.bd es None o self.bd.zona no es la zona que se est\xe1 calificando, se recarga la lectura de la base de datos
        datosIniciales: le pueden llegar los datosIniciales del edificio objeto o del edificio de referencia
        """
        if self.bd == None:
            self.bd = leerBDDesdeArchivo.BDTerciario(zona=datosIniciales.zonaHE1, tipoEdificio=datosIniciales.tipoEdificio, cargasInternas=datosIniciales.cargasInternas, extrapeninsular=datosIniciales.extrapeninsular, area=datosIniciales.area)
        elif self.bd.zona != datosIniciales.zonaHE1 or self.bd.extrapeninsular != datosIniciales.extrapeninsular or self.bd.cargasInternas != datosIniciales.cargasInternas:
            self.bd = leerBDDesdeArchivo.BDTerciario(zona=datosIniciales.zonaHE1, tipoEdificio=datosIniciales.tipoEdificio, cargasInternas=datosIniciales.cargasInternas, extrapeninsular=datosIniciales.extrapeninsular, area=datosIniciales.area)
        return

    def calificacion(self):
        self.datosIniciales = datosEdificioIniciales(self)
        if self.casoValido == False:
            return
        self.recargarBD(datosIniciales=self.datosIniciales)
        self.datosGlobales = datosEdificioGlobales(self, datosIniciales=self.datosIniciales)
        if self.casoValido == False:
            return
        self.datosResultados = datosEdificioResultados(self, datosIniciales=self.datosIniciales, datosGlobales=self.datosGlobales)
        self.datosInicialesEdifRef = copy.deepcopy(self.datosIniciales)
        self.datosInicialesEdifRef.crearEdificioReferencia()
        self.recargarBD(datosIniciales=self.datosInicialesEdifRef)
        self.datosGlobalesEdifRef = datosEdificioGlobales(self, datosIniciales=self.datosInicialesEdifRef)
        self.datosResultadosEdifRef = datosEdificioResultados(self, datosIniciales=self.datosInicialesEdifRef, datosGlobales=self.datosGlobalesEdifRef)
        self.calculoNotasIndicadoresEnergeticos()

    def calculoNotasIndicadoresEnergeticos(self):
        """
        Metodo: calculoNotasIndicadoresEnergeticos
        Permite calcular las notas de los indicadores energ\xe9ticos parciales y totales
        """
        diccNombresVariables = {'ddaBrutaCal': 'demandaCalefaccion',
         'ddaBrutaRef': 'demandaRefrigeracion',
         'emisionesCal': 'emisionesCalefaccion',
         'emisionesRef': 'emisionesRefrigeracion',
         'emisionesACS': 'emisionesACS',
         'emisionesIlum': 'emisionesIlum',
         'emisiones': 'emisionesTotales',
         'enPrimNoRenCal': 'cEPcalefaccion',
         'enPrimNoRenRef': 'cEPrefrigeracion',
         'enPrimNoRenACS': 'cEPACS',
         'enPrimNoRenIlum': 'cEPIlum',
         'enPrimNoRen': 'cEPtotal'}
        listaAux = ['AB',
         'BC',
         'CD',
         'DE',
         'EF',
         'FG']
        for key in diccNombresVariables.keys():
            exec 'self.datosResultados.%s_limites = []' % key
            for i in listaAux:
                IEElim = self.escala[i]
                exec 'valorLimite = IEElim * self.datosResultadosEdifRef.%s' % key
                exec 'self.datosResultados.%s_limite%s = valorLimite' % (key, i)
                exec 'self.datosResultados.%s_limites.append(valorLimite)' % key

            exec 'limites = self.datosResultados.%s_limites' % key
            exec 'valorCalificar = self.datosResultados.%s' % key
            nota = self.calculoNotaCalificacion(limites=limites, valorCalificar=valorCalificar)
            exec 'self.datosResultados.%s_nota = nota' % key


class ListadoEquipoGeneracion():
    """
    Contiene un atributo self.listado que contiene obj de tipo EquipoGeneracion
    Ademas, cuando se a\xf1ade al listado un obj, se recalcula coberturaM2
    """

    def __init__(self):
        self.listado = []
        self.coberturaM2 = 0.0

    def anadir(self, equipo = None):
        self.listado.append(equipo)
        self.coberturaM2 += equipo.coberturaM2


class EquipoGeneracion():

    def __init__(self, nombre = None, tipo = None, rendimiento = 0.01, generador = None, combustible = None, coberturaM2 = 0.0, coberturaPorc = 0.0, acumulacion = [False], subgrupo = '', modoObtencion = u'Por defecto', potencia = '', objListado = None):
        """
        objListado, es el obj ListadoEquipoGeneracion al que va a pertenecer
        """
        self.nombre = nombre
        self.tipo = tipo
        try:
            rendimiento = float(rendimiento)
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            rendimiento = rendimiento

        self.rendimiento = rendimiento
        self.generador = generador
        self.combustible = combustible
        try:
            coberturaM2 = float(coberturaM2)
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            coberturaM2 = coberturaM2

        self.coberturaM2 = coberturaM2
        try:
            coberturaPorc = float(coberturaPorc)
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            coberturaPorc = coberturaPorc

        self.coberturaPorc = coberturaPorc
        self.acumulacion = acumulacion
        self.subgrupo = subgrupo
        self.modoObtencion = modoObtencion
        self.potencia = potencia
        if objListado != None:
            self.objListado = objListado
            self.objListado.anadir(equipo=self)
        return


class ListadoContribucionesEnergeticas():
    """
    Contiene un atributo self.listado que contiene obj de tipo ContribucionesEnergeticas
    Ademas, cuando se a\xf1ade al listado un obj, se recalculan variables globales
    """

    def __init__(self):
        self.listado = []
        self.porcACSTotal = 0.0
        self.porcCalTotal = 0.0
        self.porcRefTotal = 0.0
        self.calorRecupACSTotal = 0.0
        self.calorRecupCalTotal = 0.0
        self.calorRecupRefTotal = 0.0
        self.electricidadGenTotal = 0.0
        self.enConsum_GasNatural = 0.0
        self.enConsum_Gasoil = 0.0
        self.enConsum_Electricidad = 0.0
        self.enConsum_GLP = 0.0
        self.enConsum_Carbon = 0.0
        self.enConsum_Biocarburante = 0.0
        self.enConsum_BiomasaNoDens = 0.0
        self.enConsum_BiomasaDens = 0.0

    def anadir(self, equipo = None):
        self.listado.append(equipo)
        self.calculoContribucionTotal(equipo)

    def calculoContribucionTotal(self, equipo):
        if equipo.porcACS == '':
            porcACS = 0.0
        else:
            porcACS = float(equipo.porcACS)
        self.porcACSTotal += porcACS
        if equipo.porcCal == '':
            porcCal = 0.0
        else:
            porcCal = float(equipo.porcCal)
        self.porcCalTotal += porcCal
        if equipo.porcRef == '':
            porcRef = 0.0
        else:
            porcRef = float(equipo.porcRef)
        self.porcRefTotal += porcRef
        if equipo.calorRecupACS == '':
            calorRecupACS = 0.0
        else:
            calorRecupACS = float(equipo.calorRecupACS)
        self.calorRecupACSTotal += calorRecupACS
        if equipo.calorRecupCal == '':
            calorRecupCal = 0.0
        else:
            calorRecupCal = float(equipo.calorRecupCal)
        self.calorRecupCalTotal += calorRecupCal
        if equipo.calorRecupRef == '':
            calorRecupRef = 0.0
        else:
            calorRecupRef = float(equipo.calorRecupRef)
        self.calorRecupRefTotal += calorRecupRef
        if equipo.electricidadGen == '':
            electricidadGen = 0.0
        else:
            electricidadGen = float(equipo.electricidadGen)
        self.electricidadGenTotal += electricidadGen
        if equipo.enConsum != '':
            if equipo.combustible == u'Gas Natural':
                self.enConsum_GasNatural += float(equipo.enConsum)
            if equipo.combustible == u'Gas\xf3leo-C':
                self.enConsum_Gasoil += float(equipo.enConsum)
            if equipo.combustible == u'Electricidad':
                self.enConsum_Electricidad += float(equipo.enConsum)
            if equipo.combustible == u'GLP':
                self.enConsum_GLP += float(equipo.enConsum)
            if equipo.combustible == u'Carb\xf3n':
                self.enConsum_Carbon += float(equipo.enConsum)
            if equipo.combustible == u'Biocarburante':
                self.enConsum_Biocarburante += float(equipo.enConsum)
            if equipo.combustible == u'Biomasa/Renovable':
                self.enConsum_BiomasaNoDens += float(equipo.enConsum)
            if equipo.combustible == u'BiomasaDens':
                self.enConsum_BiomasaDens += float(equipo.enConsum)


class ContribucionesEnergeticas():

    def __init__(self, nombre = '', porcACS = 0.0, porcCal = 0.0, porcRef = 0.0, calorRecupACS = 0.0, calorRecupCal = 0.0, calorRecupRef = 0.0, electricidadGen = 0.0, enConsum = 0.0, combustible = None, objListado = None):
        self.nombre = nombre
        self.porcACS = porcACS
        self.porcCal = porcCal
        self.porcRef = porcRef
        self.calorRecupACS = calorRecupACS
        self.calorRecupCal = calorRecupCal
        self.calorRecupRef = calorRecupRef
        self.electricidadGen = electricidadGen
        self.enConsum = enConsum
        self.combustible = combustible
        if objListado != None:
            self.objListado = objListado
            self.objListado.anadir(equipo=self)
        return


class Cerramiento():

    def __init__(self, nombre = '', tipo = '', enContactoCon = '', superficieBruta = 0.0, superficieNeta = 0.0, orientacion = '', patronSombras = u'Sin patr\xf3n', U = 0.0, masaM2 = 0.0, subgrupo = u'Edificio Objeto', listadoHuecos = [], modoObtencion = u'Por defecto'):
        self.nombre = nombre
        self.tipo = tipo
        self.enContactoCon = enContactoCon
        self.superficieBruta = float(superficieBruta)
        self.superficieNeta = float(superficieNeta)
        self.orientacion = orientacion
        self.patronSombras = patronSombras
        self.U = float(U)
        self.masaM2 = float(masaM2)
        self.subgrupo = subgrupo
        self.listadoHuecos = listadoHuecos
        self.modoObtencion = modoObtencion
        self.calculoSuperficieNeta()
        self.mensajeAviso = self.comprobar()

    def calculoSuperficieNeta(self):
        superficieHuecos = 0.0
        for h in self.listadoHuecos:
            superficieHuecos += float(h.superficie)

        self.superficieHuecos = superficieHuecos
        self.superficieNeta = self.superficieBruta - superficieHuecos

    def comprobar(self):
        mensajeAviso = None
        if self.superficieHuecos > self.superficieBruta:
            mensajeAviso = self.nombre
        return mensajeAviso


class PuenteTermico():

    def __init__(self, nombre = '', tipo = '', fi = 0.0, longitud = 0.0, cerramientoAsociado = '', subgrupo = u'Edificio Objeto'):
        self.nombre = nombre
        self.tipo = tipo
        self.fi = float(fi)
        self.longitud = float(longitud)
        self.cerramientoAsociado = cerramientoAsociado
        self.subgrupo = subgrupo