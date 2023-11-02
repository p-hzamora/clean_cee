# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: FuncDesigner\overloads.pyc
# Compiled at: 2013-05-21 10:54:48
PythonSum = sum
PythonMax = max
from ooFun import oofun
import numpy as np
from FDmisc import FuncDesignerException, Diag, Eye, raise_except, diagonal, DiagonalType, dictSum
from ooFun import atleast_oofun, Vstack, Copy
from ooarray import ooarray
from Interval import TrigonometryCriticalPoints, nonnegative_interval, ZeroCriticalPointsInterval, box_1_interval, defaultIntervalEngine
from numpy import atleast_1d, logical_and
from FuncDesigner.multiarray import multiarray
from boundsurf import boundsurf, surf
try:
    from scipy.sparse import isspmatrix, lil_matrix as Zeros
    scipyInstalled = True
except ImportError:
    scipyInstalled = False
    isspmatrix = lambda *args, **kw: False
    Zeros = np.zeros

__all__ = []
try:
    import distribution
    hasStochastic = True
except:
    hasStochastic = False

st_sin = (--- This code section failed: ---

 L.  52         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             0  'x'
                6  LOAD_GLOBAL           1  'distribution'
                9  LOAD_ATTR             2  'stochasticDistribution'
               12  CALL_FUNCTION_2       2  None
               15  POP_JUMP_IF_FALSE    61  'to 61'
               18  LOAD_GLOBAL           1  'distribution'
               21  LOAD_ATTR             2  'stochasticDistribution'
               24  LOAD_GLOBAL           3  'sin'
               27  LOAD_FAST             0  'x'
               30  LOAD_ATTR             4  'values'
               33  CALL_FUNCTION_1       1  None
               36  LOAD_FAST             0  'x'
               39  LOAD_ATTR             5  'probabilities'
               42  LOAD_ATTR             6  'copy'
               45  CALL_FUNCTION_0       0  None
               48  CALL_FUNCTION_2       2  None
               51  LOAD_ATTR             7  '_update'
               54  LOAD_FAST             0  'x'
               57  CALL_FUNCTION_1       1  None
               60  RETURN_END_IF_LAMBDA
             61_0  COME_FROM            15  '15'

 L.  53        61  LOAD_GLOBAL           0  'isinstance'
               64  LOAD_FAST             0  'x'
               67  LOAD_GLOBAL           8  'multiarray'
               70  CALL_FUNCTION_2       2  None
               73  POP_JUMP_IF_FALSE   151  'to 151'
               76  LOAD_GLOBAL           0  'isinstance'
               79  LOAD_FAST             0  'x'
               82  LOAD_ATTR             9  'flat'
               85  LOAD_CONST               0
               88  BINARY_SUBSCR    
               89  LOAD_GLOBAL           1  'distribution'
               92  LOAD_ATTR             2  'stochasticDistribution'
               95  CALL_FUNCTION_2       2  None
             98_0  COME_FROM            73  '73'
               98  POP_JUMP_IF_FALSE   151  'to 151'
              101  LOAD_GLOBAL          10  'np'
              104  LOAD_ATTR            11  'array'
              107  BUILD_LIST_0          0 
              110  LOAD_FAST             0  'x'
              113  LOAD_ATTR             9  'flat'
              116  GET_ITER         
              117  FOR_ITER             18  'to 138'
              120  STORE_FAST            1  'elem'
              123  LOAD_GLOBAL           3  'sin'
              126  LOAD_FAST             1  'elem'
              129  CALL_FUNCTION_1       1  None
              132  LIST_APPEND           2  None
              135  JUMP_BACK           117  'to 117'
              138  CALL_FUNCTION_1       1  None
              141  LOAD_ATTR            12  'view'
              144  LOAD_GLOBAL           8  'multiarray'
              147  CALL_FUNCTION_1       1  None
              150  RETURN_END_IF_LAMBDA
            151_0  COME_FROM            98  '98'

 L.  54       151  LOAD_GLOBAL          10  'np'
              154  LOAD_ATTR             3  'sin'
              157  LOAD_FAST             0  'x'
              160  CALL_FUNCTION_1       1  None
              163  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 150
) if hasStochastic else np.sin

def sin_interval(r, inp, domain, dtype):
    lb_ub, definiteRange = inp._interval(domain, dtype, allowBoundSurf=True)
    isBoundsurf = type(lb_ub) == boundsurf
    lb_ub_resolved = lb_ub.resolve()[0] if isBoundsurf else lb_ub
    lb, ub = lb_ub_resolved
    if isBoundsurf:
        if np.all(lb >= 0.0) and np.all(ub <= np.pi):
            return defaultIntervalEngine(lb_ub, np.sin, np.cos, monotonity=np.nan, convexity=-1, criticalPoint=np.pi / 2, criticalPointValue=1.0)
        if np.all(lb >= -np.pi) and np.all(ub <= 0.0):
            return defaultIntervalEngine(lb_ub, np.sin, np.cos, monotonity=np.nan, convexity=1, criticalPoint=-np.pi / 2, criticalPointValue=-1.0)
    return oofun._interval_(r, domain, dtype)


def sin(inp):
    if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
        return ooarray([ sin(elem) for elem in inp ])
    if hasStochastic and isinstance(inp, distribution.stochasticDistribution):
        return distribution.stochasticDistribution(sin(inp.values), inp.probabilities.copy())._update(inp)
    if not isinstance(inp, oofun):
        return np.sin(inp)
    r = oofun(st_sin, inp, d=(lambda x: Diag(np.cos(x))), vectorized=True, criticalPoints=TrigonometryCriticalPoints)
    r._interval_ = lambda domain, dtype: sin_interval(r, inp, domain, dtype)
    return r


st_cos = (--- This code section failed: ---

 L.  88         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             0  'x'
                6  LOAD_GLOBAL           1  'distribution'
                9  LOAD_ATTR             2  'stochasticDistribution'
               12  CALL_FUNCTION_2       2  None
               15  POP_JUMP_IF_FALSE    61  'to 61'
               18  LOAD_GLOBAL           1  'distribution'
               21  LOAD_ATTR             2  'stochasticDistribution'
               24  LOAD_GLOBAL           3  'cos'
               27  LOAD_FAST             0  'x'
               30  LOAD_ATTR             4  'values'
               33  CALL_FUNCTION_1       1  None
               36  LOAD_FAST             0  'x'
               39  LOAD_ATTR             5  'probabilities'
               42  LOAD_ATTR             6  'copy'
               45  CALL_FUNCTION_0       0  None
               48  CALL_FUNCTION_2       2  None
               51  LOAD_ATTR             7  '_update'
               54  LOAD_FAST             0  'x'
               57  CALL_FUNCTION_1       1  None
               60  RETURN_END_IF_LAMBDA
             61_0  COME_FROM            15  '15'

 L.  89        61  LOAD_GLOBAL           0  'isinstance'
               64  LOAD_FAST             0  'x'
               67  LOAD_GLOBAL           8  'multiarray'
               70  CALL_FUNCTION_2       2  None
               73  POP_JUMP_IF_FALSE   151  'to 151'
               76  LOAD_GLOBAL           0  'isinstance'
               79  LOAD_FAST             0  'x'
               82  LOAD_ATTR             9  'flat'
               85  LOAD_CONST               0
               88  BINARY_SUBSCR    
               89  LOAD_GLOBAL           1  'distribution'
               92  LOAD_ATTR             2  'stochasticDistribution'
               95  CALL_FUNCTION_2       2  None
             98_0  COME_FROM            73  '73'
               98  POP_JUMP_IF_FALSE   151  'to 151'
              101  LOAD_GLOBAL          10  'np'
              104  LOAD_ATTR            11  'array'
              107  BUILD_LIST_0          0 
              110  LOAD_FAST             0  'x'
              113  LOAD_ATTR             9  'flat'
              116  GET_ITER         
              117  FOR_ITER             18  'to 138'
              120  STORE_FAST            1  'elem'
              123  LOAD_GLOBAL           3  'cos'
              126  LOAD_FAST             1  'elem'
              129  CALL_FUNCTION_1       1  None
              132  LIST_APPEND           2  None
              135  JUMP_BACK           117  'to 117'
              138  CALL_FUNCTION_1       1  None
              141  LOAD_ATTR            12  'view'
              144  LOAD_GLOBAL           8  'multiarray'
              147  CALL_FUNCTION_1       1  None
              150  RETURN_END_IF_LAMBDA
            151_0  COME_FROM            98  '98'

 L.  90       151  LOAD_GLOBAL          10  'np'
              154  LOAD_ATTR             3  'cos'
              157  LOAD_FAST             0  'x'
              160  CALL_FUNCTION_1       1  None
              163  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 150
) if hasStochastic else np.cos

def cos_interval(r, inp, domain, dtype):
    lb_ub, definiteRange = inp._interval(domain, dtype, allowBoundSurf=True)
    isBoundsurf = type(lb_ub) == boundsurf
    lb_ub_resolved = lb_ub.resolve()[0] if isBoundsurf else lb_ub
    lb, ub = lb_ub_resolved
    if isBoundsurf and np.all(lb >= -np.pi / 2) and np.all(ub <= np.pi / 2):
        return defaultIntervalEngine(lb_ub, np.cos, (lambda x: -np.sin(x)), monotonity=np.nan, convexity=-1, criticalPoint=0.0, criticalPointValue=1.0)
    else:
        return oofun._interval_(r, domain, dtype)


def cos(inp):
    if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
        return ooarray([ cos(elem) for elem in inp ])
    if hasStochastic and isinstance(inp, distribution.stochasticDistribution):
        return distribution.stochasticDistribution(cos(inp.values), inp.probabilities.copy())._update(inp)
    if not isinstance(inp, oofun):
        return np.cos(inp)
    r = oofun(st_cos, inp, d=(lambda x: Diag(-np.sin(x))), vectorized=True, criticalPoints=TrigonometryCriticalPoints)
    r._interval_ = lambda domain, dtype: cos_interval(r, inp, domain, dtype)
    return r


st_tan = (--- This code section failed: ---

 L. 120         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             0  'x'
                6  LOAD_GLOBAL           1  'distribution'
                9  LOAD_ATTR             2  'stochasticDistribution'
               12  CALL_FUNCTION_2       2  None
               15  POP_JUMP_IF_FALSE    61  'to 61'
               18  LOAD_GLOBAL           1  'distribution'
               21  LOAD_ATTR             2  'stochasticDistribution'
               24  LOAD_GLOBAL           3  'tan'
               27  LOAD_FAST             0  'x'
               30  LOAD_ATTR             4  'values'
               33  CALL_FUNCTION_1       1  None
               36  LOAD_FAST             0  'x'
               39  LOAD_ATTR             5  'probabilities'
               42  LOAD_ATTR             6  'copy'
               45  CALL_FUNCTION_0       0  None
               48  CALL_FUNCTION_2       2  None
               51  LOAD_ATTR             7  '_update'
               54  LOAD_FAST             0  'x'
               57  CALL_FUNCTION_1       1  None
               60  RETURN_END_IF_LAMBDA
             61_0  COME_FROM            15  '15'

 L. 121        61  LOAD_GLOBAL           0  'isinstance'
               64  LOAD_FAST             0  'x'
               67  LOAD_GLOBAL           8  'multiarray'
               70  CALL_FUNCTION_2       2  None
               73  POP_JUMP_IF_FALSE   151  'to 151'
               76  LOAD_GLOBAL           0  'isinstance'
               79  LOAD_FAST             0  'x'
               82  LOAD_ATTR             9  'flat'
               85  LOAD_CONST               0
               88  BINARY_SUBSCR    
               89  LOAD_GLOBAL           1  'distribution'
               92  LOAD_ATTR             2  'stochasticDistribution'
               95  CALL_FUNCTION_2       2  None
             98_0  COME_FROM            73  '73'
               98  POP_JUMP_IF_FALSE   151  'to 151'
              101  LOAD_GLOBAL          10  'np'
              104  LOAD_ATTR            11  'array'
              107  BUILD_LIST_0          0 
              110  LOAD_FAST             0  'x'
              113  LOAD_ATTR             9  'flat'
              116  GET_ITER         
              117  FOR_ITER             18  'to 138'
              120  STORE_FAST            1  'elem'
              123  LOAD_GLOBAL           3  'tan'
              126  LOAD_FAST             1  'elem'
              129  CALL_FUNCTION_1       1  None
              132  LIST_APPEND           2  None
              135  JUMP_BACK           117  'to 117'
              138  CALL_FUNCTION_1       1  None
              141  LOAD_ATTR            12  'view'
              144  LOAD_GLOBAL           8  'multiarray'
              147  CALL_FUNCTION_1       1  None
              150  RETURN_END_IF_LAMBDA
            151_0  COME_FROM            98  '98'

 L. 122       151  LOAD_GLOBAL          10  'np'
              154  LOAD_ATTR             3  'tan'
              157  LOAD_FAST             0  'x'
              160  CALL_FUNCTION_1       1  None
              163  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 150
) if hasStochastic else np.tan

