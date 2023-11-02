# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\distutils\command\install_headers.pyc
# Compiled at: 2013-04-07 07:04:04
import os
from distutils.command.install_headers import install_headers as old_install_headers

class install_headers(old_install_headers):

    def run(self):
        headers = self.distribution.headers
        if not headers:
            return
        prefix = os.path.dirname(self.install_dir)
        for header in headers:
            if isinstance(header, tuple):
                if header[0] == 'numpy.core':
                    header = (
                     'numpy', header[1])
                    if os.path.splitext(header[1])[1] == '.inc':
                        continue
                d = os.path.join(*([prefix] + header[0].split('.')))
                header = header[1]
            else:
                d = self.install_dir
            self.mkpath(d)
            out, _ = self.copy_file(header, d)
            self.outfiles.append(out)