# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\lp_1.pyc
# Compiled at: 2012-12-08 11:04:59
"""
Example:
Let's concider the problem
15x1 + 8x2 + 80x3 -> min        (1)
subjected to
x1 + 2x2 + 3x3 <= 15              (2)
8x1 +  15x2 +  80x3 <= 80      (3)
8x1  + 80x2 + 15x3 <=150      (4)
100x1 +  10x2 + x3 >= 800     (5)
80x1 + 8x2 + 15x3 = 750         (6)
x1 + 10x2 + 100x3 = 80           (7)
x1 >= 4                                     (8)
-8 >= x2 >= -80                        (9)
"""
from .numpy import *
from openopt import LP
f = array([15, 8, 80])
A = mat('1 2 3; 8 15 80; 8 80 15; -100 -10 -1')
b = [15, 80, 150, -800]
Aeq = mat('80 8 15; 1 10 100')
beq = (750, 80)
lb = [
 4, -80, -inf]
ub = [inf, -8, inf]
p = LP(f, A=A, Aeq=Aeq, b=b, beq=beq, lb=lb, ub=ub)
r = p.minimize('pclp')
print 'objFunValue: %f' % r.ff
print 'x_opt: %s' % r.xf