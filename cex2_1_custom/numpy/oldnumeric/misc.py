# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\oldnumeric\misc.pyc
# Compiled at: 2013-04-07 07:04:04
__all__ = [
 'sort', 'copy_reg', 'clip', 'rank', 
 'sign', 'shape', 'types', 'allclose', 
 'size', 
 'choose', 'swapaxes', 'array_str', 
 'pi', 'math', 'concatenate', 
 'putmask', 'put', 
 'around', 'vdot', 'transpose', 'array2string', 'diagonal', 
 'searchsorted', 
 'copy', 'resize', 
 'array_repr', 'e', 'StringIO', 'pickle', 
 'argsort', 
 'convolve', 'cross_correlate', 
 'dot', 'outerproduct', 'innerproduct', 
 'insert']
import types, StringIO, pickle, math, copy, copy_reg, sys
if sys.version_info[0] >= 3:
    import copyreg, io
    StringIO = io.BytesIO
    copy_reg = copyreg
from numpy import sort, clip, rank, sign, shape, putmask, allclose, size, choose, swapaxes, array_str, array_repr, e, pi, put, resize, around, concatenate, vdot, transpose, diagonal, searchsorted, argsort, convolve, dot, outer as outerproduct, inner as innerproduct, correlate as cross_correlate, place as insert
from array_printer import array2string