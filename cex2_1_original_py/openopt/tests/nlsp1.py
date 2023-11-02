# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\tests\nlsp1.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt import NLSP
from numpy import asfarray, zeros, cos, sin, inf

def test(complexity=0, **kwargs):
    f = lambda x: (
     x[0] ** 3 + x[1] ** 3 - 9, x[0] - 0.5 * x[1], cos(x[2]) + x[0] - 1.5)

    def df(x):
        df = zeros((3, 3))
        df[(0, 0)] = 3 * x[0] ** 2
        df[(0, 1)] = 3 * x[1] ** 2
        df[(1, 0)] = 1
        df[(1, 1)] = -0.5
        df[(2, 0)] = 1
        df[(2, 2)] = -sin(x[2])
        return df

    x0 = [
     8, 15, 80]
    p = NLSP(f, x0, df=df, maxFunEvals=100000.0, iprint=-1, ftol=1e-06, contol=1e-35)
    p.lb = [
     -inf, -inf, 150]
    p.ub = [inf, inf, 158]
    p.c = lambda x: (x[2] - 150.8) ** 2 - 1.5
    p.dc = lambda x: asfarray((0, 0, 2 * (x[2] - 150.8)))
    r = p.solve('nssolve', **kwargs)
    return (r.istop > 0, r, p)


if __name__ == '__main__':
    isPassed, r, p = test()