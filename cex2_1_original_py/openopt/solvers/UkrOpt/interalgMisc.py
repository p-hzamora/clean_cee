# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\UkrOpt\interalgMisc.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import isnan, array, atleast_1d, asarray, all, searchsorted, logical_or, any, nan, vstack, inf, where, logical_not, min, abs, hstack, insert, logical_xor, argsort
try:
    from numpy import append
except ImportError:

    def append(*args, **kw):
        raise ImportError('function append() is absent in PyPy yet')


from interalgLLR import *
from interalgT import truncateByPlane
try:
    from bottleneck import nanmin, nanmax
except ImportError:
    from numpy import nanmin, nanmax

def r14(p, nlhc, residual, definiteRange, y, e, vv, asdf1, C, r40, g, nNodes, r41, fTol, Solutions, varTols, _in, dataType, maxNodes, _s, indTC, xRecord):
    isSNLE = p.probType in ('NLSP', 'SNLE')
    maxSolutions, solutions, coords = Solutions.maxNum, Solutions.solutions, Solutions.coords
    if len(p._discreteVarsNumList):
        y, e = adjustDiscreteVarBounds(y, e, p)
    o, a, r41 = r45(y, e, vv, p, asdf1, dataType, r41, nlhc)
    fo_prev = float(0 if isSNLE else min((r41, r40 - (fTol if maxSolutions == 1 else 0))))
    if fo_prev > 1e+300:
        fo_prev = 1e+300
    y, e, o, a, _s, indTC, nlhc, residual = func7(y, e, o, a, _s, indTC, nlhc, residual)
    if 0 and (p._linear_objective or p.convex in (1, True)) and fo_prev < 1e+300:
        indT2 = np.empty(y.shape[0])
        indT2.fill(False)
        if p._linear_objective:
            d = p._linear_objective_factor
            th = fo_prev + (p._linear_objective_scalar if p.goal not in ('min', 'minimum') else -p._linear_objective_scalar)
            y, e, indT2, ind_t = truncateByPlane(y, e, indT2, d if p.goal in ('min',
                                                                              'minimum') else -d, th)
        elif p.convex in (1, True):
            assert p.goal in ('min', 'minimum')
            wr4 = (y + e) / 2
            adjustr4WithDiscreteVariables(wr4, p)
            cs = dict([ (oovar, asarray(wr4[:, i], dataType).view(multiarray)) for i, oovar in enumerate(vv) ])
            centerValues = asdf1(cs)
            gradient = asdf1.D(cs)
            y, e, indT2, ind_t = truncateByPlane2(cs, centerValues, y, e, indT2, gradient, fo_prev, p)
        else:
            assert 0, 'bug in FD kernel'
        if ind_t is not True:
            lj = ind_t.size
            o = take(o, ind_t, axis=0, out=o[:lj])
            a = take(a, ind_t, axis=0, out=a[:lj])
            if nlhc is not None:
                nlhc = take(nlhc, ind_t, axis=0, out=nlhc[:lj])
                indTC = np.logical_or(indTC[ind_t], indT2)
            _s = _s[ind_t]
    if y.size == 0:
        return (_in, g, fo_prev, _s, Solutions, xRecord, r41, r40)
    else:
        nodes = func11(y, e, nlhc, indTC, residual, o, a, _s, p)
        if p.solver.dataHandling == 'raw':
            tmp = o.copy()
            tmp[tmp > fo_prev] = -inf
            M = atleast_1d(nanmax(tmp, 1))
            for i, node in enumerate(nodes):
                node.th_key = M[i]

            if not isSNLE:
                for node in nodes:
                    node.fo = fo_prev

            if nlhc is not None:
                for i, node in enumerate(nodes):
                    node.tnlhf = node.nlhf + node.nlhc

            else:
                for i, node in enumerate(nodes):
                    node.tnlhf = node.nlhf

            an = hstack((nodes, _in))
            tnlh_fixed_local = vstack([ node.tnlhf for node in nodes ])
            tmp = a.copy()
            tmp[tmp > fo_prev] = fo_prev
            tmp2 = tmp - o
            tmp2[tmp2 < 1e-300] = 1e-300
            tmp2[o > fo_prev] = nan
            tnlh_curr = tnlh_fixed_local - log2(tmp2)
            tnlh_curr_best = nanmin(tnlh_curr, 1)
            for i, node in enumerate(nodes):
                node.tnlh_curr = tnlh_curr[i]
                node.tnlh_curr_best = tnlh_curr_best[i]

        else:
            tnlh_curr = None
        PointVals, PointCoords = getr4Values(vv, y, e, tnlh_curr, asdf1, C, p.contol, dataType, p)
        if PointVals.size != 0:
            xk, Min = r2(PointVals, PointCoords, dataType)
        else:
            xk = p.xk
            Min = nan
        if r40 > Min:
            r40 = Min
            xRecord = xk.copy()
        if r41 > Min:
            r41 = Min
        fo = float(0 if isSNLE else min((r41, r40 - (fTol if maxSolutions == 1 else 0))))
        if p.solver.dataHandling == 'raw':
            if fo != fo_prev and not isSNLE:
                fos = array([ node.fo for node in an ])
                th_keys = array([ node.th_key for node in an ])
                delta_fos = fos - fo
                ind_update = where(10 * delta_fos > fos - th_keys)[0]
                nodesToUpdate = an[ind_update]
                update_nlh = True if ind_update.size != 0 else False
                if update_nlh:
                    updateNodes(nodesToUpdate, fo)
                tmp = asarray([ node.key for node in an ])
                r10 = where(tmp > fo)[0]
                if r10.size != 0:
                    mino = [ an[i].key for i in r10 ]
                    mmlf = nanmin(asarray(mino))
                    g = nanmin((g, mmlf))
            NN = atleast_1d([ node.tnlh_curr_best for node in an ])
            r10 = logical_or(isnan(NN), NN == inf)
            if any(r10):
                ind = where(logical_not(r10))[0]
                an = an[ind]
                NN = NN[ind]
            if not isSNLE or p.maxSolutions == 1:
                astnlh = argsort(NN)
                an = an[astnlh]
        elif isSNLE and p.maxSolutions != 1:
            an = hstack((nodes, _in))
        else:
            nodes.sort(key=(lambda obj: obj.key))
            if len(_in) == 0:
                an = nodes
            else:
                arr1 = [ node.key for node in _in ]
                arr2 = [ node.key for node in nodes ]
                r10 = searchsorted(arr1, arr2)
                an = insert(_in, r10, nodes)
        if maxSolutions != 1:
            Solutions = r46(o, a, PointCoords, PointVals, fTol, varTols, Solutions)
            p._nObtainedSolutions = len(solutions)
            if p._nObtainedSolutions > maxSolutions:
                solutions = solutions[:maxSolutions]
                p.istop = 0
                p.msg = 'user-defined maximal number of solutions (p.maxSolutions = %d) has been exeeded' % p.maxSolutions
                return (
                 an, g, fo, None, Solutions, xRecord, r41, r40)
        p.iterfcn(xRecord, r40)
        if p.istop != 0:
            return (an, g, fo, None, Solutions, xRecord, r41, r40)
        if isSNLE and maxSolutions == 1 and Min <= fTol:
            p.istop, p.msg = (1000, 'required solution has been obtained')
            return (
             an, g, fo, None, Solutions, xRecord, r41, r40)
        an, g = func9(an, fo, g, p)
        nn = maxNodes
        an, g = func5(an, nn, g, p)
        nNodes.append(len(an))
        return (
         an, g, fo, _s, Solutions, xRecord, r41, r40)