def tan_interval(inp, r, domain, dtype):
    lb_ub, definiteRange = inp._interval(domain, dtype, allowBoundSurf=True)
    isBoundSurf = type(lb_ub) == boundsurf
    lb, ub = lb_ub.resolve()[0] if isBoundSurf else lb_ub
    if np.any(lb < -np.pi / 2) or np.any(ub > np.pi / 2):
        raise FuncDesignerException('interval for tan() is unimplemented for range beyond (-pi/2, pi/2) yet')
    if isBoundSurf:
        if np.all(lb >= 0) and np.all(ub <= np.pi / 2):
            return defaultIntervalEngine(lb_ub, np.tan, r.d, monotonity=1, convexity=1)
        if np.all(lb >= -np.pi / 2) and np.all(ub <= 0):
            return defaultIntervalEngine(lb_ub, np.tan, r.d, monotonity=1, convexity=-1)
    return oofun._interval_(r, domain, dtype)


def tan(inp):
    if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
        return ooarray([ tan(elem) for elem in inp ])
    if hasStochastic and isinstance(inp, distribution.stochasticDistribution):
        return distribution.stochasticDistribution(tan(inp.values), inp.probabilities.copy())._update(inp)
    if not isinstance(inp, oofun):
        return np.tan(inp)
    r = oofun(st_tan, inp, d=(lambda x: Diag(1.0 / np.cos(x) ** 2)), vectorized=True, criticalPoints=False, engine_monotonity=1)
    r._interval_ = lambda domain, dtype: tan_interval(inp, r, domain, dtype)
    return r


__all__ += ['sin', 'cos', 'tan']
st_arcsin = (--- This code section failed: ---

 L. 160         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             0  'x'
                6  LOAD_GLOBAL           1  'distribution'
                9  LOAD_ATTR             2  'stochasticDistribution'
               12  CALL_FUNCTION_2       2  None
               15  POP_JUMP_IF_FALSE    61  'to 61'
               18  LOAD_GLOBAL           1  'distribution'
               21  LOAD_ATTR             2  'stochasticDistribution'
               24  LOAD_GLOBAL           3  'arcsin'
               27  LOAD_FAST             0  'x'
               30  LOAD_ATTR             4  'values'
               33  CALL_FUNCTION_1       1  None
               36  LOAD_FAST             0  'x'
               39  LOAD_ATTR             5  'probabilities'
               42  LOAD_ATTR             6  'copy'
               45  CALL_FUNCTION_0       0  None
               48  CALL_FUNCTION_2       2  None
               51  LOAD_ATTR             7  '_update'
               54  LOAD_FAST             0  'x'
               57  CALL_FUNCTION_1       1  None
               60  RETURN_END_IF_LAMBDA
             61_0  COME_FROM            15  '15'

 L. 161        61  LOAD_GLOBAL           0  'isinstance'
               64  LOAD_FAST             0  'x'
               67  LOAD_GLOBAL           8  'multiarray'
               70  CALL_FUNCTION_2       2  None
               73  POP_JUMP_IF_FALSE   151  'to 151'
               76  LOAD_GLOBAL           0  'isinstance'
               79  LOAD_FAST             0  'x'
               82  LOAD_ATTR             9  'flat'
               85  LOAD_CONST               0
               88  BINARY_SUBSCR    
               89  LOAD_GLOBAL           1  'distribution'
               92  LOAD_ATTR             2  'stochasticDistribution'
               95  CALL_FUNCTION_2       2  None
             98_0  COME_FROM            73  '73'
               98  POP_JUMP_IF_FALSE   151  'to 151'
              101  LOAD_GLOBAL          10  'np'
              104  LOAD_ATTR            11  'array'
              107  BUILD_LIST_0          0 
              110  LOAD_FAST             0  'x'
              113  LOAD_ATTR             9  'flat'
              116  GET_ITER         
              117  FOR_ITER             18  'to 138'
              120  STORE_FAST            1  'elem'
              123  LOAD_GLOBAL           3  'arcsin'
              126  LOAD_FAST             1  'elem'
              129  CALL_FUNCTION_1       1  None
              132  LIST_APPEND           2  None
              135  JUMP_BACK           117  'to 117'
              138  CALL_FUNCTION_1       1  None
              141  LOAD_ATTR            12  'view'
              144  LOAD_GLOBAL           8  'multiarray'
              147  CALL_FUNCTION_1       1  None
              150  RETURN_END_IF_LAMBDA
            151_0  COME_FROM            98  '98'

 L. 162       151  LOAD_GLOBAL          10  'np'
              154  LOAD_ATTR             3  'arcsin'
              157  LOAD_FAST             0  'x'
              160  CALL_FUNCTION_1       1  None
              163  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 150
) if hasStochastic else np.arcsin

def arcsin(inp):
    if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
        return ooarray([ arcsin(elem) for elem in inp ])
    if hasStochastic and isinstance(inp, distribution.stochasticDistribution):
        return distribution.stochasticDistribution(arcsin(inp.values), inp.probabilities.copy())._update(inp)
    if not isinstance(inp, oofun):
        return np.arcsin(inp)
    r = oofun(st_arcsin, inp, d=(lambda x: Diag(1.0 / np.sqrt(1.0 - x ** 2))), vectorized=True)
    r._interval_ = lambda domain, dtype: box_1_interval(inp, np.arcsin, r.d, domain, dtype)
    r.attach((inp > -1)('arcsin_domain_lower_bound_%d' % r._id, tol=-1e-07), (inp < 1)('arcsin_domain_upper_bound_%d' % r._id, tol=-1e-07))
    return r


st_arccos = (--- This code section failed: ---

 L. 181         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             0  'x'
                6  LOAD_GLOBAL           1  'distribution'
                9  LOAD_ATTR             2  'stochasticDistribution'
               12  CALL_FUNCTION_2       2  None
               15  POP_JUMP_IF_FALSE    61  'to 61'
               18  LOAD_GLOBAL           1  'distribution'
               21  LOAD_ATTR             2  'stochasticDistribution'
               24  LOAD_GLOBAL           3  'arccos'
               27  LOAD_FAST             0  'x'
               30  LOAD_ATTR             4  'values'
               33  CALL_FUNCTION_1       1  None
               36  LOAD_FAST             0  'x'
               39  LOAD_ATTR             5  'probabilities'
               42  LOAD_ATTR             6  'copy'
               45  CALL_FUNCTION_0       0  None
               48  CALL_FUNCTION_2       2  None
               51  LOAD_ATTR             7  '_update'
               54  LOAD_FAST             0  'x'
               57  CALL_FUNCTION_1       1  None
               60  RETURN_END_IF_LAMBDA
             61_0  COME_FROM            15  '15'

 L. 182        61  LOAD_GLOBAL           0  'isinstance'
               64  LOAD_FAST             0  'x'
               67  LOAD_GLOBAL           8  'multiarray'
               70  CALL_FUNCTION_2       2  None
               73  POP_JUMP_IF_FALSE   151  'to 151'
               76  LOAD_GLOBAL           0  'isinstance'
               79  LOAD_FAST             0  'x'
               82  LOAD_ATTR             9  'flat'
               85  LOAD_CONST               0
               88  BINARY_SUBSCR    
               89  LOAD_GLOBAL           1  'distribution'
               92  LOAD_ATTR             2  'stochasticDistribution'
               95  CALL_FUNCTION_2       2  None
             98_0  COME_FROM            73  '73'
               98  POP_JUMP_IF_FALSE   151  'to 151'
              101  LOAD_GLOBAL          10  'np'
              104  LOAD_ATTR            11  'array'
              107  BUILD_LIST_0          0 
              110  LOAD_FAST             0  'x'
              113  LOAD_ATTR             9  'flat'
              116  GET_ITER         
              117  FOR_ITER             18  'to 138'
              120  STORE_FAST            1  'elem'
              123  LOAD_GLOBAL           3  'arccos'
              126  LOAD_FAST             1  'elem'
              129  CALL_FUNCTION_1       1  None
              132  LIST_APPEND           2  None
              135  JUMP_BACK           117  'to 117'
              138  CALL_FUNCTION_1       1  None
              141  LOAD_ATTR            12  'view'
              144  LOAD_GLOBAL           8  'multiarray'
              147  CALL_FUNCTION_1       1  None
              150  RETURN_END_IF_LAMBDA
            151_0  COME_FROM            98  '98'

 L. 183       151  LOAD_GLOBAL          10  'np'
              154  LOAD_ATTR             3  'arccos'
              157  LOAD_FAST             0  'x'
              160  CALL_FUNCTION_1       1  None
              163  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 150
) if hasStochastic else np.arccos

def arccos(inp):
    if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
        return ooarray([ arccos(elem) for elem in inp ])
    if hasStochastic and isinstance(inp, distribution.stochasticDistribution):
        return distribution.stochasticDistribution(arccos(inp.values), inp.probabilities.copy())._update(inp)
    if not isinstance(inp, oofun):
        return np.arccos(inp)
    r = oofun(st_arccos, inp, d=(lambda x: Diag(-1.0 / np.sqrt(1.0 - x ** 2))), vectorized=True)
    r._interval_ = lambda domain, dtype: box_1_interval(inp, np.arccos, r.d, domain, dtype)
    r.attach((inp > -1)('arccos_domain_lower_bound_%d' % r._id, tol=-1e-07), (inp < 1)('arccos_domain_upper_bound_%d' % r._id, tol=-1e-07))
    return r


st_arctan = (--- This code section failed: ---

 L. 202         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             0  'x'
                6  LOAD_GLOBAL           1  'distribution'
                9  LOAD_ATTR             2  'stochasticDistribution'
               12  CALL_FUNCTION_2       2  None
               15  POP_JUMP_IF_FALSE    61  'to 61'
               18  LOAD_GLOBAL           1  'distribution'
               21  LOAD_ATTR             2  'stochasticDistribution'
               24  LOAD_GLOBAL           3  'arctan'
               27  LOAD_FAST             0  'x'
               30  LOAD_ATTR             4  'values'
               33  CALL_FUNCTION_1       1  None
               36  LOAD_FAST             0  'x'
               39  LOAD_ATTR             5  'probabilities'
               42  LOAD_ATTR             6  'copy'
               45  CALL_FUNCTION_0       0  None
               48  CALL_FUNCTION_2       2  None
               51  LOAD_ATTR             7  '_update'
               54  LOAD_FAST             0  'x'
               57  CALL_FUNCTION_1       1  None
               60  RETURN_END_IF_LAMBDA
             61_0  COME_FROM            15  '15'

 L. 203        61  LOAD_GLOBAL           0  'isinstance'
               64  LOAD_FAST             0  'x'
               67  LOAD_GLOBAL           8  'multiarray'
               70  CALL_FUNCTION_2       2  None
               73  POP_JUMP_IF_FALSE   151  'to 151'
               76  LOAD_GLOBAL           0  'isinstance'
               79  LOAD_FAST             0  'x'
               82  LOAD_ATTR             9  'flat'
               85  LOAD_CONST               0
               88  BINARY_SUBSCR    
               89  LOAD_GLOBAL           1  'distribution'
               92  LOAD_ATTR             2  'stochasticDistribution'
               95  CALL_FUNCTION_2       2  None
             98_0  COME_FROM            73  '73'
               98  POP_JUMP_IF_FALSE   151  'to 151'
              101  LOAD_GLOBAL          10  'np'
              104  LOAD_ATTR            11  'array'
              107  BUILD_LIST_0          0 
              110  LOAD_FAST             0  'x'
              113  LOAD_ATTR             9  'flat'
              116  GET_ITER         
              117  FOR_ITER             18  'to 138'
              120  STORE_FAST            1  'elem'
              123  LOAD_GLOBAL           3  'arctan'
              126  LOAD_FAST             1  'elem'
              129  CALL_FUNCTION_1       1  None
              132  LIST_APPEND           2  None
              135  JUMP_BACK           117  'to 117'
              138  CALL_FUNCTION_1       1  None
              141  LOAD_ATTR            12  'view'
              144  LOAD_GLOBAL           8  'multiarray'
              147  CALL_FUNCTION_1       1  None
              150  RETURN_END_IF_LAMBDA
            151_0  COME_FROM            98  '98'

 L. 204       151  LOAD_GLOBAL          10  'np'
              154  LOAD_ATTR             3  'arctan'
              157  LOAD_FAST             0  'x'
              160  CALL_FUNCTION_1       1  None
              163  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 150
) if hasStochastic else np.arctan

