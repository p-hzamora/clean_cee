# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\GLP.pyc
# Compiled at: 2012-12-08 11:04:59
from baseProblem import NonLinProblem
from numpy import asarray, ones, inf
from setDefaultIterFuncs import MAX_NON_SUCCESS

class GLP(NonLinProblem):
    probType = 'GLP'
    _optionalData = ['lb', 'ub', 'c', 'A', 'b']
    expectedArgs = ['f', 'x0']
    allowedGoals = ['minimum', 'min', 'maximum', 'max']
    goal = 'minimum'
    showGoal = False
    isObjFunValueASingleNumber = True
    plotOnlyCurrentMinimum = True
    _currentBestPoint = None
    _nonSuccessCounter = 0
    maxNonSuccess = 15

    def __init__(self, *args, **kwargs):
        NonLinProblem.__init__(self, *args, **kwargs)

        def maxNonSuccess(p):
            newPoint = p.point(p.xk)
            if self._currentBestPoint is None:
                self._currentBestPoint = newPoint
                return False
            else:
                if newPoint.betterThan(self._currentBestPoint):
                    self._currentBestPoint = newPoint
                    self._nonSuccessCounter = 0
                    return False
                else:
                    self._nonSuccessCounter += 1
                    if self._nonSuccessCounter > self.maxNonSuccess:
                        return (True, 'Non-Success Number > maxNonSuccess = ' + str(self.maxNonSuccess))
                    return False

                return

        self.kernelIterFuncs[MAX_NON_SUCCESS] = maxNonSuccess
        if 'lb' in kwargs.keys():
            self.n = len(kwargs['lb'])
        elif 'ub' in kwargs.keys():
            self.n = len(kwargs['ub'])
        if hasattr(self, 'n'):
            if not hasattr(self, 'lb'):
                self.lb = -inf * ones(self.n)
            if not hasattr(self, 'ub'):
                self.ub = inf * ones(self.n)
            if 'x0' not in kwargs.keys():
                self.x0 = (asarray(self.lb) + asarray(self.ub)) / 2.0