def r46(o, a, PointCoords, PointVals, fTol, varTols, Solutions):
    solutions, coords = Solutions.solutions, Solutions.coords
    r5Ind = where(PointVals < fTol)[0]
    r5 = PointCoords[r5Ind]
    for c in r5:
        if len(solutions) == 0 or not any(all(abs(c - coords) < varTols, 1)):
            solutions.append(c)
            Solutions.coords = append(Solutions.coords, c.reshape(1, -1), 0)

    return Solutions


def r45(y, e, vv, p, asdf1, dataType, r41, nlhc):
    Case = p.solver.intervalObtaining
    if Case == 1:
        ip = func10(y, e, vv)
        o, a, definiteRange = func8(ip, asdf1, dataType)
    elif Case == 2:
        f = asdf1
        o, a, definiteRange = func82(y, e, vv, f, dataType, p)
    elif Case == 3:
        ip = func10(y, e, vv)
        o, a, definiteRange = func8(ip, asdf1, dataType)
        f = asdf1
        o2, a2, definiteRange2 = func82(y, e, vv, f, dataType, p)
        from numpy import allclose
        lf, lf2 = o.copy(), o2.copy()
        lf[isnan(lf)] = 0.123
        lf2[isnan(lf2)] = 0.123
        if not allclose(lf, lf2, atol=1e-10):
            raise 0
        uf, uf2 = a.copy(), a2.copy()
        uf[isnan(uf)] = 0.123
        uf2[isnan(uf2)] = 0.123
        if not allclose(uf, uf2, atol=1e-10):
            raise 0
    if p.debug and any(a + 1e-15 < o):
        p.warn('interval lower bound exceeds upper bound, it seems to be FuncDesigner kernel bug')
    if p.debug and any(logical_xor(isnan(o), isnan(a))):
        p.err('bug in FuncDesigner intervals engine')
    m, n = e.shape
    o, a = o.reshape(2 * n, m).T, a.reshape(2 * n, m).T
    if asdf1.isUncycled and p.probType not in ('SNLE', 'NLSP') and not p.probType.startswith('MI') and len(p._discreteVarsList) == 0:
        if all(definiteRange):
            tmp1 = o[nlhc == 0] if nlhc is not None else o
            if tmp1.size != 0:
                tmp1 = nanmin(tmp1)
                tmp1 += 1e-14 * abs(tmp1)
                if tmp1 == 0:
                    tmp1 = 1e-300
                r41 = nanmin((r41, tmp1))
    return (o, a, r41)


def updateNodes(nodesToUpdate, fo):
    if len(nodesToUpdate) == 0:
        return
    a_tmp = array([ node.a for node in nodesToUpdate ])
    Tmp = a_tmp
    Tmp[Tmp > fo] = fo
    o_tmp = array([ node.o for node in nodesToUpdate ])
    Tmp -= o_tmp
    Tmp[Tmp < 1e-300] = 1e-300
    Tmp[o_tmp > fo] = nan
    tnlh_all_new = -log2(Tmp)
    del Tmp
    del a_tmp
    tnlh_all_new += vstack([ node.tnlhf for node in nodesToUpdate ])
    tnlh_curr_best = nanmin(tnlh_all_new, 1)
    o_tmp[o_tmp > fo] = -inf
    M = atleast_1d(nanmax(o_tmp, 1))
    for j, node in enumerate(nodesToUpdate):
        node.fo = fo
        node.tnlh_curr = tnlh_all_new[j]
        node.tnlh_curr_best = tnlh_curr_best[j]
        node.th_key = M[j]