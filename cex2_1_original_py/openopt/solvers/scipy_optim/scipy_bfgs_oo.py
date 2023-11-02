# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\scipy_optim\scipy_bfgs_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from scipy.optimize import fmin_bfgs
from openopt.kernel.ooMisc import isSolved
from openopt.kernel.baseSolver import baseSolver

class scipy_bfgs(baseSolver):
    __name__ = 'scipy_bfgs'
    __license__ = 'BSD'
    __alg__ = 'BFGS'
    __info__ = 'unconstrained NLP solver'
    iterfcnConnected = True

    def __init__(self):
        pass

    def __solver__(self, p):

        def iterfcn(x):
            p.xk, p.fk = x, p.f(x)
            p.iterfcn()
            if p.istop:
                raise isSolved

        p.xk = p.xf = fmin_bfgs(p.f, p.x0, fprime=p.df, disp=0, gtol=p.gtol, maxiter=p.maxIter, callback=iterfcn)
        p.istop = 1000