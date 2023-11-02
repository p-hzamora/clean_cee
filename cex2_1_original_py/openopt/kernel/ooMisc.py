# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\ooMisc.pyc
# Compiled at: 2012-12-08 11:04:59
__docformat__ = 'restructuredtext en'
from numpy import zeros, ones, copy, isfinite, where, asarray, inf, array, asfarray, dot, ndarray, prod, flatnonzero, max, abs, sqrt, sum, atleast_1d, asscalar
from nonOptMisc import scipyAbsentMsg, scipyInstalled, isspmatrix, Hstack, Vstack, coo_matrix, isPyPy
Copy = --- This code section failed: ---

 L.   6         0  LOAD_GLOBAL           0  'type'
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
try:
    from numpy import linalg
    norm = linalg.norm
except ImportError:

    def norm(x, k=2, *args, **kw):
        if len(args) or len(kw):
            raise ImportError('openopt overload for PyPy numpy linalg.norm cannot handle additional args or kwargs')
        if k == 2:
            return sqrt(sum(asarray(x) ** 2))
        if k == inf:
            return max(abs(x))
        if k == 1:
            return sum(abs(x))
        raise ImportError('unimplemented')


def Len(arg):
    if type(arg) == ndarray:
        if arg.size > 1:
            return arg.size
        if arg.size == 1 and atleast_1d(arg)[0] is not None:
            return 1
        if arg.size == 0:
            return 0
    if type(arg) in [int, float]:
        return 1
    else:
        if arg == None or arg == [] or isinstance(arg, ndarray) and arg.size == 1 and arg == array(None, dtype=object):
            return 0
        return len(arg)
        return


def xBounds2Matrix(p):
    """
    transforms lb - ub bounds into (A, x) <= b, (Aeq, x) = beq conditions
    this func is developed for those solvers that can handle lb, ub only via c(x)<=0, h(x)=0
    """
    IndLB, IndUB, IndEQ = isfinite(p.lb) & ~(p.lb == p.ub), isfinite(p.ub) & ~(p.lb == p.ub), p.lb == p.ub
    indLB, indUB, indEQ = where(IndLB)[0], where(IndUB)[0], where(IndEQ)[0]
    nLB, nUB, nEQ = Len(indLB), Len(indUB), Len(indEQ)
    if nLB > 0 or nUB > 0:
        if p.useSparse is True or isspmatrix(p.A) or scipyInstalled and nLB + nUB >= p.A.shape[0] and p.useSparse is not False:
            R1 = coo_matrix((-ones(nLB), (range(nLB), indLB)), shape=(nLB, p.n)) if nLB != 0 else zeros((0, p.n))
            R2 = coo_matrix((ones(nUB), (range(nUB), indUB)), shape=(nUB, p.n)) if nUB != 0 else zeros((0, p.n))
        else:
            R1 = zeros((nLB, p.n))
            if isPyPy:
                for i in range(nLB):
                    R1[(i, indLB[i])] = -1

            else:
                R1[(range(nLB), indLB)] = -1
            R2 = zeros((nUB, p.n))
            if isPyPy:
                for i in range(nUB):
                    R2[(i, indUB[i])] = -1

            else:
                R2[(range(nUB), indUB)] = 1
        p.A = Vstack((p.A, R1, R2))
        if hasattr(p, '_A'):
            delattr(p, '_A')
        if isspmatrix(p.A):
            if prod(p.A.shape) > 10000:
                p.A = p.A.tocsc()
                p._A = p.A
            else:
                p.A = p.A.A
        p.b = Hstack((p.b, -p.lb[IndLB], p.ub[IndUB]))
    if nEQ > 0:
        if p.useSparse is True or isspmatrix(p.Aeq) or scipyInstalled and nEQ >= p.Aeq.shape[0] and p.useSparse is not False:
            R = coo_matrix(([1] * nEQ, (range(nEQ), indEQ)), shape=(nEQ, p.n))
        else:
            R = zeros((nEQ, p.n))
        p.Aeq = Vstack((p.Aeq, R))
        if hasattr(p, '_Aeq'):
            delattr(p, '_Aeq')
        if isspmatrix(p.Aeq):
            if prod(p.Aeq.shape) > 10000:
                p.Aeq = p.Aeq.tocsc()
                p._Aeq = p.Aeq
            else:
                p.Aeq = p.Aeq.A
        p.beq = Hstack((p.beq, p.lb[IndEQ]))
    p.lb = -inf * ones(p.n)
    p.ub = inf * ones(p.n)
    nA, nAeq = prod(p.A.shape), prod(p.Aeq.shape)
    SizeThreshold = 32768
    if scipyInstalled and p.useSparse is not False:
        from scipy.sparse import csc_matrix
        if nA > SizeThreshold and not isspmatrix(p.A) and flatnonzero(p.A).size < 0.25 * nA:
            p._A = csc_matrix(p.A)
        if nAeq > SizeThreshold and not isspmatrix(p.Aeq) and flatnonzero(p.Aeq).size < 0.25 * nAeq:
            p._Aeq = csc_matrix(p.Aeq)
    if (nA > SizeThreshold or nAeq > SizeThreshold) and not scipyInstalled and p.useSparse is not False:
        p.pWarn(scipyAbsentMsg)


