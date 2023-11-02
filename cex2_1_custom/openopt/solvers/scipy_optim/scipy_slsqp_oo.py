# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\scipy_optim\scipy_slsqp_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from scipy.optimize import fmin_slsqp
import openopt
from openopt.kernel.setDefaultIterFuncs import *
from openopt.kernel.ooMisc import WholeRepr2LinConst, xBounds2Matrix
from openopt.kernel.baseSolver import baseSolver
from numpy import *

class EmptyClass:
    pass


class scipy_slsqp(baseSolver):
    __name__ = 'scipy_slsqp'
    __license__ = 'BSD'
    __authors__ = 'Dieter Kraft, connected to scipy by Rob Falck, connected to OO by Dmitrey'
    __alg__ = 'Sequential Least SQuares Programming'
    __info__ = 'constrained NLP solver'
    __optionalDataThatCanBeHandled__ = ['A', 'Aeq', 'b', 'beq', 'lb', 'ub', 'c', 'h']

    def __init__(self):
        pass

    def __solver__(self, p):
        bounds = []
        if any(isfinite(p.lb)) or any(isfinite(p.ub)):
            ind_inf = where(p.lb == -inf)[0]
            p.lb[ind_inf] = -1e+50
            ind_inf = where(p.ub == inf)[0]
            p.ub[ind_inf] = 1e+50
            for i in range(p.n):
                bounds.append((p.lb[i], p.ub[i]))

        empty_arr = array(())
        empty_arr_n = array(()).reshape(0, p.n)
        if not p.userProvided.c:
            p.c = lambda x: empty_arr.copy()
            p.dc = lambda x: empty_arr_n.copy()
        if not p.userProvided.h:
            p.h = lambda x: empty_arr.copy()
            p.dh = lambda x: empty_arr_n.copy()
        C = lambda x: -hstack((p.c(x), p.matmult(p.A, x) - p.b))
        fprime_ieqcons = lambda x: -vstack((p.dc(x), p.A))
        H = lambda x: hstack((p.h(x), p.matmult(p.Aeq, x) - p.beq))
        fprime_eqcons = lambda x: vstack((p.dh(x), p.Aeq))
        x, fx, its, imode, smode = fmin_slsqp(p.f, p.x0, bounds=bounds, f_eqcons=H, f_ieqcons=C, full_output=1, iprint=-1, fprime=p.df, fprime_eqcons=fprime_eqcons, fprime_ieqcons=fprime_ieqcons, acc=p.contol, iter=p.maxIter)
        p.msg = smode
        if imode == 0:
            p.istop = 1000
        else:
            p.istop = -1000
        p.xk, p.fk = array(x), fx