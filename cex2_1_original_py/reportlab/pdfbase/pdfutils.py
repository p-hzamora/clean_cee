# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\pdfbase\pdfutils.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = ''
import os
from reportlab import rl_config
from reportlab.lib.utils import getStringIO, ImageReader
LINEEND = '\r\n'

def _chunker(src, dst=[], chunkSize=60):
    for i in xrange(0, len(src), chunkSize):
        dst.append(src[i:i + chunkSize])

    return dst


_mode2cs = {'RGB': 'RGB', 'CMYK': 'CMYK', 'L': 'G'}
_mode2bpp = {'RGB': 3, 'CMYK': 4, 'L': 1}

def makeA85Image(filename, IMG=None):
    import zlib
    img = ImageReader(filename)
    if IMG is not None:
        IMG.append(img)
    imgwidth, imgheight = img.getSize()
    raw = img.getRGBData()
    code = []
    append = code.append
    append('BI')
    append('/W %s /H %s /BPC 8 /CS /%s /F [/A85 /Fl]' % (imgwidth, imgheight, _mode2cs[img.mode]))
    append('ID')
    assert len(raw) == imgwidth * imgheight * _mode2bpp[img.mode], 'Wrong amount of data for image'
    compressed = zlib.compress(raw)
    encoded = _AsciiBase85Encode(compressed)
    _chunker(encoded, code)
    append('EI')
    return code


def makeRawImage(filename, IMG=None):
    import zlib
    img = ImageReader(filename)
    if IMG is not None:
        IMG.append(img)
    imgwidth, imgheight = img.getSize()
    raw = img.getRGBData()
    code = []
    append = code.append
    append('BI')
    append('/W %s /H %s /BPC 8 /CS /%s /F [/Fl]' % (imgwidth, imgheight, _mode2cs[img.mode]))
    append('ID')
    assert len(raw) == imgwidth * imgheight * _mode2bpp[img.mode], 'Wrong amount of data for image'
    compressed = zlib.compress(raw)
    _chunker(compressed, code)
    append('EI')
    return code


def cacheImageFile(filename, returnInMemory=0, IMG=None):
    """Processes image as if for encoding, saves to a file with .a85 extension."""
    cachedname = os.path.splitext(filename)[0] + (rl_config.useA85 and '.a85' or '.bin')
    if filename == cachedname:
        if cachedImageExists(filename):
            from reportlab.lib.utils import open_for_read
            if returnInMemory:
                return filter(None, open_for_read(cachedname).read().split(LINEEND))
        else:
            raise IOError, 'No such cached image %s' % filename
    else:
        if rl_config.useA85:
            code = makeA85Image(filename, IMG)
        else:
            code = makeRawImage(filename, IMG)
        if returnInMemory:
            return code
    f = open(cachedname, 'wb')
    f.write(LINEEND.join(code) + LINEEND)
    f.close()
    if rl_config.verbose:
        print 'cached image as %s' % cachedname
    return


def preProcessImages(spec):
    r"""Preprocesses one or more image files.

    Accepts either a filespec ('C:\mydir\*.jpg') or a list
    of image filenames, crunches them all to save time.  Run this
    to save huge amounts of time when repeatedly building image
    documents."""
    import types, glob
    if type(spec) is types.StringType:
        filelist = glob.glob(spec)
    else:
        filelist = spec
    for filename in filelist:
        if cachedImageExists(filename):
            if rl_config.verbose:
                print 'cached version of %s already exists' % filename
        else:
            cacheImageFile(filename)


def cachedImageExists(filename):
    """Determines if a cached image already exists for a given file.

    Determines if a cached image exists which has the same name
    and equal or newer date to the given file."""
    cachedname = os.path.splitext(filename)[0] + (rl_config.useA85 and '.a85' or 'bin')
    if os.path.isfile(cachedname):
        original_date = os.stat(filename)[8]
        cached_date = os.stat(cachedname)[8]
        if original_date > cached_date:
            return 0
        return 1
    else:
        return 0


try:
    from _rl_accel import escapePDF, _instanceEscapePDF
    _escape = escapePDF
except ImportError:
    try:
        from reportlab.lib._rl_accel import escapePDF, _instanceEscapePDF
        _escape = escapePDF
    except ImportError:
        _instanceEscapePDF = None
        if rl_config.sys_version >= '2.1':
            _ESCAPEDICT = {}
            for c in xrange(0, 256):
                if c < 32 or c >= 127:
                    _ESCAPEDICT[chr(c)] = '\\%03o' % c
                elif c in (ord('\\'), ord('('), ord(')')):
                    _ESCAPEDICT[chr(c)] = '\\' + chr(c)
                else:
                    _ESCAPEDICT[chr(c)] = chr(c)

            del c

            def _escape(s):
                return ('').join(map((lambda c, d=_ESCAPEDICT: d[c]), s))


        else:

            def _escape(s):
                """Escapes some PDF symbols (in fact, parenthesis).
                PDF escapes are almost like Python ones, but brackets
                need slashes before them too. Uses Python's repr function
                and chops off the quotes first."""
                return repr(s)[1:-1].replace('(', '\\(').replace(')', '\\)')


