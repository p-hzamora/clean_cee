# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\optimize\_tstutils.pyc
# Compiled at: 2013-02-16 13:27:30
""" Parameters used in test and benchmark methods """
from __future__ import division, print_function, absolute_import
from random import random
from scipy.optimize import zeros as cc

def f1(x):
    return x * (x - 1.0)


def f2(x):
    return x ** 2 - 1


def f3(x):
    return x * (x - 1.0) * (x - 2.0) * (x - 3.0)


def f4(x):
    if x > 1:
        return 1.0 + 0.1 * x
    if x < 1:
        return -1.0 + 0.1 * x
    return 0


def f5(x):
    if x != 1:
        return 1.0 / (1.0 - x)
    return 0


def f6(x):
    if x > 1:
        return random()
    else:
        if x < 1:
            return -random()
        return 0


description = "\nf2 is a symmetric parabola, x**2 - 1\nf3 is a quartic polynomial with large hump in interval\nf4 is step function with a discontinuity at 1\nf5 is a hyperbola with vertical asymptote at 1\nf6 has random values positive to left of 1, negative to right\n\nof course these are not real problems. They just test how the\n'good' solvers behave in bad circumstances where bisection is\nreally the best. A good solver should not be much worse than\nbisection in such circumstance, while being faster for smooth\nmonotone sorts of functions.\n"
methods = [
 cc.bisect, cc.ridder, cc.brenth, cc.brentq]
mstrings = ['cc.bisect', 'cc.ridder', 'cc.brenth', 'cc.brentq']
functions = [f2, f3, f4, f5, f6]
fstrings = ['f2', 'f3', 'f4', 'f5', 'f6']