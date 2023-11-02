# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\spatial\setupscons.pyc
# Compiled at: 2013-02-16 13:27:32
from __future__ import division, print_function, absolute_import
from os.path import join

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration, get_numpy_include_dirs
    config = Configuration('spatial', parent_package, top_path)
    config.add_data_dir('tests')
    config.add_sconscript('SConstruct')
    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(maintainer='SciPy Developers', author='Anne Archibald', maintainer_email='scipy-dev@scipy.org', description='Spatial algorithms and data structures', url='http://www.scipy.org', license='SciPy License (BSD Style)', **configuration(top_path='').todict())