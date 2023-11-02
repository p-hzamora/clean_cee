# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\HongKongOpt\sqlcp_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import isfinite, any
from openopt.kernel.baseSolver import *
from sqlcp import sqlcp as SQLCP
from numpy.linalg import LinAlgError

class sqlcp(baseSolver):
    __name__ = 'sqlcp'
    __license__ = 'MIT'
    __authors__ = 'Enzo Michelangeli'
    __alg__ = 'an SQP implementation'
    __optionalDataThatCanBeHandled__ = ['A', 'Aeq', 'b', 'beq', 'lb', 'ub']
    iterfcnConnected = True
    QPsolver = None
    __info__ = 'SQP solver. Approximates f in x0 with paraboloid with same gradient and hessian,\n    then finds its minimum with a quadratic solver (qlcp by default) and uses it as new point, \n    iterating till changes in x and/or f drop below given limits. \n    Requires the Hessian to be definite positive.\n    The Hessian is initially approximated by its principal diagonal, and then\n    updated at every step with the BFGS method.\n    \n    By default it uses QP solver qlcp (license: MIT), however, latter uses LCP solver LCPSolve, that is "free for education" for now. \n    You can use other QP solver via "oosolver(\'sqlcp\', QPsolver=\'cvxopt_qp\')" or any other, including converters.\n    \n    Copyright (c) 2010 Enzo Michelangeli and IT Vision Ltd\n    '

    def __init__(self):
        pass

    def __solver__(self, p):
        A, b = (p.A, p.b) if p.nb else (None, None)
        Aeq, beq = (p.Aeq, p.beq) if p.nbeq else (None, None)
        lb = p.lb if any(isfinite(p.lb)) else None
        ub = p.ub if any(isfinite(p.ub)) else None

        def callback(x):
            p.iterfcn(x)
            if p.istop:
                return True
            return False

        try:
            SQLCP(p.f, p.x0, df=p.df, A=A, b=b, Aeq=Aeq, beq=beq, lb=p.lb, ub=p.ub, minstep=p.xtol, minfchg=1e-15, qpsolver=self.QPsolver, callback=callback)
        except LinAlgError:
            p.msg = 'linalg error, probably failed to invert Hesse matrix'
            p.istop = -100

        return