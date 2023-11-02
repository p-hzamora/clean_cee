# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\nlopt\bobyqa_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from NLOPT_AUX import NLOPT_AUX
from NLOPT_BASE import NLOPT_BASE
import nlopt

class bobyqa(NLOPT_BASE):
    __name__ = 'bobyqa'
    __alg__ = 'Bound constrained Optimization BY Quadratic Approximation'
    __authors__ = 'Michael JD Powell'
    __optionalDataThatCanBeHandled__ = ['lb', 'ub']
    __isIterPointAlwaysFeasible__ = True
    funcForIterFcnConnection = 'f'

    def __solver__(self, p):
        NLOPT_AUX(p, nlopt.LN_BOBYQA)