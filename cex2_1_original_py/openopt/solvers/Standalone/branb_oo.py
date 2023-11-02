# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\Standalone\branb_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt.kernel.baseSolver import baseSolver
from openopt.kernel.ooMisc import isSolved
from openopt.kernel.setDefaultIterFuncs import IS_NAN_IN_X, SMALL_DELTA_X, SMALL_DELTA_F
from numpy import *
from openopt import NLP, OpenOptException

class branb(baseSolver):
    __name__ = 'branb'
    __license__ = 'BSD'
    __authors__ = 'Ingar Solberg, Institutt for teknisk kybernetikk, Norges Tekniske Hrgskole, Norway, translated to Python by Dmitrey'
    __homepage__ = ''
    __alg__ = 'branch-and-cut (currently the implementation is quite primitive)'
    __info__ = ''
    __optionalDataThatCanBeHandled__ = ['A', 'Aeq', 'b', 'beq', 'lb', 'ub', 'discreteVars', 'c', 'h']
    iterfcnConnected = True
    __isIterPointAlwaysFeasible__ = lambda self, p: True
    nlpSolver = None

    def __init__(self):
        pass

    def __solver__(self, p):
        if self.nlpSolver is None:
            p.err('you should explicitely provide parameter nlpSolver (name of NLP solver to use for NLP subproblems)')
        for key in [IS_NAN_IN_X, SMALL_DELTA_X, SMALL_DELTA_F]:
            if key in p.kernelIterFuncs.keys():
                p.kernelIterFuncs.pop(key)

        p.nlpSolver = self.nlpSolver
        startPoint = p.point(p.x0)
        startPoint._f = inf
        fPoint = fminconset(p, startPoint, p)
        p.iterfcn(fPoint)
        p.istop = 1000
        return


def fminconset(p_current, bestPoint, p):
    p2 = milpTransfer(p)
    p2.lb, p2.ub = p_current.lb, p_current.ub
    try:
        r = p2.solve(p.nlpSolver)
        curr_NLP_Point = p.point(r.xf)
        curr_NLP_Point._f = r.ff
    except OpenOptException:
        r = None

    resultPoint = p.point(bestPoint.x)
    if r is None or r.istop < 0 or curr_NLP_Point.f() >= bestPoint.f():
        resultPoint._f = inf
        return resultPoint
    else:
        if r.istop == 0:
            pass
        x = curr_NLP_Point.x
        k = -1
        for i in p.discreteVars.keys():
            if not any(abs(x[i] - p.discreteVars[i]) < p.discrtol):
                k = i
                break

        if k != -1:
            p.debugmsg('k=' + str(k) + ' x[k]=' + str(x[k]) + ' p.discreteVars[k]=' + str(p.discreteVars[k]))
            Above = where(p.discreteVars[k] > x[k])[0]
            Below = where(p.discreteVars[k] < x[k])[0]
            resultPoint._f = inf
        else:
            if curr_NLP_Point.f() < bestPoint.f():
                bestPoint = curr_NLP_Point
            p.iterfcn(curr_NLP_Point)
            if p.istop:
                if bestPoint.betterThan(curr_NLP_Point):
                    p.iterfcn(bestPoint)
                raise isSolved
            return curr_NLP_Point
        if Below.size != 0:
            below = Below[-1]
            p3 = milpTransfer(p)
            p3.x0 = x.copy()
            ub1 = p_current.ub.copy()
            ub1[k] = min((ub1[k], p.discreteVars[k][below]))
            ub1[k] = p.discreteVars[k][below]
            p3.ub = ub1
            p3.lb = p_current.lb
            Point_B = fminconset(p3, bestPoint, p)
            resultPoint = Point_B
            if p.discreteConstraintsAreSatisfied(Point_B.x) and Point_B.betterThan(bestPoint):
                bestPoint = Point_B
        if Above.size != 0:
            above = Above[0]
            p4 = milpTransfer(p)
            p4.x0 = x.copy()
            lb1 = p_current.lb.copy()
            lb1[k] = max((lb1[k], p.discreteVars[k][above]))
            lb1[k] = p.discreteVars[k][above]
            p4.lb = lb1
            p4.ub = p_current.ub
            Point_A = fminconset(p4, bestPoint, p)
            resultPoint = Point_A
            if p.discreteConstraintsAreSatisfied(Point_A.x) and Point_A.betterThan(bestPoint):
                bestPoint = Point_A
        if Below.size != 0 and Above.size != 0:
            if Point_A.f() < Point_B.f():
                resultPoint = Point_A
            else:
                resultPoint = Point_B
        return resultPoint


def milpTransfer(originProb):
    newProb = NLP(originProb.f, originProb.x0)
    originProb.inspire(newProb)
    newProb.discreteVars = originProb.discreteVars

    def err(s):
        raise OpenOptException(s)

    newProb.err = err
    for fn in ['df', 'd2f', 'c', 'dc', 'h', 'dh']:
        if hasattr(originProb, fn) and getattr(originProb.userProvided, fn) or originProb.isFDmodel:
            setattr(newProb, fn, getattr(originProb, fn))

    newProb.plot = 0
    newProb.iprint = -1
    newProb.nlpSolver = originProb.nlpSolver
    return newProb