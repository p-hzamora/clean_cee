# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\UkrOpt\interalgMOP.pyc
# Compiled at: 2012-12-08 11:04:59
PythonSum = sum
from numpy import isnan, array, atleast_1d, asarray, logical_and, all, logical_or, any, arange, vstack, inf, where, logical_not, take, abs, hstack, empty, isfinite, argsort, ones, zeros, log1p, array_split
from interalgLLR import *
try:
    from bottleneck import nanargmin, nanmin
except ImportError:
    from numpy import nanmin, nanargmin

def r43_seq(Arg):
    targets_vals, targets_tols, solutionsF, lf, uf = Arg
    lf, uf = asarray(lf), asarray(uf)
    if lf.size == 0 or len(solutionsF) == 0:
        return
    m = len(lf)
    n = lf.shape[2] / 2
    r = zeros((m, 2 * n))
    for _s in solutionsF:
        s = atleast_1d(_s)
        tmp = ones((m, 2 * n))
        for i in range(len(targets_vals)):
            val, tol = targets_vals[i], targets_tols[i]
            o, a = lf[:, i], uf[:, i]
            if val == inf:
                ff = s[i] + tol
                ind = a > ff
                if any(ind):
                    t1 = a[ind]
                    t2 = o[ind]
                    t_diff = t1 - t2
                    t_diff[t_diff < 1e-200] = 1e-200
                    Tmp = (ff - t2) / t_diff
                    tmp[ind] *= Tmp
                    tmp[ff < o] = 0.0
            elif val == -inf:
                ff = s[i] - tol
                ind = o < ff
                if any(ind):
                    t1 = a[ind]
                    t2 = o[ind]
                    t_diff = t1 - t2
                    t_diff[t_diff < 1e-200] = 1e-200
                    Tmp = (t1 - ff) / t_diff
                    tmp[ind] *= Tmp
                    tmp[a < ff] = 0.0
            else:
                ff = abs(s[i] - val) - tol
                if ff <= 0:
                    continue
                _lf, _uf = o - val, a - val
                ind = logical_or(_lf < ff, _uf > -ff)
                _lf = _lf[ind]
                _uf = _uf[ind]
                _lf[_lf > ff] = ff
                _lf[_lf < -ff] = -ff
                _uf[_uf < -ff] = -ff
                _uf[_uf > ff] = ff
                r20 = a[ind] - o[ind]
                r20[r20 < 1e-200] = 1e-200
                _diff = _uf - _lf
                _diff[_diff < 1e-200] = 1e-200
                Tmp = 1.0 - (_uf - _lf) / r20
                tmp[ind] *= Tmp

        new = 0
        if new:
            ind_0 = tmp == 0.0
            ind_1 = tmp == 1.0
            r[ind_1] = inf
            ind_m = logical_not(logical_and(ind_0, ind_1))
            r[ind_m] -= log1p(-tmp[ind_m]) * 1.4426950408889634
        else:
            r -= log1p(-tmp) * 1.4426950408889634

    return r


from multiprocessing import Pool

def r43(targets, SolutionsF, lf, uf, pool, nProc):
    lf, uf = asarray(lf), asarray(uf)
    target_vals = [ t.val for t in targets ]
    target_tols = [ t.tol for t in targets ]
    if nProc == 1 or len(SolutionsF) <= 1:
        return r43_seq((target_vals, target_tols, SolutionsF, lf, uf))
    else:
        splitBySolutions = True
        if splitBySolutions:
            ss = array_split(SolutionsF, nProc)
            Args = [ (target_vals, target_tols, s, lf, uf) for s in ss ]
            result = pool.imap_unordered(r43_seq, Args)
            r = [ elem for elem in result if elem is not None ]
            return PythonSum(r)
        lf2 = array_split(lf, nProc)
        uf2 = array_split(uf, nProc)
        Args = [ (target_vals, target_tols, SolutionsF, lf2[i], uf2[i]) for i in range(nProc) ]
        result = pool.map(r43_seq, Args)
        r = [ elem for elem in result if elem is not None ]
        return vstack(r)
        return