def arctan_interval(inp, r, domain, dtype):
    lb_ub, definiteRange = inp._interval(domain, dtype, allowBoundSurf=True)
    isBoundSurf = type(lb_ub) == boundsurf
    lb, ub = lb_ub.resolve()[0] if isBoundSurf else lb_ub
    if isBoundSurf:
        if np.all(lb >= 0):
            return defaultIntervalEngine(lb_ub, np.arctan, r.d, monotonity=1, convexity=-1)
        if np.all(ub <= 0):
            return defaultIntervalEngine(lb_ub, np.arctan, r.d, monotonity=1, convexity=1)
    return oofun._interval_(r, domain, dtype)


def arctan(inp):
    if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
        return ooarray([ arctan(elem) for elem in inp ])
    if hasStochastic and isinstance(inp, distribution.stochasticDistribution):
        return distribution.stochasticDistribution(arctan(inp.values), inp.probabilities.copy())._update(inp)
    if not isinstance(inp, oofun):
        return np.arctan(inp)
    r = oofun(st_arctan, inp, d=(lambda x: Diag(1.0 / (1.0 + x ** 2))), vectorized=True, criticalPoints=False, engine_monotonity=1)
    r._interval_ = lambda domain, dtype: arctan_interval(inp, r, domain, dtype)
    return r


__all__ += ['arcsin', 'arccos', 'arctan']
st_sinh = (--- This code section failed: ---

 L. 235         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             0  'x'
                6  LOAD_GLOBAL           1  'distribution'
                9  LOAD_ATTR             2  'stochasticDistribution'
               12  CALL_FUNCTION_2       2  None
               15  POP_JUMP_IF_FALSE    61  'to 61'
               18  LOAD_GLOBAL           1  'distribution'
               21  LOAD_ATTR             2  'stochasticDistribution'
               24  LOAD_GLOBAL           3  'sinh'
               27  LOAD_FAST             0  'x'
               30  LOAD_ATTR             4  'values'
               33  CALL_FUNCTION_1       1  None
               36  LOAD_FAST             0  'x'
               39  LOAD_ATTR             5  'probabilities'
               42  LOAD_ATTR             6  'copy'
               45  CALL_FUNCTION_0       0  None
               48  CALL_FUNCTION_2       2  None
               51  LOAD_ATTR             7  '_update'
               54  LOAD_FAST             0  'x'
               57  CALL_FUNCTION_1       1  None
               60  RETURN_END_IF_LAMBDA
             61_0  COME_FROM            15  '15'

 L. 236        61  LOAD_GLOBAL           0  'isinstance'
               64  LOAD_FAST             0  'x'
               67  LOAD_GLOBAL           8  'multiarray'
               70  CALL_FUNCTION_2       2  None
               73  POP_JUMP_IF_FALSE   151  'to 151'
               76  LOAD_GLOBAL           0  'isinstance'
               79  LOAD_FAST             0  'x'
               82  LOAD_ATTR             9  'flat'
               85  LOAD_CONST               0
               88  BINARY_SUBSCR    
               89  LOAD_GLOBAL           1  'distribution'
               92  LOAD_ATTR             2  'stochasticDistribution'
               95  CALL_FUNCTION_2       2  None
             98_0  COME_FROM            73  '73'
               98  POP_JUMP_IF_FALSE   151  'to 151'
              101  LOAD_GLOBAL          10  'np'
              104  LOAD_ATTR            11  'array'
              107  BUILD_LIST_0          0 
              110  LOAD_FAST             0  'x'
              113  LOAD_ATTR             9  'flat'
              116  GET_ITER         
              117  FOR_ITER             18  'to 138'
              120  STORE_FAST            1  'elem'
              123  LOAD_GLOBAL           3  'sinh'
              126  LOAD_FAST             1  'elem'
              129  CALL_FUNCTION_1       1  None
              132  LIST_APPEND           2  None
              135  JUMP_BACK           117  'to 117'
              138  CALL_FUNCTION_1       1  None
              141  LOAD_ATTR            12  'view'
              144  LOAD_GLOBAL           8  'multiarray'
              147  CALL_FUNCTION_1       1  None
              150  RETURN_END_IF_LAMBDA
            151_0  COME_FROM            98  '98'

 L. 237       151  LOAD_GLOBAL          10  'np'
              154  LOAD_ATTR             3  'sinh'
              157  LOAD_FAST             0  'x'
              160  CALL_FUNCTION_1       1  None
              163  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 150
) if hasStochastic else np.sinh

def sinh_interval(inp, r, domain, dtype):
    lb_ub, definiteRange = inp._interval(domain, dtype, allowBoundSurf=True)
    isBoundSurf = type(lb_ub) == boundsurf
    lb, ub = lb_ub.resolve()[0] if isBoundSurf else lb_ub
    if isBoundSurf:
        if np.all(lb >= 0):
            return defaultIntervalEngine(lb_ub, np.sinh, r.d, monotonity=1, convexity=1)
        if np.all(ub <= 0):
            return defaultIntervalEngine(lb_ub, np.sinh, r.d, monotonity=1, convexity=-1)
    return oofun._interval_(r, domain, dtype)


def sinh(inp):
    if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
        return ooarray([ sinh(elem) for elem in inp ])
    if hasStochastic and isinstance(inp, distribution.stochasticDistribution):
        return distribution.stochasticDistribution(sinh(inp.values), inp.probabilities.copy())._update(inp)
    if not isinstance(inp, oofun):
        return np.sinh(inp)
    r = oofun(st_sinh, inp, d=(lambda x: Diag(np.cosh(x))), vectorized=True, criticalPoints=False, engine_monotonity=1)
    r._interval_ = lambda domain, dtype: sinh_interval(inp, r, domain, dtype)
    return r


st_cosh = (--- This code section failed: ---

 L. 289         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             0  'x'
                6  LOAD_GLOBAL           1  'distribution'
                9  LOAD_ATTR             2  'stochasticDistribution'
               12  CALL_FUNCTION_2       2  None
               15  POP_JUMP_IF_FALSE    61  'to 61'
               18  LOAD_GLOBAL           1  'distribution'
               21  LOAD_ATTR             2  'stochasticDistribution'
               24  LOAD_GLOBAL           3  'cosh'
               27  LOAD_FAST             0  'x'
               30  LOAD_ATTR             4  'values'
               33  CALL_FUNCTION_1       1  None
               36  LOAD_FAST             0  'x'
               39  LOAD_ATTR             5  'probabilities'
               42  LOAD_ATTR             6  'copy'
               45  CALL_FUNCTION_0       0  None
               48  CALL_FUNCTION_2       2  None
               51  LOAD_ATTR             7  '_update'
               54  LOAD_FAST             0  'x'
               57  CALL_FUNCTION_1       1  None
               60  RETURN_END_IF_LAMBDA
             61_0  COME_FROM            15  '15'

 L. 290        61  LOAD_GLOBAL           0  'isinstance'
               64  LOAD_FAST             0  'x'
               67  LOAD_GLOBAL           8  'multiarray'
               70  CALL_FUNCTION_2       2  None
               73  POP_JUMP_IF_FALSE   151  'to 151'
               76  LOAD_GLOBAL           0  'isinstance'
               79  LOAD_FAST             0  'x'
               82  LOAD_ATTR             9  'flat'
               85  LOAD_CONST               0
               88  BINARY_SUBSCR    
               89  LOAD_GLOBAL           1  'distribution'
               92  LOAD_ATTR             2  'stochasticDistribution'
               95  CALL_FUNCTION_2       2  None
             98_0  COME_FROM            73  '73'
               98  POP_JUMP_IF_FALSE   151  'to 151'
              101  LOAD_GLOBAL          10  'np'
              104  LOAD_ATTR            11  'array'
              107  BUILD_LIST_0          0 
              110  LOAD_FAST             0  'x'
              113  LOAD_ATTR             9  'flat'
              116  GET_ITER         
              117  FOR_ITER             18  'to 138'
              120  STORE_FAST            1  'elem'
              123  LOAD_GLOBAL           3  'cosh'
              126  LOAD_FAST             1  'elem'
              129  CALL_FUNCTION_1       1  None
              132  LIST_APPEND           2  None
              135  JUMP_BACK           117  'to 117'
              138  CALL_FUNCTION_1       1  None
              141  LOAD_ATTR            12  'view'
              144  LOAD_GLOBAL           8  'multiarray'
              147  CALL_FUNCTION_1       1  None
              150  RETURN_END_IF_LAMBDA
            151_0  COME_FROM            98  '98'

 L. 291       151  LOAD_GLOBAL          10  'np'
              154  LOAD_ATTR             3  'cosh'
              157  LOAD_FAST             0  'x'
              160  CALL_FUNCTION_1       1  None
              163  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 150
) if hasStochastic else np.cosh

def cosh(inp):
    if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
        return ooarray([ cosh(elem) for elem in inp ])
    if hasStochastic and isinstance(inp, distribution.stochasticDistribution):
        return distribution.stochasticDistribution(cosh(inp.values), inp.probabilities.copy())._update(inp)
    if not isinstance(inp, oofun):
        return np.cosh(inp)
    return oofun(st_cosh, inp, d=(lambda x: Diag(np.sinh(x))), engine_convexity=1, vectorized=True, _interval_=ZeroCriticalPointsInterval(inp, np.cosh))


__all__ += ['sinh', 'cosh']
st_tanh = (--- This code section failed: ---

 L. 309         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             0  'x'
                6  LOAD_GLOBAL           1  'distribution'
                9  LOAD_ATTR             2  'stochasticDistribution'
               12  CALL_FUNCTION_2       2  None
               15  POP_JUMP_IF_FALSE    61  'to 61'
               18  LOAD_GLOBAL           1  'distribution'
               21  LOAD_ATTR             2  'stochasticDistribution'
               24  LOAD_GLOBAL           3  'tanh'
               27  LOAD_FAST             0  'x'
               30  LOAD_ATTR             4  'values'
               33  CALL_FUNCTION_1       1  None
               36  LOAD_FAST             0  'x'
               39  LOAD_ATTR             5  'probabilities'
               42  LOAD_ATTR             6  'copy'
               45  CALL_FUNCTION_0       0  None
               48  CALL_FUNCTION_2       2  None
               51  LOAD_ATTR             7  '_update'
               54  LOAD_FAST             0  'x'
               57  CALL_FUNCTION_1       1  None
               60  RETURN_END_IF_LAMBDA
             61_0  COME_FROM            15  '15'

 L. 310        61  LOAD_GLOBAL           0  'isinstance'
               64  LOAD_FAST             0  'x'
               67  LOAD_GLOBAL           8  'multiarray'
               70  CALL_FUNCTION_2       2  None
               73  POP_JUMP_IF_FALSE   151  'to 151'
               76  LOAD_GLOBAL           0  'isinstance'
               79  LOAD_FAST             0  'x'
               82  LOAD_ATTR             9  'flat'
               85  LOAD_CONST               0
               88  BINARY_SUBSCR    
               89  LOAD_GLOBAL           1  'distribution'
               92  LOAD_ATTR             2  'stochasticDistribution'
               95  CALL_FUNCTION_2       2  None
             98_0  COME_FROM            73  '73'
               98  POP_JUMP_IF_FALSE   151  'to 151'
              101  LOAD_GLOBAL          10  'np'
              104  LOAD_ATTR            11  'array'
              107  BUILD_LIST_0          0 
              110  LOAD_FAST             0  'x'
              113  LOAD_ATTR             9  'flat'
              116  GET_ITER         
              117  FOR_ITER             18  'to 138'
              120  STORE_FAST            1  'elem'
              123  LOAD_GLOBAL           3  'tanh'
              126  LOAD_FAST             1  'elem'
              129  CALL_FUNCTION_1       1  None
              132  LIST_APPEND           2  None
              135  JUMP_BACK           117  'to 117'
              138  CALL_FUNCTION_1       1  None
              141  LOAD_ATTR            12  'view'
              144  LOAD_GLOBAL           8  'multiarray'
              147  CALL_FUNCTION_1       1  None
              150  RETURN_END_IF_LAMBDA
            151_0  COME_FROM            98  '98'

 L. 311       151  LOAD_GLOBAL          10  'np'
              154  LOAD_ATTR             3  'tanh'
              157  LOAD_FAST             0  'x'
              160  CALL_FUNCTION_1       1  None
              163  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 150
) if hasStochastic else np.tanh

def tanh_interval(inp, r, domain, dtype):
    lb_ub, definiteRange = inp._interval(domain, dtype, allowBoundSurf=True)
    isBoundSurf = type(lb_ub) == boundsurf
    lb, ub = lb_ub.resolve()[0] if isBoundSurf else lb_ub
    if isBoundSurf:
        if np.all(lb >= 0):
            return defaultIntervalEngine(lb_ub, np.tanh, r.d, monotonity=1, convexity=-1)
        if np.all(ub <= 0):
            return defaultIntervalEngine(lb_ub, np.tanh, r.d, monotonity=1, convexity=1)
    return oofun._interval_(r, domain, dtype)


