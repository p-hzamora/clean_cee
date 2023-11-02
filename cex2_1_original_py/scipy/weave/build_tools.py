# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\weave\build_tools.pyc
# Compiled at: 2013-03-29 22:51:36
""" Tools for compiling C/C++ code to extension modules

    The main function, build_extension(), takes the C/C++ file
    along with some other options and builds a Python extension.
    It uses distutils for most of the heavy lifting.

    choose_compiler() is also useful (mainly on windows anyway)
    for trying to determine whether MSVC++ or gcc is available.
    MSVC doesn't handle templates as well, so some of the code emitted
    by the python->C conversions need this info to choose what kind
    of code to create.

    The other main thing here is an alternative version of the MingW32
    compiler class.  The class makes it possible to build libraries with
    gcc even if the original version of python was built using MSVC.  It
    does this by converting a pythonxx.lib file to a libpythonxx.a file.
    Note that you need write access to the pythonxx/lib directory to do this.
"""
from __future__ import absolute_import, print_function
import sys, os, time, tempfile, commands, subprocess, warnings
from . import platform_info
import distutils.sysconfig, distutils.dir_util
from numpy.distutils.core import Extension
old_init_posix = distutils.sysconfig._init_posix

def _init_posix():
    old_init_posix()
    ld = distutils.sysconfig._config_vars['LDSHARED']
    link_cmds = ld.split()
    if gcc_exists(link_cmds[0]):
        link_cmds[0] = 'g++'
        ld = (' ').join(link_cmds)
    if sys.platform == 'darwin':
        ld = ld.replace('-arch i386', '')
        ld += ' -framework AppKit'
        cfg_vars = distutils.sysconfig._config_vars
        cfg_vars['OPT'] = cfg_vars['CFLAGS']
    distutils.sysconfig._config_vars['LDSHARED'] = ld


distutils.sysconfig._init_posix = _init_posix

class CompileError(Exception):
    pass


def create_extension(module_path, **kw):
    """ Create an Extension that can be buil by setup.py

        See build_extension for information on keyword arguments.
    """
    distutils.sysconfig.get_config_vars()
    if 'OPT' in distutils.sysconfig._config_vars:
        flags = distutils.sysconfig._config_vars['OPT']
        flags = flags.replace('-Wall', '')
        distutils.sysconfig._config_vars['OPT'] = flags
    module_dir, cpp_name = os.path.split(os.path.abspath(module_path))
    module_name, ext = os.path.splitext(cpp_name)
    sources = kw.get('sources', [])
    kw['sources'] = [module_path] + sources
    if 'PYTHONINCLUDE' in os.environ:
        path_string = os.environ['PYTHONINCLUDE']
        if sys.platform == 'win32':
            extra_include_dirs = path_string.split(';')
        else:
            extra_include_dirs = path_string.split(':')
        include_dirs = kw.get('include_dirs', [])
        kw['include_dirs'] = include_dirs + extra_include_dirs
    platform = sys.platform
    version = sys.version.lower()
    if platform[:5] == 'sunos' and 'gcc' in version:
        extra_link_args = kw.get('extra_link_args', [])
        kw['extra_link_args'] = ['-mimpure-text'] + extra_link_args
    ext = Extension(module_name, **kw)
    return ext


