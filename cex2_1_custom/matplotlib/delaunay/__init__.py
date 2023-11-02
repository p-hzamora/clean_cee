# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\delaunay\__init__.pyc
# Compiled at: 2012-10-30 18:11:14
"""Delaunay triangulation and interpolation tools.

:Author: Robert Kern <robert.kern@gmail.com>
:Copyright: Copyright 2005 Robert Kern.
:License: BSD-style license. See LICENSE.txt in the scipy source directory.
"""
from __future__ import print_function
from matplotlib._delaunay import delaunay
from .triangulate import *
from .interpolate import *
__version__ = '0.2'