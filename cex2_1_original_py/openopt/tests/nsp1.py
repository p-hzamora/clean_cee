# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\tests\nsp1.pyc
# Compiled at: 2012-12-08 11:04:59
"""
Example:
Solving nonsmooth problem
|x1| + 1.2|x2| + 1.44|x3| + ... + 1.2^N |xN| -> min
N=75
x0 = [cos(1), cos(2), ..., cos(N)]
x_opt = all-zeros
f_opt = 0
"""
from .numpy import *
from openopt import NSP
N = 1000
K = 10
P = 1.0002
P2 = 1.001
a = 3.5
f1 = lambda x: sum(abs(x) ** P)
f2 = lambda x: sum(a ** (3 + arange(K)) * abs(x[:K]) ** P2)
f = lambda x: f1(x) + f2(x)
df1 = lambda x: P * sign(x) * abs(x) ** (P - 1)
df2 = lambda x: hstack((a ** (3 + arange(K)) * P2 * abs(x[:K]) ** (P2 - 1) * sign(x[:K]), zeros(N - K)))
df = lambda x: df1(x) + df2(x)
x0 = cos(1 + asfarray(range(N)))
solvers = [
 'r2', 'ipopt', 'algencan', 'ralg']
solvers = ['r2', 'algencan', 'ralg']
solvers = [
 'r2', 'lincher']
solvers = ['ralg']
colors = [
 'r', 'b', 'k', 'g']
maxIter = 1000
for i, solver in enumerate(solvers):
    p = NSP(f, x0, df=df, xtol=1e-07, maxIter=maxIter, maxTime=150, ftol=1e-07)
    r = p.solve(solver, maxVectorNum=35, iprint=1, showLS=0, plot=0, color=colors[i], show=solver == solvers[-1])

print 'f_opt:', r.ff