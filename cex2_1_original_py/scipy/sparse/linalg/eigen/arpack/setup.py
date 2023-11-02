# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\sparse\linalg\eigen\arpack\setup.pyc
# Compiled at: 2013-02-16 13:27:32
from __future__ import division, print_function, absolute_import
from os.path import join
from scipy._build_utils import needs_g77_abi_wrapper

def configuration(parent_package='', top_path=None):
    from numpy.distutils.system_info import get_info, NotFoundError
    from numpy.distutils.misc_util import Configuration
    config = Configuration('arpack', parent_package, top_path)
    lapack_opt = get_info('lapack_opt')
    if not lapack_opt:
        raise NotFoundError('no lapack/blas resources found')
    config = Configuration('arpack', parent_package, top_path)
    arpack_sources = [
     join('ARPACK', 'SRC', '*.f')]
    arpack_sources.extend([join('ARPACK', 'UTIL', '*.f')])
    arpack_sources.extend([join('ARPACK', 'LAPACK', '*.f')])
    if needs_g77_abi_wrapper(lapack_opt):
        arpack_sources += [join('ARPACK', 'FWRAPPERS', 'veclib_cabi_f.f'),
         join('ARPACK', 'FWRAPPERS', 'veclib_cabi_c.c')]
    else:
        arpack_sources += [join('ARPACK', 'FWRAPPERS', 'dummy.f')]
    config.add_library('arpack_scipy', sources=arpack_sources, include_dirs=[
     join('ARPACK', 'SRC')], depends=[
     join('ARPACK', 'FWRAPPERS', 'veclib_cabi_f.f'),
     join('ARPACK', 'FWRAPPERS', 'veclib_cabi_c.c'),
     join('ARPACK', 'FWRAPPERS', 'dummy.f')])
    config.add_extension('_arpack', sources='arpack.pyf.src', libraries=[
     'arpack_scipy'], extra_info=lapack_opt)
    config.add_data_dir('tests')
    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())