# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\LUNP.pyc
# Compiled at: 2012-12-08 11:04:59
from ooMisc import assignScript
from baseProblem import MatrixProblem
from numpy import asfarray, ones, inf, dot, nan, zeros, any, all, isfinite, eye, hstack, vstack, asarray, atleast_2d
from ooMisc import norm
import LP

class LUNP(MatrixProblem):
    probType = 'LUNP'
    goal = 'minimum'
    allowedGoals = ['minimum', 'min']
    showGoal = False
    _optionalData = []
    expectedArgs = ['C', 'd']

    def __init__(self, *args, **kwargs):
        MatrixProblem.__init__(self, *args, **kwargs)
        self.n = self.C.shape[1]
        if self.x0 is None:
            self.x0 = zeros(self.n)
        return

    def objFunc(self, x):
        r = norm(dot(self.C, x) - self.d, inf)
        return r

    def lunp2lp(self, solver, **solver_params):
        shapeC = atleast_2d(self.C).shape
        nVars = shapeC[1] + 1
        nObj = shapeC[0]
        f = hstack(zeros(nVars))
        f[-1] = 1
        p = LP.LP(f)
        if hasattr(self, 'x0'):
            p.x0 = self.x0
        self.inspire(p)
        p.x0 = hstack((p.x0, [0]))
        p.A = vstack((hstack((self.A, zeros((atleast_2d(self.A).shape[0], 1)))),
         hstack((self.C, -ones((nObj, 1)))),
         hstack((-self.C, -ones((nObj, 1))))))
        p.b = hstack((p.b, self.d, -self.d))
        p.lb = hstack((p.lb, -inf))
        p.ub = hstack((p.ub, inf))
        p.Aeq = hstack((self.Aeq, zeros((atleast_2d(self.Aeq).shape[0], 1))))
        self.iprint = -1
        r = p.solve(solver, **solver_params)
        self.xf, self.ff, self.rf = r.xf[:-1], r.ff, r.rf
        self.istop, self.msg = p.istop, p.msg
        return r