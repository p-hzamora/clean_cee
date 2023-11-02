# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\optimize\tnc.pyc
# Compiled at: 2013-02-16 13:27:30
"""
TNC: A python interface to the TNC non-linear optimizer

TNC is a non-linear optimizer. To use it, you must provide a function to
minimize. The function must take one argument: the list of coordinates where to
evaluate the function; and it must return either a tuple, whose first element is the
value of the function, and whose second argument is the gradient of the function
(as a list of values); or None, to abort the minimization.
"""
from __future__ import division, print_function, absolute_import
from scipy.optimize import moduleTNC, approx_fprime
from .optimize import MemoizeJac, Result, _check_unknown_options
from numpy import asarray, inf, array
__all__ = [
 'fmin_tnc']
MSG_NONE = 0
MSG_ITER = 1
MSG_INFO = 2
MSG_VERS = 4
MSG_EXIT = 8
MSG_ALL = MSG_ITER + MSG_INFO + MSG_VERS + MSG_EXIT
MSGS = {MSG_NONE: 'No messages', 
   MSG_ITER: 'One line per iteration', 
   MSG_INFO: 'Informational messages', 
   MSG_VERS: 'Version info', 
   MSG_EXIT: 'Exit reasons', 
   MSG_ALL: 'All messages'}
INFEASIBLE = -1
LOCALMINIMUM = 0
FCONVERGED = 1
XCONVERGED = 2
MAXFUN = 3
LSFAIL = 4
CONSTANT = 5
NOPROGRESS = 6
USERABORT = 7
RCSTRINGS = {INFEASIBLE: 'Infeasible (low > up)', 
   LOCALMINIMUM: 'Local minima reach (|pg| ~= 0)', 
   FCONVERGED: 'Converged (|f_n-f_(n-1)| ~= 0)', 
   XCONVERGED: 'Converged (|x_n-x_(n-1)| ~= 0)', 
   MAXFUN: 'Max. number of function evaluations reach', 
   LSFAIL: 'Linear search failed', 
   CONSTANT: 'All lower bounds are equal to the upper bounds', 
   NOPROGRESS: 'Unable to progress', 
   USERABORT: 'User requested end of minimization'}

