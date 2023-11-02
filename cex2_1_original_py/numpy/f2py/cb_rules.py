# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\f2py\cb_rules.pyc
# Compiled at: 2013-04-07 07:04:04
"""

Build call-back mechanism for f2py2e.

Copyright 2000 Pearu Peterson all rights reserved,
Pearu Peterson <pearu@ioc.ee>
Permission to use, modify, and distribute this software is given under the
terms of the NumPy License.

NO WARRANTY IS EXPRESSED OR IMPLIED.  USE AT YOUR OWN RISK.
$Date: 2005/07/20 11:27:58 $
Pearu Peterson
"""
__version__ = '$Revision: 1.53 $'[10:-1]
import __version__
f2py_version = __version__.version
import pprint, sys, types
errmess = sys.stderr.write
outmess = sys.stdout.write
show = pprint.pprint
from ...auxfuncs import *
import cfuncs
cb_routine_rules = {'cbtypedefs': 'typedef #rctype#(*#name#_typedef)(#optargs_td##args_td##strarglens_td##noargs#);', 
   'body': '\n#begintitle#\nPyObject *#name#_capi = NULL;/*was Py_None*/\nPyTupleObject *#name#_args_capi = NULL;\nint #name#_nofargs = 0;\njmp_buf #name#_jmpbuf;\n/*typedef #rctype#(*#name#_typedef)(#optargs_td##args_td##strarglens_td##noargs#);*/\n#static# #rctype# #callbackname# (#optargs##args##strarglens##noargs#) {\n\tPyTupleObject *capi_arglist = #name#_args_capi;\n\tPyObject *capi_return = NULL;\n\tPyObject *capi_tmp = NULL;\n\tint capi_j,capi_i = 0;\n\tint capi_longjmp_ok = 1;\n#decl#\n#ifdef F2PY_REPORT_ATEXIT\nf2py_cb_start_clock();\n#endif\n\tCFUNCSMESS("cb:Call-back function #name# (maxnofargs=#maxnofargs#(-#nofoptargs#))\\n");\n\tCFUNCSMESSPY("cb:#name#_capi=",#name#_capi);\n\tif (#name#_capi==NULL) {\n\t\tcapi_longjmp_ok = 0;\n\t\t#name#_capi = PyObject_GetAttrString(#modulename#_module,"#argname#");\n\t}\n\tif (#name#_capi==NULL) {\n\t\tPyErr_SetString(#modulename#_error,"cb: Callback #argname# not defined (as an argument or module #modulename# attribute).\\n");\n\t\tgoto capi_fail;\n\t}\n\tif (F2PyCapsule_Check(#name#_capi)) {\n\t#name#_typedef #name#_cptr;\n\t#name#_cptr = F2PyCapsule_AsVoidPtr(#name#_capi);\n\t#returncptr#(*#name#_cptr)(#optargs_nm##args_nm##strarglens_nm#);\n\t#return#\n\t}\n\tif (capi_arglist==NULL) {\n\t\tcapi_longjmp_ok = 0;\n\t\tcapi_tmp = PyObject_GetAttrString(#modulename#_module,"#argname#_extra_args");\n\t\tif (capi_tmp) {\n\t\t\tcapi_arglist = (PyTupleObject *)PySequence_Tuple(capi_tmp);\n\t\t\tif (capi_arglist==NULL) {\n\t\t\t\tPyErr_SetString(#modulename#_error,"Failed to convert #modulename#.#argname#_extra_args to tuple.\\n");\n\t\t\t\tgoto capi_fail;\n\t\t\t}\n\t\t} else {\n\t\t\tPyErr_Clear();\n\t\t\tcapi_arglist = (PyTupleObject *)Py_BuildValue("()");\n\t\t}\n\t}\n\tif (capi_arglist == NULL) {\n\t\tPyErr_SetString(#modulename#_error,"Callback #argname# argument list is not set.\\n");\n\t\tgoto capi_fail;\n\t}\n#setdims#\n#pyobjfrom#\n\tCFUNCSMESSPY("cb:capi_arglist=",capi_arglist);\n\tCFUNCSMESS("cb:Call-back calling Python function #argname#.\\n");\n#ifdef F2PY_REPORT_ATEXIT\nf2py_cb_start_call_clock();\n#endif\n\tcapi_return = PyObject_CallObject(#name#_capi,(PyObject *)capi_arglist);\n#ifdef F2PY_REPORT_ATEXIT\nf2py_cb_stop_call_clock();\n#endif\n\tCFUNCSMESSPY("cb:capi_return=",capi_return);\n\tif (capi_return == NULL) {\n\t\tfprintf(stderr,"capi_return is NULL\\n");\n\t\tgoto capi_fail;\n\t}\n\tif (capi_return == Py_None) {\n\t\tPy_DECREF(capi_return);\n\t\tcapi_return = Py_BuildValue("()");\n\t}\n\telse if (!PyTuple_Check(capi_return)) {\n\t\tcapi_return = Py_BuildValue("(N)",capi_return);\n\t}\n\tcapi_j = PyTuple_Size(capi_return);\n\tcapi_i = 0;\n#frompyobj#\n\tCFUNCSMESS("cb:#name#:successful\\n");\n\tPy_DECREF(capi_return);\n#ifdef F2PY_REPORT_ATEXIT\nf2py_cb_stop_clock();\n#endif\n\tgoto capi_return_pt;\ncapi_fail:\n\tfprintf(stderr,"Call-back #name# failed.\\n");\n\tPy_XDECREF(capi_return);\n\tif (capi_longjmp_ok)\n\t\tlongjmp(#name#_jmpbuf,-1);\ncapi_return_pt:\n\t;\n#return#\n}\n#endtitle#\n', 
   'need': [
          'setjmp.h', 'CFUNCSMESS'], 
   'maxnofargs': '#maxnofargs#', 
   'nofoptargs': '#nofoptargs#', 
   'docstr': '\tdef #argname#(#docsignature#): return #docreturn#\\n\\\n#docstrsigns#', 
   'latexdocstr': '\n{{}\\verb@def #argname#(#latexdocsignature#): return #docreturn#@{}}\n#routnote#\n\n#latexdocstrsigns#', 
   'docstrshort': 'def #argname#(#docsignature#): return #docreturn#'}
