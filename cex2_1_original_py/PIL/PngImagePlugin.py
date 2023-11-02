# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: PIL\PngImagePlugin.pyc
# Compiled at: 2010-05-15 16:50:38
__version__ = '0.9'
import re, string, Image, ImageFile, ImagePalette, zlib

def i16(c):
    return ord(c[1]) + (ord(c[0]) << 8)


def i32(c):
    return ord(c[3]) + (ord(c[2]) << 8) + (ord(c[1]) << 16) + (ord(c[0]) << 24)


is_cid = re.compile('\\w\\w\\w\\w').match
_MAGIC = b'\x89PNG\r\n\x1a\n'
_MODES = {(1, 0): ('1', '1'), 
   (2, 0): ('L', 'L;2'), 
   (4, 0): ('L', 'L;4'), 
   (8, 0): ('L', 'L'), 
   (16, 0): ('I', 'I;16B'), 
   (8, 2): ('RGB', 'RGB'), 
   (16, 2): ('RGB', 'RGB;16B'), 
   (1, 3): ('P', 'P;1'), 
   (2, 3): ('P', 'P;2'), 
   (4, 3): ('P', 'P;4'), 
   (8, 3): ('P', 'P'), 
   (8, 4): ('LA', 'LA'), 
   (16, 4): ('RGBA', 'LA;16B'), 
   (8, 6): ('RGBA', 'RGBA'), 
   (16, 6): ('RGBA', 'RGBA;16B')}

class ChunkStream:

    def __init__(self, fp):
        self.fp = fp
        self.queue = []
        if not hasattr(Image.core, 'crc32'):
            self.crc = self.crc_skip

    def read(self):
        """Fetch a new chunk. Returns header information."""
        if self.queue:
            cid, pos, len = self.queue[-1]
            del self.queue[-1]
            self.fp.seek(pos)
        else:
            s = self.fp.read(8)
            cid = s[4:]
            pos = self.fp.tell()
            len = i32(s)
        if not is_cid(cid):
            raise SyntaxError, 'broken PNG file (chunk %s)' % repr(cid)
        return (cid, pos, len)

    def close(self):
        self.queue = self.crc = self.fp = None
        return

    def push(self, cid, pos, len):
        self.queue.append((cid, pos, len))

    def call(self, cid, pos, len):
        """Call the appropriate chunk handler"""
        if Image.DEBUG:
            print 'STREAM', cid, pos, len
        return getattr(self, 'chunk_' + cid)(pos, len)

    def crc(self, cid, data):
        """Read and verify checksum"""
        crc1 = Image.core.crc32(data, Image.core.crc32(cid))
        crc2 = (i16(self.fp.read(2)), i16(self.fp.read(2)))
        if crc1 != crc2:
            raise SyntaxError, 'broken PNG file(bad header checksum in %s)' % cid

    def crc_skip(self, cid, data):
        """Read checksum.  Used if the C module is not present"""
        self.fp.read(4)

    def verify(self, endchunk='IEND'):
        cids = []
        while 1:
            cid, pos, len = self.read()
            if cid == endchunk:
                break
            self.crc(cid, ImageFile._safe_read(self.fp, len))
            cids.append(cid)

        return cids


class PngInfo:

    def __init__(self):
        self.chunks = []

    def add(self, cid, data):
        self.chunks.append((cid, data))

    def add_text(self, key, value, zip=0):
        if zip:
            import zlib
            self.add('zTXt', key + '\x00\x00' + zlib.compress(value))
        else:
            self.add('tEXt', key + '\x00' + value)


