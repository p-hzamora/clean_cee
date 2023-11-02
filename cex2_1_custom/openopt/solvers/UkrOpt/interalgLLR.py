# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\UkrOpt\interalgLLR.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import tile, isnan, array, atleast_1d, asarray, logical_and, all, logical_or, any, nan, isinf, arange, vstack, inf, where, logical_not, take, abs, hstack, empty, prod, int16, int32, int64, log2, searchsorted, cumprod
import numpy as np
from FuncDesigner import oopoint
from FuncDesigner.multiarray import multiarray
from interalgT import *
try:
    from bottleneck import nanargmin, nanmin, nanargmax, nanmax
except ImportError:
    from numpy import nanmin, nanargmin, nanargmax, nanmax

def func82(y, e, vv, f, dataType, p):
    domain = oopoint([ (v, (y[:, i], e[:, i])) for i, v in enumerate(vv) ], skipArrayCast=True, isMultiPoint=True)
    domain.dictOfFixedFuncs = p.dictOfFixedFuncs
    r, r0 = f.iqg(domain, dataType)
    dep = f._getDep()
    o_l, o_u, a_l, a_u = ([], [], [], [])
    definiteRange = r0.definiteRange
    for v in vv:
        if v in dep:
            o_l.append(r[v][0].lb)
            o_u.append(r[v][1].lb)
            a_l.append(r[v][0].ub)
            a_u.append(r[v][1].ub)
            definiteRange = logical_and(definiteRange, r[v][0].definiteRange)
            definiteRange = logical_and(definiteRange, r[v][1].definiteRange)
        else:
            o_l.append(r0.lb)
            o_u.append(r0.lb)
            a_l.append(r0.ub)
            a_u.append(r0.ub)

    o, a = hstack(o_l + o_u), hstack(a_l + a_u)
    return (o, a, definiteRange)


def func10(y, e, vv):
    m, n = y.shape
    LB = [ [] for i in range(n) ]
    UB = [ [] for i in range(n) ]
    r4 = (y + e) / 2
    for i in range(n):
        t1, t2 = tile(y[:, i], 2 * n), tile(e[:, i], 2 * n)
        t1[((n + i) * m):((n + i + 1) * m)] = t2[(i * m):((i + 1) * m)] = r4[:, i]
        LB[i], UB[i] = t1, t2

    domain = dict([ (v, (LB[i], UB[i])) for i, v in enumerate(vv) ])
    domain = oopoint(domain, skipArrayCast=True)
    domain.isMultiPoint = True
    return domain


def func8(domain, func, dataType):
    TMP = func.interval(domain, dataType)
    return (
     asarray(TMP.lb, dtype=dataType), asarray(TMP.ub, dtype=dataType), TMP.definiteRange)


