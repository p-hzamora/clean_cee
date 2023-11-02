# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: FuncDesigner\boundsurf.pyc
# Compiled at: 2013-05-21 10:54:48
PythonSum = sum
import numpy as np
from numpy import all, any, logical_and, logical_not, isscalar, where
from operator import gt as Greater, lt as Less

def extract(b, ind):
    d = dict((k, v if isscalar(v) or v.size == 1 else v[ind]) for k, v in b.d.items())
    C = b.c
    c = C if isscalar(C) or C.size == 1 else C[ind]
    return surf(d, c)


class surf(object):
    isRendered = False
    __array_priority__ = 15

    def __init__(self, d, c):
        self.d = d
        self.c = c

    value = lambda self, point: self.c + PythonSum(point[k] * v for k, v in self.d.items())

    def exclude(self, domain, oovars, cmp):
        C = []
        d = self.d.copy()
        for v in oovars:
            tmp = d.pop(v, 0.0)
            if any(tmp):
                D = domain[v]
                C.append(where(cmp(tmp, 0), D[0], D[1]) * tmp)

        c = self.c + PythonSum(C)
        return surf(d, c)

    split = lambda self, inds: [ extract(self, ind) for ind in inds ]
    minimum = lambda self, domain: self.c + PythonSum(where(v > 0, domain[k][0], domain[k][1]) * v for k, v in self.d.items())
    maximum = lambda self, domain: self.c + PythonSum(where(v < 0, domain[k][0], domain[k][1]) * v for k, v in self.d.items())

    def render(self, domain, cmp):
        self.rendered = dict((k, where(cmp(v, 0), domain[k][0], domain[k][1]) * v) for k, v in self.d.items())
        self.resolved = PythonSum(self.rendered) + self.c
        self.isRendered = True

    def __add__(self, other):
        if type(other) == surf:
            S, O = self.d, other.d
            d = S.copy()
            d.update(O)
            for key in set(S.keys()) & set(O.keys()):
                d[key] = S[key] + O[key]

            return surf(d, self.c + other.c)
        if isscalar(other) or type(other) == np.ndarray:
            return surf(self.d, self.c + other)
        assert 0, 'unimplemented yet'

    __sub__ = lambda self, other: self.__add__(-other)
    __neg__ = lambda self: surf(dict((k, -v) for k, v in self.d.items()), -self.c)

    def __mul__(self, other):
        isArray = type(other) == np.ndarray
        if isscalar(other) or isArray:
            return surf(dict((k, v * other) for k, v in self.d.items()), self.c * other)
        assert 0, 'unimplemented yet'

    __rmul__ = __mul__

    def koeffs_mul(self, other):
        assert type(other) == surf
        S, O = self.d, other.d
        d = dict((key, S.get(key, 0.0) * O.get(key, 0.0)) for key in set(S.keys()) | set(O.keys()))
        return surf(d, 0.0)


