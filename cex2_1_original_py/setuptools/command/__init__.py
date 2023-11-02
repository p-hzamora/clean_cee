# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: setuptools\command\__init__.pyc
# Compiled at: 2006-12-28 20:52:44
__all__ = ['alias', 'bdist_egg', 'bdist_rpm', 'build_ext', 'build_py', 'develop', 
 'easy_install', 
 'egg_info', 'install', 'install_lib', 'rotate', 'saveopts', 
 'sdist', 
 'setopt', 'test', 'upload', 'install_egg_info', 'install_scripts', 
 'register', 
 'bdist_wininst']
import sys
if sys.version >= '2.5':
    __all__.remove('upload')
from distutils.command.bdist import bdist
if 'egg' not in bdist.format_commands:
    bdist.format_command['egg'] = ('bdist_egg', 'Python .egg file')
    bdist.format_commands.append('egg')
del bdist
del sys