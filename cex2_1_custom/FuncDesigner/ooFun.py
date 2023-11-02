# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: FuncDesigner\ooFun.pyc
# Compiled at: 2013-05-22 08:20:06
PythonSum = sum
from numpy import inf, asfarray, copy, all, any, atleast_2d, zeros, dot, asarray, atleast_1d, ones, ndarray, where, array, nan, vstack, eye, array_equal, isscalar, log, hstack, sum as npSum, prod, nonzero, isnan, asscalar, zeros_like, ones_like, logical_and, logical_or, isinf, logical_not, logical_xor, tile, float64, searchsorted, int8, int16, int32, int64, isfinite, log2, string_, asanyarray, bool_
try:
    from bottleneck import nanmin, nanmax
except ImportError:
    from numpy import nanmin, nanmax

from FDmisc import FuncDesignerException, Diag, Eye, pWarn, scipyAbsentMsg, scipyInstalled, raise_except, DiagonalType, isPyPy, formResolveSchedule
from ooPoint import ooPoint
from FuncDesigner.multiarray import multiarray
from Interval import Interval, adjust_lx_WithDiscreteDomain, adjust_ux_WithDiscreteDomain, mul_interval, pow_const_interval, pow_oofun_interval, div_interval, rdiv_interval, add_interval, add_const_interval, neg_interval, defaultIntervalEngine
import inspect
from baseClasses import OOArray, Stochastic
from boundsurf import boundsurf
Copy = --- This code section failed: ---

 L.  25         0  LOAD_GLOBAL           0  'type'
                3  LOAD_FAST             0  'arg'
                6  CALL_FUNCTION_1       1  None
                9  LOAD_GLOBAL           1  'ndarray'
               12  COMPARE_OP            2  ==
               15  POP_JUMP_IF_FALSE    43  'to 43'
               18  LOAD_FAST             0  'arg'
               21  LOAD_ATTR             2  'size'
               24  LOAD_CONST               1
               27  COMPARE_OP            2  ==
             30_0  COME_FROM            15  '15'
               30  POP_JUMP_IF_FALSE    43  'to 43'
               33  LOAD_GLOBAL           3  'asscalar'
               36  LOAD_FAST             0  'arg'
               39  CALL_FUNCTION_1       1  None
               42  RETURN_END_IF_LAMBDA
             43_0  COME_FROM            30  '30'
               43  LOAD_GLOBAL           4  'hasattr'
               46  LOAD_FAST             0  'arg'
               49  LOAD_CONST               'copy'
               52  CALL_FUNCTION_2       2  None
               55  POP_JUMP_IF_FALSE    68  'to 68'
               58  LOAD_FAST             0  'arg'
               61  LOAD_ATTR             5  'copy'
               64  CALL_FUNCTION_0       0  None
               67  RETURN_END_IF_LAMBDA
             68_0  COME_FROM            55  '55'
               68  LOAD_GLOBAL           5  'copy'
               71  LOAD_FAST             0  'arg'
               74  CALL_FUNCTION_1       1  None
               77  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `None' instruction at offset -1
Len = --- This code section failed: ---

 L.  26         0  LOAD_GLOBAL           0  'isscalar'
                3  LOAD_FAST             0  'x'
                6  CALL_FUNCTION_1       1  None
                9  POP_JUMP_IF_FALSE    16  'to 16'
               12  LOAD_CONST               1
               15  RETURN_END_IF_LAMBDA
             16_0  COME_FROM             9  '9'
               16  LOAD_GLOBAL           1  'type'
               19  LOAD_FAST             0  'x'
               22  CALL_FUNCTION_1       1  None
               25  LOAD_GLOBAL           2  'ndarray'
               28  COMPARE_OP            2  ==
               31  POP_JUMP_IF_FALSE    41  'to 41'
               34  LOAD_FAST             0  'x'
               37  LOAD_ATTR             3  'size'
               40  RETURN_END_IF_LAMBDA
             41_0  COME_FROM            31  '31'
               41  LOAD_GLOBAL           4  'isinstance'
               44  LOAD_FAST             0  'x'
               47  LOAD_GLOBAL           5  'Stochastic'
               50  CALL_FUNCTION_2       2  None
               53  POP_JUMP_IF_FALSE    66  'to 66'
               56  LOAD_FAST             0  'x'
               59  LOAD_ATTR             6  'values'
               62  LOAD_ATTR             3  'size'
               65  RETURN_END_IF_LAMBDA
             66_0  COME_FROM            53  '53'
               66  LOAD_GLOBAL           7  'len'
               69  LOAD_FAST             0  'x'
               72  CALL_FUNCTION_1       1  None
               75  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `None' instruction at offset -1
try:
    from DerApproximator import get_d1, check_d1
    DerApproximatorIsInstalled = True
except:
    DerApproximatorIsInstalled = False

try:
    import scipy
    from scipy.sparse import hstack as HstackSP, vstack as VstackSP, isspmatrix_csc, isspmatrix_csr, eye as SP_eye, lil_matrix as SparseMatrixConstructor

    def Hstack(Tuple):
        ind = where([ isscalar(elem) or prod(elem.shape) != 0 for elem in Tuple ])[0].tolist()
        elems = [ Tuple[i] for i in ind ]
        if any([ isspmatrix(elem) for elem in elems ]):
            return HstackSP(elems)
        s = set([ 0 if isscalar(elem) else elem.ndim for elem in elems ])
        ndim = max(s)
        if ndim <= 1:
            return hstack(elems)
        assert ndim <= 2 and 1 not in s, 'bug in FuncDesigner kernel, inform developers'
        if 0 not in s:
            return hstack(elems)
        return hstack([ atleast_2d(elem) for elem in elems ])


    def Vstack(Tuple):
        ind = where([ isscalar(elem) or prod(elem.shape) != 0 for elem in Tuple ])[0].tolist()
        elems = [ Tuple[i] for i in ind ]
        if any([ isspmatrix(elem) for elem in elems ]):
            return VstackSP(elems)
        else:
            return vstack(elems)


    from scipy.sparse import isspmatrix
except:
    scipy = None
    isspmatrix = lambda *args, **kwargs: False
    Hstack = hstack
    Vstack = vstack

