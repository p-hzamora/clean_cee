# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: FuncDesigner\ooVar.pyc
# Compiled at: 2013-05-21 10:21:10
from numpy import asarray, empty, inf, any, array, asfarray, isscalar, ndarray, int16, int32, int64, float64, tile, vstack, searchsorted, logical_or, where, asanyarray, arange, log2, logical_and, ceil
import numpy as np
from FDmisc import FuncDesignerException, isPyPy
from ooFun import oofun, BooleanOOFun, AND, OR, NOT, EQUIVALENT
from ooarray import ooarray
from baseClasses import Stochastic
from boundsurf import boundsurf, surf
f_none = lambda *args, **kw: None

class oovar(oofun):
    is_oovar = True
    domain = None
    lb = -inf
    ub = inf
    _unnamedVarNumber = 1
    __hash__ = oofun.__hash__

    def __init__(self, name=None, *args, **kwargs):
        if len(args) > 0:
            raise FuncDesignerException('incorrect args number for oovar constructor')
        if name is None:
            self.name = 'unnamed_' + str(oovar._unnamedVarNumber)
            oovar._unnamedVarNumber += 1
        else:
            kwargs['name'] = name
        oofun.__init__(self, f_none, *args, **kwargs)
        return

    def _interval_(self, domain, dtype=float64):
        tmp = domain.get(self, None)
        if tmp is None:
            return
        else:
            if isinstance(tmp, ndarray) or isscalar(tmp):
                tmp = asarray(tmp, dtype)
                return (
                 tile(tmp, (2, 1)), True)
            else:
                infinum, supremum = tmp
                if type(infinum) in (list, tuple):
                    infinum = array(infinum, dtype)
                elif isscalar(infinum):
                    infinum = dtype(infinum)
                if type(supremum) in (list, tuple):
                    supremum = array(supremum, dtype)
                elif isscalar(supremum):
                    supremum = dtype(supremum)
                if self in domain.resolveSchedule:
                    return (vstack((infinum, supremum)), True)
                S = surf({self: 1.0}, 0)
                return (boundsurf(S, S, True, domain), True)

            return

    def _getFuncCalcEngine(self, x, **kwargs):
        if hasattr(x, 'xf'):
            if x.probType == 'MOP':
                s = 'evaluation of MOP result on arguments is unimplemented yet, use r.solutions'
                raise FuncDesignerException(s)
            return self._getFuncCalcEngine(x.xf, **kwargs)
        else:
            r = x.get(self, None)
            if r is not None:
                if isinstance(r, Stochastic):
                    sz = getattr(x, 'maxDistributionSize', 0)
                    if sz == 0:
                        s = '\n                    if one of function arguments is stochastic distribution \n                    without resolving into quantified value \n                    (e.g. uniform(-10,10) instead of uniform(-10,10, 100), 100 is number of point to emulate)\n                    then you should evaluate the function \n                    onto oopoint with assigned parameter maxDistributionSize'
                        raise FuncDesignerException(s)
                    if not r.quantified:
                        r = r._yield_quantified(sz)
                    r = r.copy()
                    r.stochDep = {self: 1}
                    r.maxDistributionSize = sz
                    if r.size > sz:
                        r.reduce(sz)
                    tmp = getattr(x, '_p', None)
                    if tmp is not None:
                        r._p = tmp
                return r
            r = x.get(self.name, None)
            if r is not None:
                return r
            s = "for oovar %s the point involved doesn't contain \n            neither name nor the oovar instance. \n            Maybe you try to get function value or derivative \n            in a point where value for an oovar is missing\n            or run optimization problem \n            without setting initial value for this variable in start point\n            " % self.name
            raise FuncDesignerException(s)
            return

    def nlh(self, Lx, Ux, p, dataType, other=None):
        T0, res, DefiniteRange = get_P(self, Lx, Ux, p, dataType, other, goal_is_nlh=True)
        if type(T0) == bool:
            assert len(res) == 0
            return (
             T0, {}, DefiniteRange)
        else:
            return (
             T0, {self: res}, DefiniteRange)

    def lh(self, Lx, Ux, p, dataType, other=None):
        T0, res, DefiniteRange = get_P(self, Lx, Ux, p, dataType, other, goal_is_nlh=False)
        if type(T0) == bool:
            assert len(res) == 0
            return (
             T0, {}, DefiniteRange)
        else:
            return (
             T0, {self: res}, DefiniteRange)

    __and__ = AND
    __or__ = OR
    __invert__ = NOT
    __ne__ = lambda self, arg: NOT(self == arg)

    def __eq__(self, other):
        if (self.domain is bool or self.domain is 'bool') and isinstance(other, (oovar, BooleanOOFun)):
            return EQUIVALENT(self, other)
        else:
            return oofun.__eq__(self, other)

    def formAuxDomain(self):
        if 'aux_domain' in self.__dict__:
            return
        self.domain = asanyarray(self.domain)
        d = self.domain
        if any(d[1:] < d[:-1]):
            d.sort()
        D = int(2 ** ceil(log2(d.size)))
        self.domain, self.aux_domain = arange(D), d


