# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\UkrOpt\gsubg_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import inf, any, copy, dot, where, all, nan, isfinite, float64, isnan, max, sign, array_equal, matrix, delete, ndarray
from numpy.linalg import norm
from openopt.kernel.baseSolver import *
from openopt.kernel.setDefaultIterFuncs import *
from openopt.solvers.UkrOpt.PolytopProjection import PolytopProjection

class gsubg(baseSolver):
    __name__ = 'gsubg'
    __license__ = 'BSD'
    __authors__ = 'Dmitrey'
    __alg__ = 'Nikolay G. Zhurbenko generalized epsilon-subgradient'
    __optionalDataThatCanBeHandled__ = ['A', 'Aeq', 'b', 'beq', 'lb', 'ub', 'c', 'h']
    iterfcnConnected = True
    _canHandleScipySparse = True
    _requiresBestPointDetection = True
    h0 = 1.0
    hmult = 0.5
    T = float64
    showLS = False
    show_hs = False
    showRes = False
    show_nnan = False
    doBackwardSearch = True
    new_bs = True
    maxVectors = 100
    maxShoots = 15
    sigma = 0.001
    dual = True
    addASG = False

    def __init__(self):
        self.approach = 'all active'
        self.qpsolver = 'cvxopt_qp'
        self.ls_direction = 'simple'
        self.dilation = 'auto'

    def __solver__(self, p):
        assert self.approach == 'all active'
        dilation = self.dilation
        assert dilation in ('auto', True, False, 0, 1)
        if dilation == 'auto':
            dilation = False
            p.debugmsg('%s: autoselect set dilation to %s' % (self.__name__, dilation))
        if dilation:
            from Dilation import Dilation
            D = Dilation(p)
        Point = lambda x: p.point(x)
        h0 = self.h0
        T = self.T
        x0 = p.x0
        if p.nbeq == 0 or any(abs(p._get_AeqX_eq_Beq_residuals(x0)) > p.contol):
            x0[x0 < p.lb] = p.lb[x0 < p.lb]
            x0[x0 > p.ub] = p.ub[x0 > p.ub]
        hs = asarray(h0, T)
        bestPoint = Point(asarray(copy(x0), T))
        bestFeasiblePoint = None if not bestPoint.isFeas(True) else bestPoint
        prevIter_best_ls_point = bestPoint
        best_ls_point = bestPoint
        iterStartPoint = bestPoint
        bestPointBeforeTurn = None
        g = bestPoint._getDirection(self.approach)
        g1 = iterStartPoint._getDirection(self.approach, currBestFeasPoint=bestFeasiblePoint)
        if not any(g) and all(isfinite(g)):
            p.istop = 14 if bestPoint.isFeas(False) else -14
            p.msg = 'move direction has all-zero coords'
            return
        else:
            HS = []
            LS = []
            if p.fTol is None:
                p.warn('The solver requres user-supplied fTol (objective function tolerance); \n            since you have not provided it value, 15*ftol = %0.1e will be used' % (15 * p.ftol))
                p.fTol = 15 * p.ftol
            fTol_start = p.fTol / 2.0
            fTol = fTol_start
            subGradientNorms, points, values, isConstraint, epsilons, inactive, normedSubGradients, normed_values = ([], [], [], [], [], [], [], [])
            StoredInfo = [
             subGradientNorms, points, values, isConstraint, 
             epsilons, inactive, normedSubGradients, normed_values]
            nMaxVec = self.maxVectors
            nVec = 0
            ns = 0
            maxQPshoutouts = 15
            itn = -1
            while True:
                itn += 1
                koeffs = None
                while ns < self.maxShoots:
                    ns += 1
                    nAddedVectors = 0
                    projection = None
                    F0 = asscalar(bestFeasiblePoint.f() - fTol_start) if bestFeasiblePoint is not None else nan
                    if bestPointBeforeTurn is None:
                        sh = schedule = [
                         bestPoint]
                    else:
                        sh = [point1, point2] if point1.betterThan(point2, altLinInEq=True, bestFeasiblePoint=bestFeasiblePoint) else [point2, point1]
                        iterStartPoint = sh[-1]
                        schedule = [ point for point in sh if id(point.x) != id(points[-1]) ]
                    x = iterStartPoint.x.copy()
                    iterInitialDataSize = len(values)
                    for point in schedule:
                        if (point.sum_of_all_active_constraints() > p.contol / 10 or not isfinite(point.f())) and any(point.sum_of_all_active_constraints_gradient()):
                            nVec += 1
                            tmp = point.sum_of_all_active_constraints_gradient()
                            if not isinstance(tmp, ndarray) or isinstance(tmp, matrix):
                                tmp = tmp.A.flatten()
                            n_tmp = norm(tmp)
                            assert n_tmp != 0.0
                            normedSubGradients.append(tmp / n_tmp)
                            subGradientNorms.append(n_tmp)
                            val = point.sum_of_all_active_constraints()
                            values.append(asscalar(val))
                            normed_values.append(asscalar(val / n_tmp))
                            epsilons.append(asscalar((val + dot(point.x, tmp)) / n_tmp))
                            isConstraint.append(True)
                            points.append(point.x)
                            inactive.append(0)
                            nAddedVectors += 1
                        if bestFeasiblePoint is not None and isfinite(point.f()):
                            tmp = point.df()
                            if not isinstance(tmp, ndarray) or isinstance(tmp, matrix):
                                tmp = tmp.A
                            tmp = tmp.flatten()
                            n_tmp = norm(tmp)
                            if n_tmp < p.gtol:
                                p._df = n_tmp
                                p.iterfcn(point)
                                return
                            nVec += 1
                            normedSubGradients.append(tmp / n_tmp)
                            subGradientNorms.append(n_tmp)
                            val = point.f()
                            values.append(asscalar(val))
                            normed_values.append(asscalar(val / n_tmp))
                            epsilons.append(asscalar((val + dot(point.x, tmp)) / n_tmp))
                            isConstraint.append(False)
                            points.append(point.x)
                            inactive.append(0)
                            nAddedVectors += 1

                    if self.addASG and itn != 0 and Projection is not None:
                        tmp = Projection
                        if not isinstance(tmp, ndarray) or isinstance(tmp, matrix):
                            tmp = tmp.A
                        tmp = tmp.flatten()
                        n_tmp = norm(tmp)
                        nVec += 1
                        normedSubGradients.append(tmp / n_tmp)
                        subGradientNorms.append(n_tmp)
                        val = ProjectionVal
                        values.append(asscalar(val))
                        normed_values.append(asscalar(val / n_tmp))
                        epsilons.append(asscalar((val + dot(prevIterPoint.x, tmp)) / n_tmp))
                        if not p.isUC:
                            p.pWarn('addASG is not ajusted with constrained problems handling yet')
                        isConstraint.append(False if p.isUC else True)
                        points.append(prevIterPoint.x)
                        inactive.append(0)
                        nAddedVectors += 1
                    indToBeRemovedBySameAngle = []
                    valDistances1 = asfarray(normed_values)
                    valDistances2 = asfarray([ 0 if isConstraint[i] else -F0 for i in range(nVec) ]) / asfarray(subGradientNorms)
                    valDistances3 = asfarray([ dot(x - points[i], vec) for i, vec in enumerate(normedSubGradients) ])
                    valDistances = valDistances1 + valDistances2 + valDistances3
                    if iterInitialDataSize != 0:
                        for j in range(nAddedVectors):
                            ind = -1 - j
                            scalarProducts = dot(normedSubGradients, normedSubGradients[ind])
                            IND = where(scalarProducts > 1 - self.sigma)[0]
                            if IND.size != 0:
                                _case = 1
                                if _case == 1:
                                    mostUseful = argmax(valDistances[IND])
                                    IND = delete(IND, mostUseful)
                                    indToBeRemovedBySameAngle += IND.tolist()
                                else:
                                    indToBeRemovedBySameAngle += IND[:-1].tolist()

                    indToBeRemovedBySameAngle = list(set(indToBeRemovedBySameAngle))
                    indToBeRemovedBySameAngle.sort(reverse=True)
                    if p.debug:
                        p.debugmsg('indToBeRemovedBySameAngle: ' + str(indToBeRemovedBySameAngle) + ' from %d' % nVec)
                    if indToBeRemovedBySameAngle == range(nVec - 1, nVec - nAddedVectors - 1, -1) and ns > 5:
                        p.istop = 17
                        p.msg = 'all new subgradients have been removed due to the angle threshold'
                        return
                    valDistances = valDistances.tolist()
                    valDistances2 = valDistances2.tolist()
                    for ind in indToBeRemovedBySameAngle:
                        for List in StoredInfo + [valDistances, valDistances2]:
                            del List[ind]

                    nVec -= len(indToBeRemovedBySameAngle)
                    if nVec > nMaxVec:
                        for List in StoredInfo + [valDistances, valDistances2]:
                            del List[:-nMaxVec]

                        assert len(StoredInfo[-1]) == nMaxVec
                        nVec = nMaxVec
                    valDistances = asfarray(valDistances)
                    valDistances2 = asfarray(valDistances2)
                    indActive = where(valDistances >= 0)[0]
                    product = None
                    if p.debug:
                        p.debugmsg('fTol: %f     ns: %d' % (fTol, ns))
                    if nVec > 1:
                        normalizedSubGradients = asfarray(normedSubGradients)
                        product = dot(normalizedSubGradients, normalizedSubGradients.T)
                        for j in range(maxQPshoutouts if bestFeasiblePoint is not None else 1):
                            F = asscalar(bestFeasiblePoint.f() - fTol * 5 ** j) if bestFeasiblePoint is not None else nan
                            valDistances2_modified = asfarray([ 0 if isConstraint[i] else -F for i in range(nVec) ]) / asfarray(subGradientNorms)
                            ValDistances = valDistances + valDistances2_modified - valDistances2
                            new = 0
                            if nVec == 2 and new:
                                a, b = normedSubGradients[0] * ValDistances[0], normedSubGradients[1] * ValDistances[1]
                                a2, b2, ab = (a ** 2).sum(), (b ** 2).sum(), dot(a, b)
                                beta = a2 * (ab - b2) / (ab ** 2 - a2 * b2)
                                alpha = b2 * (ab - a2) / (ab ** 2 - a2 * b2)
                                g1 = alpha * a + beta * b
                            else:
                                koeffs = PolytopProjection(product, asfarray(ValDistances), isProduct=True, solver=self.qpsolver)
                                projection = dot(normalizedSubGradients.T, koeffs).flatten()
                                threshold = 1e-09
                                if j == 0 and any(dot(normalizedSubGradients, projection) < ValDistances * (1 - threshold * sign(ValDistances)) - threshold):
                                    p.istop = 16
                                    p.msg = 'optimal solution wrt required fTol = %g has been obtained' % p.fTol
                                    return
                                g1 = projection
                                M = norm(koeffs, inf)
                                indActive = where(koeffs >= M / 10000000.0)[0]
                                for k in indActive.tolist():
                                    inactive[k] = 0

                            NewPoint = Point(x - g1)
                            if j == 0 or NewPoint.betterThan(best_QP_Point, altLinInEq=True, bestFeasiblePoint=bestFeasiblePoint):
                                best_proj = g1
                                best_QP_Point = NewPoint
                            else:
                                g1 = best_proj
                                break

                        maxQPshoutouts = max((j + 2, 1))
                    else:
                        g1 = iterStartPoint._getDirection(self.approach, currBestFeasPoint=bestFeasiblePoint)
                    if any(isnan(g1)):
                        p.istop = 900
                        return
                    if dilation and len(sh) == 2:
                        point = sh[0] if dot(iterStartPoint._getDirection(self.approach), sh[0]._getDirection(self.approach)) < 0 else sh[1]
                        D.updateDilationMatrix(iterStartPoint._getDirection(self.approach) - point._getDirection(self.approach), alp=1.2)
                        g1 = D.getDilatedVector(g1)
                    if any(g1):
                        g1 /= p.norm(g1)
                    else:
                        p.istop = 103 if Point(x).isFeas(False) else -103
                        return
                    bestPointBeforeTurn = iterStartPoint
                    hs_cumsum = 0
                    hs_start = hs
                    if not isinstance(g1, ndarray) or isinstance(g1, matrix):
                        g1 = g1.A
                    g1 = g1.flatten()
                    hs_mult = 4.0
                    for ls in range(p.maxLineSearch):
                        assert all(isfinite(g1))
                        assert all(isfinite(x))
                        assert isfinite(hs)
                        x -= hs * g1
                        hs *= hs_mult
                        hs_cumsum += hs
                        newPoint = Point(x)
                        if self.show_nnan:
                            p.info('ls: %d nnan: %d' % (ls, newPoint.__nnan__()))
                        if ls == 0:
                            oldPoint = iterStartPoint
                            oldoldPoint = oldPoint
                        assert all(isfinite(oldPoint.x))
                        if newPoint.isFeas(False) and (bestFeasiblePoint is None or newPoint.f() > bestFeasiblePoint.f()):
                            bestFeasiblePoint = newPoint
                        if newPoint.betterThan(oldPoint, altLinInEq=True, bestFeasiblePoint=bestFeasiblePoint):
                            if newPoint.betterThan(bestPoint, altLinInEq=True):
                                bestPoint = newPoint
                            oldoldPoint = oldPoint
                            oldPoint, newPoint = newPoint, None
                        else:
                            bestPointBeforeTurn = oldoldPoint
                            if not itn % 4:
                                for fn in ['_lin_ineq', '_lin_eq']:
                                    if hasattr(newPoint, fn):
                                        delattr(newPoint, fn)

                            break

                    hs /= hs_mult
                    if ls == p.maxLineSearch - 1:
                        p.istop, p.msg = IS_LINE_SEARCH_FAILED, 'maxLineSearch (' + str(p.maxLineSearch) + ') has been exceeded'
                        return
                    p.debugmsg('ls_forward: %d' % ls)
                    maxRecNum = 400
                    point1, point2, nLSBackward = LocalizedSearch(oldoldPoint, newPoint, bestFeasiblePoint, fTol, p, maxRecNum, self.approach)
                    best_ls_point = point1 if point1.betterThan(point2, altLinInEq=True, bestFeasiblePoint=bestFeasiblePoint) else point2
                    if oldoldPoint.betterThan(best_ls_point, altLinInEq=True, bestFeasiblePoint=bestFeasiblePoint):
                        best_ls_point_with_start = oldoldPoint
                    else:
                        best_ls_point_with_start = best_ls_point
                    if best_ls_point.betterThan(bestPoint, altLinInEq=True):
                        bestPoint = best_ls_point
                    if best_ls_point.isFeas(True) and (bestFeasiblePoint is None or best_ls_point.betterThan(bestFeasiblePoint, altLinInEq=True, bestFeasiblePoint=bestFeasiblePoint)):
                        bestFeasiblePoint = best_ls_point
                    step_x = p.norm(best_ls_point.x - prevIter_best_ls_point.x)
                    HS.append(hs_start)
                    assert ls >= 0
                    LS.append(ls)
                    p.debugmsg('hs before: %0.1e' % hs)
                    if step_x != 0:
                        hs = 0.5 * step_x
                    else:
                        hs = max((hs / 10.0, p.xtol / 2.0))
                    p.debugmsg('hs after: %0.1e' % hs)
                    if itn == 0:
                        p.debugmsg('hs: ' + str(hs))
                        p.debugmsg('ls: ' + str(ls))
                    if self.showLS:
                        p.info('ls: ' + str(ls))
                    if self.show_hs:
                        p.info('hs: ' + str(hs))
                    if self.show_nnan:
                        p.info('nnan: ' + str(best_ls_point.__nnan__()))
                    if self.showRes:
                        r, fname, ind = best_ls_point.mr(True)
                        p.info(fname + str(ind))
                    if best_ls_point_with_start.betterThan(iterStartPoint, altLinInEq=True, bestFeasiblePoint=bestFeasiblePoint):
                        ns = 0
                        iterStartPoint = best_ls_point_with_start
                        break
                    else:
                        iterStartPoint = best_ls_point_with_start

                isOverHalphPi = product is not None and any(product[indActive].flatten() <= 0)
                if ns == self.maxShoots and isOverHalphPi:
                    p.istop = 17
                    p.msg = '\n                Max linesearch directions number has been exceeded \n                (probably solution has been obtained), \n                you could increase gsubg parameter "maxShoots" (current value: %d)' % self.maxShoots
                    best_ls_point = best_ls_point_with_start
                prevIter_best_ls_point = best_ls_point_with_start
                if koeffs is not None:
                    indInactive = where(koeffs < M / 10000000.0)[0]
                    for k in indInactive.tolist():
                        inactive[k] += 1

                    indInactiveToBeRemoved = where(asarray(inactive) > 5)[0].tolist()
                    if p.debug:
                        p.debugmsg('indInactiveToBeRemoved:' + str(indInactiveToBeRemoved) + ' from' + str(nVec))
                    if len(indInactiveToBeRemoved) != 0:
                        indInactiveToBeRemoved.reverse()
                        nVec -= len(indInactiveToBeRemoved)
                        for j in indInactiveToBeRemoved:
                            for List in StoredInfo:
                                del List[j]

                if hasattr(p, '_df'):
                    delattr(p, '_df')
                if best_ls_point.isFeas(False) and hasattr(best_ls_point, '_df'):
                    p._df = best_ls_point.df().copy()
                if not all(isfinite(best_ls_point.x)):
                    raise AssertionError
                    cond_same_point = array_equal(best_ls_point.x, p.xk)
                    p.iterfcn(best_ls_point)
                    if cond_same_point and not p.istop:
                        p.istop = 14
                        p.msg = 'X[k-1] and X[k] are same'
                        p.stopdict[SMALL_DELTA_X] = True
                        return
                    s2 = 0
                    if p.istop and not p.userStop:
                        if p.istop not in p.stopdict:
                            p.stopdict[p.istop] = True
                        if SMALL_DF in p.stopdict:
                            if best_ls_point.isFeas(False):
                                s2 = p.istop
                            p.stopdict.pop(SMALL_DF)
                        if SMALL_DELTA_F in p.stopdict:
                            if best_ls_point.isFeas(False) and prevIter_best_ls_point.f() != best_ls_point.f():
                                s2 = p.istop
                            p.stopdict.pop(SMALL_DELTA_F)
                        if SMALL_DELTA_X in p.stopdict and (best_ls_point.isFeas(False) or not prevIter_best_ls_point.isFeas(False) or cond_same_point):
                            s2 = p.istop
                        p.stopdict.pop(SMALL_DELTA_X)
                    if not s2 and any(p.stopdict.values()):
                        for key, val in p.stopdict.items():
                            if val == True:
                                s2 = key
                                break

                    p.istop = s2
                    for key, val in p.stopdict.items():
                        if key < 0 or key in set([FVAL_IS_ENOUGH, USER_DEMAND_STOP, BUTTON_ENOUGH_HAS_BEEN_PRESSED]):
                            return

                if p.istop:
                    return

            return