def r14MOP(p, nlhc, residual, definiteRange, y, e, vv, asdf1, C, r40, g, nNodes, r41, fTol, Solutions, varTols, _in, dataType, maxNodes, _s, indTC, xRecord):
    assert p.probType == 'MOP'
    if len(p._discreteVarsNumList):
        y, e = adjustDiscreteVarBounds(y, e, p)
    if p.nProc != 1 and getattr(p, 'pool', None) is None:
        p.pool = Pool(processes=p.nProc)
    else:
        if p.nProc == 1:
            p.pool = None
        ol, al = [], []
        targets = p.targets
        m, n = y.shape
        ol, al = [ [] for k in range(m) ], [ [] for k in range(m) ]
        for i, t in enumerate(targets):
            o, a, definiteRange = func82(y, e, vv, t.func, dataType, p)
            o, a = o.reshape(2 * n, m).T, a.reshape(2 * n, m).T
            for j in range(m):
                ol[j].append(o[j])
                al[j].append(a[j])

    nlhf = r43(targets, Solutions.F, ol, al, p.pool, p.nProc)
    fo_prev = 0
    if y.size == 0:
        return (_in, g, fo_prev, _s, Solutions, xRecord, r41, r40)
    else:
        nodes = func11(y, e, nlhc, indTC, residual, ol, al, _s, p)
        assert p.solver.dataHandling == 'raw', '"sorted" mode is unimplemented for MOP yet'
        if nlhf is None:
            new_nodes_tnlh_all = nlhc
        elif nlhc is None:
            new_nodes_tnlh_all = nlhf
        else:
            new_nodes_tnlh_all = nlhf + nlhc
        asdf1 = [ t.func for t in p.targets ]
        r5F, r5Coords = getr4Values(vv, y, e, new_nodes_tnlh_all, asdf1, C, p.contol, dataType, p)
        nIncome, nOutcome = r44(Solutions, r5Coords, r5F, targets, p.solver.sigma)
        fo = 0
        if len(_in) != 0:
            an = hstack((nodes, _in))
        else:
            an = atleast_1d(nodes)
        hasNewParetoNodes = False if nIncome == 0 else True
        if hasNewParetoNodes:
            ol2 = [ node.o for node in an ]
            al2 = [ node.a for node in an ]
            nlhc2 = [ node.nlhc for node in an ]
            nlhf2 = r43(targets, Solutions.F, ol2, al2, p.pool, p.nProc)
            tnlh_all = asarray(nlhc2) if nlhf2 is None else nlhf2 if nlhc2[0] is None else asarray(nlhc2) + nlhf2
        else:
            tnlh_all = vstack([new_nodes_tnlh_all] + [ node.tnlh_all for node in _in ]) if len(_in) != 0 else new_nodes_tnlh_all
        for i, node in enumerate(nodes):
            node.tnlh_all = tnlh_all[i]

        r10 = logical_not(any(isfinite(tnlh_all), 1))
        if any(r10):
            ind = where(logical_not(r10))[0]
            an = asarray(an[ind])
            tnlh_all = take(tnlh_all, ind, axis=0, out=tnlh_all[:ind.size])
        T1, T2 = tnlh_all[:, :tnlh_all.shape[1] / 2], tnlh_all[:, tnlh_all.shape[1] / 2:]
        T = where(logical_or(T1 < T2, isnan(T2)), T1, T2)
        t = nanargmin(T, 1)
        w = arange(t.size)
        NN = T[(w, t)].flatten()
        for i, node in enumerate(an):
            node.tnlh_all = tnlh_all[i]
            node.tnlh_curr_best = NN[i]

        astnlh = argsort(NN)
        an = an[astnlh]
        p._t = t
        if len(an) != 0:
            nlhf_fixed = asarray([ node.nlhf for node in an ])
            nlhc_fixed = asarray([ node.nlhc for node in an ])
            T = nlhf_fixed + nlhc_fixed if nlhc_fixed[0] is not None else nlhf_fixed
            p.__s = nanmin(vstack([T[(w, t)], T[(w, n + t)]]), 0)
        else:
            p.__s = array([])
        p._frontLength = len(Solutions.F)
        p._nIncome = nIncome
        p._nOutcome = nOutcome
        p.iterfcn(p.x0)
        if p.istop != 0:
            return (an, g, fo, None, Solutions, xRecord, r41, r40)
        nn = maxNodes
        an, g = func5(an, nn, g, p)
        nNodes.append(len(an))
        return (an, g, fo, _s, Solutions, xRecord, r41, r40)


def r44(Solutions, r5Coords, r5F, targets, sigma):
    nIncome, nOutcome = (0, 0)
    m = len(r5Coords)
    for j in range(m):
        if isnan(r5F[0][0]):
            continue
        if Solutions.coords.size == 0:
            Solutions.coords = array(r5Coords[j]).reshape(1, -1)
            Solutions.F.append(r5F[0])
            nIncome += 1
            continue
        M = Solutions.coords.shape[0]
        r47 = empty(M, bool)
        r47.fill(False)
        for i, target in enumerate(targets):
            f = r5F[j][i]
            F = asarray([ Solutions.F[k][i] for k in range(M) ])
            val, tol = target.val, target.tol
            Tol = sigma * tol
            if val == inf:
                r52 = f > F + Tol
            elif val == -inf:
                r52 = f < F - Tol
            else:
                r52 = abs(f - val) < abs(F - val) - Tol
            r47 = logical_or(r47, r52)

        accept_c = all(r47)
        if accept_c:
            nIncome += 1
            r48 = empty(M, bool)
            r48.fill(False)
            for i, target in enumerate(targets):
                f = r5F[j][i]
                F = asarray([ Solutions.F[k][i] for k in range(M) ])
                val, tol = target.val, target.tol
                if val == inf:
                    r36olution_better = f < F
                elif val == -inf:
                    r36olution_better = f > F
                else:
                    r36olution_better = abs(f - val) > abs(F - val)
                r48 = logical_or(r48, r36olution_better)

            r49 = logical_not(r48)
            remove_s = any(r49)
            if remove_s:
                r50 = where(r49)[0]
                nOutcome += r50.size
                Solutions.coords[r50[0]] = r5Coords[j]
                Solutions.F[r50[0]] = r5F[j]
                if r50.size > 1:
                    r49[r50[0]] = False
                    indLeft = logical_not(r49)
                    indLeftPositions = where(indLeft)[0]
                    newSolNumber = Solutions.coords.shape[0] - r50.size + 1
                    Solutions.coords = take(Solutions.coords, indLeftPositions, axis=0, out=Solutions.coords[:newSolNumber])
                    solutionsF2 = asarray(Solutions.F, object)
                    solutionsF2 = take(solutionsF2, indLeftPositions, axis=0, out=solutionsF2[:newSolNumber])
                    Solutions.F = solutionsF2.tolist()
            else:
                Solutions.coords = vstack((Solutions.coords, r5Coords[j]))
                Solutions.F.append(r5F[j])

    return (
     nIncome, nOutcome)