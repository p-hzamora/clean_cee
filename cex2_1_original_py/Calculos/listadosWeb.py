# Embedded file name: Calculos\listadosWeb.pyc
import idioma
idioma.ini()
aux = _(u'Maquina frigor\xedfica')
aux = _(u'')

def getTraduccion(listado, elemento):
    """
    M\xe9todo: getTraduccion
    Argumentos:
        listado: array con elementos del choice. Ej: listadoCombustibles
        elemento: elemento que se quiere traducir. Ej. u'BiomasaDens'
    Devuelve: elementoTraducido: Ej. u'Biomasa densificada (pelets)'
    """
    dicc = dict(listado)
    traduccion = dicc[elemento]
    return traduccion


def getElementoEnListado(listado, elemento):
    """
    M\xe9todo: getElementoEnListado
    Argumentos:
        listado: array con elementos del choice. Ej: listadoCombustibles
        elemento: elemento que se quiere traducir. Ej. u'BiomasaDens'
    Devuelve: Devuelve True si el elemento est\xe1 en el la columna izqda del listado. False en caso contrario
    """
    dicc = dict(listado)
    if elemento in dicc:
        return True
    else:
        return False


def getPosicionKeyEnListado(listado, elemento):
    """
    M\xe9todo: getPosicionKeyEnListado
    Argumentos
        listado: array con elementos del choice. Ej: listadoCombustibles
        elemento: elemento del que quiero conocer la posicion. Siempre le llega la key, es decir la posicion cero
    Devuelve la posicion
    """
    aux = [ i[0] for i in listado ]
    posicion = aux.index(elemento)
    return posicion


listadoCerramientos = [(u'Fachada', _(u'Fachada')),
 (u'Cubierta', _(u'Cubierta')),
 (u'Suelo', _(u'Suelo')),
 (u'Partici\xf3n Interior', _(u'Partici\xf3n Interior'))]
listadoPosicionCerramientos = [(u'Norte', _(u'Norte')),
 (u'Sur', _(u'Sur')),
 (u'Este', _(u'Este')),
 (u'Oeste', _(u'Oeste')),
 (u'SO', _(u'SO')),
 (u'SE', _(u'SE')),
 (u'NO', _(u'NO')),
 (u'NE', _(u'NE')),
 (u'Techo', _(u'Techo')),
 (u'Suelo', _(u'Suelo')),
 (u'C\xe1mara Sanitaria', _(u'C\xe1mara Sanitaria')),
 (u'Garaje/espacio enterrado', _(u'Garaje/espacio enterrado')),
 (u'Local en superficie', _(u'Local en superficie')),
 (u'Espacio bajo cubierta inclinada', _(u'Espacio bajo cubierta inclinada')),
 (u'Otro', _(u'Otro')),
 (u'', _(u''))]
listadoCombustiblesEquiposElectricos = [(u'Electricidad', _(u'Electricidad'))]
listadoCombustibles = [(u'Gas Natural', _(u'Gas Natural')),
 (u'Gas\xf3leo-C', _(u'Gas\xf3leo-C')),
 (u'Electricidad', _(u'Electricidad')),
 (u'GLP', _(u'GLP')),
 (u'Carb\xf3n', _(u'Carb\xf3n')),
 (u'Biocarburante', _(u'Biocarburante')),
 (u'Biomasa/Renovable', _(u'Biomasa no densificada')),
 (u'BiomasaDens', _(u'Biomasa densificada (pelets)'))]
listadoTipoSistemaVistaClasicaInstalaciones = [(u'ACS', _(u'ACS')),
 (u'Calefacci\xf3n', _(u'Calefacci\xf3n')),
 (u'Refrigeraci\xf3n', _(u'Refrigeraci\xf3n')),
 (u'Calefacci\xf3n y refrigeraci\xf3n', _(u'Calefacci\xf3n y refrigeraci\xf3n')),
 (u'ACS y calefacci\xf3n', _(u'ACS y calefacci\xf3n')),
 (u'ACS, calefacci\xf3n y refrigeraci\xf3n', _(u'ACS, calefacci\xf3n y refrigeraci\xf3n'))]