isPointCovered2 = lambda pointWithSubGradient, pointToCheck, bestFeasiblePoint, fTol, contol: pointWithSubGradient.f() - bestFeasiblePoint.f() + 0.75 * fTol > dot(pointWithSubGradient.x - pointToCheck.x, pointWithSubGradient.df())

def isPointCovered3(pointWithSubGradient, pointToCheck, bestFeasiblePoint, fTol, contol):
    if bestFeasiblePoint is not None and pointWithSubGradient.f() - bestFeasiblePoint.f() + 0.75 * fTol > dot(pointWithSubGradient.x - pointToCheck.x, pointWithSubGradient.df()):
        return True
    else:
        if not pointWithSubGradient.isFeas(True) and pointWithSubGradient.mr_alt(bestFeasPoint=bestFeasiblePoint) + 1e-15 > dot(pointWithSubGradient.x - pointToCheck.x, pointWithSubGradient._getDirection('all active', currBestFeasPoint=bestFeasiblePoint)):
            return True
        return False


def isPointCovered4(pointWithSubGradient, pointToCheck, bestFeasiblePoint, fTol, contol):
    if pointWithSubGradient.isFeas(True):
        return pointWithSubGradient.f() - bestFeasiblePoint.f() + 0.75 * fTol > dot(pointWithSubGradient.x - pointToCheck.x, pointWithSubGradient.df())
    if pointWithSubGradient.sum_of_all_active_constraints() + 0.75 * contol > dot(pointWithSubGradient.x - pointToCheck.x, pointWithSubGradient.sum_of_all_active_constraints_gradient()):
        return True
    return False


