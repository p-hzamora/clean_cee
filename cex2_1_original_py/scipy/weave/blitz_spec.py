# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\weave\blitz_spec.pyc
# Compiled at: 2013-03-29 22:51:36
"""
    build_info holds classes that define the information
    needed for building C++ extension modules for Python that
    handle different data types.  The information includes
    such as include files, libraries, and even code snippets.

    array_info -- for building functions that use scipy arrays
"""
from __future__ import absolute_import, print_function
from . import base_info
from . import standard_array_spec
import os
blitz_support_code = "\n\n// This should be declared only if they are used by some function\n// to keep from generating needless warnings. for now, we'll always\n// declare them.\n\nint _beg = blitz::fromStart;\nint _end = blitz::toEnd;\nblitz::Range _all = blitz::Range::all();\n\ntemplate<class T, int N>\nstatic blitz::Array<T,N> convert_to_blitz(PyArrayObject* arr_obj,const char* name)\n{\n    blitz::TinyVector<int,N> shape(0);\n    blitz::TinyVector<int,N> strides(0);\n    //for (int i = N-1; i >=0; i--)\n    for (int i = 0; i < N; i++)\n    {\n        shape[i] = arr_obj->dimensions[i];\n        strides[i] = arr_obj->strides[i]/sizeof(T);\n    }\n    //return blitz::Array<T,N>((T*) arr_obj->data,shape,\n    return blitz::Array<T,N>((T*) arr_obj->data,shape,strides,\n                             blitz::neverDeleteData);\n}\n\ntemplate<class T, int N>\nstatic blitz::Array<T,N> py_to_blitz(PyArrayObject* arr_obj,const char* name)\n{\n\n    blitz::TinyVector<int,N> shape(0);\n    blitz::TinyVector<int,N> strides(0);\n    //for (int i = N-1; i >=0; i--)\n    for (int i = 0; i < N; i++)\n    {\n        shape[i] = arr_obj->dimensions[i];\n        strides[i] = arr_obj->strides[i]/sizeof(T);\n    }\n    //return blitz::Array<T,N>((T*) arr_obj->data,shape,\n    return blitz::Array<T,N>((T*) arr_obj->data,shape,strides,\n                             blitz::neverDeleteData);\n}\n"
local_dir, junk = os.path.split(os.path.abspath(__file__))
blitz_dir = os.path.join(local_dir, 'blitz')

class array_info(base_info.custom_info):

    def check_compiler(self, compiler):
        msvc_msg = 'Unfortunately, the blitz arrays used to support numeric arrays will not compile with MSVC.  Please try using mingw32 (www.mingw.org).'
        if compiler == 'msvc':
            return (ValueError, self.msvc_msg)


class array_converter(standard_array_spec.array_converter):

    def init_info(self):
        standard_array_spec.array_converter.init_info(self)
        blitz_headers = ['"blitz/array.h"',
         '"numpy/arrayobject.h"',
         '<complex>', '<math.h>']
        self.headers.extend(blitz_headers)
        self.include_dirs = [blitz_dir]
        self.support_code.append(blitz_support_code)
        self.type_name = 'numpy'

    def info_object(self):
        return array_info()

    def type_spec(self, name, value):
        new_spec = standard_array_spec.array_converter.type_spec(self, name, value)
        new_spec.dims = len(value.shape)
        if new_spec.dims > 11:
            msg = "Error converting variable '" + name + "'.  blitz only supports arrays up to 11 dimensions."
            raise ValueError(msg)
        return new_spec

    def template_vars(self, inline=0):
        res = standard_array_spec.array_converter.template_vars(self, inline)
        if hasattr(self, 'dims'):
            res['dims'] = self.dims
        return res

    def declaration_code(self, templatize=0, inline=0):
        code = '%(py_var)s = %(var_lookup)s;\n%(c_type)s %(array_name)s = %(var_convert)s;\nconversion_numpy_check_type(%(array_name)s,%(num_typecode)s,"%(name)s");\nconversion_numpy_check_size(%(array_name)s,%(dims)s,"%(name)s");\nblitz::Array<%(num_type)s,%(dims)d> %(name)s = convert_to_blitz<%(num_type)s,%(dims)d>(%(array_name)s,"%(name)s");\nblitz::TinyVector<int,%(dims)d> N%(name)s = %(name)s.shape();\n'
        code = code % self.template_vars(inline=inline)
        return code

    def __cmp__(self, other):
        return cmp(self.name, other.name) or cmp(self.var_type, other.var_type) or cmp(self.dims, other.dims) or cmp(self.__class__, other.__class__)