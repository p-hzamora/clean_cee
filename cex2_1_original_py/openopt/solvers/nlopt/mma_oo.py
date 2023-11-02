# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\nlopt\mma_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from NLOPT_AUX import NLOPT_AUX
from NLOPT_BASE import NLOPT_BASE
import nlopt

class mma(NLOPT_BASE):
    __name__ = 'mma'
    __alg__ = 'Method of Moving Asymptotes'
    __optionalDataThatCanBeHandled__ = [
     'lb', 'ub', 'c', 'h', 'A', 'b', 'Aeq', 'beq']

    def __init__(self):
        pass

    def __solver__(self, p):
        NLOPT_AUX(p, nlopt.LD_MMA)