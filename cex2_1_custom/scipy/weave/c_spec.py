# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\weave\c_spec.pyc
# Compiled at: 2013-03-29 22:51:36
from __future__ import absolute_import, print_function
import types
from .base_spec import base_converter
from . import base_info
py_to_c_template = '\nclass %(type_name)s_handler\n{\npublic:\n    %(return_type)s convert_to_%(type_name)s(PyObject* py_obj, const char* name)\n    {\n        // Incref occurs even if conversion fails so that\n        // the decref in cleanup_code has a matching incref.\n        %(inc_ref_count)s\n        if (!py_obj || !%(check_func)s(py_obj))\n            handle_conversion_error(py_obj,"%(type_name)s", name);\n        return %(to_c_return)s;\n    }\n\n    %(return_type)s py_to_%(type_name)s(PyObject* py_obj, const char* name)\n    {\n        // !! Pretty sure INCREF should only be called on success since\n        // !! py_to_xxx is used by the user -- not the code generator.\n        if (!py_obj || !%(check_func)s(py_obj))\n            handle_bad_type(py_obj,"%(type_name)s", name);\n        %(inc_ref_count)s\n        return %(to_c_return)s;\n    }\n};\n\n%(type_name)s_handler x__%(type_name)s_handler = %(type_name)s_handler();\n#define convert_to_%(type_name)s(py_obj,name) \\\n        x__%(type_name)s_handler.convert_to_%(type_name)s(py_obj,name)\n#define py_to_%(type_name)s(py_obj,name) \\\n        x__%(type_name)s_handler.py_to_%(type_name)s(py_obj,name)\n\n'
simple_c_to_py_template = '\nPyObject* %(type_name)s_to_py(PyObject* obj)\n{\n    return (PyObject*) obj;\n}\n\n'

class common_base_converter(base_converter):

    def __init__(self):
        self.init_info()
        self._build_information = [self.generate_build_info()]

    def init_info(self):
        self.matching_types = []
        self.headers = []
        self.include_dirs = []
        self.libraries = []
        self.library_dirs = []
        self.sources = []
        self.support_code = []
        self.module_init_code = []
        self.warnings = []
        self.define_macros = []
        self.extra_compile_args = []
        self.extra_link_args = []
        self.use_ref_count = 1
        self.name = 'no_name'
        self.c_type = 'PyObject*'
        self.return_type = 'PyObject*'
        self.to_c_return = 'py_obj'

    def info_object(self):
        return base_info.custom_info()

    def generate_build_info(self):
        info = self.info_object()
        for header in self.headers:
            info.add_header(header)

        for d in self.include_dirs:
            info.add_include_dir(d)

        for lib in self.libraries:
            info.add_library(lib)

        for d in self.library_dirs:
            info.add_library_dir(d)

        for source in self.sources:
            info.add_source(source)

        for code in self.support_code:
            info.add_support_code(code)

        info.add_support_code(self.py_to_c_code())
        info.add_support_code(self.c_to_py_code())
        for init_code in self.module_init_code:
            info.add_module_init_code(init_code)

        for macro in self.define_macros:
            info.add_define_macro(macro)

        for warning in self.warnings:
            info.add_warning(warning)

        for arg in self.extra_compile_args:
            info.add_extra_compile_arg(arg)

        for arg in self.extra_link_args:
            info.add_extra_link_arg(arg)

        return info

    def type_match(self, value):
        return type(value) in self.matching_types

    def get_var_type(self, value):
        return type(value)

    def type_spec(self, name, value):
        new_spec = self.__class__()
        new_spec.name = name
        new_spec.var_type = self.get_var_type(value)
        return new_spec

    def template_vars(self, inline=0):
        d = {}
        d['type_name'] = self.type_name
        d['check_func'] = self.check_func
        d['c_type'] = self.c_type
        d['return_type'] = self.return_type
        d['to_c_return'] = self.to_c_return
        d['name'] = self.name
        d['py_var'] = self.py_variable()
        d['var_lookup'] = self.retrieve_py_variable(inline)
        code = 'convert_to_%(type_name)s(%(py_var)s,"%(name)s")' % d
        d['var_convert'] = code
        if self.use_ref_count:
            d['inc_ref_count'] = 'Py_XINCREF(py_obj);'
        else:
            d['inc_ref_count'] = ''
        return d

    def py_to_c_code(self):
        return py_to_c_template % self.template_vars()

    def c_to_py_code(self):
        return simple_c_to_py_template % self.template_vars()

    def declaration_code(self, templatize=0, inline=0):
        code = '%(py_var)s = %(var_lookup)s;\n%(c_type)s %(name)s = %(var_convert)s;\n' % self.template_vars(inline=inline)
        return code

    def cleanup_code(self):
        if self.use_ref_count:
            code = 'Py_XDECREF(%(py_var)s);\n' % self.template_vars()
        else:
            code = ''
        return code

    def __repr__(self):
        msg = '(file:: name: %s)' % self.name
        return msg

    def __cmp__(self, other):
        result = -1
        try:
            result = cmp(self.name, other.name) or cmp(self.__class__, other.__class__)
        except AttributeError:
            pass

        return result


