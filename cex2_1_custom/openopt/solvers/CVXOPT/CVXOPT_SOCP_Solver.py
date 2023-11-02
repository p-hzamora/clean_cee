# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\CVXOPT\CVXOPT_SOCP_Solver.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import asarray, ones, all, isfinite, copy, nan, concatenate, array, hstack, vstack, atleast_1d
from openopt.kernel.ooMisc import WholeRepr2LinConst, xBounds2Matrix
from cvxopt_misc import *
import cvxopt.solvers as cvxopt_solvers
from cvxopt.base import matrix
from openopt.kernel.setDefaultIterFuncs import SOLVED_WITH_UNIMPLEMENTED_OR_UNKNOWN_REASON, IS_MAX_ITER_REACHED, IS_MAX_TIME_REACHED, FAILED_WITH_UNIMPLEMENTED_OR_UNKNOWN_REASON, UNDEFINED

def CVXOPT_SOCP_Solver(p, solverName):
    if solverName == 'native_CVXOPT_SOCP_Solver':
        solverName = None
    cvxopt_solvers.options['maxiters'] = p.maxIter
    cvxopt_solvers.options['feastol'] = p.contol
    cvxopt_solvers.options['abstol'] = p.ftol
    if p.iprint <= 0:
        cvxopt_solvers.options['show_progress'] = False
        cvxopt_solvers.options['LPX_K_MSGLEV'] = 0
        cvxopt_solvers.options['MSK_IPAR_LOG'] = 0
    xBounds2Matrix(p)
    f = copy(p.f).reshape(-1, 1)
    Gq, hq = [], []
    C, d, q, s = (
     p.C, p.d, p.q, p.s)
    for i in range(len(q)):
        Gq.append(Matrix(vstack((-atleast_1d(q[i]), -atleast_1d(C[i])))))
        hq.append(matrix(hstack((atleast_1d(s[i]), atleast_1d(d[i]))), tc='d'))

    sol = cvxopt_solvers.socp(Matrix(p.f), Gl=Matrix(p.A), hl=Matrix(p.b), Gq=Gq, hq=hq, A=Matrix(p.Aeq), b=Matrix(p.beq), solver=solverName)
    p.msg = sol['status']
    if p.msg == 'optimal':
        p.istop = SOLVED_WITH_UNIMPLEMENTED_OR_UNKNOWN_REASON
    else:
        p.istop = -100
    if sol['x'] is not None:
        p.xf = asarray(sol['x']).flatten()
        p.ff = sum(p.dotmult(p.f, p.xf))
    else:
        p.ff = nan
        p.xf = nan * ones([p.n, 1])
    return