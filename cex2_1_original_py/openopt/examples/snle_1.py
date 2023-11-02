# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\snle_1.pyc
# Compiled at: 2012-12-08 11:04:59
"""
Solving system of equations:
x[0]**3+x[1]**3-9 = 0
x[0]-0.5*x[1] = 0
cos(x[2])+x[0]-1.5 = 0
"""
from openopt import SNLE
from numpy import asfarray, zeros, cos, sin
f = (
 (lambda x: x[0] ** 3 + x[1] ** 3 - 9), (lambda x: x[0] - 0.5 * x[1]), (lambda x: cos(x[2]) + x[0] - 1.5))
x0 = [
 8, 15, 80]
df = (
 (lambda x: [
  3 * x[0] ** 2, 3 * x[1] ** 2, 0]), (lambda x: [1, -0.5, 0]), (lambda x: [1, 0, -sin(x[2])]))
p = SNLE(f, x0, df=df)
p.plot = 1
p.maxFunEvals = 100000.0
p.iprint = 10
r = p.solve('nlp:ralg', plot=1)
print 'solution: %s' % r.xf
print 'max residual: %e' % r.ff