# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\GUI_1.pyc
# Compiled at: 2012-12-08 11:04:59
"""
OpenOpt GUI:
     function manage() usage example
"""
from openopt import NLP, manage
from numpy import cos, arange, ones, asarray, abs, zeros
N = 50
M = 5
p = NLP((lambda x: ((x - M) ** 2).sum()), cos(arange(N)))
p.lb, p.ub = -6 * ones(N), 6 * ones(N)
p.lb[3] = 5.5
p.ub[4] = 4.5
p.c = lambda x: [2 * x[0] ** 4 - 32, x[1] ** 2 + x[2] ** 2 - 8]
p.h = ((lambda x: 10.0 * (x[-1] - 1) ** 4), (lambda x: (x[-2] - 1.5) ** 4))
minTime = 1.5
p.name = 'GUI_example'
p.minTime = minTime
r = manage(p, 'ralg', plot=1, start=True)
if r is not None:
    print 'objfunc val:', r.ff