class module_converter(common_base_converter):

    def init_info(self):
        common_base_converter.init_info(self)
        self.type_name = 'module'
        self.check_func = 'PyModule_Check'
        self.matching_types = [
         types.ModuleType]


class string_converter(common_base_converter):

    def init_info(self):
        common_base_converter.init_info(self)
        self.type_name = 'string'
        self.check_func = 'PyString_Check'
        self.c_type = 'std::string'
        self.return_type = 'std::string'
        self.to_c_return = 'std::string(PyString_AsString(py_obj))'
        self.matching_types = [types.StringType]
        self.headers.append('<string>')

    def c_to_py_code(self):
        code = '\n               PyObject* string_to_py(std::string s)\n               {\n                   return PyString_FromString(s.c_str());\n               }\n               '
        return code


class unicode_converter(common_base_converter):

    def init_info(self):
        common_base_converter.init_info(self)
        self.type_name = 'unicode'
        self.check_func = 'PyUnicode_Check'
        self.c_type = 'Py_UNICODE*'
        self.return_type = self.c_type
        self.to_c_return = 'PyUnicode_AS_UNICODE(py_obj)'
        self.matching_types = [types.UnicodeType]

    def declaration_code(self, templatize=0, inline=0):
        code = '%(py_var)s = %(var_lookup)s;\n%(c_type)s %(name)s = %(var_convert)s;\nint N%(name)s = PyUnicode_GET_SIZE(%(py_var)s);\n' % self.template_vars(inline=inline)
        return code


class file_converter(common_base_converter):

    def init_info(self):
        common_base_converter.init_info(self)
        self.type_name = 'file'
        self.check_func = 'PyFile_Check'
        self.c_type = 'FILE*'
        self.return_type = self.c_type
        self.to_c_return = 'PyFile_AsFile(py_obj)'
        self.headers = ['<stdio.h>']
        self.matching_types = [types.FileType]

    def c_to_py_code(self):
        code = '\n               PyObject* file_to_py(FILE* file, const char* name,\n                                    const char* mode)\n               {\n                   return (PyObject*) PyFile_FromFile(file,\n                     const_cast<char*>(name),\n                     const_cast<char*>(mode), fclose);\n               }\n               '
        return code


num_to_c_types = {}
num_to_c_types[type(1)] = 'long'
num_to_c_types[type(1.0)] = 'double'
num_to_c_types[type(complex(1.0, 1.0))] = 'std::complex<double> '
num_to_c_types[long] = 'npy_longlong'
num_to_c_types['T'] = 'T'
num_to_c_types['G'] = 'std::complex<longdouble> '
num_to_c_types['F'] = 'std::complex<float> '
num_to_c_types['D'] = 'std::complex<double> '
num_to_c_types['g'] = 'npy_longdouble'
num_to_c_types['f'] = 'float'
num_to_c_types['d'] = 'double'
num_to_c_types['b'] = 'char'
num_to_c_types['B'] = 'npy_uchar'
num_to_c_types['B'] = 'npy_ubyte'
num_to_c_types['h'] = 'short'
num_to_c_types['H'] = 'npy_ushort'
num_to_c_types['i'] = 'int'
num_to_c_types['I'] = 'npy_uint'
num_to_c_types['?'] = 'bool'
num_to_c_types['l'] = 'long'
num_to_c_types['L'] = 'npy_ulong'
num_to_c_types['q'] = 'npy_longlong'
num_to_c_types['Q'] = 'npy_ulonglong'

