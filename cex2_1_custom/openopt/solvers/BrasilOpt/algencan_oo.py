# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\BrasilOpt\algencan_oo.pyc
# Compiled at: 2012-12-08 11:04:59
__docformat__ = 'restructuredtext en'
from .numpy import *
from openopt.kernel.baseSolver import baseSolver
import pywrapper
from openopt.kernel.setDefaultIterFuncs import SMALL_DF

class algencan(baseSolver):
    __name__ = 'algencan'
    __license__ = 'GPL'
    __authors__ = 'J. M. Martinez martinezimecc@gmail.com, Ernesto G. Birgin egbirgin@ime.usp.br, Jan Marcel Paiva Gentil jgmarcel@ime.usp.br'
    __alg__ = 'Augmented Lagrangian Multipliers'
    __homepage__ = 'http://www.ime.usp.br/~egbirgin/tango/'
    __info__ = "please pay more attention to gtol param, it's the only one ALGENCAN positive stop criterium, xtol and ftol are unused"
    __optionalDataThatCanBeHandled__ = ['A', 'Aeq', 'b', 'beq', 'lb', 'ub', 'c', 'h']
    __isIterPointAlwaysFeasible__ = lambda self, p: p.__isNoMoreThanBoxBounded__()
    __cannotHandleExceptions__ = True

    def __init__(self):
        pass

    def __solver__(self, p):

        def inip():
            """This subroutine must set some problem data.

            For achieving this objective YOU MUST MODIFY it according to your
            problem. See below where your modifications must be inserted.

            Parameters of the subroutine:

            On Entry:

            This subroutine has no input parameters.

            On Return

            n        integer,
                     number of variables,

            x        double precision x(n),
                     initial point,

            l        double precision l(n),
                     lower bounds on x,

            u        double precision u(n),
                     upper bounds on x,

            m        integer,
                     number of constraints (excluding the bounds),

            lambda   double precision lambda(m),
                     initial estimation of the Lagrange multipliers,

            equatn   logical equatn(m)
                     for each constraint j, set equatn(j) = .true. if it is an
                     equality constraint of the form c_j(x) = 0, and set
                     equatn(j) = .false. if it is an inequality constraint of
                     the form c_j(x) <= 0,

            linear   logical linear(m)
                     for each constraint j, set linear(j) = .true. if it is a
                     linear constraint, and set linear(j) = .false. if it is a
                     nonlinear constraint.
            """
            n = p.n
            nc, nh = p.nc, p.nh
            nb, nbeq = p.b.size, p.beq.size
            m = nc + nh + nb + nbeq
            x = p.x0
            l = p.lb
            l[l < -1e+20] = -1e+20
            u = p.ub
            u[u > 1e+20] = 1e+20
            lambda_ = zeros(m)
            equatn = array([False] * nc + [True] * nh + [False] * nb + [True] * nbeq)
            linear = array([False] * nc + [False] * nh + [True] * nb + [True] * nbeq)
            coded = [
             True,
             True,
             p.userProvided.d2f,
             True,
             True,
             False,
             False,
             False,
             False,
             False]
            checkder = False
            return (
             n, x, l, u, m, lambda_, equatn.tolist(), linear.tolist(), coded, checkder)

        def evalf(x):
            """This subroutine must compute the objective function.

            For achieving this objective YOU MUST MODIFY it according to your
            problem. See below where your modifications must be inserted.

            Parameters of the subroutine:

            On Entry:

            x        double precision x(n),
                     current point,

            On Return

            f        double precision,
                     objective function value at x,

            flag     integer,
                     You must set it to any number different of 0 (zero) if
                     some error ocurred during the evaluation of the objective
                     function. (For example, trying to compute the square root
                     of a negative number, dividing by zero or a very small
                     number, etc.) If everything was o.k. you must set it
                     equal to zero.
            """
            f = p.f(x)
            if f is not nan:
                flag = 0
            else:
                flag = 1
            return (f, flag)

        def evalg(x):
            """This subroutine must compute the gradient vector of the objective         function.

            For achieving these objective YOU MUST MODIFY it in the way specified
            below. However, if you decide to use numerical derivatives (we dont
            encourage this option at all!) you dont need to modify evalg.

            Parameters of the subroutine:

            On Entry:

            x        double precision x(n),
                     current point,

            On Return

            g        double precision g(n),
                     gradient vector of the objective function evaluated at x,

            flag     integer,
                     You must set it to any number different of 0 (zero) if
                     some error ocurred during the evaluation of any component
                     of the gradient vector. (For example, trying to compute
                     the square root of a negative number, dividing by zero or
                     a very small number, etc.) If everything was o.k. you
                     must set it equal to zero.
            """
            g = p.df(x)
            if any(isnan(g)):
                flag = 1
            else:
                flag = 0
            return (g, flag)

        def evalh(x):
            flag = 0
            try:
                H = p.d2f(x)
            except:
                nnzh = 0
                hlin = zeros(nnzh, int)
                hcol = zeros(nnzh, int)
                hval = zeros(nnzh, float)
                flag = 1
                return (hlin, hcol, hval, nnzh, flag)

            ind = H.nonzero()
            ind_0, ind_1 = ind
            ind_greater = ind_0 >= ind_1
            ind_0, ind_1 = ind_0[ind_greater], ind_1[ind_greater]
            nnzh = ind_0.size
            val = H[(ind_0, ind_1)]
            hlin, hcol, hval = ind_0, ind_1, val
            return (
             hlin, hcol, hval, nnzh, flag)

        def evalc(x, ind):
            """This subroutine must compute the ind-th constraint.

            For achieving this objective YOU MUST MOFIFY it according to your
            problem. See below the places where your modifications must be
            inserted.

            Parameters of the subroutine:

            On Entry:

            x        double precision x(n),
                     current point,

            ind      integer,
                     index of the constraint to be computed,

            On Return

            c        double precision,
                     i-th constraint evaluated at x,

            flag     integer
                     You must set it to any number different of 0 (zero) if
                     some error ocurred during the evaluation of the
                     constraint. (For example, trying to compute the square
                     root of a negative number, dividing by zero or a very
                     small number, etc.) If everything was o.k. you must set
                     it equal to zero.
            """
            flag = 0
            i = ind - 1
            if i < p.nc:
                c = p.c(x, i)
            elif p.nc <= i < p.nc + p.nh:
                c = p.h(x, i - p.nc)
            elif p.nc + p.nh <= i < p.nc + p.nh + p.nb:
                j = i - p.nc - p.nh
                c = p.dotmult(p.A[j], x).sum() - p.b[j]
            elif i < p.nc + p.nh + p.nb + p.nbeq:
                j = i - p.nc - p.nh - p.nb
                c = p.dotmult(p.Aeq[j], x).sum() - p.beq[j]
            else:
                flag = -1
                p.err('error in connection algencan to openopt')
            if any(isnan(c)):
                flag = -1
            return (
             c, flag)

        def evaljac(x, ind):
            """This subroutine must compute the gradient of the ind-th constraint.

            For achieving these objective YOU MUST MODIFY it in the way specified
            below.

            Parameters of the subroutine:

            On Entry:

            x        double precision x(n),
                     current point,

            ind      integer,
                     index of the constraint whose gradient will be computed,

            On Return

            nnzjac   integer,
                     number of perhaps-non-null elements of the computed
                     gradient,

            indjac   integer indjac(nnzjac),
                     see below,

            valjac   double precision valjac(nnzjac),
                     the non-null value of the partial derivative of the i-th
                     constraint with respect to the indjac(k)-th variable must
                     be saved at valjac(k).

            flag     integer
                     You must set it to any number different of 0 (zero) if
                     some error ocurred during the evaluation of the
                     constraint. (For example, trying to compute the square
                     root of a negative number, dividing by zero or a very
                     small number, etc.) If everything was o.k. you must set
                     it equal to zero.
            """
            flag = 0
            i = ind - 1
            if i < p.nc:
                dc = p.dc(x, i)
            elif p.nc <= i < p.nc + p.nh:
                dc = p.dh(x, i - p.nc)
            elif p.nc + p.nh <= i < p.nc + p.nh + p.nb:
                j = i - p.nc - p.nh
                dc = p.A[j]
            elif i < p.nc + p.nh + p.nb + p.nbeq:
                j = i - p.nc - p.nh - p.nb
                dc = p.Aeq[j]
            else:
                p.err('error in connection algencan to openopt')
            dc = dc.flatten()
            if any(isnan(dc)):
                flag = -1
                if p.debug:
                    p.warn('algencan: nan in jacobian')
            indjac, = dc.nonzero()
            valjac = dc[indjac]
            nnzjac = indjac.size
            return (
             indjac, valjac, nnzjac, flag)

        def evalhc(x, ind):
            pass

        def evalhlp(x, m, lambda_, p, goth):
            pass

        def evalfc(*args, **kwargs):
            pass

        def evalgjac(*args, **kwargs):
            pass

        def evalhl(*args, **kwargs):
            pass

        def endp(x, l, u, m, lambda_, equatn, linear):
            """This subroutine can be used to do some extra job.

            This subroutine can be used to do some extra job after the solver
            has found the solution, like some extra statistics, or to save the
            solution in some special format or to draw some graphical
            representation of the solution. If the information given by the
            solver is enough for you then leave the body of this subroutine
            empty.

            Parameters of the subroutine:

            The parameters of this subroutine are the same parameters of
            subroutine inip. But in this subroutine there are not output
            parameter. All the parameters are input parameters.
            """
            p.xk = x.copy()

        param = {'epsfeas': p.contol, 'epsopt': p.gtol, 'iprint': 0, 'ncomp': 5, 'maxtotit': p.maxIter, 'maxtotfc': p.maxFunEvals}
        pywrapper.solver(evalf, evalg, evalh, evalc, evaljac, evalhc, evalfc, evalgjac, evalhl, evalhlp, inip, endp, param)
        if p.istop == 0:
            p.istop = SMALL_DF
            p.msg = '|| gradient F(X[k]) || < gtol'