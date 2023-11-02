# File: e (Python 2.7)

from Calculos import listadosWeb
from Calculos.funcionesCalculo import coeficienteDePasoEnergiaPrimaria, coeficienteDePasoEmisiones
from Calculos.listados import programaVersion, Localizacion
from datosEdificio import datosEdificioResultados, datosEdificioGlobales
from moduloXML.archivoXML import ArchivoXML
from moduloXML.funcionesXML import calculoVolumenEspacioHabitable, calculoUhueco, calculoDemandaConjunta, calculoPorcentajeCubiertoInstalacion, calculoCompacidad, calculoSuperficieAcristalada, getValorVariable
import copy
import datetime
import directorios
import logging
DirectorioDoc = directorios.BuscaDirectorios().DirectorioDoc
Directorio = directorios.BuscaDirectorios().Directorio
valorVacio = 1e+008

def escribirXML(filename = '', objEdificio = None, datosAdmin = [], listadoConjuntosMMUsuario = [], datosConfiguracionInforme = [], tipoProcedimiento = 'CertificacionExistente'):
    """
    M\xe9todo: escribirXML
    Argumentos:
        - tipoProcedimiento: puede variar segun lo que este haciendo 'CertificacionExistente', 'CertificacionVerificacionExistente'....
    """
    xml = ArchivoXML(encoding = 'utf-8')
    if filename == None or filename == '':
        filename = DirectorioDoc + '/archivoXMl.xml'
    elif '.cex' in filename:
        filename = filename.replace('.cex', '.xml')
    elif '.CEX' in filename:
        filename = filename.replace('.CEX', '.xml')
    else:
        filename = DirectorioDoc + '/archivoXMl.xml'
    conjuntosMMSeleccionados = [
        datosConfiguracionInforme[0],
        datosConfiguracionInforme[1],
        datosConfiguracionInforme[2]]
    listadoConjuntosMMUsuarioSeleccionados = []
    for conjuntoMM in listadoConjuntosMMUsuario:
        if conjuntoMM.nombre in conjuntosMMSeleccionados:
            listadoConjuntosMMUsuarioSeleccionados.append(conjuntoMM)
            continue
    
    try:
        
        try:
            fecha = datosConfiguracionInforme[5]
            if fecha != [
                '',
                '',
                '']:
                dia = fecha[0]
                mes = fecha[1]
                anno = fecha[2]
            else:
                fecha = datetime.date.today()
                dia = fecha.day
                mes = fecha.month
                anno = fecha.year
            fechaElaboracionCertificado = u'%s/%s/%s' % (dia, mes, anno)
        except:
            xml.logErrores.append(_(u'No se ha definido la fecha de elaboraci\xc3\xb3n del certificado'))

        
        try:
            getDatosDelCertificador(xml, datosAdmin, fechaElaboracionCertificado)
        except:
            xml.logErrores.append(_(u'No se han generado los datos del certificador porque faltan o son incorrectos'))

        
        try:
            getIdentificacionEdificio(xml, objEdificio = objEdificio, datosAdmin = datosAdmin, tipoProcedimiento = 'CertificacionExistente')
        except:
            xml.logErrores.append(_(u'No se han generado los datos de identificaci\xc3\xb3n del edificio porque faltan o son incorrectos'))

        
        try:
            getDatosGeneralesYGeometria(xml, objEdificio = objEdificio)
        except:
            xml.logErrores.append(_(u'No se han generado los datos generales y la geometr\xc3\xada porque faltan datos o son incorrectos'))

        
        try:
            getCerramientosOpacos(xml, cerramientos = objEdificio.datosIniciales.listadoCerramientos)
        except:
            xml.logErrores.append(_(u'No se han generado los datos de los cerramientos opacos porque faltan o son incorrectos'))

        
        try:
            getHuecosyLucernarios(xml, huecos = objEdificio.datosIniciales.listadoHuecos)
        except:
            xml.logErrores.append(_(u'No se han generado los datos de huecos y lucernarios porque faltan o son incorrectos'))

        
        try:
            getPuentesTermicos(xml, puentesTermicos = objEdificio.datosIniciales.puentesTermicos)
        except:
            xml.logErrores.append(_(u'No se han generado los datos de Puentes t\xc3\xa9rmicos porque faltan o son incorrectos'))

        
        try:
            getGeneradores(xml, objEdificio = objEdificio)
        except:
            xml.logErrores.append(_(u'No se han generado los datos de Instalaciones t\xc3\xa9rmicas porque faltan o son incorrectos'))

        
        try:
            getTorresRefrigeracion(xml, datosTorresRefrigeracion = objEdificio.datosIniciales.sistemasTorresRefrigeracion)
        except:
            xml.logErrores.append(_(u'No se han generado los datos de las torres de refrigeraci\xc3\xb3n porque faltan o son incorrectos'))

        
        try:
            getVentiladoresyBombas(xml, datosVentiladores = objEdificio.datosIniciales.sistemasVentiladores, datosBombas = objEdificio.datosIniciales.sistemasBombas)
        except:
            xml.logErrores.append(_(u'No se han generado los datos de ventiladores y bombas porque faltan o son incorrectos'))

        
        try:
            getInstalacionesIluminacion(xml, objEdificio = objEdificio)
        except:
            xml.logErrores.append(_(u'No se han generado los datos de la instalaci\xc3\xb3n de iluminaci\xc3\xb3n porque faltan o son incorrectos'))

        
        try:
            getCondicionesFuncionamientoyOcupacion(xml, objEdificio = objEdificio)
        except:
            xml.logErrores.append(_(u'No se han generado los datos de las condiciones de funcionamiento y ocupaci\xc3\xb3n porque faltan o son incorrectos'))

        
        try:
            getContribucionesEnergeticas(xml, listadoContribuciones = objEdificio.datosIniciales.contribuciones, objEdificio = objEdificio)
        except:
            xml.logErrores.append(_(u'No se han generado los datos de Contribuciones energ\xc3\xa9ticas porque faltan o son incorrectos'))

        
        try:
            getDemanda(xml, objEdificio = objEdificio)
            getConsumo(xml, objEdificio = objEdificio)
            getEmisionesCO2(xml, objEdificio = objEdificio)
            getNotasCalificacion(xml, objEdificio = objEdificio)
        except:
            xml.logErrores.append(_(u'No se han generado los datos de Resultados de la calificaci\xc3\xb3n porque se ha producido alg\xc3\xban error'))

        
        try:
            getMedidasMejora(xml, listadoConjuntosMMUsuario = listadoConjuntosMMUsuarioSeleccionados, objEdificio = objEdificio)
        except:
            xml.logErrores.append(_(u'No se han generado los datos de las medidas de mejora porque faltan o son incorrectos'))

        
        try:
            getPruebasComprobacionesInspecciones(xml, datosConfiguracionInforme)
        except:
            xml.logErrores.append(_(u'No se han generado los datos de pruebas, comprobaciones e inspecciones porque faltan o son incorrectos. Genere previamente el informe de certificaci\xc3\xb3n y despu\xc3\xa9s el .xml.'))

        
        try:
            datosPersonalizados = { }
            getDatosPersonalizados(xml)
        except:
            xml.logErrores.append(_(u'No se han generado los datos personalizados porque faltan o son incorrectos'))

        
        try:
            xml.grabaArchivo(filename)
        except:
            xml.logErrores.append(_(u'No se ha podido grabar el archivo .xml'))

        xml.SacarLosErrores(filename)
        return xml
    except:
        xml.logErrores.append(_(u'Ha habido un problema en la generaci\xc3\xb3n del archivo .xml'))
        xml.SacarLosErrores(filename)
        return xml



