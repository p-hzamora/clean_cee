# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: distutils\command\install_headers.pyc
# Compiled at: 2011-03-08 09:43:14
"""distutils.command.install_headers

Implements the Distutils 'install_headers' command, to install C/C++ header
files to the Python include directory."""
__revision__ = '$Id$'
from distutils.core import Command

class install_headers(Command):
    description = 'install C/C++ header files'
    user_options = [
     ('install-dir=', 'd', 'directory to install header files to'),
     ('force', 'f', 'force installation (overwrite existing files)')]
    boolean_options = [
     'force']

    def initialize_options(self):
        self.install_dir = None
        self.force = 0
        self.outfiles = []
        return

    def finalize_options(self):
        self.set_undefined_options('install', ('install_headers', 'install_dir'), ('force',
                                                                                   'force'))

    def run(self):
        headers = self.distribution.headers
        if not headers:
            return
        self.mkpath(self.install_dir)
        for header in headers:
            out, _ = self.copy_file(header, self.install_dir)
            self.outfiles.append(out)

    def get_inputs(self):
        return self.distribution.headers or []

    def get_outputs(self):
        return self.outfiles