listadoInstalaciones = [(u'Caldera Est\xe1ndar', _(u'Caldera Est\xe1ndar')),
 (u'Caldera Condensaci\xf3n', _(u'Caldera Condensaci\xf3n')),
 (u'Caldera Baja Temperatura', _(u'Caldera Baja Temperatura')),
 (u'Bomba de Calor', _(u'Bomba de Calor')),
 (u'Bomba de Calor - Caudal Ref. Variable', _(u'Bomba de Calor - Caudal Ref. Variable')),
 (u'Efecto Joule', _(u'Efecto Joule')),
 (u'Equipo de Rendimiento Constante', _(u'Equipo de Rendimiento Constante'))]
listadoInstalacionesClimatizacion = [(u'Bomba de Calor', _(u'Bomba de Calor')), (u'Bomba de Calor - Caudal Ref. Variable', _(u'Bomba de Calor - Caudal Ref. Variable')), (u'Equipo de Rendimiento Constante', _(u'Equipo de Rendimiento Constante'))]
listadoInstalacionesElectrico = [(u'Maquina frigor\xedfica', _(u'M\xe1quina frigor\xedfica')), (u'M\xe1quina frigor\xedfica - Caudal Ref. Variable', _(u'M\xe1quina frigor\xedfica - Caudal Ref. Variable')), (u'Equipo de Rendimiento Constante', _(u'Equipo de Rendimiento Constante'))]
listadoOpcionesInstalacionesVistaClasica = [(u'Conocido (Ensayado/justificado)', _(u'Conocido')), (u'Estimado seg\xfan Instalaci\xf3n', _(u'Estimado')), (u'Estimado seg\xfan curva de rendimiento', _(u'Estimado sg. curva'))]
listadoOpcionesInstalaciones = [(u'Conocido (Ensayado/justificado)', _(u'Conocido (Ensayado/justificado)')), (u'Estimado seg\xfan Instalaci\xf3n', _(u'Estimado seg\xfan Instalaci\xf3n'))]
listadoOpcionesInstalacionesTerciario = [(u'Conocido (Ensayado/justificado)', _(u'Conocido (Ensayado/justificado)')), (u'Estimado seg\xfan Instalaci\xf3n', _(u'Estimado seg\xfan Instalaci\xf3n')), (u'Estimado seg\xfan curva de rendimiento', _(u'Estimado seg\xfan curva de rendimiento'))]
listadoOpcionesInstalacionesMixtos = listadoOpcionesInstalaciones
listadoOpcionesAislamientoCaldera = [(u'Bien aislada y mantenida', _(u'Bien aislada y mantenida')),
 (u'Antigua con aislamiento medio', _(u'Antigua con aislamiento medio')),
 (u'Antigua con mal aislamiento', _(u'Antigua con mal aislamiento')),
 (u'Sin aislamiento', _(u'Sin aislamiento'))]
listadoOpcionesAntiguedad = [(u'Menos de 5 a\xf1os', _(u'Posterior a 2013')), (u'Entre 5 y 10 a\xf1os', _(u'Entre 1994 y 2013')), (u'M\xe1s de 10 a\xf1os', _(u'Anterior a 1994'))]
listadoOpcionesAcumulacion = [(u'Conocido', _(u'Conocido')), (u'Estimado', _(u'Estimado')), (u'Por defecto', _(u'Por defecto'))]
listadoOpcionesAislamientoAcumulacion = [(u'Poliuretano R\xedgido', _(u'Poliuretano R\xedgido')),
 (u'Espuma de Poliuretano', _(u'Espuma de Poliuretano')),
 (u'Poliuretano Proyectado', _(u'Poliuretano Proyectado')),
 (u'Resina de Melanina', _(u'Resina de Melanina')),
 (u'Espuma de Polietileno', _(u'Espuma de Polietileno')),
 (u'Lana de Vidrio', _(u'Lana de Vidrio')),
 (u'Poliestireno', _(u'Poliestireno')),
 (u'Lana Mineral', _(u'Lana Mineral')),
 (u'Espuma Elastom\xe9rica', _(u'Espuma Elastom\xe9rica')),
 (u'Silicato de Calcio', _(u'Silicato de Calcio'))]
