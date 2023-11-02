# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\oldnumeric\array_printer.pyc
# Compiled at: 2013-04-07 07:04:04
__all__ = ['array2string']
from numpy import array2string as _array2string

def array2string(a, max_line_width=None, precision=None, suppress_small=None, separator=' ', array_output=0):
    if array_output:
        prefix = 'array('
        style = repr
    else:
        prefix = ''
        style = str
    return _array2string(a, max_line_width, precision, suppress_small, separator, prefix, style)