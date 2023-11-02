# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\SOCP.pyc
# Compiled at: 2012-12-08 11:04:59
from baseProblem import MatrixProblem
from numpy import asfarray, ones, inf, dot, asfarray, nan, zeros, isfinite, all, asscalar

class SOCP(MatrixProblem):
    probType = 'SOCP'
    _optionalData = ['A', 'Aeq', 'b', 'beq', 'lb', 'ub']
    goal = 'minimum'
    allowedGoals = ['minimum', 'min']
    showGoal = True
    expectedArgs = ['f', 'C', 'd']

    def __init__(self, *args, **kwargs):
        MatrixProblem.__init__(self, *args, **kwargs)
        self.f = asfarray(self.f)
        self.n = self.f.size
        if self.x0 is None:
            self.x0 = zeros(self.n)
        return

    def objFunc(self, x):
        return asscalar(dot(self.f, x))