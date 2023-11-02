# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: TiffImagePlugin.pyc
# Compiled at: 2010-05-15 16:50:38
__version__ = '1.3.5'
import Image, ImageFile, ImagePalette, array, string, sys
II = 'II'
MM = 'MM'
try:
    if sys.byteorder == 'little':
        native_prefix = II
    else:
        native_prefix = MM
except AttributeError:
    if ord(array.array('i', [1]).tostring()[0]):
        native_prefix = II
    else:
        native_prefix = MM

def il16(c, o=0):
    return ord(c[o]) + (ord(c[o + 1]) << 8)


def il32(c, o=0):
    return ord(c[o]) + (ord(c[o + 1]) << 8) + (ord(c[o + 2]) << 16) + (ord(c[o + 3]) << 24)


def ol16(i):
    return chr(i & 255) + chr(i >> 8 & 255)


def ol32(i):
    return chr(i & 255) + chr(i >> 8 & 255) + chr(i >> 16 & 255) + chr(i >> 24 & 255)


def ib16(c, o=0):
    return ord(c[o + 1]) + (ord(c[o]) << 8)


def ib32(c, o=0):
    return ord(c[o + 3]) + (ord(c[o + 2]) << 8) + (ord(c[o + 1]) << 16) + (ord(c[o]) << 24)


def ob16(i):
    return chr(i >> 8 & 255) + chr(i & 255)


def ob32(i):
    return chr(i >> 24 & 255) + chr(i >> 16 & 255) + chr(i >> 8 & 255) + chr(i & 255)


IMAGEWIDTH = 256
IMAGELENGTH = 257
BITSPERSAMPLE = 258
COMPRESSION = 259
PHOTOMETRIC_INTERPRETATION = 262
FILLORDER = 266
IMAGEDESCRIPTION = 270
STRIPOFFSETS = 273
SAMPLESPERPIXEL = 277
ROWSPERSTRIP = 278
STRIPBYTECOUNTS = 279
X_RESOLUTION = 282
Y_RESOLUTION = 283
PLANAR_CONFIGURATION = 284
RESOLUTION_UNIT = 296
SOFTWARE = 305
DATE_TIME = 306
ARTIST = 315
PREDICTOR = 317
COLORMAP = 320
TILEOFFSETS = 324
EXTRASAMPLES = 338
SAMPLEFORMAT = 339
JPEGTABLES = 347
COPYRIGHT = 33432
IPTC_NAA_CHUNK = 33723
PHOTOSHOP_CHUNK = 34377
ICCPROFILE = 34675
EXIFIFD = 34665
XMP = 700
COMPRESSION_INFO = {1: 'raw', 
   2: 'tiff_ccitt', 
   3: 'group3', 
   4: 'group4', 
   5: 'tiff_lzw', 
   6: 'tiff_jpeg', 
   7: 'jpeg', 
   32771: 'tiff_raw_16', 
   32773: 'packbits'}
