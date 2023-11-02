# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: c:\python27\lib\site-packages\lxml-3.2.4-py2.7-win32.egg\lxml\html\_html5builder.py
# Compiled at: 2013-12-10 09:11:58
"""
Legacy module - don't use in new code!

html5lib now has its own proper implementation.

This module implements a tree builder for html5lib that generates lxml
html element trees.  This module uses camelCase as it follows the
html5lib style guide.
"""
from html5lib.treebuilders import _base, etree as etree_builders
from lxml import html, etree

class DocumentType(object):

    def __init__(self, name, publicId, systemId):
        self.name = name
        self.publicId = publicId
        self.systemId = systemId


class Document(object):

    def __init__(self):
        self._elementTree = None
        self.childNodes = []
        return

    def appendChild(self, element):
        self._elementTree.getroot().addnext(element._element)


class TreeBuilder(_base.TreeBuilder):
    documentClass = Document
    doctypeClass = DocumentType
    elementClass = None
    commentClass = None
    fragmentClass = Document

    def __init__(self, *args, **kwargs):
        html_builder = etree_builders.getETreeModule(html, fullTree=False)
        etree_builder = etree_builders.getETreeModule(etree, fullTree=False)
        self.elementClass = html_builder.Element
        self.commentClass = etree_builder.Comment
        _base.TreeBuilder.__init__(self, *args, **kwargs)

    def reset(self):
        _base.TreeBuilder.reset(self)
        self.rootInserted = False
        self.initialComments = []
        self.doctype = None
        return

    def getDocument(self):
        return self.document._elementTree

    def getFragment(self):
        fragment = []
        element = self.openElements[0]._element
        if element.text:
            fragment.append(element.text)
        fragment.extend(element.getchildren())
        if element.tail:
            fragment.append(element.tail)
        return fragment

    def insertDoctype(self, name, publicId, systemId):
        doctype = self.doctypeClass(name, publicId, systemId)
        self.doctype = doctype

    def insertComment(self, data, parent=None):
        if not self.rootInserted:
            self.initialComments.append(data)
        else:
            _base.TreeBuilder.insertComment(self, data, parent)

    def insertRoot(self, name):
        buf = []
        if self.doctype and self.doctype.name:
            buf.append('<!DOCTYPE %s' % self.doctype.name)
            if self.doctype.publicId is not None or self.doctype.systemId is not None:
                buf.append(' PUBLIC "%s" "%s"' % (self.doctype.publicId,
                 self.doctype.systemId))
            buf.append('>')
        buf.append('<html></html>')
        root = html.fromstring(('').join(buf))
        for comment in self.initialComments:
            root.addprevious(etree.Comment(comment))

        self.document = self.documentClass()
        self.document._elementTree = root.getroottree()
        root_element = self.elementClass(name)
        root_element._element = root
        self.document.childNodes.append(root_element)
        self.openElements.append(root_element)
        self.rootInserted = True
        return