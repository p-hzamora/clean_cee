# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\nlp_d2f.pyc
# Compiled at: 2012-12-08 11:04:59
"""
this is an example of using d2f - Hesse matrix (2nd derivatives)
d2c, d2h, d2l are intended to be implemented soon 
and to be connected to ALGENCAN and/or CVXOPT 
and/or other NLP solvers

//Dmitrey
"""
from openopt import NLP
from numpy import cos, arange, ones, asarray, abs, zeros, diag
N = 300
M = 5
ff = lambda x: ((x - M) ** 4).sum()
p = NLP(ff, cos(arange(N)))
p.df = lambda x: 4 * (x - M) ** 3
p.d2f = lambda x: diag(12 * (x - M) ** 2)
r = p.solve('scipy_ncg')
print 'objfunc val: %e' % r.ff