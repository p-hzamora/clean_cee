# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: c:\python27\lib\site-packages\lxml-3.2.4-py2.7-win32.egg\lxml\html\ElementSoup.py
# Compiled at: 2013-12-10 09:11:58
"""Legacy interface to the BeautifulSoup HTML parser.
"""
__all__ = [
 'parse', 'convert_tree']
from soupparser import convert_tree, parse as _parse

def parse(file, beautifulsoup=None, makeelement=None):
    root = _parse(file, beautifulsoup=beautifulsoup, makeelement=makeelement)
    return root.getroot()