# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\distutils\command\build_py.pyc
# Compiled at: 2013-04-07 07:04:04
from distutils.command.build_py import build_py as old_build_py
from numpy.distutils.misc_util import is_string

class build_py(old_build_py):

    def run(self):
        build_src = self.get_finalized_command('build_src')
        if build_src.py_modules_dict and self.packages is None:
            self.packages = build_src.py_modules_dict.keys()
        old_build_py.run(self)
        return

    def find_package_modules(self, package, package_dir):
        modules = old_build_py.find_package_modules(self, package, package_dir)
        build_src = self.get_finalized_command('build_src')
        modules += build_src.py_modules_dict.get(package, [])
        return modules

    def find_modules(self):
        old_py_modules = self.py_modules[:]
        new_py_modules = filter(is_string, self.py_modules)
        self.py_modules[:] = new_py_modules
        modules = old_build_py.find_modules(self)
        self.py_modules[:] = old_py_modules
        return modules