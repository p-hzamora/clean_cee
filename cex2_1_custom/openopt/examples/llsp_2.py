# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\llsp_2.pyc
# Compiled at: 2012-12-08 11:04:59
__docformat__ = 'restructuredtext en'
from numpy import diag, ones, sin, cos, arange, sqrt, vstack, zeros, dot
from openopt import LLSP, NLP
N = 150
C1 = diag(sqrt(arange(N)))
C2 = (1.5 + arange(N)).reshape(1, -1) * (0.8 + arange(N)).reshape(-1, 1)
C = vstack((C1, C2))
d = arange(2 * N)
lb = -2.0 + sin(arange(N))
ub = 5 + cos(arange(N))
LLSPsolver = 'bvls'
p = LLSP(C, d, lb=lb, ub=ub)
r = p.solve(LLSPsolver)
NLPsolver = 'scipy_lbfgsb'
p2 = LLSP(C, d, lb=lb, ub=ub)
r2 = p2.solve('nlp:' + NLPsolver)
print '###########Results:###########'
print 'LLSP solver ' + LLSPsolver + ':', r.ff
print 'NLP solver ' + NLPsolver + ':', r2.ff