# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\pdfbase\pdfmetrics.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = 'This provides a database of font metric information and\nefines Font, Encoding and TypeFace classes aimed at end users.\n\nThere are counterparts to some of these in pdfbase/pdfdoc.py, but\nthe latter focus on constructing the right PDF objects.  These\nclasses are declarative and focus on letting the user construct\nand query font objects.\n\nThe module maintains a registry of font objects at run time.\n\nIt is independent of the canvas or any particular context.  It keeps\na registry of Font, TypeFace and Encoding objects.  Ideally these\nwould be pre-loaded, but due to a nasty circularity problem we\ntrap attempts to access them and do it on first access.\n'
import string, os, sys
from types import StringType, ListType, TupleType
from reportlab.pdfbase import _fontdata
from reportlab.lib.logger import warnOnce
from reportlab.lib.utils import rl_isfile, rl_glob, rl_isdir, open_and_read, open_and_readlines, findInPaths
from reportlab.rl_config import defaultEncoding, T1SearchPath
import rl_codecs
_notdefChar = chr(110)
rl_codecs.RL_Codecs.register()
standardFonts = _fontdata.standardFonts
standardEncodings = _fontdata.standardEncodings
_typefaces = {}
_encodings = {}
_fonts = {}

def _py_unicode2T1(utext, fonts):
    """return a list of (font,string) pairs representing the unicode text"""
    R = []
    font, fonts = fonts[0], fonts[1:]
    enc = font.encName
    if 'UCS-2' in enc:
        enc = 'UTF16'
    while utext:
        try:
            R.append((font, utext.encode(enc)))
            break
        except UnicodeEncodeError as e:
            i0, il = e.args[2:4]
            if i0:
                R.append((font, utext[:i0].encode(enc)))
            if fonts:
                R.extend(_py_unicode2T1(utext[i0:il], fonts))
            else:
                R.append((_notdefFont, _notdefChar * (il - i0)))
            utext = utext[il:]

    return R


try:
    from _rl_accel import unicode2T1
except ImportError:
    unicode2T1 = _py_unicode2T1

class FontError(Exception):
    pass


class FontNotFoundError(Exception):
    pass


def parseAFMFile(afmFileName):
    """Quick and dirty - gives back a top-level dictionary
    with top-level items, and a 'widths' key containing
    a dictionary of glyph names and widths.  Just enough
    needed for embedding.  A better parser would accept
    options for what data you wwanted, and preserve the
    order."""
    lines = open_and_readlines(afmFileName, 'r')
    if len(lines) <= 1:
        if lines:
            lines = string.split(lines[0], '\r')
        if len(lines) <= 1:
            raise ValueError, "AFM file %s hasn't enough data" % afmFileName
    topLevel = {}
    glyphLevel = []
    lines = [ l for l in map(string.strip, lines) if not l.lower().startswith('comment') ]
    inMetrics = 0
    for line in lines:
        if line[0:16] == 'StartCharMetrics':
            inMetrics = 1
        elif line[0:14] == 'EndCharMetrics':
            inMetrics = 0
        elif inMetrics:
            chunks = string.split(line, ';')
            chunks = map(string.strip, chunks)
            cidChunk, widthChunk, nameChunk = chunks[0:3]
            l, r = string.split(cidChunk)
            assert l == 'C', 'bad line in font file %s' % line
            cid = string.atoi(r)
            l, r = string.split(widthChunk)
            assert l == 'WX', 'bad line in font file %s' % line
            width = string.atoi(r)
            l, r = string.split(nameChunk)
            assert l == 'N', 'bad line in font file %s' % line
            name = r
            glyphLevel.append((cid, width, name))

    inHeader = 0
    for line in lines:
        if line[0:16] == 'StartFontMetrics':
            inHeader = 1
        if line[0:16] == 'StartCharMetrics':
            inHeader = 0
        elif inHeader:
            if line[0:7] == 'Comment':
                pass
            try:
                left, right = string.split(line, ' ', 1)
            except:
                raise ValueError, "Header information error in afm %s: line='%s'" % (afmFileName, line)

            try:
                right = string.atoi(right)
            except:
                pass

            topLevel[left] = right

    return (topLevel, glyphLevel)


