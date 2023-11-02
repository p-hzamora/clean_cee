# File: f (Python 2.7)

from Calculos.listadosWeb import getTraduccion, listadoCombustibles
import logging

def guardarCostesConjuntosMM(listadoCosteMedidas = [], listadoConjuntosMMUsuario = []):
    listaErrores = ''
    faltanDatos = False
    for conjuntoMM in listadoConjuntosMMUsuario:
        conjuntoMM.analisisEconomico.vidaUtil = []
        conjuntoMM.analisisEconomico.inversionInicial = []
        conjuntoMM.analisisEconomico.costeMantenimiento = []
        for costeMedida in listadoCosteMedidas:
            listaErroresConjunto = ''
            if conjuntoMM.nombre == costeMedida[1]:
                
                try:
                    conjuntoMM.analisisEconomico.vidaUtil.append(float(costeMedida[3]))
                    conjuntoMM.analisisEconomico.inversionInicial.append(float(costeMedida[4]))
                    conjuntoMM.analisisEconomico.costeMantenimiento.append(float(costeMedida[5]))
                    if float(costeMedida[3]) > 100:
                        faltanDatos = True
                        listaErroresConjunto = u'vida \xc3\xbatil'
                except ValueError:
                    faltanDatos = True
                    listaErroresConjunto = u'coste de las medidas'
                

            if listaErroresConjunto != '':
                conjuntoMM.analisisEconomico.inicializar()
                auxNombre = conjuntoMM.nombre.encode('cp1252')
                auxError = listaErroresConjunto.encode('cp1252')
                errorMedida = '   - %s: %s\n' % (auxNombre, auxError)
                listaErrores += errorMedida
                break
                continue
    
    return (faltanDatos, listaErrores)


def comprobarPreciosEnergia(datosEconomicos = [], objEdificio = None, listadoConjuntosMMUsuario = []):
    '''
    M\xe9todo: comprobarPreciosEnergia
    Argumentos:
        datosEconomicos: array conn los datos de los precios y % de la pesta\xf1a de datos eco
        objEdificio: obj del caso base
        listadoConjuntosMMUsuario: array con los conjuntos de mm definidos x usuario
    Devuelve:
        faltanDatos = False si no faltan, True si faltan, 
        listaErrores = str con errores
        diccPreciosCombustibles = combustible: precio, 
        incrementoPrecioEnergia, tipoInteres
    '''
    listaErrores = ''
    faltanDatos = False
    diccPreciosCombustibles = {
        u'Gas Natural': datosEconomicos[0],
        u'Gas\xc3\xb3leo-C': datosEconomicos[1],
        u'Electricidad': datosEconomicos[2],
        u'GLP': datosEconomicos[3],
        u'Carb\xc3\xb3n': datosEconomicos[4],
        u'Biocarburante': datosEconomicos[5],
        u'Biomasa/Renovable': datosEconomicos[6],
        u'BiomasaDens': datosEconomicos[7] }
    incrementoPrecioEnergia = datosEconomicos[8]
    tipoInteres = datosEconomicos[9]
    diccEnFinalxCombustibleCB = objEdificio.datosResultados.calculoConsumoEnFinalSegunCombustible()
    for comb in diccPreciosCombustibles:
        consumoCombustible = diccEnFinalxCombustibleCB[comb]
        precioCombustible = diccPreciosCombustibles[comb]
        combustibleTraducidoMensaje = getTraduccion(listado = listadoCombustibles, elemento = comb)
        if consumoCombustible != 0:
            
            try:
                if float(precioCombustible) < 0:
                    if listaErrores != '':
                        listaErrores += ',  '
                    listaErrores += _(u'precio de ') + combustibleTraducidoMensaje
            except ValueError:
                if listaErrores != '':
                    listaErrores += ',  '
                listaErrores += _(u'precio de ') + combustibleTraducidoMensaje
            

        for conjuntoMM in listadoConjuntosMMUsuario:
            if conjuntoMM.datosNuevoEdificio.casoValido == True:
                
                try:
                    diccEnFinalxCombustibleCM = conjuntoMM.datosNuevoEdificio.datosResultados.calculoConsumoEnFinalSegunCombustible()
                    if diccEnFinalxCombustibleCM[comb] != 0:
                        
                        try:
                            if float(precioCombustible) < 0:
                                if listaErrores != '':
                                    listaErrores += ',  '
                                listaErrores += _(u'precio de ') + combustibleTraducidoMensaje
                        except ValueError:
                            if listaErrores != '':
                                listaErrores += ',  '
                            listaErrores += _(u'precio de ') + combustibleTraducidoMensaje
                            break
                        


                continue
    
    
    try:
        float(incrementoPrecioEnergia)
    except ValueError:
        incrementoPrecioEnergia = ''

    
    try:
        float(tipoInteres)
        if float(tipoInteres) < 0:
            tipoInteres = ''
    except ValueError:
        tipoInteres = ''

    if incrementoPrecioEnergia == '':
        if listaErrores != '':
            listaErrores += ',  '
        listaErrores += _(u'incremento anual del precio de la energ\xc3\xada')
    if tipoInteres == '':
        if listaErrores != '':
            listaErrores += ',  '
        listaErrores += _(u'tipo de inter\xc3\xa9s')
    if listaErrores != '':
        faltanDatos = True
    return (faltanDatos, listaErrores, diccPreciosCombustibles, incrementoPrecioEnergia, tipoInteres)


