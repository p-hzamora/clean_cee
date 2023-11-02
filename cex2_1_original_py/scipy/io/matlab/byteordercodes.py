# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\io\matlab\byteordercodes.pyc
# Compiled at: 2013-02-16 13:27:30
""" Byteorder utilities for system - numpy byteorder encoding

Converts a variety of string codes for little endian, big endian,
native byte order and swapped byte order to explicit numpy endian
codes - one of '<' (little endian) or '>' (big endian)

"""
from __future__ import division, print_function, absolute_import
import sys
sys_is_le = sys.byteorder == 'little'
native_code = sys_is_le and '<' or '>'
swapped_code = sys_is_le and '>' or '<'
aliases = {'little': ('little', '<', 'l', 'le'), 'big': ('big', '>', 'b', 'be'), 
   'native': ('native', '='), 
   'swapped': ('swapped', 'S')}

def to_numpy_code(code):
    """
    Convert various order codings to numpy format.

    Parameters
    ----------
    code : str
        The code to convert. It is converted to lower case before parsing.
        Legal values are:
        'little', 'big', 'l', 'b', 'le', 'be', '<', '>', 'native', '=',
        'swapped', 's'.

    Returns
    -------
    out_code : {'<', '>'}
        Here '<' is the numpy dtype code for little endian,
        and '>' is the code for big endian.

    Examples
    --------
    >>> import sys
    >>> sys_is_le == (sys.byteorder == 'little')
    True
    >>> to_numpy_code('big')
    '>'
    >>> to_numpy_code('little')
    '<'
    >>> nc = to_numpy_code('native')
    >>> nc == '<' if sys_is_le else nc == '>'
    True
    >>> sc = to_numpy_code('swapped')
    >>> sc == '>' if sys_is_le else sc == '<'
    True

    """
    code = code.lower()
    if code is None:
        return native_code
    else:
        if code in aliases['little']:
            return '<'
        if code in aliases['big']:
            return '>'
        if code in aliases['native']:
            return native_code
        if code in aliases['swapped']:
            return swapped_code
        raise ValueError('We cannot handle byte order %s' % code)
        return