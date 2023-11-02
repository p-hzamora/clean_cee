# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\QP.pyc
# Compiled at: 2012-12-08 11:04:59
import NLP
from ooMisc import isspmatrix
from baseProblem import MatrixProblem
from numpy import asfarray, dot, nan, zeros, isfinite, all, ravel

class QP(MatrixProblem):
    probType = 'QP'
    goal = 'minimum'
    allowedGoals = ['minimum', 'min']
    showGoal = False
    _optionalData = ['A', 'Aeq', 'b', 'beq', 'lb', 'ub', 'QC', 'intVars']
    expectedArgs = ['H', 'f']

    def _Prepare(self):
        self.n = self.H.shape[0]
        if not hasattr(self, 'x0') or self.x0 is None or self.x0[0] == nan:
            self.x0 = zeros(self.n)
        MatrixProblem._Prepare(self)
        return

    def __init__(self, *args, **kwargs):
        MatrixProblem.__init__(self, *args, **kwargs)
        if len(args) > 1 or 'f' in kwargs.keys():
            self.f = ravel(self.f)
            self.n = self.f.size
        if len(args) > 0 or 'H' in kwargs.keys():
            if not isspmatrix(self.H):
                self.H = asfarray(self.H, float)

    def objFunc(self, x):
        return asfarray(0.5 * dot(x, self.matMultVec(self.H, x)) + dot(self.f, x).sum()).flatten()

    def qp2nlp(self, solver, **solver_params):
        if hasattr(self, 'x0'):
            p = NLP.NLP(ff, self.x0, df=dff, d2f=d2ff)
        else:
            p = NLP.NLP(ff, zeros(self.n), df=dff, d2f=d2ff)
        p.args.f = self
        p.iprint = self.iprint
        self.inspire(p)
        self.iprint = -1
        p.show = self.show
        p.plot, self.plot = self.plot, 0
        r = p.solve(solver, **solver_params)
        self.xf, self.ff, self.rf = r.xf, r.ff, r.rf
        return r


ff = lambda x, QProb: QProb.objFunc(x)

def dff(x, QProb):
    r = dot(QProb.H, x)
    if all(isfinite(QProb.f)):
        r += QProb.f
    return r


def d2ff(x, QProb):
    r = QProb.H
    return r