# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\sparse\linalg\isolve\lgmres.pyc
# Compiled at: 2013-02-16 13:27:32
from __future__ import division, print_function, absolute_import
import numpy as np
from scipy.lib.six.moves import xrange
from scipy.linalg import get_blas_funcs
from .utils import make_system
__all__ = [
 'lgmres']

def norm2(q):
    q = np.asarray(q)
    nrm2 = get_blas_funcs('nrm2', dtype=q.dtype)
    return nrm2(q)


def lgmres(A, b, x0=None, tol=1e-05, maxiter=1000, M=None, callback=None, inner_m=30, outer_k=3, outer_v=None, store_outer_Av=True):
    """
    Solve a matrix equation using the LGMRES algorithm.

    The LGMRES algorithm [BJM]_ [BPh]_ is designed to avoid some problems
    in the convergence in restarted GMRES, and often converges in fewer
    iterations.

    Parameters
    ----------
    A : {sparse matrix, dense matrix, LinearOperator}
        The real or complex N-by-N matrix of the linear system.
    b : {array, matrix}
        Right hand side of the linear system. Has shape (N,) or (N,1).
    x0  : {array, matrix}
        Starting guess for the solution.
    tol : float
        Tolerance to achieve. The algorithm terminates when either the relative
        or the absolute residual is below `tol`.
    maxiter : int
        Maximum number of iterations.  Iteration will stop after maxiter
        steps even if the specified tolerance has not been achieved.
    M : {sparse matrix, dense matrix, LinearOperator}
        Preconditioner for A.  The preconditioner should approximate the
        inverse of A.  Effective preconditioning dramatically improves the
        rate of convergence, which implies that fewer iterations are needed
        to reach a given error tolerance.
    callback : function
        User-supplied function to call after each iteration.  It is called
        as callback(xk), where xk is the current solution vector.
    inner_m : int, optional
        Number of inner GMRES iterations per each outer iteration.
    outer_k : int, optional
        Number of vectors to carry between inner GMRES iterations.
        According to [BJM]_, good values are in the range of 1...3.
        However, note that if you want to use the additional vectors to
        accelerate solving multiple similar problems, larger values may
        be beneficial.
    outer_v : list of tuples, optional
        List containing tuples ``(v, Av)`` of vectors and corresponding
        matrix-vector products, used to augment the Krylov subspace, and
        carried between inner GMRES iterations. The element ``Av`` can
        be `None` if the matrix-vector product should be re-evaluated.
        This parameter is modified in-place by `lgmres`, and can be used
        to pass "guess" vectors in and out of the algorithm when solving
        similar problems.
    store_outer_Av : bool, optional
        Whether LGMRES should store also A*v in addition to vectors `v`
        in the `outer_v` list. Default is True.

    Returns
    -------
    x : array or matrix
        The converged solution.
    info : int
        Provides convergence information:

            - 0  : successful exit
            - >0 : convergence to tolerance not achieved, number of iterations
            - <0 : illegal input or breakdown

    Notes
    -----
    The LGMRES algorithm [BJM]_ [BPh]_ is designed to avoid the
    slowing of convergence in restarted GMRES, due to alternating
    residual vectors. Typically, it often outperforms GMRES(m) of
    comparable memory requirements by some measure, or at least is not
    much worse.

    Another advantage in this algorithm is that you can supply it with
    'guess' vectors in the `outer_v` argument that augment the Krylov
    subspace. If the solution lies close to the span of these vectors,
    the algorithm converges faster. This can be useful if several very
    similar matrices need to be inverted one after another, such as in
    Newton-Krylov iteration where the Jacobian matrix often changes
    little in the nonlinear steps.

    References
    ----------
    .. [BJM] A.H. Baker and E.R. Jessup and T. Manteuffel,
             SIAM J. Matrix Anal. Appl. 26, 962 (2005).
    .. [BPh] A.H. Baker, PhD thesis, University of Colorado (2003).
             http://amath.colorado.edu/activities/thesis/allisonb/Thesis.ps

    """
    from scipy.linalg.basic import lstsq
    A, M, x, b, postprocess = make_system(A, M, x0, b)
    if not np.isfinite(b).all():
        raise ValueError('RHS must contain only finite numbers')
    matvec = A.matvec
    psolve = M.matvec
    if outer_v is None:
        outer_v = []
    axpy, dot, scal = (None, None, None)
    b_norm = norm2(b)
    if b_norm == 0:
        b_norm = 1
    for k_outer in xrange(maxiter):
        r_outer = matvec(x) - b
        if callback is not None:
            callback(x)
        if axpy is None:
            if np.iscomplexobj(r_outer) and not np.iscomplexobj(x):
                x = x.astype(r_outer.dtype)
            axpy, dot, scal = get_blas_funcs(['axpy', 'dot', 'scal'], (
             x, r_outer))
        r_norm = norm2(r_outer)
        if r_norm < tol * b_norm or r_norm < tol:
            break
        vs0 = -psolve(r_outer)
        inner_res_0 = norm2(vs0)
        if inner_res_0 == 0:
            rnorm = norm2(r_outer)
            raise RuntimeError('Preconditioner returned a zero vector; |v| ~ %.1g, |M v| = 0' % rnorm)
        vs0 = scal(1.0 / inner_res_0, vs0)
        hs = []
        vs = [vs0]
        ws = []
        y = None
        for j in xrange(1, 1 + inner_m + len(outer_v)):
            v_new = None
            if j < len(outer_v) + 1:
                z, v_new = outer_v[j - 1]
            elif j == len(outer_v) + 1:
                z = vs0
            else:
                z = vs[-1]
            if v_new is None:
                v_new = psolve(matvec(z))
            else:
                v_new = v_new.copy()
            hcur = []
            for v in vs:
                alpha = dot(v, v_new)
                hcur.append(alpha)
                v_new = axpy(v, v_new, v.shape[0], -alpha)

            hcur.append(norm2(v_new))
            if hcur[-1] == 0:
                bailout = True
            else:
                bailout = False
                v_new = scal(1.0 / hcur[-1], v_new)
            vs.append(v_new)
            hs.append(hcur)
            ws.append(z)
            if not bailout and j % 5 != 1 and j < inner_m + len(outer_v) - 1:
                continue
            hess = np.zeros((j + 1, j), x.dtype)
            e1 = np.zeros((j + 1,), x.dtype)
            e1[0] = inner_res_0
            for q in xrange(j):
                hess[:q + 2, q] = hs[q]

            y, resids, rank, s = lstsq(hess, e1)
            inner_res = norm2(np.dot(hess, y) - e1)
            if inner_res < tol * inner_res_0:
                break

        dx = ws[0] * y[0]
        for w, yc in zip(ws[1:], y[1:]):
            dx = axpy(w, dx, dx.shape[0], yc)

        nx = norm2(dx)
        if store_outer_Av:
            q = np.dot(hess, y)
            ax = vs[0] * q[0]
            for v, qc in zip(vs[1:], q[1:]):
                ax = axpy(v, ax, ax.shape[0], qc)

            outer_v.append((dx / nx, ax / nx))
        else:
            outer_v.append((dx / nx, None))
        while len(outer_v) > outer_k:
            del outer_v[0]

        x += dx
    else:
        return (
         postprocess(x), maxiter)

    return (postprocess(x), 0)