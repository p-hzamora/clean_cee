# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: FuncDesigner\FDmisc.pyc
# Compiled at: 2013-05-21 10:21:10
PythonSum = sum
from numpy import asscalar, isscalar, asfarray, ndarray, prod
import numpy as np
from baseClasses import MultiArray
scipyInstalled = True
try:
    import scipy, scipy.sparse as SP
except:
    scipyInstalled = False

from baseClasses import Stochastic

class FuncDesignerException(BaseException):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def checkSizes(a, b):
    if a.size != 1 and b.size != 1 and a.size != b.size:
        raise FuncDesignerException('operation of oovar/oofun ' + a.name + ' and object with inappropriate size:' + str(a.size) + ' vs ' + b.size)


scipyAbsentMsg = 'Probably scipy installation could speed up running the code involved'
pwSet = set()

def pWarn(msg):
    if msg in pwSet:
        return
    pwSet.add(msg)
    print 'FuncDesigner warning: ' + msg


class diagonal:
    isOnes = False
    __array_priority__ = 150000

    def __init__(self, arr, scalarMultiplier=1.0, size=0):
        self.diag = arr.copy() if arr is not None else None
        self.scalarMultiplier = scalarMultiplier if isscalar(scalarMultiplier) else asscalar(scalarMultiplier) if type(scalarMultiplier) == ndarray else scalarMultiplier[(0,
                                                                                                                                                                           0)] if scipyInstalled and SP.isspmatrix(scalarMultiplier) else raise_except()
        self.size = arr.size if size == 0 else size
        if arr is None:
            self.isOnes = True
        return

    copy = lambda self: diagonal(self.diag, scalarMultiplier=self.scalarMultiplier, size=self.size)

    def toarray(self):
        if self.isOnes:
            tmp = np.empty(self.size)
            scalarMultiplier = asscalar(self.scalarMultiplier) if type(self.scalarMultiplier) == ndarray else self.scalarMultiplier
            tmp.fill(scalarMultiplier)
            return np.diag(tmp)
        else:
            return np.diag(self.diag * self.scalarMultiplier)

    def resolve(self, useSparse):
        if useSparse in (True, 'auto') and scipyInstalled and self.size > 50:
            if self.isOnes:
                tmp = np.empty(self.size)
                tmp.fill(self.scalarMultiplier)
            else:
                tmp = self.diag * self.scalarMultiplier
            return SP.dia_matrix((tmp, 0), shape=(self.size, self.size))
        else:
            return self.toarray()

    def __add__(self, item):
        if type(item) == DiagonalType:
            if self.isOnes and item.isOnes:
                return diagonal(None, self.scalarMultiplier + item.scalarMultiplier, size=self.size)
            else:
                if self.isOnes:
                    d1 = np.empty(self.size)
                    d1.fill(self.scalarMultiplier)
                else:
                    d1 = self.diag
                if item.isOnes:
                    d2 = np.empty(item.size)
                    d2.fill(item.scalarMultiplier)
                else:
                    d2 = item.diag
                return diagonal(d1 * self.scalarMultiplier + d2 * item.scalarMultiplier)

        else:
            if np.isscalar(item) or type(item) == np.ndarray:
                return self.resolve(False) + item
            else:
                assert SP.isspmatrix(item)
                return self.resolve(True) + item

        return

    def __radd__(self, item):
        return self.__add__(item)

    def __neg__(self):
        return diagonal(self.diag, -self.scalarMultiplier, size=self.size)

    def __mul__(self, item):
        if np.isscalar(item):
            return diagonal(self.diag, item * self.scalarMultiplier, size=self.size)
        else:
            if type(item) == DiagonalType:
                scalarMultiplier = item.scalarMultiplier * self.scalarMultiplier
                if self.isOnes:
                    diag = item.diag
                elif item.isOnes:
                    diag = self.diag
                else:
                    diag = self.diag * item.diag
                return diagonal(diag, scalarMultiplier, size=self.size)
            if isinstance(item, np.ndarray):
                if item.size == 1:
                    return diagonal(self.diag, scalarMultiplier=np.asscalar(item) * self.scalarMultiplier, size=self.size)
                else:
                    if min(item.shape) == 1:
                        r = self.scalarMultiplier * item.flatten()
                        if self.diag is not None:
                            r *= self.diag
                        return r.reshape(item.shape)
                    if self.isOnes:
                        D = np.empty(self.size)
                        D.fill(self.scalarMultiplier)
                    else:
                        D = self.scalarMultiplier * self.diag if self.scalarMultiplier != 1.0 else self.diag
                    return D.reshape(-1, 1) * item

            else:
                if prod(item.shape) == 1:
                    return diagonal(self.diag, scalarMultiplier=self.scalarMultiplier * item[(0,
                                                                                              0)], size=self.size)
                else:
                    tmp = self.resolve(True)
                    if not SP.isspmatrix(tmp):
                        tmp = SP.lil_matrix(tmp)
                    return tmp._mul_sparse_matrix(item)

            return

    def __getattr__(self, attr):
        if attr == 'T':
            return self
        if attr == 'shape':
            return (self.size, self.size)
        if attr == 'ndim':
            return 2
        raise AttributeError('you are trying to obtain incorrect attribute "%s" for FuncDesigner diagonal' % attr)

    def __rmul__(self, item):
        if isscalar(item):
            return self.__mul__(item)
        return self.__mul__(item.T).T

    def __div__(self, other):
        if isinstance(other, np.ndarray) and other.size == 1:
            other = np.asscalar(other)
        if np.isscalar(other) or prod(other.shape) == 1:
            return diagonal(self.diag, self.scalarMultiplier / other, size=self.size)
        else:
            return diagonal(self.diag / other if self.diag is not None else 1.0 / other, self.scalarMultiplier, size=self.size)
            return


