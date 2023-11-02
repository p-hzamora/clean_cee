# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\residuals.pyc
# Compiled at: 2012-12-08 11:04:59
__docformat__ = 'restructuredtext en'
from numpy import asfarray, array, asarray, argmax, zeros, isfinite, all, isnan, arange
empty_arr = asfarray([])
try:
    from scipy.sparse import csr_matrix
except:
    pass

class residuals:

    def __init__(self):
        pass

    def _get_nonLinInEq_residuals(self, x):
        if hasattr(self.userProvided, 'c') and self.userProvided.c:
            return self.c(x)
        else:
            return empty_arr.copy()

    def _get_nonLinEq_residuals(self, x):
        if hasattr(self.userProvided, 'h') and self.userProvided.h:
            return self.h(x)
        else:
            return empty_arr.copy()

    def _get_AX_Less_B_residuals(self, x):
        if self.A is not None and self.A.size > 0:
            if x.ndim > 1:
                if not hasattr(self, '_A'):
                    return (self.matmult(self.A, x.T) - self.b.reshape(-1, 1)).T
                return (self._A._mul_sparse_matrix(csr_matrix(x.T)).toarray().T - self.b.reshape(-1, 1)).T
            if not hasattr(self, '_A'):
                return self.matmult(self.A, x).flatten() - self.b
            return self._A._mul_sparse_matrix(csr_matrix((x, (arange(self.n), zeros(self.n))), shape=(self.n, 1))).toarray().flatten() - self.b
        else:
            return empty_arr.copy()
            return

    def _get_AeqX_eq_Beq_residuals(self, x):
        if self.Aeq is not None and self.Aeq.size > 0:
            if x.ndim > 1:
                if not hasattr(self, '_Aeq'):
                    return (self.matmult(self.Aeq, x.T) - self.beq.reshape(-1, 1)).T
                return (self._Aeq._mul_sparse_matrix(csr_matrix(x.T)).toarray().T - self.beq.reshape(-1, 1)).T
            if not hasattr(self, '_Aeq'):
                return self.matmult(self.Aeq, x).flatten() - self.beq
            return self._Aeq._mul_sparse_matrix(csr_matrix((x, (arange(self.n), zeros(self.n))), shape=(self.n, 1))).toarray().flatten() - self.beq
        else:
            return empty_arr.copy()
            return

    def _getLbresiduals(self, x):
        return self.lb - x

    def _getUbresiduals(self, x):
        return x - self.ub

    def _getresiduals(self, x):
        r = EmptyClass()
        if self._baseClassName == 'NonLin':
            r.c = self._get_nonLinInEq_residuals(x)
            r.h = self._get_nonLinEq_residuals(x)
        else:
            r.c = r.h = 0
        r.lin_ineq = self._get_AX_Less_B_residuals(x)
        r.lin_eq = self._get_AeqX_eq_Beq_residuals(x)
        r.lb = self._getLbresiduals(x)
        r.ub = self._getUbresiduals(x)
        return r

    def getMaxResidual(self, x, retAll=False):
        """
        if retAll:  returns
        1) maxresidual
        2) name of residual type (like 'lb', 'c', 'h', 'Aeq')
        3) index of the constraint of given type
        (for example 15, 'lb', 4 means maxresidual is equal to 15, provided by lb[4])
        don't forget about Python indexing from zero!
        if retAll == False:
        returns only r
        """
        residuals = self._getresiduals(x)
        r, fname, ind = (0, None, None)
        for field in ('c', 'lin_ineq', 'lb', 'ub'):
            fv = asarray(getattr(residuals, field)).flatten()
            if fv.size > 0:
                ind_max = argmax(fv)
                val_max = fv[ind_max]
                if r < val_max:
                    r, ind, fname = val_max, ind_max, field

        for field in ('h', 'lin_eq'):
            fv = asarray(getattr(residuals, field)).flatten()
            if fv.size > 0:
                fv = abs(fv)
                ind_max = argmax(fv)
                val_max = fv[ind_max]
                if r < val_max:
                    r, ind, fname = val_max, ind_max, field

        if retAll:
            return (r, fname, ind)
        else:
            return r
            return

    def _getMaxConstrGradient2(self, x):
        g = zeros(self.n)
        mr0 = self.getMaxResidual(x)
        for j in range(self.n):
            x[j] += self.diffInt
            g[j] = self.getMaxResidual(x) - mr0
            x[j] -= self.diffInt

        g /= self.diffInt
        return g

    def getMaxConstrGradient(self, x, retAll=False):
        g = zeros(self.n)
        maxResidual, resType, ind = self.getMaxResidual(x, retAll=True)
        if resType == 'lb':
            g[ind] -= 1
        elif resType == 'ub':
            g[ind] += 1
        elif resType == 'A':
            g += self.A[ind]
        elif resType == 'Aeq':
            rr = self.matmult(self.Aeq[ind], x) - self.beq[ind]
            if rr < 0:
                g -= self.Aeq[ind]
            else:
                g += self.Aeq[ind]
        elif resType == 'c':
            dc = self.dc(x, ind).flatten()
            g += dc
        elif resType == 'h':
            dh = self.dh(x, ind).flatten()
            if self.h(x, ind) < 0:
                g -= dh
            else:
                g += dh
        if retAll:
            return (g, resType, ind)
        else:
            return g

    def isFeas(self, x):
        if any(isnan(self._get_nonLinEq_residuals(x))) or any(isnan(self._get_nonLinInEq_residuals(x))):
            return False
        is_X_finite = all(isfinite(x))
        is_ConTol_OK = self.getMaxResidual(x) <= self.contol
        cond1 = is_ConTol_OK and is_X_finite and all(isfinite(self.objFunc(x)))
        if self.probType in ('NLSP', 'SNLE'):
            return cond1 and self.F(x) < self.ftol
        else:
            return cond1

    def discreteConstraintsAreSatisfied(self, x):
        k = -1
        A = array([0, 1])
        for i in self.discreteVars.keys():
            s = self.discreteVars[i] if self.discreteVars[i] is not bool and self.discreteVars[i] is not 'bool' else A
            if not any(abs(x[i] - s) < self.discrtol):
                k = i
                break

        if k == -1:
            return True
        else:
            return False


class EmptyClass:
    pass