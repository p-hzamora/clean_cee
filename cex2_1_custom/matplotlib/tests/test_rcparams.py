# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\test_rcparams.pyc
# Compiled at: 2012-10-30 18:11:14
import os, matplotlib as mpl
mpl.rc('text', usetex=False)
mpl.rc('lines', linewidth=22)
fname = os.path.join(os.path.dirname(__file__), 'test_rcparams.rc')

def test_rcparams():
    usetex = mpl.rcParams['text.usetex']
    linewidth = mpl.rcParams['lines.linewidth']
    with mpl.rc_context(rc={'text.usetex': not usetex}):
        assert mpl.rcParams['text.usetex'] == (not usetex)
    assert mpl.rcParams['text.usetex'] == usetex
    with mpl.rc_context(fname=fname):
        assert mpl.rcParams['lines.linewidth'] == 33
    assert mpl.rcParams['lines.linewidth'] == linewidth
    with mpl.rc_context(fname=fname, rc={'lines.linewidth': 44}):
        assert mpl.rcParams['lines.linewidth'] == 44
    assert mpl.rcParams['lines.linewidth'] == linewidth
    try:
        mpl.rc_file(fname)
        assert mpl.rcParams['lines.linewidth'] == 33
    finally:
        mpl.rcParams['lines.linewidth'] = linewidth


if __name__ == '__main__':
    test_rcparams()