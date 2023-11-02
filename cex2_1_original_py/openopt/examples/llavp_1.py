# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\llavp_1.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import empty, sin, cos, arange, ones
from openopt import LLAVP
M, N = (150, 15)
C = empty((M, N))
d = empty(M)
for j in range(M):
    d[j] = 1.5 * N + 80 * sin(j)
    C[j] = 8 * sin(4.0 + arange(N)) + 15 * cos(j)

lb = sin(arange(N))
ub = lb + 1
p = LLAVP(C, d, lb=lb, ub=ub, dump=10, X=ones(N), maxIter=10000.0, maxFunEvals=1e+100)
p.plot = 1
r = p.solve('nsp:ralg', iprint=100, maxIter=1000)
print 'f_opt: %f' % r.ff