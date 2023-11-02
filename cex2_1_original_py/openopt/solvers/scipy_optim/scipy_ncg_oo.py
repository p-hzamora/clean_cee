# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\scipy_optim\scipy_ncg_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from scipy.optimize import fmin_ncg
from openopt.kernel.ooMisc import isSolved
from openopt.kernel.baseSolver import baseSolver

class scipy_ncg(baseSolver):
    __name__ = 'scipy_ncg'
    __license__ = 'BSD'
    __alg__ = 'Newton-CG'
    __info__ = 'unconstrained NLP solver, can handle 2nd derivatives'
    iterfcnConnected = True

    def __init__(self):
        pass

    def __solver__(self, p):

        def iterfcn(x):
            p.xk, p.fk = x, p.f(x)
            p.iterfcn()
            if p.istop:
                raise isSolved

        if p.userProvided.d2f:
            fhess = p.d2f
        else:
            fhess = None
        xf = fmin_ncg(p.f, p.x0, p.df, fhess=fhess, maxiter=p.maxIter + 15, disp=0, callback=iterfcn)
        ff = p.f(xf)
        p.istop = 1000
        p.xk = p.xf = xf
        p.fk = p.ff = ff
        return