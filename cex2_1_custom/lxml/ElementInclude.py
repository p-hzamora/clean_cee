# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: c:\python27\lib\site-packages\lxml-3.2.4-py2.7-win32.egg\lxml\ElementInclude.py
# Compiled at: 2013-12-10 09:11:58
"""
Limited XInclude support for the ElementTree package.

While lxml.etree has full support for XInclude (see
`etree.ElementTree.xinclude()`), this module provides a simpler, pure
Python, ElementTree compatible implementation that supports a simple
form of custom URL resolvers.
"""
from lxml import etree
import copy
try:
    from urlparse import urljoin
    from urllib2 import urlopen
except ImportError:
    from urllib.parse import urljoin
    from urllib.request import urlopen

try:
    set
except NameError:
    from sets import Set as set

XINCLUDE = '{http://www.w3.org/2001/XInclude}'
XINCLUDE_INCLUDE = XINCLUDE + 'include'
XINCLUDE_FALLBACK = XINCLUDE + 'fallback'

class FatalIncludeError(etree.LxmlSyntaxError):
    pass


def default_loader(href, parse, encoding=None):
    file = open(href, 'rb')
    if parse == 'xml':
        data = etree.parse(file).getroot()
    else:
        data = file.read()
        if not encoding:
            encoding = 'utf-8'
        data = data.decode(encoding)
    file.close()
    return data


def _lxml_default_loader(href, parse, encoding=None, parser=None):
    if parse == 'xml':
        data = etree.parse(href, parser).getroot()
    else:
        if '://' in href:
            f = urlopen(href)
        else:
            f = open(href, 'rb')
        data = f.read()
        f.close()
        if not encoding:
            encoding = 'utf-8'
        data = data.decode(encoding)
    return data


def _wrap_et_loader(loader):

    def load(href, parse, encoding=None, parser=None):
        return loader(href, parse, encoding)

    return load


def include(elem, loader=None, base_url=None):
    if base_url is None:
        if hasattr(elem, 'getroot'):
            tree = elem
            elem = elem.getroot()
        else:
            tree = elem.getroottree()
        if hasattr(tree, 'docinfo'):
            base_url = tree.docinfo.URL
    elif hasattr(elem, 'getroot'):
        elem = elem.getroot()
    _include(elem, loader, base_url=base_url)
    return


def _include(elem, loader=None, _parent_hrefs=None, base_url=None):
    if loader is not None:
        load_include = _wrap_et_loader(loader)
    else:
        load_include = _lxml_default_loader
    if _parent_hrefs is None:
        _parent_hrefs = set()
    parser = elem.getroottree().parser
    include_elements = list(elem.iter('{http://www.w3.org/2001/XInclude}*'))
    for e in include_elements:
        if e.tag == XINCLUDE_INCLUDE:
            href = urljoin(base_url, e.get('href'))
            parse = e.get('parse', 'xml')
            parent = e.getparent()
            if parse == 'xml':
                if href in _parent_hrefs:
                    raise FatalIncludeError('recursive include of %r detected' % href)
                _parent_hrefs.add(href)
                node = load_include(href, parse, parser=parser)
                if node is None:
                    raise FatalIncludeError('cannot load %r as %r' % (href, parse))
                node = _include(node, loader, _parent_hrefs)
                if e.tail:
                    node.tail = (node.tail or '') + e.tail
                if parent is None:
                    return node
                parent.replace(e, node)
            else:
                if parse == 'text':
                    text = load_include(href, parse, encoding=e.get('encoding'))
                    if text is None:
                        raise FatalIncludeError('cannot load %r as %r' % (href, parse))
                    predecessor = e.getprevious()
                    if predecessor is not None:
                        predecessor.tail = (predecessor.tail or '') + text
                    else:
                        if parent is None:
                            return text
                        parent.text = (parent.text or '') + text + (e.tail or '')
                    parent.remove(e)
                else:
                    raise FatalIncludeError('unknown parse type in xi:include tag (%r)' % parse)
        elif e.tag == XINCLUDE_FALLBACK:
            parent = e.getparent()
            if parent is not None and parent.tag != XINCLUDE_INCLUDE:
                raise FatalIncludeError('xi:fallback tag must be child of xi:include (%r)' % e.tag)
        else:
            raise FatalIncludeError('Invalid element found in XInclude namespace (%r)' % e.tag)

    return elem