OPEN_INFO = {(II, 0, 1, 1, (1,), ()): (
                           '1', '1;I'), 
   (II, 0, 1, 2, (1,), ()): (
                           '1', '1;IR'), 
   (II, 0, 1, 1, (8,), ()): (
                           'L', 'L;I'), 
   (II, 0, 1, 2, (8,), ()): (
                           'L', 'L;IR'), 
   (II, 1, 1, 1, (1,), ()): (
                           '1', '1'), 
   (II, 1, 1, 2, (1,), ()): (
                           '1', '1;R'), 
   (II, 1, 1, 1, (8,), ()): (
                           'L', 'L'), 
   (II, 1, 1, 1, (8, 8), (2,)): (
                               'LA', 'LA'), 
   (II, 1, 1, 2, (8,), ()): (
                           'L', 'L;R'), 
   (II, 1, 1, 1, (16,), ()): (
                            'I;16', 'I;16'), 
   (II, 1, 2, 1, (16,), ()): (
                            'I;16S', 'I;16S'), 
   (II, 1, 2, 1, (32,), ()): (
                            'I', 'I;32S'), 
   (II, 1, 3, 1, (32,), ()): (
                            'F', 'F;32F'), 
   (II, 2, 1, 1, (8, 8, 8), ()): (
                                'RGB', 'RGB'), 
   (II, 2, 1, 2, (8, 8, 8), ()): (
                                'RGB', 'RGB;R'), 
   (II, 2, 1, 1, (8, 8, 8, 8), (0,)): (
                                     'RGBX', 'RGBX'), 
   (II, 2, 1, 1, (8, 8, 8, 8), (1,)): (
                                     'RGBA', 'RGBa'), 
   (II, 2, 1, 1, (8, 8, 8, 8), (2,)): (
                                     'RGBA', 'RGBA'), 
   (II, 2, 1, 1, (8, 8, 8, 8), (999,)): (
                                       'RGBA', 'RGBA'), 
   (II, 3, 1, 1, (1,), ()): (
                           'P', 'P;1'), 
   (II, 3, 1, 2, (1,), ()): (
                           'P', 'P;1R'), 
   (II, 3, 1, 1, (2,), ()): (
                           'P', 'P;2'), 
   (II, 3, 1, 2, (2,), ()): (
                           'P', 'P;2R'), 
   (II, 3, 1, 1, (4,), ()): (
                           'P', 'P;4'), 
   (II, 3, 1, 2, (4,), ()): (
                           'P', 'P;4R'), 
   (II, 3, 1, 1, (8,), ()): (
                           'P', 'P'), 
   (II, 3, 1, 1, (8, 8), (2,)): (
                               'PA', 'PA'), 
   (II, 3, 1, 2, (8,), ()): (
                           'P', 'P;R'), 
   (II, 5, 1, 1, (8, 8, 8, 8), ()): (
                                   'CMYK', 'CMYK'), 
   (II, 6, 1, 1, (8, 8, 8), ()): (
                                'YCbCr', 'YCbCr'), 
   (II, 8, 1, 1, (8, 8, 8), ()): (
                                'LAB', 'LAB'), 
   (MM, 0, 1, 1, (1,), ()): (
                           '1', '1;I'), 
   (MM, 0, 1, 2, (1,), ()): (
                           '1', '1;IR'), 
   (MM, 0, 1, 1, (8,), ()): (
                           'L', 'L;I'), 
   (MM, 0, 1, 2, (8,), ()): (
                           'L', 'L;IR'), 
   (MM, 1, 1, 1, (1,), ()): (
                           '1', '1'), 
   (MM, 1, 1, 2, (1,), ()): (
                           '1', '1;R'), 
   (MM, 1, 1, 1, (8,), ()): (
                           'L', 'L'), 
   (MM, 1, 1, 1, (8, 8), (2,)): (
                               'LA', 'LA'), 
   (MM, 1, 1, 2, (8,), ()): (
                           'L', 'L;R'), 
   (MM, 1, 1, 1, (16,), ()): (
                            'I;16B', 'I;16B'), 
   (MM, 1, 2, 1, (16,), ()): (
                            'I;16BS', 'I;16BS'), 
   (MM, 1, 2, 1, (32,), ()): (
                            'I;32BS', 'I;32BS'), 
   (MM, 1, 3, 1, (32,), ()): (
                            'F;32BF', 'F;32BF'), 
   (MM, 2, 1, 1, (8, 8, 8), ()): (
                                'RGB', 'RGB'), 
   (MM, 2, 1, 2, (8, 8, 8), ()): (
                                'RGB', 'RGB;R'), 
   (MM, 2, 1, 1, (8, 8, 8, 8), (0,)): (
                                     'RGBX', 'RGBX'), 
   (MM, 2, 1, 1, (8, 8, 8, 8), (1,)): (
                                     'RGBA', 'RGBa'), 
   (MM, 2, 1, 1, (8, 8, 8, 8), (2,)): (
                                     'RGBA', 'RGBA'), 
   (MM, 2, 1, 1, (8, 8, 8, 8), (999,)): (
                                       'RGBA', 'RGBA'), 
   (MM, 3, 1, 1, (1,), ()): (
                           'P', 'P;1'), 
   (MM, 3, 1, 2, (1,), ()): (
                           'P', 'P;1R'), 
   (MM, 3, 1, 1, (2,), ()): (
                           'P', 'P;2'), 
   (MM, 3, 1, 2, (2,), ()): (
                           'P', 'P;2R'), 
   (MM, 3, 1, 1, (4,), ()): (
                           'P', 'P;4'), 
   (MM, 3, 1, 2, (4,), ()): (
                           'P', 'P;4R'), 
   (MM, 3, 1, 1, (8,), ()): (
                           'P', 'P'), 
   (MM, 3, 1, 1, (8, 8), (2,)): (
                               'PA', 'PA'), 
   (MM, 3, 1, 2, (8,), ()): (
                           'P', 'P;R'), 
   (MM, 5, 1, 1, (8, 8, 8, 8), ()): (
                                   'CMYK', 'CMYK'), 
   (MM, 6, 1, 1, (8, 8, 8), ()): (
                                'YCbCr', 'YCbCr'), 
   (MM, 8, 1, 1, (8, 8, 8), ()): (
                                'LAB', 'LAB')}
