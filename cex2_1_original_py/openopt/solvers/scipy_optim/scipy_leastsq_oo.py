# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\scipy_optim\scipy_leastsq_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from scipy.optimize import leastsq
from numpy import asfarray
from openopt.kernel.baseSolver import baseSolver

class scipy_leastsq(baseSolver):
    __name__ = 'scipy_leastsq'
    __license__ = 'BSD'
    __info__ = "\n    MINPACK's lmdif and lmder algorithms\n    "

    def __init__(self):
        pass

    def __solver__(self, p):
        p.xk = p.x0.copy()
        p.fk = asfarray(p.f(p.x0) ** 2).sum().flatten()
        p.iterfcn()
        if p.istop:
            p.xf, p.ff = p.xk, p.fk
            return
        if p.userProvided.df:
            xf, cov_x, infodict, mesg, ier = leastsq(p.f, p.x0, Dfun=p.df, xtol=p.xtol, ftol=p.ftol, maxfev=p.maxFunEvals, full_output=1)
        else:
            xf, cov_x, infodict, mesg, ier = leastsq(p.f, p.x0, xtol=p.xtol, maxfev=p.maxFunEvals, epsfcn=p.diffInt, ftol=p.ftol, full_output=1)
        if ier == 1:
            p.istop = 1000
        else:
            p.istop = -1000
        p.msg = mesg
        ff = asfarray(p.f(xf) ** 2).sum().flatten()
        p.xk = xf
        p.fk = ff
        p.xf = xf
        p.ff = ff
        p.iterfcn()