# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\lib\textsplit.pyc
# Compiled at: 2013-03-27 15:37:42
"""Helpers for text wrapping, hyphenation, Asian text splitting and kinsoku shori.

How to split a 'big word' depends on the language and the writing system.  This module
works on a Unicode string.  It ought to grow by allowing ore algoriths to be plugged
in based on possible knowledge of the language and desirable 'niceness' of the algorithm.

"""
__version__ = ' $Id$ '
from types import StringType, UnicodeType
from unicodedata import category
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.rl_config import _FUZZ
CANNOT_START_LINE = [
 '!\',.:;?!")]、。」』】〕］】）',
 '々―ぁぃぅぇぉっゃゅょゎァィゥェォッャュョヮーヵヶ',
 '゛゜・ヽヾゝゞ―‐°′″℃￠％‰']
ALL_CANNOT_START = ('').join(CANNOT_START_LINE)
CANNOT_END_LINE = [
 '‘“（[{（〔［｛〈《「『【',
 '$£@#￥＄￡＠〒§']
ALL_CANNOT_END = ('').join(CANNOT_END_LINE)

def is_multi_byte(ch):
    """Is this an Asian character?"""
    return ord(ch) >= 12288


def getCharWidths(word, fontName, fontSize):
    r"""Returns a list of glyph widths.  Should be easy to optimize in _rl_accel

    >>> getCharWidths('Hello', 'Courier', 10)
    [6.0, 6.0, 6.0, 6.0, 6.0]
    >>> from reportlab.pdfbase.cidfonts import UnicodeCIDFont
    >>> from reportlab.pdfbase.pdfmetrics import registerFont
    >>> registerFont(UnicodeCIDFont('HeiseiMin-W3'))
    >>> getCharWidths(u'\u6771\u4EAC', 'HeiseiMin-W3', 10)   #most kanji are 100 ems
    [10.0, 10.0]
    """
    return [ stringWidth(uChar, fontName, fontSize) for uChar in word ]


def wordSplit(word, maxWidths, fontName, fontSize, encoding='utf8'):
    """Attempts to break a word which lacks spaces into two parts, the first of which
    fits in the remaining space.  It is allowed to add hyphens or whatever it wishes.

    This is intended as a wrapper for some language- and user-choice-specific splitting
    algorithms.  It should only be called after line breaking on spaces, which covers western
    languages and is highly optimised already.  It works on the 'last unsplit word'.

    Presumably with further study one could write a Unicode splitting algorithm for text
    fragments whick was much faster.

    Courier characters should be 6 points wide.
    >>> wordSplit('HelloWorld', 30, 'Courier', 10)
    [[0.0, 'Hello'], [0.0, 'World']]
    >>> wordSplit('HelloWorld', 31, 'Courier', 10)
    [[1.0, 'Hello'], [1.0, 'World']]
    """
    if type(word) is not UnicodeType:
        uword = word.decode(encoding)
    else:
        uword = word
    charWidths = getCharWidths(uword, fontName, fontSize)
    lines = dumbSplit(uword, charWidths, maxWidths)
    if type(word) is not UnicodeType:
        lines2 = []
        for extraSpace, text in lines:
            lines2.append([extraSpace, text.encode(encoding)])

        lines = lines2
    return lines


def dumbSplit(word, widths, maxWidths):
    """This function attempts to fit as many characters as possible into the available
    space, cutting "like a knife" between characters.  This would do for Chinese.
    It returns a list of (text, extraSpace) items where text is a Unicode string,
    and extraSpace is the points of unused space available on the line.  This is a
    structure which is fairly easy to display, and supports 'backtracking' approaches
    after the fact.

    Test cases assume each character is ten points wide...

    >>> dumbSplit(u'Hello', [10]*5, 60)
    [[10, u'Hello']]
    >>> dumbSplit(u'Hello', [10]*5, 50)
    [[0, u'Hello']]
    >>> dumbSplit(u'Hello', [10]*5, 40)
    [[0, u'Hell'], [30, u'o']]
    """
    _more = "\n    #>>> dumbSplit(u'Hello', [10]*5, 4)   # less than one character\n    #(u'', u'Hello')\n    # this says 'Nihongo wa muzukashii desu ne!' (Japanese is difficult isn't it?) in 12 characters\n    >>> jtext = u'\\u65e5\\u672c\\u8a9e\\u306f\\u96e3\\u3057\\u3044\\u3067\\u3059\\u306d\\uff01'\n    >>> dumbSplit(jtext, [10]*11, 30)   #\n    (u'\\u65e5\\u672c\\u8a9e', u'\\u306f\\u96e3\\u3057\\u3044\\u3067\\u3059\\u306d\\uff01')\n    "
    if not isinstance(maxWidths, (list, tuple)):
        maxWidths = [maxWidths]
    assert type(word) is UnicodeType
    lines = []
    i = widthUsed = lineStartPos = 0
    maxWidth = maxWidths[0]
    nW = len(word)
    while i < nW:
        w = widths[i]
        c = word[i]
        widthUsed += w
        i += 1
        if widthUsed > maxWidth + _FUZZ and widthUsed > 0:
            extraSpace = maxWidth - widthUsed
            if ord(c) < 12288:
                limitCheck = lineStartPos + i >> 1
                for j in xrange(i - 1, limitCheck, -1):
                    cj = word[j]
                    if category(cj) == 'Zs' or ord(cj) >= 12288:
                        k = j + 1
                        if k < i:
                            j = k + 1
                            extraSpace += sum(widths[j:i])
                            w = widths[k]
                            c = word[k]
                            i = j
                            break

            if c not in ALL_CANNOT_START and i > lineStartPos + 1:
                i -= 1
                extraSpace += w
            lines.append([extraSpace, word[lineStartPos:i].strip()])
            try:
                maxWidth = maxWidths[len(lines)]
            except IndexError:
                maxWidth = maxWidths[-1]

            lineStartPos = i
            widthUsed = 0

    if widthUsed > 0:
        lines.append([maxWidth - widthUsed, word[lineStartPos:]])
    return lines


def kinsokuShoriSplit(word, widths, availWidth):
    """Split according to Japanese rules according to CJKV (Lunde).

    Essentially look for "nice splits" so that we don't end a line
    with an open bracket, or start one with a full stop, or stuff like
    that.  There is no attempt to try to split compound words into
    constituent kanji.  It currently uses wrap-down: packs as much
    on a line as possible, then backtracks if needed

    This returns a number of words each of which should just about fit
    on a line.  If you give it a whole paragraph at once, it will
    do all the splits.

    It's possible we might slightly step over the width limit
    if we do hanging punctuation marks in future (e.g. dangle a Japanese
    full stop in the right margin rather than using a whole character
    box.

    """
    lines = []
    assert len(word) == len(widths)
    curWidth = 0.0
    curLine = []
    i = 0
    while 1:
        ch = word[i]
        w = widths[i]
        if curWidth + w < availWidth:
            curLine.append(ch)
            curWidth += w
    else:
        if ch in CANNOT_END_LINE[0]:
            continue


import re
rx = re.compile('([⺀-\uffff])', re.UNICODE)

def cjkwrap(text, width, encoding='utf8'):
    return reduce((lambda line, word, width=width: '%s%s%s' % (
     line,
     [
      ' ', '\n', ''][len(line) - line.rfind('\n') - 1 + len(word.split('\n', 1)[0]) >= width or line[-1:] == '\x00' and 2],
     word)), rx.sub('\\1\\0 ', unicode(text, encoding)).split(' ')).replace('\x00', '').encode(encoding)


if __name__ == '__main__':
    import doctest, textsplit
    doctest.testmod(textsplit)