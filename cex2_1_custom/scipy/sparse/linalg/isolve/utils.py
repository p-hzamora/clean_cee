# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\sparse\linalg\isolve\utils.pyc
# Compiled at: 2013-02-16 13:27:32
from __future__ import division, print_function, absolute_import
__docformat__ = 'restructuredtext en'
__all__ = []
from warnings import warn
from numpy import asanyarray, asarray, asmatrix, array, matrix, zeros
from scipy.sparse.linalg.interface import aslinearoperator, LinearOperator, IdentityOperator
_coerce_rules = {('f', 'f'): 'f', ('f', 'd'): 'd', ('f', 'F'): 'F', ('f', 'D'): 'D', 
   ('d', 'f'): 'd', ('d', 'd'): 'd', ('d', 'F'): 'D', 
   ('d', 'D'): 'D', ('F', 'f'): 'F', ('F', 'd'): 'D', 
   ('F', 'F'): 'F', ('F', 'D'): 'D', ('D', 'f'): 'D', 
   ('D', 'd'): 'D', ('D', 'F'): 'D', ('D', 'D'): 'D'}

def coerce(x, y):
    if x not in 'fdFD':
        x = 'd'
    if y not in 'fdFD':
        y = 'd'
    return _coerce_rules[(x, y)]


def id(x):
    return x


def make_system(A, M, x0, b, xtype=None):
    """Make a linear system Ax=b

    Parameters
    ----------
    A : LinearOperator
        sparse or dense matrix (or any valid input to aslinearoperator)
    M : {LinearOperator, Nones}
        preconditioner
        sparse or dense matrix (or any valid input to aslinearoperator)
    x0 : {array_like, None}
        initial guess to iterative method
    b : array_like
        right hand side
    xtype : {'f', 'd', 'F', 'D', None}
        dtype of the x vector

    Returns
    -------
    (A, M, x, b, postprocess)
        A : LinearOperator
            matrix of the linear system
        M : LinearOperator
            preconditioner
        x : rank 1 ndarray
            initial guess
        b : rank 1 ndarray
            right hand side
        postprocess : function
            converts the solution vector to the appropriate
            type and dimensions (e.g. (N,1) matrix)

    """
    A_ = A
    A = aslinearoperator(A)
    if A.shape[0] != A.shape[1]:
        raise ValueError('expected square matrix, but got shape=%s' % (A.shape,))
    N = A.shape[0]
    b = asanyarray(b)
    if not (b.shape == (N, 1) or b.shape == (N,)):
        raise ValueError('A and b have incompatible dimensions')
    if b.dtype.char not in 'fdFD':
        b = b.astype('d')

    def postprocess(x):
        if isinstance(b, matrix):
            x = asmatrix(x)
        return x.reshape(b.shape)

    if xtype is None:
        if hasattr(A, 'dtype'):
            xtype = A.dtype.char
        else:
            xtype = A.matvec(b).dtype.char
        xtype = coerce(xtype, b.dtype.char)
    else:
        warn('Use of xtype argument is deprecated. Use LinearOperator( ... , dtype=xtype) instead.', DeprecationWarning)
        if xtype == 0:
            xtype = b.dtype.char
        elif xtype not in 'fdFD':
            raise ValueError("xtype must be 'f', 'd', 'F', or 'D'")
    b = asarray(b, dtype=xtype)
    b = b.ravel()
    if x0 is None:
        x = zeros(N, dtype=xtype)
    else:
        x = array(x0, dtype=xtype)
        if not (x.shape == (N, 1) or x.shape == (N,)):
            raise ValueError('A and x have incompatible dimensions')
        x = x.ravel()
    if M is None:
        if hasattr(A_, 'psolve'):
            psolve = A_.psolve
        else:
            psolve = id
        if hasattr(A_, 'rpsolve'):
            rpsolve = A_.rpsolve
        else:
            rpsolve = id
        if psolve is id and rpsolve is id:
            M = IdentityOperator(shape=A.shape, dtype=A.dtype)
        else:
            M = LinearOperator(A.shape, matvec=psolve, rmatvec=rpsolve, dtype=A.dtype)
    else:
        M = aslinearoperator(M)
        if A.shape != M.shape:
            raise ValueError('matrix and preconditioner have different shapes')
    return (
     A, M, x, b, postprocess)