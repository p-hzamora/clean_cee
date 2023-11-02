# Embedded file name: numpy\distutils\command\scons.pyc
import os
import sys
import os.path
from os.path import join as pjoin, dirname as pdirname
from distutils.errors import DistutilsPlatformError
from distutils.errors import DistutilsExecError, DistutilsSetupError
from numpy.distutils.command.build_ext import build_ext as old_build_ext
from numpy.distutils.ccompiler import CCompiler, new_compiler
from numpy.distutils.fcompiler import FCompiler, new_fcompiler
from numpy.distutils.exec_command import find_executable
from numpy.distutils import log
from numpy.distutils.misc_util import is_bootstrapping, get_cmd
from numpy.distutils.misc_util import get_numpy_include_dirs as _incdir
from numpy.distutils.compat import get_exception

def get_scons_build_dir():
    """Return the top path where everything produced by scons will be put.
    
    The path is relative to the top setup.py"""
    from numscons import get_scons_build_dir
    return get_scons_build_dir()


def get_scons_pkg_build_dir(pkg):
    """Return the build directory for the given package (foo.bar).
    
    The path is relative to the top setup.py"""
    from numscons.core.utils import pkg_to_path
    return pjoin(get_scons_build_dir(), pkg_to_path(pkg))


def get_scons_configres_dir():
    """Return the top path where everything produced by scons will be put.
    
    The path is relative to the top setup.py"""
    from numscons import get_scons_configres_dir
    return get_scons_configres_dir()


def get_scons_configres_filename():
    """Return the top path where everything produced by scons will be put.
    
    The path is relative to the top setup.py"""
    from numscons import get_scons_configres_filename
    return get_scons_configres_filename()


def get_scons_local_path():
    """This returns the full path where scons.py for scons-local is located."""
    from numscons import get_scons_path
    return get_scons_path()


def _get_top_dir(pkg):
    from numscons import get_scons_build_dir
    from numscons.core.utils import pkg_to_path
    scdir = pjoin(get_scons_build_dir(), pkg_to_path(pkg))
    n = scdir.count(os.sep)
    return os.sep.join([ os.pardir for i in range(n + 1) ])


def get_distutils_libdir(cmd, pkg):
    """Returns the path where distutils install libraries, relatively to the
    scons build directory."""
    return pjoin(_get_top_dir(pkg), cmd.build_lib)


def get_distutils_clibdir(cmd, pkg):
    """Returns the path where distutils put pure C libraries."""
    return pjoin(_get_top_dir(pkg), cmd.build_clib)


def get_distutils_install_prefix(pkg, inplace):
    """Returns the installation path for the current package."""
    from numscons.core.utils import pkg_to_path
    if inplace == 1:
        return pkg_to_path(pkg)
    else:
        install_cmd = get_cmd('install').get_finalized_command('install')
        return pjoin(install_cmd.install_libbase, pkg_to_path(pkg))


def get_python_exec_invoc():
    """This returns the python executable from which this file is invocated."""
    return sys.executable


def get_numpy_include_dirs(sconscript_path):
    """Return include dirs for numpy.
    
    The paths are relatively to the setup.py script path."""
    from numscons import get_scons_build_dir
    scdir = pjoin(get_scons_build_dir(), pdirname(sconscript_path))
    n = scdir.count(os.sep)
    dirs = _incdir()
    rdirs = []
    for d in dirs:
        rdirs.append(pjoin(os.sep.join([ os.pardir for i in range(n + 1) ]), d))

    return rdirs


def dirl_to_str(dirlist):
    """Given a list of directories, returns a string where the paths are
    concatenated by the path separator.
    
    example: ['foo/bar', 'bar/foo'] will return 'foo/bar:bar/foo'."""
    return os.pathsep.join(dirlist)


def dist2sconscc(compiler):
    """This converts the name passed to distutils to scons name convention (C
    compiler). compiler should be a CCompiler instance.
    
    Example:
        --compiler=intel -> intelc"""
    compiler_type = compiler.compiler_type
    if compiler_type == 'msvc':
        return 'msvc'
    elif compiler_type == 'intel':
        return 'intelc'
    else:
        return compiler.compiler[0]


def dist2sconsfc(compiler):
    """This converts the name passed to distutils to scons name convention
    (Fortran compiler). The argument should be a FCompiler instance.
    
    Example:
        --fcompiler=intel -> ifort on linux, ifl on windows"""
    if compiler.compiler_type == 'intel':
        return 'ifort'
    elif compiler.compiler_type == 'gnu':
        return 'g77'
    elif compiler.compiler_type == 'gnu95':
        return 'gfortran'
    elif compiler.compiler_type == 'sun':
        return 'sunf77'
    else:
        return 'fortran'


