# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\testing\image_util.pyc
# Compiled at: 2012-10-30 18:11:14
from __future__ import print_function
import numpy as np

def autocontrast(image, cutoff=0):
    """
    Maximize image contrast, based on histogram.  This completely
    ignores the alpha channel.
    """
    assert image.dtype == np.uint8
    output_image = np.empty((image.shape[0], image.shape[1], 3), np.uint8)
    for i in xrange(0, 3):
        plane = image[:, :, i]
        output_plane = output_image[:, :, i]
        h = np.histogram(plane, bins=256)[0]
        if cutoff:
            n = 0
            for ix in xrange(256):
                n = n + h[ix]

            cut = n * cutoff / 100
            for lo in range(256):
                if cut > h[lo]:
                    cut = cut - h[lo]
                    h[lo] = 0
                else:
                    h[lo] = h[lo] - cut
                    cut = 0
                if cut <= 0:
                    break

            cut = n * cutoff / 100
            for hi in xrange(255, -1, -1):
                if cut > h[hi]:
                    cut = cut - h[hi]
                    h[hi] = 0
                else:
                    h[hi] = h[hi] - cut
                    cut = 0
                if cut <= 0:
                    break

        for lo in xrange(256):
            if h[lo]:
                break

        for hi in xrange(255, -1, -1):
            if h[hi]:
                break

        if hi <= lo:
            output_plane[:, :] = plane
        else:
            scale = 255.0 / (hi - lo)
            offset = -lo * scale
            lut = np.arange(256, dtype=np.float)
            lut *= scale
            lut += offset
            lut = lut.clip(0, 255)
            lut = lut.astype(np.uint8)
            output_plane[:, :] = lut[plane]

    return output_image