def getDatosDelCertificador(xml, datosAdmin = [], fechaElaboracionCertificado = ''):
    aux = Localizacion()
    xml.DatosDelCertificador(NombreyApellidos = datosAdmin[11], NIF = datosAdmin[19], RazonSocial = datosAdmin[10], NIFEntidad = datosAdmin[20], Domicilio = datosAdmin[21], Municipio = datosAdmin[23], CodigoPostal = datosAdmin[24], Provincia = datosAdmin[22], ComunidadAutonoma = aux.getCCAA(datosAdmin[22]), Email = datosAdmin[13], Telefono = datosAdmin[12], Titulacion = datosAdmin[25], Fecha = fechaElaboracionCertificado)


def getIdentificacionEdificio(xml, objEdificio = None, datosAdmin = [], tipoProcedimiento = 'CertificacionExistente'):
    aux = Localizacion()
    if datosAdmin[2] == 'Otro':
        localidad = datosAdmin[4]
    else:
        localidad = datosAdmin[2]
    if objEdificio.programa == 'Residencial':
        if objEdificio.datosIniciales.tipoEdificio == u'Unifamiliar':
            tipoEdificio = 'ViviendaUnifamiliar'
        elif objEdificio.datosIniciales.tipoEdificio == u'Bloque de Viviendas':
            tipoEdificio = 'BloqueDeViviendaCompleto'
        else:
            tipoEdificio = 'ViviendaIndividualEnBloque'
    elif objEdificio.datosIniciales.tipoUsoTerciario == u'Edificio completo':
        tipoEdificio = 'EdificioUsoTerciario'
    else:
        tipoEdificio = 'LocalUsoTerciario'
    listadoRefCat = datosAdmin[15]
    xml.IdentificacionEdificio(NombreDelEdificio = datosAdmin[0], Direccion = datosAdmin[1], Municipio = localidad, CodigoPostal = datosAdmin[14], Provincia = datosAdmin[3], ComunidadAutonoma = aux.getCCAA(datosAdmin[3]), ZonaClimatica = objEdificio.datosIniciales.zonaHE1, AnoConstruccion = objEdificio.datosIniciales.annoConstruccion, ReferenciaCatastral = listadoRefCat, TipoDeEdificio = tipoEdificio, NormativaVigente = objEdificio.datosIniciales.normativaVigente, Procedimiento = programaVersion.decode('cp1252'), AlcanceInformacionXML = tipoProcedimiento)


def getDatosGeneralesYGeometria(xml, objEdificio = None):
    volumenEspacioHabitable = calculoVolumenEspacioHabitable(superficie = objEdificio.datosIniciales.area, altura = objEdificio.datosIniciales.altura)
    porcentajeSuperficieHabitableCalefactada = calculoPorcentajeCubiertoInstalacion(listadoInstalaciones = objEdificio.datosIniciales.calefaccion, superficie = objEdificio.datosIniciales.area)
    porcentajeSuperficieHabitableRefrigerada = calculoPorcentajeCubiertoInstalacion(listadoInstalaciones = objEdificio.datosIniciales.refrigeracion, superficie = objEdificio.datosIniciales.area)
    compacidad = calculoCompacidad(listadoCerramientos = objEdificio.datosIniciales.listadoCerramientos, volumenEspacioHabitable = volumenEspacioHabitable)
    if objEdificio.programa == 'Residencial':
        xml.DatosGeneralesyGeometria(NumeroDePlantasSobreRasante = round(valorVacio, 2), NumeroDePlantasBajoRasante = int(round(valorVacio, 0)), SuperficieHabitable = objEdificio.datosIniciales.area, VolumenEspacioHabitable = round(volumenEspacioHabitable, 2), Compacidad = round(compacidad, 2), PorcentajeSuperficieHabitableCalefactada = int(round(porcentajeSuperficieHabitableCalefactada, 0)), PorcentajeSuperficieHabitableRefrigerada = int(round(porcentajeSuperficieHabitableRefrigerada, 0)), Imagen = objEdificio.datosIniciales.imagen, Plano = objEdificio.datosIniciales.plano, DensidadFuentesInternas = round(objEdificio.datosIniciales.cargasInternas, 2), VentilacionUsoResidencial = objEdificio.datosIniciales.tasaVentilacion, VentilacionTotal = round(objEdificio.datosGlobales.renh / objEdificio.datosIniciales.altura, 2), DemandaDiariaACS = round(objEdificio.datosIniciales.Q_ACS, 2))
    else:
        xml.DatosGeneralesyGeometria(NumeroDePlantasSobreRasante = round(valorVacio, 2), NumeroDePlantasBajoRasante = int(round(valorVacio, 0)), SuperficieHabitable = objEdificio.datosIniciales.area, VolumenEspacioHabitable = round(volumenEspacioHabitable, 2), Compacidad = round(compacidad, 2), PorcentajeSuperficieHabitableCalefactada = int(round(porcentajeSuperficieHabitableCalefactada, 0)), PorcentajeSuperficieHabitableRefrigerada = int(round(porcentajeSuperficieHabitableRefrigerada, 0)), Imagen = objEdificio.datosIniciales.imagen, Plano = objEdificio.datosIniciales.plano, DensidadFuentesInternas = round(objEdificio.datosIniciales.cargasInternas, 2), VentilacionTotal = round(objEdificio.datosGlobales.renh / objEdificio.datosIniciales.altura, 2), DemandaDiariaACS = round(objEdificio.datosIniciales.Q_ACS, 2))
    porcentajeSupAcristaladaNorte = calculoSuperficieAcristalada(listadoCerramientos = objEdificio.datosIniciales.listadoCerramientos, orientacion = 'Norte')
    porcentajeSupAcristaladaNE = calculoSuperficieAcristalada(listadoCerramientos = objEdificio.datosIniciales.listadoCerramientos, orientacion = 'NE')
    porcentajeSupAcristaladaEste = calculoSuperficieAcristalada(listadoCerramientos = objEdificio.datosIniciales.listadoCerramientos, orientacion = 'Este')
    porcentajeSupAcristaladaSE = calculoSuperficieAcristalada(listadoCerramientos = objEdificio.datosIniciales.listadoCerramientos, orientacion = 'SE')
    porcentajeSupAcristaladaSur = calculoSuperficieAcristalada(listadoCerramientos = objEdificio.datosIniciales.listadoCerramientos, orientacion = 'Sur')
    porcentajeSupAcristaladaSO = calculoSuperficieAcristalada(listadoCerramientos = objEdificio.datosIniciales.listadoCerramientos, orientacion = 'SO')
    porcentajeSupAcristaladaOeste = calculoSuperficieAcristalada(listadoCerramientos = objEdificio.datosIniciales.listadoCerramientos, orientacion = 'Oeste')
    porcentajeSupAcristaladaNO = calculoSuperficieAcristalada(listadoCerramientos = objEdificio.datosIniciales.listadoCerramientos, orientacion = 'NO')
    xml.PorcentajeSuperficieAcristalada(N = int(round(porcentajeSupAcristaladaNorte, 0)), NE = int(round(porcentajeSupAcristaladaNE, 0)), E = int(round(porcentajeSupAcristaladaEste, 0)), SE = int(round(porcentajeSupAcristaladaSE, 0)), S = int(round(porcentajeSupAcristaladaSur, 0)), SO = int(round(porcentajeSupAcristaladaSO, 0)), O = int(round(porcentajeSupAcristaladaOeste, 0)), NO = int(round(porcentajeSupAcristaladaNO, 0)))