class scalar_converter(common_base_converter):

    def init_info(self):
        common_base_converter.init_info(self)
        self.warnings = ['disable: 4275', 'disable: 4101']
        self.headers = ['<complex>', '<math.h>']
        self.use_ref_count = 0


class int_converter(scalar_converter):

    def init_info(self):
        scalar_converter.init_info(self)
        self.type_name = 'int'
        self.check_func = 'PyInt_Check'
        self.c_type = 'int'
        self.return_type = 'int'
        self.to_c_return = '(int) PyInt_AsLong(py_obj)'
        self.matching_types = [types.IntType]


class long_converter(scalar_converter):

    def init_info(self):
        scalar_converter.init_info(self)
        self.type_name = 'long'
        self.check_func = 'PyLong_Check'
        self.c_type = 'longlong'
        self.return_type = 'longlong'
        self.to_c_return = '(longlong) PyLong_AsLongLong(py_obj)'
        self.matching_types = [types.LongType]


class float_converter(scalar_converter):

    def init_info(self):
        scalar_converter.init_info(self)
        self.type_name = 'float'
        self.check_func = 'PyFloat_Check'
        self.c_type = 'double'
        self.return_type = 'double'
        self.to_c_return = 'PyFloat_AsDouble(py_obj)'
        self.matching_types = [types.FloatType]


class complex_converter(scalar_converter):

    def init_info(self):
        scalar_converter.init_info(self)
        self.type_name = 'complex'
        self.check_func = 'PyComplex_Check'
        self.c_type = 'std::complex<double>'
        self.return_type = 'std::complex<double>'
        self.to_c_return = 'std::complex<double>(PyComplex_RealAsDouble(py_obj),PyComplex_ImagAsDouble(py_obj))'
        self.matching_types = [
         types.ComplexType]


import os
local_dir, junk = os.path.split(os.path.abspath(__file__))
scxx_dir = os.path.join(local_dir, 'scxx')

class scxx_converter(common_base_converter):

    def init_info(self):
        common_base_converter.init_info(self)
        self.headers = ['"scxx/object.h"', '"scxx/list.h"', '"scxx/tuple.h"', 
         '"scxx/dict.h"', 
         '<iostream>']
        self.include_dirs = [local_dir, scxx_dir]
        self.sources = [os.path.join(scxx_dir, 'weave_imp.cpp')]


class list_converter(scxx_converter):

    def init_info(self):
        scxx_converter.init_info(self)
        self.type_name = 'list'
        self.check_func = 'PyList_Check'
        self.c_type = 'py::list'
        self.return_type = 'py::list'
        self.to_c_return = 'py::list(py_obj)'
        self.matching_types = [types.ListType]
        self.use_ref_count = 0


class tuple_converter(scxx_converter):

    def init_info(self):
        scxx_converter.init_info(self)
        self.type_name = 'tuple'
        self.check_func = 'PyTuple_Check'
        self.c_type = 'py::tuple'
        self.return_type = 'py::tuple'
        self.to_c_return = 'py::tuple(py_obj)'
        self.matching_types = [types.TupleType]
        self.use_ref_count = 0


class dict_converter(scxx_converter):

    def init_info(self):
        scxx_converter.init_info(self)
        self.type_name = 'dict'
        self.check_func = 'PyDict_Check'
        self.c_type = 'py::dict'
        self.return_type = 'py::dict'
        self.to_c_return = 'py::dict(py_obj)'
        self.matching_types = [types.DictType]
        self.use_ref_count = 0


class instance_converter(scxx_converter):

    def init_info(self):
        scxx_converter.init_info(self)
        self.type_name = 'instance'
        self.check_func = 'PyInstance_Check'
        self.c_type = 'py::object'
        self.return_type = 'py::object'
        self.to_c_return = 'py::object(py_obj)'
        self.matching_types = [types.InstanceType]
        self.use_ref_count = 0


class catchall_converter(scxx_converter):

    def init_info(self):
        scxx_converter.init_info(self)
        self.type_name = 'catchall'
        self.check_func = ''
        self.c_type = 'py::object'
        self.return_type = 'py::object'
        self.to_c_return = 'py::object(py_obj)'
        self.use_ref_count = 0

    def type_match(self, value):
        return 1


if __name__ == '__main__':
    x = list_converter().type_spec('x', 1)
    print(x.py_to_c_code())
    print()
    print(x.c_to_py_code())
    print()
    print(x.declaration_code(inline=1))
    print()
    print(x.cleanup_code())