# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\optimize\nnls.pyc
# Compiled at: 2013-02-16 13:27:30
from __future__ import division, print_function, absolute_import
from . import _nnls
from numpy import asarray_chkfinite, zeros, double
__all__ = [
 'nnls']

def nnls(A, b):
    """
    Solve ``argmin_x || Ax - b ||_2`` for ``x>=0``. This is a wrapper
    for a FORTAN non-negative least squares solver.

    Parameters
    ----------
    A : ndarray
        Matrix ``A`` as shown above.
    b : ndarray
        Right-hand side vector.

    Returns
    -------
    x : ndarray
        Solution vector.
    rnorm : float
        The residual, ``|| Ax-b ||_2``.

    Notes
    -----
    The FORTRAN code was published in the book below. The algorithm
    is an active set method. It solves the KKT (Karush-Kuhn-Tucker)
    conditions for the non-negative least squares problem.

    References
    ----------
    Lawson C., Hanson R.J., (1987) Solving Least Squares Problems, SIAM

    """
    A, b = map(asarray_chkfinite, (A, b))
    if len(A.shape) != 2:
        raise ValueError('expected matrix')
    if len(b.shape) != 1:
        raise ValueError('expected vector')
    m, n = A.shape
    if m != b.shape[0]:
        raise ValueError('incompatible dimensions')
    w = zeros((n,), dtype=double)
    zz = zeros((m,), dtype=double)
    index = zeros((n,), dtype=int)
    x, rnorm, mode = _nnls.nnls(A, m, n, b, w, zz, index)
    if mode != 1:
        raise RuntimeError('too many iterations')
    return (x, rnorm)