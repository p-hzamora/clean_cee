# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\test_ttconv.pyc
# Compiled at: 2012-10-30 18:06:02
import matplotlib
from matplotlib.font_manager import FontProperties
from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt, os.path

@image_comparison(baseline_images=['truetype-conversion'], extensions=[
 'pdf'])
def test_truetype_conversion():
    fontname = os.path.join(os.path.dirname(__file__), 'mpltest.ttf')
    fontname = os.path.abspath(fontname)
    fontprop = FontProperties(fname=fontname, size=80)
    matplotlib.rcParams['pdf.fonttype'] = 3
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.text(0, 0, 'ABCDE', fontproperties=fontprop)
    ax.set_xticks([])
    ax.set_yticks([])