def getDiccConsumosCBFacturasSgServicioYCombustible(listadoFacturas, area, programa):
    '''
    M\xe9todo: getConsumosCBFacturasSgServicioYCombustible
    Atributos: 
        listadoFacturas: listado de arrays con datos facturas
        area: area edificio
        programa: si es residencial, pt o gt
    Devuelve:
    diccCal_CB_fact, diccRef_CB_fact, diccACS_CB_fact, diccIlum_CB_fact, diccVentiladores_CB_fact, diccBombas_CB_fact, diccTR_CB_fact
    Son diccionarios cuya key es el combustible y donde se suman los consumos para cada combustible en kWh/m2
    seg\xfan el servicio, para el caso base seg\xfan facturas   
    '''
    diccCal_CB_fact = {
        u'Gas Natural': 0,
        u'Gas\xc3\xb3leo-C': 0,
        u'Electricidad': 0,
        u'GLP': 0,
        u'Carb\xc3\xb3n': 0,
        u'Biocarburante': 0,
        u'Biomasa/Renovable': 0,
        u'BiomasaDens': 0 }
    diccRef_CB_fact = {
        u'Gas Natural': 0,
        u'Gas\xc3\xb3leo-C': 0,
        u'Electricidad': 0,
        u'GLP': 0,
        u'Carb\xc3\xb3n': 0,
        u'Biocarburante': 0,
        u'Biomasa/Renovable': 0,
        u'BiomasaDens': 0 }
    diccACS_CB_fact = {
        u'Gas Natural': 0,
        u'Gas\xc3\xb3leo-C': 0,
        u'Electricidad': 0,
        u'GLP': 0,
        u'Carb\xc3\xb3n': 0,
        u'Biocarburante': 0,
        u'Biomasa/Renovable': 0,
        u'BiomasaDens': 0 }
    diccIlum_CB_fact = {
        u'Electricidad': 0 }
    diccVentiladores_CB_fact = {
        u'Electricidad': 0 }
    diccBombas_CB_fact = {
        u'Electricidad': 0 }
    diccTorresRef_CB_fact = {
        u'Electricidad': 0 }
    for factura in listadoFacturas:
        combustible = factura[1]
        consumo = float(factura[3]) * float(factura[4])
        servicios = factura[5]
        if servicios[0][1] != False:
            aux_ACS = consumo * float(servicios[0][0]) / 100 / area
            diccACS_CB_fact[combustible] += aux_ACS
        if servicios[1][1] != False:
            aux_Cal = consumo * float(servicios[1][0]) / 100 / area
            diccCal_CB_fact[combustible] += aux_Cal
        if servicios[2][1] != False:
            aux_Ref = consumo * float(servicios[2][0]) / 100 / area
            diccRef_CB_fact[combustible] += aux_Ref
        if combustible == u'Electricidad' and programa != 'Residencial':
            
            try:
                if servicios[3][1] != False:
                    aux_Ilum = consumo * float(servicios[3][0]) / 100 / area
                    diccIlum_CB_fact[combustible] += aux_Ilum
            except:
                logging.info(u'Excepcion en: %s' % __name__)

            if programa == 'GranTerciario':
                
                try:
                    if servicios[4][1] != False:
                        aux_Ventiladores = consumo * float(servicios[4][0]) / 100 / area
                        diccVentiladores_CB_fact[combustible] += aux_Ventiladores
                except:
                    logging.info(u'Excepcion en: %s' % __name__)

                
                try:
                    if servicios[5][1] != False:
                        aux_Bombas = consumo * float(servicios[5][0]) / 100 / area
                        diccBombas_CB_fact[combustible] += aux_Bombas
                except:
                    logging.info(u'Excepcion en: %s' % __name__)

                
                try:
                    if servicios[6][1] != False:
                        aux_TR = consumo * float(servicios[6][0]) / 100 / area
                        diccTorresRef_CB_fact[combustible] += aux_TR
                logging.info(u'Excepcion en: %s' % __name__)

            
    return (diccCal_CB_fact, diccRef_CB_fact, diccACS_CB_fact, diccIlum_CB_fact, diccVentiladores_CB_fact, diccBombas_CB_fact, diccTorresRef_CB_fact)


