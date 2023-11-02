# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\lib\set_ops.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = 'From before Python had a Set class...'
import types, string

def __set_coerce(t, S):
    if t is types.ListType:
        return list(S)
    if t is types.TupleType:
        return tuple(S)
    if t is types.StringType:
        return string.join(S, '')
    return S


def unique(seq):
    result = []
    for i in seq:
        if i not in result:
            result.append(i)

    return __set_coerce(type(seq), result)


def intersect(seq1, seq2):
    result = []
    if type(seq1) != type(seq2) and type(seq2) == types.StringType:
        seq2 = list(seq2)
    for i in seq1:
        if i in seq2 and i not in result:
            result.append(i)

    return __set_coerce(type(seq1), result)


def union(seq1, seq2):
    if type(seq1) == type(seq2):
        return unique(seq1 + seq2)
    if type(seq1) == types.ListType or type(seq2) == types.ListType:
        return unique(list(seq1) + list(seq2))
    if type(seq1) == types.TupleType or type(seq2) == types.TupleType:
        return unique(tuple(seq1) + tuple(seq2))
    return unique(list(seq1) + list(seq2))