# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\scipy_optim\scipy_lbfgsb_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from scipy.optimize.lbfgsb import fmin_l_bfgs_b
import openopt
from openopt.kernel.setDefaultIterFuncs import *
from openopt.kernel.ooMisc import WholeRepr2LinConst
from openopt.kernel.baseSolver import baseSolver

class scipy_lbfgsb(baseSolver):
    __name__ = 'scipy_lbfgsb'
    __license__ = 'BSD'
    __authors__ = 'Ciyou Zhu, Richard Byrd, and Jorge Nocedal <nocedal@ece.nwu.edu>,\n    connected to scipy by David M. Cooke <cookedm@physics.mcmaster.ca> and Travis Oliphant,\n    connected to openopt by Dmitrey'
    __alg__ = 'l-bfgs-b'
    __info__ = 'box-bounded limited-memory NLP solver, can handle lb<=x<=ub constraints, some lb-ub coords can be +/- inf'
    __optionalDataThatCanBeHandled__ = ['lb', 'ub']
    __isIterPointAlwaysFeasible__ = lambda self, p: True

    def __init__(self):
        pass

    def __solver__(self, p):
        bounds = []

        def BOUND(x):
            if isfinite(x):
                return x
            else:
                return
                return

        for i in range(p.n):
            bounds.append((BOUND(p.lb[i]), BOUND(p.ub[i])))

        xf, ff, d = fmin_l_bfgs_b(p.f, p.x0, fprime=p.df, approx_grad=0, bounds=bounds, iprint=p.iprint, maxfun=p.maxFunEvals)
        if d['warnflag'] in (0, 2):
            istop = SOLVED_WITH_UNIMPLEMENTED_OR_UNKNOWN_REASON
            if d['warnflag'] == 0:
                msg = 'converged'
        elif d['warnflag'] == 1:
            istop = IS_MAX_FUN_EVALS_REACHED
        p.xk = p.xf = xf
        p.fk = p.ff = ff
        p.istop = istop
        p.iterfcn()