def getr4Values(vv, y, e, tnlh, func, C, contol, dataType, p, fo=inf):
    n = y.shape[1]
    if tnlh is None:
        wr4 = (y + e) / 2
        adjustr4WithDiscreteVariables(wr4, p)
        cs = dict([ (oovar, asarray(wr4[:, i], dataType)) for i, oovar in enumerate(vv) ])
    else:
        tnlh = tnlh.copy()
        tnlh[atleast_1d(tnlh < 1e-300)] = 1e-300
        tnlh[atleast_1d(isnan(tnlh))] = inf
        tnlh_l_inv, tnlh_u_inv = 1.0 / tnlh[:, :n], 1.0 / tnlh[:, n:]
        wr4 = (y * tnlh_l_inv + e * tnlh_u_inv) / (tnlh_l_inv + tnlh_u_inv)
        ind = tnlh_l_inv == tnlh_u_inv
        wr4[ind] = (y[ind] + e[ind]) / 2
        adjustr4WithDiscreteVariables(wr4, p)
        cs = dict([ (oovar, asarray(wr4[:, i], dataType)) for i, oovar in enumerate(vv) ])
    cs = oopoint(cs, skipArrayCast=True)
    cs.isMultiPoint = True
    cs.update(p.dictOfFixedFuncs)
    m = y.shape[0]
    if len(C) != 0:
        r15 = empty(m, bool)
        r15.fill(True)
        for _c, f, r16, r17 in C:
            c = f(cs)
            ind = logical_and(c >= r16, c <= r17)
            r15 = logical_and(r15, ind)

    else:
        r15 = True
    isMOP = p.probType == 'MOP'
    if not any(r15):
        F = empty(m, dataType)
        F.fill(2147483646 if dataType in (int32, int64, int) else nan)
        if isMOP:
            FF = [ F for k in range(p.nf) ]
    elif all(r15):
        if isMOP:
            FF = [ fun(cs) for fun in func ]
        else:
            F = func(cs)
    elif isMOP:
        FF = []
        for fun in func:
            tmp = fun(cs)
            F = empty(m, dataType)
            F.fill(2147483633 if dataType in (int32, int64, int) else nan)
            F[r15] = tmp[r15]
            FF.append(F)

    else:
        tmp = asarray(func(cs), dataType)
        F = empty(m, dataType)
        F.fill(2147483633 if dataType in (int16, int32, int64, int) else nan)
        F[r15] = tmp[r15]
    if isMOP:
        return (array(FF).T.reshape(m, len(func)).tolist(), wr4.tolist())
    else:
        return (
         atleast_1d(F), wr4)
        return


def adjustr4WithDiscreteVariables(wr4, p):
    for i in p._discreteVarsNumList:
        v = p._freeVarsList[i]
        if v.domain is bool or v.domain is 'bool':
            wr4[:, i] = where(wr4[:, i] < 0.5, 0, 1)
        else:
            tmp = wr4[:, i]
            d = v.domain
            ind = searchsorted(d, tmp, side='left')
            ind2 = searchsorted(d, tmp, side='right')
            ind3 = where(ind != ind2)[0]
            Tmp = tmp[ind3].copy()
            ind[ind == d.size] -= 1
            ind[ind == 1] = 0
            ind2[ind2 == d.size] -= 1
            ind2[ind2 == 0] = 1
            tmp1 = asarray(d[ind], p.solver.dataType)
            tmp2 = asarray(d[ind2], p.solver.dataType)
            if Tmp.size != 0:
                if str(tmp1.dtype).startswith('int'):
                    Tmp = asarray(Tmp, p.solver.dataType)
                tmp2[ind3] = Tmp.copy()
                tmp1[ind3] = Tmp.copy()
            tmp = where(abs(tmp - tmp1) < abs(tmp - tmp2), tmp1, tmp2)
            wr4[:, i] = tmp


def r2(PointVals, PointCoords, dataType):
    r23 = nanargmin(PointVals)
    if isnan(r23):
        r23 = 0
    r7 = array(PointCoords[r23], dtype=dataType)
    r8 = atleast_1d(PointVals)[r23]
    return (r7, r8)


def func3(an, maxActiveNodes, dataHandling):
    m = len(an)
    if m <= maxActiveNodes:
        return (an, array([], object))
    else:
        an1, _in = an[:maxActiveNodes], an[maxActiveNodes:]
        if getattr(an1[0], 'tnlh_curr_best', None) is not None:
            tnlh_curr_best_values = asarray([ node.tnlh_curr_best for node in an1 ])
            tmp = 2 ** (-tnlh_curr_best_values)
            Tmp = -cumprod(1.0 - tmp)
            ind2 = searchsorted(Tmp, -0.05)
            ind = ind2
            n = an[0].y.size
            M = max((5, int(maxActiveNodes / n), ind))
            M = ind
            if M == 0:
                M = 1
            tmp1, tmp2 = an1[:M], an1[M:]
            an1 = tmp1
            _in = hstack((tmp2, _in))
        cond_min_uf = 0 and dataHandling == 'raw' and hasattr(an[0], 'key')
        if cond_min_uf:
            num_nlh = min((max((1, int(0.8 * maxActiveNodes))), an1.size))
            num_uf = min((maxActiveNodes - num_nlh, int(maxActiveNodes / 2)))
            if num_uf < 15:
                num_uf = 15
            Ind = np.argsort([ node.key for node in _in ])
            min_uf_nodes = _in[Ind[:num_uf]]
            _in = _in[Ind[num_uf:]]
            an1 = np.hstack((an1, min_uf_nodes))
        return (
         an1, _in)


