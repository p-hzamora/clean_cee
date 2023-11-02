# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\ODE.pyc
# Compiled at: 2012-12-08 11:04:59
from baseProblem import NonLinProblem

class ODE(NonLinProblem):
    probType = 'ODE'
    goal = 'solution'
    allowedGoals = ['solution']
    showGoal = False
    _optionalData = []
    FuncDesignerSign = 'timeVariable'
    expectedArgs = ['equations', 'startPoint', 'timeVariable', 'times']
    ftol = None

    def __init__(self, *args, **kwargs):
        NonLinProblem.__init__(self, *args, **kwargs)
        domain, timeVariable, times = args[1:4]
        self.x0 = domain

    def objFunc(self, x):
        return 0