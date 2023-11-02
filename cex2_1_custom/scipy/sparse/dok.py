# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\sparse\dok.pyc
# Compiled at: 2013-02-16 13:27:32
"""Dictionary Of Keys based matrix"""
from __future__ import division, print_function, absolute_import
__docformat__ = 'restructuredtext en'
__all__ = [
 'dok_matrix', 'isspmatrix_dok']
import numpy as np
from scipy.lib.six.moves import zip as izip, xrange
from scipy.lib.six import iteritems
from .base import spmatrix, isspmatrix
from .sputils import isdense, getdtype, isshape, isintlike, isscalarlike, upcast
try:
    from operator import isSequenceType as _is_sequence
except ImportError:

    def _is_sequence(x):
        return hasattr(x, '__len__') or hasattr(x, '__next__') or hasattr(x, 'next')


class dok_matrix(spmatrix, dict):
    """
    Dictionary Of Keys based sparse matrix.

    This is an efficient structure for constructing sparse
    matrices incrementally.

    This can be instantiated in several ways:
        dok_matrix(D)
            with a dense matrix, D

        dok_matrix(S)
            with a sparse matrix, S

        dok_matrix((M,N), [dtype])
            create the matrix with initial shape (M,N)
            dtype is optional, defaulting to dtype='d'

    Attributes
    ----------
    dtype : dtype
        Data type of the matrix
    shape : 2-tuple
        Shape of the matrix
    ndim : int
        Number of dimensions (this is always 2)
    nnz
        Number of nonzero elements

    Notes
    -----

    Sparse matrices can be used in arithmetic operations: they support
    addition, subtraction, multiplication, division, and matrix power.

    Allows for efficient O(1) access of individual elements.
    Duplicates are not allowed.
    Can be efficiently converted to a coo_matrix once constructed.

    Examples
    --------
    >>> from scipy.sparse import *
    >>> from scipy import *
    >>> S = dok_matrix((5,5), dtype=float32)
    >>> for i in range(5):
    >>>     for j in range(5):
    >>>         S[i,j] = i+j # Update element

    """

    def __init__(self, arg1, shape=None, dtype=None, copy=False):
        dict.__init__(self)
        spmatrix.__init__(self)
        self.dtype = getdtype(dtype, default=float)
        if isinstance(arg1, tuple) and isshape(arg1):
            M, N = arg1
            self.shape = (M, N)
        elif isspmatrix(arg1):
            if isspmatrix_dok(arg1) and copy:
                arg1 = arg1.copy()
            else:
                arg1 = arg1.todok()
            if dtype is not None:
                arg1 = arg1.astype(dtype)
            self.update(arg1)
            self.shape = arg1.shape
            self.dtype = arg1.dtype
        else:
            try:
                arg1 = np.asarray(arg1)
            except:
                raise TypeError('invalid input format')

            if len(arg1.shape) != 2:
                raise TypeError('expected rank <=2 dense array or matrix')
            from .coo import coo_matrix
            self.update(coo_matrix(arg1, dtype=dtype).todok())
            self.shape = arg1.shape
            self.dtype = arg1.dtype
        return

    def getnnz(self):
        return dict.__len__(self)

    nnz = property(fget=getnnz)

    def __len__(self):
        return dict.__len__(self)

    def get(self, key, default=0.0):
        """This overrides the dict.get method, providing type checking
        but otherwise equivalent functionality.
        """
        try:
            i, j = key
            assert isintlike(i) and isintlike(j)
        except (AssertionError, TypeError, ValueError):
            raise IndexError('index must be a pair of integers')

        if i < 0 or i >= self.shape[0] or j < 0 or j >= self.shape[1]:
            raise IndexError('index out of bounds')
        return dict.get(self, key, default)

    def __getitem__(self, key):
        """If key=(i,j) is a pair of integers, return the corresponding
        element.  If either i or j is a slice or sequence, return a new sparse
        matrix with just these elements.
        """
        try:
            i, j = key
        except (ValueError, TypeError):
            raise TypeError('index must be a pair of integers or slices')

        if isintlike(i):
            if i < 0:
                i += self.shape[0]
            if i < 0 or i >= self.shape[0]:
                raise IndexError('index out of bounds')
        if isintlike(j):
            if j < 0:
                j += self.shape[1]
            if j < 0 or j >= self.shape[1]:
                raise IndexError('index out of bounds')
        if isintlike(i) and isintlike(j):
            return dict.get(self, (i, j), 0.0)
        else:
            if isinstance(i, slice):
                seq = xrange(i.start or 0, i.stop or self.shape[0], i.step or 1)
            else:
                if _is_sequence(i):
                    seq = i
                else:
                    if not isintlike(i):
                        raise TypeError('index must be a pair of integers or slices')
                    seq = None
                if seq is not None:
                    if isintlike(j):
                        first = seq[0]
                        last = seq[-1]
                        if first < 0 or first >= self.shape[0] or last < 0 or last >= self.shape[0]:
                            raise IndexError('index out of bounds')
                        newshape = (
                         last - first + 1, 1)
                        new = dok_matrix(newshape)
                        for ii, jj in self.keys():
                            if jj == j and ii >= first and ii <= last:
                                dict.__setitem__(new, (ii - first, 0), dict.__getitem__(self, (ii, jj)))

                    else:
                        raise NotImplementedError('fancy indexing supported over one axis only')
                    return new
                if isinstance(j, slice):
                    seq = xrange(j.start or 0, j.stop or self.shape[1], j.step or 1)
                elif _is_sequence(j):
                    seq = j
                else:
                    raise TypeError('index must be a pair of integers or slices')
                first = seq[0]
                last = seq[-1]
                if first < 0 or first >= self.shape[1] or last < 0 or last >= self.shape[1]:
                    raise IndexError('index out of bounds')
                newshape = (
                 1, last - first + 1)
                new = dok_matrix(newshape)
                for ii, jj in self.keys():
                    if ii == i and jj >= first and jj <= last:
                        dict.__setitem__(new, (0, jj - first), dict.__getitem__(self, (ii, jj)))

            return new
            return

    def __setitem__(self, key, value):
        try:
            i, j = key
        except (ValueError, TypeError):
            raise TypeError('index must be a pair of integers or slices')

        if isintlike(i) and isintlike(j):
            if i < 0:
                i += self.shape[0]
            if j < 0:
                j += self.shape[1]
            if i < 0 or i >= self.shape[0] or j < 0 or j >= self.shape[1]:
                raise IndexError('index out of bounds')
            if np.isscalar(value):
                if value == 0:
                    if (
                     i, j) in self:
                        del self[(i, j)]
                else:
                    dict.__setitem__(self, (i, j), self.dtype.type(value))
            else:
                raise ValueError('setting an array element with a sequence')
        else:
            if isinstance(i, slice):
                seq = xrange(i.start or 0, i.stop or self.shape[0], i.step or 1)
            else:
                if _is_sequence(i):
                    seq = i
                else:
                    if not isintlike(i):
                        raise TypeError('index must be a pair of integers or slices')
                    seq = None
                if seq is not None:
                    if isinstance(value, dok_matrix):
                        if value.shape[1] == 1:
                            for element in seq:
                                self[(element, j)] = value[(element, 0)]

                        else:
                            raise NotImplementedError('setting a 2-d slice of a dok_matrix is not yet supported')
                    elif np.isscalar(value):
                        for element in seq:
                            self[(element, j)] = value

                    else:
                        try:
                            if len(seq) != len(value):
                                raise ValueError('index and value ranges must have the same length')
                        except TypeError:
                            raise TypeError('unsupported type for dok_matrix.__setitem__')

                        for element, val in izip(seq, value):
                            self[(element, j)] = val

                else:
                    if isinstance(j, slice):
                        seq = xrange(j.start or 0, j.stop or self.shape[1], j.step or 1)
                    else:
                        if _is_sequence(j):
                            seq = j
                        else:
                            raise TypeError('index must be a pair of integers or slices')
                        if isinstance(value, dok_matrix):
                            if value.shape[0] == 1:
                                for element in seq:
                                    self[(i, element)] = value[(0, element)]

                            else:
                                raise NotImplementedError('setting a 2-d slice of a dok_matrix is not yet supported')
                        elif np.isscalar(value):
                            for element in seq:
                                self[(i, element)] = value

                        else:
                            try:
                                if len(seq) != len(value):
                                    raise ValueError('index and value ranges must have the same length')
                            except TypeError:
                                raise TypeError('unsupported type for dok_matrix.__setitem__')

                            for element, val in izip(seq, value):
                                self[(i, element)] = val

        return

    def __add__(self, other):
        if isscalarlike(other):
            new = dok_matrix(self.shape, dtype=self.dtype)
            M, N = self.shape
            for i in xrange(M):
                for j in xrange(N):
                    aij = self.get((i, j), 0) + other
                    if aij != 0:
                        new[(i, j)] = aij

        elif isinstance(other, dok_matrix):
            if other.shape != self.shape:
                raise ValueError('matrix dimensions are not equal')
            new = dok_matrix(self.shape, dtype=self.dtype)
            new.update(self)
            for key in other.keys():
                new[key] += other[key]

        elif isspmatrix(other):
            csc = self.tocsc()
            new = csc + other
        elif isdense(other):
            new = self.todense() + other
        else:
            raise TypeError('data type not understood')
        return new

    def __radd__(self, other):
        if isscalarlike(other):
            new = dok_matrix(self.shape, dtype=self.dtype)
            M, N = self.shape
            for i in xrange(M):
                for j in xrange(N):
                    aij = self.get((i, j), 0) + other
                    if aij != 0:
                        new[(i, j)] = aij

        elif isinstance(other, dok_matrix):
            if other.shape != self.shape:
                raise ValueError('matrix dimensions are not equal')
            new = dok_matrix(self.shape, dtype=self.dtype)
            new.update(self)
            for key in other:
                new[key] += other[key]

        elif isspmatrix(other):
            csc = self.tocsc()
            new = csc + other
        elif isdense(other):
            new = other + self.todense()
        else:
            raise TypeError('data type not understood')
        return new

    def __neg__(self):
        new = dok_matrix(self.shape, dtype=self.dtype)
        for key in self.keys():
            new[key] = -self[key]

        return new

    def _mul_scalar(self, other):
        new = dok_matrix(self.shape, dtype=self.dtype)
        for key, val in iteritems(self):
            new[key] = val * other

        return new

    def _mul_vector(self, other):
        result = np.zeros(self.shape[0], dtype=upcast(self.dtype, other.dtype))
        for (i, j), v in iteritems(self):
            result[i] += v * other[j]

        return result

    def _mul_multivector(self, other):
        M, N = self.shape
        n_vecs = other.shape[1]
        result = np.zeros((M, n_vecs), dtype=upcast(self.dtype, other.dtype))
        for (i, j), v in iteritems(self):
            result[i, :] += v * other[j, :]

        return result

    def __imul__(self, other):
        if isscalarlike(other):
            for key, val in iteritems(self):
                self[key] = val * other

            return self
        return NotImplementedError

    def __truediv__(self, other):
        if isscalarlike(other):
            new = dok_matrix(self.shape, dtype=self.dtype)
            for key, val in iteritems(self):
                new[key] = val / other

            return new
        return self.tocsr() / other

    def __itruediv__(self, other):
        if isscalarlike(other):
            for key, val in iteritems(self):
                self[key] = val / other

            return self
        return NotImplementedError

    def transpose(self):
        """ Return the transpose
        """
        M, N = self.shape
        new = dok_matrix((N, M), dtype=self.dtype)
        for key, value in iteritems(self):
            new[(key[1], key[0])] = value

        return new

    def conjtransp(self):
        """ Return the conjugate transpose
        """
        M, N = self.shape
        new = dok_matrix((N, M), dtype=self.dtype)
        for key, value in iteritems(self):
            new[(key[1], key[0])] = np.conj(value)

        return new

    def copy(self):
        new = dok_matrix(self.shape, dtype=self.dtype)
        new.update(self)
        return new

    def take(self, cols_or_rows, columns=1):
        new = dok_matrix(dtype=self.dtype)
        indx = int(columns == 1)
        N = len(cols_or_rows)
        if indx:
            for key in self.keys():
                num = np.searchsorted(cols_or_rows, key[1])
                if num < N:
                    newkey = (
                     key[0], num)
                    new[newkey] = self[key]

        else:
            for key in self.keys():
                num = np.searchsorted(cols_or_rows, key[0])
                if num < N:
                    newkey = (
                     num, key[1])
                    new[newkey] = self[key]

        return new

    def split(self, cols_or_rows, columns=1):
        base = dok_matrix()
        ext = dok_matrix()
        indx = int(columns == 1)
        if indx:
            for key in self.keys():
                num = np.searchsorted(cols_or_rows, key[1])
                if cols_or_rows[num] == key[1]:
                    newkey = (
                     key[0], num)
                    ext[newkey] = self[key]
                else:
                    newkey = (
                     key[0], key[1] - num)
                    base[newkey] = self[key]

        else:
            for key in self.keys():
                num = np.searchsorted(cols_or_rows, key[0])
                if cols_or_rows[num] == key[0]:
                    newkey = (
                     num, key[1])
                    ext[newkey] = self[key]
                else:
                    newkey = (
                     key[0] - num, key[1])
                    base[newkey] = self[key]

        return (
         base, ext)

    def tocoo(self):
        """ Return a copy of this matrix in COOrdinate format"""
        from .coo import coo_matrix
        if self.nnz == 0:
            return coo_matrix(self.shape, dtype=self.dtype)
        else:
            data = np.asarray(list(self.values()), dtype=self.dtype)
            indices = np.asarray(list(self.keys()), dtype=np.intc).T
            return coo_matrix((data, indices), shape=self.shape, dtype=self.dtype)

    def todok(self, copy=False):
        if copy:
            return self.copy()
        else:
            return self

    def tocsr(self):
        """ Return a copy of this matrix in Compressed Sparse Row format"""
        return self.tocoo().tocsr()

    def tocsc(self):
        """ Return a copy of this matrix in Compressed Sparse Column format"""
        return self.tocoo().tocsc()

    def toarray(self, order=None, out=None):
        """See the docstring for `spmatrix.toarray`."""
        return self.tocoo().toarray(order=order, out=out)

    def resize(self, shape):
        """ Resize the matrix in-place to dimensions given by 'shape'.

        Any non-zero elements that lie outside the new shape are removed.
        """
        if not isshape(shape):
            raise TypeError('dimensions must be a 2-tuple of positive integers')
        newM, newN = shape
        M, N = self.shape
        if newM < M or newN < N:
            for i, j in list(self.keys()):
                if i >= newM or j >= newN:
                    del self[(i, j)]

        self._shape = shape


def isspmatrix_dok(x):
    return isinstance(x, dok_matrix)