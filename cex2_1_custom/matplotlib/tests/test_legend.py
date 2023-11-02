# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\test_legend.pyc
# Compiled at: 2012-10-30 18:11:14
import numpy as np
from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt

@image_comparison(baseline_images=['legend_auto1'], tol=0.0015, remove_text=True)
def test_legend_auto1():
    """Test automatic legend placement"""
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = np.arange(100)
    ax.plot(x, 50 - x, 'o', label='y=1')
    ax.plot(x, x - 50, 'o', label='y=-1')
    ax.legend(loc=0)


@image_comparison(baseline_images=['legend_auto2'], remove_text=True)
def test_legend_auto2():
    """Test automatic legend placement"""
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = np.arange(100)
    b1 = ax.bar(x, x, color='m')
    b2 = ax.bar(x, x[::-1], color='g')
    ax.legend([b1[0], b2[0]], ['up', 'down'], loc=0)


@image_comparison(baseline_images=['legend_various_labels'], remove_text=True)
def test_various_labels():
    fig = plt.figure()
    ax = fig.add_subplot(121)
    ax.plot(range(4), 'o', label=1)
    ax.plot(np.linspace(4, 4.1), 'o', label='Développés')
    ax.plot(range(4, 1, -1), 'o', label='__nolegend__')
    ax.legend(numpoints=1)


@image_comparison(baseline_images=['fancy'], remove_text=True)
def test_fancy():
    plt.subplot(121)
    plt.scatter(range(10), range(10, 0, -1), label='XX\nXX')
    plt.plot([5] * 10, 'o--', label='XX')
    plt.errorbar(range(10), range(10), xerr=0.5, yerr=0.5, label='XX')
    plt.legend(loc='center left', bbox_to_anchor=[1.0, 0.5], ncol=2, shadow=True, title='My legend', numpoints=1)