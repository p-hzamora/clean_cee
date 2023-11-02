# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\test_artist.pyc
# Compiled at: 2012-11-06 09:32:24
from __future__ import print_function
from matplotlib.testing.decorators import cleanup
import matplotlib.pyplot as plt, matplotlib.patches as mpatches, matplotlib.transforms as mtrans, matplotlib.collections as mcollections

@cleanup
def test_patch_transform_of_none():
    ax = plt.axes()
    ax.set_xlim([1, 3])
    ax.set_ylim([1, 3])
    xy_data = (2, 2)
    xy_pix = ax.transData.transform_point(xy_data)
    e = mpatches.Ellipse(xy_data, width=1, height=1, fc='yellow', alpha=0.5)
    ax.add_patch(e)
    assert e._transform == ax.transData
    e = mpatches.Ellipse(xy_pix, width=120, height=120, fc='coral', transform=None, alpha=0.5)
    ax.add_patch(e)
    assert isinstance(e._transform, mtrans.IdentityTransform)
    e = mpatches.Ellipse(xy_pix, width=100, height=100, transform=mtrans.IdentityTransform(), alpha=0.5)
    ax.add_patch(e)
    assert isinstance(e._transform, mtrans.IdentityTransform)
    return


@cleanup
def test_collection_transform_of_none():
    ax = plt.axes()
    ax.set_xlim([1, 3])
    ax.set_ylim([1, 3])
    xy_data = (2, 2)
    xy_pix = ax.transData.transform_point(xy_data)
    e = mpatches.Ellipse(xy_data, width=1, height=1)
    c = mcollections.PatchCollection([e], facecolor='yellow', alpha=0.5)
    ax.add_collection(c)
    assert c.get_offset_transform() + c.get_transform() == ax.transData
    e = mpatches.Ellipse(xy_pix, width=120, height=120)
    c = mcollections.PatchCollection([e], facecolor='coral', alpha=0.5)
    c.set_transform(None)
    ax.add_collection(c)
    assert isinstance(c.get_transform(), mtrans.IdentityTransform)
    e = mpatches.Ellipse(xy_pix, width=100, height=100)
    c = mcollections.PatchCollection([e], transform=mtrans.IdentityTransform(), alpha=0.5)
    ax.add_collection(c)
    assert isinstance(c._transOffset, mtrans.IdentityTransform)
    return


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'], exit=False)