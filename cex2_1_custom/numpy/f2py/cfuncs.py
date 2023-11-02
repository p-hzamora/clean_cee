# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\f2py\cfuncs.pyc
# Compiled at: 2013-04-07 07:04:04
"""

C declarations, CPP macros, and C functions for f2py2e.
Only required declarations/macros/functions will be used.

Copyright 1999,2000 Pearu Peterson all rights reserved,
Pearu Peterson <pearu@ioc.ee>
Permission to use, modify, and distribute this software is given under the
terms of the NumPy License.

NO WARRANTY IS EXPRESSED OR IMPLIED.  USE AT YOUR OWN RISK.
$Date: 2005/05/06 11:42:34 $
Pearu Peterson
"""
__version__ = '$Revision: 1.75 $'[10:-1]
import __version__
f2py_version = __version__.version
import types, sys, copy
errmess = sys.stderr.write
outneeds = {'includes0': [], 'includes': [], 'typedefs': [], 'typedefs_generated': [], 'userincludes': [], 'cppmacros': [], 'cfuncs': [], 'callbacks': [], 'f90modhooks': [], 'commonhooks': []}
needs = {}
includes0 = {'includes0': '/*need_includes0*/'}
includes = {'includes': '/*need_includes*/'}
userincludes = {'userincludes': '/*need_userincludes*/'}
typedefs = {'typedefs': '/*need_typedefs*/'}
typedefs_generated = {'typedefs_generated': '/*need_typedefs_generated*/'}
cppmacros = {'cppmacros': '/*need_cppmacros*/'}
cfuncs = {'cfuncs': '/*need_cfuncs*/'}
callbacks = {'callbacks': '/*need_callbacks*/'}
f90modhooks = {'f90modhooks': '/*need_f90modhooks*/', 'initf90modhooksstatic': '/*initf90modhooksstatic*/', 
   'initf90modhooksdynamic': '/*initf90modhooksdynamic*/'}
