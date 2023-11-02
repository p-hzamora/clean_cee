# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\f2py\auxfuncs.pyc
# Compiled at: 2013-04-07 07:04:04
"""

Auxiliary functions for f2py2e.

Copyright 1999,2000 Pearu Peterson all rights reserved,
Pearu Peterson <pearu@ioc.ee>
Permission to use, modify, and distribute this software is given under the
terms of the NumPy (BSD style) LICENSE.

NO WARRANTY IS EXPRESSED OR IMPLIED.  USE AT YOUR OWN RISK.
$Date: 2005/07/24 19:01:55 $
Pearu Peterson
"""
__version__ = '$Revision: 1.65 $'[10:-1]
import __version__
f2py_version = __version__.version
import pprint, sys, types, cfuncs
errmess = sys.stderr.write
show = pprint.pprint
options = {}
debugoptions = []
wrapfuncs = 1
if sys.version_info[0] >= 3:
    from functools import reduce

def outmess(t):
    if options.get('verbose', 1):
        sys.stdout.write(t)


def debugcapi(var):
    return 'capi' in debugoptions


def _isstring(var):
    return 'typespec' in var and var['typespec'] == 'character' and not isexternal(var)


def isstring(var):
    return _isstring(var) and not isarray(var)


def ischaracter(var):
    return isstring(var) and 'charselector' not in var


def isstringarray(var):
    return isarray(var) and _isstring(var)


def isarrayofstrings(var):
    return isstringarray(var) and var['dimension'][-1] == '(*)'


def isarray(var):
    return 'dimension' in var and not isexternal(var)


def isscalar(var):
    return not (isarray(var) or isstring(var) or isexternal(var))


def iscomplex(var):
    return isscalar(var) and var.get('typespec') in ('complex', 'double complex')


def islogical(var):
    return isscalar(var) and var.get('typespec') == 'logical'


def isinteger(var):
    return isscalar(var) and var.get('typespec') == 'integer'


def isreal(var):
    return isscalar(var) and var.get('typespec') == 'real'


def get_kind(var):
    try:
        return var['kindselector']['*']
    except KeyError:
        try:
            return var['kindselector']['kind']
        except KeyError:
            pass


def islong_long(var):
    if not isscalar(var):
        return 0
    if var.get('typespec') not in ('integer', 'logical'):
        return 0
    return get_kind(var) == '8'


def isunsigned_char(var):
    if not isscalar(var):
        return 0
    if var.get('typespec') != 'integer':
        return 0
    return get_kind(var) == '-1'


def isunsigned_short(var):
    if not isscalar(var):
        return 0
    if var.get('typespec') != 'integer':
        return 0
    return get_kind(var) == '-2'


def isunsigned(var):
    if not isscalar(var):
        return 0
    if var.get('typespec') != 'integer':
        return 0
    return get_kind(var) == '-4'


def isunsigned_long_long(var):
    if not isscalar(var):
        return 0
    if var.get('typespec') != 'integer':
        return 0
    return get_kind(var) == '-8'


def isdouble(var):
    if not isscalar(var):
        return 0
    if not var.get('typespec') == 'real':
        return 0
    return get_kind(var) == '8'


def islong_double(var):
    if not isscalar(var):
        return 0
    if not var.get('typespec') == 'real':
        return 0
    return get_kind(var) == '16'


def islong_complex(var):
    if not iscomplex(var):
        return 0
    return get_kind(var) == '32'


def iscomplexarray(var):
    return isarray(var) and var.get('typespec') in ('complex', 'double complex')


def isint1array(var):
    return isarray(var) and var.get('typespec') == 'integer' and get_kind(var) == '1'


def isunsigned_chararray(var):
    return isarray(var) and var.get('typespec') in ('integer', 'logical') and get_kind(var) == '-1'


def isunsigned_shortarray(var):
    return isarray(var) and var.get('typespec') in ('integer', 'logical') and get_kind(var) == '-2'


def isunsignedarray(var):
    return isarray(var) and var.get('typespec') in ('integer', 'logical') and get_kind(var) == '-4'


def isunsigned_long_longarray(var):
    return isarray(var) and var.get('typespec') in ('integer', 'logical') and get_kind(var) == '-8'


def issigned_chararray(var):
    return isarray(var) and var.get('typespec') in ('integer', 'logical') and get_kind(var) == '1'


def issigned_shortarray(var):
    return isarray(var) and var.get('typespec') in ('integer', 'logical') and get_kind(var) == '2'


def issigned_array(var):
    return isarray(var) and var.get('typespec') in ('integer', 'logical') and get_kind(var) == '4'