def dist2sconscxx(compiler):
    """This converts the name passed to distutils to scons name convention
    (C++ compiler). The argument should be a Compiler instance."""
    if compiler.compiler_type == 'msvc':
        return compiler.compiler_type
    return compiler.compiler_cxx[0]


def get_compiler_executable(compiler):
    """For any give CCompiler instance, this gives us the name of C compiler
    (the actual executable).
    
    NOTE: does NOT work with FCompiler instances."""
    if compiler.compiler_type == 'msvc':
        return 'cl.exe'
    else:
        return compiler.compiler[0]


def get_f77_compiler_executable(compiler):
    """For any give FCompiler instance, this gives us the name of F77 compiler
    (the actual executable)."""
    return compiler.compiler_f77[0]


def get_cxxcompiler_executable(compiler):
    """For any give CCompiler instance, this gives us the name of CXX compiler
    (the actual executable).
    
    NOTE: does NOT work with FCompiler instances."""
    if compiler.compiler_type == 'msvc':
        return 'cl.exe'
    else:
        return compiler.compiler_cxx[0]


def get_tool_path(compiler):
    """Given a distutils.ccompiler.CCompiler class, returns the path of the
    toolset related to C compilation."""
    fullpath_exec = find_executable(get_compiler_executable(compiler))
    if fullpath_exec:
        fullpath = pdirname(fullpath_exec)
    else:
        raise DistutilsSetupError('Could not find compiler executable info for scons')
    return fullpath


def get_f77_tool_path(compiler):
    """Given a distutils.ccompiler.FCompiler class, returns the path of the
    toolset related to F77 compilation."""
    fullpath_exec = find_executable(get_f77_compiler_executable(compiler))
    if fullpath_exec:
        fullpath = pdirname(fullpath_exec)
    else:
        raise DistutilsSetupError('Could not find F77 compiler executable info for scons')
    return fullpath


def get_cxx_tool_path(compiler):
    """Given a distutils.ccompiler.CCompiler class, returns the path of the
    toolset related to C compilation."""
    fullpath_exec = find_executable(get_cxxcompiler_executable(compiler))
    if fullpath_exec:
        fullpath = pdirname(fullpath_exec)
    else:
        raise DistutilsSetupError('Could not find compiler executable info for scons')
    return fullpath


def protect_path(path):
    """Convert path (given as a string) to something the shell will have no
    problem to understand (space, etc... problems)."""
    if path:
        return '"' + path + '"'
    else:
        return '""'


def parse_package_list(pkglist):
    return pkglist.split(',')


def find_common(seq1, seq2):
    """Given two list, return the index of the common items.
    
    The index are relative to seq1.
    
    Note: do not handle duplicate items."""
    dict2 = dict([ (i, None) for i in seq2 ])
    return [ i for i in range(len(seq1)) if dict2.has_key(seq1[i]) ]


def select_packages(sconspkg, pkglist):
    """Given a list of packages in pkglist, return the list of packages which
    match this list."""
    common = find_common(sconspkg, pkglist)
    if not len(common) == len(pkglist):
        msg = 'the package list contains a package not found in the current list. The current list is %s' % sconspkg
        raise ValueError(msg)
    return common


def check_numscons(minver):
    """Check that we can use numscons.
    
    minver is a 3 integers tuple which defines the min version."""
    try:
        import numscons
    except ImportError:
        e = get_exception()
        raise RuntimeError('importing numscons failed (error was %s), using scons within distutils is not possible without this package ' % str(e))

    try:
        from numscons import version_info
        if isinstance(version_info[0], str):
            raise ValueError('Numscons %s or above expected (detected 0.10.0)' % str(minver))
        version_info = tuple(version_info)
        if version_info[:3] < minver:
            raise ValueError('Numscons %s or above expected (got %s) ' % (str(minver), str(version_info[:3])))
    except ImportError:
        raise RuntimeError('You need numscons >= %s to build numpy with numscons (imported numscons path is %s).' % (minver, numscons.__file__))