PREFIXES = [
 'MM\x00*', 'II*\x00', b'II\xbc\x00']

def _accept(prefix):
    return prefix[:4] in PREFIXES


class ImageFileDirectory():

    def __init__(self, prefix):
        self.prefix = prefix[:2]
        if self.prefix == MM:
            self.i16, self.i32 = ib16, ib32
            self.o16, self.o32 = ob16, ob32
        elif self.prefix == II:
            self.i16, self.i32 = il16, il32
            self.o16, self.o32 = ol16, ol32
        else:
            raise SyntaxError('not a TIFF IFD')
        self.reset()

    def reset(self):
        self.tags = {}
        self.tagdata = {}
        self.tagtype = {}
        self.next = None
        return

    def keys(self):
        return self.tagdata.keys() + self.tags.keys()

    def items(self):
        items = self.tags.items()
        for tag in self.tagdata.keys():
            items.append((tag, self[tag]))

        return items

    def __len__(self):
        return len(self.tagdata) + len(self.tags)

    def __getitem__(self, tag):
        try:
            return self.tags[tag]
        except KeyError:
            type, data = self.tagdata[tag]
            size, handler = self.load_dispatch[type]
            self.tags[tag] = data = handler(self, data)
            del self.tagdata[tag]
            return data

    def get(self, tag, default=None):
        try:
            return self[tag]
        except KeyError:
            return default

    def getscalar(self, tag, default=None):
        try:
            value = self[tag]
            if len(value) != 1:
                if tag == SAMPLEFORMAT:
                    raise KeyError
                raise ValueError, 'not a scalar'
            return value[0]
        except KeyError:
            if default is None:
                raise
            return default

        return

    def has_key(self, tag):
        return self.tags.has_key(tag) or self.tagdata.has_key(tag)

    def __setitem__(self, tag, value):
        if type(value) is not type(()):
            value = (
             value,)
        self.tags[tag] = value

    load_dispatch = {}

    def load_byte(self, data):
        l = []
        for i in range(len(data)):
            l.append(ord(data[i]))

        return tuple(l)

    load_dispatch[1] = (1, load_byte)

    def load_string(self, data):
        if data[-1:] == '\x00':
            data = data[:-1]
        return data

    load_dispatch[2] = (1, load_string)

    def load_short(self, data):
        l = []
        for i in range(0, len(data), 2):
            l.append(self.i16(data, i))

        return tuple(l)

    load_dispatch[3] = (2, load_short)

    def load_long(self, data):
        l = []
        for i in range(0, len(data), 4):
            l.append(self.i32(data, i))

        return tuple(l)

    load_dispatch[4] = (4, load_long)

    def load_rational(self, data):
        l = []
        for i in range(0, len(data), 8):
            l.append((self.i32(data, i), self.i32(data, i + 4)))

        return tuple(l)

    load_dispatch[5] = (8, load_rational)

    def load_float(self, data):
        a = array.array('f', data)
        if self.prefix != native_prefix:
            a.byteswap()
        return tuple(a)

    load_dispatch[11] = (4, load_float)

    def load_double(self, data):
        a = array.array('d', data)
        if self.prefix != native_prefix:
            a.byteswap()
        return tuple(a)

    load_dispatch[12] = (8, load_double)

    def load_undefined(self, data):
        return data

    load_dispatch[7] = (1, load_undefined)

    def load(self, fp):
        self.reset()
        i16 = self.i16
        i32 = self.i32
        for i in range(i16(fp.read(2))):
            ifd = fp.read(12)
            tag, typ = i16(ifd), i16(ifd, 2)
            if Image.DEBUG:
                import TiffTags
                tagname = TiffTags.TAGS.get(tag, 'unknown')
                typname = TiffTags.TYPES.get(typ, 'unknown')
                print 'tag: %s (%d)' % (tagname, tag),
                print '- type: %s (%d)' % (typname, typ),
            try:
                dispatch = self.load_dispatch[typ]
            except KeyError:
                if Image.DEBUG:
                    print '- unsupported type', typ
                continue

            size, handler = dispatch
            size = size * i32(ifd, 4)
            if size > 4:
                here = fp.tell()
                fp.seek(i32(ifd, 8))
                data = ImageFile._safe_read(fp, size)
                fp.seek(here)
            else:
                data = ifd[8:8 + size]
            if len(data) != size:
                raise IOError, 'not enough data'
            self.tagdata[tag] = (typ, data)
            self.tagtype[tag] = typ
            if Image.DEBUG:
                if tag in (COLORMAP, IPTC_NAA_CHUNK, PHOTOSHOP_CHUNK, ICCPROFILE, XMP):
                    print '- value: <table: %d bytes>' % size
                else:
                    print '- value:', self[tag]

        self.next = i32(fp.read(4))

    def save(self, fp):
        o16 = self.o16
        o32 = self.o32
        fp.write(o16(len(self.tags)))
        tags = self.tags.items()
        tags.sort()
        directory = []
        append = directory.append
        offset = fp.tell() + len(self.tags) * 12 + 4
        stripoffsets = None
        for tag, value in tags:
            typ = None
            if self.tagtype.has_key(tag):
                typ = self.tagtype[tag]
            if typ == 1:
                data = value = string.join(map(chr, value), '')
            elif typ == 7:
                data = value = string.join(value, '')
            elif type(value[0]) is type(''):
                typ = 2
                data = value = string.join(value, '\x00') + '\x00'
            else:
                if tag == STRIPOFFSETS:
                    stripoffsets = len(directory)
                    typ = 4
                elif tag in (X_RESOLUTION, Y_RESOLUTION):
                    typ = 5
                elif not typ:
                    typ = 3
                    for v in value:
                        if v >= 65536:
                            typ = 4

                if typ == 3:
                    data = string.join(map(o16, value), '')
                else:
                    data = string.join(map(o32, value), '')
            if Image.DEBUG:
                import TiffTags
                tagname = TiffTags.TAGS.get(tag, 'unknown')
                typname = TiffTags.TYPES.get(typ, 'unknown')
                print 'save: %s (%d)' % (tagname, tag),
                print '- type: %s (%d)' % (typname, typ),
                if tag in (COLORMAP, IPTC_NAA_CHUNK, PHOTOSHOP_CHUNK, ICCPROFILE, XMP):
                    size = len(data)
                    print '- value: <table: %d bytes>' % size
                else:
                    print '- value:', value
            if len(data) == 4:
                append((tag, typ, len(value), data, ''))
            elif len(data) < 4:
                append((tag, typ, len(value), data + (4 - len(data)) * '\x00', ''))
            else:
                count = len(value)
                if typ == 5:
                    count = count / 2
                append((tag, typ, count, o32(offset), data))
                offset = offset + len(data)
                if offset & 1:
                    offset = offset + 1

        if stripoffsets is not None:
            tag, typ, count, value, data = directory[stripoffsets]
            assert not data, 'multistrip support not yet implemented'
            value = o32(self.i32(value) + offset)
            directory[stripoffsets] = (tag, typ, count, value, data)
        for tag, typ, count, value, data in directory:
            if Image.DEBUG > 1:
                print tag, typ, count, repr(value), repr(data)
            fp.write(o16(tag) + o16(typ) + o32(count) + value)

        fp.write('\x00\x00\x00\x00')
        for tag, typ, count, value, data in directory:
            fp.write(data)
            if len(data) & 1:
                fp.write('\x00')

        return offset


