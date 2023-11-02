# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\sle_1.pyc
# Compiled at: 2012-12-08 11:04:59
__docformat__ = 'restructuredtext en'
from .numpy import *
from openopt import SLE
N = 1000
C = empty((N, N))
d = 1.5 + 80 * sin(arange(N))
for j in xrange(N):
    C[j] = 8 * sin(4.0 + arange(j, N + j) ** 2) + 15 * cos(j)

p = SLE(C, d)
r = p.solve()
print 'max residual: %e' % r.ff