listadoOpcionesBombas = [(u'Bomba de caudal constante', _(u'Bomba de caudal constante')), (u'Bomba de varias velocidades', _(u'Bomba de varias velocidades'))]
listadoOpcionesVentiladores = [(u'Ventilador de caudal constante', _(u'Ventilador de caudal constante')), (u'Ventilador de varias velocidades', _(u'Ventilador de varias velocidades'))]
listadoOpcionesTorreDeRefrigeracion = [(u'Torre de refrigeraci\xf3n: 1 velocidad', _(u'Torre de refrigeraci\xf3n: 1 velocidad')), (u'Torre de refrigeraci\xf3n: velocidad variable', _(u'Torre de refrigeraci\xf3n: velocidad variable'))]
listadoOpcionesConsumoBombasOVentiladores = [(u'Conocido (Ensayado/justificado)', _(u'Conocido (Ensayado/justificado)')), (u'Estimado', _(u'Estimado'))]
listadoOpcionesConsumoBombasOVentiladoresCaudalVariable = [(u'Conocido (Ensayado/justificado)', _(u'Conocido (Ensayado/justificado)')), (u'Estimado por escalones', _(u'Estimado por escalones')), (u'Estimado por curva', _(u'Estimado por curva'))]
listadoOpcionesServicioBombas = [(u'ACS', _(u'ACS')), (u'Calefacci\xf3n', _(u'Calefacci\xf3n')), (u'Refrigeraci\xf3n', _(u'Refrigeraci\xf3n'))]
listadoOpcionesServicioVentiladores = [(u'Calefacci\xf3n', _(u'Calefacci\xf3n')), (u'Refrigeraci\xf3n', _(u'Refrigeraci\xf3n'))]
tablaZona1 = [(u'Administrativo en general', _(u'Administrativo en general')),
 (u'Salas de diagn\xf3stico', _(u'Salas de diagn\xf3stico')),
 (u'Pabellones de exposici\xf3n o ferias', _(u'Pabellones de exposici\xf3n o ferias')),
 (u'Aulas y laboratorios', _(u'Aulas y laboratorios')),
 (u'Habitaciones de hospital', _(u'Habitaciones de hospital')),
 (u'Zonas comunes', _(u'Zonas comunes')),
 (u'Almacenes,  archivos,  salas t\xe9cnicas y cocinas', _(u'Almacenes,  archivos,  salas t\xe9cnicas y cocinas')),
 (u'Espacios deportivos', _(u'Espacios deportivos')),
 (u'Otros', _(u'Otros'))]
tablaZona2 = [(u'Administrativo en general', _(u'Administrativo en general')),
 (u'Estaciones de transporte', _(u'Estaciones de transporte')),
 (u'Supermercados,  hipermercados y grandes almacenes', _(u'Supermercados,  hipermercados y grandes almacenes')),
 (u'Bibliotecas,  museos y galer\xedas de arte', _(u'Bibliotecas,  museos y galer\xedas de arte')),
 (u'Zonas comunes en edificios residenciales', _(u'Zonas comunes en edificios residenciales')),
 (u'Centros comerciales (excluidas tiendas)', _(u'Centros comerciales (excluidas tiendas)')),
 (u'Hosteler\xeda y restauraci\xf3n', _(u'Hosteler\xeda y restauraci\xf3n')),
 (u'Religioso en general', _(u'Religioso en general')),
 (u'Auditorios,  salas de actos,  usos m\xfaltiples,  convenciones,  espect\xe1culos...', _(u'Auditorios,  salas de actos,  usos m\xfaltiples,  convenciones,  espect\xe1culos...')),
 (u'Tiendas y peque\xf1o comercio', _(u'Tiendas y peque\xf1o comercio')),
 (u'Zonas comunes', _(u'Zonas comunes')),
 (u'Habitaciones de hoteles,  hostales...', _(u'Habitaciones de hoteles,  hostales...')),
 (u'Otros', _(u'Otros'))]
