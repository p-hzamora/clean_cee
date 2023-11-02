# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\distutils\interactive.pyc
# Compiled at: 2013-04-07 07:04:04
import os, sys
from pprint import pformat
__all__ = [
 'interactive_sys_argv']

def show_information(*args):
    print 'Python', sys.version
    for a in ['platform', 'prefix', 'byteorder', 'path']:
        print 'sys.%s = %s' % (a, pformat(getattr(sys, a)))

    for a in ['name']:
        print 'os.%s = %s' % (a, pformat(getattr(os, a)))

    if hasattr(os, 'uname'):
        print 'system,node,release,version,machine = ', os.uname()


def show_environ(*args):
    for k, i in os.environ.items():
        print '  %s = %s' % (k, i)


def show_fortran_compilers(*args):
    from fcompiler import show_fcompilers
    show_fcompilers()


def show_compilers(*args):
    from distutils.ccompiler import show_compilers
    show_compilers()


def show_tasks(argv, ccompiler, fcompiler):
    print '\nTasks:\n  i       - Show python/platform/machine information\n  ie      - Show environment information\n  c       - Show C compilers information\n  c<name> - Set C compiler (current:%s)\n  f       - Show Fortran compilers information\n  f<name> - Set Fortran compiler (current:%s)\n  e       - Edit proposed sys.argv[1:].\n\nTask aliases:\n  0         - Configure\n  1         - Build\n  2         - Install\n  2<prefix> - Install with prefix.\n  3         - Inplace build\n  4         - Source distribution\n  5         - Binary distribution\n\nProposed sys.argv = %s\n    ' % (ccompiler, fcompiler, argv)


import shlex

def edit_argv(*args):
    argv = args[0]
    readline = args[1]
    if readline is not None:
        readline.add_history((' ').join(argv[1:]))
    try:
        s = raw_input('Edit argv [UpArrow to retrive %r]: ' % (' ').join(argv[1:]))
    except EOFError:
        return

    if s:
        argv[1:] = shlex.split(s)
    return


def interactive_sys_argv(argv):
    print '=' * 72
    print 'Starting interactive session'
    print '-' * 72
    readline = None
    try:
        try:
            import readline
        except ImportError:
            pass
        else:
            import tempfile
            tdir = tempfile.gettempdir()
            username = os.environ.get('USER', os.environ.get('USERNAME', 'UNKNOWN'))
            histfile = os.path.join(tdir, '.pyhist_interactive_setup-' + username)
            try:
                try:
                    readline.read_history_file(histfile)
                except IOError:
                    pass

                import atexit
                atexit.register(readline.write_history_file, histfile)
            except AttributeError:
                pass

    except Exception as msg:
        print msg

    task_dict = {'i': show_information, 'ie': show_environ, 
       'f': show_fortran_compilers, 
       'c': show_compilers, 
       'e': edit_argv}
    c_compiler_name = None
    f_compiler_name = None
    while 1:
        show_tasks(argv, c_compiler_name, f_compiler_name)
        try:
            task = raw_input('Choose a task (^D to quit, Enter to continue with setup): ')
        except EOFError:
            print
            task = 'quit'

        ltask = task.lower()
        if task == '':
            break
        if ltask == 'quit':
            sys.exit()
        task_func = task_dict.get(ltask, None)
        if task_func is None:
            if ltask[0] == 'c':
                c_compiler_name = task[1:]
                if c_compiler_name == 'none':
                    c_compiler_name = None
                continue
            if ltask[0] == 'f':
                f_compiler_name = task[1:]
                if f_compiler_name == 'none':
                    f_compiler_name = None
                continue
            if task[0] == '2' and len(task) > 1:
                prefix = task[1:]
                task = task[0]
            else:
                prefix = None
            if task == '4':
                argv[1:] = [
                 'sdist', '-f']
                continue
            else:
                if task in '01235':
                    cmd_opts = {'config': [], 'config_fc': [], 'build_ext': [], 'build_src': [], 'build_clib': []}
                    if c_compiler_name is not None:
                        c = '--compiler=%s' % c_compiler_name
                        cmd_opts['config'].append(c)
                        if task != '0':
                            cmd_opts['build_ext'].append(c)
                            cmd_opts['build_clib'].append(c)
                    if f_compiler_name is not None:
                        c = '--fcompiler=%s' % f_compiler_name
                        cmd_opts['config_fc'].append(c)
                        if task != '0':
                            cmd_opts['build_ext'].append(c)
                            cmd_opts['build_clib'].append(c)
                    if task == '3':
                        cmd_opts['build_ext'].append('--inplace')
                        cmd_opts['build_src'].append('--inplace')
                    conf = []
                    sorted_keys = [
                     'config', 'config_fc', 
                     'build_src', 
                     'build_clib', 
                     'build_ext']
                    for k in sorted_keys:
                        opts = cmd_opts[k]
                        if opts:
                            conf.extend([k] + opts)

                    if task == '0':
                        if 'config' not in conf:
                            conf.append('config')
                        argv[1:] = conf
                    elif task == '1':
                        argv[1:] = conf + ['build']
                    if task == '2':
                        if prefix is not None:
                            argv[1:] = conf + ['install', '--prefix=%s' % prefix]
                        else:
                            argv[1:] = conf + ['install']
                    else:
                        if task == '3':
                            argv[1:] = conf + ['build']
                        elif task == '5':
                            if sys.platform == 'win32':
                                argv[1:] = conf + ['bdist_wininst']
                            else:
                                argv[1:] = conf + ['bdist']
                else:
                    print 'Skipping unknown task:', `task`
        else:
            print '-' * 68
            try:
                task_func(argv, readline)
            except Exception as msg:
                print 'Failed running task %s: %s' % (task, msg)
                break

            print '-' * 68
        print

    print '-' * 72
    return argv