# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: c:\python27\lib\site-packages\lxml-3.2.4-py2.7-win32.egg\lxml\html\soupparser.py
# Compiled at: 2013-12-10 09:11:58
"""External interface to the BeautifulSoup HTML parser.
"""
__all__ = [
 'fromstring', 'parse', 'convert_tree']
from lxml import etree, html
from BeautifulSoup import BeautifulSoup, Tag, Comment, ProcessingInstruction, NavigableString

def fromstring(data, beautifulsoup=None, makeelement=None, **bsargs):
    """Parse a string of HTML data into an Element tree using the
    BeautifulSoup parser.

    Returns the root ``<html>`` Element of the tree.

    You can pass a different BeautifulSoup parser through the
    `beautifulsoup` keyword, and a diffent Element factory function
    through the `makeelement` keyword.  By default, the standard
    ``BeautifulSoup`` class and the default factory of `lxml.html` are
    used.
    """
    return _parse(data, beautifulsoup, makeelement, **bsargs)


def parse(file, beautifulsoup=None, makeelement=None, **bsargs):
    """Parse a file into an ElemenTree using the BeautifulSoup parser.

    You can pass a different BeautifulSoup parser through the
    `beautifulsoup` keyword, and a diffent Element factory function
    through the `makeelement` keyword.  By default, the standard
    ``BeautifulSoup`` class and the default factory of `lxml.html` are
    used.
    """
    if not hasattr(file, 'read'):
        file = open(file)
    root = _parse(file, beautifulsoup, makeelement, **bsargs)
    return etree.ElementTree(root)


def convert_tree(beautiful_soup_tree, makeelement=None):
    """Convert a BeautifulSoup tree to a list of Element trees.

    Returns a list instead of a single root Element to support
    HTML-like soup with more than one root element.

    You can pass a different Element factory through the `makeelement`
    keyword.
    """
    if makeelement is None:
        makeelement = html.html_parser.makeelement
    root = _convert_tree(beautiful_soup_tree, makeelement)
    children = root.getchildren()
    for child in children:
        root.remove(child)

    return children


def _parse(source, beautifulsoup, makeelement, **bsargs):
    if beautifulsoup is None:
        beautifulsoup = BeautifulSoup
    if makeelement is None:
        makeelement = html.html_parser.makeelement
    if 'convertEntities' not in bsargs:
        bsargs['convertEntities'] = 'html'
    tree = beautifulsoup(source, **bsargs)
    root = _convert_tree(tree, makeelement)
    if len(root) == 1 and root[0].tag == 'html':
        return root[0]
    else:
        root.tag = 'html'
        return root


def _convert_tree(beautiful_soup_tree, makeelement):
    root = makeelement(beautiful_soup_tree.name, attrib=dict(beautiful_soup_tree.attrs))
    _convert_children(root, beautiful_soup_tree, makeelement)
    return root


def _convert_children(parent, beautiful_soup_tree, makeelement):
    SubElement = etree.SubElement
    et_child = None
    for child in beautiful_soup_tree:
        if isinstance(child, Tag):
            et_child = SubElement(parent, child.name, attrib=dict([ (k, unescape(v)) for k, v in child.attrs ]))
            _convert_children(et_child, child, makeelement)
        elif type(child) is NavigableString:
            _append_text(parent, et_child, unescape(child))
        elif isinstance(child, Comment):
            parent.append(etree.Comment(child))
        elif isinstance(child, ProcessingInstruction):
            parent.append(etree.ProcessingInstruction(*child.split(' ', 1)))
        else:
            _append_text(parent, et_child, unescape(child))

    return


def _append_text(parent, element, text):
    if element is None:
        parent.text = (parent.text or '') + text
    else:
        element.tail = (element.tail or '') + text
    return


try:
    from html.entities import name2codepoint
except ImportError:
    from htmlentitydefs import name2codepoint

import re
handle_entities = re.compile('&(\\w+);').sub

def unescape(string):
    if not string:
        return ''

    def unescape_entity(m):
        try:
            return unichr(name2codepoint[m.group(1)])
        except KeyError:
            return m.group(0)

    return handle_entities(unescape_entity, string)