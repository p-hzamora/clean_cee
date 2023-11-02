# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\nlopt\stogo_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from NLOPT_AUX import NLOPT_AUX
from NLOPT_BASE import NLOPT_BASE
import nlopt
from numpy import isinf

class stogo(NLOPT_BASE):
    __name__ = 'stogo'
    __alg__ = ''
    __optionalDataThatCanBeHandled__ = ['lb', 'ub']
    __isIterPointAlwaysFeasible__ = lambda self, p: True
    _requiresFiniteBoxBounds = True
    funcForIterFcnConnection = 'f'
    useRand = True

    def __init__(self):
        pass

    def __solver__(self, p):
        p.maxNonSuccess = 10000000000.0
        p.maxIter = 10000000000.0
        if isinf(p.maxTime):
            s = 'currently due to some Python <-> C++ code connection issues \n            the solver stogo requires finite user-defined maxTime; \n            since you have not provided it, 15 sec will be used'
            p.pWarn(s)
            p.maxTime = 15
        solver = nlopt.GD_STOGO_RAND if self.useRand else nlopt.GD_STOGO
        NLOPT_AUX(p, solver)