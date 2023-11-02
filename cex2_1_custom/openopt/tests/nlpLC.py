# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\tests\nlpLC.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt import NLP
from numpy import cos, arange, ones, asarray, zeros, mat, array
N = 100
f = lambda x: ((x - 5) ** 2).sum()
df = lambda x: 2 * (x - 5)
x0 = 8 * cos(arange(N))

def c(x):
    r = zeros(N - 1)
    for i in xrange(N - 1):
        r[i] = x[i] ** 2 + x[i + 1] ** 2 - 1

    return r


def dc(x):
    r = zeros((N - 1, N))
    for i in xrange(N - 1):
        r[(i, i)] = 2 * x[i]
        r[(i, i + 1)] = 2 * x[i + 1]

    return r


lb = -6 * ones(N)
ub = 6 * ones(N)
ub[4] = 4
lb[5], ub[5] = (8, 15)
A, b = (None, None)
Aeq, beq = (None, None)
contol = 1e-07
gtol = 1e-07
p = NLP(f, x0, df=df, c=c, dc=dc, gtol=gtol, contol=contol, iprint=50, maxIter=10000, maxFunEvals=10000000.0, name='NLP_1')
p.plot = 0
p.checkdf()
p.checkdc()
p.checkdh()

def MyIterFcn(p):
    return 0


p.user.mylist = []
solver = 'algencan'
solver = 'ralg'
p.debug = 1
r = p.solve(solver, showLS=0, iprint=10, maxTime=50, callback=MyIterFcn)