def issigned_long_longarray(var):
    return isarray(var) and var.get('typespec') in ('integer', 'logical') and get_kind(var) == '8'


def isallocatable(var):
    return 'attrspec' in var and 'allocatable' in var['attrspec']


def ismutable(var):
    return not ('dimension' not in var or isstring(var))


def ismoduleroutine(rout):
    return 'modulename' in rout


def ismodule(rout):
    return 'block' in rout and 'module' == rout['block']


def isfunction(rout):
    return 'block' in rout and 'function' == rout['block']


def isfunction_wrap(rout):
    if isintent_c(rout):
        return 0
    return wrapfuncs and isfunction(rout) and not isexternal(rout)


def issubroutine(rout):
    return 'block' in rout and 'subroutine' == rout['block']


def issubroutine_wrap(rout):
    if isintent_c(rout):
        return 0
    return issubroutine(rout) and hasassumedshape(rout)


def hasassumedshape(rout):
    if rout.get('hasassumedshape'):
        return True
    for a in rout['args']:
        for d in rout['vars'].get(a, {}).get('dimension', []):
            if d == ':':
                rout['hasassumedshape'] = True
                return True

    return False


def isroutine(rout):
    return isfunction(rout) or issubroutine(rout)


def islogicalfunction(rout):
    if not isfunction(rout):
        return 0
    if 'result' in rout:
        a = rout['result']
    else:
        a = rout['name']
    if a in rout['vars']:
        return islogical(rout['vars'][a])
    return 0


def islong_longfunction(rout):
    if not isfunction(rout):
        return 0
    if 'result' in rout:
        a = rout['result']
    else:
        a = rout['name']
    if a in rout['vars']:
        return islong_long(rout['vars'][a])
    return 0


def islong_doublefunction(rout):
    if not isfunction(rout):
        return 0
    if 'result' in rout:
        a = rout['result']
    else:
        a = rout['name']
    if a in rout['vars']:
        return islong_double(rout['vars'][a])
    return 0


def iscomplexfunction(rout):
    if not isfunction(rout):
        return 0
    if 'result' in rout:
        a = rout['result']
    else:
        a = rout['name']
    if a in rout['vars']:
        return iscomplex(rout['vars'][a])
    return 0


def iscomplexfunction_warn(rout):
    if iscomplexfunction(rout):
        outmess('    **************************************************************\n        Warning: code with a function returning complex value\n        may not work correctly with your Fortran compiler.\n        Run the following test before using it in your applications:\n        $(f2py install dir)/test-site/{b/runme_scalar,e/runme}\n        When using GNU gcc/g77 compilers, codes should work correctly.\n    **************************************************************\n')
        return 1
    return 0


def isstringfunction(rout):
    if not isfunction(rout):
        return 0
    if 'result' in rout:
        a = rout['result']
    else:
        a = rout['name']
    if a in rout['vars']:
        return isstring(rout['vars'][a])
    return 0


def hasexternals(rout):
    return 'externals' in rout and rout['externals']


def isthreadsafe(rout):
    return 'f2pyenhancements' in rout and 'threadsafe' in rout['f2pyenhancements']


def hasvariables(rout):
    return 'vars' in rout and rout['vars']


def isoptional(var):
    return 'attrspec' in var and 'optional' in var['attrspec'] and 'required' not in var['attrspec'] and isintent_nothide(var)


def isexternal(var):
    return 'attrspec' in var and 'external' in var['attrspec']


def isrequired(var):
    return not isoptional(var) and isintent_nothide(var)


def isintent_in(var):
    if 'intent' not in var:
        return 1
    if 'hide' in var['intent']:
        return 0
    if 'inplace' in var['intent']:
        return 0
    if 'in' in var['intent']:
        return 1
    if 'out' in var['intent']:
        return 0
    if 'inout' in var['intent']:
        return 0
    if 'outin' in var['intent']:
        return 0
    return 1


def isintent_inout(var):
    return 'intent' in var and ('inout' in var['intent'] or 'outin' in var['intent']) and 'in' not in var['intent'] and 'hide' not in var['intent'] and 'inplace' not in var['intent']


def isintent_out(var):
    return 'out' in var.get('intent', [])


def isintent_hide(var):
    return 'intent' in var and ('hide' in var['intent'] or 'out' in var['intent'] and 'in' not in var['intent'] and not l_or(isintent_inout, isintent_inplace)(var))


def isintent_nothide(var):
    return not isintent_hide(var)


def isintent_c(var):
    return 'c' in var.get('intent', [])


def isintent_cache(var):
    return 'cache' in var.get('intent', [])