class oofun(object):
    tol = 0.0
    d = None
    input = None
    is_oovar = False
    isConstraint = False
    discrete = False
    _isSum = False
    _isProd = False
    stencil = 3
    evals = 0
    same = 0
    same_d = 0
    evals_d = 0
    engine_convexity = nan
    engine_monotonity = nan
    diffInt = 1.5e-08
    maxViolation = 0.01
    _unnamedFunNumber = 1
    _lastDiffVarsID = 0
    _lastFuncVarsID = 0
    _lastOrderVarsID = 0
    criticalPoints = None
    vectorized = False
    _neg_elem = None
    _usedIn = 0
    _level = 0
    _id = 0
    _BroadCastID = 0
    _broadcast_id = 0
    _point_id = 0
    _point_id1 = 0
    _f_key_prev = None
    _f_val_prev = None
    _d_key_prev = None
    _d_val_prev = None
    __array_priority__ = 15
    pWarn = lambda self, msg: pWarn(msg)

    def disp(self, msg):
        print msg

    nlh = lambda self, *args, **kw: raise_except('probably you have involved boolean operation on continuous function, that is error')
    lh = lambda self, *args, **kw: raise_except('probably you have involved boolean operation on continuous function, that is error')

    def __getattr__(self, attr):
        if attr == '__len__':
            if isPyPy:
                return 1
            raise AttributeError('using len(oofun) is not possible yet, try using oofun.size instead')
        elif attr == 'isUncycled':
            self._getDep()
            return self.isUncycled
        if attr == 'isCostly':
            return self.d is None and not self._isSum
        else:
            if attr == 'resolveSchedule':
                formResolveSchedule(self)
                return self.resolveSchedule
            if attr != 'size':
                raise AttributeError('you are trying to obtain incorrect attribute "%s" for FuncDesigner oofun "%s"' % (attr, self.name))
            r = oofun((lambda x: asarray(x).size), self, discrete=True, getOrder=(lambda *args, **kwargs: 0))
            self.size = r
            return r

    def __init__(self, fun, input=None, *args, **kwargs):
        assert len(args) == 0
        self.fun = fun
        self.attachedConstraints = set()
        self.args = ()
        self._id = oofun._id
        oofun._id += 1
        if 'name' not in kwargs.keys():
            self.name = 'unnamed_oofun_' + str(oofun._unnamedFunNumber)
            oofun._unnamedFunNumber += 1
        for key, item in kwargs.items():
            setattr(self, key, item)

        if isinstance(input, (tuple, list)):
            self.input = [ elem if isinstance(elem, (oofun, OOArray)) else array(elem, 'float') for elem in input ]
        elif input is not None:
            self.input = [
             input]
        else:
            self.input = [
             None]
        if input is not None:
            for elem in self.input:
                if isinstance(elem, oofun):
                    elem._usedIn += 1

        return

    __hash__ = lambda self: self._id

    def attach(self, *args, **kwargs):
        if len(kwargs) != 0:
            raise FuncDesignerException('keyword arguments are not implemented for FuncDesigner function "attach"')
        assert len(args) != 0
        Args = args[0] if len(args) == 1 and type(args[0]) in (tuple, list, set) else args
        for arg in Args:
            if not isinstance(arg, BaseFDConstraint):
                raise FuncDesignerException('the FD function "attach" currently expects only constraints')

        self.attachedConstraints.update(Args)
        return self

    def removeAttachedConstraints(self):
        self.attachedConstraints = set()

    __repr__ = lambda self: self.name

    def _interval_(self, domain, dtype):
        INP = self.input[0]
        arg_lb_ub, definiteRange = INP._interval(domain, dtype, allowBoundSurf=True)
        isBoundsurf = type(arg_lb_ub) == boundsurf
        arg_lb_ub_resolved = arg_lb_ub.resolve()[0] if isBoundsurf else arg_lb_ub
        if isBoundsurf and self.engine_convexity is not nan and all(isfinite(arg_lb_ub_resolved)):
            return defaultIntervalEngine(arg_lb_ub, self.fun, self.d, self.engine_monotonity, self.engine_convexity)
        else:
            criticalPointsFunc = self.criticalPoints
            if criticalPointsFunc in (None, False):
                arg_infinum, arg_supremum = arg_lb_ub_resolved[0], arg_lb_ub_resolved[1]
                if not isscalar(arg_infinum) and arg_infinum.size > 1 and not self.vectorized:
                    raise FuncDesignerException('not implemented for vectorized oovars yet')
                Tmp = self.fun(arg_lb_ub_resolved)
                if self.engine_monotonity == -1:
                    Tmp = Tmp[::-1]
                else:
                    assert self.engine_monotonity in (0, 1), 'interval computations are unimplemented for the oofun yet'
            else:
                tmp = [
                 arg_lb_ub_resolved] + criticalPointsFunc(arg_lb_ub_resolved)
                Tmp = self.fun(vstack(tmp))
                Tmp = vstack((nanmin(Tmp, 0), nanmax(Tmp, 0)))
            return (
             Tmp, definiteRange)

    def interval(self, domain, dtype=float, resetStoredIntervals=True, allowBoundSurf=False):
        if type(domain) != ooPoint:
            domain = ooPoint(domain, skipArrayCast=True)
        domain.resolveSchedule = {} if domain.surf_preference else self.resolveSchedule
        lb_ub, definiteRange = self._interval(domain, dtype, allowBoundSurf=allowBoundSurf)
        if resetStoredIntervals:
            domain.storedIntervals = {}
        if type(lb_ub) == ndarray:
            return Interval(lb_ub[0], lb_ub[1], definiteRange)
        else:
            return lb_ub

    def _interval(self, domain, dtype, allowBoundSurf=False):
        tmp = domain.dictOfFixedFuncs.get(self, None)
        if tmp is not None:
            return (tile(tmp, (2, 1)), True)
        else:
            v = domain.modificationVar
            r = None
            if v is None or (v not in self._getDep() or self.is_oovar) and self is not v:
                r = domain.storedIntervals.get(self, None)
            if r is None and v is not None:
                r = domain.localStoredIntervals.get(self, None)
            if r is None:
                r = self._interval_(domain, dtype)
                if domain.useSave:
                    domain.storedIntervals[self] = r
                if v is not None and self._usedIn > 1:
                    domain.localStoredIntervals[self] = r
            if type(r[0]) == boundsurf:
                if allowBoundSurf:
                    R, definiteRange = r
                    Tmp = domain.resolveSchedule.get(self, ())
                    if len(Tmp):
                        R = R.exclude(Tmp)
                    return (
                     R, definiteRange)
                else:
                    return r[0].resolve()

            return r

    def iqg(self, domain, dtype=float, lb=None, ub=None, UB=None):
        if type(domain) != ooPoint:
            domain = ooPoint(domain, skipArrayCast=True)
            domain.isMultiPoint = True
        domain.useSave = True
        r0 = self.interval(domain, dtype, resetStoredIntervals=False)
        r0.lb, r0.ub = atleast_1d(r0.lb).copy(), atleast_1d(r0.ub).copy()
        domain.useSave = False
        if lb is not None and ub is not None:
            ind = logical_or(logical_or(r0.ub < lb, r0.lb > ub), all(logical_and(r0.lb >= lb, r0.ub <= ub)))
        else:
            if UB is not None:
                ind = r0.lb > UB
            else:
                ind = None
            useSlicing = False
            if ind is not None:
                if all(ind):
                    return ({}, r0)
                j = where(~ind)[0]
                if 0 and j.size < 0.85 * ind.size:
                    useSlicing = True
                    tmp = []
                    for key, val in domain.storedIntervals.items():
                        Interval, definiteRange = val
                        if type(definiteRange) not in (bool, bool_):
                            definiteRange = definiteRange[j]
                        tmp.append((key, (Interval[:, j], definiteRange)))

                    _storedIntervals = dict(tmp)
                    Tmp = []
                    for key, val in domain.storedSums.items():
                        R0, DefiniteRange0 = val.pop(-1)
                        R0 = R0[:, j]
                        if type(DefiniteRange0) not in (bool, bool_):
                            DefiniteRange0 = DefiniteRange0[j]
                        tmp = []
                        for k, v in val.items():
                            v = v[:, j]
                            tmp.append((k, v))

                        val = dict(tmp)
                        val[-1] = (R0, DefiniteRange0)
                        Tmp.append((key, val))

                    _storedSums = dict(Tmp)
                    Tmp = []
                    for key, val in domain.items():
                        lb_, ub_ = val
                        Tmp.append((key, (lb_[j], ub_[j])))

                    dictOfFixedFuncs = domain.dictOfFixedFuncs
                    domain2 = ooPoint(Tmp, skipArrayCast=True)
                    domain2.storedSums = _storedSums
                    domain2.storedIntervals = _storedIntervals
                    domain2.dictOfFixedFuncs = dictOfFixedFuncs
                    domain2.isMultiPoint = True
                    domain = domain2
            domain.useAsMutable = True
            r = {}
            Dep = ((self.is_oovar or self._getDep)() if 1 else set([self])).intersection(domain.keys())
            for i, v in enumerate(Dep):
                domain.modificationVar = v
                r_l, r_u = self._iqg(domain, dtype, r0)
                if useSlicing and r_l is not r0:
                    lf1, lf2, uf1, uf2 = (
                     r_l.lb, r_u.lb, r_l.ub, r_u.ub)
                    Lf1, Lf2, Uf1, Uf2 = (Copy(r0.lb), Copy(r0.lb), Copy(r0.ub), Copy(r0.ub))
                    Lf1[:, j], Lf2[:, j], Uf1[:, j], Uf2[:, j] = (lf1, lf2, uf1, uf2)
                    r_l.lb, r_u.lb, r_l.ub, r_u.ub = (Lf1, Lf2, Uf1, Uf2)
                    if type(r0.definiteRange) not in (bool, bool_):
                        d1, d2 = r_l.definiteRange, r_u.definiteRange
                        D1, D2 = atleast_1d(r0.definiteRange).copy(), atleast_1d(r0.definiteRange).copy()
                        D1[j], D2[j] = d1, d2
                        r_l.definiteRange, r_u.definiteRange = D1, D2
                r[v] = (
                 r_l, r_u)
                if not self.isUncycled:
                    lf1, lf2, uf1, uf2 = (
                     r_l.lb, r_u.lb, r_l.ub, r_u.ub)
                    lf, uf = nanmin(vstack((lf1, lf2)), 0), nanmax(vstack((uf1, uf2)), 0)
                    if i == 0:
                        L, U = lf.copy(), uf.copy()
                    else:
                        L[L < lf] = lf[L < lf].copy()
                        U[U > uf] = uf[U > uf].copy()

        if not self.isUncycled:
            for R in r.values():
                r1, r2 = R
                if type(r1.lb) != ndarray:
                    r1.lb, r2.lb, r1.ub, r2.ub = (
                     atleast_1d(r1.lb), atleast_1d(r2.lb), atleast_1d(r1.ub), atleast_1d(r2.ub))
                r1.lb[r1.lb < L] = L[r1.lb < L]
                r2.lb[r2.lb < L] = L[r2.lb < L]
                r1.ub[r1.ub > U] = U[r1.ub > U]
                r2.ub[r2.ub > U] = U[r2.ub > U]

            r0.lb[r0.lb < L] = L[r0.lb < L]
            r0.ub[r0.ub > U] = U[r0.ub > U]
        domain.useSave = True
        domain.useAsMutable = False
        domain.modificationVar = None
        domain.storedIntervals = {}
        return (
         r, r0)

    def _iqg(self, domain, dtype, r0):
        v = domain.modificationVar
        v_0 = domain[v]
        lb, ub = v_0[0], v_0[1]
        if v.domain is not None and array_equal(lb, ub):
            return (r0, r0)
        else:
            assert dtype in (float, float64, int32, int16), 'other types unimplemented yet'
            middle = 0.5 * (lb + ub)
            if v.domain is not None:
                middle1, middle2 = middle.copy(), middle.copy()
                adjust_ux_WithDiscreteDomain(middle1, v)
                adjust_lx_WithDiscreteDomain(middle2, v)
            else:
                middle1 = middle2 = middle
            domain[v] = (v_0[0], middle1)
            domain.localStoredIntervals = {}
            r_l = self.interval(domain, dtype, resetStoredIntervals=False)
            domain[v] = (
             middle2, v_0[1])
            domain.localStoredIntervals = {}
            r_u = self.interval(domain, dtype, resetStoredIntervals=False)
            domain[v] = v_0
            domain.localStoredIntervals = {}
            return (r_l, r_u)

    __pos__ = lambda self: self

    def __add__(self, other):
        for frame_tuple in inspect.stack():
            frame = frame_tuple[0]
            if 'func_code' in dir(frame) and 'func_code' in dir(npSum) and frame.f_code is npSum.func_code:
                pWarn('\n                seems like you use numpy.sum() on FuncDesigner object(s), \n                using FuncDesigner.sum() instead is highly recommended')

        if not isinstance(other, (oofun, list, ndarray, tuple)) and not isscalar(other):
            raise FuncDesignerException('operation oofun_add is not implemented for the type ' + str(type(other)))
        other_is_sum = isinstance(other, oofun) and other._isSum
        from overloads import sum
        if self._isSum and other_is_sum:
            return sum(self._summation_elements + other._summation_elements)
        if self._isSum:
            return sum(self._summation_elements + [other])
        if other_is_sum:
            return sum(other._summation_elements + [self])

        def aux_d(x, y):
            Xsize, Ysize = Len(x), Len(y)
            if Xsize == 1:
                return ones(Ysize)
            if Ysize == 1:
                return Eye(Xsize)
            if Xsize == Ysize:
                if not isinstance(x, multiarray):
                    return Eye(Ysize)
                return ones(Ysize).view(multiarray)
            raise FuncDesignerException('for oofun summation a+b should be size(a)=size(b) or size(a)=1 or size(b)=1')

        if isinstance(other, oofun):
            r = oofun((lambda x, y: x + y), [self, other], d=((lambda x, y: aux_d(x, y)), (lambda x, y: aux_d(y, x))), _isSum=True)
            r._summation_elements = [self, other]
            r.discrete = self.discrete and other.discrete
            r.getOrder = lambda *args, **kwargs: max((self.getOrder(*args, **kwargs), other.getOrder(*args, **kwargs)))
            r._interval_ = lambda *args, **kw: add_interval(self, other, *args, **kw)
        else:
            if isscalar(other) and other == 0:
                return self
            if isinstance(other, OOArray):
                return other + self
        if isinstance(other, ndarray):
            other = other.copy()
        r = oofun((lambda a: a + other), self, _isSum=True)
        r._summation_elements = [self, other]
        r.d = lambda x: aux_d(x, other)
        r._getFuncCalcEngine = lambda *args, **kwargs: self._getFuncCalcEngine(*args, **kwargs) + other
        r.discrete = self.discrete
        r.getOrder = self.getOrder
        Other2 = tile(other, (2, 1))
        r._interval_ = lambda *args, **kw: add_const_interval(self, Other2, *args, **kw)
        if isscalar(other) or asarray(other).size == 1 or 'size' in self.__dict__ and self.size is asarray(other).size:
            r._D = lambda *args, **kwargs: self._D(*args, **kwargs)
        r.vectorized = True
        return r

    __radd__ = __add__

    def __neg__(self):
        if self._neg_elem is not None:
            return self._neg_elem
        else:
            if self._isSum:
                from overloads import sum as FDsum
                return FDsum([ -elem for elem in self._summation_elements ])
            r = oofun((lambda a: -a), self, d=(lambda a: -Eye(Len(a))))
            r._neg_elem = self
            r._getFuncCalcEngine = lambda *args, **kwargs: -self._getFuncCalcEngine(*args, **kwargs)
            r.getOrder = self.getOrder
            r._D = lambda *args, **kwargs: dict((key, -value) for key, value in self._D(*args, **kwargs).items())
            r.d = raise_except
            r.criticalPoints = False
            r.vectorized = True
            r._interval_ = lambda *args, **kw: neg_interval(self, *args, **kw)
            return r

    __sub__ = lambda self, other: self + (-asfarray(other).copy() if type(other) in (list, tuple, ndarray) else -other)
    __rsub__ = lambda self, other: (asfarray(other).copy() if type(other) in (list, tuple, ndarray) else other) + -self

    def __div__(self, other):
        if isinstance(other, OOArray):
            return other.__rdiv__(self)
        if isinstance(other, list):
            other = asarray(other)
        if isscalar(other) or type(other) == ndarray:
            return self * (1.0 / other)
        if isinstance(other, oofun):
            r = oofun((lambda x, y: x / y), [self, other])

            def aux_dx(x, y):
                y = asfarray(y)
                Xsize, Ysize = x.size, y.size
                assert Xsize != 1 and (Xsize == Ysize or Ysize == 1), 'incorrect size for oofun devision'
                if Xsize != 1:
                    if Ysize == 1:
                        r = Diag(None, size=Xsize, scalarMultiplier=1.0 / y)
                    else:
                        r = Diag(1.0 / y)
                else:
                    r = 1.0 / y
                return r

            def aux_dy(x, y):
                x = asfarray(x)
                Xsize, Ysize = Len(x), Len(y)
                r = -x / y ** 2
                if Ysize != 1:
                    assert Xsize == Ysize or Xsize == 1, 'incorrect size for oofun devision'
                    r = Diag(r)
                return r

            r.d = (aux_dx, aux_dy)

            def getOrder(*args, **kwargs):
                order1, order2 = self.getOrder(*args, **kwargs), other.getOrder(*args, **kwargs)
                if order2 == 0:
                    return order1
                return inf

            r.getOrder = getOrder
            r._interval_ = lambda *args, **kw: div_interval(self, other, *args, **kw)
        else:
            other = array(other, 'float')
            r = oofun((lambda a: a / other), self, discrete=self.discrete)
            r.getOrder = self.getOrder
            r._getFuncCalcEngine = lambda *args, **kwargs: self._getFuncCalcEngine(*args, **kwargs) / other
            r.d = lambda x: 1.0 / other if isscalar(x) or x.size == 1 else Diag(ones(x.size) / other)
            r.criticalPoints = False
            if other.size == 1:
                r._D = lambda *args, **kwargs: dict([ (key, value / other) for key, value in self._D(*args, **kwargs).items() ])
                r.d = raise_except
        r.vectorized = True
        return r

    def __rdiv__(self, other):
        if isinstance(other, OOArray) and any([ isinstance(elem, oofun) for elem in atleast_1d(other) ]):
            return other.__div__(self)
        other = array(other, 'float')
        r = oofun((lambda x: other / x), self, discrete=self.discrete)
        r.d = lambda x: Diag(-other / x ** 2)
        r._interval_ = lambda *args, **kw: rdiv_interval(self, other, *args, **kw)

        def getOrder(*args, **kwargs):
            order = self.getOrder(*args, **kwargs)
            if order == 0:
                return 0
            return inf

        r.getOrder = getOrder
        r.vectorized = True
        return r

    def __mul__(self, other):
        if isinstance(other, OOArray):
            return other.__mul__(self)
        isOtherOOFun = isinstance(other, oofun)
        if isinstance(other, list):
            other = asarray(other)
        if self._isProd:
            if not isinstance(self._prod_elements[-1], (oofun, OOArray)):
                if not isOtherOOFun:
                    return self._prod_elements[0] * (other * self._prod_elements[-1])
                return self._prod_elements[0] * other * self._prod_elements[-1]
        if isOtherOOFun:
            r = oofun((lambda x, y: x * y), [self, other])
            r.d = ((lambda x, y: mul_aux_d(x, y)), (lambda x, y: mul_aux_d(y, x)))
            r.getOrder = lambda *args, **kwargs: self.getOrder(*args, **kwargs) + other.getOrder(*args, **kwargs)
        else:
            other = other.copy() if isinstance(other, ndarray) else asarray(other)
            r = oofun((lambda x: x * other), self, discrete=self.discrete)
            r.getOrder = self.getOrder
            r._getFuncCalcEngine = lambda *args, **kwargs: other * self._getFuncCalcEngine(*args, **kwargs)
            r.criticalPoints = False
            if isscalar(other) or asarray(other).size == 1:
                r._D = lambda *args, **kwargs: dict([ (key, value * other) for key, value in self._D(*args, **kwargs).items() ])
                r.d = raise_except
            else:
                r.d = lambda x: mul_aux_d(x, other)
        r._interval_ = lambda *args, **kw: mul_interval(self, other, isOtherOOFun, *args, **kw)
        r.vectorized = True
        r._isProd = True
        elems1 = [self._isProd or self] if 1 else self._prod_elements
        elems2 = [other] if not isinstance(other, oofun) or not other._isProd else other._prod_elements
        r._prod_elements = elems1 + elems2
        return r

    __rmul__ = __mul__

    def __pow__(self, other):
        if isinstance(other, OOArray):
            return other.__rpow__(self)
        d_x = lambda x, y: (y * x ** (y - 1) if isscalar(x) or x.size == 1 or isinstance(x, multiarray) else Diag(y * x ** (y - 1))) if y is not 2 else Diag(2 * x)
        d_y = lambda x, y: x ** y * log(x) if (isscalar(y) or y.size == 1) and not isinstance(x, multiarray) else Diag(x ** y * log(x))
        other_is_oofun = isinstance(other, oofun)
        if not other_is_oofun:
            if isscalar(other):
                if type(other) == int:
                    pass
                else:
                    other = asarray(other, dtype=type(other))
            elif not isinstance(other, ndarray):
                other = asarray(other, dtype='float' if type(other) in (int, int8, int16, int32, int64) else type(other)).copy()
            f = lambda x: asanyarray(x) ** other
            d = lambda x: d_x(x, other)
            input = self
            interval = lambda *args, **kw: pow_const_interval(self, other, *args, **kw)
        else:
            f = lambda x, y: asanyarray(x) ** y
            d = (d_x, d_y)
            input = [self, other]
            interval = lambda *args, **kw: pow_oofun_interval(self, other, *args, **kw)
        r = oofun(f, input, d=d, _interval_=interval)
        if not other_is_oofun:
            r.getOrder = lambda *args, **kw: other * self.getOrder(*args, **kw) if isscalar(other) and int(other) == other and other >= 0 else inf
        if isinstance(other, oofun) or not isinstance(other, int) or type(other) == ndarray and other.flatten()[0] != int:
            r.attach((self > 0)('pow_domain_%d' % r._id, tol=-1e-07))
        r.vectorized = True
        return r

    def __rpow__(self, other):
        assert not isinstance(other, oofun)
        other_is_scalar = isscalar(other)
        if other_is_scalar:
            if type(other) == int:
                other = float(other)
        elif not isinstance(other, ndarray):
            other = asarray(other, 'float' if type(other) in (int, int32, int64, int16, int8) else type(other))
        f = lambda x: other ** x
        d = lambda x: Diag(other ** x * log(other))
        r = oofun(f, self, d=d, criticalPoints=False, vectorized=True)
        if other_is_scalar:
            r.engine_convexity = 1
            r.engine_monotonity = 1 if other > 1 else -1 if other >= 0 else nan
        return r

    def __xor__(self, other):
        raise FuncDesignerException('For power of oofuns use a**b, not a^b')

    def __rxor__(self, other):
        raise FuncDesignerException('For power of oofuns use a**b, not a^b')

    def __getitem__(self, ind):
        if isinstance(ind, oofun):
            self.pWarn('Slicing oofun by oofun IS NOT IMPLEMENTED PROPERLY YET')
            f = lambda x, _ind: x[_ind]

            def d(x, _ind):
                r = zeros(x.shape)
                r[_ind] = 1
                return r

        else:
            if type(ind) not in (int, int32, int64, int16, int8):
                return self.__getslice__(ind.start, ind.stop)
            if not hasattr(self, '_slicesIndexDict'):
                self._slicesIndexDict = {}
            if ind in self._slicesIndexDict:
                return self._slicesIndexDict[ind]
            f = lambda x: x[ind]

            def d(x):
                Xsize = Len(x)
                condBigMatrix = Xsize > 100
                if condBigMatrix and scipyInstalled:
                    r = SparseMatrixConstructor((1, x.shape[0]))
                    r[(0, ind)] = 1.0
                else:
                    if condBigMatrix and not scipyInstalled:
                        self.pWarn(scipyAbsentMsg)
                    r = zeros_like(x)
                    r[ind] = 1
                return r

        r = oofun(f, self, d=d, size=1, getOrder=self.getOrder)
        self._slicesIndexDict[ind] = r
        return r

    def __getslice__(self, ind1, ind2):
        if ind1 is None:
            ind1 = 0
        if ind2 is None:
            if 'size' in self.__dict__ and type(self.size) in (int, int8, int16, int32, int64):
                ind2 = self.size
            else:
                raise FuncDesignerException('if oofun.size is not provided then you should provide full slice coords, e.g. x[3:10], not x[3:]')
        assert not isinstance(ind1, oofun) and not isinstance(ind2, oofun), 'slicing by oofuns is unimplemented yet'
        f = lambda x: x[ind1:ind2]

        def d(x):
            condBigMatrix = Len(x) > 100
            if condBigMatrix and not scipyInstalled:
                self.pWarn(scipyAbsentMsg)
            if condBigMatrix and scipyInstalled:
                r = SP_eye(ind2 - ind1, ind2 - ind1)
                if ind1 != 0:
                    m1 = SparseMatrixConstructor((ind2 - ind1, ind1))
                    r = Hstack((SparseMatrixConstructor((ind2 - ind1, ind1)), r))
                if ind2 != x.size:
                    r = Hstack((r, SparseMatrixConstructor((ind2 - ind1, x.size - ind2))))
            else:
                m1 = zeros((ind2 - ind1, ind1))
                m2 = eye(ind2 - ind1)
                m3 = zeros((ind2 - ind1, x.size - ind2))
                r = hstack((m1, m2, m3))
            return r

        r = oofun(f, self, d=d, getOrder=self.getOrder)
        return r

    def sum(self):

        def d(x):
            if type(x) == ndarray and x.ndim > 1:
                raise FuncDesignerException('sum(x) is not implemented yet for arrays with ndim > 1')
            return ones_like(x)

        def interval(domain, dtype):
            if type(domain) == ooPoint and domain.isMultiPoint:
                raise FuncDesignerException('interval calculations are unimplemented for sum(oofun) yet')
            lb_ub, definiteRange = self._interval(domain, dtype)
            lb, ub = lb_ub[0], lb_ub[1]
            return (vstack((npSum(lb, 0), npSum(ub, 0))), definiteRange)

        r = oofun(npSum, self, getOrder=self.getOrder, _interval_=interval, d=d)
        return r

    def prod(self):
        r = oofun(prod, self)

        def d(x):
            x = asarray(x)
            if x.ndim > 1:
                raise FuncDesignerException('prod(x) is not implemented yet for arrays with ndim > 1')
            ind_zero = where(x == 0)[0].tolist()
            ind_nonzero = nonzero(x)[0].tolist()
            numOfZeros = len(ind_zero)
            r = prod(x) / x
            if numOfZeros >= 2:
                r[ind_zero] = 0
            elif numOfZeros == 1:
                r[ind_zero] = prod(x[ind_nonzero])
            return r

        r.d = d
        return r

    def __gt__(self, other):
        if self.is_oovar and not isinstance(other, (oofun, OOArray)) and not (isinstance(other, ndarray) and str(other.dtype) == 'object'):
            r = BoxBoundConstraint(self, lb=other)
        else:
            if isinstance(other, OOArray) or isinstance(other, ndarray) and str(other.dtype) == 'object':
                return other.__le__(self)
            r = Constraint(self - other, lb=0.0)
        return r

    __ge__ = __gt__

    def __lt__(self, other):
        if self.is_oovar and not isinstance(other, (oofun, OOArray)) and not (isinstance(other, ndarray) and str(other.dtype) == 'object'):
            r = BoxBoundConstraint(self, ub=other)
        else:
            if isinstance(other, OOArray) or isinstance(other, ndarray) and str(other.dtype) == 'object':
                return other.__ge__(self)
            r = Constraint(self - other, ub=0.0)
        return r

    __le__ = __lt__
    __eq__ = lambda self, other: self.eq(other)

    def eq(self, other):
        if other is None or other is () or type(other) == list and len(other) == 0:
            return False
        if type(other) in (str, string_):
            if 'aux_domain' not in self.__dict__:
                if not self.is_oovar:
                    raise FuncDesignerException('comparing with non-numeric data is allowed for string oovars, not for oofuns')
                self.formAuxDomain()
            ind = searchsorted(self.aux_domain, other, 'left')
            if self.aux_domain[ind] != other:
                raise FuncDesignerException('compared value %s is absent in oovar %s domain' % (other, self.name))
            r = Constraint(self - ind, ub=0.0, lb=0.0, tol=0.5)
            if self.is_oovar:
                r.nlh = lambda Lx, Ux, p, dataType: self.nlh(Lx, Ux, p, dataType, ind)
            return r
        if 'startswith' in dir(other):
            return False
        else:
            r = Constraint(self - other, ub=0.0, lb=0.0)
            if self.is_oovar and isscalar(other) and self.domain is not None:
                if self.domain is bool or self.domain is 'bool':
                    if other not in (0, 1):
                        raise FuncDesignerException('bool oovar can be compared with [0,1] only')
                    r.nlh = self.nlh if other == 1.0 else (~self).nlh
                elif self.domain is not int and self.domain is not 'int':
                    pass
            return r

    def _getInput(self, *args, **kwargs):
        r = []
        for item in self.input:
            tmp = item._getFuncCalcEngine(*args, **kwargs) if isinstance(item, oofun) else item(*args, **kwargs) if isinstance(item, OOArray) else item
            r.append(tmp if type(tmp) not in (list, tuple, Stochastic) else asanyarray(tmp))

        return tuple(r)

    def _getDep(self):
        if hasattr(self, 'dep'):
            return self.dep
        else:
            if self.input is None:
                self.dep = None
            else:
                if type(self.input) not in (list, tuple) and not isinstance(self.input, OOArray):
                    self.input = [
                     self.input]
                r_oovars = []
                r_oofuns = []
                isUncycled = True
                Tmp = set()
                for Elem in self.input:
                    if isinstance(Elem, OOArray):
                        for _elem in Elem:
                            if isinstance(_elem, oofun):
                                Tmp.add(_elem)

                for Elem in list(Tmp) + self.input:
                    if not isinstance(Elem, oofun):
                        continue
                    if Elem.is_oovar:
                        r_oovars.append(Elem)
                        continue
                    tmp = Elem._getDep()
                    if not Elem.isUncycled:
                        isUncycled = False
                    if tmp is None or len(tmp) == 0:
                        continue
                    r_oofuns.append(tmp)

                r = set(r_oovars)
                if len(r_oofuns) != 0:
                    r.update(*r_oofuns)
                if len(r_oovars) + sum([ len(elem) for elem in r_oofuns ]) != len(r):
                    isUncycled = False
                self.isUncycled = isUncycled
                self.dep = r
            return self.dep

    def _getFunc(self, *args, **kwargs):
        Args = args
        if len(args) == 0 and len(kwargs) == 0:
            raise FuncDesignerException('at least one argument is required')
        if len(args) != 0:
            if type(args[0]) != str:
                assert not isinstance(args[0], oofun), "you can't invoke oofun on another one oofun"
                x = args[0]
                if isinstance(x, dict) and not isinstance(x, ooPoint):
                    x = ooPoint(x)
                    Args = (x,) + args[1:]
                if self.is_oovar:
                    return self._getFuncCalcEngine(*Args, **kwargs)
            else:
                self.name = args[0]
                return self
        else:
            for fn in ['name', 'size', 'tol']:
                if fn in kwargs:
                    setattr(self, fn, kwargs[fn])

            return self
        if hasattr(x, 'probType') and x.probType == 'MOP':
            s = 'evaluation of MOP result on arguments is unimplemented yet, use r.solutions'
            raise FuncDesignerException(s)
        return self._getFuncCalcEngine(*Args, **kwargs)

    def _getFuncCalcEngine(self, *args, **kwargs):
        x = args[0]
        dep = self._getDep()
        CondSamePointByID = True if type(x) == ooPoint and not x.isMultiPoint and self._point_id == x._id else False
        fixedVarsScheduleID = kwargs.get('fixedVarsScheduleID', -1)
        fixedVars = kwargs.get('fixedVars', None)
        Vars = kwargs.get('Vars', None)
        sameVarsScheduleID = fixedVarsScheduleID == self._lastFuncVarsID
        rebuildFixedCheck = not sameVarsScheduleID
        if fixedVarsScheduleID != -1:
            self._lastFuncVarsID = fixedVarsScheduleID
        if rebuildFixedCheck:
            self._isFixed = fixedVars is not None and dep.issubset(fixedVars) or Vars is not None and dep.isdisjoint(Vars)
        if isinstance(x, ooPoint) and x.isMultiPoint:
            cond_same_point = False
        else:
            cond_same_point = CondSamePointByID or self._f_val_prev is not None and (self._isFixed or self.isCostly and all([ array_equal((x if isinstance(x, dict) else x.xf)[elem], self._f_key_prev[elem]) for elem in dep & set((x if isinstance(x, dict) else x.xf).keys()) ]))
        if cond_same_point:
            self.same += 1
            tmp = self._f_val_prev
            if isinstance(tmp, (ndarray, Stochastic)):
                return tmp.copy()
            return tmp
        else:
            self.evals += 1
            if type(self.args) != tuple:
                self.args = (
                 self.args,)
            Input = self._getInput(*args, **kwargs)
            if not isinstance(x, ooPoint) or not x.isMultiPoint or self.vectorized:
                if self.args != ():
                    Input += self.args
                Tmp = self.fun(*Input)
                if isinstance(Tmp, (list, tuple)):
                    tmp = hstack(Tmp) if len(Tmp) > 1 else Tmp[0]
                else:
                    tmp = Tmp
            else:
                if hasattr(x, 'N'):
                    N = x.N
                else:
                    N = 1
                    for inp in Input:
                        if not isinstance(inp, Stochastic):
                            N = inp.size if type(inp) == ndarray else 1
                            break

                inputs = zip(*[ atleast_1d(inp) if not isinstance(inp, Stochastic) and type(inp) == ndarray and inp.size == N else [inp] * N for inp in Input ])
                Tmp = [ self.fun(*inp) if self.args == () else self.fun(*(inp + self.args)) for inp in inputs ]
                if N == 1:
                    tmp = Tmp[0]
                else:
                    tmp = array([ elem for elem in Tmp ], object).view(multiarray)
            if isinstance(tmp, Stochastic):
                if 'xf' in x.__dict__:
                    maxDistributionSize = getattr(x.xf, 'maxDistributionSize', 0)
                else:
                    maxDistributionSize = getattr(x, 'maxDistributionSize', 0)
                if maxDistributionSize == 0:
                    s = '\n                    if one of function arguments is stochastic distribution \n                    without resolving into quantified value \n                    (e.g. uniform(-10,10) instead of uniform(-10,10, 100), 100 is number of point to emulate)\n                    then you should evaluate the function \n                    onto oopoint with assigned parameter maxDistributionSize'
                    raise FuncDesignerException(s)
                if tmp.size > maxDistributionSize:
                    tmp.reduce(maxDistributionSize)
                tmp.maxDistributionSize = maxDistributionSize
            if type(x) == ooPoint and not x.isMultiPoint and not (isinstance(tmp, ndarray) and type(tmp) != ndarray) or self._isFixed:
                try:
                    t1 = dict([ (elem, copy((x if isinstance(x, dict) else x.xf)[elem])) for elem in dep ]) if self.isCostly else None
                    t2 = tmp.copy() if isinstance(tmp, (ndarray, Stochastic)) else tmp
                    self._f_key_prev, self._f_val_prev = t1, t2
                    if type(x) == ooPoint:
                        self._point_id = x._id
                except:
                    pass

            r = tmp
            return r

    __call__ = _getFunc

    def D(self, x, Vars=None, fixedVars=None, resultKeysType='vars', useSparse=False, exactShape=False, fixedVarsScheduleID=-1):
        if Vars is not None and fixedVars is not None:
            raise FuncDesignerException('No more than one argument from "Vars" and "fixedVars" is allowed for the function')
        if not isinstance(x, ooPoint):
            x = ooPoint(x)
        initialVars = Vars
        if Vars is not None:
            if type(Vars) in [list, tuple]:
                Vars = set(Vars)
            elif isinstance(Vars, oofun):
                if not Vars.is_oovar:
                    raise FuncDesignerException('argument Vars is expected as oovar or python list/tuple of oovar instances')
                Vars = set([Vars])
        if fixedVars is not None:
            if type(fixedVars) in [list, tuple]:
                fixedVars = set(fixedVars)
            elif isinstance(fixedVars, oofun):
                if not fixedVars.is_oovar:
                    raise FuncDesignerException('argument fixedVars is expected as oovar or python list/tuple of oovar instances')
                fixedVars = set([fixedVars])
        r = self._D(x, fixedVarsScheduleID, Vars, fixedVars, useSparse=useSparse)
        r = dict((key, val if type(val) != DiagonalType else val.resolve(useSparse)) for key, val in r.items())
        is_oofun = isinstance(initialVars, oofun)
        if is_oofun and not initialVars.is_oovar:
            raise FuncDesignerException('Cannot perform differentiation by non-oovar input')
        if resultKeysType == 'names':
            raise FuncDesignerException('This possibility is out of date, \n            if it is still present somewhere in FuncDesigner doc inform developers')
        else:
            if resultKeysType == 'vars':
                rr = {}
                for oov, val in x.items():
                    if oov not in r or fixedVars is not None and oov in fixedVars:
                        continue
                    tmp = r[oov]
                    if useSparse == False and hasattr(tmp, 'toarray'):
                        tmp = tmp.toarray()
                    if not exactShape and not isspmatrix(tmp) and not isscalar(tmp):
                        if tmp.size == 1:
                            tmp = asscalar(tmp)
                        elif min(tmp.shape) == 1:
                            tmp = tmp.flatten()
                    rr[oov] = tmp

                if not is_oofun:
                    return rr
                return rr[initialVars]
            raise FuncDesignerException('Incorrect argument resultKeysType, should be "vars" or "names"')
        return

    def _D(self, x, fixedVarsScheduleID, Vars=None, fixedVars=None, useSparse='auto'):
        if self.is_oovar:
            if fixedVars is not None and self in fixedVars or Vars is not None and self not in Vars:
                return {}
            tmp = x[self]
            if not isinstance(tmp, multiarray):
                return {self: Eye(asarray(tmp).size)}
            return {self: ones_like(tmp).view(multiarray)}
        else:
            if self.input[0] is None:
                return {}
            if self.discrete:
                return {}
            CondSamePointByID = True if isinstance(x, ooPoint) and self._point_id1 == x._id else False
            sameVarsScheduleID = fixedVarsScheduleID == self._lastDiffVarsID
            dep = self._getDep()
            rebuildFixedCheck = not sameVarsScheduleID
            if rebuildFixedCheck:
                self._isFixed = fixedVars is not None and dep.issubset(fixedVars) or Vars is not None and dep.isdisjoint(Vars)
            if self._isFixed:
                return {}
            involveStore = self.isCostly
            cond_same_point = sameVarsScheduleID and (CondSamePointByID and self._d_val_prev is not None or involveStore and self._d_key_prev is not None and all([ array_equal(x[elem], self._d_key_prev[elem]) for elem in dep ]))
            if cond_same_point:
                self.same_d += 1
                return dict((key, Copy(val)) for key, val in self._d_val_prev.items())
            self.evals_d += 1
            if isinstance(x, ooPoint):
                self._point_id1 = x._id
            if fixedVarsScheduleID != -1:
                self._lastDiffVarsID = fixedVarsScheduleID
            derivativeSelf = self._getDerivativeSelf(x, fixedVarsScheduleID, Vars, fixedVars)
            r = Derivative()
            ac = -1
            for i, inp in enumerate(self.input):
                if not isinstance(inp, oofun):
                    continue
                if inp.discrete:
                    continue
                if inp.is_oovar:
                    if Vars is not None and inp not in Vars or fixedVars is not None and inp in fixedVars:
                        continue
                    ac += 1
                    tmp = derivativeSelf[ac]
                    val = r.get(inp, None)
                    if val is not None:
                        if isscalar(tmp) or type(val) == type(tmp) == ndarray and prod(tmp.shape) <= prod(val.shape):
                            r[inp] += tmp
                        else:
                            if isspmatrix(val) and type(tmp) == DiagonalType:
                                tmp = tmp.resolve(True)
                            r[inp] = r[inp] + tmp
                    else:
                        r[inp] = tmp
                else:
                    ac += 1
                    elem_d = inp._D(x, fixedVarsScheduleID, Vars=Vars, fixedVars=fixedVars, useSparse=useSparse)
                    t1 = derivativeSelf[ac]
                    for key, val in elem_d.items():
                        if isinstance(t1, Stochastic) or (isscalar(val) or isinstance(val, multiarray)) and (isscalar(t1) or isinstance(t1, multiarray)):
                            rr = t1 * val
                        elif isinstance(val, Stochastic):
                            rr = val * t1
                        elif type(t1) == DiagonalType and type(val) == DiagonalType:
                            rr = t1 * val
                        elif type(t1) == DiagonalType or type(val) == DiagonalType:
                            if isspmatrix(t1):
                                rr = t1._mul_sparse_matrix(val.resolve(True))
                            else:
                                if not isPyPy or type(val) != DiagonalType:
                                    rr = t1 * val
                                else:
                                    rr = (val * t1.T).T
                        elif isscalar(val) or isscalar(t1) or prod(t1.shape) == 1 or prod(val.shape) == 1:
                            rr = (t1 if isscalar(t1) or prod(t1.shape) > 1 else asscalar(t1) if isinstance(t1, ndarray) else t1[(0,
                                                                                                                                 0)]) * (val if isscalar(val) or prod(val.shape) > 1 else asscalar(val) if isinstance(val, ndarray) else val[(0,
                                                                                                                                                                                                                                              0)])
                        else:
                            if val.ndim < 2:
                                val = atleast_2d(val)
                            if useSparse is False:
                                t2 = val
                            else:
                                t1, t2 = self._considerSparse(t1, val)
                            if not type(t1) == type(t2) == ndarray:
                                if not scipyInstalled:
                                    self.pWarn(scipyAbsentMsg)
                                    rr = dot(t1, t2)
                                else:
                                    t1 = t1 if isspmatrix_csc(t1) else t1.tocsc() if isspmatrix(t1) else scipy.sparse.csc_matrix(t1)
                                    t2 = t2 if isspmatrix_csr(t2) else t2.tocsr() if isspmatrix(t2) else scipy.sparse.csr_matrix(t2)
                                    if t2.shape[0] != t1.shape[1]:
                                        if t2.shape[1] == t1.shape[1]:
                                            t2 = t2.T
                                        else:
                                            raise FuncDesignerException('incorrect shape in FuncDesigner function _D(), inform developers about the bug')
                                    rr = t1._mul_sparse_matrix(t2)
                                    if useSparse is False:
                                        rr = rr.toarray()
                            else:
                                rr = dot(t1, t2)
                        Val = r.get(key, None)
                        ValType = type(Val)
                        if Val is not None:
                            if type(rr) == DiagonalType:
                                if ValType == DiagonalType:
                                    Val = Val + rr
                                else:
                                    tmp = rr.resolve(useSparse)
                                    if type(tmp) == ndarray and hasattr(Val, 'toarray'):
                                        Val = Val.toarray()
                                    if type(tmp) == ValType == ndarray and Val.size >= tmp.size:
                                        Val += tmp
                                    else:
                                        Val = Val + tmp
                            else:
                                if isinstance(Val, ndarray) and hasattr(rr, 'toarray'):
                                    rr = rr.toarray()
                                elif hasattr(Val, 'toarray') and isinstance(rr, ndarray):
                                    Val = Val.toarray()
                                if type(rr) == ValType == ndarray and rr.size == Val.size:
                                    Val += rr
                                else:
                                    Val = Val + rr
                            r[key] = Val
                        else:
                            r[key] = rr

            self._d_val_prev = dict([ (key, Copy(value)) for key, value in r.items() ])
            self._d_key_prev = dict([ (elem, Copy(x[elem])) for elem in dep ]) if involveStore else None
            return r

    def _considerSparse(self, t1, t2):
        if int64(prod(t1.shape)) * int64(prod(t2.shape)) > 32768 and isinstance(t1, ndarray) and t1.nonzero()[0].size < 0.25 * t1.size or isinstance(t2, ndarray) and t2.nonzero()[0].size < 0.25 * t2.size:
            if scipy is None:
                self.pWarn(scipyAbsentMsg)
                return (
                 t1, t2)
            t1 = isinstance(t1, scipy.sparse.csc_matrix) or scipy.sparse.csc_matrix(t1)
        if t1.shape[1] != t2.shape[0]:
            if not t1.shape[0] == t2.shape[0]:
                raise AssertionError('bug in FuncDesigner Kernel, inform developers')
                t1 = t1.T
            if not isinstance(t2, scipy.sparse.csr_matrix):
                t2 = scipy.sparse.csr_matrix(t2)
        return (
         t1, t2)

    def _getDerivativeSelf(self, x, fixedVarsScheduleID, Vars, fixedVars):
        Input = self._getInput(x, fixedVarsScheduleID=fixedVarsScheduleID, Vars=Vars, fixedVars=fixedVars)
        expectedTotalInputLength = sum([ Len(elem) for elem in Input ])
        hasUserSuppliedDerivative = self.d is not None
        if hasUserSuppliedDerivative:
            derivativeSelf = []
            if type(self.d) == tuple:
                if len(self.d) != len(self.input):
                    raise FuncDesignerException('oofun error: num(derivatives) not equal to neither 1 nor num(inputs)')
                for i, deriv in enumerate(self.d):
                    inp = self.input[i]
                    if not isinstance(inp, oofun) or inp.discrete:
                        continue
                    if inp.is_oovar and (Vars is not None and inp not in Vars or fixedVars is not None and inp in fixedVars):
                        continue
                    if deriv is None:
                        if not DerApproximatorIsInstalled:
                            raise FuncDesignerException('To perform gradients check you should have DerApproximator installed, see http://openopt.org/DerApproximator')
                        derivativeSelf.append(get_d1(self.fun, Input, diffInt=self.diffInt, stencil=self.stencil, args=self.args, varForDifferentiation=i, pointVal=self._getFuncCalcEngine(x), exactShape=True))
                    else:
                        tmp = deriv(*Input)
                        if not isscalar(tmp) and type(tmp) in (ndarray, tuple, list) and type(tmp) != DiagonalType:
                            tmp = atleast_2d(tmp)
                            _tmp = Input[i]
                            Tmp = 1 if isscalar(_tmp) or prod(_tmp.shape) == 1 else len(Input[i])
                            if tmp.shape[1] != Tmp:
                                if tmp.shape[0] != Tmp:
                                    raise FuncDesignerException('error in getDerivativeSelf()')
                                tmp = tmp.T
                        derivativeSelf.append(tmp)

            else:
                tmp = self.d(*Input)
                if not isscalar(tmp) and type(tmp) in (ndarray, tuple, list):
                    tmp = atleast_2d(tmp)
                    if tmp.shape[1] != expectedTotalInputLength:
                        if tmp.shape[0] != expectedTotalInputLength:
                            raise FuncDesignerException('error in getDerivativeSelf()')
                        tmp = tmp.T
                ac = 0
                if isinstance(tmp, ndarray) and hasattr(tmp, 'toarray') and not isinstance(tmp, multiarray):
                    tmp = tmp.A
                if len(Input) == 1:
                    derivativeSelf = [
                     tmp]
                else:
                    for i, inp in enumerate(Input):
                        t = self.input[i]
                        if t.discrete or t.is_oovar and (Vars is not None and t not in Vars or fixedVars is not None and t in fixedVars):
                            ac += inp.size
                            continue
                        if isinstance(tmp, ndarray):
                            TMP = tmp[:, ac:ac + Len(inp)]
                        elif isscalar(tmp):
                            TMP = tmp
                        elif type(tmp) == DiagonalType:
                            if tmp.size == inp.size and ac == 0:
                                TMP = tmp
                            else:
                                if inp.size > 150 and tmp.size > 150:
                                    tmp = tmp.resolve(True).tocsc()
                                else:
                                    tmp = tmp.resolve(False)
                                TMP = tmp[:, ac:ac + inp.size]
                        else:
                            TMP = tmp.tocsc()[:, ac:ac + inp.size]
                        ac += Len(inp)
                        derivativeSelf.append(TMP)

        else:
            if Vars is not None or fixedVars is not None:
                raise FuncDesignerException("sorry, custom oofun derivatives don't work with Vars/fixedVars arguments yet")
            if not DerApproximatorIsInstalled:
                raise FuncDesignerException('To perform this operation you should have DerApproximator installed, see http://openopt.org/DerApproximator')
            derivativeSelf = get_d1(self.fun, Input, diffInt=self.diffInt, stencil=self.stencil, args=self.args, pointVal=self._getFuncCalcEngine(x), exactShape=True)
            if type(derivativeSelf) == tuple:
                derivativeSelf = list(derivativeSelf)
            elif type(derivativeSelf) != list:
                derivativeSelf = [
                 derivativeSelf]
        return derivativeSelf

    def D2(self, x):
        raise FuncDesignerException('2nd derivatives for obj-funcs are not implemented yet')

    def check_d1(self, point):
        if self.d is None:
            self.disp('Error: no user-provided derivative(s) for oofun ' + self.name + ' are attached')
            return
        else:
            separator = 75 * '*'
            self.disp(separator)
            assert type(self.d) != list
            val = self(point)
            input = self._getInput(point)
            ds = self._getDerivativeSelf(point, fixedVarsScheduleID=-1, Vars=None, fixedVars=None)
            self.disp(self.name + ': checking user-supplied gradient')
            self.disp('according to:')
            self.disp('    diffInt = ' + str(self.diffInt))
            self.disp('    |1 - info_user/info_numerical| < maxViolation = ' + str(self.maxViolation))
            j = -1
            for i in range(len(self.input)):
                if len(self.input) > 1:
                    self.disp('by input variable number ' + str(i) + ':')
                if isinstance(self.d, tuple) and self.d[i] is None:
                    self.disp('user-provided derivative for input number ' + str(i) + ' is absent, skipping the one;')
                    self.disp(separator)
                    continue
                if not isinstance(self.input[i], oofun):
                    self.disp('input number ' + str(i) + ' is not oofun instance, skipping the one;')
                    self.disp(separator)
                    continue
                j += 1
                check_d1((lambda *args: self.fun(*args)), ds[j], input, func_name=self.name, diffInt=self.diffInt, pointVal=val, args=self.args, stencil=max((3, self.stencil)), maxViolation=self.maxViolation, varForCheck=i)

            return

    def getOrder(self, Vars=None, fixedVars=None, fixedVarsScheduleID=-1):
        if isinstance(Vars, oofun):
            Vars = set([Vars])
        elif Vars is not None and type(Vars) != set:
            Vars = set(Vars)
        if isinstance(fixedVars, oofun):
            fixedVars = set([fixedVars])
        elif fixedVars is not None and type(fixedVars) != set:
            fixedVars = set(fixedVars)
        sameVarsScheduleID = fixedVarsScheduleID == self._lastOrderVarsID
        rebuildFixedCheck = not sameVarsScheduleID
        if fixedVarsScheduleID != -1:
            self._lastOrderVarsID = fixedVarsScheduleID
        if rebuildFixedCheck:
            if self.discrete:
                self._order = 0
            if self.is_oovar:
                if fixedVars is not None and self in fixedVars or Vars is not None and self not in Vars:
                    self._order = 0
                else:
                    self._order = 1
            else:
                orders = []
                for inp in self.input:
                    if isinstance(inp, oofun):
                        orders.append(inp.getOrder(Vars, fixedVars))
                    elif isinstance(inp, OOArray):
                        orders += [ elem.getOrder(Vars, fixedVars) if isinstance(elem, oofun) else 0 for elem in inp.view(ndarray) ]

                self._order = inf if any(asarray(orders) != 0) else 0
        return self._order

    def _broadcast(self, func, useAttachedConstraints, *args, **kwargs):
        if self._broadcast_id == oofun._BroadCastID:
            return
        else:
            self._broadcast_id = oofun._BroadCastID
            if self.input is not None:
                for inp in self.input:
                    if not isinstance(inp, oofun):
                        continue
                    inp._broadcast(func, useAttachedConstraints, *args, **kwargs)

            if useAttachedConstraints:
                for c in self.attachedConstraints:
                    c._broadcast(func, useAttachedConstraints, *args, **kwargs)

            func(self, *args, **kwargs)
            return

    def uncertainty(self, point, deviations, actionOnAbsentDeviations='warning'):
        """ 
        result = oofun.uncertainty(point, deviations, actionOnAbsentDeviations='warning')
        point and deviations should be Python dicts of pairs (oovar, value_for_oovar)
        actionOnAbsentDeviations = 
        'error' (raise FuncDesigner exception) | 
        'skip' (treat as fixed number with zero deviation) |
        'warning' (print warning, treat as fixed number) 
        
        Sparse large-scale examples haven't been tested,
        we could implement and test it properly on demand
        """
        dep = self._getDep()
        dev_keys = set(deviations.keys())
        set_diff = dep.difference(dev_keys)
        nAbsent = len(set_diff)
        if actionOnAbsentDeviations != 'skip':
            if len(set_diff) != 0:
                if actionOnAbsentDeviations == 'warning':
                    pWarn('\n                    dict of deviations miss %d variables (oovars): %s;\n                    they will be treated as fixed numbers with zero deviations\n                    ' % (nAbsent, list(set_diff)))
                else:
                    raise FuncDesignerException('dict of deviations miss %d variable(s) (oovars): %s' % (nAbsent, list(set_diff)))
        d = self.D(point, exactShape=True) if nAbsent == 0 else self.D(point, fixedVars=set_diff, exactShape=True)
        tmp = [ dot(val, deviations[key] if isscalar(deviations[key]) else asarray(deviations[key]).reshape(-1, 1)) ** 2 for key, val in d.items() ]
        tmp = [ asscalar(elem) if isinstance(elem, ndarray) and elem.size == 1 else elem for elem in tmp ]
        r = atleast_2d(hstack(tmp)).sum(1)
        return r ** 0.5

    __rtruediv__ = __rdiv__
    __truediv__ = __div__

    def IMPLICATION(*args, **kw):
        raise FuncDesignerException('oofun.IMPLICATION is temporary disabled, use ifThen(...) or IMPLICATION(...) instead')


