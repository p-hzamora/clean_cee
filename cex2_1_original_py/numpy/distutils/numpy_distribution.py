# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\distutils\numpy_distribution.pyc
# Compiled at: 2013-04-07 07:04:04
from distutils.core import Distribution

class NumpyDistribution(Distribution):

    def __init__(self, attrs=None):
        self.scons_data = []
        self.installed_libraries = []
        self.installed_pkg_config = {}
        Distribution.__init__(self, attrs)

    def has_scons_scripts(self):
        return bool(self.scons_data)