commonhooks = {'commonhooks': '/*need_commonhooks*/', 'initcommonhooks': '/*need_initcommonhooks*/'}
includes0['math.h'] = '#include <math.h>'
includes0['string.h'] = '#include <string.h>'
includes0['setjmp.h'] = '#include <setjmp.h>'
includes['Python.h'] = '#include "Python.h"'
needs['arrayobject.h'] = ['Python.h']
includes['arrayobject.h'] = '#define PY_ARRAY_UNIQUE_SYMBOL PyArray_API\n#include "arrayobject.h"'
includes['arrayobject.h'] = '#include "fortranobject.h"'
includes['stdarg.h'] = '#include <stdarg.h>'
typedefs['unsigned_char'] = 'typedef unsigned char unsigned_char;'
typedefs['unsigned_short'] = 'typedef unsigned short unsigned_short;'
typedefs['unsigned_long'] = 'typedef unsigned long unsigned_long;'
typedefs['signed_char'] = 'typedef signed char signed_char;'
typedefs['long_long'] = '#ifdef _WIN32\ntypedef __int64 long_long;\n#else\ntypedef long long long_long;\ntypedef unsigned long long unsigned_long_long;\n#endif\n'
typedefs['insinged_long_long'] = '#ifdef _WIN32\ntypedef __uint64 long_long;\n#else\ntypedef unsigned long long unsigned_long_long;\n#endif\n'
typedefs['long_double'] = '#ifndef _LONG_DOUBLE\ntypedef long double long_double;\n#endif\n'
typedefs['complex_long_double'] = 'typedef struct {long double r,i;} complex_long_double;'
typedefs['complex_float'] = 'typedef struct {float r,i;} complex_float;'
typedefs['complex_double'] = 'typedef struct {double r,i;} complex_double;'
typedefs['string'] = 'typedef char * string;'
cppmacros['CFUNCSMESS'] = '#ifdef DEBUGCFUNCS\n#define CFUNCSMESS(mess) fprintf(stderr,"debug-capi:"mess);\n#define CFUNCSMESSPY(mess,obj) CFUNCSMESS(mess) \\\n\tPyObject_Print((PyObject *)obj,stderr,Py_PRINT_RAW);\\\n\tfprintf(stderr,"\\n");\n#else\n#define CFUNCSMESS(mess)\n#define CFUNCSMESSPY(mess,obj)\n#endif\n'
cppmacros['F_FUNC'] = '#if defined(PREPEND_FORTRAN)\n#if defined(NO_APPEND_FORTRAN)\n#if defined(UPPERCASE_FORTRAN)\n#define F_FUNC(f,F) _##F\n#else\n#define F_FUNC(f,F) _##f\n#endif\n#else\n#if defined(UPPERCASE_FORTRAN)\n#define F_FUNC(f,F) _##F##_\n#else\n#define F_FUNC(f,F) _##f##_\n#endif\n#endif\n#else\n#if defined(NO_APPEND_FORTRAN)\n#if defined(UPPERCASE_FORTRAN)\n#define F_FUNC(f,F) F\n#else\n#define F_FUNC(f,F) f\n#endif\n#else\n#if defined(UPPERCASE_FORTRAN)\n#define F_FUNC(f,F) F##_\n#else\n#define F_FUNC(f,F) f##_\n#endif\n#endif\n#endif\n#if defined(UNDERSCORE_G77)\n#define F_FUNC_US(f,F) F_FUNC(f##_,F##_)\n#else\n#define F_FUNC_US(f,F) F_FUNC(f,F)\n#endif\n'
cppmacros['F_WRAPPEDFUNC'] = '#if defined(PREPEND_FORTRAN)\n#if defined(NO_APPEND_FORTRAN)\n#if defined(UPPERCASE_FORTRAN)\n#define F_WRAPPEDFUNC(f,F) _F2PYWRAP##F\n#else\n#define F_WRAPPEDFUNC(f,F) _f2pywrap##f\n#endif\n#else\n#if defined(UPPERCASE_FORTRAN)\n#define F_WRAPPEDFUNC(f,F) _F2PYWRAP##F##_\n#else\n#define F_WRAPPEDFUNC(f,F) _f2pywrap##f##_\n#endif\n#endif\n#else\n#if defined(NO_APPEND_FORTRAN)\n#if defined(UPPERCASE_FORTRAN)\n#define F_WRAPPEDFUNC(f,F) F2PYWRAP##F\n#else\n#define F_WRAPPEDFUNC(f,F) f2pywrap##f\n#endif\n#else\n#if defined(UPPERCASE_FORTRAN)\n#define F_WRAPPEDFUNC(f,F) F2PYWRAP##F##_\n#else\n#define F_WRAPPEDFUNC(f,F) f2pywrap##f##_\n#endif\n#endif\n#endif\n#if defined(UNDERSCORE_G77)\n#define F_WRAPPEDFUNC_US(f,F) F_WRAPPEDFUNC(f##_,F##_)\n#else\n#define F_WRAPPEDFUNC_US(f,F) F_WRAPPEDFUNC(f,F)\n#endif\n'
cppmacros['F_MODFUNC'] = '#if defined(F90MOD2CCONV1) /*E.g. Compaq Fortran */\n#if defined(NO_APPEND_FORTRAN)\n#define F_MODFUNCNAME(m,f) $ ## m ## $ ## f\n#else\n#define F_MODFUNCNAME(m,f) $ ## m ## $ ## f ## _\n#endif\n#endif\n\n#if defined(F90MOD2CCONV2) /*E.g. IBM XL Fortran, not tested though */\n#if defined(NO_APPEND_FORTRAN)\n#define F_MODFUNCNAME(m,f)  __ ## m ## _MOD_ ## f\n#else\n#define F_MODFUNCNAME(m,f)  __ ## m ## _MOD_ ## f ## _\n#endif\n#endif\n\n#if defined(F90MOD2CCONV3) /*E.g. MIPSPro Compilers */\n#if defined(NO_APPEND_FORTRAN)\n#define F_MODFUNCNAME(m,f)  f ## .in. ## m\n#else\n#define F_MODFUNCNAME(m,f)  f ## .in. ## m ## _\n#endif\n#endif\n/*\n#if defined(UPPERCASE_FORTRAN)\n#define F_MODFUNC(m,M,f,F) F_MODFUNCNAME(M,F)\n#else\n#define F_MODFUNC(m,M,f,F) F_MODFUNCNAME(m,f)\n#endif\n*/\n\n#define F_MODFUNC(m,f) (*(f2pymodstruct##m##.##f))\n'
cppmacros['SWAPUNSAFE'] = '#define SWAP(a,b) (size_t)(a) = ((size_t)(a) ^ (size_t)(b));\\\n (size_t)(b) = ((size_t)(a) ^ (size_t)(b));\\\n (size_t)(a) = ((size_t)(a) ^ (size_t)(b))\n'
cppmacros['SWAP'] = '#define SWAP(a,b,t) {\\\n\tt *c;\\\n\tc = a;\\\n\ta = b;\\\n\tb = c;}\n'
cppmacros['PRINTPYOBJERR'] = '#define PRINTPYOBJERR(obj)\\\n\tfprintf(stderr,"#modulename#.error is related to ");\\\n\tPyObject_Print((PyObject *)obj,stderr,Py_PRINT_RAW);\\\n\tfprintf(stderr,"\\n");\n'
cppmacros['MINMAX'] = '#ifndef max\n#define max(a,b) ((a > b) ? (a) : (b))\n#endif\n#ifndef min\n#define min(a,b) ((a < b) ? (a) : (b))\n#endif\n#ifndef MAX\n#define MAX(a,b) ((a > b) ? (a) : (b))\n#endif\n#ifndef MIN\n#define MIN(a,b) ((a < b) ? (a) : (b))\n#endif\n'
needs['len..'] = ['f2py_size']
cppmacros['len..'] = '#define rank(var) var ## _Rank\n#define shape(var,dim) var ## _Dims[dim]\n#define old_rank(var) (((PyArrayObject *)(capi_ ## var ## _tmp))->nd)\n#define old_shape(var,dim) (((PyArrayObject *)(capi_ ## var ## _tmp))->dimensions[dim])\n#define fshape(var,dim) shape(var,rank(var)-dim-1)\n#define len(var) shape(var,0)\n#define flen(var) fshape(var,0)\n#define old_size(var) PyArray_SIZE((PyArrayObject *)(capi_ ## var ## _tmp))\n/* #define index(i) capi_i ## i */\n#define slen(var) capi_ ## var ## _len\n#define size(var, ...) f2py_size((PyArrayObject *)(capi_ ## var ## _tmp), ## __VA_ARGS__, -1)\n'
needs['f2py_size'] = ['stdarg.h']
cfuncs['f2py_size'] = 'static int f2py_size(PyArrayObject* var, ...)\n{\n  npy_int sz = 0;\n  npy_int dim;\n  npy_int rank;\n  va_list argp;\n  va_start(argp, var);\n  dim = va_arg(argp, npy_int);\n  if (dim==-1)\n    {\n      sz = PyArray_SIZE(var);\n    }\n  else\n    {\n      rank = PyArray_NDIM(var);\n      if (dim>=1 && dim<=rank)\n        sz = PyArray_DIM(var, dim-1);\n      else\n        fprintf(stderr, "f2py_size: 2nd argument value=%d fails to satisfy 1<=value<=%d. Result will be 0.\\n", dim, rank);\n    }\n  va_end(argp);\n  return sz;\n}\n'
cppmacros['pyobj_from_char1'] = '#define pyobj_from_char1(v) (PyInt_FromLong(v))'
cppmacros['pyobj_from_short1'] = '#define pyobj_from_short1(v) (PyInt_FromLong(v))'
needs['pyobj_from_int1'] = ['signed_char']
cppmacros['pyobj_from_int1'] = '#define pyobj_from_int1(v) (PyInt_FromLong(v))'
cppmacros['pyobj_from_long1'] = '#define pyobj_from_long1(v) (PyLong_FromLong(v))'
needs['pyobj_from_long_long1'] = ['long_long']
cppmacros['pyobj_from_long_long1'] = '#ifdef HAVE_LONG_LONG\n#define pyobj_from_long_long1(v) (PyLong_FromLongLong(v))\n#else\n#warning HAVE_LONG_LONG is not available. Redefining pyobj_from_long_long.\n#define pyobj_from_long_long1(v) (PyLong_FromLong(v))\n#endif\n'
needs['pyobj_from_long_double1'] = ['long_double']
cppmacros['pyobj_from_long_double1'] = '#define pyobj_from_long_double1(v) (PyFloat_FromDouble(v))'
cppmacros['pyobj_from_double1'] = '#define pyobj_from_double1(v) (PyFloat_FromDouble(v))'
cppmacros['pyobj_from_float1'] = '#define pyobj_from_float1(v) (PyFloat_FromDouble(v))'
needs['pyobj_from_complex_long_double1'] = ['complex_long_double']
cppmacros['pyobj_from_complex_long_double1'] = '#define pyobj_from_complex_long_double1(v) (PyComplex_FromDoubles(v.r,v.i))'
needs['pyobj_from_complex_double1'] = ['complex_double']
cppmacros['pyobj_from_complex_double1'] = '#define pyobj_from_complex_double1(v) (PyComplex_FromDoubles(v.r,v.i))'
needs['pyobj_from_complex_float1'] = ['complex_float']
cppmacros['pyobj_from_complex_float1'] = '#define pyobj_from_complex_float1(v) (PyComplex_FromDoubles(v.r,v.i))'
needs['pyobj_from_string1'] = ['string']
cppmacros['pyobj_from_string1'] = '#define pyobj_from_string1(v) (PyString_FromString((char *)v))'
needs['pyobj_from_string1size'] = ['string']
cppmacros['pyobj_from_string1size'] = '#define pyobj_from_string1size(v,len) (PyString_FromStringAndSize((char *)v, len))'
needs['TRYPYARRAYTEMPLATE'] = ['PRINTPYOBJERR']
cppmacros['TRYPYARRAYTEMPLATE'] = '/* New SciPy */\n#define TRYPYARRAYTEMPLATECHAR case NPY_STRING: *(char *)(arr->data)=*v; break;\n#define TRYPYARRAYTEMPLATELONG case NPY_LONG: *(long *)(arr->data)=*v; break;\n#define TRYPYARRAYTEMPLATEOBJECT case NPY_OBJECT: (arr->descr->f->setitem)(pyobj_from_ ## ctype ## 1(*v),arr->data); break;\n\n#define TRYPYARRAYTEMPLATE(ctype,typecode) \\\n        PyArrayObject *arr = NULL;\\\n        if (!obj) return -2;\\\n        if (!PyArray_Check(obj)) return -1;\\\n        if (!(arr=(PyArrayObject *)obj)) {fprintf(stderr,"TRYPYARRAYTEMPLATE:");PRINTPYOBJERR(obj);return 0;}\\\n        if (arr->descr->type==typecode)  {*(ctype *)(arr->data)=*v; return 1;}\\\n        switch (arr->descr->type_num) {\\\n                case NPY_DOUBLE: *(double *)(arr->data)=*v; break;\\\n                case NPY_INT: *(int *)(arr->data)=*v; break;\\\n                case NPY_LONG: *(long *)(arr->data)=*v; break;\\\n                case NPY_FLOAT: *(float *)(arr->data)=*v; break;\\\n                case NPY_CDOUBLE: *(double *)(arr->data)=*v; break;\\\n                case NPY_CFLOAT: *(float *)(arr->data)=*v; break;\\\n                case NPY_BOOL: *(npy_bool *)(arr->data)=(*v!=0); break;\\\n                case NPY_UBYTE: *(unsigned char *)(arr->data)=*v; break;\\\n                case NPY_BYTE: *(signed char *)(arr->data)=*v; break;\\\n                case NPY_SHORT: *(short *)(arr->data)=*v; break;\\\n                case NPY_USHORT: *(npy_ushort *)(arr->data)=*v; break;\\\n                case NPY_UINT: *(npy_uint *)(arr->data)=*v; break;\\\n                case NPY_ULONG: *(npy_ulong *)(arr->data)=*v; break;\\\n                case NPY_LONGLONG: *(npy_longlong *)(arr->data)=*v; break;\\\n                case NPY_ULONGLONG: *(npy_ulonglong *)(arr->data)=*v; break;\\\n                case NPY_LONGDOUBLE: *(npy_longdouble *)(arr->data)=*v; break;\\\n                case NPY_CLONGDOUBLE: *(npy_longdouble *)(arr->data)=*v; break;\\\n                case NPY_OBJECT: (arr->descr->f->setitem)(pyobj_from_ ## ctype ## 1(*v),arr->data, arr); break;\\\n        default: return -2;\\\n        };\\\n        return 1\n'
needs['TRYCOMPLEXPYARRAYTEMPLATE'] = [
 'PRINTPYOBJERR']