def comprobarEstanTodasFacturas(listadoACS_CB, listadoCal_CB, listadoRef_CB, listadoIlum_CB, listadoVentiladores_CB, listadoBombas_CB, listadoTorresRef_CB, diccCal_CB_fact, diccRef_CB_fact, diccACS_CB_fact, diccIlum_CB_fact, diccVentiladores_CB_fact, diccBombas_CB_fact, diccTorresRef_CB_fact):
    '''
    M\xe9todo: comprobarEstanTodasFacturas
    Argumentos: listados de instalaciones del caso base y diccionario x servicio y combustible del caso base real
    Devuelve arrayErrores. Comprueba que para todos los servicios y combustibles se ha indicado una factura
    '''
    arrayErrores = []
    arrayErrores += comprobarFacturaXaCombustibleEquiposGeneracion(listadoInst = listadoACS_CB, dicc_CB_fact = diccACS_CB_fact, servicio = _(u'ACS'))
    arrayErrores += comprobarFacturaXaCombustibleEquiposGeneracion(listadoInst = listadoCal_CB, dicc_CB_fact = diccCal_CB_fact, servicio = _(u'calefacci\xc3\xb3n'))
    arrayErrores += comprobarFacturaXaCombustibleEquiposGeneracion(listadoInst = listadoRef_CB, dicc_CB_fact = diccRef_CB_fact, servicio = _(u'refrigeraci\xc3\xb3n'))
    arrayErrores += comprobarFacturaXaCombustibleEquiposGT(listadoInst = listadoIlum_CB, dicc_CB_fact = diccIlum_CB_fact, servicio = _(u'iluminaci\xc3\xb3n'))
    arrayErrores += comprobarFacturaXaCombustibleEquiposGT(listadoInst = listadoVentiladores_CB, dicc_CB_fact = diccVentiladores_CB_fact, servicio = _(u'ventiladores'))
    arrayErrores += comprobarFacturaXaCombustibleEquiposGT(listadoInst = listadoBombas_CB, dicc_CB_fact = diccBombas_CB_fact, servicio = _(u'bombas'))
    arrayErrores += comprobarFacturaXaCombustibleEquiposGT(listadoInst = listadoTorresRef_CB, dicc_CB_fact = diccTorresRef_CB_fact, servicio = _(u'torres de refrigeraci\xc3\xb3n'))
    return arrayErrores


def comprobarFacturaXaCombustibleEquiposGeneracion(listadoInst, dicc_CB_fact, servicio):
    '''
    M\xe9todo: comprobarFacturaXaCombustible
    Argumentos: 
        listadoInst: listado de instalaciones del cso base
        dicc_CB_fact: diccionario de consumos del caso base segun facturas xa el mismo servicio que el listado de instalaciones
        servicio: para que aparezca en mensaje de error
    Se comprueba que para cada combustible y servicio se ha definido la factura adecuada. 
    Devuelve arrayErrores
    '''
    arrayErrores = []
    listadoCombustiblesCBFact = []
    for equipo in listadoInst:
        if equipo.combustible not in listadoCombustiblesCBFact:
            listadoCombustiblesCBFact.append(equipo.combustible)
            continue
    for combustible in listadoCombustiblesCBFact:
        combustibleTraducidoMensaje = getTraduccion(listado = listadoCombustibles, elemento = combustible)
        if dicc_CB_fact[combustible] == 0:
            error = _(u'    - factura de %s para %s\n' % (combustibleTraducidoMensaje, servicio))
            arrayErrores.append(error)
            continue
    return arrayErrores