class boundsurf(object):
    __array_priority__ = 15
    isRendered = False

    def __init__(self, lowersurf, uppersurf, definiteRange, domain):
        self.l = lowersurf
        self.u = uppersurf
        self.definiteRange = definiteRange
        self.domain = domain

    Size = lambda self: max((len(self.l.d), len(self.u.d), 1))
    exclude = lambda self, oovars: boundsurf(self.l.exclude(self.domain, oovars, Greater), self.u.exclude(self.domain, oovars, Less), self.definiteRange, self.domain)

    def split(self, condition1, condition2):
        inds = (
         where(condition1)[0],
         where(logical_and(condition2, logical_not(condition1)))[0],
         where(logical_and(logical_not(condition1), logical_not(condition2)))[0])
        L = self.l.split(inds)
        U = self.u.split(inds) if self.l is not self.u else L
        definiteRange = self.definiteRange
        DefiniteRange = [definiteRange] * len(inds) if type(definiteRange) == bool or definiteRange.size == 1 else [ definiteRange[ind] for ind in inds ]
        return (
         inds, [ boundsurf(L[i], U[i], DefiniteRange[i], self.domain) for i in range(len(inds)) ])

    def join(self, inds, B):
        L = surf.join(inds, (b.l for b in B))
        U = surf.join(inds, (b.u for b in B))
        definiteRange = B[0].definiteRange if np.array_equiv(B[0].definiteRange, B[1].definiteRange) and np.array_equiv(B[0].definiteRange, B[2].definiteRange) else Join(inds, (B[0].definiteRange, B[1].definiteRange, B[2].definiteRange))
        return boundsurf(L, U, definiteRange, B[0].domain)

    def resolve(self):
        r = np.vstack((self.l.minimum(self.domain), self.u.maximum(self.domain)))
        assert r.shape[0] == 2, 'bug in FD kernel'
        return (r, self.definiteRange)

    def render(self):
        if self.isRendered:
            return
        self.isRendered = True

    values = lambda self, point: (
     self.l.value(point), self.u.value(point))
    isfinite = lambda self: all(np.isfinite(self.l.c)) and all(np.isfinite(self.u.c))

    def __add__(self, other):
        if isscalar(other) or type(other) == np.ndarray and other.size == 1:
            if self.l is self.u:
                tmp = self.l + other
                rr = (tmp, tmp)
            else:
                rr = (
                 self.l + other, self.u + other)
            return boundsurf(rr[0], rr[1], self.definiteRange, self.domain)
        if type(other) == boundsurf:
            if self.l is self.u and other.l is other.u:
                tmp = self.l + other.l
                rr = (tmp, tmp)
            else:
                rr = (
                 self.l + other.l, self.u + other.u)
            return boundsurf(rr[0], rr[1], self.definiteRange & other.definiteRange, self.domain)
        if type(other) == np.ndarray:
            assert other.shape[0] == 2, 'unimplemented yet'
            return boundsurf(self.l + other[0], self.u + other[1], self.definiteRange, self.domain)
        assert 0, 'unimplemented yet'

    __radd__ = __add__

    def __neg__(self):
        l, u = self.l, self.u
        if l is u:
            tmp = surf(dict((k, -v) for k, v in u.d.items()), -u.c)
            L, U = tmp, tmp
        else:
            L = surf(dict((k, -v) for k, v in u.d.items()), -u.c)
            U = surf(dict((k, -v) for k, v in l.d.items()), -l.c)
        return boundsurf(L, U, self.definiteRange, self.domain)

    __sub__ = lambda self, other: self.__add__(-other)

    def __mul__(self, other):
        R1 = self.resolve()[0]
        definiteRange = self.definiteRange
        selfPositive = all(R1 >= 0)
        selfNegative = all(R1 <= 0)
        isArray = type(other) == np.ndarray
        isBoundSurf = type(other) == boundsurf
        R2 = other.resolve()[0] if isBoundSurf else other
        R2_is_scalar = isscalar(R2)
        if not R2_is_scalar and R2.size != 1:
            assert R2.shape[0] == 2, 'bug or unimplemented yet'
            R2Positive = all(R2 >= 0)
            R2Negative = all(R2 <= 0)
            assert R2Positive or R2Negative, 'bug or unimplemented yet'
        if R2_is_scalar or isArray and R2.size == 1:
            if self.l is self.u:
                tmp = self.l * R2
                rr = (tmp, tmp)
            else:
                rr = (self.l * R2, self.u * R2) if R2 >= 0 else (self.u * R2, self.l * R2)
        elif isArray:
            assert selfPositive or selfNegative, 'unimplemented yet'
            if selfPositive:
                rr = (self.l * R2[0], self.u * R2[1]) if R2Positive else (self.u * R2[0], self.l * R2[1])
            else:
                assert selfNegative
                rr = (self.u * R2[1], self.l * R2[0]) if R2Negative else (self.l * R2[1], self.u * R2[0])
        else:
            if isBoundSurf:
                assert selfPositive or selfNegative, 'bug or unimplemented yet'
                definiteRange = logical_and(definiteRange, other.definiteRange)
                r = ((self if selfPositive else -self).log() + (other if R2Positive else -other).log()).exp()
                r.definiteRange = definiteRange
                if selfPositive == R2Positive:
                    return r
                return -r
            assert 0, 'bug or unimplemented yet'
        R = boundsurf(rr[0], rr[1], definiteRange, self.domain)
        return R

    __rmul__ = __mul__

    def __div__(self, other):
        R1 = self.resolve()[0]
        definiteRange = self.definiteRange
        selfPositive = all(R1 >= 0)
        selfNegative = all(R1 <= 0)
        isBoundSurf = type(other) == boundsurf
        assert isBoundSurf
        R2 = other.resolve()[0]
        assert R2.shape[0] == 2, 'bug or unimplemented yet'
        R2Positive = all(R2 >= 0)
        R2Negative = all(R2 <= 0)
        assert (selfPositive or selfNegative) and (R2Positive or R2Negative), 'bug or unimplemented yet'
        definiteRange = logical_and(definiteRange, other.definiteRange)
        r = ((self if selfPositive else -self).log() - (other if R2Positive else -other).log()).exp()
        r.definiteRange = definiteRange
        if selfPositive == R2Positive:
            return r
        return -r

    __truediv__ = __div__

    def log(self):
        from Interval import defaultIntervalEngine
        return defaultIntervalEngine(self, np.log, (lambda x: 1.0 / x), monotonity=1, convexity=-1, feasLB=0.0)[0]

    def exp(self):
        from Interval import defaultIntervalEngine
        return defaultIntervalEngine(self, np.exp, np.exp, monotonity=1, convexity=1)[0]

    def copy(self):
        assert '__iadd__' not in self.__dict__
        assert '__imul__' not in self.__dict__
        assert '__idiv__' not in self.__dict__
        assert '__isub__' not in self.__dict__
        return self

    abs = lambda self: boundsurf_abs(self)

    def __pow__(self, other):
        R0 = self.resolve()[0]
        assert R0.shape[0] == 2, 'unimplemented yet'
        assert isscalar(other) and other in (-1, 2, 0.5), 'unimplemented yet'
        if other == 0.5:
            from Interval import defaultIntervalEngine
            return defaultIntervalEngine(self, np.sqrt, (lambda x: 0.5 / np.sqrt(x)), monotonity=1, convexity=-1, feasLB=0.0)[0]
        if other == 2:
            from Interval import defaultIntervalEngine
            return defaultIntervalEngine(self, (lambda x: x ** 2), (lambda x: 2 * x), monotonity=1 if all(R0 >= 0) else -1 if all(R0 <= 0) else np.nan, convexity=1, criticalPoint=0.0, criticalPointValue=0.0)[0]
        if other == -1:
            from Interval import defaultIntervalEngine
            return defaultIntervalEngine(self, (lambda x: 1.0 / x), (lambda x: -1.0 / x ** 2), monotonity=-1, convexity=1 if all(R0 >= 0) else -1 if all(R0 <= 0) else np.nan, criticalPoint=np.nan, criticalPointValue=np.nan)[0]


def boundsurf_abs(b):
    r, definiteRange = b.resolve()
    lf, uf = r
    assert lf.ndim <= 1, 'unimplemented yet'
    ind_l = lf >= 0
    if all(ind_l):
        return (b, b.definiteRange)
    ind_u = uf <= 0
    if all(ind_u):
        return (-b, b.definiteRange)
    from Interval import defaultIntervalEngine
    return defaultIntervalEngine(b, np.abs, np.sign, monotonity=np.nan, convexity=1, criticalPoint=0.0, criticalPointValue=0.0)


def Join(inds, arrays):
    r = np.empty(PythonSum(arr.size for arr in arrays), arrays[0].dtype)
    for ind, arr in zip(inds, arrays):
        r[ind] = arr

    return r