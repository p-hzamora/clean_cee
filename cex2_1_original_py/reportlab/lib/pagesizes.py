# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\lib\pagesizes.pyc
# Compiled at: 2013-03-27 15:37:42
"""This module defines a few common page sizes in points (1/72 inch).
To be expanded to include things like label sizes, envelope windows
etc."""
__version__ = ' $Id$ '
from reportlab.lib.units import cm, inch
_W, _H = 21 * cm, 29.7 * cm
A6 = (
 _W * 0.5, _H * 0.5)
A5 = (_H * 0.5, _W)
A4 = (_W, _H)
A3 = (_H, _W * 2)
A2 = (_W * 2, _H * 2)
A1 = (_H * 2, _W * 4)
A0 = (_W * 4, _H * 4)
LETTER = (
 8.5 * inch, 11 * inch)
LEGAL = (8.5 * inch, 14 * inch)
ELEVENSEVENTEEN = (11 * inch, 17 * inch)
letter = LETTER
legal = LEGAL
elevenSeventeen = ELEVENSEVENTEEN
_BW, _BH = 25 * cm, 35.3 * cm
B6 = (_BW * 0.5, _BH * 0.5)
B5 = (_BH * 0.5, _BW)
B4 = (_BW, _BH)
B3 = (_BH * 2, _BW)
B2 = (_BW * 2, _BH * 2)
B1 = (_BH * 4, _BW * 2)
B0 = (_BW * 4, _BH * 4)

def landscape(pagesize):
    """Use this to get page orientation right"""
    a, b = pagesize
    if a < b:
        return (b, a)
    else:
        return (
         a, b)


def portrait(pagesize):
    """Use this to get page orientation right"""
    a, b = pagesize
    if a >= b:
        return (b, a)
    else:
        return (
         a, b)