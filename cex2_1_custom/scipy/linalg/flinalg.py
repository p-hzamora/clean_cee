# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\linalg\flinalg.pyc
# Compiled at: 2013-02-16 13:27:30
from __future__ import division, print_function, absolute_import
__all__ = [
 'get_flinalg_funcs']
try:
    from . import _flinalg
except ImportError:
    _flinalg = None
    has_column_major_storage = lambda a: 0

def has_column_major_storage(arr):
    return arr.flags['FORTRAN']


_type_conv = {'f': 's', 'd': 'd', 'F': 'c', 'D': 'z'}

def get_flinalg_funcs(names, arrays=(), debug=0):
    """Return optimal available _flinalg function objects with
    names. arrays are used to determine optimal prefix."""
    ordering = []
    for i in range(len(arrays)):
        t = arrays[i].dtype.char
        if t not in _type_conv:
            t = 'd'
        ordering.append((t, i))

    if ordering:
        ordering.sort()
        required_prefix = _type_conv[ordering[0][0]]
    else:
        required_prefix = 'd'
    if ordering and has_column_major_storage(arrays[ordering[0][1]]):
        suffix1, suffix2 = ('_c', '_r')
    else:
        suffix1, suffix2 = ('_r', '_c')
    funcs = []
    for name in names:
        func_name = required_prefix + name
        func = getattr(_flinalg, func_name + suffix1, getattr(_flinalg, func_name + suffix2, None))
        funcs.append(func)

    return tuple(funcs)