# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\weave\swigptr.pyc
# Compiled at: 2013-03-29 22:51:36
from __future__ import absolute_import, print_function
swigptr_code = '\n\n/***********************************************************************\n * $Header$\n * swig_lib/python/python.cfg\n *\n * Contains variable linking and pointer type-checking code.\n ************************************************************************/\n\n#include <string.h>\n#include <stdlib.h>\n\n#ifdef __cplusplus\nextern "C" {\n#endif\n#include "Python.h"\n\n/* Definitions for Windows/Unix exporting */\n#if defined(_WIN32) || defined(__WIN32__)\n#   if defined(_MSC_VER)\n#       define SWIGEXPORT(a) __declspec(dllexport) a\n#   else\n#       if defined(__BORLANDC__)\n#           define SWIGEXPORT(a) a _export\n#       else\n#           define SWIGEXPORT(a) a\n#       endif\n#   endif\n#else\n#   define SWIGEXPORT(a) a\n#endif\n\n#ifdef SWIG_GLOBAL\n#define SWIGSTATICRUNTIME(a) SWIGEXPORT(a)\n#else\n#define SWIGSTATICRUNTIME(a) static a\n#endif\n\ntypedef struct {\n  char  *name;\n  PyObject *(*get_attr)(void);\n  int (*set_attr)(PyObject *);\n} swig_globalvar;\n\ntypedef struct swig_varlinkobject {\n  PyObject_HEAD\n  swig_globalvar **vars;\n  int      nvars;\n  int      maxvars;\n} swig_varlinkobject;\n\n/* ----------------------------------------------------------------------\n   swig_varlink_repr()\n\n   Function for python repr method\n   ---------------------------------------------------------------------- */\n\nstatic PyObject *\nswig_varlink_repr(swig_varlinkobject *v)\n{\n  v = v;\n  return PyString_FromString("<Global variables>");\n}\n\n/* ---------------------------------------------------------------------\n   swig_varlink_print()\n\n   Print out all of the global variable names\n   --------------------------------------------------------------------- */\n\nstatic int\nswig_varlink_print(swig_varlinkobject *v, FILE *fp, int flags)\n{\n\n  int i = 0;\n  flags = flags;\n  fprintf(fp,"Global variables { ");\n  while (v->vars[i]) {\n    fprintf(fp,"%s", v->vars[i]->name);\n    i++;\n    if (v->vars[i]) fprintf(fp,", ");\n  }\n  fprintf(fp," }\\n");\n  return 0;\n}\n\n/* --------------------------------------------------------------------\n   swig_varlink_getattr\n\n   This function gets the value of a variable and returns it as a\n   PyObject.   In our case, we\'ll be looking at the datatype and\n   converting into a number or string\n   -------------------------------------------------------------------- */\n\nstatic PyObject *\nswig_varlink_getattr(swig_varlinkobject *v, char *n)\n{\n  int i = 0;\n  char temp[128];\n\n  while (v->vars[i]) {\n    if (strcmp(v->vars[i]->name,n) == 0) {\n      return (*v->vars[i]->get_attr)();\n    }\n    i++;\n  }\n  sprintf(temp,"C global variable %s not found.", n);\n  PyErr_SetString(PyExc_NameError,temp);\n  return NULL;\n}\n\n/* -------------------------------------------------------------------\n   swig_varlink_setattr()\n\n   This function sets the value of a variable.\n   ------------------------------------------------------------------- */\n\nstatic int\nswig_varlink_setattr(swig_varlinkobject *v, char *n, PyObject *p)\n{\n  char temp[128];\n  int i = 0;\n  while (v->vars[i]) {\n    if (strcmp(v->vars[i]->name,n) == 0) {\n      return (*v->vars[i]->set_attr)(p);\n    }\n    i++;\n  }\n  sprintf(temp,"C global variable %s not found.", n);\n  PyErr_SetString(PyExc_NameError,temp);\n  return 1;\n}\n\nstatichere PyTypeObject varlinktype = {\n/*  PyObject_HEAD_INIT(&PyType_Type)  Note : This doesn\'t work on some machines */\n  PyObject_HEAD_INIT(0)\n  0,\n  "varlink",                          /* Type name    */\n  sizeof(swig_varlinkobject),         /* Basic size   */\n  0,                                  /* Itemsize     */\n  0,                                  /* Deallocator  */\n  (printfunc) swig_varlink_print,     /* Print        */\n  (getattrfunc) swig_varlink_getattr, /* get attr     */\n  (setattrfunc) swig_varlink_setattr, /* Set attr     */\n  0,                                  /* tp_compare   */\n  (reprfunc) swig_varlink_repr,       /* tp_repr      */\n  0,                                  /* tp_as_number */\n  0,                                  /* tp_as_mapping*/\n  0,                                  /* tp_hash      */\n};\n\n/* Create a variable linking object for use later */\n\nSWIGSTATICRUNTIME(PyObject *)\nSWIG_newvarlink(void)\n{\n  swig_varlinkobject *result = 0;\n  result = PyMem_NEW(swig_varlinkobject,1);\n  varlinktype.ob_type = &PyType_Type;    /* Patch varlinktype into a PyType */\n  result->ob_type = &varlinktype;\n  /*  _Py_NewReference(result);  Does not seem to be necessary */\n  result->nvars = 0;\n  result->maxvars = 64;\n  result->vars = (swig_globalvar **) malloc(64*sizeof(swig_globalvar *));\n  result->vars[0] = 0;\n  result->ob_refcnt = 0;\n  Py_XINCREF((PyObject *) result);\n  return ((PyObject*) result);\n}\n\nSWIGSTATICRUNTIME(void)\nSWIG_addvarlink(PyObject *p, char *name,\n           PyObject *(*get_attr)(void), int (*set_attr)(PyObject *p))\n{\n  swig_varlinkobject *v;\n  v= (swig_varlinkobject *) p;\n\n  if (v->nvars >= v->maxvars -1) {\n    v->maxvars = 2*v->maxvars;\n    v->vars = (swig_globalvar **) realloc(v->vars,v->maxvars*sizeof(swig_globalvar *));\n    if (v->vars == NULL) {\n      fprintf(stderr,"SWIG : Fatal error in initializing Python module.\\n");\n      exit(1);\n    }\n  }\n  v->vars[v->nvars] = (swig_globalvar *) malloc(sizeof(swig_globalvar));\n  v->vars[v->nvars]->name = (char *) malloc(strlen(name)+1);\n  strcpy(v->vars[v->nvars]->name,name);\n  v->vars[v->nvars]->get_attr = get_attr;\n  v->vars[v->nvars]->set_attr = set_attr;\n  v->nvars++;\n  v->vars[v->nvars] = 0;\n}\n\n/* -----------------------------------------------------------------------------\n * Pointer type-checking\n * ----------------------------------------------------------------------------- */\n\n/* SWIG pointer structure */\ntypedef struct SwigPtrType {\n  char               *name;               /* Datatype name                  */\n  int                 len;                /* Length (used for optimization) */\n  void               *(*cast)(void *);    /* Pointer casting function       */\n  struct SwigPtrType *next;               /* Linked list pointer            */\n} SwigPtrType;\n\n/* Pointer cache structure */\ntypedef struct {\n  int                 stat;               /* Status (valid) bit             */\n  SwigPtrType        *tp;                 /* Pointer to type structure      */\n  char                name[256];          /* Given datatype name            */\n  char                mapped[256];        /* Equivalent name                */\n} SwigCacheType;\n\nstatic int SwigPtrMax  = 64;           /* Max entries that can be currently held */\nstatic int SwigPtrN    = 0;            /* Current number of entries              */\nstatic int SwigPtrSort = 0;            /* Status flag indicating sort            */\nstatic int SwigStart[256];             /* Starting positions of types            */\nstatic SwigPtrType *SwigPtrTable = 0;  /* Table containing pointer equivalences  */\n\n/* Cached values */\n#define SWIG_CACHESIZE  8\n#define SWIG_CACHEMASK  0x7\nstatic SwigCacheType SwigCache[SWIG_CACHESIZE];\nstatic int SwigCacheIndex = 0;\nstatic int SwigLastCache = 0;\n\n/* Sort comparison function */\nstatic int swigsort(const void *data1, const void *data2) {\n        SwigPtrType *d1 = (SwigPtrType *) data1;\n        SwigPtrType *d2 = (SwigPtrType *) data2;\n        return strcmp(d1->name,d2->name);\n}\n\n/* Register a new datatype with the type-checker */\nSWIGSTATICRUNTIME(void)\nSWIG_RegisterMapping(char *origtype, char *newtype, void *(*cast)(void *)) {\n  int i;\n  SwigPtrType *t = 0,*t1;\n\n  /* Allocate the pointer table if necessary */\n  if (!SwigPtrTable) {\n    SwigPtrTable = (SwigPtrType *) malloc(SwigPtrMax*sizeof(SwigPtrType));\n  }\n\n  /* Grow the table */\n  if (SwigPtrN >= SwigPtrMax) {\n    SwigPtrMax = 2*SwigPtrMax;\n    SwigPtrTable = (SwigPtrType *) realloc((char *) SwigPtrTable,SwigPtrMax*sizeof(SwigPtrType));\n  }\n  for (i = 0; i < SwigPtrN; i++) {\n    if (strcmp(SwigPtrTable[i].name,origtype) == 0) {\n      t = &SwigPtrTable[i];\n      break;\n    }\n  }\n  if (!t) {\n    t = &SwigPtrTable[SwigPtrN++];\n    t->name = origtype;\n    t->len = strlen(t->name);\n    t->cast = 0;\n    t->next = 0;\n  }\n\n  /* Check for existing entries */\n  while (t->next) {\n    if ((strcmp(t->name,newtype) == 0)) {\n      if (cast) t->cast = cast;\n      return;\n    }\n    t = t->next;\n  }\n  t1 = (SwigPtrType *) malloc(sizeof(SwigPtrType));\n  t1->name = newtype;\n  t1->len = strlen(t1->name);\n  t1->cast = cast;\n  t1->next = 0;\n  t->next = t1;\n  SwigPtrSort = 0;\n}\n\n/* Make a pointer value string */\nSWIGSTATICRUNTIME(void)\nSWIG_MakePtr(char *c, const void *ptr, char *type) {\n  static char hex[17] = "0123456789abcdef";\n  unsigned long p, s;\n  char result[24], *r;\n  r = result;\n  p = (unsigned long) ptr;\n  if (p > 0) {\n    while (p > 0) {\n      s = p & 0xf;\n      *(r++) = hex[s];\n      p = p >> 4;\n    }\n    *r = \'_\';\n    while (r >= result)\n      *(c++) = *(r--);\n    strcpy (c, type);\n  } else {\n    strcpy (c, "NULL");\n  }\n}\n\n/* Function for getting a pointer value */\nSWIGSTATICRUNTIME(char *)\nSWIG_GetPtr(char *c, void **ptr, char *t)\n{\n  //std::cout << t << " " << c << std::endl;\n  unsigned long p;\n  char temp_type[256], *name;\n  int  i, len, start, end;\n  SwigPtrType *sp,*tp;\n  SwigCacheType *cache;\n  register int d;\n  p = 0;\n  /* Pointer values must start with leading underscore */\n  if (*c != \'_\') {\n    *ptr = (void *) 0;\n    if (strcmp(c,"NULL") == 0) return (char *) 0;\n    else c;\n  }\n  c++;\n  /* Extract hex value from pointer */\n  while (d = *c) {\n    if ((d >= \'0\') && (d <= \'9\'))\n      p = (p << 4) + (d - \'0\');\n    else if ((d >= \'a\') && (d <= \'f\'))\n      p = (p << 4) + (d - (\'a\'-10));\n    else\n      break;\n    c++;\n  }\n  *ptr = (void *) p;\n  //std::cout << t << " " << c << std::endl;\n  if ((!t) || (strcmp(t,c)==0))\n      return (char *) 0;\n  else\n  {\n      // added ej -- if type check fails, its always an error.\n      return (char*) 1;\n  }\n  if (!SwigPtrSort) {\n    qsort((void *) SwigPtrTable, SwigPtrN, sizeof(SwigPtrType), swigsort);\n    for (i = 0; i < 256; i++) SwigStart[i] = SwigPtrN;\n    for (i = SwigPtrN-1; i >= 0; i--) SwigStart[(int) (SwigPtrTable[i].name[1])] = i;\n    for (i = 255; i >= 1; i--) {\n      if (SwigStart[i-1] > SwigStart[i])\n        SwigStart[i-1] = SwigStart[i];\n    }\n    SwigPtrSort = 1;\n    for (i = 0; i < SWIG_CACHESIZE; i++) SwigCache[i].stat = 0;\n  }\n  /* First check cache for matches.  Uses last cache value as starting point */\n  cache = &SwigCache[SwigLastCache];\n  for (i = 0; i < SWIG_CACHESIZE; i++) {\n    if (cache->stat && (strcmp(t,cache->name) == 0) && (strcmp(c,cache->mapped) == 0)) {\n      cache->stat++;\n      if (cache->tp->cast) *ptr = (*(cache->tp->cast))(*ptr);\n      return (char *) 0;\n    }\n    SwigLastCache = (SwigLastCache+1) & SWIG_CACHEMASK;\n    if (!SwigLastCache) cache = SwigCache;\n    else cache++;\n  }\n  /* Type mismatch.  Look through type-mapping table */\n  start = SwigStart[(int) t[1]];\n  end = SwigStart[(int) t[1]+1];\n  sp = &SwigPtrTable[start];\n\n  /* Try to find a match */\n  while (start <= end) {\n    if (strncmp(t,sp->name,sp->len) == 0) {\n      name = sp->name;\n      len = sp->len;\n      tp = sp->next;\n      /* Try to find entry for our given datatype */\n      while(tp) {\n        if (tp->len >= 255) {\n          return c;\n        }\n        strcpy(temp_type,tp->name);\n        strncat(temp_type,t+len,255-tp->len);\n        if (strcmp(c,temp_type) == 0) {\n          strcpy(SwigCache[SwigCacheIndex].mapped,c);\n          strcpy(SwigCache[SwigCacheIndex].name,t);\n          SwigCache[SwigCacheIndex].stat = 1;\n          SwigCache[SwigCacheIndex].tp = tp;\n          SwigCacheIndex = SwigCacheIndex & SWIG_CACHEMASK;\n          /* Get pointer value */\n          *ptr = (void *) p;\n          if (tp->cast) *ptr = (*(tp->cast))(*ptr);\n          return (char *) 0;\n        }\n        tp = tp->next;\n      }\n    }\n    sp++;\n    start++;\n  }\n  return c;\n}\n\n/* New object-based GetPointer function. This uses the Python abstract\n * object interface to automatically dereference the \'this\' attribute\n * of shadow objects. */\n\nSWIGSTATICRUNTIME(char *)\nSWIG_GetPtrObj(PyObject *obj, void **ptr, char *type) {\n  PyObject *sobj = obj;\n  char     *str;\n  if (!PyString_Check(obj)) {\n    sobj = PyObject_GetAttrString(obj,"this");\n    if (!sobj) return "";\n  }\n  str = PyString_AsString(sobj);\n  //printf("str: %s\\n", str);\n  return SWIG_GetPtr(str,ptr,type);\n}\n\n#ifdef __cplusplus\n}\n#endif\n\n'