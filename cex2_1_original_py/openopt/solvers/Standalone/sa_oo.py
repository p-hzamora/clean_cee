# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\Standalone\sa_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt.kernel.baseSolver import baseSolver
from openopt.kernel.setDefaultIterFuncs import SMALL_DELTA_X, SMALL_DELTA_F, MAX_NON_SUCCESS
from .tsp import main

class sa(baseSolver):
    __name__ = 'sa'
    __license__ = 'BSD'
    __authors__ = 'John Montgomery, connected to OO by Dmitrey'
    __alg__ = 'simulated annealing'
    __license__ = 'Creative Commons Attribution 3.0 Unported'
    iterfcnConnected = True
    __homepage__ = ''
    __info__ = ''
    __isIterPointAlwaysFeasible__ = True

    def __solver__(self, p):
        p.kernelIterFuncs.pop(SMALL_DELTA_X, None)
        p.kernelIterFuncs.pop(SMALL_DELTA_F, None)
        p.kernelIterFuncs.pop(MAX_NON_SUCCESS, None)
        p._bestPoint = p.point(p.x0)
        p.solver._requiresBestPointDetection = True
        M = p.M
        iterations, score, best = main(M, p)
        p.ff = p.fk = score
        p.xk = p.xf = best
        if p.istop == 0:
            p.istop = 1000
        return