def func1(tnlhf, tnlhf_curr, residual, y, e, o, a, _s_prev, p, indT):
    m, n = y.shape
    w = arange(m)
    if p.probType == 'IP':
        oc_modL, oc_modU = o[:, :n], o[:, n:]
        ac_modL, ac_modU = a[:, :n], a[:, n:]
        mino = where(oc_modL < oc_modU, oc_modL, oc_modU)
        maxa = where(ac_modL < ac_modU, ac_modU, ac_modL)
        tmp = a[:, 0:n] - o[:, 0:n] + a[:, n:] - o[:, n:]
        t = nanargmin(tmp, 1)
        d = 0.5 * tmp[(w, t)]
        ind = 2 ** (1.0 / n) * d >= _s_prev
        _s = nanmin(maxa - mino, 1)
        indD = logical_not(ind)
        indD = ind
        indD = None
    elif p.solver.dataHandling == 'sorted':
        _s = func13(o, a)
        t = nanargmin(a, 1) % n
        d = nanmax([a[(w, t)] - o[(w, t)],
         a[(w, n + t)] - o[(w, n + t)]], 0)
        ind = d >= _s_prev / 2 ** (1e-12 / n)
        indD = empty(m, bool)
        indD.fill(True)
    elif p.solver.dataHandling == 'raw':
        if p.probType == 'MOP':
            t = p._t[:m]
            p._t = p._t[m:]
            d = _s = p.__s[:m]
            p.__s = p.__s[m:]
        else:
            T = tnlhf_curr
            tnlh_curr_1, tnlh_curr_2 = T[:, 0:n], T[:, n:]
            TNHL_curr_min = where(logical_or(tnlh_curr_1 < tnlh_curr_2, isnan(tnlh_curr_2)), tnlh_curr_1, tnlh_curr_2)
            t = nanargmin(TNHL_curr_min, 1)
            T = tnlhf
            d = nanmin(vstack([T[(w, t)], T[(w, n + t)]]), 0)
            _s = d
        if any(_s_prev < d):
            pass
        ind = _s_prev <= d + 1.0 / n
        indQ = d >= _s_prev - 1.0 / n
        indD = logical_or(indQ, logical_not(indT))
    else:
        assert 0
    if any(ind):
        r10 = where(ind)[0]
        bs = e[r10] - y[r10]
        t[r10] = nanargmax(bs, 1)
    return (t, _s, indD)


def func13(o, a):
    m, n = o.shape
    n /= 2
    L1, L2, U1, U2 = (
     o[:, :n], o[:, n:], a[:, :n], a[:, n:])
    U = where(logical_or(U1 < U2, isnan(U1)), U2, U1)
    L = where(logical_or(L2 < L1, isnan(L1)), L2, L1)
    return nanmax(U - L, 1)


def func2(y, e, t, vv, tnlhf_curr):
    new_y, new_e = y.copy(), e.copy()
    m, n = y.shape
    w = arange(m)
    th = (new_y[(w, t)] + new_e[(w, t)]) / 2
    BoolVars = [ v.domain is bool or v.domain is 'bool' for v in vv ]
    if not str(th.dtype).startswith('float') and any(BoolVars):
        indBool = where(BoolVars)[0]
        if len(indBool) != n:
            boolCoords = where([ t[j] in indBool for j in range(m) ])[0]
            new_y[(w, t)] = th
            new_e[(w, t)] = th
            new_y[(boolCoords, t[boolCoords])] = 1
            new_e[(boolCoords, t[boolCoords])] = 0
        else:
            new_y[(w, t)] = 1
            new_e[(w, t)] = 0
    else:
        new_y[(w, t)] = th
        new_e[(w, t)] = th
    new_y = vstack((y, new_y))
    new_e = vstack((new_e, e))
    if tnlhf_curr is not None:
        tnlhf_curr_local = hstack((tnlhf_curr[(w, t)], tnlhf_curr[(w, n + t)]))
    else:
        tnlhf_curr_local = None
    return (
     new_y, new_e, tnlhf_curr_local)


