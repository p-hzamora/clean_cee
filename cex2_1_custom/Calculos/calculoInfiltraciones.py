# Embedded file name: Calculos\calculoInfiltraciones.pyc
"""
Modulo: calculoInfiltraciones.py

"""
from openopt import NLSP
import logging
nHuecos = 0.67
nOpacos = 0.67
nAireadores = 0.5
CopacosUnifamiliar = 1.8
PopacosUnifamiliar = 4.0
CopacosBloque = 1.95
PopacosBloque = 4.0
CopacosTerciario = 1.95
PopacosTerciario = 4.0
Caireadores = 50.0
Paireadores = 100.0
CpExpuesto = 0.25
CpNoExpuesto = -0.5
CpCubiertas = -0.6

def presiones(v_viento, CpExpuesto, CpNoExpuesto, CpCubiertas):
    """
    Metodo: presiones
    ARGUMENTOS:
                v_viento:
    En esta funcion adicional se calculan las presiones sobre la fachada expuesta y no expuesta en funcion
    de la velocidad de viento
    Devuelve la presion en:
    - fachada expuesta
    - fachada no expuesta
    - lucernario
    En este momento, no se est\xe1 utilizando      
    """
    pe = 1.0 / 2 * 1.2 * CpExpuesto * v_viento ** 2
    pne = 1.0 / 2 * 1.2 * CpNoExpuesto * v_viento ** 2
    pluc = 1.0 / 2 * 1.2 * CpCubiertas * v_viento ** 2
    return [pe, pne, pluc]


def caudal(C, deltaP, n):
    """
    Metodo: caudal
    ARGUMENTOS:
                C:
                deltaP:
                n:
     La siguiente funcion calcula el caudal de infiltracion que pasa por un elemento de la fachada en funcion del
     deltaP, del C (coeficiente de infiltracion normalizado a 1 Pa) y del n (exponente). 
     Esta funcion hay que llamarla 6 o 7 veces (para cada uno de los elementos de flujo, sobre la fachada expuesta y no
     expuesta y si hay lucernarios sobre los lucernarios)               
     Q en l/s
    """
    if deltaP >= 0:
        q = C * deltaP ** n
    else:
        q = -C * (-deltaP) ** n
    return q


def residuo_caudales(P, Ch, Co, Ca, QHS3, nHuecos, nOpacos, nAireadores):
    """
    Metodo: residuo_caudales
    ARGUMENTOS:
     P[0]: presion interior v = 0
     P[1]: presion interior v = 4
     Ch: caudal normalizado (l/s) a 1 Pa debido a los defectos de estanqueidad por las ventanas
     Co: caudal normalizado (l/s) a 1 Pa debido a los defectos de estanqueidad por la envolvente
     Ca: caudal normalizado (l/s) a 1 Pa debido a la presencia de aireadores
     QHS3: caudal de ventilacion por cumplimiento del HS3 (l/s)
                
     Esta es la funcion que emplea el solver para calcular
     la presion interior de equilibrio          
    """
    if P[1] > 0:
        P[1] = -P[1]
    if P[0] > 0:
        P[0] = -P[0]
    residuo_0 = Ch / 2.0 * (0.0 - P[0]) ** nHuecos + Co / 2.0 * (0.0 - P[0]) ** nOpacos + Ca / 2.0 * (0.0 - P[0]) ** nAireadores + Ch / 2.0 * (0.0 - P[0]) ** nHuecos + Co / 2.0 * (0.0 - P[0]) ** nOpacos + Ca / 2.0 * (0.0 - P[0]) ** nAireadores - QHS3
    if -4.8 - P[1] >= 0:
        residuo_4 = Ch / 2.0 * (2.4 - P[1]) ** nHuecos + Co / 2.0 * (2.4 - P[1]) ** nOpacos + Ca / 2.0 * (2.4 - P[1]) ** nAireadores + Ch / 2.0 * (-4.8 - P[1]) ** nHuecos + Co / 2.0 * (-4.8 - P[1]) ** nOpacos + Ca / 2.0 * (-4.8 - P[1]) ** nAireadores - QHS3
    else:
        residuo_4 = Ch / 2.0 * (2.4 - P[1]) ** nHuecos + Co / 2.0 * (2.4 - P[1]) ** nOpacos + Ca / 2.0 * (2.4 - P[1]) ** nAireadores - Ch / 2.0 * abs(-4.8 - P[1]) ** nHuecos - Co / 2.0 * abs(-4.8 - P[1]) ** nOpacos - Ca / 2.0 * abs(-4.8 - P[1]) ** nAireadores - QHS3
    return [residuo_0, residuo_4]


