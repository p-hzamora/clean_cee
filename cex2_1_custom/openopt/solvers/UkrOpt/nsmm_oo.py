# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\UkrOpt\nsmm_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import asfarray, argmax, inf, log10, max
from numpy.linalg import norm
from openopt.kernel.baseSolver import baseSolver
from openopt import NSP
from string import rjust

class nsmm(baseSolver):
    __name__ = 'nsmm'
    __license__ = 'BSD'
    __authors__ = 'Dmitrey Kroshko'
    __alg__ = 'based on Naum Z. Shor r-alg'
    iterfcnConnected = True
    __optionalDataThatCanBeHandled__ = ['A', 'Aeq', 'b', 'beq', 'lb', 'ub', 'c', 'h']
    __info__ = '\n    Solves mini-max problem\n    via minimizing max (F[i]) using NSP solver (default UkrOpt.ralg).\n\n    Can handle user-supplied gradient/subradient (p.df field)\n    If the one is not available -\n    splitting equations to separate functions is recommended\n    (to speedup calculations):\n    f = [func1, func2, ...] or f = ([func1, func2, ...)\n    '

    def __init__(self):
        pass

    def __solver__(self, p):
        f = lambda x: max(p.f(x))

        def df(x):
            F = p.f(x)
            ind = argmax(F)
            return p.df(x, ind)

        def iterfcn(*args, **kwargs):
            p2.primalIterFcn(*args, **kwargs)
            p.xk = p2.xk.copy()
            p.fk = p2.fk
            p.rk = p2.rk
            p.istop = p2.istop
            if p.istop and p2.rk <= p2.contol:
                p.msg = p2.msg
            p.iterfcn()

        p2 = NSP(f, p.x0, df=df, xtol=p.xtol, ftol=p.ftol, gtol=p.gtol, A=p.A, b=p.b, Aeq=p.Aeq, beq=p.beq, lb=p.lb, ub=p.ub, maxFunEvals=p.maxFunEvals, fEnough=p.fEnough, maxIter=p.maxIter, iprint=-1, maxtime=p.maxTime, maxCPUTime=p.maxCPUTime, noise=p.noise)
        if p.userProvided.c:
            p2.c, p2.dc = p.c, p.dc
        if p.userProvided.h:
            p2.h, p2.dh = p.h, p.dh
        p2.primalIterFcn, p2.iterfcn = p2.iterfcn, iterfcn
        r2 = p2.solve('ralg')
        xf = r2.xf
        p.xk = p.xf = xf
        p.fk = p.ff = max(p.f(xf))