class TypeFace:

    def __init__(self, name):
        self.name = name
        self.glyphNames = []
        self.glyphWidths = {}
        self.ascent = 0
        self.descent = 0
        self.familyName = None
        self.bold = 0
        self.italic = 0
        if name == 'ZapfDingbats':
            self.requiredEncoding = 'ZapfDingbatsEncoding'
        elif name == 'Symbol':
            self.requiredEncoding = 'SymbolEncoding'
        else:
            self.requiredEncoding = None
        if name in standardFonts:
            self.builtIn = 1
            self._loadBuiltInData(name)
        else:
            self.builtIn = 0
        return

    def _loadBuiltInData(self, name):
        """Called for the built in 14 fonts.  Gets their glyph data.
        We presume they never change so this can be a shared reference."""
        name = str(name)
        self.glyphWidths = _fontdata.widthsByFontGlyph[name]
        self.glyphNames = self.glyphWidths.keys()
        self.ascent, self.descent = _fontdata.ascent_descent[name]

    def getFontFiles(self):
        """Info function, return list of the font files this depends on."""
        return []

    def findT1File(self, ext='.pfb'):
        possible_exts = (string.lower(ext), string.upper(ext))
        if hasattr(self, 'pfbFileName'):
            r_basename = os.path.splitext(self.pfbFileName)[0]
            for e in possible_exts:
                if rl_isfile(r_basename + e):
                    return r_basename + e

        try:
            r = _fontdata.findT1File(self.name)
        except:
            afm = bruteForceSearchForAFM(self.name)
            if afm:
                if string.lower(ext) == '.pfb':
                    for e in possible_exts:
                        pfb = os.path.splitext(afm)[0] + e
                        if rl_isfile(pfb):
                            r = pfb
                        else:
                            r = None

                elif string.lower(ext) == '.afm':
                    r = afm
            else:
                r = None

        if r is None:
            warnOnce("Can't find %s for face '%s'" % (ext, self.name))
        return r


def bruteForceSearchForFile(fn, searchPath=None):
    if searchPath is None:
        from reportlab.rl_config import T1SearchPath as searchPath
    if rl_isfile(fn):
        return fn
    else:
        bfn = os.path.basename(fn)
        for dirname in searchPath:
            if not rl_isdir(dirname):
                continue
            tfn = os.path.join(dirname, bfn)
            if rl_isfile(tfn):
                return tfn

        return fn


def bruteForceSearchForAFM(faceName):
    """Looks in all AFM files on path for face with given name.

    Returns AFM file name or None.  Ouch!"""
    from reportlab.rl_config import T1SearchPath
    for dirname in T1SearchPath:
        if not rl_isdir(dirname):
            continue
        possibles = rl_glob(dirname + os.sep + '*.[aA][fF][mM]')
        for possible in possibles:
            try:
                topDict, glyphDict = parseAFMFile(possible)
                if topDict['FontName'] == faceName:
                    return possible
            except:
                t, v, b = sys.exc_info()
                v.args = ((' ').join(map(str, v.args)) + ', while looking for faceName=%r' % faceName,)
                raise


