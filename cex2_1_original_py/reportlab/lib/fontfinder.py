# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\lib\fontfinder.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = "This provides some general-purpose tools for finding fonts.\n\nThe FontFinder object can search for font files.  It aims to build\na catalogue of fonts which our framework can work with.  It may be useful\nif you are building GUIs or design-time interfaces and want to present users\nwith a choice of fonts.\n\nThere are 3 steps to using it\n1. create FontFinder and set options and directories\n2. search\n3. query\n\n>>> import fontfinder\n>>> ff = fontfinder.FontFinder()\n>>> ff.addDirectories([dir1, dir2, dir3])\n>>> ff.search()\n>>> ff.getFamilyNames()   #or whichever queries you want...\n\nBecause the disk search takes some time to find and parse hundreds of fonts,\nit can use a cache to store a file with all fonts found. The cache file name\n\nFor each font found, it creates a structure with\n- the short font name\n- the long font name\n- the principal file (.pfb for type 1 fonts), and the metrics file if appropriate\n- the time modified (unix time stamp)\n- a type code ('ttf')\n- the family name\n- bold and italic attributes\n\nOne common use is to display families in a dialog for end users;\nthen select regular, bold and italic variants of the font.  To get\nthe initial list, use getFamilyNames; these will be in alpha order.\n\n>>> ff.getFamilyNames()\n['Bitstream Vera Sans', 'Century Schoolbook L', 'Dingbats', 'LettErrorRobot',\n'MS Gothic', 'MS Mincho', 'Nimbus Mono L', 'Nimbus Roman No9 L',\n'Nimbus Sans L', 'Vera', 'Standard Symbols L',\n'URW Bookman L', 'URW Chancery L', 'URW Gothic L', 'URW Palladio L']\n\nOne can then obtain a specific font as follows\n\n>>> f = ff.getFont('Bitstream Vera Sans', bold=False, italic=True)\n>>> f.fullName\n'Bitstream Vera Sans'\n>>> f.fileName\n'C:\\code\\reportlab\\fonts\\Vera.ttf'\n>>>\n\nIt can also produce an XML report of fonts found by family, for the benefit\nof non-Python applications.\n\nFuture plans might include using this to auto-register fonts; and making it\nupdate itself smartly on repeated instantiation.\n"
import sys, time, os, cPickle, tempfile
from xml.sax.saxutils import quoteattr
try:
    from hashlib import md5
except ImportError:
    from md5 import md5

EXTENSIONS = [
 '.ttf', '.ttc', '.otf', '.pfb', '.pfa']
FF_FIXED = 1 << 0
FF_SERIF = 1 << 1
FF_SYMBOLIC = 1 << 2
FF_SCRIPT = 1 << 3
FF_NONSYMBOLIC = 1 << 5
FF_ITALIC = 1 << 6
FF_ALLCAP = 1 << 16
FF_SMALLCAP = 1 << 17
FF_FORCEBOLD = 1 << 18

class FontDescriptor:
    """This is a short descriptive record about a font.

    typeCode should be a file extension e.g. ['ttf','ttc','otf','pfb','pfa']
    """

    def __init__(self):
        self.name = None
        self.fullName = None
        self.familyName = None
        self.styleName = None
        self.isBold = False
        self.isItalic = False
        self.isFixedPitch = False
        self.isSymbolic = False
        self.typeCode = None
        self.fileName = None
        self.metricsFileName = None
        self.timeModified = 0
        return

    def __repr__(self):
        return 'FontDescriptor(%s)' % self.name

    def getTag(self):
        """Return an XML tag representation"""
        attrs = []
        for k, v in self.__dict__.items():
            if k not in ('timeModified', ):
                if v:
                    attrs.append('%s=%s' % (k, quoteattr(str(v))))

        return '<font ' + (' ').join(attrs) + '/>'


from reportlab.lib.utils import rl_isdir, rl_isfile, rl_listdir, rl_getmtime

