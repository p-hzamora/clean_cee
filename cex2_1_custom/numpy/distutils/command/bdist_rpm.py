# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\distutils\command\bdist_rpm.pyc
# Compiled at: 2013-04-07 07:04:04
import os, sys
if 'setuptools' in sys.modules:
    from setuptools.command.bdist_rpm import bdist_rpm as old_bdist_rpm
else:
    from distutils.command.bdist_rpm import bdist_rpm as old_bdist_rpm

class bdist_rpm(old_bdist_rpm):

    def _make_spec_file(self):
        spec_file = old_bdist_rpm._make_spec_file(self)
        setup_py = os.path.basename(sys.argv[0])
        if setup_py == 'setup.py':
            return spec_file
        new_spec_file = []
        for line in spec_file:
            line = line.replace('setup.py', setup_py)
            new_spec_file.append(line)

        return new_spec_file