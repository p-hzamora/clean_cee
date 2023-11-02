# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: wx\__init__.pyc
# Compiled at: 2011-07-15 22:30:40
import __version__
__version__ = __version__.VERSION_STRING
__all__ = [
 'build', 
 'lib', 
 'py', 
 'tools', 
 'animate', 
 'aui', 
 'calendar', 
 'combo', 
 'grid', 
 'html', 
 'media', 
 'richtext', 
 'webkit', 
 'wizard', 
 'xrc', 
 'gizmos', 
 'glcanvas', 
 'stc']
from wx._core import *
del wx
if 'wxMSW' in PlatformInfo:
    __all__ += ['activex']
import wx._core
__docfilter__ = wx._core.__DocFilter(globals())
__all__ += [ name for name in dir(wx._core) if not name.startswith('_') ]