class TiffImageFile(ImageFile.ImageFile):
    format = 'TIFF'
    format_description = 'Adobe TIFF'

    def _open(self):
        """Open the first image in a TIFF file"""
        ifh = self.fp.read(8)
        if ifh[:4] not in PREFIXES:
            raise SyntaxError, 'not a TIFF file'
        self.tag = self.ifd = ImageFileDirectory(ifh[:2])
        self.__first = self.__next = self.ifd.i32(ifh, 4)
        self.__frame = -1
        self.__fp = self.fp
        self._seek(0)

    def seek(self, frame):
        """Select a given frame as current image"""
        if frame < 0:
            frame = 0
        self._seek(frame)

    def tell(self):
        """Return the current frame number"""
        return self._tell()

    def _seek(self, frame):
        self.fp = self.__fp
        if frame < self.__frame:
            self.__frame = -1
            self.__next = self.__first
        while self.__frame < frame:
            if not self.__next:
                raise EOFError, 'no more images in TIFF file'
            self.fp.seek(self.__next)
            self.tag.load(self.fp)
            self.__next = self.tag.next
            self.__frame = self.__frame + 1

        self._setup()

    def _tell(self):
        return self.__frame

    def _decoder(self, rawmode, layer):
        """Setup decoder contexts"""
        args = None
        if rawmode == 'RGB' and self._planar_configuration == 2:
            rawmode = rawmode[layer]
        compression = self._compression
        if compression == 'raw':
            args = (
             rawmode, 0, 1)
        elif compression == 'jpeg':
            args = (
             rawmode, '')
            if self.tag.has_key(JPEGTABLES):
                self.tile_prefix = self.tag[JPEGTABLES]
        elif compression == 'packbits':
            args = rawmode
        elif compression == 'tiff_lzw':
            args = rawmode
            if self.tag.has_key(317):
                self.decoderconfig = (self.tag[PREDICTOR][0],)
        if self.tag.has_key(ICCPROFILE):
            self.info['icc_profile'] = self.tag[ICCPROFILE]
        return args

    def _setup(self):
        """Setup this image object based on current tags"""
        if self.tag.has_key(48129):
            raise IOError, 'Windows Media Photo files not yet supported'
        getscalar = self.tag.getscalar
        self._compression = COMPRESSION_INFO[getscalar(COMPRESSION, 1)]
        self._planar_configuration = getscalar(PLANAR_CONFIGURATION, 1)
        photo = getscalar(PHOTOMETRIC_INTERPRETATION, 0)
        fillorder = getscalar(FILLORDER, 1)
        if Image.DEBUG:
            print '*** Summary ***'
            print '- compression:', self._compression
            print '- photometric_interpretation:', photo
            print '- planar_configuration:', self._planar_configuration
            print '- fill_order:', fillorder
        xsize = getscalar(IMAGEWIDTH)
        ysize = getscalar(IMAGELENGTH)
        self.size = (xsize, ysize)
        if Image.DEBUG:
            print '- size:', self.size
        format = getscalar(SAMPLEFORMAT, 1)
        key = (
         self.tag.prefix, photo, format, fillorder,
         self.tag.get(BITSPERSAMPLE, (1, )),
         self.tag.get(EXTRASAMPLES, ()))
        if Image.DEBUG:
            print 'format key:', key
        try:
            self.mode, rawmode = OPEN_INFO[key]
        except KeyError:
            if Image.DEBUG:
                print '- unsupported format'
            raise SyntaxError, 'unknown pixel mode'

        if Image.DEBUG:
            print '- raw mode:', rawmode
            print '- pil mode:', self.mode
        self.info['compression'] = self._compression
        xres = getscalar(X_RESOLUTION, (1, 1))
        yres = getscalar(Y_RESOLUTION, (1, 1))
        if xres and yres:
            xres = xres[0] / (xres[1] or 1)
            yres = yres[0] / (yres[1] or 1)
            resunit = getscalar(RESOLUTION_UNIT, 1)
            if resunit == 2:
                self.info['dpi'] = (
                 xres, yres)
            else:
                if resunit == 3:
                    self.info['dpi'] = (
                     xres * 2.54, yres * 2.54)
                else:
                    self.info['resolution'] = (
                     xres, yres)
        x = y = l = 0
        self.tile = []
        if self.tag.has_key(STRIPOFFSETS):
            h = getscalar(ROWSPERSTRIP, ysize)
            w = self.size[0]
            a = None
            for o in self.tag[STRIPOFFSETS]:
                if not a:
                    a = self._decoder(rawmode, l)
                self.tile.append((
                 self._compression,
                 (
                  0, min(y, ysize), w, min(y + h, ysize)),
                 o, a))
                y = y + h
                if y >= self.size[1]:
                    x = y = 0
                    l = l + 1
                    a = None

        elif self.tag.has_key(TILEOFFSETS):
            w = getscalar(322)
            h = getscalar(323)
            a = None
            for o in self.tag[TILEOFFSETS]:
                if not a:
                    a = self._decoder(rawmode, l)
                self.tile.append((
                 self._compression,
                 (
                  x, y, x + w, y + h),
                 o, a))
                x = x + w
                if x >= self.size[0]:
                    x, y = 0, y + h
                    if y >= self.size[1]:
                        x = y = 0
                        l = l + 1
                        a = None

        else:
            if Image.DEBUG:
                print '- unsupported data organization'
            raise SyntaxError('unknown data organization')
        if self.mode == 'P':
            palette = map((lambda a: chr(a / 256)), self.tag[COLORMAP])
            self.palette = ImagePalette.raw('RGB;L', string.join(palette, ''))
        return


