# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\scipy_optim\scipy_broyden2_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from scipy.optimize import broyden2
from numpy import asfarray
from openopt.kernel.baseSolver import baseSolver

class scipy_broyden2(baseSolver):
    __name__ = 'scipy_broyden2'
    __license__ = 'BSD'
    __alg__ = 'a quasi-Newton-Raphson method, updates the inverse Jacobian directly'
    __info__ = '\n    solves system of n non-linear equations with n variables. \n    '

    def __init__(self):
        pass

    def __solver__(self, p):
        p.xk = p.x0.copy()
        p.fk = asfarray(max(abs(p.f(p.x0)))).flatten()
        p.iterfcn()
        if p.istop:
            p.xf, p.ff = p.xk, p.fk
            return
        try:
            xf = broyden2(p.f, p.x0, iter=p.maxIter)
        except:
            p.istop = -1000
            return

        p.xk = p.xf = asfarray(xf)
        p.fk = p.ff = asfarray(max(abs(p.f(xf)))).flatten()
        p.istop = 1000
        p.iterfcn()