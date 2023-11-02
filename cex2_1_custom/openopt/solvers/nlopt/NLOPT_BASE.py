# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\nlopt\NLOPT_BASE.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt.kernel.baseSolver import baseSolver

class NLOPT_BASE(baseSolver):
    __license__ = 'LGPL'
    __authors__ = 'Steven G. Johnson'
    _requiresBestPointDetection = True