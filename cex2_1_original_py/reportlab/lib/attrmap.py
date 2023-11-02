# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\lib\attrmap.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = 'Framework for objects whose assignments are checked. Used by graphics.\n\nWe developed reportlab/graphics prior to Python 2 and metaclasses. For the\ngraphics, we wanted to be able to declare the attributes of a class, check\nthem on assignment, and convert from string arguments.  Examples of\nattrmap-based objects can be found in reportlab/graphics/shapes.  It lets\nus defined structures like the one below, which are seen more modern form in\nDjango models and other frameworks.\n\nWe\'ll probably replace this one day soon, hopefully with no impact on client\ncode.\n\nclass Rect(SolidShape):\n    """Rectangle, possibly with rounded corners."""\n\n    _attrMap = AttrMap(BASE=SolidShape,\n        x = AttrMapValue(isNumber),\n        y = AttrMapValue(isNumber),\n        width = AttrMapValue(isNumber),\n        height = AttrMapValue(isNumber),\n        rx = AttrMapValue(isNumber),\n        ry = AttrMapValue(isNumber),\n        )\n\n\n'
from UserDict import UserDict
from reportlab.lib.validators import isAnything, _SequenceTypes, DerivedValue
from reportlab import rl_config

class CallableValue:
    """a class to allow callable initial values"""

    def __init__(self, func, *args, **kw):
        self.func = func
        self.args = args
        self.kw = kw

    def __call__(self):
        return self.func(*self.args, **self.kw)


class AttrMapValue:
    """Simple multi-value holder for attribute maps"""

    def __init__(self, validate=None, desc=None, initial=None, advancedUsage=0, **kw):
        self.validate = validate or isAnything
        self.desc = desc
        self._initial = initial
        self._advancedUsage = advancedUsage
        for k, v in kw.items():
            setattr(self, k, v)

    def __getattr__(self, name):
        if name == 'initial':
            if isinstance(self._initial, CallableValue):
                return self._initial()
            return self._initial
        if name == 'hidden':
            return 0
        raise AttributeError, name

    def __repr__(self):
        return 'AttrMapValue(%s)' % (', ').join([ '%s=%r' % i for i in self.__dict__.iteritems() ])


class AttrMap(UserDict):

    def __init__(self, BASE=None, UNWANTED=[], **kw):
        data = {}
        if BASE:
            if isinstance(BASE, AttrMap):
                data = BASE.data
            else:
                if type(BASE) not in (type(()), type([])):
                    BASE = (BASE,)
                for B in BASE:
                    if hasattr(B, '_attrMap'):
                        data.update(getattr(B._attrMap, 'data', {}))
                    else:
                        raise ValueError, 'BASE=%s has wrong kind of value' % str(B)

        UserDict.__init__(self, data)
        self.remove(UNWANTED)
        self.data.update(kw)

    def update(self, kw):
        if isinstance(kw, AttrMap):
            kw = kw.data
        self.data.update(kw)

    def remove(self, unwanted):
        for k in unwanted:
            try:
                del self[k]
            except KeyError:
                pass

    def clone(self, UNWANTED=[], **kw):
        c = AttrMap(BASE=self, UNWANTED=UNWANTED)
        c.update(kw)
        return c


def validateSetattr(obj, name, value):
    """validate setattr(obj,name,value)"""
    if rl_config.shapeChecking:
        map = obj._attrMap
        if map and name[0] != '_':
            if isinstance(value, DerivedValue):
                pass
            else:
                try:
                    validate = map[name].validate
                    if not validate(value):
                        raise AttributeError, "Illegal assignment of '%s' to '%s' in class %s" % (value, name, obj.__class__.__name__)
                except KeyError:
                    raise AttributeError, "Illegal attribute '%s' in class %s" % (name, obj.__class__.__name__)

    obj.__dict__[name] = value


def _privateAttrMap(obj, ret=0):
    """clone obj._attrMap if required"""
    A = obj._attrMap
    oA = getattr(obj.__class__, '_attrMap', None)
    if ret:
        if oA is A:
            return (A.clone(), oA)
        else:
            return (
             A, None)

    elif oA is A:
        obj._attrMap = A.clone()
    return


def _findObjectAndAttr(src, P):
    """Locate the object src.P for P a string, return parent and name of attribute
    """
    P = string.split(P, '.')
    if len(P) == 0:
        return (None, None)
    else:
        for p in P[0:-1]:
            src = getattr(src, p)

        return (
         src, P[-1])
        return


def hook__setattr__(obj):
    if not hasattr(obj, '__attrproxy__'):
        C = obj.__class__
        import new
        obj.__class__ = new.classobj(C.__name__, (C,) + C.__bases__, {'__attrproxy__': [], '__setattr__': lambda self, k, v, osa=getattr(obj, '__setattr__', None), hook=hook: hook(self, k, v, osa)})
    return


def addProxyAttribute(src, name, validate=None, desc=None, initial=None, dst=None):
    """
    Add a proxy attribute 'name' to src with targets dst
    """
    assert hasattr(src, '_attrMap'), 'src object has no _attrMap'
    A, oA = _privateAttrMap(src, 1)
    if type(dst) not in _SequenceTypes:
        dst = (dst,)
    D = []
    DV = []
    for d in dst:
        if type(d) in _SequenceTypes:
            d, e = d[0], d[1:]
        obj, attr = _findObjectAndAttr(src, d)
        if obj:
            dA = getattr(obj, '_attrMap', None)

    return