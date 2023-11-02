# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\f2py\__version__.pyc
# Compiled at: 2013-04-07 07:04:04
major = 2
try:
    from __svn_version__ import version
    version_info = (major, version)
    version = '%s_%s' % version_info
except (ImportError, ValueError):
    version = str(major)