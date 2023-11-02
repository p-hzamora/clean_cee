# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\test_colorbar.pyc
# Compiled at: 2012-11-08 06:38:04
from matplotlib import rcParams, rcParamsDefault
from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.cm import get_cmap
from matplotlib.colorbar import ColorbarBase

def _colorbar_extensions(spacing):
    cmap = get_cmap('RdBu', lut=5)
    clevs = [-5.0, -2.5, -0.5, 0.5, 1.5, 3.5]
    norms = dict()
    norms['neither'] = BoundaryNorm(clevs, len(clevs) - 1)
    norms['min'] = BoundaryNorm([-10] + clevs[1:], len(clevs) - 1)
    norms['max'] = BoundaryNorm(clevs[:-1] + [10], len(clevs) - 1)
    norms['both'] = BoundaryNorm([-10] + clevs[1:-1] + [10], len(clevs) - 1)
    fig = plt.figure()
    fig.subplots_adjust(hspace=0.6)
    for i, extension_type in enumerate(('neither', 'min', 'max', 'both')):
        norm = norms[extension_type]
        boundaries = values = norm.boundaries
        for j, extendfrac in enumerate((None, 'auto', 0.1)):
            cax = fig.add_subplot(12, 1, i * 3 + j + 1)
            for item in cax.get_xticklabels() + cax.get_yticklabels() + cax.get_xticklines() + cax.get_yticklines():
                item.set_visible(False)

            cb = ColorbarBase(cax, cmap=cmap, norm=norm, boundaries=boundaries, values=values, extend=extension_type, extendfrac=extendfrac, orientation='horizontal', spacing=spacing)

    return fig


@image_comparison(baseline_images=[
 'colorbar_extensions_uniform', 'colorbar_extensions_proportional'], extensions=[
 'png'])
def test_colorbar_extensions():
    rcParams.update(rcParamsDefault)
    fig1 = _colorbar_extensions('uniform')
    fig2 = _colorbar_extensions('proportional')


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'], exit=False)