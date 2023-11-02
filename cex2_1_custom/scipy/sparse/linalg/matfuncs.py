# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\sparse\linalg\matfuncs.pyc
# Compiled at: 2013-02-16 13:27:32
"""
Sparse matrix functions
"""
from __future__ import division, print_function, absolute_import
__all__ = [
 'expm', 'inv']
from numpy import asarray, dot, eye, ceil, log2
from numpy import matrix as mat
import numpy as np
from scipy.linalg.misc import norm
from scipy.linalg.basic import solve, inv
from scipy.sparse.base import isspmatrix
from scipy.sparse.construct import eye as speye
from scipy.sparse.linalg import spsolve

def inv(A):
    """
    Compute the inverse of a sparse matrix

    .. versionadded:: 0.12.0

    Parameters
    ----------
    A : (M,M) ndarray or sparse matrix
        square matrix to be inverted

    Returns
    -------
    Ainv : (M,M) ndarray or sparse matrix
        inverse of `A`

    Notes
    -----
    This computes the sparse inverse of `A`.  If the inverse of `A` is expected
    to be non-sparse, it will likely be faster to convert `A` to dense and use
    scipy.linalg.inv.

    """
    I = speye(A.shape[0], A.shape[1], dtype=A.dtype, format=A.format)
    Ainv = spsolve(A, I)
    return Ainv


def expm(A):
    """
    Compute the matrix exponential using Pade approximation.

    .. versionadded:: 0.12.0

    Parameters
    ----------
    A : (M,M) array or sparse matrix
        2D Array or Matrix (sparse or dense) to be exponentiated

    Returns
    -------
    expA : (M,M) ndarray
        Matrix exponential of `A`

    References
    ----------
    N. J. Higham,
    "The Scaling and Squaring Method for the Matrix Exponential Revisited",
    SIAM. J. Matrix Anal. & Appl. 26, 1179 (2005).

    """
    n_squarings = 0
    Aissparse = isspmatrix(A)
    if Aissparse:
        A_L1 = max(abs(A).sum(axis=0).flat)
        ident = speye(A.shape[0], A.shape[1], dtype=A.dtype, format=A.format)
    else:
        A = asarray(A)
        A_L1 = norm(A, 1)
        ident = eye(A.shape[0], A.shape[1], dtype=A.dtype)
    if A.dtype == 'float64' or A.dtype == 'complex128':
        if A_L1 < 0.01495585217958292:
            U, V = _pade3(A, ident)
        elif A_L1 < 0.253939833006323:
            U, V = _pade5(A, ident)
        elif A_L1 < 0.9504178996162932:
            U, V = _pade7(A, ident)
        elif A_L1 < 2.097847961257068:
            U, V = _pade9(A, ident)
        else:
            maxnorm = 5.371920351148152
            n_squarings = max(0, int(ceil(log2(A_L1 / maxnorm))))
            A = A / 2 ** n_squarings
            U, V = _pade13(A, ident)
    else:
        if A.dtype == 'float32' or A.dtype == 'complex64':
            if A_L1 < 0.4258730016922831:
                U, V = _pade3(A, ident)
            elif A_L1 < 1.880152677804762:
                U, V = _pade5(A, ident)
            else:
                maxnorm = 3.92572478313866
                n_squarings = max(0, int(ceil(log2(A_L1 / maxnorm))))
                A = A / 2 ** n_squarings
                U, V = _pade7(A, ident)
        else:
            raise ValueError('invalid type: ' + str(A.dtype))
        P = U + V
        Q = -U + V
        if Aissparse:
            from scipy.sparse.linalg import spsolve
            R = spsolve(Q, P)
        else:
            R = solve(Q, P)
        for i in range(n_squarings):
            R = R.dot(R)

    return R


def _pade3(A, ident):
    b = (120.0, 60.0, 12.0, 1.0)
    A2 = A.dot(A)
    U = A.dot(b[3] * A2 + b[1] * ident)
    V = b[2] * A2 + b[0] * ident
    return (U, V)


def _pade5(A, ident):
    b = (30240.0, 15120.0, 3360.0, 420.0, 30.0, 1.0)
    A2 = A.dot(A)
    A4 = A2.dot(A2)
    U = A.dot(b[5] * A4 + b[3] * A2 + b[1] * ident)
    V = b[4] * A4 + b[2] * A2 + b[0] * ident
    return (U, V)


def _pade7(A, ident):
    b = (17297280.0, 8648640.0, 1995840.0, 277200.0, 25200.0, 1512.0, 56.0, 1.0)
    A2 = A.dot(A)
    A4 = A2.dot(A2)
    A6 = A4.dot(A2)
    U = A.dot(b[7] * A6 + b[5] * A4 + b[3] * A2 + b[1] * ident)
    V = b[6] * A6 + b[4] * A4 + b[2] * A2 + b[0] * ident
    return (U, V)


def _pade9(A, ident):
    b = (17643225600.0, 8821612800.0, 2075673600.0, 302702400.0, 30270240.0, 2162160.0,
         110880.0, 3960.0, 90.0, 1.0)
    A2 = A.dot(A)
    A4 = A2.dot(A2)
    A6 = A4.dot(A2)
    A8 = A6.dot(A2)
    U = A.dot(b[9] * A8 + b[7] * A6 + b[5] * A4 + b[3] * A2 + b[1] * ident)
    V = b[8] * A8 + b[6] * A6 + b[4] * A4 + b[2] * A2 + b[0] * ident
    return (U, V)


def _pade13(A, ident):
    b = (6.476475253248e+16, 3.238237626624e+16, 7771770303897600.0, 1187353796428800.0,
         129060195264000.0, 10559470521600.0, 670442572800.0, 33522128640.0, 1323241920.0,
         40840800.0, 960960.0, 16380.0, 182.0, 1.0)
    A2 = A.dot(A)
    A4 = A2.dot(A2)
    A6 = A4.dot(A2)
    U = A.dot(A6.dot(b[13] * A6 + b[11] * A4 + b[9] * A2) + b[7] * A6 + b[5] * A4 + b[3] * A2 + b[1] * ident)
    V = A6.dot(b[12] * A6 + b[10] * A4 + b[8] * A2) + b[6] * A6 + b[4] * A4 + b[2] * A2 + b[0] * ident
    return (U, V)