cb_rout_rules = [
 {'separatorsfor': {'decl': '\n', 'args': ',', 
                      'optargs': '', 'pyobjfrom': '\n', 'freemem': '\n', 'args_td': ',', 
                      'optargs_td': '', 'args_nm': ',', 
                      'optargs_nm': '', 'frompyobj': '\n', 
                      'setdims': '\n', 'docstrsigns': '\\n"\n"', 
                      'latexdocstrsigns': '\n', 
                      'latexdocstrreq': '\n', 
                      'latexdocstropt': '\n', 'latexdocstrout': '\n', 
                      'latexdocstrcbs': '\n'}, 
    'decl': '/*decl*/', 
    'pyobjfrom': '/*pyobjfrom*/', 'frompyobj': '/*frompyobj*/', 'args': [], 'optargs': '', 'return': '', 'strarglens': '', 'freemem': '/*freemem*/', 'args_td': [], 'optargs_td': '', 'strarglens_td': '', 'args_nm': [], 'optargs_nm': '', 'strarglens_nm': '', 'noargs': '', 
    'setdims': '/*setdims*/', 
    'docstrsigns': '', 
    'latexdocstrsigns': '', 'docstrreq': '\tRequired arguments:', 
    'docstropt': '\tOptional arguments:', 
    'docstrout': '\tReturn objects:', 
    'docstrcbs': '\tCall-back functions:', 
    'docreturn': '', 
    'docsign': '', 'docsignopt': '', 'latexdocstrreq': '\\noindent Required arguments:', 
    'latexdocstropt': '\\noindent Optional arguments:', 
    'latexdocstrout': '\\noindent Return objects:', 
    'latexdocstrcbs': '\\noindent Call-back functions:', 
    'routnote': {hasnote: '--- #note#', l_not(hasnote): ''}},
 {'decl': '\t#ctype# return_value;', 
    'frompyobj': [{debugcapi: '\tCFUNCSMESS("cb:Getting return_value->");'},
                '\tif (capi_j>capi_i)\n\t\tGETSCALARFROMPYTUPLE(capi_return,capi_i++,&return_value,#ctype#,"#ctype#_from_pyobj failed in converting return_value of call-back function #name# to C #ctype#\\n");', {debugcapi: '\tfprintf(stderr,"#showvalueformat#.\\n",return_value);'}], 
    'need': [
           '#ctype#_from_pyobj', {debugcapi: 'CFUNCSMESS'}, 'GETSCALARFROMPYTUPLE'], 
    'return': '\treturn return_value;', 
    '_check': l_and(isfunction, l_not(isstringfunction), l_not(iscomplexfunction))},
 {'pyobjfrom': {debugcapi: '\tfprintf(stderr,"debug-capi:cb:#name#:%d:\\n",return_value_len);'}, 'args': '#ctype# return_value,int return_value_len', 
    'args_nm': 'return_value,&return_value_len', 
    'args_td': '#ctype# ,int', 
    'frompyobj': [{debugcapi: '\tCFUNCSMESS("cb:Getting return_value->\\"");'},
                '\tif (capi_j>capi_i)\n\t\tGETSTRFROMPYTUPLE(capi_return,capi_i++,return_value,return_value_len);', {debugcapi: '\tfprintf(stderr,"#showvalueformat#\\".\\n",return_value);'}], 
    'need': [
           '#ctype#_from_pyobj', {debugcapi: 'CFUNCSMESS'},
           'string.h', 'GETSTRFROMPYTUPLE'], 
    'return': 'return;', 
    '_check': isstringfunction},
 {'optargs': '\n#ifndef F2PY_CB_RETURNCOMPLEX\n#ctype# *return_value\n#endif\n', 
    'optargs_nm': '\n#ifndef F2PY_CB_RETURNCOMPLEX\nreturn_value\n#endif\n', 
    'optargs_td': '\n#ifndef F2PY_CB_RETURNCOMPLEX\n#ctype# *\n#endif\n', 
    'decl': '\n#ifdef F2PY_CB_RETURNCOMPLEX\n\t#ctype# return_value;\n#endif\n', 
    'frompyobj': [{debugcapi: '\tCFUNCSMESS("cb:Getting return_value->");'},
                '\tif (capi_j>capi_i)\n#ifdef F2PY_CB_RETURNCOMPLEX\n\t\tGETSCALARFROMPYTUPLE(capi_return,capi_i++,&return_value,#ctype#,"#ctype#_from_pyobj failed in converting return_value of call-back function #name# to C #ctype#\\n");\n#else\n\t\tGETSCALARFROMPYTUPLE(capi_return,capi_i++,return_value,#ctype#,"#ctype#_from_pyobj failed in converting return_value of call-back function #name# to C #ctype#\\n");\n#endif\n',
                {debugcapi: '\n#ifdef F2PY_CB_RETURNCOMPLEX\n\tfprintf(stderr,"#showvalueformat#.\\n",(return_value).r,(return_value).i);\n#else\n\tfprintf(stderr,"#showvalueformat#.\\n",(*return_value).r,(*return_value).i);\n#endif\n\n'}], 
    'return': '\n#ifdef F2PY_CB_RETURNCOMPLEX\n\treturn return_value;\n#else\n\treturn;\n#endif\n', 
    'need': [
           '#ctype#_from_pyobj', {debugcapi: 'CFUNCSMESS'},
           'string.h', 'GETSCALARFROMPYTUPLE', '#ctype#'], 
    '_check': iscomplexfunction},
 {'docstrout': '\t\t#pydocsignout#', 'latexdocstrout': [
                     '\\item[]{{}\\verb@#pydocsignout#@{}}', {hasnote: '--- #note#'}], 
    'docreturn': '#rname#,', 
    '_check': isfunction}, {'_check': issubroutine, 'return': 'return;'}]