class PngStream(ChunkStream):

    def __init__(self, fp):
        ChunkStream.__init__(self, fp)
        self.im_info = {}
        self.im_text = {}
        self.im_size = (0, 0)
        self.im_mode = None
        self.im_tile = None
        self.im_palette = None
        return

    def chunk_iCCP(self, pos, len):
        s = ImageFile._safe_read(self.fp, len)
        i = string.find(s, chr(0))
        if Image.DEBUG:
            print 'iCCP profile name', s[:i]
            print 'Compression method', ord(s[i])
        comp_method = ord(s[i])
        if comp_method != 0:
            raise SyntaxError('Unknown compression method %s in iCCP chunk' % comp_method)
        try:
            icc_profile = zlib.decompress(s[i + 2:])
        except zlib.error:
            icc_profile = None

        self.im_info['icc_profile'] = icc_profile
        return s

    def chunk_IHDR(self, pos, len):
        s = ImageFile._safe_read(self.fp, len)
        self.im_size = (i32(s), i32(s[4:]))
        try:
            self.im_mode, self.im_rawmode = _MODES[(ord(s[8]), ord(s[9]))]
        except:
            pass

        if ord(s[12]):
            self.im_info['interlace'] = 1
        if ord(s[11]):
            raise SyntaxError, 'unknown filter category'
        return s

    def chunk_IDAT(self, pos, len):
        self.im_tile = [
         (
          'zip', (0, 0) + self.im_size, pos, self.im_rawmode)]
        self.im_idat = len
        raise EOFError

    def chunk_IEND(self, pos, len):
        raise EOFError

    def chunk_PLTE(self, pos, len):
        s = ImageFile._safe_read(self.fp, len)
        if self.im_mode == 'P':
            self.im_palette = (
             'RGB', s)
        return s

    def chunk_tRNS(self, pos, len):
        s = ImageFile._safe_read(self.fp, len)
        if self.im_mode == 'P':
            i = string.find(s, chr(0))
            if i >= 0:
                self.im_info['transparency'] = i
        elif self.im_mode == 'L':
            self.im_info['transparency'] = i16(s)
        elif self.im_mode == 'RGB':
            self.im_info['transparency'] = (
             i16(s), i16(s[2:]), i16(s[4:]))
        return s

    def chunk_gAMA(self, pos, len):
        s = ImageFile._safe_read(self.fp, len)
        self.im_info['gamma'] = i32(s) / 100000.0
        return s

    def chunk_pHYs(self, pos, len):
        s = ImageFile._safe_read(self.fp, len)
        px, py = i32(s), i32(s[4:])
        unit = ord(s[8])
        if unit == 1:
            dpi = (
             int(px * 0.0254 + 0.5), int(py * 0.0254 + 0.5))
            self.im_info['dpi'] = dpi
        elif unit == 0:
            self.im_info['aspect'] = (
             px, py)
        return s

    def chunk_tEXt(self, pos, len):
        s = ImageFile._safe_read(self.fp, len)
        try:
            k, v = string.split(s, '\x00', 1)
        except ValueError:
            k = s
            v = ''

        if k:
            self.im_info[k] = self.im_text[k] = v
        return s

    def chunk_zTXt(self, pos, len):
        s = ImageFile._safe_read(self.fp, len)
        k, v = string.split(s, '\x00', 1)
        comp_method = ord(v[0])
        if comp_method != 0:
            raise SyntaxError('Unknown compression method %s in zTXt chunk' % comp_method)
        import zlib
        self.im_info[k] = self.im_text[k] = zlib.decompress(v[1:])
        return s


def _accept(prefix):
    return prefix[:8] == _MAGIC


class PngImageFile(ImageFile.ImageFile):
    format = 'PNG'
    format_description = 'Portable network graphics'

    def _open(self):
        if self.fp.read(8) != _MAGIC:
            raise SyntaxError, 'not a PNG file'
        self.png = PngStream(self.fp)
        while 1:
            cid, pos, len = self.png.read()
            try:
                s = self.png.call(cid, pos, len)
            except EOFError:
                break
            except AttributeError:
                if Image.DEBUG:
                    print cid, pos, len, '(unknown)'
                s = ImageFile._safe_read(self.fp, len)

            self.png.crc(cid, s)

        self.mode = self.png.im_mode
        self.size = self.png.im_size
        self.info = self.png.im_info
        self.text = self.png.im_text
        self.tile = self.png.im_tile
        if self.png.im_palette:
            rawmode, data = self.png.im_palette
            self.palette = ImagePalette.raw(rawmode, data)
        self.__idat = len

    def verify(self):
        """Verify PNG file"""
        if self.fp is None:
            raise RuntimeError('verify must be called directly after open')
        self.fp.seek(self.tile[0][2] - 8)
        self.png.verify()
        self.png.close()
        self.fp = None
        return

    def load_prepare(self):
        """internal: prepare to read PNG file"""
        if self.info.get('interlace'):
            self.decoderconfig = self.decoderconfig + (1, )
        ImageFile.ImageFile.load_prepare(self)

    def load_read(self, bytes):
        """internal: read more image data"""
        while self.__idat == 0:
            self.fp.read(4)
            cid, pos, len = self.png.read()
            if cid not in ('IDAT', 'DDAT'):
                self.png.push(cid, pos, len)
                return ''
            self.__idat = len

        if bytes <= 0:
            bytes = self.__idat
        else:
            bytes = min(bytes, self.__idat)
        self.__idat = self.__idat - bytes
        return self.fp.read(bytes)

    def load_end(self):
        """internal: finished reading image data"""
        self.png.close()
        self.png = None
        return


def o16(i):
    return chr(i >> 8 & 255) + chr(i & 255)


def o32(i):
    return chr(i >> 24 & 255) + chr(i >> 16 & 255) + chr(i >> 8 & 255) + chr(i & 255)