def calculoTasaVentilacion(volumen = 0.0, area = 0.0, listadoCerramientos = [], listadoHuecos = [], tasaCalculo = 0.0, esEdificioExistente = True, programa = '', tipoEdificio = '', nHuecos = nHuecos, nOpacos = nOpacos, nAireadores = nAireadores, CopacosUnifamiliar = CopacosUnifamiliar, PopacosUnifamiliar = PopacosUnifamiliar, CopacosBloque = CopacosBloque, PopacosBloque = PopacosBloque, CopacosTerciario = CopacosTerciario, PopacosTerciario = PopacosTerciario, Caireadores = Caireadores, Paireadores = Paireadores, CpExpuesto = CpExpuesto, CpNoExpuesto = CpNoExpuesto, CpCubiertas = CpCubiertas):
    """
    Metodo: calculoTasaVentilacion
    
    ARGUMENTOS:
                volumen = volumen acondicionado del edificio m3 (para todo el edifici,
        area =  m2  (para todo el edificio),
        listadoCerramientos = [] array de objetos
        listadoHuecos = [], 
        tasaCalculo en ren/h,
        esEdificioExistente = True si es, False si es edificio nuevo para la ventilacion
        programa = 'Residencial', 'Terciario'
        tipoEdificio = 'Unifamiliar', 'Bloque'...
        
    Calcula la tasa de ventilacion en ren/h en funcion de los datos de huecos y cerramientos del edificio
    """
    Chuecos1Pa_enLPorS = calculoCaudalHuecos(listadoHuecos=listadoHuecos, nHuecos=nHuecos)
    Copacos1Pa_enLPorS = calculoCaudalOpacos(listadoCerramientos=listadoCerramientos, programa=programa, tipoEdificio=tipoEdificio, CopacosUnifamiliar=CopacosUnifamiliar, PopacosUnifamiliar=PopacosUnifamiliar, CopacosBloque=CopacosBloque, PopacosBloque=PopacosBloque, CopacosTerciario=CopacosTerciario, PopacosTerciario=PopacosTerciario, nOpacos=nOpacos)
    superficieHuecos = 0.0
    for h in listadoHuecos:
        superficieHuecos += float(h.superficie)

    Caireadores1Pa_enLPorS = calculoCaudalAireadores(Chuecos1Pa_enLPorS=Chuecos1Pa_enLPorS, superficieHuecos=superficieHuecos, Caireadores=Caireadores, Paireadores=Paireadores, nHuecos=nHuecos)
    tasa = calculoTasaMedia(volumen=volumen, tasaCalculo=tasaCalculo, Ch=Chuecos1Pa_enLPorS, Co=Copacos1Pa_enLPorS, Ca=Caireadores1Pa_enLPorS, nHuecos=nHuecos, nOpacos=nOpacos, nAireadores=nAireadores)
    return tasa


