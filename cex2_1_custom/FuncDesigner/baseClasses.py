# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: FuncDesigner\baseClasses.pyc
# Compiled at: 2012-11-26 10:00:30
from numpy import ndarray

class OOArray(ndarray):
    pass


class MultiArray(ndarray):
    pass


def distrib_err_fcn(*args, **kw):
    from FDmisc import FuncDesignerException
    raise FuncDesignerException('\n            direct operations (like +, -, *, /, ** etc) on stochastic distributions are forbidden,\n            you should declare FuncDesigner variables, define function(s) on them \n            and then get new distribution via evaluating the obtained oofun(s) on a data point\n            ')


stochasticDistribution = 'stochastic distribution'

class Stochastic:

    def __init__(self):
        self._str = stochasticDistribution

    __repr__ = lambda self: self._str
    __add__ = __mul__ = __pow__ = __rpow__ = __rmul__ = __radd__ = __neg__ = __pos__ = distrib_err_fcn