def nlh_and(_input, dep, Lx, Ux, p, dataType):
    nlh_0 = array(0.0)
    R = {}
    DefiniteRange = True
    elems_nlh = [ elem.nlh(Lx, Ux, p, dataType) if isinstance(elem, oofun) else (0, {}, None) if elem is True else (inf, {}, None) if elem is False else raise_except() for elem in _input
                ]
    for T0, res, DefiniteRange2 in elems_nlh:
        DefiniteRange = logical_and(DefiniteRange, DefiniteRange2)

    for T0, res, DefiniteRange2 in elems_nlh:
        if T0 is None or T0 is True:
            continue
        if T0 is False or all(T0 == inf):
            return (inf, {}, DefiniteRange)
        if all(isnan(T0)):
            raise FuncDesignerException('unimplemented for non-oofun or fixed oofun input yet')
        if type(T0) == ndarray:
            if nlh_0.shape == T0.shape:
                nlh_0 += T0
            else:
                if nlh_0.size == T0.size:
                    nlh_0 += T0.reshape(nlh_0.shape)
                else:
                    nlh_0 = nlh_0 + T0
        else:
            nlh_0 += T0
        T_0_vect = T0.reshape(-1, 1) if type(T0) == ndarray else T0
        for v, val in res.items():
            r = R.get(v, None)
            if r is None:
                R[v] = val - T_0_vect
            else:
                r += (val if r.shape == val.shape else val.reshape(r.shape)) - T_0_vect

    nlh_0_shape = nlh_0.shape
    nlh_0 = nlh_0.reshape(-1, 1)
    for v, val in R.items():
        tmp = val + nlh_0
        tmp[isnan(tmp)] = inf
        R[v] = tmp

    return (nlh_0.reshape(nlh_0_shape), R, DefiniteRange)