def fmin_tnc(func, x0, fprime=None, args=(), approx_grad=0, bounds=None, epsilon=1e-08, scale=None, offset=None, messages=MSG_ALL, maxCGit=-1, maxfun=None, eta=-1, stepmx=0, accuracy=0, fmin=0, ftol=-1, xtol=-1, pgtol=-1, rescale=-1, disp=None, callback=None):
    """
    Minimize a function with variables subject to bounds, using
    gradient information in a truncated Newton algorithm. This
    method wraps a C implementation of the algorithm.

    Parameters
    ----------
    func : callable ``func(x, *args)``
        Function to minimize.  Must do one of:

        1. Return f and g, where f is the value of the function and g its
           gradient (a list of floats).

        2. Return the function value but supply gradient function
           seperately as `fprime`.

        3. Return the function value and set ``approx_grad=True``.

        If the function returns None, the minimization
        is aborted.
    x0 : list of floats
        Initial estimate of minimum.
    fprime : callable ``fprime(x, *args)``
        Gradient of `func`. If None, then either `func` must return the
        function value and the gradient (``f,g = func(x, *args)``)
        or `approx_grad` must be True.
    args : tuple
        Arguments to pass to function.
    approx_grad : bool
        If true, approximate the gradient numerically.
    bounds : list
        (min, max) pairs for each element in x0, defining the
        bounds on that parameter. Use None or +/-inf for one of
        min or max when there is no bound in that direction.
    epsilon : float
        Used if approx_grad is True. The stepsize in a finite
        difference approximation for fprime.
    scale : list of floats
        Scaling factors to apply to each variable.  If None, the
        factors are up-low for interval bounded variables and
        1+|x] fo the others.  Defaults to None
    offset : float
        Value to substract from each variable.  If None, the
        offsets are (up+low)/2 for interval bounded variables
        and x for the others.
    messages :
        Bit mask used to select messages display during
        minimization values defined in the MSGS dict.  Defaults to
        MGS_ALL.
    disp : int
        Integer interface to messages.  0 = no message, 5 = all messages
    maxCGit : int
        Maximum number of hessian*vector evaluations per main
        iteration.  If maxCGit == 0, the direction chosen is
        -gradient if maxCGit < 0, maxCGit is set to
        max(1,min(50,n/2)).  Defaults to -1.
    maxfun : int
        Maximum number of function evaluation.  if None, maxfun is
        set to max(100, 10*len(x0)).  Defaults to None.
    eta : float
        Severity of the line search. if < 0 or > 1, set to 0.25.
        Defaults to -1.
    stepmx : float
        Maximum step for the line search.  May be increased during
        call.  If too small, it will be set to 10.0.  Defaults to 0.
    accuracy : float
        Relative precision for finite difference calculations.  If
        <= machine_precision, set to sqrt(machine_precision).
        Defaults to 0.
    fmin : float
        Minimum function value estimate.  Defaults to 0.
    ftol : float
        Precision goal for the value of f in the stoping criterion.
        If ftol < 0.0, ftol is set to 0.0 defaults to -1.
    xtol : float
        Precision goal for the value of x in the stopping
        criterion (after applying x scaling factors).  If xtol <
        0.0, xtol is set to sqrt(machine_precision).  Defaults to
        -1.
    pgtol : float
        Precision goal for the value of the projected gradient in
        the stopping criterion (after applying x scaling factors).
        If pgtol < 0.0, pgtol is set to 1e-2 * sqrt(accuracy).
        Setting it to 0.0 is not recommended.  Defaults to -1.
    rescale : float
        Scaling factor (in log10) used to trigger f value
        rescaling.  If 0, rescale at each iteration.  If a large
        value, never rescale.  If < 0, rescale is set to 1.3.
    callback : callable, optional
        Called after each iteration, as callback(xk), where xk is the
        current parameter vector.

    Returns
    -------
    x : list of floats
        The solution.
    nfeval : int
        The number of function evaluations.
    rc : int
        Return code as defined in the RCSTRINGS dict.

    See also
    --------
    minimize: Interface to minimization algorithms for multivariate
        functions. See the 'TNC' `method` in particular.

    Notes
    -----
    The underlying algorithm is truncated Newton, also called
    Newton Conjugate-Gradient. This method differs from
    scipy.optimize.fmin_ncg in that

    1. It wraps a C implementation of the algorithm
    2. It allows each variable to be given an upper and lower bound.

    The algorithm incoporates the bound constraints by determining
    the descent direction as in an unconstrained truncated Newton,
    but never taking a step-size large enough to leave the space
    of feasible x's. The algorithm keeps track of a set of
    currently active constraints, and ignores them when computing
    the minimum allowable step size. (The x's associated with the
    active constraint are kept fixed.) If the maximum allowable
    step size is zero then a new constraint is added. At the end
    of each iteration one of the constraints may be deemed no
    longer active and removed. A constraint is considered
    no longer active is if it is currently active
    but the gradient for that variable points inward from the
    constraint. The specific constraint removed is the one
    associated with the variable of largest index whose
    constraint is no longer active.

    References
    ----------
    Wright S., Nocedal J. (2006), 'Numerical Optimization'

    Nash S.G. (1984), "Newton-Type Minimization Via the Lanczos Method",
    SIAM Journal of Numerical Analysis 21, pp. 770-778

    """
    if approx_grad:
        fun = func
        jac = None
    elif fprime is None:
        fun = MemoizeJac(func)
        jac = fun.derivative
    else:
        fun = func
        jac = fprime
    if disp is not None:
        mesg_num = disp
    else:
        mesg_num = {0: MSG_NONE, 1: MSG_ITER, 2: MSG_INFO, 3: MSG_VERS, 4: MSG_EXIT, 
           5: MSG_ALL}.get(messages, MSG_ALL)
    opts = {'eps': epsilon, 'scale': scale, 
       'offset': offset, 
       'mesg_num': mesg_num, 
       'maxCGit': maxCGit, 
       'maxiter': maxfun, 
       'eta': eta, 
       'stepmx': stepmx, 
       'accuracy': accuracy, 
       'minfev': fmin, 
       'ftol': ftol, 'xtol': xtol, 
       'gtol': pgtol, 
       'rescale': rescale, 
       'disp': False}
    res = _minimize_tnc(fun, x0, args, jac, bounds, callback=callback, **opts)
    return (
     res['x'], res['nfev'], res['status'])