def func12(an, maxActiveNodes, p, Solutions, vv, varTols, fo):
    solutions, r6 = Solutions.solutions, Solutions.coords
    if len(an) == 0:
        return (array([]), array([]), array([]), array([]))
    else:
        _in = an
        if r6.size != 0:
            r11, r12 = r6 - varTols, r6 + varTols
        y, e, S = [], [], []
        Tnlhf_curr_local = []
        n = p.n
        N = 0
        maxSolutions = p.maxSolutions
        while True:
            an1Candidates, _in = func3(_in, maxActiveNodes, p.solver.dataHandling)
            yc, ec, oc, ac, SIc = (
             asarray([ t.y for t in an1Candidates ]),
             asarray([ t.e for t in an1Candidates ]),
             asarray([ t.o for t in an1Candidates ]),
             asarray([ t.a for t in an1Candidates ]),
             asarray([ t._s for t in an1Candidates ]))
            if p.probType == 'MOP':
                tnlhf_curr = asarray([ t.tnlh_all for t in an1Candidates ])
                tnlhf = None
            elif p.solver.dataHandling == 'raw':
                tnlhf = asarray([ t.tnlhf for t in an1Candidates ])
                tnlhf_curr = asarray([ t.tnlh_curr for t in an1Candidates ])
            else:
                tnlhf, tnlhf_curr = (None, None)
            if p.probType != 'IP':
                indtc = asarray([ t.indtc for t in an1Candidates ])
                residual = None
                indT = func4(p, yc, ec, oc, ac, fo, tnlhf_curr)
                if indtc[0] is not None:
                    indT = logical_or(indT, indtc)
            else:
                residual = None
                indT = None
            t, _s, indD = func1(tnlhf, tnlhf_curr, residual, yc, ec, oc, ac, SIc, p, indT)
            new = 0
            nn = 0
            if new and p.probType in ('MOP', 'SNLE', 'NLSP', 'GLP', 'NLP', 'MINLP') and p.maxSolutions == 1:
                arr = tnlhf_curr if p.solver.dataHandling == 'raw' else oc
                M = arr.shape[0]
                w = arange(M)
                Midles = 0.5 * (yc[(w, t)] + ec[(w, t)])
                arr_1, arr2 = arr[(w, t)], arr[(w, n + t)]
                Arr = hstack((arr_1, arr2))
                ind = np.argsort(Arr)
                Ind = set(ind[:maxActiveNodes])
                tag_all, tag_1, tag_2 = [], [], []
                sn = []
                for i in range(M):
                    cond1, cond2 = i in Ind, i + M in Ind
                    if cond1:
                        if cond2:
                            tag_all.append(i)
                        else:
                            tag_1.append(i)
                    elif cond2:
                        tag_2.append(i)
                    else:
                        sn.append(an1Candidates[i])

                list_lx, list_ux = [], []
                _s_new = []
                updateTC = an1Candidates[0].indtc is not None
                isRaw = p.solver.dataHandling == 'raw'
                for i in tag_1:
                    node = an1Candidates[i]
                    I = t[i]
                    node.key = node.o[n + I]
                    node._s = _s[i]
                    if isRaw:
                        node.tnlh_curr[I] = node.tnlh_curr[n + I]
                        node.tnlh_curr_best = nanmin(node.tnlh_curr)
                    lx, ux = yc[i], ec[i]
                    if nn:
                        node.o[I], node.a[I] = node.o[n + I], node.a[n + I]
                        node.o[node.o < node.o[n + I]], node.a[node.a > node.a[n + I]] = node.o[n + I], node.a[n + I]
                    else:
                        node.o[n + I], node.a[n + I] = node.o[I], node.a[I]
                        node.o[node.o < node.o[I]], node.a[node.a > node.a[I]] = node.o[I], node.a[I]
                    for Attr in ('nlhf', 'nlhc', 'tnlhf', 'tnlh_curr', 'tnlh_all'):
                        r = getattr(node, Attr, None)
                        if r is not None:
                            if nn:
                                r[I] = r[n + I]
                            else:
                                r[n + I] = r[I]

                    mx = ux.copy()
                    mx[I] = Midles[i]
                    list_lx.append(lx)
                    list_ux.append(mx)
                    node.y = lx.copy()
                    node.y[I] = Midles[i]
                    if updateTC:
                        node.indtc = True
                    _s_new.append(node._s)
                    sn.append(node)

                for i in tag_2:
                    node = an1Candidates[i]
                    I = t[i]
                    node.key = node.o[I]
                    node._s = _s[i]
                    if isRaw:
                        node.tnlh_curr[n + I] = node.tnlh_curr[I]
                        node.tnlh_curr_best = nanmin(node.tnlh_curr)
                    lx, ux = yc[i], ec[i]
                    if nn:
                        node.o[n + I], node.a[n + I] = node.o[I], node.a[I]
                        node.o[node.o < node.o[I]], node.a[node.a > node.a[I]] = node.o[I], node.a[I]
                    else:
                        node.o[I], node.a[I] = node.o[n + I], node.a[n + I]
                        node.o[node.o < node.o[n + I]], node.a[node.a > node.a[n + I]] = node.o[n + I], node.a[n + I]
                    for Attr in ('nlhf', 'nlhc', 'tnlhf', 'tnlh_curr', 'tnlh_all'):
                        r = getattr(node, Attr, None)
                        if r is not None:
                            if nn:
                                r[n + I] = r[I]
                            else:
                                r[I] = r[n + I]

                    mx = lx.copy()
                    mx[I] = Midles[i]
                    list_lx.append(mx)
                    list_ux.append(ux)
                    node.e = ux.copy()
                    node.e[I] = Midles[i]
                    if updateTC:
                        node.indtc = True
                    _s_new.append(node._s)
                    sn.append(node)

                for i in tag_all:
                    node = an1Candidates[i]
                    I = t[i]
                    lx, ux = yc[i], ec[i]
                    mx = ux.copy()
                    mx[I] = Midles[i]
                    list_lx.append(lx)
                    list_ux.append(mx)
                    mx = lx.copy()
                    mx[I] = Midles[i]
                    list_lx.append(mx)
                    list_ux.append(ux)
                    _s_new.append(_s[i])
                    _s_new.append(_s[i])

                _in = sn + _in.tolist()
                if p.solver.dataHandling == 'sorted':
                    _in.sort(key=(lambda obj: obj.key))
                else:
                    _in.sort(key=(lambda obj: obj.tnlh_curr_best))
                NEW_lx, NEW_ux, NEW__in, NEW__s = (
                 vstack(list_lx), vstack(list_ux), array(_in), hstack(_s_new))
                return (
                 NEW_lx, NEW_ux, NEW__in, NEW__s)
            NewD = 1
            if NewD and indD is not None:
                s4d = _s[indD]
                sf = _s[logical_not(indD)]
                _s = hstack((s4d, s4d, sf))
                yf, ef = yc[logical_not(indD)], ec[logical_not(indD)]
                yc, ec = yc[indD], ec[indD]
                t = t[indD]
            else:
                _s = tile(_s, 2)
            yc, ec, tnlhf_curr_local = func2(yc, ec, t, vv, tnlhf_curr)
            if NewD and indD is not None:
                yc = vstack((yc, yf))
                ec = vstack((ec, ef))
            if maxSolutions == 1 or len(solutions) == 0:
                y, e, Tnlhf_curr_local = yc, ec, tnlhf_curr_local
                break
            for i in range(len(solutions)):
                ind = logical_and(all(yc >= r11[i], 1), all(ec <= r12[i], 1))
                if any(ind):
                    j = where(logical_not(ind))[0]
                    lj = j.size
                    yc = take(yc, j, axis=0, out=yc[:lj])
                    ec = take(ec, j, axis=0, out=ec[:lj])
                    _s = _s[j]
                    if tnlhf_curr_local is not None:
                        tnlhf_curr_local = tnlhf_curr_local[j]

            y.append(yc)
            e.append(ec)
            S.append(_s)
            N += yc.shape[0]
            if len(_in) == 0 or N >= maxActiveNodes:
                y, e, _s = vstack(y), vstack(e), hstack(S)
                break

        return (
         y, e, _in, _s)


