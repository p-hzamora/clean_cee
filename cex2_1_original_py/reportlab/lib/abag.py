# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\lib\abag.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = 'Data structure to hold a collection of attributes, used by styles.'

class ABag:
    """
    'Attribute Bag' - a trivial BAG class for holding attributes.

    This predates modern Python.  Doing this again, we'd use a subclass
    of dict.

    You may initialize with keyword arguments.
    a = ABag(k0=v0,....,kx=vx,....) ==> getattr(a,'kx')==vx

    c = a.clone(ak0=av0,.....) copy with optional additional attributes.
    """

    def __init__(self, **attr):
        self.__dict__.update(attr)

    def clone(self, **attr):
        n = ABag(**self.__dict__)
        if attr:
            n.__dict__.update(attr)
        return n

    def __repr__(self):
        D = self.__dict__
        K = D.keys()
        K.sort()
        return '%s(%s)' % (self.__class__.__name__, (', ').join([ '%s=%r' % (k, D[k]) for k in K ]))


if __name__ == '__main__':
    AB = ABag(a=1, c='hello')
    CD = AB.clone()
    print AB
    print CD