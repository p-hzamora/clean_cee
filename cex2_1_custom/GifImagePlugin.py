# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: GifImagePlugin.pyc
# Compiled at: 2010-05-15 16:50:38
__version__ = '0.9'
import Image, ImageFile, ImagePalette

def i16(c):
    return ord(c[0]) + (ord(c[1]) << 8)


def o16(i):
    return chr(i & 255) + chr(i >> 8 & 255)


def _accept(prefix):
    return prefix[:6] in ('GIF87a', 'GIF89a')


class GifImageFile(ImageFile.ImageFile):
    format = 'GIF'
    format_description = 'Compuserve GIF'
    global_palette = None

    def data(self):
        s = self.fp.read(1)
        if s and ord(s):
            return self.fp.read(ord(s))
        else:
            return

    def _open(self):
        s = self.fp.read(13)
        if s[:6] not in ('GIF87a', 'GIF89a'):
            raise SyntaxError, 'not a GIF file'
        self.info['version'] = s[:6]
        self.size = (
         i16(s[6:]), i16(s[8:]))
        self.tile = []
        flags = ord(s[10])
        bits = (flags & 7) + 1
        if flags & 128:
            self.info['background'] = ord(s[11])
            p = self.fp.read(3 << bits)
            for i in range(0, len(p), 3):
                if not chr(i / 3) == p[i] == p[i + 1] == p[i + 2]:
                    p = ImagePalette.raw('RGB', p)
                    self.global_palette = self.palette = p
                    break

        self.__fp = self.fp
        self.__rewind = self.fp.tell()
        self.seek(0)

    def seek(self, frame):
        if frame == 0:
            self.__offset = 0
            self.dispose = None
            self.__frame = -1
            self.__fp.seek(self.__rewind)
        if frame != self.__frame + 1:
            raise ValueError, 'cannot seek to frame %d' % frame
        self.__frame = frame
        self.tile = []
        self.fp = self.__fp
        if self.__offset:
            self.fp.seek(self.__offset)
            while self.data():
                pass

            self.__offset = 0
        if self.dispose:
            self.im = self.dispose
            self.dispose = None
        self.palette = self.global_palette
        while 1:
            s = self.fp.read(1)
            if not s or s == ';':
                break
        else:
            if s == '!':
                s = self.fp.read(1)
                block = self.data()
                if ord(s) == 249:
                    flags = ord(block[0])
                    if flags & 1:
                        self.info['transparency'] = ord(block[3])
                    self.info['duration'] = i16(block[1:3]) * 10
                    try:
                        if flags & 8:
                            self.dispose = Image.core.fill('P', self.size, self.info['background'])
                        elif flags & 16:
                            self.dispose = self.im.copy()
                    except (AttributeError, KeyError):
                        pass

                elif ord(s) == 255:
                    self.info['extension'] = (
                     block, self.fp.tell())
                    if block[:11] == 'NETSCAPE2.0':
                        block = self.data()
                        if len(block) >= 3 and ord(block[0]) == 1:
                            self.info['loop'] = i16(block[1:3])
                while self.data():
                    pass

            elif s == ',':
                s = self.fp.read(9)
                x0, y0 = i16(s[0:]), i16(s[2:])
                x1, y1 = x0 + i16(s[4:]), y0 + i16(s[6:])
                flags = ord(s[8])
                interlace = flags & 64 != 0
                if flags & 128:
                    bits = (flags & 7) + 1
                    self.palette = ImagePalette.raw('RGB', self.fp.read(3 << bits))
                bits = ord(self.fp.read(1))
                self.__offset = self.fp.tell()
                self.tile = [
                 ('gif',
                  (
                   x0, y0, x1, y1),
                  self.__offset,
                  (
                   bits, interlace))]
                break
            else:
                continue

        if not self.tile:
            raise EOFError, 'no more images in GIF file'
        self.mode = 'L'
        if self.palette:
            self.mode = 'P'
        return

    def tell(self):
        return self.__frame


try:
    import _imaging_gif
except ImportError:
    _imaging_gif = None

RAWMODE = {'1': 'L', 
   'L': 'L', 
   'P': 'P'}

def _save(im, fp, filename):
    if _imaging_gif:
        try:
            _imaging_gif.save(im, fp, filename)
            return
        except IOError:
            pass

    try:
        rawmode = RAWMODE[im.mode]
        imOut = im
    except KeyError:
        if Image.getmodebase(im.mode) == 'RGB':
            imOut = im.convert('P')
            rawmode = 'P'
        else:
            imOut = im.convert('L')
            rawmode = 'L'

    for s in getheader(imOut, im.encoderinfo):
        fp.write(s)

    flags = 0
    try:
        interlace = im.encoderinfo['interlace']
    except KeyError:
        interlace = 1

    if min(im.size) < 16:
        interlace = 0
    if interlace:
        flags = flags | 64
    try:
        transparency = im.encoderinfo['transparency']
    except KeyError:
        pass
    else:
        fp.write('!' + chr(249) + chr(4) + chr(1) + o16(0) + chr(int(transparency)) + chr(0))

    fp.write(',' + o16(0) + o16(0) + o16(im.size[0]) + o16(im.size[1]) + chr(flags) + chr(8))
    imOut.encoderconfig = (
     8, interlace)
    ImageFile._save(imOut, fp, [('gif', (0, 0) + im.size, 0, rawmode)])
    fp.write('\x00')
    fp.write(';')
    try:
        fp.flush()
    except:
        pass


def _save_netpbm(im, fp, filename):
    import os
    file = im._dump()
    if im.mode != 'RGB':
        os.system('ppmtogif %s >%s' % (file, filename))
    else:
        os.system('ppmquant 256 %s | ppmtogif >%s' % (file, filename))
    try:
        os.unlink(file)
    except:
        pass


def getheader(im, info=None):
    """Return a list of strings representing a GIF header"""
    optimize = info and info.get('optimize', 0)
    s = [
     'GIF87a' + o16(im.size[0]) + o16(im.size[1]) + chr(135) + chr(0) + chr(0)]
    if optimize:
        i = 0
        maxcolor = 0
        for count in im.histogram():
            if count:
                maxcolor = i
            i = i + 1

    else:
        maxcolor = 256
    if im.mode == 'P':
        s.append(im.im.getpalette('RGB')[:maxcolor * 3])
    else:
        for i in range(maxcolor):
            s.append(chr(i) * 3)

    return s


def getdata(im, offset=(0, 0), **params):
    """Return a list of strings representing this image.
       The first string is a local image header, the rest contains
       encoded image data."""

    class collector:
        data = []

        def write(self, data):
            self.data.append(data)

    im.load()
    fp = collector()
    try:
        im.encoderinfo = params
        fp.write(',' + o16(offset[0]) + o16(offset[1]) + o16(im.size[0]) + o16(im.size[1]) + chr(0) + chr(8))
        ImageFile._save(im, fp, [('gif', (0, 0) + im.size, 0, RAWMODE[im.mode])])
        fp.write('\x00')
    finally:
        del im.encoderinfo

    return fp.data


Image.register_open(GifImageFile.format, GifImageFile, _accept)
Image.register_save(GifImageFile.format, _save)
Image.register_extension(GifImageFile.format, '.gif')
Image.register_mime(GifImageFile.format, 'image/gif')