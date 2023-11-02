# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: FuncDesigner\integrate.pyc
# Compiled at: 2011-05-08 10:44:46
from ooFun import oofun, atleast_oofun
import numpy as np
from FDmisc import FuncDesignerException
from translator import FuncDesignerTranslator
from ooPoint import ooPoint as oopoint
from ooVar import oovar
try:
    from scipy import integrate
    scipyInstalled = True
except:
    scipyInstalled = False

def integrator(func, domain, **kwargs):
    if not scipyInstalled:
        raise FuncDesignerException('to use scipy_integrate_quad you should have scipy installed, see scipy.org')
    integration_var, a, b = domain
    if not isinstance(integration_var, oovar):
        raise FuncDesignerException('integration variable must be FuncDesigner oovar')
    a, b, func = atleast_oofun(a), atleast_oofun(b), atleast_oofun(func)

    def f(point=None):
        p2 = point.copy()

        def vect_func(x):
            p2[integration_var] = x
            tmp = func(p2)
            if np.isscalar(tmp):
                return tmp
            if tmp.size == 1:
                return np.asscalar(tmp)
            FuncDesignerException('incorrect data type, probably bug in uncDesigner kernel')

        return integrate.quad(vect_func, a(point), b(point), **kwargs)[0]

    r = oofun(f, None)
    r.fun = lambda *args: f(point=r._Point)
    tmp_f = r._getFunc
    tmp_D = r._D

    def aux_f(*args, **kwargs):
        if isinstance(args[0], dict):
            r._Point = args[0]
        return tmp_f(*args, **kwargs)

    def aux_D(*args, **kwargs):
        raise FuncDesignerException('derivatives from scipy_quad are not implemented yet')
        if isinstance(args[0], dict):
            r._Point = args[0]
        return tmp_D(*args, **kwargs)

    r._getFunc = aux_f
    r._D = aux_D
    return r