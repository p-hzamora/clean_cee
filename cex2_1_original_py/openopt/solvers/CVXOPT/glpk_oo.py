# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\CVXOPT\glpk_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt.kernel.baseSolver import baseSolver
from openopt import OpenOptException

class glpk(baseSolver):
    __name__ = 'glpk'
    __license__ = 'GPL v.2'
    __authors__ = 'http://www.gnu.org/software/glpk + Python bindings from http://abel.ee.ucla.edu/cvxopt'
    __homepage__ = 'http://www.gnu.org/software/glpk'
    __optionalDataThatCanBeHandled__ = [
     'A', 'Aeq', 'b', 'beq', 'lb', 'ub', 'intVars', 'binVars']
    _canHandleScipySparse = True

    def __init__(self):
        try:
            import cvxopt
        except ImportError:
            raise OpenOptException('for solver glpk cvxopt is required, but it was not found')

    def __solver__(self, p):
        from CVXOPT_LP_Solver import CVXOPT_LP_Solver
        return CVXOPT_LP_Solver(p, 'glpk')