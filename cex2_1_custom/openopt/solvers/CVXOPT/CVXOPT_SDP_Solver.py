# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\CVXOPT\CVXOPT_SDP_Solver.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import asarray, ones, all, isfinite, copy, nan, concatenate, array, asfarray, zeros
from openopt.kernel.ooMisc import WholeRepr2LinConst, xBounds2Matrix
from cvxopt_misc import *
import cvxopt.solvers as cvxopt_solvers
from cvxopt.base import matrix
from openopt.kernel.setDefaultIterFuncs import SOLVED_WITH_UNIMPLEMENTED_OR_UNKNOWN_REASON, IS_MAX_ITER_REACHED, IS_MAX_TIME_REACHED, FAILED_WITH_UNIMPLEMENTED_OR_UNKNOWN_REASON, UNDEFINED

def converter_to_CVXOPT_SDP_Matrices_from_OO_SDP_Class(OO_SDP_Class_2D_Dict_S, nVars):
    a = OO_SDP_Class_2D_Dict_S
    R = {}
    for i, j in a.keys():
        if i not in R.keys():
            R[i] = zeros((nVars, asarray(a[(i, 0)]).size))
        R[i][j] = asfarray(a[(i, j)]).flatten()

    r = []
    for i in R.keys():
        r.append(Matrix(R[i].T))

    return r


def DictToList(d):
    i = 0
    r = []
    while i in d.keys():
        r.append(matrix(d[i], tc='d'))
        i += 1

    return r


def CVXOPT_SDP_Solver(p, solverName):
    if solverName == 'native_CVXOPT_SDP_Solver':
        solverName = None
    cvxopt_solvers.options['maxiters'] = p.maxIter
    cvxopt_solvers.options['feastol'] = p.contol
    cvxopt_solvers.options['abstol'] = p.ftol
    if p.iprint <= 0:
        cvxopt_solvers.options['show_progress'] = False
        cvxopt_solvers.options['LPX_K_MSGLEV'] = 0
    xBounds2Matrix(p)
    f = copy(p.f).reshape(-1, 1)
    sol = cvxopt_solvers.sdp(Matrix(p.f), Matrix(p.A), Matrix(p.b), converter_to_CVXOPT_SDP_Matrices_from_OO_SDP_Class(p.S, p.n), DictToList(p.d), Matrix(p.Aeq), Matrix(p.beq), solverName)
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
        p.xf = nan * ones(p.n)
    return