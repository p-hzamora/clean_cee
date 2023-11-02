# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\integrate\setup.pyc
# Compiled at: 2013-02-16 13:27:30
from __future__ import division, print_function, absolute_import
from os.path import join

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    from numpy.distutils.system_info import get_info
    config = Configuration('integrate', parent_package, top_path)
    blas_opt = get_info('blas_opt', notfound_action=2)
    config.add_library('linpack_lite', sources=[
     join('linpack_lite', '*.f')])
    config.add_library('mach', sources=[
     join('mach', '*.f')], config_fc={'noopt': (__file__, 1)})
    config.add_library('quadpack', sources=[
     join('quadpack', '*.f')])
    config.add_library('odepack', sources=[
     join('odepack', '*.f')])
    config.add_library('dop', sources=[
     join('dop', '*.f')])
    config.add_extension('_quadpack', sources=[
     '_quadpackmodule.c'], libraries=[
     'quadpack', 'linpack_lite', 'mach'], depends=[
     'quadpack.h', '__quadpack.h'])
    libs = [
     'odepack', 'linpack_lite', 'mach']
    if 'libraries' in blas_opt:
        libs.extend(blas_opt['libraries'])
    newblas = {}
    for key in blas_opt.keys():
        if key == 'libraries':
            continue
        newblas[key] = blas_opt[key]

    config.add_extension('_odepack', sources=[
     '_odepackmodule.c'], libraries=libs, depends=[
     '__odepack.h', 'multipack.h'], **newblas)
    config.add_extension('vode', sources=[
     'vode.pyf'], libraries=libs, **newblas)
    config.add_extension('lsoda', sources=[
     'lsoda.pyf'], libraries=libs, **newblas)
    config.add_extension('_dop', sources=[
     'dop.pyf'], libraries=[
     'dop'])
    config.add_data_dir('tests')
    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())