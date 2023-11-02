# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\HongKongOpt\qlcp_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt.kernel.baseSolver import baseSolver
from QPSolve import QPSolve

class qlcp(baseSolver):
    __license__ = 'MIT'
    __authors__ = 'Enzo Michelangeli'
    __name__ = 'qlcp'
    __alg__ = 'Lemke algorithm, using linear complementarity problem'
    __optionalDataThatCanBeHandled__ = [
     'lb', 'ub', 'A', 'b', 'Aeq', 'beq']

    def __init__(self):
        pass

    def __solver__(self, p):
        x, retcode = QPSolve(p.H, p.f, p.A, p.b, p.Aeq, p.beq, p.lb, p.ub)
        if retcode[0] == 1:
            p.istop = 1000
            p.xf = x
        else:
            p.istop = -1