cb_arg_rules = [
 {'docstropt': {l_and(isoptional, isintent_nothide): '\t\t#pydocsign#'}, 'docstrreq': {l_and(isrequired, isintent_nothide): '\t\t#pydocsign#'}, 'docstrout': {isintent_out: '\t\t#pydocsignout#'}, 'latexdocstropt': {l_and(isoptional, isintent_nothide): ['\\item[]{{}\\verb@#pydocsign#@{}}', {hasnote: '--- #note#'}]}, 'latexdocstrreq': {l_and(isrequired, isintent_nothide): ['\\item[]{{}\\verb@#pydocsign#@{}}', {hasnote: '--- #note#'}]}, 'latexdocstrout': {isintent_out: ['\\item[]{{}\\verb@#pydocsignout#@{}}',
                                    {l_and(hasnote, isintent_hide): '--- #note#', l_and(hasnote, isintent_nothide): '--- See above.'}]}, 
    'docsign': {l_and(isrequired, isintent_nothide): '#varname#,'}, 'docsignopt': {l_and(isoptional, isintent_nothide): '#varname#,'}, 'depend': ''},
 {'args': {l_and(isscalar, isintent_c): '#ctype# #varname_i#', 
             l_and(isscalar, l_not(isintent_c)): '#ctype# *#varname_i#_cb_capi', 
             isarray: '#ctype# *#varname_i#', 
             isstring: '#ctype# #varname_i#'}, 
    'args_nm': {l_and(isscalar, isintent_c): '#varname_i#', 
                l_and(isscalar, l_not(isintent_c)): '#varname_i#_cb_capi', 
                isarray: '#varname_i#', 
                isstring: '#varname_i#'}, 
    'args_td': {l_and(isscalar, isintent_c): '#ctype#', 
                l_and(isscalar, l_not(isintent_c)): '#ctype# *', 
                isarray: '#ctype# *', 
                isstring: '#ctype#'}, 
    'strarglens': {isstring: ',int #varname_i#_cb_len'}, 'strarglens_td': {isstring: ',int'}, 'strarglens_nm': {isstring: ',#varname_i#_cb_len'}},
 {'decl': {l_not(isintent_c): '\t#ctype# #varname_i#=(*#varname_i#_cb_capi);'}, 'error': {l_and(isintent_c, isintent_out, throw_error('intent(c,out) is forbidden for callback scalar arguments')): ''}, 
    'frompyobj': [{debugcapi: '\tCFUNCSMESS("cb:Getting #varname#->");'}, {isintent_out: '\tif (capi_j>capi_i)\n\t\tGETSCALARFROMPYTUPLE(capi_return,capi_i++,#varname_i#_cb_capi,#ctype#,"#ctype#_from_pyobj failed in converting argument #varname# of call-back function #name# to C #ctype#\\n");'}, {l_and(debugcapi, l_and(l_not(iscomplex), isintent_c)): '\tfprintf(stderr,"#showvalueformat#.\\n",#varname_i#);'}, {l_and(debugcapi, l_and(l_not(iscomplex), l_not(isintent_c))): '\tfprintf(stderr,"#showvalueformat#.\\n",*#varname_i#_cb_capi);'}, {l_and(debugcapi, l_and(iscomplex, isintent_c)): '\tfprintf(stderr,"#showvalueformat#.\\n",(#varname_i#).r,(#varname_i#).i);'}, {l_and(debugcapi, l_and(iscomplex, l_not(isintent_c))): '\tfprintf(stderr,"#showvalueformat#.\\n",(*#varname_i#_cb_capi).r,(*#varname_i#_cb_capi).i);'}], 'need': [{isintent_out: ['#ctype#_from_pyobj', 'GETSCALARFROMPYTUPLE']}, {debugcapi: 'CFUNCSMESS'}], '_check': isscalar},
 {'pyobjfrom': [
                {isintent_in: '\tif (#name#_nofargs>capi_i)\n\t\tif (PyTuple_SetItem((PyObject *)capi_arglist,capi_i++,pyobj_from_#ctype#1(#varname_i#)))\n\t\t\tgoto capi_fail;'},
                {isintent_inout: '\tif (#name#_nofargs>capi_i)\n\t\tif (PyTuple_SetItem((PyObject *)capi_arglist,capi_i++,pyarr_from_p_#ctype#1(#varname_i#_cb_capi)))\n\t\t\tgoto capi_fail;'}], 
    'need': [{isintent_in: 'pyobj_from_#ctype#1'}, {isintent_inout: 'pyarr_from_p_#ctype#1'}, {iscomplex: '#ctype#'}], '_check': l_and(isscalar, isintent_nothide), 
    '_optional': ''},
 {'frompyobj': [{debugcapi: '\tCFUNCSMESS("cb:Getting #varname#->\\"");'},
                '\tif (capi_j>capi_i)\n\t\tGETSTRFROMPYTUPLE(capi_return,capi_i++,#varname_i#,#varname_i#_cb_len);', {debugcapi: '\tfprintf(stderr,"#showvalueformat#\\":%d:.\\n",#varname_i#,#varname_i#_cb_len);'}], 
    'need': [
           '#ctype#', 'GETSTRFROMPYTUPLE', {debugcapi: 'CFUNCSMESS'}, 'string.h'], 
    '_check': l_and(isstring, isintent_out)},
 {'pyobjfrom': [{debugcapi: '\tfprintf(stderr,"debug-capi:cb:#varname#=\\"#showvalueformat#\\":%d:\\n",#varname_i#,#varname_i#_cb_len);'},
                {isintent_in: '\tif (#name#_nofargs>capi_i)\n\t\tif (PyTuple_SetItem((PyObject *)capi_arglist,capi_i++,pyobj_from_#ctype#1size(#varname_i#,#varname_i#_cb_len)))\n\t\t\tgoto capi_fail;'},
                {isintent_inout: '\tif (#name#_nofargs>capi_i) {\n\t\tint #varname_i#_cb_dims[] = {#varname_i#_cb_len};\n\t\tif (PyTuple_SetItem((PyObject *)capi_arglist,capi_i++,pyarr_from_p_#ctype#1(#varname_i#,#varname_i#_cb_dims)))\n\t\t\tgoto capi_fail;\n\t}'}], 
    'need': [{isintent_in: 'pyobj_from_#ctype#1size'}, {isintent_inout: 'pyarr_from_p_#ctype#1'}], '_check': l_and(isstring, isintent_nothide), 
    '_optional': ''},
 {'decl': '\tnpy_intp #varname_i#_Dims[#rank#] = {#rank*[-1]#};', 
    'setdims': '\t#cbsetdims#;', 
    '_check': isarray, 
    '_depend': ''},
 {'pyobjfrom': [{debugcapi: '\tfprintf(stderr,"debug-capi:cb:#varname#\\n");'},
                {isintent_c: '\tif (#name#_nofargs>capi_i) {\n\t\tPyArrayObject *tmp_arr = (PyArrayObject *)PyArray_New(&PyArray_Type,#rank#,#varname_i#_Dims,#atype#,NULL,(char*)#varname_i#,0,NPY_CARRAY,NULL); /*XXX: Hmm, what will destroy this array??? */\n', 
                   l_not(isintent_c): '\tif (#name#_nofargs>capi_i) {\n\t\tPyArrayObject *tmp_arr = (PyArrayObject *)PyArray_New(&PyArray_Type,#rank#,#varname_i#_Dims,#atype#,NULL,(char*)#varname_i#,0,NPY_FARRAY,NULL); /*XXX: Hmm, what will destroy this array??? */\n'},
                '\n\t\tif (tmp_arr==NULL)\n\t\t\tgoto capi_fail;\n\t\tif (PyTuple_SetItem((PyObject *)capi_arglist,capi_i++,(PyObject *)tmp_arr))\n\t\t\tgoto capi_fail;\n}'], 
    '_check': l_and(isarray, isintent_nothide, l_or(isintent_in, isintent_inout)), 
    '_optional': ''},
 {'frompyobj': [{debugcapi: '\tCFUNCSMESS("cb:Getting #varname#->");'},
                '\tif (capi_j>capi_i) {\n\t\tPyArrayObject *rv_cb_arr = NULL;\n\t\tif ((capi_tmp = PyTuple_GetItem(capi_return,capi_i++))==NULL) goto capi_fail;\n\t\trv_cb_arr =  array_from_pyobj(#atype#,#varname_i#_Dims,#rank#,F2PY_INTENT_IN', {isintent_c: '|F2PY_INTENT_C'},
                ',capi_tmp);\n\t\tif (rv_cb_arr == NULL) {\n\t\t\tfprintf(stderr,"rv_cb_arr is NULL\\n");\n\t\t\tgoto capi_fail;\n\t\t}\n\t\tMEMCOPY(#varname_i#,rv_cb_arr->data,PyArray_NBYTES(rv_cb_arr));\n\t\tif (capi_tmp != (PyObject *)rv_cb_arr) {\n\t\t\tPy_DECREF(rv_cb_arr);\n\t\t}\n\t}', {debugcapi: '\tfprintf(stderr,"<-.\\n");'}], 
    'need': [
           'MEMCOPY', {iscomplexarray: '#ctype#'}], 
    '_check': l_and(isarray, isintent_out)},
 {'docreturn': '#varname#,', 
    '_check': isintent_out}]
