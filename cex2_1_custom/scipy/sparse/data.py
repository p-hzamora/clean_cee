# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\sparse\data.pyc
# Compiled at: 2013-02-16 13:27:32
"""Base class for sparse matrice with a .data attribute

    subclasses must provide a _with_data() method that
    creates a new matrix with the same sparsity pattern
    as self but with a different data array

"""
from __future__ import division, print_function, absolute_import
__all__ = []
import numpy as np
from .base import spmatrix
from .sputils import isscalarlike

class _data_matrix(spmatrix):

    def __init__(self):
        spmatrix.__init__(self)

    def _get_dtype(self):
        return self.data.dtype

    def _set_dtype(self, newtype):
        self.data.dtype = newtype

    dtype = property(fget=_get_dtype, fset=_set_dtype)

    def __abs__(self):
        return self._with_data(abs(self.data))

    def _real(self):
        return self._with_data(self.data.real)

    def _imag(self):
        return self._with_data(self.data.imag)

    def __neg__(self):
        return self._with_data(-self.data)

    def __imul__(self, other):
        if isscalarlike(other):
            self.data *= other
            return self
        raise NotImplementedError

    def __itruediv__(self, other):
        if isscalarlike(other):
            recip = 1.0 / other
            self.data *= recip
            return self
        raise NotImplementedError

    def astype(self, t):
        return self._with_data(self.data.astype(t))

    def conj(self):
        return self._with_data(self.data.conj())

    def copy(self):
        return self._with_data(self.data.copy(), copy=True)

    def _mul_scalar(self, other):
        return self._with_data(self.data * other)


for npfunc in [np.sin, np.tan, np.arcsin, np.arctan, np.sinh, np.tanh,
 np.arcsinh, np.arctanh, np.rint, np.sign, np.expm1, np.log1p,
 np.deg2rad, np.rad2deg, np.floor, np.ceil, np.trunc]:
    name = npfunc.__name__

    def _create_method(op):

        def method(self):
            result = op(self.data)
            x = self._with_data(result, copy=True)
            return x

        method.__doc__ = 'Element-wise %s.\n\nSee numpy.%s for more information.' % (
         name, name)
        method.__name__ = name
        return method


    setattr(_data_matrix, name, _create_method(npfunc))