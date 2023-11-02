# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\testing\numpytest.pyc
# Compiled at: 2013-04-07 07:04:04
import os, sys, traceback
__all__ = [
 'IgnoreException', 'importall']
DEBUG = 0
get_frame = sys._getframe

class IgnoreException(Exception):
    """Ignoring this exception due to disabled feature"""
    pass


def output_exception(printstream=sys.stdout):
    try:
        type, value, tb = sys.exc_info()
        info = traceback.extract_tb(tb)
        filename, lineno, function, text = info[-1]
        msg = '%s:%d: %s: %s (in %s)\n' % (
         filename, lineno, type.__name__, str(value), function)
        printstream.write(msg)
    finally:
        type = value = tb = None

    return


def importall(package):
    """
    Try recursively to import all subpackages under package.
    """
    if isinstance(package, str):
        package = __import__(package)
    package_name = package.__name__
    package_dir = os.path.dirname(package.__file__)
    for subpackage_name in os.listdir(package_dir):
        subdir = os.path.join(package_dir, subpackage_name)
        if not os.path.isdir(subdir):
            continue
        if not os.path.isfile(os.path.join(subdir, '__init__.py')):
            continue
        name = package_name + '.' + subpackage_name
        try:
            exec 'import %s as m' % name
        except Exception as msg:
            print 'Failed importing %s: %s' % (name, msg)
            continue

        importall(m)