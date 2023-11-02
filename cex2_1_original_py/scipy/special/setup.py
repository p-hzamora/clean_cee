# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\special\setup.pyc
# Compiled at: 2013-02-16 13:27:32
from __future__ import division, print_function, absolute_import
import os, sys
from os.path import join
from distutils.sysconfig import get_python_inc
import numpy
from numpy.distutils.misc_util import get_numpy_include_dirs
try:
    from numpy.distutils.misc_util import get_info
except ImportError:
    raise ValueError('numpy >= 1.4 is required (detected %s from %s)' % (
     numpy.__version__, numpy.__file__))

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('special', parent_package, top_path)
    define_macros = []
    if sys.platform == 'win32':
        define_macros.append(('_USE_MATH_DEFINES', None))
    curdir = os.path.abspath(os.path.dirname(__file__))
    inc_dirs = [get_python_inc()]
    if inc_dirs[0] != get_python_inc(plat_specific=1):
        inc_dirs.append(get_python_inc(plat_specific=1))
    inc_dirs.append(get_numpy_include_dirs())
    config.add_library('sc_c_misc', sources=[join('c_misc', '*.c')], include_dirs=[
     curdir] + inc_dirs, macros=define_macros)
    config.add_library('sc_cephes', sources=[join('cephes', '*.c')], include_dirs=[
     curdir] + inc_dirs, macros=define_macros)
    config.add_library('sc_mach', sources=[join('mach', '*.f')], config_fc={'noopt': (__file__, 1)})
    config.add_library('sc_amos', sources=[join('amos', '*.f')])
    config.add_library('sc_cdf', sources=[join('cdflib', '*.f')])
    config.add_library('sc_specfun', sources=[join('specfun', '*.f')])
    config.add_extension('specfun', sources=[
     'specfun.pyf'], f2py_options=[
     '--no-wrap-functions'], define_macros=[], libraries=[
     'sc_specfun'])
    config.add_extension('_ufuncs', libraries=[
     'sc_amos', 'sc_c_misc', 'sc_cephes', 'sc_mach', 
     'sc_cdf', 
     'sc_specfun'], depends=[
     '_logit.h', 'cephes.h', 
     'amos_wrappers.h', 
     'cdf_wrappers.h', 
     'specfun_wrappers.h', 
     'c_misc/misc.h', 'cephes/mconf.h', 
     'cephes/cephes_names.h'], sources=[
     '_ufuncs.c', 'sf_error.c', '_logit.c.src', 
     'amos_wrappers.c', 
     'cdf_wrappers.c', 'specfun_wrappers.c'], include_dirs=[
     curdir], define_macros=define_macros, extra_info=get_info('npymath'))
    config.add_extension('_ufuncs_cxx', sources=[
     '_ufuncs_cxx.cxx',
     'sf_error.c',
     '_faddeeva.cxx',
     'Faddeeva.cc'], libraries=[
     'sc_cephes'], include_dirs=[
     curdir], define_macros=define_macros, extra_info=get_info('npymath'))
    config.add_data_files('tests/*.py')
    config.add_data_files('tests/data/README')
    config.add_data_files('tests/data/*.npz')
    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())