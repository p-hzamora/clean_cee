# Embedded file name: Instalaciones\escalonamientoEquipos.pyc

def escalonamiento(listaFraccionPotencias, listaFraccionMinimaEquipo, fcpSistema):
    frac2 = []
    for fcpS in fcpSistema:
        frac1 = []
        equipo = 0
        equipoAnterior = 0
        posicion = 0
        fraccionPotenciaAcumulada = 0
        demanda_cubierta = False
        for equipo, frac_min in zip(listaFraccionPotencias, listaFraccionMinimaEquipo):
            if fraccionPotenciaAcumulada + equipo < fcpS:
                frac1.append(1.0)
                fraccionPotenciaAcumulada += equipo
                posicion += 1
            elif demanda_cubierta == False:
                demanda_cubierta = True
                fraccion = (fcpS - fraccionPotenciaAcumulada) / equipo
                if fraccion < frac_min and posicion != 0:
                    frac1[-1] = frac1[-1] + (fraccion - frac_min) * equipo / equipoAnterior
                    frac1.append(frac_min)
                else:
                    frac1.append(fraccion)
                fraccionPotenciaAcumulada += equipo
                posicion += 1
            else:
                frac1.append(0.0)
                posicion += 1
            equipoAnterior = equipo

        frac2.append(frac1)

    return frac2


def porcentajeEnergiaEquipos(listaFraccionPotencias, fcpSistema, porcentajeEnergiaSistema):
    fraccionPotenciaMinimaEquipo = [ 0.3 for x in listaFraccionPotencias ]
    equipos = escalonamiento(listaFraccionPotencias, fraccionPotenciaMinimaEquipo, fcpSistema)
    porcEnerEquip2 = []
    for fcp, porcentajeEnergia, equip in zip(fcpSistema, porcentajeEnergiaSistema, equipos):
        porcEnerEquip1 = [ (equip[i] * listaFraccionPotencias[i] / porcentajeEnergia if porcentajeEnergia != 0.0 else 0.0) for i in range(len(listaFraccionPotencias)) ]
        porcEnerEquip2.append(porcEnerEquip1)

    n_equipos = len(listaFraccionPotencias)
    energia_equipo2 = []
    for i in range(n_equipos):
        energia_equipo = 0
        for el in porcEnerEquip2:
            energia_equipo += el[i]

        energia_equipo2.append(energia_equipo)

    aux1 = [ porcentajeEnergiaSistema[i] / fcpSistema[i] for i in range(len(fcpSistema)) ]
    total = sum(aux1)
    porcentaje_tiempo = [ x / total for x in aux1 ]
    betaComb = []
    for i in range(n_equipos):
        porcentajeTiempoAcumulado = 0.0
        eqxpT_Acumulado = 0.0
        for eq, pT in zip(equipos, porcentaje_tiempo):
            if eq[i] > 0.0:
                porcentajeTiempoAcumulado += pT
                eqxpT_Acumulado = eqxpT_Acumulado + eq[i] * pT

        if porcentajeTiempoAcumulado > 0.0:
            betaComb.append(eqxpT_Acumulado / porcentajeTiempoAcumulado)
        else:
            betaComb.append(0.0)

    return (energia_equipo2, betaComb)