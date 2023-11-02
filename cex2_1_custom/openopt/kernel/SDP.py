# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\SDP.pyc
# Compiled at: 2012-12-08 11:04:59
from baseProblem import MatrixProblem
from numpy import asfarray, ones, inf, dot, asfarray, nan, zeros, isfinite, all

class SDP(MatrixProblem):
    _optionalData = [
     'A', 'Aeq', 'b', 'beq', 'lb', 'ub', 'S', 'd']
    expectedArgs = ['f']
    goal = 'minimum'
    allowedGoals = [
     'minimum', 'min']
    showGoal = True

    def __init__(self, *args, **kwargs):
        self.probType = 'SDP'
        self.S = {}
        self.d = {}
        MatrixProblem.__init__(self, *args, **kwargs)
        self.f = asfarray(self.f)
        self.n = self.f.size
        if self.x0 is None:
            self.x0 = zeros(self.n)
        return

    def _Prepare(self):
        MatrixProblem._Prepare(self)
        if self.solver.__name__ in ('cvxopt_sdp', 'dsdp'):
            try:
                from cvxopt.base import matrix
                matrixConverter = lambda x: matrix(x, tc='d')
            except:
                self.err('cvxopt must be installed')

        else:
            matrixConverter = asfarray
        for i in self.S.keys():
            self.S[i] = matrixConverter(self.S[i])

        for i in self.d.keys():
            self.d[i] = matrixConverter(self.d[i])

    def __finalize__(self):
        MatrixProblem.__finalize__(self)
        if self.goal in ('max', 'maximum'):
            self.f = -self.f
            for fn in ['fk']:
                if hasattr(self, fn):
                    setattr(self, fn, -getattr(self, fn))

    def objFunc(self, x):
        return asfarray(dot(self.f, x).sum()).flatten()