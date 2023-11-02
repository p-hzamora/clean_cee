# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\oldnumeric\typeconv.pyc
# Compiled at: 2013-04-07 07:04:04
__all__ = [
 'oldtype2dtype', 'convtypecode', 'convtypecode2', 'oldtypecodes']
import numpy as np
oldtype2dtype = {'1': np.dtype(np.byte), 's': np.dtype(np.short), 
   'w': np.dtype(np.ushort), 
   'u': np.dtype(np.uintc), 
   None: np.dtype(int)}

def convtypecode(typecode, dtype=None):
    if dtype is None:
        try:
            return oldtype2dtype[typecode]
        except:
            return np.dtype(typecode)

    else:
        return dtype
    return


def convtypecode2(typecode, dtype=None):
    if dtype is None:
        if typecode is None:
            return
        try:
            return oldtype2dtype[typecode]
        except:
            return np.dtype(typecode)

    else:
        return dtype
    return


_changedtypes = {'B': 'b', 'b': '1', 'h': 's', 
   'H': 'w', 
   'I': 'u'}

class _oldtypecodes(dict):

    def __getitem__(self, obj):
        char = np.dtype(obj).char
        try:
            return _changedtypes[char]
        except KeyError:
            return char


oldtypecodes = _oldtypecodes()