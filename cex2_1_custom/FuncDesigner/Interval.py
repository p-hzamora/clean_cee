# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: FuncDesigner\Interval.pyc
# Compiled at: 2013-05-21 10:21:10
from numpy import ndarray, asscalar, isscalar, floor, pi, inf, nan, copy as Copy, logical_and, logical_or, where, asarray, any, all, atleast_1d, vstack, searchsorted, logical_not
import numpy as np
from FDmisc import FuncDesignerException, Diag
from FuncDesigner.multiarray import multiarray
from boundsurf import boundsurf, surf
try:
    from bottleneck import nanmin, nanmax
except ImportError:
    from numpy import nanmin, nanmax

class Interval:

    def __init__(self, l, u, definiteRange):
        if isinstance(l, ndarray) and l.size == 1:
            l = asscalar(l)
        if isinstance(u, ndarray) and u.size == 1:
            u = asscalar(u)
        self.lb, self.ub, self.definiteRange = l, u, definiteRange

    def __str__(self):
        return 'FuncDesigner interval with lower bound %s and upper bound %s' % (self.lb, self.ub)

    def __repr__(self):
        return str(self)


def ZeroCriticalPoints(lb_ub):
    arg_infinum, arg_supremum = lb_ub[0], lb_ub[1]
    if isscalar(arg_infinum):
        if arg_infinum < 0.0 < arg_supremum:
            return [0.0]
        return []
    tmp = Copy(arg_infinum)
    tmp[atleast_1d(logical_and(arg_infinum < 0.0, arg_supremum > 0.0))] = 0.0
    return [tmp]


def TrigonometryCriticalPoints(lb_ub):
    arg_infinum, arg_supremum = lb_ub[0], lb_ub[1]
    arrN = asarray(atleast_1d(floor(2 * arg_infinum / pi)), int)
    Tmp = []
    for i in range(1, 6):
        th = (arrN + i) * pi / 2
        ind = logical_and(arg_infinum < th, th < arg_supremum)
        if not any(ind):
            break
        tmp = atleast_1d(Copy(arg_infinum))
        tmp[atleast_1d(ind)] = asarray((arrN[ind] + i) * pi / 2, dtype=tmp.dtype)
        Tmp.append(tmp)

    return Tmp


def ZeroCriticalPointsInterval(inp, func):
    is_abs = func == np.abs
    is_cosh = func == np.cosh

    def interval(domain, dtype):
        allowBoundSurf = is_abs or is_cosh
        lb_ub, definiteRange = inp._interval(domain, dtype, allowBoundSurf=allowBoundSurf)
        if type(lb_ub) == boundsurf:
            if is_abs:
                return lb_ub.abs()
            if is_cosh:
                return defaultIntervalEngine(lb_ub, func, np.sinh, np.nan, 1, 0.0, 1.0)
            assert 0, 'bug or unimplemented yet'
        lb, ub = lb_ub[0], lb_ub[1]
        ind1, ind2 = lb < 0.0, ub > 0.0
        ind = logical_and(ind1, ind2)
        tmp = vstack((lb, ub))
        TMP = func(tmp)
        t_min, t_max = atleast_1d(nanmin(TMP, 0)), atleast_1d(nanmax(TMP, 0))
        if any(ind):
            F0 = func(0.0)
            t_min[atleast_1d(logical_and(ind, t_min > F0))] = F0
            t_max[atleast_1d(logical_and(ind, t_max < F0))] = F0
        return (
         vstack((t_min, t_max)), definiteRange)

    return interval


