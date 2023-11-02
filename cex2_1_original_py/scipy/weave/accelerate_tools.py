# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\weave\accelerate_tools.pyc
# Compiled at: 2013-03-29 22:51:36
"""
accelerate_tools contains the interface for on-the-fly building of
C++ equivalents to Python functions.
"""
from __future__ import absolute_import, print_function
from types import InstanceType, XRangeType
import inspect, scipy.weave.md5_load as md5, scipy.weave as weave
from numpy.testing import assert_
from .bytecodecompiler import CXXCoder, Type_Descriptor, Function_Descriptor

def CStr(s):
    """Hacky way to get legal C string from Python string"""
    if s is None:
        return '""'
    else:
        assert_(isinstance(s, str), msg='only None and string allowed')
        r = repr('"' + s)
        return '"' + r[2:-1] + '"'


class Instance(Type_Descriptor):
    cxxtype = 'PyObject*'

    def __init__(self, prototype):
        self.prototype = prototype

    def check(self, s):
        return 'PyInstance_Check(%s)' % s

    def inbound(self, s):
        return s

    def outbound(self, s):
        return (
         s, 0)

    def get_attribute(self, name):
        proto = getattr(self.prototype, name)
        T = lookup_type(proto)
        code = 'tempPY = PyObject_GetAttrString(%%(rhs)s,"%s");\n' % name
        convert = T.inbound('tempPY')
        code += '%%(lhsType)s %%(lhs)s = %s;\n' % convert
        return (T, code)

    def set_attribute(self, name):
        proto = getattr(self.prototype, name)
        T = lookup_type(proto)
        convert, owned = T.outbound('%(rhs)s')
        code = 'tempPY = %s;' % convert
        if not owned:
            code += ' Py_INCREF(tempPY);'
        code += ' PyObject_SetAttrString(%%(lhs)s,"%s",tempPY);' % name
        code += ' Py_DECREF(tempPY);\n'
        return (T, code)


class Basic(Type_Descriptor):
    owned = 1

    def check(self, s):
        return '%s(%s)' % (self.checker, s)

    def inbound(self, s):
        return '%s(%s)' % (self.inbounder, s)

    def outbound(self, s):
        return ('%s(%s)' % (self.outbounder, s), self.owned)


class Basic_Number(Basic):

    def literalizer(self, s):
        return str(s)

    def binop(self, symbol, a, b):
        assert_(symbol in ('+', '-', '*', '/'), msg=symbol)
        return ('%s %s %s' % (a, symbol, b), self)


class Integer(Basic_Number):
    cxxtype = 'long'
    checker = 'PyInt_Check'
    inbounder = 'PyInt_AsLong'
    outbounder = 'PyInt_FromLong'


class Double(Basic_Number):
    cxxtype = 'double'
    checker = 'PyFloat_Check'
    inbounder = 'PyFloat_AsDouble'
    outbounder = 'PyFloat_FromDouble'


class String(Basic):
    cxxtype = 'char*'
    checker = 'PyString_Check'
    inbounder = 'PyString_AsString'
    outbounder = 'PyString_FromString'

    def literalizer(self, s):
        return CStr(s)


Integer = Integer()
Double = Double()
String = String()
import numpy as np

class Vector(Type_Descriptor):
    cxxtype = 'PyArrayObject*'
    refcount = 1
    dims = 1
    module_init_code = 'import_array();\n'
    inbounder = '(PyArrayObject*)'
    outbounder = '(PyObject*)'
    owned = 0
    prerequisites = Type_Descriptor.prerequisites + [
     '#include "numpy/arrayobject.h"']
    dims = 1

    def check(self, s):
        return 'PyArray_Check(%s) && ((PyArrayObject*)%s)->nd == %d &&  ((PyArrayObject*)%s)->descr->type_num == %s' % (
         s, s, self.dims, s, self.typecode)

    def inbound(self, s):
        return '%s(%s)' % (self.inbounder, s)

    def outbound(self, s):
        return ('%s(%s)' % (self.outbounder, s), self.owned)

    def getitem(self, A, v, t):
        assert_(self.dims == len(v), msg='Expect dimension %d' % self.dims)
        code = '*((%s*)(%s->data' % (self.cxxbase, A)
        for i in range(self.dims):
            code += '+%s*%s->strides[%d]' % (v[i], A, i)

        code += '))'
        return (code, self.pybase)

    def setitem(self, A, v, t):
        return self.getitem(A, v, t)


class matrix(Vector):
    dims = 2


class IntegerVector(Vector):
    typecode = 'PyArray_INT'
    cxxbase = 'int'
    pybase = Integer


class Integermatrix(matrix):
    typecode = 'PyArray_INT'
    cxxbase = 'int'
    pybase = Integer


class LongVector(Vector):
    typecode = 'PyArray_LONG'
    cxxbase = 'long'
    pybase = Integer


class Longmatrix(matrix):
    typecode = 'PyArray_LONG'
    cxxbase = 'long'
    pybase = Integer


class DoubleVector(Vector):
    typecode = 'PyArray_DOUBLE'
    cxxbase = 'double'
    pybase = Double


class Doublematrix(matrix):
    typecode = 'PyArray_DOUBLE'
    cxxbase = 'double'
    pybase = Double


class XRange(Type_Descriptor):
    cxxtype = 'XRange'
    prerequisites = [
     '\n    class XRange {\n    public:\n    XRange(long aLow, long aHigh, long aStep=1)\n    : low(aLow),high(aHigh),step(aStep)\n    {\n    }\n    XRange(long aHigh)\n    : low(0),high(aHigh),step(1)\n    {\n    }\n    long low;\n    long high;\n    long step;\n    };']