def calculoTasaVentilacionBlowerDoorTest(q50 = 0.0, n = 0.0, volumen = 0.0, area = 0.0, listadoCerramientos = [], listadoHuecos = [], tasaCalculo = 0.0, esEdificioExistente = True, programa = '', tipoEdificio = '', nHuecos = nHuecos, nOpacos = nOpacos, nAireadores = nAireadores, CopacosUnifamiliar = CopacosUnifamiliar, PopacosUnifamiliar = PopacosUnifamiliar, CopacosBloque = CopacosBloque, PopacosBloque = PopacosBloque, CopacosTerciario = CopacosTerciario, PopacosTerciario = PopacosTerciario, Caireadores = Caireadores, Paireadores = Paireadores, CpExpuesto = CpExpuesto, CpNoExpuesto = CpNoExpuesto, CpCubiertas = CpCubiertas):
    """
    Metodo: calculoTasaVentilacionBlowerDoorTest
    
    
    ARGUMENTOS:
                q50: caudal de infiltracion normalizado a 50 Pa (l/s)
                n: exponente de la curva caudal - presion Q = q50 * (deltaP)**n
        volumen = volumen acondicionado del edificio m3 (para todo el edifici,
        area =  m2  (para todo el edificio),
        listadoCerramientos = [] array de objetos
        listadoHuecos = [], 
        tasaCalculo en ren/h,
        esEdificioExistente = True si es, False si es edificio nuevo para la ventilacion
        programa = 'Residencial', 'Terciario'
        tipoEdificio = 'Unifamiliar', 'Bloque'...
                
        Calcula la tasa de ventilacion en ren/h en funcion de la medicion del BlowerDoorTest 
    """
    ChuecosYOpacos1Pa_enLPorS = q50 / 50.0 ** n
    superficieHuecos = 0.0
    for h in listadoHuecos:
        superficieHuecos += float(h.superficie)

    Copacos1Pa_enLPorS = calculoCaudalOpacos(listadoCerramientos=listadoCerramientos, programa=programa, tipoEdificio=tipoEdificio, CopacosUnifamiliar=CopacosUnifamiliar, PopacosUnifamiliar=PopacosUnifamiliar, CopacosBloque=CopacosBloque, PopacosBloque=PopacosBloque, CopacosTerciario=CopacosTerciario, PopacosTerciario=PopacosTerciario, nOpacos=nOpacos)
    Chuecos1Pa_enLPorS = ChuecosYOpacos1Pa_enLPorS - Copacos1Pa_enLPorS
    Caireadores1Pa_enLPorS = calculoCaudalAireadores(Chuecos1Pa_enLPorS=Chuecos1Pa_enLPorS, superficieHuecos=superficieHuecos, Caireadores=Caireadores, Paireadores=Paireadores, nHuecos=nHuecos)
    tasa = calculoTasaMedia(volumen=volumen, tasaCalculo=tasaCalculo, Ch=ChuecosYOpacos1Pa_enLPorS, Co=0.0, Ca=Caireadores1Pa_enLPorS, nHuecos=nHuecos, nOpacos=nOpacos, nAireadores=nAireadores)
    return tasa


def calculoCaudalHuecos(listadoHuecos = [], nHuecos = None):
    """
    Metodo: calculoCaudalHuecos
    Argumentos: 
        listadoHuecos = listado de huecos del edificio. son objetos,
        nHuecos
    Devuelve el caudal a 1 Pa de infiltracion por huecos, en l/s
    """
    sumaSupPorPermeabilidad = 0.0
    superficieHuecos = 0.0
    for h in listadoHuecos:
        superficieHuecos += float(h.superficie)
        sumaSupPorPermeabilidad += float(h.superficie) * float(h.permeabilidadValor)

    if superficieHuecos > 0:
        Chuecos100Pa = sumaSupPorPermeabilidad / superficieHuecos
    else:
        Chuecos100Pa = 0.0
    Chuecos1Pa = Chuecos100Pa / 100 ** nHuecos
    Chuecos1Pa_enLPorSM2 = Chuecos1Pa * 1000.0 / 3600.0
    Chuecos1Pa_enLPorS = Chuecos1Pa_enLPorSM2 * superficieHuecos
    return Chuecos1Pa_enLPorS


def calculoCaudalOpacos(listadoCerramientos = [], programa = 'Residencial', tipoEdificio = 'Unifamiliar', CopacosUnifamiliar = None, PopacosUnifamiliar = None, CopacosBloque = None, PopacosBloque = None, CopacosTerciario = None, PopacosTerciario = None, nOpacos = None):
    """
    M\xe9todo: calculoCaudalOpacos
    Argumentos: 
        listadoCerramientos = listado de cerr del edificio. son objetos
        programa = Residencial, Peque\xf1oTerciario, GranTerciario'
        tipoEdificio = Unifamiliar, BloqueViviendas....
    Devuelve el caudal a 1 Pa de infiltracion por cerr, en l/s
    """
    superficieOpacos = 0.0
    for cerr in listadoCerramientos:
        if cerr.tipo in ('Fachada', 'Cubierta') and cerr.enContactoCon == 'aire':
            superficieOpacos += cerr.superficieNeta

    if programa == 'Residencial':
        if tipoEdificio == 'Unifamiliar':
            Copacos4Pa = CopacosUnifamiliar
            Popacos = PopacosUnifamiliar
        else:
            Copacos4Pa = CopacosBloque
            Popacos = PopacosBloque
    else:
        Copacos4Pa = CopacosTerciario
        Popacos = PopacosTerciario
    Copacos1Pa = Copacos4Pa / Popacos ** nOpacos
    Copacos1Pa_enLPorSM2 = Copacos1Pa * 1000 / 3600
    Copacos1Pa_enLPorS = Copacos1Pa_enLPorSM2 * superficieOpacos
    return Copacos1Pa_enLPorS