def comprobarFacturaXaCombustibleEquiposGT(listadoInst, dicc_CB_fact, servicio):
    '''
    M\xe9todo: comprobarFacturaXaCombustibleEquiposGT
    Argumentos: 
        listadoInst: listado de instalaciones del cso base
        dicc_CB_fact: diccionario de consumos del caso base segun facturas xa el mismo servicio que el listado de instalaciones
        servicio: para que aparezca en mensaje de error
    Se comprueba que est\xe1 la factura de electricidad definida para el servicio correspondiente. 
    Devuelve arrayErrores
    '''
    arrayErrores = []
    combustible = u'Electricidad'
    if dicc_CB_fact[combustible] == 0 and len(listadoInst) > 0:
        combustibleTraducidoMensaje = getTraduccion(listado = listadoCombustibles, elemento = combustible)
        error = _(u'    - factura de %s para %s\n' % (combustibleTraducidoMensaje, servicio))
        arrayErrores.append(error)
    return arrayErrores


def comprobarQueNoHayFacturasExtra(listadoACS_CB, listadoCal_CB, listadoRef_CB, listadoIlum_CB, listadoVentiladores_CB, listadoBombas_CB, listadoTorresRef_CB, diccCal_CB_fact, diccRef_CB_fact, diccACS_CB_fact, diccIlum_CB_fact, diccVentiladores_CB_fact, diccBombas_CB_fact, diccTorresRef_CB_fact):
    '''
    M\xe9todo: comprobarQueNoHayFacturasExtra
    Argumentos: listados de instalaciones del caso base y diccionario x servicio y combustible del caso base real
    Devuelve arrayErrores. Se comprueba que no haya facturas para combustibles y servicios que no existen en caso base
    '''
    arrayErrores = []
    arrayErrores += comprobarQueNoHayFacturaExtraXaCombustibleEquiposGeneracion(listadoInst = listadoACS_CB, dicc_CB_fact = diccACS_CB_fact, servicio = _(u'ACS'))
    arrayErrores += comprobarQueNoHayFacturaExtraXaCombustibleEquiposGeneracion(listadoInst = listadoCal_CB, dicc_CB_fact = diccCal_CB_fact, servicio = _(u'calefacci\xc3\xb3n'))
    arrayErrores += comprobarQueNoHayFacturaExtraXaCombustibleEquiposGeneracion(listadoInst = listadoRef_CB, dicc_CB_fact = diccRef_CB_fact, servicio = _(u'refrigeraci\xc3\xb3n'))
    arrayErrores += comprobarQueNoHayFacturaExtraXaCombustibleEquiposGT(listadoInst = listadoIlum_CB, dicc_CB_fact = diccIlum_CB_fact, servicio = _(u'iluminaci\xc3\xb3n'))
    arrayErrores += comprobarQueNoHayFacturaExtraXaCombustibleEquiposGT(listadoInst = listadoVentiladores_CB, dicc_CB_fact = diccVentiladores_CB_fact, servicio = _(u'ventiladores'))
    arrayErrores += comprobarQueNoHayFacturaExtraXaCombustibleEquiposGT(listadoInst = listadoBombas_CB, dicc_CB_fact = diccBombas_CB_fact, servicio = _(u'bombas'))
    arrayErrores += comprobarQueNoHayFacturaExtraXaCombustibleEquiposGT(listadoInst = listadoTorresRef_CB, dicc_CB_fact = diccTorresRef_CB_fact, servicio = _(u'torres de refrigeraci\xc3\xb3n'))
    return arrayErrores


def comprobarQueNoHayFacturaExtraXaCombustibleEquiposGeneracion(listadoInst, dicc_CB_fact, servicio):
    '''
    M\xe9todo: comprobarQueNoHayFacturaExtraXaCombustibleEquiposGeneracion
    Argumentos: 
        listadoInst: listado de instalaciones del cso base
        dicc_CB_fact: diccionario de consumos del caso base segun facturas xa el mismo servicio que el listado de instalaciones
        servicio: para que aparezca en mensaje de error
    Se comprueba que no hay facturas extra de combustibles y servicios que no se han definido en caso base 
    Devuelve arrayErrores
    '''
    arrayErrores = []
    listadoCombustiblesCB = []
    for equipo in listadoInst:
        if equipo.combustible not in listadoCombustiblesCB:
            listadoCombustiblesCB.append(equipo.combustible)
            continue
    listadoCombustiblesFactura = []
    for combustible in dicc_CB_fact:
        if dicc_CB_fact[combustible] > 0 and combustible not in listadoCombustiblesFactura:
            listadoCombustiblesFactura.append(combustible)
            continue
    for combustible in listadoCombustiblesFactura:
        if combustible not in listadoCombustiblesCB:
            combustibleTraducidoMensaje = getTraduccion(listado = listadoCombustibles, elemento = combustible)
            error = _(u'    - factura de %s para %s\n' % (combustibleTraducidoMensaje, servicio))
            arrayErrores.append(error)
            continue
    return arrayErrores


