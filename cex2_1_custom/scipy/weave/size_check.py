# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\weave\size_check.pyc
# Compiled at: 2013-03-29 22:51:36
from __future__ import absolute_import, print_function
from numpy import ones, ndarray, array, asarray, concatenate, zeros, shape, alltrue, equal, divide, arccos, arcsin, arctan, cos, cosh, sin, sinh, exp, ceil, floor, fabs, log, log10, sqrt, argmin, argmax, argsort, around, absolute, sign, negative, float32
import sys
numericTypes = (
 int, long, float, complex)

def isnumeric(t):
    return isinstance(t, numericTypes)


def time_it():
    import time
    expr = 'ex[:,1:,1:] =   ca_x[:,1:,1:] * ex[:,1:,1:]+ cb_y_x[:,1:,1:] * (hz[:,1:,1:] - hz[:,:-1,1:])- cb_z_x[:,1:,1:] * (hy[:,1:,1:] - hy[:,1:,:-1])'
    ex = ones((10, 10, 10), dtype=float32)
    ca_x = ones((10, 10, 10), dtype=float32)
    cb_y_x = ones((10, 10, 10), dtype=float32)
    cb_z_x = ones((10, 10, 10), dtype=float32)
    hz = ones((10, 10, 10), dtype=float32)
    hy = ones((10, 10, 10), dtype=float32)
    N = 1
    t1 = time.time()
    for i in range(N):
        passed = check_expr(expr, locals())

    t2 = time.time()
    print('time per call:', (t2 - t1) / N)
    print('passed:', passed)


def check_expr(expr, local_vars, global_vars={}):
    """ Currently only checks expressions (not suites).
        Doesn't check that lhs = rhs. checked by compiled func though
    """
    values = {}
    for var, val in global_vars.items():
        if isinstance(val, ndarray):
            values[var] = dummy_array(val, name=var)
        elif isnumeric(val):
            values[var] = val

    for var, val in local_vars.items():
        if isinstance(val, ndarray):
            values[var] = dummy_array(val, name=var)
        if isnumeric(val):
            values[var] = val

    exec (
     expr, values)
    try:
        exec (expr, values)
    except:
        try:
            eval(expr, values)
        except:
            return 0

    return 1


empty = array(())
empty_slice = slice(None)

def make_same_length(x, y):
    try:
        Nx = len(x)
    except:
        Nx = 0

    try:
        Ny = len(y)
    except:
        Ny = 0

    if Nx == Ny == 0:
        return (empty, empty)
    if Nx == Ny:
        return (asarray(x), asarray(y))
    diff = abs(Nx - Ny)
    front = ones(diff, int)
    if Nx > Ny:
        return (asarray(x), concatenate((front, y)))
    if Ny > Nx:
        return (concatenate((front, x)), asarray(y))


def binary_op_size(xx, yy):
    """ This returns the resulting size from operating on xx, and yy
        with a binary operator.  It accounts for broadcasting, and
        throws errors if the array sizes are incompatible.
    """
    x, y = make_same_length(xx, yy)
    res = zeros(len(x))
    for i in range(len(x)):
        if x[i] == y[i]:
            res[i] = x[i]
        elif x[i] == 1:
            res[i] = y[i]
        elif y[i] == 1:
            res[i] = x[i]
        else:
            raise ValueError('frames are not aligned')

    return res