def nlh_xor(_input, dep, Lx, Ux, p, dataType):
    nlh_0 = array(0.0)
    nlh_list = []
    nlh_list_m = {}
    num_inf_m = {}
    S_finite = array(0.0)
    num_inf_0 = atleast_1d(0)
    num_inf_elems = []
    R_diff = {}
    R_inf = {}
    DefiniteRange = True
    elems_lh = [ elem.lh(Lx, Ux, p, dataType) if isinstance(elem, oofun) else (inf, {}, None) if elem is True else (0, {}, None) if elem is False else raise_except() for elem in _input
               ]
    for T0, res, DefiniteRange2 in elems_lh:
        DefiniteRange = logical_and(DefiniteRange, DefiniteRange2)

    for j, (T0, res, DefiniteRange2) in enumerate(elems_lh):
        if T0 is None:
            raise FuncDesignerException('probably bug in FD kernel')
        if all(isnan(T0)):
            raise FuncDesignerException('unimplemented for non-oofun or fixed oofun input yet')
        T_inf = where(isfinite(T0), 0, 1)
        num_inf_elems.append(T_inf)
        T0 = where(isfinite(T0), T0, 0.0)
        two_pow_t0 = 2.0 ** T0
        if type(T0) == ndarray:
            if nlh_0.shape == T0.shape:
                nlh_0 += T0
                num_inf_0 += T_inf
                S_finite += two_pow_t0
            elif nlh_0.size == T0.size:
                nlh_0 += T0.reshape(nlh_0.shape)
                num_inf_0 += T_inf.reshape(nlh_0.shape)
                S_finite += two_pow_t0.reshape(nlh_0.shape)
            else:
                nlh_0 = nlh_0 + T0
                num_inf_0 = num_inf_0 + T_inf
                S_finite = S_finite + two_pow_t0.reshape(nlh_0.shape)
        else:
            nlh_0 += T0
            num_inf_0 += T_inf
            S_finite += two_pow_t0
        nlh_list.append(T0)
        for v, val in res.items():
            T_inf_v = where(isfinite(val), 0, 1)
            val_noninf = where(isfinite(val), val, 0)
            T0v = val_noninf - T0.reshape(-1, 1)
            r = nlh_list_m.get(v, None)
            if r is None:
                nlh_list_m[v] = [
                 (
                  j, T0v)]
                num_inf_m[v] = [(j, T_inf_v.copy())]
            else:
                r.append((j, T0v))
                num_inf_m[v].append((j, T_inf_v.copy()))
            r = R_inf.get(v, None)
            T_inf = T_inf.reshape(-1, 1)
            if r is None:
                R_inf[v] = T_inf_v - T_inf
                R_diff[v] = T0v.copy()
            else:
                r += (T_inf_v if r.shape == T_inf_v.shape else T_inf_v.reshape(r.shape)) - T_inf
                R_diff[v] += T0v

    nlh_1 = [ nlh_0 - elem for elem in nlh_list ]
    num_infs = [ num_inf_0 - t for t in num_inf_elems ]
    S1 = PythonSum([ 2.0 ** where(num_infs[j] == 0, -t, -inf) for j, t in enumerate(nlh_1) ])
    S2 = atleast_1d(len(elems_lh) * 2.0 ** (-nlh_0))
    S2[num_inf_0 != 0] = 0
    nlh_t = -log2(S1 - S2)
    R = {}
    nlh_0 = nlh_0.reshape(-1, 1)
    num_inf_0 = num_inf_0.reshape(-1, 1)
    for v, nlh_diff in R_diff.items():
        nlh = nlh_0 + nlh_diff
        nlh_1 = [ nlh - elem.reshape(-1, 1) for elem in nlh_list ]
        for j, val in nlh_list_m[v]:
            nlh_1[j] -= val

        Tmp = R_inf[v] + num_inf_0
        num_infs = [Tmp] * len(nlh_1)
        for j, num_inf in num_inf_m[v]:
            num_infs[j] = num_inf

        num_infs2 = [ Tmp - elem for elem in num_infs ]
        S1 = PythonSum([ 2.0 ** where(num_infs2[j] == 0, -elem, -inf) for j, elem in enumerate(nlh_1) ])
        S2 = atleast_1d(len(elems_lh) * 2.0 ** (-nlh))
        S2[Tmp.reshape(S2.shape) != 0] = 0
        R[v] = -log2(S1 - S2)

    for v, val in R.items():
        val[isnan(val)] = inf
        val[val < 0.0] = 0.0

    return (
     nlh_t, R, DefiniteRange)


