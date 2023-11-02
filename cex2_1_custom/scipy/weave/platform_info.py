# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\weave\platform_info.pyc
# Compiled at: 2013-03-29 22:51:36
""" Information about platform and python version and compilers

    This information is manly used to build directory names that
    keep the object files and shared libaries straight when
    multiple platforms share the same file system.
"""
from __future__ import absolute_import, print_function
import os, sys, subprocess, distutils
from distutils.sysconfig import customize_compiler
from numpy.distutils.ccompiler import new_compiler
from numpy.distutils.core import setup
import distutils.bcppcompiler

def dummy_dist():
    distutils.core._setup_stop_after = 'commandline'
    dist = setup(name='dummy')
    distutils.core._setup_stop_after = None
    return dist


def create_compiler_instance(dist):
    opts = dist.command_options.get('build_ext', None)
    compiler_name = ''
    if opts:
        comp = opts.get('compiler', ('', ''))
        compiler_name = comp[1]
    if not compiler_name:
        compiler_name = None
    compiler = new_compiler(compiler=compiler_name)
    customize_compiler(compiler)
    return compiler


def compiler_exe_name(compiler):
    exe_name = ''
    if hasattr(compiler, 'compiler'):
        exe_name = compiler.compiler[0]
    elif hasattr(compiler, 'cc'):
        exe_name = compiler.cc
    elif compiler.__class__ is distutils.bcppcompiler.BCPPCompiler:
        exe_name = 'brcc32'
    return exe_name


def compiler_exe_path(exe_name):
    exe_path = None
    if os.path.exists(exe_name):
        exe_path = exe_name
    else:
        path_string = os.environ['PATH']
        path_string = os.path.expandvars(path_string)
        path_string = os.path.expanduser(path_string)
        paths = path_string.split(os.pathsep)
        for path in paths:
            path = os.path.join(path, exe_name)
            if os.path.exists(path):
                exe_path = path
                break
            path = path + '.exe'
            if os.path.exists(path):
                exe_path = path
                break

    return exe_path


def check_sum(file):
    import scipy.weave.md5_load as md5
    try:
        f = open(file, 'r')
        bytes = f.read(-1)
    except IOError:
        bytes = ''

    chk_sum = md5.md5(bytes)
    return chk_sum.hexdigest()


def get_compiler_dir(compiler_name):
    """ Try to figure out the compiler directory based on the
        input compiler name.  This is fragile and really should
        be done at the distutils level inside the compiler.  I
        think it is only useful on windows at the moment.
    """
    compiler_type = choose_compiler(compiler_name)
    configure_sys_argv(compiler_type)
    dist = dummy_dist()
    compiler_obj = create_compiler_instance(dist)
    exe_name = compiler_exe_name(compiler_obj)
    exe_path = compiler_exe_path(exe_name)
    if not exe_path:
        raise ValueError("The '%s' compiler was not found." % compiler_name)
    chk_sum = check_sum(exe_path)
    restore_sys_argv()
    return 'compiler_' + chk_sum


def choose_compiler(compiler_name=''):
    """ Try and figure out which compiler is gonna be used on windows.
        On other platforms, it just returns whatever value it is given.

        converts 'gcc' to 'mingw32' on win32
    """
    if not compiler_name:
        compiler_name = ''
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


old_argv = []

def configure_sys_argv(compiler_name):
    global old_argv
    old_argv = sys.argv[:]
    sys.argv = ['', 'build_ext', '--compiler=' + compiler_name]


def restore_sys_argv():
    sys.argv = old_argv


def gcc_exists(name='gcc'):
    """ Test to make sure gcc is found

        Does this return correct value on win98???
    """
    result = 0
    cmd = '%s -v' % name
    try:
        p = subprocess.Popen([str(name), '-v'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        str_result = p.stdout.read()
        if 'Reading specs' in str_result:
            result = 1
    except:
        result = not os.system(cmd)

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
            version = distutils.msvccompiler.get_devstudio_versions()
        except:
            version = distutils.msvccompiler.get_build_version()

        if version:
            result = 1

    return result


if __name__ == '__main__':
    path = get_compiler_dir('gcc')
    print('gcc path:', path)
    print()
    try:
        path = get_compiler_dir('msvc')
        print('gcc path:', path)
    except ValueError:
        pass