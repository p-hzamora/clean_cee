# File: f (Python 2.7)

from Calculos.calculoSuperficies import actualizarSuperficiesInstalaciones, actualizarSuperficiesIluminacion
from MedidasDeMejora.objetoGrupoMejoras import grupoMedidasMejora

def actualizarCoberturaDeConjuntosMM(listadoConjuntosMM, zonaCambiada, superficieCambiada):
    '''
    M\xe9todo: actualizarCoberturaDeConjuntosMM
    Argumentos:
    Al actualizar la superficie del edificio objeto o de una zona, es necesario actualizar las superficies cubiertas en las zonas
    Se mantiene el % cubierto y se modifican los m2. 
    Devuelve el nuevo listadoConjuntosMM
    '''
    for conjuntoMM in listadoConjuntosMM:
        if isinstance(conjuntoMM, grupoMedidasMejora) or conjuntoMM.mejoras[1][2] == True:
            listadoInstalacionesSuperficiesInicial = [
                conjuntoMM.mejoras[1][1][0],
                conjuntoMM.mejoras[1][1][1],
                conjuntoMM.mejoras[1][1][2],
                conjuntoMM.mejoras[1][1][3],
                conjuntoMM.mejoras[1][1][4],
                conjuntoMM.mejoras[1][1][5]]
            listadoInstalacionesSuperficies = actualizarSuperficiesInstalaciones(listadoInstalaciones = listadoInstalacionesSuperficiesInicial, superficieCambiada = superficieCambiada, zonaCambiada = zonaCambiada)
            conjuntoMM.mejoras[1][1][0] = listadoInstalacionesSuperficies[0]
            conjuntoMM.mejoras[1][1][1] = listadoInstalacionesSuperficies[1]
            conjuntoMM.mejoras[1][1][2] = listadoInstalacionesSuperficies[2]
            conjuntoMM.mejoras[1][1][3] = listadoInstalacionesSuperficies[3]
            conjuntoMM.mejoras[1][1][4] = listadoInstalacionesSuperficies[4]
            conjuntoMM.mejoras[1][1][5] = listadoInstalacionesSuperficies[5]
        
    
    return listadoConjuntosMM


def actualizarSuperficieIluminacionDeConjuntosMM(listadoConjuntosMM, listadoSubgrupos, superficieHabitable):
    '''
    M\xe9todo: actualizarSuperficieIluminacionDeConjuntosMM
    Atributos: 
        listadoConjuntosMM: 
        listadoSubgrupos:
        superficieHabitable: superficie habitable del edificio: ya que en subgrupos tiene la informacion de todos los subgrupos pero no sabe la superficie del edificio obj
    Devuelve el listado de conjuntos de MM modificaddo
    '''
    for conjuntoMM in listadoConjuntosMM:
        if isinstance(conjuntoMM, grupoMedidasMejora) or conjuntoMM.mejoras[1][2] == True:
            nuevaInstalacionIluminacion = actualizarSuperficiesIluminacion(subgrupos = listadoSubgrupos, superficieHabitable = superficieHabitable, arrayIluminacion = conjuntoMM.mejoras[1][1][7])
            conjuntoMM.mejoras[1][1][7] = nuevaInstalacionIluminacion
        
    
    return listadoConjuntosMM


