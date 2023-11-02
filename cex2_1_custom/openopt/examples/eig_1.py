# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\eig_1.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt import EIG
import numpy.random as nr
nr.seed(0)
N = 5
A = nr.rand(N, N)
p = EIG(A, goal={'lm': 3})
r = p.solve('arpack')
print r.eigenvalues
print r.eigenvectors