# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\pdfbase\cidfonts.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = 'CID (Asian multi-byte) font support.\n\nThis defines classes to represent CID fonts.  They know how to calculate\ntheir own width and how to write themselves into PDF files.'
import os
from types import ListType, TupleType, DictType
from string import find, split, strip
import marshal, time
try:
    from hashlib import md5
except ImportError:
    from md5 import md5

import reportlab
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase._cidfontdata import allowedTypeFaces, allowedEncodings, CIDFontInfo, defaultUnicodeEncodings, widthsByUnichar
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfdoc
from reportlab.pdfbase.pdfutils import _escape
from reportlab.rl_config import CMapSearchPath
DISABLE_CMAP = True

def findCMapFile(name):
    """Returns full filename, or raises error"""
    for dirname in CMapSearchPath:
        cmapfile = dirname + os.sep + name
        if os.path.isfile(cmapfile):
            return cmapfile

    raise IOError, 'CMAP file for encodings "%s" not found!' % name


def structToPDF(structure):
    """Converts deeply nested structure to PDFdoc dictionary/array objects"""
    if type(structure) is DictType:
        newDict = {}
        for k, v in structure.items():
            newDict[k] = structToPDF(v)

        return pdfdoc.PDFDictionary(newDict)
    else:
        if type(structure) in (ListType, TupleType):
            newList = []
            for elem in structure:
                newList.append(structToPDF(elem))

            return pdfdoc.PDFArray(newList)
        return structure


class CIDEncoding(pdfmetrics.Encoding):
    """Multi-byte encoding.  These are loaded from CMAP files.

    A CMAP file is like a mini-codec.  It defines the correspondence
    between code points in the (multi-byte) input data and Character
    IDs. """

    def __init__(self, name, useCache=1):
        self.name = name
        self._mapFileHash = None
        self._codeSpaceRanges = []
        self._notDefRanges = []
        self._cmap = {}
        self.source = None
        if not DISABLE_CMAP:
            if useCache:
                from reportlab.lib.utils import get_rl_tempdir
                fontmapdir = get_rl_tempdir('FastCMAPS')
                if os.path.isfile(fontmapdir + os.sep + name + '.fastmap'):
                    self.fastLoad(fontmapdir)
                    self.source = fontmapdir + os.sep + name + '.fastmap'
                else:
                    self.parseCMAPFile(name)
                    self.source = 'CMAP: ' + name
                    self.fastSave(fontmapdir)
            else:
                self.parseCMAPFile(name)
        return

    def _hash(self, text):
        hasher = md5()
        hasher.update(text)
        return hasher.digest()

    def parseCMAPFile(self, name):
        """This is a tricky one as CMAP files are Postscript
        ones.  Some refer to others with a 'usecmap'
        command"""
        cmapfile = findCMapFile(name)
        rawdata = open(cmapfile, 'r').read()
        self._mapFileHash = self._hash(rawdata)
        usecmap_pos = find(rawdata, 'usecmap')
        if usecmap_pos > -1:
            chunk = rawdata[0:usecmap_pos]
            words = split(chunk)
            otherCMAPName = words[-1]
            self.parseCMAPFile(otherCMAPName)
        words = split(rawdata)
        while words != []:
            if words[0] == 'begincodespacerange':
                words = words[1:]
                while words[0] != 'endcodespacerange':
                    strStart, strEnd, words = words[0], words[1], words[2:]
                    start = int(strStart[1:-1], 16)
                    end = int(strEnd[1:-1], 16)
                    self._codeSpaceRanges.append((start, end))

            elif words[0] == 'beginnotdefrange':
                words = words[1:]
                while words[0] != 'endnotdefrange':
                    strStart, strEnd, strValue = words[0:3]
                    start = int(strStart[1:-1], 16)
                    end = int(strEnd[1:-1], 16)
                    value = int(strValue)
                    self._notDefRanges.append((start, end, value))
                    words = words[3:]

            elif words[0] == 'begincidrange':
                words = words[1:]
                while words[0] != 'endcidrange':
                    strStart, strEnd, strValue = words[0:3]
                    start = int(strStart[1:-1], 16)
                    end = int(strEnd[1:-1], 16)
                    value = int(strValue)
                    offset = 0
                    while start + offset <= end:
                        self._cmap[start + offset] = value + offset
                        offset = offset + 1

                    words = words[3:]

            else:
                words = words[1:]

    def translate(self, text):
        """Convert a string into a list of CIDs"""
        output = []
        cmap = self._cmap
        lastChar = ''
        for char in text:
            if lastChar != '':
                num = ord(lastChar) * 256 + ord(char)
            else:
                num = ord(char)
            lastChar = char
            found = 0
            for low, high in self._codeSpaceRanges:
                if low < num < high:
                    try:
                        cid = cmap[num]
                    except KeyError:
                        cid = 0
                        for low2, high2, notdef in self._notDefRanges:
                            if low2 < num < high2:
                                cid = notdef
                                break

                    output.append(cid)
                    found = 1
                    break

            if found:
                lastChar = ''
            else:
                lastChar = char

        return output

    def fastSave(self, directory):
        f = open(os.path.join(directory, self.name + '.fastmap'), 'wb')
        marshal.dump(self._mapFileHash, f)
        marshal.dump(self._codeSpaceRanges, f)
        marshal.dump(self._notDefRanges, f)
        marshal.dump(self._cmap, f)
        f.close()

    def fastLoad(self, directory):
        started = time.clock()
        f = open(os.path.join(directory, self.name + '.fastmap'), 'rb')
        self._mapFileHash = marshal.load(f)
        self._codeSpaceRanges = marshal.load(f)
        self._notDefRanges = marshal.load(f)
        self._cmap = marshal.load(f)
        f.close()
        finished = time.clock()

    def getData(self):
        """Simple persistence helper.  Return a dict with all that matters."""
        return {'mapFileHash': self._mapFileHash, 
           'codeSpaceRanges': self._codeSpaceRanges, 
           'notDefRanges': self._notDefRanges, 
           'cmap': self._cmap}