def isintent_copy(var):
    return 'copy' in var.get('intent', [])


def isintent_overwrite(var):
    return 'overwrite' in var.get('intent', [])


def isintent_callback(var):
    return 'callback' in var.get('intent', [])


def isintent_inplace(var):
    return 'inplace' in var.get('intent', [])


def isintent_aux(var):
    return 'aux' in var.get('intent', [])


def isintent_aligned4(var):
    return 'aligned4' in var.get('intent', [])


def isintent_aligned8(var):
    return 'aligned8' in var.get('intent', [])


def isintent_aligned16(var):
    return 'aligned16' in var.get('intent', [])


isintent_dict = {isintent_in: 'INTENT_IN', isintent_inout: 'INTENT_INOUT', isintent_out: 'INTENT_OUT', 
   isintent_hide: 'INTENT_HIDE', isintent_cache: 'INTENT_CACHE', 
   isintent_c: 'INTENT_C', 
   isoptional: 'OPTIONAL', isintent_inplace: 'INTENT_INPLACE', 
   isintent_aligned4: 'INTENT_ALIGNED4', 
   isintent_aligned8: 'INTENT_ALIGNED8', 
   isintent_aligned16: 'INTENT_ALIGNED16'}

def isprivate(var):
    return 'attrspec' in var and 'private' in var['attrspec']


def hasinitvalue(var):
    return '=' in var


def hasinitvalueasstring(var):
    if not hasinitvalue(var):
        return 0
    return var['='][0] in ('"', "'")


def hasnote(var):
    return 'note' in var


def hasresultnote(rout):
    if not isfunction(rout):
        return 0
    if 'result' in rout:
        a = rout['result']
    else:
        a = rout['name']
    if a in rout['vars']:
        return hasnote(rout['vars'][a])
    return 0


def hascommon(rout):
    return 'common' in rout


def containscommon(rout):
    if hascommon(rout):
        return 1
    if hasbody(rout):
        for b in rout['body']:
            if containscommon(b):
                return 1

    return 0


def containsmodule(block):
    if ismodule(block):
        return 1
    if not hasbody(block):
        return 0
    for b in block['body']:
        if containsmodule(b):
            return 1

    return 0


def hasbody(rout):
    return 'body' in rout


def hascallstatement(rout):
    return getcallstatement(rout) is not None


def istrue(var):
    return 1


def isfalse(var):
    return 0


class F2PYError(Exception):
    pass


class throw_error:

    def __init__(self, mess):
        self.mess = mess

    def __call__(self, var):
        mess = '\n\n  var = %s\n  Message: %s\n' % (var, self.mess)
        raise F2PYError, mess


def l_and(*f):
    l, l2 = 'lambda v', []
    for i in range(len(f)):
        l = '%s,f%d=f[%d]' % (l, i, i)
        l2.append('f%d(v)' % i)

    return eval('%s:%s' % (l, (' and ').join(l2)))


def l_or(*f):
    l, l2 = 'lambda v', []
    for i in range(len(f)):
        l = '%s,f%d=f[%d]' % (l, i, i)
        l2.append('f%d(v)' % i)

    return eval('%s:%s' % (l, (' or ').join(l2)))


def l_not(f):
    return eval('lambda v,f=f:not f(v)')


def isdummyroutine(rout):
    try:
        return rout['f2pyenhancements']['fortranname'] == ''
    except KeyError:
        return 0


def getfortranname(rout):
    try:
        name = rout['f2pyenhancements']['fortranname']
        if name == '':
            raise KeyError
        if not name:
            errmess('Failed to use fortranname from %s\n' % rout['f2pyenhancements'])
            raise KeyError
    except KeyError:
        name = rout['name']

    return name


def getmultilineblock(rout, blockname, comment=1, counter=0):
    try:
        r = rout['f2pyenhancements'].get(blockname)
    except KeyError:
        return

    if not r:
        return
    if counter > 0 and type(r) is type(''):
        return
    if type(r) is type([]):
        if counter >= len(r):
            return
        r = r[counter]
    if r[:3] == "'''":
        if comment:
            r = '\t/* start ' + blockname + ' multiline (' + `counter` + ') */\n' + r[3:]
        else:
            r = r[3:]
        if r[-3:] == "'''":
            if comment:
                r = r[:-3] + '\n\t/* end multiline (' + `counter` + ')*/'
            else:
                r = r[:-3]
        else:
            errmess("%s multiline block should end with `'''`: %s\n" % (
             blockname, repr(r)))
    return r


def getcallstatement(rout):
    return getmultilineblock(rout, 'callstatement')


