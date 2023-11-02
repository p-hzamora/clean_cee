# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\sparse\linalg\isolve\minres.pyc
# Compiled at: 2013-02-16 13:27:32
from __future__ import division, print_function, absolute_import
from numpy import sqrt, inner, finfo, zeros
from numpy.linalg import norm
from .utils import make_system
from .iterative import set_docstring
__all__ = [
 'minres']
header = 'Use MINimum RESidual iteration to solve Ax=b\n\nMINRES minimizes norm(A*x - b) for a real symmetric matrix A.  Unlike\nthe Conjugate Gradient method, A can be indefinite or singular.\n\nIf shift != 0 then the method solves (A - shift*I)x = b\n'
Ainfo = 'The real symmetric N-by-N matrix of the linear system'
footer = '\nNotes\n-----\nTHIS FUNCTION IS EXPERIMENTAL AND SUBJECT TO CHANGE!\n\nReferences\n----------\nSolution of sparse indefinite systems of linear equations,\n    C. C. Paige and M. A. Saunders (1975),\n    SIAM J. Numer. Anal. 12(4), pp. 617-629.\n    http://www.stanford.edu/group/SOL/software/minres.html\n\nThis file is a translation of the following MATLAB implementation:\n    http://www.stanford.edu/group/SOL/software/minres/matlab/\n'

