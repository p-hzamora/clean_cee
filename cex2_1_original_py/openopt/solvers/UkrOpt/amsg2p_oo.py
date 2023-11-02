# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\UkrOpt\amsg2p_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt.kernel.baseSolver import *
from numpy import isfinite
from amsg2p import amsg2p as Solver

class amsg2p(baseSolver):
    __name__ = 'amsg2p'
    __license__ = 'BSD'
    __authors__ = 'Dmitrey'
    __alg__ = 'Petro I. Stetsyuk, amsg2p'
    __optionalDataThatCanBeHandled__ = []
    iterfcnConnected = True
    showRes = False
    show_nnan = False
    gamma = 1.0

    def __init__(self):
        pass

    def __solver__(self, p):
        if not p.isUC:
            p.warn('Handling of constraints is not implemented properly for the solver %s yet' % self.__name__)
        if p.fOpt is None:
            if not isfinite(p.fEnough):
                p.err('the solver %s requires providing optimal value fOpt')
            else:
                p.warn("you haven't provided optimal value fOpt for the solver %s; fEnough = %0.2e will be used instead" % (self.__name__, p.fEnough))
                p.fOpt = p.fEnough
        if p.fTol is None:
            s = '\n            the solver %s requires providing required objective function tolerance fTol\n            15*ftol = %0.1e will be used instead\n            ' % (self.__name__, p.ftol)
            p.pWarn(s)
            fTol = 15 * p.ftol
        else:
            fTol = p.fTol

        def itefcn(*args, **kwargs):
            p.iterfcn(*args, **kwargs)
            return p.istop

        x, itn = Solver(p.f, p.df, p.x0, fTol, p.fOpt, self.gamma, itefcn)
        if p.f(x) < p.fOpt + fTol:
            p.istop = 10
        return