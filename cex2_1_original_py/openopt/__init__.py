# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\__init__.pyc
# Compiled at: 2012-12-08 11:04:58
import os, sys
curr_dir = ('').join([ elem + os.sep for elem in __file__.split(os.sep)[:-1] ])
sys.path += [curr_dir, curr_dir + 'kernel']
from ooVersionNumber import __version__
from oo import *
from GUI import manage
from oologfcn import OpenOptException
from nonOptMisc import oosolver
from mfa import MFA
isE = False
try:
    import enthought
    isE = True
except ImportError:
    pass

try:
    import envisage, mayavi
    isE = True
except ImportError:
    pass

try:
    import xy
    isE = False
except ImportError:
    pass

if isE:
    s = '\n    Seems like you are using OpenOpt from \n    commercial Enthought Python Distribution;\n    consider using free GPL-licensed alternatives\n    PythonXY (http://www.pythonxy.com) or\n    Sage (http://sagemath.org) instead.\n    '
    print s