# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\test_spines.pyc
# Compiled at: 2012-10-30 18:11:14
from __future__ import print_function
import numpy as np, matplotlib
from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt

@image_comparison(baseline_images=['spines_axes_positions'])
def test_spines_axes_positions():
    fig = plt.figure()
    x = np.linspace(0, 2 * np.pi, 100)
    y = 2 * np.sin(x)
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('centered spines')
    ax.plot(x, y)
    ax.spines['right'].set_position(('axes', 0.1))
    ax.yaxis.set_ticks_position('right')
    ax.spines['top'].set_position(('axes', 0.25))
    ax.xaxis.set_ticks_position('top')
    ax.spines['left'].set_color('none')
    ax.spines['bottom'].set_color('none')