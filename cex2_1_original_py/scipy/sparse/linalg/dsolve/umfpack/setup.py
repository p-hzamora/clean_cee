# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\sparse\linalg\dsolve\umfpack\setup.pyc
# Compiled at: 2013-02-16 13:27:32
from __future__ import division, print_function, absolute_import

def configuration(parent_package='', top_path=None):
    import numpy
    from numpy.distutils.misc_util import Configuration
    from numpy.distutils.system_info import get_info, dict_append
    config = Configuration('umfpack', parent_package, top_path)
    config.add_data_dir('tests')
    umf_info = get_info('umfpack', notfound_action=1)
    umfpack_i_file = config.paths('umfpack.i')[0]

    def umfpack_i(ext, build_dir):
        if umf_info:
            return umfpack_i_file

    blas_info = get_info('blas_opt')
    build_info = {}
    dict_append(build_info, **umf_info)
    dict_append(build_info, **blas_info)
    config.add_extension('__umfpack', sources=[
     umfpack_i], depends=[
     'umfpack.i'], **build_info)
    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())