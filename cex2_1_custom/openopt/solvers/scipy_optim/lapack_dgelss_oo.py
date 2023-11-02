# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\scipy_optim\lapack_dgelss_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from scipy.linalg.flapack import dgelss
from numpy.linalg import norm
from numpy import dot, asfarray, atleast_1d
from openopt.kernel.baseSolver import baseSolver

class lapack_dgelss(baseSolver):
    __name__ = 'lapack_dgelss'
    __license__ = 'BSD'
    __authors__ = 'Univ. of Tennessee, Univ. of California Berkeley, NAG Ltd., Courant Institute, Argonne National Lab, and Rice University'
    __info__ = 'wrapper to LAPACK dgelss routine (double precision), requires scipy & LAPACK 3.0 or newer installed'

    def __init__(self):
        pass

    def __solver__(self, p):
        res = dgelss(p.C, p.d)
        x, info = res[1], res[-1]
        xf = x[:p.C.shape[1]]
        ff = atleast_1d(asfarray(p.F(xf)))
        p.xf = p.xk = xf
        p.ff = p.fk = ff
        if info == 0:
            p.istop = 1000
        else:
            p.istop = -1000