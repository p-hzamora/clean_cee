# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\milp_1.pyc
# Compiled at: 2012-12-08 11:04:59
__docformat__ = 'restructuredtext en'
from .numpy import *
from openopt import MILP
f = [
 1, 2, 3, 4, 5, 4, 2, 1]
intVars = [
 4, 7]
lb = -1.5 * ones(8)
ub = 15 * ones(8)
A = zeros((5, 8))
b = zeros(5)
for i in xrange(5):
    for j in xrange(8):
        A[(i, j)] = -8 + sin(8 * i) + cos(15 * j)

    b[i] = -150 + 80 * sin(80 * i)

p = MILP(f=f, lb=lb, ub=ub, A=A, b=b, intVars=intVars, goal='min')
r = p.solve('lpSolve')
print 'f_opt: %f' % r.ff
print 'x_opt: %s' % r.xf