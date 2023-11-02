# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\nllsp_1.pyc
# Compiled at: 2012-12-08 11:04:59
"""
Let us solve the overdetermined nonlinear equations:
a^2 + b^2 = 15
a^4 + b^4 = 100
a = 3.5

Let us concider the problem as
x[0]**2 + x[1]**2 - 15 = 0
x[0]**4 + x[1]**4 - 100 = 0
x[0] - 3.5 = 0

Now we will solve the one using solver scipy_leastsq
"""
from openopt import NLLSP
from .numpy import *
f = lambda x: (
 (x ** 2).sum() - 15, (x ** 4).sum() - 100, x[0] - 3.5)

def df(x):
    r = zeros((3, 2))
    r[(0, 0)] = 2 * x[0]
    r[(0, 1)] = 2 * x[1]
    r[(1, 0)] = 4 * x[0] ** 3
    r[(1, 1)] = 4 * x[1] ** 3
    r[(2, 0)] = 1
    return r


x0 = [
 1.5, 8]
p = NLLSP(f, x0, df=df, xtol=1.5e-08, ftol=1.5e-08)
p.checkdf()
r = p.solve('nlp:ralg', iprint=1, plot=1)
print 'x_opt:', r.xf
print 'funcs Values:', p.f(r.xf)
print 'f_opt:', r.ff, '; sum of squares (should be same value):', (p.f(r.xf) ** 2).sum()