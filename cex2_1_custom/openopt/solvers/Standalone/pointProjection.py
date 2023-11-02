# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\Standalone\pointProjection.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import *
from openopt import *

def pointProjection(x, lb, ub, A, b, Aeq, beq):
    n = x.size
    p = QP(H=eye(n), f=-x, A=A, b=b, Aeq=Aeq, beq=beq, lb=lb, ub=ub)
    r = p.solve('cvxopt_qp')
    return r.xf


if __name__ == '__main__':
    x = array((1, 2, 3))
    lb, ub = (None, None)
    A = [3, 4, 5]
    b = -15
    Aeq, beq = (None, None)
    proj = pointProjection(x, lb, ub, A, b, Aeq, beq)
    print proj