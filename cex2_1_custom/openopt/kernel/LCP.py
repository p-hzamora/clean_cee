# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\LCP.pyc
# Compiled at: 2012-12-08 11:04:59
from ooMisc import assignScript
from nonOptMisc import isspmatrix
from baseProblem import MatrixProblem
from numpy import asarray, ones, inf, dot, nan, zeros, isnan, any, vstack, array, asfarray
from ooMisc import norm

class LCP(MatrixProblem):
    _optionalData = []
    expectedArgs = [
     'M', 'q']
    goal = 'solve'
    probType = 'LCP'
    allowedGoals = ['solve']
    showGoal = False

    def __init__(self, *args, **kwargs):
        MatrixProblem.__init__(self, *args, **kwargs)
        self.x0 = zeros(2 * len(self.q))

    def objFunc(self, x):
        return norm(dot(self.M, x[x.size / 2:]) + self.q - x[:x.size / 2], inf)