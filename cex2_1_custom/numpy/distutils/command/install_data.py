# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\distutils\command\install_data.pyc
# Compiled at: 2013-04-07 07:04:04
import sys
have_setuptools = 'setuptools' in sys.modules
from distutils.command.install_data import install_data as old_install_data

class install_data(old_install_data):

    def run(self):
        old_install_data.run(self)
        if have_setuptools:
            self.run_command('install_clib')

    def finalize_options(self):
        self.set_undefined_options('install', ('install_lib', 'install_dir'), ('root',
                                                                               'root'), ('force',
                                                                                         'force'))