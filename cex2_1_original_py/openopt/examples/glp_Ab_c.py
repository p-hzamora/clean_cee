# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\glp_Ab_c.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt import GLP
from numpy import *
f = lambda x: (x[0] - 1.5) ** 2 + sin(0.8 * x[1] ** 2 + 15) ** 4 + cos(0.8 * x[2] ** 2 + 15) ** 4 + (x[3] - 7.5) ** 4
lb, ub = -ones(4), ones(4)
A = mat('1 0 0 1; 0 1 0 1')
b = [0.15, 1.5]
c = lambda x: (
 x[0] ** 2 + x[2] ** 2 - 0.15, 1.5 * x[0] ** 2 + x[1] ** 2 - 1.5)
p = GLP(f, lb=lb, ub=ub, A=A, b=b, c=c, maxIter=250, maxFunEvals=100000.0, maxTime=30, maxCPUTime=30)
r = p.solve('de', mutationRate=0.15, plot=1)
x_opt, f_opt = r.xf, r.ff