def build_extension(module_path, compiler_name='', build_dir=None, temp_dir=None, verbose=0, **kw):
    """ Build the file given by module_path into a Python extension module.

        build_extensions uses distutils to build Python extension modules.
        kw arguments not used are passed on to the distutils extension
        module.  Directory settings can handle absoulte settings, but don't
        currently expand '~' or environment variables.

        module_path   -- the full path name to the c file to compile.
                         Something like:  /full/path/name/module_name.c
                         The name of the c/c++ file should be the same as the
                         name of the module (i.e. the initmodule() routine)
        compiler_name -- The name of the compiler to use.  On Windows if it
                         isn't given, MSVC is used if it exists (is found).
                         gcc is used as a second choice. If neither are found,
                         the default distutils compiler is used. Acceptable
                         names are 'gcc', 'msvc' or any of the compiler names
                         shown by distutils.ccompiler.show_compilers()
        build_dir     -- The location where the resulting extension module
                         should be placed. This location must be writable.  If
                         it isn't, several default locations are tried.  If the
                         build_dir is not in the current python path, a warning
                         is emitted, and it is added to the end of the path.
                         build_dir defaults to the current directory.
        temp_dir      -- The location where temporary files (*.o or *.obj)
                         from the build are placed. This location must be
                         writable.  If it isn't, several default locations are
                         tried.  It defaults to tempfile.gettempdir()
        verbose       -- 0, 1, or 2.  0 is as quiet as possible. 1 prints
                         minimal information.  2 is noisy.
        **kw          -- keyword arguments. These are passed on to the
                         distutils extension module.  Most of the keywords
                         are listed below.

        Distutils keywords.  These are cut and pasted from Greg Ward's
        distutils.extension.Extension class for convenience:

        sources : [string]
          list of source filenames, relative to the distribution root
          (where the setup script lives), in Unix form (slash-separated)
          for portability.  Source files may be C, C++, SWIG (.i),
          platform-specific resource files, or whatever else is recognized
          by the "build_ext" command as source for a Python extension.
          Note: The module_path file is always appended to the front of this
                list
        include_dirs : [string]
          list of directories to search for C/C++ header files (in Unix
          form for portability)
        define_macros : [(name : string, value : string|None)]
          list of macros to define; each macro is defined using a 2-tuple,
          where 'value' is either the string to define it to or None to
          define it without a particular value (equivalent of "#define
          FOO" in source or -DFOO on Unix C compiler command line)
        undef_macros : [string]
          list of macros to undefine explicitly
        library_dirs : [string]
          list of directories to search for C/C++ libraries at link time
        libraries : [string]
          list of library names (not filenames or paths) to link against
        runtime_library_dirs : [string]
          list of directories to search for C/C++ libraries at run time
          (for shared extensions, this is when the extension is loaded)
        extra_objects : [string]
          list of extra files to link with (eg. object files not implied
          by 'sources', static library that must be explicitly specified,
          binary resource files, etc.)
        extra_compile_args : [string]
          any extra platform- and compiler-specific information to use
          when compiling the source files in 'sources'.  For platforms and
          compilers where "command line" makes sense, this is typically a
          list of command-line arguments, but for other platforms it could
          be anything.
        extra_link_args : [string]
          any extra platform- and compiler-specific information to use
          when linking object files together to create the extension (or
          to create a new static Python interpreter).  Similar
          interpretation as for 'extra_compile_args'.
        export_symbols : [string]
          list of symbols to be exported from a shared extension.  Not
          used on all platforms, and not generally necessary for Python
          extensions, which typically export exactly one symbol: "init" +
          extension_name.
    """
    success = 0
    from numpy.distutils.core import setup
    from numpy.distutils.log import set_verbosity
    set_verbosity(-1)
    import distutils.sysconfig
    distutils.sysconfig.get_config_vars()
    if 'OPT' in distutils.sysconfig._config_vars:
        flags = distutils.sysconfig._config_vars['OPT']
        flags = flags.replace('-Wall', '')
        distutils.sysconfig._config_vars['OPT'] = flags
    module_dir, cpp_name = os.path.split(os.path.abspath(module_path))
    module_name, ext = os.path.splitext(cpp_name)
    temp_dir = configure_temp_dir(temp_dir)
    build_dir = configure_build_dir(module_dir)
    compiler_dir = platform_info.get_compiler_dir(compiler_name)
    temp_dir = os.path.join(temp_dir, compiler_dir)
    distutils.dir_util.mkpath(temp_dir)
    compiler_name = choose_compiler(compiler_name)
    configure_sys_argv(compiler_name, temp_dir, build_dir)
    try:
        if verbose == 1:
            print('Compiling code...')
        if verbose > 1:
            verb = 1
        else:
            verb = 0
        t1 = time.time()
        ext = create_extension(module_path, **kw)
        builtin = sys.modules['__builtin__']
        old_SysExit = builtin.__dict__['SystemExit']
        builtin.__dict__['SystemExit'] = CompileError
        import copy
        environ = copy.deepcopy(os.environ)
        try:
            setup(name=module_name, ext_modules=[ext], verbose=verb)
        finally:
            os.environ = environ
            builtin.__dict__['SystemExit'] = old_SysExit

        t2 = time.time()
        if verbose == 1:
            print('finished compiling (sec): ', t2 - t1)
        success = 1
        configure_python_path(build_dir)
    except SyntaxError:
        success = 0

    restore_sys_argv()
    return success


