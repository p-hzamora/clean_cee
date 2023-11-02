# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\test_text.pyc
# Compiled at: 2012-10-30 18:11:14
from __future__ import print_function
import numpy as np, matplotlib
from matplotlib.testing.decorators import image_comparison, knownfailureif, cleanup
import matplotlib.pyplot as plt, warnings
from nose.tools import with_setup

@image_comparison(baseline_images=['font_styles'])
def test_font_styles():
    from matplotlib import _get_data_path
    data_path = _get_data_path()

    def find_matplotlib_font(**kw):
        prop = FontProperties(**kw)
        path = findfont(prop, directory=data_path)
        return FontProperties(fname=path)

    from matplotlib.font_manager import FontProperties, findfont
    warnings.filterwarnings('ignore', "findfont: Font family \\['Foo'\\] " + 'not found. Falling back to .', UserWarning, module='matplotlib.font_manager')
    fig = plt.figure()
    ax = plt.subplot(1, 1, 1)
    normalFont = find_matplotlib_font(family='sans-serif', style='normal', variant='normal', size=14)
    ax.annotate('Normal Font', (0.1, 0.1), xycoords='axes fraction', fontproperties=normalFont)
    boldFont = find_matplotlib_font(family='Foo', style='normal', variant='normal', weight='bold', stretch=500, size=14)
    ax.annotate('Bold Font', (0.1, 0.2), xycoords='axes fraction', fontproperties=boldFont)
    boldItemFont = find_matplotlib_font(family='sans serif', style='italic', variant='normal', weight=750, stretch=500, size=14)
    ax.annotate('Bold Italic Font', (0.1, 0.3), xycoords='axes fraction', fontproperties=boldItemFont)
    lightFont = find_matplotlib_font(family='sans-serif', style='normal', variant='normal', weight=200, stretch=500, size=14)
    ax.annotate('Light Font', (0.1, 0.4), xycoords='axes fraction', fontproperties=lightFont)
    condensedFont = find_matplotlib_font(family='sans-serif', style='normal', variant='normal', weight=500, stretch=100, size=14)
    ax.annotate('Condensed Font', (0.1, 0.5), xycoords='axes fraction', fontproperties=condensedFont)
    ax.set_xticks([])
    ax.set_yticks([])


@image_comparison(baseline_images=['multiline'])
def test_multiline():
    fig = plt.figure()
    ax = plt.subplot(1, 1, 1)
    ax.set_title('multiline\ntext alignment')
    ax.set_xticks([])
    ax.set_yticks([])


@image_comparison(baseline_images=['antialiased'], extensions=['png'], freetype_version=('2.4.5',
                                                                                         '2.4.6'))
def test_antialiasing():
    matplotlib.rcParams['text.antialiased'] = True
    fig = plt.figure(figsize=(5.25, 0.75))
    fig.text(0.5, 0.75, 'antialiased', horizontalalignment='center', verticalalignment='center')
    fig.text(0.5, 0.25, '$\\sqrt{x}$', horizontalalignment='center', verticalalignment='center')


def test_afm_kerning():
    from matplotlib.afm import AFM
    from matplotlib.font_manager import findfont
    fn = findfont('Helvetica', fontext='afm')
    with open(fn, 'rb') as (fh):
        afm = AFM(fh)
    assert afm.string_width_height('VAVAVAVAVAVA') == (7174.0, 718)


@image_comparison(baseline_images=['text_contains'], extensions=['png'])
def test_contains():
    import matplotlib.backend_bases as mbackend
    fig = plt.figure()
    ax = plt.axes()
    mevent = mbackend.MouseEvent('button_press_event', fig.canvas, 0.5, 0.5, 1, None)
    xs = np.linspace(0.25, 0.75, 30)
    ys = np.linspace(0.25, 0.75, 30)
    xs, ys = np.meshgrid(xs, ys)
    txt = plt.text(0.48, 0.52, 'hello world', ha='center', fontsize=30, rotation=30)
    plt.draw()
    for x, y in zip(xs.flat, ys.flat):
        mevent.x, mevent.y = plt.gca().transAxes.transform_point([x, y])
        contains, _ = txt.contains(mevent)
        color = 'yellow' if contains else 'red'
        vl = ax.viewLim.frozen()
        ax.plot(x, y, 'o', color=color)
        ax.viewLim.set(vl)

    return