# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\UkrOpt\interalgT.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import isnan, take, any, all, logical_or, logical_and, logical_not, atleast_1d, where, asarray, argmin, argsort, isfinite
import numpy as np
from bisect import bisect_right
from FuncDesigner.Interval import adjust_lx_WithDiscreteDomain, adjust_ux_WithDiscreteDomain
try:
    from bottleneck import nanmin
except ImportError:
    from numpy import nanmin

def adjustDiscreteVarBounds(y, e, p):
    for i in p._discreteVarsNumList:
        v = p._freeVarsList[i]
        adjust_lx_WithDiscreteDomain(y[:, i], v)
        adjust_ux_WithDiscreteDomain(e[:, i], v)

    ind = any(y > e, 1)
    if any(ind):
        ind = where(logical_not(ind))[0]
        s = ind.size
        y = take(y, ind, axis=0, out=y[:s])
        e = take(e, ind, axis=0, out=e[:s])
    return (
     y, e)


def func7(y, e, o, a, _s, indT, nlhc, residual):
    r10 = logical_and(all(isnan(o), 1), all(isnan(a), 1))
    if any(r10):
        j = where(logical_not(r10))[0]
        lj = j.size
        y = take(y, j, axis=0, out=y[:lj])
        e = take(e, j, axis=0, out=e[:lj])
        o = take(o, j, axis=0, out=o[:lj])
        a = take(a, j, axis=0, out=a[:lj])
        _s = _s[j]
        if indT is not None:
            indT = indT[j]
        if nlhc is not None:
            nlhc = take(nlhc, j, axis=0, out=nlhc[:lj])
        if residual is not None:
            residual = take(residual, j, axis=0, out=residual[:lj])
    return (
     y, e, o, a, _s, indT, nlhc, residual)


def func9(an, fo, g, p):
    if p.probType in ('NLSP', 'SNLE') and p.maxSolutions != 1:
        mino = atleast_1d([ node.key for node in an ])
        ind = mino > 0
        if not any(ind):
            return (an, g)
        g = nanmin((g, nanmin(mino[ind])))
        ind2 = where(logical_not(ind))[0]
        an = asarray(an[ind2])
        return (an, g)
    elif p.solver.dataHandling == 'sorted':
        mino = [ node.key for node in an ]
        ind = bisect_right(mino, fo)
        if ind == len(mino):
            return (an, g)
        g = nanmin((g, nanmin(atleast_1d(mino[ind]))))
        return (an[:ind], g)
    else:
        if p.solver.dataHandling == 'raw':
            mino = [ node.key for node in an ]
            mino = atleast_1d(mino)
            r10 = mino > fo
            if not any(r10):
                return (an, g)
            ind = where(r10)[0]
            g = nanmin((g, nanmin(atleast_1d(mino)[ind])))
            an = asarray(an)
            ind2 = where(logical_not(r10))[0]
            an = asarray(an[ind2])
            return (an, g)
            return (
             an, g)
        assert 0, 'incorrect nodes remove approach'


def func5(an, nn, g, p):
    m = len(an)
    if m <= nn:
        return (an, g)
    mino = [ node.key for node in an ]
    if nn == 1:
        ind = argmin(mino)
        assert ind in (0, 1), 'error in interalg engine'
        g = nanmin((mino[1 - ind], g))
        an = atleast_1d([an[ind]])
    elif m > nn:
        if p.solver.dataHandling == 'raw':
            ind = argsort(mino)
            th = mino[ind[nn]]
            ind2 = where(mino < th)[0]
            g = nanmin((th, g))
            an = an[ind2]
        else:
            g = nanmin((mino[nn], g))
            an = an[:nn]
    return (
     an, g)


def func4(p, y, e, o, a, fo, tnlhf_curr=None):
    if fo is None and tnlhf_curr is None:
        return False
    else:
        if y.size == 0:
            return False
        cs = (y + e) / 2
        n = y.shape[1]
        if tnlhf_curr is not None:
            tnlh_modL = tnlhf_curr[:, 0:n]
            ind = logical_not(isfinite(tnlh_modL))
        else:
            s = o[:, 0:n]
            ind = logical_or(s > fo, isnan(s))
        indT = any(ind, 1)
        if any(ind):
            y[ind] = cs[ind]
            if p.probType != 'MOP':
                a[:, 0:n][ind] = a[:, n:2 * n][ind]
                o[:, 0:n][ind] = o[:, n:2 * n][ind]
            if tnlhf_curr is not None:
                tnlhf_curr[:, 0:n][ind] = tnlhf_curr[:, n:2 * n][ind]
        if tnlhf_curr is not None:
            tnlh_modU = tnlhf_curr[:, n:2 * n]
            ind = logical_not(isfinite(tnlh_modU))
        else:
            q = o[:, n:2 * n]
            ind = logical_or(q > fo, isnan(q))
        indT = logical_or(any(ind, 1), indT)
        if any(ind):
            e[ind] = cs[ind].copy()
            if p.probType != 'MOP':
                a[:, n:2 * n][ind] = a[:, 0:n][ind]
                o[:, n:2 * n][ind] = o[:, 0:n][ind]
            if tnlhf_curr is not None:
                tnlhf_curr[:, n:2 * n][ind] = tnlhf_curr[:, 0:n][ind]
        return indT


