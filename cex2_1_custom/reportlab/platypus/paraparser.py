# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\platypus\paraparser.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = 'The parser used to process markup within paragraphs'
import string, re
from types import TupleType, UnicodeType, StringType
import sys, os, copy, base64
try:
    import cPickle as pickle
except:
    import pickle

import unicodedata, reportlab.lib.sequencer
from reportlab.lib.abag import ABag
from reportlab.lib.utils import ImageReader
from reportlab.lib import xmllib
from reportlab.lib.colors import toColor, white, black, red, Color
from reportlab.lib.fonts import tt2ps, ps2tt
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.units import inch, mm, cm, pica
_re_para = re.compile('^\\s*<\\s*para(?:\\s+|>|/>)')
sizeDelta = 2
subFraction = 0.5
superFraction = 0.5
DEFAULT_INDEX_NAME = '_indexAdd'

def _convnum(s, unit=1, allowRelative=True):
    if s[0] in ('+', '-') and allowRelative:
        try:
            return (
             'relative', int(s) * unit)
        except ValueError:
            return (
             'relative', float(s) * unit)

    else:
        try:
            return int(s) * unit
        except ValueError:
            return float(s) * unit


def _num(s, unit=1, allowRelative=True):
    """Convert a string like '10cm' to an int or float (in points).
       The default unit is point, but optionally you can use other
       default units like mm.
    """
    if s.endswith('cm'):
        unit = cm
        s = s[:-2]
    if s.endswith('in'):
        unit = inch
        s = s[:-2]
    if s.endswith('pt'):
        unit = 1
        s = s[:-2]
    if s.endswith('i'):
        unit = inch
        s = s[:-1]
    if s.endswith('mm'):
        unit = mm
        s = s[:-2]
    if s.endswith('pica'):
        unit = pica
        s = s[:-4]
    return _convnum(s, unit, allowRelative)


def _numpct(s, unit=1, allowRelative=False):
    if s.endswith('%'):
        return _PCT(_convnum(s[:-1], allowRelative=allowRelative))
    else:
        return _num(s, unit, allowRelative)


class _PCT():

    def __init__(self, v):
        self._value = v * 0.01

    def normalizedValue(self, normalizer):
        normalizer = normalizer or getattr(self, '_normalizer')
        return normalizer * self._value


def _valignpc(s):
    s = s.lower()
    if s in ('baseline', 'sub', 'super', 'top', 'text-top', 'middle', 'bottom', 'text-bottom'):
        return s
    if s.endswith('%'):
        n = _convnum(s[:-1])
        if isinstance(n, tuple):
            n = n[1]
        return _PCT(n)
    n = _num(s)
    if isinstance(n, tuple):
        n = n[1]
    return n


def _autoLeading(x):
    x = x.lower()
    if x in ('', 'min', 'max', 'off'):
        return x
    raise ValueError('Invalid autoLeading=%r' % x)


def _align(s):
    s = string.lower(s)
    if s == 'left':
        return TA_LEFT
    if s == 'right':
        return TA_RIGHT
    if s == 'justify':
        return TA_JUSTIFY
    if s in ('centre', 'center'):
        return TA_CENTER
    raise ValueError


_paraAttrMap = {'font': ('fontName', None), 'face': (
          'fontName', None), 
   'fontsize': (
              'fontSize', _num), 
   'size': (
          'fontSize', _num), 
   'leading': (
             'leading', _num), 
   'autoleading': (
                 'autoLeading', _autoLeading), 
   'lindent': (
             'leftIndent', _num), 
   'rindent': (
             'rightIndent', _num), 
   'findent': (
             'firstLineIndent', _num), 
   'align': (
           'alignment', _align), 
   'spaceb': (
            'spaceBefore', _num), 
   'spacea': (
            'spaceAfter', _num), 
   'bfont': (
           'bulletFontName', None), 
   'bfontsize': (
               'bulletFontSize', _num), 
   'boffsety': (
              'bulletOffsetY', _num), 
   'bindent': (
             'bulletIndent', _num), 
   'bcolor': (
            'bulletColor', toColor), 
   'color': (
           'textColor', toColor), 
   'backcolor': (
               'backColor', toColor), 
   'bgcolor': (
             'backColor', toColor), 
   'bg': (
        'backColor', toColor), 
   'fg': (
        'textColor', toColor)}
_bulletAttrMap = {'font': (
          'bulletFontName', None), 
   'face': (
          'bulletFontName', None), 
   'size': (
          'bulletFontSize', _num), 
   'fontsize': (
              'bulletFontSize', _num), 
   'offsety': (
             'bulletOffsetY', _num), 
   'indent': (
            'bulletIndent', _num), 
   'color': (
           'bulletColor', toColor), 
   'fg': (
        'bulletColor', toColor)}