listaTipoEquipo = [(u'Incandescente', _(u'Incandescente')),
 (u'Incandescentes hal\xf3genas', _(u'Incandescentes hal\xf3genas')),
 (u'Fluorescencia lineal de 26 mm', _(u'Fluorescencia lineal de 26 mm')),
 (u'Fluorescencia lineal de 16 mm', _(u'Fluorescencia lineal de 16 mm')),
 (u'Fluorescencia compacta', _(u'Fluorescencia compacta')),
 (u'Sodio Blanco', _(u'Sodio Blanco')),
 (u'Vapor de Mercurio', _(u'Vapor de Mercurio')),
 (u'Halogenuros met\xe1licos', _(u'Halogenuros met\xe1licos')),
 (u'Inducci\xf3n', _(u'Inducci\xf3n')),
 (u'LED', _(u'LED Spot (puntual, bombilla)')),
 (u'LED Tube (lineal)', _(u'LED Tube (lineal)'))]
listadoOpcionesIluminacion = [(u'Conocido(ensayado/justificado)', _(u'Conocido(ensayado/justificado)')), (u'Estimado', _(u'Estimado'))]
listadoOpcionesBdC = [(u'Aire-Aire', _(u'Aire-Aire')),
 (u'Aire-Agua', _(u'Aire-Agua')),
 (u'Agua-Aire', _(u'Agua-Aire')),
 (u'Agua-Agua', _(u'Agua-Agua'))]
listadoOpcionesOrientacion = [(u'Norte', _(u'Norte')),
 (u'Sur', _(u'Sur')),
 (u'Este', _(u'Este')),
 (u'Oeste', _(u'Oeste')),
 (u'SO', _(u'SO')),
 (u'SE', _(u'SE')),
 (u'NO', _(u'NO')),
 (u'NE', _(u'NE'))]
listadoOpcionesOrientacionSombras = [(u'Sur', _(u'Sur')),
 (u'Este', _(u'Este')),
 (u'Oeste', _(u'Oeste')),
 (u'SO', _(u'SO')),
 (u'SE', _(u'SE')),
 (u'NO', _(u'NO')),
 (u'NE', _(u'NE'))]
listadoOpcionesU = [(u'Conocidas', _(u'Conocidas')), (u'Estimadas', _(u'Estimadas')), (u'Por defecto', _(u'Por defecto'))]
listadoOpcionesUFachadaTerreno = [(u'Estimadas', _(u'Estimadas')), (u'Por defecto', _(u'Por defecto'))]
listadoOpcionesUSueloTerreno = [(u'Estimadas', _(u'Estimadas')), (u'Por defecto', _(u'Por defecto'))]
listadoOpcionesComposicionCubiertaConAire = [(u'Cubierta plana', _(u'Cubierta plana')), (u'Cubierta inclinada', _(u'Cubierta inclinada'))]
listadoOpcionesComposicionCubiertaConAireEstimada = [(u'Cubierta plana', _(u'Cubierta plana')),
 (u'Cubierta plana ventilada', _(u'Cubierta plana ventilada')),
 (u'Cubierta ajardinada', _(u'Cubierta ajardinada')),
 (u'Cubierta inclinada', _(u'Cubierta inclinada')),
 (u'Cubierta inclinada ventilada', _(u'Cubierta inclinada ventilada'))]
