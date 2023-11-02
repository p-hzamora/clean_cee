# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\graphics\barcode\code93.pyc
# Compiled at: 2013-03-27 15:37:42
from reportlab.lib.units import inch
from common import MultiWidthBarcode
import string
_patterns = {'0': ('AcAaAb', 0), 
   '1': ('AaAbAc', 1), '2': ('AaAcAb', 2), '3': ('AaAdAa', 3), 
   '4': ('AbAaAc', 4), '5': ('AbAbAb', 5), '6': ('AbAcAa', 6), 
   '7': ('AaAaAd', 7), '8': ('AcAbAa', 8), '9': ('AdAaAa', 9), 
   'A': ('BaAaAc', 10), 'B': ('BaAbAb', 11), 'C': ('BaAcAa', 12), 
   'D': ('BbAaAb', 13), 'E': ('BbAbAa', 14), 'F': ('BcAaAa', 15), 
   'G': ('AaBaAc', 16), 'H': ('AaBbAb', 17), 'I': ('AaBcAa', 18), 
   'J': ('AbBaAb', 19), 'K': ('AcBaAa', 20), 'L': ('AaAaBc', 21), 
   'M': ('AaAbBb', 22), 'N': ('AaAcBa', 23), 'O': ('AbAaBb', 24), 
   'P': ('AcAaBa', 25), 'Q': ('BaBaAb', 26), 'R': ('BaBbAa', 27), 
   'S': ('BaAaBb', 28), 'T': ('BaAbBa', 29), 'U': ('BbAaBa', 30), 
   'V': ('BbBaAa', 31), 'W': ('AaBaBb', 32), 'X': ('AaBbBa', 33), 
   'Y': ('AbBaBa', 34), 'Z': ('AbCaAa', 35), '-': ('AbAaCa', 36), 
   '.': ('CaAaAb', 37), ' ': ('CaAbAa', 38), '$': ('CbAaAa', 39), 
   '/': ('AaBaCa', 40), '+': ('AaCaBa', 41), '%': ('BaAaCa', 42), 
   '#': ('AbAbBa', 43), '!': ('CaBaAa', 44), '=': ('CaAaBa', 45), 
   '&': ('AbBbAa', 46), 'start': ('AaAaDa', -1), 
   'stop': ('AaAaDaA', -2)}
_charsbyval = {}
for k, v in _patterns.items():
    _charsbyval[v[1]] = k

_extended = {'\x00': '!U', 
   '\x01': '#A', '\x02': '#B', '\x03': '#C', '\x04': '#D', 
   '\x05': '#E', '\x06': '#F', '\x07': '#G', '\x08': '#H', 
   '\t': '#I', '\n': '#J', '\x0b': '#K', '\x0c': '#L', 
   '\r': '#M', '\x0e': '#N', '\x0f': '#O', '\x10': '#P', 
   '\x11': '#Q', '\x12': '#R', '\x13': '#S', '\x14': '#T', 
   '\x15': '#U', '\x16': '#V', '\x17': '#W', '\x18': '#X', 
   '\x19': '#Y', '\x1a': '#Z', '\x1b': '!A', '\x1c': '!B', 
   '\x1d': '!C', '\x1e': '!D', '\x1f': '!E', '!': '=A', 
   '"': '=B', '#': '=C', '$': '=D', '%': '=E', 
   '&': '=F', "'": '=G', '(': '=H', ')': '=I', 
   '*': '=J', '+': '=K', ',': '=L', '/': '=O', 
   ':': '=Z', ';': '!F', '<': '!G', '=': '!H', 
   '>': '!I', '?': '!J', '@': '!V', '[': '!K', 
   '\\': '!L', ']': '!M', '^': '!N', '_': '!O', 
   '`': '!W', 'a': '&A', 'b': '&B', 'c': '&C', 
   'd': '&D', 'e': '&E', 'f': '&F', 'g': '&G', 
   'h': '&H', 'i': '&I', 'j': '&J', 'k': '&K', 
   'l': '&L', 'm': '&M', 'n': '&N', 'o': '&O', 
   'p': '&P', 'q': '&Q', 'r': '&R', 's': '&S', 
   't': '&T', 'u': '&U', 'v': '&V', 'w': '&W', 
   'x': '&X', 'y': '&Y', 'z': '&Z', '{': '!P', 
   '|': '!Q', '}': '!R', '~': '!S', '\x7f': '!T'}