def tanh(inp):
    if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
        return ooarray([ tanh(elem) for elem in inp ])
    if hasStochastic and isinstance(inp, distribution.stochasticDistribution):
        return distribution.stochasticDistribution(tanh(inp.values), inp.probabilities.copy())._update(inp)
    if not isinstance(inp, oofun):
        return np.tanh(inp)
    r = oofun(st_tanh, inp, d=(lambda x: Diag(1.0 / np.cosh(x) ** 2)), vectorized=True, criticalPoints=False, engine_monotonity=1)
    r._interval_ = lambda domain, dtype: tanh_interval(inp, r, domain, dtype)
    return r


st_arctanh = (--- This code section failed: ---

 L. 339         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             0  'x'
                6  LOAD_GLOBAL           1  'distribution'
                9  LOAD_ATTR             2  'stochasticDistribution'
               12  CALL_FUNCTION_2       2  None
               15  POP_JUMP_IF_FALSE    61  'to 61'
               18  LOAD_GLOBAL           1  'distribution'
               21  LOAD_ATTR             2  'stochasticDistribution'
               24  LOAD_GLOBAL           3  'arctanh'
               27  LOAD_FAST             0  'x'
               30  LOAD_ATTR             4  'values'
               33  CALL_FUNCTION_1       1  None
               36  LOAD_FAST             0  'x'
               39  LOAD_ATTR             5  'probabilities'
               42  LOAD_ATTR             6  'copy'
               45  CALL_FUNCTION_0       0  None
               48  CALL_FUNCTION_2       2  None
               51  LOAD_ATTR             7  '_update'
               54  LOAD_FAST             0  'x'
               57  CALL_FUNCTION_1       1  None
               60  RETURN_END_IF_LAMBDA
             61_0  COME_FROM            15  '15'

 L. 340        61  LOAD_GLOBAL           0  'isinstance'
               64  LOAD_FAST             0  'x'
               67  LOAD_GLOBAL           8  'multiarray'
               70  CALL_FUNCTION_2       2  None
               73  POP_JUMP_IF_FALSE   151  'to 151'
               76  LOAD_GLOBAL           0  'isinstance'
               79  LOAD_FAST             0  'x'
               82  LOAD_ATTR             9  'flat'
               85  LOAD_CONST               0
               88  BINARY_SUBSCR    
               89  LOAD_GLOBAL           1  'distribution'
               92  LOAD_ATTR             2  'stochasticDistribution'
               95  CALL_FUNCTION_2       2  None
             98_0  COME_FROM            73  '73'
               98  POP_JUMP_IF_FALSE   151  'to 151'
              101  LOAD_GLOBAL          10  'np'
              104  LOAD_ATTR            11  'array'
              107  BUILD_LIST_0          0 
              110  LOAD_FAST             0  'x'
              113  LOAD_ATTR             9  'flat'
              116  GET_ITER         
              117  FOR_ITER             18  'to 138'
              120  STORE_FAST            1  'elem'
              123  LOAD_GLOBAL           3  'arctanh'
              126  LOAD_FAST             1  'elem'
              129  CALL_FUNCTION_1       1  None
              132  LIST_APPEND           2  None
              135  JUMP_BACK           117  'to 117'
              138  CALL_FUNCTION_1       1  None
              141  LOAD_ATTR            12  'view'
              144  LOAD_GLOBAL           8  'multiarray'
              147  CALL_FUNCTION_1       1  None
              150  RETURN_END_IF_LAMBDA
            151_0  COME_FROM            98  '98'

 L. 341       151  LOAD_GLOBAL          10  'np'
              154  LOAD_ATTR             3  'arctanh'
              157  LOAD_FAST             0  'x'
              160  CALL_FUNCTION_1       1  None
              163  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 150
) if hasStochastic else np.arctanh

def arctanh(inp):
    if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
        return ooarray([ arctanh(elem) for elem in inp ])
    if hasStochastic and isinstance(inp, distribution.stochasticDistribution):
        return distribution.stochasticDistribution(arctanh(inp.values), inp.probabilities.copy())._update(inp)
    if not isinstance(inp, oofun):
        return np.arctanh(inp)
    r = oofun(st_arctanh, inp, d=(lambda x: Diag(1.0 / (1.0 - x ** 2))), vectorized=True, criticalPoints=False)
    r._interval_ = lambda domain, dtype: box_1_interval(inp, np.arctanh, r.d, domain, dtype)
    return r


__all__ += ['tanh', 'arctanh']
st_arcsinh = (--- This code section failed: ---

 L. 360         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             0  'x'
                6  LOAD_GLOBAL           1  'distribution'
                9  LOAD_ATTR             2  'stochasticDistribution'
               12  CALL_FUNCTION_2       2  None
               15  POP_JUMP_IF_FALSE    61  'to 61'
               18  LOAD_GLOBAL           1  'distribution'
               21  LOAD_ATTR             2  'stochasticDistribution'
               24  LOAD_GLOBAL           3  'arcsinh'
               27  LOAD_FAST             0  'x'
               30  LOAD_ATTR             4  'values'
               33  CALL_FUNCTION_1       1  None
               36  LOAD_FAST             0  'x'
               39  LOAD_ATTR             5  'probabilities'
               42  LOAD_ATTR             6  'copy'
               45  CALL_FUNCTION_0       0  None
               48  CALL_FUNCTION_2       2  None
               51  LOAD_ATTR             7  '_update'
               54  LOAD_FAST             0  'x'
               57  CALL_FUNCTION_1       1  None
               60  RETURN_END_IF_LAMBDA
             61_0  COME_FROM            15  '15'

 L. 361        61  LOAD_GLOBAL           0  'isinstance'
               64  LOAD_FAST             0  'x'
               67  LOAD_GLOBAL           8  'multiarray'
               70  CALL_FUNCTION_2       2  None
               73  POP_JUMP_IF_FALSE   151  'to 151'
               76  LOAD_GLOBAL           0  'isinstance'
               79  LOAD_FAST             0  'x'
               82  LOAD_ATTR             9  'flat'
               85  LOAD_CONST               0
               88  BINARY_SUBSCR    
               89  LOAD_GLOBAL           1  'distribution'
               92  LOAD_ATTR             2  'stochasticDistribution'
               95  CALL_FUNCTION_2       2  None
             98_0  COME_FROM            73  '73'
               98  POP_JUMP_IF_FALSE   151  'to 151'
              101  LOAD_GLOBAL          10  'np'
              104  LOAD_ATTR            11  'array'
              107  BUILD_LIST_0          0 
              110  LOAD_FAST             0  'x'
              113  LOAD_ATTR             9  'flat'
              116  GET_ITER         
              117  FOR_ITER             18  'to 138'
              120  STORE_FAST            1  'elem'
              123  LOAD_GLOBAL           3  'arcsinh'
              126  LOAD_FAST             1  'elem'
              129  CALL_FUNCTION_1       1  None
              132  LIST_APPEND           2  None
              135  JUMP_BACK           117  'to 117'
              138  CALL_FUNCTION_1       1  None
              141  LOAD_ATTR            12  'view'
              144  LOAD_GLOBAL           8  'multiarray'
              147  CALL_FUNCTION_1       1  None
              150  RETURN_END_IF_LAMBDA
            151_0  COME_FROM            98  '98'

 L. 362       151  LOAD_GLOBAL          10  'np'
              154  LOAD_ATTR             3  'arcsinh'
              157  LOAD_FAST             0  'x'
              160  CALL_FUNCTION_1       1  None
              163  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 150
) if hasStochastic else np.arcsinh

def arcsinh_interval(inp, r, domain, dtype):
    lb_ub, definiteRange = inp._interval(domain, dtype, allowBoundSurf=True)
    isBoundSurf = type(lb_ub) == boundsurf
    lb, ub = lb_ub.resolve()[0] if isBoundSurf else lb_ub
    if isBoundSurf:
        if np.all(lb >= 0):
            return defaultIntervalEngine(lb_ub, np.arcsinh, r.d, monotonity=1, convexity=-1)
        if np.all(ub <= 0):
            return defaultIntervalEngine(lb_ub, np.arcsinh, r.d, monotonity=1, convexity=1)
    return oofun._interval_(r, domain, dtype)


def arcsinh(inp):
    if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
        return ooarray([ arcsinh(elem) for elem in inp ])
    if hasStochastic and isinstance(inp, distribution.stochasticDistribution):
        return distribution.stochasticDistribution(arcsinh(inp.values), inp.probabilities.copy())._update(inp)
    if not isinstance(inp, oofun):
        return np.arcsinh(inp)
    r = oofun(st_arcsinh, inp, d=(lambda x: Diag(1.0 / np.sqrt(1 + x ** 2))), vectorized=True, criticalPoints=False, engine_monotonity=1)
    r._interval_ = lambda domain, dtype: arcsinh_interval(inp, r, domain, dtype)
    return r


st_arccosh = (--- This code section failed: ---

 L. 398         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             0  'x'
                6  LOAD_GLOBAL           1  'distribution'
                9  LOAD_ATTR             2  'stochasticDistribution'
               12  CALL_FUNCTION_2       2  None
               15  POP_JUMP_IF_FALSE    61  'to 61'
               18  LOAD_GLOBAL           1  'distribution'
               21  LOAD_ATTR             2  'stochasticDistribution'
               24  LOAD_GLOBAL           3  'arccosh'
               27  LOAD_FAST             0  'x'
               30  LOAD_ATTR             4  'values'
               33  CALL_FUNCTION_1       1  None
               36  LOAD_FAST             0  'x'
               39  LOAD_ATTR             5  'probabilities'
               42  LOAD_ATTR             6  'copy'
               45  CALL_FUNCTION_0       0  None
               48  CALL_FUNCTION_2       2  None
               51  LOAD_ATTR             7  '_update'
               54  LOAD_FAST             0  'x'
               57  CALL_FUNCTION_1       1  None
               60  RETURN_END_IF_LAMBDA
             61_0  COME_FROM            15  '15'

 L. 399        61  LOAD_GLOBAL           0  'isinstance'
               64  LOAD_FAST             0  'x'
               67  LOAD_GLOBAL           8  'multiarray'
               70  CALL_FUNCTION_2       2  None
               73  POP_JUMP_IF_FALSE   151  'to 151'
               76  LOAD_GLOBAL           0  'isinstance'
               79  LOAD_FAST             0  'x'
               82  LOAD_ATTR             9  'flat'
               85  LOAD_CONST               0
               88  BINARY_SUBSCR    
               89  LOAD_GLOBAL           1  'distribution'
               92  LOAD_ATTR             2  'stochasticDistribution'
               95  CALL_FUNCTION_2       2  None
             98_0  COME_FROM            73  '73'
               98  POP_JUMP_IF_FALSE   151  'to 151'
              101  LOAD_GLOBAL          10  'np'
              104  LOAD_ATTR            11  'array'
              107  BUILD_LIST_0          0 
              110  LOAD_FAST             0  'x'
              113  LOAD_ATTR             9  'flat'
              116  GET_ITER         
              117  FOR_ITER             18  'to 138'
              120  STORE_FAST            1  'elem'
              123  LOAD_GLOBAL           3  'arccosh'
              126  LOAD_FAST             1  'elem'
              129  CALL_FUNCTION_1       1  None
              132  LIST_APPEND           2  None
              135  JUMP_BACK           117  'to 117'
              138  CALL_FUNCTION_1       1  None
              141  LOAD_ATTR            12  'view'
              144  LOAD_GLOBAL           8  'multiarray'
              147  CALL_FUNCTION_1       1  None
              150  RETURN_END_IF_LAMBDA
            151_0  COME_FROM            98  '98'

 L. 400       151  LOAD_GLOBAL          10  'np'
              154  LOAD_ATTR             3  'arccosh'
              157  LOAD_FAST             0  'x'
              160  CALL_FUNCTION_1       1  None
              163  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 150
) if hasStochastic else np.arccosh

def arccosh(inp):
    if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
        return ooarray([ arccosh(elem) for elem in inp ])
    if hasStochastic and isinstance(inp, distribution.stochasticDistribution):
        return distribution.stochasticDistribution(arccosh(inp.values), inp.probabilities.copy())._update(inp)
    if not isinstance(inp, oofun):
        return np.arccosh(inp)
    r = oofun(st_arccosh, inp, d=(lambda x: Diag(1.0 / np.sqrt(x ** 2 - 1.0))), vectorized=True, engine_monotonity=1, engine_convexity=-1)
    F0, shift = (0.0, 1.0)
    r._interval_ = lambda domain, dtype: nonnegative_interval(inp, np.arccosh, r.d, domain, dtype, F0, shift)
    return r


__all__ += ['arcsinh', 'arccosh']

def angle(inp1, inp2):
    return arccos(sum(inp1 * inp2) / sqrt(sum(inp1 ** 2) * sum(inp2 ** 2)))


