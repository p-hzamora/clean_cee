# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\io\setupscons.pyc
# Compiled at: 2013-02-16 13:27:30
from __future__ import division, print_function, absolute_import

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('io', parent_package, top_path, setup_name='setupscons.py')
    config.add_sconscript('SConstruct')
    config.add_data_dir('tests')
    config.add_subpackage('matlab')
    config.add_subpackage('arff')
    config.add_subpackage('harwell_boeing')
    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())