def getCerramientosOpacos(xml, cerramientos = []):
    diccTipoCerramiento = {
        u'Fachada': {
            u'aire': u'Fachada',
            u'edificio': u'Adiabatico',
            u'terreno': u'Fachada' },
        u'Cubierta': {
            u'aire': u'Cubierta',
            u'terreno': u'Cubierta' },
        u'Suelo': {
            u'aire': u'Suelo',
            u'terreno': u'Suelo' },
        u'Partici\xc3\xb3n Interior': {
            u'vertical': u'ParticionInteriorVertical',
            u'horizontal inferior': u'ParticionInteriorHorizontal',
            u'horizontal superior': u'ParticionInteriorHorizontal' } }
    for cerr in cerramientos:
        listadoCapas = []
        if cerr.tipo == 'Partici\xf3n Interior':
            if cerr.enContactoCon == 'vertical':
                orientacion = 'Vertical'
            else:
                orientacion = 'Horizontal'
        elif cerr.orientacion == 'Techo':
            orientacion = 'Horizontal'
        else:
            orientacion = cerr.orientacion
        tipoCerramiento = diccTipoCerramiento[cerr.tipo][cerr.enContactoCon]
        xml.CerramientoOpaco(Nombre = cerr.nombre, Tipo = tipoCerramiento, Superficie = round(cerr.superficieBruta, 2), Orientacion = orientacion, Transmitancia = round(cerr.U, 2), ModoDeObtencion = getModoObtencion(cerr.modoObtencion), Capas = listadoCapas)
    


def getHuecosyLucernarios(xml, huecos = []):
    for hueco in huecos:
        if hueco.__tipo__ == 'HuecoConocidas':
            modoObtencion = u'Conocidas'
            tipoVidrio = ''
            tipoMarco = ''
        else:
            modoObtencion = u'Estimadas'
            tipoVidrio = hueco.tipoVidrio
            tipoMarco = hueco.tipoMarco
        if hueco.orientacion == 'Techo':
            orientacion = 'Horizontal'
        else:
            orientacion = hueco.orientacion
        xml.Hueco(Nombre = hueco.descripcion, Tipo = hueco.tipo, Superficie = round(float(hueco.superficie), 2), Transmitancia = round(hueco.calculoUhueco(), 2), FactorSolar = round(float(hueco.calculoFShueco()), 2), ModoDeObtencionTransmitancia = getModoObtencion(modoObtencion), ModoDeObtencionFactorSolar = getModoObtencion(modoObtencion), Orientacion = orientacion)
    


def getPuentesTermicos(xml, puentesTermicos = []):
    for pt in puentesTermicos:
        if pt[5] == 'usuario_fi':
            modoDeObtencion = getModoObtencion('Conocid')
        else:
            modoDeObtencion = getModoObtencion('PorDefecto')
        xml.PuenteTermico(Nombre = pt[0], Tipo = pt[2], Longitud = round(float(pt[4]), 2), Transmitancia = round(float(pt[3]), 2), ModoDeObtencion = modoDeObtencion)
    


def getGeneradores(xml, objEdificio = None):
    getGeneradoreTermicos(xml, instalaciones = objEdificio.datosIniciales.calefaccion.listado, contador = 1, objEdificio = objEdificio)
    getGeneradoreTermicos(xml, instalaciones = objEdificio.datosIniciales.refrigeracion.listado, contador = 2, objEdificio = objEdificio)
    getGeneradoreTermicos(xml, instalaciones = objEdificio.datosIniciales.ACS.listado, contador = 0, objEdificio = objEdificio)


def getGeneradoreTermicos(xml, instalaciones = [], contador = 0, objEdificio = None):
    '''0: instalacion de ACS
       1: instalacion de calefaccion
       2: instalacion de refrigeracion '''
    for inst in instalaciones:
        if inst.combustible == u'Electricidad':
            if objEdificio.datosIniciales.extrapeninsular == False:
                vectorCombustible = u'ElectricidadPeninsular'
            elif objEdificio.datosIniciales.provincia == 'Illes Balears':
                vectorCombustible = u'ElectricidadBaleares'
            elif objEdificio.datosIniciales.provincia in ('Las Palmas', 'Santa Cruz de Tenerife'):
                vectorCombustible = u'ElectricidadCanarias'
            else:
                vectorCombustible = u'ElectricidadCeutayMelilla'
        else:
            diccCombustible = {
                u'Gas Natural': 'GasNatural',
                u'Gas\xc3\xb3leo-C': 'GasoleoC',
                u'GLP': 'GLP',
                u'Carb\xc3\xb3n': 'Carbon',
                u'BiomasaDens': 'BiomasaPellet',
                u'Biomasa/Renovable': 'BiomasaOtros',
                u'Biocarburante': 'Biocarburante' }
            vectorCombustible = diccCombustible[inst.combustible]
        if inst.potencia == '':
            potencia = valorVacio
        else:
            
            try:
                potencia = round(float(inst.potencia), 2)
            except:
                potencia = valorVacio

        rendimientoNominal = valorVacio
        if contador == 0:
            xml.InstalacionACS(Nombre = inst.nombre, Tipo = inst.generador, PotenciaNominal = potencia, RendimientoNominal = round(rendimientoNominal, 2), RendimientoEstacional = inst.rendimiento, VectorEnergetico = vectorCombustible, ModoDeObtencion = getModoObtencion(inst.modoObtencion))
            continue
        if contador == 1:
            xml.GeneradorDeCalefaccion(Nombre = inst.nombre, Tipo = inst.generador, PotenciaNominal = potencia, RendimientoNominal = round(rendimientoNominal, 2), RendimientoEstacional = inst.rendimiento, VectorEnergetico = vectorCombustible, ModoDeObtencion = getModoObtencion(inst.modoObtencion))
            continue
        if contador == 2:
            xml.GeneradorDeRefrigeracion(Nombre = inst.nombre, Tipo = inst.generador, PotenciaNominal = potencia, RendimientoNominal = round(rendimientoNominal, 2), RendimientoEstacional = inst.rendimiento, VectorEnergetico = vectorCombustible, ModoDeObtencion = getModoObtencion(inst.modoObtencion))
            continue


