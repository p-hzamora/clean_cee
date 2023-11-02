# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\SLE.pyc
# Compiled at: 2012-12-08 11:04:59
from ooMisc import assignScript
from baseProblem import MatrixProblem
from numpy import asfarray, ones, inf, dot, nan, zeros, any, all, isfinite, eye, vstack, hstack, flatnonzero, isscalar, ndarray, atleast_2d, zeros_like
from ooMisc import norm
from oologfcn import OpenOptException
import NLP
from nonOptMisc import scipyInstalled, Vstack
try:
    import scipy
    scipyInstalled = True
except:
    scipyInstalled = False

class SLE(MatrixProblem):
    expectedArgs = [
     'C', 'd']
    probType = 'SLE'
    goal = 'solution'
    allowedGoals = ['solution']
    showGoal = False
    FuncDesignerSign = 'C'
    solver = 'defaultSLEsolver'
    _optionalData = []
    _isPrepared = False

    def __init__(self, *args, **kwargs):
        MatrixProblem.__init__(self, *args, **kwargs)

    _useSparse = lambda self: True if scipyInstalled and self.n > 100 else False

    def objFunc(self, x):
        if isinstance(self.C, ndarray):
            return norm(dot(self.C, x) - self.d, inf)
        else:
            t1 = self.C_as_csc
            t2 = scipy.sparse.csr_matrix(x)
            if t2.shape[0] != t1.shape[1]:
                if t2.shape[1] == t1.shape[1]:
                    t2 = t2.T
                else:
                    raise FuncDesignerException('incorrect shape in FuncDesigner function _D(), inform developers about the bug')
            rr = t1._mul_sparse_matrix(t2)
            return norm(rr.toarray().flatten() - self.d, inf)

    def _Prepare(self):
        if self._isPrepared:
            return
        self._isPrepared = True
        if isinstance(self.d, dict):
            self.x0 = self.d
        MatrixProblem._Prepare(self)
        if self.isFDmodel:
            equations = self.C
            AsSparse = bool(self.useSparse) if type(self.useSparse) != str else self._useSparse()
            C, d = [], []
            if len(self._fixedVars) < len(self._freeVars):
                Z = dict([ (v, zeros_like(self._x0[v]) if v not in self._fixedVars else self._x0[v]) for v in self._x0.keys() ])
            else:
                Z = dict([ (v, zeros_like(self._x0[v]) if v in self._freeVars else self._x0[v]) for v in self._x0.keys() ])
            for lin_oofun in equations:
                if lin_oofun.getOrder(self.freeVars, self.fixedVars) > 1:
                    raise OpenOptException('SLE constructor requires all equations to be linear')
                C.append(self._pointDerivative2array(lin_oofun.D(Z, **self._D_kwargs), useSparse=AsSparse))
                d.append(-lin_oofun(Z))

            self.d = hstack(d).flatten()
            self.C = Vstack(C)
            if hasattr(self.C, 'tocsc'):
                self.C_as_csc = self.C.tocsc()
            if isinstance(self.C, ndarray) and self.n > 100 and len(flatnonzero(self.C)) / self.C.size < 0.3:
                s = "Probably you'd better solve this SLE as sparse"
                if not scipyInstalled:
                    s += ' (requires scipy installed)'
                self.pWarn(s)
        self.x0 = zeros(self.C.shape[1])