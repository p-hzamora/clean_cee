# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\weave\common_info.pyc
# Compiled at: 2013-03-29 22:51:36
""" Generic support code for:
        error handling code found in every weave module
        local/global dictionary access code for inline() modules
        swig pointer (old style) conversion support

"""
from __future__ import absolute_import, print_function
from . import base_info
module_support_code = '\n\n// global None value for use in functions.\nnamespace py {\nobject None = object(Py_None);\n}\n\nconst char* find_type(PyObject* py_obj)\n{\n    if(py_obj == NULL) return "C NULL value";\n    if(PyCallable_Check(py_obj)) return "callable";\n    if(PyString_Check(py_obj)) return "string";\n    if(PyInt_Check(py_obj)) return "int";\n    if(PyFloat_Check(py_obj)) return "float";\n    if(PyDict_Check(py_obj)) return "dict";\n    if(PyList_Check(py_obj)) return "list";\n    if(PyTuple_Check(py_obj)) return "tuple";\n    if(PyFile_Check(py_obj)) return "file";\n    if(PyModule_Check(py_obj)) return "module";\n\n    //should probably do more intergation (and thinking) on these.\n    if(PyCallable_Check(py_obj) && PyInstance_Check(py_obj)) return "callable";\n    if(PyInstance_Check(py_obj)) return "instance";\n    if(PyCallable_Check(py_obj)) return "callable";\n    return "unknown type";\n}\n\nvoid throw_error(PyObject* exc, const char* msg)\n{\n //printf("setting python error: %s\\n",msg);\n  PyErr_SetString(exc, msg);\n  //printf("throwing error\\n");\n  throw 1;\n}\n\nvoid handle_bad_type(PyObject* py_obj, const char* good_type, const char* var_name)\n{\n    char msg[500];\n    sprintf(msg,"received \'%s\' type instead of \'%s\' for variable \'%s\'",\n            find_type(py_obj),good_type,var_name);\n    throw_error(PyExc_TypeError,msg);\n}\n\nvoid handle_conversion_error(PyObject* py_obj, const char* good_type, const char* var_name)\n{\n    char msg[500];\n    sprintf(msg,"Conversion Error:, received \'%s\' type instead of \'%s\' for variable \'%s\'",\n            find_type(py_obj),good_type,var_name);\n    throw_error(PyExc_TypeError,msg);\n}\n\n'

class basic_module_info(base_info.base_info):
    _headers = [
     '"Python.h"', '"compile.h"', '"frameobject.h"']
    _support_code = [module_support_code]


get_variable_support_code = '\nvoid handle_variable_not_found(const char* var_name)\n{\n    char msg[500];\n    sprintf(msg,"Conversion Error: variable \'%s\' not found in local or global scope.",var_name);\n    throw_error(PyExc_NameError,msg);\n}\nPyObject* get_variable(const char* name,PyObject* locals, PyObject* globals)\n{\n    // no checking done for error -- locals and globals should\n    // already be validated as dictionaries.  If var is NULL, the\n    // function calling this should handle it.\n    PyObject* var = NULL;\n    var = PyDict_GetItemString(locals,name);\n    if (!var)\n    {\n        var = PyDict_GetItemString(globals,name);\n    }\n    if (!var)\n        handle_variable_not_found(name);\n    return var;\n}\n'
py_to_raw_dict_support_code = '\nPyObject* py_to_raw_dict(PyObject* py_obj, const char* name)\n{\n    // simply check that the value is a valid dictionary pointer.\n    if(!py_obj || !PyDict_Check(py_obj))\n        handle_bad_type(py_obj, "dictionary", name);\n    return py_obj;\n}\n'

class inline_info(base_info.base_info):
    _support_code = [
     get_variable_support_code, py_to_raw_dict_support_code]


from . import swigptr
swig_support_code = swigptr.swigptr_code

class swig_info(base_info.base_info):
    _support_code = [
     swig_support_code]