_OUTMODES = {'1': (
       '1', chr(1) + chr(0)), 
   'L;1': (
         'L;1', chr(1) + chr(0)), 
   'L;2': (
         'L;2', chr(2) + chr(0)), 
   'L;4': (
         'L;4', chr(4) + chr(0)), 
   'L': (
       'L', chr(8) + chr(0)), 
   'LA': (
        'LA', chr(8) + chr(4)), 
   'I': (
       'I;16B', chr(16) + chr(0)), 
   'P;1': (
         'P;1', chr(1) + chr(3)), 
   'P;2': (
         'P;2', chr(2) + chr(3)), 
   'P;4': (
         'P;4', chr(4) + chr(3)), 
   'P': (
       'P', chr(8) + chr(3)), 
   'RGB': (
         'RGB', chr(8) + chr(2)), 
   'RGBA': (
          'RGBA', chr(8) + chr(6))}

def putchunk(fp, cid, *data):
    """Write a PNG chunk (including CRC field)"""
    data = string.join(data, '')
    fp.write(o32(len(data)) + cid)
    fp.write(data)
    hi, lo = Image.core.crc32(data, Image.core.crc32(cid))
    fp.write(o16(hi) + o16(lo))


class _idat:

    def __init__(self, fp, chunk):
        self.fp = fp
        self.chunk = chunk

    def write(self, data):
        self.chunk(self.fp, 'IDAT', data)


def _save(im, fp, filename, chunk=putchunk, check=0):
    mode = im.mode
    if mode == 'P':
        if im.encoderinfo.has_key('bits'):
            n = 1 << im.encoderinfo['bits']
        else:
            n = 256
        if n <= 2:
            bits = 1
        elif n <= 4:
            bits = 2
        elif n <= 16:
            bits = 4
        else:
            bits = 8
        if bits != 8:
            mode = '%s;%d' % (mode, bits)
    if im.encoderinfo.has_key('dictionary'):
        dictionary = im.encoderinfo['dictionary']
    else:
        dictionary = ''
    im.encoderconfig = (im.encoderinfo.has_key('optimize'), dictionary)
    try:
        rawmode, mode = _OUTMODES[mode]
    except KeyError:
        raise IOError, 'cannot write mode %s as PNG' % mode

    if check:
        return check
    fp.write(_MAGIC)
    chunk(fp, 'IHDR', o32(im.size[0]), o32(im.size[1]), mode, chr(0), chr(0), chr(0))
    if im.mode == 'P':
        chunk(fp, 'PLTE', im.im.getpalette('RGB'))
    if im.encoderinfo.has_key('transparency'):
        if im.mode == 'P':
            transparency = max(0, min(255, im.encoderinfo['transparency']))
            chunk(fp, 'tRNS', chr(255) * transparency + chr(0))
        elif im.mode == 'L':
            transparency = max(0, min(65535, im.encoderinfo['transparency']))
            chunk(fp, 'tRNS', o16(transparency))
        else:
            if im.mode == 'RGB':
                red, green, blue = im.encoderinfo['transparency']
                chunk(fp, 'tRNS', o16(red) + o16(green) + o16(blue))
            else:
                raise IOError('cannot use transparency for this mode')
    dpi = im.encoderinfo.get('dpi')
    if dpi:
        chunk(fp, 'pHYs', o32(int(dpi[0] / 0.0254 + 0.5)), o32(int(dpi[1] / 0.0254 + 0.5)), chr(1))
    info = im.encoderinfo.get('pnginfo')
    if info:
        for cid, data in info.chunks:
            chunk(fp, cid, data)

    if im.info.has_key('icc_profile'):
        try:
            import ICCProfile
            p = ICCProfile.ICCProfile(im.info['icc_profile'])
            name = p.tags.desc.get('ASCII', p.tags.desc.get('Unicode', p.tags.desc.get('Macintosh', p.tags.desc.get('en', {}).get('US', 'ICC Profile')))).encode('latin1', 'replace')[:79]
        except ImportError:
            name = 'ICC Profile'

        data = name + '\x00\x00' + zlib.compress(im.info['icc_profile'])
        chunk(fp, 'iCCP', data)
    ImageFile._save(im, _idat(fp, chunk), [('zip', (0, 0) + im.size, 0, rawmode)])
    chunk(fp, 'IEND', '')
    try:
        fp.flush()
    except:
        pass


def getchunks(im, **params):
    """Return a list of PNG chunks representing this image."""

    class collector:
        data = []

        def write(self, data):
            pass

        def append(self, chunk):
            self.data.append(chunk)

    def append(fp, cid, *data):
        data = string.join(data, '')
        hi, lo = Image.core.crc32(data, Image.core.crc32(cid))
        crc = o16(hi) + o16(lo)
        fp.append((cid, data, crc))

    fp = collector()
    try:
        im.encoderinfo = params
        _save(im, fp, None, append)
    finally:
        del im.encoderinfo

    return fp.data


Image.register_open('PNG', PngImageFile, _accept)
Image.register_save('PNG', _save)
Image.register_extension('PNG', '.png')
Image.register_mime('PNG', 'image/png')