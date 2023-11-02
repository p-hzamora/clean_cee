# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\weave\numpy_scalar_spec.pyc
# Compiled at: 2013-03-29 22:51:36
""" Converters for all of NumPy's scalar types such as
    int32, float32, complex128, etc.
"""
from __future__ import absolute_import, print_function
import numpy
from . import c_spec

class numpy_complex_scalar_converter(c_spec.complex_converter):
    """ Handles conversion of all the NumPy complex types.
        This uses the same machinery as the standard python
        complex converter.
    """

    def init_info(self):
        c_spec.complex_converter.init_info(self)
        self.matching_types = numpy.sctypes['complex']