old_argv = []

def configure_sys_argv(compiler_name, temp_dir, build_dir):
    global old_argv
    old_argv = sys.argv[:]
    sys.argv = [, build_ext, --build-lib, build_dir, 
     --build-temp, temp_dir]
    if compiler_name == 'gcc':
        sys.argv.insert(2, '--compiler=' + compiler_name)
    elif compiler_name:
        sys.argv.insert(2, '--compiler=' + compiler_name)


def restore_sys_argv():
    sys.argv = old_argv


def configure_python_path(build_dir):
    python_paths = [ os.path.abspath(x) for x in sys.path ]
    if os.path.abspath(build_dir) not in python_paths:
        sys.path.append(os.path.abspath(build_dir))


def choose_compiler(compiler_name=''):
    """ Try and figure out which compiler is gonna be used on windows.
        On other platforms, it just returns whatever value it is given.

        converts 'gcc' to 'mingw32' on win32
    """
    if sys.platform == 'win32':
        if not compiler_name:
            if msvc_exists():
                compiler_name = 'msvc'
            elif gcc_exists():
                compiler_name = 'mingw32'
        elif compiler_name == 'gcc':
            compiler_name = 'mingw32'
    elif compiler_name == 'gcc':
        compiler_name = 'unix'
    return compiler_name


def gcc_exists(name='gcc'):
    """ Test to make sure gcc is found."""
    result = 0
    cmd = [str(name), '-v']
    try:
        if sys.platform == 'win32':
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        else:
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        str_result = p.stdout.read()
        if 'specs' in str_result:
            result = 1
    except:
        result = not os.system((' ').join(cmd))

    return result


