# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\pdfbase\_fontdata.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = "Database of font related things\n\n    - standardFonts - tuple of the 14 standard string font names\n    - standardEncodings - tuple of the known standard font names\n    - encodings - a mapping object from standard encoding names (and minor variants)\n      to the encoding vectors ie the tuple of string glyph names\n    - widthsByFontGlyph - fontname x glyphname --> width of glyph\n    - widthVectorsByFont - fontName -> vector of widths \n    \n    This module defines a static, large data structure.  At the request\n    of the Jython project, we have split this off into separate modules\n    as Jython cannot handle more than 64k of bytecode in the 'top level'\n    code of a Python module.  \n"
import UserDict, os, sys
widthVectorsByFont = {}
fontsByName = {}
fontsByBaseEnc = {}
standardFonts = ('Courier', 'Courier-Bold', 'Courier-Oblique', 'Courier-BoldOblique',
                 'Helvetica', 'Helvetica-Bold', 'Helvetica-Oblique', 'Helvetica-BoldOblique',
                 'Times-Roman', 'Times-Bold', 'Times-Italic', 'Times-BoldItalic',
                 'Symbol', 'ZapfDingbats')
standardFontAttributes = {'Courier': ('Courier', 0, 0), 
   'Courier-Bold': ('Courier', 1, 0), 
   'Courier-Oblique': ('Courier', 0, 1), 
   'Courier-BoldOblique': ('Courier', 1, 1), 
   'Helvetica': ('Helvetica', 0, 0), 
   'Helvetica-Bold': ('Helvetica', 1, 0), 
   'Helvetica-Oblique': ('Helvetica', 0, 1), 
   'Helvetica-BoldOblique': ('Helvetica', 1, 1), 
   'Times-Roman': ('Times-Roman', 0, 0), 
   'Times-Bold': ('Times-Roman', 1, 0), 
   'Times-Italic': ('Times-Roman', 0, 1), 
   'Times-BoldItalic': ('Times-Roman', 1, 1), 
   'Symbol': ('Symbol', 0, 0), 
   'ZapfDingbats': ('ZapfDingbats', 0, 0)}
_font2fnrMapWin32 = {'symbol': 'sy______', 
   'zapfdingbats': 'zd______', 
   'helvetica': '_a______', 
   'helvetica-bold': '_ab_____', 
   'helvetica-boldoblique': '_abi____', 
   'helvetica-oblique': '_ai_____', 
   'times-bold': '_eb_____', 
   'times-bolditalic': '_ebi____', 
   'times-italic': '_ei_____', 
   'times-roman': '_er_____', 
   'courier-bold': 'cob_____', 
   'courier-boldoblique': 'cobo____', 
   'courier': 'com_____', 
   'courier-oblique': 'coo_____'}
if sys.platform in ('linux2', ):
    _font2fnrMapLinux2 = {'symbol': 'Symbol', 'zapfdingbats': 'ZapfDingbats', 
       'helvetica': 'Arial', 
       'helvetica-bold': 'Arial-Bold', 
       'helvetica-boldoblique': 'Arial-BoldItalic', 
       'helvetica-oblique': 'Arial-Italic', 
       'times-bold': 'TimesNewRoman-Bold', 
       'times-bolditalic': 'TimesNewRoman-BoldItalic', 
       'times-italic': 'TimesNewRoman-Italic', 
       'times-roman': 'TimesNewRoman', 
       'courier-bold': 'Courier-Bold', 
       'courier-boldoblique': 'Courier-BoldOblique', 
       'courier': 'Courier', 
       'courier-oblique': 'Courier-Oblique'}
    _font2fnrMap = _font2fnrMapLinux2
    for k, v in _font2fnrMap.items():
        if k in _font2fnrMapWin32.keys():
            _font2fnrMapWin32[v.lower()] = _font2fnrMapWin32[k]

    del k
    del v
