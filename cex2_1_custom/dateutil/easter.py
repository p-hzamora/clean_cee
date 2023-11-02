# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: dateutil\easter.pyc
# Compiled at: 2012-11-06 15:31:10
"""
Copyright (c) 2003-2007  Gustavo Niemeyer <gustavo@niemeyer.net>

This module offers extensions to the standard python 2.3+
datetime module.
"""
__author__ = 'Gustavo Niemeyer <gustavo@niemeyer.net>'
__license__ = 'PSF License'
import datetime
__all__ = [
 'easter', 'EASTER_JULIAN', 'EASTER_ORTHODOX', 'EASTER_WESTERN']
EASTER_JULIAN = 1
EASTER_ORTHODOX = 2
EASTER_WESTERN = 3

def easter(year, method=EASTER_WESTERN):
    """
    This method was ported from the work done by GM Arts,
    on top of the algorithm by Claus Tondering, which was
    based in part on the algorithm of Ouding (1940), as
    quoted in "Explanatory Supplement to the Astronomical
    Almanac", P.  Kenneth Seidelmann, editor.

    This algorithm implements three different easter
    calculation methods:
    
    1 - Original calculation in Julian calendar, valid in
        dates after 326 AD
    2 - Original method, with date converted to Gregorian
        calendar, valid in years 1583 to 4099
    3 - Revised method, in Gregorian calendar, valid in
        years 1583 to 4099 as well

    These methods are represented by the constants:

    EASTER_JULIAN   = 1
    EASTER_ORTHODOX = 2
    EASTER_WESTERN  = 3

    The default method is method 3.
    
    More about the algorithm may be found at:

    http://users.chariot.net.au/~gmarts/eastalg.htm

    and

    http://www.tondering.dk/claus/calendar.html

    """
    if not 1 <= method <= 3:
        raise ValueError, 'invalid method'
    y = year
    g = y % 19
    e = 0
    if method < 3:
        i = (19 * g + 15) % 30
        j = (y + y // 4 + i) % 7
        if method == 2:
            e = 10
            if y > 1600:
                e = e + y // 100 - 16 - (y // 100 - 16) // 4
    else:
        c = y // 100
        h = (c - c // 4 - (8 * c + 13) // 25 + 19 * g + 15) % 30
        i = h - h // 28 * (1 - h // 28 * (29 // (h + 1)) * ((21 - g) // 11))
        j = (y + y // 4 + i + 2 - c + c // 4) % 7
    p = i - j + e
    d = 1 + (p + 27 + (p + 6) // 40) % 31
    m = 3 + (p + 26) // 30
    return datetime.date(int(y), int(m), int(d))