def nlh_not(_input_bool_oofun, dep, Lx, Ux, p, dataType):
    if _input_bool_oofun is True or _input_bool_oofun is False:
        raise 'unimplemented for non-oofun input yet'
    T0, res, DefiniteRange = _input_bool_oofun.nlh(Lx, Ux, p, dataType)
    T = reverse_l2P(T0)
    R = dict([ (v, reverse_l2P(val)) for v, val in res.items() ])
    return (T, R, DefiniteRange)


def reverse_l2P(l2P):
    l2P = atleast_1d(l2P)
    r = 1.0 / l2P
    ind = l2P < 15
    r[ind] = -log2(1 - 2 ** (-l2P[ind]))
    return r


def AND(*args):
    Args = args[0] if len(args) == 1 and isinstance(args[0], (ndarray, tuple, list, set)) else args
    assert not isinstance(args[0], ndarray), 'unimplemented yet'
    for arg in Args:
        if not isinstance(arg, oofun):
            raise FuncDesignerException('FuncDesigner logical AND currently is implemented for oofun instances only')

    f = logical_and if len(Args) == 2 else alt_AND_engine
    r = BooleanOOFun(f, Args, vectorized=True)
    r.nlh = lambda *arguments: nlh_and(Args, r._getDep(), *arguments)
    r.oofun = r
    return r


