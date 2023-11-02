# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\scipy_optim\scipy_cobyla_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from scipy.optimize import fmin_cobyla
import openopt
from openopt.kernel.setDefaultIterFuncs import *
from openopt.kernel.ooMisc import WholeRepr2LinConst, xBounds2Matrix
from openopt.kernel.baseSolver import baseSolver
from numpy import inf, array, copy

class EmptyClass:
    pass


class scipy_cobyla(baseSolver):
    __name__ = 'scipy_cobyla'
    __license__ = 'BSD'
    __authors__ = 'undefined'
    __alg__ = 'Constrained Optimization BY Linear Approximation'
    __info__ = 'constrained NLP solver, no user-defined derivatives are handled'
    __optionalDataThatCanBeHandled__ = ['A', 'Aeq', 'b', 'beq', 'lb', 'ub', 'c', 'h']
    funcForIterFcnConnection = 'f'

    def __init__(self):
        pass

    def __solver__(self, p):
        xBounds2Matrix(p)
        p.cobyla = EmptyClass()
        if p.userProvided.c:
            p.cobyla.nc = p.c(p.x0).size
        else:
            p.cobyla.nc = 0
        if p.userProvided.h:
            p.cobyla.nh = p.h(p.x0).size
        else:
            p.cobyla.nh = 0
        det_arr = cumsum(array((p.cobyla.nc, p.cobyla.nh, p.b.size, p.beq.size, p.cobyla.nh, p.beq.size)))
        cons = []
        for i in range(det_arr[-1]):
            if i < det_arr[0]:
                c = lambda x, i=i: -p.c(x)[i]
            elif det_arr[0] <= i < det_arr[1]:
                j = i - det_arr[0]
                c = lambda x, j=j: p.h(x)[j]
            elif det_arr[1] <= i < det_arr[2]:
                j = i - det_arr[1]
                c = lambda x, j=j: p.b[j] - p.dotmult(p.A[j], x).sum()
            elif det_arr[2] <= i < det_arr[3]:
                j = i - det_arr[2]
                c = lambda x, j=j: p.dotmult(p.Aeq[j], x).sum() - p.beq[j]
            elif det_arr[3] <= i < det_arr[4]:
                j = i - det_arr[3]
                c = lambda x, j=j: -p.h(x)[j]
            elif det_arr[4] <= i < det_arr[5]:
                j = i - det_arr[4]
                c = lambda x, j=j: p.dotmult(p.Aeq[j], x).sum() - p.beq[j]
            else:
                p.err('error in connection cobyla to openopt')
            cons.append(c)

        xf = fmin_cobyla(p.f, p.x0, cons=tuple(cons), iprint=0, maxfun=p.maxFunEvals, rhoend=p.xtol)
        p.xk = xf
        p.fk = p.f(xf)
        p.istop = 1000