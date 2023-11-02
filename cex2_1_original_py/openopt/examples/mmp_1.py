# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\mmp_1.pyc
# Compiled at: 2012-12-08 11:04:59
"""
Example of solving Mini-Max Problem
via converter to NLP

latter works via solving NLP
t -> min
subjected to
t >= f0(x)
t >= f1(x)
...
t >= fk(x)

Splitting f into separate funcs could benefit some solvers
(ralg, algencan; see NLP docpage for more details)
but is not implemented yet
"""
from .numpy import *
from .openopt import *
n = 15
f1 = lambda x: (x[0] - 15) ** 2 + (x[1] - 80) ** 2 + (x[2:] ** 2).sum()
f2 = lambda x: (x[1] - 15) ** 2 + (x[2] - 8) ** 2 + (abs(x[3:] - 100) ** 1.5).sum()
f3 = lambda x: (x[2] - 8) ** 2 + (x[0] - 80) ** 2 + (abs(x[4:] + 150) ** 1.2).sum()
f = [f1, f2, f3]
lb = [
 0] * n
ub = [15, inf, 80] + (n - 3) * [inf]
A = array([[4, 5, 6] + [0] * (n - 3), [80, 8, 15] + [0] * (n - 3)])
b = [100, 350]
Aeq = [
 15, 8, 80] + [0] * (n - 3)
beq = 90
c1 = lambda x: x[0] + (x[1] / 8) ** 2 - 15
c2 = lambda x: x[0] + (x[2] / 80) ** 2 - 15
c = [c1, c2]
h = lambda x: x[0] + x[2] ** 2 - x[1]
x0 = [
 0, 1, 2] + [1.5] * (n - 3)
p = MMP(f, x0, lb=lb, ub=ub, A=A, b=b, Aeq=Aeq, beq=beq, c=c, h=h, xtol=1e-06, ftol=1e-06)
p.plot = 1
r = p.solve('nlp:ipopt', iprint=50, maxIter=1000.0)
print 'MMP result:', r.ff
F = lambda x: max([f1(x), f2(x), f3(x)])
p = NSP(F, x0, iprint=50, lb=lb, ub=ub, c=c, h=h, A=A, b=b, Aeq=Aeq, beq=beq, xtol=1e-06, ftol=1e-06)
r_nsp = p.solve('ipopt', maxIter=1000.0)
print 'NSP result:', r_nsp.ff, 'difference:', r_nsp.ff - r.ff