def TruncateByCuttingPlane(f, f_val, y, e, lb, ub, point, gradient):
    gradient_squared_norm = np.sum(gradient ** 2)
    gradient_multiplier = gradient / gradient_squared_norm
    delta_l = gradient_multiplier * (f_val - lb)
    H = point + delta_l


def truncateByPlane(y, e, indT, A, b):
    ind_trunc = True
    assert np.asarray(b).size <= 1, 'unimplemented yet'
    m, n = y.shape
    if m == 0:
        if not e.size == 0:
            raise AssertionError('bug in interalg engine')
            return (
             y, e, indT, ind_trunc)
        ind_positive = where(A > 0)[0]
        ind_negative = where(A < 0)[0]
        A1 = A[ind_positive]
        S1 = A1 * y[:, ind_positive]
        A2 = A[ind_negative]
        S2 = A2 * e[:, ind_negative]
        s1, s2 = np.sum(S1, 1), np.sum(S2, 1)
        S = s1 + s2
        if ind_positive.size != 0:
            S1_ = b - S.reshape(-1, 1) + S1
            Alt_ub = S1_ / A1
            for _i, i in enumerate(ind_positive):
                alt_ub = Alt_ub[:, _i]
                ind = e[:, i] > alt_ub
                e[(ind, i)] = alt_ub[ind]
                indT[ind] = True

        if ind_negative.size != 0:
            S2_ = b - S.reshape(-1, 1) + S2
            Alt_lb = S2_ / A2
            for _i, i in enumerate(ind_negative):
                alt_lb = Alt_lb[:, _i]
                ind = y[:, i] < alt_lb
                y[(ind, i)] = alt_lb[ind]
                indT[ind] = True

        ind = np.all(e >= y, 1)
        ind_trunc = np.all(ind) or where(ind)[0]
        lj = ind_trunc.size
        y = take(y, ind_trunc, axis=0, out=y[:lj])
        e = take(e, ind_trunc, axis=0, out=e[:lj])
        indT = indT[ind_trunc]
    return (y, e, indT, ind_trunc)


def truncateByPlane2(cs, centerValues, y, e, indT, gradient, fo, p):
    ind_trunc = True
    assert np.asarray(fo).size <= 1, 'unimplemented yet'
    m, n = y.shape
    if m == 0:
        if not e.size == 0:
            raise AssertionError('bug in interalg engine')
            return (
             y, e, indT, ind_trunc)
        oovarsIndDict = p._oovarsIndDict
        ind = np.array([ oovarsIndDict[oov][0] for oov in gradient.keys() ])
        y2, e2 = y[:, ind], e[:, ind]
        A = np.vstack([ np.asarray(elem).reshape(1, -1) for elem in gradient.values() ]).T
        cs = 0.5 * (y2 + e2)
        b = np.sum(A * cs, 1) - centerValues.view(np.ndarray) + fo
        A_positive = where(A > 0, A, 0)
        A_negative = where(A < 0, A, 0)
        S1 = A_positive * y2
        S2 = A_negative * e2
        s1, s2 = np.sum(S1, 1), np.sum(S2, 1)
        S = s1 + s2
        alt_fo1 = where(A_positive != 0, (b.reshape(-1, 1) - S.reshape(-1, 1) + S1) / A_positive, np.inf)
        ind1 = logical_and(e2 > alt_fo1, A_positive != 0)
        e2[ind1] = alt_fo1[ind1]
        alt_fo2 = where(A_negative != 0, (b.reshape(-1, 1) - S.reshape(-1, 1) + S2) / A_negative, -np.inf)
        ind2 = logical_and(y2 < alt_fo2, A_negative != 0)
        y2[ind2] = alt_fo2[ind2]
        y[:, ind], e[:, ind] = y2, e2
        indT[np.any(ind1, 1)] = True
        indT[np.any(ind2, 1)] = True
        ind = np.all(e >= y, 1)
        ind_trunc = np.all(ind) or where(ind)[0]
        lj = ind_trunc.size
        y = take(y, ind_trunc, axis=0, out=y[:lj])
        e = take(e, ind_trunc, axis=0, out=e[:lj])
        indT = indT[ind_trunc]
    return (
     y, e, indT, ind_trunc)