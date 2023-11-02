# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\lunp_1.pyc
# Compiled at: 2012-12-08 11:04:59
__docformat__ = 'restructuredtext en'
from .numpy import *
from openopt import LUNP
M, N = (1500, 150)
C = empty((M, N))
d = empty(M)
for j in xrange(M):
    d[j] = 1.5 * N + 80 * sin(j)
    C[j] = 8 * sin(4.0 + arange(N)) + 15 * cos(j)

lb = sin(arange(N))
ub = lb + 1
p = LUNP(C, d, lb=lb, ub=ub)
r = p.solve('lp:glpk', iprint=-1)
print 'f_opt:', r.ff