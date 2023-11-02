# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\NSP.pyc
# Compiled at: 2012-12-08 11:04:59
from ooMisc import assignScript
from baseProblem import NonLinProblem
from numpy import asarray, ones, inf

class NSP(NonLinProblem):
    _optionalData = [
     'A', 'Aeq', 'b', 'beq', 'lb', 'ub', 'c', 'h']
    expectedArgs = ['f', 'x0']
    probType = 'NSP'
    JacobianApproximationStencil = 3
    allowedGoals = ['minimum', 'min', 'maximum', 'max']
    showGoal = True

    def __init__(self, *args, **kwargs):
        self.goal = 'minimum'
        NonLinProblem.__init__(self, *args, **kwargs)