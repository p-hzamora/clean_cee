# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\nlp_2.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt import NLP
from numpy import cos, arange, ones, asarray, abs, zeros
N = 30
M = 5
ff = lambda x: ((x - M) ** 2).sum()
p = NLP(ff, cos(arange(N)))
p.df = lambda x: 2 * (x - M)
p.c = lambda x: [2 * x[0] ** 4 - 32, x[1] ** 2 + x[2] ** 2 - 8]

def dc(x):
    r = zeros((2, p.n))
    r[(0, 0)] = 8 * x[0] ** 3
    r[(1, 1)] = 2 * x[1]
    r[(1, 2)] = 2 * x[2]
    return r


p.dc = dc
h1 = lambda x: 10.0 * (x[-1] - 1) ** 4
h2 = lambda x: (x[-2] - 1.5) ** 4
p.h = lambda x: (h1(x), h2(x))

def dh(x):
    r = zeros((2, p.n))
    r[(0, -1)] = 40.0 * (x[-1] - 1) ** 3
    r[(1, -2)] = 4 * (x[-2] - 1.5) ** 3
    return r


p.dh = dh
p.lb = -6 * ones(N)
p.ub = 6 * ones(N)
p.lb[3] = 5.5
p.ub[4] = 4.5
solver = 'ralg'
r = p.solve(solver, maxIter=1504, plot=1)