cppmacros['TRYCOMPLEXPYARRAYTEMPLATE'] = '#define TRYCOMPLEXPYARRAYTEMPLATEOBJECT case NPY_OBJECT: (arr->descr->f->setitem)(pyobj_from_complex_ ## ctype ## 1((*v)),arr->data, arr); break;\n#define TRYCOMPLEXPYARRAYTEMPLATE(ctype,typecode)\\\n        PyArrayObject *arr = NULL;\\\n        if (!obj) return -2;\\\n        if (!PyArray_Check(obj)) return -1;\\\n        if (!(arr=(PyArrayObject *)obj)) {fprintf(stderr,"TRYCOMPLEXPYARRAYTEMPLATE:");PRINTPYOBJERR(obj);return 0;}\\\n        if (arr->descr->type==typecode) {\\\n            *(ctype *)(arr->data)=(*v).r;\\\n            *(ctype *)(arr->data+sizeof(ctype))=(*v).i;\\\n            return 1;\\\n        }\\\n        switch (arr->descr->type_num) {\\\n                case NPY_CDOUBLE: *(double *)(arr->data)=(*v).r;*(double *)(arr->data+sizeof(double))=(*v).i;break;\\\n                case NPY_CFLOAT: *(float *)(arr->data)=(*v).r;*(float *)(arr->data+sizeof(float))=(*v).i;break;\\\n                case NPY_DOUBLE: *(double *)(arr->data)=(*v).r; break;\\\n                case NPY_LONG: *(long *)(arr->data)=(*v).r; break;\\\n                case NPY_FLOAT: *(float *)(arr->data)=(*v).r; break;\\\n                case NPY_INT: *(int *)(arr->data)=(*v).r; break;\\\n                case NPY_SHORT: *(short *)(arr->data)=(*v).r; break;\\\n                case NPY_UBYTE: *(unsigned char *)(arr->data)=(*v).r; break;\\\n                case NPY_BYTE: *(signed char *)(arr->data)=(*v).r; break;\\\n                case NPY_BOOL: *(npy_bool *)(arr->data)=((*v).r!=0 && (*v).i!=0); break;\\\n                case NPY_USHORT: *(npy_ushort *)(arr->data)=(*v).r; break;\\\n                case NPY_UINT: *(npy_uint *)(arr->data)=(*v).r; break;\\\n                case NPY_ULONG: *(npy_ulong *)(arr->data)=(*v).r; break;\\\n                case NPY_LONGLONG: *(npy_longlong *)(arr->data)=(*v).r; break;\\\n                case NPY_ULONGLONG: *(npy_ulonglong *)(arr->data)=(*v).r; break;\\\n                case NPY_LONGDOUBLE: *(npy_longdouble *)(arr->data)=(*v).r; break;\\\n                case NPY_CLONGDOUBLE: *(npy_longdouble *)(arr->data)=(*v).r;*(npy_longdouble *)(arr->data+sizeof(npy_longdouble))=(*v).i;break;\\\n                case NPY_OBJECT: (arr->descr->f->setitem)(pyobj_from_complex_ ## ctype ## 1((*v)),arr->data, arr); break;\\\n                default: return -2;\\\n        };\\\n        return -1;\n'
needs['GETSTRFROMPYTUPLE'] = [
 'STRINGCOPYN', 'PRINTPYOBJERR']