class Encoding:
    """Object to help you create and refer to encodings."""

    def __init__(self, name, base=None):
        self.name = name
        self.frozen = 0
        if name in standardEncodings:
            assert base is None, "Can't have a base encoding for a standard encoding"
            self.baseEncodingName = name
            self.vector = _fontdata.encodings[name]
        elif base == None:
            self.baseEncodingName = defaultEncoding
            self.vector = _fontdata.encodings[defaultEncoding]
        elif type(base) is StringType:
            baseEnc = getEncoding(base)
            self.baseEncodingName = baseEnc.name
            self.vector = baseEnc.vector[:]
        elif type(base) in (ListType, TupleType):
            self.baseEncodingName = defaultEncoding
            self.vector = base[:]
        elif isinstance(base, Encoding):
            self.baseEncodingName = base.name
            self.vector = base.vector[:]
        return

    def __getitem__(self, index):
        """Return glyph name for that code point, or None"""
        return self.vector[index]

    def __setitem__(self, index, value):
        assert self.frozen == 0, 'Cannot modify a frozen encoding'
        if self.vector[index] != value:
            L = list(self.vector)
            L[index] = value
            self.vector = tuple(L)

    def freeze(self):
        self.vector = tuple(self.vector)
        self.frozen = 1

    def isEqual(self, other):
        return self.name == other.name and tuple(self.vector) == tuple(other.vector)

    def modifyRange(self, base, newNames):
        """Set a group of character names starting at the code point 'base'."""
        assert self.frozen == 0, 'Cannot modify a frozen encoding'
        idx = base
        for name in newNames:
            self.vector[idx] = name
            idx = idx + 1

    def getDifferences(self, otherEnc):
        """
        Return a compact list of the code points differing between two encodings

        This is in the Adobe format: list of
           [[b1, name1, name2, name3],
           [b2, name4]]
           
        where b1...bn is the starting code point, and the glyph names following
        are assigned consecutive code points.
        
        """
        ranges = []
        curRange = None
        for i in xrange(len(self.vector)):
            glyph = self.vector[i]
            if glyph == otherEnc.vector[i]:
                if curRange:
                    ranges.append(curRange)
                    curRange = []
            elif curRange:
                curRange.append(glyph)
            elif glyph:
                curRange = [
                 i, glyph]

        if curRange:
            ranges.append(curRange)
        return ranges

    def makePDFObject(self):
        """Returns a PDF Object representing self"""
        from reportlab.pdfbase import pdfdoc
        D = {}
        baseEnc = getEncoding(self.baseEncodingName)
        differences = self.getDifferences(baseEnc)
        if differences == []:
            return pdfdoc.PDFName(self.baseEncodingName)
        else:
            diffArray = []
            for range in differences:
                diffArray.append(range[0])
                for glyphName in range[1:]:
                    if glyphName is not None:
                        diffArray.append('/' + glyphName)

            D['Differences'] = pdfdoc.PDFArray(diffArray)
            D['BaseEncoding'] = pdfdoc.PDFName(self.baseEncodingName)
            D['Type'] = pdfdoc.PDFName('Encoding')
            PD = pdfdoc.PDFDictionary(D)
            return PD
            return


standardT1SubstitutionFonts = []

class Font:
    """Represents a font (i.e combination of face and encoding).

    Defines suitable machinery for single byte fonts.  This is
    a concrete class which can handle the basic built-in fonts;
    not clear yet if embedded ones need a new font class or
    just a new typeface class (which would do the job through
    composition)"""
    _multiByte = 0
    _dynamicFont = 0

    def __init__(self, name, faceName, encName):
        self.fontName = name
        face = self.face = getTypeFace(faceName)
        self.encoding = getEncoding(encName)
        self.encName = encName
        if face.builtIn and face.requiredEncoding is None:
            _ = standardT1SubstitutionFonts
        else:
            _ = []
        self.substitutionFonts = _
        self._calcWidths()
        self._notdefChar = _notdefChar
        self._notdefFont = name == 'ZapfDingbats' and self or _notdefFont
        return

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self.face.name)

    def _calcWidths(self):
        """Vector of widths for stringWidth function"""
        w = [
         0] * 256
        gw = self.face.glyphWidths
        vec = self.encoding.vector
        for i in range(256):
            glyphName = vec[i]
            if glyphName is not None:
                try:
                    width = gw[glyphName]
                    w[i] = width
                except KeyError:
                    import reportlab.rl_config
                    if reportlab.rl_config.warnOnMissingFontGlyphs:
                        print 'typeface "%s" does not have a glyph "%s", bad font!' % (self.face.name, glyphName)

        self.widths = w
        return

    def _py_stringWidth(self, text, size, encoding='utf8'):
        """This is the "purist" approach to width.  The practical approach
        is to use the stringWidth function, which may be swapped in for one
        written in C."""
        if not isinstance(text, unicode):
            text = text.decode(encoding)
        return sum([ sum(map(f.widths.__getitem__, map(ord, t))) for f, t in unicode2T1(text, [self] + self.substitutionFonts) ]) * 0.001 * size

    stringWidth = _py_stringWidth

    def _formatWidths(self):
        """returns a pretty block in PDF Array format to aid inspection"""
        text = '['
        for i in range(256):
            text = text + ' ' + str(self.widths[i])
            if i == 255:
                text = text + ' ]'
            if i % 16 == 15:
                text = text + '\n'

        return text

    def addObjects(self, doc):
        """Makes and returns one or more PDF objects to be added
        to the document.  The caller supplies the internal name
        to be used (typically F1, F2... in sequence) """
        from reportlab.pdfbase import pdfdoc
        internalName = 'F' + repr(len(doc.fontMapping) + 1)
        pdfFont = pdfdoc.PDFType1Font()
        pdfFont.Name = internalName
        pdfFont.BaseFont = self.face.name
        pdfFont.__Comment__ = 'Font %s' % self.fontName
        pdfFont.Encoding = self.encoding.makePDFObject()
        if self.face.name not in standardFonts:
            pdfFont.FirstChar = 0
            pdfFont.LastChar = 255
            pdfFont.Widths = pdfdoc.PDFArray(self.widths)
            pdfFont.FontDescriptor = self.face.addObjects(doc)
        ref = doc.Reference(pdfFont, internalName)
        fontDict = doc.idToObject['BasicFonts'].dict
        fontDict[internalName] = pdfFont
        doc.fontMapping[self.fontName] = '/' + internalName


