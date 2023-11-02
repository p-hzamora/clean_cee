# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\minlp_1.pyc
# Compiled at: 2012-12-08 11:04:59
"""
Example of MINLP
It is recommended to read help(NLP) before
and /examples/nlp_1.py 
"""
from openopt import MINLP
from .numpy import *
N = 150
K = 50
f = lambda x: ((x - 5.45) ** 2).sum()
df = lambda x: 2 * (x - 5.45)
x0 = 8 * cos(arange(N))
p = MINLP(f, x0, df=df, maxIter=1000.0)
p.lb = [
 -6.5] * N
p.ub = [6.5] * N
p.contol = 1.1e-06
p.name = 'minlp_1'
nlpSolver = 'ipopt'
p.discreteVars = {7: range(3, 10), 8: range(3, 10), 9: [2, 3.1, 9]}
p.discrtol = 1.1e-05
r = p.solve('branb', nlpSolver=nlpSolver, plot=False)