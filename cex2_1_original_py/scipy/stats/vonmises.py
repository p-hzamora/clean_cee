# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\stats\vonmises.pyc
# Compiled at: 2013-02-16 13:27:32
from __future__ import division, print_function, absolute_import
import numpy as np, scipy.stats
from scipy.special import i0
import numpy.testing

def von_mises_cdf_series(k, x, p):
    x = float(x)
    s = np.sin(x)
    c = np.cos(x)
    sn = np.sin(p * x)
    cn = np.cos(p * x)
    R = 0
    V = 0
    for n in range(p - 1, 0, -1):
        sn, cn = sn * c - cn * s, cn * c + sn * s
        R = 1.0 / (2 * n / k + R)
        V = R * (sn / n + V)

    return 0.5 + x / (2 * np.pi) + V / np.pi


def von_mises_cdf_normalapprox(k, x, C1):
    b = np.sqrt(2 / np.pi) * np.exp(k) / i0(k)
    z = b * np.sin(x / 2.0)
    C = 24 * k
    chi = z - z ** 3 / ((C - 2 * z ** 2 - 16) / 3.0 - (z ** 4 + 1.75 * z ** 2 + 83.5) / (C + C1 - z ** 2 + 3)) ** 2
    return scipy.stats.norm.cdf(z)


def von_mises_cdf(k, x):
    ix = 2 * np.pi * np.round(x / (2 * np.pi))
    x = x - ix
    k = float(k)
    CK = 50
    a = [28.0, 0.5, 100.0, 5.0]
    C1 = 50.1
    if k < CK:
        p = int(np.ceil(a[0] + a[1] * k - a[2] / (k + a[3])))
        F = np.clip(von_mises_cdf_series(k, x, p), 0, 1)
    else:
        F = von_mises_cdf_normalapprox(k, x, C1)
    return F + ix