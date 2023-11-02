# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\graphics\barcode\usps.pyc
# Compiled at: 2013-03-27 15:37:42
from reportlab.lib.units import inch
from common import Barcode
import string
_fim_patterns = {'A': '||  |  ||', 
   'B': '| || || |', 
   'C': '|| | | ||', 
   'D': '||| | |||'}
_postnet_patterns = {'1': '...||', 
   '2': '..|.|', '3': '..||.', '4': '.|..|', '5': '.|.|.', 
   '6': '.||..', '7': '|...|', '8': '|..|.', '9': '|.|..', 
   '0': '||...', 'S': '|'}

class FIM(Barcode):
    """
    FIM (Facing ID Marks) encode only one letter.
    There are currently four defined:

    A   Courtesy reply mail with pre-printed POSTNET
    B   Business reply mail without pre-printed POSTNET
    C   Business reply mail with pre-printed POSTNET
    D   OCR Readable mail without pre-printed POSTNET

    Options that may be passed to constructor:

        value (single character string from the set A - D. required.):
            The value to encode.

        quiet (bool, default 0):
            Whether to include quiet zones in the symbol.

    The following may also be passed, but doing so will generate nonstandard
    symbols which should not be used. This is mainly documented here to
    show the defaults:

        barHeight (float, default 5/8 inch):
            Height of the code. This might legitimately be overriden to make
            a taller symbol that will 'bleed' off the edge of the paper,
            leaving 5/8 inch remaining.

        lquiet (float, default 1/4 inch):
            Quiet zone size to left of code, if quiet is true.
            Default is the greater of .25 inch, or .15 times the symbol's
            length.

        rquiet (float, default 15/32 inch):
            Quiet zone size to right left of code, if quiet is true.

    Sources of information on FIM:

    USPS Publication 25, A Guide to Business Mail Preparation
    http://new.usps.com/cpim/ftp/pubs/pub25.pdf
    """
    barWidth = inch * (1.0 / 32.0)
    spaceWidth = inch * (1.0 / 16.0)
    barHeight = inch * (5.0 / 8.0)
    rquiet = inch * 0.25
    lquiet = inch * (15.0 / 32.0)
    quiet = 0

    def __init__(self, value='', **args):
        for k, v in args.items():
            setattr(self, k, v)

        Barcode.__init__(self, value)

    def validate(self):
        self.valid = 1
        self.validated = ''
        for c in self.value:
            if c in string.whitespace:
                continue
            elif c in 'abcdABCD':
                self.validated = self.validated + string.upper(c)
            else:
                self.valid = 0

        if len(self.validated) != 1:
            raise ValueError, 'Input must be exactly one character'
        return self.validated

    def decompose(self):
        self.decomposed = ''
        for c in self.encoded:
            self.decomposed = self.decomposed + _fim_patterns[c]

        return self.decomposed

    def computeSize(self):
        self._width = (len(self.decomposed) - 1) * self.spaceWidth + self.barWidth
        if self.quiet:
            self._width += self.lquiet + self.rquiet
        self._height = self.barHeight

    def draw(self):
        self._calculate()
        left = self.quiet and self.lquiet or 0
        for c in self.decomposed:
            if c == '|':
                self.rect(left, 0.0, self.barWidth, self.barHeight)
            left += self.spaceWidth

        self.drawHumanReadable()

    def _humanText(self):
        return self.value


class POSTNET(Barcode):
    """
    POSTNET is used in the US to encode "zip codes" (postal codes) on
    mail. It can encode 5, 9, or 11 digit codes. I've read that it's
    pointless to do 5 digits, since USPS will just have to re-print
    them with 9 or 11 digits.

    Sources of information on POSTNET:

    USPS Publication 25, A Guide to Business Mail Preparation
    http://new.usps.com/cpim/ftp/pubs/pub25.pdf
    """
    quiet = 0
    shortHeight = inch * 0.05
    barHeight = inch * 0.125
    barWidth = inch * 0.018
    spaceWidth = inch * 0.0275

    def __init__(self, value='', **args):
        for k, v in args.items():
            setattr(self, k, v)

        Barcode.__init__(self, value)

    def validate(self):
        self.validated = ''
        self.valid = 1
        count = 0
        for c in self.value:
            if c in string.whitespace + '-':
                pass
            elif c in string.digits:
                count = count + 1
                if count == 6:
                    self.validated = self.validated + '-'
                self.validated = self.validated + c
            else:
                self.valid = 0

        if len(self.validated) not in (5, 10, 12):
            self.valid = 0
        return self.validated

    def encode(self):
        self.encoded = 'S'
        check = 0
        for c in self.validated:
            if c in string.digits:
                self.encoded = self.encoded + c
                check = check + string.atoi(c)
            elif c == '-':
                pass
            else:
                raise ValueError, 'Invalid character in input'

        check = (10 - check) % 10
        self.encoded = self.encoded + repr(check) + 'S'
        return self.encoded

    def decompose(self):
        self.decomposed = ''
        for c in self.encoded:
            self.decomposed = self.decomposed + _postnet_patterns[c]

        return self.decomposed

    def computeSize(self):
        self._width = len(self.decomposed) * self.barWidth + (len(self.decomposed) - 1) * self.spaceWidth
        self._height = self.barHeight

    def draw(self):
        self._calculate()
        sdown = self.barHeight - self.shortHeight
        left = 0
        for c in self.decomposed:
            if c == '.':
                h = self.shortHeight
            else:
                h = self.barHeight
            self.rect(left, 0.0, self.barWidth, h)
            left = left + self.barWidth + self.spaceWidth

        self.drawHumanReadable()

    def _humanText(self):
        return self.encoded[1:-1]