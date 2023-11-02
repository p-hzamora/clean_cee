# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\glp_2.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt import GLP
from numpy import *
f = lambda x: (x[0] - 1.5) ** 2 + sin(0.8 * x[1] ** 2 + 15) ** 4 + cos(0.8 * x[2] ** 2 + 15) ** 4 + (x[3] - 7.5) ** 4
p = GLP(f, lb=-ones(4), ub=ones(4), maxIter=1000.0, maxFunEvals=100000.0, maxTime=3, maxCPUTime=3)
r = p.solve('pswarm', x0=[0, 0, 0, 0], plot=0, debug=1, maxIter=200)
x_opt, f_opt = r.xf, r.ff