def nonnegative_interval(inp, func, deriv, domain, dtype, F0, shift=0.0):
    is_arccosh = func == np.arccosh
    is_sqrt = func == np.sqrt
    is_log = func in (np.log, np.log2, np.log10, np.log1p)
    if not (is_arccosh or is_sqrt or is_log):
        raise AssertionError('unimplemented yet')
        lb_ub, definiteRange = inp._interval(domain, dtype, allowBoundSurf=True)
        isBoundSurf = type(lb_ub) == boundsurf
        if isBoundSurf and (is_sqrt or is_log):
            r, definiteRange = defaultIntervalEngine(lb_ub, func, deriv, monotonity=1, convexity=-1, feasLB=0.0)
            return (
             r, r.definiteRange)
        if is_arccosh:
            r, definiteRange = defaultIntervalEngine(lb_ub, func, deriv, monotonity=1, convexity=-1, feasLB=1.0)
            return (
             r, r.definiteRange)
        lb_ub_resolved = lb_ub.resolve()[0]
    else:
        lb_ub_resolved = lb_ub
    lb, ub = lb_ub_resolved[0], lb_ub_resolved[1]
    th = shift
    ind = where(lb < th)[0]
    if ind.size != 0:
        lb_ub_resolved = lb_ub_resolved.copy()
        lb_ub_resolved[0][logical_and(ind, ub >= th)] = th
        if definiteRange is not False:
            if type(definiteRange) != np.ndarray:
                definiteRange = np.empty_like(lb, bool)
                definiteRange.fill(True)
            definiteRange[ind] = False
    r = func(lb_ub_resolved)
    return (
     r, definiteRange)


def box_1_interval(inp, func, deriv, domain, dtype):
    assert func in (np.arcsin, np.arccos, np.arctanh)
    lb_ub, definiteRange = inp._interval(domain, dtype, allowBoundSurf=True)
    isBoundSurf = type(lb_ub) == boundsurf
    lb_ub_resolved = lb_ub.resolve()[0] if isBoundSurf else lb_ub
    if isBoundSurf:
        isNegative = all(lb_ub_resolved <= 0)
        isPositive = all(lb_ub_resolved >= 0)
        if isNegative or isPositive:
            assert func in (np.arcsin, np.arccos, np.arctanh)
            monotonity = 1 if func in (np.arcsin, np.arctanh) else -1
            convexity = 1 if (func in (np.arcsin, np.arctanh)) == isPositive else -1
            return defaultIntervalEngine(lb_ub, func, deriv, monotonity, convexity, feasLB=-1.0, feasUB=1.0)
    lb_ub_resolved, definiteRange = adjustBounds(lb_ub_resolved, definiteRange, -1.0, 1.0)
    t_min_max = func(lb_ub_resolved)
    if func == np.arccos:
        t_min_max = t_min_max[::-1]
    return (t_min_max, definiteRange)


def adjust_lx_WithDiscreteDomain(Lx, v):
    if v.domain is bool or v.domain is 'bool':
        Lx[Lx != 0] = 1
    else:
        d = v.domain
        ind = searchsorted(d, Lx, 'left')
        ind2 = searchsorted(d, Lx, 'right')
        ind3 = where(ind != ind2)[0]
        Tmp = d[ind[ind3]]
        ind[ind == d.size] -= 1
        Lx[:] = d[ind]
        Lx[ind3] = asarray(Tmp, dtype=Lx.dtype)


def adjust_ux_WithDiscreteDomain(Ux, v):
    if v.domain is bool or v.domain is 'bool':
        Ux[Ux != 1] = 0
    else:
        d = v.domain
        ind = searchsorted(d, Ux, 'left')
        ind2 = searchsorted(d, Ux, 'right')
        ind3 = where(ind != ind2)[0]
        Tmp = d[ind[ind3]]
        ind[ind == 0] = 1
        Ux[:] = d[ind - 1]
        Ux[ind3] = asarray(Tmp, dtype=Ux.dtype)


def add_interval(self, other, domain, dtype):
    domain1, definiteRange1 = self._interval(domain, dtype, allowBoundSurf=True)
    domain2, definiteRange2 = other._interval(domain, dtype, allowBoundSurf=True)
    return (domain1 + domain2, logical_and(definiteRange1, definiteRange2))


