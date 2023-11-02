# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\interpolate\interpnd_info.pyc
# Compiled at: 2013-02-16 13:27:30
"""
Here we perform some symbolic computations required for the N-D
interpolation routines in `interpnd.pyx`.

"""
from __future__ import division, print_function, absolute_import
from .sympy import *

def _estimate_gradients_2d_global():
    f1, f2, df1, df2, x = symbols(['f1', 'f2', 'df1', 'df2', 'x'])
    c = [f1, (df1 + 3 * f1) / 3, (df2 + 3 * f2) / 3, f2]
    w = 0
    for k in range(4):
        w += binomial(3, k) * c[k] * x ** k * (1 - x) ** (3 - k)

    wpp = w.diff(x, 2).expand()
    intwpp2 = (wpp ** 2).integrate((x, 0, 1)).expand()
    A = Matrix([[intwpp2.coeff(df1 ** 2), intwpp2.coeff(df1 * df2) / 2],
     [
      intwpp2.coeff(df1 * df2) / 2, intwpp2.coeff(df2 ** 2)]])
    B = Matrix([[intwpp2.coeff(df1).subs(df2, 0)],
     [
      intwpp2.coeff(df2).subs(df1, 0)]]) / 2
    print('A')
    print(A)
    print('B')
    print(B)
    print('solution')
    print(A.inv() * B)