def calculoCaudalAireadores(Chuecos1Pa_enLPorS = 0.0, superficieHuecos = 0.0, Caireadores = None, Paireadores = None, nHuecos = None):
    """
    M\xe9todo: calculoCaudalAireadores
    Argumentos: 
        superficieHuecos = suma superficieHuecos
    Devuelve el caudal a 1 Pa de infiltracion por aireadores, en l/s
    """
    Chuecos1Pa_enLPorSM2_Clase1 = Caireadores / Paireadores ** nHuecos / 3.6
    if superficieHuecos > 0:
        Chuecos1Pa_enLPorSM2 = Chuecos1Pa_enLPorS / superficieHuecos
    else:
        Chuecos1Pa_enLPorSM2 = 0
    if Chuecos1Pa_enLPorSM2 < Chuecos1Pa_enLPorSM2_Clase1:
        Caireadores1Pa_enLPorSM2 = Chuecos1Pa_enLPorSM2_Clase1 - Chuecos1Pa_enLPorSM2
        Caireadores1Pa_enLPorS = Caireadores1Pa_enLPorSM2 * superficieHuecos
    else:
        Caireadores1Pa_enLPorS = 0.0
    return Caireadores1Pa_enLPorS


def calculoTasaMedia(volumen = 0.0, tasaCalculo = 0.0, Ch = 0.0, Co = 0.0, Ca = 0.0, nHuecos = 0.0, nOpacos = 0.0, nAireadores = 0.0):
    """
    Metodo: calculoTasaMedia
    Argumentos: 
        volumen edificio.
        tasaCalculo  en renh
        Ch: infiltraciones huecos en l/s,
        Co: infiltraciones opacos en l/s,
        Ca: infiltraciones aireadores admision en l/s.
    Calcula la tasa de ventilacion en ren/h, a partir de los datos ya procesados de Caireadores, opacos, huecos,...
    """
    QHS3 = volumen * tasaCalculo * 1000.0 / 3600.0
    f = [lambda x: residuo_caudales(x, Ch, Co, Ca, QHS3, nHuecos, nOpacos, nAireadores)]
    desired_ftol = 0.001
    x0 = [-0.1, -0.1]
    p = NLSP(f, x0, ftol=desired_ftol, iprint=-1, maxFunEvals=int(10000000.0))
    r = p.solve('scipy_fsolve')
    if r.isFeasible == True:
        Qfe_v0 = caudal(Ch / 2.0, 0.0 - r.xf[0], nHuecos) + caudal(Co / 2.0, 0.0 - r.xf[0], nOpacos) + caudal(Ca / 2, 0 - r.xf[0], nAireadores)
        Qfe_v4 = caudal(Ch / 2.0, 2.4 - r.xf[1], nHuecos) + caudal(Co / 2.0, 2.4 - r.xf[1], nOpacos) + caudal(Ca / 2, 2.4 - r.xf[1], nAireadores)
        Qfne_v0 = caudal(Ch / 2.0, 0.0 - r.xf[0], nHuecos) + caudal(Co / 2.0, 0.0 - r.xf[0], nOpacos) + caudal(Ca / 2, 0 - r.xf[0], nAireadores)
        Qfne_v4 = caudal(Ch / 2.0, -4.8 - r.xf[1], nHuecos) + caudal(Co / 2.0, -4.8 - r.xf[1], nOpacos) + caudal(Ca / 2, -4.8 - r.xf[1], nAireadores)
        Q_v0 = Qfe_v0 + Qfne_v0
        if Qfne_v4 < 0:
            Q_v4 = Qfe_v4
        else:
            Q_v4 = Qfe_v4 + Qfne_v4
        Q = (Q_v0 + Q_v4) / 2.0
        tasa = Q * 3.6 / volumen
    else:
        logging.warning(u'El solver no ha encontrado una tasa adecuada de infiltraci\xf3n.')
        tasa = tasaCalculo
    return tasa