class CIDTypeFace(pdfmetrics.TypeFace):
    """Multi-byte type face.

    Conceptually similar to a single byte typeface,
    but the glyphs are identified by a numeric Character
    ID (CID) and not a glyph name. """

    def __init__(self, name):
        """Initialised from one of the canned dictionaries in allowedEncodings

        Or rather, it will be shortly..."""
        pdfmetrics.TypeFace.__init__(self, name)
        self._extractDictInfo(name)

    def _extractDictInfo(self, name):
        try:
            fontDict = CIDFontInfo[name]
        except KeyError:
            raise KeyError, "Unable to find information on CID typeface '%s'" % name + 'Only the following font names work:' + repr(allowedTypeFaces)

        descFont = fontDict['DescendantFonts'][0]
        self.ascent = descFont['FontDescriptor']['Ascent']
        self.descent = descFont['FontDescriptor']['Descent']
        self._defaultWidth = descFont['DW']
        self._explicitWidths = self._expandWidths(descFont['W'])

    def _expandWidths(self, compactWidthArray):
        """Expands Adobe nested list structure to get a dictionary of widths.

        Here is an example of such a structure.::
        
            (
            # starting at character ID 1, next n  characters have the widths given.
            1,  (277,305,500,668,668,906,727,305,445,445,508,668,305,379,305,539),
            # all Characters from ID 17 to 26 are 668 em units wide
            17, 26, 668,
            27, (305, 305, 668, 668, 668, 566, 871, 727, 637, 652, 699, 574, 555,
                 676, 687, 242, 492, 664, 582, 789, 707, 734, 582, 734, 605, 605,
                 641, 668, 727, 945, 609, 609, 574, 445, 668, 445, 668, 668, 590,
                 555, 609, 547, 602, 574, 391, 609, 582, 234, 277, 539, 234, 895,
                 582, 605, 602, 602, 387, 508, 441, 582, 562, 781, 531, 570, 555,
                 449, 246, 449, 668),
            # these must be half width katakana and the like.
            231, 632, 500
            )
        
        """
        data = compactWidthArray[:]
        widths = {}
        while data:
            start, data = data[0], data[1:]
            if type(data[0]) in (ListType, TupleType):
                items, data = data[0], data[1:]
                for offset in range(len(items)):
                    widths[start + offset] = items[offset]

            else:
                end, width, data = data[0], data[1], data[2:]
                for idx in range(start, end + 1):
                    widths[idx] = width

        return widths

    def getCharWidth(self, characterId):
        return self._explicitWidths.get(characterId, self._defaultWidth)