cppmacros['GETSTRFROMPYTUPLE'] = '#define GETSTRFROMPYTUPLE(tuple,index,str,len) {\\\n\t\tPyObject *rv_cb_str = PyTuple_GetItem((tuple),(index));\\\n\t\tif (rv_cb_str == NULL)\\\n\t\t\tgoto capi_fail;\\\n\t\tif (PyString_Check(rv_cb_str)) {\\\n\t\t\tstr[len-1]=\'\\0\';\\\n\t\t\tSTRINGCOPYN((str),PyString_AS_STRING((PyStringObject*)rv_cb_str),(len));\\\n\t\t} else {\\\n\t\t\tPRINTPYOBJERR(rv_cb_str);\\\n\t\t\tPyErr_SetString(#modulename#_error,"string object expected");\\\n\t\t\tgoto capi_fail;\\\n\t\t}\\\n\t}\n'
cppmacros['GETSCALARFROMPYTUPLE'] = '#define GETSCALARFROMPYTUPLE(tuple,index,var,ctype,mess) {\\\n\t\tif ((capi_tmp = PyTuple_GetItem((tuple),(index)))==NULL) goto capi_fail;\\\n\t\tif (!(ctype ## _from_pyobj((var),capi_tmp,mess)))\\\n\t\t\tgoto capi_fail;\\\n\t}\n'
cppmacros['FAILNULL'] = '\\\n#define FAILNULL(p) do {                                            \\\n    if ((p) == NULL) {                                              \\\n        PyErr_SetString(PyExc_MemoryError, "NULL pointer found");   \\\n        goto capi_fail;                                             \\\n    }                                                               \\\n} while (0)\n'
needs['MEMCOPY'] = ['string.h', 'FAILNULL']
cppmacros['MEMCOPY'] = '#define MEMCOPY(to,from,n)\\\n    do { FAILNULL(to); FAILNULL(from); (void)memcpy(to,from,n); } while (0)\n'
cppmacros['STRINGMALLOC'] = '#define STRINGMALLOC(str,len)\\\n\tif ((str = (string)malloc(sizeof(char)*(len+1))) == NULL) {\\\n\t\tPyErr_SetString(PyExc_MemoryError, "out of memory");\\\n\t\tgoto capi_fail;\\\n\t} else {\\\n\t\t(str)[len] = \'\\0\';\\\n\t}\n'
cppmacros['STRINGFREE'] = '#define STRINGFREE(str) do {if (!(str == NULL)) free(str);} while (0)\n'
needs['STRINGCOPYN'] = ['string.h', 'FAILNULL']
cppmacros['STRINGCOPYN'] = "#define STRINGCOPYN(to,from,buf_size)                           \\\n    do {                                                        \\\n        int _m = (buf_size);                                    \\\n        char *_to = (to);                                       \\\n        char *_from = (from);                                   \\\n        FAILNULL(_to); FAILNULL(_from);                         \\\n        (void)strncpy(_to, _from, sizeof(char)*_m);             \\\n        _to[_m-1] = '\\0';                                      \\\n        /* Padding with spaces instead of nulls */              \\\n        for (_m -= 2; _m >= 0 && _to[_m] == '\\0'; _m--) {      \\\n            _to[_m] = ' ';                                      \\\n        }                                                       \\\n    } while (0)\n"
needs['STRINGCOPY'] = ['string.h', 'FAILNULL']
cppmacros['STRINGCOPY'] = '#define STRINGCOPY(to,from)\\\n    do { FAILNULL(to); FAILNULL(from); (void)strcpy(to,from); } while (0)\n'
cppmacros['CHECKGENERIC'] = '#define CHECKGENERIC(check,tcheck,name) \\\n\tif (!(check)) {\\\n\t\tPyErr_SetString(#modulename#_error,"("tcheck") failed for "name);\\\n\t\t/*goto capi_fail;*/\\\n\t} else '
cppmacros['CHECKARRAY'] = '#define CHECKARRAY(check,tcheck,name) \\\n\tif (!(check)) {\\\n\t\tPyErr_SetString(#modulename#_error,"("tcheck") failed for "name);\\\n\t\t/*goto capi_fail;*/\\\n\t} else '
cppmacros['CHECKSTRING'] = '#define CHECKSTRING(check,tcheck,name,show,var)\\\n\tif (!(check)) {\\\n\t\tchar errstring[256];\\\n\t\tsprintf(errstring, "%s: "show, "("tcheck") failed for "name, slen(var), var);\\\n\t\tPyErr_SetString(#modulename#_error, errstring);\\\n\t\t/*goto capi_fail;*/\\\n\t} else '
cppmacros['CHECKSCALAR'] = '#define CHECKSCALAR(check,tcheck,name,show,var)\\\n\tif (!(check)) {\\\n\t\tchar errstring[256];\\\n\t\tsprintf(errstring, "%s: "show, "("tcheck") failed for "name, var);\\\n\t\tPyErr_SetString(#modulename#_error,errstring);\\\n\t\t/*goto capi_fail;*/\\\n\t} else '
cppmacros['ARRSIZE'] = '#define ARRSIZE(dims,rank) (_PyArray_multiply_list(dims,rank))'
cppmacros['OLDPYNUM'] = '#ifdef OLDPYNUM\n#error You need to intall Numeric Python version 13 or higher. Get it from http:/sourceforge.net/project/?group_id=1369\n#endif\n'
cfuncs['calcarrindex'] = 'static int calcarrindex(int *i,PyArrayObject *arr) {\n\tint k,ii = i[0];\n\tfor (k=1; k < arr->nd; k++)\n\t\tii += (ii*(arr->dimensions[k] - 1)+i[k]); /* assuming contiguous arr */\n\treturn ii;\n}'
cfuncs['calcarrindextr'] = 'static int calcarrindextr(int *i,PyArrayObject *arr) {\n\tint k,ii = i[arr->nd-1];\n\tfor (k=1; k < arr->nd; k++)\n\t\tii += (ii*(arr->dimensions[arr->nd-k-1] - 1)+i[arr->nd-k-1]); /* assuming contiguous arr */\n\treturn ii;\n}'
cfuncs['forcomb'] = 'static struct { int nd;npy_intp *d;int *i,*i_tr,tr; } forcombcache;\nstatic int initforcomb(npy_intp *dims,int nd,int tr) {\n  int k;\n  if (dims==NULL) return 0;\n  if (nd<0) return 0;\n  forcombcache.nd = nd;\n  forcombcache.d = dims;\n  forcombcache.tr = tr;\n  if ((forcombcache.i = (int *)malloc(sizeof(int)*nd))==NULL) return 0;\n  if ((forcombcache.i_tr = (int *)malloc(sizeof(int)*nd))==NULL) return 0;\n  for (k=1;k<nd;k++) {\n    forcombcache.i[k] = forcombcache.i_tr[nd-k-1] = 0;\n  }\n  forcombcache.i[0] = forcombcache.i_tr[nd-1] = -1;\n  return 1;\n}\nstatic int *nextforcomb(void) {\n  int j,*i,*i_tr,k;\n  int nd=forcombcache.nd;\n  if ((i=forcombcache.i) == NULL) return NULL;\n  if ((i_tr=forcombcache.i_tr) == NULL) return NULL;\n  if (forcombcache.d == NULL) return NULL;\n  i[0]++;\n  if (i[0]==forcombcache.d[0]) {\n    j=1;\n    while ((j<nd) && (i[j]==forcombcache.d[j]-1)) j++;\n    if (j==nd) {\n      free(i);\n      free(i_tr);\n      return NULL;\n    }\n    for (k=0;k<j;k++) i[k] = i_tr[nd-k-1] = 0;\n    i[j]++;\n    i_tr[nd-j-1]++;\n  } else\n    i_tr[nd-1]++;\n  if (forcombcache.tr) return i_tr;\n  return i;\n}'
needs['try_pyarr_from_string'] = ['STRINGCOPYN', 'PRINTPYOBJERR', 'string']
cfuncs['try_pyarr_from_string'] = 'static int try_pyarr_from_string(PyObject *obj,const string str) {\n\tPyArrayObject *arr = NULL;\n\tif (PyArray_Check(obj) && (!((arr = (PyArrayObject *)obj) == NULL)))\n\t\t{ STRINGCOPYN(arr->data,str,PyArray_NBYTES(arr)); }\n\treturn 1;\ncapi_fail:\n\tPRINTPYOBJERR(obj);\n\tPyErr_SetString(#modulename#_error,"try_pyarr_from_string failed");\n\treturn 0;\n}\n'
needs['string_from_pyobj'] = ['string', 'STRINGMALLOC', 'STRINGCOPYN']
cfuncs['string_from_pyobj'] = 'static int string_from_pyobj(string *str,int *len,const string inistr,PyObject *obj,const char *errmess) {\n\tPyArrayObject *arr = NULL;\n\tPyObject *tmp = NULL;\n#ifdef DEBUGCFUNCS\nfprintf(stderr,"string_from_pyobj(str=\'%s\',len=%d,inistr=\'%s\',obj=%p)\\n",(char*)str,*len,(char *)inistr,obj);\n#endif\n\tif (obj == Py_None) {\n\t\tif (*len == -1)\n\t\t\t*len = strlen(inistr); /* Will this cause problems? */\n\t\tSTRINGMALLOC(*str,*len);\n\t\tSTRINGCOPYN(*str,inistr,*len+1);\n\t\treturn 1;\n\t}\n\tif (PyArray_Check(obj)) {\n\t\tif ((arr = (PyArrayObject *)obj) == NULL)\n\t\t\tgoto capi_fail;\n\t\tif (!ISCONTIGUOUS(arr)) {\n\t\t\tPyErr_SetString(PyExc_ValueError,"array object is non-contiguous.");\n\t\t\tgoto capi_fail;\n\t\t}\n\t\tif (*len == -1)\n\t\t\t*len = (arr->descr->elsize)*PyArray_SIZE(arr);\n\t\tSTRINGMALLOC(*str,*len);\n\t\tSTRINGCOPYN(*str,arr->data,*len+1);\n\t\treturn 1;\n\t}\n\tif (PyString_Check(obj)) {\n\t\ttmp = obj;\n\t\tPy_INCREF(tmp);\n\t}\n#if PY_VERSION_HEX >= 0x03000000\n\telse if (PyUnicode_Check(obj)) {\n\t\ttmp = PyUnicode_AsASCIIString(obj);\n\t}\n\telse {\n\t\tPyObject *tmp2;\n\t\ttmp2 = PyObject_Str(obj);\n\t\tif (tmp2) {\n\t\t\ttmp = PyUnicode_AsASCIIString(tmp2);\n\t\t\tPy_DECREF(tmp2);\n\t\t}\n\t\telse {\n\t\t\ttmp = NULL;\n\t\t}\n\t}\n#else\n\telse {\n\t\ttmp = PyObject_Str(obj);\n\t}\n#endif\n\tif (tmp == NULL) goto capi_fail;\n\tif (*len == -1)\n\t\t*len = PyString_GET_SIZE(tmp);\n\tSTRINGMALLOC(*str,*len);\n\tSTRINGCOPYN(*str,PyString_AS_STRING(tmp),*len+1);\n\tPy_DECREF(tmp);\n\treturn 1;\ncapi_fail:\n\tPy_XDECREF(tmp);\n\t{\n\t\tPyObject* err = PyErr_Occurred();\n\t\tif (err==NULL) err = #modulename#_error;\n\t\tPyErr_SetString(err,errmess);\n\t}\n\treturn 0;\n}\n'
needs['char_from_pyobj'] = ['int_from_pyobj']
cfuncs['char_from_pyobj'] = 'static int char_from_pyobj(char* v,PyObject *obj,const char *errmess) {\n\tint i=0;\n\tif (int_from_pyobj(&i,obj,errmess)) {\n\t\t*v = (char)i;\n\t\treturn 1;\n\t}\n\treturn 0;\n}\n'
needs['signed_char_from_pyobj'] = ['int_from_pyobj', 'signed_char']
cfuncs['signed_char_from_pyobj'] = 'static int signed_char_from_pyobj(signed_char* v,PyObject *obj,const char *errmess) {\n\tint i=0;\n\tif (int_from_pyobj(&i,obj,errmess)) {\n\t\t*v = (signed_char)i;\n\t\treturn 1;\n\t}\n\treturn 0;\n}\n'
needs['short_from_pyobj'] = ['int_from_pyobj']
cfuncs['short_from_pyobj'] = 'static int short_from_pyobj(short* v,PyObject *obj,const char *errmess) {\n\tint i=0;\n\tif (int_from_pyobj(&i,obj,errmess)) {\n\t\t*v = (short)i;\n\t\treturn 1;\n\t}\n\treturn 0;\n}\n'
cfuncs['int_from_pyobj'] = 'static int int_from_pyobj(int* v,PyObject *obj,const char *errmess) {\n\tPyObject* tmp = NULL;\n\tif (PyInt_Check(obj)) {\n\t\t*v = (int)PyInt_AS_LONG(obj);\n\t\treturn 1;\n\t}\n\ttmp = PyNumber_Int(obj);\n\tif (tmp) {\n\t\t*v = PyInt_AS_LONG(tmp);\n\t\tPy_DECREF(tmp);\n\t\treturn 1;\n\t}\n\tif (PyComplex_Check(obj))\n\t\ttmp = PyObject_GetAttrString(obj,"real");\n\telse if (PyString_Check(obj) || PyUnicode_Check(obj))\n\t\t/*pass*/;\n\telse if (PySequence_Check(obj))\n\t\ttmp = PySequence_GetItem(obj,0);\n\tif (tmp) {\n\t\tPyErr_Clear();\n\t\tif (int_from_pyobj(v,tmp,errmess)) {Py_DECREF(tmp); return 1;}\n\t\tPy_DECREF(tmp);\n\t}\n\t{\n\t\tPyObject* err = PyErr_Occurred();\n\t\tif (err==NULL) err = #modulename#_error;\n\t\tPyErr_SetString(err,errmess);\n\t}\n\treturn 0;\n}\n'
cfuncs['long_from_pyobj'] = 'static int long_from_pyobj(long* v,PyObject *obj,const char *errmess) {\n\tPyObject* tmp = NULL;\n\tif (PyInt_Check(obj)) {\n\t\t*v = PyInt_AS_LONG(obj);\n\t\treturn 1;\n\t}\n\ttmp = PyNumber_Int(obj);\n\tif (tmp) {\n\t\t*v = PyInt_AS_LONG(tmp);\n\t\tPy_DECREF(tmp);\n\t\treturn 1;\n\t}\n\tif (PyComplex_Check(obj))\n\t\ttmp = PyObject_GetAttrString(obj,"real");\n\telse if (PyString_Check(obj) || PyUnicode_Check(obj))\n\t\t/*pass*/;\n\telse if (PySequence_Check(obj))\n\t\ttmp = PySequence_GetItem(obj,0);\n\tif (tmp) {\n\t\tPyErr_Clear();\n\t\tif (long_from_pyobj(v,tmp,errmess)) {Py_DECREF(tmp); return 1;}\n\t\tPy_DECREF(tmp);\n\t}\n\t{\n\t\tPyObject* err = PyErr_Occurred();\n\t\tif (err==NULL) err = #modulename#_error;\n\t\tPyErr_SetString(err,errmess);\n\t}\n\treturn 0;\n}\n'
needs['long_long_from_pyobj'] = ['long_long']
cfuncs['long_long_from_pyobj'] = 'static int long_long_from_pyobj(long_long* v,PyObject *obj,const char *errmess) {\n\tPyObject* tmp = NULL;\n\tif (PyLong_Check(obj)) {\n\t\t*v = PyLong_AsLongLong(obj);\n\t\treturn (!PyErr_Occurred());\n\t}\n\tif (PyInt_Check(obj)) {\n\t\t*v = (long_long)PyInt_AS_LONG(obj);\n\t\treturn 1;\n\t}\n\ttmp = PyNumber_Long(obj);\n\tif (tmp) {\n\t\t*v = PyLong_AsLongLong(tmp);\n\t\tPy_DECREF(tmp);\n\t\treturn (!PyErr_Occurred());\n\t}\n\tif (PyComplex_Check(obj))\n\t\ttmp = PyObject_GetAttrString(obj,"real");\n\telse if (PyString_Check(obj) || PyUnicode_Check(obj))\n\t\t/*pass*/;\n\telse if (PySequence_Check(obj))\n\t\ttmp = PySequence_GetItem(obj,0);\n\tif (tmp) {\n\t\tPyErr_Clear();\n\t\tif (long_long_from_pyobj(v,tmp,errmess)) {Py_DECREF(tmp); return 1;}\n\t\tPy_DECREF(tmp);\n\t}\n\t{\n\t\tPyObject* err = PyErr_Occurred();\n\t\tif (err==NULL) err = #modulename#_error;\n\t\tPyErr_SetString(err,errmess);\n\t}\n\treturn 0;\n}\n'
needs['long_double_from_pyobj'] = ['double_from_pyobj', 'long_double']
cfuncs['long_double_from_pyobj'] = 'static int long_double_from_pyobj(long_double* v,PyObject *obj,const char *errmess) {\n\tdouble d=0;\n\tif (PyArray_CheckScalar(obj)){\n\t\tif PyArray_IsScalar(obj, LongDouble) {\n\t\t\tPyArray_ScalarAsCtype(obj, v);\n\t\t\treturn 1;\n\t\t}\n\t\telse if (PyArray_Check(obj) && PyArray_TYPE(obj)==NPY_LONGDOUBLE) {\n\t\t\t(*v) = *((npy_longdouble *)PyArray_DATA(obj));\n\t\t\treturn 1;\n\t\t}\n\t}\n\tif (double_from_pyobj(&d,obj,errmess)) {\n\t\t*v = (long_double)d;\n\t\treturn 1;\n\t}\n\treturn 0;\n}\n'
cfuncs['double_from_pyobj'] = 'static int double_from_pyobj(double* v,PyObject *obj,const char *errmess) {\n\tPyObject* tmp = NULL;\n\tif (PyFloat_Check(obj)) {\n#ifdef __sgi\n\t\t*v = PyFloat_AsDouble(obj);\n#else\n\t\t*v = PyFloat_AS_DOUBLE(obj);\n#endif\n\t\treturn 1;\n\t}\n\ttmp = PyNumber_Float(obj);\n\tif (tmp) {\n#ifdef __sgi\n\t\t*v = PyFloat_AsDouble(tmp);\n#else\n\t\t*v = PyFloat_AS_DOUBLE(tmp);\n#endif\n\t\tPy_DECREF(tmp);\n\t\treturn 1;\n\t}\n\tif (PyComplex_Check(obj))\n\t\ttmp = PyObject_GetAttrString(obj,"real");\n\telse if (PyString_Check(obj) || PyUnicode_Check(obj))\n\t\t/*pass*/;\n\telse if (PySequence_Check(obj))\n\t\ttmp = PySequence_GetItem(obj,0);\n\tif (tmp) {\n\t\tPyErr_Clear();\n\t\tif (double_from_pyobj(v,tmp,errmess)) {Py_DECREF(tmp); return 1;}\n\t\tPy_DECREF(tmp);\n\t}\n\t{\n\t\tPyObject* err = PyErr_Occurred();\n\t\tif (err==NULL) err = #modulename#_error;\n\t\tPyErr_SetString(err,errmess);\n\t}\n\treturn 0;\n}\n'
needs['float_from_pyobj'] = ['double_from_pyobj']
cfuncs['float_from_pyobj'] = 'static int float_from_pyobj(float* v,PyObject *obj,const char *errmess) {\n\tdouble d=0.0;\n\tif (double_from_pyobj(&d,obj,errmess)) {\n\t\t*v = (float)d;\n\t\treturn 1;\n\t}\n\treturn 0;\n}\n'
needs['complex_long_double_from_pyobj'] = ['complex_long_double', 'long_double',
 'complex_double_from_pyobj']
