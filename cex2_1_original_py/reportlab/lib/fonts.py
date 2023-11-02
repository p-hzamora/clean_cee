# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\lib\fonts.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = "Utilities to associate bold and italic versions of fonts into families\n\nBold, italic and plain fonts are usually implemented in separate disk files;\nbut non-trivial apps want <b>this</b> to do the right thing.   We therefore\nneed to keep 'mappings' between the font family name and the right group\nof up to 4 implementation fonts to use.\n\nMost font-handling code lives in pdfbase, and this probably should too.\n\n"
import sys, os
_family_alias = {'serif': 'times', 
   'sansserif': 'helvetica', 
   'monospaced': 'courier', 
   'arial': 'helvetica'}
_tt2ps_map = {('times', 0, 0): 'Times-Roman', 
   ('times', 1, 0): 'Times-Bold', 
   ('times', 0, 1): 'Times-Italic', 
   ('times', 1, 1): 'Times-BoldItalic', 
   ('courier', 0, 0): 'Courier', 
   ('courier', 1, 0): 'Courier-Bold', 
   ('courier', 0, 1): 'Courier-Oblique', 
   ('courier', 1, 1): 'Courier-BoldOblique', 
   ('helvetica', 0, 0): 'Helvetica', 
   ('helvetica', 1, 0): 'Helvetica-Bold', 
   ('helvetica', 0, 1): 'Helvetica-Oblique', 
   ('helvetica', 1, 1): 'Helvetica-BoldOblique', 
   ('symbol', 0, 0): 'Symbol', 
   ('symbol', 1, 0): 'Symbol', 
   ('symbol', 0, 1): 'Symbol', 
   ('symbol', 1, 1): 'Symbol', 
   ('zapfdingbats', 0, 0): 'ZapfDingbats', 
   ('zapfdingbats', 1, 0): 'ZapfDingbats', 
   ('zapfdingbats', 0, 1): 'ZapfDingbats', 
   ('zapfdingbats', 1, 1): 'ZapfDingbats'}
_ps2tt_map = {}
for k, v in _tt2ps_map.items():
    if k not in _ps2tt_map:
        _ps2tt_map[v.lower()] = k

def ps2tt(psfn):
    """ps fontname to family name, bold, italic"""
    psfn = psfn.lower()
    if psfn in _ps2tt_map:
        return _ps2tt_map[psfn]
    raise ValueError("Can't map determine family/bold/italic for %s" % psfn)


def tt2ps(fn, b, i):
    """family name + bold & italic to ps font name"""
    K = (
     fn.lower(), b, i)
    if K in _tt2ps_map:
        return _tt2ps_map[K]
    fn, b1, i1 = ps2tt(K[0])
    K = (fn, b1 | b, i1 | i)
    if K in _tt2ps_map:
        return _tt2ps_map[K]
    raise ValueError("Can't find concrete font for family=%s, bold=%d, italic=%d" % (fn, b, i))


def addMapping(face, bold, italic, psname):
    """allow a custom font to be put in the mapping"""
    k = (
     face.lower(), bold, italic)
    _tt2ps_map[k] = psname
    _ps2tt_map[psname.lower()] = k