def comprobarQueNoHayFacturaExtraXaCombustibleEquiposGT(listadoInst, dicc_CB_fact, servicio):
    '''
    M\xe9todo: comprobarFacturaXaCombustibleEquiposGT
    Argumentos: 
        listadoInst: listado de instalaciones del cso base
        dicc_CB_fact: diccionario de consumos del caso base segun facturas xa el mismo servicio que el listado de instalaciones
        servicio: para que aparezca en mensaje de error
    Se comprueba que no hay facturas extra de combustibles y servicios que no se han definido en caso base 
    Devuelve arrayErrores
    '''
    arrayErrores = []
    combustible = u'Electricidad'
    if dicc_CB_fact[combustible] > 0 and len(listadoInst) == 0:
        combustibleTraducidoMensaje = getTraduccion(listado = listadoCombustibles, elemento = combustible)
        error = _(u'    - factura de %s para %s\n' % (combustibleTraducidoMensaje, servicio))
        arrayErrores.append(error)
    return arrayErrores


def calculoDdaNetaCBFact(instServicio = None, dicc_CB_fact = { }):
    '''
    M\xe9todo: calculoDdaNetaCBFact
    Argumentos:
            listadoInst: obj del listado de instalaciones para el srvicio
            dicc_CB_fact: diccionario de consumos del caso base segun facturas xa el mismo servicio que el listado de instalaciones
    Calcula la demanda neta para el caso real, seg\xfan lo indicado en las facturas.
    Coge el consumo para cada factura y con el rendimiento de cada instalaci\xf3n y su cobertura calcula la demanda neta para cada instalaci\xf3n
    y a partir de ah\xed la demanda neta total.
    Cuidado: la cobertura de cada instalaci\xf3n no es la indicada en el caso base pq puede ser que en el caso base se haya indicado xej.
    que la cal se cubre el 50% con gas natural y 50% con electricidad y las facturas digan otra cosa
    Para ello se calcula la cobertura real de cada instalacion
    '''
    ddaNetaTotal = 0
    for combustible in dicc_CB_fact:
        consumoCombustible = dicc_CB_fact[combustible]
        coberturaM2Combustible = 0
        for equipo in instServicio.listado:
            if equipo.combustible == combustible:
                coberturaM2Combustible += equipo.coberturaM2
                continue
        for equipo in instServicio.listado:
            if equipo.combustible == combustible:
                coberturaRealEquipo = equipo.coberturaM2 / coberturaM2Combustible
                ddaNetaEquipo = (consumoCombustible * equipo.rendimiento / 100) * coberturaRealEquipo
                ddaNetaTotal += ddaNetaEquipo
                continue
    
    return ddaNetaTotal


def calculoTasaCMrespectoCBTeorico(valor_CB_teor = 0, valor_CM_teor = 0):
    '''
    M\xe9todo: calculoTasaCMrespectoCBTeorico
    Argumentos:
        valor_CB_teor: valor que se quiere calcular para el caso base te\xf3rico
        valor_CM_teor: valor que se quiere calcular para el caso mejorado te\xf3rico
    Devuelve la tasa que supone el caso mejorado te\xf3rico respecto al caso base te\xf3rico
    '''
    
    try:
        tasa = valor_CM_teor / valor_CB_teor
    except ZeroDivisionError:
        tasa = 0

    return tasa


def calculoCMfacturas(valor_CB_teor = 0, valor_CM_teor = 0, valor_CB_fact = 0):
    '''
    M\xe9todo: calculoCMfacturas
    Argumentos:
            valor_CB_teor: valor que se quiere calcular para el caso base te\xf3rico
            valor_CM_teor: valor que se quiere calcular para el caso mejorado te\xf3rico
            valor_CB_fact: valor que se quiere calcular para el caso base facturas

    Devuelve el valor que se quiere calcular para el caso mejorado facturas
    '''
    tasa = calculoTasaCMrespectoCBTeorico(valor_CB_teor = valor_CB_teor, valor_CM_teor = valor_CM_teor)
    valor_CM_fact = valor_CB_fact * tasa
    return valor_CM_fact


