# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\weave\_dumb_shelve.pyc
# Compiled at: 2013-02-16 13:27:32
from __future__ import division, print_function, absolute_import
from shelve import Shelf
try:
    import zlib
except ImportError:
    pass

import pickle

class DbfilenameShelf(Shelf):
    """Shelf implementation using the "anydbm" generic dbm interface.

    This is initialized with the filename for the dbm database.
    See the module's __doc__ string for an overview of the interface.
    """

    def __init__(self, filename, flag='c'):
        from . import _dumbdbm_patched
        Shelf.__init__(self, _dumbdbm_patched.open(filename, flag))

    def __getitem__(self, key):
        compressed = self.dict[key]
        try:
            r = zlib.decompress(compressed)
        except zlib.error:
            r = compressed
        except NameError:
            r = compressed

        return pickle.loads(r)

    def __setitem__(self, key, value):
        s = pickle.dumps(value, 1)
        try:
            self.dict[key] = zlib.compress(s)
        except NameError:
            self.dict[key] = s


def open(filename, flag='c'):
    """Open a persistent dictionary for reading and writing.

    Argument is the filename for the dbm database.
    See the module's __doc__ string for an overview of the interface.
    """
    return DbfilenameShelf(filename, flag)