# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\Standalone\lsqr.pyc
# Compiled at: 2012-12-08 11:04:59
"""
Solve the least-squares problem

  minimize ||Ax-b||

using LSQR.  This is a line-by-line translation from Matlab code
available at http://www.stanford.edu/~saunders/lsqr.

Michael P. Friedlander, University of British Columbia
Dominique Orban, Ecole Polytechnique de Montreal
$Id$
"""
from numpy import zeros, dot
from openopt.kernel.ooMisc import norm
from math import sqrt

def normof2(x, y):
    return sqrt(x ** 2 + y ** 2)


def normof4(x1, x2, x3, x4):
    return sqrt(x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2)


def lsqr(m, n, aprod, b, damp, atol, btol, conlim, itnlim, show, wantvar=False, callback=(lambda x: None)):
    """
    [ x, istop, itn, r1norm, r2norm, anorm, acond, arnorm, xnorm, var ]...
    = lsqr( m, n, @aprod, b, damp, atol, btol, conlim, itnlim, show );
    
    LSQR solves  Ax = b  or  min ||b - Ax||_2  if damp = 0, or

       min || [ b ]  -  [   A    ] x ||   otherwise.
           || [ 0 ]     [ damp I ]   ||2

    A  is an m by n matrix defined by  y = aprod(mode, m, n, x),
    where aprod refers to a function that performs the matrix-vector operations.
    If mode = 1,   aprod  must return  y = Ax   without altering x.
    If mode = 2,   aprod  must return  y = A'x  without altering x.

    ----------------------------------------------------------------------
    LSQR uses an iterative (conjugate-gradient-like) method.

    For further information, see 

    1. C. C. Paige and M. A. Saunders (1982a).
       LSQR: An algorithm for sparse linear equations and sparse least squares,
       ACM TOMS 8(1), 43-71.
    2. C. C. Paige and M. A. Saunders (1982b).
       Algorithm 583.  LSQR: Sparse linear equations and least squares problems,
       ACM TOMS 8(2), 195-209.
    3. M. A. Saunders (1995).  Solution of sparse rectangular systems using
       LSQR and CRAIG, BIT 35, 588-604.

    Input parameters:

    atol, btol  are stopping tolerances.  If both are 1.0e-9 (say),
                the final residual norm should be accurate to about 9 digits.
                (The final x will usually have fewer correct digits,
                depending on cond(A) and the size of damp.)
    conlim      is also a stopping tolerance.  lsqr terminates if an estimate
                of cond(A) exceeds conlim.  For compatible systems Ax = b,
                conlim could be as large as 1.0e+12 (say).  For least-squares
                problems, conlim should be less than 1.0e+8.
                Maximum precision can be obtained by setting
                atol = btol = conlim = zero, but the number of iterations
                may then be excessive.
    itnlim      is an explicit limit on iterations (for safety).
    show        if set to 1, gives an iteration log.
                If set to 0, suppresses output.

    Output parameters:

    x           is the final solution.
    istop       gives the reason for termination.
    istop       = 1 means x is an approximate solution to Ax = b.
                = 2 means x approximately solves the least-squares problem.
                r1norm      = norm(r), where r = b - Ax.
                r2norm      = sqrt( norm(r)^2  +  damp^2 * norm(x)^2 )
                = r1norm if damp = 0.
    anorm       = estimate of Frobenius norm of Abar = [  A   ].
                                                       [damp*I]
    acond       = estimate of cond(Abar).
    arnorm      = estimate of norm(A'*r - damp^2*x).
    xnorm       = norm(x).
    var         (if present) estimates all diagonals of (A'A)^{-1} (if damp=0)
                or more generally (A'A + damp^2*I)^{-1}.
                This is well defined if A has full column rank or damp > 0.
                (Not sure what var means if rank(A) < n and damp = 0.)
                
    ----------------------------------------------------------------------
    """
    msg = [
     'The exact solution is  x = 0                              ', 
     'Ax - b is small enough, given atol, btol                  ', 
     'The least-squares solution is good enough, given atol     ', 
     'The estimate of cond(Abar) has exceeded conlim            ', 
     'Ax - b is small enough for this machine                   ', 
     'The least-squares solution is good enough for this machine', 
     'Cond(Abar) seems to be too large for this machine         ', 
     'The iteration limit has been reached                      ']
    if wantvar:
        var = zeros(n, 1)
    else:
        var = None
    itn = 0
    istop = 0
    nstop = 0
    ctol = 0.0
    if conlim > 0.0:
        ctol = 1.0 / conlim
    anorm = 0.0
    acond = 0.0
    dampsq = damp ** 2
    ddnorm = 0.0
    res2 = 0.0
    xnorm = 0.0
    xxnorm = 0.0
    z = 0.0
    cs2 = -1.0
    sn2 = 0.0
    u = b[:m]
    x = zeros(n)
    alfa = 0.0
    beta = norm(u)
    if beta > 0:
        u = 1.0 / beta * u
        v = aprod(2, m, n, u)
        alfa = norm(v)
    if alfa > 0:
        v = 1.0 / alfa * v
        w = v.copy()
    arnorm = alfa * beta
    if arnorm == 0:
        return (
         x, istop, itn, r1norm, r2norm, anorm, acond, arnorm, xnorm, var)
    else:
        rhobar = alfa
        phibar = beta
        bnorm = beta
        rnorm = beta
        r1norm = rnorm
        r2norm = rnorm
        head1 = '   Itn      x(1)       r1norm     r2norm '
        head2 = ' Compatible   LS      Norm A   Cond A'
        if show:
            test1 = 1.0
            test2 = alfa / beta
            str1 = '%6g %12.5e' % (itn, x[0])
            str2 = ' %10.3e %10.3e' % (r1norm, r2norm)
            str3 = '  %8.1e %8.1e' % (test1, test2)
        while itn < itnlim:
            itn = itn + 1
            u = aprod(1, m, n, v) - alfa * u
            beta = norm(u)
            if beta > 0:
                u = 1.0 / beta * u
                anorm = normof4(anorm, alfa, beta, damp)
                v = aprod(2, m, n, u) - beta * v
                alfa = norm(v)
                if alfa > 0:
                    v = 1.0 / alfa * v
            rhobar1 = normof2(rhobar, damp)
            cs1 = rhobar / rhobar1
            sn1 = damp / rhobar1
            psi = sn1 * phibar
            phibar = cs1 * phibar
            rho = normof2(rhobar1, beta)
            cs = rhobar1 / rho
            sn = beta / rho
            theta = sn * alfa
            rhobar = -cs * alfa
            phi = cs * phibar
            phibar = sn * phibar
            tau = sn * phi
            t1 = phi / rho
            t2 = -theta / rho
            dk = 1.0 / rho * w
            x = x + t1 * w
            w = v + t2 * w
            ddnorm = ddnorm + norm(dk) ** 2
            if wantvar:
                var = var + dk * dk
            delta = sn2 * rho
            gambar = -cs2 * rho
            rhs = phi - delta * z
            zbar = rhs / gambar
            xnorm = sqrt(xxnorm + zbar ** 2)
            gamma = normof2(gambar, theta)
            cs2 = gambar / gamma
            sn2 = theta / gamma
            z = rhs / gamma
            xxnorm = xxnorm + z ** 2
            acond = anorm * sqrt(ddnorm)
            res1 = phibar ** 2
            res2 = res2 + psi ** 2
            rnorm = sqrt(res1 + res2)
            arnorm = alfa * abs(tau)
            r1sq = rnorm ** 2 - dampsq * xxnorm
            r1norm = sqrt(abs(r1sq))
            if r1sq < 0:
                r1norm = -r1norm
            r2norm = rnorm
            test1 = rnorm / bnorm
            test2 = arnorm / (anorm * rnorm)
            test3 = 1.0 / acond
            t1 = test1 / (1 + anorm * xnorm / bnorm)
            rtol = btol + atol * anorm * xnorm / bnorm
            if itn >= itnlim:
                istop = 7
            if 1 + test3 <= 1:
                istop = 6
            if 1 + test2 <= 1:
                istop = 5
            if 1 + t1 <= 1:
                istop = 4
            if test3 <= ctol:
                istop = 3
            if test2 <= atol:
                istop = 2
            if test1 <= rtol:
                istop = 1
            prnt = False
            if n <= 40:
                prnt = True
            if itn <= 10:
                prnt = True
            if itn >= itnlim - 10:
                prnt = True
            if itn % 10 == 0:
                prnt = True
            if test3 <= 2 * ctol:
                prnt = True
            if test2 <= 10 * atol:
                prnt = True
            if test1 <= 10 * rtol:
                prnt = True
            if istop != 0:
                prnt = True
            if prnt and show:
                str1 = '%6g %12.5e' % (itn, x[0])
                str2 = ' %10.3e %10.3e' % (r1norm, r2norm)
                str3 = '  %8.1e %8.1e' % (test1, test2)
                str4 = ' %8.1e %8.1e' % (anorm, acond)
            if istop > 0:
                break
            callback(x)

        return (
         x, istop, itn, r1norm, r2norm, anorm, acond, arnorm, xnorm, var)