def actualizarNombreSubgrupoDeConjuntosMM(listadoConjuntosMM, nombreNuevoSubgrupo, nombreAntiguoSubgrupo):
    '''
    M\xe9todo: actualizarNombreSubgrupoDeConjuntosMM
    Argumentos:
        listadoConjuntosMM
        nombreNuevoSubgrupo: nombre nuevo que toma el subgrupo
        nombreAntiguoSubgrupo: nombre antiguo que toma el subgrupo
    Actualiza el las instalaciones de los conjuntos de mm los nombres de los subgrupos modificados
    '''
    for conjuntoMM in listadoConjuntosMM:
        if isinstance(conjuntoMM, grupoMedidasMejora) or conjuntoMM.mejoras[1][2] == True:
            conjuntoMM.mejoras[1][1][0] = actualizaNombreSubgrupoInstalacion(listadoInstalacion = conjuntoMM.mejoras[1][1][0], nombreNuevoSubgrupo = nombreNuevoSubgrupo, nombreAntiguoSubgrupo = nombreAntiguoSubgrupo)
            conjuntoMM.mejoras[1][1][1] = actualizaNombreSubgrupoInstalacion(listadoInstalacion = conjuntoMM.mejoras[1][1][1], nombreNuevoSubgrupo = nombreNuevoSubgrupo, nombreAntiguoSubgrupo = nombreAntiguoSubgrupo)
            conjuntoMM.mejoras[1][1][2] = actualizaNombreSubgrupoInstalacion(listadoInstalacion = conjuntoMM.mejoras[1][1][2], nombreNuevoSubgrupo = nombreNuevoSubgrupo, nombreAntiguoSubgrupo = nombreAntiguoSubgrupo)
            conjuntoMM.mejoras[1][1][3] = actualizaNombreSubgrupoInstalacion(listadoInstalacion = conjuntoMM.mejoras[1][1][3], nombreNuevoSubgrupo = nombreNuevoSubgrupo, nombreAntiguoSubgrupo = nombreAntiguoSubgrupo)
            conjuntoMM.mejoras[1][1][4] = actualizaNombreSubgrupoInstalacion(listadoInstalacion = conjuntoMM.mejoras[1][1][4], nombreNuevoSubgrupo = nombreNuevoSubgrupo, nombreAntiguoSubgrupo = nombreAntiguoSubgrupo)
            conjuntoMM.mejoras[1][1][5] = actualizaNombreSubgrupoInstalacion(listadoInstalacion = conjuntoMM.mejoras[1][1][5], nombreNuevoSubgrupo = nombreNuevoSubgrupo, nombreAntiguoSubgrupo = nombreAntiguoSubgrupo)
            conjuntoMM.mejoras[1][1][6] = actualizaNombreSubgrupoInstalacion(listadoInstalacion = conjuntoMM.mejoras[1][1][6], nombreNuevoSubgrupo = nombreNuevoSubgrupo, nombreAntiguoSubgrupo = nombreAntiguoSubgrupo)
            conjuntoMM.mejoras[1][1][7] = actualizaNombreSubgrupoInstalacion(listadoInstalacion = conjuntoMM.mejoras[1][1][7], nombreNuevoSubgrupo = nombreNuevoSubgrupo, nombreAntiguoSubgrupo = nombreAntiguoSubgrupo)
            conjuntoMM.mejoras[1][1][8] = actualizaNombreSubgrupoInstalacion(listadoInstalacion = conjuntoMM.mejoras[1][1][8], nombreNuevoSubgrupo = nombreNuevoSubgrupo, nombreAntiguoSubgrupo = nombreAntiguoSubgrupo)
            conjuntoMM.mejoras[1][1][9] = actualizaNombreSubgrupoInstalacion(listadoInstalacion = conjuntoMM.mejoras[1][1][9], nombreNuevoSubgrupo = nombreNuevoSubgrupo, nombreAntiguoSubgrupo = nombreAntiguoSubgrupo)
            conjuntoMM.mejoras[1][1][10] = actualizaNombreSubgrupoInstalacion(listadoInstalacion = conjuntoMM.mejoras[1][1][10], nombreNuevoSubgrupo = nombreNuevoSubgrupo, nombreAntiguoSubgrupo = nombreAntiguoSubgrupo)
            conjuntoMM.mejoras[1][1][11] = actualizaNombreSubgrupoInstalacion(listadoInstalacion = conjuntoMM.mejoras[1][1][11], nombreNuevoSubgrupo = nombreNuevoSubgrupo, nombreAntiguoSubgrupo = nombreAntiguoSubgrupo)
        
    
    return listadoConjuntosMM


def actualizaNombreSubgrupoInstalacion(listadoInstalacion, nombreNuevoSubgrupo, nombreAntiguoSubgrupo):
    for inst in listadoInstalacion:
        if inst[-1] == nombreAntiguoSubgrupo:
            inst[-1] = nombreNuevoSubgrupo
            continue
    return listadoInstalacion