def alt_AND_engine(*input):
    tmp = input[0]
    for i in range(1, len(input)):
        tmp = logical_and(tmp, input[i])

    return tmp


XOR_prev = lambda arg1, arg2: arg1 & ~arg2 | ~arg1 & arg2

def XOR(*args):
    Args = args[0] if len(args) == 1 and isinstance(args[0], (ndarray, tuple, list, set)) else args
    assert not isinstance(args[0], ndarray), 'unimplemented yet'
    for arg in Args:
        if not isinstance(arg, oofun):
            raise FuncDesignerException('FuncDesigner logical XOR currently is implemented for oofun instances only')

    r = BooleanOOFun(f_xor, Args, vectorized=True)
    r.nlh = lambda *arguments: nlh_xor(Args, r._getDep(), *arguments)
    r.oofun = r
    return r


def f_xor(*args):
    r = sum(array(args), 0)
    return r == 1


EQUIVALENT = lambda arg1, arg2: arg1 & arg2 | ~arg1 & ~arg2

def NOT(_bool_oofun):
    if not not isinstance(_bool_oofun, (ndarray, list, tuple, set)):
        raise AssertionError('disjunctive and other logical constraint are not implemented for ooarrays/ndarrays/lists/tuples yet')
        raise (isinstance(_bool_oofun, oofun) or FuncDesignerException)('FuncDesigner logical NOT currently is implemented for oofun instances only')
    r = BooleanOOFun(logical_not, [_bool_oofun], vectorized=True)
    r.oofun = r
    if _bool_oofun.is_oovar:
        r.lh = lambda *arguments: nlh_not(_bool_oofun, r._getDep(), *arguments)
        r.nlh = _bool_oofun.lh
    else:
        r.nlh = lambda *arguments: nlh_not(_bool_oofun, r._getDep(), *arguments)
    return r


