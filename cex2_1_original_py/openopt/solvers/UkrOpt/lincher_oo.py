# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\UkrOpt\lincher_oo.pyc
# Compiled at: 2012-12-08 11:04:59
__docformat__ = 'restructuredtext en'
from numpy import diag, ones, inf, any, copy, sqrt, vstack, concatenate, asarray, nan, where, array, zeros, exp, isfinite
from .openopt.kernel.baseSolver import *
from openopt import LP, QP, NLP, LLSP, NSP
from openopt.kernel.ooMisc import WholeRepr2LinConst
from numpy import arange, sign, hstack
from UkrOptMisc import getDirectionOptimPoint, getConstrDirection
import os

class lincher(baseSolver):
    __name__ = 'lincher'
    __license__ = 'BSD'
    __authors__ = 'Dmitrey'
    __alg__ = 'a linearization-based solver written in Cherkassy town, Ukraine'
    __optionalDataThatCanBeHandled__ = ['A', 'Aeq', 'b', 'beq', 'lb', 'ub', 'c', 'h']
    __isIterPointAlwaysFeasible__ = lambda self, p: p.__isNoMoreThanBoxBounded__()
    iterfcnConnected = True

    def __init__(self):
        pass

    def __solver__(self, p):
        n = p.n
        x0 = copy(p.x0)
        xPrev = x0.copy()
        xf = x0.copy()
        xk = x0.copy()
        p.xk = x0.copy()
        f0 = p.f(x0)
        fk = f0
        ff = f0
        p.fk = fk
        df0 = p.df(x0)
        isBB = p.__isNoMoreThanBoxBounded__()
        H = diag(ones(p.n))
        if not p.userProvided.c:
            p.c = lambda x: array([])
            p.dc = lambda x: array([]).reshape(0, p.n)
        if not p.userProvided.h:
            p.h = lambda x: array([])
            p.dh = lambda x: array([]).reshape(0, p.n)
        p.use_subproblem = 'QP'
        for k in range(p.maxIter + 4):
            if isBB:
                f0 = p.f(xk)
                df = p.df(xk)
                direction = -df
                f1 = p.f(xk + direction)
                ind_l = direction <= p.lb - xk
                direction[ind_l] = (p.lb - xk)[ind_l]
                ind_u = direction >= p.ub - xk
                direction[ind_u] = (p.ub - xk)[ind_u]
                ff = p.f(xk + direction)
            else:
                mr = p.getMaxResidual(xk)
                if mr > p.contol:
                    mr_grad = p.getMaxConstrGradient(xk)
                lb = p.lb - xk
                ub = p.ub - xk
                c, dc, h, dh, df = (p.c(xk), p.dc(xk), p.h(xk), p.dh(xk), p.df(xk))
                A, Aeq = vstack((dc, p.A)), vstack((dh, p.Aeq))
                b = concatenate((-c, p.b - p.matmult(p.A, xk)))
                beq = concatenate((-h, p.beq - p.matmult(p.Aeq, xk)))
                if b.size != 0:
                    isFinite = isfinite(b)
                    ind = where(isFinite)[0]
                    A, b = A[ind], b[ind]
                if beq.size != 0:
                    isFinite = isfinite(beq)
                    ind = where(isFinite)[0]
                    Aeq, beq = Aeq[ind], beq[ind]
                if p.use_subproblem == 'LP':
                    linprob = LP(df, A=A, Aeq=Aeq, b=b, beq=beq, lb=lb, ub=ub)
                    linprob.iprint = -1
                    r2 = linprob.solve('cvxopt_glpk')
                    if r2.istop <= 0:
                        p.istop = -12
                        p.msg = 'failed to solve LP subproblem'
                        return
                else:
                    if p.use_subproblem == 'QP':
                        qp = QP(H=H, f=df, A=A, Aeq=Aeq, b=b, beq=beq, lb=lb, ub=ub)
                        qp.iprint = -1
                        r2 = qp.solve('cvxopt_qp')
                        if r2.istop <= 0:
                            for i in range(4):
                                if p.debug:
                                    p.warn('iter ' + str(k) + ': attempt Num ' + str(i) + ' to solve QP subproblem has failed')
                                A2 = vstack((A, Aeq, -Aeq))
                                b2 = concatenate((b, beq, -beq)) + pow(10, i) * p.contol
                                qp = QP(H=H, f=df, A=A2, b=b2, iprint=-5)
                                qp.lb = lb - pow(10, i) * p.contol
                                qp.ub = ub + pow(10, i) * p.contol
                                try:
                                    r2 = qp.solve('cvxopt_qp')
                                except:
                                    r2.istop = -11

                                if r2.istop > 0:
                                    break

                            if r2.istop <= 0:
                                p.istop = -11
                                p.msg = 'failed to solve QP subproblem'
                                return
                    elif p.use_subproblem == 'LLSP':
                        direction_c = getConstrDirection(p, xk, regularization=1e-07)
                    else:
                        p.err('incorrect or unknown subproblem')
                if isBB:
                    X0 = xk.copy()
                    N = 0
                    result, newX = chLineSearch(p, X0, direction, N, isBB)
                elif p.use_subproblem != 'LLSP':
                    duals = r2.duals
                    N = 1.05 * abs(duals).sum()
                    direction = r2.xf
                    X0 = xk.copy()
                    result, newX = chLineSearch(p, X0, direction, N, isBB)
                else:
                    direction_f = -df
                    p2 = NSP(LLSsubprobF, [0.8, 0.8], ftol=0, gtol=0, xtol=1e-05, iprint=-1)
                    p2.args.f = (xk, direction_f, direction_c, p, 1e+20)
                    r_subprob = p2.solve('ralg')
                    alpha = r_subprob.xf
                    newX = xk + alpha[0] * direction_f + alpha[1] * direction_c
                    result = 0
                if result != 0:
                    p.istop = result
                    p.xf = newX
                    return
                xk = newX.copy()
                fk = p.f(xk)
                p.xk, p.fk = copy(xk), copy(fk)
                p.iterfcn()
                if p.istop:
                    p.xf = xk
                    p.ff = fk
                    return