def getContribucionesEnergeticas(xml, listadoContribuciones = None, objEdificio = None):
    '''
    listadoContribuciones es objeto del tipo ListadoContribucionesEnergeticas que contiene
    un listado que tiene como elementos objetos de tipo ContribucionesEnergeticas
    '''
    if len(listadoContribuciones.listado) > 0:
        objEdificioSinContribuciones = copy.deepcopy(objEdificio)
        objEdificioSinContribuciones.datosIniciales.sistemasContribuciones = []
        objEdificioSinContribuciones.datosIniciales.contribuciones = objEdificioSinContribuciones.datosIniciales.getListadoContribuciones()
        if objEdificio.programa != 'Residencial':
            objEdificioSinContribuciones.recargarBD(datosIniciales = objEdificioSinContribuciones.datosIniciales)
        objEdificioSinContribuciones.datosGlobales = datosEdificioGlobales(objEdificioSinContribuciones, datosIniciales = objEdificioSinContribuciones.datosIniciales)
        objEdificioSinContribuciones.datosResultados = datosEdificioResultados(objEdificioSinContribuciones, datosIniciales = objEdificioSinContribuciones.datosIniciales, datosGlobales = objEdificioSinContribuciones.datosGlobales)
        reduccionEnPrimNoRen = objEdificioSinContribuciones.datosResultados.enPrimNoRenMostrar - objEdificio.datosResultados.enPrimNoRenMostrar
        reduccionEmisiones = objEdificioSinContribuciones.datosResultados.emisionesMostrar - objEdificio.datosResultados.emisionesMostrar
        xml.EnergiaRenovable(ReduccionGlobalEnergiaPrimariaNoRenovable = round(reduccionEnPrimNoRen, 2), ReduccionGlobalEmisionesCO2 = round(reduccionEmisiones, 2))
    for inst in listadoContribuciones.listado:
        porcACS = getValorVariable(variable = inst.porcACS)
        porcCal = getValorVariable(variable = inst.porcCal)
        porcRef = getValorVariable(variable = inst.porcRef)
        if porcACS > 0 and porcCal > 0 or porcRef > 0:
            xml.EnergiaRenovableTermica(Nombre = inst.nombre, ConsumoFinalCalefaccion = round(porcCal, 2), ConsumoFinalRefrigeracion = round(porcRef, 2), ConsumoFinalACS = round(porcACS, 2), DemandaACS = round(porcACS, 2))
        calorRecupACS = getValorVariable(variable = inst.calorRecupACS)
        calorRecupCal = getValorVariable(variable = inst.calorRecupCal)
        calorRecupRef = getValorVariable(variable = inst.calorRecupRef)
        electricidadGen = getValorVariable(variable = inst.electricidadGen)
        enConsum = getValorVariable(variable = inst.enConsum)
        if not calorRecupACS > 0 and calorRecupCal > 0 and calorRecupRef > 0 and electricidadGen > 0:
            if enConsum > 0:
                xml.EnergiaRenovableElectrica(Nombre = inst.nombre, EnergiaGeneradaAutoconsumida = round(electricidadGen, 2))
                continue
            return None


def getTorresRefrigeracion(xml, datosTorresRefrigeracion):
    for inst in datosTorresRefrigeracion:
        tipo = listadosWeb.listadoOpcionesTorreDeRefrigeracion[inst[3]][0]
        xml.TorreRefrigeracion(Nombre = inst[0], Tipo = tipo, ServicioAsociado = u'Refrigeraci\xc3\xb3n', ConsumoDeEnergia = round(float(inst[2]), 2))
    


def getVentiladoresyBombas(xml, datosVentiladores, datosBombas):
    instalaciones = datosVentiladores + datosBombas
    for inst in instalaciones:
        if inst[1] == 'ventiladores':
            tipo = listadosWeb.listadoOpcionesVentiladores[inst[3]][0]
            servicio = listadosWeb.listadoOpcionesServicioVentiladores[inst[12]][0]
        elif inst[1] == 'bombas':
            tipo = listadosWeb.listadoOpcionesBombas[inst[3]][0]
            servicio = listadosWeb.listadoOpcionesServicioBombas[inst[12]][0]
        xml.VentilacionYBombeo(Nombre = inst[0], Tipo = tipo, ServicioAsociado = servicio, ConsumoDeEnergia = round(float(inst[2]), 2))
    


def getInstalacionesIluminacion(xml, objEdificio = None):
    if objEdificio.programa == 'Residencial':
        return None
    potenciaTotalInstalada = None
    for inst in objEdificio.datosIniciales.sistemasIluminacion:
        potenciaTotalInstalada += float(inst[2])
    
    potenciaTotalInstaladaM2 = round(potenciaTotalInstalada / objEdificio.datosIniciales.area, 2)
    xml.PotenciaTotalInstaladaIluminacion(PotenciaTotalInstalada = potenciaTotalInstaladaM2)
    for inst in objEdificio.datosIniciales.sistemasIluminacion:
        xml.InstalacionIluminacion(Nombre = inst[0], PotenciaInstalada = round(float(inst[2]), 2), VEEI = round(float(inst[3]), 2), IluminanciaMedia = round(float(inst[9][1]), 2), ModoDeObtencion = getModoObtencion(inst[8]))
    