_fontAttrMap = {'size': ('fontSize', _num), 'face': (
          'fontName', None), 
   'name': (
          'fontName', None), 
   'fg': (
        'textColor', toColor), 
   'color': (
           'textColor', toColor), 
   'backcolor': (
               'backColor', toColor), 
   'bgcolor': (
             'backColor', toColor)}
_spanAttrMap = {'size': ('fontSize', _num), 'face': (
          'fontName', None), 
   'name': (
          'fontName', None), 
   'fg': (
        'textColor', toColor), 
   'color': (
           'textColor', toColor), 
   'backcolor': (
               'backColor', toColor), 
   'bgcolor': (
             'backColor', toColor), 
   'style': (
           'style', None)}
_linkAttrMap = {'size': ('fontSize', _num), 'face': (
          'fontName', None), 
   'name': (
          'fontName', None), 
   'fg': (
        'textColor', toColor), 
   'color': (
           'textColor', toColor), 
   'backcolor': (
               'backColor', toColor), 
   'bgcolor': (
             'backColor', toColor), 
   'dest': (
          'link', None), 
   'destination': (
                 'link', None), 
   'target': (
            'link', None), 
   'href': (
          'link', None)}
_anchorAttrMap = {'fontSize': ('fontSize', _num), 'fontName': (
              'fontName', None), 
   'name': (
          'name', None), 
   'fg': (
        'textColor', toColor), 
   'color': (
           'textColor', toColor), 
   'backcolor': (
               'backColor', toColor), 
   'bgcolor': (
             'backColor', toColor), 
   'href': (
          'href', None)}
_imgAttrMap = {'src': (
         'src', None), 
   'width': (
           'width', _numpct), 
   'height': (
            'height', _numpct), 
   'valign': (
            'valign', _valignpc)}
_indexAttrMap = {'name': (
          'name', None), 
   'item': (
          'item', None), 
   'offset': (
            'offset', None), 
   'format': (
            'format', None)}

def _addAttributeNames(m):
    K = m.keys()
    for k in K:
        n = m[k][0]
        if n not in m:
            m[n] = m[k]
        n = string.lower(n)
        if n not in m:
            m[n] = m[k]


_addAttributeNames(_paraAttrMap)
_addAttributeNames(_fontAttrMap)
_addAttributeNames(_spanAttrMap)
_addAttributeNames(_bulletAttrMap)
_addAttributeNames(_anchorAttrMap)
_addAttributeNames(_linkAttrMap)

def _applyAttributes(obj, attr):
    for k, v in attr.items():
        if type(v) is TupleType and v[0] == 'relative':
            if hasattr(obj, k):
                v = v[1] + getattr(obj, k)
            else:
                v = v[1]
        setattr(obj, k, v)


