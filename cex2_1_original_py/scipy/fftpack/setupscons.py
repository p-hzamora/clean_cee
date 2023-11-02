# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\fftpack\setupscons.pyc
# Compiled at: 2013-02-16 13:27:30
from __future__ import division, print_function, absolute_import
from os.path import join

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    from numpy.distutils.system_info import get_info
    config = Configuration('fftpack', parent_package, top_path)
    config.add_sconscript('SConstruct')
    config.add_data_dir('tests')
    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    from .fftpack_version import fftpack_version
    setup(version=fftpack_version, description='fftpack - Discrete Fourier Transform package', author='Pearu Peterson', author_email='pearu@cens.ioc.ee', maintainer_email='scipy-dev@scipy.org', license='SciPy License (BSD Style)', **configuration(top_path='').todict())