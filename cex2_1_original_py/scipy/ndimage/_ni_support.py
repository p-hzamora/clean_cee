# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\ndimage\_ni_support.pyc
# Compiled at: 2013-02-16 13:27:30
from __future__ import division, print_function, absolute_import
import numpy
from scipy.lib.six import integer_types, string_types

def _extend_mode_to_code(mode):
    """Convert an extension mode to the corresponding integer code.
    """
    if mode == 'nearest':
        return 0
    if mode == 'wrap':
        return 1
    if mode == 'reflect':
        return 2
    if mode == 'mirror':
        return 3
    if mode == 'constant':
        return 4
    raise RuntimeError('boundary mode not supported')


def _normalize_sequence(input, rank, array_type=None):
    """If input is a scalar, create a sequence of length equal to the
    rank by duplicating the input. If input is a sequence,
    check if its length is equal to the length of array.
    """
    if isinstance(input, integer_types + (float,)):
        normalized = [
         input] * rank
    else:
        normalized = list(input)
        if len(normalized) != rank:
            err = 'sequence argument must have length equal to input rank'
            raise RuntimeError(err)
    return normalized


def _get_output(output, input, shape=None):
    if shape is None:
        shape = input.shape
    if output is None:
        output = numpy.zeros(shape, dtype=input.dtype.name)
        return_value = output
    elif type(output) in [type(type), type(numpy.zeros((4, )).dtype)]:
        output = numpy.zeros(shape, dtype=output)
        return_value = output
    elif type(output) in string_types:
        output = numpy.typeDict[output]
        output = numpy.zeros(shape, dtype=output)
        return_value = output
    else:
        if output.shape != shape:
            raise RuntimeError('output shape not correct')
        return_value = None
    return (
     output, return_value)


def _check_axis(axis, rank):
    if axis < 0:
        axis += rank
    if axis < 0 or axis >= rank:
        raise ValueError('invalid axis')
    return axis