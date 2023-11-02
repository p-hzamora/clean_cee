# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\nlp_4.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt import NLP
from numpy import cos, arange, ones, asarray, zeros, mat, array, sin, cos, sign, abs, inf
N = 1500
K = 50
p = NLP((lambda x: abs(x - 5).sum()), 8 * cos(arange(N)), iprint=50, maxIter=1000.0)
p.df = lambda x: sign(x - 5)
p.lb = 5 * ones(N) + sin(arange(N)) - 0.1
p.ub = 5 * ones(N) + sin(arange(N)) + 0.1
p.lb[:(N / 4)] = -inf
p.ub[(3 * N / 4):] = inf
p.contol = 1e-06
p.plot = 1
p.maxFunEvals = 10000000.0
p.name = 'nlp_4'
p.debug = 1
solver = 'ralg'
solver = 'gsubg'
solver = 'algencan'
r = p.solve(solver, xlabel='time', fTol=10, debug=0, maxIter=5500, plot=0, maxTime=1000, ftol=1e-08, xtol=1e-06, iprint=1, showLS=0, showFeas=0, show_hs=0)