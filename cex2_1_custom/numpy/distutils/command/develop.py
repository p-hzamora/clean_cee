# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\distutils\command\develop.pyc
# Compiled at: 2013-04-07 07:04:04
""" Override the develop command from setuptools so we can ensure that our
generated files (from build_src or build_scripts) are properly converted to real
files with filenames.
"""
from setuptools.command.develop import develop as old_develop

class develop(old_develop):
    __doc__ = old_develop.__doc__

    def install_for_development(self):
        self.reinitialize_command('build_src', inplace=1)
        self.run_command('build_scripts')
        old_develop.install_for_development(self)