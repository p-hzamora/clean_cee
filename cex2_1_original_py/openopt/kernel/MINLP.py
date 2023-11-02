# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\MINLP.pyc
# Compiled at: 2012-12-08 11:04:59
from ooMisc import assignScript
from baseProblem import NonLinProblem
from numpy import asarray, ones, inf, array, sort, ndarray

class MINLP(NonLinProblem):
    _optionalData = [
     'A', 'Aeq', 'b', 'beq', 'lb', 'ub', 'c', 'h', 'discreteVars']
    probType = 'MINLP'
    allowedGoals = ['minimum', 'min', 'maximum', 'max']
    showGoal = True
    plotOnlyCurrentMinimum = True
    discrtol = 1e-05
    expectedArgs = ['f', 'x0']

    def __init__(self, *args, **kwargs):
        self.goal = 'minimum'
        self.discreteVars = {}
        NonLinProblem.__init__(self, *args, **kwargs)
        self.iprint = 1

    def _Prepare(self):
        if hasattr(self, 'prepared') and self.prepared == True:
            return
        else:
            NonLinProblem._Prepare(self)
            if self.isFDmodel:
                r = {}
                for iv in self.freeVars:
                    if iv.domain is None:
                        continue
                    ind1, ind2 = self._oovarsIndDict[iv]
                    assert ind2 - ind1 == 1
                    r[ind1] = iv.domain

                self.discreteVars = r
            for key in self.discreteVars.keys():
                fv = self.discreteVars[key]
                if type(fv) not in [list, tuple, ndarray] and fv not in ('bool', bool):
                    self.err('each element from discreteVars dictionary should be list or tuple of allowed values')
                if fv is not bool and fv is not 'bool':
                    fv = sort(fv)
                lowest = 0 if fv is bool or fv is 'bool' else fv[0]
                biggest = 1 if fv is bool or fv is 'bool' else fv[-1]
                if lowest > self.ub[key]:
                    self.err('variable ' + str(key) + ': smallest allowed discrete value ' + str(fv[0]) + ' exeeds imposed upper bound ' + str(self.ub[key]))
                if biggest < self.lb[key]:
                    self.err('variable ' + str(key) + ': biggest allowed discrete value ' + str(fv[-1]) + ' is less than imposed lower bound ' + str(self.lb[key]))
                self.discreteVars[key] = fv

            return