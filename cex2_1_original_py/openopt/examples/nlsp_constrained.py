# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\nlsp_constrained.pyc
# Compiled at: 2012-12-08 11:04:59
"""
Solving system of equations:
x[0]**3+x[1]**3-9 = 0
x[0]-0.5*x[1] = 0
cos(x[2])+x[0]-1.5 = 0
with some constraints:
150 <= x[2] <= 158
and possible non-linear constraint:
(x[2] - 150.8)**2 <= 1.5

Note:
1. Using Ax <= b constraints is also allowed
2. You can try using equality constraints (h(x)=0, Aeq x = beq) as well.
3. Required function tolerance is p.ftol, constraints tolerance is p.contol,
and hence using h(x)=0 constraints is not 100% same
to some additional f coords
"""
from openopt import SNLE
from .numpy import *
f = lambda x: (
 x[0] ** 3 + x[1] ** 3 - 9, x[0] - 0.5 * x[1], cos(x[2]) + x[0] - 1.5)

def df(x):
    df = zeros((3, 3))
    df[(0, 0)] = 3 * x[0] ** 2
    df[(0, 1)] = 3 * x[1] ** 2
    df[(1, 0)] = 1
    df[(1, 1)] = -0.5
    df[(2, 0)] = 1
    df[(2, 2)] = -sin(x[2])
    return df


x0 = [
 8, 15, 80]
p = SNLE(f, x0, df=df, maxFunEvals=100000.0, iprint=10, plot=1, ftol=1e-08, contol=1e-15)
p.lb, p.ub = [
 -inf] * 3, [inf] * 3
p.lb[2], p.ub[2] = (145, 150)
p.c = lambda x: (x[2] - 146) ** 2 - 1.5
p.dc = lambda x: asfarray((0, 0, 2 * (x[2] - 146)))
r = p.solve('nlp:ralg', xlabel='iter', iprint=10, plot=1)
print 'solution: %s' % r.xf
print 'max residual: %e' % r.ff