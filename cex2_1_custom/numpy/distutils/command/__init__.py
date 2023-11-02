# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\distutils\command\__init__.pyc
# Compiled at: 2013-04-07 07:04:04
"""distutils.command

Package containing implementation of all the standard Distutils
commands."""
__revision__ = '$Id: __init__.py,v 1.3 2005/05/16 11:08:49 pearu Exp $'
distutils_all = [
 'clean', 
 'install_clib', 
 'install_scripts', 
 'bdist', 
 'bdist_dumb', 
 'bdist_wininst']
__import__('distutils.command', globals(), locals(), distutils_all)
__all__ = [
 'build', 
 'config_compiler', 
 'config', 
 'build_src', 
 'build_py', 
 'build_ext', 
 'build_clib', 
 'build_scripts', 
 'install', 
 'install_data', 
 'install_headers', 
 'install_lib', 
 'bdist_rpm', 
 'sdist'] + distutils_all