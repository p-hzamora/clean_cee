# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: setuptools\command\bdist_rpm.pyc
# Compiled at: 2007-05-22 19:55:50
from distutils.command.bdist_rpm import bdist_rpm as _bdist_rpm
import sys, os

class bdist_rpm(_bdist_rpm):

    def initialize_options(self):
        _bdist_rpm.initialize_options(self)
        self.no_egg = None
        return

    if sys.version < '2.5':

        def move_file(self, src, dst, level=1):
            _bdist_rpm.move_file(self, src, dst, level)
            if dst == self.dist_dir and src.endswith('.rpm'):
                getattr(self.distribution, 'dist_files', []).append((
                 'bdist_rpm',
                 src.endswith('.src.rpm') and 'any' or sys.version[:3],
                 os.path.join(dst, os.path.basename(src))))

    def run(self):
        self.run_command('egg_info')
        _bdist_rpm.run(self)

    def _make_spec_file(self):
        version = self.distribution.get_version()
        rpmversion = version.replace('-', '_')
        spec = _bdist_rpm._make_spec_file(self)
        line23 = '%define version ' + version
        line24 = '%define version ' + rpmversion
        spec = [ line.replace('Source0: %{name}-%{version}.tar', 'Source0: %{name}-%{unmangled_version}.tar').replace('setup.py install ', 'setup.py install --single-version-externally-managed ').replace('%setup', '%setup -n %{name}-%{unmangled_version}').replace(line23, line24) for line in spec
               ]
        spec.insert(spec.index(line24) + 1, '%define unmangled_version ' + version)
        return spec