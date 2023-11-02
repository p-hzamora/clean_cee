# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\scipy_optim\numpy_eig_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt.kernel.baseSolver import baseSolver
from openopt.kernel.nonOptMisc import Vstack, isspmatrix
from numpy.linalg import eig

class numpy_eig(baseSolver):
    __name__ = 'numpy_eig'
    __license__ = 'BSD'
    __authors__ = ''
    __alg__ = ''
    __info__ = '    '
    __optionalDataThatCanBeHandled__ = []
    _canHandleScipySparse = True

    def __solver__(self, p):
        A = p.C
        if isspmatrix(A):
            p.warn('numpy.linalg.eig cannot handle sparse matrices, cast to dense will be performed')
            A = A.A
        if p._goal != 'all':
            p.err('numpy_eig cannot handle the goal "%s" yet' % p._goal)
        eigenvalues, eigenvectors = eig(A)
        p.xf = p.xk = Vstack((eigenvalues, eigenvectors))
        p.eigenvalues = eigenvalues
        p.eigenvectors = eigenvectors
        p.ff = 0