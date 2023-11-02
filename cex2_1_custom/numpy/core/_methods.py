# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\core\_methods.pyc
# Compiled at: 2013-04-07 07:04:04
from numpy.core import multiarray as mu
from numpy.core import umath as um
from numpy.core.numeric import asanyarray

def _amax(a, axis=None, out=None, keepdims=False):
    return um.maximum.reduce(a, axis=axis, out=out, keepdims=keepdims)


def _amin(a, axis=None, out=None, keepdims=False):
    return um.minimum.reduce(a, axis=axis, out=out, keepdims=keepdims)


def _sum(a, axis=None, dtype=None, out=None, keepdims=False):
    return um.add.reduce(a, axis=axis, dtype=dtype, out=out, keepdims=keepdims)


def _prod(a, axis=None, dtype=None, out=None, keepdims=False):
    return um.multiply.reduce(a, axis=axis, dtype=dtype, out=out, keepdims=keepdims)


def _any(a, axis=None, dtype=None, out=None, keepdims=False):
    return um.logical_or.reduce(a, axis=axis, dtype=dtype, out=out, keepdims=keepdims)


def _all(a, axis=None, dtype=None, out=None, keepdims=False):
    return um.logical_and.reduce(a, axis=axis, dtype=dtype, out=out, keepdims=keepdims)


def _count_reduce_items(arr, axis):
    if axis is None:
        axis = tuple(xrange(arr.ndim))
    if not isinstance(axis, tuple):
        axis = (
         axis,)
    items = 1
    for ax in axis:
        items *= arr.shape[ax]

    return items


def _mean(a, axis=None, dtype=None, out=None, keepdims=False):
    arr = asanyarray(a)
    if dtype is None and arr.dtype.kind in ('b', 'u', 'i'):
        ret = um.add.reduce(arr, axis=axis, dtype='f8', out=out, keepdims=keepdims)
    else:
        ret = um.add.reduce(arr, axis=axis, dtype=dtype, out=out, keepdims=keepdims)
    rcount = _count_reduce_items(arr, axis)
    if isinstance(ret, mu.ndarray):
        ret = um.true_divide(ret, rcount, out=ret, casting='unsafe', subok=False)
    else:
        ret = ret / float(rcount)
    return ret


def _var(a, axis=None, dtype=None, out=None, ddof=0, keepdims=False):
    arr = asanyarray(a)
    if dtype is None and arr.dtype.kind in ('b', 'u', 'i'):
        arrmean = um.add.reduce(arr, axis=axis, dtype='f8', keepdims=True)
    else:
        arrmean = um.add.reduce(arr, axis=axis, dtype=dtype, keepdims=True)
    rcount = _count_reduce_items(arr, axis)
    if isinstance(arrmean, mu.ndarray):
        arrmean = um.true_divide(arrmean, rcount, out=arrmean, casting='unsafe', subok=False)
    else:
        arrmean = arrmean / float(rcount)
    x = arr - arrmean
    if arr.dtype.kind == 'c':
        x = um.multiply(x, um.conjugate(x), out=x).real
    else:
        x = um.multiply(x, x, out=x)
    ret = um.add.reduce(x, axis=axis, dtype=dtype, out=out, keepdims=keepdims)
    if not keepdims and isinstance(rcount, mu.ndarray):
        rcount = rcount.squeeze(axis=axis)
    rcount -= ddof
    if isinstance(ret, mu.ndarray):
        ret = um.true_divide(ret, rcount, out=ret, casting='unsafe', subok=False)
    else:
        ret = ret / float(rcount)
    return ret


def _std(a, axis=None, dtype=None, out=None, ddof=0, keepdims=False):
    ret = _var(a, axis=axis, dtype=dtype, out=out, ddof=ddof, keepdims=keepdims)
    if isinstance(ret, mu.ndarray):
        ret = um.sqrt(ret, out=ret)
    else:
        ret = um.sqrt(ret)
    return ret