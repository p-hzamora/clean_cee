# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\nlp_ALGENCAN.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt import NLP
from numpy import cos, arange, ones, asarray, zeros, mat, array
N = 50
f = lambda x: ((x - 1) ** 4).sum()
x0 = cos(arange(N))
p = NLP(f, x0, maxIter=1000.0, maxFunEvals=100000.0)
p.df = lambda x: 4 * (x - 1) ** 3
p.lb = -5 * ones(N)
p.ub = 15 * ones(N)
p.ub[4] = -2.5
p.lb[5], p.ub[5] = (3.5, 4.5)
p.A = zeros((3, N))
p.A[(0, 9)] = 1
p.A[(0, 19)] = 1
p.A[1, 10:12] = -1
p.A[2] = -ones(N)
p.b = [1.5, -1.6, -1.1 * N]
p.Aeq = zeros(N)
p.Aeq[20:22] = 1
p.beq = 2.5
p.c = lambda x: [
 2 * x[0] ** 4 - 1.0 / 32, x[1] ** 2 + x[2] ** 2 - 1.0 / 8, x[25] ** 2 + x[35] ** 2 + x[25] * x[35] - 2.5]

def DC(x):
    r = zeros((3, N))
    r[(0, 0)] = 8 * x[0] ** 3
    r[(1, 1)] = 2 * x[1]
    r[(1, 2)] = 2 * x[2]
    r[(2, 25)] = 2 * x[25] + x[35]
    r[(2, 35)] = 2 * x[35] + x[25]
    return r


p.dc = DC
p.h = lambda x: (
 10000.0 * (x[-1] - 1) ** 4, (x[-2] - 1.5) ** 4)

def DH(x):
    r = zeros((2, p.n))
    r[(0, -1)] = 40000.0 * (x[-1] - 1) ** 3
    r[(1, -2)] = 4 * (x[-2] - 1.5) ** 3
    return r


p.dh = DH
p.contol = 0.001
p.gtol = 1e-05
p.checkdf()
p.checkdc()
p.checkdh()
p.plot = 0
p.iprint = 0
p.df_iter = 4
p.maxTime = 4000
p.debug = 1
r = p.solve('ralg')