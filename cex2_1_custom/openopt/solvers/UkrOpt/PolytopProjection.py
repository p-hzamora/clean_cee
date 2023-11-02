# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\UkrOpt\PolytopProjection.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt import QP
from numpy import dot, asfarray, ones, zeros, max
from numpy.linalg import norm

def PolytopProjection(data, T=1.0, isProduct=False, solver=None):
    if solver is None:
        solver = 'cvxopt_qp'
    if isProduct:
        H = data
        n = data.shape[0]
        m = len(T)
    else:
        H = dot(data, data.T)
        n, m = data.shape
    f = -asfarray(T) * ones(n)
    p = QP(H, f, lb=zeros(n), iprint=-1, maxIter=150)
    xtol = 1e-06
    if max(T) < 100000.0 * xtol:
        xtol = max(T) / 100000.0
    r = p._solve(solver, ftol=1e-16, xtol=xtol, maxIter=10000)
    sol = r.xf
    if isProduct:
        return r.xf
    else:
        s = dot(data.T, r.xf)
        return (s.flatten(), r.xf)
        return