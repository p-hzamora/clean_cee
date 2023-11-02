# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\distutils\command\build.pyc
# Compiled at: 2013-04-07 07:04:04
import os, sys
from distutils.command.build import build as old_build
from distutils.util import get_platform
from numpy.distutils.command.config_compiler import show_fortran_compilers

class build(old_build):
    sub_commands = [
     (
      'config_cc', (lambda *args: True)),
     (
      'config_fc', (lambda *args: True)),
     (
      'build_src', old_build.has_ext_modules)] + old_build.sub_commands
    user_options = old_build.user_options + [
     ('fcompiler=', None, 'specify the Fortran compiler type')]
    help_options = old_build.help_options + [
     (
      'help-fcompiler', None, 'list available Fortran compilers',
      show_fortran_compilers)]

    def initialize_options(self):
        old_build.initialize_options(self)
        self.fcompiler = None
        return

    def finalize_options(self):
        build_scripts = self.build_scripts
        old_build.finalize_options(self)
        plat_specifier = '.%s-%s' % (get_platform(), sys.version[0:3])
        if build_scripts is None:
            self.build_scripts = os.path.join(self.build_base, 'scripts' + plat_specifier)
        return

    def run(self):
        old_build.run(self)