NAND = lambda *args, **kw: NOT(AND(*args, **kw))
NOR = lambda *args, **kw: NOT(OR(*args, **kw))

def OR(*args):
    Args = args[0] if len(args) == 1 and isinstance(args[0], (ndarray, list, tuple, set)) else args
    assert not isinstance(args[0], ndarray), 'unimplemented yet'
    for arg in Args:
        if not isinstance(arg, oofun):
            raise FuncDesignerException('FuncDesigner logical AND currently is implemented for oofun instances only')

    r = ~AND([ ~elem for elem in Args ])
    r.oofun = r
    return r


class BooleanOOFun(oofun):
    _unnamedBooleanOOFunNumber = 0
    discrete = True

    def __init__(self, func, _input, *args, **kwargs):
        oofun.__init__(self, func, _input, *args, **kwargs)
        BooleanOOFun._unnamedBooleanOOFunNumber += 1
        self.name = 'unnamed_boolean_oofun_' + str(BooleanOOFun._unnamedBooleanOOFunNumber)
        self.oofun = oofun((lambda *args, **kw: asanyarray(func(*args, **kw), int8)), _input, vectorized=True)
        self.lb = self.ub = 1

    __hash__ = oofun.__hash__

    def size(self, *args, **kwargs):
        raise FuncDesignerException('currently BooleanOOFun.size() is disabled')

    def D(self, *args, **kwargs):
        raise FuncDesignerException('currently BooleanOOFun.D() is disabled')

    def _D(self, *args, **kwargs):
        raise FuncDesignerException('currently BooleanOOFun._D() is disabled')

    def nlh(self, *args, **kw):
        raise FuncDesignerException('This is virtual method to be overloaded in derived class instance')

    __and__ = AND
    __eq__ = EQUIVALENT
    __ne__ = lambda self, arg: NOT(self == arg)

    def __or__(self, other):
        return ~(~self & ~other)

    def __xor__(self, other):
        return BooleanOOFun(logical_xor, (self, other), vectorized=True)

    def __invert__(self):
        r = BooleanOOFun(logical_not, self, vectorized=True)
        r.nlh = lambda *args: nlh_not(self, r._getDep(), *args)
        r.oofun = r
        return r