class lineSearchFunction(object):

    def __init__(self, p, x0, N):
        self.p = p
        self.x0 = x0
        self.N = N

    def __call__(self, x):
        return float(self.p.f(x) + self.N * max(self.p.getMaxResidual(x), 0.999 * self.p.contol))

    def gradient_numerical(self, x):
        g = zeros(self.p.n)
        f0 = self.__call__(x)
        for i in range(self.p.n):
            x[i] += self.p.diffInt
            g[i] = self.__call__(x) - f0
            x[i] -= self.p.diffInt

        g /= self.p.diffInt
        return g

    def gradient(self, x):
        N = self.N
        g = self.p.df(x) + N * self.p.getMaxConstrGradient(x)
        return g


def LLSsubprobF(alpha, x, direction_f, direction_c, p, S=1e+30):
    x2 = x + alpha[0] * direction_f + alpha[1] * direction_c
    constr = p.getMaxResidual(x2)
    fval = p.f(x2)
    return max(constr - p.contol, 0) * S + fval


def chLineSearch(p, x0, direction, N, isBB):
    lsF = lineSearchFunction(p, x0, N)
    c1, c2 = (0.0001, 0.9)
    result = 0
    ls_solver = 'Armijo_modified'
    if ls_solver == 'scipy.optimize.line_search':
        old_fval = p.dotmult(lsF.gradient(x0), direction).sum()
        old_old_fval = old_fval / 2.0
        results = scipy_optimize_linesearch(lsF, lsF.gradient, x0, direction, lsF.gradient(x0), old_fval, old_old_fval, c1=c1, c2=c2)
        alpha = results[0]
        destination = x0 + alpha * direction
    elif ls_solver == 'Matthieu.optimizers.BacktrackingSearch':
        state = {'direction': direction, 'gradient': lsF.gradient(x0)}
        mylinesearch = line_search.BacktrackingSearch()
        destination = mylinesearch(function=lsF, origin=x0, step=direction, state=state)
    elif ls_solver == 'Matthieu.optimizers.StrongWolfePowellRule':
        state = {'direction': direction, 'gradient': lsF.gradient(x0)}
        mylinesearch = line_search.StrongWolfePowellRule()
        destination = mylinesearch(function=lsF, origin=x0, step=direction, state=state)
    elif ls_solver == 'Armijo_modified3':
        alpha, alpha_min = 1.0, 0.45 * p.xtol / p.norm(direction)
        lsF_x0 = lsF(x0)
        C1 = abs(c1 * (p.norm(direction) ** 2).sum())
        iterValues.r0 = p.getMaxResidual(x0)
        while 1:
            print 'stage 1'
            if lsF(x0 + direction * alpha) <= lsF_x0 - alpha * C1 and p.getMaxResidual(x0 + direction * alpha) <= max(p.contol, iterValues.r0):
                assert alpha >= 0
                break
            alpha /= 2.0
            if alpha < alpha_min:
                if p.debug:
                    p.warn('alpha less alpha_min')
                break

        if alpha == 1.0:
            print 'stage 2'
            K = 1.5
            lsF_prev = lsF_x0
            for i in range(p.maxLineSearch):
                lsF_new = lsF(x0 + K * direction * alpha)
                newConstr = p.getMaxResidual(x0 + K * direction * alpha)
                if lsF_new > lsF_prev or newConstr > max(p.contol, iterValues.r0):
                    break
                else:
                    alpha *= K
                    lsF_prev = lsF_new

        destination = x0 + direction * alpha
    elif ls_solver == 'Armijo_modified':
        alpha, alpha_min = 1.0, 0.15 * p.xtol / p.norm(direction)
        grad_x0 = lsF.gradient(x0)
        C1 = abs(c1 * (p.norm(direction) ** 2).sum())
        lsF_x0 = lsF(x0)
        while 1:
            if lsF(x0 + direction * alpha) <= lsF_x0 - alpha * C1:
                assert alpha >= 0
                break
            alpha /= 2.0
            if alpha < alpha_min:
                if p.debug:
                    p.warn('alpha less alpha_min')
                break

        destination = x0 + direction * alpha
        if alpha == 1.0 and not isBB:
            K = 1.5
            lsF_prev = lsF_x0
            for i in range(p.maxLineSearch):
                x_new = x0 + K * direction * alpha
                lsF_new = lsF(x_new)
                if lsF_new >= lsF_prev:
                    break
                else:
                    destination = x_new
                    alpha *= K
                    lsF_prev = lsF_new

    elif ls_solver == 'Armijo_modified2':
        grad_objFun_x0 = p.df(x0)
        grad_iterValues.r_x0 = p.getMaxConstrGradient(x0)
        C1_objFun = c1 * p.dotmult(direction, grad_objFun_x0).sum()
        C1_constr = c1 * p.dotmult(direction, grad_iterValues.r_x0).sum()
        f0 = p.f(x0)
        f_prev = f0
        allowedConstr_start = max(0.999 * p.contol, p.getMaxResidual(x0))
        alpha, alpha_min = (1.0, 1e-11)
        isConstrAccepted = False
        isObjFunAccepted = False
        while alpha >= alpha_min:
            x_new = x0 + direction * alpha
            if not isConstrAccepted:
                currConstr = p.getMaxResidual(x_new)
                if currConstr > allowedConstr_start + alpha * C1_constr:
                    alpha /= 2.0
                    continue
                    AcceptedConstr = max(0.999 * p.contol, currConstr)
                    isConstrAccepted = True
                currConstr = isObjFunAccepted or p.getMaxResidual(x_new)
                if currConstr > p.contol and (currConstr > 1.3 * AcceptedConstr or currConstr > allowedConstr_start + alpha * C1_constr):
                    isObjFunAccepted = True
                    alpha = min(1.0, 2.0 * alpha)
                    break
                f_new = p.f(x_new)
                if f_new > f0 + alpha * C1_objFun:
                    alpha /= 2.0
                    f_prev = f_new
                    continue
                else:
                    isObjFunAccepted = True
                    break

        if p.debug and alpha < alpha_min:
            p.warn('alpha less alpha_min')
        if alpha == 1.0:
            K = 1.5
            f_prev = f0
            allowedConstr = allowedConstr_start
            for i in range(p.maxLineSearch):
                x_new = x0 + K * direction * alpha
                f_new = p.f(x_new)
                if f_new > f_prev or p.getMaxResidual(x_new) > allowedConstr:
                    break
                else:
                    allowedConstr = max(0.99 * p.contol, min(allowedConstr, currConstr))
                    alpha *= K
                    f_new = f_prev

        destination = x0 + direction * alpha
    else:
        p.error('unknown line-search optimizer')
    return (result, destination)