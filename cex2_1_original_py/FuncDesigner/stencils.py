# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: FuncDesigner\stencils.pyc
# Compiled at: 2012-06-09 20:11:06
from numpy import all, abs
from overloads import hstack
from FDmisc import FuncDesignerException

def d(arg, v, **kw):
    N = len(v)
    stencil = kw.get('stencil', 3)
    if stencil not in (2, 3):
        raise FuncDesignerException('for d1 only stencil = 2 and 3 are implemented')
    timestep = v[1] - v[0]
    if not all(abs(v[1:] - v[:-1] - timestep) < 1e-10):
        raise FuncDesignerException('unimplemented for non-uniform step yet')
    if stencil == 2:
        r1 = -3 * arg[0] + 4 * arg[1] - arg[2]
        r2 = (arg[2:N] - arg[0:N - 2]) / 2.0
        r3 = 3 * arg[N - 1] - 4 * arg[N - 2] + arg[N - 3]
        return hstack((r1, r2, r3)) / timestep
    if stencil == 3:
        r1 = -22 * arg[0] + 36 * arg[1] - 18 * arg[2] + 4 * arg[3]
        r2 = -22 * arg[1] + 36 * arg[2] - 18 * arg[3] + 4 * arg[4]
        r3 = arg[0:N - 4] - 8 * arg[1:N - 3] + 8 * arg[3:N - 1] - arg[4:N]
        r4 = 22 * arg[N - 5] - 36 * arg[N - 4] + 18 * arg[N - 3] - 4 * arg[N - 2]
        r5 = 22 * arg[N - 4] - 36 * arg[N - 3] + 18 * arg[N - 2] - 4 * arg[N - 1]
        return hstack((r1, r2, r3, r4, r5)) / (12 * timestep)
    return r


def d2(arg, v, **kw):
    N = len(v)
    timestep = v[1] - v[0]
    if not all(abs(v[1:] - v[:-1] - timestep) < 1e-10):
        raise FuncDesignerException('unimplemented for non-uniform step yet')
    stencil = kw.get('stencil', 1)
    if stencil not in (1, ):
        raise FuncDesignerException('for d2 only stencil = 1 is implemented')
    if stencil == 1:
        r1 = arg[0] - 2 * arg[1] + arg[2]
        r2 = arg[0:N - 2] - 2 * arg[1:N - 1] + arg[2:N]
        r3 = arg[N - 1] - 2 * arg[N - 2] + arg[N - 3]
        return hstack((r1, r2, r3)) / timestep ** 2