# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\LLSP.pyc
# Compiled at: 2012-12-08 11:04:59
from baseProblem import MatrixProblem
from numpy import ones, inf, dot, zeros, any, all, isfinite, eye
from ooMisc import norm
import NLP

class LLSP(MatrixProblem):
    _optionalData = [
     'damp', 'X', 'c']
    expectedArgs = ['C', 'd']
    probType = 'LLSP'
    goal = 'minimum'
    allowedGoals = ['minimum', 'min']
    showGoal = False
    FuncDesignerSign = 'C'

    def __init__(self, *args, **kwargs):
        MatrixProblem.__init__(self, *args, **kwargs)
        if 'damp' not in kwargs.keys():
            self.damp = None
        if 'f' not in kwargs.keys():
            self.f = None
        if not self._isFDmodel():
            if len(args) > 0:
                self.n = args[0].shape[1]
            else:
                self.n = kwargs['C'].shape[1]
            if not hasattr(self, 'lb'):
                self.lb = -inf * ones(self.n)
            if not hasattr(self, 'ub'):
                self.ub = inf * ones(self.n)
            if self.x0 is None:
                self.x0 = zeros(self.n)
        elif type(self.C) not in (set, tuple, list):
            if 'is_oovar' not in dir(self.C):
                s = '\n                    Icorrect data type for LLSP constructor, \n                    first argument should be numpy ndarray, \n                    scipy sparse matrix, FuncDesigner oofun or list of oofuns'
                self.err(s)
            self.C = [
             self.C]
        return

    def objFunc(self, x):
        r = norm(self.matMultVec(self.C, x) - self.d) ** 2 / 2.0
        if self.damp is not None:
            r += self.damp * norm(x - self.X) ** 2 / 2.0
        if self.f is not None:
            r += dot(self.f, x)
        return r

    def llsp2nlp(self, solver, **solver_params):
        if hasattr(self, 'x0'):
            p = NLP.NLP(ff, self.x0, df=dff, d2f=d2ff)
        else:
            p = NLP.NLP(ff, zeros(self.n), df=dff, d2f=d2ff)
        p.args.f = self
        self.inspire(p)
        self.iprint = -1
        p.show = self.show
        p.plot, self.plot = self.plot, 0
        r = p.solve(solver, **solver_params)
        self.xf, self.ff, self.rf = r.xf, r.ff, r.rf
        return r

    def _Prepare(self):
        if isinstance(self.d, dict):
            self.x0 = self.d
        MatrixProblem._Prepare(self)
        if self.isFDmodel:
            self.C, self.d = self._linearOOFunsToMatrices(self.C)
        if self.damp is not None and (not hasattr(self, 'X') or not any(isfinite(self.X))):
            self.X = zeros(self.n)
        return


ff = lambda x, LLSPprob: LLSPprob.objFunc(x)

def dff(x, p):
    r = p.matMultVec(p.C.T, p.matMultVec(p.C, x) - p.d)
    if p.damp is not None and p.damp != 0:
        r += p.damp * (x - p.X)
    if p.f is not None and all(isfinite(p.f)):
        r += p.f
    return r


def d2ff(x, p):
    r = dot(p.C.T, p.C)
    if p.damp is not None:
        r += p.damp * eye(x.size)
    return r