cfuncs['complex_long_double_from_pyobj'] = 'static int complex_long_double_from_pyobj(complex_long_double* v,PyObject *obj,const char *errmess) {\n\tcomplex_double cd={0.0,0.0};\n\tif (PyArray_CheckScalar(obj)){\n\t\tif PyArray_IsScalar(obj, CLongDouble) {\n\t\t\tPyArray_ScalarAsCtype(obj, v);\n\t\t\treturn 1;\n\t\t}\n\t\telse if (PyArray_Check(obj) && PyArray_TYPE(obj)==NPY_CLONGDOUBLE) {\n\t\t\t(*v).r = ((npy_clongdouble *)PyArray_DATA(obj))->real;\n\t\t\t(*v).i = ((npy_clongdouble *)PyArray_DATA(obj))->imag;\n\t\t\treturn 1;\n\t\t}\n\t}\n\tif (complex_double_from_pyobj(&cd,obj,errmess)) {\n\t\t(*v).r = (long_double)cd.r;\n\t\t(*v).i = (long_double)cd.i;\n\t\treturn 1;\n\t}\n\treturn 0;\n}\n'
needs['complex_double_from_pyobj'] = ['complex_double']
cfuncs['complex_double_from_pyobj'] = 'static int complex_double_from_pyobj(complex_double* v,PyObject *obj,const char *errmess) {\n\tPy_complex c;\n\tif (PyComplex_Check(obj)) {\n\t\tc=PyComplex_AsCComplex(obj);\n\t\t(*v).r=c.real, (*v).i=c.imag;\n\t\treturn 1;\n\t}\n\tif (PyArray_IsScalar(obj, ComplexFloating)) {\n\t\tif (PyArray_IsScalar(obj, CFloat)) {\n\t\t\tnpy_cfloat new;\n\t\t\tPyArray_ScalarAsCtype(obj, &new);\n\t\t\t(*v).r = (double)new.real;\n\t\t\t(*v).i = (double)new.imag;\n\t\t}\n\t\telse if (PyArray_IsScalar(obj, CLongDouble)) {\n\t\t\tnpy_clongdouble new;\n\t\t\tPyArray_ScalarAsCtype(obj, &new);\n\t\t\t(*v).r = (double)new.real;\n\t\t\t(*v).i = (double)new.imag;\n\t\t}\n\t\telse { /* if (PyArray_IsScalar(obj, CDouble)) */\n\t\t\tPyArray_ScalarAsCtype(obj, v);\n\t\t}\n\t\treturn 1;\n\t}\n\tif (PyArray_CheckScalar(obj)) { /* 0-dim array or still array scalar */\n\t\tPyObject *arr;\n\t\tif (PyArray_Check(obj)) {\n\t\t\tarr = PyArray_Cast((PyArrayObject *)obj, NPY_CDOUBLE);\n\t\t}\n\t\telse {\n\t\t\tarr = PyArray_FromScalar(obj, PyArray_DescrFromType(NPY_CDOUBLE));\n\t\t}\n\t\tif (arr==NULL) return 0;\n\t\t(*v).r = ((npy_cdouble *)PyArray_DATA(arr))->real;\n\t\t(*v).i = ((npy_cdouble *)PyArray_DATA(arr))->imag;\n\t\treturn 1;\n\t}\n\t/* Python does not provide PyNumber_Complex function :-( */\n\t(*v).i=0.0;\n\tif (PyFloat_Check(obj)) {\n#ifdef __sgi\n\t\t(*v).r = PyFloat_AsDouble(obj);\n#else\n\t\t(*v).r = PyFloat_AS_DOUBLE(obj);\n#endif\n\t\treturn 1;\n\t}\n\tif (PyInt_Check(obj)) {\n\t\t(*v).r = (double)PyInt_AS_LONG(obj);\n\t\treturn 1;\n\t}\n\tif (PyLong_Check(obj)) {\n\t\t(*v).r = PyLong_AsDouble(obj);\n\t\treturn (!PyErr_Occurred());\n\t}\n\tif (PySequence_Check(obj) && !(PyString_Check(obj) || PyUnicode_Check(obj))) {\n\t\tPyObject *tmp = PySequence_GetItem(obj,0);\n\t\tif (tmp) {\n\t\t\tif (complex_double_from_pyobj(v,tmp,errmess)) {\n\t\t\t\tPy_DECREF(tmp);\n\t\t\t\treturn 1;\n\t\t\t}\n\t\t\tPy_DECREF(tmp);\n\t\t}\n\t}\n\t{\n\t\tPyObject* err = PyErr_Occurred();\n\t\tif (err==NULL)\n\t\t\terr = PyExc_TypeError;\n\t\tPyErr_SetString(err,errmess);\n\t}\n\treturn 0;\n}\n'
needs['complex_float_from_pyobj'] = ['complex_float', 'complex_double_from_pyobj']
cfuncs['complex_float_from_pyobj'] = 'static int complex_float_from_pyobj(complex_float* v,PyObject *obj,const char *errmess) {\n\tcomplex_double cd={0.0,0.0};\n\tif (complex_double_from_pyobj(&cd,obj,errmess)) {\n\t\t(*v).r = (float)cd.r;\n\t\t(*v).i = (float)cd.i;\n\t\treturn 1;\n\t}\n\treturn 0;\n}\n'
needs['try_pyarr_from_char'] = ['pyobj_from_char1', 'TRYPYARRAYTEMPLATE']
cfuncs['try_pyarr_from_char'] = "static int try_pyarr_from_char(PyObject* obj,char* v) {\n\tTRYPYARRAYTEMPLATE(char,'c');\n}\n"
needs['try_pyarr_from_signed_char'] = ['TRYPYARRAYTEMPLATE', 'unsigned_char']
cfuncs['try_pyarr_from_unsigned_char'] = "static int try_pyarr_from_unsigned_char(PyObject* obj,unsigned_char* v) {\n\tTRYPYARRAYTEMPLATE(unsigned_char,'b');\n}\n"
needs['try_pyarr_from_signed_char'] = ['TRYPYARRAYTEMPLATE', 'signed_char']
cfuncs['try_pyarr_from_signed_char'] = "static int try_pyarr_from_signed_char(PyObject* obj,signed_char* v) {\n\tTRYPYARRAYTEMPLATE(signed_char,'1');\n}\n"
needs['try_pyarr_from_short'] = ['pyobj_from_short1', 'TRYPYARRAYTEMPLATE']
cfuncs['try_pyarr_from_short'] = "static int try_pyarr_from_short(PyObject* obj,short* v) {\n\tTRYPYARRAYTEMPLATE(short,'s');\n}\n"
needs['try_pyarr_from_int'] = ['pyobj_from_int1', 'TRYPYARRAYTEMPLATE']
cfuncs['try_pyarr_from_int'] = "static int try_pyarr_from_int(PyObject* obj,int* v) {\n\tTRYPYARRAYTEMPLATE(int,'i');\n}\n"
needs['try_pyarr_from_long'] = ['pyobj_from_long1', 'TRYPYARRAYTEMPLATE']
cfuncs['try_pyarr_from_long'] = "static int try_pyarr_from_long(PyObject* obj,long* v) {\n\tTRYPYARRAYTEMPLATE(long,'l');\n}\n"
needs['try_pyarr_from_long_long'] = ['pyobj_from_long_long1', 'TRYPYARRAYTEMPLATE', 'long_long']
cfuncs['try_pyarr_from_long_long'] = "static int try_pyarr_from_long_long(PyObject* obj,long_long* v) {\n\tTRYPYARRAYTEMPLATE(long_long,'L');\n}\n"
needs['try_pyarr_from_float'] = ['pyobj_from_float1', 'TRYPYARRAYTEMPLATE']
cfuncs['try_pyarr_from_float'] = "static int try_pyarr_from_float(PyObject* obj,float* v) {\n\tTRYPYARRAYTEMPLATE(float,'f');\n}\n"
needs['try_pyarr_from_double'] = ['pyobj_from_double1', 'TRYPYARRAYTEMPLATE']
cfuncs['try_pyarr_from_double'] = "static int try_pyarr_from_double(PyObject* obj,double* v) {\n\tTRYPYARRAYTEMPLATE(double,'d');\n}\n"
needs['try_pyarr_from_complex_float'] = ['pyobj_from_complex_float1', 'TRYCOMPLEXPYARRAYTEMPLATE', 'complex_float']
cfuncs['try_pyarr_from_complex_float'] = "static int try_pyarr_from_complex_float(PyObject* obj,complex_float* v) {\n\tTRYCOMPLEXPYARRAYTEMPLATE(float,'F');\n}\n"
needs['try_pyarr_from_complex_double'] = ['pyobj_from_complex_double1', 'TRYCOMPLEXPYARRAYTEMPLATE', 'complex_double']
cfuncs['try_pyarr_from_complex_double'] = "static int try_pyarr_from_complex_double(PyObject* obj,complex_double* v) {\n\tTRYCOMPLEXPYARRAYTEMPLATE(double,'D');\n}\n"
needs['create_cb_arglist'] = [
 'CFUNCSMESS', 'PRINTPYOBJERR', 'MINMAX']
