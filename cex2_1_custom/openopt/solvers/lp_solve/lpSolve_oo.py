# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\lp_solve\lpSolve_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from lp_solve import lp_solve as lps
from openopt.kernel.baseSolver import baseSolver
from numpy import asarray, inf, ones, nan, ravel
from openopt.kernel.ooMisc import LinConst2WholeRepr

def List(x):
    if x == None or x.size == 0:
        return
    return x.tolist()
    return


class lpSolve(baseSolver):
    __name__ = 'lpSolve'
    __license__ = 'LGPL'
    __authors__ = 'Michel Berkelaar, michel@es.ele.tue.nl'
    __homepage__ = 'http://sourceforge.net/projects/lpsolve, http://www.cs.sunysb.edu/~algorith/implement/lpsolve/implement.shtml, http://www.nabble.com/lp_solve-f14350i70.html'
    __alg__ = 'lpsolve'
    __info__ = 'use p.scale = 1 or True to turn scale mode on'
    __optionalDataThatCanBeHandled__ = ['A', 'Aeq', 'b', 'beq', 'lb', 'ub', 'intVars']

    def __init__(self):
        pass

    def __solver__(self, p):
        LinConst2WholeRepr(p)
        f = -asarray(p.f)
        scalemode = False
        if p.scale in [1, True]:
            scalemode = 1
        elif p.scale not in [None, 0, False]:
            p.warn(self.__name__ + ' requires p.scale from [None, 0, False, 1, True], other value obtained, so scale = 1 will be used')
            scalemode = 1
        obj, x_opt, duals = lps(List(f.flatten()), List(p.Awhole), List(p.bwhole.flatten()), List(p.dwhole.flatten()), List(p.lb.flatten()), List(p.ub.flatten()), (1 + asarray(p.intVars)).tolist(), scalemode)
        if obj != []:
            p.xf = ravel(x_opt)
            p.duals = duals
            p.istop = 1
        else:
            p.ff = nan
            p.xf = nan * ones(p.n)
            p.duals = []
            p.istop = -1
        return