def _normalizeLineEnds(text, desired=LINEEND, unlikely='\x00\x01\x02\x03'):
    """Normalizes different line end character(s).

    Ensures all instances of CR, LF and CRLF end up as
    the specified one."""
    return text.replace('\r\n', unlikely).replace('\r', unlikely).replace('\n', unlikely).replace(unlikely, desired)


def _AsciiHexEncode(input):
    """Encodes input using ASCII-Hex coding.

    This is a verbose encoding used for binary data within
    a PDF file.  One byte binary becomes two bytes of ASCII.
    Helper function used by images."""
    output = getStringIO()
    for char in input:
        output.write('%02x' % ord(char))

    output.write('>')
    return output.getvalue()


def _AsciiHexDecode(input):
    """Decodes input using ASCII-Hex coding.

    Not used except to provide a test of the inverse function."""
    stripped = ('').join(input.split())
    assert stripped[-1] == '>', 'Invalid terminator for Ascii Hex Stream'
    stripped = stripped[:-1]
    assert len(stripped) % 2 == 0, 'Ascii Hex stream has odd number of bytes'
    return ('').join([ chr(int(stripped[i:i + 2], 16)) for i in xrange(0, len(stripped), 2) ])


def _AsciiBase85EncodePYTHON(input):
    """Encodes input using ASCII-Base85 coding.

        This is a compact encoding used for binary data within
        a PDF file.  Four bytes of binary data become five bytes of
        ASCII.  This is the default method used for encoding images."""
    whole_word_count, remainder_size = divmod(len(input), 4)
    cut = 4 * whole_word_count
    body, lastbit = input[0:cut], input[cut:]
    out = [].append
    for i in xrange(whole_word_count):
        offset = i * 4
        b1 = ord(body[offset])
        b2 = ord(body[offset + 1])
        b3 = ord(body[offset + 2])
        b4 = ord(body[offset + 3])
        if b1 < 128:
            num = ((b1 << 8 | b2) << 8 | b3) << 8 | b4
        else:
            num = 16777216 * b1 + 65536 * b2 + 256 * b3 + b4
        if num == 0:
            out('z')
        else:
            temp, c5 = divmod(num, 85)
            temp, c4 = divmod(temp, 85)
            temp, c3 = divmod(temp, 85)
            c1, c2 = divmod(temp, 85)
            assert 52200625 * c1 + 614125 * c2 + 7225 * c3 + 85 * c4 + c5 == num, 'dodgy code!'
            out(chr(c1 + 33))
            out(chr(c2 + 33))
            out(chr(c3 + 33))
            out(chr(c4 + 33))
            out(chr(c5 + 33))

    if remainder_size > 0:
        while len(lastbit) < 4:
            lastbit = lastbit + '\x00'

        b1 = ord(lastbit[0])
        b2 = ord(lastbit[1])
        b3 = ord(lastbit[2])
        b4 = ord(lastbit[3])
        num = 16777216 * b1 + 65536 * b2 + 256 * b3 + b4
        temp, c5 = divmod(num, 85)
        temp, c4 = divmod(temp, 85)
        temp, c3 = divmod(temp, 85)
        c1, c2 = divmod(temp, 85)
        lastword = chr(c1 + 33) + chr(c2 + 33) + chr(c3 + 33) + chr(c4 + 33) + chr(c5 + 33)
        out(lastword[0:remainder_size + 1])
    out('~>')
    return ('').join(out.__self__)


