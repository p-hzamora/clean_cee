# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\baseSolver.pyc
# Compiled at: 2012-12-08 11:04:59
__docformat__ = 'restructuredtext en'
from numpy import asarray, copy, ravel, isnan, where, isscalar, asscalar
from openopt.kernel.Point import Point

class baseSolver:

    def __init__(self):
        pass

    __name__ = 'Undefined. If you are a user and got the message, inform developers please.'
    __license__ = 'Undefined. If you are a user and got the message, inform developers please.'
    __authors__ = 'Undefined. If you are a user and got the message, inform developers please.'
    __alg__ = 'Undefined'
    __solver__ = 'Undefined. If you are a user and got the message, inform developers please.'
    __homepage__ = 'Undefined. Use web search'
    __info__ = 'None'
    _requiresBestPointDetection = False
    _requiresFiniteBoxBounds = False
    useStopByException = True
    __optionalDataThatCanBeHandled__ = []
    __isIterPointAlwaysFeasible__ = lambda self, p: p.isUC
    iterfcnConnected = False
    funcForIterFcnConnection = 'df'
    _canHandleScipySparse = False
    properTextOutput = False
    useLinePoints = False
    __expectedArgs__ = [
     'xk', 'fk', 'rk']

    def __decodeIterFcnArgs__(self, p, *args, **kwargs):
        """
        decode and assign x, f, maxConstr
        (and/or other fields) to p.iterValues
        """
        fArg = True
        if len(args) > 0 and isinstance(args[0], Point):
            if len(args) != 1:
                p.err('incorrect iterfcn args, if you see this contact OO developers')
            point = args[0]
            p.xk, p.fk = point.x, point.f()
            p.rk, p.rtk, p.rik = point.mr(True)
            p.nNaNs = point.nNaNs()
            if p.solver._requiresBestPointDetection and (p.iter == 0 or point.betterThan(p._bestPoint)):
                p._bestPoint = point
        else:
            if len(args) > 0:
                p.xk = args[0]
            elif 'xk' in kwargs.keys():
                p.xk = kwargs['xk']
            elif not hasattr(p, 'xk'):
                p.err('iterfcn must get x value, if you see it inform oo developers')
            if p._baseClassName == 'NonLin':
                C = p.c(p.xk)
                H = p.h(p.xk)
                p.nNaNs = len(where(isnan(C))[0]) + len(where(isnan(H))[0])
            if p.solver._requiresBestPointDetection:
                currPoint = p.point(p.xk)
                if p.iter == 0 or currPoint.betterThan(p._bestPoint):
                    p._bestPoint = currPoint
            if len(args) > 1:
                p.fk = args[1]
            elif 'fk' in kwargs.keys():
                p.fk = kwargs['fk']
            else:
                fArg = False
            if len(args) > 2:
                p.rk = args[2]
            elif 'rk' in kwargs.keys():
                p.rk = kwargs['rk']
            else:
                p.rk, p.rtk, p.rik = p.getMaxResidual(p.xk, True)
        p.iterValues.r.append(ravel(p.rk)[0])
        if p.probType != 'IP':
            p.rk, p.rtk, p.rik = p.getMaxResidual(p.xk, True)
            p.iterValues.rt.append(p.rtk)
            p.iterValues.ri.append(p.rik)
        if p._baseClassName == 'NonLin':
            p.iterValues.nNaNs.append(p.nNaNs)
        p.iterValues.x.append(copy(p.xk))
        if not p.storeIterPoints and len(p.iterValues.x) > 2:
            p.iterValues.x.pop(0)
        if not fArg:
            p.Fk = p.F(p.xk)
            p.fk = copy(p.Fk)
        elif asarray(p.fk).size > 1:
            if p.debug and p.iter <= 1:
                p.warn('please fix solver iter output func, objFuncVal should be single number (use p.F)')
            p.Fk = p.objFuncMultiple2Single(asarray(p.fk))
        else:
            p.Fk = p.fk
        v = ravel(p.Fk)[0]
        if p.invertObjFunc:
            v = -v
        p.iterValues.f.append(v)
        if not isscalar(p.fk) and p.fk.size == 1:
            p.fk = asscalar(p.fk)