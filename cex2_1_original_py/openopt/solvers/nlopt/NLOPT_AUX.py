# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\nlopt\NLOPT_AUX.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt.kernel.setDefaultIterFuncs import SOLVED_WITH_UNIMPLEMENTED_OR_UNKNOWN_REASON, SMALL_DELTA_X, SMALL_DELTA_F
from numpy import isfinite, asscalar, asfarray, abs, copy, isinf, ones, array
import nlopt

def NLOPT_AUX(p, solver, opts=None):

    def myfunc(x, grad):
        if grad.size > 0:
            grad[:] = p.df(x.copy())
        return asscalar(p.f(x))

    if solver in [nlopt.LD_MMA] and (p.nbeq != 0 or p.nh != 0):
        opt = nlopt.opt(nlopt.LD_AUGLAG, p.n)
        opt2 = nlopt.opt(solver, p.n)
        setStopCriteria(opt2, p, reduce=10.0)
        opt.set_local_optimizer(opt2)
    else:
        if solver == nlopt.G_MLSL_LDS:
            opt = nlopt.opt(nlopt.G_MLSL_LDS, p.n)
            opt2 = nlopt.opt(nlopt.LD_TNEWTON_PRECOND_RESTART, p.n)
            setStopCriteria(opt2, p, reduce=10.0)
            opt.set_local_optimizer(opt2)
        else:
            opt = nlopt.opt(solver, p.n)
        if opts is not None:
            for option, val in opts.items():
                getattr(opt, option)(val)

        opt.set_min_objective(myfunc)
        if any(p.lb == p.ub):
            p.pWarn('nlopt solvers badly handle problems with variables fixed via setting lb=ub')
        lb = [ elem if isfinite(elem) else float(elem) for elem in p.lb.tolist() ]
        ub = [ elem if isfinite(elem) else float(elem) for elem in p.ub.tolist() ]
        if any(isfinite(lb)):
            opt.set_lower_bounds(lb)
        if any(isfinite(ub)):
            opt.set_upper_bounds(ub)
        if p.nc > 0:

            def c(result, x, grad):
                if grad.size > 0:
                    grad[:] = p.dc(x.copy())
                result[:] = p.c(x)

            opt.add_inequality_mconstraint(c, array([p.contol] * p.nc).copy())
        if p.nb > 0:

            def c_lin(result, x, grad):
                if grad.size > 0:
                    grad[:] = p.A.copy()
                result[:] = p._get_AX_Less_B_residuals(x)

            opt.add_inequality_mconstraint(c_lin, array([p.contol] * p.nb).copy())
        if p.nh > 0:

            def h(result, x, grad):
                if grad.size > 0:
                    grad[:] = p.dh(x.copy())
                result[:] = p.h(x).copy()

            opt.add_equality_mconstraint(h, array([p.contol] * p.nh))
        if p.nbeq > 0:

            def h_lin(result, x, grad):
                if grad.size > 0:
                    grad[:] = p.Aeq.copy()
                result[:] = p._get_AeqX_eq_Beq_residuals(x)

            opt.add_equality_mconstraint(h_lin, array([p.contol] * p.nbeq))
        setStopCriteria(opt, p)
        x0 = asfarray(p.x0).copy()
        LB = copy(lb)
        ind = x0 <= LB
        x0[ind] = LB[ind]
        UB = copy(ub)
        ind = x0 >= UB
        x0[ind] = UB[ind]
        try:
            x = opt.optimize(x0.tolist()).copy()
        except:
            pass

    p.xk = p._bestPoint.x
    iStop = opt.get_stopval()
    if p.istop == 0:
        if iStop == nlopt.XTOL_REACHED:
            p.istop, p.msg = SMALL_DELTA_X, '|| X[k] - X[k-1] || < xtol'
        else:
            if iStop == nlopt.FTOL_REACHED:
                p.istop, p.msg = SMALL_DELTA_F, '|| F[k] - F[k-1] || < ftol'
            else:
                p.istop = SOLVED_WITH_UNIMPLEMENTED_OR_UNKNOWN_REASON
    return


def setStopCriteria(opt, p, reduce=1.0):
    opt.set_xtol_abs(p.xtol / reduce)
    opt.set_ftol_abs(p.ftol / reduce)
    opt.set_maxeval(p.maxFunEvals)
    if isfinite(p.maxTime):
        opt.set_maxtime(p.maxTime)