st_exp = (--- This code section failed: ---

 L. 428         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             0  'x'
                6  LOAD_GLOBAL           1  'distribution'
                9  LOAD_ATTR             2  'stochasticDistribution'
               12  CALL_FUNCTION_2       2  None
               15  POP_JUMP_IF_FALSE    61  'to 61'
               18  LOAD_GLOBAL           1  'distribution'
               21  LOAD_ATTR             2  'stochasticDistribution'
               24  LOAD_GLOBAL           3  'exp'
               27  LOAD_FAST             0  'x'
               30  LOAD_ATTR             4  'values'
               33  CALL_FUNCTION_1       1  None
               36  LOAD_FAST             0  'x'
               39  LOAD_ATTR             5  'probabilities'
               42  LOAD_ATTR             6  'copy'
               45  CALL_FUNCTION_0       0  None
               48  CALL_FUNCTION_2       2  None
               51  LOAD_ATTR             7  '_update'
               54  LOAD_FAST             0  'x'
               57  CALL_FUNCTION_1       1  None
               60  RETURN_END_IF_LAMBDA
             61_0  COME_FROM            15  '15'

 L. 429        61  LOAD_GLOBAL           0  'isinstance'
               64  LOAD_FAST             0  'x'
               67  LOAD_GLOBAL           8  'multiarray'
               70  CALL_FUNCTION_2       2  None
               73  POP_JUMP_IF_FALSE   151  'to 151'
               76  LOAD_GLOBAL           0  'isinstance'
               79  LOAD_FAST             0  'x'
               82  LOAD_ATTR             9  'flat'
               85  LOAD_CONST               0
               88  BINARY_SUBSCR    
               89  LOAD_GLOBAL           1  'distribution'
               92  LOAD_ATTR             2  'stochasticDistribution'
               95  CALL_FUNCTION_2       2  None
             98_0  COME_FROM            73  '73'
               98  POP_JUMP_IF_FALSE   151  'to 151'
              101  LOAD_GLOBAL          10  'np'
              104  LOAD_ATTR            11  'array'
              107  BUILD_LIST_0          0 
              110  LOAD_FAST             0  'x'
              113  LOAD_ATTR             9  'flat'
              116  GET_ITER         
              117  FOR_ITER             18  'to 138'
              120  STORE_FAST            1  'elem'
              123  LOAD_GLOBAL           3  'exp'
              126  LOAD_FAST             1  'elem'
              129  CALL_FUNCTION_1       1  None
              132  LIST_APPEND           2  None
              135  JUMP_BACK           117  'to 117'
              138  CALL_FUNCTION_1       1  None
              141  LOAD_ATTR            12  'view'
              144  LOAD_GLOBAL           8  'multiarray'
              147  CALL_FUNCTION_1       1  None
              150  RETURN_END_IF_LAMBDA
            151_0  COME_FROM            98  '98'

 L. 430       151  LOAD_GLOBAL          10  'np'
              154  LOAD_ATTR             3  'exp'
              157  LOAD_FAST             0  'x'
              160  CALL_FUNCTION_1       1  None
              163  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 150
) if hasStochastic else np.exp

def exp(inp):
    if isinstance(inp, ooarray):
        return ooarray([ exp(elem) for elem in inp ])
    if hasStochastic and isinstance(inp, distribution.stochasticDistribution):
        return distribution.stochasticDistribution(exp(inp.values), inp.probabilities.copy())._update(inp)
    if not isinstance(inp, oofun):
        return np.exp(inp)
    return oofun(st_exp, inp, d=(lambda x: Diag(np.exp(x))), vectorized=True, criticalPoints=False, engine_convexity=1, engine_monotonity=1)


st_sqrt = (--- This code section failed: ---

 L. 445         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             0  'x'
                6  LOAD_GLOBAL           1  'distribution'
                9  LOAD_ATTR             2  'stochasticDistribution'
               12  CALL_FUNCTION_2       2  None
               15  POP_JUMP_IF_FALSE    61  'to 61'
               18  LOAD_GLOBAL           1  'distribution'
               21  LOAD_ATTR             2  'stochasticDistribution'
               24  LOAD_GLOBAL           3  'sqrt'
               27  LOAD_FAST             0  'x'
               30  LOAD_ATTR             4  'values'
               33  CALL_FUNCTION_1       1  None
               36  LOAD_FAST             0  'x'
               39  LOAD_ATTR             5  'probabilities'
               42  LOAD_ATTR             6  'copy'
               45  CALL_FUNCTION_0       0  None
               48  CALL_FUNCTION_2       2  None
               51  LOAD_ATTR             7  '_update'
               54  LOAD_FAST             0  'x'
               57  CALL_FUNCTION_1       1  None
               60  RETURN_END_IF_LAMBDA
             61_0  COME_FROM            15  '15'

 L. 446        61  LOAD_GLOBAL           0  'isinstance'
               64  LOAD_FAST             0  'x'
               67  LOAD_GLOBAL           8  'multiarray'
               70  CALL_FUNCTION_2       2  None
               73  POP_JUMP_IF_FALSE   151  'to 151'
               76  LOAD_GLOBAL           0  'isinstance'
               79  LOAD_FAST             0  'x'
               82  LOAD_ATTR             9  'flat'
               85  LOAD_CONST               0
               88  BINARY_SUBSCR    
               89  LOAD_GLOBAL           1  'distribution'
               92  LOAD_ATTR             2  'stochasticDistribution'
               95  CALL_FUNCTION_2       2  None
             98_0  COME_FROM            73  '73'
               98  POP_JUMP_IF_FALSE   151  'to 151'
              101  LOAD_GLOBAL          10  'np'
              104  LOAD_ATTR            11  'array'
              107  BUILD_LIST_0          0 
              110  LOAD_FAST             0  'x'
              113  LOAD_ATTR             9  'flat'
              116  GET_ITER         
              117  FOR_ITER             18  'to 138'
              120  STORE_FAST            1  'elem'
              123  LOAD_GLOBAL           3  'sqrt'
              126  LOAD_FAST             1  'elem'
              129  CALL_FUNCTION_1       1  None
              132  LIST_APPEND           2  None
              135  JUMP_BACK           117  'to 117'
              138  CALL_FUNCTION_1       1  None
              141  LOAD_ATTR            12  'view'
              144  LOAD_GLOBAL           8  'multiarray'
              147  CALL_FUNCTION_1       1  None
              150  RETURN_END_IF_LAMBDA
            151_0  COME_FROM            98  '98'

 L. 447       151  LOAD_GLOBAL          10  'np'
              154  LOAD_ATTR             3  'sqrt'
              157  LOAD_FAST             0  'x'
              160  CALL_FUNCTION_1       1  None
              163  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 150
) if hasStochastic else np.sqrt

def sqrt(inp, attachConstraints=True):
    if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
        return ooarray([ sqrt(elem) for elem in inp ])
    if hasStochastic and isinstance(inp, distribution.stochasticDistribution):
        return distribution.stochasticDistribution(sqrt(inp.values), inp.probabilities.copy())._update(inp)
    if not isinstance(inp, oofun):
        return np.sqrt(inp)
    r = oofun(st_sqrt, inp, d=(lambda x: Diag(0.5 / np.sqrt(x))), vectorized=True, engine_monotonity=1, engine_convexity=-1)
    r._interval_ = lambda domain, dtype: nonnegative_interval(inp, np.sqrt, r.d, domain, dtype, 0.0)
    if attachConstraints:
        r.attach((inp > 0)('sqrt_domain_zero_bound_%d' % r._id, tol=-1e-07))
    return r


__all__ += ['angle', 'exp', 'sqrt']
st_abs = (--- This code section failed: ---

 L. 468         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             0  'x'
                6  LOAD_GLOBAL           1  'distribution'
                9  LOAD_ATTR             2  'stochasticDistribution'
               12  CALL_FUNCTION_2       2  None
               15  POP_JUMP_IF_FALSE    61  'to 61'
               18  LOAD_GLOBAL           1  'distribution'
               21  LOAD_ATTR             2  'stochasticDistribution'
               24  LOAD_GLOBAL           3  'abs'
               27  LOAD_FAST             0  'x'
               30  LOAD_ATTR             4  'values'
               33  CALL_FUNCTION_1       1  None
               36  LOAD_FAST             0  'x'
               39  LOAD_ATTR             5  'probabilities'
               42  LOAD_ATTR             6  'copy'
               45  CALL_FUNCTION_0       0  None
               48  CALL_FUNCTION_2       2  None
               51  LOAD_ATTR             7  '_update'
               54  LOAD_FAST             0  'x'
               57  CALL_FUNCTION_1       1  None
               60  RETURN_END_IF_LAMBDA
             61_0  COME_FROM            15  '15'

 L. 469        61  LOAD_GLOBAL           0  'isinstance'
               64  LOAD_FAST             0  'x'
               67  LOAD_GLOBAL           8  'multiarray'
               70  CALL_FUNCTION_2       2  None
               73  POP_JUMP_IF_FALSE   151  'to 151'
               76  LOAD_GLOBAL           0  'isinstance'
               79  LOAD_FAST             0  'x'
               82  LOAD_ATTR             9  'flat'
               85  LOAD_CONST               0
               88  BINARY_SUBSCR    
               89  LOAD_GLOBAL           1  'distribution'
               92  LOAD_ATTR             2  'stochasticDistribution'
               95  CALL_FUNCTION_2       2  None
             98_0  COME_FROM            73  '73'
               98  POP_JUMP_IF_FALSE   151  'to 151'
              101  LOAD_GLOBAL          10  'np'
              104  LOAD_ATTR            11  'array'
              107  BUILD_LIST_0          0 
              110  LOAD_FAST             0  'x'
              113  LOAD_ATTR             9  'flat'
              116  GET_ITER         
              117  FOR_ITER             18  'to 138'
              120  STORE_FAST            1  'elem'
              123  LOAD_GLOBAL           3  'abs'
              126  LOAD_FAST             1  'elem'
              129  CALL_FUNCTION_1       1  None
              132  LIST_APPEND           2  None
              135  JUMP_BACK           117  'to 117'
              138  CALL_FUNCTION_1       1  None
              141  LOAD_ATTR            12  'view'
              144  LOAD_GLOBAL           8  'multiarray'
              147  CALL_FUNCTION_1       1  None
              150  RETURN_END_IF_LAMBDA
            151_0  COME_FROM            98  '98'

 L. 470       151  LOAD_GLOBAL          10  'np'
              154  LOAD_ATTR             3  'abs'
              157  LOAD_FAST             0  'x'
              160  CALL_FUNCTION_1       1  None
              163  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 150
) if hasStochastic else np.abs

def abs(inp):
    if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
        return ooarray([ abs(elem) for elem in inp ])
    if hasStochastic and isinstance(inp, distribution.stochasticDistribution):
        return distribution.stochasticDistribution(abs(inp.values), inp.probabilities.copy())._update(inp)
    if not isinstance(inp, oofun):
        return np.abs(inp)
    return oofun(st_abs, inp, d=(lambda x: Diag(np.sign(x))), vectorized=True, _interval_=ZeroCriticalPointsInterval(inp, np.abs))


__all__ += ['abs']
st_log = (--- This code section failed: ---

 L. 487         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             0  'x'
                6  LOAD_GLOBAL           1  'distribution'
                9  LOAD_ATTR             2  'stochasticDistribution'
               12  CALL_FUNCTION_2       2  None
               15  POP_JUMP_IF_FALSE    61  'to 61'
               18  LOAD_GLOBAL           1  'distribution'
               21  LOAD_ATTR             2  'stochasticDistribution'
               24  LOAD_GLOBAL           3  'log'
               27  LOAD_FAST             0  'x'
               30  LOAD_ATTR             4  'values'
               33  CALL_FUNCTION_1       1  None
               36  LOAD_FAST             0  'x'
               39  LOAD_ATTR             5  'probabilities'
               42  LOAD_ATTR             6  'copy'
               45  CALL_FUNCTION_0       0  None
               48  CALL_FUNCTION_2       2  None
               51  LOAD_ATTR             7  '_update'
               54  LOAD_FAST             0  'x'
               57  CALL_FUNCTION_1       1  None
               60  RETURN_END_IF_LAMBDA
             61_0  COME_FROM            15  '15'

 L. 488        61  LOAD_GLOBAL           0  'isinstance'
               64  LOAD_FAST             0  'x'
               67  LOAD_GLOBAL           8  'multiarray'
               70  CALL_FUNCTION_2       2  None
               73  POP_JUMP_IF_FALSE   151  'to 151'
               76  LOAD_GLOBAL           0  'isinstance'
               79  LOAD_FAST             0  'x'
               82  LOAD_ATTR             9  'flat'
               85  LOAD_CONST               0
               88  BINARY_SUBSCR    
               89  LOAD_GLOBAL           1  'distribution'
               92  LOAD_ATTR             2  'stochasticDistribution'
               95  CALL_FUNCTION_2       2  None
             98_0  COME_FROM            73  '73'
               98  POP_JUMP_IF_FALSE   151  'to 151'
              101  LOAD_GLOBAL          10  'np'
              104  LOAD_ATTR            11  'array'
              107  BUILD_LIST_0          0 
              110  LOAD_FAST             0  'x'
              113  LOAD_ATTR             9  'flat'
              116  GET_ITER         
              117  FOR_ITER             18  'to 138'
              120  STORE_FAST            1  'elem'
              123  LOAD_GLOBAL           3  'log'
              126  LOAD_FAST             1  'elem'
              129  CALL_FUNCTION_1       1  None
              132  LIST_APPEND           2  None
              135  JUMP_BACK           117  'to 117'
              138  CALL_FUNCTION_1       1  None
              141  LOAD_ATTR            12  'view'
              144  LOAD_GLOBAL           8  'multiarray'
              147  CALL_FUNCTION_1       1  None
              150  RETURN_END_IF_LAMBDA
            151_0  COME_FROM            98  '98'

 L. 489       151  LOAD_GLOBAL          10  'np'
              154  LOAD_ATTR             3  'log'
              157  LOAD_FAST             0  'x'
              160  CALL_FUNCTION_1       1  None
              163  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 150
) if hasStochastic else np.log