def add_const_interval(self, c, domain, dtype):
    r, definiteRange = self._interval(domain, dtype, allowBoundSurf=True)
    return (r + c, definiteRange)


def neg_interval(self, domain, dtype):
    r, definiteRange = self._interval(domain, dtype, allowBoundSurf=True)
    if type(r) == ndarray:
        assert r.shape[0] == 2
        return (
         -np.flipud(r), definiteRange)
    else:
        return (
         -r, definiteRange)


def mul_interval(self, other, isOtherOOFun, domain, dtype):
    lb1_ub1, definiteRange = self._interval(domain, dtype, allowBoundSurf=True)
    if isOtherOOFun:
        lb2_ub2, definiteRange2 = other._interval(domain, dtype, allowBoundSurf=True)
        definiteRange = logical_and(definiteRange, definiteRange2)
        if type(lb2_ub2) != boundsurf and type(lb1_ub1) == boundsurf:
            lb2_ub2, lb1_ub1 = lb1_ub1, lb2_ub2
        tmp1 = lb1_ub1.resolve()[0] if type(lb1_ub1) == boundsurf else lb1_ub1
        if type(lb2_ub2) == boundsurf:
            tmp2 = lb2_ub2.resolve()[0]
            t2_positive = all(tmp2 >= 0)
            t2_negative = all(tmp2 <= 0)
            if t2_positive or t2_negative:
                t1_positive = all(tmp1 >= 0)
                t1_negative = all(tmp1 <= 0)
                if t1_positive or t1_negative:
                    ind_z1 = logical_or(tmp1[0] == 0, tmp1[1] == 0)
                    ind_z2 = logical_or(tmp2[0] == 0, tmp2[1] == 0)
                    ind_i1 = logical_or(np.isinf(tmp1[0]), np.isinf(tmp1[1]))
                    ind_i2 = logical_or(np.isinf(tmp2[0]), np.isinf(tmp2[1]))
                    if not any(logical_and(ind_z1, ind_i2)) and not any(logical_and(ind_z2, ind_i1)):
                        r = lb1_ub1 * lb2_ub2
                        return (
                         r, r.definiteRange)
            elif domain.surf_preference and not any(np.isinf(tmp1)) and not any(np.isinf(tmp2)):
                r = 0.25 * ((lb1_ub1 + lb2_ub2) ** 2 - (lb1_ub1 - lb2_ub2) ** 2)
                domain.exactRange = False
                return (
                 r, r.definiteRange)
        else:
            tmp2 = lb2_ub2
        lb2, ub2 = tmp2[0], tmp2[1]
    else:
        if type(lb1_ub1) == boundsurf:
            assert isscalar(other) or other.size == 1, 'bug in FD kernel'
            return (
             lb1_ub1 * other, definiteRange)
        lb2, ub2 = other, other
    if type(lb1_ub1) == boundsurf:
        lb1_ub1 = lb1_ub1.resolve()[0]
    lb1, ub1 = lb1_ub1[0], lb1_ub1[1]
    firstPositive = all(lb1 >= 0)
    firstNegative = all(ub1 <= 0)
    secondPositive = all(lb2 >= 0)
    secondNegative = all(ub2 <= 0)
    if firstPositive and secondPositive:
        t_min, t_max = atleast_1d(lb1 * lb2), atleast_1d(ub1 * ub2)
    elif firstNegative and secondNegative:
        t_min, t_max = atleast_1d(ub1 * ub2), atleast_1d(lb1 * lb2)
    elif firstPositive and secondNegative:
        t_min, t_max = atleast_1d(lb2 * ub1), atleast_1d(lb1 * ub2)
    elif firstNegative and secondPositive:
        t_min, t_max = atleast_1d(lb1 * ub2), atleast_1d(lb2 * ub1)
    elif isscalar(other):
        t_min, t_max = (lb1 * other, ub1 * other) if other >= 0 else (ub1 * other, lb1 * other)
    else:
        if isOtherOOFun:
            t = vstack((lb1 * lb2, ub1 * lb2,
             lb1 * ub2, ub1 * ub2))
        else:
            t = vstack((lb1 * other, ub1 * other))
        t_min, t_max = atleast_1d(nanmin(t, 0)), atleast_1d(nanmax(t, 0))
    if any(np.isinf(lb1)) or any(np.isinf(lb2)) or any(np.isinf(ub1)) or any(np.isinf(ub2)):
        ind1_zero_minus = logical_and(lb1 < 0, ub1 >= 0)
        ind1_zero_plus = logical_and(lb1 <= 0, ub1 > 0)
        ind2_zero_minus = logical_and(lb2 < 0, ub2 >= 0)
        ind2_zero_plus = logical_and(lb2 <= 0, ub2 > 0)
        has_plus_inf_1 = logical_or(logical_and(ind1_zero_minus, lb2 == -inf), logical_and(ind1_zero_plus, ub2 == inf))
        has_plus_inf_2 = logical_or(logical_and(ind2_zero_minus, lb1 == -inf), logical_and(ind2_zero_plus, ub1 == inf))
        ind = logical_or(logical_and(lb1 == -inf, ub2 == 0), logical_and(lb2 == -inf, ub1 == 0))
        t_max[atleast_1d(logical_and(ind, t_max < 0.0))] = 0.0
        t_max[atleast_1d(logical_or(has_plus_inf_1, has_plus_inf_2))] = inf
        t_max[atleast_1d(logical_or(logical_and(lb1 == 0, ub2 == inf), logical_and(lb2 == 0, ub1 == inf)))] = inf
        has_minus_inf_1 = logical_or(logical_and(ind1_zero_plus, lb2 == -inf), logical_and(ind1_zero_minus, ub2 == inf))
        has_minus_inf_2 = logical_or(logical_and(ind2_zero_plus, lb1 == -inf), logical_and(ind2_zero_minus, ub1 == inf))
        t_min[atleast_1d(logical_or(logical_and(lb1 == 0, ub2 == inf), logical_and(lb2 == 0, ub1 == inf)))] = 0.0
        t_min[atleast_1d(logical_or(logical_and(lb1 == -inf, ub2 == 0), logical_and(lb2 == -inf, ub1 == 0)))] = 0.0
        t_min[atleast_1d(logical_or(has_minus_inf_1, has_minus_inf_2))] = -inf
    return (
     vstack((t_min, t_max)), definiteRange)


