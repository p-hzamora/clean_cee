# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\sparse\linalg\isolve\setup.pyc
# Compiled at: 2013-02-16 13:27:32
from __future__ import division, print_function, absolute_import
import os, sys, re
from distutils.dep_util import newer_group, newer
from glob import glob
from os.path import join
from scipy._build_utils import needs_g77_abi_wrapper

def configuration(parent_package='', top_path=None):
    from numpy.distutils.system_info import get_info, NotFoundError
    from numpy.distutils.misc_util import Configuration
    config = Configuration('isolve', parent_package, top_path)
    lapack_opt = get_info('lapack_opt')
    if not lapack_opt:
        raise NotFoundError('no lapack/blas resources found')
    methods = [
     'BiCGREVCOM.f.src', 
     'BiCGSTABREVCOM.f.src', 
     'CGREVCOM.f.src', 
     'CGSREVCOM.f.src', 
     'GMRESREVCOM.f.src', 
     'QMRREVCOM.f.src']
    if needs_g77_abi_wrapper(lapack_opt):
        methods += [join('FWRAPPERS', 'veclib_cabi_f.f'),
         join('FWRAPPERS', 'veclib_cabi_c.c')]
    else:
        methods += [join('FWRAPPERS', 'dummy.f')]
    Util = [
     'STOPTEST2.f.src', 'getbreak.f.src']
    sources = Util + methods + ['_iterative.pyf.src']
    config.add_extension('_iterative', sources=[ join('iterative', x) for x in sources ], extra_info=lapack_opt, depends=[ join('iterative', 'FWRAPPERS', x) for x in [
     'veclib_cabi_f.f', 'veclib_cabi_c.c', 'dummy.f']
                                                                                                                         ])
    config.add_data_dir('tests')
    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())