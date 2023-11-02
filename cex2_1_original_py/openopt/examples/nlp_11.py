# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\nlp_11.pyc
# Compiled at: 2012-12-08 11:04:59
"""
Example:
(x0-5)^2 + (x2-5)^2 + ... +(x149-5)^2 -> min

subjected to

# lb<= x <= ub:
x4 <= 4
8 <= x5 <= 15

# Ax <= b
x0+...+x149 >= 825
x9 + x19 <= 3
x10+x11 <= 9

# Aeq x = beq
x100+x101 = 11

# c(x) <= 0
2*x0^4-32 <= 0
x1^2+x2^2-8 <= 0

# h(x) = 0
(x[149]-1)**6 = 0
(x[148]-1.5)**6 = 0
"""
from openopt import NLP
from numpy import cos, arange, ones, asarray, zeros, mat, array
N = 150
f = lambda x: ((x - 5) ** 2).sum()
df = lambda x: 2 * (x - 5)
x0 = 8 * cos(arange(N))
c = [
 (lambda x: 2 * x[0] ** 4 - 32), (lambda x: x[1] ** 2 + x[2] ** 2 - 8)]
dc0 = lambda x: [
 8 * x[0] ** 3] + [0] * (N - 1)
dc1 = lambda x: [0, 2 * x[1], 2 * x[2]] + [0] * (N - 3)
dc = [dc0, dc1]

def h(x):
    return (
     (x[-1] - 1) ** 6, (x[-2] - 1.5) ** 6)


def dh(x):
    r = zeros((2, N))
    r[(0, -1)] = 6 * (x[-1] - 1) ** 5
    r[(1, -2)] = 6 * (x[-2] - 1.5) ** 5
    return r


lb = -6 * ones(N)
ub = 6 * ones(N)
ub[4] = 4
lb[5], ub[5] = (8, 15)
A = zeros((3, N))
A[(0, 9)] = 1
A[(0, 19)] = 1
A[1, 10:12] = 1
A[2] = -ones(N)
b = [7, 9, -825]
Aeq = zeros((1, N))
Aeq[0, 100:102] = 1
beq = 11
contol = 1e-06
gtol = 1e-07
p = NLP(f, x0, df=df, c=c, dc=dc, h=h, dh=dh, A=A, b=b, Aeq=Aeq, beq=beq, lb=lb, ub=ub, gtol=gtol, contol=contol, iprint=50, maxIter=10000, maxFunEvals=10000000.0, name='NLP_1')
p.plot = 1
p.checkdf()
p.checkdc()
p.checkdh()

def MyIterFcn(p):
    return 0


p.user.mylist = []
solver = 'algencan'
solver = 'ralg'
p.debug = 1
r = p.solve(solver, showRej=1, iprint=1, maxTime=15000, newLinEq=1, callback=MyIterFcn)