def _AsciiBase85DecodePYTHON(input):
    """Decodes input using ASCII-Base85 coding.

        This is not used - Acrobat Reader decodes for you
        - but a round trip is essential for testing."""
    stripped = ('').join(input.split())
    assert stripped[-2:] == '~>', 'Invalid terminator for Ascii Base 85 Stream'
    stripped = stripped[:-2]
    stripped = stripped.replace('z', '!!!!!')
    whole_word_count, remainder_size = divmod(len(stripped), 5)
    cut = 5 * whole_word_count
    body, lastbit = stripped[0:cut], stripped[cut:]
    out = [].append
    for i in xrange(whole_word_count):
        offset = i * 5
        c1 = ord(body[offset]) - 33
        c2 = ord(body[offset + 1]) - 33
        c3 = ord(body[offset + 2]) - 33
        c4 = ord(body[offset + 3]) - 33
        c5 = ord(body[offset + 4]) - 33
        num = 52200625 * c1 + 614125 * c2 + 7225 * c3 + 85 * c4 + c5
        temp, b4 = divmod(num, 256)
        temp, b3 = divmod(temp, 256)
        b1, b2 = divmod(temp, 256)
        assert num == 16777216 * b1 + 65536 * b2 + 256 * b3 + b4, 'dodgy code!'
        out(chr(b1))
        out(chr(b2))
        out(chr(b3))
        out(chr(b4))

    if remainder_size > 0:
        while len(lastbit) < 5:
            lastbit = lastbit + '!'

        c1 = ord(lastbit[0]) - 33
        c2 = ord(lastbit[1]) - 33
        c3 = ord(lastbit[2]) - 33
        c4 = ord(lastbit[3]) - 33
        c5 = ord(lastbit[4]) - 33
        num = (((85 * c1 + c2) * 85 + c3) * 85 + c4) * 85 + (c5 + (0, 0, 16777215,
                                                                   65535, 255)[remainder_size])
        temp, b4 = divmod(num, 256)
        temp, b3 = divmod(temp, 256)
        b1, b2 = divmod(temp, 256)
        assert num == 16777216 * b1 + 65536 * b2 + 256 * b3 + b4, 'dodgy code!'
        if remainder_size == 2:
            lastword = chr(b1)
        elif remainder_size == 3:
            lastword = chr(b1) + chr(b2)
        elif remainder_size == 4:
            lastword = chr(b1) + chr(b2) + chr(b3)
        else:
            lastword = ''
        out(lastword)
    return ('').join(out.__self__)


try:
    from _rl_accel import _AsciiBase85Encode
except ImportError:
    try:
        from reportlab.lib._rl_accel import _AsciiBase85Encode
    except ImportError:
        _AsciiBase85Encode = _AsciiBase85EncodePYTHON

try:
    from _rl_accel import _AsciiBase85Decode
except ImportError:
    try:
        from reportlab.lib._rl_accel import _AsciiBase85Decode
    except ImportError:
        _AsciiBase85Decode = _AsciiBase85DecodePYTHON

def _wrap(input, columns=60):
    """Wraps input at a given column size by inserting LINEEND characters."""
    output = []
    length = len(input)
    i = 0
    pos = columns * i
    while pos < length:
        output.append(input[pos:pos + columns])
        i = i + 1
        pos = columns * i

    if len(output[-1]) == 1:
        output[(-2):] = [
         output[-2][:-1], output[-2][-1] + output[-1]]
    return LINEEND.join(output)


def readJPEGInfo(image):
    """Read width, height and number of components from open JPEG file."""
    import struct
    from pdfdoc import PDFError
    validMarkers = [
     192, 193, 194]
    noParamMarkers = [
     208, 209, 210, 211, 212, 213, 214, 215, 216, 1]
    unsupportedMarkers = [
     195, 197, 198, 199, 200, 201, 202, 203, 205, 206, 207]
    done = 0
    while not done:
        x = struct.unpack('B', image.read(1))
        if x[0] == 255:
            x = struct.unpack('B', image.read(1))
            if x[0] in validMarkers:
                image.seek(2, 1)
                x = struct.unpack('B', image.read(1))
                if x[0] != 8:
                    raise PDFError('JPEG must have 8 bits per component')
                y = struct.unpack('BB', image.read(2))
                height = (y[0] << 8) + y[1]
                y = struct.unpack('BB', image.read(2))
                width = (y[0] << 8) + y[1]
                y = struct.unpack('B', image.read(1))
                color = y[0]
                return (
                 width, height, color)
            if x[0] in unsupportedMarkers:
                raise PDFError('JPEG Unsupported JPEG marker: %0.2x' % x[0])
            elif x[0] not in noParamMarkers:
                x = struct.unpack('BB', image.read(2))
                image.seek((x[0] << 8) + x[1] - 2, 1)


class _fusc:

    def __init__(self, k, n):
        assert k, 'Argument k should be a non empty string'
        self._k = k
        self._klen = len(k)
        self._n = int(n) or 7

    def encrypt(self, s):
        return self.__rotate(_AsciiBase85Encode(('').join(map(chr, self.__fusc(map(ord, s))))), self._n)

    def decrypt(self, s):
        return ('').join(map(chr, self.__fusc(map(ord, _AsciiBase85Decode(self.__rotate(s, -self._n))))))

    def __rotate(self, s, n):
        l = len(s)
        if n < 0:
            n = l + n
        n %= l
        if not n:
            return s
        return s[-n:] + s[:l - n]

    def __fusc(self, s):
        slen = len(s)
        return map((lambda x, y: x ^ y), s, map(ord, ((int(slen / self._klen) + 1) * self._k)[:slen]))