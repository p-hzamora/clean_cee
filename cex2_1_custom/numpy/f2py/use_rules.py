# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\f2py\use_rules.pyc
# Compiled at: 2013-04-07 07:04:04
"""

Build 'use others module data' mechanism for f2py2e.

Unfinished.

Copyright 2000 Pearu Peterson all rights reserved,
Pearu Peterson <pearu@ioc.ee>
Permission to use, modify, and distribute this software is given under the
terms of the NumPy License.

NO WARRANTY IS EXPRESSED OR IMPLIED.  USE AT YOUR OWN RISK.
$Date: 2000/09/10 12:35:43 $
Pearu Peterson
"""
__version__ = '$Revision: 1.3 $'[10:-1]
f2py_version = 'See `f2py -v`'
import pprint, sys
errmess = sys.stderr.write
outmess = sys.stdout.write
show = pprint.pprint
from ...auxfuncs import *
usemodule_rules = {'body': '\n#begintitle#\nstatic char doc_#apiname#[] = "\\\nVariable wrapper signature:\\n\\\n\t #name# = get_#name#()\\n\\\nArguments:\\n\\\n#docstr#";\nextern F_MODFUNC(#usemodulename#,#USEMODULENAME#,#realname#,#REALNAME#);\nstatic PyObject *#apiname#(PyObject *capi_self, PyObject *capi_args) {\n/*#decl#*/\n\tif (!PyArg_ParseTuple(capi_args, "")) goto capi_fail;\nprintf("c: %d\\n",F_MODFUNC(#usemodulename#,#USEMODULENAME#,#realname#,#REALNAME#));\n\treturn Py_BuildValue("");\ncapi_fail:\n\treturn NULL;\n}\n', 
   'method': '\t{"get_#name#",#apiname#,METH_VARARGS|METH_KEYWORDS,doc_#apiname#},', 
   'need': [
          'F_MODFUNC']}

def buildusevars(m, r):
    ret = {}
    outmess('\t\tBuilding use variable hooks for module "%s" (feature only for F90/F95)...\n' % m['name'])
    varsmap = {}
    revmap = {}
    if 'map' in r:
        for k in r['map'].keys():
            if r['map'][k] in revmap:
                outmess('\t\t\tVariable "%s<=%s" is already mapped by "%s". Skipping.\n' % (r['map'][k], k, revmap[r['map'][k]]))
            else:
                revmap[r['map'][k]] = k

    if 'only' in r and r['only']:
        for v in r['map'].keys():
            if r['map'][v] in m['vars']:
                if revmap[r['map'][v]] == v:
                    varsmap[v] = r['map'][v]
                else:
                    outmess('\t\t\tIgnoring map "%s=>%s". See above.\n' % (v, r['map'][v]))
            else:
                outmess('\t\t\tNo definition for variable "%s=>%s". Skipping.\n' % (v, r['map'][v]))

    else:
        for v in m['vars'].keys():
            if v in revmap:
                varsmap[v] = revmap[v]
            else:
                varsmap[v] = v

        for v in varsmap.keys():
            ret = dictappend(ret, buildusevar(v, varsmap[v], m['vars'], m['name']))

    return ret


def buildusevar(name, realname, vars, usemodulename):
    outmess('\t\t\tConstructing wrapper function for variable "%s=>%s"...\n' % (name, realname))
    ret = {}
    vrd = {'name': name, 'realname': realname, 
       'REALNAME': realname.upper(), 
       'usemodulename': usemodulename, 
       'USEMODULENAME': usemodulename.upper(), 
       'texname': name.replace('_', '\\_'), 
       'begintitle': gentitle('%s=>%s' % (name, realname)), 
       'endtitle': gentitle('end of %s=>%s' % (name, realname)), 
       'apiname': '#modulename#_use_%s_from_%s' % (realname, usemodulename)}
    nummap = {0: 'Ro', 1: 'Ri', 2: 'Rii', 3: 'Riii', 4: 'Riv', 5: 'Rv', 6: 'Rvi', 7: 'Rvii', 8: 'Rviii', 9: 'Rix'}
    vrd['texnamename'] = name
    for i in nummap.keys():
        vrd['texnamename'] = vrd['texnamename'].replace(`i`, nummap[i])

    if hasnote(vars[realname]):
        vrd['note'] = vars[realname]['note']
    rd = dictappend({}, vrd)
    var = vars[realname]
    print name, realname, vars[realname]
    ret = applyrules(usemodule_rules, rd)
    return ret