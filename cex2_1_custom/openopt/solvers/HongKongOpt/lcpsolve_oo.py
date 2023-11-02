# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\HongKongOpt\lcpsolve_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import isfinite, any, hstack
from openopt.kernel.baseSolver import *
from sqlcp import sqlcp as SQLCP
from numpy.linalg import LinAlgError
from LCPSolve import LCPSolve

class lcpsolve(baseSolver):
    __name__ = 'lcp'
    __license__ = 'MIT'
    __authors__ = 'Rob Dittmar, Enzo Michelangeli and IT Vision Ltd'
    __alg__ = "Lemke's Complementary Pivot algorithm"
    __optionalDataThatCanBeHandled__ = []
    __info__ = '  '
    pivtol = 1e-08

    def __init__(self):
        pass

    def __solver__(self, p):
        w, z, retcode = LCPSolve(p.M, p.q, pivtol=self.pivtol)
        p.xf = hstack((w, z))
        if retcode[0] == 1:
            p.istop = 1000
            p.msg = 'success'
        elif retcode[0] == 2:
            p.istop = -1000
            p.msg = 'ray termination'