SAVE_INFO = {'1': (
       '1', II, 1, 1, (1,), None), 
   'L': (
       'L', II, 1, 1, (8,), None), 
   'LA': (
        'LA', II, 1, 1, (8, 8), 2), 
   'P': (
       'P', II, 3, 1, (8,), None), 
   'PA': (
        'PA', II, 3, 1, (8, 8), 2), 
   'I': (
       'I;32S', II, 1, 2, (32,), None), 
   'I;16': (
          'I;16', II, 1, 1, (16,), None), 
   'I;16S': (
           'I;16S', II, 1, 2, (16,), None), 
   'F': (
       'F;32F', II, 1, 3, (32,), None), 
   'RGB': (
         'RGB', II, 2, 1, (8, 8, 8), None), 
   'RGBX': (
          'RGBX', II, 2, 1, (8, 8, 8, 8), 0), 
   'RGBA': (
          'RGBA', II, 2, 1, (8, 8, 8, 8), 2), 
   'CMYK': (
          'CMYK', II, 5, 1, (8, 8, 8, 8), None), 
   'YCbCr': (
           'YCbCr', II, 6, 1, (8, 8, 8), None), 
   'LAB': (
         'LAB', II, 8, 1, (8, 8, 8), None), 
   'I;32BS': (
            'I;32BS', MM, 1, 2, (32,), None), 
   'I;16B': (
           'I;16B', MM, 1, 1, (16,), None), 
   'I;16BS': (
            'I;16BS', MM, 1, 2, (16,), None), 
   'F;32BF': (
            'F;32BF', MM, 1, 3, (32,), None)}

