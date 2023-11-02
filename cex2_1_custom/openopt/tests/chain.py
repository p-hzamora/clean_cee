# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\tests\chain.pyc
# Compiled at: 2012-12-08 11:04:59
"""
The test is related to obsolete OpenOpt version and doesn't work for now
It was used to write an article related to numerical optimization.
"""
from .numpy import *
from .openopt import *
TestCollection = xrange(5, 26)
TestCollection = [
 21]
P = 0
xyCoordsAlwaysExist = False
solvers = [
 'ralg', 'ipopt', 'scipy_cobyla']
solvers = ['ralg', 'ipopt']
solvers = ['ralg']
PLOT = 0
Results = {}
contol = 1e-08
xl, yl = (0, 15)
yThreshold = -1.0
LeftPointForceX = 10.0
LeftPointForceY = -3000.0
maxY = array(['inf', 10.0399786566, 5.61033453009, 2.06002552258, -0.96112448303, -4.13674736433, 
 -7.84375429882, -11.8094052553, -14.9106560481, -17.1598341467, -18.7959512268, 
 -20.240402618, -21.6919090157, -22.9270315304, -23.5750132311, -23.5920241002, 
 -23.2285382362, -22.6103728598, -21.5974976575, -19.9739484665, -17.7441144032, 
 -15.2828386661, -12.9735192373, -10.7235600474, -8.05824588682, -4.62542867851]) + yThreshold