IntegerVector = IntegerVector()
Integermatrix = Integermatrix()
LongVector = LongVector()
Longmatrix = Longmatrix()
DoubleVector = DoubleVector()
Doublematrix = Doublematrix()
XRange = XRange()
typedefs = {int: Integer, 
   float: Double, 
   str: String, 
   (np.ndarray, 1, int): IntegerVector, 
   (np.ndarray, 2, int): Integermatrix, 
   (np.ndarray, 1, np.long): LongVector, 
   (np.ndarray, 2, np.long): Longmatrix, 
   (np.ndarray, 1, float): DoubleVector, 
   (np.ndarray, 2, float): Doublematrix, 
   XRangeType: XRange}
import math
functiondefs = {(len, (String,)): Function_Descriptor(code='strlen(%s)', return_type=Integer), 
   (len, (LongVector,)): Function_Descriptor(code='PyArray_Size((PyObject*)%s)', return_type=Integer), 
   (float, (Integer,)): Function_Descriptor(code='(double)(%s)', return_type=Double), 
   (range, (Integer, Integer)): Function_Descriptor(code='XRange(%s)', return_type=XRange), 
   (range, Integer): Function_Descriptor(code='XRange(%s)', return_type=XRange), 
   (math.sin, (Double,)): Function_Descriptor(code='sin(%s)', return_type=Double), 
   (math.cos, (Double,)): Function_Descriptor(code='cos(%s)', return_type=Double), 
   (math.sqrt, (Double,)): Function_Descriptor(code='sqrt(%s)', return_type=Double)}

def lookup_type(x):
    T = type(x)
    try:
        return typedefs[T]
    except:
        if isinstance(T, np.ndarray):
            return typedefs[(T, len(x.shape), x.dtype.char)]
        if issubclass(T, InstanceType):
            return Instance(x)
        raise NotImplementedError(T)


class accelerate(object):

    def __init__(self, function, *args, **kw):
        assert_(inspect.isfunction(function))
        self.function = function
        self.module = inspect.getmodule(function)
        if self.module is None:
            import __main__
            self.module = __main__
        self.__call_map = {}
        return

    def __cache(self, *args):
        raise TypeError

    def __call__(self, *args):
        try:
            return self.__cache(*args)
        except TypeError:
            signature = tuple(map(lookup_type, args))
            try:
                fast = self.__call_map[signature]
            except:
                fast = self.singleton(signature)
                self.__cache = fast
                self.__call_map[signature] = fast

            return fast(*args)

    def signature(self, *args):
        signature = tuple(map(lookup_type, args))
        return self.singleton(signature)

    def singleton(self, signature):
        identifier = self.identifier(signature)
        f = self.function
        try:
            print('lookup', self.module.__name__ + '_weave')
            accelerated_module = __import__(self.module.__name__ + '_weave')
            print('have accelerated', self.module.__name__ + '_weave')
            fast = getattr(accelerated_module, identifier)
            return fast
        except ImportError:
            accelerated_module = None
        except AttributeError:
            pass

        P = self.accelerate(signature, identifier)
        E = weave.ext_tools.ext_module(self.module.__name__ + '_weave')
        E.add_function(P)
        E.generate_file()
        weave.build_tools.build_extension(self.module.__name__ + '_weave.cpp', verbose=2)
        if accelerated_module:
            raise NotImplementedError('Reload')
        else:
            accelerated_module = __import__(self.module.__name__ + '_weave')
        fast = getattr(accelerated_module, identifier)
        return fast

    def identifier(self, signature):
        f = self.function
        co = f.func_code
        identifier = str(signature) + str(co.co_argcount) + str(co.co_consts) + str(co.co_varnames) + co.co_code
        return 'F' + md5.md5(identifier).hexdigest()

    def accelerate(self, signature, identifier):
        P = Python2CXX(self.function, signature, name=identifier)
        return P

    def code(self, *args):
        if len(args) != self.function.func_code.co_argcount:
            raise TypeError('%s() takes exactly %d arguments (%d given)' % (
             self.function.__name__,
             self.function.func_code.co_argcount,
             len(args)))
        signature = tuple(map(lookup_type, args))
        ident = self.function.__name__
        return self.accelerate(signature, ident).function_code()


class Python2CXX(CXXCoder):

    def typedef_by_value(self, v):
        T = lookup_type(v)
        if T not in self.used:
            self.used.append(T)
        return T

    def function_by_signature(self, signature):
        descriptor = functiondefs[signature]
        if descriptor.return_type not in self.used:
            self.used.append(descriptor.return_type)
        return descriptor

    def __init__(self, f, signature, name=None):
        assert_(inspect.isfunction(f))
        assert_(reduce((lambda x, y: x and y), map((lambda x: isinstance(x, Type_Descriptor)), signature), 1), msg='%s not all type objects' % signature)
        self.arg_specs = []
        self.customize = weave.base_info.custom_info()
        CXXCoder.__init__(self, f, signature, name)

    def function_code(self):
        code = self.wrapped_code()
        for T in self.used:
            if T is not None and T.module_init_code:
                self.customize.add_module_init_code(T.module_init_code)

        return code

    def python_function_definition_code(self):
        return '{ "%s", wrapper_%s, METH_VARARGS, %s },\n' % (
         self.name,
         self.name,
         CStr(self.function.__doc__))