def log(inp):
    if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
        return ooarray([ log(elem) for elem in inp ])
    if hasStochastic and isinstance(inp, distribution.stochasticDistribution):
        return distribution.stochasticDistribution(log(inp.values), inp.probabilities.copy())._update(inp)
    if not isinstance(inp, oofun):
        return np.log(inp)
    d = lambda x: Diag(1.0 / x)
    r = oofun(st_log, inp, d=d, vectorized=True, engine_monotonity=1, engine_convexity=-1)
    r._interval_ = lambda domain, dtype: nonnegative_interval(inp, np.log, r.d, domain, dtype, 0.0)
    r.attach((inp > 1e-300)('log_domain_zero_bound_%d' % r._id, tol=-1e-07))
    return r


st_log10 = (--- This code section failed: ---

 L. 507         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             0  'x'
                6  LOAD_GLOBAL           1  'distribution'
                9  LOAD_ATTR             2  'stochasticDistribution'
               12  CALL_FUNCTION_2       2  None
               15  POP_JUMP_IF_FALSE    61  'to 61'
               18  LOAD_GLOBAL           1  'distribution'
               21  LOAD_ATTR             2  'stochasticDistribution'
               24  LOAD_GLOBAL           3  'log10'
               27  LOAD_FAST             0  'x'
               30  LOAD_ATTR             4  'values'
               33  CALL_FUNCTION_1       1  None
               36  LOAD_FAST             0  'x'
               39  LOAD_ATTR             5  'probabilities'
               42  LOAD_ATTR             6  'copy'
               45  CALL_FUNCTION_0       0  None
               48  CALL_FUNCTION_2       2  None
               51  LOAD_ATTR             7  '_update'
               54  LOAD_FAST             0  'x'
               57  CALL_FUNCTION_1       1  None
               60  RETURN_END_IF_LAMBDA
             61_0  COME_FROM            15  '15'

 L. 508        61  LOAD_GLOBAL           0  'isinstance'
               64  LOAD_FAST             0  'x'
               67  LOAD_GLOBAL           8  'multiarray'
               70  CALL_FUNCTION_2       2  None
               73  POP_JUMP_IF_FALSE   151  'to 151'
               76  LOAD_GLOBAL           0  'isinstance'
               79  LOAD_FAST             0  'x'
               82  LOAD_ATTR             9  'flat'
               85  LOAD_CONST               0
               88  BINARY_SUBSCR    
               89  LOAD_GLOBAL           1  'distribution'
               92  LOAD_ATTR             2  'stochasticDistribution'
               95  CALL_FUNCTION_2       2  None
             98_0  COME_FROM            73  '73'
               98  POP_JUMP_IF_FALSE   151  'to 151'
              101  LOAD_GLOBAL          10  'np'
              104  LOAD_ATTR            11  'array'
              107  BUILD_LIST_0          0 
              110  LOAD_FAST             0  'x'
              113  LOAD_ATTR             9  'flat'
              116  GET_ITER         
              117  FOR_ITER             18  'to 138'
              120  STORE_FAST            1  'elem'
              123  LOAD_GLOBAL           3  'log10'
              126  LOAD_FAST             1  'elem'
              129  CALL_FUNCTION_1       1  None
              132  LIST_APPEND           2  None
              135  JUMP_BACK           117  'to 117'
              138  CALL_FUNCTION_1       1  None
              141  LOAD_ATTR            12  'view'
              144  LOAD_GLOBAL           8  'multiarray'
              147  CALL_FUNCTION_1       1  None
              150  RETURN_END_IF_LAMBDA
            151_0  COME_FROM            98  '98'

 L. 509       151  LOAD_GLOBAL          10  'np'
              154  LOAD_ATTR             3  'log10'
              157  LOAD_FAST             0  'x'
              160  CALL_FUNCTION_1       1  None
              163  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 150
) if hasStochastic else np.log10
INV_LOG_10 = 1.0 / np.log(10)

def log10(inp):
    if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
        return ooarray([ log10(elem) for elem in inp ])
    if hasStochastic and isinstance(inp, distribution.stochasticDistribution):
        return distribution.stochasticDistribution(log10(inp.values), inp.probabilities.copy())._update(inp)
    if not isinstance(inp, oofun):
        return np.log10(inp)
    d = lambda x: Diag(INV_LOG_10 / x)
    r = oofun(st_log10, inp, d=d, vectorized=True, engine_monotonity=1, engine_convexity=-1)
    r._interval_ = lambda domain, dtype: nonnegative_interval(inp, np.log10, r.d, domain, dtype, 0.0)
    r.attach((inp > 1e-300)('log10_domain_zero_bound_%d' % r._id, tol=-1e-07))
    return r


st_log2 = (--- This code section failed: ---

 L. 528         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             0  'x'
                6  LOAD_GLOBAL           1  'distribution'
                9  LOAD_ATTR             2  'stochasticDistribution'
               12  CALL_FUNCTION_2       2  None
               15  POP_JUMP_IF_FALSE    61  'to 61'
               18  LOAD_GLOBAL           1  'distribution'
               21  LOAD_ATTR             2  'stochasticDistribution'
               24  LOAD_GLOBAL           3  'log2'
               27  LOAD_FAST             0  'x'
               30  LOAD_ATTR             4  'values'
               33  CALL_FUNCTION_1       1  None
               36  LOAD_FAST             0  'x'
               39  LOAD_ATTR             5  'probabilities'
               42  LOAD_ATTR             6  'copy'
               45  CALL_FUNCTION_0       0  None
               48  CALL_FUNCTION_2       2  None
               51  LOAD_ATTR             7  '_update'
               54  LOAD_FAST             0  'x'
               57  CALL_FUNCTION_1       1  None
               60  RETURN_END_IF_LAMBDA
             61_0  COME_FROM            15  '15'

 L. 529        61  LOAD_GLOBAL           0  'isinstance'
               64  LOAD_FAST             0  'x'
               67  LOAD_GLOBAL           8  'multiarray'
               70  CALL_FUNCTION_2       2  None
               73  POP_JUMP_IF_FALSE   151  'to 151'
               76  LOAD_GLOBAL           0  'isinstance'
               79  LOAD_FAST             0  'x'
               82  LOAD_ATTR             9  'flat'
               85  LOAD_CONST               0
               88  BINARY_SUBSCR    
               89  LOAD_GLOBAL           1  'distribution'
               92  LOAD_ATTR             2  'stochasticDistribution'
               95  CALL_FUNCTION_2       2  None
             98_0  COME_FROM            73  '73'
               98  POP_JUMP_IF_FALSE   151  'to 151'
              101  LOAD_GLOBAL          10  'np'
              104  LOAD_ATTR            11  'array'
              107  BUILD_LIST_0          0 
              110  LOAD_FAST             0  'x'
              113  LOAD_ATTR             9  'flat'
              116  GET_ITER         
              117  FOR_ITER             18  'to 138'
              120  STORE_FAST            1  'elem'
              123  LOAD_GLOBAL           3  'log2'
              126  LOAD_FAST             1  'elem'
              129  CALL_FUNCTION_1       1  None
              132  LIST_APPEND           2  None
              135  JUMP_BACK           117  'to 117'
              138  CALL_FUNCTION_1       1  None
              141  LOAD_ATTR            12  'view'
              144  LOAD_GLOBAL           8  'multiarray'
              147  CALL_FUNCTION_1       1  None
              150  RETURN_END_IF_LAMBDA
            151_0  COME_FROM            98  '98'

 L. 530       151  LOAD_GLOBAL          10  'np'
              154  LOAD_ATTR             3  'log2'
              157  LOAD_FAST             0  'x'
              160  CALL_FUNCTION_1       1  None
              163  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 150
) if hasStochastic else np.log2
INV_LOG_2 = 1.0 / np.log(2)

def log2(inp):
    if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
        return ooarray([ log2(elem) for elem in inp ])
    if hasStochastic and isinstance(inp, distribution.stochasticDistribution):
        return distribution.stochasticDistribution(log2(inp.values), inp.probabilities.copy())._update(inp)
    if not isinstance(inp, oofun):
        return np.log2(inp)
    d = lambda x: Diag(INV_LOG_2 / x)
    r = oofun(st_log2, inp, d=d, vectorized=True, engine_monotonity=1, engine_convexity=-1)
    r._interval_ = lambda domain, dtype: nonnegative_interval(inp, np.log2, r.d, domain, dtype, 0.0)
    r.attach((inp > 1e-300)('log2_domain_zero_bound_%d' % r._id, tol=-1e-07))
    return r


__all__ += ['log', 'log2', 'log10']

def dot(inp1, inp2):
    if not isinstance(inp1, oofun) and not isinstance(inp2, oofun):
        return np.dot(inp1, inp2)

    def aux_d(x, y):
        if y.size == 1:
            r = np.empty_like(x)
            r.fill(y)
            return Diag(r)
        else:
            return y

    r = oofun((lambda x, y: x * y if x.size == 1 or y.size == 1 else np.dot(x, y)), [inp1, inp2], d=((lambda x, y: aux_d(x, y)), (lambda x, y: aux_d(y, x))))
    r.getOrder = lambda *args, **kwargs: (inp1.getOrder(*args, **kwargs) if isinstance(inp1, oofun) else 0) + (inp2.getOrder(*args, **kwargs) if isinstance(inp2, oofun) else 0)
    return r


def cross(a, b):
    if not isinstance(a, oofun) and not isinstance(b, oofun):
        return np.cross(a, b)

    def aux_d(x, y):
        assert x.size == 3 and y.size == 3, 'currently FuncDesigner cross(x,y) is implemented for arrays of length 3 only'
        return np.array([[0, -y[2], y[1]], [y[2], 0, -y[0]], [-y[1], y[0], 0]])

    r = oofun((lambda x, y: np.cross(x, y)), [a, b], d=((lambda x, y: -aux_d(x, y)), (lambda x, y: aux_d(y, x))))
    r.getOrder = lambda *args, **kwargs: (a.getOrder(*args, **kwargs) if isinstance(a, oofun) else 0) + (b.getOrder(*args, **kwargs) if isinstance(b, oofun) else 0)
    return r


__all__ += ['dot', 'cross']

def ceil(inp):
    if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
        return ooarray([ ceil(elem) for elem in inp ])
    if not isinstance(inp, oofun):
        return np.ceil(inp)
    r = oofun((lambda x: np.ceil(x)), inp, vectorized=True, engine_monotonity=1)
    r._D = lambda *args, **kwargs: raise_except('derivative for FD ceil is unimplemented yet')
    r.criticalPoints = False
    return r


def floor(inp):
    if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
        return ooarray([ floor(elem) for elem in inp ])
    if not isinstance(inp, oofun):
        return np.floor(inp)
    r = oofun((lambda x: np.floor(x)), inp, vectorized=True, engine_monotonity=1)
    r._D = lambda *args, **kwargs: raise_except('derivative for FD floor is unimplemented yet')
    r.criticalPoints = False
    return r