greeks = {'Aacute': 'Á', 
   'aacute': 'á', 
   'Acirc': 'Â', 
   'acirc': 'â', 
   'acute': '´', 
   'AElig': 'Æ', 
   'aelig': 'æ', 
   'Agrave': 'À', 
   'agrave': 'à', 
   'alefsym': 'ℵ', 
   'Alpha': 'Α', 
   'alpha': 'α', 
   'and': '∧', 
   'ang': '∠', 
   'Aring': 'Å', 
   'aring': 'å', 
   'asymp': '≈', 
   'Atilde': 'Ã', 
   'atilde': 'ã', 
   'Auml': 'Ä', 
   'auml': 'ä', 
   'bdquo': '„', 
   'Beta': 'Β', 
   'beta': 'β', 
   'brvbar': '¦', 
   'bull': '•', 
   'cap': '∩', 
   'Ccedil': 'Ç', 
   'ccedil': 'ç', 
   'cedil': '¸', 
   'cent': '¢', 
   'Chi': 'Χ', 
   'chi': 'χ', 
   'circ': 'ˆ', 
   'clubs': '♣', 
   'cong': '≅', 
   'copy': '©', 
   'crarr': '↵', 
   'cup': '∪', 
   'curren': '¤', 
   'dagger': '†', 
   'Dagger': '‡', 
   'darr': '↓', 
   'dArr': '⇓', 
   'deg': '°', 
   'delta': 'δ', 
   'Delta': '∆', 
   'diams': '♦', 
   'divide': '÷', 
   'Eacute': 'É', 
   'eacute': 'é', 
   'Ecirc': 'Ê', 
   'ecirc': 'ê', 
   'Egrave': 'È', 
   'egrave': 'è', 
   'empty': '∅', 
   'emsp': '\u2003', 
   'ensp': '\u2002', 
   'Epsilon': 'Ε', 
   'epsilon': 'ε', 
   'epsiv': 'ε', 
   'equiv': '≡', 
   'Eta': 'Η', 
   'eta': 'η', 
   'ETH': 'Ð', 
   'eth': 'ð', 
   'Euml': 'Ë', 
   'euml': 'ë', 
   'euro': '€', 
   'exist': '∃', 
   'fnof': 'ƒ', 
   'forall': '∀', 
   'frac12': '½', 
   'frac14': '¼', 
   'frac34': '¾', 
   'frasl': '⁄', 
   'Gamma': 'Γ', 
   'gamma': 'γ', 
   'ge': '≥', 
   'harr': '↔', 
   'hArr': '⇔', 
   'hearts': '♥', 
   'hellip': '…', 
   'Iacute': 'Í', 
   'iacute': 'í', 
   'Icirc': 'Î', 
   'icirc': 'î', 
   'iexcl': '¡', 
   'Igrave': 'Ì', 
   'igrave': 'ì', 
   'image': 'ℑ', 
   'infin': '∞', 
   'int': '∫', 
   'Iota': 'Ι', 
   'iota': 'ι', 
   'iquest': '¿', 
   'isin': '∈', 
   'Iuml': 'Ï', 
   'iuml': 'ï', 
   'Kappa': 'Κ', 
   'kappa': 'κ', 
   'Lambda': 'Λ', 
   'lambda': 'λ', 
   'lang': '〈', 
   'laquo': '«', 
   'larr': '←', 
   'lArr': '⇐', 
   'lceil': '\uf8ee', 
   'ldquo': '“', 
   'le': '≤', 
   'lfloor': '\uf8f0', 
   'lowast': '∗', 
   'loz': '◊', 
   'lrm': '\u200e', 
   'lsaquo': '‹', 
   'lsquo': '‘', 
   'macr': '¯', 
   'mdash': '—', 
   'micro': 'µ', 
   'middot': '·', 
   'minus': '−', 
   'mu': 'µ', 
   'Mu': 'Μ', 
   'nabla': '∇', 
   'nbsp': '\xa0', 
   'ndash': '–', 
   'ne': '≠', 
   'ni': '∋', 
   'notin': '∉', 
   'not': '¬', 
   'nsub': '⊄', 
   'Ntilde': 'Ñ', 
   'ntilde': 'ñ', 
   'Nu': 'Ν', 
   'nu': 'ν', 
   'Oacute': 'Ó', 
   'oacute': 'ó', 
   'Ocirc': 'Ô', 
   'ocirc': 'ô', 
   'OElig': 'Œ', 
   'oelig': 'œ', 
   'Ograve': 'Ò', 
   'ograve': 'ò', 
   'oline': '\uf8e5', 
   'omega': 'ω', 
   'Omega': 'Ω', 
   'Omicron': 'Ο', 
   'omicron': 'ο', 
   'oplus': '⊕', 
   'ordf': 'ª', 
   'ordm': 'º', 
   'or': '∨', 
   'Oslash': 'Ø', 
   'oslash': 'ø', 
   'Otilde': 'Õ', 
   'otilde': 'õ', 
   'otimes': '⊗', 
   'Ouml': 'Ö', 
   'ouml': 'ö', 
   'para': '¶', 
   'part': '∂', 
   'permil': '‰', 
   'perp': '⊥', 
   'phis': 'φ', 
   'Phi': 'Φ', 
   'phi': 'ϕ', 
   'piv': 'ϖ', 
   'Pi': 'Π', 
   'pi': 'π', 
   'plusmn': '±', 
   'pound': '£', 
   'prime': '′', 
   'Prime': '″', 
   'prod': '∏', 
   'prop': '∝', 
   'Psi': 'Ψ', 
   'psi': 'ψ', 
   'radic': '√', 
   'rang': '〉', 
   'raquo': '»', 
   'rarr': '→', 
   'rArr': '⇒', 
   'rceil': '\uf8f9', 
   'rdquo': '”', 
   'real': 'ℜ', 
   'reg': '®', 
   'rfloor': '\uf8fb', 
   'Rho': 'Ρ', 
   'rho': 'ρ', 
   'rlm': '\u200f', 
   'rsaquo': '›', 
   'rsquo': '’', 
   'sbquo': '‚', 
   'Scaron': 'Š', 
   'scaron': 'š', 
   'sdot': '⋅', 
   'sect': '§', 
   'shy': '\xad', 
   'sigmaf': 'ς', 
   'sigmav': 'ς', 
   'Sigma': 'Σ', 
   'sigma': 'σ', 
   'sim': '∼', 
   'spades': '♠', 
   'sube': '⊆', 
   'sub': '⊂', 
   'sum': '∑', 
   'sup1': '¹', 
   'sup2': '²', 
   'sup3': '³', 
   'supe': '⊇', 
   'sup': '⊃', 
   'szlig': 'ß', 
   'Tau': 'Τ', 
   'tau': 'τ', 
   'there4': '∴', 
   'thetasym': 'ϑ', 
   'thetav': 'ϑ', 
   'Theta': 'Θ', 
   'theta': 'θ', 
   'thinsp': '\u2009', 
   'THORN': 'Þ', 
   'thorn': 'þ', 
   'tilde': '˜', 
   'times': '×', 
   'trade': '\uf8ea', 
   'Uacute': 'Ú', 
   'uacute': 'ú', 
   'uarr': '↑', 
   'uArr': '⇑', 
   'Ucirc': 'Û', 
   'ucirc': 'û', 
   'Ugrave': 'Ù', 
   'ugrave': 'ù', 
   'uml': '¨', 
   'upsih': 'ϒ', 
   'Upsilon': 'Υ', 
   'upsilon': 'υ', 
   'Uuml': 'Ü', 
   'uuml': 'ü', 
   'weierp': '℘', 
   'Xi': 'Ξ', 
   'xi': 'ξ', 
   'Yacute': 'Ý', 
   'yacute': 'ý', 
   'yen': '¥', 
   'yuml': 'ÿ', 
   'Yuml': 'Ÿ', 
   'Zeta': 'Ζ', 
   'zeta': 'ζ', 
   'zwj': '\u200d', 
   'zwnj': '\u200c'}