def _minimize_tnc(fun, x0, args=(), jac=None, bounds=None, eps=1e-08, scale=None, offset=None, mesg_num=None, maxCGit=-1, maxiter=None, eta=-1, stepmx=0, accuracy=0, minfev=0, ftol=-1, xtol=-1, gtol=-1, rescale=-1, disp=False, callback=None, **unknown_options):
    """
    Minimize a scalar function of one or more variables using a truncated
    Newton (TNC) algorithm.

    Options for the TNC algorithm are:
        eps : float
            Step size used for numerical approximation of the jacobian.
        scale : list of floats
            Scaling factors to apply to each variable.  If None, the
            factors are up-low for interval bounded variables and
            1+|x] fo the others.  Defaults to None
        offset : float
            Value to substract from each variable.  If None, the
            offsets are (up+low)/2 for interval bounded variables
            and x for the others.
        disp : bool
           Set to True to print convergence messages.
        maxCGit : int
            Maximum number of hessian*vector evaluations per main
            iteration.  If maxCGit == 0, the direction chosen is
            -gradient if maxCGit < 0, maxCGit is set to
            max(1,min(50,n/2)).  Defaults to -1.
        maxiter : int
            Maximum number of function evaluation.  if None, `maxiter` is
            set to max(100, 10*len(x0)).  Defaults to None.
        eta : float
            Severity of the line search. if < 0 or > 1, set to 0.25.
            Defaults to -1.
        stepmx : float
            Maximum step for the line search.  May be increased during
            call.  If too small, it will be set to 10.0.  Defaults to 0.
        accuracy : float
            Relative precision for finite difference calculations.  If
            <= machine_precision, set to sqrt(machine_precision).
            Defaults to 0.
        minfev : float
            Minimum function value estimate.  Defaults to 0.
        ftol : float
            Precision goal for the value of f in the stoping criterion.
            If ftol < 0.0, ftol is set to 0.0 defaults to -1.
        xtol : float
            Precision goal for the value of x in the stopping
            criterion (after applying x scaling factors).  If xtol <
            0.0, xtol is set to sqrt(machine_precision).  Defaults to
            -1.
        gtol : float
            Precision goal for the value of the projected gradient in
            the stopping criterion (after applying x scaling factors).
            If gtol < 0.0, gtol is set to 1e-2 * sqrt(accuracy).
            Setting it to 0.0 is not recommended.  Defaults to -1.
        rescale : float
            Scaling factor (in log10) used to trigger f value
            rescaling.  If 0, rescale at each iteration.  If a large
            value, never rescale.  If < 0, rescale is set to 1.3.

    This function is called by the `minimize` function with `method=TNC`.
    It is not supposed to be called directly.
    """
    _check_unknown_options(unknown_options)
    epsilon = eps
    maxfun = maxiter
    fmin = minfev
    pgtol = gtol
    x0 = asarray(x0, dtype=float).tolist()
    n = len(x0)
    if bounds is None:
        bounds = [
         (None, None)] * n
    if len(bounds) != n:
        raise ValueError('length of x0 != length of bounds')
    if mesg_num is not None:
        messages = {0: MSG_NONE, 1: MSG_ITER, 2: MSG_INFO, 3: MSG_VERS, 4: MSG_EXIT, 5: MSG_ALL}.get(mesg_num, MSG_ALL)
    else:
        if disp:
            messages = MSG_ALL
        else:
            messages = MSG_NONE
        if jac is None:

            def func_and_grad(x):
                x = asarray(x)
                f = fun(x, *args)
                g = approx_fprime(x, fun, epsilon, *args)
                return (f, list(g))

        else:

            def func_and_grad(x):
                x = asarray(x)
                f = fun(x, *args)
                g = jac(x, *args)
                return (f, list(g))

        low = [
         0] * n
        up = [0] * n
        for i in range(n):
            if bounds[i] is None:
                l, u = -inf, inf
            else:
                l, u = bounds[i]
                if l is None:
                    low[i] = -inf
                else:
                    low[i] = l
                if u is None:
                    up[i] = inf
                else:
                    up[i] = u

    if scale is None:
        scale = []
    if offset is None:
        offset = []
    if maxfun is None:
        maxfun = max(100, 10 * len(x0))
    rc, nf, nit, x = moduleTNC.minimize(func_and_grad, x0, low, up, scale, offset, messages, maxCGit, maxfun, eta, stepmx, accuracy, fmin, ftol, xtol, pgtol, rescale, callback)
    xopt = array(x)
    funv, jacv = func_and_grad(xopt)
    return Result(x=xopt, fun=funv, jac=jacv, nfev=nf, nit=nit, status=rc, message=RCSTRINGS[rc], success=-1 < rc < 3)


if __name__ == '__main__':

    def example():
        print('Example')

        def function(x):
            f = pow(x[0], 2.0) + pow(abs(x[1]), 3.0)
            g = [0, 0]
            g[0] = 2.0 * x[0]
            g[1] = 3.0 * pow(abs(x[1]), 2.0)
            if x[1] < 0:
                g[1] = -g[1]
            return (
             f, g)

        x, nf, rc = fmin_tnc(function, [-7, 3], bounds=([-10, 1], [10, 10]))
        print('After', nf, 'function evaluations, TNC returned:', RCSTRINGS[rc])
        print('x =', x)
        print('exact value = [0, 1]')
        print()


    example()