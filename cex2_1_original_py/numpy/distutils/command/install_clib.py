# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\distutils\command\install_clib.pyc
# Compiled at: 2013-04-07 07:04:04
import os
from distutils.core import Command
from distutils.ccompiler import new_compiler
from numpy.distutils.misc_util import get_cmd

class install_clib(Command):
    description = 'Command to install installable C libraries'
    user_options = []

    def initialize_options(self):
        self.install_dir = None
        self.outfiles = []
        return

    def finalize_options(self):
        self.set_undefined_options('install', ('install_lib', 'install_dir'))

    def run(self):
        build_clib_cmd = get_cmd('build_clib')
        build_dir = build_clib_cmd.build_clib
        if not build_clib_cmd.compiler:
            compiler = new_compiler(compiler=None)
            compiler.customize(self.distribution)
        else:
            compiler = build_clib_cmd.compiler
        for l in self.distribution.installed_libraries:
            target_dir = os.path.join(self.install_dir, l.target_dir)
            name = compiler.library_filename(l.name)
            source = os.path.join(build_dir, name)
            self.mkpath(target_dir)
            self.outfiles.append(self.copy_file(source, target_dir)[0])

        return

    def get_outputs(self):
        return self.outfiles