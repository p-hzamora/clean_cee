# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\Point.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import copy, isnan, array, argmax, abs, vstack, zeros, any, isfinite, all, where, asscalar, dot, sqrt, nanmax, isscalar, logical_or, matrix, prod, arange, ndarray, asarray, sum
from ooMisc import norm
from nonOptMisc import Copy, isPyPy
empty_arr = array(())
try:
    from scipy.sparse import isspmatrix, csr_matrix
    scipyInstalled = True
except ImportError:
    scipyInstalled = False
    isspmatrix = lambda *args, **kwargs: False

class Point:
    """
    the class is used to prevent calling non-linear constraints more than once
    f, c, h are funcs for obtaining objFunc, non-lin ineq and eq constraints.
    df, dc, dh are funcs for obtaining 1st derivatives.
    """
    __expectedArgs__ = [
     'x', 'f', 'mr']

    def __init__(self, p, x, *args, **kwargs):
        self.p = p
        self.x = copy(x)
        self.isMultiArray = self.x.ndim > 1
        for i, arg in enumerate(args):
            setattr(self, '_' + self.__expectedArgs__[i], args[i])

        for name, val in kwargs.items():
            setattr(self, '_' + name, val)

    def f(self):
        if not hasattr(self, '_f'):
            if self.p._baseClassName == 'NonLin' and self.p.probType != 'IP':
                func = self.p.f if self.p.isObjFunValueASingleNumber else self.p.F
                self._f = func(self.x)
            else:
                self._f = self.p.objFunc(self.x)
        return copy(self._f)

    def df(self):
        if not hasattr(self, '_df'):
            self._df = self.p.df(self.x)
        return Copy(self._df)

    def c(self, ind=None):
        if not self.p.userProvided.c:
            return empty_arr.copy()
        else:
            if ind is None:
                if not hasattr(self, '_c'):
                    self._c = self.p.c(self.x)
                    self._nNaNs_C = isnan(self._c).sum(self._c.ndim - 1)
                    if self.isMultiArray:
                        tmp = self._c
                        delattr(self, '_c')
                        return tmp
                return copy(self._c)
            else:
                if hasattr(self, '_c'):
                    return copy(self._c[ind])
                return copy(self.p.c(self.x, ind))

            return

    def dc(self, ind=None):
        if not self.p.userProvided.c:
            return empty_arr.copy().reshape(0, self.p.n)
        else:
            if ind is None:
                if not hasattr(self, '_dc'):
                    self._dc = self.p.dc(self.x)
                return Copy(self._dc)
            else:
                if hasattr(self, '_dc'):
                    return Copy(self._dc[ind])
                return Copy(self.p.dc(self.x, ind))

            return

    def h(self, ind=None):
        if not self.p.userProvided.h:
            return empty_arr.copy()
        else:
            if ind is None:
                if not hasattr(self, '_h'):
                    self._h = self.p.h(self.x)
                    self._nNaNs_H = isnan(self._h).sum(self._h.ndim - 1)
                    if self.isMultiArray:
                        tmp = self._h
                        delattr(self, '_h')
                        return tmp
                return copy(self._h)
            else:
                if hasattr(self, '_h'):
                    return copy(self._h[ind])
                return copy(self.p.h(self.x, ind))

            return

    def dh(self, ind=None):
        if not self.p.userProvided.h:
            return empty_arr.copy().reshape(0, self.p.n)
        else:
            if ind is None:
                if not hasattr(self, '_dh'):
                    self._dh = self.p.dh(self.x)
                return Copy(self._dh)
            else:
                if hasattr(self, '_dh'):
                    return Copy(self._dh[ind])
                return Copy(self.p.dh(self.x, ind))

            return

    def d2f(self):
        if not hasattr(self, '_d2f'):
            self._d2f = self.p.d2f(self.x)
        return copy(self._d2f)

    def lin_ineq(self):
        if not hasattr(self, '_lin_ineq'):
            self._lin_ineq = self.p._get_AX_Less_B_residuals(self.x)
        return copy(self._lin_ineq)

    def lin_eq(self):
        if not hasattr(self, '_lin_eq'):
            self._lin_eq = self.p._get_AeqX_eq_Beq_residuals(self.x)
        return copy(self._lin_eq)

    def lb(self):
        if not hasattr(self, '_lb'):
            self._lb = self.p.lb - self.x
        return copy(self._lb)

    def ub(self):
        if not hasattr(self, '_ub'):
            self._ub = self.x - self.p.ub
        return copy(self._ub)

    def mr(self, retAll=False, checkBoxBounds=True):
        if not hasattr(self, '_mr'):
            r, fname, ind = (0, None, 0)
            if self.isMultiArray:
                r = zeros(self.x.shape[0])
            ineqs = ['lin_ineq', 'lb', 'ub'] if checkBoxBounds else ['lin_ineq']
            eqs = ['lin_eq']
            if self.p._baseClassName == 'NonLin':
                ineqs.append('c')
                eqs.append('h')
            for field in ineqs:
                fv = array(getattr(self, field)())
                if fv.size > 0:
                    val_max = nanmax(fv, fv.ndim - 1)
                    r = where(r < val_max, val_max, r)
                    if not self.isMultiArray and not isnan(val_max):
                        ind_max = where(fv == val_max)[0][0]
                        if r < val_max:
                            r, ind, fname = val_max, ind_max, field

            for field in eqs:
                fv = array(getattr(self, field)())
                if fv.size > 0:
                    fv = abs(fv)
                    val_max = nanmax(fv, fv.ndim - 1)
                    r = where(r < val_max, val_max, r)
                    if not self.isMultiArray and not isnan(val_max):
                        ind_max = argmax(fv)
                        if r < val_max:
                            r, ind, fname = val_max, ind_max, field

            if not self.isMultiArray:
                self._mr, self._mrName, self._mrInd = r, fname, ind
        if retAll:
            return (asscalar(copy(self._mr)), self._mrName, asscalar(copy(self._mrInd)))
        else:
            if not self.isMultiArray:
                return asscalar(copy(self._mr))
            else:
                return r

            return

    def sum_of_all_active_constraints(self):
        if not hasattr(self, '_sum_of_all_active_constraints'):
            p = self.p
            if p.solver.__name__ == 'ralg':
                tol = p.contol / 2.0
            else:
                tol = 0.0
            c, h = self.c(), self.h()
            all_lin = self.all_lin()
            self._sum_of_all_active_constraints = (c[c > 0] - 0).sum() + (h[h > tol] - tol).sum() - (h[h < -tol] + tol).sum() + all_lin
        return Copy(self._sum_of_all_active_constraints)

    def mr_alt(self, retAll=False, bestFeasiblePoint=None):
        if hasattr(self, '_mr_alt'):
            delattr(self, '_mr_alt')
        if not hasattr(self, '_mr_alt'):
            p = self.p
            if not hasattr(p.solver, 'approach') or p.solver.approach == 'all active':
                val = self.sum_of_all_active_constraints()
                if bestFeasiblePoint is not None:
                    pass
                self._mr_alt, self._mrName_alt, self._mrInd_alt = val, 'all active', 0
            else:
                p.err('bug in openopt kernel, inform developers')
        if retAll:
            return (asscalar(copy(self._mr_alt)), self._mrName_alt, asscalar(copy(self._mrInd_alt)))
        else:
            return asscalar(copy(self._mr_alt))
            return

    def dmr(self, retAll=False):
        if not hasattr(self, '_dmr') or retAll and not hasattr(self, '_dmrInd'):
            g = zeros(self.p.n)
            maxResidual, resType, ind = self.mr(retAll=True)
            if resType == 'lb':
                g[ind] -= 1
            elif resType == 'ub':
                g[ind] += 1
            elif resType == 'lin_ineq':
                g += self.p.A[ind]
            elif resType == 'lin_eq':
                rr = self.p.matmult(self.p.Aeq[ind], self.x) - self.p.beq[ind]
                if rr < 0:
                    g -= self.p.Aeq[ind]
                else:
                    g += self.p.Aeq[ind]
            elif resType == 'c':
                dc = self.dc(ind=ind).flatten()
                g += dc
            elif resType == 'h':
                dh = self.dh(ind=ind).flatten()
                if self.p.h(self.x, ind) < 0:
                    g -= dh
                else:
                    g += dh
            self._dmr, self._dmrName, self._dmrInd = g, resType, ind
        if retAll:
            return (copy(self._dmr), self._dmrName, copy(self._dmrInd))
        else:
            return copy(self._dmr)

    def betterThan(self, point2compare, altLinInEq=False, bestFeasiblePoint=None):
        """
        usage: result = involvedPoint.better(pointToCompare)

        returns True if the involvedPoint is better than pointToCompare
        and False otherwise
        (if NOT better, mb same fval and same residuals or residuals less than desired contol)
        """
        if self.p.isUC:
            return self.f() < point2compare.f()
        if altLinInEq:
            mr, point2compareResidual = self.mr_alt(bestFeasiblePoint=bestFeasiblePoint), point2compare.mr_alt(bestFeasiblePoint=bestFeasiblePoint)
        else:
            mr, point2compareResidual = self.mr(), point2compare.mr()
        self_nNaNs, point2compare_nNaNs = self.nNaNs(), point2compare.nNaNs()
        if point2compare_nNaNs > self_nNaNs:
            return True
        if point2compare_nNaNs < self_nNaNs:
            return False
        if self_nNaNs == 0:
            if mr > self.p.contol and mr > point2compareResidual:
                return False
            if point2compareResidual > self.p.contol and point2compareResidual > mr:
                return True
        else:
            if mr == 0 and point2compareResidual == 0:
                if self.p.solver.__name__ not in ('interalg', 'de'):
                    self.p.err('you should provide at least one active constraint in each point from R^n where some constraints are undefined')
            return mr < point2compareResidual
        point2compareF_is_NaN = isnan(point2compare.f())
        selfF_is_NaN = isnan(self.f())
        if isPyPy:
            if type(point2compareF_is_NaN) == ndarray:
                point2compareF_is_NaN = asscalar(point2compareF_is_NaN)
            if type(selfF_is_NaN) == ndarray:
                selfF_is_NaN = asscalar(selfF_is_NaN)
        if not point2compareF_is_NaN:
            if not selfF_is_NaN:
                return self.f() < point2compare.f()
            else:
                return False

        else:
            if selfF_is_NaN:
                return mr < point2compareResidual
            else:
                return True

    def isFeas(self, altLinInEq):
        if not all(isfinite(self.f())):
            return False
        if self.p.isUC:
            return True
        if self.nNaNs() != 0:
            return False
        contol = self.p.contol
        if altLinInEq:
            if self.mr_alt() > contol:
                return False
        elif hasattr(self, '_mr'):
            if self._mr > contol:
                return False
        else:
            if any(self.lb() > contol):
                return False
            if any(self.ub() > contol):
                return False
            if any(abs(self.lin_eq()) > contol):
                return False
            if any(self.lin_ineq() > contol):
                return False
            if any(abs(self.h()) > contol):
                return False
            if any(self.c() > contol):
                return False
        return True

    def nNaNs(self):
        if self.p._baseClassName != 'NonLin':
            return 0
        hasC, hasH = self.p.userProvided.c, self.p.userProvided.h
        if hasH and not hasattr(self, '_nNaNs_H'):
            self.h()
        if hasC and not hasattr(self, '_nNaNs_C'):
            self.c()
        r = (self._nNaNs_C if hasC else 0) + (self._nNaNs_H if hasH else 0)
        return r

    def linePoint(self, alp, point2, ls=None):
        p = self.p
        r = p.point(self.x * (1 - alp) + point2.x * alp)
        if not p.iter % 16:
            lin_ineq_predict = self.lin_ineq() * (1 - alp) + point2.lin_ineq() * alp
            r._lin_ineq = lin_ineq_predict
            r._lin_eq = self.lin_eq() * (1 - alp) + point2.lin_eq() * alp
        if 0 < alp < 1:
            c1, c2 = self.c(), point2.c()
            ind1 = logical_or(c1 > 0, isnan(c1))
            ind2 = logical_or(c2 > 0, isnan(c2))
            ind = logical_or(ind1, ind2)
            _c = zeros(p.nc)
            if any(ind):
                _c[ind] = p.c(r.x, where(ind)[0])
            r._c = _c
            r._nNaNs_C = isnan(_c).sum(_c.ndim - 1)
        return r

    def all_lin(self):
        if not hasattr(self, '_all_lin'):
            lb, ub, lin_ineq = self.lb(), self.ub(), self.lin_ineq()
            r = 0.0
            lin_eq = self.lin_eq()
            ind_lb, ind_ub = lb > 0.0, ub > 0.0
            ind_lin_ineq = lin_ineq > 0.0
            ind_lin_eq = abs(lin_eq) > 0.0
            USE_SQUARES = 1
            if USE_SQUARES:
                if any(ind_lb):
                    r += sum(lb[ind_lb] ** 2)
                if any(ind_ub):
                    r += sum(ub[ind_ub] ** 2)
                if any(ind_lin_ineq):
                    r += sum(lin_ineq[ind_lin_ineq] ** 2)
                if any(ind_lin_eq):
                    r += sum(lin_eq[ind_lin_eq] ** 2)
                self._all_lin = r / self.p.contol
            else:
                if any(ind_lb):
                    r += sum(lb[ind_lb])
                if any(ind_ub):
                    r += sum(ub[ind_ub])
                if any(ind_lin_ineq):
                    r += sum(lin_ineq[ind_lin_ineq])
                if any(ind_lin_eq):
                    r += sum(abs(lin_eq[ind_lin_eq]))
                self._all_lin = r
        return copy(self._all_lin)

    def all_lin_gradient(self):
        if not hasattr(self, '_all_lin_gradient'):
            p = self.p
            n = p.n
            d = zeros(n)
            lb, ub = self.lb(), self.ub()
            lin_ineq = self.lin_ineq()
            lin_eq = self.lin_eq()
            ind_lb, ind_ub = lb > 0.0, ub > 0.0
            ind_lin_ineq = lin_ineq > 0.0
            ind_lin_eq = abs(lin_eq) != 0.0
            USE_SQUARES = 1
            if USE_SQUARES:
                if any(ind_lb):
                    d[ind_lb] -= lb[ind_lb]
                if any(ind_ub):
                    d[ind_ub] += ub[ind_ub]
                if any(ind_lin_ineq):
                    b = p.b[ind_lin_ineq]
                    if hasattr(p, '_A'):
                        a = p._A[ind_lin_ineq]
                        tmp = a._mul_sparse_matrix(csr_matrix((self.x, (arange(n), zeros(n))), shape=(n, 1))).toarray().flatten() - b
                        d += a.T._mul_sparse_matrix(tmp.reshape(tmp.size, 1)).A.flatten()
                    else:
                        if isPyPy:
                            a = vstack([ p.A[j] for j in where(ind_lin_ineq)[0] ])
                        else:
                            a = p.A[ind_lin_ineq]
                        d += dot(a.T, dot(a, self.x) - b)
                if any(ind_lin_eq):
                    if isspmatrix(p.Aeq):
                        p.err('this solver is not ajusted to handle sparse Aeq matrices yet')
                    aeq = p.Aeq
                    beq = p.beq
                    d += dot(aeq.T, dot(aeq, self.x) - beq)
                self._all_lin_gradient = 2.0 * d / p.contol
            else:
                if any(ind_lb):
                    d[ind_lb] -= 1
                if any(ind_ub):
                    d[ind_ub] += 1
                if any(ind_lin_ineq):
                    b = p.b[ind_lin_ineq]
                    if hasattr(p, '_A'):
                        d += p._A[ind_lin_ineq].sum(0).A.flatten()
                    else:
                        d += p.A[ind_lin_ineq].sum(0).flatten()
                if any(ind_lin_eq):
                    p.err('not implemented yet, if you see it inform OpenOpt developers')
                self._all_lin_gradient = d
        return copy(self._all_lin_gradient)

    def sum_of_all_active_constraints_gradient(self):
        if not hasattr(self, '_sum_of_all_active_constraints_gradient'):
            p = self.p
            contol = p.contol
            x = self.x
            direction = self.all_lin_gradient()
            if p.solver.__name__ == 'ralg':
                new = 1
            elif p.solver.__name__ == 'gsubg':
                new = 0
            else:
                p.err('unhandled case in Point._getDirection')
            if p.userProvided.c:
                th = 0.0
                C = p.c(x)
                Ind = C > th
                ind = where(Ind)[0]
                activeC = asarray(C[Ind])
                if len(ind) > 0:
                    tmp = p.dc(x, ind)
                    if new:
                        if tmp.ndim == 1 or min(tmp.shape) == 1:
                            if hasattr(tmp, 'toarray'):
                                tmp = tmp.toarray()
                            if activeC.size == prod(tmp.shape):
                                activeC = activeC.reshape(tmp.shape)
                            tmp *= (activeC - th * 0.999999999999999) / norm(tmp)
                        else:
                            if hasattr(tmp, 'toarray'):
                                tmp = tmp.toarray()
                            tmp *= ((activeC - th * 0.999999999999999) / sqrt((tmp ** 2).sum(1))).reshape(-1, 1)
                    if tmp.ndim > 1:
                        tmp = tmp.sum(0)
                    direction += (tmp.A if type(tmp) != ndarray else tmp).flatten()
            if p.userProvided.h:
                th = contol / 2.0
                H = p.h(x)
                Ind1 = H > th
                ind1 = where(Ind1)[0]
                H1 = asarray(H[Ind1])
                if len(ind1) > 0:
                    tmp = p.dh(x, ind1)
                    if new:
                        if tmp.ndim == 1 or min(tmp.shape) == 1:
                            if hasattr(tmp, 'toarray'):
                                tmp = tmp.toarray()
                            if H1.size == prod(tmp.shape):
                                H1 = H1.reshape(tmp.shape)
                            tmp *= (H1 - th * 0.999999999999999) / norm(tmp)
                        else:
                            if hasattr(tmp, 'toarray'):
                                tmp = tmp.toarray()
                            tmp *= ((H1 - th * 0.999999999999999) / sqrt((tmp ** 2).sum(1))).reshape(-1, 1)
                    if tmp.ndim > 1:
                        tmp = tmp.sum(0)
                    direction += (tmp.A if isspmatrix(tmp) or hasattr(tmp, 'toarray') else tmp).flatten()
                ind2 = where(H < -th)[0]
                H2 = H[ind2]
                if len(ind2) > 0:
                    tmp = p.dh(x, ind2)
                    if new:
                        if tmp.ndim == 1 or min(tmp.shape) == 1:
                            if hasattr(tmp, 'toarray'):
                                tmp = tmp.toarray()
                            if H2.size == prod(tmp.shape):
                                H2 = H2.reshape(tmp.shape)
                            tmp *= (-H2 - th * 0.999999999999999) / norm(tmp)
                        else:
                            if hasattr(tmp, 'toarray'):
                                tmp = tmp.toarray()
                            tmp *= ((-H2 - th * 0.999999999999999) / sqrt((tmp ** 2).sum(1))).reshape(-1, 1)
                    if tmp.ndim > 1:
                        tmp = tmp.sum(0)
                    direction -= (tmp.A if isspmatrix(tmp) or isinstance(tmp, matrix) else tmp).flatten()
            self._sum_of_all_active_constraints_gradient = direction
        return Copy(self._sum_of_all_active_constraints_gradient)

    def _getDirection(self, approach, currBestFeasPoint=None):
        if self.isFeas(altLinInEq=True):
            self.direction, self.dType = self.df(), 'f'
            if type(self.direction) != ndarray:
                self.direction = self.direction.A.flatten()
            return self.direction.copy()
        else:
            if approach == 'all active':
                self.dType = 'all active'
                self.direction = self.sum_of_all_active_constraints_gradient()
            else:
                maxRes, fname, ind = self.mr_alt(1, bestFeasiblePoint=currBestFeasPoint)
                if fname == 'all_lin':
                    d = self.all_lin_gradient()
                    self.dType = 'all_lin'
                elif fname == 'lin_eq':
                    self.p.err('kernel error, inform openopt developers')
                elif fname == 'c':
                    d = self.dmr()
                    self.dType = 'c'
                elif fname == 'h':
                    d = self.dmr()
                    self.dType = 'h'
                else:
                    self.p.err('error in getDirection (unknown residual type ' + fname + ' ), you should report the bug')
                self.direction = d.flatten()
            if type(self.direction) != ndarray:
                self.direction = self.direction.A.flatten()
            contol, fTol = self.p.contol, self.p.fTol
            if currBestFeasPoint is not None and self.f() + 0.25 * fTol > currBestFeasPoint.f():
                pass
            return self.direction.copy()
            return