class ParaFrag(ABag):
    """class ParaFrag contains the intermediate representation of string
    segments as they are being parsed by the XMLParser.
    fontname, fontSize, rise, textColor, cbDefn
    """
    pass


_greek2Utf8 = None

def _greekConvert(data):
    global _greek2Utf8
    if not _greek2Utf8:
        from reportlab.pdfbase.rl_codecs import RL_Codecs
        import codecs
        dm = decoding_map = codecs.make_identity_dict(xrange(32, 256))
        for k in xrange(0, 32):
            dm[k] = None

        dm.update(RL_Codecs._RL_Codecs__rl_codecs_data['symbol'][0])
        _greek2Utf8 = {}
        for k, v in dm.iteritems():
            if not v:
                u = '\x00'
            else:
                u = unichr(v).encode('utf8')
            _greek2Utf8[chr(k)] = u

    return ('').join(map(_greek2Utf8.__getitem__, data))


class ParaParser(xmllib.XMLParser):

    def __getattr__(self, attrName):
        """This way we can handle <TAG> the same way as <tag> (ignoring case)."""
        if attrName != attrName.lower() and attrName != 'caseSensitive' and not self.caseSensitive and (attrName.startswith('start_') or attrName.startswith('end_')):
            return getattr(self, attrName.lower())
        raise AttributeError, attrName

    def start_b(self, attributes):
        self._push(bold=1)

    def end_b(self):
        self._pop(bold=1)

    def start_strong(self, attributes):
        self._push(bold=1)

    def end_strong(self):
        self._pop(bold=1)

    def start_i(self, attributes):
        self._push(italic=1)

    def end_i(self):
        self._pop(italic=1)

    def start_em(self, attributes):
        self._push(italic=1)

    def end_em(self):
        self._pop(italic=1)

    def start_u(self, attributes):
        self._push(underline=1)

    def end_u(self):
        self._pop(underline=1)

    def start_strike(self, attributes):
        self._push(strike=1)

    def end_strike(self):
        self._pop(strike=1)

    def start_link(self, attributes):
        self._push(**self.getAttributes(attributes, _linkAttrMap))

    def end_link(self):
        frag = self._stack[-1]
        del self._stack[-1]
        assert frag.link != None
        return

    def start_a(self, attributes):
        A = self.getAttributes(attributes, _anchorAttrMap)
        name = A.get('name', None)
        if name is not None:
            name = name.strip()
            if not name:
                self._syntax_error('<a name="..."/> anchor variant requires non-blank name')
            if len(A) > 1:
                self._syntax_error('<a name="..."/> anchor variant only allows name attribute')
                A = dict(name=A['name'])
            A['_selfClosingTag'] = 'anchor'
        else:
            href = A.get('href', '').strip()
            if not href:
                self._syntax_error('<a> tag must have non-blank name or href attribute')
            A['link'] = href
            A.pop('href')
        self._push(**A)
        return

    def end_a(self):
        frag = self._stack[-1]
        sct = getattr(frag, '_selfClosingTag', '')
        if sct:
            assert sct == 'anchor' and frag.name, 'Parser failure in <a/>'
            defn = frag.cbDefn = ABag()
            defn.label = defn.kind = 'anchor'
            defn.name = frag.name
            del frag.name
            del frag._selfClosingTag
            self.handle_data('')
            self._pop()
        else:
            del self._stack[-1]
            assert frag.link != None
        return

    def start_img(self, attributes):
        A = self.getAttributes(attributes, _imgAttrMap)
        if not A.get('src'):
            self._syntax_error('<img> needs src attribute')
        A['_selfClosingTag'] = 'img'
        self._push(**A)

    def end_img(self):
        frag = self._stack[-1]
        assert getattr(frag, '_selfClosingTag', ''), 'Parser failure in <img/>'
        defn = frag.cbDefn = ABag()
        defn.kind = 'img'
        defn.src = getattr(frag, 'src', None)
        defn.image = ImageReader(defn.src)
        size = defn.image.getSize()
        defn.width = getattr(frag, 'width', size[0])
        defn.height = getattr(frag, 'height', size[1])
        defn.valign = getattr(frag, 'valign', 'bottom')
        del frag._selfClosingTag
        self.handle_data('')
        self._pop()
        return

    def start_super(self, attributes):
        self._push(super=1)

    def end_super(self):
        self._pop(super=1)

    start_sup = start_super
    end_sup = end_super

    def start_sub(self, attributes):
        self._push(sub=1)

    def end_sub(self):
        self._pop(sub=1)

    def handle_charref(self, name):
        try:
            if name[0] == 'x':
                n = int(name[1:], 16)
            else:
                n = int(name)
        except ValueError:
            self.unknown_charref(name)
            return

        self.handle_data(unichr(n).encode('utf8'))

    def handle_entityref(self, name):
        if name in greeks:
            self.handle_data(greeks[name])
        else:
            xmllib.XMLParser.handle_entityref(self, name)

    def syntax_error(self, lineno, message):
        self._syntax_error(message)

    def _syntax_error(self, message):
        if message[:10] == 'attribute ' and message[-17:] == ' value not quoted':
            return
        self.errors.append(message)

    def start_greek(self, attr):
        self._push(greek=1)

    def end_greek(self):
        self._pop(greek=1)

    def start_unichar(self, attr):
        if 'name' in attr:
            if 'code' in attr:
                self._syntax_error('<unichar/> invalid with both name and code attributes')
            try:
                v = unicodedata.lookup(attr['name']).encode('utf8')
            except KeyError:
                self._syntax_error('<unichar/> invalid name attribute\n"%s"' % name)
                v = '\x00'

        elif 'code' in attr:
            try:
                v = unichr(int(eval(attr['code']))).encode('utf8')
            except:
                self._syntax_error('<unichar/> invalid code attribute %s' % attr['code'])
                v = '\x00'

        else:
            v = None
            if attr:
                self._syntax_error('<unichar/> invalid attribute %s' % attr.keys()[0])
        if v is not None:
            self.handle_data(v)
        self._push(_selfClosingTag='unichar')
        return

    def end_unichar(self):
        self._pop()

    def start_font(self, attr):
        self._push(**self.getAttributes(attr, _fontAttrMap))

    def end_font(self):
        self._pop()

    def start_span(self, attr):
        A = self.getAttributes(attr, _spanAttrMap)
        if 'style' in A:
            style = self.findSpanStyle(A.pop('style'))
            D = {}
            for k in ('fontName fontSize textColor backColor').split():
                v = getattr(style, k, self)
                if v is self:
                    continue
                D[k] = v

            D.update(A)
            A = D
        self._push(**A)

    end_span = end_font

    def start_br(self, attr):
        self._push(_selfClosingTag='br', lineBreak=True, text='')

    def end_br(self):
        frag = self._stack[-1]
        assert frag._selfClosingTag == 'br' and frag.lineBreak, 'Parser failure in <br/>'
        del frag._selfClosingTag
        self.handle_data('')
        self._pop()

    def _initial_frag(self, attr, attrMap, bullet=0):
        style = self._style
        if attr != {}:
            style = copy.deepcopy(style)
            _applyAttributes(style, self.getAttributes(attr, attrMap))
            self._style = style
        frag = ParaFrag()
        frag.sub = 0
        frag.super = 0
        frag.rise = 0
        frag.underline = 0
        frag.strike = 0
        frag.greek = 0
        frag.link = None
        if bullet:
            frag.fontName, frag.bold, frag.italic = ps2tt(style.bulletFontName)
            frag.fontSize = style.bulletFontSize
            frag.textColor = hasattr(style, 'bulletColor') and style.bulletColor or style.textColor
        else:
            frag.fontName, frag.bold, frag.italic = ps2tt(style.fontName)
            frag.fontSize = style.fontSize
            frag.textColor = style.textColor
        return frag

    def start_para(self, attr):
        self._stack = [
         self._initial_frag(attr, _paraAttrMap)]

    def end_para(self):
        self._pop()

    def start_bullet(self, attr):
        if hasattr(self, 'bFragList'):
            self._syntax_error('only one <bullet> tag allowed')
        self.bFragList = []
        frag = self._initial_frag(attr, _bulletAttrMap, 1)
        frag.isBullet = 1
        self._stack.append(frag)

    def end_bullet(self):
        self._pop()

    def start_seqdefault(self, attr):
        try:
            default = attr['id']
        except KeyError:
            default = None

        self._seq.setDefaultCounter(default)
        return

    def end_seqdefault(self):
        pass

    def start_seqreset(self, attr):
        try:
            id = attr['id']
        except KeyError:
            id = None

        try:
            base = int(attr['base'])
        except:
            base = 0

        self._seq.reset(id, base)
        return

    def end_seqreset(self):
        pass

    def start_seqchain(self, attr):
        try:
            order = attr['order']
        except KeyError:
            order = ''

        order = order.split()
        seq = self._seq
        for p, c in zip(order[:-1], order[1:]):
            seq.chain(p, c)

    end_seqchain = end_seqreset

    def start_seqformat(self, attr):
        try:
            id = attr['id']
        except KeyError:
            id = None

        try:
            value = attr['value']
        except KeyError:
            value = '1'

        self._seq.setFormat(id, value)
        return

    end_seqformat = end_seqreset
    start_seqDefault = start_seqdefault
    end_seqDefault = end_seqdefault
    start_seqReset = start_seqreset
    end_seqReset = end_seqreset
    start_seqChain = start_seqchain
    end_seqChain = end_seqchain
    start_seqFormat = start_seqformat
    end_seqFormat = end_seqformat

    def start_seq(self, attr):
        if 'template' in attr:
            templ = attr['template']
            self.handle_data(templ % self._seq)
            return
        else:
            if 'id' in attr:
                id = attr['id']
            else:
                id = None
            increment = attr.get('inc', None)
            if not increment:
                output = self._seq.nextf(id)
            elif increment.lower() == 'no':
                output = self._seq.thisf(id)
            else:
                incr = int(increment)
                output = self._seq.thisf(id)
                self._seq.reset(id, self._seq._this() + incr)
            self.handle_data(output)
            return

    def end_seq(self):
        pass

    def start_onDraw(self, attr):
        defn = ABag()
        if 'name' in attr:
            defn.name = attr['name']
        else:
            self._syntax_error('<onDraw> needs at least a name attribute')
        if 'label' in attr:
            defn.label = attr['label']
        defn.kind = 'onDraw'
        self._push(cbDefn=defn)
        self.handle_data('')
        self._pop()

    end_onDraw = end_seq

    def start_index(self, attr):
        attr = self.getAttributes(attr, _indexAttrMap)
        defn = ABag()
        if 'item' in attr:
            label = attr['item']
        else:
            self._syntax_error('<index> needs at least an item attribute')
        if 'name' in attr:
            name = attr['name']
        else:
            name = DEFAULT_INDEX_NAME
        format = attr.get('format', None)
        if format is not None and format not in ('123', 'I', 'i', 'ABC', 'abc'):
            raise ValueError('index tag format is %r not valid 123 I i ABC or abc' % offset)
        offset = attr.get('offset', None)
        if offset is not None:
            try:
                offset = int(offset)
            except:
                raise ValueError('index tag offset is %r not an int' % offset)

        defn.label = base64.encodestring(pickle.dumps((label, format, offset))).strip()
        defn.name = name
        defn.kind = 'index'
        self._push(cbDefn=defn)
        self.handle_data('')
        self._pop()
        return

    end_index = end_seq

    def _push(self, **attr):
        frag = copy.copy(self._stack[-1])
        _applyAttributes(frag, attr)
        self._stack.append(frag)

    def _pop(self, **kw):
        frag = self._stack[-1]
        del self._stack[-1]
        for k, v in kw.items():
            assert getattr(frag, k) == v

        return frag

    def getAttributes(self, attr, attrMap):
        A = {}
        for k, v in attr.items():
            if not self.caseSensitive:
                k = string.lower(k)
            if k in attrMap.keys():
                j = attrMap[k]
                func = j[1]
                try:
                    A[j[0]] = func is None and v or func(v)
                except:
                    self._syntax_error('%s: invalid value %s' % (k, v))

            else:
                self._syntax_error('invalid attribute name %s' % k)

        return A

    def __init__(self, verbose=0):
        self.caseSensitive = 0
        xmllib.XMLParser.__init__(self, verbose=verbose)

    def _iReset(self):
        self.fragList = []
        if hasattr(self, 'bFragList'):
            delattr(self, 'bFragList')

    def _reset(self, style):
        """reset the parser"""
        xmllib.XMLParser.reset(self)
        self.errors = []
        self._style = style
        self._iReset()

    def handle_data(self, data):
        """Creates an intermediate representation of string segments."""
        frag = copy.copy(self._stack[-1])
        if hasattr(frag, 'cbDefn'):
            kind = frag.cbDefn.kind
            if data:
                self._syntax_error('Only empty <%s> tag allowed' % kind)
        else:
            if hasattr(frag, '_selfClosingTag'):
                if data != '':
                    self._syntax_error('No content allowed in %s tag' % frag._selfClosingTag)
                return
            if frag.sub == 1 and frag.super == 1:
                frag.sub = 0
                frag.super = 0
            if frag.sub:
                frag.rise = -frag.fontSize * subFraction
                frag.fontSize = max(frag.fontSize - sizeDelta, 3)
            elif frag.super:
                frag.rise = frag.fontSize * superFraction
                frag.fontSize = max(frag.fontSize - sizeDelta, 3)
            if frag.greek:
                frag.fontName = 'symbol'
                data = _greekConvert(data)
        frag.fontName = tt2ps(frag.fontName, frag.bold, frag.italic)
        frag.text = data
        if hasattr(frag, 'isBullet'):
            delattr(frag, 'isBullet')
            self.bFragList.append(frag)
        else:
            self.fragList.append(frag)

    def handle_cdata(self, data):
        self.handle_data(data)

    def _setup_for_parse(self, style):
        self._seq = reportlab.lib.sequencer.getSequencer()
        self._reset(style)

    def parse(self, text, style):
        """Given a formatted string will return a list of
        ParaFrag objects with their calculated widths.
        If errors occur None will be returned and the
        self.errors holds a list of the error messages.
        """
        enc = self._enc = 'utf8'
        self._UNI = type(text) is UnicodeType
        if self._UNI:
            text = text.encode(enc)
        self._setup_for_parse(style)
        if not (len(text) >= 6 and text[0] == '<' and _re_para.match(text)):
            text = '<para>' + text + '</para>'
        self.feed(text)
        self.close()
        return self._complete_parse()

    def _complete_parse(self):
        del self._seq
        style = self._style
        del self._style
        if len(self.errors) == 0:
            fragList = self.fragList
            bFragList = hasattr(self, 'bFragList') and self.bFragList or None
            self._iReset()
        else:
            fragList = bFragList = None
        if self._UNI:
            if fragList:
                for frag in fragList:
                    frag.text = unicode(frag.text, self._enc)

            if bFragList:
                for frag in bFragList:
                    frag.text = unicode(frag.text, self._enc)

        return (
         style, fragList, bFragList)

    def _tt_parse(self, tt):
        tag = tt[0]
        try:
            start = getattr(self, 'start_' + tag)
            end = getattr(self, 'end_' + tag)
        except AttributeError:
            raise ValueError('Invalid tag "%s"' % tag)

        start(tt[1] or {})
        C = tt[2]
        if C:
            M = self._tt_handlers
            for c in C:
                M[type(c) is TupleType](c)

        end()

    def tt_parse(self, tt, style):
        """parse from tupletree form"""
        self._setup_for_parse(style)
        self._tt_handlers = (self.handle_data, self._tt_parse)
        self._tt_parse(tt)
        return self._complete_parse()

    def findSpanStyle(self, style):
        raise ValueError('findSpanStyle not implemented in this parser')


