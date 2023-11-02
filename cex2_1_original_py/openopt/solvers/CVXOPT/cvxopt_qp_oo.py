# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\CVXOPT\cvxopt_qp_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt.kernel.baseSolver import baseSolver
from CVXOPT_QP_Solver import CVXOPT_QP_Solver

class cvxopt_qp(baseSolver):
    __name__ = 'cvxopt_qp'
    __license__ = 'LGPL'
    __authors__ = 'http://abel.ee.ucla.edu/cvxopt'
    __alg__ = 'see http://abel.ee.ucla.edu/cvxopt'
    __optionalDataThatCanBeHandled__ = ['A', 'Aeq', 'b', 'beq', 'lb', 'ub']
    properTextOutput = True
    _canHandleScipySparse = True

    def __init__(self):
        pass

    def __solver__(self, p):
        return CVXOPT_QP_Solver(p, 'native_CVXOPT_QP_Solver')