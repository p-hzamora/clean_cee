# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\UkrOpt\Dilation.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import dot, zeros, float64, diag, ones, ndarray, isfinite, all, asarray
from numpy.linalg import norm

class Dilation:

    def __init__(self, p):
        self.T = float64
        self.b = diag(ones(p.n, dtype=self.T))

    def getDilatedVector(self, vec):
        assert type(vec) == ndarray and all(isfinite(vec))
        tmp = dot(self.b.T, vec)
        if any(tmp):
            tmp /= norm(tmp)
        return dot(self.b, tmp)

    def updateDilationMatrix(self, vec, alp=2.0):
        assert type(vec) == ndarray and all(isfinite(vec))
        g = dot(self.b.T, vec)
        ng = norm(g)
        if all(isfinite(g)) and ng > 1e-50:
            g = (g / ng).reshape(-1, 1)
            vec1 = dot(self.b, g)
            w = asarray(1.0 / alp - 1.0, self.T)
            vec2 = w * g.T
            self.b += dot(vec1, vec2)