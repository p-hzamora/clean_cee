# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\distutils\extension.pyc
# Compiled at: 2013-04-07 07:04:04
"""distutils.extension

Provides the Extension class, used to describe C/C++ extension
modules in setup scripts.

Overridden to support f2py.
"""
__revision__ = '$Id: extension.py,v 1.1 2005/04/09 19:29:34 pearu Exp $'
from distutils.extension import Extension as old_Extension
import re
cxx_ext_re = re.compile('.*[.](cpp|cxx|cc)\\Z', re.I).match
fortran_pyf_ext_re = re.compile('.*[.](f90|f95|f77|for|ftn|f|pyf)\\Z', re.I).match

class Extension(old_Extension):

    def __init__(self, name, sources, include_dirs=None, define_macros=None, undef_macros=None, library_dirs=None, libraries=None, runtime_library_dirs=None, extra_objects=None, extra_compile_args=None, extra_link_args=None, export_symbols=None, swig_opts=None, depends=None, language=None, f2py_options=None, module_dirs=None, extra_f77_compile_args=None, extra_f90_compile_args=None):
        old_Extension.__init__(self, name, [], include_dirs, define_macros, undef_macros, library_dirs, libraries, runtime_library_dirs, extra_objects, extra_compile_args, extra_link_args, export_symbols)
        self.sources = sources
        self.swig_opts = swig_opts or []
        if isinstance(self.swig_opts, basestring):
            import warnings
            msg = 'swig_opts is specified as a string instead of a list'
            warnings.warn(msg, SyntaxWarning)
            self.swig_opts = self.swig_opts.split()
        self.depends = depends or []
        self.language = language
        self.f2py_options = f2py_options or []
        self.module_dirs = module_dirs or []
        self.extra_f77_compile_args = extra_f77_compile_args or []
        self.extra_f90_compile_args = extra_f90_compile_args or []

    def has_cxx_sources(self):
        for source in self.sources:
            if cxx_ext_re(str(source)):
                return True

        return False

    def has_f2py_sources(self):
        for source in self.sources:
            if fortran_pyf_ext_re(source):
                return True

        return False