def getcallprotoargument(rout, cb_map={}):
    r = getmultilineblock(rout, 'callprotoargument', comment=0)
    if r:
        return r
    if hascallstatement(rout):
        outmess('warning: callstatement is defined without callprotoargument\n')
        return
    from capi_maps import getctype
    arg_types, arg_types2 = [], []
    if l_and(isstringfunction, l_not(isfunction_wrap))(rout):
        arg_types.extend(['char*', 'size_t'])
    for n in rout['args']:
        var = rout['vars'][n]
        if isintent_callback(var):
            continue
        if n in cb_map:
            ctype = cb_map[n] + '_typedef'
        else:
            ctype = getctype(var)
            if l_and(isintent_c, l_or(isscalar, iscomplex))(var):
                pass
            elif isstring(var):
                pass
            else:
                ctype = ctype + '*'
            if isstring(var) or isarrayofstrings(var):
                arg_types2.append('size_t')
        arg_types.append(ctype)

    proto_args = (',').join(arg_types + arg_types2)
    if not proto_args:
        proto_args = 'void'
    return proto_args


def getusercode(rout):
    return getmultilineblock(rout, 'usercode')


def getusercode1(rout):
    return getmultilineblock(rout, 'usercode', counter=1)


def getpymethoddef(rout):
    return getmultilineblock(rout, 'pymethoddef')


def getargs(rout):
    sortargs, args = [], []
    if 'args' in rout:
        args = rout['args']
        if 'sortvars' in rout:
            for a in rout['sortvars']:
                if a in args:
                    sortargs.append(a)

            for a in args:
                if a not in sortargs:
                    sortargs.append(a)

        else:
            sortargs = rout['args']
    return (
     args, sortargs)


def getargs2(rout):
    sortargs, args = [], rout.get('args', [])
    auxvars = [ a for a in rout['vars'].keys() if isintent_aux(rout['vars'][a]) and a not in args
              ]
    args = auxvars + args
    if 'sortvars' in rout:
        for a in rout['sortvars']:
            if a in args:
                sortargs.append(a)

        for a in args:
            if a not in sortargs:
                sortargs.append(a)

    else:
        sortargs = auxvars + rout['args']
    return (
     args, sortargs)


def getrestdoc(rout):
    if 'f2pymultilines' not in rout:
        return
    else:
        k = None
        if rout['block'] == 'python module':
            k = (
             rout['block'], rout['name'])
        return rout['f2pymultilines'].get(k, None)


def gentitle(name):
    l = (80 - len(name) - 6) // 2
    return '/*%s %s %s*/' % (l * '*', name, l * '*')


def flatlist(l):
    if type(l) == types.ListType:
        return reduce((lambda x, y, f=flatlist: x + f(y)), l, [])
    return [
     l]


def stripcomma(s):
    if s and s[-1] == ',':
        return s[:-1]
    return s


def replace(str, d, defaultsep=''):
    if type(d) == types.ListType:
        return map((lambda d, f=replace, sep=defaultsep, s=str: f(s, d, sep)), d)
    if type(str) == types.ListType:
        return map((lambda s, f=replace, sep=defaultsep, d=d: f(s, d, sep)), str)
    for k in 2 * d.keys():
        if k == 'separatorsfor':
            continue
        if 'separatorsfor' in d and k in d['separatorsfor']:
            sep = d['separatorsfor'][k]
        else:
            sep = defaultsep
        if type(d[k]) == types.ListType:
            str = str.replace('#%s#' % k, sep.join(flatlist(d[k])))
        else:
            str = str.replace('#%s#' % k, d[k])

    return str


def dictappend(rd, ar):
    if type(ar) == types.ListType:
        for a in ar:
            rd = dictappend(rd, a)

        return rd
    for k in ar.keys():
        if k[0] == '_':
            continue
        if k in rd:
            if type(rd[k]) == str:
                rd[k] = [
                 rd[k]]
            if type(rd[k]) == types.ListType:
                if type(ar[k]) == types.ListType:
                    rd[k] = rd[k] + ar[k]
                else:
                    rd[k].append(ar[k])
            elif type(rd[k]) == types.DictType:
                if type(ar[k]) == types.DictType:
                    if k == 'separatorsfor':
                        for k1 in ar[k].keys():
                            if k1 not in rd[k]:
                                rd[k][k1] = ar[k][k1]

                    else:
                        rd[k] = dictappend(rd[k], ar[k])
        else:
            rd[k] = ar[k]

    return rd


