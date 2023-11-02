# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: distutils\spawn.pyc
# Compiled at: 2012-02-24 21:58:20
"""distutils.spawn

Provides the 'spawn()' function, a front-end to various platform-
specific functions for launching another program in a sub-process.
Also provides the 'find_executable()' to search the path for a given
executable name.
"""
__revision__ = '$Id$'
import sys, os
from distutils.errors import DistutilsPlatformError, DistutilsExecError
from distutils import log

def spawn(cmd, search_path=1, verbose=0, dry_run=0):
    """Run another program, specified as a command list 'cmd', in a new process.

    'cmd' is just the argument list for the new process, ie.
    cmd[0] is the program to run and cmd[1:] are the rest of its arguments.
    There is no way to run a program with a name different from that of its
    executable.

    If 'search_path' is true (the default), the system's executable
    search path will be used to find the program; otherwise, cmd[0]
    must be the exact path to the executable.  If 'dry_run' is true,
    the command will not actually be run.

    Raise DistutilsExecError if running the program fails in any way; just
    return on success.
    """
    if os.name == 'posix':
        _spawn_posix(cmd, search_path, dry_run=dry_run)
    elif os.name == 'nt':
        _spawn_nt(cmd, search_path, dry_run=dry_run)
    elif os.name == 'os2':
        _spawn_os2(cmd, search_path, dry_run=dry_run)
    else:
        raise DistutilsPlatformError, "don't know how to spawn programs on platform '%s'" % os.name


def _nt_quote_args(args):
    """Quote command-line arguments for DOS/Windows conventions.

    Just wraps every argument which contains blanks in double quotes, and
    returns a new argument list.
    """
    for i, arg in enumerate(args):
        if ' ' in arg:
            args[i] = '"%s"' % arg

    return args


def _spawn_nt(cmd, search_path=1, verbose=0, dry_run=0):
    executable = cmd[0]
    cmd = _nt_quote_args(cmd)
    if search_path:
        executable = find_executable(executable) or executable
    log.info((' ').join([executable] + cmd[1:]))
    if not dry_run:
        try:
            rc = os.spawnv(os.P_WAIT, executable, cmd)
        except OSError as exc:
            raise DistutilsExecError, "command '%s' failed: %s" % (cmd[0], exc[-1])

        if rc != 0:
            raise DistutilsExecError, "command '%s' failed with exit status %d" % (cmd[0], rc)


def _spawn_os2(cmd, search_path=1, verbose=0, dry_run=0):
    executable = cmd[0]
    if search_path:
        executable = find_executable(executable) or executable
    log.info((' ').join([executable] + cmd[1:]))
    if not dry_run:
        try:
            rc = os.spawnv(os.P_WAIT, executable, cmd)
        except OSError as exc:
            raise DistutilsExecError, "command '%s' failed: %s" % (cmd[0], exc[-1])

        if rc != 0:
            log.debug("command '%s' failed with exit status %d" % (cmd[0], rc))
            raise DistutilsExecError, "command '%s' failed with exit status %d" % (cmd[0], rc)


if sys.platform == 'darwin':
    from distutils import sysconfig
    _cfg_target = None
    _cfg_target_split = None

def _spawn_posix(cmd, search_path=1, verbose=0, dry_run=0):
    global _cfg_target
    global _cfg_target_split
    log.info((' ').join(cmd))
    if dry_run:
        return
    else:
        exec_fn = search_path and os.execvp or os.execv
        exec_args = [cmd[0], cmd]
        if sys.platform == 'darwin':
            if _cfg_target is None:
                _cfg_target = sysconfig.get_config_var('MACOSX_DEPLOYMENT_TARGET') or ''
                if _cfg_target:
                    _cfg_target_split = [ int(x) for x in _cfg_target.split('.') ]
            if _cfg_target:
                cur_target = os.environ.get('MACOSX_DEPLOYMENT_TARGET', _cfg_target)
                if _cfg_target_split > [ int(x) for x in cur_target.split('.') ]:
                    my_msg = '$MACOSX_DEPLOYMENT_TARGET mismatch: now "%s" but "%s" during configure' % (
                     cur_target, _cfg_target)
                    raise DistutilsPlatformError(my_msg)
                env = dict(os.environ, MACOSX_DEPLOYMENT_TARGET=cur_target)
                exec_fn = search_path and os.execvpe or os.execve
                exec_args.append(env)
        pid = os.fork()
        if pid == 0:
            try:
                exec_fn(*exec_args)
            except OSError as e:
                sys.stderr.write('unable to execute %s: %s\n' % (
                 cmd[0], e.strerror))
                os._exit(1)

            sys.stderr.write('unable to execute %s for unknown reasons' % cmd[0])
            os._exit(1)
        else:
            while 1:
                try:
                    pid, status = os.waitpid(pid, 0)
                except OSError as exc:
                    import errno
                    if exc.errno == errno.EINTR:
                        continue
                    raise DistutilsExecError, "command '%s' failed: %s" % (cmd[0], exc[-1])

                if os.WIFSIGNALED(status):
                    raise DistutilsExecError, "command '%s' terminated by signal %d" % (
                     cmd[0], os.WTERMSIG(status))
                elif os.WIFEXITED(status):
                    exit_status = os.WEXITSTATUS(status)
                    if exit_status == 0:
                        return
                    raise DistutilsExecError, "command '%s' failed with exit status %d" % (
                     cmd[0], exit_status)
                elif os.WIFSTOPPED(status):
                    continue
                else:
                    raise DistutilsExecError, "unknown error executing '%s': termination status %d" % (
                     cmd[0], status)

        return


def find_executable(executable, path=None):
    """Tries to find 'executable' in the directories listed in 'path'.

    A string listing directories separated by 'os.pathsep'; defaults to
    os.environ['PATH'].  Returns the complete filename or None if not found.
    """
    if path is None:
        path = os.environ['PATH']
    paths = path.split(os.pathsep)
    base, ext = os.path.splitext(executable)
    if (sys.platform == 'win32' or os.name == 'os2') and ext != '.exe':
        executable = executable + '.exe'
    if not os.path.isfile(executable):
        for p in paths:
            f = os.path.join(p, executable)
            if os.path.isfile(f):
                return f

        return
    return executable
    return