st_sign = (--- This code section failed: ---

 L. 599         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             0  'x'
                6  LOAD_GLOBAL           1  'distribution'
                9  LOAD_ATTR             2  'stochasticDistribution'
               12  CALL_FUNCTION_2       2  None
               15  POP_JUMP_IF_FALSE    61  'to 61'
               18  LOAD_GLOBAL           1  'distribution'
               21  LOAD_ATTR             2  'stochasticDistribution'
               24  LOAD_GLOBAL           3  'sign'
               27  LOAD_FAST             0  'x'
               30  LOAD_ATTR             4  'values'
               33  CALL_FUNCTION_1       1  None
               36  LOAD_FAST             0  'x'
               39  LOAD_ATTR             5  'probabilities'
               42  LOAD_ATTR             6  'copy'
               45  CALL_FUNCTION_0       0  None
               48  CALL_FUNCTION_2       2  None
               51  LOAD_ATTR             7  '_update'
               54  LOAD_FAST             0  'x'
               57  CALL_FUNCTION_1       1  None
               60  RETURN_END_IF_LAMBDA
             61_0  COME_FROM            15  '15'

 L. 600        61  LOAD_GLOBAL           0  'isinstance'
               64  LOAD_FAST             0  'x'
               67  LOAD_GLOBAL           8  'multiarray'
               70  CALL_FUNCTION_2       2  None
               73  POP_JUMP_IF_FALSE   151  'to 151'
               76  LOAD_GLOBAL           0  'isinstance'
               79  LOAD_FAST             0  'x'
               82  LOAD_ATTR             9  'flat'
               85  LOAD_CONST               0
               88  BINARY_SUBSCR    
               89  LOAD_GLOBAL           1  'distribution'
               92  LOAD_ATTR             2  'stochasticDistribution'
               95  CALL_FUNCTION_2       2  None
             98_0  COME_FROM            73  '73'
               98  POP_JUMP_IF_FALSE   151  'to 151'
              101  LOAD_GLOBAL          10  'np'
              104  LOAD_ATTR            11  'array'
              107  BUILD_LIST_0          0 
              110  LOAD_FAST             0  'x'
              113  LOAD_ATTR             9  'flat'
              116  GET_ITER         
              117  FOR_ITER             18  'to 138'
              120  STORE_FAST            1  'elem'
              123  LOAD_GLOBAL           3  'sign'
              126  LOAD_FAST             1  'elem'
              129  CALL_FUNCTION_1       1  None
              132  LIST_APPEND           2  None
              135  JUMP_BACK           117  'to 117'
              138  CALL_FUNCTION_1       1  None
              141  LOAD_ATTR            12  'view'
              144  LOAD_GLOBAL           8  'multiarray'
              147  CALL_FUNCTION_1       1  None
              150  RETURN_END_IF_LAMBDA
            151_0  COME_FROM            98  '98'

 L. 601       151  LOAD_GLOBAL          10  'np'
              154  LOAD_ATTR             3  'sign'
              157  LOAD_FAST             0  'x'
              160  CALL_FUNCTION_1       1  None
              163  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 150
) if hasStochastic else np.sign

def sign(inp):
    if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
        return ooarray([ sign(elem) for elem in inp ])
    if hasStochastic and isinstance(inp, distribution.stochasticDistribution):
        return distribution.stochasticDistribution(sign(inp.values), inp.probabilities.copy())._update(inp)
    if not isinstance(inp, oofun):
        return np.sign(inp)
    r = oofun(st_sign, inp, vectorized=True, d=(lambda x: 0.0), engine_monotonity=1)
    r.criticalPoints = False
    return r


__all__ += ['ceil', 'floor', 'sign']

def sum_engine(r0, *args):
    if not hasStochastic:
        return PythonSum(args) + r0
    Args, Args_st = [], {}
    for elem in args:
        if isinstance(elem, distribution.stochasticDistribution):
            stDep = frozenset(elem.stochDep.keys())
            tmp = Args_st.get(stDep, None)
            if tmp is None:
                Args_st[stDep] = [
                 elem]
            else:
                Args_st[stDep].append(elem)
        else:
            Args.append(elem)

    r = PythonSum(Args) + r0
    if len(Args_st) == 0:
        return r
    else:
        for key, val in Args_st.items():
            maxDistributionSize = val[0].maxDistributionSize
            break

        stValues = Args_st.values()
        r1 = 0.0
        for elem in stValues:
            tmp = PythonSum(elem)
            r1 = tmp + r1
            r1.reduce(maxDistributionSize)

        r1 = r1 + r
        r1.maxDistributionSize = maxDistributionSize
        return r1


def sum_interval(R0, r, INP, domain, dtype):
    if len(INP) <= 10:
        B = []
        _r = [
         R0]
        DefiniteRange = True
        for inp in INP:
            arg_lb_ub, definiteRange = inp._interval(domain, dtype, allowBoundSurf=True)
            DefiniteRange = np.logical_and(DefiniteRange, definiteRange)
            if type(arg_lb_ub) == boundsurf:
                B.append(arg_lb_ub)
            else:
                _r.append(arg_lb_ub)

        _r = PythonSum(_r)
        R = _r if len(B) == 0 else boundsurf_sum(B, _r, DefiniteRange, domain)
        return (
         R, DefiniteRange)
    else:
        v = domain.modificationVar
        if v is not None:
            R, DefiniteRange = domain.storedSums[r][-1]
            has_infs = not (np.all(np.isfinite(R)) if type(R) != boundsurf else R.isfinite())
            if has_infs:
                R = np.asarray(R0, dtype).copy()
                if domain.isMultiPoint:
                    R = np.tile(R, (1, len(list(domain.values())[0][0])))
                DefiniteRange = True
                for inp in INP:
                    arg_lb_ub, definiteRange = inp._interval(domain, dtype)
                    if type(R) == type(arg_lb_ub) == np.ndarray and R.shape == arg_lb_ub.shape:
                        R += arg_lb_ub
                    else:
                        R = R + arg_lb_ub

                return (R, DefiniteRange)
            R = R - domain.storedSums[r][v]
            R2 = np.zeros((2, 1))
            B = []
            for inp in r.storedSumsFuncs[v]:
                arg_lb_ub, definiteRange = inp._interval(domain, dtype, allowBoundSurf=True)
                DefiniteRange = logical_and(DefiniteRange, definiteRange)
                if type(arg_lb_ub) == np.ndarray:
                    if R2.shape == arg_lb_ub.shape:
                        R2 += arg_lb_ub
                    else:
                        R2 = R2 + arg_lb_ub
                else:
                    B.append(arg_lb_ub)

            if type(R) == boundsurf:
                B.append(R)
                R = boundsurf_sum(B, R2, DefiniteRange, domain)
                R.definiteRange = logical_and(R.definiteRange, DefiniteRange)
            elif len(B):
                R = boundsurf_sum(B, R + R2, DefiniteRange, domain)
            else:
                R = R + R2
            return (
             R, DefiniteRange)
        D = {}
        R = np.asarray(R0).copy()
        if domain.isMultiPoint:
            R = np.tile(R, (1, len(list(domain.values())[0][0])))
        DefiniteRange = True
        B = []
        for inp in INP:
            arg_lb_ub, definiteRange = inp._interval(domain, dtype, allowBoundSurf=True)
            Tmp = (inp.is_oovar or inp._getDep)() if 1 else [inp]
            for oov in Tmp:
                tmp = D.get(oov, None)
                if tmp is None:
                    D[oov] = arg_lb_ub.copy()
                elif type(tmp) == type(arg_lb_ub) == np.ndarray and tmp.shape == arg_lb_ub.shape:
                    D[oov] += arg_lb_ub
                else:
                    D[oov] = tmp + arg_lb_ub

            DefiniteRange = logical_and(DefiniteRange, definiteRange)
            if type(arg_lb_ub) == boundsurf:
                B.append(arg_lb_ub)
            elif type(R) == np.ndarray == type(arg_lb_ub) and R.shape == arg_lb_ub.shape:
                R += arg_lb_ub
            else:
                R = R + arg_lb_ub

        if len(B):
            R = boundsurf_sum(B, R, DefiniteRange, domain)
            if 1 or R.Size() > 5:
                R = R.resolve()[0]
            D = dict((k, v.resolve()[0] if v.__class__ == boundsurf else v) for k, v in D.items())
        if v is None:
            D[-1] = (
             R, DefiniteRange)
        domain.storedSums[r] = D
        return (
         R, DefiniteRange)


def boundsurf_sum(B, s, DefiniteRange, domain):
    L = PythonSum([ b.l.c for b in B ]) + s[0]
    U = PythonSum([ b.u.c for b in B ]) + s[1]
    Ld = dictSum([ b.l.d for b in B ])
    Ud = dictSum([ b.u.d for b in B ])
    return boundsurf(surf(Ld, L), surf(Ud, U), DefiniteRange, domain)


def sum_derivative(r_, r0, INP, dep, point, fixedVarsScheduleID, Vars=None, fixedVars=None, useSparse='auto'):
    r = {}
    isSP = hasattr(point, 'maxDistributionSize') and point.maxDistributionSize != 0
    for elem in INP:
        if not elem.is_oovar and (elem.input is None or len(elem.input) == 0 or elem.input[0] is None):
            continue
        if elem.discrete:
            continue
        if elem.is_oovar:
            if fixedVars is not None and elem in fixedVars or Vars is not None and elem not in Vars:
                continue
            sz = np.asarray(point[elem]).size
            tmpres = (isinstance(point[elem], multiarray) or Eye)(sz) if 1 else np.ones(sz).view(multiarray)
            r_val = r.get(elem, None)
            if isSP:
                if r_val is not None:
                    r_val.append(tmpres)
                else:
                    r[elem] = [
                     tmpres]
            else:
                if r_val is not None:
                    if sz != 1 and isinstance(r_val, np.ndarray) and not isinstance(tmpres, np.ndarray):
                        tmpres = tmpres.toarray()
                    else:
                        if not np.isscalar(r_val) and not isinstance(r_val, np.ndarray) and isinstance(tmpres, np.ndarray):
                            r[elem] = r_val.toarray()
                        Tmp = tmpres.resolve(True) if isspmatrix(r[elem]) and type(tmpres) == DiagonalType else tmpres
                        try:
                            r[elem] += Tmp
                        except:
                            r[elem] = r[elem] + Tmp

                else:
                    r[elem] = tmpres
        else:
            tmp = elem._D(point, fixedVarsScheduleID, Vars, fixedVars, useSparse=useSparse)
            for key, val in tmp.items():
                r_val = r.get(key, None)
                if isSP:
                    if r_val is not None:
                        r_val.append(val)
                    else:
                        r[key] = [
                         val]
                elif r_val is not None:
                    if not np.isscalar(val) and isinstance(r_val, np.ndarray) and not isinstance(val, np.ndarray):
                        val = val.toarray()
                    elif not np.isscalar(r_val) and not isinstance(r_val, np.ndarray) and isinstance(val, np.ndarray):
                        r[key] = r_val.toarray()
                    if isspmatrix(r_val) and type(val) == DiagonalType:
                        val = val.resolve(True)
                    else:
                        if isspmatrix(val) and type(r_val) == DiagonalType:
                            r[key] = r_val.resolve(True)
                        try:
                            r[key] += val
                        except:
                            r[key] = r_val + val

                else:
                    r[key] = Copy(val)

    if isSP:
        for key, val in r.items():
            r[key] = sum_engine(0.0, *val)

    if useSparse is False:
        for key, val in r.items():
            if hasattr(val, 'toarray'):
                r[key] = val.toarray()

    if not isSP:
        Size = np.asarray(r0).size
        if Size == 1 and not point.isMultiPoint:
            if r_._lastFuncVarsID == fixedVarsScheduleID:
                if not np.isscalar(r_._f_val_prev):
                    Size = r_._f_val_prev.size
            else:
                Size = np.asarray(r_._getFuncCalcEngine(point, Vars=Vars, fixedVars=fixedVars, fixedVarsScheduleID=fixedVarsScheduleID)).size
        if Size != 1 and not point.isMultiPoint:
            for key, val in r.items():
                if not isinstance(val, diagonal):
                    if np.isscalar(val) or np.prod(val.shape) <= 1:
                        tmp = np.empty((Size, 1))
                        tmp.fill(val if np.isscalar(val) else val.item())
                        r[key] = tmp
                    elif val.shape[0] != Size:
                        tmp = np.tile(val, (Size, 1))
                        r[key] = tmp

    return r


def sum_getOrder(INP, *args, **kwargs):
    orders = [
     0] + [ inp.getOrder(*args, **kwargs) for inp in INP ]
    return np.max(orders)


