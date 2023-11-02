# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\fontconfig_pattern.pyc
# Compiled at: 2012-11-06 15:31:10
"""
A module for parsing and generating fontconfig patterns.

See the `fontconfig pattern specification
<http://www.fontconfig.org/fontconfig-user.html>`_ for more
information.
"""
from __future__ import print_function
import re, sys
if sys.version_info[0] >= 3:
    from matplotlib.pyparsing_py3 import Literal, ZeroOrMore, Optional, Regex, StringEnd, ParseException, Suppress
else:
    from matplotlib.pyparsing_py2 import Literal, ZeroOrMore, Optional, Regex, StringEnd, ParseException, Suppress
family_punc = '\\\\\\-:,'
family_unescape = re.compile('\\\\([%s])' % family_punc).sub
family_escape = re.compile('([%s])' % family_punc).sub
value_punc = '\\\\=_:,'
value_unescape = re.compile('\\\\([%s])' % value_punc).sub
value_escape = re.compile('([%s])' % value_punc).sub

class FontconfigPatternParser:
    """A simple pyparsing-based parser for fontconfig-style patterns.

    See the `fontconfig pattern specification
    <http://www.fontconfig.org/fontconfig-user.html>`_ for more
    information.
    """
    _constants = {'thin': ('weight', 'light'), 
       'extralight': ('weight', 'light'), 
       'ultralight': ('weight', 'light'), 
       'light': ('weight', 'light'), 
       'book': ('weight', 'book'), 
       'regular': ('weight', 'regular'), 
       'normal': ('weight', 'normal'), 
       'medium': ('weight', 'medium'), 
       'demibold': ('weight', 'demibold'), 
       'semibold': ('weight', 'semibold'), 
       'bold': ('weight', 'bold'), 
       'extrabold': ('weight', 'extra bold'), 
       'black': ('weight', 'black'), 
       'heavy': ('weight', 'heavy'), 
       'roman': ('slant', 'normal'), 
       'italic': ('slant', 'italic'), 
       'oblique': ('slant', 'oblique'), 
       'ultracondensed': ('width', 'ultra-condensed'), 
       'extracondensed': ('width', 'extra-condensed'), 
       'condensed': ('width', 'condensed'), 
       'semicondensed': ('width', 'semi-condensed'), 
       'expanded': ('width', 'expanded'), 
       'extraexpanded': ('width', 'extra-expanded'), 
       'ultraexpanded': ('width', 'ultra-expanded')}

    def __init__(self):
        family = Regex('([^%s]|(\\\\[%s]))*' % (
         family_punc, family_punc)).setParseAction(self._family)
        size = Regex('([0-9]+\\.?[0-9]*|\\.[0-9]+)').setParseAction(self._size)
        name = Regex('[a-z]+').setParseAction(self._name)
        value = Regex('([^%s]|(\\\\[%s]))*' % (
         value_punc, value_punc)).setParseAction(self._value)
        families = (family + ZeroOrMore(Literal(',') + family)).setParseAction(self._families)
        point_sizes = (size + ZeroOrMore(Literal(',') + size)).setParseAction(self._point_sizes)
        property = (name + Suppress(Literal('=')) + value + ZeroOrMore(Suppress(Literal(',')) + value) | name).setParseAction(self._property)
        pattern = Optional(families) + Optional(Literal('-') + point_sizes) + ZeroOrMore(Literal(':') + property) + StringEnd()
        self._parser = pattern
        self.ParseException = ParseException

    def parse(self, pattern):
        """
        Parse the given fontconfig *pattern* and return a dictionary
        of key/value pairs useful for initializing a
        :class:`font_manager.FontProperties` object.
        """
        props = self._properties = {}
        try:
            self._parser.parseString(pattern)
        except self.ParseException as e:
            raise ValueError("Could not parse font string: '%s'\n%s" % (pattern, e))

        self._properties = None
        self._parser.resetCache()
        return props

    def _family(self, s, loc, tokens):
        return [
         family_unescape('\\1', str(tokens[0]))]

    def _size(self, s, loc, tokens):
        return [
         float(tokens[0])]

    def _name(self, s, loc, tokens):
        return [
         str(tokens[0])]

    def _value(self, s, loc, tokens):
        return [
         value_unescape('\\1', str(tokens[0]))]

    def _families(self, s, loc, tokens):
        self._properties['family'] = [ str(x) for x in tokens ]
        return []

    def _point_sizes(self, s, loc, tokens):
        self._properties['size'] = [ str(x) for x in tokens ]
        return []

    def _property(self, s, loc, tokens):
        if len(tokens) == 1:
            if tokens[0] in self._constants:
                key, val = self._constants[tokens[0]]
                self._properties.setdefault(key, []).append(val)
        else:
            key = tokens[0]
            val = tokens[1:]
            self._properties.setdefault(key, []).extend(val)
        return []


parse_fontconfig_pattern = FontconfigPatternParser().parse

def generate_fontconfig_pattern(d):
    """
    Given a dictionary of key/value pairs, generates a fontconfig
    pattern string.
    """
    props = []
    families = ''
    size = ''
    for key in ('family style variant weight stretch file size').split():
        val = getattr(d, 'get_' + key)()
        if val is not None and val != []:
            if type(val) == list:
                val = [ value_escape('\\\\\\1', str(x)) for x in val if x is not None ]
                if val != []:
                    val = (',').join(val)
            props.append(':%s=%s' % (key, val))

    return ('').join(props)