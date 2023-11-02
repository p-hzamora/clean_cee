# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: setuptools\command\install.pyc
# Compiled at: 2008-02-15 13:29:24
import setuptools, sys, glob
from distutils.command.install import install as _install
from distutils.errors import DistutilsArgError

class install(_install):
    """Use easy_install to install the package, w/dependencies"""
    user_options = _install.user_options + [
     ('old-and-unmanageable', None, 'Try not to use this!'),
     ('single-version-externally-managed', None, "used by system package builders to create 'flat' eggs")]
    boolean_options = _install.boolean_options + [
     'old-and-unmanageable', 'single-version-externally-managed']
    new_commands = [
     (
      'install_egg_info', (lambda self: True)),
     (
      'install_scripts', (lambda self: True))]
    _nc = dict(new_commands)
    sub_commands = [ cmd for cmd in _install.sub_commands if cmd[0] not in _nc ] + new_commands

    def initialize_options(self):
        _install.initialize_options(self)
        self.old_and_unmanageable = None
        self.single_version_externally_managed = None
        self.no_compile = None
        return

    def finalize_options(self):
        _install.finalize_options(self)
        if self.root:
            self.single_version_externally_managed = True
        elif self.single_version_externally_managed:
            if not self.root and not self.record:
                raise DistutilsArgError('You must specify --record or --root when building system packages')

    def handle_extra_path(self):
        if self.root or self.single_version_externally_managed:
            return _install.handle_extra_path(self)
        else:
            self.path_file = None
            self.extra_dirs = ''
            return

    def run(self):
        if self.old_and_unmanageable or self.single_version_externally_managed:
            return _install.run(self)
        caller = sys._getframe(2)
        caller_module = caller.f_globals.get('__name__', '')
        caller_name = caller.f_code.co_name
        if caller_module != 'distutils.dist' or caller_name != 'run_commands':
            _install.run(self)
        else:
            self.do_egg_install()

    def do_egg_install(self):
        easy_install = self.distribution.get_command_class('easy_install')
        cmd = easy_install(self.distribution, args='x', root=self.root, record=self.record)
        cmd.ensure_finalized()
        cmd.always_copy_from = '.'
        cmd.package_index.scan(glob.glob('*.egg'))
        self.run_command('bdist_egg')
        args = [self.distribution.get_command_obj('bdist_egg').egg_output]
        if setuptools.bootstrap_install_from:
            args.insert(0, setuptools.bootstrap_install_from)
        cmd.args = args
        cmd.run()
        setuptools.bootstrap_install_from = None
        return