Fields = [
 'key', 'y', 'e', 'nlhf', 'nlhc', 'indtc', 'residual', 'o', 'a', '_s']
MOP_Fields = ['y', 'e', 'nlhf', 'nlhc', 'indtc', 'residual', 'o', 'a', '_s']
IP_fields = [
 'key', 'minres', 'minres_ind', 'complementary_minres', 'y', 'e', 'o', 'a', 
 '_s', 'F', 'volume', 'volumeResidual']

def func11(y, e, nlhc, indTC, residual, o, a, _s, p):
    m, n = y.shape
    if p.probType == 'IP':
        w = arange(m)
        ind = nanargmin(a[:, 0:n] - o[:, 0:n] + a[:, n:] - o[:, n:], 1)
        sup_inf_diff = 0.5 * (a[(w, ind)] - o[(w, ind)] + a[(w, n + ind)] - o[(w, n + ind)])
        diffao = a - o
        minres_ind = nanargmin(diffao, 1)
        minres = diffao[(w, minres_ind)]
        complementary_minres = diffao[(w, where(minres_ind < n, minres_ind + n, minres_ind - n))]
        volume = prod(e - y, 1)
        volumeResidual = volume * sup_inf_diff
        F = 0.25 * (a[(w, ind)] + o[(w, ind)] + a[(w, n + ind)] + o[(w, n + ind)])
        return [ si(IP_fields, sup_inf_diff[i], minres[i], minres_ind[i], complementary_minres[i], y[i], e[i], o[i], a[i], _s[i], F[i], volume[i], volumeResidual[i]) for i in range(m) ]
    else:
        residual = None
        tmp = asarray(a) - asarray(o)
        tmp[tmp < 1e-300] = 1e-300
        nlhf = log2(tmp)
        if nlhf.ndim == 3:
            nlhf = nlhf.sum(axis=1)
        if p.probType == 'MOP':
            return [ si(MOP_Fields, y[i], e[i], nlhf[i], nlhc[i] if nlhc is not None else None, indTC[i] if indTC is not None else None, residual[i] if residual is not None else None, [ o[i][k] for k in range(p.nf) ], [ a[i][k] for k in range(p.nf) ], _s[i]) for i in range(m)
                   ]
        s, q = o[:, 0:n], o[:, n:2 * n]
        Tmp = nanmax(where(q < s, q, s), 1)
        nlhf[logical_and(isinf(a), isinf(nlhf))] = 1e+300
        assert p.probType in ('GLP', 'NLP', 'NSP', 'SNLE', 'NLSP', 'MINLP')
        return [ si(Fields, Tmp[i], y[i], e[i], nlhf[i], nlhc[i] if nlhc is not None else None, indTC[i] if indTC is not None else None, residual[i] if residual is not None else None, o[i], a[i], _s[i]) for i in range(m)
               ]
        return


class si():

    def __init__(self, fields, *args, **kwargs):
        for i in range(len(fields)):
            setattr(self, fields[i], args[i])