PFB_MARKER = chr(128)
PFB_ASCII = chr(1)
PFB_BINARY = chr(2)
PFB_EOF = chr(3)

def _pfbSegLen(p, d):
    """compute a pfb style length from the first 4 bytes of string d"""
    return (ord(d[p + 3]) << 8 | ord(d[p + 2]) << 8 | ord(d[p + 1])) << 8 | ord(d[p])


def _pfbCheck(p, d, m, fn):
    if d[p] != PFB_MARKER or d[p + 1] != m:
        raise ValueError, "Bad pfb file'%s' expected chr(%d)chr(%d) at char %d, got chr(%d)chr(%d)" % (fn, ord(PFB_MARKER), ord(m), p, ord(d[p]), ord(d[p + 1]))
    if m == PFB_EOF:
        return
    p = p + 2
    l = _pfbSegLen(p, d)
    p = p + 4
    if p + l > len(d):
        raise ValueError, "Bad pfb file'%s' needed %d+%d bytes have only %d!" % (fn, p, l, len(d))
    return (
     p, p + l)


class EmbeddedType1Face(TypeFace):
    """A Type 1 font other than one of the basic 14.

    Its glyph data will be embedded in the PDF file."""

    def __init__(self, afmFileName, pfbFileName):
        TypeFace.__init__(self, None)
        afmFileName = findInPaths(afmFileName, T1SearchPath)
        pfbFileName = findInPaths(pfbFileName, T1SearchPath)
        self.afmFileName = os.path.abspath(afmFileName)
        self.pfbFileName = os.path.abspath(pfbFileName)
        self.requiredEncoding = None
        self._loadGlyphs(pfbFileName)
        self._loadMetrics(afmFileName)
        return

    def getFontFiles(self):
        return [self.afmFileName, self.pfbFileName]

    def _loadGlyphs(self, pfbFileName):
        """Loads in binary glyph data, and finds the four length
        measurements needed for the font descriptor"""
        pfbFileName = bruteForceSearchForFile(pfbFileName)
        assert rl_isfile(pfbFileName), 'file %s not found' % pfbFileName
        d = open_and_read(pfbFileName, 'b')
        s1, l1 = _pfbCheck(0, d, PFB_ASCII, pfbFileName)
        s2, l2 = _pfbCheck(l1, d, PFB_BINARY, pfbFileName)
        s3, l3 = _pfbCheck(l2, d, PFB_ASCII, pfbFileName)
        _pfbCheck(l3, d, PFB_EOF, pfbFileName)
        self._binaryData = d[s1:l1] + d[s2:l2] + d[s3:l3]
        self._length = len(self._binaryData)
        self._length1 = l1 - s1
        self._length2 = l2 - s2
        self._length3 = l3 - s3

    def _loadMetrics(self, afmFileName):
        """Loads in and parses font metrics"""
        afmFileName = bruteForceSearchForFile(afmFileName)
        topLevel, glyphData = parseAFMFile(afmFileName)
        self.name = topLevel['FontName']
        self.familyName = topLevel['FamilyName']
        self.ascent = topLevel.get('Ascender', 1000)
        self.descent = topLevel.get('Descender', 0)
        self.capHeight = topLevel.get('CapHeight', 1000)
        self.italicAngle = topLevel.get('ItalicAngle', 0)
        self.stemV = topLevel.get('stemV', 0)
        self.xHeight = topLevel.get('XHeight', 1000)
        strBbox = topLevel.get('FontBBox', [0, 0, 1000, 1000])
        tokens = string.split(strBbox)
        self.bbox = []
        for tok in tokens:
            self.bbox.append(string.atoi(tok))

        glyphWidths = {}
        for cid, width, name in glyphData:
            glyphWidths[name] = width

        self.glyphWidths = glyphWidths
        self.glyphNames = glyphWidths.keys()
        self.glyphNames.sort()
        if topLevel.get('EncodingScheme', None) == 'FontSpecific':
            names = [
             None] * 256
            for code, width, name in glyphData:
                if code >= 0 and code <= 255:
                    names[code] = name

            encName = self.name + 'Encoding'
            self.requiredEncoding = encName
            enc = Encoding(encName, names)
            registerEncoding(enc)
        return

    def addObjects(self, doc):
        """Add whatever needed to PDF file, and return a FontDescriptor reference"""
        from reportlab.pdfbase import pdfdoc
        fontFile = pdfdoc.PDFStream()
        fontFile.content = self._binaryData
        fontFile.dictionary['Length1'] = self._length1
        fontFile.dictionary['Length2'] = self._length2
        fontFile.dictionary['Length3'] = self._length3
        fontFileRef = doc.Reference(fontFile, 'fontFile:' + self.pfbFileName)
        fontDescriptor = pdfdoc.PDFDictionary({'Type': '/FontDescriptor', 
           'Ascent': self.ascent, 
           'CapHeight': self.capHeight, 
           'Descent': self.descent, 
           'Flags': 34, 
           'FontBBox': pdfdoc.PDFArray(self.bbox), 
           'FontName': pdfdoc.PDFName(self.name), 
           'ItalicAngle': self.italicAngle, 
           'StemV': self.stemV, 
           'XHeight': self.xHeight, 
           'FontFile': fontFileRef})
        fontDescriptorRef = doc.Reference(fontDescriptor, 'fontDescriptor:' + self.name)
        return fontDescriptorRef


