# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\lib\rltempfile.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = 'Helper for the test suite - determines where to write output.\n\nWhen our test suite runs as source, a script "test_foo.py" will typically\ncreate "test_foo.pdf" alongside it.  But if you are testing a package of\ncompiled code inside a zip archive, this won\'t work.  This determines\nwhere to write test suite output, creating a subdirectory of /tmp/ or\nwhatever if needed.\n\n'
_rl_tempdir = None
__all__ = ('get_rl_tempdir', 'get_rl_tempdir')
import os, tempfile

def _rl_getuid():
    if hasattr(os, 'getuid'):
        return os.getuid()
    else:
        return ''


def get_rl_tempdir(*subdirs):
    global _rl_tempdir
    if _rl_tempdir is None:
        _rl_tempdir = os.path.join(tempfile.gettempdir(), 'ReportLab_tmp%s' % str(_rl_getuid()))
    d = _rl_tempdir
    if subdirs:
        d = os.path.join(*((d,) + subdirs))
    try:
        os.makedirs(d)
    except:
        pass

    return d


def get_rl_tempfile(fn=None):
    if not fn:
        fn = tempfile.mktemp()
    return os.path.join(get_rl_tempdir(), fn)