def getDiccConsumosCMFacturasSgServicio(ddaNeta = 0, instServicio = None):
    '''
    M\xe9todo: getDiccConsumosCMFacturasSgServicio
    Argumentos:
            ddaNeta: demanda neta para el servicio que estoy calculando el dicc
            instServicio: obj del listado de instalaciones para el servicio
    Crea un diccionario para cada combustible, metiendo en kWh/m2 el consumo para dicho servicio y comb
    '''
    dicc_CM_fact = {
        u'Gas Natural': 0,
        u'Gas\xc3\xb3leo-C': 0,
        u'Electricidad': 0,
        u'GLP': 0,
        u'Carb\xc3\xb3n': 0,
        u'Biocarburante': 0,
        u'Biomasa/Renovable': 0,
        u'BiomasaDens': 0 }
    for equipo in instServicio.listado:
        consumoEquipo = (ddaNeta / equipo.rendimiento / 100) * (equipo.coberturaM2 / instServicio.coberturaM2)
        dicc_CM_fact[equipo.combustible] += consumoEquipo
    
    return dicc_CM_fact


def getDiccConsumosContribuciones(listadoContribuciones = None, area = 1):
    '''
    M\xe9todo: getDiccConsumosContribuciones
    Argumentos:
            listadoContribuciones: obj de tipo ListadoContribucionesEnergeticas
            area: area calificable
    Crea un diccionario para cada combustible, metiendo en kWh/m2 el consumo para cada comb
    '''
    lc = listadoContribuciones
    electricidadTotal = lc.enConsum_Electricidad - lc.electricidadGenTotal
    dicc = {
        u'Gas Natural': lc.enConsum_GasNatural / area,
        u'Gas\xc3\xb3leo-C': lc.enConsum_Gasoil / area,
        u'Electricidad': electricidadTotal / area,
        u'GLP': lc.enConsum_GLP / area,
        u'Carb\xc3\xb3n': lc.enConsum_Carbon / area,
        u'Biocarburante': lc.enConsum_Biocarburante / area,
        u'Biomasa/Renovable': lc.enConsum_BiomasaNoDens / area,
        u'BiomasaDens': lc.enConsum_BiomasaDens / area }
    return dicc


def calculoPrecioCombustibleConsumidoPorServicio(diccCal = { }, diccRef = { }, diccACS = { }, diccIlum = { }, diccVentiladores = { }, diccBombas = { }, diccTorresRef = { }, diccContribuciones = { }, diccPreciosCombustibles = { }, area = 1):
    """
    M\xe9todo: calculoPrecioCombustibleConsumido
    Argumentos:
        diccCal, diccRef...: diccionario con el consumo en kWh/m2 para cada combustible
        diccIlum, diccVentiladores, diccBombas y diccTorresRef: solo tienen como key u'Electricidad'
    Devuelve: el precio del consumo total de combustible
    """
    precio = 0
    for comb in diccPreciosCombustibles:
        consumo = diccCal[comb] + diccRef[comb] + diccACS[comb] + diccContribuciones[comb]
        if comb == u'Electricidad':
            consumo += diccIlum[comb] + diccVentiladores[comb] + diccBombas[comb] + diccTorresRef[comb]
        if consumo != 0:
            precio += consumo * float(diccPreciosCombustibles[comb]) * area
            continue
    return precio


def calculoPrecioCombustibleConsumido(diccConsumoCombustible = { }, diccPreciosCombustibles = { }, area = 1):
    """
    M\xe9todo: calculoPrecioCombustibleConsumido
    Argumentos:
        diccConsumoCombustible: diccionario con el consumo en kWh/m2 para cada combustible
        diccIlum, diccVentiladores, diccBombas y diccTorresRef: solo tienen como key u'Electricidad'
    Devuelve: el precio del consumo total de combustible
    """
    precio = 0
    for comb in diccPreciosCombustibles:
        consumo = diccConsumoCombustible[comb]
        if consumo != 0:
            precio += consumo * float(diccPreciosCombustibles[comb]) * area
            continue
    return precio

