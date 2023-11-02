# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\test_arrow_patches.pyc
# Compiled at: 2012-11-06 08:42:20
import matplotlib.pyplot as plt
from matplotlib.testing.decorators import image_comparison

def draw_arrow(ax, t, r):
    ax.annotate('', xy=(0.5, 0.5 + r), xytext=(0.5, 0.5), size=30, arrowprops=dict(arrowstyle=t, fc='b', ec='k'))


@image_comparison(baseline_images=['fancyarrow_test_image'])
def test_fancyarrow():
    r = [0.4, 0.3, 0.2, 0.1]
    t = ['fancy', 'simple']
    fig, axes = plt.subplots(len(t), len(r), squeeze=False, subplot_kw=dict(aspect=True), figsize=(8,
                                                                                                   4.5))
    for i_r, r1 in enumerate(r):
        for i_t, t1 in enumerate(t):
            ax = axes[(i_t, i_r)]
            draw_arrow(ax, t1, r1)
            ax.tick_params(labelleft=False, labelbottom=False)


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'], exit=False)