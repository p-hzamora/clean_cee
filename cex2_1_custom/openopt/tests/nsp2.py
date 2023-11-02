# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\tests\nsp2.pyc
# Compiled at: 2012-12-08 11:04:59
"""
Example:
Solving nonsmooth problem
#K|x1| + |x2| -> min
#x0 = [10^4, 10]
x_opt = all-zeros
f_opt = 0
"""
from .numpy import *
from openopt import NSP
K = 1000
f = lambda x: abs(x[0]) + abs(x[1]) * K + abs(x[2]) * K ** 2
x0 = [
 1000, 0.011, 0.01]
df = lambda x: [
 sign(x[0]), sign(x[1]) * K, sign(x[2]) * K ** 2]
solvers = [
 'r2', 'ipopt', 'algencan', 'ralg']
solvers = ['r2', 'algencan', 'ralg']
solvers = [
 'r2', 'lincher']
solvers = ['ralg']
solvers = ['r2']
colors = [
 'r', 'b', 'k', 'g']
maxIter = 1000
for i, solver in enumerate(solvers):
    p = NSP(f, x0, df=df, xtol=1e-11, ftol=1e-10, maxIter=maxIter, maxTime=150)
    r = p.solve(solver, maxVectorNum=4, iprint=1, showLS=0, plot=0, color=colors[i], show=solver == solvers[-1])

print 'f_opt:', r.ff