cb_map = {}

def buildcallbacks(m):
    global cb_map
    cb_map[m['name']] = []
    for bi in m['body']:
        if bi['block'] == 'interface':
            for b in bi['body']:
                if b:
                    buildcallback(b, m['name'])
                else:
                    errmess('warning: empty body for %s\n' % m['name'])


def buildcallback(rout, um):
    import capi_maps
    outmess('\tConstructing call-back function "cb_%s_in_%s"\n' % (rout['name'], um))
    args, depargs = getargs(rout)
    capi_maps.depargs = depargs
    var = rout['vars']
    vrd = capi_maps.cb_routsign2map(rout, um)
    rd = dictappend({}, vrd)
    cb_map[um].append([rout['name'], rd['name']])
    for r in cb_rout_rules:
        if '_check' in r and r['_check'](rout) or '_check' not in r:
            ar = applyrules(r, vrd, rout)
            rd = dictappend(rd, ar)

    savevrd = {}
    for i, a in enumerate(args):
        vrd = capi_maps.cb_sign2map(a, var[a], index=i)
        savevrd[a] = vrd
        for r in cb_arg_rules:
            if '_depend' in r:
                continue
            if '_optional' in r and isoptional(var[a]):
                continue
            if '_check' in r and r['_check'](var[a]) or '_check' not in r:
                ar = applyrules(r, vrd, var[a])
                rd = dictappend(rd, ar)
                if '_break' in r:
                    break

    for a in args:
        vrd = savevrd[a]
        for r in cb_arg_rules:
            if '_depend' in r:
                continue
            if '_optional' not in r or '_optional' in r and isrequired(var[a]):
                continue
            if '_check' in r and r['_check'](var[a]) or '_check' not in r:
                ar = applyrules(r, vrd, var[a])
                rd = dictappend(rd, ar)
                if '_break' in r:
                    break

    for a in depargs:
        vrd = savevrd[a]
        for r in cb_arg_rules:
            if '_depend' not in r:
                continue
            if '_optional' in r:
                continue
            if '_check' in r and r['_check'](var[a]) or '_check' not in r:
                ar = applyrules(r, vrd, var[a])
                rd = dictappend(rd, ar)
                if '_break' in r:
                    break

    if 'args' in rd and 'optargs' in rd:
        if type(rd['optargs']) == type([]):
            rd['optargs'] = rd['optargs'] + [
             '\n#ifndef F2PY_CB_RETURNCOMPLEX\n,\n#endif\n']
            rd['optargs_nm'] = rd['optargs_nm'] + [
             '\n#ifndef F2PY_CB_RETURNCOMPLEX\n,\n#endif\n']
            rd['optargs_td'] = rd['optargs_td'] + [
             '\n#ifndef F2PY_CB_RETURNCOMPLEX\n,\n#endif\n']
    if type(rd['docreturn']) == types.ListType:
        rd['docreturn'] = stripcomma(replace('#docreturn#', {'docreturn': rd['docreturn']}))
    optargs = stripcomma(replace('#docsignopt#', {'docsignopt': rd['docsignopt']}))
    if optargs == '':
        rd['docsignature'] = stripcomma(replace('#docsign#', {'docsign': rd['docsign']}))
    else:
        rd['docsignature'] = replace('#docsign#[#docsignopt#]', {'docsign': rd['docsign'], 'docsignopt': optargs})
    rd['latexdocsignature'] = rd['docsignature'].replace('_', '\\_')
    rd['latexdocsignature'] = rd['latexdocsignature'].replace(',', ', ')
    rd['docstrsigns'] = []
    rd['latexdocstrsigns'] = []
    for k in ['docstrreq', 'docstropt', 'docstrout', 'docstrcbs']:
        if k in rd and type(rd[k]) == types.ListType:
            rd['docstrsigns'] = rd['docstrsigns'] + rd[k]
        k = 'latex' + k
        if k in rd and type(rd[k]) == types.ListType:
            rd['latexdocstrsigns'] = rd['latexdocstrsigns'] + rd[k][0:1] + ['\\begin{description}'] + rd[k][1:] + [
             '\\end{description}']

    if 'args' not in rd:
        rd['args'] = ''
        rd['args_td'] = ''
        rd['args_nm'] = ''
    if not (rd.get('args') or rd.get('optargs') or rd.get('strarglens')):
        rd['noargs'] = 'void'
    ar = applyrules(cb_routine_rules, rd)
    cfuncs.callbacks[rd['name']] = ar['body']
    if type(ar['need']) == str:
        ar['need'] = [
         ar['need']]
    if 'need' in rd:
        for t in cfuncs.typedefs.keys():
            if t in rd['need']:
                ar['need'].append(t)

    cfuncs.typedefs_generated[rd['name'] + '_typedef'] = ar['cbtypedefs']
    ar['need'].append(rd['name'] + '_typedef')
    cfuncs.needs[rd['name']] = ar['need']
    capi_maps.lcb2_map[rd['name']] = {'maxnofargs': ar['maxnofargs'], 'nofoptargs': ar['nofoptargs'], 
       'docstr': ar['docstr'], 
       'latexdocstr': ar['latexdocstr'], 
       'argname': rd['argname']}
    outmess('\t  %s\n' % ar['docstrshort'])