if __name__ == '__main__':
    from reportlab.platypus import cleanBlockQuotedText
    from reportlab.lib.styles import _baseFontName
    _parser = ParaParser()

    def check_text(text, p=_parser):
        print '##########'
        text = cleanBlockQuotedText(text)
        l, rv, bv = p.parse(text, style)
        if rv is None:
            for l in _parser.errors:
                print l

        else:
            print 'ParaStyle', l.fontName, l.fontSize, l.textColor
            for l in rv:
                print l.fontName, l.fontSize, l.textColor, l.bold, l.rise, '|%s|' % l.text[:25],
                if hasattr(l, 'cbDefn'):
                    print 'cbDefn', getattr(l.cbDefn, 'name', ''), getattr(l.cbDefn, 'label', ''), l.cbDefn.kind
                else:
                    print

        return


    style = ParaFrag()
    style.fontName = _baseFontName
    style.fontSize = 12
    style.textColor = black
    style.bulletFontName = black
    style.bulletFontName = _baseFontName
    style.bulletFontSize = 12
    text = '\n    <b><i><greek>a</greek>D</i></b>&beta;<unichr value="0x394"/>\n    <font name="helvetica" size="15" color=green>\n    Tell me, O muse, of that ingenious hero who travelled far and wide\n    after</font> he had sacked the famous town of Troy. Many cities did he visit,\n    and many were the nations with whose manners and customs he was acquainted;\n    moreover he suffered much by sea while trying to save his own life\n    and bring his men safely home; but do what he might he could not save\n    his men, for they perished through their own sheer folly in eating\n    the cattle of the Sun-god Hyperion; so the god prevented them from\n    ever reaching home. Tell me, too, about all these things, O daughter\n    of Jove, from whatsoever source you<super>1</super> may know them.\n    '
    check_text(text)
    check_text('<para> </para>')
    check_text('<para font="%s" size=24 leading=28.8 spaceAfter=72>ReportLab -- Reporting for the Internet Age</para>' % _baseFontName)
    check_text('\n    <font color=red>&tau;</font>Tell me, O muse, of that ingenious hero who travelled far and wide\n    after he had sacked the famous town of Troy. Many cities did he visit,\n    and many were the nations with whose manners and customs he was acquainted;\n    moreover he suffered much by sea while trying to save his own life\n    and bring his men safely home; but do what he might he could not save\n    his men, for they perished through their own sheer folly in eating\n    the cattle of the Sun-god Hyperion; so the god prevented them from\n    ever reaching home. Tell me, too, about all these things, O daughter\n    of Jove, from whatsoever source you may know them.')
    check_text('\n    Telemachus took this speech as of good omen and rose at once, for\n    he was bursting with what he had to say. He stood in the middle of\n    the assembly and the good herald Pisenor brought him his staff. Then,\n    turning to Aegyptius, "Sir," said he, "it is I, as you will shortly\n    learn, who have convened you, for it is I who am the most aggrieved.\n    I have not got wind of any host approaching about which I would warn\n    you, nor is there any matter of public moment on which I would speak.\n    My grieveance is purely personal, and turns on two great misfortunes\n    which have fallen upon my house. The first of these is the loss of\n    my excellent father, who was chief among all you here present, and\n    was like a father to every one of you; the second is much more serious,\n    and ere long will be the utter ruin of my estate. The sons of all\n    the chief men among you are pestering my mother to marry them against\n    her will. They are afraid to go to her father Icarius, asking him\n    to choose the one he likes best, and to provide marriage gifts for\n    his daughter, but day by day they keep hanging about my father\'s house,\n    sacrificing our oxen, sheep, and fat goats for their banquets, and\n    never giving so much as a thought to the quantity of wine they drink.\n    No estate can stand such recklessness; we have now no Ulysses to ward\n    off harm from our doors, and I cannot hold my own against them. I\n    shall never all my days be as good a man as he was, still I would\n    indeed defend myself if I had power to do so, for I cannot stand such\n    treatment any longer; my house is being disgraced and ruined. Have\n    respect, therefore, to your own consciences and to public opinion.\n    Fear, too, the wrath of heaven, lest the gods should be displeased\n    and turn upon you. I pray you by Jove and Themis, who is the beginning\n    and the end of councils, [do not] hold back, my friends, and leave\n    me singlehanded- unless it be that my brave father Ulysses did some\n    wrong to the Achaeans which you would now avenge on me, by aiding\n    and abetting these suitors. Moreover, if I am to be eaten out of house\n    and home at all, I had rather you did the eating yourselves, for I\n    could then take action against you to some purpose, and serve you\n    with notices from house to house till I got paid in full, whereas\n    now I have no remedy."')
    check_text('\nBut as the sun was rising from the fair sea into the firmament of\nheaven to shed light on mortals and immortals, they reached Pylos\nthe city of Neleus. Now the people of Pylos were gathered on the sea\nshore to offer sacrifice of black bulls to Neptune lord of the Earthquake.\nThere were nine guilds with five hundred men in each, and there were\nnine bulls to each guild. As they were eating the inward meats and\nburning the thigh bones [on the embers] in the name of Neptune, Telemachus\nand his crew arrived, furled their sails, brought their ship to anchor,\nand went ashore. ')
    check_text('\nSo the neighbours and kinsmen of Menelaus were feasting and making\nmerry in his house. There was a bard also to sing to them and play\nhis lyre, while two tumblers went about performing in the midst of\nthem when the man struck up with his tune.]')
    check_text('\n"When we had passed the [Wandering] rocks, with Scylla and terrible\nCharybdis, we reached the noble island of the sun-god, where were\nthe goodly cattle and sheep belonging to the sun Hyperion. While still\nat sea in my ship I could bear the cattle lowing as they came home\nto the yards, and the sheep bleating. Then I remembered what the blind\nTheban prophet Teiresias had told me, and how carefully Aeaean Circe\nhad warned me to shun the island of the blessed sun-god. So being\nmuch troubled I said to the men, \'My men, I know you are hard pressed,\nbut listen while I <strike>tell you the prophecy that</strike> Teiresias made me, and\nhow carefully Aeaean Circe warned me to shun the island of the blessed\nsun-god, for it was here, she said, that our worst danger would lie.\nHead the ship, therefore, away from the island.')
    check_text('A&lt;B&gt;C&amp;D&quot;E&apos;F')
    check_text('A&lt; B&gt; C&amp; D&quot; E&apos; F')
    check_text('<![CDATA[<>&\'"]]>')
    check_text('<bullet face=courier size=14 color=green>+</bullet>\nThere was a bard also to sing to them and play\nhis lyre, while two tumblers went about performing in the midst of\nthem when the man struck up with his tune.]')
    check_text('<onDraw name="myFunc" label="aaa   bbb">A paragraph')
    check_text('<para><onDraw name="myFunc" label="aaa   bbb">B paragraph</para>')
    _parser.caseSensitive = 0
    check_text('Here comes <FONT FACE="Helvetica" SIZE="14pt">Helvetica 14</FONT> with <STRONG>strong</STRONG> <EM>emphasis</EM>.')
    check_text('Here comes <font face="Helvetica" size="14pt">Helvetica 14</font> with <Strong>strong</Strong> <em>emphasis</em>.')
    check_text('Here comes <font face="Courier" size="3cm">Courier 3cm</font> and normal again.')
    check_text('Before the break <br/>the middle line <br/> and the last line.')
    check_text("This should be an inline image <img src='../../../docs/images/testimg.gif'/>!")
    check_text('aaa&nbsp;bbbb <u>underline&#32;</u> cccc')