class BaseFDConstraint(BooleanOOFun):
    isConstraint = True
    tol = 0.0
    expected_kwargs = set(['tol', 'name'])
    __hash__ = oofun.__hash__

    def __call__(self, *args, **kwargs):
        expected_kwargs = self.expected_kwargs
        if not set(kwargs.keys()).issubset(expected_kwargs):
            raise FuncDesignerException('Unexpected kwargs: should be in ' + str(expected_kwargs) + ' got: ' + str(kwargs.keys()))
        for elem in expected_kwargs:
            if elem in kwargs:
                setattr(self, elem, kwargs[elem])

        if len(args) > 1:
            raise FuncDesignerException('No more than single argument is expected')
        if len(args) == 0:
            if len(kwargs) == 0:
                raise FuncDesignerException('You should provide at least one argument')
            return self
        if isinstance(args[0], str):
            self.name = args[0]
            return self
        if hasattr(args[0], 'xf'):
            return self(args[0].xf)
        return self._getFuncCalcEngine(*args, **kwargs)

    def _getFuncCalcEngine(self, *args, **kwargs):
        if not isinstance(args[0], dict):
            raise FuncDesignerException('unexpected type: %s' % type(args[0]))
        isMultiPoint = isinstance(args[0], ooPoint) and args[0].isMultiPoint == True
        val = self.oofun(args[0])
        Tol = max((0.0, self.tol))
        if isMultiPoint:
            return logical_and(self.lb - Tol <= val, val <= self.ub + Tol)
        if any(isnan(val)):
            return False
        if any(atleast_1d(self.lb - val) > Tol):
            return False
        if any(atleast_1d(val - self.ub) > Tol):
            return False
        return True

    def __init__(self, oofun_Involved, *args, **kwargs):
        BooleanOOFun.__init__(self, oofun_Involved._getFuncCalcEngine, ((oofun_Involved.is_oovar or oofun_Involved).input if 1 else oofun_Involved), *args, **kwargs)
        if len(args) != 0:
            raise FuncDesignerException('No args are allowed for FuncDesigner constraint constructor, only some kwargs')
        self.oofun = oofun_Involved


class SmoothFDConstraint(BaseFDConstraint):
    __getitem__ = lambda self, point: self.__call__(point)
    __hash__ = oofun.__hash__

    def __init__(self, *args, **kwargs):
        BaseFDConstraint.__init__(self, *args, **kwargs)
        self.lb, self.ub = -inf, inf
        for key, val in kwargs.items():
            if key in ('lb', 'ub', 'tol'):
                setattr(self, key, asfarray(val))
            else:
                raise FuncDesignerException('Unexpected key in FuncDesigner constraint constructor kwargs')

    def lh(self, *args, **kw):
        if '_invert' not in self.__dict__:
            self._invert = NOT(self)
        return self._invert.nlh(*args, **kw)

    def nlh(self, Lx, Ux, p, dataType):
        m = Lx.shape[0]
        assert m == 0 and 0, 'bug in FuncDesigner'
        tol = self.tol if self.tol > 0.0 else p.contol if self.tol == 0 else 0.0
        if p.solver.dataHandling == 'sorted':
            tol = 0
        selfDep = (self.oofun.is_oovar or self.oofun._getDep)() if 1 else set([self.oofun])
        domainData = [ (v, (Lx[:, k], Ux[:, k])) for k, v in enumerate(p._freeVarsList) if v in selfDep ]
        domain = ooPoint(domainData, skipArrayCast=True)
        domain.isMultiPoint = True
        domain.dictOfFixedFuncs = p.dictOfFixedFuncs
        r, r0 = self.oofun.iqg(domain, dataType, self.lb, self.ub)
        Lf, Uf = r0.lb, r0.ub
        tmp = getSmoothNLH(tile(Lf, (2, 1)), tile(Uf, (2, 1)), self.lb, self.ub, tol, m, dataType)
        T02 = tmp
        T0 = T02[:, tmp.shape[1] / 2:].flatten()
        res = {}
        if len(r):
            dep = selfDep.intersection(domain.keys())
            for v in dep:
                Lf, Uf = vstack((r[v][0].lb, r[v][1].lb)), vstack((r[v][0].ub, r[v][1].ub))
                tmp = getSmoothNLH(Lf, Uf, self.lb, self.ub, tol, m, dataType)
                res[v] = tmp

        return (
         T0, res, r0.definiteRange)


def getSmoothNLH(Lf, Uf, lb, ub, tol, m, dataType):
    M = prod(Lf.shape) / (2 * m)
    Lf, Uf = Lf.reshape(2 * M, m).T, Uf.reshape(2 * M, m).T
    lf1, lf2, uf1, uf2 = (
     Lf[:, 0:M], Lf[:, M:2 * M], Uf[:, 0:M], Uf[:, M:2 * M])
    UfLfDiff = Uf - Lf
    if UfLfDiff.dtype.type in [int8, int16, int32, int64, int]:
        UfLfDiff = asfarray(UfLfDiff)
    if lb == ub:
        val = ub
        ind1, ind2 = val - tol > Uf, val + tol < Lf
        Uf_t, Lf_t = Uf.copy(), Lf.copy()
        if Uf.dtype.type in [int8, int16, int32, int64, int] or Lf.dtype.type in [int8, int16, int32, int64, int]:
            Uf_t, Lf_t = asfarray(Uf_t), asfarray(Lf_t)
        Uf_t[Uf_t > val + tol] = val + tol
        Lf_t[Lf_t < val - tol] = val - tol
        allowedLineSegmentLength = Uf_t - Lf_t
        tmp = allowedLineSegmentLength / UfLfDiff
        tmp[logical_or(isinf(Lf), isinf(Uf))] = 1e-10
        tmp[allowedLineSegmentLength == 0.0] = 1.0
        tmp[tmp < 1e-300] = 1e-300
        tmp[val - tol > Uf] = 0
        tmp[val + tol < Lf] = 0
    elif isfinite(lb) and not isfinite(ub):
        tmp = (Uf - (lb - tol)) / UfLfDiff
        tmp[logical_and(isinf(Lf), logical_not(isinf(Uf)))] = 1e-10
        tmp[isinf(Uf)] = 0.9999999999
        tmp[tmp < 1e-300] = 1e-300
        tmp[tmp > 1.0] = 1.0
        tmp[lb - tol > Uf] = 0
        tmp[lb <= Lf] = 1
    elif isfinite(ub) and not isfinite(lb):
        tmp = (ub + tol - Lf) / UfLfDiff
        tmp[isinf(Lf)] = 0.9999999999
        tmp[logical_and(isinf(Uf), logical_not(isinf(Lf)))] = 1e-10
        tmp[tmp < 1e-300] = 1e-300
        tmp[tmp > 1.0] = 1.0
        tmp[ub + tol < Lf] = 0
        tmp[ub >= Uf] = 1
    else:
        raise FuncDesignerException('this part of interalg code is unimplemented for double-box-bound constraints yet')
    tmp = -log2(tmp)
    tmp[isnan(tmp)] = inf
    return tmp


class Constraint(SmoothFDConstraint):
    __hash__ = oofun.__hash__

    def __init__(self, *args, **kwargs):
        SmoothFDConstraint.__init__(self, *args, **kwargs)


class BoxBoundConstraint(SmoothFDConstraint):

    def __init__(self, *args, **kwargs):
        SmoothFDConstraint.__init__(self, *args, **kwargs)

    __hash__ = oofun.__hash__


class Derivative(dict):

    def __init__(self):
        pass


def atleast_oofun(arg):
    if isinstance(arg, oofun):
        return arg
    else:
        if hasattr(arg, 'copy'):
            tmp = arg.copy()
            return oofun((lambda *args, **kwargs: tmp), input=None, getOrder=(lambda *args, **kwargs: 0), discrete=True)
        if isscalar(arg):
            tmp = array(arg, 'float')
            return oofun((lambda *args, **kwargs: tmp), input=None, getOrder=(lambda *args, **kwargs: 0), discrete=True)
        raise FuncDesignerException('incorrect type for the function _atleast_oofun')
        return


def mul_aux_d(x, y):
    Xsize, Ysize = Len(x), Len(y)
    if Xsize == 1:
        return Copy(y)
    else:
        if Ysize == 1:
            return Diag(None, scalarMultiplier=y, size=Xsize)
        if Xsize == Ysize:
            return Diag(y)
        raise FuncDesignerException('for oofun multiplication a*b should be size(a)=size(b) or size(a)=1 or size(b)=1')
        return