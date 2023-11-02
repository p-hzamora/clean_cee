# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: setuptools\command\install_lib.pyc
# Compiled at: 2006-09-20 19:05:02
from distutils.command.install_lib import install_lib as _install_lib
import os

class install_lib(_install_lib):
    """Don't add compiled flags to filenames of non-Python files"""

    def _bytecode_filenames(self, py_filenames):
        bytecode_files = []
        for py_file in py_filenames:
            if not py_file.endswith('.py'):
                continue
            if self.compile:
                bytecode_files.append(py_file + 'c')
            if self.optimize > 0:
                bytecode_files.append(py_file + 'o')

        return bytecode_files

    def run(self):
        self.build()
        outfiles = self.install()
        if outfiles is not None:
            self.byte_compile(outfiles)
        return

    def get_exclusions(self):
        exclude = {}
        nsp = self.distribution.namespace_packages
        if nsp and self.get_finalized_command('install').single_version_externally_managed:
            for pkg in nsp:
                parts = pkg.split('.')
                while parts:
                    pkgdir = os.path.join(self.install_dir, *parts)
                    for f in ('__init__.py', '__init__.pyc', '__init__.pyo'):
                        exclude[os.path.join(pkgdir, f)] = 1

                    parts.pop()

        return exclude

    def copy_tree(self, infile, outfile, preserve_mode=1, preserve_times=1, preserve_symlinks=0, level=1):
        if not (preserve_mode and preserve_times and not preserve_symlinks):
            raise AssertionError
            exclude = self.get_exclusions()
            return exclude or _install_lib.copy_tree(self, infile, outfile)
        from setuptools.archive_util import unpack_directory
        from distutils import log
        outfiles = []

        def pf(src, dst):
            if dst in exclude:
                log.warn('Skipping installation of %s (namespace package)', dst)
                return False
            log.info('copying %s -> %s', src, os.path.dirname(dst))
            outfiles.append(dst)
            return dst

        unpack_directory(infile, outfile, pf)
        return outfiles

    def get_outputs(self):
        outputs = _install_lib.get_outputs(self)
        exclude = self.get_exclusions()
        if exclude:
            return [ f for f in outputs if f not in exclude ]
        return outputs