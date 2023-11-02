# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\tests\rastrigin.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt import GLP
from numpy import *
f = lambda x: (x * x - 10 * cos(2 * pi * x) + 10).sum()
p = GLP(f, lb=-ones(10) * 5.12, ub=ones(10) * 5.12, maxIter=1000.0, maxFunEvals=100000.0, maxTime=10, maxCPUTime=10)
r = p.solve('de', plot=0)
x_opt, f_opt = r.xf, r.ff
print x_opt