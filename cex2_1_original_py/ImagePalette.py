# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: ImagePalette.pyc
# Compiled at: 2010-05-15 16:50:38
import array, Image, ImageColor

class ImagePalette:
    """Colour palette for palette mapped images"""

    def __init__(self, mode='RGB', palette=None):
        self.mode = mode
        self.rawmode = None
        self.palette = palette or range(256) * len(self.mode)
        self.colors = {}
        self.dirty = None
        if len(self.mode) * 256 != len(self.palette):
            raise ValueError, 'wrong palette size'
        return

    def getdata(self):
        if self.rawmode:
            return (self.rawmode, self.palette)
        return (
         self.mode + ';L', self.tostring())

    def tostring(self):
        if self.rawmode:
            raise ValueError('palette contains raw palette data')
        if Image.isStringType(self.palette):
            return self.palette
        return array.array('B', self.palette).tostring()

    def getcolor(self, color):
        if self.rawmode:
            raise ValueError('palette contains raw palette data')
        if Image.isTupleType(color):
            try:
                return self.colors[color]
            except KeyError:
                if Image.isStringType(self.palette):
                    self.palette = map(int, self.palette)
                index = len(self.colors)
                if index >= 256:
                    raise ValueError('cannot allocate more than 256 colors')
                self.colors[color] = index
                self.palette[index] = color[0]
                self.palette[index + 256] = color[1]
                self.palette[index + 512] = color[2]
                self.dirty = 1
                return index

        else:
            raise ValueError('unknown color specifier: %r' % color)

    def save(self, fp):
        if self.rawmode:
            raise ValueError('palette contains raw palette data')
        if type(fp) == type(''):
            fp = open(fp, 'w')
        fp.write('# Palette\n')
        fp.write('# Mode: %s\n' % self.mode)
        for i in range(256):
            fp.write('%d' % i)
            for j in range(i, len(self.palette), 256):
                fp.write(' %d' % self.palette[j])

            fp.write('\n')

        fp.close()


def raw(rawmode, data):
    palette = ImagePalette()
    palette.rawmode = rawmode
    palette.palette = data
    palette.dirty = 1
    return palette


def _make_linear_lut(black, white):
    lut = []
    if black == 0:
        for i in range(256):
            lut.append(white * i / 255)

    else:
        raise NotImplementedError
    return lut


def _make_gamma_lut(exp, mode='RGB'):
    lut = []
    for i in range(256):
        lut.append(int((i / 255.0) ** exp * 255.0 + 0.5))

    return lut


def new(mode, data):
    return Image.core.new_palette(mode, data)


def negative(mode='RGB'):
    palette = range(256)
    palette.reverse()
    return ImagePalette(mode, palette * len(mode))


def random(mode='RGB'):
    from random import randint
    palette = []
    for i in range(256 * len(mode)):
        palette.append(randint(0, 255))

    return ImagePalette(mode, palette)


def sepia(white='#fff0c0'):
    r, g, b = ImageColor.getrgb(white)
    r = _make_linear_lut(0, r)
    g = _make_linear_lut(0, g)
    b = _make_linear_lut(0, b)
    return ImagePalette('RGB', r + g + b)


def wedge(mode='RGB'):
    return ImagePalette(mode, range(256) * len(mode))


def load(filename):
    fp = open(filename, 'rb')
    lut = None
    if not lut:
        try:
            import GimpPaletteFile
            fp.seek(0)
            p = GimpPaletteFile.GimpPaletteFile(fp)
            lut = p.getpalette()
        except (SyntaxError, ValueError):
            pass

    if not lut:
        try:
            import GimpGradientFile
            fp.seek(0)
            p = GimpGradientFile.GimpGradientFile(fp)
            lut = p.getpalette()
        except (SyntaxError, ValueError):
            pass

    if not lut:
        try:
            import PaletteFile
            fp.seek(0)
            p = PaletteFile.PaletteFile(fp)
            lut = p.getpalette()
        except (SyntaxError, ValueError):
            pass

    if not lut:
        raise IOError, 'cannot load palette'
    return lut