DiagonalType = type(diagonal(np.array([0, 0])))
Eye = lambda n: 1.0 if n == 1 else diagonal(None, size=n)

def Diag(x, *args, **kw):
    if isscalar(x) or type(x) == ndarray and x.size == 1 or isinstance(x, (Stochastic, MultiArray)):
        return x
    return diagonal((asfarray(x) if x is not None else x), *args, **kw)
    return


def dictSum(dicts):
    K = set().union(*[ set(d.keys()) for d in dicts ])
    R = dict((v, []) for v in K)
    for d in dicts:
        for k, val in d.items():
            R[k].append(val)

    r = dict((k, PythonSum(val)) for k, val in R.items())
    return r


class fixedVarsScheduleID:
    fixedVarsScheduleID = 0

    def _getDiffVarsID(*args):
        fixedVarsScheduleID.fixedVarsScheduleID += 1
        return fixedVarsScheduleID.fixedVarsScheduleID


DiffVarsID = fixedVarsScheduleID()
_getDiffVarsID = lambda *args: DiffVarsID._getDiffVarsID(*args)
try:
    import numpypy
    isPyPy = True
except ImportError:
    isPyPy = False

def raise_except(*args, **kwargs):
    raise FuncDesignerException('bug in FuncDesigner engine, inform developers')


class Extras:
    pass


def broadcast(func, oofuncs, useAttachedConstraints, *args, **kwargs):
    from ooFun import oofun
    if isinstance(oofuncs, oofun):
        oofuncs = [
         oofuncs]
    oofun._BroadCastID += 1
    for oof in oofuncs:
        if oof is not None:
            oof._broadcast(func, useAttachedConstraints, *args, **kwargs)

    return


def _getAllAttachedConstraints(oofuns):
    from FuncDesigner import broadcast
    r = set()

    def F(oof):
        r.update(oof.attachedConstraints)

    broadcast(F, oofuns, useAttachedConstraints=True)
    return r


def formDepCounter(oofuns):
    from FuncDesigner import broadcast, oofun
    R = {}

    def func(oof):
        if oof.is_oovar:
            R[oof] = {oof: 1}
            return
        dicts = [ R.get(inp) for inp in oof.input if isinstance(inp, oofun) ]
        R[oof] = dictSum(dicts)

    broadcast(func, oofuns, useAttachedConstraints=False)
    return R


def formResolveSchedule(oof):
    depsNumber = formDepCounter(oof)

    def F(ff, depsNumberDict, baseFuncDepsNumber, R):
        tmp = depsNumberDict[ff]
        s = []
        for k, v in tmp.items():
            if baseFuncDepsNumber[k] == v:
                s.append(k)
                baseFuncDepsNumber[k] -= 1

        if len(s):
            R[ff] = s

    R = {}
    broadcast(F, oof, False, depsNumber, depsNumber[oof].copy(), R)
    R.pop(oof, None)
    oof.resolveSchedule = R
    return