def oovars(*args, **kw):
    if isPyPy:
        raise FuncDesignerException("\n        for PyPy using oovars() is impossible yet. \n        You could use oovar(size=n), also \n        you can create list or tuple of oovars in a cycle, e.g.\n        a = [oovar('a'+str(i)) for i in range(100)]\n        but you should ensure you haven't operations like k*a or a+val in your code, \n        it may work in completely different way (e.g. k*a will produce Python list of k a instances)\n        ")
    lb = kw.pop('lb', None)
    ub = kw.pop('ub', None)
    if len(args) == 1:
        if type(args[0]) in (int, int16, int32, int64):
            r = ooarray([ oovar(**kw) for i in range(args[0]) ])
        elif type(args[0]) in [list, tuple]:
            r = ooarray([ oovar(name=args[0][i], **kw) for i in range(len(args[0])) ])
        else:
            if type(args[0]) == str:
                r = ooarray([ oovar(name=s, **kw) for s in args[0].split() ])
            else:
                raise FuncDesignerException('incorrect args number for oovars constructor')
    else:
        r = ooarray([ oovar(name=args[i], **kw) for i in range(len(args)) ])
    if lb is not None and (np.isscalar(lb) or isinstance(lb, np.ndarray) and lb.size == 1):
        for v in r.view(np.ndarray):
            v.lb = lb

    else:
        if not type(lb) in (list, tuple, ndarray):
            raise AssertionError
            for i, v in enumerate(r):
                v.lb = lb[i]

        if ub is not None and (np.isscalar(ub) or isinstance(ub, np.ndarray) and ub.size == 1):
            for v in r.view(np.ndarray):
                v.ub = ub

        else:
            if not type(ub) in (list, tuple, ndarray):
                raise AssertionError
                for i, v in enumerate(r):
                    v.ub = ub[i]

            r._is_array_of_oovars = True
            return r


def get_P(v, Lx, Ux, p, dataType, other=None, goal_is_nlh=True):
    DefiniteRange = True
    d = v.domain
    if d is None:
        raise FuncDesignerException('probably you are invoking boolean operation on continuous oovar')
    if d is int or d is 'int':
        raise FuncDesignerException('probably you are invoking boolean operation on non-boolean oovar')
    inds = p._oovarsIndDict.get(v, None)
    m = Lx.shape[0]
    if inds is None:
        res = {}
        if v.domain is bool or v.domain is 'bool':
            if goal_is_nlh:
                T0 = True if p._x0[v] == 1 else False
            else:
                T0 = False if p._x0[v] == 1 else True
        else:
            assert other is not None, 'bug in FD kernel: called nlh with incorrect domain type'
            if goal_is_nlh:
                T0 = False if p._x0[v] != other else True
            else:
                T0 = False if p._x0[v] == other else True
        return (
         T0, res, DefiniteRange)
    else:
        ind1, ind2 = inds
        assert ind2 - ind1 == 1, 'unimplemented for oovars of size > 1 yet'
        lx, ux = Lx[:, ind1], Ux[:, ind1]
        if d is bool or d is 'bool':
            T0 = empty(m)
            if goal_is_nlh:
                T0.fill(inf)
                T0[ux != lx] = 1.0
                T0[lx == 1.0] = 0.0
                T2 = vstack((where(lx == 1, 0, inf), where(ux == 1, 0, inf))).T
            else:
                T0.fill(0)
                T0[ux != lx] = 1.0
                T0[lx == 1.0] = inf
                T2 = vstack((where(lx == 1, inf, 0), where(ux == 1, inf, 0))).T
        else:
            assert other is not None, 'bug in FD kernel: called nlh with incorrect domain type'
            mx = 0.5 * (lx + ux)
            prev = 0
            if prev:
                ind = logical_and(mx == other, lx != ux)
                if any(ind):
                    p.pWarn('seems like a categorical variables bug in FuncDesigner kernel, inform developers')
                I = searchsorted(d, lx, 'right') - 1
                J = searchsorted(d, mx, 'right') - 1
                K = searchsorted(d, ux, 'right') - 1
                D0, D1, D2 = d[I], d[J], d[K]
                d1, d2 = D0, D1
                tmp1 = asfarray(J - I + 1 + where(d2 == other, 1, 0))
                tmp1[logical_or(other < d1, other > d2)] = inf
                d1, d2 = D1, D2
                tmp2 = asfarray(K - J + 1 + where(d2 == other, 1, 0))
                tmp2[logical_or(other < d1, other > d2)] = inf
                if goal_is_nlh:
                    T2 = log2(vstack((tmp1, tmp2)).T)
                else:
                    T2 = log2(vstack((tmp1, tmp2)).T)
                d1, d2 = D0, D2
                tmp = asfarray(K - I + where(d2 == other, 1, 0))
                tmp[logical_or(other < d1, other > d2)] = inf
                T0 = log2(tmp)
            else:
                assert np.all(d == array(d, int)) and len(d) == d[-1] - d[0] + 1, 'bug in FD kernel'
                assert goal_is_nlh, 'unimplemented yet'
                tmp = ux - lx
                tmp[other < lx] = inf
                tmp[other > ux] = inf
                tmp[logical_and(tmp == 0, other == lx)] = 0.0
                T0 = log2(tmp + 1)
                floor_mx = np.floor(mx)
                tmp1 = floor_mx - lx
                tmp1[other < lx] = inf
                tmp1[other > floor_mx] = inf
                tmp1[logical_and(tmp1 == 0, other == lx)] = 0.0
                ceil_mx = np.ceil(mx)
                tmp2 = ux - ceil_mx
                tmp2[other > ux] = inf
                tmp2[other < ceil_mx] = inf
                tmp2[logical_and(tmp2 == 0, other == ux)] = 0.0
                if goal_is_nlh:
                    T2 = log2(vstack((tmp1, tmp2)).T + 1.0)
                else:
                    assert 0, 'unimplemented yet'
        res = T2
        return (
         T0, res, DefiniteRange)