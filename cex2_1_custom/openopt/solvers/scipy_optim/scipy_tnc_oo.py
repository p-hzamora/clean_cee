# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\scipy_optim\scipy_tnc_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from scipy.optimize.tnc import fmin_tnc
import scipy.optimize.tnc as tnc, openopt
from openopt.kernel.setDefaultIterFuncs import *
from openopt.kernel.ooMisc import WholeRepr2LinConst
from openopt.kernel.baseSolver import baseSolver

class scipy_tnc(baseSolver):
    __name__ = 'scipy_tnc'
    __license__ = 'BSD'
    __authors__ = 'Stephen G. Nash'
    __alg__ = 'undefined'
    __info__ = 'box-bounded NLP solver, can handle lb<=x<=ub constraints, some lb-ub coords can be +/- inf'
    __optionalDataThatCanBeHandled__ = ['lb', 'ub']
    __isIterPointAlwaysFeasible__ = lambda self, p: True

    def __init__(self):
        pass

    def __solver__(self, p):
        bounds = []
        for i in range(p.n):
            bounds.append((p.lb[i], p.ub[i]))

        messages = 0
        maxfun = p.maxFunEvals
        if maxfun > 100000000.0:
            p.warn('tnc cannot handle maxFunEvals > 1e8, the value will be used')
            maxfun = int(100000000.0)
        xf, nfeval, rc = fmin_tnc(p.f, x0=p.x0, fprime=p.df, args=(), approx_grad=0, bounds=bounds, messages=messages, maxfun=maxfun, ftol=p.ftol, xtol=p.xtol, pgtol=p.gtol)
        if rc in (tnc.INFEASIBLE, tnc.NOPROGRESS):
            istop = FAILED_WITH_UNIMPLEMENTED_OR_UNKNOWN_REASON
        elif rc == tnc.FCONVERGED:
            istop = SMALL_DELTA_F
        elif rc == tnc.XCONVERGED:
            istop = SMALL_DELTA_X
        elif rc == tnc.MAXFUN:
            istop = IS_MAX_FUN_EVALS_REACHED
        elif rc == tnc.LSFAIL:
            istop = IS_LINE_SEARCH_FAILED
        elif rc == tnc.CONSTANT:
            istop = IS_ALL_VARS_FIXED
        elif rc == tnc.LOCALMINIMUM:
            istop = SOLVED_WITH_UNIMPLEMENTED_OR_UNKNOWN_REASON
        else:
            p.err('unknown stop reason')
        msg = tnc.RCSTRINGS[rc]
        p.istop, p.msg = istop, msg
        p.xf = xf