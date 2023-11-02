# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\dual.pyc
# Compiled at: 2013-04-07 07:04:04
"""
Aliases for functions which may be accelerated by Scipy.

Scipy_ can be built to use accelerated or otherwise improved libraries
for FFTs, linear algebra, and special functions. This module allows
developers to transparently support these accelerated functions when
scipy is available but still support users who have only installed
Numpy.

.. _Scipy : http://www.scipy.org

"""
__all__ = [
 'fft', 'ifft', 'fftn', 'ifftn', 'fft2', 'ifft2', 
 'norm', 'inv', 'svd', 
 'solve', 'det', 'eig', 'eigvals', 
 'eigh', 'eigvalsh', 'lstsq', 'pinv', 
 'cholesky', 'i0']
import numpy.linalg as linpkg, numpy.fft as fftpkg
from numpy.lib import i0
import sys
fft = fftpkg.fft
ifft = fftpkg.ifft
fftn = fftpkg.fftn
ifftn = fftpkg.ifftn
fft2 = fftpkg.fft2
ifft2 = fftpkg.ifft2
norm = linpkg.norm
inv = linpkg.inv
svd = linpkg.svd
solve = linpkg.solve
det = linpkg.det
eig = linpkg.eig
eigvals = linpkg.eigvals
eigh = linpkg.eigh
eigvalsh = linpkg.eigvalsh
lstsq = linpkg.lstsq
pinv = linpkg.pinv
cholesky = linpkg.cholesky
_restore_dict = {}

def register_func(name, func):
    if name not in __all__:
        raise ValueError('%s not a dual function.' % name)
    f = sys._getframe(0).f_globals
    _restore_dict[name] = f[name]
    f[name] = func


def restore_func(name):
    if name not in __all__:
        raise ValueError('%s not a dual function.' % name)
    try:
        val = _restore_dict[name]
    except KeyError:
        return

    sys._getframe(0).f_globals[name] = val


def restore_all():
    for name in _restore_dict.keys():
        restore_func(name)