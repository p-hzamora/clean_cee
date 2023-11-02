# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: decoradores.pyc
# Compiled at: 2014-02-18 15:21:03


def deco(i):

    def _deco(f):

        def inner(*args, **kwargs):
            r = f(*args, **kwargs)
            return r

        return inner

    return _deco