class scons(old_build_ext):
    description = 'Scons builder'
    library_options = [('with-perflib=', None, 'Specify which performance library to use for BLAS/LAPACK/etc...Examples: mkl/atlas/sunper/accelerate'),
     ('with-mkl-lib=', None, 'TODO'),
     ('with-mkl-include=', None, 'TODO'),
     ('with-mkl-libraries=', None, 'TODO'),
     ('with-atlas-lib=', None, 'TODO'),
     ('with-atlas-include=', None, 'TODO'),
     ('with-atlas-libraries=', None, 'TODO')]
    user_options = [('jobs=', 'j', 'specify number of worker threads when executingscons'),
     ('inplace', 'i', 'If specified, build in place.'),
     ('import-env', 'e', 'If specified, import user environment into scons env["ENV"].'),
     ('bypass', 'b', 'Bypass distutils compiler detection (experimental).'),
     ('scons-tool-path=', None, 'specify additional path (absolute) to look for scons tools'),
     ('silent=', None, 'specify whether scons output should less verbose(1), silent (2), super silent (3) or not (0, default)'),
     ('log-level=', None, 'specify log level for numscons. Any value valid for the logging python module is valid'),
     ('package-list=', None, 'If specified, only run scons on the given packages (example: --package-list=scipy.cluster). If empty, no package is built'),
     ('fcompiler=', None, 'specify the Fortran compiler type'),
     ('compiler=', None, 'specify the C compiler type'),
     ('cxxcompiler=', None, 'specify the C++ compiler type (same as C by default)'),
     ('debug', 'g', 'compile/link with debugging information')] + library_options

    def initialize_options(self):
        old_build_ext.initialize_options(self)
        self.build_clib = None
        self.debug = 0
        self.compiler = None
        self.cxxcompiler = None
        self.fcompiler = None
        self.jobs = None
        self.silent = 0
        self.import_env = 0
        self.scons_tool_path = ''
        self._bypass_distutils_cc = False
        self.scons_compiler = None
        self.scons_compiler_path = None
        self.scons_fcompiler = None
        self.scons_fcompiler_path = None
        self.scons_cxxcompiler = None
        self.scons_cxxcompiler_path = None
        self.package_list = None
        self.inplace = 0
        self.bypass = 0
        self.log_level = 50
        self.with_perflib = []
        self.with_mkl_lib = []
        self.with_mkl_include = []
        self.with_mkl_libraries = []
        self.with_atlas_lib = []
        self.with_atlas_include = []
        self.with_atlas_libraries = []
        return

    def _init_ccompiler(self, compiler_type):
        if compiler_type == 'msvc':
            self._bypass_distutils_cc = True
        try:
            distutils_compiler = new_compiler(compiler=compiler_type, verbose=self.verbose, dry_run=self.dry_run, force=self.force)
            distutils_compiler.customize(self.distribution)
            if hasattr(distutils_compiler, 'initialize'):
                distutils_compiler.initialize()
            self.scons_compiler = dist2sconscc(distutils_compiler)
            self.scons_compiler_path = protect_path(get_tool_path(distutils_compiler))
        except DistutilsPlatformError:
            e = get_exception()
            if not self._bypass_distutils_cc:
                raise e
            else:
                self.scons_compiler = compiler_type

    def _init_fcompiler(self, compiler_type):
        self.fcompiler = new_fcompiler(compiler=compiler_type, verbose=self.verbose, dry_run=self.dry_run, force=self.force)
        if self.fcompiler is not None:
            self.fcompiler.customize(self.distribution)
            self.scons_fcompiler = dist2sconsfc(self.fcompiler)
            self.scons_fcompiler_path = protect_path(get_f77_tool_path(self.fcompiler))
        return

    def _init_cxxcompiler(self, compiler_type):
        cxxcompiler = new_compiler(compiler=compiler_type, verbose=self.verbose, dry_run=self.dry_run, force=self.force)
        if cxxcompiler is not None:
            cxxcompiler.customize(self.distribution, need_cxx=1)
            cxxcompiler.customize_cmd(self)
            self.cxxcompiler = cxxcompiler.cxx_compiler()
            try:
                get_cxx_tool_path(self.cxxcompiler)
            except DistutilsSetupError:
                self.cxxcompiler = None

            if self.cxxcompiler:
                self.scons_cxxcompiler = dist2sconscxx(self.cxxcompiler)
                self.scons_cxxcompiler_path = protect_path(get_cxx_tool_path(self.cxxcompiler))
        return

    def finalize_options(self):
        old_build_ext.finalize_options(self)
        self.sconscripts = []
        self.pre_hooks = []
        self.post_hooks = []
        self.pkg_names = []
        self.pkg_paths = []
        if self.distribution.has_scons_scripts():
            for i in self.distribution.scons_data:
                self.sconscripts.append(i.scons_path)
                self.pre_hooks.append(i.pre_hook)
                self.post_hooks.append(i.post_hook)
                self.pkg_names.append(i.parent_name)
                self.pkg_paths.append(i.pkg_path)

            build_clib_cmd = get_cmd('build_clib').get_finalized_command('build_clib')
            self.build_clib = build_clib_cmd.build_clib
        if not self.cxxcompiler:
            self.cxxcompiler = self.compiler
        if len(self.sconscripts) > 0:
            if self.bypass:
                self.scons_compiler = self.compiler
                self.scons_fcompiler = self.fcompiler
                self.scons_cxxcompiler = self.cxxcompiler
            else:
                self._init_ccompiler(self.compiler)
                self._init_fcompiler(self.fcompiler)
                self._init_cxxcompiler(self.cxxcompiler)
        if self.package_list:
            self.package_list = parse_package_list(self.package_list)

    def _call_scons(self, scons_exec, sconscript, pkg_name, pkg_path, bootstrapping):
        cmd = [scons_exec,
         '-f',
         sconscript,
         '-I.']
        if self.jobs:
            cmd.append(' --jobs=%d' % int(self.jobs))
        if self.inplace:
            cmd.append('inplace=1')
        cmd.append('scons_tool_path="%s"' % self.scons_tool_path)
        cmd.append('src_dir="%s"' % pdirname(sconscript))
        cmd.append('pkg_path="%s"' % pkg_path)
        cmd.append('pkg_name="%s"' % pkg_name)
        cmd.append('log_level=%s' % self.log_level)
        cmd.append('distutils_libdir=%s' % protect_path(get_distutils_libdir(self, pkg_name)))
        cmd.append('distutils_clibdir=%s' % protect_path(get_distutils_clibdir(self, pkg_name)))
        prefix = get_distutils_install_prefix(pkg_name, self.inplace)
        cmd.append('distutils_install_prefix=%s' % protect_path(prefix))
        if not self._bypass_distutils_cc:
            cmd.append('cc_opt=%s' % self.scons_compiler)
        if self.scons_compiler_path:
            cmd.append('cc_opt_path=%s' % self.scons_compiler_path)
        else:
            cmd.append('cc_opt=%s' % self.scons_compiler)
        cmd.append('debug=%s' % self.debug)
        if self.scons_fcompiler:
            cmd.append('f77_opt=%s' % self.scons_fcompiler)
        if self.scons_fcompiler_path:
            cmd.append('f77_opt_path=%s' % self.scons_fcompiler_path)
        if self.scons_cxxcompiler:
            cmd.append('cxx_opt=%s' % self.scons_cxxcompiler)
        if self.scons_cxxcompiler_path:
            cmd.append('cxx_opt_path=%s' % self.scons_cxxcompiler_path)
        cmd.append('include_bootstrap=%s' % dirl_to_str(get_numpy_include_dirs(sconscript)))
        cmd.append('bypass=%s' % self.bypass)
        cmd.append('import_env=%s' % self.import_env)
        if self.silent:
            if int(self.silent) == 2:
                cmd.append('-Q')
            elif int(self.silent) == 3:
                cmd.append('-s')
        cmd.append('silent=%d' % int(self.silent))
        cmd.append('bootstrapping=%d' % bootstrapping)
        cmdstr = ' '.join(cmd)
        if int(self.silent) < 1:
            log.info('Executing scons command (pkg is %s): %s ', pkg_name, cmdstr)
        else:
            log.info('======== Executing scons command for pkg %s =========', pkg_name)
        st = os.system(cmdstr)
        if st:
            msg = 'Error while executing scons command.'
            msg += ' See above for more information.\n'
            msg += 'If you think it is a problem in numscons, you can also try executing the scons\ncommand with --log-level option for more detailed output of what numscons is\ndoing, for example --log-level=0; the lowest the level is, the more detailed\nthe output it.'
            raise DistutilsExecError(msg)

    def run(self):
        if len(self.sconscripts) < 1:
            return
        else:
            check_numscons(minver=(0, 11, 0))
            if self.package_list is not None:
                id = select_packages(self.pkg_names, self.package_list)
                sconscripts = [ self.sconscripts[i] for i in id ]
                pre_hooks = [ self.pre_hooks[i] for i in id ]
                post_hooks = [ self.post_hooks[i] for i in id ]
                pkg_names = [ self.pkg_names[i] for i in id ]
                pkg_paths = [ self.pkg_paths[i] for i in id ]
            else:
                sconscripts = self.sconscripts
                pre_hooks = self.pre_hooks
                post_hooks = self.post_hooks
                pkg_names = self.pkg_names
                pkg_paths = self.pkg_paths
            if is_bootstrapping():
                bootstrapping = 1
            else:
                bootstrapping = 0
            scons_exec = get_python_exec_invoc()
            scons_exec += ' ' + protect_path(pjoin(get_scons_local_path(), 'scons.py'))
            for sconscript, pre_hook, post_hook, pkg_name, pkg_path in zip(sconscripts, pre_hooks, post_hooks, pkg_names, pkg_paths):
                if pre_hook:
                    pre_hook()
                if sconscript:
                    self._call_scons(scons_exec, sconscript, pkg_name, pkg_path, bootstrapping)
                if post_hook:
                    post_hook(**{'pkg_name': pkg_name,
                     'scons_cmd': self})

            return