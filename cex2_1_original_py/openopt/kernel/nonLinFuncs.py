# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\nonLinFuncs.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import *
from setDefaultIterFuncs import USER_DEMAND_EXIT
from ooMisc import killThread, setNonLinFuncsNumber
from nonOptMisc import scipyInstalled, Vstack, isspmatrix, isPyPy
try:
    from DerApproximator import get_d1
    DerApproximatorIsInstalled = True
except:
    DerApproximatorIsInstalled = False

class nonLinFuncs():

    def __init__(self):
        pass

    def wrapped_func(p, x, IND, userFunctionType, ignorePrev, getDerivative):
        if isinstance(x, dict):
            if not p.isFDmodel:
                p.err('calling the function with argument of type dict is allowed for FuncDesigner models only')
            x = p._point2vector(x)
        if not getattr(p.userProvided, userFunctionType):
            return array([])
        else:
            if p.istop == USER_DEMAND_EXIT:
                if p.solver.useStopByException:
                    raise killThread
                else:
                    return nan
            if getDerivative and not p.isFDmodel and not DerApproximatorIsInstalled:
                p.err('For the problem you should have DerApproximator installed, see http://openopt.org/DerApproximator')
            funcs = getattr(p.user, userFunctionType)
            if IND is not None:
                ind = p.getCorrectInd(IND)
            else:
                ind = None
            if not isspmatrix(x):
                x = atleast_1d(x)
            elif p.debug:
                p.pWarn('[oo debug] sparse matrix x in nonlinfuncs.py has been encountered')
            args = getattr(p.args, userFunctionType)
            if not hasattr(p, 'n' + userFunctionType):
                setNonLinFuncsNumber(p, userFunctionType)
            if x.shape[0] != p.n and (x.ndim < 2 or x.shape[1] != p.n):
                p.err('x with incorrect shape passed to non-linear function')
            if getDerivative or x.ndim <= 1 or x.shape[0] == 1:
                nXvectors = 1
                x_0 = copy(x)
            else:
                nXvectors = x.shape[0]
            if p.isFDmodel:
                if getDerivative:
                    if p.freeVars is None or p.fixedVars is not None and len(p.freeVars) < len(p.fixedVars):
                        funcs2 = [ lambda x, i=i: p._pointDerivative2array(funcs[i].D(x, Vars=p.freeVars, useSparse=p.useSparse, fixedVarsScheduleID=p._FDVarsID, exactShape=True), useSparse=p.useSparse, func=funcs[i], point=x)
                         for i in range(len(funcs))
                                 ]
                    else:
                        funcs2 = [ lambda x, i=i: p._pointDerivative2array(funcs[i].D(x, fixedVars=p.fixedVars, useSparse=p.useSparse, fixedVarsScheduleID=p._FDVarsID, exactShape=True), useSparse=p.useSparse, func=funcs[i], point=x)
                         for i in range(len(funcs))
                                 ]
                else:
                    if p.freeVars is None or p.fixedVars is not None and len(p.freeVars) < len(p.fixedVars):
                        funcs2 = [ lambda x, i=i: funcs[i]._getFuncCalcEngine(x, Vars=p.freeVars, fixedVarsScheduleID=p._FDVarsID) for i in range(len(funcs))
                                 ]
                    else:
                        funcs2 = [ lambda x, i=i: funcs[i]._getFuncCalcEngine(x, fixedVars=p.fixedVars, fixedVarsScheduleID=p._FDVarsID)
                         for i in range(len(funcs))
                                 ]
            else:
                funcs2 = funcs
            if ind is None:
                Funcs = funcs2
            elif ind is not None and p.functype[userFunctionType] == 'some funcs R^nvars -> R':
                Funcs = [ funcs2[i] for i in ind ]
            else:
                Funcs = getFuncsAndExtractIndexes(p, funcs2, ind, userFunctionType)
            Args = () if p.isFDmodel else args
            if nXvectors == 1:
                if p.isFDmodel:
                    X = p._vector2point(x)
                    X._p = p
                else:
                    X = x
            if nXvectors > 1:
                if userFunctionType == 'f':
                    assert p.isObjFunValueASingleNumber
                    if p.isFDmodel:
                        if not ind is None:
                            raise AssertionError
                            if p.hasVectorizableFuncs:
                                from FuncDesigner.ooPoint import ooPoint as oopoint
                                from FuncDesigner.multiarray import multiarray
                                xx = []
                                counter = 0
                                for i, oov in enumerate(p._freeVarsList):
                                    s = p._optVarSizes[oov]
                                    xx.append((oov, (x[:, counter:counter + s].flatten() if s == 1 else x[:, counter:counter + s]).view(multiarray)))
                                    counter += s

                                X = oopoint(xx)
                                X.update(p.dictOfFixedFuncs)
                                X.maxDistributionSize = p.maxDistributionSize
                                X._p = p
                            if len(p.unvectorizableFuncs) != 0:
                                XX = [ p._vector2point(x[i]) for i in range(nXvectors) ]
                                for _X in XX:
                                    _X._p = p
                                    _X.update(p.dictOfFixedFuncs)

                            r = vstack([ [ fun(xx) for xx in XX ] if funcs[i] in p.unvectorizableFuncs else fun(X) for i, fun in enumerate(Funcs) ]).T
                        else:
                            X = [ (x[i],) + Args for i in range(nXvectors) ]
                            R = []
                            for xx in X:
                                tmp = [ fun(*xx) for fun in Funcs ]
                                r_ = hstack(tmp[0]) if len(tmp) == 1 and isinstance(tmp[0], (list, tuple)) else hstack(tmp) if len(tmp) > 1 else tmp[0]
                                R.append(r_)

                            r = hstack(R)
                    elif not getDerivative:
                        tmp = [ fun(*((X,) + Args)) for fun in Funcs ]
                        r = hstack(tmp[0]) if len(tmp) == 1 and isinstance(tmp[0], (list, tuple)) else hstack(tmp) if len(tmp) > 1 else tmp[0]
                    elif getDerivative and p.isFDmodel:
                        rr = [ fun(X) for fun in Funcs ]
                        r = Vstack(rr) if scipyInstalled and any([ isspmatrix(elem) for elem in rr ]) else vstack(rr)
                    else:
                        r = []
                        if getDerivative:
                            diffInt = p.diffInt
                            abs_x = abs(x)
                            finiteDiffNumbers = 1e-10 * abs_x
                            if p.diffInt.size == 1:
                                finiteDiffNumbers[finiteDiffNumbers < diffInt] = diffInt
                            else:
                                finiteDiffNumbers[finiteDiffNumbers < diffInt] = diffInt[finiteDiffNumbers < diffInt]
                        else:
                            r = []
                        for index, fun in enumerate(Funcs):
                            if not getDerivative:
                                r.append(fun(*((X,) + Args)))
                            if getDerivative:

                                def func(x):
                                    r = fun(*((x,) + Args))
                                    if type(r) not in (list, tuple) or len(r) != 1:
                                        return r
                                    return r[0]

                                d1 = get_d1(func, x, pointVal=None, diffInt=finiteDiffNumbers, stencil=p.JacobianApproximationStencil, exactShape=True)
                                r.append(d1)

                        r = (getDerivative or hstack)(r) if 1 else vstack(r)
                    if type(r) != ndarray and not isscalar(r):
                        r = r.view(ndarray).flatten() if userFunctionType == 'f' else r.view(ndarray)
                    elif userFunctionType == 'f' and p.isObjFunValueASingleNumber and not isscalar(r):
                        if prod(r.shape) > 1 and not getDerivative and nXvectors == 1:
                            p.err('implicit summation in objective is no longer available to prevent possibly hidden bugs')
                    if userFunctionType == 'f' and p.isObjFunValueASingleNumber and getDerivative and r.ndim > 1:
                        if min(r.shape) > 1:
                            p.err('incorrect shape of objective func derivative')
                        if hasattr(r, 'toarray'):
                            r = r.toarray()
                        r = r.flatten()
                if userFunctionType != 'f' and nXvectors != 1:
                    r = r.reshape(nXvectors, int(r.size / nXvectors))
                if nXvectors == 1 and (not getDerivative or prod(r.shape) == 1):
                    r = r.flatten() if type(r) == ndarray else (isscalar(r) or r.toarray().flatten)() if 1 else atleast_1d(r)
                if p.invertObjFunc and userFunctionType == 'f':
                    r = -r
                if getDerivative or ind is None:
                    p.nEvals[userFunctionType] += nXvectors
                else:
                    p.nEvals[userFunctionType] = p.nEvals[userFunctionType] + float(nXvectors * len(ind)) / getattr(p, 'n' + userFunctionType)
            if getDerivative:
                if not x.size == p.n:
                    raise AssertionError
                    x = x_0
                if userFunctionType == 'f' and hasattr(p, 'solver') and p.solver.funcForIterFcnConnection == 'f' and hasattr(p, 'f_iter') and not getDerivative and (p.nEvals['f'] % p.f_iter == 0 or nXvectors > 1):
                    p.iterfcn(x, r)
            return r

    def wrapped_1st_derivatives(p, x, ind_, funcType, ignorePrev, useSparse):
        if isinstance(x, dict):
            if not p.isFDmodel:
                p.err('calling the function with argument of type dict is allowed for FuncDesigner models only')
            if ind_ is not None:
                p.err('the operation is turned off for argument of type dict when ind!=None')
            x = p._point2vector(x)
        if ind_ is not None:
            ind = p.getCorrectInd(ind_)
        else:
            ind = None
        if p.istop == USER_DEMAND_EXIT:
            if p.solver.useStopByException:
                raise killThread
            else:
                return nan
        derivativesType = 'd' + funcType
        prevKey = p.prevVal[derivativesType]['key']
        if prevKey is not None and p.iter > 0 and array_equal(x, prevKey) and ind is None and not ignorePrev:
            assert p.prevVal[derivativesType]['val'] is not None
            return copy(p.prevVal[derivativesType]['val'])
        else:
            if ind is None and not ignorePrev:
                p.prevVal[derivativesType]['ind'] = copy(x)
            nFuncs = getattr(p, 'n' + funcType)
            x = atleast_1d(x)
            if hasattr(p.userProvided, derivativesType) and getattr(p.userProvided, derivativesType):
                funcs = getattr(p.user, derivativesType)
                if ind is None or nFuncs == 1 and p.functype[funcType] == 'single func':
                    Funcs = funcs
                elif ind is not None and p.functype[funcType] == 'some funcs R^nvars -> R':
                    Funcs = [ funcs[i] for i in ind ]
                else:
                    Funcs = getFuncsAndExtractIndexes(p, funcs, ind, funcType)
                derivatives = []
                for fun in Funcs:
                    tmp = atleast_1d(fun(*((x,) + getattr(p.args, funcType))))
                    if tmp.size % p.n != 0:
                        if funcType == 'f':
                            p.err('incorrect user-supplied (sub)gradient size of objective function')
                        else:
                            if funcType == 'c':
                                p.err('incorrect user-supplied (sub)gradient size of non-lin inequality constraints')
                            elif funcType == 'h':
                                p.err('incorrect user-supplied (sub)gradient size of non-lin equality constraints')
                    if tmp.ndim == 1:
                        m = 1
                    else:
                        m = tmp.shape[0]
                    if p.functype[funcType] == 'some funcs R^nvars -> R' and m != 1:
                        p.err('incorrect shape of user-supplied derivative, it should be in accordance with user-provided func size')
                    derivatives.append(tmp)

                derivatives = Vstack(derivatives) if any(isspmatrix(derivatives)) else vstack(derivatives)
                if ind is None:
                    p.nEvals[derivativesType] += 1
                else:
                    p.nEvals[derivativesType] = p.nEvals[derivativesType] + float(len(ind)) / nFuncs
                if funcType == 'f':
                    if p.invertObjFunc:
                        derivatives = -derivatives
                    if p.isObjFunValueASingleNumber:
                        if not isinstance(derivatives, ndarray):
                            derivatives = derivatives.toarray()
                        derivatives = derivatives.flatten()
            else:
                derivatives = p.wrapped_func(x, ind, funcType, True, True)
                if ind is None:
                    p.nEvals[derivativesType] -= 1
                else:
                    p.nEvals[derivativesType] = p.nEvals[derivativesType] - float(len(ind)) / nFuncs
            if useSparse is False or not scipyInstalled or not hasattr(p, 'solver') or not p.solver._canHandleScipySparse:
                if not isinstance(derivatives, ndarray):
                    derivatives = derivatives.toarray()
            if type(derivatives) != ndarray and isinstance(derivatives, ndarray):
                derivatives = derivatives.A
            if ind is None and not ignorePrev:
                p.prevVal[derivativesType]['val'] = derivatives
            if funcType == 'f':
                if hasattr(p, 'solver') and not p.solver.iterfcnConnected and p.solver.funcForIterFcnConnection == 'df':
                    if p.df_iter is True:
                        p.iterfcn(x)
                    elif p.nEvals[derivativesType] % p.df_iter == 0:
                        p.iterfcn(x)
                if p.isObjFunValueASingleNumber and type(derivatives) == ndarray and derivatives.ndim > 1:
                    derivatives = derivatives.flatten()
            return derivatives

    def user_d2f(p, x):
        assert x.ndim == 1
        p.nEvals['d2f'] += 1
        assert len(p.user.d2f) == 1
        r = p.user.d2f[0](*((x,) + p.args.f))
        if p.invertObjFunc:
            r = -r
        return r

    def user_d2c(p, x):
        return ()

    def user_d2h(p, x):
        return ()

    def user_l(p, x):
        return ()

    def user_dl(p, x):
        return ()

    def user_d2l(p, x):
        return ()

    def getCorrectInd(p, ind):
        if ind is None or type(ind) in [list, tuple]:
            result = ind
        else:
            try:
                result = atleast_1d(ind).tolist()
            except:
                raise ValueError('%s is an unknown func index type!' % type(ind))

        return result