def _cvt_res(value):
    if type(value) in (type([]), type(())):
        assert len(value) % 2 == 0
        return value
    if type(value) == type(1):
        return (value, 1)
    value = float(value)
    return (int(value * 65536), 65536)


def _save(im, fp, filename):
    try:
        rawmode, prefix, photo, format, bits, extra = SAVE_INFO[im.mode]
    except KeyError:
        raise IOError, 'cannot write mode %s as TIFF' % im.mode

    ifd = ImageFileDirectory(prefix)
    if fp.tell() == 0:
        fp.write(ifd.prefix + ifd.o16(42) + ifd.o32(8))
    ifd[IMAGEWIDTH] = im.size[0]
    ifd[IMAGELENGTH] = im.size[1]
    if hasattr(im, 'tag'):
        for key in (RESOLUTION_UNIT, X_RESOLUTION, Y_RESOLUTION):
            if im.tag.tagdata.has_key(key):
                ifd[key] = im.tag.tagdata.get(key)

        ifd.tagtype = im.tag.tagtype
        for key in (IPTC_NAA_CHUNK, PHOTOSHOP_CHUNK, XMP):
            if im.tag.has_key(key):
                ifd[key] = im.tag[key]

        if im.info.has_key('icc_profile'):
            ifd[ICCPROFILE] = im.info['icc_profile']
    if im.encoderinfo.has_key('description'):
        ifd[IMAGEDESCRIPTION] = im.encoderinfo['description']
    if im.encoderinfo.has_key('resolution'):
        ifd[X_RESOLUTION] = ifd[Y_RESOLUTION] = _cvt_res(im.encoderinfo['resolution'])
    if im.encoderinfo.has_key('x resolution'):
        ifd[X_RESOLUTION] = _cvt_res(im.encoderinfo['x resolution'])
    if im.encoderinfo.has_key('y resolution'):
        ifd[Y_RESOLUTION] = _cvt_res(im.encoderinfo['y resolution'])
    if im.encoderinfo.has_key('resolution unit'):
        unit = im.encoderinfo['resolution unit']
        if unit == 'inch':
            ifd[RESOLUTION_UNIT] = 2
        else:
            if unit == 'cm' or unit == 'centimeter':
                ifd[RESOLUTION_UNIT] = 3
            else:
                ifd[RESOLUTION_UNIT] = 1
    if im.encoderinfo.has_key('software'):
        ifd[SOFTWARE] = im.encoderinfo['software']
    if im.encoderinfo.has_key('date time'):
        ifd[DATE_TIME] = im.encoderinfo['date time']
    if im.encoderinfo.has_key('artist'):
        ifd[ARTIST] = im.encoderinfo['artist']
    if im.encoderinfo.has_key('copyright'):
        ifd[COPYRIGHT] = im.encoderinfo['copyright']
    dpi = im.encoderinfo.get('dpi')
    if dpi:
        ifd[RESOLUTION_UNIT] = 2
        ifd[X_RESOLUTION] = _cvt_res(dpi[0])
        ifd[Y_RESOLUTION] = _cvt_res(dpi[1])
    if bits != (1, ):
        ifd[BITSPERSAMPLE] = bits
        if len(bits) != 1:
            ifd[SAMPLESPERPIXEL] = len(bits)
    if extra is not None:
        ifd[EXTRASAMPLES] = extra
    if format != 1:
        ifd[SAMPLEFORMAT] = format
    ifd[PHOTOMETRIC_INTERPRETATION] = photo
    if im.mode == 'P':
        lut = im.im.getpalette('RGB', 'RGB;L')
        ifd[COLORMAP] = tuple(map((lambda v: ord(v) * 256), lut))
    stride = len(bits) * ((im.size[0] * bits[0] + 7) / 8)
    ifd[ROWSPERSTRIP] = im.size[1]
    ifd[STRIPBYTECOUNTS] = stride * im.size[1]
    ifd[STRIPOFFSETS] = 0
    ifd[COMPRESSION] = 1
    offset = ifd.save(fp)
    ImageFile._save(im, fp, [
     (
      'raw', (0, 0) + im.size, offset, (rawmode, stride, 1))])
    if im.encoderinfo.has_key('_debug_multipage'):
        im._debug_multipage = ifd
    return


Image.register_open('TIFF', TiffImageFile, _accept)
Image.register_save('TIFF', _save)
Image.register_extension('TIFF', '.tif')
Image.register_extension('TIFF', '.tiff')
Image.register_mime('TIFF', 'image/tiff')