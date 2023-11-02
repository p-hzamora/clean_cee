# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: FuncDesigner\ooPoint.pyc
# Compiled at: 2013-05-17 20:50:10
from FDmisc import FuncDesignerException
from baseClasses import Stochastic
from numpy import asanyarray, ndarray, isscalar
try:
    from scipy.sparse import isspmatrix
except ImportError:
    isspmatrix = lambda *args, **kw: False

Len = --- This code section failed: ---

 L.  17         0  LOAD_GLOBAL           0  'isscalar'
                3  LOAD_FAST             0  'x'
                6  CALL_FUNCTION_1       1  None
                9  POP_JUMP_IF_FALSE    16  'to 16'
               12  LOAD_CONST               1
               15  RETURN_END_IF_LAMBDA
             16_0  COME_FROM             9  '9'
               16  LOAD_GLOBAL           1  'type'
               19  LOAD_FAST             0  'x'
               22  CALL_FUNCTION_1       1  None
               25  LOAD_GLOBAL           2  'ndarray'
               28  COMPARE_OP            2  ==
               31  POP_JUMP_IF_FALSE    41  'to 41'
               34  LOAD_FAST             0  'x'
               37  LOAD_ATTR             3  'size'
               40  RETURN_END_IF_LAMBDA
             41_0  COME_FROM            31  '31'
               41  LOAD_GLOBAL           4  'len'
               44  LOAD_FAST             0  'x'
               47  CALL_FUNCTION_1       1  None
               50  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `None' instruction at offset -1

def ooMultiPoint(*args, **kw):
    kw['skipArrayCast'] = True
    r = ooPoint(*args, **kw)
    r.isMultiPoint = True
    return r


class ooPoint(dict):
    _id = 0
    isMultiPoint = False
    modificationVar = None
    useSave = True
    useAsMutable = False
    exactRange = True
    surf_preference = False

    def __init__(self, *args, **kwargs):
        self.storedIntervals = {}
        self.storedSums = {}
        self.dictOfFixedFuncs = {}
        for fn in ('isMultiPoint', 'modificationVar', 'useSave', 'useAsMutable', 'maxDistributionSize',
                   'resolveSchedule'):
            tmp = kwargs.get(fn, None)
            if tmp is not None:
                setattr(self, fn, tmp)

        if kwargs.get('skipArrayCast', False):
            Asanyarray = lambda arg: arg
        else:
            Asanyarray = lambda arg: asanyarray(arg) if not isinstance(arg, Stochastic) else arg
        if args:
            if not isinstance(args[0], dict):
                items = [ (key, (isscalar(val) or Asanyarray)(val) if 1 else float(val) if type(val) == int else val) for key, val in args[0] ]
            else:
                items = [ (key, (isscalar(val) or Asanyarray)(val) if 1 else float(val) if type(val) == int else val) for key, val in args[0].items() ]
        elif kwargs:
            items = [ (key, (isscalar(val) or Asanyarray)(val) if 1 else float(val) if type(val) == int else val) for key, val in kwargs.items() ]
        else:
            raise FuncDesignerException('incorrect oopoint constructor arguments')
        dict.__init__(self, items)
        ooPoint._id += 1
        self._id = ooPoint._id
        return

    def __setitem__(self, *args, **kwargs):
        if not self.useAsMutable:
            raise FuncDesignerException('ooPoint must be immutable')
        dict.__setitem__(self, *args, **kwargs)