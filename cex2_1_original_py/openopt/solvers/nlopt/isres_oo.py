# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\nlopt\isres_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from NLOPT_AUX import NLOPT_AUX
from NLOPT_BASE import NLOPT_BASE
import nlopt

class isres(NLOPT_BASE):
    __name__ = 'isres'
    __alg__ = 'Improved Stochastic Ranking Evolution Strategy'
    __authors__ = 'S. G. Johnson'
    __optionalDataThatCanBeHandled__ = [
     'lb', 'ub', 'A', 'Aeq', 'b', 'beq', 'c', 'h']
    funcForIterFcnConnection = 'f'
    population = 0
    __isIterPointAlwaysFeasible__ = True
    _requiresFiniteBoxBounds = True

    def __init__(self):
        pass

    def __solver__(self, p):
        nlopt_opts = {'set_population': self.population} if self.population != 0 else {}
        if self.population != 0:
            p.f_iter = self.population
        NLOPT_AUX(p, nlopt.GN_ISRES, nlopt_opts)