def registerTypeFace(face):
    assert isinstance(face, TypeFace), 'Not a TypeFace: %s' % face
    _typefaces[face.name] = face
    if face.name not in standardFonts:
        registerFontFamily(face.name)


def registerEncoding(enc):
    assert isinstance(enc, Encoding), 'Not an Encoding: %s' % enc
    if enc.name in _encodings:
        if enc.isEqual(_encodings[enc.name]):
            enc.freeze()
        else:
            raise FontError('Encoding "%s" already registered with a different name vector!' % enc.name)
    else:
        _encodings[enc.name] = enc
        enc.freeze()


def registerFontFamily(family, normal=None, bold=None, italic=None, boldItalic=None):
    from reportlab.lib import fonts
    if not normal:
        normal = family
    family = family.lower()
    if not boldItalic:
        boldItalic = italic or bold or normal
    if not bold:
        bold = normal
    if not italic:
        italic = normal
    fonts.addMapping(family, 0, 0, normal)
    fonts.addMapping(family, 1, 0, bold)
    fonts.addMapping(family, 0, 1, italic)
    fonts.addMapping(family, 1, 1, boldItalic)


def registerFont(font):
    """Registers a font, including setting up info for accelerated stringWidth"""
    fontName = font.fontName
    _fonts[fontName] = font
    if font._multiByte:
        registerFontFamily(font.fontName)


def getTypeFace(faceName):
    """Lazily construct known typefaces if not found"""
    try:
        return _typefaces[faceName]
    except KeyError:
        if faceName in standardFonts:
            face = TypeFace(faceName)
            face.familyName, face.bold, face.italic = _fontdata.standardFontAttributes[faceName]
            registerTypeFace(face)
            return face
        afm = bruteForceSearchForAFM(faceName)
        if afm:
            for e in ('.pfb', '.PFB'):
                pfb = os.path.splitext(afm)[0] + e
                if rl_isfile(pfb):
                    break

            assert rl_isfile(pfb), 'file %s not found!' % pfb
            face = EmbeddedType1Face(afm, pfb)
            registerTypeFace(face)
            return face
        raise


