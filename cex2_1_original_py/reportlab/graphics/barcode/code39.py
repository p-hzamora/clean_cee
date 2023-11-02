# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\graphics\barcode\code39.pyc
# Compiled at: 2013-03-27 15:37:42
from reportlab.lib.units import inch
from common import Barcode
import string
_patterns = {'0': ('bsbSBsBsb', 0), 
   '1': ('BsbSbsbsB', 1), '2': ('bsBSbsbsB', 2), 
   '3': ('BsBSbsbsb', 3), '4': ('bsbSBsbsB', 4), 
   '5': ('BsbSBsbsb', 5), '6': ('bsBSBsbsb', 6), 
   '7': ('bsbSbsBsB', 7), '8': ('BsbSbsBsb', 8), 
   '9': ('bsBSbsBsb', 9), 'A': ('BsbsbSbsB', 10), 
   'B': ('bsBsbSbsB', 11), 'C': ('BsBsbSbsb', 12), 
   'D': ('bsbsBSbsB', 13), 'E': ('BsbsBSbsb', 14), 
   'F': ('bsBsBSbsb', 15), 'G': ('bsbsbSBsB', 16), 
   'H': ('BsbsbSBsb', 17), 'I': ('bsBsbSBsb', 18), 
   'J': ('bsbsBSBsb', 19), 'K': ('BsbsbsbSB', 20), 
   'L': ('bsBsbsbSB', 21), 'M': ('BsBsbsbSb', 22), 
   'N': ('bsbsBsbSB', 23), 'O': ('BsbsBsbSb', 24), 
   'P': ('bsBsBsbSb', 25), 'Q': ('bsbsbsBSB', 26), 
   'R': ('BsbsbsBSb', 27), 'S': ('bsBsbsBSb', 28), 
   'T': ('bsbsBsBSb', 29), 'U': ('BSbsbsbsB', 30), 
   'V': ('bSBsbsbsB', 31), 'W': ('BSBsbsbsb', 32), 
   'X': ('bSbsBsbsB', 33), 'Y': ('BSbsBsbsb', 34), 
   'Z': ('bSBsBsbsb', 35), '-': ('bSbsbsBsB', 36), 
   '.': ('BSbsbsBsb', 37), ' ': ('bSBsbsBsb', 38), 
   '*': ('bSbsBsBsb', None), '$': ('bSbSbSbsb', 39), 
   '/': ('bSbSbsbSb', 40), '+': ('bSbsbSbSb', 41), 
   '%': ('bsbSbSbSb', 42)}
_stdchrs = string.digits + string.uppercase + '-. $/+%'
_extended = {'\x00': '%U', 
   '\x01': '$A', '\x02': '$B', '\x03': '$C', '\x04': '$D', 
   '\x05': '$E', '\x06': '$F', '\x07': '$G', '\x08': '$H', 
   '\t': '$I', '\n': '$J', '\x0b': '$K', '\x0c': '$L', 
   '\r': '$M', '\x0e': '$N', '\x0f': '$O', '\x10': '$P', 
   '\x11': '$Q', '\x12': '$R', '\x13': '$S', '\x14': '$T', 
   '\x15': '$U', '\x16': '$V', '\x17': '$W', '\x18': '$X', 
   '\x19': '$Y', '\x1a': '$Z', '\x1b': '%A', '\x1c': '%B', 
   '\x1d': '%C', '\x1e': '%D', '\x1f': '%E', '!': '/A', 
   '"': '/B', '#': '/C', '$': '/D', '%': '/E', 
   '&': '/F', "'": '/G', '(': '/H', ')': '/I', 
   '*': '/J', '+': '/K', ',': '/L', '/': '/O', 
   ':': '/Z', ';': '%F', '<': '%G', '=': '%H', 
   '>': '%I', '?': '%J', '@': '%V', '[': '%K', 
   '\\': '%L', ']': '%M', '^': '%N', '_': '%O', 
   '`': '%W', 'a': '+A', 'b': '+B', 'c': '+C', 
   'd': '+D', 'e': '+E', 'f': '+F', 'g': '+G', 
   'h': '+H', 'i': '+I', 'j': '+J', 'k': '+K', 
   'l': '+L', 'm': '+M', 'n': '+N', 'o': '+O', 
   'p': '+P', 'q': '+Q', 'r': '+R', 's': '+S', 
   't': '+T', 'u': '+U', 'v': '+V', 'w': '+W', 
   'x': '+X', 'y': '+Y', 'z': '+Z', '{': '%P', 
   '|': '%Q', '}': '%R', '~': '%S', '\x7f': '%T'}
