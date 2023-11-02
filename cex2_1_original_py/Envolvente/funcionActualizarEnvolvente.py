# Embedded file name: Envolvente\funcionActualizarEnvolvente.pyc
from Envolvente.tablasValores import tablasValores

def actualizarEnvolvente(listadoCerramientos, normativaVigente, zonaHE1, zonaNBE):
    """
    M\xe9todo: actualizarEnvolvente
    Argumentos:
                listadoCerramientos :array con datos de los cerramientos
                normativaVigente: anterior, NBE, CTE
                zonaHE1,
                zonaNBE
    Devuelve el array de listadoCerramientos actualizado. Actualiza los cerramientos con valores por defecto
    que son los que dependen de la zona climatica y la normativa vigente
    """
    for cerr in listadoCerramientos:
        if 'defecto' in cerr[8]:
            if cerr[1] == 'Cubierta' and cerr[-1] == 'aire':
                valoresCerr = tablasValores('Cubierta', 'aire', [normativaVigente,
                 zonaHE1,
                 zonaNBE,
                 cerr[9][0]], 'Por defecto')
                UCerramiento = valoresCerr.UCerramiento
                densidadCerramiento = valoresCerr.densidadCerramiento
                cerr[3] = UCerramiento
                cerr[4] = densidadCerramiento
            elif cerr[1] == 'Cubierta' and cerr[-1] == 'terreno':
                valoresCerr = tablasValores('Cubierta', 'terreno', [normativaVigente, zonaHE1], 'Por defecto')
                UCerramiento = valoresCerr.UCerramiento
                densidadCerramiento = valoresCerr.densidadCerramiento
                cerr[3] = UCerramiento
                cerr[4] = densidadCerramiento
            elif cerr[1] == 'Fachada' and cerr[-1] == 'aire':
                valoresCerr = tablasValores('Fachada', 'aire', [normativaVigente, zonaHE1, zonaNBE], 'Por defecto')
                UCerramiento = valoresCerr.UCerramiento
                densidadCerramiento = valoresCerr.densidadCerramiento
                cerr[3] = UCerramiento
                cerr[4] = densidadCerramiento
            elif cerr[1] == 'Fachada' and cerr[-1] == 'terreno':
                valoresCerr = tablasValores('Fachada', 'terreno', [normativaVigente, zonaHE1], 'Por defecto')
                UCerramiento = valoresCerr.UCerramiento
                densidadCerramiento = valoresCerr.densidadCerramiento
                cerr[3] = UCerramiento
                cerr[4] = densidadCerramiento
            elif cerr[1] == 'Suelo' and cerr[-1] == 'aire':
                valoresCerr = tablasValores('Suelo', 'aire', [normativaVigente, zonaHE1, zonaNBE], 'Por defecto')
                UCerramiento = valoresCerr.UCerramiento
                densidadCerramiento = valoresCerr.densidadCerramiento
                cerr[3] = UCerramiento
                cerr[4] = densidadCerramiento
            elif cerr[1] == 'Suelo' and cerr[-1] == 'terreno':
                if cerr[9] == True:
                    profundidad = '-0.5'
                else:
                    profundidad = '+0.5'
                valoresCerr = tablasValores('Suelo', 'terreno', [normativaVigente, zonaHE1, profundidad], 'Por defecto')
                UCerramiento = valoresCerr.UCerramiento
                densidadCerramiento = valoresCerr.densidadCerramiento
                cerr[3] = UCerramiento
                cerr[4] = densidadCerramiento
            elif cerr[1] == u'Partici\xf3n Interior' and cerr[-1] == 'vertical':
                valoresCerr = tablasValores('Particion', 'Vertical', [normativaVigente, zonaHE1, zonaNBE], 'Por defecto')
                UCerramiento = valoresCerr.UCerramiento
                densidadCerramiento = valoresCerr.densidadCerramiento
                cerr[3] = UCerramiento
                cerr[4] = densidadCerramiento
            elif cerr[1] == u'Partici\xf3n Interior' and cerr[-1] == 'horizontal superior' and cerr[5] == 'Espacio bajo cubierta inclinada':
                valoresCerr = tablasValores('Particion', 'HorizontalSuperiorBajoCubierta', [normativaVigente, zonaHE1, zonaNBE], 'Por defecto')
                UCerramiento = valoresCerr.UCerramiento
                densidadCerramiento = valoresCerr.densidadCerramiento
                cerr[3] = UCerramiento
                cerr[4] = densidadCerramiento
            elif cerr[1] == u'Partici\xf3n Interior' and cerr[-1] == 'horizontal superior' and cerr[5] == 'Otro':
                valoresCerr = tablasValores('Particion', 'HorizontalSuperiorOtro', [normativaVigente, zonaHE1, zonaNBE], 'Por defecto')
                UCerramiento = valoresCerr.UCerramiento
                densidadCerramiento = valoresCerr.densidadCerramiento
                cerr[3] = UCerramiento
                cerr[4] = densidadCerramiento
            elif cerr[1] == u'Partici\xf3n Interior' and cerr[-1] == 'horizontal inferior' and cerr[5] != u'C\xe1mara Sanitaria':
                valoresCerr = tablasValores('Particion', 'HorizontalInferior', [normativaVigente, zonaHE1, zonaNBE], 'Por defecto')
                UCerramiento = valoresCerr.UCerramiento
                densidadCerramiento = valoresCerr.densidadCerramiento
                cerr[3] = UCerramiento
                cerr[4] = densidadCerramiento
            elif cerr[1] == u'Partici\xf3n Interior' and cerr[-1] == 'horizontal inferior' and cerr[5] == u'C\xe1mara Sanitaria':
                valoresCerr = tablasValores('Particion', 'CamaraSanitaria', [normativaVigente, zonaHE1, zonaNBE], 'Por defecto')
                UCerramiento = valoresCerr.UCerramiento
                densidadCerramiento = valoresCerr.densidadCerramiento
                cerr[3] = UCerramiento
                cerr[4] = densidadCerramiento

    return listadoCerramientos