listadoOpcionesComposicionFachadaConAire = [(u'1/2 pie de f\xe1brica de ladrillo', _(u'1/2 pie de f\xe1brica de ladrillo')),
 (u'1 pie de f\xe1brica de ladrillo', _(u'1 pie de f\xe1brica de ladrillo')),
 (u'F\xe1brica de bloques de hormig\xf3n', _(u'F\xe1brica de bloques de hormig\xf3n')),
 (u'F\xe1brica de bloques de pic\xf3n', _(u'F\xe1brica de bloques de pic\xf3n')),
 (u'Muro de piedra', _(u'Muro de piedra')),
 (u'Muro de adobe/tapial', _(u'Muro de adobe/tapial'))]
listadoOpcionesComposicionSueloConAire = [(u'Unidireccional', _(u'Unidireccional')),
 (u'Reticular', _(u'Reticular')),
 (u'Losa', _(u'Losa')),
 (u'De Madera', _(u'De Madera'))]
listadoOpcionesTipoForjado = [(u'Unidireccional', _(u'Unidireccional')),
 (u'Reticular', _(u'Reticular')),
 (u'Casetones recuperables', _(u'Casetones recuperables')),
 (u'Losa', _(u'Losa'))]
listadoOpcionesTipoForjadoInclinadaVentilada = [(u'Unidireccional', _(u'Unidireccional')), (u'Losa', _(u'Losa'))]
listadoOpcionesTipoForjadoInclinadaOtra = [(u'Unidireccional', _(u'Unidireccional')), (u'Losa', _(u'Losa')), (u'Tablero soporte', _(u'Tablero soporte'))]
listadoOpcionesCamaraAire = [(u'Ligeramente ventilada', _(u'Ligeramente ventilada')), (u'Ventilada', _(u'Ventilada'))]
listadoOpcionesAislamiento = [(u'EPS', _(u'EPS')),
 (u'XPS', _(u'XPS')),
 (u'MW', _(u'MW')),
 (u'PUR', _(u'PUR')),
 (u'Otro', _(u'Otro')),
 (u'Desconocido', _(u'Desconocido'))]
listadoOpcionesAislamiento2 = [(u'EPS', _(u'EPS')),
 (u'XPS', _(u'XPS')),
 (u'MW', _(u'MW')),
 (u'PUR', _(u'PUR')),
 (u'Otro', _(u'Otro'))]
listadoOpcionesFachadas = [(u'Doble hoja con c\xe1mara', _(u'Doble hoja con c\xe1mara')), (u'Una hoja', _(u'Una hoja')), (u'Fachada ventilada', _(u'Fachada ventilada'))]
listadoOpcionesCamaraAireFachada = [(u'No ventilada', _(u'No ventilada')),
 (u'Ligeramente ventilada', _(u'Ligeramente ventilada')),
 (u'Ventilada', _(u'Ventilada')),
 (u'Rellena de Aislamiento', _(u'Rellena de Aislamiento'))]
listadoOpcionesPosicionAislamiento = [(u'Por el exterior', _(u'Por el exterior')), (u'Por el interior', _(u'Por el interior'))]
listadoOpcionesPosicionAislamientoParticion = [(u'La partici\xf3n', _(u'La partici\xf3n')), (u'El cerramiento', _(u'El cerramiento')), (u'Ambos', _(u'Ambos'))]
listadoOpcionesInercia = [(u'Pesado >= 200 kg/m2', _(u'Pesado >= 200 kg/m2')), (u'Ligero < 200 kg/m2', _(u'Ligero < 200 kg/m2'))]
listadoOpcionesEstanqueidad = [(u'Poco estanco', _(u'Poco estanco')), (u'Estanco', _(u'Estanco')), (u'Valor conocido', _(u'Valor conocido'))]
listadoOpcionesEstanqueidadCTE = [(u'Estanco', _(u'Estanco')), (u'Valor conocido', _(u'Valor conocido'))]
listadoOpcionesPropiedadesTermicasHuecos = [(u'Conocidas', _(u'Conocidas')), (u'Estimadas', _(u'Estimadas'))]
listadoOpcionesVidrios = [(u'Simple', _(u'Simple')), (u'Doble', _(u'Doble')), (u'Doble bajo emisivo', _(u'Doble bajo emisivo'))]
listadoOpcionesMarcos = [(u'Met\xe1lico sin RPT', _(u'Met\xe1lico sin RPT')),
 (u'Met\xe1lico con RPT', _(u'Met\xe1lico con RPT')),
 (u'PVC', _(u'PVC')),
 (u'Madera', _(u'Madera'))]