def div_interval(self, other, domain, dtype):
    lb1_ub1, definiteRange1 = self._interval(domain, dtype, allowBoundSurf=True)
    lb2_ub2, definiteRange2 = other._interval(domain, dtype, allowBoundSurf=True)
    definiteRange = logical_and(definiteRange1, definiteRange2)
    tmp1 = lb1_ub1.resolve()[0] if type(lb1_ub1) == boundsurf else lb1_ub1
    t1_positive = all(tmp1 >= 0)
    t1_negative = all(tmp1 <= 0)
    tmp2 = lb2_ub2.resolve()[0] if type(lb2_ub2) == boundsurf else lb2_ub2
    t2_positive = all(tmp2 >= 0)
    t2_negative = all(tmp2 <= 0)
    if (type(lb1_ub1) == boundsurf or type(lb2_ub2) == boundsurf) and (t1_positive or t1_negative) and (t2_positive or t2_negative):
        assert tmp2.shape[0] == 2
        tmp = lb1_ub1 / lb2_ub2 if type(lb2_ub2) == boundsurf else lb1_ub1 * (1.0 / tmp2[::-1])
        return (
         tmp, tmp.definiteRange)
    lb1, ub1 = tmp1[0], tmp1[1]
    lb2, ub2 = tmp2[0], tmp2[1]
    lb2, ub2 = asarray(lb2, dtype), asarray(ub2, dtype)
    tmp = vstack((lb1 / lb2, lb1 / ub2, ub1 / lb2, ub1 / ub2))
    r1, r2 = nanmin(tmp, 0), nanmax(tmp, 0)
    ind = logical_or(lb1 == 0.0, ub1 == 0.0)
    r1[atleast_1d(logical_and(ind, r1 > 0.0))] = 0.0
    r2[atleast_1d(logical_and(ind, r2 < 0.0))] = 0.0
    ind2_zero_minus = logical_and(lb2 < 0, ub2 >= 0)
    ind2_zero_plus = logical_and(lb2 <= 0, ub2 > 0)
    r1[atleast_1d(logical_or(logical_and(ind2_zero_minus, ub1 > 0), logical_and(ind2_zero_plus, lb1 < 0)))] = -inf
    r2[atleast_1d(logical_or(logical_and(ind2_zero_minus, lb1 < 0), logical_and(ind2_zero_plus, ub1 > 0)))] = inf
    return (
     vstack((r1, r2)), definiteRange)