@set_docstring(header, Ainfo, footer)
def minres(A, b, x0=None, shift=0.0, tol=1e-05, maxiter=None, xtype=None, M=None, callback=None, show=False, check=False):
    A, M, x, b, postprocess = make_system(A, M, x0, b, xtype)
    matvec = A.matvec
    psolve = M.matvec
    first = 'Enter minres.   '
    last = 'Exit  minres.   '
    n = A.shape[0]
    if maxiter is None:
        maxiter = 5 * n
    msg = [
     ' beta2 = 0.  If M = I, b and x are eigenvectors    ', 
     ' beta1 = 0.  The exact solution is  x = 0          ', 
     ' A solution to Ax = b was found, given rtol        ', 
     ' A least-squares solution was found, given rtol    ', 
     ' Reasonable accuracy achieved, given eps           ', 
     ' x has converged to an eigenvector                 ', 
     ' acond has exceeded 0.1/eps                        ', 
     ' The iteration limit was reached                   ', 
     ' A  does not define a symmetric matrix             ', 
     ' M  does not define a symmetric matrix             ', 
     ' M  does not define a pos-def preconditioner       ']
    if show:
        print(first + 'Solution of symmetric Ax = b')
        print(first + 'n      =  %3g     shift  =  %23.14e' % (n, shift))
        print(first + 'itnlim =  %3g     rtol   =  %11.2e' % (maxiter, tol))
        print()
    istop = 0
    itn = 0
    Anorm = 0
    Acond = 0
    rnorm = 0
    ynorm = 0
    xtype = x.dtype
    eps = finfo(xtype).eps
    x = zeros(n, dtype=xtype)
    y = b
    r1 = b
    y = psolve(b)
    beta1 = inner(b, y)
    if beta1 < 0:
        raise ValueError('indefinite preconditioner')
    elif beta1 == 0:
        return (postprocess(x), 0)
    beta1 = sqrt(beta1)
    if check:
        w = matvec(y)
        r2 = matvec(w)
        s = inner(w, w)
        t = inner(y, r2)
        z = abs(s - t)
        epsa = (s + eps) * eps ** 0.3333333333333333
        if z > epsa:
            raise ValueError('non-symmetric matrix')
        r2 = psolve(y)
        s = inner(y, y)
        t = inner(r1, r2)
        z = abs(s - t)
        epsa = (s + eps) * eps ** 0.3333333333333333
        if z > epsa:
            raise ValueError('non-symmetric preconditioner')
    oldb = 0
    beta = beta1
    dbar = 0
    epsln = 0
    qrnorm = beta1
    phibar = beta1
    rhs1 = beta1
    rhs2 = 0
    tnorm2 = 0
    ynorm2 = 0
    cs = -1
    sn = 0
    w = zeros(n, dtype=xtype)
    w2 = zeros(n, dtype=xtype)
    r2 = r1
    if show:
        print()
        print()
        print('   Itn     x(1)     Compatible    LS       norm(A)  cond(A) gbar/|A|')
    while itn < maxiter:
        itn += 1
        s = 1.0 / beta
        v = s * y
        y = matvec(v)
        y = y - shift * v
        if itn >= 2:
            y = y - beta / oldb * r1
        alfa = inner(v, y)
        y = y - alfa / beta * r2
        r1 = r2
        r2 = y
        y = psolve(r2)
        oldb = beta
        beta = inner(r2, y)
        if beta < 0:
            raise ValueError('non-symmetric matrix')
        beta = sqrt(beta)
        tnorm2 += alfa ** 2 + oldb ** 2 + beta ** 2
        if itn == 1:
            if beta / beta1 <= 10 * eps:
                istop = -1
            gmax = abs(alfa)
            gmin = gmax
        oldeps = epsln
        delta = cs * dbar + sn * alfa
        gbar = sn * dbar - cs * alfa
        epsln = sn * beta
        dbar = -cs * beta
        root = norm([gbar, dbar])
        Arnorm = phibar * root
        gamma = norm([gbar, beta])
        gamma = max(gamma, eps)
        cs = gbar / gamma
        sn = beta / gamma
        phi = cs * phibar
        phibar = sn * phibar
        denom = 1.0 / gamma
        w1 = w2
        w2 = w
        w = (v - oldeps * w1 - delta * w2) * denom
        x = x + phi * w
        gmax = max(gmax, gamma)
        gmin = min(gmin, gamma)
        z = rhs1 / gamma
        ynorm2 = z ** 2 + ynorm2
        rhs1 = rhs2 - delta * z
        rhs2 = -epsln * z
        Anorm = sqrt(tnorm2)
        ynorm = sqrt(ynorm2)
        epsa = Anorm * eps
        epsx = Anorm * ynorm * eps
        epsr = Anorm * ynorm * tol
        diag = gbar
        if diag == 0:
            diag = epsa
        qrnorm = phibar
        rnorm = qrnorm
        test1 = rnorm / (Anorm * ynorm)
        test2 = root / Anorm
        Acond = gmax / gmin
        if istop == 0:
            t1 = 1 + test1
            t2 = 1 + test2
            if t2 <= 1:
                istop = 2
            if t1 <= 1:
                istop = 1
            if itn >= maxiter:
                istop = 6
            if Acond >= 0.1 / eps:
                istop = 4
            if epsx >= beta1:
                istop = 3
            if test2 <= tol:
                istop = 2
            if test1 <= tol:
                istop = 1
        prnt = False
        if n <= 40:
            prnt = True
        if itn <= 10:
            prnt = True
        if itn >= maxiter - 10:
            prnt = True
        if itn % 10 == 0:
            prnt = True
        if qrnorm <= 10 * epsx:
            prnt = True
        if qrnorm <= 10 * epsr:
            prnt = True
        if Acond <= 0.01 / eps:
            prnt = True
        if istop != 0:
            prnt = True
        if show and prnt:
            str1 = '%6g %12.5e %10.3e' % (itn, x[0], test1)
            str2 = ' %10.3e' % (test2,)
            str3 = ' %8.1e %8.1e %8.1e' % (Anorm, Acond, gbar / Anorm)
            print(str1 + str2 + str3)
            if itn % 10 == 0:
                print()
        if callback is not None:
            callback(x)
        if istop != 0:
            break

    if show:
        print()
        print(last + ' istop   =  %3g               itn   =%5g' % (istop, itn))
        print(last + ' Anorm   =  %12.4e      Acond =  %12.4e' % (Anorm, Acond))
        print(last + ' rnorm   =  %12.4e      ynorm =  %12.4e' % (rnorm, ynorm))
        print(last + ' Arnorm  =  %12.4e' % (Arnorm,))
        print(last + msg[istop + 1])
    if istop == 6:
        info = maxiter
    else:
        info = 0
    return (postprocess(x), info)


if __name__ == '__main__':
    from scipy import ones, arange
    from scipy.linalg import norm
    from scipy.sparse import spdiags
    n = 10
    residuals = []

    def cb(x):
        residuals.append(norm(b - A * x))


    A = spdiags([arange(1, n + 1, dtype=float)], [0], n, n, format='csr')
    M = spdiags([1.0 / arange(1, n + 1, dtype=float)], [0], n, n, format='csr')
    A.psolve = M.matvec
    b = 0 * ones(A.shape[0])
    x = minres(A, b, tol=1e-12, maxiter=None, callback=cb)