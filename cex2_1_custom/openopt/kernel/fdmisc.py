# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\fdmisc.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import hstack, vstack, atleast_1d, cumsum, asarray, zeros, ndarray, prod, ones, copy, nan, flatnonzero, array_equal, asanyarray
from nonOptMisc import scipyInstalled, Hstack, Vstack, isspmatrix, SparseMatrixConstructor, DenseMatrixConstructor
try:
    from numpy import count_nonzero
except:
    count_nonzero = lambda elem: len(flatnonzero(asarray(elem)))

def setStartVectorAndTranslators(p):
    startPoint = p.x0
    fixedVars, freeVars = (None, None)
    from FuncDesigner import ooarray

    def getVars(t):
        vars1 = [ v for v in t if t is not None else [] if type(v) != ooarray ]
        vars2 = [ v for v in t if t is not None else [] if type(v) == ooarray ]
        t = vars1
        for elem in vars2:
            t += elem.tolist()

        return t

    if p.freeVars is not None:
        if not (isinstance(p.freeVars, (list, tuple, ndarray, set)) or hasattr(p.freeVars, 'is_oovar')):
            raise AssertionError
            p.freeVars = [
             p.freeVars]
            freeVars = p.freeVars
        else:
            freeVars = list(p.freeVars)
        freeVars = getVars(freeVars)
        fixedVars = list(set(startPoint.keys()).difference(set(freeVars)))
        p.fixedVars = fixedVars
    else:
        if p.fixedVars is not None:
            if not (isinstance(p.fixedVars, (list, tuple, ndarray, set)) or hasattr(p.fixedVars, 'is_oovar')):
                raise AssertionError
                p.fixedVars = [
                 p.fixedVars]
                fixedVars = p.fixedVars
            else:
                fixedVars = list(p.fixedVars)
                p.fixedVars = fixedVars
            fixedVars = getVars(fixedVars)
            freeVars = list(set(startPoint.keys()).difference(set(fixedVars)))
            p.freeVars = freeVars
        else:
            freeVars = list(startPoint.keys())
        from FuncDesigner import _Stochastic
        nn = len(freeVars)
        for i in range(nn):
            v = freeVars[nn - 1 - i]
            if isinstance(startPoint[v], _Stochastic):
                if fixedVars is None:
                    p.fixedVars = fixedVars = [
                     v]
                else:
                    fixedVars.append(v)
                if freeVars is None:
                    freeVars = p.freeVars = startPoint.keys()
                del freeVars[nn - 1 - i]

        freeVars.sort(key=(lambda elem: elem._id))
        p._freeVarsList = freeVars
        p._discreteVarsNumList = []
        p._discreteVarsList = []
        for i, v in enumerate(p._freeVarsList):
            if v.domain is not None:
                p._discreteVarsNumList.append(i)
                p._discreteVarsList.append(v)

        p._fixedVars = set(fixedVars) if fixedVars is not None else set()
        p._freeVars = set(freeVars) if freeVars is not None else set()
        tmp = {}
        for oov in freeVars:
            val = startPoint[oov]
            tmp[oov] = 1 if isinstance(val, _Stochastic) else asanyarray(val).size

    p._optVarSizes = tmp
    sizes = p._optVarSizes
    point2vector = lambda point: atleast_1d(hstack([ point[oov] if oov in point else zeros(sizes[oov]) for oov in p._optVarSizes ]))
    vector_x0 = point2vector(startPoint)
    n = vector_x0.size
    p.n = n
    oovar_sizes = [ len(atleast_1d(startPoint[elem]).flatten()) for elem in freeVars ]
    oovar_indexes = cumsum([0] + oovar_sizes)
    from FuncDesigner import oopoint
    startDictData = []
    if fixedVars is not None:
        for v in fixedVars:
            val = startPoint.get(v, 'absent')
            if val == 'absent':
                p.err('value for fixed variable %s is absent in start point' % v.name)
            startDictData.append((v, val))

    p._FDtranslator = {'prevX': nan}

    def vector2point(x):
        x = atleast_1d(x).copy()
        if array_equal(x, p._FDtranslator['prevX']):
            return p._FDtranslator['prevVal']
        r = startDictData
        tmp = [ (oov, x[oovar_indexes[i]:oovar_indexes[i + 1]] if oovar_indexes[i + 1] - oovar_indexes[i] > 1 else x[oovar_indexes[i]]) for i, oov in enumerate(freeVars) ]
        r = oopoint(r + tmp, skipArrayCast=True)
        r.maxDistributionSize = p.maxDistributionSize
        p._FDtranslator['prevVal'] = r
        p._FDtranslator['prevX'] = copy(x)
        return r

    oovarsIndDict = dict([ (oov, (oovar_indexes[i], oovar_indexes[i + 1])) for i, oov in enumerate(freeVars) ])

    def pointDerivative2array(pointDerivarive, useSparse='auto', func=None, point=None):
        if not scipyInstalled and useSparse == 'auto':
            useSparse = False
        if useSparse is True and not scipyInstalled:
            p.err('to handle sparse matrices you should have module scipy installed')
        if len(pointDerivarive) == 0:
            if func is not None:
                funcLen = func(point).size
                if useSparse is not False:
                    return SparseMatrixConstructor((funcLen, n))
                return DenseMatrixConstructor((funcLen, n))
            else:
                p.err('unclear error, maybe you have constraint independend on any optimization variables')
        Items = pointDerivarive.items()
        key, val = Items[0] if type(Items) == list else next(iter(Items))
        if isinstance(val, float) or isinstance(val, ndarray) and val.shape == ():
            val = atleast_1d(val)
        var_inds = oovarsIndDict[key]
        funcLen = int(round(prod(val.shape) / (var_inds[1] - var_inds[0])))
        involveSparse = useSparse
        if useSparse == 'auto':
            nTotal = n * funcLen
            nNonZero = sum([ elem.size if isspmatrix(elem) else count_nonzero(elem) for elem in pointDerivarive.values() ])
            involveSparse = 4 * nNonZero < nTotal and nTotal > 1000
        if involveSparse:
            r2 = []
            hasSparse = False
            if len(freeVars) > 5 * len(pointDerivarive):
                ind_Z = 0
                derivative_items = list(pointDerivarive.items())
                derivative_items.sort(key=(lambda elem: elem[0]._id))
                for oov, val in derivative_items:
                    ind_start, ind_end = oovarsIndDict[oov]
                    if ind_start != ind_Z:
                        r2.append(SparseMatrixConstructor((funcLen, ind_start - ind_Z)))
                    if not isspmatrix(val):
                        val = asarray(val)
                    r2.append(val)
                    ind_Z = ind_end

                if ind_Z != n:
                    r2.append(SparseMatrixConstructor((funcLen, n - ind_Z)))
            else:
                zeros_start_ind = 0
                zeros_end_ind = 0
                for i, var in enumerate(freeVars):
                    if var in pointDerivarive:
                        if zeros_end_ind != zeros_start_ind:
                            r2.append(SparseMatrixConstructor((funcLen, zeros_end_ind - zeros_start_ind)))
                            zeros_start_ind = zeros_end_ind
                        tmp = pointDerivarive[var]
                        if isspmatrix(tmp):
                            hasSparse = True
                        else:
                            tmp = asarray(tmp)
                        if tmp.ndim < 2:
                            tmp = tmp.reshape(funcLen, prod(tmp.shape) // funcLen)
                        r2.append(tmp)
                    else:
                        zeros_end_ind += oovar_sizes[i]
                        hasSparse = True

            if zeros_end_ind != zeros_start_ind:
                r2.append(SparseMatrixConstructor((funcLen, zeros_end_ind - zeros_start_ind)))
            r3 = Hstack(r2)
            if isspmatrix(r3) and r3.nnz > 0.25 * prod(r3.shape):
                r3 = r3.A
            return r3
        if funcLen == 1:
            r = DenseMatrixConstructor(n)
        else:
            r = SparseMatrixConstructor((funcLen, n)) if involveSparse else DenseMatrixConstructor((funcLen, n))
        for key, val in pointDerivarive.items():
            indexes = oovarsIndDict[key]
            if not involveSparse and isspmatrix(val):
                val = val.A
            if r.ndim == 1:
                r[(indexes[0]):(indexes[1])] = val.flatten() if type(val) == ndarray else val
            else:
                r[:, indexes[0]:indexes[1]] = val if val.shape == r.shape else val.reshape((funcLen, prod(val.shape) / funcLen))

        if useSparse is True and funcLen == 1:
            return SparseMatrixConstructor(r)
        else:
            if r.ndim <= 1:
                r = r.reshape(1, -1)
            if useSparse is False and hasattr(r, 'toarray'):
                r = r.toarray()
            return r
            return

    def getPattern(oofuns):
        assert isinstance(oofuns, list), 'oofuns should be Python list, inform developers of the bug'
        R = []
        for oof in oofuns:
            SIZE = asarray(oof(startPoint)).size
            r = []
            dep = oof._getDep()
            if len(p._fixedVars) != 0:
                dep = dep & p._freeVars if len(p._freeVars) < len(p._fixedVars) else dep.difference(p._fixedVars)
            ind_Z = 0
            vars = list(dep)
            vars.sort(key=(lambda elem: elem._id))
            for oov in vars:
                ind_start, ind_end = oovarsIndDict[oov]
                if ind_start != ind_Z:
                    r.append(SparseMatrixConstructor((SIZE, ind_start - ind_Z)))
                r.append(ones((SIZE, ind_end - ind_start)))
                ind_Z = ind_end

            if ind_Z != n:
                r.append(SparseMatrixConstructor((SIZE, n - ind_Z)))
            if any([ isspmatrix(elem) for elem in r ]):
                rr = Hstack(r) if len(r) > 1 else r[0]
            elif len(r) > 1:
                rr = hstack(r)
            else:
                rr = r[0]
            R.append(rr)

        result = Vstack(R) if any([ isspmatrix(_r) for _r in R ]) else vstack(R)
        return result

    p._getPattern = getPattern
    p.freeVars, p.fixedVars = freeVars, fixedVars
    p._point2vector, p._vector2point = point2vector, vector2point
    p._pointDerivative2array = pointDerivative2array
    p._oovarsIndDict = oovarsIndDict
    p._x0, p.x0 = p.x0, vector_x0

    def linearOOFunsToMatrices(oofuns):
        C, d = [], []
        Z = p._vector2point(zeros(p.n))
        for elem in oofuns:
            if elem.isConstraint:
                lin_oofun = elem.oofun
            else:
                lin_oofun = elem
            if lin_oofun.getOrder(p.freeVars, p.fixedVars) > 1:
                from oologfcn import OpenOptException
                raise OpenOptException("this function hasn't been intended to work with nonlinear FuncDesigner oofuns")
            C.append(p._pointDerivative2array(lin_oofun.D(Z, **p._D_kwargs), useSparse=p.useSparse))
            d.append(-lin_oofun(Z))

        C, d = Vstack(C), hstack(d).flatten()
        return (
         C, d)

    p._linearOOFunsToMatrices = linearOOFunsToMatrices
    return