class FontFinder:

    def __init__(self, dirs=[], useCache=True, validate=False):
        self.useCache = useCache
        self.validate = validate
        self._dirs = set(dirs)
        self._fonts = []
        self._skippedFiles = []
        self._badFiles = []
        self._fontsByName = {}
        self._fontsByFamily = {}
        self._fontsByFamilyBoldItalic = {}

    def addDirectory(self, dirName):
        if rl_isdir(dirName):
            self._dirs.add(dirName)

    def addDirectories(self, dirNames):
        for dirName in dirNames:
            self.addDirectory(dirName)

    def getFamilyNames(self):
        """Returns a list of the distinct font families found"""
        if not self._fontsByFamily:
            fonts = self._fonts
            for font in fonts:
                fam = font.familyName
                if fam in self._fontsByFamily:
                    self._fontsByFamily[fam].append(font)
                else:
                    self._fontsByFamily[fam] = [
                     font]

        names = self._fontsByFamily.keys()
        names.sort()
        return names

    def getFontsInFamily(self, familyName):
        """Return list of all font objects with this family name"""
        return self._fontsByFamily.get(familyName, [])

    def getFamilyXmlReport(self):
        """Reports on all families found as XML.
        """
        lines = []
        lines.append('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>')
        lines.append('<font_families>')
        for dirName in self._dirs:
            lines.append('    <directory name=%s/>' % quoteattr(dirName))

        for familyName in self.getFamilyNames():
            if familyName:
                lines.append('    <family name=%s>' % quoteattr(familyName))
                for font in self.getFontsInFamily(familyName):
                    lines.append('        ' + font.getTag())

                lines.append('    </family>')

        lines.append('</font_families>')
        return ('\n').join(lines)

    def getFontsWithAttributes(self, **kwds):
        """This is a general lightweight search."""
        selected = []
        for font in self._fonts:
            OK = True
            for k, v in kwds.items():
                if getattr(font, k, None) != v:
                    OK = False

            if OK:
                selected.append(font)

        return selected

    def getFont(self, familyName, bold=False, italic=False):
        """Try to find a font matching the spec"""
        for font in self._fonts:
            if font.familyName == familyName:
                if font.isBold == bold:
                    if font.isItalic == italic:
                        return font

        raise KeyError('Cannot find font %s with bold=%s, italic=%s' % (familyName, bold, italic))

    def _getCacheFileName(self):
        """Base this on the directories...same set of directories
        should give same cache"""
        hash = md5(('').join(self._dirs)).hexdigest()
        from reportlab.lib.utils import get_rl_tempfile
        fn = get_rl_tempfile('fonts_%s.dat' % hash)
        return fn

    def save(self, fileName):
        f = open(fileName, 'w')
        cPickle.dump(self, f)
        f.close()

    def load(self, fileName):
        f = open(fileName, 'r')
        finder2 = cPickle.load(f)
        f.close()
        self.__dict__.update(finder2.__dict__)

    def search(self):
        started = time.clock()
        if not self._dirs:
            raise ValueError('Font search path is empty!  Please specify search directories using addDirectory or addDirectories')
        if self.useCache:
            cfn = self._getCacheFileName()
            if rl_isfile(cfn):
                try:
                    self.load(cfn)
                    return
                except:
                    pass

        from stat import ST_MTIME
        for dirName in self._dirs:
            fileNames = rl_listdir(dirName)
            for fileName in fileNames:
                root, ext = os.path.splitext(fileName)
                if ext.lower() in EXTENSIONS:
                    f = FontDescriptor()
                    f.fileName = os.path.normpath(os.path.join(dirName, fileName))
                    f.timeModified = rl_getmtime(f.fileName)
                    ext = ext.lower()
                    if ext[0] == '.':
                        ext = ext[1:]
                    f.typeCode = ext
                    if ext in ('otf', 'pfa'):
                        self._skippedFiles.append(fileName)
                    elif ext in ('ttf', 'ttc'):
                        from reportlab.pdfbase.ttfonts import TTFontFile, TTFError
                        try:
                            font = TTFontFile(fileName, validate=self.validate)
                        except TTFError:
                            self._badFiles.append(fileName)
                            continue

                        f.name = font.name
                        f.fullName = font.fullName
                        f.styleName = font.styleName
                        f.familyName = font.familyName
                        f.isBold = FF_FORCEBOLD == FF_FORCEBOLD & font.flags
                        f.isItalic = FF_ITALIC == FF_ITALIC & font.flags
                    elif ext == 'pfb':
                        if rl_isfile(os.path.join(dirName, root + '.afm')):
                            f.metricsFileName = os.path.normpath(os.path.join(dirName, root + '.afm'))
                        elif rl_isfile(os.path.join(dirName, root + '.AFM')):
                            f.metricsFileName = os.path.normpath(os.path.join(dirName, root + '.AFM'))
                        else:
                            self._skippedFiles.append(fileName)
                            continue
                        from reportlab.pdfbase.pdfmetrics import parseAFMFile
                        info, glyphs = parseAFMFile(f.metricsFileName)
                        f.name = info['FontName']
                        f.fullName = info.get('FullName', f.name)
                        f.familyName = info.get('FamilyName', None)
                        f.isItalic = float(info.get('ItalicAngle', 0)) > 0.0
                        f.isBold = 'bold' in info.get('Weight', '').lower()
                    self._fonts.append(f)

        if self.useCache:
            self.save(cfn)
        finished = time.clock()
        return


def test():
    from reportlab import rl_config
    ff = FontFinder()
    ff.useCache = True
    ff.validate = True
    import reportlab
    ff.addDirectory('C:\\windows\\fonts')
    rlFontDir = os.path.join(os.path.dirname(reportlab.__file__), 'fonts')
    ff.addDirectory(rlFontDir)
    ff.search()
    print 'cache file name...'
    print ff._getCacheFileName()
    print 'families...'
    for familyName in ff.getFamilyNames():
        print '\t%s' % familyName

    print
    print 'fonts called Vera:',
    for font in ff.getFontsInFamily('Bitstream Vera Sans'):
        print '\t%s' % font.name

    print
    print 'Bold fonts\n\t'
    for font in ff.getFontsWithAttributes(isBold=True, isItalic=False):
        print font.fullName,

    print 'family report'
    print ff.getFamilyXmlReport()


if __name__ == '__main__':
    test()