listadoOpcionesParticionHorizontalInferior = [(u'C\xe1mara Sanitaria', _(u'C\xe1mara Sanitaria')), (u'Garaje/espacio enterrado', _(u'Garaje/espacio enterrado')), (u'Local en superficie', _(u'Local en superficie'))]
listadoOpcionesParticionHorizontalSuperior = [(u'Espacio bajo cubierta inclinada', _(u'Espacio bajo cubierta inclinada')), (u'Otro', _(u'Otro'))]
listadoOpcionesVentilacionEspacioNH = [(u'Ligeramente Ventilado', _(u'Ligeramente Ventilado')), (u'Ventilado', _(u'Ventilado'))]
listadoOpcionesUParticion = [(u'Conocida', _(u'Conocida')), (u'Por defecto', _(u'Por defecto'))]
listadoOpcionesPuentesTermicos = [(u'Pilar integrado en fachada', _(u'Pilar integrado en fachada')),
 (u'Pilar en Esquina', _(u'Pilar en Esquina')),
 (u'Contorno de hueco', _(u'Contorno de hueco')),
 (u'Caja de Persiana', _(u'Caja de Persiana')),
 (u'Encuentro de fachada con forjado', _(u'Encuentro de fachada con forjado')),
 (u'Encuentro de fachada con voladizo', _(u'Encuentro de fachada con voladizo')),
 (u'Encuentro de fachada con cubierta', _(u'Encuentro de fachada con cubierta')),
 (u'Encuentro de fachada con suelo en contacto con el aire', _(u'Encuentro de fachada con suelo en contacto con el aire')),
 (u'Encuentro de fachada con solera', _(u'Encuentro de fachada con solera')),
 (u'Jamba', _(u'Jamba')),
 (u'Dintel', _(u'Dintel')),
 (u'Alfeizar', _(u'Alfeizar')),
 (u'Esquina hacia el exterior', _(u'Esquina hacia el exterior')),
 (u'Esquina hacia el interior', _(u'Esquina hacia el interior'))]
listadoOpcionesEntrevigado = [(u'Cer\xe1micas', _(u'Cer\xe1micas')), (u'De Hormig\xf3n', _(u'De Hormig\xf3n'))]
listadoOpcionesEntrevigadoReticular = [(u'Cer\xe1micas', _(u'Cer\xe1micas')), (u'De Hormig\xf3n', _(u'De Hormig\xf3n')), (u'Recuperables', _(u'Recuperables'))]
listadoOpcionesAislamientoSueloTerreno = [(u'Continuo', _(u'Continuo')), (u'Perimetral', _(u'Perimetral'))]
listadoOpcionesConocimientoAislamientoSueloTerreno = [(u'Conocida', _(u'Conocida')), (u'No conocida', _(u'No conocida'))]
listadoOpcionesElementoMejorado = [(u'Aislamiento t\xe9rmico', _(u'Aislamiento t\xe9rmico')),
 (u'Huecos', _(u'Huecos')),
 (u'Puentes t\xe9rmicos', _(u'Puentes t\xe9rmicos')),
 (u'Instalaciones', _(u'Instalaciones'))]
listadoOpcionesMedidaMejora = [(u'Medida por defecto', _(u'Medida por defecto')), (u'Definida por el usuario', _(u'Definida por el usuario'))]
listaClasesVentanas = [(u'Clase 0 (no ensayada)', _(u'Clase 0 (no ensayada)')),
 (u'Clase 1', _(u'Clase 1')),
 (u'Clase 2', _(u'Clase 2')),
 (u'Clase 3', _(u'Clase 3')),
 (u'Clase 4', _(u'Clase 4'))]
