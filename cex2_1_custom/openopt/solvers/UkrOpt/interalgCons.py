# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\UkrOpt\interalgCons.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import empty, where, logical_and, logical_not, take, logical_or, isnan, zeros, log2, isfinite, int8, int16, int32, int64, isinf, asfarray, any, asarray
from interalgLLR import func8, func10
from interalgT import adjustDiscreteVarBounds, truncateByPlane
try:
    from bottleneck import nanmin, nanmax
except ImportError:
    from numpy import nanmin, nanmax

def processConstraints(C0, y, e, _s, p, dataType):
    n = p.n
    m = y.shape[0]
    r15 = empty(m, bool)
    nlh = zeros((m, 2 * n))
    r15.fill(True)
    DefiniteRange = True
    if len(p._discreteVarsNumList):
        y, e = adjustDiscreteVarBounds(y, e, p)
    for f, r16, r17, tol in C0:
        if p.solver.dataHandling == 'sorted':
            tol = 0
        ip = func10(y, e, p._freeVarsList)
        ip.dictOfFixedFuncs = p.dictOfFixedFuncs
        o, a, definiteRange = func8(ip, f, dataType)
        DefiniteRange = logical_and(DefiniteRange, definiteRange)
        o, a = o.reshape(2 * n, m).T, a.reshape(2 * n, m).T
        lf1, lf2, uf1, uf2 = (
         o[:, 0:n], o[:, n:2 * n], a[:, 0:n], a[:, n:2 * n])
        o_ = where(logical_or(lf1 > lf2, isnan(lf1)), lf2, lf1)
        a_ = where(logical_or(uf1 > uf2, isnan(uf2)), uf1, uf2)
        om, am = nanmin(o_, 1), nanmax(a_, 1)
        ind = logical_and(am >= r16, om <= r17)
        r15 = logical_and(r15, ind)
        aor20 = a - o
        if dataType in [int8, int16, int32, int64, int]:
            aor20 = asfarray(aor20)
        a_t, o_t = a.copy(), o.copy()
        if dataType in [int8, int16, int32, int64, int]:
            a_t, o_t = asfarray(a_t), asfarray(o_t)
        if r16 == r17:
            val = r17
            a_t[a_t > val + tol] = val + tol
            o_t[o_t < val - tol] = val - tol
            r24 = a_t - o_t
            tmp = r24 / aor20
            tmp[logical_or(isinf(o), isinf(a))] = 1e-10
            tmp[r24 == 0.0] = 1.0
            tmp[tmp < 1e-300] = 1e-300
            tmp[val > a] = 0
            tmp[val < o] = 0
        elif isfinite(r16) and not isfinite(r17):
            tmp = (a - r16 + tol) / aor20
            tmp[logical_and(isinf(o), logical_not(isinf(a)))] = 1e-10
            tmp[isinf(a)] = 0.9999999999
            tmp[tmp < 1e-300] = 1e-300
            tmp[tmp > 1.0] = 1.0
            tmp[r16 > a] = 0
            tmp[r16 <= o] = 1
        elif isfinite(r17) and not isfinite(r16):
            tmp = (r17 - a + tol) / aor20
            tmp[isinf(o)] = 0.9999999999
            tmp[logical_and(isinf(a), logical_not(isinf(o)))] = 1e-10
            tmp[tmp < 1e-300] = 1e-300
            tmp[tmp > 1.0] = 1.0
            tmp[r17 < o] = 0
            tmp[r17 >= a] = 1
        else:
            p.err('this part of interalg code is unimplemented for double-box-bound constraints yet')
        nlh -= log2(tmp)

    ind = where(r15)[0]
    lj = ind.size
    if lj != m:
        y = take(y, ind, axis=0, out=y[:lj])
        e = take(e, ind, axis=0, out=e[:lj])
        nlh = take(nlh, ind, axis=0, out=nlh[:lj])
        _s = _s[ind]
    return (
     y, e, nlh, None, DefiniteRange, None, _s)


def processConstraints2(C0, y, e, _s, p, dataType):
    n = p.n
    m = y.shape[0]
    indT = empty(m, bool)
    indT.fill(False)
    for i in range(p.nb):
        y, e, indT, ind_trunc = truncateByPlane(y, e, indT, p.A[i], p.b[i])
        if ind_trunc is not True:
            _s = _s[ind_trunc]

    for i in range(p.nbeq):
        y, e, indT, ind_trunc = truncateByPlane(y, e, indT, p.Aeq[i], p.beq[i])
        if ind_trunc is not True:
            _s = _s[ind_trunc]
        y, e, indT, ind_trunc = truncateByPlane(y, e, indT, -p.Aeq[i], -p.beq[i])
        if ind_trunc is not True:
            _s = _s[ind_trunc]

    DefiniteRange = True
    if len(p._discreteVarsNumList):
        adjustDiscreteVarBounds(y, e, p)
    m = y.shape[0]
    nlh = zeros((m, 2 * n))
    nlh_0 = zeros(m)
    for c, f, lb, ub, tol in C0:
        m = y.shape[0]
        if m == 0:
            return (y.reshape(0, n), e.reshape(0, n), nlh.reshape(0, 2 * n), None, True, False, _s)
        assert nlh.shape[0] == y.shape[0]
        T0, res, DefiniteRange2 = c.nlh(y, e, p, dataType)
        DefiniteRange = logical_and(DefiniteRange, DefiniteRange2)
        assert T0.ndim <= 1, 'unimplemented yet'
        nlh_0 += T0
        assert nlh.shape[0] == m
        if len(res):
            for j, v in enumerate(p._freeVarsList):
                tmp = res.get(v, None)
                if tmp is None:
                    continue
                else:
                    nlh[:, n + j] += tmp[:, tmp.shape[1] / 2:].flatten() - T0
                    nlh[:, j] += tmp[:, :tmp.shape[1] / 2].flatten() - T0

        assert nlh.shape[0] == m
        ind = where(logical_and(any(isfinite(nlh), 1), isfinite(nlh_0)))[0]
        lj = ind.size
        if lj != m:
            y = take(y, ind, axis=0, out=y[:lj])
            e = take(e, ind, axis=0, out=e[:lj])
            nlh = take(nlh, ind, axis=0, out=nlh[:lj])
            nlh_0 = nlh_0[ind]
            indT = indT[ind]
            _s = _s[ind]
            if asarray(DefiniteRange).size != 1:
                DefiniteRange = take(DefiniteRange, ind, axis=0, out=DefiniteRange[:lj])
        assert nlh.shape[0] == y.shape[0]
        ind = logical_not(isfinite(nlh))
        if any(ind):
            indT[any(ind, 1)] = True
            ind_l, ind_u = ind[:, :ind.shape[1] / 2], ind[:, ind.shape[1] / 2:]
            tmp_l, tmp_u = 0.5 * (y[ind_l] + e[ind_l]), 0.5 * (y[ind_u] + e[ind_u])
            y[ind_l], e[ind_u] = tmp_l, tmp_u
            if len(p._discreteVarsNumList):
                if tmp_l.ndim > 1:
                    adjustDiscreteVarBounds(tmp_l, tmp_u, p)
                else:
                    adjustDiscreteVarBounds(y, e, p)
            nlh_l, nlh_u = nlh[:, nlh.shape[1] / 2:], nlh[:, :nlh.shape[1] / 2]
            nlh_l[ind_u], nlh_u[ind_l] = nlh_u[ind_u].copy(), nlh_l[ind_l].copy()

    nlh += nlh_0.reshape(-1, 1)
    residual = None
    return (
     y, e, nlh, residual, DefiniteRange, indT, _s)