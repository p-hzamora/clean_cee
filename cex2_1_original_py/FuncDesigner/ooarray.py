# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: FuncDesigner\ooarray.pyc
# Compiled at: 2013-03-19 17:02:14
from baseClasses import OOArray
from FuncDesigner.multiarray import multiarray
from ooFun import oofun, Constraint
from numpy import isscalar, asscalar, ndarray, asarray, atleast_1d, asanyarray
import numpy as np
from FDmisc import FuncDesignerException

class ooarray(OOArray):
    __array_priority__ = 25
    _is_array_of_oovars = False

    def __new__(self, *args, **kwargs):
        tmp = args[0] if len(args) == 1 else args
        obj = asarray(tmp).view(self)
        obj._id = oofun._id
        obj.name = 'unnamed_ooarray_%d' % obj._id
        oofun._id += 1
        return obj

    __hash__ = lambda self: self._id

    def __len__(self):
        return self.size

    expected_kwargs = set(('tol', 'name'))

    def __call__(self, *args, **kwargs):
        expected_kwargs = self.expected_kwargs
        for elem in expected_kwargs:
            if elem in kwargs:
                setattr(self, elem, kwargs[elem])

        if len(args) > 1:
            raise FuncDesignerException('No more than single argument is expected')
        if len(args) == 0:
            if len(kwargs) == 0:
                raise FuncDesignerException('You should provide at least one argument')
        if len(args) != 0 and isinstance(args[0], str):
            self.name = args[0]
            for i, elem in enumerate(self.view(ndarray)):
                if isinstance(elem, oofun):
                    elem(self.name + '_' + str(i))

            args = args[1:]
            if len(args) == 0:
                return self
        if self._is_array_of_oovars and isinstance(args[0], dict) and self in args[0] and len(args) == 1 and len(kwargs) == 0:
            return args[0][self]
        else:
            Tmp = [ self[i](*args, **kwargs) if isinstance(self[i], oofun) else self[i] for i in range(self.size) ]
            tmp = asanyarray(Tmp)
            if np.any([ isinstance(elem, multiarray) for elem in Tmp ]):
                tmp = tmp.T.view(multiarray)
            if tmp.ndim == 2 or tmp.dtype != object:
                return tmp
            return ooarray(tmp)

    def __mul__(self, other):
        if self.size == 1:
            return ooarray(asscalar(self) * other)
        if isscalar(other):
            return ooarray(self.view(ndarray) * other if self.dtype != object else [ self[i] * other for i in range(self.size) ])
        if isinstance(other, oofun):
            hasSize = 'size' in dir(other)
            if not hasSize:
                other.size = 1
            if other.size == 1:
                if any([ isinstance(elem, oofun) for elem in atleast_1d(self) ]):
                    s = atleast_1d(self)
                    return ooarray([ s[i] * other for i in range(self.size) ])
                return ooarray(self * other)
            else:
                s, o = atleast_1d(self), atleast_1d(other)
                return ooarray([ s[i] * o[i] for i in range(self.size) ])
        else:
            if isinstance(other, ndarray):
                return ooarray(self * asscalar(other) if other.size == 1 else [ self[i] * other[i] for i in range(other.size) ])
            if type(other) in (list, tuple):
                r = self * asarray(other)
                return r
            raise FuncDesignerException('bug in multiplication')

    def __div__(self, other):
        if self.size == 1:
            return asscalar(self) / other
        if isscalar(other) or isinstance(other, ndarray) and other.size in (1, self.size):
            return self * (1.0 / other)
        if isinstance(other, oofun):
            if self.dtype != object:
                return self.view(ndarray) / other
            else:
                s = atleast_1d(self)
                return ooarray([ s[i] / other for i in range(self.size) ])

        elif isinstance(other, ooarray):
            if self.dtype != object:
                return self.view(ndarray) / other.view(ndarray)
            else:
                s, o = atleast_1d(self), atleast_1d(other)
                return ooarray([ s[i] / o[i] for i in range(self.size) ])

        else:
            raise FuncDesignerException('unimplemented yet')

    __truediv__ = __div__
    __floordiv__ = __div__

    def __rdiv__(self, other):
        if self.size == 1:
            return other / asscalar(self)
        return ooarray([ 1.0 / elem for elem in self.view(ndarray) ]) * other

    __rtruediv__ = __rdiv__

    def __add__(self, other):
        if isinstance(other, list):
            other = ooarray(other)
        if isscalar(other) or isinstance(other, ndarray) and other.size in (1, self.size):
            r = ooarray(self.view(ndarray) + other)
        elif isinstance(other, oofun):
            if self.dtype != object:
                r = self.view(ndarray) + other
            else:
                s = atleast_1d(self)
                r = ooarray([ s[i] + other for i in range(self.size) ])
        elif isinstance(other, ndarray):
            if self.dtype != object:
                r = self.view(ndarray) + other.view(ndarray)
            else:
                if self.size == 1:
                    r = other + asscalar(self)
                else:
                    r = ooarray([ self[i] + other[i] for i in range(self.size) ])
        else:
            raise FuncDesignerException('unimplemented yet')
        if isinstance(r, ndarray) and r.size == 1:
            r = asscalar(r)
        return r

    __radd__ = __add__
    __rmul__ = __mul__

    def __pow__(self, other):
        if isinstance(other, ndarray) and other.size > 1 and self.size > 1:
            return ooarray([ self[i] ** other[i] for i in range(self.size) ])
        Self = atleast_1d(self.view(ndarray))
        if any(isinstance(elem, (ooarray, oofun)) for elem in Self):
            return ooarray([ elem ** other for elem in Self ])
        return self.view(ndarray) ** other

    def __rpow__(self, other):
        if isscalar(other) or 'size' in dir(other) and isscalar(other.size) and other.size == 1 or 'size' not in dir(other):
            return ooarray([ other ** elem for elem in self.tolist() ])
        return ooarray([ other[i] ** elem for i, elem in enumerate(self.tolist()) ])

    def __eq__(self, other):
        r = self - other
        if r.dtype != object:
            return all(r)
        if r.size == 1:
            return asscalar(r) == 0
        return ooarray([ Constraint(elem, lb=0.0, ub=0.0) for elem in r.tolist() ])

    def __lt__(self, other):
        if self.dtype != object and (not isinstance(other, ooarray) or other.dtype != object):
            return self.view(ndarray) < (other.view(ndarray) if isinstance(other, ooarray) else other)
        if isinstance(other, (ndarray, list, tuple)) and self.size > 1 and len(other) > 1:
            return ooarray([ self[i] < other[i] for i in range(self.size) ])
        if isscalar(other) or isinstance(other, (ndarray, list, tuple)) and len(other) == 1:
            return ooarray([ elem < other for elem in self ])
        if isinstance(other, oofun):
            if 'size' in other.__dict__ and not isinstance(other.size, oofun):
                if other.size == self.size:
                    return ooarray([ elem[i] < other[i] for i in range(self.size) ])
                if self.size == 1:
                    return ooarray([ self[0] < other[i] for i in range(other.size) ])
                FuncDesignerException('bug or yet unimplemented case in FD kernel')
            else:
                return ooarray([ elem < other for elem in self ])
        raise FuncDesignerException('unimplemented yet')

    def __le__(self, other):
        if self.dtype != object and (not isinstance(other, ooarray) or other.dtype != object):
            return self.view(ndarray) <= (other.view(ndarray) if isinstance(other, ooarray) else other)
        if isinstance(other, (ndarray, list, tuple)) and self.size > 1 and len(other) > 1:
            return ooarray([ self[i] <= other[i] for i in range(self.size) ])
        if isscalar(other) or isinstance(other, (ndarray, list, tuple)) and len(other) == 1:
            return ooarray([ elem <= other for elem in self ])
        if isinstance(other, oofun):
            if 'size' in other.__dict__ and not isinstance(other.size, oofun):
                if other.size == self.size:
                    return ooarray([ elem[i] <= other[i] for i in range(self.size) ])
                if self.size == 1:
                    return ooarray([ self[0] <= other[i] for i in range(other.size) ])
                FuncDesignerException('bug or yet unimplemented case in FD kernel')
            else:
                return ooarray([ elem <= other for elem in self ])
        raise FuncDesignerException('unimplemented yet')

    def __gt__(self, other):
        if self.dtype != object and (not isinstance(other, ooarray) or other.dtype != object):
            return self.view(ndarray) > (other.view(ndarray) if isinstance(other, ooarray) else other)
        if isinstance(other, (ndarray, list, tuple)) and self.size > 1 and len(other) > 1:
            return ooarray([ self[i] > other[i] for i in range(self.size) ])
        if isscalar(other) or isinstance(other, (ndarray, list, tuple)) and len(other) == 1:
            return ooarray([ elem > other for elem in self ])
        if isinstance(other, oofun):
            if 'size' in other.__dict__ and not isinstance(other.size, oofun):
                if other.size == self.size:
                    return ooarray([ elem[i] > other[i] for i in range(self.size) ])
                if self.size == 1:
                    return ooarray([ self[0] > other[i] for i in range(other.size) ])
                FuncDesignerException('bug or yet unimplemented case in FD kernel')
            else:
                return ooarray([ elem > other for elem in self ])
        raise FuncDesignerException('unimplemented yet')

    def __ge__(self, other):
        if self.dtype != object and (not isinstance(other, ooarray) or other.dtype != object):
            return self.view(ndarray) >= (other.view(ndarray) if isinstance(other, ooarray) else other)
        if isinstance(other, (ndarray, list, tuple)) and self.size > 1 and len(other) > 1:
            return ooarray([ self[i] >= other[i] for i in range(self.size) ])
        if isscalar(other) or isinstance(other, (ndarray, list, tuple)) and len(other) == 1:
            return ooarray([ elem >= other for elem in self ])
        if isinstance(other, oofun):
            if 'size' in other.__dict__ and not isinstance(other.size, oofun):
                if other.size == self.size:
                    return ooarray([ elem[i] >= other[i] for i in range(self.size) ])
                if self.size == 1:
                    return ooarray([ self[0] >= other[i] for i in range(other.size) ])
                FuncDesignerException('bug or yet unimplemented case in FD kernel')
            else:
                return ooarray([ elem >= other for elem in self ])
        raise FuncDesignerException('unimplemented yet')