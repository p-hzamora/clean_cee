# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\f2py\__init__.pyc
# Compiled at: 2013-04-07 07:04:04
__all__ = [
 'run_main', 'compile', 'f2py_testing']
import os, sys, commands, f2py2e, f2py_testing, diagnose
from info import __doc__
run_main = f2py2e.run_main
main = f2py2e.main

def compile(source, modulename='untitled', extra_args='', verbose=1, source_fn=None):
    """ Build extension module from processing source with f2py.
    Read the source of this function for more information.
    """
    from numpy.distutils.exec_command import exec_command
    import tempfile
    if source_fn is None:
        fname = os.path.join(tempfile.mktemp() + '.f')
    else:
        fname = source_fn
    f = open(fname, 'w')
    f.write(source)
    f.close()
    args = ' -c -m %s %s %s' % (modulename, fname, extra_args)
    c = '%s -c "import numpy.f2py as f2py2e;f2py2e.main()" %s' % (sys.executable, args)
    s, o = exec_command(c)
    if source_fn is None:
        try:
            os.remove(fname)
        except OSError:
            pass

    return s


from numpy.testing import Tester
test = Tester().test
bench = Tester().bench