# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\Standalone\lsqr_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt.kernel.ooMisc import norm
from numpy import dot, asfarray, atleast_1d, zeros, ones, float64, where, inf, ndarray, flatnonzero
from openopt.kernel.baseSolver import baseSolver
from openopt.kernel.nonOptMisc import isspmatrix, scipyInstalled, scipyAbsentMsg, isPyPy
from lsqr import lsqr as LSQR
try:
    from scipy.sparse import csc_matrix, csr_matrix
except:
    pass

class lsqr(baseSolver):
    __name__ = 'lsqr'
    __license__ = 'GPL?'
    __authors__ = 'Michael P. Friedlander (University of British Columbia), Dominique Orban (Ecole Polytechnique de Montreal)'
    __alg__ = 'an iterative (conjugate-gradient-like) method'
    __info__ = "    \n    Parameters: atol (default 1e-9), btol (1e-9), conlim ('autoselect', default 1e8 for LLSP and 1e12 for SLE)\n    \n    For further information, see \n\n    1. C. C. Paige and M. A. Saunders (1982a).\n       LSQR: An algorithm for sparse linear equations and sparse least squares,\n       ACM TOMS 8(1), 43-71.\n    2. C. C. Paige and M. A. Saunders (1982b).\n       Algorithm 583.  LSQR: Sparse linear equations and least squares problems,\n       ACM TOMS 8(2), 195-209.\n    3. M. A. Saunders (1995).  Solution of sparse rectangular systems using\n       LSQR and CRAIG, BIT 35, 588-604."
    __optionalDataThatCanBeHandled__ = [
     'damp', 'X']
    _canHandleScipySparse = True
    atol = 1e-09
    btol = 1e-09
    conlim = 'autoselect'

    def __init__(self):
        pass

    def __solver__(self, p):
        condX = hasattr(p, 'X') and any(p.X)
        if condX:
            p.err("sorry, the solver can't handle non-zero X data yet, but you can easily handle it by yourself")
        C, d = p.C, p.d
        m, n = C.shape[0], p.n
        if scipyInstalled:
            if isspmatrix(C) or 0.25 * C.size > flatnonzero(C).size:
                C = csc_matrix(C)
        elif not isPyPy and 0.25 * C.size > flatnonzero(C).size:
            p.pWarn(scipyAbsentMsg)
        CT = C.T

        def aprod(mode, m, n, x):
            if mode == 1:
                if not isspmatrix(C):
                    r = dot(C, x).flatten() if 1 else C._mul_sparse_matrix(csr_matrix(x.reshape(x.size, 1))).A.flatten()
                    return r
                if mode == 2:
                    return isspmatrix(C) or dot(CT, x).flatten()
                return CT._mul_sparse_matrix(csr_matrix(x.reshape(x.size, 1))).A.flatten()

        if self.conlim == 'autoselect':
            conlim = 1000000000000.0 if m == n else 100000000.0
        damp = self.damp if hasattr(self, 'damp') and self.damp is not None else 0
        show = False
        x, istop, itn, r1norm, r2norm, anorm, acond, arnorm, xnorm, var = LSQR(m, n, aprod, d, damp, 1e-09, 1e-09, conlim, p.maxIter, show, wantvar=False, callback=p.iterfcn)
        p.istop = 1000
        p.debugmsg('lsqr iterations elapsed: %d' % itn)
        p.xf = x
        return