# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\test_backend_pdf.pyc
# Compiled at: 2012-10-17 10:23:54
from matplotlib import rcParams
from matplotlib import pyplot as plt
from matplotlib.testing.decorators import image_comparison, knownfailureif

@image_comparison(baseline_images=['pdf_use14corefonts'], extensions=['pdf'])
def test_use14corefonts():
    rcParams['backend'] = 'pdf'
    rcParams['pdf.use14corefonts'] = True
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.size'] = 8
    rcParams['font.sans-serif'] = ['Helvetica']
    title = 'Test PDF backend with option use14corefonts=True'
    text = 'A three-line text positioned just above a blue line\n    and containing some French characters and the euro symbol:\n    "Merci pépé pour les 10 €"'
    plt.figure()
    plt.title(title)
    plt.text(0.5, 0.5, text, horizontalalignment='center', fontsize=24)
    plt.axhline(0.5, linewidth=0.5)