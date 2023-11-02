# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\UkrOpt\ralg_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import diag, array, sqrt, eye, ones, inf, any, copy, zeros, dot, where, all, sum, isfinite, float64, isnan, log10, max, sign, array_equal, logical_and, matrix
from openopt.kernel.ooMisc import norm
try:
    from numpy.linalg import solve, LinAlgError
except ImportError:
    LinAlgError = Exception

    def solve(*args, **kw):
        print 'ralg with equality constraints is unimplemented yet'
        raise Exception('ralg with equality constraints is unimplemented yet')


from openopt.kernel.nonOptMisc import scipyAbsentMsg, scipyInstalled, isPyPy
import openopt
from openopt.kernel.baseSolver import *
from openopt.kernel.ooMisc import economyMult, Len
from openopt.kernel.setDefaultIterFuncs import *
from openopt.solvers.UkrOpt.UkrOptMisc import getBestPointAfterTurn

class ralg(baseSolver):
    __name__ = 'ralg'
    __license__ = 'BSD'
    __authors__ = 'Dmitrey'
    __alg__ = 'Naum Z. Shor R-algorithm with adaptive space dilation & some modifications'
    __optionalDataThatCanBeHandled__ = ['A', 'Aeq', 'b', 'beq', 'lb', 'ub', 'c', 'h']
    iterfcnConnected = True
    _canHandleScipySparse = True
    B = None
    alp, h0, nh, q1, q2 = (2.0, 1.0, 3, 'default:0.9 for NLP, 1.0 for NSP', 1.1)
    hmult = 0.5
    S = 0
    T = float64
    dilationType = 'plain difference'
    showLS = False
    show_hs = False
    showRej = False
    showRes = False
    show_nnan = False
    doBackwardSearch = True
    approach = 'all active'
    newLinEq = True
    new_bs = True
    skipPrevIterNaNsInDilation = True
    innerState = None
    penalties = False

    def needRej(self, p, b, g, g_dilated):
        return 100000000000000.0 * p.norm(g_dilated) < p.norm(g)

    def __init__(self):
        pass

    def __solver__(self, p):
        alp, h0, nh, q1, q2 = (
         self.alp, self.h0, self.nh, self.q1, self.q2)
        if isPyPy:
            if p.nc != 0 or p.nh != 0:
                p.warn('in PyPy ralg may work incorrectly with nonlinear constraints yet')
            if p.nbeq != 0 or any(p.lb == p.ub):
                p.err('in PyPy ralg cannot handle linear equality constraints yet')
        if type(q1) == str:
            if p.probType == 'NLP' and p.isUC:
                q1 = 0.9
            else:
                q1 = 1.0
        T = self.T
        n = p.n
        x0 = p.x0
        if p.nbeq == 0 or any(abs(p._get_AeqX_eq_Beq_residuals(x0)) > p.contol):
            x0[x0 < p.lb] = p.lb[x0 < p.lb]
            x0[x0 > p.ub] = p.ub[x0 > p.ub]
        ind_box_eq = where(p.lb == p.ub)[0]
        nEQ = ind_box_eq.size
        if nEQ != 0:
            initLenBeq = p.nbeq
            Aeq, beq, nbeq = copy(p.Aeq), copy(p.beq), p.nbeq
            p.Aeq = zeros([Len(p.beq) + nEQ, p.n])
            p.beq = zeros(Len(p.beq) + nEQ)
            p.beq[:(Len(beq))] = beq
            p.Aeq[:(Len(beq))] = Aeq
            for i in range(len(ind_box_eq)):
                p.Aeq[(initLenBeq + i, ind_box_eq[i])] = 1
                p.beq[initLenBeq + i] = p.lb[ind_box_eq[i]]

            p.nbeq += nEQ
        if not self.newLinEq or p.nbeq == 0:
            needProjection = False
            B0 = eye(n, dtype=T)
            restoreProb = lambda *args: 0
            Aeq_r, beq_r, nbeq_r = (None, None, 0)
        else:
            needProjection = True
            B0 = self.getPrimevalDilationMatrixWRTlinEqConstraints(p)
            if any(abs(p._get_AeqX_eq_Beq_residuals(x0)) > p.contol / 16.0):
                try:
                    x0 = self.linEqProjection(x0, p.Aeq, p.beq)
                except LinAlgError:
                    s = 'Failed to obtain projection of start point to linear equality constraints subspace, probably the system is infeasible'
                    p.istop, p.msg = -25, s
                    return

            if nEQ == 0:
                Aeq_r, beq_r, nbeq_r = p.Aeq, p.beq, p.nbeq
            else:
                Aeq_r, beq_r, nbeq_r = Aeq, beq, nbeq
            p.Aeq, p.beq, p.nbeq = (None, None, 0)

            def restoreProb():
                p.Aeq, p.beq, p.nbeq = Aeq_r, beq_r, nbeq_r

        b = B0.copy() if self.B is None else self.B
        hs = asarray(h0, T)
        if self.innerState is not None:
            hs = self.innerState['hs']
            b = self.innerState['B']
        ls_arr = []
        w = asarray(1.0 / alp - 1.0, T)
        bestPoint = p.point(array(copy(x0).tolist(), T))
        prevIter_best_ls_point = bestPoint
        prevIter_PointForDilation = bestPoint
        g = bestPoint._getDirection(self.approach)
        prevDirectionForDilation = g
        moveDirection = g
        if not any(g) and all(isfinite(g)):
            p.iterfcn(bestPoint)
            restoreProb()
            p.istop = 14 if bestPoint.isFeas(False) else -14
            p.msg = 'move direction has all-zero coords'
            return
        else:
            HS = []
            LS = []
            SwitchEncountered = False
            selfNeedRej = False
            doScale = False
            fTol = p.fTol if p.fTol is not None else 15 * p.ftol
            if self.penalties:
                oldVal = p.f(p.x0)
                newVal = inf
                x = p.x0
                if p.nh != 0:
                    _Aeq = p.dh(x)
                    _beq = -p.h(x)
                    df = p.df(x)
                    if n >= 150 and not scipyInstalled:
                        p.pWarn(scipyAbsentMsg)
                    if n > 100 and scipyInstalled:
                        from scipy.sparse import eye as Eye
                        HH = Eye(n, n)
                    else:
                        HH = eye(n)
                    qp = openopt.QP(H=HH, f=df, Aeq=_Aeq, beq=_beq)
                    QPsolver = openopt.oosolver('cvxopt_qp', iprint=-1)
                    if not QPsolver.isInstalled:
                        S = None
                    else:
                        r = qp.solve(QPsolver)
                        S = 10.0 * sum(abs(r.duals)) if r.istop > 0 else None
                    while any(p.h(x)) > p.contol:
                        if S is not None:
                            p2 = getattr(openopt, p.probType)(p.f, x)
                            p.inspire(p2)
                            p2.x0 = x
                            p2.h = p2.dh = None
                            p2.userProvided.h = p2.userProvided.dh = False
                            p2.nh = 0
                            p2.f = lambda *args, **kwargs: p.f(*args, **kwargs) + sum(abs(S * p.h(*args, **kwargs)))
                            p2.df = lambda *args, **kwargs: p.df(*args, **kwargs) + dot(S * sign(p.h(*args, **kwargs)), p.dh(*args, **kwargs))
                            r2 = p2.solve(p.solver, iprint=10)
                            if r2.stopcase >= 0:
                                x = r2.xf
                                p.solver.innerState = r2.extras['innerState']
                                oldVal, newVal = newVal, r2.ff
                            elif r2.istop == IS_LINE_SEARCH_FAILED:
                                pass
                            if p.isFeas(p2.xk):
                                p.xf = p.xk = p2.xk
                                p.istop, p.msg = p2.istop, p2.msg
                                return
                            S *= 50
                        else:
                            break

            for itn in range(p.maxIter + 10):
                doDilation = True
                lastPointOfSameType = None
                alp_addition = 0.0
                iterStartPoint = prevIter_best_ls_point
                x = iterStartPoint.x.copy()
                g_tmp = economyMult(b.T, moveDirection)
                if any(g_tmp):
                    g_tmp /= p.norm(g_tmp)
                g1 = p.matmult(b, g_tmp)
                hs_cumsum = 0
                hs_start = hs
                for ls in range(p.maxLineSearch):
                    hs_mult = 1.0
                    if ls > 20:
                        hs_mult = 2.0
                    elif ls > 10:
                        hs_mult = 1.5
                    elif ls > 2:
                        hs_mult = 1.05
                    hs *= hs_mult
                    x -= hs * g1
                    hs_cumsum += hs
                    newPoint = p.point(x) if ls == 0 else iterStartPoint.linePoint(hs_cumsum / (hs_cumsum - hs), oldPoint)
                    if not p.isUC:
                        if newPoint.isFeas(True) == iterStartPoint.isFeas(True):
                            lastPointOfSameType = newPoint
                    if self.show_nnan:
                        p.info('ls: %d nnan: %d' % (ls, newPoint.__nnan__()))
                    if ls == 0:
                        oldPoint = prevIter_best_ls_point
                        oldoldPoint = oldPoint
                    if newPoint.betterThan(oldPoint, altLinInEq=True):
                        if newPoint.betterThan(bestPoint, altLinInEq=False):
                            bestPoint = newPoint
                        oldoldPoint = oldPoint
                        oldPoint, newPoint = newPoint, None
                    else:
                        if not itn % 4:
                            for fn in ['_lin_ineq', '_lin_eq']:
                                if hasattr(newPoint, fn):
                                    delattr(newPoint, fn)

                        break

                hs /= hs_mult
                if ls == p.maxLineSearch - 1:
                    p.istop, p.msg = IS_LINE_SEARCH_FAILED, 'maxLineSearch (' + str(p.maxLineSearch) + ') has been exceeded, the problem seems to be unbounded'
                    restoreProb()
                    return
                PointForDilation = newPoint
                mdx = max((150, 1.5 * p.n)) * p.xtol
                if itn == 0:
                    mdx = max((hs / 128.0, 128 * p.xtol))
                ls_backward = 0
                maxLS = 3 if ls == 0 else 1
                if self.doBackwardSearch:
                    if self.new_bs:
                        best_ls_point, PointForDilation, ls_backward = getBestPointAfterTurn(oldoldPoint, newPoint, maxLS=maxLS, maxDeltaF=150 * p.ftol, maxDeltaX=mdx, altLinInEq=True, new_bs=True)
                        if PointForDilation.isFeas(True) == iterStartPoint.isFeas(True):
                            lastPointOfSameType = PointForDilation
                    else:
                        best_ls_point, ls_backward = getBestPointAfterTurn(oldoldPoint, newPoint, maxLS=maxLS, altLinInEq=True, new_bs=False)
                        PointForDilation = best_ls_point
                    if best_ls_point.betterThan(bestPoint):
                        bestPoint = best_ls_point
                    if ls == 0 and ls_backward == -maxLS:
                        alp_addition += 0.25
                    if ls_backward <= -1 and itn != 0:
                        pass
                best_ls_point = PointForDilation
                step_x = p.norm(PointForDilation.x - prevIter_PointForDilation.x)
                step_f = abs(PointForDilation.f() - prevIter_PointForDilation.f())
                HS.append(hs_start)
                assert ls >= 0
                LS.append(ls)
                if itn > 3:
                    mean_ls = (3 * LS[-1] + 2 * LS[-2] + LS[-3]) / 6.0
                    j0 = 3.3
                    if mean_ls > j0:
                        hs = (mean_ls - j0 + 1) ** 0.5 * hs_start
                    else:
                        hs = hs_start
                        if ls == 0 and ls_backward == -maxLS:
                            shift_x = step_x / p.xtol
                            RD = log10(shift_x + 1e-100)
                            if PointForDilation.isFeas(True) or prevIter_PointForDilation.isFeas(True):
                                RD = min((RD, asscalar(asarray(log10(step_f / p.ftol + 1e-100)))))
                            if RD > 1.0:
                                mp = (
                                 0.5, (ls / j0) ** 0.5, 1 - 0.2 * RD)
                                hs *= max(mp)
                best_ls_point = PointForDilation
                involve_lastPointOfSameType = False
                if lastPointOfSameType is not None and PointForDilation.isFeas(True) != prevIter_PointForDilation.isFeas(True):
                    assert self.dilationType == 'plain difference'
                    PointForDilation = lastPointOfSameType
                    involve_lastPointOfSameType = True
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
                if self.skipPrevIterNaNsInDilation:
                    c_prev, c_current = prevIter_PointForDilation.c(), PointForDilation.c()
                    h_prev, h_current = prevIter_PointForDilation.h(), PointForDilation.h()
                NaN_derivatives_excluded = False
                if self.skipPrevIterNaNsInDilation:
                    if not self.approach == 'all active':
                        raise AssertionError
                        if not prevIter_PointForDilation.isFeas(True):
                            ind_switch_ineq_to_nan = where(logical_and(isnan(c_current), c_prev > 0))[0]
                            if len(ind_switch_ineq_to_nan) != 0:
                                NaN_derivatives_excluded = True
                                tmp = prevIter_PointForDilation.dc(ind_switch_ineq_to_nan)
                                if hasattr(tmp, 'toarray'):
                                    tmp = tmp.A
                                if len(ind_switch_ineq_to_nan) > 1:
                                    tmp *= (c_prev[ind_switch_ineq_to_nan] / sqrt((tmp ** 2).sum(1))).reshape(-1, 1)
                                else:
                                    tmp *= c_prev[ind_switch_ineq_to_nan] / norm(tmp)
                                if tmp.ndim > 1:
                                    tmp = tmp.sum(0)
                                if not isinstance(tmp, ndarray) or isinstance(tmp, matrix):
                                    tmp = tmp.A.flatten()
                                prevDirectionForDilation -= tmp
                            ind_switch_eq_to_nan = where(logical_and(isnan(h_current), h_prev > 0))[0]
                            if len(ind_switch_eq_to_nan) != 0:
                                NaN_derivatives_excluded = True
                                tmp = prevIter_PointForDilation.dh(ind_switch_eq_to_nan)
                                if tmp.ndim > 1:
                                    tmp = tmp.sum(0)
                                if not isinstance(tmp, ndarray) or isinstance(tmp, matrix):
                                    tmp = tmp.A.flatten()
                                prevDirectionForDilation -= tmp
                            ind_switch_eq_to_nan = where(logical_and(isnan(h_current), h_prev < 0))[0]
                            if len(ind_switch_eq_to_nan) != 0:
                                NaN_derivatives_excluded = True
                                tmp = prevIter_PointForDilation.dh(ind_switch_eq_to_nan)
                                if tmp.ndim > 1:
                                    tmp = tmp.sum(0)
                                if not isinstance(tmp, ndarray) or isinstance(tmp, matrix):
                                    tmp = tmp.A.flatten()
                                prevDirectionForDilation += tmp
                    directionForDilation = PointForDilation._getDirection(self.approach)
                    if self.skipPrevIterNaNsInDilation:
                        ind_switch_ineq_from_nan = PointForDilation.isFeas(True) or where(logical_and(isnan(c_prev), c_current > 0))[0]
                        if len(ind_switch_ineq_from_nan) != 0:
                            NaN_derivatives_excluded = True
                            tmp = PointForDilation.dc(ind_switch_ineq_from_nan)
                            if hasattr(tmp, 'toarray'):
                                tmp = tmp.A
                            if len(ind_switch_ineq_from_nan) > 1:
                                tmp *= (c_current[ind_switch_ineq_from_nan] / sqrt((tmp ** 2).sum(1))).reshape(-1, 1)
                            else:
                                tmp *= c_current[ind_switch_ineq_from_nan] / norm(tmp)
                            if tmp.ndim > 1:
                                tmp = tmp.sum(0)
                            if not isinstance(tmp, ndarray) or isinstance(tmp, matrix):
                                tmp = tmp.A.flatten()
                            directionForDilation -= tmp
                        ind_switch_eq_from_nan = where(logical_and(isnan(h_prev), h_current > 0))[0]
                        if len(ind_switch_eq_from_nan) != 0:
                            NaN_derivatives_excluded = True
                            tmp = PointForDilation.dh(ind_switch_eq_from_nan)
                            if tmp.ndim > 1:
                                tmp = tmp.sum(0)
                            if not isinstance(tmp, ndarray) or isinstance(tmp, matrix):
                                tmp = tmp.A.flatten()
                            directionForDilation -= tmp
                        ind_switch_eq_from_nan = where(logical_and(isnan(h_prev), h_current < 0))[0]
                        if len(ind_switch_eq_from_nan) != 0:
                            NaN_derivatives_excluded = True
                            tmp = PointForDilation.dh(ind_switch_eq_from_nan)
                            if tmp.ndim > 1:
                                tmp = tmp.sum(0)
                            if not isinstance(tmp, ndarray) or isinstance(tmp, matrix):
                                tmp = tmp.A.flatten()
                            directionForDilation += tmp
                if self.dilationType == 'normalized' and (fname_p not in ('lb', 'ub',
                                                                          'lin_eq',
                                                                          'lin_ineq') or fname_ not in ('lb',
                                                                                                        'ub',
                                                                                                        'lin_eq',
                                                                                                        'lin_ineq')) and (fname_p != fname_ or ind_p != ind_):
                    G2, G = directionForDilation / norm(directionForDilation), prevDirectionForDilation / norm(prevDirectionForDilation)
                else:
                    G2, G = directionForDilation, prevDirectionForDilation
                if prevIter_PointForDilation.isFeas(True) == PointForDilation.isFeas(True):
                    g1 = G2 - G
                elif prevIter_PointForDilation.isFeas(True):
                    g1 = G2.copy()
                else:
                    g1 = G.copy()
                    alp_addition += 0.05
                if norm(G2 - G) < 1e-12 * min((norm(G2), norm(G))) and (involve_lastPointOfSameType or NaN_derivatives_excluded):
                    p.debugmsg("ralg: 'last point of same type gradient' is used")
                    g1 = G2
                if doDilation:
                    g = economyMult(b.T, g1)
                    ng = p.norm(g)
                    if self.needRej(p, b, g1, g) or selfNeedRej:
                        selfNeedRej = False
                        if self.showRej or p.debug:
                            p.info('debug msg: matrix B restoration in ralg solver')
                        b = B0.copy()
                        hs = p.norm(prevIter_best_ls_point.x - best_ls_point.x)
                    if ng < 1e-40:
                        hs *= 0.9
                        p.debugmsg('small dilation direction norm (%e), skipping' % ng)
                    if all(isfinite(g)) and ng > 1e-50 and doDilation:
                        g = (g / ng).reshape(-1, 1)
                        vec1 = economyMult(b, g).reshape(-1, 1)
                        w = asarray(1.0 / (alp + alp_addition) - 1.0, T)
                        vec2 = w * g.T
                        b += p.matmult(vec1, vec2)
                if hasattr(p, '_df'):
                    delattr(p, '_df')
                if best_ls_point.isFeas(False) and hasattr(best_ls_point, '_df'):
                    p._df = best_ls_point.df().copy()
                p.iterfcn(best_ls_point)
                cond_same_point = array_equal(best_ls_point.x, prevIter_best_ls_point.x)
                if cond_same_point and not p.istop:
                    p.istop = 14
                    p.msg = 'X[k-1] and X[k] are same'
                    p.stopdict[SMALL_DELTA_X] = True
                    restoreProb()
                    self.innerState = {'B': b, 'hs': hs}
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
                    if SMALL_DELTA_X in p.stopdict:
                        if best_ls_point.isFeas(False) or not prevIter_best_ls_point.isFeas(False) or cond_same_point:
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
                            p.iterfcn(bestPoint)
                            self.innerState = {'B': b, 'hs': hs}
                            return

                if p.istop:
                    restoreProb()
                    p.iterfcn(bestPoint)
                    self.innerState = {'B': b, 'hs': hs}
                    return
                prevIter_best_ls_point = best_ls_point
                prevIter_PointForDilation = best_ls_point
                prevDirectionForDilation = best_ls_point._getDirection(self.approach)
                moveDirection = best_ls_point._getDirection(self.approach)

            return

    def getPrimevalDilationMatrixWRTlinEqConstraints(self, p):
        n, Aeq, beq = p.n, p.Aeq, p.beq
        nLinEq = len(p.beq)
        ind_fixed = where(p.lb == p.ub)[0]
        arr = ones(n, dtype=self.T)
        arr[ind_fixed] = 0
        b = diag(arr)
        if hasattr(Aeq, 'tocsc'):
            Aeq = Aeq.tocsc()
        for i in range(nLinEq):
            vec = Aeq[i]
            if hasattr(vec, 'toarray'):
                vec = vec.toarray().flatten()
            g = economyMult(b.T, vec)
            if not any(g):
                continue
            ng = norm(g)
            g = (g / ng).reshape(-1, 1)
            vec1 = p.matmult(b, g)
            vec2 = -g.T
            b += p.matmult(vec1, vec2)

        return b

    def linEqProjection(self, x, Aeq, beq):
        if hasattr(Aeq, 'toarray'):
            Aeq = Aeq.toarray()
        AeqT = Aeq.T
        AeqAeqT = dot(Aeq, AeqT)
        Aeqx = dot(Aeq, x)
        AeqT_AeqAeqT_inv_Aeqx = dot(AeqT, ravel(solve(AeqAeqT, Aeqx)))
        AeqT_AeqAeqT_inv_beq = dot(AeqT, ravel(solve(AeqAeqT, beq)))
        xf = x - AeqT_AeqAeqT_inv_Aeqx + AeqT_AeqAeqT_inv_beq
        return xf