def _encode93(str):
    s = map(None, str)
    s.reverse()
    i = 0
    v = 1
    c = 0
    while i < len(s):
        c = c + v * _patterns[s[i]][1]
        i = i + 1
        v = v + 1
        if v > 20:
            v = 1

    s.insert(0, _charsbyval[c % 47])
    i = 0
    v = 1
    c = 0
    while i < len(s):
        c = c + v * _patterns[s[i]][1]
        i = i + 1
        v = v + 1
        if v > 15:
            v = 1

    s.insert(0, _charsbyval[c % 47])
    s.reverse()
    return string.join(s, '')


class _Code93Base(MultiWidthBarcode):
    barWidth = inch * 0.0075
    lquiet = None
    rquiet = None
    quiet = 1
    barHeight = None
    stop = 1

    def __init__(self, value='', **args):
        if type(value) is type(1):
            value = str(value)
        for k, v in args.iteritems():
            setattr(self, k, v)

        if self.quiet:
            if self.lquiet is None:
                self.lquiet = max(inch * 0.25, self.barWidth * 10.0)
                self.rquiet = max(inch * 0.25, self.barWidth * 10.0)
        else:
            self.lquiet = self.rquiet = 0.0
        MultiWidthBarcode.__init__(self, value)
        return

    def decompose(self):
        dval = self.stop and [_patterns['start'][0]] or []
        dval += [ _patterns[c][0] for c in self.encoded ]
        if self.stop:
            dval.append(_patterns['stop'][0])
        self.decomposed = ('').join(dval)
        return self.decomposed


class Standard93(_Code93Base):
    """
    Code 93 is a Uppercase alphanumeric symbology with some punctuation.
    See Extended Code 93 for a variant that can represent the entire
    128 characrter ASCII set.
    
    Options that may be passed to constructor:

        value (int, or numeric string. required.):
            The value to encode.
   
        barWidth (float, default .0075):
            X-Dimension, or width of the smallest element
            Minumum is .0075 inch (7.5 mils).
            
        barHeight (float, see default below):
            Height of the symbol.  Default is the height of the two
            bearer bars (if they exist) plus the greater of .25 inch
            or .15 times the symbol's length.

        quiet (bool, default 1):
            Wether to include quiet zones in the symbol.
            
        lquiet (float, see default below):
            Quiet zone size to left of code, if quiet is true.
            Default is the greater of .25 inch, or 10 barWidth
            
        rquiet (float, defaults as above):
            Quiet zone size to right left of code, if quiet is true.

        stop (bool, default 1):
            Whether to include start/stop symbols.

    Sources of Information on Code 93:

    http://www.semiconductor.agilent.com/barcode/sg/Misc/code_93.html

    Official Spec, "NSI/AIM BC5-1995, USS" is available for US$45 from
    http://www.aimglobal.org/aimstore/
    """

    def validate(self):
        vval = ''
        self.valid = 1
        for c in self.value:
            if c in string.lowercase:
                c = string.upper(c)
            if c not in _patterns:
                self.valid = 0
                continue
            vval = vval + c

        self.validated = vval
        return vval

    def encode(self):
        self.encoded = _encode93(self.validated)
        return self.encoded


class Extended93(_Code93Base):
    """
    Extended Code 93 is a convention for encoding the entire 128 character
    set using pairs of characters to represent the characters missing in
    Standard Code 93. It is very much like Extended Code 39 in that way.
    
    See Standard93 for arguments.
    """

    def validate(self):
        vval = []
        self.valid = 1
        a = vval.append
        for c in self.value:
            if c not in _patterns and c not in _extended:
                self.valid = 0
                continue
            a(c)

        self.validated = ('').join(vval)
        return self.validated

    def encode(self):
        self.encoded = ''
        for c in self.validated:
            if c in _patterns:
                self.encoded = self.encoded + c
            elif c in _extended:
                self.encoded = self.encoded + _extended[c]
            else:
                raise ValueError

        self.encoded = _encode93(self.encoded)
        return self.encoded

    def _humanText(self):
        return self.validated + self.encoded[-2:]