def LinConst2WholeRepr(p):
    """
    transforms  (A, x) <= b, (Aeq, x) = beq into Awhole, bwhole, dwhole constraints (see help(LP))
    this func is developed for those solvers that can handle linear (in)equality constraints only via Awhole
    """
    if p.A == None and p.Aeq == None:
        return
    else:
        p.Awhole = Vstack([ elem for elem in [p.Awhole, p.A, p.Aeq] if elem is not None ])
        p.A, p.Aeq = (None, None)
        bwhole = Copy(p.bwhole)
        p.bwhole = zeros(Len(p.b) + Len(p.beq) + Len(p.bwhole))
        p.bwhole[:(Len(bwhole))] = bwhole
        p.bwhole[(Len(bwhole)):(Len(bwhole) + Len(p.b))] = p.b
        p.bwhole[(Len(bwhole) + Len(p.b)):] = p.beq
        dwhole = Copy(p.dwhole)
        p.dwhole = zeros(Len(p.bwhole))
        if dwhole.size:
            p.dwhole[:(Len(bwhole))] = dwhole
        p.dwhole[(Len(bwhole)):(Len(bwhole) + Len(p.b))] = -1
        p.dwhole[(Len(bwhole) + Len(p.b)):] = 0
        p.b = None
        p.beq = None
        return


def WholeRepr2LinConst(p):
    """
    transforms  Awhole, bwhole, dwhole  into (A, x) <= b, (Aeq, x) = beq constraints (see help(LP))
    this func is developed for those solvers that can handle linear (in)equality constraints only via Awhole
    """
    if p.dwhole == None:
        return
    else:
        ind_less = where(p.dwhole == -1)[0]
        ind_greater = where(p.dwhole == 1)[0]
        ind_equal = where(p.dwhole == 0)[0]
        if len(ind_equal) != 0:
            Aeq, beq = Copy(p.Aeq), Copy(p.beq)
            p.Aeq = zeros([Len(p.beq) + len(ind_equal), p.n])
            if Aeq.size:
                p.Aeq[:(Len(p.beq))] = Aeq
            if len(ind_equal):
                p.Aeq[(Len(p.beq)):] = p.Awhole[ind_equal]
            p.beq = zeros([Len(p.beq) + len(ind_equal)])
            if beq.size:
                p.beq[:(Len(beq))] = beq
            if len(ind_equal):
                p.beq[(Len(beq)):] = p.bwhole[ind_equal]
        if len(ind_less) + len(ind_greater) > 0:
            A, b = Copy(p.A), Copy(p.b)
            p.A = zeros([Len(p.b) + len(ind_less) + len(ind_greater), p.n])
            if A.size:
                p.A[:(Len(p.b))] = A
            p.A[(Len(p.b)):(Len(p.b) + len(ind_less))] = p.Awhole[ind_less]
            p.A[(Len(p.b) + len(ind_less)):] = -p.Awhole[ind_greater]
            p.b = zeros(Len(p.b) + len(ind_less) + len(ind_greater))
            if b.size:
                p.b[:(Len(b))] = b
            if len(ind_less):
                p.b[(Len(b)):(Len(b) + len(ind_less))] = p.bwhole[ind_less]
            if len(ind_greater):
                p.b[(Len(b) + len(ind_less)):] = -p.bwhole[ind_greater]
        p.Awhole = None
        p.bwhole = None
        p.dwhole = None
        return