class CIDFont(pdfmetrics.Font):
    """Represents a built-in multi-byte font"""
    _multiByte = 1

    def __init__(self, face, encoding):
        assert face in allowedTypeFaces, "TypeFace '%s' not supported! Use any of these instead: %s" % (face, allowedTypeFaces)
        self.faceName = face
        self.face = CIDTypeFace(face)
        assert encoding in allowedEncodings, "Encoding '%s' not supported!  Use any of these instead: %s" % (encoding, allowedEncodings)
        self.encodingName = encoding
        self.encoding = CIDEncoding(encoding)
        self.fontName = self.faceName + '-' + self.encodingName
        self.name = self.fontName
        self.isVertical = self.encodingName[-1] == 'V'
        self.substitutionFonts = []

    def formatForPdf(self, text):
        encoded = _escape(text)
        return encoded

    def stringWidth(self, text, size, encoding=None):
        """This presumes non-Unicode input.  UnicodeCIDFont wraps it for that context"""
        cidlist = self.encoding.translate(text)
        if self.isVertical:
            return len(cidlist) * size
        else:
            w = 0
            for cid in cidlist:
                w = w + self.face.getCharWidth(cid)

            return 0.001 * w * size

    def addObjects(self, doc):
        """The explicit code in addMinchoObjects and addGothicObjects
        will be replaced by something that pulls the data from
        _cidfontdata.py in the next few days."""
        internalName = 'F' + repr(len(doc.fontMapping) + 1)
        bigDict = CIDFontInfo[self.face.name]
        bigDict['Name'] = '/' + internalName
        bigDict['Encoding'] = '/' + self.encodingName
        cidObj = structToPDF(bigDict)
        r = doc.Reference(cidObj, internalName)
        fontDict = doc.idToObject['BasicFonts'].dict
        fontDict[internalName] = r
        doc.fontMapping[self.name] = '/' + internalName


class UnicodeCIDFont(CIDFont):
    r"""Wraps up CIDFont to hide explicit encoding choice;
    encodes text for output as UTF16.

    lang should be one of 'jpn',chs','cht','kor' for now.
    if vertical is set, it will select a different widths array
    and possibly glyphs for some punctuation marks.

    halfWidth is only for Japanese.

    >>> dodgy = UnicodeCIDFont('nonexistent')
    Traceback (most recent call last):
    ...
    KeyError: "don't know anything about CID font nonexistent"
    >>> heisei = UnicodeCIDFont('HeiseiMin-W3')
    >>> heisei.name
    'HeiseiMin-W3'
    >>> heisei.language
    'jpn'
    >>> heisei.encoding.name
    'UniJIS-UCS2-H'
    >>> #This is how PDF data gets encoded.
    >>> print heisei.formatForPdf('hello')
    \000h\000e\000l\000l\000o
    >>> tokyo = u'\u6771\u4AEC'
    >>> print heisei.formatForPdf(tokyo)
    gqJ\354

    """

    def __init__(self, face, isVertical=False, isHalfWidth=False):
        try:
            lang, defaultEncoding = defaultUnicodeEncodings[face]
        except KeyError:
            raise KeyError("don't know anything about CID font %s" % face)

        self.language = lang
        enc = defaultEncoding[:-1]
        if isHalfWidth:
            enc = enc + 'HW-'
        if isVertical:
            enc = enc + 'V'
        else:
            enc = enc + 'H'
        CIDFont.__init__(self, face, enc)
        self.name = self.fontName = face
        self.vertical = isVertical
        self.isHalfWidth = isHalfWidth
        self.unicodeWidths = widthsByUnichar[self.name]

    def formatForPdf(self, text):
        from codecs import utf_16_be_encode
        if type(text) is not unicode:
            text = text.decode('utf8')
        utfText = utf_16_be_encode(text)[0]
        encoded = _escape(utfText)
        return encoded

    def stringWidth(self, text, size, encoding=None):
        """Just ensure we do width test on characters, not bytes..."""
        if type(text) is type(''):
            text = text.decode('utf8')
        widths = self.unicodeWidths
        return size * 0.001 * sum([ widths.get(uch, 1000) for uch in text ])


def precalculate(cmapdir):
    import os
    files = os.listdir(cmapdir)
    for file in files:
        if os.path.isfile(cmapdir + os.sep + self.name + '.fastmap'):
            continue
        try:
            enc = CIDEncoding(file)
        except:
            print 'cannot parse %s, skipping' % enc
            continue

        enc.fastSave(cmapdir)
        print 'saved %s.fastmap' % file


def test():
    c = Canvas('test_japanese.pdf')
    c.setFont('Helvetica', 30)
    c.drawString(100, 700, 'Japanese Font Support')
    pdfmetrics.registerFont(CIDFont('HeiseiMin-W3', '90ms-RKSJ-H'))
    pdfmetrics.registerFont(CIDFont('HeiseiKakuGo-W5', '90ms-RKSJ-H'))
    c.setFont('HeiseiMin-W3-90ms-RKSJ-H', 16)
    message1 = b'\x82\xb1\x82\xea\x82\xcd\x95\xbd\x90\xac\x96\xbe\x92\xa9\x82\xc5\x82\xb7\x81B'
    c.drawString(100, 675, message1)
    c.save()
    print 'saved test_japanese.pdf'
    encName = '90ms-RKSJ-H'
    enc = CIDEncoding(encName)
    print message1, '->', enc.translate(message1)
    f = CIDFont('HeiseiMin-W3', '90ms-RKSJ-H')
    print 'width = %0.2f' % f.stringWidth(message1, 10)


if __name__ == '__main__':
    import doctest, cidfonts
    doctest.testmod(cidfonts)