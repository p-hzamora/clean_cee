# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\distutils\command\sdist.pyc
# Compiled at: 2013-04-07 07:04:04
import sys
if 'setuptools' in sys.modules:
    from setuptools.command.sdist import sdist as old_sdist
else:
    from distutils.command.sdist import sdist as old_sdist
from numpy.distutils.misc_util import get_data_files

class sdist(old_sdist):

    def add_defaults(self):
        old_sdist.add_defaults(self)
        dist = self.distribution
        if dist.has_data_files():
            for data in dist.data_files:
                self.filelist.extend(get_data_files(data))

        if dist.has_headers():
            headers = []
            for h in dist.headers:
                if isinstance(h, str):
                    headers.append(h)
                else:
                    headers.append(h[1])

            self.filelist.extend(headers)