def getEncoding(encName):
    """Lazily construct known encodings if not found"""
    try:
        return _encodings[encName]
    except KeyError:
        if encName in standardEncodings:
            enc = Encoding(encName)
            registerEncoding(enc)
            return enc
        raise


def findFontAndRegister(fontName):
    """search for and register a font given its name"""
    face = getTypeFace(fontName)
    if face.requiredEncoding:
        font = Font(fontName, fontName, face.requiredEncoding)
    else:
        font = Font(fontName, fontName, defaultEncoding)
    registerFont(font)
    return font


def getFont(fontName):
    """Lazily constructs known fonts if not found.

    Names of form 'face-encoding' will be built if
    face and encoding are known.  Also if the name is
    just one of the standard 14, it will make up a font
    in the default encoding."""
    try:
        return _fonts[fontName]
    except KeyError:
        return findFontAndRegister(fontName)


_notdefFont = getFont('ZapfDingbats')
standardT1SubstitutionFonts.extend([getFont('Symbol'), _notdefFont])

def getAscentDescent(fontName, fontSize=None):
    font = getFont(fontName)
    try:
        ascent = font.ascent
        descent = font.descent
    except:
        ascent = font.face.ascent
        descent = font.face.descent

    if fontSize:
        norm = fontSize / 1000.0
        return (
         ascent * norm, descent * norm)
    else:
        return (
         ascent, descent)


def getAscent(fontName, fontSize=None):
    return getAscentDescent(fontName, fontSize)[0]


def getDescent(fontName, fontSize=None):
    return getAscentDescent(fontName, fontSize)[1]


def getRegisteredFontNames():
    """Returns what's in there"""
    reg = _fonts.keys()
    reg.sort()
    return reg


def stringWidth(text, fontName, fontSize, encoding='utf8'):
    """Compute width of string in points;
    not accelerated as fast enough because of _instanceStringWidthU"""
    return getFont(fontName).stringWidth(text, fontSize, encoding=encoding)


try:
    from _rl_accel import _instanceStringWidthU
    import new
    Font.stringWidth = new.instancemethod(_instanceStringWidthU, None, Font)
except ImportError:
    pass

def dumpFontData():
    print 'Registered Encodings:'
    keys = _encodings.keys()
    keys.sort()
    for encName in keys:
        print '   ', encName

    print
    print 'Registered Typefaces:'
    faces = _typefaces.keys()
    faces.sort()
    for faceName in faces:
        print '   ', faceName

    print
    print 'Registered Fonts:'
    k = _fonts.keys()
    k.sort()
    for key in k:
        font = _fonts[key]
        print '    %s (%s/%s)' % (font.fontName, font.face.name, font.encoding.name)


def test3widths(texts):
    import time
    for fontName in standardFonts[0:1]:
        t0 = time.time()
        w = getFont(fontName).widths
        for text in texts:
            l2 = 0
            for ch in text:
                l2 = l2 + w[ord(ch)]

        t1 = time.time()
        print 'slow stringWidth took %0.4f' % (t1 - t0)
        t0 = time.time()
        for text in texts:
            l3 = getFont(fontName).stringWidth(text, 10)

        t1 = time.time()
        print 'class lookup and stringWidth took %0.4f' % (t1 - t0)
        print


def testStringWidthAlgorithms():
    rawdata = open('../../rlextra/rml2pdf/doc/rml_user_guide.prep').read()
    print 'rawdata length %d' % len(rawdata)
    print 'test one huge string...'
    test3widths([rawdata])
    print
    words = string.split(rawdata)
    print 'test %d shorter strings (average length %0.2f chars)...' % (len(words), 1.0 * len(rawdata) / len(words))
    test3widths(words)


def test():
    helv = TypeFace('Helvetica')
    registerTypeFace(helv)
    print helv.glyphNames[0:30]
    wombat = TypeFace('Wombat')
    print wombat.glyphNames
    registerTypeFace(wombat)
    dumpFontData()


def _reset(initial_dicts=dict(_typefaces=_typefaces.copy(), _encodings=_encodings.copy(), _fonts=_fonts.copy())):
    for k, v in initial_dicts.iteritems():
        d = globals()[k]
        d.clear()
        d.update(v)


from reportlab.rl_config import register_reset
register_reset(_reset)
del register_reset
if __name__ == '__main__':
    test()
    testStringWidthAlgorithms()