# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\sparse\linalg\dsolve\setup.pyc
# Compiled at: 2013-02-16 13:27:32
from __future__ import division, print_function, absolute_import
from os.path import join, dirname
import sys, os, glob

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    from numpy.distutils.system_info import get_info
    config = Configuration('dsolve', parent_package, top_path)
    config.add_data_dir('tests')
    lapack_opt = get_info('lapack_opt', notfound_action=2)
    if sys.platform == 'win32':
        superlu_defs = [
         ('NO_TIMER', 1)]
    else:
        superlu_defs = []
    superlu_defs.append(('USE_VENDOR_BLAS', 1))
    superlu_src = join(dirname(__file__), 'SuperLU', 'SRC')
    sources = list(glob.glob(join(superlu_src, '*.c')))
    if os.name == 'nt' and ('FPATH' in os.environ or 'MKLROOT' in os.environ):
        sources.remove(join(superlu_src, 'lsame.c'))
    config.add_library('superlu_src', sources=sources, macros=superlu_defs, include_dirs=[
     superlu_src])
    config.add_extension('_superlu', sources=[
     '_superlumodule.c',
     '_superlu_utils.c',
     '_superluobject.c'], libraries=[
     'superlu_src'], extra_info=lapack_opt)
    config.add_subpackage('umfpack')
    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())