listaOpcionesDobleVentana = [(u'Ninguna', _(u'Ninguna')), (u'Vidrio Simple', _(u'Vidrio Simple')), (u'Vidrio Doble', _(u'Vidrio Doble'))]
listadoOpcionesMMInstalaciones = [(u'Equipo de ACS', _(u'Equipo de ACS')),
 (u'Equipo de s\xf3lo calefacci\xf3n', _(u'Equipo de s\xf3lo calefacci\xf3n')),
 (u'Equipo de s\xf3lo refrigeraci\xf3n', _(u'Equipo de s\xf3lo refrigeraci\xf3n')),
 (u'Equipo de calefacci\xf3n y refrigeraci\xf3n', _(u'Equipo de calefacci\xf3n y refrigeraci\xf3n')),
 (u'Equipo mixto de calefacci\xf3n y ACS', _(u'Equipo mixto de calefacci\xf3n y ACS')),
 (u'Equipo mixto de calefacci\xf3n,  refrigeraci\xf3n y ACS', _(u'Equipo mixto de calefacci\xf3n,  refrigeraci\xf3n y ACS')),
 (u'Contribuciones energ\xe9ticas', _(u'Contribuciones energ\xe9ticas'))]
listadoOpcionesMMInstalacionePT = [(u'Equipo de ACS', _(u'Equipo de ACS')),
 (u'Equipo de s\xf3lo calefacci\xf3n', _(u'Equipo de s\xf3lo calefacci\xf3n')),
 (u'Equipo de s\xf3lo refrigeraci\xf3n', _(u'Equipo de s\xf3lo refrigeraci\xf3n')),
 (u'Equipo de calefacci\xf3n y refrigeraci\xf3n', _(u'Equipo de calefacci\xf3n y refrigeraci\xf3n')),
 (u'Equipo mixto de calefacci\xf3n y ACS', _(u'Equipo mixto de calefacci\xf3n y ACS')),
 (u'Equipo mixto de calefacci\xf3n,  refrigeraci\xf3n y ACS', _(u'Equipo mixto de calefacci\xf3n,  refrigeraci\xf3n y ACS')),
 (u'Contribuciones energ\xe9ticas', _(u'Contribuciones energ\xe9ticas')),
 (u'Equipo de iluminaci\xf3n', _(u'Equipo de iluminaci\xf3n')),
 (u'Equipo de aire primario', _(u'Equipo de aire primario'))]
listadoOpcionesMMInstalacioneGT = [(u'Equipo de ACS', _(u'Equipo de ACS')),
 (u'Equipo de s\xf3lo calefacci\xf3n', _(u'Equipo de s\xf3lo calefacci\xf3n')),
 (u'Equipo de s\xf3lo refrigeraci\xf3n', _(u'Equipo de s\xf3lo refrigeraci\xf3n')),
 (u'Equipo de calefacci\xf3n y refrigeraci\xf3n', _(u'Equipo de calefacci\xf3n y refrigeraci\xf3n')),
 (u'Equipo mixto de calefacci\xf3n y ACS', _(u'Equipo mixto de calefacci\xf3n y ACS')),
 (u'Equipo mixto de calefacci\xf3n,  refrigeraci\xf3n y ACS', _(u'Equipo mixto de calefacci\xf3n,  refrigeraci\xf3n y ACS')),
 (u'Contribuciones energ\xe9ticas', _(u'Contribuciones energ\xe9ticas')),
 (u'Equipo de iluminaci\xf3n', _(u'Equipo de iluminaci\xf3n')),
 (u'Equipo de aire primario', _(u'Equipo de aire primario')),
 (u'Ventiladores', _(u'Ventiladores')),
 (u'Equipo de bombeo', _(u'Equipo de bombeo')),
 (u'Torres de refrigeraci\xf3n', _(u'Torres de refrigeraci\xf3n'))]
normativaVigente = [(u'Anterior', _(u'Anterior')),
 (u'NBE-CT-79', _(u'NBE-CT-79')),
 (u'C.T.E.', _(u'CTE 2006')),
 (u'CTE 2013', _(u'CTE 2013'))]
