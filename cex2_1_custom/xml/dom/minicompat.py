# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: xml\dom\minicompat.pyc
# Compiled at: 2011-05-30 06:53:54
"""Python version compatibility support for minidom."""
__all__ = [
 'NodeList', 'EmptyNodeList', 'StringTypes', 'defproperty']
import xml.dom
try:
    unicode
except NameError:
    StringTypes = (
     type(''),)
else:
    StringTypes = (
     type(''), type(unicode('')))

class NodeList(list):
    __slots__ = ()

    def item(self, index):
        if 0 <= index < len(self):
            return self[index]

    def _get_length(self):
        return len(self)

    def _set_length(self, value):
        raise xml.dom.NoModificationAllowedErr("attempt to modify read-only attribute 'length'")

    length = property(_get_length, _set_length, doc='The number of nodes in the NodeList.')

    def __getstate__(self):
        return list(self)

    def __setstate__(self, state):
        self[:] = state


class EmptyNodeList(tuple):
    __slots__ = ()

    def __add__(self, other):
        NL = NodeList()
        NL.extend(other)
        return NL

    def __radd__(self, other):
        NL = NodeList()
        NL.extend(other)
        return NL

    def item(self, index):
        return

    def _get_length(self):
        return 0

    def _set_length(self, value):
        raise xml.dom.NoModificationAllowedErr("attempt to modify read-only attribute 'length'")

    length = property(_get_length, _set_length, doc='The number of nodes in the NodeList.')


def defproperty(klass, name, doc):
    get = getattr(klass, '_get_' + name).im_func

    def set(self, value, name=name):
        raise xml.dom.NoModificationAllowedErr('attempt to modify read-only attribute ' + repr(name))

    assert not hasattr(klass, '_set_' + name), 'expected not to find _set_' + name
    prop = property(get, set, doc=doc)
    setattr(klass, name, prop)