_extchrs = _stdchrs + string.lowercase + '\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f' + '\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f' + '*!\'#&"(),:;<=>?@[\\]^_`{|}~\x7f'

def _encode39(value, cksum, stop):
    v = sum([ _patterns[c][1] for c in value ]) % 43
    if cksum:
        value += _stdchrs[v]
    if stop:
        value = '*' + value + '*'
    return value


class _Code39Base(Barcode):
    barWidth = inch * 0.0075
    lquiet = None
    rquiet = None
    quiet = 1
    gap = None
    barHeight = None
    ratio = 2.2
    checksum = 1
    bearers = 0.0
    stop = 1

    def __init__(self, value='', **args):
        for k, v in args.iteritems():
            setattr(self, k, v)

        if self.quiet:
            if self.lquiet is None:
                self.lquiet = max(inch * 0.25, self.barWidth * 10.0)
                self.rquiet = max(inch * 0.25, self.barWidth * 10.0)
        else:
            self.lquiet = self.rquiet = 0.0
        Barcode.__init__(self, value)
        return

    def decompose(self):
        dval = ''
        for c in self.encoded:
            dval = dval + _patterns[c][0] + 'i'

        self.decomposed = dval[:-1]
        return self.decomposed

    def _humanText(self):
        return self.stop and self.encoded[1:-1] or self.encoded


class Standard39(_Code39Base):
    """
    Options that may be passed to constructor:

        value (int, or numeric string. required.):
            The value to encode.

        barWidth (float, default .0075):
            X-Dimension, or width of the smallest element
            Minumum is .0075 inch (7.5 mils).

        ratio (float, default 2.2):
            The ratio of wide elements to narrow elements.
            Must be between 2.0 and 3.0 (or 2.2 and 3.0 if the
            barWidth is greater than 20 mils (.02 inch))

        gap (float or None, default None):
            width of intercharacter gap. None means "use barWidth".

        barHeight (float, see default below):
            Height of the symbol.  Default is the height of the two
            bearer bars (if they exist) plus the greater of .25 inch
            or .15 times the symbol's length.

        checksum (bool, default 1):
            Wether to compute and include the check digit

        bearers (float, in units of barWidth. default 0):
            Height of bearer bars (horizontal bars along the top and
            bottom of the barcode). Default is 0 (no bearers).

        quiet (bool, default 1):
            Wether to include quiet zones in the symbol.

        lquiet (float, see default below):
            Quiet zone size to left of code, if quiet is true.
            Default is the greater of .25 inch, or .15 times the symbol's
            length.

        rquiet (float, defaults as above):
            Quiet zone size to right left of code, if quiet is true.

        stop (bool, default 1):
            Whether to include start/stop symbols.

    Sources of Information on Code 39:

    http://www.semiconductor.agilent.com/barcode/sg/Misc/code_39.html
    http://www.adams1.com/pub/russadam/39code.html
    http://www.barcodeman.com/c39_1.html

    Official Spec, "ANSI/AIM BC1-1995, USS" is available for US$45 from
    http://www.aimglobal.org/aimstore/
    """

    def validate(self):
        vval = [].append
        self.valid = 1
        for c in self.value:
            if c in string.lowercase:
                c = string.upper(c)
            if c not in _stdchrs:
                self.valid = 0
                continue
            vval(c)

        self.validated = ('').join(vval.__self__)
        return self.validated

    def encode(self):
        self.encoded = _encode39(self.validated, self.checksum, self.stop)
        return self.encoded


class Extended39(_Code39Base):
    """
    Extended Code 39 is a convention for encoding additional characters
    not present in stanmdard Code 39 by using pairs of characters to
    represent the characters missing in Standard Code 39.

    See Standard39 for arguments.

    Sources of Information on Extended Code 39:

    http://www.semiconductor.agilent.com/barcode/sg/Misc/xcode_39.html
    http://www.barcodeman.com/c39_ext.html
    """

    def validate(self):
        vval = ''
        self.valid = 1
        for c in self.value:
            if c not in _extchrs:
                self.valid = 0
                continue
            vval = vval + c

        self.validated = vval
        return vval

    def encode(self):
        self.encoded = ''
        for c in self.validated:
            if c in _extended:
                self.encoded = self.encoded + _extended[c]
            elif c in _stdchrs:
                self.encoded = self.encoded + c
            else:
                raise ValueError

        self.encoded = _encode39(self.encoded, self.checksum, self.stop)
        return self.encoded