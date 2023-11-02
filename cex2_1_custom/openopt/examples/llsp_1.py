# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\llsp_1.pyc
# Compiled at: 2012-12-08 11:04:59
import sys
sys.path.append('/home/dmitrey/OOSuite/OpenOpt')
from numpy import empty, sin, cos, arange
from openopt import LLSP
M, N = (1500, 1000)
C = empty((M, N))
d = empty(M)
for j in range(M):
    d[j] = 1.5 * N + 80 * sin(j)
    C[j] = 8 * sin(4.0 + arange(N)) + 15 * cos(j)

p = LLSP(C, d)
r = p.solve('lsmr')
print 'f_opt: %f' % r.ff