def getCondicionesFuncionamientoyOcupacion(xml, objEdificio = None):
    if objEdificio.programa == 'Residencial':
        perfilUso = 'residencial-24h-baja'
    else:
        diccPerfilUso = {
            u'Intensidad Baja - 8h': u'noresidencial-8h-baja',
            u'Intensidad Media - 8h': u'noresidencial-8h-media',
            u'Intensidad Alta - 8h': u'noresidencial-8h-alta',
            u'Intensidad Baja - 12h': u'noresidencial-12h-baja',
            u'Intensidad Media - 12h': u'noresidencial-12h-media',
            u'Intensidad Alta - 12h': u'noresidencial-12h-alta',
            u'Intensidad Baja - 16h': u'noresidencial-16h-baja',
            u'Intensidad Media - 16h': u'noresidencial-16h-media',
            u'Intensidad Alta - 16h': u'noresidencial-16h-alta',
            u'Intensidad Baja - 24h': u'noresidencial-24h-baja',
            u'Intensidad Media - 24h': u'noresidencial-24h-media',
            u'Intensidad Alta - 24h': u'noresidencial-24h-alta' }
        perfilUso = diccPerfilUso[objEdificio.datosIniciales.tipoEdificio]
    superficieZonas = 0
    for zona in objEdificio.subgrupos:
        xml.CondicionesFuncionamientoyOcupacion(Nombre = zona.nombre, Superficie = round(float(zona.superficie), 2), NivelDeAcondicionamiento = 'Acondicionado', PerfilDeUso = perfilUso)
        superficieZonas += float(zona.superficie)
    
    if superficieZonas < objEdificio.datosIniciales.area:
        superficieEdificioObjeto = objEdificio.datosIniciales.area - superficieZonas
        xml.CondicionesFuncionamientoyOcupacion(Nombre = 'Edificio Objeto', Superficie = round(superficieEdificioObjeto, 2), NivelDeAcondicionamiento = 'Acondicionado', PerfilDeUso = perfilUso)


def getDemanda(xml, objEdificio = None):
    ddaConjunta = calculoDemandaConjunta(extrapeninsular = objEdificio.datosIniciales.extrapeninsular, ddaCal = objEdificio.datosResultados.ddaBrutaCal, ddaRef = objEdificio.datosResultados.ddaBrutaRef)
    ddaGlobal = objEdificio.datosResultados.ddaBrutaCal + objEdificio.datosResultados.ddaBrutaRef + objEdificio.datosResultados.ddaBrutaACS
    xml.DemandaEdificioObjeto(Global = round(ddaGlobal, 2), Calefaccion = round(objEdificio.datosResultados.ddaBrutaCal, 2), Refrigeracion = round(objEdificio.datosResultados.ddaBrutaRef, 2), ACS = round(objEdificio.datosResultados.ddaBrutaACS, 2), Conjunta = round(ddaConjunta, 2), Calefaccion08 = valorVacio, Refrigeracion08 = valorVacio, Conjunta08 = valorVacio, Ahorro08 = valorVacio)
    if objEdificio.programa != 'Residencial':
        ddaConjuntaEdifRef = calculoDemandaConjunta(extrapeninsular = objEdificio.datosInicialesEdifRef.extrapeninsular, ddaCal = objEdificio.datosResultadosEdifRef.ddaBrutaCal, ddaRef = objEdificio.datosResultadosEdifRef.ddaBrutaRef)
        ddaGlobalEdifRef = objEdificio.datosResultadosEdifRef.ddaBrutaCal + objEdificio.datosResultadosEdifRef.ddaBrutaRef + objEdificio.datosResultadosEdifRef.ddaBrutaACS
        xml.DemandaEdificioDeReferencia(Global = round(ddaGlobalEdifRef, 2), Calefaccion = round(objEdificio.datosResultadosEdifRef.ddaBrutaCal, 2), Refrigeracion = round(objEdificio.datosResultadosEdifRef.ddaBrutaRef, 2), ACS = round(objEdificio.datosResultadosEdifRef.ddaBrutaACS, 2), Conjunta = round(ddaConjunta, 2), Calefaccion08 = valorVacio, Refrigeracion08 = valorVacio, Conjunta08 = valorVacio)


def getConsumo(xml, objEdificio = None):
    extrapeninsular = objEdificio.datosIniciales.extrapeninsular
    provincia = objEdificio.datosIniciales.provincia
    xml.ConsumoFactoresdePasoFinalAPrimariaNoRenovable(GasNatural = coeficienteDePasoEnergiaPrimaria(u'Gas Natural', provincia, extrapeninsular)[2], GasoleoC = coeficienteDePasoEnergiaPrimaria(u'Gas\xc3\xb3leo-C', provincia, extrapeninsular)[2], GLP = coeficienteDePasoEnergiaPrimaria(u'GLP', provincia, extrapeninsular)[2], Carbon = coeficienteDePasoEnergiaPrimaria(u'Carb\xc3\xb3n', provincia, extrapeninsular)[2], BiomasaPellet = coeficienteDePasoEnergiaPrimaria(u'BiomasaDens', extrapeninsular)[2], BiomasaOtros = coeficienteDePasoEnergiaPrimaria(u'Biomasa/Renovable', provincia, extrapeninsular)[2], ElectricidadPeninsular = coeficienteDePasoEnergiaPrimaria(u'Electricidad', u'Navarra', extrapeninsular)[2], ElectricidadBaleares = coeficienteDePasoEnergiaPrimaria(u'Electricidad', u'Illes Balears', extrapeninsular)[2], ElectricidadCanarias = coeficienteDePasoEnergiaPrimaria(u'Electricidad', u'Las Palmas', extrapeninsular)[2], ElectricidadCeutayMelilla = coeficienteDePasoEnergiaPrimaria(u'Electricidad', u'Ceuta', extrapeninsular)[2], Biocarburante = coeficienteDePasoEnergiaPrimaria(u'Biocarburante', provincia, extrapeninsular)[2])
    xml.ConsumoFactoresdePasoFinalAEmisiones(GasNatural = coeficienteDePasoEmisiones(u'Gas Natural', provincia, extrapeninsular), GasoleoC = coeficienteDePasoEmisiones(u'Gas\xc3\xb3leo-C', provincia, extrapeninsular), GLP = coeficienteDePasoEmisiones(u'GLP', provincia, extrapeninsular), Carbon = coeficienteDePasoEmisiones(u'Carb\xc3\xb3n', provincia, extrapeninsular), BiomasaPellet = coeficienteDePasoEmisiones(u'BiomasaDens', provincia, extrapeninsular), BiomasaOtros = coeficienteDePasoEmisiones(u'Biomasa/Renovable', provincia, extrapeninsular), ElectricidadPeninsular = coeficienteDePasoEmisiones(u'Electricidad', u'Navarra', extrapeninsular), ElectricidadBaleares = coeficienteDePasoEmisiones(u'Electricidad', u'Illes Balears', extrapeninsular), ElectricidadCanarias = coeficienteDePasoEmisiones(u'Electricidad', u'Las Palmas', extrapeninsular), ElectricidadCeutayMelilla = coeficienteDePasoEmisiones(u'Electricidad', u'Ceuta', extrapeninsular), Biocarburante = coeficienteDePasoEmisiones(u'Biocarburante', provincia, extrapeninsular))
    diccCombustible = {
        u'GasNatural': u'GasNatural',
        u'GasoleoC': u'Gasoil',
        u'Electricidad': u'Electricidad',
        u'GLP': u'GLP',
        u'Carbon': u'Carbon',
        u'BiomasaPellet': u'BiomasaDens',
        u'BiomasaOtros': u'BiomasaNoDens',
        u'Biocarburante': u'Biocarburante' }
    for comb in diccCombustible.keys():
        exec 'enFinalRealGlobal = round(objEdificio.datosResultados.enFinalReal_%s,2)' % diccCombustible[comb]
        exec 'enFinalRealCalefaccion = round(objEdificio.datosResultados.enFinalRealCal_%s,2)' % diccCombustible[comb]
        exec 'enFinalRealRefrigeracion = round(objEdificio.datosResultados.enFinalRealRef_%s,2)' % diccCombustible[comb]
        exec 'enFinalRealACS = round(objEdificio.datosResultados.enFinalRealACS_%s,2)' % diccCombustible[comb]
        exec 'enFinalRealIluminacion = round(objEdificio.datosResultados.enFinalRealIlum_%s,2)' % diccCombustible[comb]
        if comb == u'Electricidad':
            if objEdificio.datosIniciales.extrapeninsular == False:
                comb = u'ElectricidadPeninsular'
            elif objEdificio.datosIniciales.provincia == 'Illes Balears':
                comb = u'ElectricidadBaleares'
            elif objEdificio.datosIniciales.provincia in ('Las Palmas', 'Santa Cruz de Tenerife'):
                comb = u'ElectricidadCanarias'
            else:
                comb = u'ElectricidadCeutayMelilla'
        xml.ConsumoEnergiaFinal(Combustible = comb, Global = enFinalRealGlobal, Calefaccion = enFinalRealCalefaccion, Refrigeracion = enFinalRealRefrigeracion, ACS = enFinalRealACS, Iluminacion = enFinalRealIluminacion)
    
    xml.ConsumoEnergiaPrimariaNoRenovable(Global = round(objEdificio.datosResultados.enPrimNoRenMostrar, 2), Calefaccion = round(objEdificio.datosResultados.enPrimNoRenCal, 2), Refrigeracion = round(objEdificio.datosResultados.enPrimNoRenRef, 2), ACS = round(objEdificio.datosResultados.enPrimNoRenACS, 2), Iluminacion = round(objEdificio.datosResultados.enPrimNoRenIlum, 2))


