# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\scipy_optim\scipy_fsolve_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from scipy.optimize import fsolve
from numpy import asfarray
from openopt.kernel.baseSolver import baseSolver

class scipy_fsolve(baseSolver):
    __name__ = 'scipy_fsolve'
    __license__ = 'BSD'
    __info__ = '\n    solves system of n non-linear equations with n variables.\n    '

    def __init__(self):
        pass

    def __solver__(self, p):
        xf = fsolve(p.f, p.x0, fprime=p.df, xtol=p.xtol, maxfev=p.maxFunEvals)
        p.istop = 1000
        p.iterfcn(xf)