def assignScript(p, dictOfParams):
    for key, val in dictOfParams.items():
        if key == 'manage':
            continue
        setattr(p, key, val)


def setNonLinFuncsNumber(p, userFunctionType):
    args = getattr(p.args, userFunctionType)
    fv = getattr(p.user, userFunctionType)
    if p.isFDmodel:
        from FuncDesigner import oopoint
        X = oopoint(p._x0, maxDistributionSize=p.maxDistributionSize)
        kwargs = {'Vars': p.freeVars, 'fixedVarsScheduleID': p._FDVarsID, 'fixedVars': p.fixedVars}
    else:
        X = p.x0
        kwargs = {}
    if len(fv) == 1:
        p.functype[userFunctionType] = 'single func'
    if fv is None or type(fv) in [list, tuple] and (len(fv) == 0 or fv[0] is None):
        setattr(p, 'n' + userFunctionType, 0)
    elif type(fv) in [list, tuple] and len(fv) > 1:
        number = 0
        arr = []
        for func in fv:
            if isinstance(func, (list, tuple, set, ndarray)):
                for elem in func:
                    number += asarray(elem(*((X,) + args))).size

            else:
                number += asarray(func(*((X,) + args))).size
            arr.append(number)

        if len(arr) < number:
            p.functype[userFunctionType] = 'block'
        elif len(arr) > 1:
            p.functype[userFunctionType] = 'some funcs R^nvars -> R'
        else:
            assert p.functype[userFunctionType] == 'single func'
        setattr(p, 'n' + userFunctionType, number)
        if p.functype[userFunctionType] == 'block':
            setattr(p, 'arr_of_indexes_' + userFunctionType, array(arr) - 1)
    else:
        if type(fv) in [list, tuple]:
            FV = fv[0]
        else:
            FV = fv
        tmp = FV(*((X,) + args), **kwargs)
        if p.isFDmodel:
            if 'quantified' in dir(tmp):
                p.err('\n                Optimization problem objective and constraints cannot be of type Stochastic, \n                you can handle only functions on them like mean(X), std(X), var(X), P(X<Y) etc')
        setattr(p, 'n' + userFunctionType, sum([ asarray(elem).size for elem in tmp ]) if isinstance(tmp, (list, tuple)) else asarray(tmp).size)
    return


def economyMult(M, V):
    assert V.ndim <= 1 or V.shape[1] == 1
    if True or all(V) or isPyPy:
        return dot(M, V)
    else:
        ind = where(V != 0)[0]
        r = dot(M[:, ind], V[ind])
        return r


def Find(M):
    if isinstance(M, ndarray):
        rows, cols = where(M)
        vals = M[(rows, cols)]
    else:
        from scipy import sparse as sp
        assert sp.isspmatrix(M)
        rows, cols, vals = sp.find(M)
    return (
     rows.tolist(), cols.tolist(), vals.tolist())


class isSolved(BaseException):

    def __init__(self):
        pass


class killThread(BaseException):

    def __init__(self):
        pass