def getEmisionesCO2(xml, objEdificio = None):
    emisionesConsumoElectrico = objEdificio.datosResultados.emisiones_Electricidad
    emisionesOtros = objEdificio.datosResultados.emisiones - emisionesConsumoElectrico
    emisionesConsumoElectricoTotal = emisionesConsumoElectrico * objEdificio.datosIniciales.area
    emisionesOtrosTotal = emisionesOtros * objEdificio.datosIniciales.area
    xml.EmisionesCO2(Global = round(objEdificio.datosResultados.emisionesMostrar, 2), Calefaccion = round(objEdificio.datosResultados.emisionesCal, 2), Refrigeracion = round(objEdificio.datosResultados.emisionesRef, 2), ACS = round(objEdificio.datosResultados.emisionesACS, 2), Iluminacion = round(objEdificio.datosResultados.emisionesIlum, 2), ConsumoElectrico = round(emisionesConsumoElectrico, 2), ConsumoOtros = round(emisionesOtros, 2), TotalConsumoElectrico = round(emisionesConsumoElectricoTotal, 2), TotalConsumoOtros = round(emisionesOtrosTotal, 2))


def getNotasCalificacion(xml, objEdificio = None):
    if objEdificio.programa == 'Residencial' and objEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
        xml.CalificacionDemanda(Calefaccion = objEdificio.datosResultados.ddaBrutaCal_nota)
    else:
        xml.CalificacionDemanda(Calefaccion = objEdificio.datosResultados.ddaBrutaCal_nota, Refrigeracion = objEdificio.datosResultados.ddaBrutaRef_nota)
    xml.EscalaDemandaCalefaccion(A = round(objEdificio.datosResultados.ddaBrutaCal_limiteAB, 2), B = round(objEdificio.datosResultados.ddaBrutaCal_limiteBC, 2), C = round(objEdificio.datosResultados.ddaBrutaCal_limiteCD, 2), D = round(objEdificio.datosResultados.ddaBrutaCal_limiteDE, 2), E = round(objEdificio.datosResultados.ddaBrutaCal_limiteEF, 2), F = round(objEdificio.datosResultados.ddaBrutaCal_limiteFG, 2))
    if objEdificio.programa == 'Residencial' and objEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
        pass
    xml.EscalaDemandaRefrigeracion(A = round(objEdificio.datosResultados.ddaBrutaRef_limiteAB, 2), B = round(objEdificio.datosResultados.ddaBrutaRef_limiteBC, 2), C = round(objEdificio.datosResultados.ddaBrutaRef_limiteCD, 2), D = round(objEdificio.datosResultados.ddaBrutaRef_limiteDE, 2), E = round(objEdificio.datosResultados.ddaBrutaRef_limiteEF, 2), F = round(objEdificio.datosResultados.ddaBrutaRef_limiteFG, 2))
    if objEdificio.programa == 'Residencial':
        if objEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
            xml.CalificacionEnergiaPrimariaNoRenovable(Global = objEdificio.datosResultados.enPrimNoRen_nota, Calefaccion = objEdificio.datosResultados.enPrimNoRenCal_nota, ACS = objEdificio.datosResultados.enPrimNoRenACS_nota)
        else:
            xml.CalificacionEnergiaPrimariaNoRenovable(Global = objEdificio.datosResultados.enPrimNoRen_nota, Calefaccion = objEdificio.datosResultados.enPrimNoRenCal_nota, Refrigeracion = objEdificio.datosResultados.enPrimNoRenRef_nota, ACS = objEdificio.datosResultados.enPrimNoRenACS_nota)
    else:
        xml.CalificacionEnergiaPrimariaNoRenovable(Global = objEdificio.datosResultados.enPrimNoRen_nota, Calefaccion = objEdificio.datosResultados.enPrimNoRenCal_nota, Refrigeracion = objEdificio.datosResultados.enPrimNoRenRef_nota, ACS = objEdificio.datosResultados.enPrimNoRenACS_nota, Iluminacion = objEdificio.datosResultados.enPrimNoRenIlum_nota)
    xml.EscalaEnPrimNoRen(A = round(objEdificio.datosResultados.enPrimNoRen_limiteAB, 2), B = round(objEdificio.datosResultados.enPrimNoRen_limiteBC, 2), C = round(objEdificio.datosResultados.enPrimNoRen_limiteCD, 2), D = round(objEdificio.datosResultados.enPrimNoRen_limiteDE, 2), E = round(objEdificio.datosResultados.enPrimNoRen_limiteEF, 2), F = round(objEdificio.datosResultados.enPrimNoRen_limiteFG, 2))
    if objEdificio.programa == 'Residencial':
        if objEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
            xml.CalificacionEmisionesCO2(Global = objEdificio.datosResultados.emisiones_nota, Calefaccion = objEdificio.datosResultados.emisionesCal_nota, ACS = objEdificio.datosResultados.emisionesACS_nota)
        else:
            xml.CalificacionEmisionesCO2(Global = objEdificio.datosResultados.emisiones_nota, Calefaccion = objEdificio.datosResultados.emisionesCal_nota, Refrigeracion = objEdificio.datosResultados.emisionesRef_nota, ACS = objEdificio.datosResultados.emisionesACS_nota)
    else:
        xml.CalificacionEmisionesCO2(Global = objEdificio.datosResultados.emisiones_nota, Calefaccion = objEdificio.datosResultados.emisionesCal_nota, Refrigeracion = objEdificio.datosResultados.emisionesRef_nota, ACS = objEdificio.datosResultados.emisionesACS_nota, Iluminacion = objEdificio.datosResultados.emisionesIlum_nota)
    xml.EscalaEmisiones(A = round(objEdificio.datosResultados.emisiones_limiteAB, 2), B = round(objEdificio.datosResultados.emisiones_limiteBC, 2), C = round(objEdificio.datosResultados.emisiones_limiteCD, 2), D = round(objEdificio.datosResultados.emisiones_limiteDE, 2), E = round(objEdificio.datosResultados.emisiones_limiteEF, 2), F = round(objEdificio.datosResultados.emisiones_limiteFG, 2))


