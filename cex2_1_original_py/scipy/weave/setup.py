# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\weave\setup.pyc
# Compiled at: 2013-03-29 22:51:36
from __future__ import absolute_import, print_function
from os.path import join

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('weave', parent_package, top_path)
    config.add_data_dir('tests')
    config.add_data_dir('scxx')
    config.add_data_dir(join('blitz', 'blitz'))
    config.add_data_dir('doc')
    config.add_data_dir('examples')
    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    from .weave_version import weave_version
    setup(version=weave_version, description='Tools for inlining C/C++ in Python', author='Eric Jones', author_email='eric@enthought.com', licence='SciPy License (BSD Style)', url='http://www.scipy.org', **configuration(top_path='').todict())