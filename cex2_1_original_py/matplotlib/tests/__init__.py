# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\__init__.pyc
# Compiled at: 2012-10-30 18:11:14
from __future__ import print_function
from matplotlib import rcParams, rcdefaults, use
_multiprocess_can_split_ = True

def setup():
    use('Agg', warn=False)
    rcdefaults()
    rcParams['font.family'] = 'Bitstream Vera Sans'
    rcParams['text.hinting'] = False
    rcParams['text.hinting_factor'] = 8
    rcParams['text.antialiased'] = False