def getMedidasMejora(xml, listadoConjuntosMMUsuario = [], objEdificio = None):
    for conjunto in listadoConjuntosMMUsuario:
        ddaGlobalConjunto = conjunto.datosNuevoEdificio.datosResultados.ddaBrutaCal + conjunto.datosNuevoEdificio.datosResultados.ddaBrutaRef + conjunto.datosNuevoEdificio.datosResultados.ddaBrutaACS
        ddaGlobal = objEdificio.datosResultados.ddaBrutaCal + objEdificio.datosResultados.ddaBrutaRef + objEdificio.datosResultados.ddaBrutaACS
        if objEdificio.programa == 'Residencial':
            if objEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
                xml.MedidaDeMejora(Nombre = conjunto.nombre, Descripcion = conjunto.caracteristicas, CosteEstimado = str(conjunto.calculoInversionInicial()), OtrosDatos = conjunto.otrosDatos, Demanda = {
                    'Global': round(ddaGlobalConjunto, 2),
                    'GlobalDiferenciaSituacionInicial': round(ddaGlobal - ddaGlobalConjunto, 2),
                    'Calefaccion': round(conjunto.datosNuevoEdificio.datosResultados.ddaBrutaCal, 2),
                    'Refrigeracion': round(conjunto.datosNuevoEdificio.datosResultados.ddaBrutaRef, 2) }, CalificacionDemanda = {
                    'Calefaccion': conjunto.datosNuevoEdificio.datosResultados.ddaBrutaCal_nota }, EnergiaFinal = {
                    'Global': round(conjunto.datosNuevoEdificio.datosResultados.enFinalMostrar, 2),
                    'Calefaccion': round(conjunto.datosNuevoEdificio.datosResultados.enFinalCal, 2),
                    'Refrigeracion': round(conjunto.datosNuevoEdificio.datosResultados.enFinalRef, 2),
                    'ACS': round(conjunto.datosNuevoEdificio.datosResultados.enFinalACS, 2) }, EnergiaPrimariaNoRenovable = {
                    'Global': round(conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenMostrar, 2),
                    'GlobalDiferenciaSituacionInicial': round(objEdificio.datosResultados.enPrimNoRenMostrar - conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenMostrar, 2),
                    'Calefaccion': round(conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenCal, 2),
                    'Refrigeracion': round(conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenRef, 2),
                    'ACS': round(conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenACS, 2) }, CalificacionEnergiaPrimariaNoRenovable = {
                    'Global': conjunto.datosNuevoEdificio.datosResultados.enPrimNoRen_nota,
                    'Calefaccion': conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenCal_nota,
                    'ACS': conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenACS_nota }, EmisionesCO2 = {
                    'Global': round(conjunto.datosNuevoEdificio.datosResultados.emisionesMostrar, 2),
                    'GlobalDiferenciaSituacionInicial': round(objEdificio.datosResultados.emisionesMostrar - conjunto.datosNuevoEdificio.datosResultados.emisionesMostrar, 2),
                    'Calefaccion': round(conjunto.datosNuevoEdificio.datosResultados.emisionesCal, 2),
                    'Refrigeracion': round(conjunto.datosNuevoEdificio.datosResultados.emisionesRef, 2),
                    'ACS': round(conjunto.datosNuevoEdificio.datosResultados.emisionesACS, 2) }, CalificacionEmisionesCO2 = {
                    'Global': conjunto.datosNuevoEdificio.datosResultados.emisiones_nota,
                    'Calefaccion': conjunto.datosNuevoEdificio.datosResultados.emisionesCal_nota,
                    'ACS': conjunto.datosNuevoEdificio.datosResultados.emisionesACS_nota })
            else:
                xml.MedidaDeMejora(Nombre = conjunto.nombre, Descripcion = conjunto.caracteristicas, CosteEstimado = str(conjunto.calculoInversionInicial()), OtrosDatos = conjunto.otrosDatos, Demanda = {
                    'Global': round(ddaGlobalConjunto, 2),
                    'GlobalDiferenciaSituacionInicial': round(ddaGlobal - ddaGlobalConjunto, 2),
                    'Calefaccion': round(conjunto.datosNuevoEdificio.datosResultados.ddaBrutaCal, 2),
                    'Refrigeracion': round(conjunto.datosNuevoEdificio.datosResultados.ddaBrutaRef, 2) }, CalificacionDemanda = {
                    'Calefaccion': conjunto.datosNuevoEdificio.datosResultados.ddaBrutaCal_nota,
                    'Refrigeracion': conjunto.datosNuevoEdificio.datosResultados.ddaBrutaRef_nota }, EnergiaFinal = {
                    'Global': round(conjunto.datosNuevoEdificio.datosResultados.enFinalMostrar, 2),
                    'Calefaccion': round(conjunto.datosNuevoEdificio.datosResultados.enFinalCal, 2),
                    'Refrigeracion': round(conjunto.datosNuevoEdificio.datosResultados.enFinalRef, 2),
                    'ACS': round(conjunto.datosNuevoEdificio.datosResultados.enFinalACS, 2) }, EnergiaPrimariaNoRenovable = {
                    'Global': round(conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenMostrar, 2),
                    'GlobalDiferenciaSituacionInicial': round(objEdificio.datosResultados.enPrimNoRenMostrar - conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenMostrar, 2),
                    'Calefaccion': round(conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenCal, 2),
                    'Refrigeracion': round(conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenRef, 2),
                    'ACS': round(conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenACS, 2) }, CalificacionEnergiaPrimariaNoRenovable = {
                    'Global': conjunto.datosNuevoEdificio.datosResultados.enPrimNoRen_nota,
                    'Calefaccion': conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenCal_nota,
                    'Refrigeracion': conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenRef_nota,
                    'ACS': conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenACS_nota }, EmisionesCO2 = {
                    'Global': round(conjunto.datosNuevoEdificio.datosResultados.emisionesMostrar, 2),
                    'GlobalDiferenciaSituacionInicial': round(objEdificio.datosResultados.emisionesMostrar - conjunto.datosNuevoEdificio.datosResultados.emisionesMostrar, 2),
                    'Calefaccion': round(conjunto.datosNuevoEdificio.datosResultados.emisionesCal, 2),
                    'Refrigeracion': round(conjunto.datosNuevoEdificio.datosResultados.emisionesRef, 2),
                    'ACS': round(conjunto.datosNuevoEdificio.datosResultados.emisionesACS, 2) }, CalificacionEmisionesCO2 = {
                    'Global': conjunto.datosNuevoEdificio.datosResultados.emisiones_nota,
                    'Calefaccion': conjunto.datosNuevoEdificio.datosResultados.emisionesCal_nota,
                    'Refrigeracion': conjunto.datosNuevoEdificio.datosResultados.emisionesRef_nota,
                    'ACS': conjunto.datosNuevoEdificio.datosResultados.emisionesACS_nota })
        xml.MedidaDeMejora(Nombre = conjunto.nombre, Descripcion = conjunto.caracteristicas, CosteEstimado = conjunto.calculoInversionInicial(), OtrosDatos = conjunto.otrosDatos, Demanda = {
            'Global': round(ddaGlobalConjunto, 2),
            'GlobalDiferenciaSituacionInicial': round(ddaGlobal - ddaGlobalConjunto, 2),
            'Calefaccion': round(conjunto.datosNuevoEdificio.datosResultados.ddaBrutaCal, 2),
            'Refrigeracion': round(conjunto.datosNuevoEdificio.datosResultados.ddaBrutaRef, 2) }, CalificacionDemanda = {
            'Calefaccion': conjunto.datosNuevoEdificio.datosResultados.ddaBrutaCal_nota,
            'Refrigeracion': conjunto.datosNuevoEdificio.datosResultados.ddaBrutaRef_nota }, EnergiaFinal = {
            'Global': round(conjunto.datosNuevoEdificio.datosResultados.enFinalMostrar, 2),
            'Calefaccion': round(conjunto.datosNuevoEdificio.datosResultados.enFinalCal, 2),
            'Refrigeracion': round(conjunto.datosNuevoEdificio.datosResultados.enFinalRef, 2),
            'ACS': round(conjunto.datosNuevoEdificio.datosResultados.enFinalACS, 2),
            'Iluminacion': round(conjunto.datosNuevoEdificio.datosResultados.enFinalIlum, 2) }, EnergiaPrimariaNoRenovable = {
            'Global': round(conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenMostrar, 2),
            'GlobalDiferenciaSituacionInicial': round(objEdificio.datosResultados.enPrimNoRenMostrar - conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenMostrar, 2),
            'Calefaccion': round(conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenCal, 2),
            'Refrigeracion': round(conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenRef, 2),
            'ACS': round(conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenACS, 2),
            'Iluminacion': round(conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenIlum, 2) }, CalificacionEnergiaPrimariaNoRenovable = {
            'Global': conjunto.datosNuevoEdificio.datosResultados.enPrimNoRen_nota,
            'Calefaccion': conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenCal_nota,
            'Refrigeracion': conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenRef_nota,
            'ACS': conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenACS_nota,
            'Iluminacion': conjunto.datosNuevoEdificio.datosResultados.enPrimNoRenIlum_nota }, EmisionesCO2 = {
            'Global': round(conjunto.datosNuevoEdificio.datosResultados.emisionesMostrar, 2),
            'GlobalDiferenciaSituacionInicial': round(objEdificio.datosResultados.emisionesMostrar - conjunto.datosNuevoEdificio.datosResultados.emisionesMostrar, 2),
            'Calefaccion': round(conjunto.datosNuevoEdificio.datosResultados.emisionesCal, 2),
            'Refrigeracion': round(conjunto.datosNuevoEdificio.datosResultados.emisionesRef, 2),
            'ACS': round(conjunto.datosNuevoEdificio.datosResultados.emisionesACS, 2),
            'Iluminacion': round(conjunto.datosNuevoEdificio.datosResultados.emisionesIlum, 2) }, CalificacionEmisionesCO2 = {
            'Global': conjunto.datosNuevoEdificio.datosResultados.emisiones_nota,
            'Calefaccion': conjunto.datosNuevoEdificio.datosResultados.emisionesCal_nota,
            'Refrigeracion': conjunto.datosNuevoEdificio.datosResultados.emisionesRef_nota,
            'ACS': conjunto.datosNuevoEdificio.datosResultados.emisionesACS_nota,
            'Iluminacion': conjunto.datosNuevoEdificio.datosResultados.emisionesIlum_nota })
    


def getPruebasComprobacionesInspecciones(xml, configuracionInforme):
    textoPruebasComprobacionesInspecciones = configuracionInforme[3]
    
    try:
        fechaVisita = '%s/%s/%s' % (configuracionInforme[6][0], configuracionInforme[6][1], configuracionInforme[6][2])
    except:
        fechaVisita = '-'

    xml.PruebasComprobacionesInspecciones(FechaVisita = fechaVisita, Datos = textoPruebasComprobacionesInspecciones)


def getDatosPersonalizados(xml):
    fechaGeneracion = datetime.date.today()
    xml.DatosPersonalizados(Aplicacion = 'CE3X', FechaGeneracion = '%s/%s/%s' % (fechaGeneracion.day, fechaGeneracion.month, fechaGeneracion.year))


def getModoObtencion(modoObtencionCE3X):
    '''
    Devuelve el modo de obtencion que detecta CE3X
    '''
    if 'Conocid' in modoObtencionCE3X:
        return 'Usuario'
    if None in modoObtencionCE3X:
        return 'Estimado'
    return None

