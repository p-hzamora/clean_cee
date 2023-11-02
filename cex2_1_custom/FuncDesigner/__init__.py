# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: FuncDesigner\__init__.pyc
# Compiled at: 2013-05-17 08:27:06
import os, sys
curr_dir = ('').join([ elem + os.sep for elem in __file__.split(os.sep)[:-1] ])
sys.path += [curr_dir]
__version__ = '0.45'
from ooVar import oovar, oovars
from ooFun import oofun, AND, OR, NOT, NAND, NOR, XOR
from ooSystem import ooSystem as oosystem
from translator import FuncDesignerTranslator as ootranslator
from ooPoint import ooPoint as oopoint, ooMultiPoint
from baseClasses import Stochastic as _Stochastic
from FDmisc import FuncDesignerException, _getDiffVarsID, _getAllAttachedConstraints, broadcast
try:
    import distribution
    from distribution import P, mean, var, std
except ImportError:

    def sp_err(self, *args, **kw):
        raise FuncDesignerException('\n        to use FuncDesigner stochastic programming \n        you should have FuncDesigner with its stochastic module installed\n        (this addon is commercial, free for research/educational small-scale problems only).\n        Visit http://openopt.org/StochasticProgramming for more details.\n        ')


    class Distribution:
        __getattr__ = sp_err


    distribution = Distribution()
    P = mean = var = std = sp_err

from ooarray import ooarray
from numpy import ndarray

def IMPLICATION(condition, *args):
    if condition is False:
        return True
    if len(args) == 1 and isinstance(args[0], (tuple, set, list, ndarray)):
        if condition is not True:
            return ooarray([ IMPLICATION(condition, elem) for elem in args[0] ])
        return args[0]
    if len(args) > 1:
        if condition is not True:
            return ooarray([ IMPLICATION(condition, elem) for elem in args ])
        return args
    if condition is not True:
        return NOT(condition & NOT(args[0]))
    return args[0]


ifThen = IMPLICATION
from sle import sle
from ode import ode
from dae import dae
from overloads import *
from stencils import d, d2
from interpolate import scipy_InterpolatedUnivariateSpline as interpolator
from integrate import integrator
isE = False
try:
    import enthought
    isE = True
except ImportError:
    pass

try:
    import envisage, mayavi
    isE = True
except ImportError:
    pass

try:
    import xy
    isE = False
except ImportError:
    pass

if isE:
    s = '\n    Seems like you are using OpenOpt from \n    commercial Enthought Python Distribution;\n    consider using free GPL-licensed alternatives\n    PythonXY (http://www.pythonxy.com) or\n    Sage (http://sagemath.org) instead.\n    '
    print s
del isE
del curr_dir
del os
del sys