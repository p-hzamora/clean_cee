# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\CVXOPT\cvxopt_misc.pyc
# Compiled at: 2012-12-08 11:04:59
import cvxopt, cvxopt.base
from openopt.kernel.ooMisc import Len
matrix = cvxopt.base.matrix
sparse = cvxopt.base.sparse
Sparse = cvxopt.spmatrix
from numpy import asfarray, copy, array, prod
from openopt.kernel.nonOptMisc import isspmatrix

def Matrix(x):
    if x is None or hasattr(x, 'shape') and prod(x.shape) == 0:
        return
    if isspmatrix(x):
        if min(x.shape) > 1:
            from scipy.sparse import find
            I, J, values = find(x)
            return Sparse(array(values, float).tolist(), I.tolist(), J.tolist(), x.shape)
        x = x.toarray()
    x = asfarray(x)
    if x.ndim > 1 and x.nonzero()[0].size < 0.3 * x.size:
        return sparse(x.tolist()).T
    else:
        return matrix(x, tc='d')
        return


def xBounds2cvxoptMatrix(p):
    """
    transforms lb - ub bounds into (A, x) <= b, (Aeq, x) = beq conditions
    this func is developed for those solvers that can handle lb, ub only via c(x)<=0, h(x)=0
    """
    indLB, indUB, indEQ = where(isfinite(p.lb) & ~(p.lb == p.ub))[0], where(isfinite(p.ub) & ~(p.lb == p.ub))[0], where(p.lb == p.ub)[0]
    initLenB = Len(p.b)
    initLenBeq = Len(p.beq)
    nLB, nUB, nEQ = Len(indLB), Len(indUB), Len(indEQ)
    if nLB > 0 or nUB > 0:
        A, b = copy(p.A), copy(p.b)
        p.A = zeros([Len(p.b) + nLB + nUB, p.n])
        p.b = zeros(Len(p.b) + nLB + nUB)
        p.b[:(Len(b))] = b.flatten()
        p.A[:(Len(b))] = A
        for i in range(len(indLB)):
            p.A[(initLenB + i, indLB[i])] = -1
            p.b[initLenB + i] = -p.lb[indLB[i]]

        for i in range(len(indUB)):
            p.A[(initLenB + len(indLB) + i, indUB[i])] = 1
            p.b[initLenB + len(indLB) + i] = p.ub[indUB[i]]

    if nEQ > 0:
        Aeq, beq = copy(p.Aeq), copy(p.beq)
        p.Aeq = zeros([Len(p.beq) + nEQ, p.n])
        p.beq = zeros(Len(p.beq) + nEQ)
        p.beq[:(Len(beq))] = beq
        p.Aeq[:(Len(beq))] = Aeq
        for i in range(len(indEQ)):
            p.Aeq[(initLenBeq + i, indEQ[i])] = 1
            p.beq[initLenBeq + i] = p.lb[indEQ[i]]

    p.lb = -inf * ones(p.n)
    p.ub = inf * ones(p.n)