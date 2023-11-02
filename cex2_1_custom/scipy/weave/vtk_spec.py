# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\weave\vtk_spec.pyc
# Compiled at: 2013-03-29 22:51:36
"""
VTK type converter.

This module handles conversion between VTK C++ and VTK Python objects
so that one can write inline C++ code to manipulate VTK Python
objects.  It requires that you have VTK and the VTK-Python wrappers
installed.  It has been tested with VTK 4.0 and above.  You will need
to call inline with include_dirs, library_dirs and often even
libraries appropriately set for this to work without errors.
Sometimes you might need to include additional headers.

Distributed under the SciPy License.

Authors:
  Prabhu Ramachandran <prabhu@aero.iitm.ernet.in>
  Eric Jones <eric@enthought.com>
"""
from __future__ import absolute_import, print_function
from .c_spec import common_base_converter
vtk_py_to_c_template = '\nclass %(type_name)s_handler\n{\npublic:\n    %(c_type)s convert_to_%(type_name)s(PyObject* py_obj, const char* name)\n    {\n        %(c_type)s vtk_ptr = (%(c_type)s) vtkPythonGetPointerFromObject(py_obj, "%(type_name)s");\n        if (!vtk_ptr)\n            handle_conversion_error(py_obj,"%(type_name)s", name);\n        %(inc_ref_count)s\n        return vtk_ptr;\n    }\n\n    %(c_type)s py_to_%(type_name)s(PyObject* py_obj, const char* name)\n    {\n        %(c_type)s vtk_ptr = (%(c_type)s) vtkPythonGetPointerFromObject(py_obj, "%(type_name)s");\n        if (!vtk_ptr)\n            handle_bad_type(py_obj,"%(type_name)s", name);\n        %(inc_ref_count)s\n        return vtk_ptr;\n    }\n};\n\n%(type_name)s_handler x__%(type_name)s_handler = %(type_name)s_handler();\n#define convert_to_%(type_name)s(py_obj,name) \\\n        x__%(type_name)s_handler.convert_to_%(type_name)s(py_obj,name)\n#define py_to_%(type_name)s(py_obj,name) \\\n        x__%(type_name)s_handler.py_to_%(type_name)s(py_obj,name)\n\n'
vtk_c_to_py_template = '\nPyObject* %(type_name)s_to_py(vtkObjectBase* obj)\n{\n    return vtkPythonGetObjectFromPointer(obj);\n}\n'

class vtk_converter(common_base_converter):

    def __init__(self, class_name='undefined'):
        self.class_name = class_name
        common_base_converter.__init__(self)

    def init_info(self):
        common_base_converter.init_info(self)
        self.type_name = self.class_name
        self.c_type = self.class_name + '*'
        self.return_type = self.c_type
        self.to_c_return = None
        self.check_func = None
        hdr = self.class_name + '.h'
        self.headers.extend(['"vtkPythonUtil.h"', '"vtkObject.h"',
         '"%s"' % hdr])
        self.libraries.extend(['vtkCommonPython', 'vtkCommon'])
        return

    def type_match(self, value):
        is_match = 0
        try:
            if value.IsA('vtkObject'):
                is_match = 1
        except AttributeError:
            pass

        return is_match

    def generate_build_info(self):
        if self.class_name != 'undefined':
            res = common_base_converter.generate_build_info(self)
        else:
            from . import base_info
            res = base_info.base_info()
        return res

    def py_to_c_code(self):
        return vtk_py_to_c_template % self.template_vars()

    def c_to_py_code(self):
        return vtk_c_to_py_template % self.template_vars()

    def type_spec(self, name, value):
        class_name = value.__class__.__name__
        new_spec = self.__class__(class_name)
        new_spec.name = name
        return new_spec

    def __cmp__(self, other):
        res = -1
        try:
            res = cmp(self.name, other.name) or cmp(self.__class__, other.__class__) or cmp(self.class_name, other.class_name) or cmp(self.type_name, other.type_name)
        except:
            pass

        return res