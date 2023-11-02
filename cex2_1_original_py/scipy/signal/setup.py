# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\signal\setup.pyc
# Compiled at: 2013-02-16 13:27:32
from __future__ import division, print_function, absolute_import

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('signal', parent_package, top_path)
    config.add_data_dir('tests')
    config.add_extension('sigtools', sources=[
     'sigtoolsmodule.c', 'firfilter.c', 
     'medianfilter.c', 
     'lfilter.c.src', 
     'correlate_nd.c.src'], depends=[
     'sigtools.h'], include_dirs=[
     '.'])
    config.add_extension('_spectral', sources=['_spectral.c'])
    config.add_extension('spline', sources=[
     'splinemodule.c', 'S_bspline_util.c', 'D_bspline_util.c', 
     'C_bspline_util.c', 
     'Z_bspline_util.c', 'bspline_util.c'])
    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())