def sum(inp, *args, **kwargs):
    if type(inp) == np.ndarray and inp.dtype != object:
        return np.sum(inp, *args, **kwargs)
    else:
        if isinstance(inp, ooarray) and inp.dtype != object:
            inp = inp.view(np.ndarray)
        cond_ooarray = isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp))
        if cond_ooarray and inp.size == 1:
            return np.asscalar(inp).sum()
        condIterableOfOOFuns = type(inp) in (list, tuple) or cond_ooarray
        if not isinstance(inp, oofun) and not condIterableOfOOFuns:
            return np.sum(inp, *args, **kwargs)
        if isinstance(inp, ooarray) and any(isinstance(elem, oofun) for elem in atleast_1d(inp)):
            inp = inp.tolist()
        if condIterableOfOOFuns:
            d, INP, r0 = [], [], 0.0
            for elem in inp:
                if not isinstance(elem, oofun):
                    r0 = r0 + np.asanyarray(elem)
                    continue
                INP.append(elem)

            if len(INP) == 0:
                return r0
            r = oofun((lambda *args: sum_engine(r0, *args)), INP, _isSum=True)
            r._summation_elements = INP if np.isscalar(r0) and r0 == 0.0 else INP + [r0]
            r.storedSumsFuncs = {}
            for inp in INP:
                Dep = [inp] if inp.is_oovar else inp._getDep()
                for v in Dep:
                    if v not in r.storedSumsFuncs:
                        r.storedSumsFuncs[v] = set()
                    r.storedSumsFuncs[v].add(inp)

            r.getOrder = lambda *args, **kw: sum_getOrder(INP, *args, **kw)
            R0 = np.tile(r0, (2, 1))
            r._interval_ = lambda *args, **kw: sum_interval(R0, r, INP, *args, **kw)
            r.vectorized = True
            r_dep = r._getDep()
            r._D = lambda *args, **kw: sum_derivative(r, r0, INP, r_dep, *args, **kw)
            return r
        return inp.sum(*args, **kwargs)


def prod(inp, *args, **kwargs):
    if not isinstance(inp, oofun):
        return np.prod(inp, *args, **kwargs)
    if len(args) != 0 or len(kwargs) != 0:
        raise FuncDesignerException('oofun for prod(x, *args,**kwargs) is not implemented yet')
    return inp.prod()


def norm(*args, **kwargs):
    if len(kwargs) or len(args) > 1:
        return np.linalg.norm(*args, **kwargs)
    r = sqrt(sum(args[0] ** 2), attachConstraints=False)
    return r


__all__ += ['sum', 'prod', 'norm']

def size(inp, *args, **kwargs):
    if not isinstance(inp, oofun):
        return np.size(inp, *args, **kwargs)
    return inp.size


def ifThenElse(condition, val1, val2, *args, **kwargs):
    assert len(args) == 0 and len(kwargs) == 0
    Val1 = atleast_oofun(val1)
    Val2 = atleast_oofun(val2)
    if isinstance(condition, bool):
        if condition:
            return Val1
        return Val2
    if isinstance(condition, oofun):
        f = lambda conditionResult, value1Result, value2Result: value1Result if conditionResult else value2Result
        r = oofun(f, [condition, val1, val2])
        r.D = --- This code section failed: ---

 L.1059         0  LOAD_DEREF            2  'condition'
                3  LOAD_FAST             0  'point'
                6  CALL_FUNCTION_1       1  None
                9  POP_JUMP_IF_FALSE    52  'to 52'
               12  LOAD_GLOBAL           0  'isinstance'
               15  LOAD_DEREF            1  'Val1'
               18  LOAD_GLOBAL           1  'oofun'
               21  CALL_FUNCTION_2       2  None
               24  POP_JUMP_IF_FALSE    48  'to 48'
               27  LOAD_DEREF            1  'Val1'
               30  LOAD_ATTR             2  'D'
               33  LOAD_FAST             0  'point'
               36  LOAD_FAST             1  'args'
               39  LOAD_FAST             2  'kwargs'
               42  CALL_FUNCTION_VAR_KW_1     1  None
               45  JUMP_ABSOLUTE        89  'to 89'
               48  BUILD_MAP_0           0  None
               51  RETURN_VALUE_LAMBDA
             52_0  COME_FROM             9  '9'

 L.1060        52  LOAD_GLOBAL           0  'isinstance'
               55  LOAD_DEREF            0  'Val2'
               58  LOAD_GLOBAL           1  'oofun'
               61  CALL_FUNCTION_2       2  None
               64  POP_JUMP_IF_FALSE    86  'to 86'
               67  LOAD_DEREF            0  'Val2'
               70  LOAD_ATTR             2  'D'
               73  LOAD_FAST             0  'point'
               76  LOAD_FAST             1  'args'
               79  LOAD_FAST             2  'kwargs'
               82  CALL_FUNCTION_VAR_KW_1     1  None
               85  RETURN_END_IF_LAMBDA
             86_0  COME_FROM            64  '64'
               86  BUILD_MAP_0           0  None
               89  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `None' instruction at offset -1
        r._D = --- This code section failed: ---

 L.1061         0  LOAD_DEREF            2  'condition'
                3  LOAD_FAST             0  'point'
                6  CALL_FUNCTION_1       1  None
                9  POP_JUMP_IF_FALSE    52  'to 52'
               12  LOAD_GLOBAL           0  'isinstance'
               15  LOAD_DEREF            1  'Val1'
               18  LOAD_GLOBAL           1  'oofun'
               21  CALL_FUNCTION_2       2  None
               24  POP_JUMP_IF_FALSE    48  'to 48'
               27  LOAD_DEREF            1  'Val1'
               30  LOAD_ATTR             2  '_D'
               33  LOAD_FAST             0  'point'
               36  LOAD_FAST             1  'args'
               39  LOAD_FAST             2  'kwargs'
               42  CALL_FUNCTION_VAR_KW_1     1  None
               45  JUMP_ABSOLUTE        89  'to 89'
               48  BUILD_MAP_0           0  None
               51  RETURN_VALUE_LAMBDA
             52_0  COME_FROM             9  '9'

 L.1062        52  LOAD_GLOBAL           0  'isinstance'
               55  LOAD_DEREF            0  'Val2'
               58  LOAD_GLOBAL           1  'oofun'
               61  CALL_FUNCTION_2       2  None
               64  POP_JUMP_IF_FALSE    86  'to 86'
               67  LOAD_DEREF            0  'Val2'
               70  LOAD_ATTR             2  '_D'
               73  LOAD_FAST             0  'point'
               76  LOAD_FAST             1  'args'
               79  LOAD_FAST             2  'kwargs'
               82  CALL_FUNCTION_VAR_KW_1     1  None
               85  RETURN_END_IF_LAMBDA
             86_0  COME_FROM            64  '64'
               86  BUILD_MAP_0           0  None
               89  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `None' instruction at offset -1
        r.d = errFunc
        return r
    raise FuncDesignerException('ifThenElse requires 1st argument (condition) to be either boolean or oofun, got %s instead' % type(condition))


__all__ += ['size', 'ifThenElse']

def decision(*args, **kwargs):
    pass


def max(inp, *args, **kwargs):
    if type(inp) in (list, tuple, np.ndarray) and (len(args) == 0 or len(args) == 1 and not isinstance(args[0], oofun)) and not any(isinstance(elem, oofun) for elem in inp if type(inp) in (list, tuple) else np.atleast_1d(inp)):
        return np.max(inp, *args, **kwargs)
    assert len(args) == len(kwargs) == 0, 'incorrect data type in FuncDesigner max or not implemented yet'
    if isinstance(inp, oofun):
        f = lambda x: np.max(x)

        def d(x):
            df = inp.d(x)
            ind = np.argmax(x)
            return df[ind, :]

        def interval(domain, dtype):
            lb_ub, definiteRange = inp._interval(domain, dtype)
            tmp1, tmp2 = lb_ub[0], lb_ub[1]
            return (np.vstack((np.max(np.vstack(tmp1), 0), np.max(np.vstack(tmp2), 0))), np.all(definiteRange, 0))

        r = oofun(f, inp, d=d, size=1, _interval_=interval)
    elif type(inp) in (list, tuple, ooarray):
        f = lambda *args: np.max([ arg for arg in args ])

        def interval(domain, dtype):
            arg_inf, arg_sup, tmp, DefiniteRange = ([], [], -np.inf, True)
            for _inp in inp:
                if isinstance(_inp, oofun):
                    lb_ub, definiteRange = _inp._interval(domain, dtype)
                    tmp1, tmp2 = lb_ub[0], lb_ub[1]
                    arg_inf.append(tmp1)
                    arg_sup.append(tmp2)
                    DefiniteRange = logical_and(DefiniteRange, definiteRange)
                elif tmp < _inp:
                    tmp = _inp

            r1, r2 = np.max(np.vstack(arg_inf), 0), np.max(np.vstack(arg_sup), 0)
            r1[r1 < tmp] = tmp
            r2[r2 < tmp] = tmp
            return (np.vstack((r1, r2)), DefiniteRange)

        r = oofun(f, inp, size=1, _interval_=interval)

        def _D(point, *args, **kwargs):
            ind = np.argmax([ s(point) if isinstance(s, oofun) else s for s in r.input ])
            if isinstance(r.input[ind], oofun):
                return r.input[ind]._D(point, *args, **kwargs)
            return {}

        r._D = _D
    else:
        return np.max(inp, *args, **kwargs)
    return r


def min(inp, *args, **kwargs):
    if type(inp) in (list, tuple, np.ndarray) and (len(args) == 0 or len(args) == 1 and not isinstance(args[0], oofun)) and not any(isinstance(elem, oofun) for elem in inp if type(inp) in (list, tuple) else np.atleast_1d(inp)):
        return np.min(inp, *args, **kwargs)
    assert len(args) == len(kwargs) == 0, 'incorrect data type in FuncDesigner min or not implemented yet'
    if isinstance(inp, oofun):
        f = lambda x: np.min(x)

        def d(x):
            df = inp.d(x)
            ind = np.argmin(x)
            return df[ind, :]

        def interval(domain, dtype):
            lb_ub, definiteRange = inp._interval(domain, dtype)
            tmp1, tmp2 = lb_ub[0], lb_ub[1]
            return (np.vstack((np.min(np.vstack(tmp1), 0), np.min(np.vstack(tmp2), 0))), np.all(definiteRange, 0))

        r = oofun(f, inp, d=d, size=1, _interval_=interval)
    elif type(inp) in (list, tuple, ooarray):
        f = lambda *args: np.min([ arg for arg in args ])

        def interval(domain, dtype):
            arg_inf, arg_sup, tmp, DefiniteRange = ([], [], np.inf, True)
            for _inp in inp:
                if isinstance(_inp, oofun):
                    lb_ub, definiteRange = _inp._interval(domain, dtype)
                    tmp1, tmp2 = lb_ub[0], lb_ub[1]
                    arg_inf.append(tmp1)
                    arg_sup.append(tmp2)
                    DefiniteRange = logical_and(DefiniteRange, definiteRange)
                elif tmp > _inp:
                    tmp = _inp

            r1, r2 = np.min(np.vstack(arg_inf), 0), np.min(np.vstack(arg_sup), 0)
            if np.isfinite(tmp):
                r1[r1 > tmp] = tmp
                r2[r2 > tmp] = tmp
            return (
             np.vstack((r1, r2)), DefiniteRange)

        r = oofun(f, inp, size=1, _interval_=interval)

        def _D(point, *args, **kwargs):
            ind = np.argmin([ s(point) if isinstance(s, oofun) else s for s in r.input ])
            if isinstance(r.input[ind], oofun):
                return r.input[ind]._D(point, *args, **kwargs)
            return {}

        r._D = _D
    else:
        return np.min(inp, *args, **kwargs)
    return r


__all__ += ['min', 'max']
det3 = lambda a, b, c: a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0]) + a[2] * (b[0] * c[1] - b[1] * c[0])
__all__ += ['det3']

def hstack(tup):
    c = [ isinstance(t, (oofun, ooarray)) for t in tup ]
    if any(isinstance(t, ooarray) for t in tup):
        return ooarray(np.hstack(tup))
    if not any(c):
        return np.hstack(tup)
    f = lambda *x: np.hstack(x)

    def getOrder(*args, **kwargs):
        orders = [
         0] + [ inp.getOrder(*args, **kwargs) for inp in tup ]
        return np.max(orders)

    r = oofun(f, tup, getOrder=getOrder)

    def _D(*args, **kwargs):
        sizes = [ (t(args[0], fixedVarsScheduleID=kwargs.get('fixedVarsScheduleID', -1)) if c[i] else np.asarray(t)).size for i, t in enumerate(tup) ]
        tmp = [ elem._D(*args, **kwargs) if c[i] else None for i, elem in enumerate(tup) ]
        res = {}
        for v in r._getDep():
            Temp = []
            for i, t in enumerate(tup):
                if c[i]:
                    temp = tmp[i].get(v, None)
                    if temp is not None:
                        Temp.append(temp if type(temp) != DiagonalType else temp.resolve(kwargs['useSparse']))
                    else:
                        Temp.append((Zeros if sizes[i] * np.asarray(args[0][v]).size > 1000 else np.zeros)((sizes[i], np.asarray(args[0][v]).size)))
                else:
                    sz = np.atleast_1d(t).shape[0]
                    Temp.append(Zeros((sz, 1)) if sz > 100 else np.zeros(sz))

            rr = Vstack([ elem for elem in Temp ])
            res[v] = rr if not isspmatrix(rr) or 0.3 * prod(rr.shape) > rr.size else rr.toarray()

        return res

    r._D = _D
    return r


__all__ += ['hstack']

def errFunc(*args, **kwargs):
    raise FuncDesignerException('error in FuncDesigner kernel, inform developers')