else:
    _font2fnrMap = _font2fnrMapWin32

def _findFNR(fontName):
    return _font2fnrMap[fontName.lower()]


from reportlab.rl_config import T1SearchPath
from reportlab.lib.utils import rl_isfile

def _searchT1Dirs(n, rl_isfile=rl_isfile, T1SearchPath=T1SearchPath):
    assert T1SearchPath != [], 'No Type-1 font search path'
    for d in T1SearchPath:
        f = os.path.join(d, n)
        if rl_isfile(f):
            return f

    return


del T1SearchPath
del rl_isfile

def findT1File(fontName, ext='.pfb'):
    if sys.platform in ('linux2', ) and ext == '.pfb':
        try:
            f = _searchT1Dirs(_findFNR(fontName))
            if f:
                return f
        except:
            pass

        try:
            f = _searchT1Dirs(_font2fnrMapWin32[fontName.lower()] + ext)
            if f:
                return f
        except:
            pass

    return _searchT1Dirs(_findFNR(fontName) + ext)


standardEncodings = ('WinAnsiEncoding', 'MacRomanEncoding', 'StandardEncoding', 'SymbolEncoding',
                     'ZapfDingbatsEncoding', 'PDFDocEncoding', 'MacExpertEncoding')

class _Name2StandardEncodingMap(UserDict.UserDict):
    """Trivial fake dictionary with some [] magic"""
    _XMap = {'winansi': 'WinAnsiEncoding', 'macroman': 'MacRomanEncoding', 'standard': 'StandardEncoding', 'symbol': 'SymbolEncoding', 'zapfdingbats': 'ZapfDingbatsEncoding', 'pdfdoc': 'PDFDocEncoding', 'macexpert': 'MacExpertEncoding'}

    def __setitem__(self, x, v):
        y = x.lower()
        if y[-8:] == 'encoding':
            y = y[:-8]
        y = self._XMap[y]
        if y in self.keys():
            raise IndexError, 'Encoding %s is already set' % y
        self.data[y] = v

    def __getitem__(self, x):
        y = x.lower()
        if y[-8:] == 'encoding':
            y = y[:-8]
        y = self._XMap[y]
        return self.data[y]


encodings = _Name2StandardEncodingMap()
for keyname in standardEncodings:
    modname = '_fontdata_enc_%s' % keyname.lower()[:-8]
    module = __import__(modname, globals(), locals())
    encodings[keyname] = getattr(module, keyname)

ascent_descent = {'Courier': (629, -157), 
   'Courier-Bold': (626, -142), 
   'Courier-BoldOblique': (626, -142), 
   'Courier-Oblique': (629, -157), 
   'Helvetica': (718, -207), 
   'Helvetica-Bold': (718, -207), 
   'Helvetica-BoldOblique': (718, -207), 
   'Helvetica-Oblique': (718, -207), 
   'Times-Roman': (683, -217), 
   'Times-Bold': (676, -205), 
   'Times-BoldItalic': (699, -205), 
   'Times-Italic': (683, -205), 
   'Symbol': (0, 0), 
   'ZapfDingbats': (0, 0)}
widthsByFontGlyph = {}
for fontName in standardFonts:
    modname = '_fontdata_widths_%s' % fontName.lower().replace('-', '')
    module = __import__(modname, globals(), locals())
    widthsByFontGlyph[fontName] = module.widths

def _reset(initial_dicts=dict(ascent_descent=ascent_descent.copy(), fontsByBaseEnc=fontsByBaseEnc.copy(), fontsByName=fontsByName.copy(), standardFontAttributes=standardFontAttributes.copy(), widthVectorsByFont=widthVectorsByFont.copy(), widthsByFontGlyph=widthsByFontGlyph.copy())):
    for k, v in initial_dicts.iteritems():
        d = globals()[k]
        d.clear()
        d.update(v)


from reportlab.rl_config import register_reset
register_reset(_reset)
del register_reset