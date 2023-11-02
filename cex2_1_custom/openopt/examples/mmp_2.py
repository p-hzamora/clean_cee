# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\mmp_2.pyc
# Compiled at: 2012-12-08 11:04:59
"""
Example of solving Mini-Max Problem
max { (x0-15)^2+(x1-80)^2, (x1-15)^2 + (x2-8)^2, (x2-8)^2 + (x0-80)^2 } -> min
Currently nsmm is single OO solver available for MMP
It defines function F(x) = max_i {f[i](x)}
and solves NSP F(x) -> min using solver ralg.
It's very far from specialized solvers (like MATLAB fminimax),
but it's better than having nothing at all,
and allows using of nonsmooth and noisy funcs.
This solver is intended to be enhanced in future.
"""
from .numpy import *
from .openopt import *
f1 = lambda x: (x[0] - 15) ** 2 + (x[1] - 80) ** 2
f2 = lambda x: (x[1] - 15) ** 2 + (x[2] - 8) ** 2
f3 = lambda x: (x[2] - 8) ** 2 + (x[0] - 80) ** 2
f = [f1, f2, f3]
lb = [
 0] * 3
ub = [15, inf, 80]
A = mat('4 5 6; 80 8 15')
b = [100, 350]
Aeq = mat('15 8 80')
beq = 90
c1 = lambda x: x[0] + (x[1] / 8) ** 2 - 15
c2 = lambda x: x[0] + (x[2] / 80) ** 2 - 15
c = [c1, c2]
h = lambda x: x[0] + x[2] ** 2 - x[1]
x0 = [
 0, 1, 2]
p = MMP(f, x0, lb=lb, ub=ub, A=A, b=b, Aeq=Aeq, beq=beq, c=c, h=h, xtol=1e-06, ftol=1e-06)
r = p.solve('nsmm', iprint=1, NLPsolver='ralg', maxIter=1000.0, minIter=100.0)
print 'MMP result:', r.ff
F = lambda x: max([f1(x), f2(x), f3(x)])
p = NSP(F, x0, lb=lb, ub=ub, c=c, h=h, A=A, b=b, Aeq=Aeq, beq=beq, xtol=1e-06, ftol=1e-06)
r_nsp = p.solve('ralg')