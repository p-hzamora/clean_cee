# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\test_triangulation.pyc
# Compiled at: 2012-10-30 18:11:14
import numpy as np, matplotlib.pyplot as plt, matplotlib.tri as mtri, matplotlib.delaunay as mdel
from nose.tools import assert_equal
from numpy.testing import assert_array_equal, assert_array_almost_equal
from matplotlib.testing.decorators import image_comparison

def test_delaunay():
    x = [
     0, 1, 1, 0]
    y = [0, 0, 1, 1]
    npoints = 4
    ntriangles = 2
    nedges = 5
    mpl_triang = mtri.Triangulation(x, y)
    del_triang = mdel.Triangulation(x, y)
    assert_array_almost_equal(mpl_triang.x, x)
    assert_array_almost_equal(mpl_triang.x, del_triang.x)
    assert_array_almost_equal(mpl_triang.y, y)
    assert_array_almost_equal(mpl_triang.y, del_triang.y)
    assert_equal(len(mpl_triang.triangles), ntriangles)
    assert_equal(np.min(mpl_triang.triangles), 0)
    assert_equal(np.max(mpl_triang.triangles), npoints - 1)
    assert_array_equal(mpl_triang.triangles, del_triang.triangle_nodes)
    assert_equal(len(mpl_triang.edges), nedges)
    assert_equal(np.min(mpl_triang.edges), 0)
    assert_equal(np.max(mpl_triang.edges), npoints - 1)
    assert_array_equal(mpl_triang.edges, del_triang.edge_db)


def test_delaunay_duplicate_points():
    import warnings
    x = [
     0, 1, 0, 1, 0]
    y = [0, 0, 0, 1, 1]
    duplicate_index = 2
    npoints = 4
    nduplicates = 1
    ntriangles = 2
    nedges = 5
    warnings.simplefilter('ignore')
    mpl_triang = mtri.Triangulation(x, y)
    del_triang = mdel.Triangulation(x, y)
    warnings.resetwarnings()
    assert_equal(len(mpl_triang.x), npoints + nduplicates)
    assert_equal(len(del_triang.x), npoints)
    assert_array_almost_equal(mpl_triang.x, x)
    assert_array_almost_equal(del_triang.x[:duplicate_index], x[:duplicate_index])
    assert_array_almost_equal(del_triang.x[duplicate_index:], x[duplicate_index + 1:])
    assert_equal(len(mpl_triang.y), npoints + nduplicates)
    assert_equal(len(del_triang.y), npoints)
    assert_array_almost_equal(mpl_triang.y, y)
    assert_array_almost_equal(del_triang.y[:duplicate_index], y[:duplicate_index])
    assert_array_almost_equal(del_triang.y[duplicate_index:], y[duplicate_index + 1:])
    assert_equal(len(mpl_triang.triangles), ntriangles)
    assert_equal(np.min(mpl_triang.triangles), 0)
    assert_equal(np.max(mpl_triang.triangles), npoints - 1 + nduplicates)
    assert_equal(len(del_triang.triangle_nodes), ntriangles)
    assert_equal(np.min(del_triang.triangle_nodes), 0)
    assert_equal(np.max(del_triang.triangle_nodes), npoints - 1)
    converted_indices = np.where(mpl_triang.triangles > duplicate_index, mpl_triang.triangles - nduplicates, mpl_triang.triangles)
    assert_array_equal(del_triang.triangle_nodes, converted_indices)
    assert_equal(len(mpl_triang.edges), nedges)
    assert_equal(np.min(mpl_triang.edges), 0)
    assert_equal(np.max(mpl_triang.edges), npoints - 1 + nduplicates)
    assert_equal(len(del_triang.edge_db), nedges)
    assert_equal(np.min(del_triang.edge_db), 0)
    assert_equal(np.max(del_triang.edge_db), npoints - 1)
    converted_indices = np.where(mpl_triang.edges > duplicate_index, mpl_triang.edges - nduplicates, mpl_triang.edges)
    assert_array_equal(del_triang.edge_db, converted_indices)


@image_comparison(baseline_images=['tripcolor1'])
def test_tripcolor():
    x = np.asarray([0, 0.5, 1, 0, 0.5, 1, 0, 0.5, 1, 0.75])
    y = np.asarray([0, 0, 0, 0.5, 0.5, 0.5, 1, 1, 1, 0.75])
    triangles = np.asarray([
     [
      0, 1, 3], [1, 4, 3],
     [
      1, 2, 4], [2, 5, 4],
     [
      3, 4, 6], [4, 7, 6],
     [
      4, 5, 9], [7, 4, 9], [8, 7, 9], [5, 8, 9]])
    triang = mtri.Triangulation(x, y, triangles)
    Cpoints = x + 0.5 * y
    xmid = x[triang.triangles].mean(axis=1)
    ymid = y[triang.triangles].mean(axis=1)
    Cfaces = 0.5 * xmid + ymid
    plt.subplot(121)
    plt.tripcolor(triang, Cpoints, edgecolors='k')
    plt.title('point colors')
    plt.subplot(122)
    plt.tripcolor(triang, facecolors=Cfaces, edgecolors='k')
    plt.title('facecolors')