listadoZonaHE1_peninsular = [(u'A3', _(u'A3')),
 (u'A4', _(u'A4')),
 (u'B3', _(u'B3')),
 (u'B4', _(u'B4')),
 (u'C1', _(u'C1')),
 (u'C2', _(u'C2')),
 (u'C3', _(u'C3')),
 (u'C4', _(u'C4')),
 (u'D1', _(u'D1')),
 (u'D2', _(u'D2')),
 (u'D3', _(u'D3')),
 (u'E1', _(u'E1'))]
listadoZonaHE1_extrapeninsular = [(u'alpha1', u'\u02511'),
 (u'alpha2', u'\u02512'),
 (u'alpha3', u'\u02513'),
 (u'alpha4', u'\u02514'),
 (u'A1', _(u'A1')),
 (u'A2', _(u'A2')),
 (u'A3', _(u'A3')),
 (u'A4', _(u'A4')),
 (u'B1', _(u'B1')),
 (u'B2', _(u'B2')),
 (u'B3', _(u'B3')),
 (u'B4', _(u'B4')),
 (u'C1', _(u'C1')),
 (u'C2', _(u'C2')),
 (u'C3', _(u'C3')),
 (u'C4', _(u'C4')),
 (u'D1', _(u'D1')),
 (u'D2', _(u'D2')),
 (u'D3', _(u'D3')),
 (u'E1', _(u'E1'))]
listadoZonaHE4 = [(u'I', _(u'I')),
 (u'II', _(u'II')),
 (u'III', _(u'III')),
 (u'IV', _(u'IV')),
 (u'V', _(u'V'))]
tipoEdificioResidencial = [(u'Unifamiliar', _(u'Unifamiliar')), (u'Bloque de Viviendas', _(u'Bloque de Viviendas')), (u'Vivienda Individual', _(u'Vivienda Individual'))]
tipoEdificioTerciario = [(u'Edificio completo', _(u'Edificio completo')), (u'Local', _(u'Local'))]
listadoCalendarios = [(u'Intensidad Baja - 8h', _(u'Intensidad Baja - 8h')),
 (u'Intensidad Media - 8h', _(u'Intensidad Media - 8h')),
 (u'Intensidad Alta - 8h', _(u'Intensidad Alta - 8h')),
 (u'Intensidad Baja - 12h', _(u'Intensidad Baja - 12h')),
 (u'Intensidad Media - 12h', _(u'Intensidad Media - 12h')),
 (u'Intensidad Alta - 12h', _(u'Intensidad Alta - 12h')),
 (u'Intensidad Baja - 16h', _(u'Intensidad Baja - 16h')),
 (u'Intensidad Media - 16h', _(u'Intensidad Media - 16h')),
 (u'Intensidad Alta - 16h', _(u'Intensidad Alta - 16h')),
 (u'Intensidad Baja - 24h', _(u'Intensidad Baja - 24h')),
 (u'Intensidad Media - 24h', _(u'Intensidad Media - 24h')),
 (u'Intensidad Alta - 24h', _(u'Intensidad Alta - 24h'))]
diccHorarios = {u'Intensidad Baja - 8h': '8h',
 u'Intensidad Media - 8h': '8h',
 u'Intensidad Alta - 8h': '8h',
 u'Intensidad Baja - 12h': '12h',
 u'Intensidad Media - 12h': '12h',
 u'Intensidad Alta - 12h': '12h',
 u'Intensidad Baja - 16h': '16h',
 u'Intensidad Media - 16h': '16h',
 u'Intensidad Alta - 16h': '16h',
 u'Intensidad Baja - 24h': '24h',
 u'Intensidad Media - 24h': '24h',
 u'Intensidad Alta - 24h': '24h'}
listadoMasas = [(u'Ligera', _(u'Ligera')), (u'Media', _(u'Media')), (u'Pesada', _(u'Pesada'))]