isPointCovered = isPointCovered4

def LocalizedSearch(point1, point2, bestFeasiblePoint, fTol, p, maxRecNum, approach):
    contol = p.contol
    for i in range(maxRecNum):
        if p.debug:
            p.debugmsg('req num: %d from %d' % (i, maxRecNum))
        new = 0
        if new:
            if point1.betterThan(point2, altLinInEq=True, bestFeasiblePoint=bestFeasiblePoint) and isPointCovered(point2, point1, bestFeasiblePoint, fTol) or point2.betterThan(point1, altLinInEq=True, bestFeasiblePoint=bestFeasiblePoint) and isPointCovered(point1, point2, bestFeasiblePoint, fTol):
                break
        else:
            isPoint1Covered = isPointCovered(point2, point1, bestFeasiblePoint, fTol, contol)
            isPoint2Covered = isPointCovered(point1, point2, bestFeasiblePoint, fTol, contol)
            if isPoint1Covered and isPoint2Covered:
                break
        point = point1.linePoint(0.5, point2)
        if point.isFeas(False) and (bestFeasiblePoint is None or bestFeasiblePoint.f() > point.f()):
            bestFeasiblePoint = point
        if dot(point._getDirection(approach, currBestFeasPoint=bestFeasiblePoint), point1.x - point2.x) < 0:
            point2 = point
        else:
            point1 = point

    return (
     point1, point2, i)