# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\weave\weave_version.pyc
# Compiled at: 2013-03-29 22:51:36
from __future__ import absolute_import, print_function
major = 0
minor = 4
micro = 9
release_level = ''
if release_level:
    weave_version = '%(major)d.%(minor)d.%(micro)d_%(release_level)s' % locals()
else:
    weave_version = '%(major)d.%(minor)d.%(micro)d' % locals()