def rdiv_interval(self, other, domain, dtype):
    arg_lb_ub, definiteRange = self._interval(domain, dtype, allowBoundSurf=True)
    if type(arg_lb_ub) == boundsurf:
        arg_lb_ub_resolved = arg_lb_ub.resolve()[0]
        if all(arg_lb_ub_resolved >= 0) or all(arg_lb_ub_resolved <= 0):
            return (other * arg_lb_ub ** (-1), definiteRange)
        arg_lb_ub = arg_lb_ub_resolved
    arg_infinum, arg_supremum = arg_lb_ub[0], arg_lb_ub[1]
    if other.size != 1:
        raise FuncDesignerException('this case for interval calculations is unimplemented yet')
    r = vstack((other / arg_supremum, other / arg_infinum))
    r1, r2 = nanmin(r, 0), nanmax(r, 0)
    ind_zero_minus = logical_and(arg_infinum < 0, arg_supremum >= 0)
    if any(ind_zero_minus):
        r1[atleast_1d(logical_and(ind_zero_minus, other > 0))] = -inf
        r2[atleast_1d(logical_and(ind_zero_minus, other < 0))] = inf
    ind_zero_plus = logical_and(arg_infinum <= 0, arg_supremum > 0)
    if any(ind_zero_plus):
        r1[atleast_1d(logical_and(ind_zero_plus, other < 0))] = -inf
        r2[atleast_1d(logical_and(ind_zero_plus, other > 0))] = inf
    return (vstack((r1, r2)), definiteRange)


def pow_const_interval(self, other, domain, dtype):
    lb_ub, definiteRange = self._interval(domain, dtype, allowBoundSurf=True)
    isBoundSurf = type(lb_ub) == boundsurf
    lb_ub_resolved = lb_ub.resolve()[0] if isBoundSurf else lb_ub
    if isBoundSurf and not any(np.isinf(lb_ub_resolved)):
        lb_ub_resolved = lb_ub.resolve()[0]
        other_isPositive = other > 0
        domain_isPositive = all(lb_ub_resolved >= 0)
        other_is_int = asarray(other, int) == other
        if domain_isPositive or other_is_int and other > 0 and other % 2 == 0:
            return defaultIntervalEngine(lb_ub, (lambda x: x ** other), (lambda x: other * x ** (other - 1)), monotonity=1 if other_isPositive and domain_isPositive else np.nan, convexity=1 if other > 1.0 or other < 0 else -1, criticalPoint=0.0, criticalPointValue=0.0)
        domain_isNegative = all(lb_ub_resolved <= 0.0)
        if domain_isNegative and other_is_int:
            return defaultIntervalEngine(lb_ub, (lambda x: x ** other), (lambda x: other * x ** (other - 1)), monotonity=1 if other % 2 == 0 else -1, convexity=1 if other % 2 == 0 else -1, criticalPoint=np.nan, criticalPointValue=np.nan)
    allowBoundSurf = True if isscalar(other) and other == 0.5 else False
    if type(lb_ub) == boundsurf:
        if allowBoundSurf:
            return (lb_ub ** other, definiteRange)
        lb_ub = lb_ub_resolved
    Tmp = lb_ub ** other
    t_min, t_max = nanmin(Tmp, 0), nanmax(Tmp, 0)
    lb, ub = lb_ub[0], lb_ub[1]
    ind = lb < 0.0
    if any(ind):
        isNonInteger = other != asarray(other, int)
        if any(isNonInteger):
            definiteRange = False
        ind_nan = logical_and(logical_and(ind, isNonInteger), ub < 0)
        if any(ind_nan):
            t_max[atleast_1d(ind_nan)] = nan
        t_min[atleast_1d(logical_and(ind, logical_and(t_min > 0, ub >= 0)))] = 0.0
    return (
     vstack((t_min, t_max)), definiteRange)