class dummy_array(object):

    def __init__(self, ary, ary_is_shape=0, name=None):
        self.name = name
        if ary_is_shape:
            self.shape = ary
        else:
            try:
                self.shape = shape(ary)
            except:
                self.shape = empty

    def binary_op(self, other):
        try:
            x = other.shape
        except AttributeError:
            x = empty

        new_shape = binary_op_size(self.shape, x)
        return dummy_array(new_shape, 1)

    def __cmp__(self, other):
        if isnumeric(other):
            return 0
        if len(self.shape) == len(other.shape) == 0:
            return 0
        return not alltrue(equal(self.shape, other.shape), axis=0)

    def __add__(self, other):
        return self.binary_op(other)

    def __radd__(self, other):
        return self.binary_op(other)

    def __sub__(self, other):
        return self.binary_op(other)

    def __rsub__(self, other):
        return self.binary_op(other)

    def __mul__(self, other):
        return self.binary_op(other)

    def __rmul__(self, other):
        return self.binary_op(other)

    def __div__(self, other):
        return self.binary_op(other)

    def __rdiv__(self, other):
        return self.binary_op(other)

    def __mod__(self, other):
        return self.binary_op(other)

    def __rmod__(self, other):
        return self.binary_op(other)

    def __lshift__(self, other):
        return self.binary_op(other)

    def __rshift__(self, other):
        return self.binary_op(other)

    def __neg__(self, other):
        return self

    def __pos__(self, other):
        return self

    def __abs__(self, other):
        return self

    def __invert__(self, other):
        return self

    def __setitem__(self, indices, val):
        pass

    def __len__(self):
        return self.shape[0]

    def __getslice__(self, i, j):
        i = max(i, 0)
        j = max(j, 0)
        return self.__getitem__((slice(i, j),))

    def __getitem__(self, indices):
        if not isinstance(indices, tuple):
            indices = (
             indices,)
        if Ellipsis in indices:
            raise IndexError('Ellipsis not currently supported')
        new_dims = []
        dim = 0
        for index in indices:
            try:
                dim_len = self.shape[dim]
            except IndexError:
                raise IndexError('To many indices specified')

            if index is empty_slice:
                slc_len = dim_len
            elif isinstance(index, slice):
                beg, end, step = index.start, index.stop, index.step
                if beg is None:
                    beg = 0
                if end == sys.maxint or end is None:
                    end = dim_len
                if step is None:
                    step = 1
                if beg < 0:
                    beg += dim_len
                if end < 0:
                    end += dim_len
                if beg < 0:
                    beg = 0
                if beg > dim_len:
                    beg = dim_len
                if end < 0:
                    end = 0
                if end > dim_len:
                    end = dim_len
                if beg == end:
                    beg, end, step = (0, 0, 1)
                elif beg >= dim_len and step > 0:
                    beg, end, step = (0, 0, 1)
                elif step > 0 and beg <= end:
                    pass
                elif step > 0 and beg > end:
                    beg, end, step = (0, 0, 1)
                elif step < 0 and index.start is None and index.stop is None:
                    beg, end, step = 0, dim_len, -step
                elif step < 0 and index.start is None:
                    beg, end, step = end + 1, dim_len, -step
                elif step < 0 and index.stop is None:
                    beg, end, step = 0, beg + 1, -step
                elif step < 0 and beg > end:
                    beg, end, step = end, beg, -step
                elif step < 0 and beg < end:
                    beg, end, step = 0, 0, -step
                slc_len = abs(divide(end - beg - 1, step) + 1)
                new_dims.append(slc_len)
            else:
                if index < 0:
                    index += dim_len
                if index >= 0 and index < dim_len:
                    pass
                else:
                    raise IndexError('Index out of range')
            dim += 1

        new_dims.extend(self.shape[dim:])
        if 0 in new_dims:
            raise IndexError('Zero length slices not currently supported')
        return dummy_array(new_dims, 1)

    def __repr__(self):
        val = str((self.name, str(self.shape)))
        return val


def unary(ary):
    return ary


def not_implemented(ary):
    return ary


unary_op = [
 arccos, arcsin, arctan, cos, cosh, sin, sinh, 
 exp, ceil, floor, fabs, 
 log, log10, sqrt]
unsupported = [
 argmin, argmax, argsort, around, absolute, sign, negative, floor]
for func in unary_op:
    func = unary

for func in unsupported:
    func = not_implemented

def reduction(ary, axis=0):
    if axis < 0:
        axis += len(ary.shape)
    if axis < 0 or axis >= len(ary.shape):
        raise ValueError('Dimension not in array')
    new_dims = list(ary.shape[:axis]) + list(ary.shape[axis + 1:])
    return dummy_array(new_dims, 1)


def take(ary, axis=0):
    raise NotImplemented