for n in TestCollection:
    oovarInit = oovar('leftPointForces', v0=[LeftPointForceX, LeftPointForceY], lb=[0, -inf])
    MaxForces = 100 * sin(arange(n)) + 5000 * ones(n) + array([-1371.63831, -1606.94848, -1746.85759, 
     -1770.99023, -1762.95446, 
     -1832.32862, 
     -2013.27466, -2232.92838, -2379.90432, 
     -2407.86079, 
     -2376.04148, -2392.20174, 
     -2512.27773, -2688.25834, -2814.48159, 
     -2827.91948, 
     -2763.85327, -2718.73406, 
     -2759.69731, -2862.37323, -2936.13565, 
     -2912.60196, 
     -2807.26185, -2699.90883, 
     -2659.82371, -2682.85823, -2697.93719, 
     -2637.22331, 
     -2498.86567, -2345.12448, 
     -2244.0519, -2207.90597, -2183.42816, 
     -2103.68051, 
     -1950.71662, -1770.36769, 
     -1629.11926, -1553.45727, -1506.21766, 
     -1422.12572, 
     -1268.85753, -1076.14103, 
     -907.638583, -802.510393, -739.726398, 
     -658.001243, 
     -512.877756, -317.504802, 
     -130.014677, 0.00999898976])[:n]
    lengths = 5 * ones(n) + cos(arange(n))
    masses = 15 * ones(n) + 4 * cos(arange(n))
    g = 10
    Fm = masses * g
    s = [
     20, 20]
    AdditionalMasses = oovar('AdditionalMasses', v0=s + [(100.0 - sum(s)) / (n - len(s))] * (n - len(s)), lb=zeros(n))
    from .blockMisc import *

    def blockEngineFunc(inp, AdditionalMasses, blockID):
        if blockID == 0:
            lFx, lFy, lx, ly, prevBlockForceThreshold, prev_yLimit = (
             inp[0], inp[1], xl, yl, 0, 0)
        else:
            lFx, lFy, lx, ly, prevBlockForceThreshold, prev_yLimit = (
             inp[0], inp[1], inp[2], inp[3], inp[4], inp[5])
        prevBlockBroken = blockID >= 0 and isnan(prevBlockForceThreshold) or prevBlockForceThreshold > 0 and P == 0 or prev_yLimit > 0 or isnan(prev_yLimit) and P == 0 and not xyCoordsAlwaysExist
        Fwhole = sqrt(lFx ** 2 + lFy ** 2)
        ForceThreshold = (Fwhole - MaxForces[blockID]) / 10000.0
        CurrentAdditionalMass = AdditionalMasses[blockID]
        rFy = lFy + Fm[blockID] + CurrentAdditionalMass * g
        rFx = lFx
        dx, dy = lengths[blockID] * lFx / Fwhole, lengths[blockID] * lFy / Fwhole
        rx = lx + dx
        ry = ly + dy
        yLimit = ly - maxY[blockID]
        if P != 0:
            projection, distance = project2ball(x=[lFx, lFy], radius=MaxForces[blockID], center=0)
            ForceThreshold += P * distance / 10000.0
            projection, distance = project2box(ly, -inf, maxY[blockID])
            if distance > 0:
                yLimit = P / 10000.0 * distance
        if prevBlockBroken or prev_yLimit > 0 and P == 0:
            rx, ry, ForceThreshold, rFx, rFy, yLimit = (
             nan, nan, nan, nan, nan, nan)
        r = array((rFx, rFy, rx, ry, ForceThreshold, yLimit))
        return r


    def derivative_blockEngineFunc(inp, AdditionalMasses, blockID):
        if blockID == 0:
            lFx, lFy, lx, ly, prevBlockForceThreshold, prev_yLimit = (
             inp[0], inp[1], xl, yl, 0, 0)
        else:
            lFx, lFy, lx, ly, prevBlockForceThreshold, prev_yLimit = (
             inp[0], inp[1], inp[2], inp[3], inp[4], inp[5])
        if blockID == 0:
            nVars = 2 + len(AdditionalMasses)
        else:
            nVars = 6 + len(AdditionalMasses)
        r = zeros((6, nVars))
        r[(0, 0)] = 1
        r[(1, 1)] = 1
        r[(1, len(inp) + blockID)] = g
        if blockID != 0:
            r[(2, 2)] = 1
        Fwhole = sqrt(lFx ** 2 + lFy ** 2)
        r[(2, 0)] = lengths[blockID] * lFy ** 2 / Fwhole ** 3
        r[(2, 1)] = -lengths[blockID] * lFx * lFy / Fwhole ** 3
        if blockID != 0:
            r[(3, 3)] = 1
        r[(3, 0)] = -lengths[blockID] * lFx * lFy / Fwhole ** 3
        r[(3, 1)] = lengths[blockID] * lFx ** 2 / Fwhole ** 3
        r[(4, 0)] = lFx / Fwhole / 10000.0
        r[(4, 1)] = lFy / Fwhole / 10000.0
        if blockID != 0:
            r[(5, 3)] = 1.0
        if P != 0:
            projection, distance = project2ball(x=[lFx, lFy], radius=MaxForces[blockID], center=0)
            if distance != 0:
                penalty_derivative = P / 10000.0 * project2ball_derivative(x=[lFx, lFy], radius=MaxForces[blockID], center=0)
                r[(4, 0)] += penalty_derivative[0]
                r[(4, 1)] += penalty_derivative[1]
            projection, distance = project2box(ly, -inf, maxY[blockID])
            if distance > 0:
                r[(5, 3)] = P / 10000.0 * project2box_derivative(ly, -inf, maxY[blockID])
        prevBlockBroken = blockID >= 0 and isnan(prevBlockForceThreshold) or prevBlockForceThreshold > 0 and P == 0 or prev_yLimit > 0 or isnan(prev_yLimit) and P == 0 and not xyCoordsAlwaysExist
        if prevBlockBroken:
            r *= nan
        return r


    ooFuncs, c = [], []
    constrYmax = []
    for i in xrange(n):
        oof = oofun(blockEngineFunc, args=copy(i), name='blockEngine' + str(i))
        if i == 0:
            oof.input = (
             oovarInit, AdditionalMasses)
        else:
            oof.input = (
             ooFuncs[i - 1], AdditionalMasses)
        oof.d = derivative_blockEngineFunc
        ooFuncs.append(oof)
        c.append(oolin([0, 0, 0, 0, 1, 0], input=ooFuncs[copy(i)], name='maxForce' + str(i)))
        c.append(oolin([0, 0, 0, 0, 0, 1], input=ooFuncs[copy(i)], name='Ylimit' + str(i)))

    f = oofun((lambda z: z[0] ** 1.5), input=ooFuncs[-1], d=(lambda z: [0, 0, 1.5 * z[0] ** 0.5, 0, 0, 0]), name='objFunc')
    sumOfMasses = oofun((lambda z: 1 - z.sum() / 100.0), input=AdditionalMasses, d=(lambda z: -ones(n) / 100.0), name='sOm')
    c.append(sumOfMasses)
    colors = [
     'b', 'r', 'g', 'y', 'm', 'c']
    for j, solver in enumerate(solvers):
        p = NLP(f, c=c, goal='max', gtol=1e-06, plot=0, contol=contol, maxFunEvals=10000000000.0)

        def callback(p):
            print p.c(p.xk)
            return 0


        if solver == 'scipy_cobyla':
            p.f_iter = max((int(n / 2), 5))
        if solver == 'ipopt':
            p.maxIter = 1500 - 40 * n
        else:
            p.maxIter = 15000
        r = p.solve(solver, plot=0, showFeas=1, maxTime=150, iprint=-1, ftol=1e-06, xtol=1e-06)
        Results[(n, p.solver.__name__)] = r
        if r.isFeasible:
            msgF = '+'
        else:
            msgF = '-'
        print 'n=%d' % n, 'f=%3.2f' % r.ff + '[' + msgF + ']', 'Time=%3.1f' % r.elapsed['solver_time']
        if PLOT:
            hold(1)
            for i, oof in enumerate(ooFuncs):
                if i == 0:
                    plot([xl, ooFuncs[0](p.xk)[0]], [yl, ooFuncs[0](p.xk)[1]], colors[j])
                    plot([xl, ooFuncs[0](p.x0)[0]], [yl, ooFuncs[0](p.x0)[1]], 'k')
                else:
                    plot([ooFuncs[i - 1](p.xk)[0], ooFuncs[i](p.xk)[0]], [ooFuncs[i - 1](p.xk)[1], ooFuncs[i](p.xk)[1]], colors[j])
                    plot([ooFuncs[i - 1](p.x0)[0], ooFuncs[i](p.x0)[0]], [ooFuncs[i - 1](p.x0)[1], ooFuncs[i](p.x0)[1]], 'k')

    if PLOT:
        show()