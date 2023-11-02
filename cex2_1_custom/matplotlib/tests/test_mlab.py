# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\test_mlab.pyc
# Compiled at: 2012-10-30 18:11:14
from __future__ import print_function
import sys, numpy as np, matplotlib.mlab as mlab, tempfile
from nose.tools import raises

def test_colinear_pca():
    a = mlab.PCA._get_colinear()
    pca = mlab.PCA(a)
    assert np.allclose(pca.fracs[2:], 0.0)
    assert np.allclose(pca.Y[:, 2:], 0.0)


def test_recarray_csv_roundtrip():
    expected = np.recarray((99, ), [
     (
      'x', np.float), ('y', np.float), ('t', np.float)])
    expected['x'][:] = np.linspace(-1000000000.0, -1, 99)
    expected['y'][:] = np.linspace(1, 1000000000.0, 99)
    expected['t'][:] = np.linspace(0, 0.01, 99)
    if sys.version_info[0] == 2:
        fd = tempfile.TemporaryFile(suffix='csv', mode='wb+')
    else:
        fd = tempfile.TemporaryFile(suffix='csv', mode='w+', newline='')
    mlab.rec2csv(expected, fd)
    fd.seek(0)
    actual = mlab.csv2rec(fd)
    fd.close()
    assert np.allclose(expected['x'], actual['x'])
    assert np.allclose(expected['y'], actual['y'])
    assert np.allclose(expected['t'], actual['t'])


@raises(ValueError)
def test_rec2csv_bad_shape():
    try:
        bad = np.recarray((99, 4), [('x', np.float), ('y', np.float)])
        fd = tempfile.TemporaryFile(suffix='csv')
        mlab.rec2csv(bad, fd)
    finally:
        fd.close()


def test_prctile():
    x = [
     1, 2, 3]
    assert mlab.prctile(x, 50) == np.median(x)
    x = [
     1, 2, 3, 4]
    assert mlab.prctile(x, 50) == np.median(x)
    ob1 = [
     1, 1, 2, 2, 1, 2, 4, 3, 2, 2, 2, 3, 4, 5, 6, 7, 8, 
     9, 7, 6, 4, 5, 5]
    p = [0, 75, 100]
    expected = [1, 5.5, 9]
    actual = mlab.prctile(ob1, p)
    assert np.allclose(expected, actual)
    for pi, expectedi in zip(p, expected):
        actuali = mlab.prctile(ob1, pi)
        assert np.allclose(expectedi, actuali)