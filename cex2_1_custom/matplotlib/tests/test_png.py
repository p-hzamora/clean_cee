# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\test_png.pyc
# Compiled at: 2012-10-30 18:11:14
from matplotlib.testing.decorators import image_comparison, knownfailureif
from matplotlib import pyplot as plt
import matplotlib.cm as cm, glob, os, numpy as np

@image_comparison(baseline_images=['pngsuite'], extensions=['png'])
def test_pngsuite():
    dirname = os.path.join(os.path.dirname(__file__), 'baseline_images', 'pngsuite')
    files = glob.glob(os.path.join(dirname, 'basn*.png'))
    files.sort()
    fig = plt.figure(figsize=(len(files), 2))
    for i, fname in enumerate(files):
        data = plt.imread(fname)
        cmap = None
        if data.ndim == 2:
            cmap = cm.gray
        plt.imshow(data, extent=[i, i + 1, 0, 1], cmap=cmap)

    plt.gca().get_frame().set_facecolor('#ddffff')
    plt.gca().set_xlim(0, len(files))
    return


def test_imread_png_uint16():
    from matplotlib import _png
    img = _png.read_png_int(os.path.join(os.path.dirname(__file__), 'baseline_images/test_png/uint16.png'))
    assert img.dtype == np.uint16
    assert np.sum(img.flatten()) == 134184960