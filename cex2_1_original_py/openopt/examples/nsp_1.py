# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\nsp_1.pyc
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
N = 75
objFun = lambda x: sum(1.2 ** arange(len(x)) * abs(x))
x0 = cos(1 + asfarray(range(N)))
p = NSP(objFun, x0, maxFunEvals=10000000.0, xtol=1e-08)
p.maxIter = 5000
p.df = lambda x: 1.2 ** arange(len(x)) * sign(x)
r = p.solve('ralg')
print 'x_opt: %s' % r.xf
print 'f_opt: %f' % r.ff