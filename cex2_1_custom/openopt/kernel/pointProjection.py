# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\pointProjection.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import eye

def pointProjection(x, lb, ub, A, b, Aeq, beq):
    from openopt import QP
    n = x.size
    p = QP(H=eye(n), f=-x, A=A, b=b, Aeq=Aeq, beq=beq, lb=lb, ub=ub)
    r = p.solve('nlp:scipy_slsqp', contol=1e-08, iprint=-1)
    return r.xf