cfuncs['create_cb_arglist'] = 'static int create_cb_arglist(PyObject* fun,PyTupleObject* xa,const int maxnofargs,const int nofoptargs,int *nofargs,PyTupleObject **args,const char *errmess) {\n\tPyObject *tmp = NULL;\n\tPyObject *tmp_fun = NULL;\n\tint tot,opt,ext,siz,i,di=0;\n\tCFUNCSMESS("create_cb_arglist\\n");\n\ttot=opt=ext=siz=0;\n\t/* Get the total number of arguments */\n\tif (PyFunction_Check(fun))\n\t\ttmp_fun = fun;\n\telse {\n\t\tdi = 1;\n\t\tif (PyObject_HasAttrString(fun,"im_func")) {\n\t\t\ttmp_fun = PyObject_GetAttrString(fun,"im_func");\n\t\t}\n\t\telse if (PyObject_HasAttrString(fun,"__call__")) {\n\t\t\ttmp = PyObject_GetAttrString(fun,"__call__");\n\t\t\tif (PyObject_HasAttrString(tmp,"im_func"))\n\t\t\t\ttmp_fun = PyObject_GetAttrString(tmp,"im_func");\n\t\t\telse {\n\t\t\t\ttmp_fun = fun; /* built-in function */\n\t\t\t\ttot = maxnofargs;\n\t\t\t\tif (xa != NULL)\n\t\t\t\t\ttot += PyTuple_Size((PyObject *)xa);\n\t\t\t}\n\t\t\tPy_XDECREF(tmp);\n\t\t}\n\t\telse if (PyFortran_Check(fun) || PyFortran_Check1(fun)) {\n\t\t\ttot = maxnofargs;\n\t\t\tif (xa != NULL)\n\t\t\t\ttot += PyTuple_Size((PyObject *)xa);\n\t\t\ttmp_fun = fun;\n\t\t}\n\t\telse if (F2PyCapsule_Check(fun)) {\n\t\t\ttot = maxnofargs;\n\t\t\tif (xa != NULL)\n\t\t\t\text = PyTuple_Size((PyObject *)xa);\n\t\t\tif(ext>0) {\n\t\t\t\tfprintf(stderr,"extra arguments tuple cannot be used with CObject call-back\\n");\n\t\t\t\tgoto capi_fail;\n\t\t\t}\n\t\t\ttmp_fun = fun;\n\t\t}\n\t}\nif (tmp_fun==NULL) {\nfprintf(stderr,"Call-back argument must be function|instance|instance.__call__|f2py-function but got %s.\\n",(fun==NULL?"NULL":Py_TYPE(fun)->tp_name));\ngoto capi_fail;\n}\n#if PY_VERSION_HEX >= 0x03000000\n\tif (PyObject_HasAttrString(tmp_fun,"__code__")) {\n\t\tif (PyObject_HasAttrString(tmp = PyObject_GetAttrString(tmp_fun,"__code__"),"co_argcount"))\n#else\n\tif (PyObject_HasAttrString(tmp_fun,"func_code")) {\n\t\tif (PyObject_HasAttrString(tmp = PyObject_GetAttrString(tmp_fun,"func_code"),"co_argcount"))\n#endif\n\t\t\ttot = PyInt_AsLong(PyObject_GetAttrString(tmp,"co_argcount")) - di;\n\t\tPy_XDECREF(tmp);\n\t}\n\t/* Get the number of optional arguments */\n#if PY_VERSION_HEX >= 0x03000000\n\tif (PyObject_HasAttrString(tmp_fun,"__defaults__"))\n\t\tif (PyTuple_Check(tmp = PyObject_GetAttrString(tmp_fun,"__defaults__")))\n#else\n\tif (PyObject_HasAttrString(tmp_fun,"func_defaults"))\n\t\tif (PyTuple_Check(tmp = PyObject_GetAttrString(tmp_fun,"func_defaults")))\n#endif\n\t\t\topt = PyTuple_Size(tmp);\n\t\tPy_XDECREF(tmp);\n\t/* Get the number of extra arguments */\n\tif (xa != NULL)\n\t\text = PyTuple_Size((PyObject *)xa);\n\t/* Calculate the size of call-backs argument list */\n\tsiz = MIN(maxnofargs+ext,tot);\n\t*nofargs = MAX(0,siz-ext);\n#ifdef DEBUGCFUNCS\n\tfprintf(stderr,"debug-capi:create_cb_arglist:maxnofargs(-nofoptargs),tot,opt,ext,siz,nofargs=%d(-%d),%d,%d,%d,%d,%d\\n",maxnofargs,nofoptargs,tot,opt,ext,siz,*nofargs);\n#endif\n\tif (siz<tot-opt) {\n\t\tfprintf(stderr,"create_cb_arglist: Failed to build argument list (siz) with enough arguments (tot-opt) required by user-supplied function (siz,tot,opt=%d,%d,%d).\\n",siz,tot,opt);\n\t\tgoto capi_fail;\n\t}\n\t/* Initialize argument list */\n\t*args = (PyTupleObject *)PyTuple_New(siz);\n\tfor (i=0;i<*nofargs;i++) {\n\t\tPy_INCREF(Py_None);\n\t\tPyTuple_SET_ITEM((PyObject *)(*args),i,Py_None);\n\t}\n\tif (xa != NULL)\n\t\tfor (i=(*nofargs);i<siz;i++) {\n\t\t\ttmp = PyTuple_GetItem((PyObject *)xa,i-(*nofargs));\n\t\t\tPy_INCREF(tmp);\n\t\t\tPyTuple_SET_ITEM(*args,i,tmp);\n\t\t}\n\tCFUNCSMESS("create_cb_arglist-end\\n");\n\treturn 1;\ncapi_fail:\n\tif ((PyErr_Occurred())==NULL)\n\t\tPyErr_SetString(#modulename#_error,errmess);\n\treturn 0;\n}\n'

