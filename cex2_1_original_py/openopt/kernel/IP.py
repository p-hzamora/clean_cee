# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\IP.pyc
# Compiled at: 2012-12-08 11:04:59
from baseProblem import NonLinProblem
from numpy import inf

class IP(NonLinProblem):
    probType = 'IP'
    goal = 'solution'
    allowedGoals = ['solution']
    showGoal = False
    _optionalData = []
    expectedArgs = ['f', 'domain']
    ftol = None

    def __init__(self, *args, **kwargs):
        NonLinProblem.__init__(self, *args, **kwargs)
        domain = args[1]
        self.x0 = dict([ (v, 0.5 * (val[0] + val[1])) for v, val in domain.items() ])
        self.constraints = [ v > bounds[0] for v, bounds in domain.items() ] + [ v < bounds[1] for v, bounds in domain.items() ]
        self._Residual = inf

    def objFunc(self, x):
        return 0