def eliminarSubgrupoDeConjuntosMM(listadoConjuntosMM, subgrupoEliminado):
    '''
    M\xe9todo: eliminarSubgrupoDeConjuntosMM
    Argumentos: 
        listadoConjuntosMM 
        subgrupoEliminado: 
    Devuelve el listado de conjuntos de medidas de mejora en las que se ha eliminado las instalaciones que pertenecen a un subgrupo
    que se esta borrando
    
    '''
    for conjuntoMM in listadoConjuntosMM:
        if isinstance(conjuntoMM, grupoMedidasMejora) or conjuntoMM.mejoras[1][2] == True:
            conjuntoMM.mejoras[1][1][0] = eliminarInstalacionDeSubgrupo(listadoInstalacion = conjuntoMM.mejoras[1][1][0], subgrupoEliminado = subgrupoEliminado)
            conjuntoMM.mejoras[1][1][1] = eliminarInstalacionDeSubgrupo(listadoInstalacion = conjuntoMM.mejoras[1][1][1], subgrupoEliminado = subgrupoEliminado)
            conjuntoMM.mejoras[1][1][2] = eliminarInstalacionDeSubgrupo(listadoInstalacion = conjuntoMM.mejoras[1][1][2], subgrupoEliminado = subgrupoEliminado)
            conjuntoMM.mejoras[1][1][3] = eliminarInstalacionDeSubgrupo(listadoInstalacion = conjuntoMM.mejoras[1][1][3], subgrupoEliminado = subgrupoEliminado)
            conjuntoMM.mejoras[1][1][4] = eliminarInstalacionDeSubgrupo(listadoInstalacion = conjuntoMM.mejoras[1][1][4], subgrupoEliminado = subgrupoEliminado)
            conjuntoMM.mejoras[1][1][5] = eliminarInstalacionDeSubgrupo(listadoInstalacion = conjuntoMM.mejoras[1][1][5], subgrupoEliminado = subgrupoEliminado)
            conjuntoMM.mejoras[1][1][6] = eliminarInstalacionDeSubgrupo(listadoInstalacion = conjuntoMM.mejoras[1][1][6], subgrupoEliminado = subgrupoEliminado)
            conjuntoMM.mejoras[1][1][7] = eliminarInstalacionDeSubgrupo(listadoInstalacion = conjuntoMM.mejoras[1][1][7], subgrupoEliminado = subgrupoEliminado)
            conjuntoMM.mejoras[1][1][8] = eliminarInstalacionDeSubgrupo(listadoInstalacion = conjuntoMM.mejoras[1][1][8], subgrupoEliminado = subgrupoEliminado)
            conjuntoMM.mejoras[1][1][9] = eliminarInstalacionDeSubgrupo(listadoInstalacion = conjuntoMM.mejoras[1][1][9], subgrupoEliminado = subgrupoEliminado)
            conjuntoMM.mejoras[1][1][10] = eliminarInstalacionDeSubgrupo(listadoInstalacion = conjuntoMM.mejoras[1][1][10], subgrupoEliminado = subgrupoEliminado)
            conjuntoMM.mejoras[1][1][11] = eliminarInstalacionDeSubgrupo(listadoInstalacion = conjuntoMM.mejoras[1][1][11], subgrupoEliminado = subgrupoEliminado)
        
    
    return listadoConjuntosMM


def eliminarInstalacionDeSubgrupo(listadoInstalacion, subgrupoEliminado):
    nuevaInstalacionACS = []
    for inst in listadoInstalacion:
        if inst[-1] != subgrupoEliminado:
            nuevaInstalacionACS.append(inst)
            continue
    return nuevaInstalacionACS


def existenInstalacionesColgandoDeZonaModificadaOEliminadaEnConjuntosMM(listadoConjuntosMM, subgrupoModifOElim):
    existeInstColgandoDeZonaEliminadaEnConjuntoMM = False
    for conjuntoMM in listadoConjuntosMM:
        if isinstance(conjuntoMM, grupoMedidasMejora) or conjuntoMM.mejoras[1][2] == True:
            for inst in conjuntoMM.mejoras[1][1][0] + conjuntoMM.mejoras[1][1][1] + conjuntoMM.mejoras[1][1][2] + conjuntoMM.mejoras[1][1][3] + conjuntoMM.mejoras[1][1][4] + conjuntoMM.mejoras[1][1][5] + conjuntoMM.mejoras[1][1][6] + conjuntoMM.mejoras[1][1][7] + conjuntoMM.mejoras[1][1][8] + conjuntoMM.mejoras[1][1][9] + conjuntoMM.mejoras[1][1][10]:
                if inst[-1] == subgrupoModifOElim:
                    existeInstColgandoDeZonaEliminadaEnConjuntoMM = True
                    return existeInstColgandoDeZonaEliminadaEnConjuntoMM
            
        
    
    return existeInstColgandoDeZonaEliminadaEnConjuntoMM