def buildcfuncs():
    from capi_maps import c2capi_map
    for k in c2capi_map.keys():
        m = 'pyarr_from_p_%s1' % k
        cppmacros[m] = '#define %s(v) (PyArray_SimpleNewFromData(0,NULL,%s,(char *)v))' % (m, c2capi_map[k])

    k = 'string'
    m = 'pyarr_from_p_%s1' % k
    cppmacros[m] = '#define %s(v,dims) (PyArray_SimpleNewFromData(1,dims,NPY_CHAR,(char *)v))' % m


def append_needs(need, flag=1):
    global needs
    global outneeds
    if type(need) == types.ListType:
        for n in need:
            append_needs(n, flag)

    elif type(need) == str:
        if not need:
            return
        if need in includes0:
            n = 'includes0'
        elif need in includes:
            n = 'includes'
        elif need in typedefs:
            n = 'typedefs'
        elif need in typedefs_generated:
            n = 'typedefs_generated'
        elif need in cppmacros:
            n = 'cppmacros'
        elif need in cfuncs:
            n = 'cfuncs'
        elif need in callbacks:
            n = 'callbacks'
        elif need in f90modhooks:
            n = 'f90modhooks'
        elif need in commonhooks:
            n = 'commonhooks'
        else:
            errmess('append_needs: unknown need %s\n' % `need`)
            return
        if need in outneeds[n]:
            return
        if flag:
            tmp = {}
            if need in needs:
                for nn in needs[need]:
                    t = append_needs(nn, 0)
                    if type(t) == types.DictType:
                        for nnn in t.keys():
                            if nnn in tmp:
                                tmp[nnn] = tmp[nnn] + t[nnn]
                            else:
                                tmp[nnn] = t[nnn]

            for nn in tmp.keys():
                for nnn in tmp[nn]:
                    if nnn not in outneeds[nn]:
                        outneeds[nn] = [
                         nnn] + outneeds[nn]

            outneeds[n].append(need)
        else:
            tmp = {}
            if need in needs:
                for nn in needs[need]:
                    t = append_needs(nn, flag)
                    if type(t) == types.DictType:
                        for nnn in t.keys():
                            if nnn in tmp:
                                tmp[nnn] = t[nnn] + tmp[nnn]
                            else:
                                tmp[nnn] = t[nnn]

            if n not in tmp:
                tmp[n] = []
            tmp[n].append(need)
            return tmp
    else:
        errmess('append_needs: expected list or string but got :%s\n' % `need`)


def get_needs():
    res = {}
    for n in outneeds.keys():
        out = []
        saveout = copy.copy(outneeds[n])
        while len(outneeds[n]) > 0:
            if outneeds[n][0] not in needs:
                out.append(outneeds[n][0])
                del outneeds[n][0]
            else:
                flag = 0
                for k in outneeds[n][1:]:
                    if k in needs[outneeds[n][0]]:
                        flag = 1
                        break

                if flag:
                    outneeds[n] = outneeds[n][1:] + [outneeds[n][0]]
                else:
                    out.append(outneeds[n][0])
                    del outneeds[n][0]
            if saveout and 0 not in map((lambda x, y: x == y), saveout, outneeds[n]) and outneeds[n] != []:
                print n, saveout
                errmess('get_needs: no progress in sorting needs, probably circular dependence, skipping.\n')
                out = out + saveout
                break
            saveout = copy.copy(outneeds[n])

        if out == []:
            out = [
             n]
        res[n] = out

    return res