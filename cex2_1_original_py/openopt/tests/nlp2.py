# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\tests\nlp2.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import log
from openopt import NLP
x0 = [
 4, 5, 6]
f = lambda x: x[0] ** 4 + x[1] ** 4 + x[2] ** 4
df = lambda x: [4 * x[0] ** 3, 4 * x[1] ** 3, 4 * x[2] ** 3]
h = lambda x: [(x[0] - 1) ** 2, (x[1] - 1) ** 4]
dh = lambda x: [[2 * (x[0] - 1), 0, 0], [0, 4 * (x[1] - 1) ** 3, 0]]
colors = ['r', 'b', 'g', 'k', 'y']
solvers = ['ralg', 'scipy_cobyla', 'algencan', 'ipopt', 'scipy_slsqp']
solvers = ['ralg', 'algencan']
contol = 1e-08
gtol = 1e-08
for i, solver in enumerate(solvers):
    p = NLP(f, x0, df=df, h=h, dh=dh, gtol=gtol, diffInt=0.1, contol=contol, iprint=1000, maxIter=100000.0, maxTime=50, maxFunEvals=100000000.0, color=colors[i], plot=0, show=i == len(solvers))
    p.checkdh()
    r = p.solve(solver)