def getFuncsAndExtractIndexes(p, funcs, ind, userFunctionType):
    if ind is None:
        return funcs
    else:
        if len(funcs) == 1:

            def f(*args, **kwargs):
                tmp = funcs[0](*args, **kwargs)
                if isspmatrix(tmp):
                    tmp = tmp.tocsc()
                elif not isinstance(tmp, ndarray) or tmp.ndim == 0:
                    tmp = atleast_1d(tmp)
                if isPyPy:
                    return atleast_1d([ tmp[i] for i in ind ])
                return tmp[ind]

            return [
             f]
        arr_of_indexes = getattr(p, 'arr_of_indexes_' + userFunctionType)
        if isPyPy:
            Left_arr_indexes = searchsorted(arr_of_indexes, ind)
            left_arr_indexes = [ int(elem) for elem in atleast_1d(Left_arr_indexes) ]
        else:
            left_arr_indexes = searchsorted(arr_of_indexes, ind)
        indLenght = len(ind)
        Funcs2 = []
        IndDict = {}
        for i in range(indLenght):
            if left_arr_indexes[i] != 0:
                num_of_funcs_before_arr_left_border = arr_of_indexes[left_arr_indexes[i] - 1]
                inner_ind = ind[i] - num_of_funcs_before_arr_left_border - 1
            else:
                inner_ind = ind[i]
            if left_arr_indexes[i] in IndDict.keys():
                IndDict[left_arr_indexes[i]].append(inner_ind)
            else:
                IndDict[left_arr_indexes[i]] = [
                 inner_ind]
                Funcs2.append([funcs[left_arr_indexes[i]], IndDict[left_arr_indexes[i]]])

        Funcs = []
        for i in range(len(Funcs2)):

            def f_aux(x, i=i):
                r = Funcs2[i][0](x)
                if not isscalar(r):
                    if isPyPy:
                        if isspmatrix(r):
                            r = r.tocsc()[Funcs2[i][1]]
                        else:
                            tmp = atleast_1d(r)
                            r = atleast_1d([ tmp[i] for i in Funcs2[i][1] ])
                    else:
                        r = r.tocsc()[Funcs2[i][1]] if isspmatrix(r) else atleast_1d(r)[Funcs2[i][1]]
                return r

            Funcs.append(f_aux)

        return Funcs