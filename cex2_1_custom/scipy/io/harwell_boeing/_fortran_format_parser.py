# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\io\harwell_boeing\_fortran_format_parser.pyc
# Compiled at: 2013-02-16 13:27:30
"""
Preliminary module to handle fortran formats for IO. Does not use this outside
scipy.sparse io for now, until the API is deemed reasonable.

The *Format classes handle conversion between fortran and python format, and
FortranFormatParser can create *Format instances from raw fortran format
strings (e.g. '(3I4)', '(10I3)', etc...)
"""
from __future__ import division, print_function, absolute_import
import re, warnings, numpy as np
__all__ = [
 'BadFortranFormat', 'FortranFormatParser', 'IntFormat', 'ExpFormat']
TOKENS = {'LPAR': '\\(', 
   'RPAR': '\\)', 
   'INT_ID': 'I', 
   'EXP_ID': 'E', 
   'INT': '\\d+', 
   'DOT': '\\.'}

class BadFortranFormat(SyntaxError):
    pass


def number_digits(n):
    return int(np.floor(np.log10(np.abs(n))) + 1)


class IntFormat(object):

    @classmethod
    def from_number(cls, n, min=None):
        """Given an integer, returns a "reasonable" IntFormat instance to represent
        any number between 0 and n if n > 0, -n and n if n < 0

        Parameters
        ----------
        n : int
            max number one wants to be able to represent
        min : int
            minimum number of characters to use for the format

        Returns
        -------
        res : IntFormat
            IntFormat instance with reasonable (see Notes) computed width

        Notes
        -----
        Reasonable should be understood as the minimal string length necessary
        without losing precision. For example, IntFormat.from_number(1) will
        return an IntFormat instance of width 2, so that any 0 and 1 may be
        represented as 1-character strings without loss of information.
        """
        width = number_digits(n) + 1
        if n < 0:
            width += 1
        repeat = 80 // width
        return cls(width, min, repeat=repeat)

    def __init__(self, width, min=None, repeat=None):
        self.width = width
        self.repeat = repeat
        self.min = min

    def __repr__(self):
        r = 'IntFormat('
        if self.repeat:
            r += '%d' % self.repeat
        r += 'I%d' % self.width
        if self.min:
            r += '.%d' % self.min
        return r + ')'

    @property
    def fortran_format(self):
        r = '('
        if self.repeat:
            r += '%d' % self.repeat
        r += 'I%d' % self.width
        if self.min:
            r += '.%d' % self.min
        return r + ')'

    @property
    def python_format(self):
        return '%' + str(self.width) + 'd'


class ExpFormat(object):

    @classmethod
    def from_number(cls, n, min=None):
        """Given a float number, returns a "reasonable" ExpFormat instance to
        represent any number between -n and n.

        Parameters
        ----------
        n : float
            max number one wants to be able to represent
        min : int
            minimum number of characters to use for the format

        Returns
        -------
        res : ExpFormat
            ExpFormat instance with reasonable (see Notes) computed width

        Notes
        -----
        Reasonable should be understood as the minimal string length necessary
        to avoid losing precision.
        """
        finfo = np.finfo(n.dtype)
        n_prec = finfo.precision + 1
        n_exp = number_digits(np.max(np.abs([finfo.maxexp, finfo.minexp])))
        width = 2 + n_prec + 1 + n_exp + 1
        if n < 0:
            width += 1
        repeat = int(np.floor(80 / width))
        return cls(width, n_prec, min, repeat=repeat)

    def __init__(self, width, significand, min=None, repeat=None):
        """        Parameters
        ----------
        width : int
            number of characters taken by the string (includes space).
        """
        self.width = width
        self.significand = significand
        self.repeat = repeat
        self.min = min

    def __repr__(self):
        r = 'ExpFormat('
        if self.repeat:
            r += '%d' % self.repeat
        r += 'E%d.%d' % (self.width, self.significand)
        if self.min:
            r += 'E%d' % self.min
        return r + ')'

    @property
    def fortran_format(self):
        r = '('
        if self.repeat:
            r += '%d' % self.repeat
        r += 'E%d.%d' % (self.width, self.significand)
        if self.min:
            r += 'E%d' % self.min
        return r + ')'

    @property
    def python_format(self):
        return '%' + str(self.width - 1) + '.' + str(self.significand) + 'E'


class Token(object):

    def __init__(self, type, value, pos):
        self.type = type
        self.value = value
        self.pos = pos

    def __str__(self):
        return 'Token(\'%s\', "%s")' % (self.type, self.value)

    def __repr__(self):
        return self.__str__()


class Tokenizer(object):

    def __init__(self):
        self.tokens = list(TOKENS.keys())
        self.res = [ re.compile(TOKENS[i]) for i in self.tokens ]

    def input(self, s):
        self.data = s
        self.curpos = 0
        self.len = len(s)

    def next_token(self):
        curpos = self.curpos
        tokens = self.tokens
        while curpos < self.len:
            for i, r in enumerate(self.res):
                m = r.match(self.data, curpos)
                if m is None:
                    continue
                else:
                    self.curpos = m.end()
                    return Token(self.tokens[i], m.group(), self.curpos)
            else:
                raise SyntaxError('Unknown character at position %d (%s)' % (
                 self.curpos, self.data[curpos]))

        return


class FortranFormatParser(object):
    """Parser for fortran format strings. The parse method returns a *Format
    instance.

    Notes
    -----
    Only ExpFormat (exponential format for floating values) and IntFormat
    (integer format) for now.
    """

    def __init__(self):
        self.tokenizer = Tokenizer()

    def parse(self, s):
        self.tokenizer.input(s)
        tokens = []
        try:
            while True:
                t = self.tokenizer.next_token()
                if t is None:
                    break
                else:
                    tokens.append(t)

            return self._parse_format(tokens)
        except SyntaxError as e:
            raise BadFortranFormat(str(e))

        return

    def _get_min(self, tokens):
        next = tokens.pop(0)
        if not next.type == 'DOT':
            raise SyntaxError()
        next = tokens.pop(0)
        return next.value

    def _expect(self, token, tp):
        if not token.type == tp:
            raise SyntaxError()

    def _parse_format(self, tokens):
        if not tokens[0].type == 'LPAR':
            raise SyntaxError("Expected left parenthesis at position %d (got '%s')" % (
             0, tokens[0].value))
        elif not tokens[-1].type == 'RPAR':
            raise SyntaxError("Expected right parenthesis at position %d (got '%s')" % (
             len(tokens), tokens[-1].value))
        tokens = tokens[1:-1]
        types = [ t.type for t in tokens ]
        if types[0] == 'INT':
            repeat = int(tokens.pop(0).value)
        else:
            repeat = None
        next = tokens.pop(0)
        if next.type == 'INT_ID':
            next = self._next(tokens, 'INT')
            width = int(next.value)
            if tokens:
                min = int(self._get_min(tokens))
            else:
                min = None
            return IntFormat(width, min, repeat)
        else:
            if next.type == 'EXP_ID':
                next = self._next(tokens, 'INT')
                width = int(next.value)
                next = self._next(tokens, 'DOT')
                next = self._next(tokens, 'INT')
                significand = int(next.value)
                if tokens:
                    next = self._next(tokens, 'EXP_ID')
                    next = self._next(tokens, 'INT')
                    min = int(next.value)
                else:
                    min = None
                return ExpFormat(width, significand, min, repeat)
            raise SyntaxError('Invalid formater type %s' % next.value)
            return

    def _next(self, tokens, tp):
        if not len(tokens) > 0:
            raise SyntaxError()
        next = tokens.pop(0)
        self._expect(next, tp)
        return next