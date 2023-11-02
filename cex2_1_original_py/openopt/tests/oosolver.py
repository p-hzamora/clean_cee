# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\tests\oosolver.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt import oosolver, NLP
ipopt = oosolver('ipopt', color='r')
ralg = oosolver('ralg', color='k', alp=4.0)
solvers = [ralg, ipopt]
for solver in solvers:
    assert solver.isInstalled, 'solver ' + solver.__name__ + ' is not installed'
    p = NLP(x0=15, f=(lambda x: x ** 4), df=(lambda x: 4 * x ** 3), iprint=0)
    r = p.solve(solver, plot=1, show=solver == solvers[-1])