def pow_oofun_interval(self, other, domain, dtype):
    lb1_ub1, definiteRange1 = self._interval(domain, dtype)
    lb1, ub1 = lb1_ub1[0], lb1_ub1[1]
    lb2_ub2, definiteRange2 = other._interval(domain, dtype)
    lb2, ub2 = lb2_ub2[0], lb2_ub2[1]
    T = vstack((lb1 ** lb2, lb1 ** ub2, ub1 ** lb1, ub1 ** ub2))
    t_min, t_max = nanmin(T, 0), nanmax(T, 0)
    definiteRange = logical_and(definiteRange1, definiteRange2)
    ind1 = lb1 < 0
    if any(ind1):
        definiteRange = False
        ind2 = ub1 >= 0
        t_min[atleast_1d(logical_and(logical_and(ind1, ind2), logical_and(t_min > 0.0, ub2 > 0.0)))] = 0.0
        t_max[atleast_1d(logical_and(ind1, logical_not(ind2)))] = nan
        t_min[atleast_1d(logical_and(ind1, logical_not(ind2)))] = nan
    return (
     vstack((t_min, t_max)), definiteRange)


def defaultIntervalEngine(arg_lb_ub, fun, deriv, monotonity, convexity, criticalPoint=np.nan, criticalPointValue=np.nan, feasLB=-inf, feasUB=inf):
    L, U, domain, definiteRange = (arg_lb_ub.l, arg_lb_ub.u, arg_lb_ub.domain, arg_lb_ub.definiteRange)
    R0 = arg_lb_ub.resolve()[0]
    assert R0.shape[0] == 2, 'unimplemented yet'
    if feasLB != -inf or feasUB != inf:
        R0, definiteRange = adjustBounds(R0, definiteRange, feasLB, feasUB)
    r_l, r_u = R0
    R2 = fun(R0)
    ind_inf = np.where(np.logical_or(np.isinf(R2[0]), np.isinf(R2[1])))[0]
    koeffs = (R2[1] - R2[0]) / (r_u - r_l)
    koeffs[ind_inf] = 0.0
    ind_eq = where(r_u == r_l)[0]
    Ld, Ud = L.d, U.d
    if monotonity == 1:
        new_l_resolved, new_u_resolved = R2
        U_dict, L_dict = Ud, Ld
        _argmin, _argmax = r_l, r_u
    elif monotonity == -1:
        new_u_resolved, new_l_resolved = R2
        U_dict, L_dict = Ld, Ud
        _argmin, _argmax = r_u, r_l
    else:
        ind = R2[1] > R2[0]
        R2.sort(axis=0)
        new_l_resolved, new_u_resolved = R2
        _argmin = where(ind, r_l, r_u)
        _argmax = where(ind, r_u, r_l)
        if criticalPoint is not np.nan:
            ind_c = logical_and(r_l < criticalPoint, r_u > criticalPoint)
            if convexity == 1:
                new_l_resolved[ind_c] = criticalPointValue
                _argmin[ind_c] = criticalPoint
            elif convexity == -1:
                new_u_resolved[ind_c] = criticalPointValue
                _argmax[ind_c] = criticalPoint
        Keys = set().union(set(Ld.keys()), set(Ud.keys()))
        L_dict = dict((k, where(ind, Ld.get(k, 0), Ud.get(k, 0))) for k in Keys)
        U_dict = dict((k, where(ind, Ud.get(k, 0), Ld.get(k, 0))) for k in Keys)
    if convexity == -1:
        tmp2 = deriv(_argmax.view(multiarray)).view(ndarray).flatten()
        tmp2[ind_inf] = 0.0
        d_new = dict((v, tmp2 * val) for v, val in L_dict.items())
        U_new = surf(d_new, 0.0)
        U_new.c = new_u_resolved - U_new.maximum(domain)
        ind_inf2 = np.isinf(new_u_resolved)
        if any(ind_inf2):
            U_new.c = where(ind_inf2, new_u_resolved, U_new.c)
        if len(U_dict) >= 1:
            if ind_eq.size:
                koeffs[ind_eq] = tmp2[ind_eq]
            d_new = dict((v, koeffs * val) for v, val in U_dict.items())
            L_new = surf(d_new, 0.0)
            L_new.c = new_l_resolved - L_new.minimum(domain)
            if any(ind_inf2):
                L_new.c = where(ind_inf2, new_l_resolved, L_new.c)
        else:
            L_new = surf({}, new_l_resolved)
        R = boundsurf(L_new, U_new, definiteRange, domain)
    elif convexity == 1:
        tmp2 = deriv(_argmin.view(multiarray)).view(ndarray).flatten()
        tmp2[ind_inf] = 0.0
        d_new = dict((v, tmp2 * val) for v, val in L_dict.items())
        L_new = surf(d_new, 0.0)
        L_new.c = new_l_resolved - L_new.minimum(domain)
        ind_inf2 = np.isinf(new_l_resolved)
        if any(ind_inf2):
            L_new.c = where(ind_inf2, new_l_resolved, L_new.c)
        if len(U_dict) >= 1:
            if ind_eq.size:
                koeffs[ind_eq] = tmp2[ind_eq]
            d_new = dict((v, koeffs * val) for v, val in U_dict.items())
            U_new = surf(d_new, 0.0)
            U_new.c = new_u_resolved - U_new.maximum(domain)
            if any(ind_inf2):
                U_new.c = where(ind_inf2, new_u_resolved, U_new.c)
        else:
            U_new = surf({}, new_u_resolved)
        R = boundsurf(L_new, U_new, definiteRange, domain)
    else:
        raise FuncDesignerException('bug in FD kernel')
    return (
     R, definiteRange)


def adjustBounds(R0, definiteRange, feasLB, feasUB):
    r_l, r_u = R0
    ind_L = r_l < feasLB
    ind_l = where(ind_L)[0]
    ind_U = r_u > feasUB
    ind_u = where(ind_U)[0]
    if ind_l.size != 0 or ind_u.size != 0:
        R0 = R0.copy()
        r_l, r_u = R0
    if ind_l.size != 0:
        r_l[logical_and(ind_L, r_u >= feasLB)] = feasLB
        if definiteRange is not False:
            if type(definiteRange) != np.ndarray:
                definiteRange = np.empty_like(r_l, bool)
                definiteRange.fill(True)
            definiteRange[ind_l] = False
    if ind_u.size != 0:
        r_u[logical_and(ind_U, r_l <= feasUB)] = feasUB
        if definiteRange is not False:
            if type(definiteRange) != np.ndarray:
                definiteRange = np.empty_like(r_l, bool)
                definiteRange.fill(True)
            definiteRange[ind_u] = False
    return (
     R0, definiteRange)