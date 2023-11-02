# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\weave\converters.pyc
# Compiled at: 2013-03-29 22:51:36
""" converters.py
"""
from __future__ import absolute_import, print_function
from . import common_info
from . import c_spec
default = [
 c_spec.int_converter(),
 c_spec.float_converter(),
 c_spec.complex_converter(),
 c_spec.unicode_converter(),
 c_spec.string_converter(),
 c_spec.list_converter(),
 c_spec.dict_converter(),
 c_spec.tuple_converter(),
 c_spec.file_converter(),
 c_spec.instance_converter()]
try:
    from . import standard_array_spec
    default.append(standard_array_spec.array_converter())
except ImportError:
    pass

try:
    from . import numpy_scalar_spec
    default.append(numpy_scalar_spec.numpy_complex_scalar_converter())
except ImportError:
    pass

try:
    from . import vtk_spec
    default.insert(0, vtk_spec.vtk_converter())
except IndexError:
    pass

default.append(c_spec.catchall_converter())
standard_info = [
 common_info.basic_module_info()]
standard_info += [ x.generate_build_info() for x in default ]
try:
    from . import blitz_spec
    blitz = [
     blitz_spec.array_converter()] + default
    blitz.append(c_spec.catchall_converter())
except:
    pass