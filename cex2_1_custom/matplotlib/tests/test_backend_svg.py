# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\test_backend_svg.pyc
# Compiled at: 2012-10-30 18:11:14
from __future__ import print_function
import matplotlib.pyplot as plt, numpy as np, sys
from io import BytesIO
import xml.parsers.expat
from matplotlib.testing.decorators import knownfailureif, cleanup

@cleanup
def test_visibility():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x = np.linspace(0, 4 * np.pi, 50)
    y = np.sin(x)
    yerr = np.ones_like(y)
    a, b, c = ax.errorbar(x, y, yerr=yerr, fmt='ko')
    for artist in b:
        artist.set_visible(False)

    fd = BytesIO()
    fig.savefig(fd, format='svg')
    fd.seek(0)
    buf = fd.read()
    fd.close()
    parser = xml.parsers.expat.ParserCreate()
    parser.Parse(buf)