def msvc_exists():
    """ Determine whether MSVC is available on the machine.
    """
    result = 0
    try:
        p = subprocess.Popen(['cl'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        str_result = p.stdout.read()
        if 'Microsoft' in str_result:
            result = 1
    except:
        import distutils.msvccompiler
        try:
            cc = distutils.msvccompiler.MSVCCompiler()
            cc.initialize()
            p = subprocess.Popen([cc.cc])
            result = 1
        except distutils.errors.DistutilsPlatformError:
            pass
        except WindowsError:
            pass

    return result


if os.name == 'nt':

    def run_command(command):
        """ not sure how to get exit status on nt. """
        p = subprocess.Popen(['cl'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = p.stdout.read()
        return (0, text)


else:
    run_command = commands.getstatusoutput

def configure_temp_dir(temp_dir=None):
    if temp_dir is None:
        temp_dir = tempfile.gettempdir()
    elif not os.path.exists(temp_dir) or not os.access(temp_dir, os.W_OK):
        print("warning: specified temp_dir '%s' does not exist or is not writable. Using the default temp directory" % temp_dir)
        temp_dir = tempfile.gettempdir()
    if not os.access(temp_dir, os.W_OK):
        msg = "Either the temp or build directory wasn't writable. Check these locations: '%s'" % temp_dir
        raise ValueError(msg)
    return temp_dir


def configure_build_dir(build_dir=None):
    if build_dir and (not os.path.exists(build_dir) or not os.access(build_dir, os.W_OK)):
        msg = "specified build_dir '%s' does not exist or is not writable. Trying default locations" % build_dir
        warnings.warn(msg)
        build_dir = None
    if build_dir is None:
        build_dir = os.curdir
        if not os.access(build_dir, os.W_OK):
            print("warning:, neither the module's directory nor the current directory are writable.  Using the temporarydirectory.")
            build_dir = tempfile.gettempdir()
    if not os.access(build_dir, os.W_OK):
        msg = "The build directory wasn't writable. Check this location: '%s'" % build_dir
        raise ValueError(msg)
    return os.path.abspath(build_dir)


if sys.platform == 'win32':
    import distutils.cygwinccompiler
    from distutils.version import StrictVersion
    from distutils.errors import CompileError
    from distutils.unixccompiler import UnixCCompiler

    class Mingw32CCompiler(distutils.cygwinccompiler.CygwinCCompiler):
        """ A modified MingW32 compiler compatible with an MSVC built Python.

        """
        compiler_type = 'mingw32'

        def __init__(self, verbose=0, dry_run=0, force=0):
            distutils.cygwinccompiler.CygwinCCompiler.__init__(self, verbose, dry_run, force)
            if self.gcc_version is None:
                import re
                p = subprocess.Popen(['gcc', ' -dumpversion'], shell=True, stdout=subprocess.PIPE)
                out_string = p.stdout.read()
                result = re.search('(\\d+\\.\\d+)', out_string)
                if result:
                    self.gcc_version = StrictVersion(result.group(1))
            if self.gcc_version <= '2.91.57':
                entry_point = '--entry _DllMain@12'
            else:
                entry_point = ''
            if self.linker_dll == 'dllwrap':
                self.linker = 'dllwrap' + ' --driver-name g++'
            elif self.linker_dll == 'gcc':
                self.linker = 'g++'
            if not import_library_exists():
                build_import_library()
            if self.gcc_version <= '3.0.0':
                self.set_executables(compiler='gcc -mno-cygwin -O2 -w', compiler_so='gcc -mno-cygwin -mdll -O2 -w -Wstrict-prototypes', linker_exe='g++ -mno-cygwin', linker_so='%s -mno-cygwin -mdll -static %s' % (
                 self.linker, entry_point))
            else:
                self.set_executables(compiler='gcc -mno-cygwin -O2 -w', compiler_so='gcc -O2 -w -Wstrict-prototypes', linker_exe='g++ ', linker_so='g++ -shared')
            self.compiler_cxx = [
             'g++']
            self.dll_libraries = []
            return

        def link(self, target_desc, objects, output_filename, output_dir, libraries, library_dirs, runtime_library_dirs, export_symbols=None, debug=0, extra_preargs=None, extra_postargs=None, build_temp=None, target_lang=None):
            if self.gcc_version < '3.0.0':
                distutils.cygwinccompiler.CygwinCCompiler.link(self, target_desc, objects, output_filename, output_dir, libraries, library_dirs, runtime_library_dirs, None, debug, extra_preargs, extra_postargs, build_temp, target_lang)
            else:
                UnixCCompiler.link(self, target_desc, objects, output_filename, output_dir, libraries, library_dirs, runtime_library_dirs, None, debug, extra_preargs, extra_postargs, build_temp, target_lang)
            return


    distutils.cygwinccompiler.Mingw32CCompiler = Mingw32CCompiler

    def import_library_exists():
        """ on windows platforms, make sure a gcc import library exists
        """
        if os.name == 'nt':
            lib_name = 'libpython%d%d.a' % tuple(sys.version_info[:2])
            full_path = os.path.join(sys.prefix, 'libs', lib_name)
            if not os.path.exists(full_path):
                return 0
        return 1


    def build_import_library():
        """ Build the import libraries for Mingw32-gcc on Windows
        """
        from numpy.distutils import lib2def
        lib_name = 'python%d%d.lib' % tuple(sys.version_info[:2])
        lib_file = os.path.join(sys.prefix, 'libs', lib_name)
        def_name = 'python%d%d.def' % tuple(sys.version_info[:2])
        def_file = os.path.join(sys.prefix, 'libs', def_name)
        nm_cmd = '%s %s' % (lib2def.DEFAULT_NM, lib_file)
        nm_output = lib2def.getnm(nm_cmd)
        dlist, flist = lib2def.parse_nm(nm_output)
        lib2def.output_def(dlist, flist, lib2def.DEF_HEADER, open(def_file, 'w'))
        out_name = 'libpython%d%d.a' % tuple(sys.version_info[:2])
        out_file = os.path.join(sys.prefix, 'libs', out_name)
        dll_name = 'python%d%d.dll' % tuple(sys.version_info[:2])
        args = (dll_name, def_file, out_file)
        cmd = 'dlltool --dllname %s --def %s --output-lib %s' % args
        success = not os.system(cmd)
        if not success:
            print('WARNING: failed to build import library for gcc. Linking will fail.')