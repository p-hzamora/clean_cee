# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\lib\units.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = 'Defines inch, cm, mm etc as multiples of a point\n\nYou can now in user-friendly units by doing::\n\n    from reportlab.lib.units import inch\n    r = Rect(0, 0, 3 * inch, 6 * inch)\n\n'
inch = 72.0
cm = inch / 2.54
mm = cm * 0.1
pica = 12.0

def toLength(s):
    """convert a string to  a length"""
    try:
        if s[-2:] == 'cm':
            return float(s[:-2]) * cm
        else:
            if s[-2:] == 'in':
                return float(s[:-2]) * inch
            if s[-2:] == 'pt':
                return float(s[:-2])
            if s[-1:] == 'i':
                return float(s[:-1]) * inch
            if s[-2:] == 'mm':
                return float(s[:-2]) * mm
            if s[-4:] == 'pica':
                return float(s[:-4]) * pica
            return float(s)

    except:
        raise ValueError, "Can't convert '%s' to length" % s