def applyrules--- This code section failed: ---

 L. 655         0  BUILD_MAP_0           0  None
                3  STORE_FAST            3  'ret'

 L. 656         6  LOAD_GLOBAL           0  'type'
                9  LOAD_FAST             0  'rules'
               12  CALL_FUNCTION_1       1  None
               15  LOAD_GLOBAL           1  'types'
               18  LOAD_ATTR             2  'ListType'
               21  COMPARE_OP            2  ==
               24  POP_JUMP_IF_FALSE    97  'to 97'

 L. 657        27  SETUP_LOOP           63  'to 93'
               30  LOAD_FAST             0  'rules'
               33  GET_ITER         
               34  FOR_ITER             55  'to 92'
               37  STORE_FAST            4  'r'

 L. 658        40  LOAD_GLOBAL           3  'applyrules'
               43  LOAD_FAST             4  'r'
               46  LOAD_FAST             1  'd'
               49  LOAD_FAST             2  'var'
               52  CALL_FUNCTION_3       3  None
               55  STORE_FAST            5  'rr'

 L. 659        58  LOAD_GLOBAL           4  'dictappend'
               61  LOAD_FAST             3  'ret'
               64  LOAD_FAST             5  'rr'
               67  CALL_FUNCTION_2       2  None
               70  STORE_FAST            3  'ret'

 L. 660        73  LOAD_CONST               '_break'
               76  LOAD_FAST             5  'rr'
               79  COMPARE_OP            6  in
               82  POP_JUMP_IF_FALSE    34  'to 34'

 L. 661        85  BREAK_LOOP       
               86  JUMP_BACK            34  'to 34'
               89  JUMP_BACK            34  'to 34'
               92  POP_BLOCK        
             93_0  COME_FROM            27  '27'

 L. 662        93  LOAD_FAST             3  'ret'
               96  RETURN_VALUE     
             97_0  COME_FROM            24  '24'

 L. 663        97  LOAD_CONST               '_check'
              100  LOAD_FAST             0  'rules'
              103  COMPARE_OP            6  in
              106  POP_JUMP_IF_FALSE   130  'to 130'
              109  LOAD_FAST             0  'rules'
              112  LOAD_CONST               '_check'
              115  BINARY_SUBSCR    
              116  LOAD_FAST             2  'var'
              119  CALL_FUNCTION_1       1  None
              122  UNARY_NOT        
            123_0  COME_FROM           106  '106'
              123  POP_JUMP_IF_FALSE   130  'to 130'

 L. 664       126  LOAD_FAST             3  'ret'
              129  RETURN_END_IF    
            130_0  COME_FROM           123  '123'

 L. 665       130  LOAD_CONST               'need'
              133  LOAD_FAST             0  'rules'
              136  COMPARE_OP            6  in
              139  POP_JUMP_IF_FALSE   206  'to 206'

 L. 666       142  LOAD_GLOBAL           3  'applyrules'
              145  BUILD_MAP_1           1  None
              148  LOAD_FAST             0  'rules'
              151  LOAD_CONST               'need'
              154  BINARY_SUBSCR    
              155  LOAD_CONST               'needs'
              158  STORE_MAP        
              159  LOAD_FAST             1  'd'
              162  LOAD_FAST             2  'var'
              165  CALL_FUNCTION_3       3  None
              168  STORE_FAST            6  'res'

 L. 667       171  LOAD_CONST               'needs'
              174  LOAD_FAST             6  'res'
              177  COMPARE_OP            6  in
              180  POP_JUMP_IF_FALSE   206  'to 206'

 L. 668       183  LOAD_GLOBAL           5  'cfuncs'
              186  LOAD_ATTR             6  'append_needs'
              189  LOAD_FAST             6  'res'
              192  LOAD_CONST               'needs'
              195  BINARY_SUBSCR    
              196  CALL_FUNCTION_1       1  None
              199  POP_TOP          
              200  JUMP_ABSOLUTE       206  'to 206'
              203  JUMP_FORWARD          0  'to 206'
            206_0  COME_FROM           203  '203'

 L. 670       206  SETUP_LOOP          739  'to 948'
              209  LOAD_FAST             0  'rules'
              212  LOAD_ATTR             7  'keys'
              215  CALL_FUNCTION_0       0  None
              218  GET_ITER         
              219  FOR_ITER            725  'to 947'
              222  STORE_FAST            7  'k'

 L. 671       225  LOAD_FAST             7  'k'
              228  LOAD_CONST               'separatorsfor'
              231  COMPARE_OP            2  ==
              234  POP_JUMP_IF_FALSE   257  'to 257'

 L. 672       237  LOAD_FAST             0  'rules'
              240  LOAD_FAST             7  'k'
              243  BINARY_SUBSCR    
              244  LOAD_FAST             3  'ret'
              247  LOAD_FAST             7  'k'
              250  STORE_SUBSCR     
              251  JUMP_BACK           219  'to 219'
              254  JUMP_FORWARD          0  'to 257'
            257_0  COME_FROM           254  '254'

 L. 673       257  LOAD_GLOBAL           0  'type'
              260  LOAD_FAST             0  'rules'
              263  LOAD_FAST             7  'k'
              266  BINARY_SUBSCR    
              267  CALL_FUNCTION_1       1  None
              270  LOAD_GLOBAL           8  'str'
              273  COMPARE_OP            2  ==
              276  POP_JUMP_IF_FALSE   305  'to 305'

 L. 674       279  LOAD_GLOBAL           9  'replace'
              282  LOAD_FAST             0  'rules'
              285  LOAD_FAST             7  'k'
              288  BINARY_SUBSCR    
              289  LOAD_FAST             1  'd'
              292  CALL_FUNCTION_2       2  None
              295  LOAD_FAST             3  'ret'
              298  LOAD_FAST             7  'k'
              301  STORE_SUBSCR     
              302  JUMP_FORWARD        542  'to 847'

 L. 675       305  LOAD_GLOBAL           0  'type'
              308  LOAD_FAST             0  'rules'
              311  LOAD_FAST             7  'k'
              314  BINARY_SUBSCR    
              315  CALL_FUNCTION_1       1  None
              318  LOAD_GLOBAL           1  'types'
              321  LOAD_ATTR             2  'ListType'
              324  COMPARE_OP            2  ==
              327  POP_JUMP_IF_FALSE   425  'to 425'

 L. 676       330  BUILD_LIST_0          0 
              333  LOAD_FAST             3  'ret'
              336  LOAD_FAST             7  'k'
              339  STORE_SUBSCR     

 L. 677       340  SETUP_LOOP          504  'to 847'
              343  LOAD_FAST             0  'rules'
              346  LOAD_FAST             7  'k'
              349  BINARY_SUBSCR    
              350  GET_ITER         
              351  FOR_ITER             67  'to 421'
              354  STORE_FAST            8  'i'

 L. 678       357  LOAD_GLOBAL           3  'applyrules'
              360  BUILD_MAP_1           1  None
              363  LOAD_FAST             8  'i'
              366  LOAD_FAST             7  'k'
              369  STORE_MAP        
              370  LOAD_FAST             1  'd'
              373  LOAD_FAST             2  'var'
              376  CALL_FUNCTION_3       3  None
              379  STORE_FAST            9  'ar'

 L. 679       382  LOAD_FAST             7  'k'
              385  LOAD_FAST             9  'ar'
              388  COMPARE_OP            6  in
              391  POP_JUMP_IF_FALSE   351  'to 351'

 L. 680       394  LOAD_FAST             3  'ret'
              397  LOAD_FAST             7  'k'
              400  BINARY_SUBSCR    
              401  LOAD_ATTR            10  'append'
              404  LOAD_FAST             9  'ar'
              407  LOAD_FAST             7  'k'
              410  BINARY_SUBSCR    
              411  CALL_FUNCTION_1       1  None
              414  POP_TOP          
              415  JUMP_BACK           351  'to 351'
              418  JUMP_BACK           351  'to 351'
              421  POP_BLOCK        
            422_0  COME_FROM           340  '340'
              422  JUMP_FORWARD        422  'to 847'

 L. 681       425  LOAD_FAST             7  'k'
              428  LOAD_CONST               0
              431  BINARY_SUBSCR    
              432  LOAD_CONST               '_'
              435  COMPARE_OP            2  ==
              438  POP_JUMP_IF_FALSE   447  'to 447'

 L. 682       441  CONTINUE            219  'to 219'
              444  JUMP_FORWARD        400  'to 847'

 L. 683       447  LOAD_GLOBAL           0  'type'
              450  LOAD_FAST             0  'rules'
              453  LOAD_FAST             7  'k'
              456  BINARY_SUBSCR    
              457  CALL_FUNCTION_1       1  None
              460  LOAD_GLOBAL           1  'types'
              463  LOAD_ATTR            11  'DictType'
              466  COMPARE_OP            2  ==
              469  POP_JUMP_IF_FALSE   828  'to 828'

 L. 684       472  BUILD_LIST_0          0 
              475  LOAD_FAST             3  'ret'
              478  LOAD_FAST             7  'k'
              481  STORE_SUBSCR     

 L. 685       482  SETUP_LOOP          362  'to 847'
              485  LOAD_FAST             0  'rules'
              488  LOAD_FAST             7  'k'
              491  BINARY_SUBSCR    
              492  LOAD_ATTR             7  'keys'
              495  CALL_FUNCTION_0       0  None
              498  GET_ITER         
              499  FOR_ITER            322  'to 824'
              502  STORE_FAST           10  'k1'

 L. 686       505  LOAD_GLOBAL           0  'type'
              508  LOAD_FAST            10  'k1'
              511  CALL_FUNCTION_1       1  None
              514  LOAD_GLOBAL           1  'types'
              517  LOAD_ATTR            12  'FunctionType'
              520  COMPARE_OP            2  ==
              523  POP_JUMP_IF_FALSE   499  'to 499'
              526  LOAD_FAST            10  'k1'
              529  LOAD_FAST             2  'var'
              532  CALL_FUNCTION_1       1  None
            535_0  COME_FROM           523  '523'
              535  POP_JUMP_IF_FALSE   499  'to 499'

 L. 687       538  LOAD_GLOBAL           0  'type'
              541  LOAD_FAST             0  'rules'
              544  LOAD_FAST             7  'k'
              547  BINARY_SUBSCR    
              548  LOAD_FAST            10  'k1'
              551  BINARY_SUBSCR    
              552  CALL_FUNCTION_1       1  None
              555  LOAD_GLOBAL           1  'types'
              558  LOAD_ATTR             2  'ListType'
              561  COMPARE_OP            2  ==
              564  POP_JUMP_IF_FALSE   701  'to 701'

 L. 688       567  SETUP_LOOP          248  'to 818'
              570  LOAD_FAST             0  'rules'
              573  LOAD_FAST             7  'k'
              576  BINARY_SUBSCR    
              577  LOAD_FAST            10  'k1'
              580  BINARY_SUBSCR    
              581  GET_ITER         
              582  FOR_ITER            112  'to 697'
              585  STORE_FAST            8  'i'

 L. 689       588  LOAD_GLOBAL           0  'type'
              591  LOAD_FAST             8  'i'
              594  CALL_FUNCTION_1       1  None
              597  LOAD_GLOBAL           1  'types'
              600  LOAD_ATTR            11  'DictType'
              603  COMPARE_OP            2  ==
              606  POP_JUMP_IF_FALSE   668  'to 668'

 L. 690       609  LOAD_GLOBAL           3  'applyrules'
              612  BUILD_MAP_1           1  None
              615  LOAD_FAST             8  'i'
              618  LOAD_CONST               'supertext'
              621  STORE_MAP        
              622  LOAD_FAST             1  'd'
              625  LOAD_FAST             2  'var'
              628  CALL_FUNCTION_3       3  None
              631  STORE_FAST            6  'res'

 L. 691       634  LOAD_CONST               'supertext'
              637  LOAD_FAST             6  'res'
              640  COMPARE_OP            6  in
              643  POP_JUMP_IF_FALSE   659  'to 659'

 L. 692       646  LOAD_FAST             6  'res'
              649  LOAD_CONST               'supertext'
              652  BINARY_SUBSCR    
              653  STORE_FAST            8  'i'
              656  JUMP_ABSOLUTE       668  'to 668'

 L. 693       659  LOAD_CONST               ''
              662  STORE_FAST            8  'i'
              665  JUMP_FORWARD          0  'to 668'
            668_0  COME_FROM           665  '665'

 L. 694       668  LOAD_FAST             3  'ret'
              671  LOAD_FAST             7  'k'
              674  BINARY_SUBSCR    
              675  LOAD_ATTR            10  'append'
              678  LOAD_GLOBAL           9  'replace'
              681  LOAD_FAST             8  'i'
              684  LOAD_FAST             1  'd'
              687  CALL_FUNCTION_2       2  None
              690  CALL_FUNCTION_1       1  None
              693  POP_TOP          
              694  JUMP_BACK           582  'to 582'
              697  POP_BLOCK        
            698_0  COME_FROM           567  '567'
              698  JUMP_ABSOLUTE       821  'to 821'

 L. 696       701  LOAD_FAST             0  'rules'
              704  LOAD_FAST             7  'k'
              707  BINARY_SUBSCR    
              708  LOAD_FAST            10  'k1'
              711  BINARY_SUBSCR    
              712  STORE_FAST            8  'i'

 L. 697       715  LOAD_GLOBAL           0  'type'
              718  LOAD_FAST             8  'i'
              721  CALL_FUNCTION_1       1  None
              724  LOAD_GLOBAL           1  'types'
              727  LOAD_ATTR            11  'DictType'
              730  COMPARE_OP            2  ==
              733  POP_JUMP_IF_FALSE   792  'to 792'

 L. 698       736  LOAD_GLOBAL           3  'applyrules'
              739  BUILD_MAP_1           1  None
              742  LOAD_FAST             8  'i'
              745  LOAD_CONST               'supertext'
              748  STORE_MAP        
              749  LOAD_FAST             1  'd'
              752  CALL_FUNCTION_2       2  None
              755  STORE_FAST            6  'res'

 L. 699       758  LOAD_CONST               'supertext'
              761  LOAD_FAST             6  'res'
              764  COMPARE_OP            6  in
              767  POP_JUMP_IF_FALSE   783  'to 783'

 L. 700       770  LOAD_FAST             6  'res'
              773  LOAD_CONST               'supertext'
              776  BINARY_SUBSCR    
              777  STORE_FAST            8  'i'
              780  JUMP_ABSOLUTE       792  'to 792'

 L. 701       783  LOAD_CONST               ''
              786  STORE_FAST            8  'i'
              789  JUMP_FORWARD          0  'to 792'
            792_0  COME_FROM           789  '789'

 L. 702       792  LOAD_FAST             3  'ret'
              795  LOAD_FAST             7  'k'
              798  BINARY_SUBSCR    
              799  LOAD_ATTR            10  'append'
              802  LOAD_GLOBAL           9  'replace'
              805  LOAD_FAST             8  'i'
              808  LOAD_FAST             1  'd'
              811  CALL_FUNCTION_2       2  None
              814  CALL_FUNCTION_1       1  None
              817  POP_TOP          
              818  JUMP_BACK           499  'to 499'
              821  JUMP_BACK           499  'to 499'
              824  POP_BLOCK        
            825_0  COME_FROM           482  '482'
              825  JUMP_FORWARD         19  'to 847'

 L. 704       828  LOAD_GLOBAL          13  'errmess'
              831  LOAD_CONST               'applyrules: ignoring rule %s.\n'
              834  LOAD_FAST             0  'rules'
              837  LOAD_FAST             7  'k'
              840  BINARY_SUBSCR    
              841  UNARY_CONVERT    
              842  BINARY_MODULO    
              843  CALL_FUNCTION_1       1  None
              846  POP_TOP          
            847_0  COME_FROM           482  '482'
            847_1  COME_FROM           340  '340'
            847_2  COME_FROM           340  '340'
            847_3  COME_FROM           302  '302'

 L. 705       847  LOAD_GLOBAL           0  'type'
              850  LOAD_FAST             3  'ret'
              853  LOAD_FAST             7  'k'
              856  BINARY_SUBSCR    
              857  CALL_FUNCTION_1       1  None
              860  LOAD_GLOBAL           1  'types'
              863  LOAD_ATTR             2  'ListType'
              866  COMPARE_OP            2  ==
              869  POP_JUMP_IF_FALSE   219  'to 219'

 L. 706       872  LOAD_GLOBAL          14  'len'
              875  LOAD_FAST             3  'ret'
              878  LOAD_FAST             7  'k'
              881  BINARY_SUBSCR    
              882  CALL_FUNCTION_1       1  None
              885  LOAD_CONST               1
              888  COMPARE_OP            2  ==
              891  POP_JUMP_IF_FALSE   915  'to 915'

 L. 707       894  LOAD_FAST             3  'ret'
              897  LOAD_FAST             7  'k'
              900  BINARY_SUBSCR    
              901  LOAD_CONST               0
              904  BINARY_SUBSCR    
              905  LOAD_FAST             3  'ret'
              908  LOAD_FAST             7  'k'
              911  STORE_SUBSCR     
              912  JUMP_FORWARD          0  'to 915'
            915_0  COME_FROM           912  '912'

 L. 708       915  LOAD_FAST             3  'ret'
              918  LOAD_FAST             7  'k'
              921  BINARY_SUBSCR    
              922  BUILD_LIST_0          0 
              925  COMPARE_OP            2  ==
              928  POP_JUMP_IF_FALSE   944  'to 944'

 L. 709       931  LOAD_FAST             3  'ret'
              934  LOAD_FAST             7  'k'
              937  DELETE_SUBSCR    
              938  JUMP_ABSOLUTE       944  'to 944'
              941  JUMP_BACK           219  'to 219'
              944  JUMP_BACK           219  'to 219'
              947  POP_BLOCK        
            948_0  COME_FROM           206  '206'

 L. 710       948  LOAD_FAST             3  'ret'
              951  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `JUMP_FORWARD' instruction at offset 254