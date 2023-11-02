# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\f2py\crackfortran.pyc
# Compiled at: 2013-04-07 07:04:04
"""
crackfortran --- read fortran (77,90) code and extract declaration information.
    Usage is explained in the comment block below.

Copyright 1999-2004 Pearu Peterson all rights reserved,
Pearu Peterson <pearu@ioc.ee>
Permission to use, modify, and distribute this software is given under the
terms of the NumPy License.

NO WARRANTY IS EXPRESSED OR IMPLIED.  USE AT YOUR OWN RISK.
$Date: 2005/09/27 07:13:49 $
Pearu Peterson
"""
__version__ = '$Revision: 1.177 $'[10:-1]
import platform, __version__
f2py_version = __version__.version
import sys, string, fileinput, re, pprint, os, copy
from ...auxfuncs import *
strictf77 = 1
sourcecodeform = 'fix'
quiet = 0
verbose = 1
tabchar = 4 * ' '
pyffilename = ''
f77modulename = ''
skipemptyends = 0
ignorecontains = 1
dolowercase = 1
debug = []
groupcounter = 0
grouplist = {groupcounter: []}
neededmodule = -1
expectbegin = 1
skipblocksuntil = -1
usermodules = []
f90modulevars = {}
gotnextfile = 1
filepositiontext = ''
currentfilename = ''
skipfunctions = []
skipfuncs = []
onlyfuncs = []
include_paths = []
previous_context = None

def show(o, f=0):
    pprint.pprint(o)


errmess = sys.stderr.write

def outmess(line, flag=1):
    global filepositiontext
    global quiet
    global verbose
    if not verbose:
        return
    if not quiet:
        if flag:
            sys.stdout.write(filepositiontext)
        sys.stdout.write(line)


re._MAXCACHE = 50
defaultimplicitrules = {}
for c in 'abcdefghopqrstuvwxyz$_':
    defaultimplicitrules[c] = {'typespec': 'real'}

for c in 'ijklmn':
    defaultimplicitrules[c] = {'typespec': 'integer'}

del c
badnames = {}
invbadnames = {}
for n in ['int', 'double', 'float', 'char', 'short', 'long', 'void', 'case', 'while', 
 'return', 
 'signed', 'unsigned', 'if', 'for', 'typedef', 'sizeof', 'union', 
 'struct', 
 'static', 'register', 'new', 'break', 'do', 'goto', 'switch', 
 'continue', 
 'else', 'inline', 'extern', 'delete', 'const', 'auto', 
 'len', 'rank', 
 'shape', 'index', 'slen', 'size', '_i', 
 'max', 'min', 
 'flen', 'fshape', 
 'string', 
 'complex_double', 'float_double', 'stdin', 'stderr', 'stdout', 
 'type', 
 'default']:
    badnames[n] = n + '_bn'
    invbadnames[n + '_bn'] = n

def rmbadname1(name):
    if name in badnames:
        errmess('rmbadname1: Replacing "%s" with "%s".\n' % (name, badnames[name]))
        return badnames[name]
    return name


def rmbadname(names):
    return map(rmbadname1, names)


def undo_rmbadname1(name):
    if name in invbadnames:
        errmess('undo_rmbadname1: Replacing "%s" with "%s".\n' % (
         name, invbadnames[name]))
        return invbadnames[name]
    return name


def undo_rmbadname(names):
    return map(undo_rmbadname1, names)


def getextension(name):
    i = name.rfind('.')
    if i == -1:
        return ''
    if '\\' in name[i:]:
        return ''
    if '/' in name[i:]:
        return ''
    return name[i + 1:]


is_f_file = re.compile('.*[.](for|ftn|f77|f)\\Z', re.I).match
_has_f_header = re.compile('-[*]-\\s*fortran\\s*-[*]-', re.I).search
_has_f90_header = re.compile('-[*]-\\s*f90\\s*-[*]-', re.I).search
_has_fix_header = re.compile('-[*]-\\s*fix\\s*-[*]-', re.I).search
_free_f90_start = re.compile('[^c*]\\s*[^\\s\\d\\t]', re.I).match

def is_free_format(file):
    """Check if file is in free format Fortran."""
    result = 0
    f = open(file, 'r')
    line = f.readline()
    n = 15
    if _has_f_header(line):
        n = 0
    else:
        if _has_f90_header(line):
            n = 0
            result = 1
        while n > 0 and line:
            if line[0] != '!' and line.strip():
                n -= 1
                if line[0] != '\t' and _free_f90_start(line[:5]) or line[-2:-1] == '&':
                    result = 1
                    break
            line = f.readline()

    f.close()
    return result


def readfortrancode(ffile, dowithline=show, istop=1):
    """
    Read fortran codes from files and
     1) Get rid of comments, line continuations, and empty lines; lower cases.
     2) Call dowithline(line) on every line.
     3) Recursively call itself when statement "include '<filename>'" is met.
    """
    global beginpattern
    global currentfilename
    global dolowercase
    global filepositiontext
    global gotnextfile
    global include_paths
    global quiet
    global sourcecodeform
    global strictf77
    global verbose
    if not istop:
        saveglobals = (
         gotnextfile, filepositiontext, currentfilename, sourcecodeform, strictf77,
         beginpattern, quiet, verbose, dolowercase)
    if ffile == []:
        return
    else:
        localdolowercase = dolowercase
        cont = 0
        finalline = ''
        ll = ''
        commentline = re.compile('(?P<line>([^"]*["][^"]*["][^"!]*|[^\\\']*\\\'[^\\\']*\\\'[^\\\'!]*|[^!\\\'"]*))!{1}(?P<rest>.*)')
        includeline = re.compile('\\s*include\\s*(\\\'|")(?P<name>[^\\\'"]*)(\\\'|")', re.I)
        cont1 = re.compile('(?P<line>.*)&\\s*\\Z')
        cont2 = re.compile('(\\s*&|)(?P<line>.*)')
        mline_mark = re.compile(".*?'''")
        if istop:
            dowithline('', -1)
        ll, l1 = ('', '')
        spacedigits = [' '] + map(str, range(10))
        filepositiontext = ''
        fin = fileinput.FileInput(ffile)
        while 1:
            l = fin.readline()
            if not l:
                break
            if fin.isfirstline():
                filepositiontext = ''
                currentfilename = fin.filename()
                gotnextfile = 1
                l1 = l
                strictf77 = 0
                sourcecodeform = 'fix'
                ext = os.path.splitext(currentfilename)[1]
                if is_f_file(currentfilename) and not (_has_f90_header(l) or _has_fix_header(l)):
                    strictf77 = 1
                elif is_free_format(currentfilename) and not _has_fix_header(l):
                    sourcecodeform = 'free'
                if strictf77:
                    beginpattern = beginpattern77
                else:
                    beginpattern = beginpattern90
                outmess('\tReading file %s (format:%s%s)\n' % (
                 `currentfilename`, sourcecodeform,
                 strictf77 and ',strict' or ''))
            l = l.expandtabs().replace(b'\xa0', ' ')
            while not l == '':
                if l[-1] not in '\n\r\x0c':
                    break
                l = l[:-1]

            if not strictf77:
                r = commentline.match(l)
                if r:
                    l = r.group('line') + ' '
                    rl = r.group('rest')
                    if rl[:4].lower() == 'f2py':
                        l = l + '    '
                        r = commentline.match(rl[4:])
                        if r:
                            l = l + r.group('line')
                        else:
                            l = l + rl[4:]
            if l.strip() == '':
                cont = 0
                continue
            if sourcecodeform == 'fix':
                if l[0] in ('*', 'c', '!', 'C', '#'):
                    if l[1:5].lower() == 'f2py':
                        l = '     ' + l[5:]
                    else:
                        cont = 0
                        continue
                elif strictf77:
                    if len(l) > 72:
                        l = l[:72]
                if l[0] not in spacedigits:
                    raise Exception('readfortrancode: Found non-(space,digit) char in the first column.\n\tAre you sure that this code is in fix form?\n\tline=%s' % `l`)
                if (not cont or strictf77) and len(l) > 5 and not l[5] == ' ':
                    ll = ll + l[6:]
                    finalline = ''
                    origfinalline = ''
                elif not strictf77:
                    r = cont1.match(l)
                    if r:
                        l = r.group('line')
                    if cont:
                        ll = ll + cont2.match(l).group('line')
                        finalline = ''
                        origfinalline = ''
                    else:
                        l = '     ' + l[5:]
                        if localdolowercase:
                            finalline = ll.lower()
                        else:
                            finalline = ll
                        origfinalline = ll
                        ll = l
                    cont = r is not None
                else:
                    l = '     ' + l[5:]
                    if localdolowercase:
                        finalline = ll.lower()
                    else:
                        finalline = ll
                    origfinalline = ll
                    ll = l
            elif sourcecodeform == 'free':
                if not cont and ext == '.pyf' and mline_mark.match(l):
                    l = l + '\n'
                    while 1:
                        lc = fin.readline()
                        if not lc:
                            errmess('Unexpected end of file when reading multiline\n')
                            break
                        l = l + lc
                        if mline_mark.match(lc):
                            break

                    l = l.rstrip()
                r = cont1.match(l)
                if r:
                    l = r.group('line')
                if cont:
                    ll = ll + cont2.match(l).group('line')
                    finalline = ''
                    origfinalline = ''
                else:
                    if localdolowercase:
                        finalline = ll.lower()
                    else:
                        finalline = ll
                    origfinalline = ll
                    ll = l
                cont = r is not None
            else:
                raise ValueError("Flag sourcecodeform must be either 'fix' or 'free': %s" % `sourcecodeform`)
            filepositiontext = 'Line #%d in %s:"%s"\n\t' % (fin.filelineno() - 1, currentfilename, l1)
            m = includeline.match(origfinalline)
            if m:
                fn = m.group('name')
                if os.path.isfile(fn):
                    readfortrancode(fn, dowithline=dowithline, istop=0)
                else:
                    include_dirs = [
                     os.path.dirname(currentfilename)] + include_paths
                    foundfile = 0
                    for inc_dir in include_dirs:
                        fn1 = os.path.join(inc_dir, fn)
                        if os.path.isfile(fn1):
                            foundfile = 1
                            readfortrancode(fn1, dowithline=dowithline, istop=0)
                            break

                    if not foundfile:
                        outmess('readfortrancode: could not find include file %s in %s. Ignoring.\n' % (`fn`, os.pathsep.join(include_dirs)))
            else:
                dowithline(finalline)
            l1 = ll

        if localdolowercase:
            finalline = ll.lower()
        else:
            finalline = ll
        origfinalline = ll
        filepositiontext = 'Line #%d in %s:"%s"\n\t' % (fin.filelineno() - 1, currentfilename, l1)
        m = includeline.match(origfinalline)
        if m:
            fn = m.group('name')
            if os.path.isfile(fn):
                readfortrancode(fn, dowithline=dowithline, istop=0)
            else:
                include_dirs = [
                 os.path.dirname(currentfilename)] + include_paths
                foundfile = 0
                for inc_dir in include_dirs:
                    fn1 = os.path.join(inc_dir, fn)
                    if os.path.isfile(fn1):
                        foundfile = 1
                        readfortrancode(fn1, dowithline=dowithline, istop=0)
                        break

                if not foundfile:
                    outmess('readfortrancode: could not find include file %s in %s. Ignoring.\n' % (`fn`, os.pathsep.join(include_dirs)))
        else:
            dowithline(finalline)
        filepositiontext = ''
        fin.close()
        if istop:
            dowithline('', 1)
        else:
            gotnextfile, filepositiontext, currentfilename, sourcecodeform, strictf77, beginpattern, quiet, verbose, dolowercase = saveglobals
        return


beforethisafter = '\\s*(?P<before>%s(?=\\s*(\\b(%s)\\b)))' + '\\s*(?P<this>(\\b(%s)\\b))' + '\\s*(?P<after>%s)\\s*\\Z'
fortrantypes = 'character|logical|integer|real|complex|double\\s*(precision\\s*(complex|)|complex)|type(?=\\s*\\([\\w\\s,=(*)]*\\))|byte'
typespattern = (re.compile(beforethisafter % ('', fortrantypes, fortrantypes, '.*'), re.I), 'type')
typespattern4implicit = re.compile(beforethisafter % ('', fortrantypes + '|static|automatic|undefined', fortrantypes + '|static|automatic|undefined', '.*'), re.I)
functionpattern = (
 re.compile(beforethisafter % ('([a-z]+[\\w\\s(=*+-/)]*?|)', 'function', 'function', '.*'), re.I), 'begin')
subroutinepattern = (re.compile(beforethisafter % ('[a-z\\s]*?', 'subroutine', 'subroutine', '.*'), re.I), 'begin')
groupbegins77 = 'program|block\\s*data'
beginpattern77 = (re.compile(beforethisafter % ('', groupbegins77, groupbegins77, '.*'), re.I), 'begin')
groupbegins90 = groupbegins77 + '|module(?!\\s*procedure)|python\\s*module|interface|type(?!\\s*\\()'
beginpattern90 = (re.compile(beforethisafter % ('', groupbegins90, groupbegins90, '.*'), re.I), 'begin')
groupends = 'end|endprogram|endblockdata|endmodule|endpythonmodule|endinterface'
endpattern = (re.compile(beforethisafter % ('', groupends, groupends, '[\\w\\s]*'), re.I), 'end')
endifs = '(end\\s*(if|do|where|select|while|forall))|(module\\s*procedure)'
endifpattern = (re.compile(beforethisafter % ('[\\w]*?', endifs, endifs, '[\\w\\s]*'), re.I), 'endif')
implicitpattern = (
 re.compile(beforethisafter % ('', 'implicit', 'implicit', '.*'), re.I), 'implicit')
dimensionpattern = (re.compile(beforethisafter % ('', 'dimension|virtual', 'dimension|virtual', '.*'), re.I), 'dimension')
externalpattern = (re.compile(beforethisafter % ('', 'external', 'external', '.*'), re.I), 'external')
optionalpattern = (re.compile(beforethisafter % ('', 'optional', 'optional', '.*'), re.I), 'optional')
requiredpattern = (re.compile(beforethisafter % ('', 'required', 'required', '.*'), re.I), 'required')
publicpattern = (re.compile(beforethisafter % ('', 'public', 'public', '.*'), re.I), 'public')
privatepattern = (re.compile(beforethisafter % ('', 'private', 'private', '.*'), re.I), 'private')
intrisicpattern = (re.compile(beforethisafter % ('', 'intrisic', 'intrisic', '.*'), re.I), 'intrisic')
intentpattern = (re.compile(beforethisafter % ('', 'intent|depend|note|check', 'intent|depend|note|check', '\\s*\\(.*?\\).*'), re.I), 'intent')
parameterpattern = (re.compile(beforethisafter % ('', 'parameter', 'parameter', '\\s*\\(.*'), re.I), 'parameter')
datapattern = (re.compile(beforethisafter % ('', 'data', 'data', '.*'), re.I), 'data')
callpattern = (re.compile(beforethisafter % ('', 'call', 'call', '.*'), re.I), 'call')
entrypattern = (re.compile(beforethisafter % ('', 'entry', 'entry', '.*'), re.I), 'entry')
callfunpattern = (re.compile(beforethisafter % ('', 'callfun', 'callfun', '.*'), re.I), 'callfun')
commonpattern = (re.compile(beforethisafter % ('', 'common', 'common', '.*'), re.I), 'common')
usepattern = (re.compile(beforethisafter % ('', 'use', 'use', '.*'), re.I), 'use')
containspattern = (re.compile(beforethisafter % ('', 'contains', 'contains', ''), re.I), 'contains')
formatpattern = (re.compile(beforethisafter % ('', 'format', 'format', '.*'), re.I), 'format')
f2pyenhancementspattern = (
 re.compile(beforethisafter % ('', 'threadsafe|fortranname|callstatement|callprotoargument|usercode|pymethoddef', 'threadsafe|fortranname|callstatement|callprotoargument|usercode|pymethoddef', '.*'), re.I | re.S), 'f2pyenhancements')
multilinepattern = (re.compile("\\s*(?P<before>''')(?P<this>.*?)(?P<after>''')\\s*\\Z", re.S), 'multiline')

def _simplifyargs(argsline):
    a = []
    for n in markoutercomma(argsline).split('@,@'):
        for r in '(),':
            n = n.replace(r, '_')

        a.append(n)

    return (',').join(a)


crackline_re_1 = re.compile('\\s*(?P<result>\\b[a-z]+[\\w]*\\b)\\s*[=].*', re.I)

def crackline(line, reset=0):
    """
    reset=-1  --- initialize
    reset=0   --- crack the line
    reset=1   --- final check if mismatch of blocks occured

    Cracked data is saved in grouplist[0].
    """
    global expectbegin
    global f77modulename
    global gotnextfile
    global groupcache
    global groupcounter
    global grouplist
    global groupname
    global neededmodule
    global previous_context
    global skipblocksuntil
    global skipemptyends
    if ';' in line and not (f2pyenhancementspattern[0].match(line) or multilinepattern[0].match(line)):
        for l in line.split(';'):
            assert reset == 0, `reset`
            crackline(l, reset)

        return
    if reset < 0:
        groupcounter = 0
        groupname = {groupcounter: ''}
        groupcache = {groupcounter: {}}
        grouplist = {groupcounter: []}
        groupcache[groupcounter]['body'] = []
        groupcache[groupcounter]['vars'] = {}
        groupcache[groupcounter]['block'] = ''
        groupcache[groupcounter]['name'] = ''
        neededmodule = -1
        skipblocksuntil = -1
        return
    if reset > 0:
        fl = 0
        if f77modulename and neededmodule == groupcounter:
            fl = 2
        while groupcounter > fl:
            outmess('crackline: groupcounter=%s groupname=%s\n' % (`groupcounter`, `groupname`))
            outmess('crackline: Mismatch of blocks encountered. Trying to fix it by assuming "end" statement.\n')
            grouplist[groupcounter - 1].append(groupcache[groupcounter])
            grouplist[groupcounter - 1][-1]['body'] = grouplist[groupcounter]
            del grouplist[groupcounter]
            groupcounter = groupcounter - 1

        if f77modulename and neededmodule == groupcounter:
            grouplist[groupcounter - 1].append(groupcache[groupcounter])
            grouplist[groupcounter - 1][-1]['body'] = grouplist[groupcounter]
            del grouplist[groupcounter]
            groupcounter = groupcounter - 1
            grouplist[groupcounter - 1].append(groupcache[groupcounter])
            grouplist[groupcounter - 1][-1]['body'] = grouplist[groupcounter]
            del grouplist[groupcounter]
            groupcounter = groupcounter - 1
            neededmodule = -1
        return
    if line == '':
        return
    else:
        flag = 0
        for pat in [dimensionpattern, externalpattern, intentpattern, optionalpattern, 
         requiredpattern, 
         parameterpattern, 
         datapattern, publicpattern, privatepattern, 
         intrisicpattern, 
         endifpattern, 
         endpattern, 
         formatpattern, 
         beginpattern, 
         functionpattern, subroutinepattern, 
         implicitpattern, 
         typespattern, commonpattern, 
         callpattern, 
         usepattern, containspattern, 
         entrypattern, 
         f2pyenhancementspattern, 
         multilinepattern]:
            m = pat[0].match(line)
            if m:
                break
            flag = flag + 1

        if not m:
            re_1 = crackline_re_1
            if 0 <= skipblocksuntil <= groupcounter:
                return
            if 'externals' in groupcache[groupcounter]:
                for name in groupcache[groupcounter]['externals']:
                    if name in invbadnames:
                        name = invbadnames[name]
                    if 'interfaced' in groupcache[groupcounter] and name in groupcache[groupcounter]['interfaced']:
                        continue
                    m1 = re.match('(?P<before>[^"]*)\\b%s\\b\\s*@\\(@(?P<args>[^@]*)@\\)@.*\\Z' % name, markouterparen(line), re.I)
                    if m1:
                        m2 = re_1.match(m1.group('before'))
                        a = _simplifyargs(m1.group('args'))
                        if m2:
                            line = 'callfun %s(%s) result (%s)' % (name, a, m2.group('result'))
                        else:
                            line = 'callfun %s(%s)' % (name, a)
                        m = callfunpattern[0].match(line)
                        if not m:
                            outmess('crackline: could not resolve function call for line=%s.\n' % `line`)
                            return
                        analyzeline(m, 'callfun', line)
                        return

            if verbose > 1 or verbose == 1 and currentfilename.lower().endswith('.pyf'):
                previous_context = None
                outmess('crackline:%d: No pattern for line\n' % groupcounter)
            return
        if pat[1] == 'end':
            if 0 <= skipblocksuntil < groupcounter:
                groupcounter = groupcounter - 1
                if skipblocksuntil <= groupcounter:
                    return
            if groupcounter <= 0:
                raise Exception('crackline: groupcounter(=%s) is nonpositive. Check the blocks.' % groupcounter)
            m1 = beginpattern[0].match(line)
            if m1 and not m1.group('this') == groupname[groupcounter]:
                raise Exception('crackline: End group %s does not match with previous Begin group %s\n\t%s' % (
                 `(m1.group('this'))`, `(groupname[groupcounter])`,
                 filepositiontext))
            if skipblocksuntil == groupcounter:
                skipblocksuntil = -1
            grouplist[groupcounter - 1].append(groupcache[groupcounter])
            grouplist[groupcounter - 1][-1]['body'] = grouplist[groupcounter]
            del grouplist[groupcounter]
            groupcounter = groupcounter - 1
            if not skipemptyends:
                expectbegin = 1
        elif pat[1] == 'begin':
            if 0 <= skipblocksuntil <= groupcounter:
                groupcounter = groupcounter + 1
                return
            gotnextfile = 0
            analyzeline(m, pat[1], line)
            expectbegin = 0
        elif pat[1] == 'endif':
            pass
        elif pat[1] == 'contains':
            if ignorecontains:
                return
            if 0 <= skipblocksuntil <= groupcounter:
                return
            skipblocksuntil = groupcounter
        else:
            if 0 <= skipblocksuntil <= groupcounter:
                return
            analyzeline(m, pat[1], line)
        return


def markouterparen(line):
    l = ''
    f = 0
    for c in line:
        if c == '(':
            f = f + 1
            if f == 1:
                l = l + '@(@'
            continue
        elif c == ')':
            f = f - 1
            if f == 0:
                l = l + '@)@'
            continue
        l = l + c

    return l


def markoutercomma(line, comma=','):
    l = ''
    f = 0
    cc = ''
    for c in line:
        if (not cc or cc == ')') and c == '(':
            f = f + 1
            cc = ')'
        elif not cc and c == "'" and (not l or l[-1] != '\\'):
            f = f + 1
            cc = "'"
        elif c == cc:
            f = f - 1
            if f == 0:
                cc = ''
        elif c == comma and f == 0:
            l = l + '@' + comma + '@'
            continue
        l = l + c

    assert not f, `(f, line, l, cc)`
    return l


def unmarkouterparen(line):
    r = line.replace('@(@', '(').replace('@)@', ')')
    return r


def appenddecl(decl, decl2, force=1):
    if not decl:
        decl = {}
    if not decl2:
        return decl
    if decl is decl2:
        return decl
    for k in decl2.keys():
        if k == 'typespec':
            if force or k not in decl:
                decl[k] = decl2[k]
        elif k == 'attrspec':
            for l in decl2[k]:
                decl = setattrspec(decl, l, force)

        elif k == 'kindselector':
            decl = setkindselector(decl, decl2[k], force)
        elif k == 'charselector':
            decl = setcharselector(decl, decl2[k], force)
        elif k in ('=', 'typename'):
            if force or k not in decl:
                decl[k] = decl2[k]
        elif k == 'note':
            pass
        elif k in ('intent', 'check', 'dimension', 'optional', 'required'):
            errmess('appenddecl: "%s" not implemented.\n' % k)
        else:
            raise Exception('appenddecl: Unknown variable definition key:' + str(k))

    return decl


selectpattern = re.compile('\\s*(?P<this>(@\\(@.*?@\\)@|[*][\\d*]+|[*]\\s*@\\(@.*?@\\)@|))(?P<after>.*)\\Z', re.I)
nameargspattern = re.compile('\\s*(?P<name>\\b[\\w$]+\\b)\\s*(@\\(@\\s*(?P<args>[\\w\\s,]*)\\s*@\\)@|)\\s*((result(\\s*@\\(@\\s*(?P<result>\\b[\\w$]+\\b)\\s*@\\)@|))|(bind\\s*@\\(@\\s*(?P<bind>.*)\\s*@\\)@))*\\s*\\Z', re.I)
callnameargspattern = re.compile('\\s*(?P<name>\\b[\\w$]+\\b)\\s*@\\(@\\s*(?P<args>.*)\\s*@\\)@\\s*\\Z', re.I)
real16pattern = re.compile('([-+]?(?:\\d+(?:\\.\\d*)?|\\d*\\.\\d+))[dD]((?:[-+]?\\d+)?)')
real8pattern = re.compile('([-+]?((?:\\d+(?:\\.\\d*)?|\\d*\\.\\d+))[eE]((?:[-+]?\\d+)?)|(\\d+\\.\\d*))')
_intentcallbackpattern = re.compile('intent\\s*\\(.*?\\bcallback\\b', re.I)

def _is_intent_callback(vdecl):
    for a in vdecl.get('attrspec', []):
        if _intentcallbackpattern.match(a):
            return 1

    return 0


def _resolvenameargspattern(line):
    line = markouterparen(line)
    m1 = nameargspattern.match(line)
    if m1:
        return (m1.group('name'), m1.group('args'), m1.group('result'), m1.group('bind'))
    else:
        m1 = callnameargspattern.match(line)
        if m1:
            return (m1.group('name'), m1.group('args'), None, None)
        return (
         None, [], None, None)


def analyzeline--- This code section failed: ---

 L. 731         0  LOAD_FAST             0  'm'
                3  LOAD_ATTR             0  'group'
                6  LOAD_CONST               'this'
                9  CALL_FUNCTION_1       1  None
               12  STORE_FAST            3  'block'

 L. 732        15  LOAD_FAST             1  'case'
               18  LOAD_CONST               'multiline'
               21  COMPARE_OP            3  !=
               24  POP_JUMP_IF_FALSE    36  'to 36'

 L. 733        27  LOAD_CONST               None
               30  STORE_GLOBAL          2  'previous_context'
               33  JUMP_FORWARD          0  'to 36'
             36_0  COME_FROM            33  '33'

 L. 734        36  LOAD_GLOBAL           3  'expectbegin'
               39  POP_JUMP_IF_FALSE   243  'to 243'
               42  LOAD_FAST             1  'case'
               45  LOAD_CONST               ('begin', 'call', 'callfun', 'type')
               48  COMPARE_OP            7  not-in
             51_0  COME_FROM            39  '39'
               51  POP_JUMP_IF_FALSE   243  'to 243'

 L. 735        54  LOAD_GLOBAL           4  'skipemptyends'
               57  UNARY_NOT        
               58  POP_JUMP_IF_FALSE   243  'to 243'
               61  LOAD_GLOBAL           5  'groupcounter'
               64  LOAD_CONST               1
               67  COMPARE_OP            0  <
             70_0  COME_FROM            58  '58'
             70_1  COME_FROM            51  '51'
               70  POP_JUMP_IF_FALSE   243  'to 243'

 L. 736        73  LOAD_GLOBAL           6  'os'
               76  LOAD_ATTR             7  'path'
               79  LOAD_ATTR             8  'basename'
               82  LOAD_GLOBAL           9  'currentfilename'
               85  CALL_FUNCTION_1       1  None
               88  LOAD_ATTR            10  'split'
               91  LOAD_CONST               '.'
               94  CALL_FUNCTION_1       1  None
               97  LOAD_CONST               0
              100  BINARY_SUBSCR    
              101  STORE_FAST            4  'newname'

 L. 737       104  LOAD_GLOBAL          11  'outmess'
              107  LOAD_CONST               'analyzeline: no group yet. Creating program group with name "%s".\n'
              110  LOAD_FAST             4  'newname'
              113  BINARY_MODULO    
              114  CALL_FUNCTION_1       1  None
              117  POP_TOP          

 L. 738       118  LOAD_CONST               0
              121  STORE_GLOBAL         12  'gotnextfile'

 L. 739       124  LOAD_GLOBAL           5  'groupcounter'
              127  LOAD_CONST               1
              130  BINARY_ADD       
              131  STORE_GLOBAL          5  'groupcounter'

 L. 740       134  LOAD_CONST               'program'
              137  LOAD_GLOBAL          13  'groupname'
              140  LOAD_GLOBAL           5  'groupcounter'
              143  STORE_SUBSCR     

 L. 741       144  BUILD_MAP_0           0  None
              147  LOAD_GLOBAL          14  'groupcache'
              150  LOAD_GLOBAL           5  'groupcounter'
              153  STORE_SUBSCR     

 L. 742       154  BUILD_LIST_0          0 
              157  LOAD_GLOBAL          15  'grouplist'
              160  LOAD_GLOBAL           5  'groupcounter'
              163  STORE_SUBSCR     

 L. 743       164  BUILD_LIST_0          0 
              167  LOAD_GLOBAL          14  'groupcache'
              170  LOAD_GLOBAL           5  'groupcounter'
              173  BINARY_SUBSCR    
              174  LOAD_CONST               'body'
              177  STORE_SUBSCR     

 L. 744       178  BUILD_MAP_0           0  None
              181  LOAD_GLOBAL          14  'groupcache'
              184  LOAD_GLOBAL           5  'groupcounter'
              187  BINARY_SUBSCR    
              188  LOAD_CONST               'vars'
              191  STORE_SUBSCR     

 L. 745       192  LOAD_CONST               'program'
              195  LOAD_GLOBAL          14  'groupcache'
              198  LOAD_GLOBAL           5  'groupcounter'
              201  BINARY_SUBSCR    
              202  LOAD_CONST               'block'
              205  STORE_SUBSCR     

 L. 746       206  LOAD_FAST             4  'newname'
              209  LOAD_GLOBAL          14  'groupcache'
              212  LOAD_GLOBAL           5  'groupcounter'
              215  BINARY_SUBSCR    
              216  LOAD_CONST               'name'
              219  STORE_SUBSCR     

 L. 747       220  LOAD_CONST               'fromsky'
              223  LOAD_GLOBAL          14  'groupcache'
              226  LOAD_GLOBAL           5  'groupcounter'
              229  BINARY_SUBSCR    
              230  LOAD_CONST               'from'
              233  STORE_SUBSCR     

 L. 748       234  LOAD_CONST               0
              237  STORE_GLOBAL          3  'expectbegin'
              240  JUMP_FORWARD          0  'to 243'
            243_0  COME_FROM           240  '240'

 L. 749       243  LOAD_FAST             1  'case'
              246  LOAD_CONST               ('begin', 'call', 'callfun')
              249  COMPARE_OP            6  in
              252  POP_JUMP_IF_FALSE  2304  'to 2304'

 L. 751       255  LOAD_FAST             3  'block'
              258  LOAD_ATTR            16  'lower'
              261  CALL_FUNCTION_0       0  None
              264  STORE_FAST            3  'block'

 L. 752       267  LOAD_GLOBAL          17  're'
              270  LOAD_ATTR            18  'match'
              273  LOAD_CONST               'block\\s*data'
              276  LOAD_FAST             3  'block'
              279  LOAD_GLOBAL          17  're'
              282  LOAD_ATTR            19  'I'
              285  CALL_FUNCTION_3       3  None
              288  POP_JUMP_IF_FALSE   300  'to 300'
              291  LOAD_CONST               'block data'
              294  STORE_FAST            3  'block'
              297  JUMP_FORWARD          0  'to 300'
            300_0  COME_FROM           297  '297'

 L. 753       300  LOAD_GLOBAL          17  're'
              303  LOAD_ATTR            18  'match'
              306  LOAD_CONST               'python\\s*module'
              309  LOAD_FAST             3  'block'
              312  LOAD_GLOBAL          17  're'
              315  LOAD_ATTR            19  'I'
              318  CALL_FUNCTION_3       3  None
              321  POP_JUMP_IF_FALSE   333  'to 333'
              324  LOAD_CONST               'python module'
              327  STORE_FAST            3  'block'
              330  JUMP_FORWARD          0  'to 333'
            333_0  COME_FROM           330  '330'

 L. 754       333  LOAD_GLOBAL          20  '_resolvenameargspattern'
              336  LOAD_FAST             0  'm'
              339  LOAD_ATTR             0  'group'
              342  LOAD_CONST               'after'
              345  CALL_FUNCTION_1       1  None
              348  CALL_FUNCTION_1       1  None
              351  UNPACK_SEQUENCE_4     4 
              354  STORE_FAST            5  'name'
              357  STORE_FAST            6  'args'
              360  STORE_FAST            7  'result'
              363  STORE_FAST            8  'bind'

 L. 755       366  LOAD_FAST             5  'name'
              369  LOAD_CONST               None
              372  COMPARE_OP            8  is
              375  POP_JUMP_IF_FALSE   433  'to 433'

 L. 756       378  LOAD_FAST             3  'block'
              381  LOAD_CONST               'block data'
              384  COMPARE_OP            2  ==
              387  POP_JUMP_IF_FALSE   399  'to 399'

 L. 757       390  LOAD_CONST               '_BLOCK_DATA_'
              393  STORE_FAST            5  'name'
              396  JUMP_FORWARD          6  'to 405'

 L. 759       399  LOAD_CONST               ''
              402  STORE_FAST            5  'name'
            405_0  COME_FROM           396  '396'

 L. 760       405  LOAD_FAST             3  'block'
              408  LOAD_CONST               ('interface', 'block data')
              411  COMPARE_OP            7  not-in
              414  POP_JUMP_IF_FALSE   433  'to 433'

 L. 761       417  LOAD_GLOBAL          11  'outmess'
              420  LOAD_CONST               'analyzeline: No name/args pattern found for line.\n'
              423  CALL_FUNCTION_1       1  None
              426  POP_TOP          
              427  JUMP_ABSOLUTE       433  'to 433'
              430  JUMP_FORWARD          0  'to 433'
            433_0  COME_FROM           430  '430'

 L. 763       433  LOAD_FAST             3  'block'
              436  LOAD_FAST             5  'name'
              439  LOAD_GLOBAL           5  'groupcounter'
              442  BUILD_TUPLE_3         3 
              445  STORE_GLOBAL          2  'previous_context'

 L. 764       448  LOAD_FAST             6  'args'
              451  POP_JUMP_IF_FALSE   509  'to 509'
              454  LOAD_GLOBAL          21  'rmbadname'
              457  BUILD_LIST_0          0 
              460  LOAD_GLOBAL          22  'markoutercomma'
              463  LOAD_FAST             6  'args'
              466  CALL_FUNCTION_1       1  None
              469  LOAD_ATTR            10  'split'
              472  LOAD_CONST               '@,@'
              475  CALL_FUNCTION_1       1  None
              478  GET_ITER         
              479  FOR_ITER             18  'to 500'
              482  STORE_FAST            9  'x'
              485  LOAD_FAST             9  'x'
              488  LOAD_ATTR            23  'strip'
              491  CALL_FUNCTION_0       0  None
              494  LIST_APPEND           2  None
              497  JUMP_BACK           479  'to 479'
              500  CALL_FUNCTION_1       1  None
              503  STORE_FAST            6  'args'
              506  JUMP_FORWARD          6  'to 515'

 L. 765       509  BUILD_LIST_0          0 
              512  STORE_FAST            6  'args'
            515_0  COME_FROM           506  '506'

 L. 766       515  LOAD_CONST               ''
              518  LOAD_FAST             6  'args'
              521  COMPARE_OP            6  in
              524  POP_JUMP_IF_FALSE   572  'to 572'

 L. 767       527  SETUP_LOOP           29  'to 559'
              530  LOAD_CONST               ''
              533  LOAD_FAST             6  'args'
              536  COMPARE_OP            6  in
              539  POP_JUMP_IF_FALSE   558  'to 558'

 L. 768       542  LOAD_FAST             6  'args'
              545  LOAD_ATTR            24  'remove'
              548  LOAD_CONST               ''
              551  CALL_FUNCTION_1       1  None
              554  POP_TOP          
              555  JUMP_BACK           530  'to 530'
              558  POP_BLOCK        
            559_0  COME_FROM           527  '527'

 L. 769       559  LOAD_GLOBAL          11  'outmess'
              562  LOAD_CONST               'analyzeline: argument list is malformed (missing argument).\n'
              565  CALL_FUNCTION_1       1  None
              568  POP_TOP          
              569  JUMP_FORWARD          0  'to 572'
            572_0  COME_FROM           569  '569'

 L. 772       572  LOAD_CONST               0
              575  STORE_FAST           10  'needmodule'

 L. 773       578  LOAD_CONST               0
              581  STORE_FAST           11  'needinterface'

 L. 775       584  LOAD_FAST             1  'case'
              587  LOAD_CONST               ('call', 'callfun')
              590  COMPARE_OP            6  in
              593  POP_JUMP_IF_FALSE   738  'to 738'

 L. 776       596  LOAD_CONST               1
              599  STORE_FAST           11  'needinterface'

 L. 777       602  LOAD_CONST               'args'
              605  LOAD_GLOBAL          14  'groupcache'
              608  LOAD_GLOBAL           5  'groupcounter'
              611  BINARY_SUBSCR    
              612  COMPARE_OP            7  not-in
              615  POP_JUMP_IF_FALSE   622  'to 622'

 L. 778       618  LOAD_CONST               None
              621  RETURN_END_IF    
            622_0  COME_FROM           615  '615'

 L. 779       622  LOAD_FAST             5  'name'
              625  LOAD_GLOBAL          14  'groupcache'
              628  LOAD_GLOBAL           5  'groupcounter'
              631  BINARY_SUBSCR    
              632  LOAD_CONST               'args'
              635  BINARY_SUBSCR    
              636  COMPARE_OP            7  not-in
              639  POP_JUMP_IF_FALSE   646  'to 646'

 L. 780       642  LOAD_CONST               None
              645  RETURN_END_IF    
            646_0  COME_FROM           639  '639'

 L. 781       646  SETUP_LOOP           38  'to 687'
              649  LOAD_GLOBAL          15  'grouplist'
              652  LOAD_GLOBAL           5  'groupcounter'
              655  BINARY_SUBSCR    
              656  GET_ITER         
              657  FOR_ITER             26  'to 686'
              660  STORE_FAST           12  'it'

 L. 782       663  LOAD_FAST            12  'it'
              666  LOAD_CONST               'name'
              669  BINARY_SUBSCR    
              670  LOAD_FAST             5  'name'
              673  COMPARE_OP            2  ==
              676  POP_JUMP_IF_FALSE   657  'to 657'

 L. 783       679  LOAD_CONST               None
              682  RETURN_END_IF    
            683_0  COME_FROM           676  '676'
              683  JUMP_BACK           657  'to 657'
              686  POP_BLOCK        
            687_0  COME_FROM           646  '646'

 L. 784       687  LOAD_FAST             5  'name'
              690  LOAD_GLOBAL          14  'groupcache'
              693  LOAD_GLOBAL           5  'groupcounter'
              696  BINARY_SUBSCR    
              697  LOAD_CONST               'interfaced'
              700  BINARY_SUBSCR    
              701  COMPARE_OP            6  in
              704  POP_JUMP_IF_FALSE   711  'to 711'

 L. 785       707  LOAD_CONST               None
              710  RETURN_END_IF    
            711_0  COME_FROM           704  '704'

 L. 786       711  BUILD_MAP_2           2  None
              714  LOAD_CONST               'subroutine'
              717  LOAD_CONST               'call'
              720  STORE_MAP        
              721  LOAD_CONST               'function'
              724  LOAD_CONST               'callfun'
              727  STORE_MAP        
              728  LOAD_FAST             1  'case'
              731  BINARY_SUBSCR    
              732  STORE_FAST            3  'block'
              735  JUMP_FORWARD          0  'to 738'
            738_0  COME_FROM           735  '735'

 L. 787       738  LOAD_GLOBAL          25  'f77modulename'
              741  POP_JUMP_IF_FALSE   808  'to 808'
              744  LOAD_GLOBAL          26  'neededmodule'
              747  LOAD_CONST               -1
              750  COMPARE_OP            2  ==
              753  POP_JUMP_IF_FALSE   808  'to 808'
              756  LOAD_GLOBAL           5  'groupcounter'
              759  LOAD_CONST               1
              762  COMPARE_OP            1  <=
            765_0  COME_FROM           753  '753'
            765_1  COME_FROM           741  '741'
              765  POP_JUMP_IF_FALSE   808  'to 808'

 L. 788       768  LOAD_GLOBAL           5  'groupcounter'
              771  LOAD_CONST               2
              774  BINARY_ADD       
              775  STORE_GLOBAL         26  'neededmodule'

 L. 789       778  LOAD_CONST               1
              781  STORE_FAST           10  'needmodule'

 L. 790       784  LOAD_FAST             3  'block'
              787  LOAD_CONST               'interface'
              790  COMPARE_OP            3  !=
              793  POP_JUMP_IF_FALSE   808  'to 808'

 L. 791       796  LOAD_CONST               1
              799  STORE_FAST           11  'needinterface'
              802  JUMP_ABSOLUTE       808  'to 808'
              805  JUMP_FORWARD          0  'to 808'
            808_0  COME_FROM           805  '805'

 L. 793       808  LOAD_GLOBAL           5  'groupcounter'
              811  LOAD_CONST               1
              814  BINARY_ADD       
              815  STORE_GLOBAL          5  'groupcounter'

 L. 794       818  BUILD_MAP_0           0  None
              821  LOAD_GLOBAL          14  'groupcache'
              824  LOAD_GLOBAL           5  'groupcounter'
              827  STORE_SUBSCR     

 L. 795       828  BUILD_LIST_0          0 
              831  LOAD_GLOBAL          15  'grouplist'
              834  LOAD_GLOBAL           5  'groupcounter'
              837  STORE_SUBSCR     

 L. 796       838  LOAD_FAST            10  'needmodule'
              841  POP_JUMP_IF_FALSE  1018  'to 1018'

 L. 797       844  LOAD_GLOBAL          27  'verbose'
              847  LOAD_CONST               1
              850  COMPARE_OP            4  >
              853  POP_JUMP_IF_FALSE   877  'to 877'

 L. 798       856  LOAD_GLOBAL          11  'outmess'
              859  LOAD_CONST               'analyzeline: Creating module block %s\n'
              862  LOAD_GLOBAL          25  'f77modulename'
              865  UNARY_CONVERT    
              866  BINARY_MODULO    
              867  LOAD_CONST               0
              870  CALL_FUNCTION_2       2  None
              873  POP_TOP          
              874  JUMP_FORWARD          0  'to 877'
            877_0  COME_FROM           874  '874'

 L. 799       877  LOAD_CONST               'module'
              880  LOAD_GLOBAL          13  'groupname'
              883  LOAD_GLOBAL           5  'groupcounter'
              886  STORE_SUBSCR     

 L. 800       887  LOAD_CONST               'python module'
              890  LOAD_GLOBAL          14  'groupcache'
              893  LOAD_GLOBAL           5  'groupcounter'
              896  BINARY_SUBSCR    
              897  LOAD_CONST               'block'
              900  STORE_SUBSCR     

 L. 801       901  LOAD_GLOBAL          25  'f77modulename'
              904  LOAD_GLOBAL          14  'groupcache'
              907  LOAD_GLOBAL           5  'groupcounter'
              910  BINARY_SUBSCR    
              911  LOAD_CONST               'name'
              914  STORE_SUBSCR     

 L. 802       915  LOAD_CONST               ''
              918  LOAD_GLOBAL          14  'groupcache'
              921  LOAD_GLOBAL           5  'groupcounter'
              924  BINARY_SUBSCR    
              925  LOAD_CONST               'from'
              928  STORE_SUBSCR     

 L. 803       929  BUILD_LIST_0          0 
              932  LOAD_GLOBAL          14  'groupcache'
              935  LOAD_GLOBAL           5  'groupcounter'
              938  BINARY_SUBSCR    
              939  LOAD_CONST               'body'
              942  STORE_SUBSCR     

 L. 804       943  BUILD_LIST_0          0 
              946  LOAD_GLOBAL          14  'groupcache'
              949  LOAD_GLOBAL           5  'groupcounter'
              952  BINARY_SUBSCR    
              953  LOAD_CONST               'externals'
              956  STORE_SUBSCR     

 L. 805       957  BUILD_LIST_0          0 
              960  LOAD_GLOBAL          14  'groupcache'
              963  LOAD_GLOBAL           5  'groupcounter'
              966  BINARY_SUBSCR    
              967  LOAD_CONST               'interfaced'
              970  STORE_SUBSCR     

 L. 806       971  BUILD_MAP_0           0  None
              974  LOAD_GLOBAL          14  'groupcache'
              977  LOAD_GLOBAL           5  'groupcounter'
              980  BINARY_SUBSCR    
              981  LOAD_CONST               'vars'
              984  STORE_SUBSCR     

 L. 807       985  LOAD_GLOBAL           5  'groupcounter'
              988  LOAD_CONST               1
              991  BINARY_ADD       
              992  STORE_GLOBAL          5  'groupcounter'

 L. 808       995  BUILD_MAP_0           0  None
              998  LOAD_GLOBAL          14  'groupcache'
             1001  LOAD_GLOBAL           5  'groupcounter'
             1004  STORE_SUBSCR     

 L. 809      1005  BUILD_LIST_0          0 
             1008  LOAD_GLOBAL          15  'grouplist'
             1011  LOAD_GLOBAL           5  'groupcounter'
             1014  STORE_SUBSCR     
             1015  JUMP_FORWARD          0  'to 1018'
           1018_0  COME_FROM          1015  '1015'

 L. 810      1018  LOAD_FAST            11  'needinterface'
             1021  POP_JUMP_IF_FALSE  1231  'to 1231'

 L. 811      1024  LOAD_GLOBAL          27  'verbose'
             1027  LOAD_CONST               1
             1030  COMPARE_OP            4  >
             1033  POP_JUMP_IF_FALSE  1056  'to 1056'

 L. 812      1036  LOAD_GLOBAL          11  'outmess'
             1039  LOAD_CONST               'analyzeline: Creating additional interface block (groupcounter=%s).\n'
             1042  LOAD_GLOBAL           5  'groupcounter'
             1045  BINARY_MODULO    
             1046  LOAD_CONST               0
             1049  CALL_FUNCTION_2       2  None
             1052  POP_TOP          
             1053  JUMP_FORWARD          0  'to 1056'
           1056_0  COME_FROM          1053  '1053'

 L. 813      1056  LOAD_CONST               'interface'
             1059  LOAD_GLOBAL          13  'groupname'
             1062  LOAD_GLOBAL           5  'groupcounter'
             1065  STORE_SUBSCR     

 L. 814      1066  LOAD_CONST               'interface'
             1069  LOAD_GLOBAL          14  'groupcache'
             1072  LOAD_GLOBAL           5  'groupcounter'
             1075  BINARY_SUBSCR    
             1076  LOAD_CONST               'block'
             1079  STORE_SUBSCR     

 L. 815      1080  LOAD_CONST               'unknown_interface'
             1083  LOAD_GLOBAL          14  'groupcache'
             1086  LOAD_GLOBAL           5  'groupcounter'
             1089  BINARY_SUBSCR    
             1090  LOAD_CONST               'name'
             1093  STORE_SUBSCR     

 L. 816      1094  LOAD_CONST               '%s:%s'
             1097  LOAD_GLOBAL          14  'groupcache'
             1100  LOAD_GLOBAL           5  'groupcounter'
             1103  LOAD_CONST               1
             1106  BINARY_SUBTRACT  
             1107  BINARY_SUBSCR    
             1108  LOAD_CONST               'from'
             1111  BINARY_SUBSCR    
             1112  LOAD_GLOBAL          14  'groupcache'
             1115  LOAD_GLOBAL           5  'groupcounter'
             1118  LOAD_CONST               1
             1121  BINARY_SUBTRACT  
             1122  BINARY_SUBSCR    
             1123  LOAD_CONST               'name'
             1126  BINARY_SUBSCR    
             1127  BUILD_TUPLE_2         2 
             1130  BINARY_MODULO    
             1131  LOAD_GLOBAL          14  'groupcache'
             1134  LOAD_GLOBAL           5  'groupcounter'
             1137  BINARY_SUBSCR    
             1138  LOAD_CONST               'from'
             1141  STORE_SUBSCR     

 L. 817      1142  BUILD_LIST_0          0 
             1145  LOAD_GLOBAL          14  'groupcache'
             1148  LOAD_GLOBAL           5  'groupcounter'
             1151  BINARY_SUBSCR    
             1152  LOAD_CONST               'body'
             1155  STORE_SUBSCR     

 L. 818      1156  BUILD_LIST_0          0 
             1159  LOAD_GLOBAL          14  'groupcache'
             1162  LOAD_GLOBAL           5  'groupcounter'
             1165  BINARY_SUBSCR    
             1166  LOAD_CONST               'externals'
             1169  STORE_SUBSCR     

 L. 819      1170  BUILD_LIST_0          0 
             1173  LOAD_GLOBAL          14  'groupcache'
             1176  LOAD_GLOBAL           5  'groupcounter'
             1179  BINARY_SUBSCR    
             1180  LOAD_CONST               'interfaced'
             1183  STORE_SUBSCR     

 L. 820      1184  BUILD_MAP_0           0  None
             1187  LOAD_GLOBAL          14  'groupcache'
             1190  LOAD_GLOBAL           5  'groupcounter'
             1193  BINARY_SUBSCR    
             1194  LOAD_CONST               'vars'
             1197  STORE_SUBSCR     

 L. 821      1198  LOAD_GLOBAL           5  'groupcounter'
             1201  LOAD_CONST               1
             1204  BINARY_ADD       
             1205  STORE_GLOBAL          5  'groupcounter'

 L. 822      1208  BUILD_MAP_0           0  None
             1211  LOAD_GLOBAL          14  'groupcache'
             1214  LOAD_GLOBAL           5  'groupcounter'
             1217  STORE_SUBSCR     

 L. 823      1218  BUILD_LIST_0          0 
             1221  LOAD_GLOBAL          15  'grouplist'
             1224  LOAD_GLOBAL           5  'groupcounter'
             1227  STORE_SUBSCR     
             1228  JUMP_FORWARD          0  'to 1231'
           1231_0  COME_FROM          1228  '1228'

 L. 824      1231  LOAD_FAST             3  'block'
             1234  LOAD_GLOBAL          13  'groupname'
             1237  LOAD_GLOBAL           5  'groupcounter'
             1240  STORE_SUBSCR     

 L. 825      1241  LOAD_FAST             3  'block'
             1244  LOAD_GLOBAL          14  'groupcache'
             1247  LOAD_GLOBAL           5  'groupcounter'
             1250  BINARY_SUBSCR    
             1251  LOAD_CONST               'block'
             1254  STORE_SUBSCR     

 L. 826      1255  LOAD_FAST             5  'name'
             1258  POP_JUMP_IF_TRUE   1274  'to 1274'
             1261  LOAD_CONST               'unknown_'
             1264  LOAD_FAST             3  'block'
             1267  BINARY_ADD       
             1268  STORE_FAST            5  'name'
             1271  JUMP_FORWARD          0  'to 1274'
           1274_0  COME_FROM          1271  '1271'

 L. 827      1274  LOAD_FAST             0  'm'
             1277  LOAD_ATTR             0  'group'
             1280  LOAD_CONST               'before'
             1283  CALL_FUNCTION_1       1  None
             1286  LOAD_GLOBAL          14  'groupcache'
             1289  LOAD_GLOBAL           5  'groupcounter'
             1292  BINARY_SUBSCR    
             1293  LOAD_CONST               'prefix'
             1296  STORE_SUBSCR     

 L. 828      1297  LOAD_GLOBAL          28  'rmbadname1'
             1300  LOAD_FAST             5  'name'
             1303  CALL_FUNCTION_1       1  None
             1306  LOAD_GLOBAL          14  'groupcache'
             1309  LOAD_GLOBAL           5  'groupcounter'
             1312  BINARY_SUBSCR    
             1313  LOAD_CONST               'name'
             1316  STORE_SUBSCR     

 L. 829      1317  LOAD_FAST             7  'result'
             1320  LOAD_GLOBAL          14  'groupcache'
             1323  LOAD_GLOBAL           5  'groupcounter'
             1326  BINARY_SUBSCR    
             1327  LOAD_CONST               'result'
             1330  STORE_SUBSCR     

 L. 830      1331  LOAD_GLOBAL           5  'groupcounter'
             1334  LOAD_CONST               1
             1337  COMPARE_OP            2  ==
             1340  POP_JUMP_IF_FALSE  1360  'to 1360'

 L. 831      1343  LOAD_GLOBAL           9  'currentfilename'
             1346  LOAD_GLOBAL          14  'groupcache'
             1349  LOAD_GLOBAL           5  'groupcounter'
             1352  BINARY_SUBSCR    
             1353  LOAD_CONST               'from'
             1356  STORE_SUBSCR     
             1357  JUMP_FORWARD        105  'to 1465'

 L. 833      1360  LOAD_GLOBAL          25  'f77modulename'
             1363  POP_JUMP_IF_FALSE  1417  'to 1417'
             1366  LOAD_GLOBAL           5  'groupcounter'
             1369  LOAD_CONST               3
             1372  COMPARE_OP            2  ==
           1375_0  COME_FROM          1363  '1363'
             1375  POP_JUMP_IF_FALSE  1417  'to 1417'

 L. 834      1378  LOAD_CONST               '%s:%s'
             1381  LOAD_GLOBAL          14  'groupcache'
             1384  LOAD_GLOBAL           5  'groupcounter'
             1387  LOAD_CONST               1
             1390  BINARY_SUBTRACT  
             1391  BINARY_SUBSCR    
             1392  LOAD_CONST               'from'
             1395  BINARY_SUBSCR    
             1396  LOAD_GLOBAL           9  'currentfilename'
             1399  BUILD_TUPLE_2         2 
             1402  BINARY_MODULO    
             1403  LOAD_GLOBAL          14  'groupcache'
             1406  LOAD_GLOBAL           5  'groupcounter'
             1409  BINARY_SUBSCR    
             1410  LOAD_CONST               'from'
             1413  STORE_SUBSCR     
             1414  JUMP_FORWARD         48  'to 1465'

 L. 836      1417  LOAD_CONST               '%s:%s'
             1420  LOAD_GLOBAL          14  'groupcache'
             1423  LOAD_GLOBAL           5  'groupcounter'
             1426  LOAD_CONST               1
             1429  BINARY_SUBTRACT  
             1430  BINARY_SUBSCR    
             1431  LOAD_CONST               'from'
             1434  BINARY_SUBSCR    
             1435  LOAD_GLOBAL          14  'groupcache'
             1438  LOAD_GLOBAL           5  'groupcounter'
             1441  LOAD_CONST               1
             1444  BINARY_SUBTRACT  
             1445  BINARY_SUBSCR    
             1446  LOAD_CONST               'name'
             1449  BINARY_SUBSCR    
             1450  BUILD_TUPLE_2         2 
             1453  BINARY_MODULO    
             1454  LOAD_GLOBAL          14  'groupcache'
             1457  LOAD_GLOBAL           5  'groupcounter'
             1460  BINARY_SUBSCR    
             1461  LOAD_CONST               'from'
             1464  STORE_SUBSCR     
           1465_0  COME_FROM          1414  '1414'
           1465_1  COME_FROM          1357  '1357'

 L. 837      1465  SETUP_LOOP           52  'to 1520'
             1468  LOAD_GLOBAL          14  'groupcache'
             1471  LOAD_GLOBAL           5  'groupcounter'
             1474  BINARY_SUBSCR    
             1475  LOAD_ATTR            29  'keys'
             1478  CALL_FUNCTION_0       0  None
             1481  GET_ITER         
             1482  FOR_ITER             34  'to 1519'
             1485  STORE_FAST           13  'k'

 L. 838      1488  LOAD_GLOBAL          14  'groupcache'
             1491  LOAD_GLOBAL           5  'groupcounter'
             1494  BINARY_SUBSCR    
             1495  LOAD_FAST            13  'k'
             1498  BINARY_SUBSCR    
             1499  POP_JUMP_IF_TRUE   1482  'to 1482'

 L. 839      1502  LOAD_GLOBAL          14  'groupcache'
             1505  LOAD_GLOBAL           5  'groupcounter'
             1508  BINARY_SUBSCR    
             1509  LOAD_FAST            13  'k'
             1512  DELETE_SUBSCR    
             1513  JUMP_BACK          1482  'to 1482'
             1516  JUMP_BACK          1482  'to 1482'
             1519  POP_BLOCK        
           1520_0  COME_FROM          1465  '1465'

 L. 841      1520  LOAD_FAST             6  'args'
             1523  LOAD_GLOBAL          14  'groupcache'
             1526  LOAD_GLOBAL           5  'groupcounter'
             1529  BINARY_SUBSCR    
             1530  LOAD_CONST               'args'
             1533  STORE_SUBSCR     

 L. 842      1534  BUILD_LIST_0          0 
             1537  LOAD_GLOBAL          14  'groupcache'
             1540  LOAD_GLOBAL           5  'groupcounter'
             1543  BINARY_SUBSCR    
             1544  LOAD_CONST               'body'
             1547  STORE_SUBSCR     

 L. 843      1548  BUILD_LIST_0          0 
             1551  LOAD_GLOBAL          14  'groupcache'
             1554  LOAD_GLOBAL           5  'groupcounter'
             1557  BINARY_SUBSCR    
             1558  LOAD_CONST               'externals'
             1561  STORE_SUBSCR     

 L. 844      1562  BUILD_LIST_0          0 
             1565  LOAD_GLOBAL          14  'groupcache'
             1568  LOAD_GLOBAL           5  'groupcounter'
             1571  BINARY_SUBSCR    
             1572  LOAD_CONST               'interfaced'
             1575  STORE_SUBSCR     

 L. 845      1576  BUILD_MAP_0           0  None
             1579  LOAD_GLOBAL          14  'groupcache'
             1582  LOAD_GLOBAL           5  'groupcounter'
             1585  BINARY_SUBSCR    
             1586  LOAD_CONST               'vars'
             1589  STORE_SUBSCR     

 L. 846      1590  BUILD_MAP_0           0  None
             1593  LOAD_GLOBAL          14  'groupcache'
             1596  LOAD_GLOBAL           5  'groupcounter'
             1599  BINARY_SUBSCR    
             1600  LOAD_CONST               'entry'
             1603  STORE_SUBSCR     

 L. 848      1604  LOAD_FAST             3  'block'
             1607  LOAD_CONST               'type'
             1610  COMPARE_OP            2  ==
             1613  POP_JUMP_IF_FALSE  1633  'to 1633'

 L. 849      1616  BUILD_LIST_0          0 
             1619  LOAD_GLOBAL          14  'groupcache'
             1622  LOAD_GLOBAL           5  'groupcounter'
             1625  BINARY_SUBSCR    
             1626  LOAD_CONST               'varnames'
             1629  STORE_SUBSCR     
             1630  JUMP_FORWARD          0  'to 1633'
           1633_0  COME_FROM          1630  '1630'

 L. 851      1633  LOAD_FAST             1  'case'
             1636  LOAD_CONST               ('call', 'callfun')
             1639  COMPARE_OP            6  in
             1642  POP_JUMP_IF_FALSE  1793  'to 1793'

 L. 852      1645  LOAD_FAST             5  'name'
             1648  LOAD_GLOBAL          14  'groupcache'
             1651  LOAD_GLOBAL           5  'groupcounter'
             1654  LOAD_CONST               2
             1657  BINARY_SUBTRACT  
             1658  BINARY_SUBSCR    
             1659  LOAD_CONST               'externals'
             1662  BINARY_SUBSCR    
             1663  COMPARE_OP            7  not-in
             1666  POP_JUMP_IF_FALSE  1697  'to 1697'

 L. 853      1669  LOAD_GLOBAL          14  'groupcache'
             1672  LOAD_GLOBAL           5  'groupcounter'
             1675  LOAD_CONST               2
             1678  BINARY_SUBTRACT  
             1679  BINARY_SUBSCR    
             1680  LOAD_CONST               'externals'
             1683  BINARY_SUBSCR    
             1684  LOAD_ATTR            30  'append'
             1687  LOAD_FAST             5  'name'
             1690  CALL_FUNCTION_1       1  None
             1693  POP_TOP          
             1694  JUMP_FORWARD          0  'to 1697'
           1697_0  COME_FROM          1694  '1694'

 L. 854      1697  LOAD_GLOBAL          31  'copy'
             1700  LOAD_ATTR            32  'deepcopy'
             1703  LOAD_GLOBAL          14  'groupcache'
             1706  LOAD_GLOBAL           5  'groupcounter'
             1709  LOAD_CONST               2
             1712  BINARY_SUBTRACT  
             1713  BINARY_SUBSCR    
             1714  LOAD_CONST               'vars'
             1717  BINARY_SUBSCR    
             1718  CALL_FUNCTION_1       1  None
             1721  LOAD_GLOBAL          14  'groupcache'
             1724  LOAD_GLOBAL           5  'groupcounter'
             1727  BINARY_SUBSCR    
             1728  LOAD_CONST               'vars'
             1731  STORE_SUBSCR     

 L. 857      1732  SETUP_EXCEPT         48  'to 1783'
             1735  LOAD_GLOBAL          14  'groupcache'
             1738  LOAD_GLOBAL           5  'groupcounter'
             1741  BINARY_SUBSCR    
             1742  LOAD_CONST               'vars'
             1745  BINARY_SUBSCR    
             1746  LOAD_FAST             5  'name'
             1749  BINARY_SUBSCR    
             1750  LOAD_GLOBAL          14  'groupcache'
             1753  LOAD_GLOBAL           5  'groupcounter'
             1756  BINARY_SUBSCR    
             1757  LOAD_CONST               'vars'
             1760  BINARY_SUBSCR    
             1761  LOAD_FAST             5  'name'
             1764  BINARY_SUBSCR    
             1765  LOAD_CONST               'attrspec'
             1768  BINARY_SUBSCR    
             1769  LOAD_ATTR            33  'index'
             1772  LOAD_CONST               'external'
             1775  CALL_FUNCTION_1       1  None
             1778  DELETE_SUBSCR    
             1779  POP_BLOCK        
             1780  JUMP_ABSOLUTE      1793  'to 1793'
           1783_0  COME_FROM          1732  '1732'

 L. 858      1783  POP_TOP          
             1784  POP_TOP          
             1785  POP_TOP          
             1786  JUMP_ABSOLUTE      1793  'to 1793'
             1789  END_FINALLY      
           1790_0  COME_FROM          1789  '1789'
             1790  JUMP_FORWARD          0  'to 1793'
           1793_0  COME_FROM          1790  '1790'

 L. 859      1793  LOAD_FAST             3  'block'
             1796  LOAD_CONST               ('function', 'subroutine')
             1799  COMPARE_OP            6  in
             1802  POP_JUMP_IF_FALSE  2026  'to 2026'

 L. 860      1805  SETUP_EXCEPT         59  'to 1867'
             1808  LOAD_GLOBAL          34  'appenddecl'
             1811  LOAD_GLOBAL          14  'groupcache'
             1814  LOAD_GLOBAL           5  'groupcounter'
             1817  BINARY_SUBSCR    
             1818  LOAD_CONST               'vars'
             1821  BINARY_SUBSCR    
             1822  LOAD_FAST             5  'name'
             1825  BINARY_SUBSCR    
             1826  LOAD_GLOBAL          14  'groupcache'
             1829  LOAD_GLOBAL           5  'groupcounter'
             1832  LOAD_CONST               2
             1835  BINARY_SUBTRACT  
             1836  BINARY_SUBSCR    
             1837  LOAD_CONST               'vars'
             1840  BINARY_SUBSCR    
             1841  LOAD_CONST               ''
             1844  BINARY_SUBSCR    
             1845  CALL_FUNCTION_2       2  None
             1848  LOAD_GLOBAL          14  'groupcache'
             1851  LOAD_GLOBAL           5  'groupcounter'
             1854  BINARY_SUBSCR    
             1855  LOAD_CONST               'vars'
             1858  BINARY_SUBSCR    
             1859  LOAD_FAST             5  'name'
             1862  STORE_SUBSCR     
             1863  POP_BLOCK        
             1864  JUMP_FORWARD          7  'to 1874'
           1867_0  COME_FROM          1805  '1805'

 L. 861      1867  POP_TOP          
             1868  POP_TOP          
             1869  POP_TOP          
             1870  JUMP_FORWARD          1  'to 1874'
             1873  END_FINALLY      
           1874_0  COME_FROM          1873  '1873'
           1874_1  COME_FROM          1864  '1864'

 L. 862      1874  LOAD_FAST             1  'case'
             1877  LOAD_CONST               'callfun'
             1880  COMPARE_OP            2  ==
             1883  POP_JUMP_IF_FALSE  1984  'to 1984'

 L. 863      1886  LOAD_FAST             7  'result'
             1889  POP_JUMP_IF_FALSE  1984  'to 1984'
             1892  LOAD_FAST             7  'result'
             1895  LOAD_GLOBAL          14  'groupcache'
             1898  LOAD_GLOBAL           5  'groupcounter'
             1901  BINARY_SUBSCR    
             1902  LOAD_CONST               'vars'
             1905  BINARY_SUBSCR    
             1906  COMPARE_OP            6  in
           1909_0  COME_FROM          1889  '1889'
             1909  POP_JUMP_IF_FALSE  1984  'to 1984'

 L. 864      1912  LOAD_FAST             5  'name'
             1915  LOAD_FAST             7  'result'
             1918  COMPARE_OP            2  ==
             1921  POP_JUMP_IF_TRUE   1981  'to 1981'

 L. 865      1924  LOAD_GLOBAL          34  'appenddecl'
             1927  LOAD_GLOBAL          14  'groupcache'
             1930  LOAD_GLOBAL           5  'groupcounter'
             1933  BINARY_SUBSCR    
             1934  LOAD_CONST               'vars'
             1937  BINARY_SUBSCR    
             1938  LOAD_FAST             5  'name'
             1941  BINARY_SUBSCR    
             1942  LOAD_GLOBAL          14  'groupcache'
             1945  LOAD_GLOBAL           5  'groupcounter'
             1948  BINARY_SUBSCR    
             1949  LOAD_CONST               'vars'
             1952  BINARY_SUBSCR    
             1953  LOAD_FAST             7  'result'
             1956  BINARY_SUBSCR    
             1957  CALL_FUNCTION_2       2  None
             1960  LOAD_GLOBAL          14  'groupcache'
             1963  LOAD_GLOBAL           5  'groupcounter'
             1966  BINARY_SUBSCR    
             1967  LOAD_CONST               'vars'
             1970  BINARY_SUBSCR    
             1971  LOAD_FAST             5  'name'
             1974  STORE_SUBSCR     
             1975  JUMP_ABSOLUTE      1981  'to 1981'
             1978  JUMP_ABSOLUTE      1984  'to 1984'
             1981  JUMP_FORWARD          0  'to 1984'
           1984_0  COME_FROM          1981  '1981'

 L. 867      1984  SETUP_EXCEPT         29  'to 2016'
             1987  LOAD_GLOBAL          14  'groupcache'
             1990  LOAD_GLOBAL           5  'groupcounter'
             1993  LOAD_CONST               2
             1996  BINARY_SUBTRACT  
             1997  BINARY_SUBSCR    
             1998  LOAD_CONST               'interfaced'
             2001  BINARY_SUBSCR    
             2002  LOAD_ATTR            30  'append'
             2005  LOAD_FAST             5  'name'
             2008  CALL_FUNCTION_1       1  None
             2011  POP_TOP          
             2012  POP_BLOCK        
             2013  JUMP_ABSOLUTE      2026  'to 2026'
           2016_0  COME_FROM          1984  '1984'

 L. 868      2016  POP_TOP          
             2017  POP_TOP          
             2018  POP_TOP          
             2019  JUMP_ABSOLUTE      2026  'to 2026'
             2022  END_FINALLY      
           2023_0  COME_FROM          2022  '2022'
             2023  JUMP_FORWARD          0  'to 2026'
           2026_0  COME_FROM          2023  '2023'

 L. 869      2026  LOAD_FAST             3  'block'
             2029  LOAD_CONST               'function'
             2032  COMPARE_OP            2  ==
             2035  POP_JUMP_IF_FALSE  2150  'to 2150'

 L. 870      2038  LOAD_GLOBAL          35  'typespattern'
             2041  LOAD_CONST               0
             2044  BINARY_SUBSCR    
             2045  LOAD_ATTR            18  'match'
             2048  LOAD_FAST             0  'm'
             2051  LOAD_ATTR             0  'group'
             2054  LOAD_CONST               'before'
             2057  CALL_FUNCTION_1       1  None
             2060  LOAD_CONST               ' '
             2063  BINARY_ADD       
             2064  LOAD_FAST             5  'name'
             2067  BINARY_ADD       
             2068  CALL_FUNCTION_1       1  None
             2071  STORE_FAST           14  't'

 L. 871      2074  LOAD_FAST            14  't'
             2077  POP_JUMP_IF_FALSE  2150  'to 2150'

 L. 872      2080  LOAD_GLOBAL          36  'cracktypespec0'
             2083  LOAD_FAST            14  't'
             2086  LOAD_ATTR             0  'group'
             2089  LOAD_CONST               'this'
             2092  CALL_FUNCTION_1       1  None
             2095  LOAD_FAST            14  't'
             2098  LOAD_ATTR             0  'group'
             2101  LOAD_CONST               'after'
             2104  CALL_FUNCTION_1       1  None
             2107  CALL_FUNCTION_2       2  None
             2110  UNPACK_SEQUENCE_4     4 
             2113  STORE_FAST           15  'typespec'
             2116  STORE_FAST           16  'selector'
             2119  STORE_FAST           17  'attr'
             2122  STORE_FAST           18  'edecl'

 L. 873      2125  LOAD_GLOBAL          37  'updatevars'
             2128  LOAD_FAST            15  'typespec'
             2131  LOAD_FAST            16  'selector'
             2134  LOAD_FAST            17  'attr'
             2137  LOAD_FAST            18  'edecl'
             2140  CALL_FUNCTION_4       4  None
             2143  POP_TOP          
             2144  JUMP_ABSOLUTE      2150  'to 2150'
             2147  JUMP_FORWARD          0  'to 2150'
           2150_0  COME_FROM          2147  '2147'

 L. 875      2150  LOAD_FAST             1  'case'
             2153  LOAD_CONST               ('call', 'callfun')
             2156  COMPARE_OP            6  in
             2159  POP_JUMP_IF_FALSE  7502  'to 7502'

 L. 876      2162  LOAD_GLOBAL          15  'grouplist'
             2165  LOAD_GLOBAL           5  'groupcounter'
             2168  LOAD_CONST               1
             2171  BINARY_SUBTRACT  
             2172  BINARY_SUBSCR    
             2173  LOAD_ATTR            30  'append'
             2176  LOAD_GLOBAL          14  'groupcache'
             2179  LOAD_GLOBAL           5  'groupcounter'
             2182  BINARY_SUBSCR    
             2183  CALL_FUNCTION_1       1  None
             2186  POP_TOP          

 L. 877      2187  LOAD_GLOBAL          15  'grouplist'
             2190  LOAD_GLOBAL           5  'groupcounter'
             2193  BINARY_SUBSCR    
             2194  LOAD_GLOBAL          15  'grouplist'
             2197  LOAD_GLOBAL           5  'groupcounter'
             2200  LOAD_CONST               1
             2203  BINARY_SUBTRACT  
             2204  BINARY_SUBSCR    
             2205  LOAD_CONST               -1
             2208  BINARY_SUBSCR    
             2209  LOAD_CONST               'body'
             2212  STORE_SUBSCR     

 L. 878      2213  LOAD_GLOBAL          15  'grouplist'
             2216  LOAD_GLOBAL           5  'groupcounter'
             2219  DELETE_SUBSCR    

 L. 879      2220  LOAD_GLOBAL           5  'groupcounter'
             2223  LOAD_CONST               1
             2226  BINARY_SUBTRACT  
             2227  STORE_GLOBAL          5  'groupcounter'

 L. 880      2230  LOAD_GLOBAL          15  'grouplist'
             2233  LOAD_GLOBAL           5  'groupcounter'
             2236  LOAD_CONST               1
             2239  BINARY_SUBTRACT  
             2240  BINARY_SUBSCR    
             2241  LOAD_ATTR            30  'append'
             2244  LOAD_GLOBAL          14  'groupcache'
             2247  LOAD_GLOBAL           5  'groupcounter'
             2250  BINARY_SUBSCR    
             2251  CALL_FUNCTION_1       1  None
             2254  POP_TOP          

 L. 881      2255  LOAD_GLOBAL          15  'grouplist'
             2258  LOAD_GLOBAL           5  'groupcounter'
             2261  BINARY_SUBSCR    
             2262  LOAD_GLOBAL          15  'grouplist'
             2265  LOAD_GLOBAL           5  'groupcounter'
             2268  LOAD_CONST               1
             2271  BINARY_SUBTRACT  
             2272  BINARY_SUBSCR    
             2273  LOAD_CONST               -1
             2276  BINARY_SUBSCR    
             2277  LOAD_CONST               'body'
             2280  STORE_SUBSCR     

 L. 882      2281  LOAD_GLOBAL          15  'grouplist'
             2284  LOAD_GLOBAL           5  'groupcounter'
             2287  DELETE_SUBSCR    

 L. 883      2288  LOAD_GLOBAL           5  'groupcounter'
             2291  LOAD_CONST               1
             2294  BINARY_SUBTRACT  
             2295  STORE_GLOBAL          5  'groupcounter'
             2298  JUMP_ABSOLUTE      7502  'to 7502'
             2301  JUMP_FORWARD       5198  'to 7502'

 L. 885      2304  LOAD_FAST             1  'case'
             2307  LOAD_CONST               'entry'
             2310  COMPARE_OP            2  ==
             2313  POP_JUMP_IF_FALSE  2492  'to 2492'

 L. 886      2316  LOAD_GLOBAL          20  '_resolvenameargspattern'
             2319  LOAD_FAST             0  'm'
             2322  LOAD_ATTR             0  'group'
             2325  LOAD_CONST               'after'
             2328  CALL_FUNCTION_1       1  None
             2331  CALL_FUNCTION_1       1  None
             2334  UNPACK_SEQUENCE_4     4 
             2337  STORE_FAST            5  'name'
             2340  STORE_FAST            6  'args'
             2343  STORE_FAST            7  'result'
             2346  STORE_FAST            8  'bind'

 L. 887      2349  LOAD_FAST             5  'name'
             2352  LOAD_CONST               None
             2355  COMPARE_OP            9  is-not
             2358  POP_JUMP_IF_FALSE  7502  'to 7502'

 L. 888      2361  LOAD_FAST             6  'args'
             2364  POP_JUMP_IF_FALSE  2422  'to 2422'

 L. 889      2367  LOAD_GLOBAL          21  'rmbadname'
             2370  BUILD_LIST_0          0 
             2373  LOAD_GLOBAL          22  'markoutercomma'
             2376  LOAD_FAST             6  'args'
             2379  CALL_FUNCTION_1       1  None
             2382  LOAD_ATTR            10  'split'
             2385  LOAD_CONST               '@,@'
             2388  CALL_FUNCTION_1       1  None
             2391  GET_ITER         
             2392  FOR_ITER             18  'to 2413'
             2395  STORE_FAST            9  'x'
             2398  LOAD_FAST             9  'x'
             2401  LOAD_ATTR            23  'strip'
             2404  CALL_FUNCTION_0       0  None
             2407  LIST_APPEND           2  None
             2410  JUMP_BACK          2392  'to 2392'
             2413  CALL_FUNCTION_1       1  None
             2416  STORE_FAST            6  'args'
             2419  JUMP_FORWARD          6  'to 2428'

 L. 890      2422  BUILD_LIST_0          0 
             2425  STORE_FAST            6  'args'
           2428_0  COME_FROM          2419  '2419'

 L. 891      2428  LOAD_FAST             7  'result'
             2431  LOAD_CONST               None
             2434  COMPARE_OP            8  is
             2437  POP_JUMP_IF_TRUE   2453  'to 2453'
             2440  LOAD_ASSERT              AssertionError
             2443  LOAD_FAST             7  'result'
             2446  UNARY_CONVERT    
             2447  CALL_FUNCTION_1       1  None
             2450  RAISE_VARARGS_1       1  None

 L. 892      2453  LOAD_FAST             6  'args'
             2456  LOAD_GLOBAL          14  'groupcache'
             2459  LOAD_GLOBAL           5  'groupcounter'
             2462  BINARY_SUBSCR    
             2463  LOAD_CONST               'entry'
             2466  BINARY_SUBSCR    
             2467  LOAD_FAST             5  'name'
             2470  STORE_SUBSCR     

 L. 893      2471  LOAD_CONST               'entry'
             2474  LOAD_FAST             5  'name'
             2477  LOAD_GLOBAL           5  'groupcounter'
             2480  BUILD_TUPLE_3         3 
             2483  STORE_GLOBAL          2  'previous_context'
             2486  JUMP_ABSOLUTE      7502  'to 7502'
             2489  JUMP_FORWARD       5010  'to 7502'

 L. 894      2492  LOAD_FAST             1  'case'
             2495  LOAD_CONST               'type'
             2498  COMPARE_OP            2  ==
             2501  POP_JUMP_IF_FALSE  2594  'to 2594'

 L. 895      2504  LOAD_GLOBAL          36  'cracktypespec0'
             2507  LOAD_FAST             3  'block'
             2510  LOAD_FAST             0  'm'
             2513  LOAD_ATTR             0  'group'
             2516  LOAD_CONST               'after'
             2519  CALL_FUNCTION_1       1  None
             2522  CALL_FUNCTION_2       2  None
             2525  UNPACK_SEQUENCE_4     4 
             2528  STORE_FAST           15  'typespec'
             2531  STORE_FAST           16  'selector'
             2534  STORE_FAST           17  'attr'
             2537  STORE_FAST           18  'edecl'

 L. 896      2540  LOAD_GLOBAL          37  'updatevars'
             2543  LOAD_FAST            15  'typespec'
             2546  LOAD_FAST            16  'selector'
             2549  LOAD_FAST            17  'attr'
             2552  LOAD_FAST            18  'edecl'
             2555  CALL_FUNCTION_4       4  None
             2558  STORE_FAST           19  'last_name'

 L. 897      2561  LOAD_FAST            19  'last_name'
             2564  LOAD_CONST               None
             2567  COMPARE_OP            9  is-not
             2570  POP_JUMP_IF_FALSE  7502  'to 7502'

 L. 898      2573  LOAD_CONST               'variable'
             2576  LOAD_FAST            19  'last_name'
             2579  LOAD_GLOBAL           5  'groupcounter'
             2582  BUILD_TUPLE_3         3 
             2585  STORE_GLOBAL          2  'previous_context'
             2588  JUMP_ABSOLUTE      7502  'to 7502'
             2591  JUMP_FORWARD       4908  'to 7502'

 L. 899      2594  LOAD_FAST             1  'case'
             2597  LOAD_CONST               ('dimension', 'intent', 'optional', 'required', 'external', 'public', 'private', 'intrisic')
             2600  COMPARE_OP            6  in
             2603  POP_JUMP_IF_FALSE  3696  'to 3696'

 L. 900      2606  LOAD_GLOBAL          14  'groupcache'
             2609  LOAD_GLOBAL           5  'groupcounter'
             2612  BINARY_SUBSCR    
             2613  LOAD_CONST               'vars'
             2616  BINARY_SUBSCR    
             2617  STORE_FAST           18  'edecl'

 L. 901      2620  LOAD_FAST             0  'm'
             2623  LOAD_ATTR             0  'group'
             2626  LOAD_CONST               'after'
             2629  CALL_FUNCTION_1       1  None
             2632  LOAD_ATTR            23  'strip'
             2635  CALL_FUNCTION_0       0  None
             2638  STORE_FAST           20  'll'

 L. 902      2641  LOAD_FAST            20  'll'
             2644  LOAD_ATTR            39  'find'
             2647  LOAD_CONST               '::'
             2650  CALL_FUNCTION_1       1  None
             2653  STORE_FAST           21  'i'

 L. 903      2656  LOAD_FAST            21  'i'
             2659  LOAD_CONST               0
             2662  COMPARE_OP            0  <
             2665  POP_JUMP_IF_FALSE  2848  'to 2848'
             2668  LOAD_FAST             1  'case'
             2671  LOAD_CONST               'intent'
             2674  COMPARE_OP            2  ==
           2677_0  COME_FROM          2665  '2665'
             2677  POP_JUMP_IF_FALSE  2848  'to 2848'

 L. 904      2680  LOAD_GLOBAL          40  'markouterparen'
             2683  LOAD_FAST            20  'll'
             2686  CALL_FUNCTION_1       1  None
             2689  LOAD_ATTR            39  'find'
             2692  LOAD_CONST               '@)@'
             2695  CALL_FUNCTION_1       1  None
             2698  LOAD_CONST               2
             2701  BINARY_SUBTRACT  
             2702  STORE_FAST           21  'i'

 L. 905      2705  LOAD_FAST            20  'll'
             2708  LOAD_FAST            21  'i'
             2711  LOAD_CONST               1
             2714  BINARY_ADD       
             2715  SLICE+2          
             2716  LOAD_CONST               '::'
             2719  BINARY_ADD       
             2720  LOAD_FAST            20  'll'
             2723  LOAD_FAST            21  'i'
             2726  LOAD_CONST               1
             2729  BINARY_ADD       
             2730  SLICE+1          
             2731  BINARY_ADD       
             2732  STORE_FAST           20  'll'

 L. 906      2735  LOAD_FAST            20  'll'
             2738  LOAD_ATTR            39  'find'
             2741  LOAD_CONST               '::'
             2744  CALL_FUNCTION_1       1  None
             2747  STORE_FAST           21  'i'

 L. 907      2750  LOAD_FAST            20  'll'
             2753  LOAD_FAST            21  'i'
             2756  SLICE+1          
             2757  LOAD_CONST               '::'
             2760  COMPARE_OP            2  ==
             2763  POP_JUMP_IF_FALSE  2848  'to 2848'
             2766  LOAD_CONST               'args'
             2769  LOAD_GLOBAL          14  'groupcache'
             2772  LOAD_GLOBAL           5  'groupcounter'
             2775  BINARY_SUBSCR    
             2776  COMPARE_OP            6  in
           2779_0  COME_FROM          2763  '2763'
             2779  POP_JUMP_IF_FALSE  2848  'to 2848'

 L. 908      2782  LOAD_GLOBAL          11  'outmess'
             2785  LOAD_CONST               'All arguments will have attribute %s%s\n'
             2788  LOAD_FAST             0  'm'
             2791  LOAD_ATTR             0  'group'
             2794  LOAD_CONST               'this'
             2797  CALL_FUNCTION_1       1  None
             2800  LOAD_FAST            20  'll'
             2803  LOAD_FAST            21  'i'
             2806  SLICE+2          
             2807  BUILD_TUPLE_2         2 
             2810  BINARY_MODULO    
             2811  CALL_FUNCTION_1       1  None
             2814  POP_TOP          

 L. 909      2815  LOAD_FAST            20  'll'
             2818  LOAD_CONST               ','
             2821  LOAD_ATTR            41  'join'
             2824  LOAD_GLOBAL          14  'groupcache'
             2827  LOAD_GLOBAL           5  'groupcounter'
             2830  BINARY_SUBSCR    
             2831  LOAD_CONST               'args'
             2834  BINARY_SUBSCR    
             2835  CALL_FUNCTION_1       1  None
             2838  BINARY_ADD       
             2839  STORE_FAST           20  'll'
             2842  JUMP_ABSOLUTE      2848  'to 2848'
             2845  JUMP_FORWARD          0  'to 2848'
           2848_0  COME_FROM          2845  '2845'

 L. 910      2848  LOAD_FAST            21  'i'
             2851  LOAD_CONST               0
             2854  COMPARE_OP            0  <
             2857  POP_JUMP_IF_FALSE  2875  'to 2875'
             2860  LOAD_CONST               0
             2863  STORE_FAST           21  'i'
             2866  LOAD_CONST               ''
             2869  STORE_FAST           22  'pl'
             2872  JUMP_FORWARD         30  'to 2905'

 L. 911      2875  LOAD_FAST            20  'll'
             2878  LOAD_FAST            21  'i'
             2881  SLICE+2          
             2882  LOAD_ATTR            23  'strip'
             2885  CALL_FUNCTION_0       0  None
             2888  STORE_FAST           22  'pl'
             2891  LOAD_FAST            20  'll'
             2894  LOAD_FAST            21  'i'
             2897  LOAD_CONST               2
             2900  BINARY_ADD       
             2901  SLICE+1          
             2902  STORE_FAST           20  'll'
           2905_0  COME_FROM          2872  '2872'

 L. 912      2905  LOAD_GLOBAL          22  'markoutercomma'
             2908  LOAD_FAST            22  'pl'
             2911  CALL_FUNCTION_1       1  None
             2914  LOAD_ATTR            10  'split'
             2917  LOAD_CONST               '@,@'
             2920  CALL_FUNCTION_1       1  None
             2923  STORE_FAST           23  'ch'

 L. 913      2926  LOAD_GLOBAL          42  'len'
             2929  LOAD_FAST            23  'ch'
             2932  CALL_FUNCTION_1       1  None
             2935  LOAD_CONST               1
             2938  COMPARE_OP            4  >
             2941  POP_JUMP_IF_FALSE  2984  'to 2984'

 L. 914      2944  LOAD_FAST            23  'ch'
             2947  LOAD_CONST               0
             2950  BINARY_SUBSCR    
             2951  STORE_FAST           22  'pl'

 L. 915      2954  LOAD_GLOBAL          11  'outmess'
             2957  LOAD_CONST               'analyzeline: cannot handle multiple attributes without type specification. Ignoring %r.\n'
             2960  LOAD_CONST               ','
             2963  LOAD_ATTR            41  'join'
             2966  LOAD_FAST            23  'ch'
             2969  LOAD_CONST               1
             2972  SLICE+1          
             2973  CALL_FUNCTION_1       1  None
             2976  BINARY_MODULO    
             2977  CALL_FUNCTION_1       1  None
             2980  POP_TOP          
             2981  JUMP_FORWARD          0  'to 2984'
           2984_0  COME_FROM          2981  '2981'

 L. 916      2984  LOAD_CONST               None
             2987  STORE_FAST           19  'last_name'

 L. 918      2990  SETUP_LOOP          656  'to 3649'
             2993  BUILD_LIST_0          0 
             2996  LOAD_GLOBAL          22  'markoutercomma'
             2999  LOAD_FAST            20  'll'
             3002  CALL_FUNCTION_1       1  None
             3005  LOAD_ATTR            10  'split'
             3008  LOAD_CONST               '@,@'
             3011  CALL_FUNCTION_1       1  None
             3014  GET_ITER         
             3015  FOR_ITER             18  'to 3036'
             3018  STORE_FAST            9  'x'
             3021  LOAD_FAST             9  'x'
             3024  LOAD_ATTR            23  'strip'
             3027  CALL_FUNCTION_0       0  None
             3030  LIST_APPEND           2  None
             3033  JUMP_BACK          3015  'to 3015'
             3036  GET_ITER         
             3037  FOR_ITER            608  'to 3648'
             3040  STORE_FAST           24  'e'

 L. 919      3043  LOAD_GLOBAL          43  'namepattern'
             3046  LOAD_ATTR            18  'match'
             3049  LOAD_FAST            24  'e'
             3052  CALL_FUNCTION_1       1  None
             3055  STORE_FAST           25  'm1'

 L. 920      3058  LOAD_FAST            25  'm1'
             3061  POP_JUMP_IF_TRUE   3123  'to 3123'

 L. 921      3064  LOAD_FAST             1  'case'
             3067  LOAD_CONST               ('public', 'private')
             3070  COMPARE_OP            6  in
             3073  POP_JUMP_IF_FALSE  3085  'to 3085'
             3076  LOAD_CONST               ''
             3079  STORE_FAST           13  'k'
             3082  JUMP_ABSOLUTE      3144  'to 3144'

 L. 923      3085  LOAD_FAST             0  'm'
             3088  LOAD_ATTR            44  'groupdict'
             3091  CALL_FUNCTION_0       0  None
             3094  PRINT_ITEM       
             3095  PRINT_NEWLINE_CONT

 L. 924      3096  LOAD_GLOBAL          11  'outmess'
             3099  LOAD_CONST               'analyzeline: no name pattern found in %s statement for %s. Skipping.\n'
             3102  LOAD_FAST             1  'case'
             3105  LOAD_FAST            24  'e'
             3108  UNARY_CONVERT    
             3109  BUILD_TUPLE_2         2 
             3112  BINARY_MODULO    
             3113  CALL_FUNCTION_1       1  None
             3116  POP_TOP          

 L. 925      3117  CONTINUE           3037  'to 3037'
             3120  JUMP_FORWARD         21  'to 3144'

 L. 927      3123  LOAD_GLOBAL          28  'rmbadname1'
             3126  LOAD_FAST            25  'm1'
             3129  LOAD_ATTR             0  'group'
             3132  LOAD_CONST               'name'
             3135  CALL_FUNCTION_1       1  None
             3138  CALL_FUNCTION_1       1  None
             3141  STORE_FAST           13  'k'
           3144_0  COME_FROM          3120  '3120'

 L. 928      3144  LOAD_FAST            13  'k'
             3147  LOAD_FAST            18  'edecl'
             3150  COMPARE_OP            7  not-in
             3153  POP_JUMP_IF_FALSE  3169  'to 3169'

 L. 929      3156  BUILD_MAP_0           0  None
             3159  LOAD_FAST            18  'edecl'
             3162  LOAD_FAST            13  'k'
             3165  STORE_SUBSCR     
             3166  JUMP_FORWARD          0  'to 3169'
           3169_0  COME_FROM          3166  '3166'

 L. 930      3169  LOAD_FAST             1  'case'
             3172  LOAD_CONST               'dimension'
             3175  COMPARE_OP            2  ==
             3178  POP_JUMP_IF_FALSE  3203  'to 3203'

 L. 931      3181  LOAD_FAST             1  'case'
             3184  LOAD_FAST            25  'm1'
             3187  LOAD_ATTR             0  'group'
             3190  LOAD_CONST               'after'
             3193  CALL_FUNCTION_1       1  None
             3196  BINARY_ADD       
             3197  STORE_FAST           26  'ap'
             3200  JUMP_FORWARD          0  'to 3203'
           3203_0  COME_FROM          3200  '3200'

 L. 932      3203  LOAD_FAST             1  'case'
             3206  LOAD_CONST               'intent'
             3209  COMPARE_OP            2  ==
             3212  POP_JUMP_IF_FALSE  3430  'to 3430'

 L. 933      3215  LOAD_FAST             0  'm'
             3218  LOAD_ATTR             0  'group'
             3221  LOAD_CONST               'this'
             3224  CALL_FUNCTION_1       1  None
             3227  LOAD_FAST            22  'pl'
             3230  BINARY_ADD       
             3231  STORE_FAST           26  'ap'

 L. 934      3234  LOAD_GLOBAL          45  '_intentcallbackpattern'
             3237  LOAD_ATTR            18  'match'
             3240  LOAD_FAST            26  'ap'
             3243  CALL_FUNCTION_1       1  None
             3246  POP_JUMP_IF_FALSE  3430  'to 3430'

 L. 935      3249  LOAD_FAST            13  'k'
             3252  LOAD_GLOBAL          14  'groupcache'
             3255  LOAD_GLOBAL           5  'groupcounter'
             3258  BINARY_SUBSCR    
             3259  LOAD_CONST               'args'
             3262  BINARY_SUBSCR    
             3263  COMPARE_OP            7  not-in
             3266  POP_JUMP_IF_FALSE  3410  'to 3410'

 L. 936      3269  LOAD_GLOBAL           5  'groupcounter'
             3272  LOAD_CONST               1
             3275  COMPARE_OP            4  >
             3278  POP_JUMP_IF_FALSE  3393  'to 3393'

 L. 937      3281  LOAD_CONST               '__user__'
             3284  LOAD_GLOBAL          14  'groupcache'
             3287  LOAD_GLOBAL           5  'groupcounter'
             3290  LOAD_CONST               2
             3293  BINARY_SUBTRACT  
             3294  BINARY_SUBSCR    
             3295  LOAD_CONST               'name'
             3298  BINARY_SUBSCR    
             3299  COMPARE_OP            7  not-in
             3302  POP_JUMP_IF_FALSE  3318  'to 3318'

 L. 938      3305  LOAD_GLOBAL          11  'outmess'
             3308  LOAD_CONST               'analyzeline: missing __user__ module (could be nothing)\n'
             3311  CALL_FUNCTION_1       1  None
             3314  POP_TOP          
             3315  JUMP_FORWARD          0  'to 3318'
           3318_0  COME_FROM          3315  '3315'

 L. 939      3318  LOAD_FAST            13  'k'
             3321  LOAD_GLOBAL          14  'groupcache'
             3324  LOAD_GLOBAL           5  'groupcounter'
             3327  BINARY_SUBSCR    
             3328  LOAD_CONST               'name'
             3331  BINARY_SUBSCR    
             3332  COMPARE_OP            3  !=
             3335  POP_JUMP_IF_FALSE  3407  'to 3407'

 L. 940      3338  LOAD_GLOBAL          11  'outmess'
             3341  LOAD_CONST               'analyzeline: appending intent(callback) %s to %s arguments\n'

 L. 941      3344  LOAD_FAST            13  'k'
             3347  LOAD_GLOBAL          14  'groupcache'
             3350  LOAD_GLOBAL           5  'groupcounter'
             3353  BINARY_SUBSCR    
             3354  LOAD_CONST               'name'
             3357  BINARY_SUBSCR    
             3358  BUILD_TUPLE_2         2 
             3361  BINARY_MODULO    
             3362  CALL_FUNCTION_1       1  None
             3365  POP_TOP          

 L. 942      3366  LOAD_GLOBAL          14  'groupcache'
             3369  LOAD_GLOBAL           5  'groupcounter'
             3372  BINARY_SUBSCR    
             3373  LOAD_CONST               'args'
             3376  BINARY_SUBSCR    
             3377  LOAD_ATTR            30  'append'
             3380  LOAD_FAST            13  'k'
             3383  CALL_FUNCTION_1       1  None
             3386  POP_TOP          
             3387  JUMP_ABSOLUTE      3407  'to 3407'
             3390  JUMP_ABSOLUTE      3424  'to 3424'

 L. 944      3393  LOAD_GLOBAL          46  'errmess'
             3396  LOAD_CONST               'analyzeline: intent(callback) %s is ignored'
             3399  LOAD_FAST            13  'k'
             3402  BINARY_MODULO    
             3403  CALL_FUNCTION_1       1  None
             3406  POP_TOP          
             3407  JUMP_ABSOLUTE      3427  'to 3427'

 L. 946      3410  LOAD_GLOBAL          46  'errmess'
             3413  LOAD_CONST               'analyzeline: intent(callback) %s is already in argument list'

 L. 947      3416  LOAD_FAST            13  'k'
             3419  BINARY_MODULO    
             3420  CALL_FUNCTION_1       1  None
             3423  POP_TOP          
             3424  JUMP_ABSOLUTE      3430  'to 3430'
             3427  JUMP_FORWARD          0  'to 3430'
           3430_0  COME_FROM          3427  '3427'

 L. 948      3430  LOAD_FAST             1  'case'
             3433  LOAD_CONST               ('optional', 'required', 'public', 'external', 'private', 'intrisic')
             3436  COMPARE_OP            6  in
             3439  POP_JUMP_IF_FALSE  3451  'to 3451'

 L. 949      3442  LOAD_FAST             1  'case'
             3445  STORE_FAST           26  'ap'
             3448  JUMP_FORWARD          0  'to 3451'
           3451_0  COME_FROM          3448  '3448'

 L. 950      3451  LOAD_CONST               'attrspec'
             3454  LOAD_FAST            18  'edecl'
             3457  LOAD_FAST            13  'k'
             3460  BINARY_SUBSCR    
             3461  COMPARE_OP            6  in
             3464  POP_JUMP_IF_FALSE  3491  'to 3491'

 L. 951      3467  LOAD_FAST            18  'edecl'
             3470  LOAD_FAST            13  'k'
             3473  BINARY_SUBSCR    
             3474  LOAD_CONST               'attrspec'
             3477  BINARY_SUBSCR    
             3478  LOAD_ATTR            30  'append'
             3481  LOAD_FAST            26  'ap'
             3484  CALL_FUNCTION_1       1  None
             3487  POP_TOP          
             3488  JUMP_FORWARD         17  'to 3508'

 L. 953      3491  LOAD_FAST            26  'ap'
             3494  BUILD_LIST_1          1 
             3497  LOAD_FAST            18  'edecl'
             3500  LOAD_FAST            13  'k'
             3503  BINARY_SUBSCR    
             3504  LOAD_CONST               'attrspec'
             3507  STORE_SUBSCR     
           3508_0  COME_FROM          3488  '3488'

 L. 954      3508  LOAD_FAST             1  'case'
             3511  LOAD_CONST               'external'
             3514  COMPARE_OP            2  ==
             3517  POP_JUMP_IF_FALSE  3639  'to 3639'

 L. 955      3520  LOAD_GLOBAL          14  'groupcache'
             3523  LOAD_GLOBAL           5  'groupcounter'
             3526  BINARY_SUBSCR    
             3527  LOAD_CONST               'block'
             3530  BINARY_SUBSCR    
             3531  LOAD_CONST               'program'
             3534  COMPARE_OP            2  ==
             3537  POP_JUMP_IF_FALSE  3556  'to 3556'

 L. 956      3540  LOAD_GLOBAL          11  'outmess'
             3543  LOAD_CONST               'analyzeline: ignoring program arguments\n'
             3546  CALL_FUNCTION_1       1  None
             3549  POP_TOP          

 L. 957      3550  CONTINUE           3037  'to 3037'
             3553  JUMP_FORWARD          0  'to 3556'
           3556_0  COME_FROM          3553  '3553'

 L. 958      3556  LOAD_FAST            13  'k'
             3559  LOAD_GLOBAL          14  'groupcache'
             3562  LOAD_GLOBAL           5  'groupcounter'
             3565  BINARY_SUBSCR    
             3566  LOAD_CONST               'args'
             3569  BINARY_SUBSCR    
             3570  COMPARE_OP            7  not-in
             3573  POP_JUMP_IF_FALSE  3582  'to 3582'

 L. 960      3576  CONTINUE           3037  'to 3037'
             3579  JUMP_FORWARD          0  'to 3582'
           3582_0  COME_FROM          3579  '3579'

 L. 961      3582  LOAD_CONST               'externals'
             3585  LOAD_GLOBAL          14  'groupcache'
             3588  LOAD_GLOBAL           5  'groupcounter'
             3591  BINARY_SUBSCR    
             3592  COMPARE_OP            7  not-in
             3595  POP_JUMP_IF_FALSE  3615  'to 3615'

 L. 962      3598  BUILD_LIST_0          0 
             3601  LOAD_GLOBAL          14  'groupcache'
             3604  LOAD_GLOBAL           5  'groupcounter'
             3607  BINARY_SUBSCR    
             3608  LOAD_CONST               'externals'
             3611  STORE_SUBSCR     
             3612  JUMP_FORWARD          0  'to 3615'
           3615_0  COME_FROM          3612  '3612'

 L. 963      3615  LOAD_GLOBAL          14  'groupcache'
             3618  LOAD_GLOBAL           5  'groupcounter'
             3621  BINARY_SUBSCR    
             3622  LOAD_CONST               'externals'
             3625  BINARY_SUBSCR    
             3626  LOAD_ATTR            30  'append'
             3629  LOAD_FAST            13  'k'
             3632  CALL_FUNCTION_1       1  None
             3635  POP_TOP          
             3636  JUMP_FORWARD          0  'to 3639'
           3639_0  COME_FROM          3636  '3636'

 L. 964      3639  LOAD_FAST            13  'k'
             3642  STORE_FAST           19  'last_name'
             3645  JUMP_BACK          3037  'to 3037'
             3648  POP_BLOCK        
           3649_0  COME_FROM          2990  '2990'

 L. 965      3649  LOAD_FAST            18  'edecl'
             3652  LOAD_GLOBAL          14  'groupcache'
             3655  LOAD_GLOBAL           5  'groupcounter'
             3658  BINARY_SUBSCR    
             3659  LOAD_CONST               'vars'
             3662  STORE_SUBSCR     

 L. 966      3663  LOAD_FAST            19  'last_name'
             3666  LOAD_CONST               None
             3669  COMPARE_OP            9  is-not
             3672  POP_JUMP_IF_FALSE  7502  'to 7502'

 L. 967      3675  LOAD_CONST               'variable'
             3678  LOAD_FAST            19  'last_name'
             3681  LOAD_GLOBAL           5  'groupcounter'
             3684  BUILD_TUPLE_3         3 
             3687  STORE_GLOBAL          2  'previous_context'
             3690  JUMP_ABSOLUTE      7502  'to 7502'
             3693  JUMP_FORWARD       3806  'to 7502'

 L. 968      3696  LOAD_FAST             1  'case'
             3699  LOAD_CONST               'parameter'
             3702  COMPARE_OP            2  ==
             3705  POP_JUMP_IF_FALSE  4430  'to 4430'

 L. 969      3708  LOAD_GLOBAL          14  'groupcache'
             3711  LOAD_GLOBAL           5  'groupcounter'
             3714  BINARY_SUBSCR    
             3715  LOAD_CONST               'vars'
             3718  BINARY_SUBSCR    
             3719  STORE_FAST           18  'edecl'

 L. 970      3722  LOAD_FAST             0  'm'
             3725  LOAD_ATTR             0  'group'
             3728  LOAD_CONST               'after'
             3731  CALL_FUNCTION_1       1  None
             3734  LOAD_ATTR            23  'strip'
             3737  CALL_FUNCTION_0       0  None
             3740  LOAD_CONST               1
             3743  LOAD_CONST               -1
             3746  SLICE+3          
             3747  STORE_FAST           20  'll'

 L. 971      3750  LOAD_CONST               None
             3753  STORE_FAST           19  'last_name'

 L. 972      3756  SETUP_LOOP          624  'to 4383'
             3759  LOAD_GLOBAL          22  'markoutercomma'
             3762  LOAD_FAST            20  'll'
             3765  CALL_FUNCTION_1       1  None
             3768  LOAD_ATTR            10  'split'
             3771  LOAD_CONST               '@,@'
             3774  CALL_FUNCTION_1       1  None
             3777  GET_ITER         
             3778  FOR_ITER            601  'to 4382'
             3781  STORE_FAST           24  'e'

 L. 973      3784  SETUP_EXCEPT         50  'to 3837'

 L. 974      3787  BUILD_LIST_0          0 
             3790  LOAD_FAST            24  'e'
             3793  LOAD_ATTR            10  'split'
             3796  LOAD_CONST               '='
             3799  CALL_FUNCTION_1       1  None
             3802  GET_ITER         
             3803  FOR_ITER             18  'to 3824'
             3806  STORE_FAST            9  'x'
             3809  LOAD_FAST             9  'x'
             3812  LOAD_ATTR            23  'strip'
             3815  CALL_FUNCTION_0       0  None
             3818  LIST_APPEND           2  None
             3821  JUMP_BACK          3803  'to 3803'
             3824  UNPACK_SEQUENCE_2     2 
             3827  STORE_FAST           13  'k'
             3830  STORE_FAST           27  'initexpr'
             3833  POP_BLOCK        
             3834  JUMP_FORWARD         30  'to 3867'
           3837_0  COME_FROM          3784  '3784'

 L. 975      3837  POP_TOP          
             3838  POP_TOP          
             3839  POP_TOP          

 L. 976      3840  LOAD_GLOBAL          11  'outmess'
             3843  LOAD_CONST               'analyzeline: could not extract name,expr in parameter statement "%s" of "%s"\n'
             3846  LOAD_FAST            24  'e'
             3849  LOAD_FAST            20  'll'
             3852  BUILD_TUPLE_2         2 
             3855  BINARY_MODULO    
             3856  CALL_FUNCTION_1       1  None
             3859  POP_TOP          
             3860  CONTINUE           3778  'to 3778'
             3863  JUMP_FORWARD          1  'to 3867'
             3866  END_FINALLY      
           3867_0  COME_FROM          3866  '3866'
           3867_1  COME_FROM          3834  '3834'

 L. 977      3867  LOAD_GLOBAL          47  'get_parameters'
             3870  LOAD_FAST            18  'edecl'
             3873  CALL_FUNCTION_1       1  None
             3876  STORE_FAST           28  'params'

 L. 978      3879  LOAD_GLOBAL          28  'rmbadname1'
             3882  LOAD_FAST            13  'k'
             3885  CALL_FUNCTION_1       1  None
             3888  STORE_FAST           13  'k'

 L. 979      3891  LOAD_FAST            13  'k'
             3894  LOAD_FAST            18  'edecl'
             3897  COMPARE_OP            7  not-in
             3900  POP_JUMP_IF_FALSE  3916  'to 3916'

 L. 980      3903  BUILD_MAP_0           0  None
             3906  LOAD_FAST            18  'edecl'
             3909  LOAD_FAST            13  'k'
             3912  STORE_SUBSCR     
             3913  JUMP_FORWARD          0  'to 3916'
           3916_0  COME_FROM          3913  '3913'

 L. 981      3916  LOAD_CONST               '='
             3919  LOAD_FAST            18  'edecl'
             3922  LOAD_FAST            13  'k'
             3925  BINARY_SUBSCR    
             3926  COMPARE_OP            6  in
             3929  POP_JUMP_IF_FALSE  3987  'to 3987'
             3932  LOAD_FAST            18  'edecl'
             3935  LOAD_FAST            13  'k'
             3938  BINARY_SUBSCR    
             3939  LOAD_CONST               '='
             3942  BINARY_SUBSCR    
             3943  LOAD_FAST            27  'initexpr'
             3946  COMPARE_OP            2  ==
             3949  UNARY_NOT        
           3950_0  COME_FROM          3929  '3929'
             3950  POP_JUMP_IF_FALSE  3987  'to 3987'

 L. 982      3953  LOAD_GLOBAL          11  'outmess'
             3956  LOAD_CONST               'analyzeline: Overwriting the value of parameter "%s" ("%s") with "%s".\n'
             3959  LOAD_FAST            13  'k'
             3962  LOAD_FAST            18  'edecl'
             3965  LOAD_FAST            13  'k'
             3968  BINARY_SUBSCR    
             3969  LOAD_CONST               '='
             3972  BINARY_SUBSCR    
             3973  LOAD_FAST            27  'initexpr'
             3976  BUILD_TUPLE_3         3 
             3979  BINARY_MODULO    
             3980  CALL_FUNCTION_1       1  None
             3983  POP_TOP          
             3984  JUMP_FORWARD          0  'to 3987'
           3987_0  COME_FROM          3984  '3984'

 L. 983      3987  LOAD_GLOBAL          48  'determineexprtype'
             3990  LOAD_FAST            27  'initexpr'
             3993  LOAD_FAST            28  'params'
             3996  CALL_FUNCTION_2       2  None
             3999  STORE_FAST           14  't'

 L. 984      4002  LOAD_FAST            14  't'
             4005  POP_JUMP_IF_FALSE  4220  'to 4220'

 L. 985      4008  LOAD_FAST            14  't'
             4011  LOAD_ATTR            49  'get'
             4014  LOAD_CONST               'typespec'
             4017  CALL_FUNCTION_1       1  None
             4020  LOAD_CONST               'real'
             4023  COMPARE_OP            2  ==
             4026  POP_JUMP_IF_FALSE  4153  'to 4153'

 L. 986      4029  LOAD_GLOBAL          50  'list'
             4032  LOAD_FAST            27  'initexpr'
             4035  CALL_FUNCTION_1       1  None
             4038  STORE_FAST           29  'tt'

 L. 987      4041  SETUP_LOOP           91  'to 4135'
             4044  LOAD_GLOBAL          51  'real16pattern'
             4047  LOAD_ATTR            52  'finditer'
             4050  LOAD_FAST            27  'initexpr'
             4053  CALL_FUNCTION_1       1  None
             4056  GET_ITER         
             4057  FOR_ITER             74  'to 4134'
             4060  STORE_FAST            0  'm'

 L. 988      4063  LOAD_GLOBAL          50  'list'

 L. 989      4066  LOAD_FAST            27  'initexpr'
             4069  LOAD_FAST             0  'm'
             4072  LOAD_ATTR            53  'start'
             4075  CALL_FUNCTION_0       0  None
             4078  LOAD_FAST             0  'm'
             4081  LOAD_ATTR            54  'end'
             4084  CALL_FUNCTION_0       0  None
             4087  SLICE+3          
             4088  LOAD_ATTR            16  'lower'
             4091  CALL_FUNCTION_0       0  None
             4094  LOAD_ATTR            55  'replace'
             4097  LOAD_CONST               'd'
             4100  LOAD_CONST               'e'
             4103  CALL_FUNCTION_2       2  None
             4106  CALL_FUNCTION_1       1  None
             4109  LOAD_FAST            29  'tt'
             4112  LOAD_FAST             0  'm'
             4115  LOAD_ATTR            53  'start'
             4118  CALL_FUNCTION_0       0  None
             4121  LOAD_FAST             0  'm'
             4124  LOAD_ATTR            54  'end'
             4127  CALL_FUNCTION_0       0  None
             4130  STORE_SLICE+3    
             4131  JUMP_BACK          4057  'to 4057'
             4134  POP_BLOCK        
           4135_0  COME_FROM          4041  '4041'

 L. 990      4135  LOAD_CONST               ''
             4138  LOAD_ATTR            41  'join'
             4141  LOAD_FAST            29  'tt'
             4144  CALL_FUNCTION_1       1  None
             4147  STORE_FAST           27  'initexpr'
             4150  JUMP_ABSOLUTE      4220  'to 4220'

 L. 991      4153  LOAD_FAST            14  't'
             4156  LOAD_ATTR            49  'get'
             4159  LOAD_CONST               'typespec'
             4162  CALL_FUNCTION_1       1  None
             4165  LOAD_CONST               'complex'
             4168  COMPARE_OP            2  ==
             4171  POP_JUMP_IF_FALSE  4220  'to 4220'

 L. 992      4174  LOAD_FAST            27  'initexpr'
             4177  LOAD_CONST               1
             4180  SLICE+1          
             4181  LOAD_ATTR            16  'lower'
             4184  CALL_FUNCTION_0       0  None
             4187  LOAD_ATTR            55  'replace'
             4190  LOAD_CONST               'd'
             4193  LOAD_CONST               'e'
             4196  CALL_FUNCTION_2       2  None
             4199  LOAD_ATTR            55  'replace'

 L. 993      4202  LOAD_CONST               ','
             4205  LOAD_CONST               '+1j*('
             4208  CALL_FUNCTION_2       2  None
             4211  STORE_FAST           27  'initexpr'
             4214  JUMP_ABSOLUTE      4220  'to 4220'
             4217  JUMP_FORWARD          0  'to 4220'
           4220_0  COME_FROM          4217  '4217'

 L. 994      4220  SETUP_EXCEPT         22  'to 4245'

 L. 995      4223  LOAD_GLOBAL          56  'eval'
             4226  LOAD_FAST            27  'initexpr'
             4229  BUILD_MAP_0           0  None
             4232  LOAD_FAST            28  'params'
             4235  CALL_FUNCTION_3       3  None
             4238  STORE_FAST           30  'v'
             4241  POP_BLOCK        
             4242  JUMP_FORWARD         51  'to 4296'
           4245_0  COME_FROM          4220  '4220'

 L. 996      4245  DUP_TOP          
             4246  LOAD_GLOBAL          57  'SyntaxError'
             4249  LOAD_GLOBAL          58  'NameError'
             4252  LOAD_GLOBAL          59  'TypeError'
             4255  BUILD_TUPLE_3         3 
             4258  COMPARE_OP           10  exception-match
             4261  POP_JUMP_IF_FALSE  4295  'to 4295'
             4264  POP_TOP          
             4265  STORE_FAST           31  'msg'
             4268  POP_TOP          

 L. 997      4269  LOAD_GLOBAL          46  'errmess'
             4272  LOAD_CONST               'analyzeline: Failed to evaluate %r. Ignoring: %s\n'

 L. 998      4275  LOAD_FAST            27  'initexpr'
             4278  LOAD_FAST            31  'msg'
             4281  BUILD_TUPLE_2         2 
             4284  BINARY_MODULO    
             4285  CALL_FUNCTION_1       1  None
             4288  POP_TOP          

 L. 999      4289  CONTINUE           3778  'to 3778'
             4292  JUMP_FORWARD          1  'to 4296'
             4295  END_FINALLY      
           4296_0  COME_FROM          4295  '4295'
           4296_1  COME_FROM          4242  '4242'

 L.1000      4296  LOAD_GLOBAL          60  'repr'
             4299  LOAD_FAST            30  'v'
             4302  CALL_FUNCTION_1       1  None
             4305  LOAD_FAST            18  'edecl'
             4308  LOAD_FAST            13  'k'
             4311  BINARY_SUBSCR    
             4312  LOAD_CONST               '='
             4315  STORE_SUBSCR     

 L.1001      4316  LOAD_CONST               'attrspec'
             4319  LOAD_FAST            18  'edecl'
             4322  LOAD_FAST            13  'k'
             4325  BINARY_SUBSCR    
             4326  COMPARE_OP            6  in
             4329  POP_JUMP_IF_FALSE  4356  'to 4356'

 L.1002      4332  LOAD_FAST            18  'edecl'
             4335  LOAD_FAST            13  'k'
             4338  BINARY_SUBSCR    
             4339  LOAD_CONST               'attrspec'
             4342  BINARY_SUBSCR    
             4343  LOAD_ATTR            30  'append'
             4346  LOAD_CONST               'parameter'
             4349  CALL_FUNCTION_1       1  None
             4352  POP_TOP          
             4353  JUMP_FORWARD         17  'to 4373'

 L.1003      4356  LOAD_CONST               'parameter'
             4359  BUILD_LIST_1          1 
             4362  LOAD_FAST            18  'edecl'
             4365  LOAD_FAST            13  'k'
             4368  BINARY_SUBSCR    
             4369  LOAD_CONST               'attrspec'
             4372  STORE_SUBSCR     
           4373_0  COME_FROM          4353  '4353'

 L.1004      4373  LOAD_FAST            13  'k'
             4376  STORE_FAST           19  'last_name'
             4379  JUMP_BACK          3778  'to 3778'
             4382  POP_BLOCK        
           4383_0  COME_FROM          3756  '3756'

 L.1005      4383  LOAD_FAST            18  'edecl'
             4386  LOAD_GLOBAL          14  'groupcache'
             4389  LOAD_GLOBAL           5  'groupcounter'
             4392  BINARY_SUBSCR    
             4393  LOAD_CONST               'vars'
             4396  STORE_SUBSCR     

 L.1006      4397  LOAD_FAST            19  'last_name'
             4400  LOAD_CONST               None
             4403  COMPARE_OP            9  is-not
             4406  POP_JUMP_IF_FALSE  7502  'to 7502'

 L.1007      4409  LOAD_CONST               'variable'
             4412  LOAD_FAST            19  'last_name'
             4415  LOAD_GLOBAL           5  'groupcounter'
             4418  BUILD_TUPLE_3         3 
             4421  STORE_GLOBAL          2  'previous_context'
             4424  JUMP_ABSOLUTE      7502  'to 7502'
             4427  JUMP_FORWARD       3072  'to 7502'

 L.1008      4430  LOAD_FAST             1  'case'
             4433  LOAD_CONST               'implicit'
             4436  COMPARE_OP            2  ==
             4439  POP_JUMP_IF_FALSE  5163  'to 5163'

 L.1009      4442  LOAD_FAST             0  'm'
             4445  LOAD_ATTR             0  'group'
             4448  LOAD_CONST               'after'
             4451  CALL_FUNCTION_1       1  None
             4454  LOAD_ATTR            23  'strip'
             4457  CALL_FUNCTION_0       0  None
             4460  LOAD_ATTR            16  'lower'
             4463  CALL_FUNCTION_0       0  None
             4466  LOAD_CONST               'none'
             4469  COMPARE_OP            2  ==
             4472  POP_JUMP_IF_FALSE  4492  'to 4492'

 L.1010      4475  LOAD_CONST               None
             4478  LOAD_GLOBAL          14  'groupcache'
             4481  LOAD_GLOBAL           5  'groupcounter'
             4484  BINARY_SUBSCR    
             4485  LOAD_CONST               'implicit'
             4488  STORE_SUBSCR     
             4489  JUMP_ABSOLUTE      7502  'to 7502'

 L.1011      4492  LOAD_FAST             0  'm'
             4495  LOAD_ATTR             0  'group'
             4498  LOAD_CONST               'after'
             4501  CALL_FUNCTION_1       1  None
             4504  POP_JUMP_IF_FALSE  7502  'to 7502'

 L.1012      4507  LOAD_CONST               'implicit'
             4510  LOAD_GLOBAL          14  'groupcache'
             4513  LOAD_GLOBAL           5  'groupcounter'
             4516  BINARY_SUBSCR    
             4517  COMPARE_OP            6  in
             4520  POP_JUMP_IF_FALSE  4540  'to 4540'

 L.1013      4523  LOAD_GLOBAL          14  'groupcache'
             4526  LOAD_GLOBAL           5  'groupcounter'
             4529  BINARY_SUBSCR    
             4530  LOAD_CONST               'implicit'
             4533  BINARY_SUBSCR    
             4534  STORE_FAST           32  'impl'
             4537  JUMP_FORWARD          6  'to 4546'

 L.1014      4540  BUILD_MAP_0           0  None
             4543  STORE_FAST           32  'impl'
           4546_0  COME_FROM          4537  '4537'

 L.1015      4546  LOAD_FAST            32  'impl'
             4549  LOAD_CONST               None
             4552  COMPARE_OP            8  is
             4555  POP_JUMP_IF_FALSE  4577  'to 4577'

 L.1016      4558  LOAD_GLOBAL          11  'outmess'
             4561  LOAD_CONST               'analyzeline: Overwriting earlier "implicit none" statement.\n'
             4564  CALL_FUNCTION_1       1  None
             4567  POP_TOP          

 L.1017      4568  BUILD_MAP_0           0  None
             4571  STORE_FAST           32  'impl'
             4574  JUMP_FORWARD          0  'to 4577'
           4577_0  COME_FROM          4574  '4574'

 L.1018      4577  SETUP_LOOP          563  'to 5143'
             4580  LOAD_GLOBAL          22  'markoutercomma'
             4583  LOAD_FAST             0  'm'
             4586  LOAD_ATTR             0  'group'
             4589  LOAD_CONST               'after'
             4592  CALL_FUNCTION_1       1  None
             4595  CALL_FUNCTION_1       1  None
             4598  LOAD_ATTR            10  'split'
             4601  LOAD_CONST               '@,@'
             4604  CALL_FUNCTION_1       1  None
             4607  GET_ITER         
             4608  FOR_ITER            531  'to 5142'
             4611  STORE_FAST           24  'e'

 L.1019      4614  BUILD_MAP_0           0  None
             4617  STORE_FAST           33  'decl'

 L.1020      4620  LOAD_GLOBAL          17  're'
             4623  LOAD_ATTR            18  'match'
             4626  LOAD_CONST               '\\s*(?P<this>.*?)\\s*(\\(\\s*(?P<after>[a-z-, ]+)\\s*\\)\\s*|)\\Z'
             4629  LOAD_FAST            24  'e'
             4632  LOAD_GLOBAL          17  're'
             4635  LOAD_ATTR            19  'I'
             4638  CALL_FUNCTION_3       3  None
             4641  STORE_FAST           25  'm1'

 L.1021      4644  LOAD_FAST            25  'm1'
             4647  POP_JUMP_IF_TRUE   4670  'to 4670'

 L.1022      4650  LOAD_GLOBAL          11  'outmess'
             4653  LOAD_CONST               'analyzeline: could not extract info of implicit statement part "%s"\n'
             4656  LOAD_FAST            24  'e'
             4659  BINARY_MODULO    
             4660  CALL_FUNCTION_1       1  None
             4663  POP_TOP          
             4664  JUMP_BACK          4608  'to 4608'
             4667  JUMP_FORWARD          0  'to 4670'
           4670_0  COME_FROM          4667  '4667'

 L.1023      4670  LOAD_GLOBAL          61  'typespattern4implicit'
             4673  LOAD_ATTR            18  'match'
             4676  LOAD_FAST            25  'm1'
             4679  LOAD_ATTR             0  'group'
             4682  LOAD_CONST               'this'
             4685  CALL_FUNCTION_1       1  None
             4688  CALL_FUNCTION_1       1  None
             4691  STORE_FAST           34  'm2'

 L.1024      4694  LOAD_FAST            34  'm2'
             4697  POP_JUMP_IF_TRUE   4720  'to 4720'

 L.1025      4700  LOAD_GLOBAL          11  'outmess'
             4703  LOAD_CONST               'analyzeline: could not extract types pattern of implicit statement part "%s"\n'
             4706  LOAD_FAST            24  'e'
             4709  BINARY_MODULO    
             4710  CALL_FUNCTION_1       1  None
             4713  POP_TOP          
             4714  JUMP_BACK          4608  'to 4608'
             4717  JUMP_FORWARD          0  'to 4720'
           4720_0  COME_FROM          4717  '4717'

 L.1026      4720  LOAD_GLOBAL          36  'cracktypespec0'
             4723  LOAD_FAST            34  'm2'
             4726  LOAD_ATTR             0  'group'
             4729  LOAD_CONST               'this'
             4732  CALL_FUNCTION_1       1  None
             4735  LOAD_FAST            34  'm2'
             4738  LOAD_ATTR             0  'group'
             4741  LOAD_CONST               'after'
             4744  CALL_FUNCTION_1       1  None
             4747  CALL_FUNCTION_2       2  None
             4750  UNPACK_SEQUENCE_4     4 
             4753  STORE_FAST           15  'typespec'
             4756  STORE_FAST           16  'selector'
             4759  STORE_FAST           17  'attr'
             4762  STORE_FAST           18  'edecl'

 L.1027      4765  LOAD_GLOBAL          62  'cracktypespec'
             4768  LOAD_FAST            15  'typespec'
             4771  LOAD_FAST            16  'selector'
             4774  CALL_FUNCTION_2       2  None
             4777  UNPACK_SEQUENCE_3     3 
             4780  STORE_FAST           35  'kindselect'
             4783  STORE_FAST           36  'charselect'
             4786  STORE_FAST           37  'typename'

 L.1028      4789  LOAD_FAST            15  'typespec'
             4792  LOAD_FAST            33  'decl'
             4795  LOAD_CONST               'typespec'
             4798  STORE_SUBSCR     

 L.1029      4799  LOAD_FAST            35  'kindselect'
             4802  LOAD_FAST            33  'decl'
             4805  LOAD_CONST               'kindselector'
             4808  STORE_SUBSCR     

 L.1030      4809  LOAD_FAST            36  'charselect'
             4812  LOAD_FAST            33  'decl'
             4815  LOAD_CONST               'charselector'
             4818  STORE_SUBSCR     

 L.1031      4819  LOAD_FAST            37  'typename'
             4822  LOAD_FAST            33  'decl'
             4825  LOAD_CONST               'typename'
             4828  STORE_SUBSCR     

 L.1032      4829  SETUP_LOOP           40  'to 4872'
             4832  LOAD_FAST            33  'decl'
             4835  LOAD_ATTR            29  'keys'
             4838  CALL_FUNCTION_0       0  None
             4841  GET_ITER         
             4842  FOR_ITER             26  'to 4871'
             4845  STORE_FAST           13  'k'

 L.1033      4848  LOAD_FAST            33  'decl'
             4851  LOAD_FAST            13  'k'
             4854  BINARY_SUBSCR    
             4855  POP_JUMP_IF_TRUE   4842  'to 4842'
             4858  LOAD_FAST            33  'decl'
             4861  LOAD_FAST            13  'k'
             4864  DELETE_SUBSCR    
             4865  JUMP_BACK          4842  'to 4842'
             4868  JUMP_BACK          4842  'to 4842'
             4871  POP_BLOCK        
           4872_0  COME_FROM          4829  '4829'

 L.1034      4872  SETUP_LOOP          264  'to 5139'
             4875  LOAD_GLOBAL          22  'markoutercomma'
             4878  LOAD_FAST            25  'm1'
             4881  LOAD_ATTR             0  'group'
             4884  LOAD_CONST               'after'
             4887  CALL_FUNCTION_1       1  None
             4890  CALL_FUNCTION_1       1  None
             4893  LOAD_ATTR            10  'split'
             4896  LOAD_CONST               '@,@'
             4899  CALL_FUNCTION_1       1  None
             4902  GET_ITER         
             4903  FOR_ITER            232  'to 5138'
             4906  STORE_FAST           38  'r'

 L.1035      4909  LOAD_CONST               '-'
             4912  LOAD_FAST            38  'r'
             4915  COMPARE_OP            6  in
             4918  POP_JUMP_IF_FALSE  5001  'to 5001'

 L.1036      4921  SETUP_EXCEPT         50  'to 4974'
             4924  BUILD_LIST_0          0 
             4927  LOAD_FAST            38  'r'
             4930  LOAD_ATTR            10  'split'
             4933  LOAD_CONST               '-'
             4936  CALL_FUNCTION_1       1  None
             4939  GET_ITER         
             4940  FOR_ITER             18  'to 4961'
             4943  STORE_FAST            9  'x'
             4946  LOAD_FAST             9  'x'
             4949  LOAD_ATTR            23  'strip'
             4952  CALL_FUNCTION_0       0  None
             4955  LIST_APPEND           2  None
             4958  JUMP_BACK          4940  'to 4940'
             4961  UNPACK_SEQUENCE_2     2 
             4964  STORE_FAST           39  'begc'
             4967  STORE_FAST           40  'endc'
             4970  POP_BLOCK        
             4971  JUMP_ABSOLUTE      5017  'to 5017'
           4974_0  COME_FROM          4921  '4921'

 L.1037      4974  POP_TOP          
             4975  POP_TOP          
             4976  POP_TOP          

 L.1038      4977  LOAD_GLOBAL          11  'outmess'
             4980  LOAD_CONST               'analyzeline: expected "<char>-<char>" instead of "%s" in range list of implicit statement\n'
             4983  LOAD_FAST            38  'r'
             4986  BINARY_MODULO    
             4987  CALL_FUNCTION_1       1  None
             4990  POP_TOP          
             4991  CONTINUE           4903  'to 4903'
             4994  JUMP_ABSOLUTE      5017  'to 5017'
             4997  END_FINALLY      
           4998_0  COME_FROM          4997  '4997'
             4998  JUMP_FORWARD         16  'to 5017'

 L.1039      5001  LOAD_FAST            38  'r'
             5004  LOAD_ATTR            23  'strip'
             5007  CALL_FUNCTION_0       0  None
             5010  DUP_TOP          
             5011  STORE_FAST           39  'begc'
             5014  STORE_FAST           40  'endc'
           5017_0  COME_FROM          4998  '4998'

 L.1040      5017  LOAD_GLOBAL          42  'len'
             5020  LOAD_FAST            39  'begc'
             5023  CALL_FUNCTION_1       1  None
             5026  LOAD_GLOBAL          42  'len'
             5029  LOAD_FAST            40  'endc'
             5032  CALL_FUNCTION_1       1  None
             5035  DUP_TOP          
             5036  ROT_THREE        
             5037  COMPARE_OP            2  ==
             5040  JUMP_IF_FALSE_OR_POP  5052  'to 5052'
             5043  LOAD_CONST               1
             5046  COMPARE_OP            2  ==
             5049  JUMP_FORWARD          2  'to 5054'
           5052_0  COME_FROM          5040  '5040'
             5052  ROT_TWO          
             5053  POP_TOP          
           5054_0  COME_FROM          5049  '5049'
             5054  POP_JUMP_IF_TRUE   5077  'to 5077'

 L.1041      5057  LOAD_GLOBAL          11  'outmess'
             5060  LOAD_CONST               'analyzeline: expected "<char>-<char>" instead of "%s" in range list of implicit statement (2)\n'
             5063  LOAD_FAST            38  'r'
             5066  BINARY_MODULO    
             5067  CALL_FUNCTION_1       1  None
             5070  POP_TOP          
             5071  JUMP_BACK          4903  'to 4903'
             5074  JUMP_FORWARD          0  'to 5077'
           5077_0  COME_FROM          5074  '5074'

 L.1042      5077  SETUP_LOOP           55  'to 5135'
             5080  LOAD_GLOBAL          63  'range'
             5083  LOAD_GLOBAL          64  'ord'
             5086  LOAD_FAST            39  'begc'
             5089  CALL_FUNCTION_1       1  None
             5092  LOAD_GLOBAL          64  'ord'
             5095  LOAD_FAST            40  'endc'
             5098  CALL_FUNCTION_1       1  None
             5101  LOAD_CONST               1
             5104  BINARY_ADD       
             5105  CALL_FUNCTION_2       2  None
             5108  GET_ITER         
             5109  FOR_ITER             22  'to 5134'
             5112  STORE_FAST           41  'o'

 L.1043      5115  LOAD_FAST            33  'decl'
             5118  LOAD_FAST            32  'impl'
             5121  LOAD_GLOBAL          65  'chr'
             5124  LOAD_FAST            41  'o'
             5127  CALL_FUNCTION_1       1  None
             5130  STORE_SUBSCR     
             5131  JUMP_BACK          5109  'to 5109'
             5134  POP_BLOCK        
           5135_0  COME_FROM          5077  '5077'
             5135  JUMP_BACK          4903  'to 4903'
             5138  POP_BLOCK        
           5139_0  COME_FROM          4872  '4872'
             5139  JUMP_BACK          4608  'to 4608'
             5142  POP_BLOCK        
           5143_0  COME_FROM          4577  '4577'

 L.1044      5143  LOAD_FAST            32  'impl'
             5146  LOAD_GLOBAL          14  'groupcache'
             5149  LOAD_GLOBAL           5  'groupcounter'
             5152  BINARY_SUBSCR    
             5153  LOAD_CONST               'implicit'
             5156  STORE_SUBSCR     
             5157  JUMP_ABSOLUTE      7502  'to 7502'
             5160  JUMP_FORWARD       2339  'to 7502'

 L.1045      5163  LOAD_FAST             1  'case'
             5166  LOAD_CONST               'data'
             5169  COMPARE_OP            2  ==
             5172  POP_JUMP_IF_FALSE  6205  'to 6205'

 L.1046      5175  BUILD_LIST_0          0 
             5178  STORE_FAST           20  'll'

 L.1047      5181  LOAD_CONST               ''
             5184  STORE_FAST           42  'dl'
             5187  LOAD_CONST               ''
             5190  STORE_FAST           43  'il'
             5193  LOAD_CONST               0
             5196  STORE_FAST           44  'f'
             5199  LOAD_CONST               1
             5202  STORE_FAST           45  'fc'
             5205  LOAD_CONST               0
             5208  STORE_FAST           46  'inp'

 L.1048      5211  SETUP_LOOP          286  'to 5500'
             5214  LOAD_FAST             0  'm'
             5217  LOAD_ATTR             0  'group'
             5220  LOAD_CONST               'after'
             5223  CALL_FUNCTION_1       1  None
             5226  GET_ITER         
             5227  FOR_ITER            269  'to 5499'
             5230  STORE_FAST           47  'c'

 L.1049      5233  LOAD_FAST            46  'inp'
             5236  POP_JUMP_IF_TRUE   5298  'to 5298'

 L.1050      5239  LOAD_FAST            47  'c'
             5242  LOAD_CONST               "'"
             5245  COMPARE_OP            2  ==
             5248  POP_JUMP_IF_FALSE  5261  'to 5261'
             5251  LOAD_FAST            45  'fc'
             5254  UNARY_NOT        
             5255  STORE_FAST           45  'fc'
             5258  JUMP_FORWARD          0  'to 5261'
           5261_0  COME_FROM          5258  '5258'

 L.1051      5261  LOAD_FAST            47  'c'
             5264  LOAD_CONST               '/'
             5267  COMPARE_OP            2  ==
             5270  POP_JUMP_IF_FALSE  5298  'to 5298'
             5273  LOAD_FAST            45  'fc'
           5276_0  COME_FROM          5270  '5270'
             5276  POP_JUMP_IF_FALSE  5298  'to 5298'
             5279  LOAD_FAST            44  'f'
             5282  LOAD_CONST               1
             5285  BINARY_ADD       
             5286  STORE_FAST           44  'f'
             5289  JUMP_BACK          5227  'to 5227'
             5292  JUMP_ABSOLUTE      5298  'to 5298'
             5295  JUMP_FORWARD          0  'to 5298'
           5298_0  COME_FROM          5295  '5295'

 L.1052      5298  LOAD_FAST            47  'c'
             5301  LOAD_CONST               '('
             5304  COMPARE_OP            2  ==
             5307  POP_JUMP_IF_FALSE  5323  'to 5323'
             5310  LOAD_FAST            46  'inp'
             5313  LOAD_CONST               1
             5316  BINARY_ADD       
             5317  STORE_FAST           46  'inp'
             5320  JUMP_FORWARD         25  'to 5348'

 L.1053      5323  LOAD_FAST            47  'c'
             5326  LOAD_CONST               ')'
             5329  COMPARE_OP            2  ==
             5332  POP_JUMP_IF_FALSE  5348  'to 5348'
             5335  LOAD_FAST            46  'inp'
             5338  LOAD_CONST               1
             5341  BINARY_SUBTRACT  
             5342  STORE_FAST           46  'inp'
             5345  JUMP_FORWARD          0  'to 5348'
           5348_0  COME_FROM          5345  '5345'
           5348_1  COME_FROM          5320  '5320'

 L.1054      5348  LOAD_FAST            44  'f'
             5351  LOAD_CONST               0
             5354  COMPARE_OP            2  ==
             5357  POP_JUMP_IF_FALSE  5373  'to 5373'
             5360  LOAD_FAST            42  'dl'
             5363  LOAD_FAST            47  'c'
             5366  BINARY_ADD       
             5367  STORE_FAST           42  'dl'
             5370  JUMP_BACK          5227  'to 5227'

 L.1055      5373  LOAD_FAST            44  'f'
             5376  LOAD_CONST               1
             5379  COMPARE_OP            2  ==
             5382  POP_JUMP_IF_FALSE  5398  'to 5398'
             5385  LOAD_FAST            43  'il'
             5388  LOAD_FAST            47  'c'
             5391  BINARY_ADD       
             5392  STORE_FAST           43  'il'
             5395  JUMP_BACK          5227  'to 5227'

 L.1056      5398  LOAD_FAST            44  'f'
             5401  LOAD_CONST               2
             5404  COMPARE_OP            2  ==
             5407  POP_JUMP_IF_FALSE  5227  'to 5227'

 L.1057      5410  LOAD_FAST            42  'dl'
             5413  LOAD_ATTR            23  'strip'
             5416  CALL_FUNCTION_0       0  None
             5419  STORE_FAST           42  'dl'

 L.1058      5422  LOAD_FAST            42  'dl'
             5425  LOAD_ATTR            66  'startswith'
             5428  LOAD_CONST               ','
             5431  CALL_FUNCTION_1       1  None
             5434  POP_JUMP_IF_FALSE  5456  'to 5456'

 L.1059      5437  LOAD_FAST            42  'dl'
             5440  LOAD_CONST               1
             5443  SLICE+1          
             5444  LOAD_ATTR            23  'strip'
             5447  CALL_FUNCTION_0       0  None
             5450  STORE_FAST           42  'dl'
             5453  JUMP_FORWARD          0  'to 5456'
           5456_0  COME_FROM          5453  '5453'

 L.1060      5456  LOAD_FAST            20  'll'
             5459  LOAD_ATTR            30  'append'
             5462  LOAD_FAST            42  'dl'
             5465  LOAD_FAST            43  'il'
             5468  BUILD_LIST_2          2 
             5471  CALL_FUNCTION_1       1  None
             5474  POP_TOP          

 L.1061      5475  LOAD_FAST            47  'c'
             5478  STORE_FAST           42  'dl'
             5481  LOAD_CONST               ''
             5484  STORE_FAST           43  'il'
             5487  LOAD_CONST               0
             5490  STORE_FAST           44  'f'
             5493  JUMP_BACK          5227  'to 5227'
             5496  JUMP_BACK          5227  'to 5227'
             5499  POP_BLOCK        
           5500_0  COME_FROM          5211  '5211'

 L.1062      5500  LOAD_FAST            44  'f'
             5503  LOAD_CONST               2
             5506  COMPARE_OP            2  ==
             5509  POP_JUMP_IF_FALSE  5580  'to 5580'

 L.1063      5512  LOAD_FAST            42  'dl'
             5515  LOAD_ATTR            23  'strip'
             5518  CALL_FUNCTION_0       0  None
             5521  STORE_FAST           42  'dl'

 L.1064      5524  LOAD_FAST            42  'dl'
             5527  LOAD_ATTR            66  'startswith'
             5530  LOAD_CONST               ','
             5533  CALL_FUNCTION_1       1  None
             5536  POP_JUMP_IF_FALSE  5558  'to 5558'

 L.1065      5539  LOAD_FAST            42  'dl'
             5542  LOAD_CONST               1
             5545  SLICE+1          
             5546  LOAD_ATTR            23  'strip'
             5549  CALL_FUNCTION_0       0  None
             5552  STORE_FAST           42  'dl'
             5555  JUMP_FORWARD          0  'to 5558'
           5558_0  COME_FROM          5555  '5555'

 L.1066      5558  LOAD_FAST            20  'll'
             5561  LOAD_ATTR            30  'append'
             5564  LOAD_FAST            42  'dl'
             5567  LOAD_FAST            43  'il'
             5570  BUILD_LIST_2          2 
             5573  CALL_FUNCTION_1       1  None
             5576  POP_TOP          
             5577  JUMP_FORWARD          0  'to 5580'
           5580_0  COME_FROM          5577  '5577'

 L.1067      5580  BUILD_MAP_0           0  None
             5583  STORE_FAST           48  'vars'

 L.1068      5586  LOAD_CONST               'vars'
             5589  LOAD_GLOBAL          14  'groupcache'
             5592  LOAD_GLOBAL           5  'groupcounter'
             5595  BINARY_SUBSCR    
             5596  COMPARE_OP            6  in
             5599  POP_JUMP_IF_FALSE  5619  'to 5619'

 L.1069      5602  LOAD_GLOBAL          14  'groupcache'
             5605  LOAD_GLOBAL           5  'groupcounter'
             5608  BINARY_SUBSCR    
             5609  LOAD_CONST               'vars'
             5612  BINARY_SUBSCR    
             5613  STORE_FAST           48  'vars'
             5616  JUMP_FORWARD          0  'to 5619'
           5619_0  COME_FROM          5616  '5616'

 L.1070      5619  LOAD_CONST               None
             5622  STORE_FAST           19  'last_name'

 L.1071      5625  SETUP_LOOP          530  'to 6158'
             5628  LOAD_FAST            20  'll'
             5631  GET_ITER         
             5632  FOR_ITER            522  'to 6157'
             5635  STORE_FAST           49  'l'

 L.1072      5638  BUILD_LIST_0          0 
             5641  LOAD_FAST            49  'l'
             5644  GET_ITER         
             5645  FOR_ITER             18  'to 5666'
             5648  STORE_FAST            9  'x'
             5651  LOAD_FAST             9  'x'
             5654  LOAD_ATTR            23  'strip'
             5657  CALL_FUNCTION_0       0  None
             5660  LIST_APPEND           2  None
             5663  JUMP_BACK          5645  'to 5645'
             5666  STORE_FAST           49  'l'

 L.1073      5669  LOAD_FAST            49  'l'
             5672  LOAD_CONST               0
             5675  BINARY_SUBSCR    
             5676  LOAD_CONST               0
             5679  BINARY_SUBSCR    
             5680  LOAD_CONST               ','
             5683  COMPARE_OP            2  ==
             5686  POP_JUMP_IF_FALSE  5710  'to 5710'
             5689  LOAD_FAST            49  'l'
             5692  LOAD_CONST               0
             5695  BINARY_SUBSCR    
             5696  LOAD_CONST               1
             5699  SLICE+1          
             5700  LOAD_FAST            49  'l'
             5703  LOAD_CONST               0
             5706  STORE_SUBSCR     
             5707  JUMP_FORWARD          0  'to 5710'
           5710_0  COME_FROM          5707  '5707'

 L.1074      5710  LOAD_FAST            49  'l'
             5713  LOAD_CONST               0
             5716  BINARY_SUBSCR    
             5717  LOAD_CONST               0
             5720  BINARY_SUBSCR    
             5721  LOAD_CONST               '('
             5724  COMPARE_OP            2  ==
             5727  POP_JUMP_IF_FALSE  5754  'to 5754'

 L.1075      5730  LOAD_GLOBAL          11  'outmess'
             5733  LOAD_CONST               'analyzeline: implied-DO list "%s" is not supported. Skipping.\n'
             5736  LOAD_FAST            49  'l'
             5739  LOAD_CONST               0
             5742  BINARY_SUBSCR    
             5743  BINARY_MODULO    
             5744  CALL_FUNCTION_1       1  None
             5747  POP_TOP          

 L.1076      5748  CONTINUE           5632  'to 5632'
             5751  JUMP_FORWARD          0  'to 5754'
           5754_0  COME_FROM          5751  '5751'

 L.1080      5754  LOAD_CONST               0
             5757  STORE_FAST           21  'i'
             5760  LOAD_CONST               0
             5763  STORE_FAST           50  'j'
             5766  LOAD_GLOBAL          42  'len'
             5769  LOAD_FAST            49  'l'
             5772  LOAD_CONST               1
             5775  BINARY_SUBSCR    
             5776  CALL_FUNCTION_1       1  None
             5779  STORE_FAST           51  'llen'

 L.1081      5782  SETUP_LOOP          369  'to 6154'
             5785  LOAD_GLOBAL          21  'rmbadname'
             5788  BUILD_LIST_0          0 
             5791  LOAD_GLOBAL          22  'markoutercomma'
             5794  LOAD_FAST            49  'l'
             5797  LOAD_CONST               0
             5800  BINARY_SUBSCR    
             5801  CALL_FUNCTION_1       1  None
             5804  LOAD_ATTR            10  'split'
             5807  LOAD_CONST               '@,@'
             5810  CALL_FUNCTION_1       1  None
             5813  GET_ITER         
             5814  FOR_ITER             18  'to 5835'
             5817  STORE_FAST            9  'x'
             5820  LOAD_FAST             9  'x'
             5823  LOAD_ATTR            23  'strip'
             5826  CALL_FUNCTION_0       0  None
             5829  LIST_APPEND           2  None
             5832  JUMP_BACK          5814  'to 5814'
             5835  CALL_FUNCTION_1       1  None
             5838  GET_ITER         
             5839  FOR_ITER            311  'to 6153'
             5842  STORE_FAST           30  'v'

 L.1082      5845  LOAD_FAST            30  'v'
             5848  LOAD_CONST               0
             5851  BINARY_SUBSCR    
             5852  LOAD_CONST               '('
             5855  COMPARE_OP            2  ==
             5858  POP_JUMP_IF_FALSE  5881  'to 5881'

 L.1083      5861  LOAD_GLOBAL          11  'outmess'
             5864  LOAD_CONST               'analyzeline: implied-DO list "%s" is not supported. Skipping.\n'
             5867  LOAD_FAST            30  'v'
             5870  BINARY_MODULO    
             5871  CALL_FUNCTION_1       1  None
             5874  POP_TOP          

 L.1086      5875  CONTINUE           5839  'to 5839'
             5878  JUMP_FORWARD          0  'to 5881'
           5881_0  COME_FROM          5878  '5878'

 L.1087      5881  LOAD_CONST               0
             5884  STORE_FAST           45  'fc'

 L.1088      5887  SETUP_LOOP           83  'to 5973'
             5890  LOAD_FAST            21  'i'
             5893  LOAD_FAST            51  'llen'
             5896  COMPARE_OP            0  <
             5899  POP_JUMP_IF_FALSE  5972  'to 5972'
             5902  LOAD_FAST            45  'fc'
             5905  POP_JUMP_IF_TRUE   5929  'to 5929'
             5908  LOAD_FAST            49  'l'
             5911  LOAD_CONST               1
             5914  BINARY_SUBSCR    
             5915  LOAD_FAST            21  'i'
             5918  BINARY_SUBSCR    
             5919  LOAD_CONST               ','
             5922  COMPARE_OP            2  ==
             5925  UNARY_NOT        
           5926_0  COME_FROM          5905  '5905'
           5926_1  COME_FROM          5899  '5899'
             5926  POP_JUMP_IF_FALSE  5972  'to 5972'

 L.1089      5929  LOAD_FAST            49  'l'
             5932  LOAD_CONST               1
             5935  BINARY_SUBSCR    
             5936  LOAD_FAST            21  'i'
             5939  BINARY_SUBSCR    
             5940  LOAD_CONST               "'"
             5943  COMPARE_OP            2  ==
             5946  POP_JUMP_IF_FALSE  5959  'to 5959'
             5949  LOAD_FAST            45  'fc'
             5952  UNARY_NOT        
             5953  STORE_FAST           45  'fc'
             5956  JUMP_FORWARD          0  'to 5959'
           5959_0  COME_FROM          5956  '5956'

 L.1090      5959  LOAD_FAST            21  'i'
             5962  LOAD_CONST               1
             5965  BINARY_ADD       
             5966  STORE_FAST           21  'i'
             5969  JUMP_BACK          5890  'to 5890'
             5972  POP_BLOCK        
           5973_0  COME_FROM          5887  '5887'

 L.1091      5973  LOAD_FAST            21  'i'
             5976  LOAD_CONST               1
             5979  BINARY_ADD       
             5980  STORE_FAST           21  'i'

 L.1093      5983  LOAD_FAST            30  'v'
             5986  LOAD_FAST            48  'vars'
             5989  COMPARE_OP            7  not-in
             5992  POP_JUMP_IF_FALSE  6008  'to 6008'

 L.1094      5995  BUILD_MAP_0           0  None
             5998  LOAD_FAST            48  'vars'
             6001  LOAD_FAST            30  'v'
             6004  STORE_SUBSCR     
             6005  JUMP_FORWARD          0  'to 6008'
           6008_0  COME_FROM          6005  '6005'

 L.1095      6008  LOAD_CONST               '='
             6011  LOAD_FAST            48  'vars'
             6014  LOAD_FAST            30  'v'
             6017  BINARY_SUBSCR    
             6018  COMPARE_OP            6  in
             6021  POP_JUMP_IF_FALSE  6109  'to 6109'
             6024  LOAD_FAST            48  'vars'
             6027  LOAD_FAST            30  'v'
             6030  BINARY_SUBSCR    
             6031  LOAD_CONST               '='
             6034  BINARY_SUBSCR    
             6035  LOAD_FAST            49  'l'
             6038  LOAD_CONST               1
             6041  BINARY_SUBSCR    
             6042  LOAD_FAST            50  'j'
             6045  LOAD_FAST            21  'i'
             6048  LOAD_CONST               1
             6051  BINARY_SUBTRACT  
             6052  SLICE+3          
             6053  COMPARE_OP            2  ==
             6056  UNARY_NOT        
           6057_0  COME_FROM          6021  '6021'
             6057  POP_JUMP_IF_FALSE  6109  'to 6109'

 L.1096      6060  LOAD_GLOBAL          11  'outmess'
             6063  LOAD_CONST               'analyzeline: changing init expression of "%s" ("%s") to "%s"\n'
             6066  LOAD_FAST            30  'v'
             6069  LOAD_FAST            48  'vars'
             6072  LOAD_FAST            30  'v'
             6075  BINARY_SUBSCR    
             6076  LOAD_CONST               '='
             6079  BINARY_SUBSCR    
             6080  LOAD_FAST            49  'l'
             6083  LOAD_CONST               1
             6086  BINARY_SUBSCR    
             6087  LOAD_FAST            50  'j'
             6090  LOAD_FAST            21  'i'
             6093  LOAD_CONST               1
             6096  BINARY_SUBTRACT  
             6097  SLICE+3          
             6098  BUILD_TUPLE_3         3 
             6101  BINARY_MODULO    
             6102  CALL_FUNCTION_1       1  None
             6105  POP_TOP          
             6106  JUMP_FORWARD          0  'to 6109'
           6109_0  COME_FROM          6106  '6106'

 L.1097      6109  LOAD_FAST            49  'l'
             6112  LOAD_CONST               1
             6115  BINARY_SUBSCR    
             6116  LOAD_FAST            50  'j'
             6119  LOAD_FAST            21  'i'
             6122  LOAD_CONST               1
             6125  BINARY_SUBTRACT  
             6126  SLICE+3          
             6127  LOAD_FAST            48  'vars'
             6130  LOAD_FAST            30  'v'
             6133  BINARY_SUBSCR    
             6134  LOAD_CONST               '='
             6137  STORE_SUBSCR     

 L.1098      6138  LOAD_FAST            21  'i'
             6141  STORE_FAST           50  'j'

 L.1099      6144  LOAD_FAST            30  'v'
             6147  STORE_FAST           19  'last_name'
             6150  JUMP_BACK          5839  'to 5839'
             6153  POP_BLOCK        
           6154_0  COME_FROM          5782  '5782'
             6154  JUMP_BACK          5632  'to 5632'
             6157  POP_BLOCK        
           6158_0  COME_FROM          5625  '5625'

 L.1100      6158  LOAD_FAST            48  'vars'
             6161  LOAD_GLOBAL          14  'groupcache'
             6164  LOAD_GLOBAL           5  'groupcounter'
             6167  BINARY_SUBSCR    
             6168  LOAD_CONST               'vars'
             6171  STORE_SUBSCR     

 L.1101      6172  LOAD_FAST            19  'last_name'
             6175  LOAD_CONST               None
             6178  COMPARE_OP            9  is-not
             6181  POP_JUMP_IF_FALSE  7502  'to 7502'

 L.1102      6184  LOAD_CONST               'variable'
             6187  LOAD_FAST            19  'last_name'
             6190  LOAD_GLOBAL           5  'groupcounter'
             6193  BUILD_TUPLE_3         3 
             6196  STORE_GLOBAL          2  'previous_context'
             6199  JUMP_ABSOLUTE      7502  'to 7502'
             6202  JUMP_FORWARD       1297  'to 7502'

 L.1103      6205  LOAD_FAST             1  'case'
             6208  LOAD_CONST               'common'
             6211  COMPARE_OP            2  ==
             6214  POP_JUMP_IF_FALSE  6723  'to 6723'

 L.1104      6217  LOAD_FAST             0  'm'
             6220  LOAD_ATTR             0  'group'
             6223  LOAD_CONST               'after'
             6226  CALL_FUNCTION_1       1  None
             6229  LOAD_ATTR            23  'strip'
             6232  CALL_FUNCTION_0       0  None
             6235  STORE_FAST            2  'line'

 L.1105      6238  LOAD_FAST             2  'line'
             6241  LOAD_CONST               0
             6244  BINARY_SUBSCR    
             6245  LOAD_CONST               '/'
             6248  COMPARE_OP            2  ==
             6251  POP_JUMP_IF_TRUE   6267  'to 6267'
             6254  LOAD_CONST               '//'
             6257  LOAD_FAST             2  'line'
             6260  BINARY_ADD       
             6261  STORE_FAST            2  'line'
             6264  JUMP_FORWARD          0  'to 6267'
           6267_0  COME_FROM          6264  '6264'

 L.1106      6267  BUILD_LIST_0          0 
             6270  STORE_FAST           52  'cl'

 L.1107      6273  LOAD_CONST               0
             6276  STORE_FAST           44  'f'
             6279  LOAD_CONST               ''
             6282  STORE_FAST           53  'bn'
             6285  LOAD_CONST               ''
             6288  STORE_FAST           54  'ol'

 L.1108      6291  SETUP_LOOP          158  'to 6452'
             6294  LOAD_FAST             2  'line'
             6297  GET_ITER         
             6298  FOR_ITER            150  'to 6451'
             6301  STORE_FAST           47  'c'

 L.1109      6304  LOAD_FAST            47  'c'
             6307  LOAD_CONST               '/'
             6310  COMPARE_OP            2  ==
             6313  POP_JUMP_IF_FALSE  6332  'to 6332'
             6316  LOAD_FAST            44  'f'
             6319  LOAD_CONST               1
             6322  BINARY_ADD       
             6323  STORE_FAST           44  'f'
             6326  JUMP_BACK          6298  'to 6298'
             6329  JUMP_FORWARD          0  'to 6332'
           6332_0  COME_FROM          6329  '6329'

 L.1110      6332  LOAD_FAST            44  'f'
             6335  LOAD_CONST               3
             6338  COMPARE_OP            5  >=
             6341  POP_JUMP_IF_FALSE  6415  'to 6415'

 L.1111      6344  LOAD_FAST            53  'bn'
             6347  LOAD_ATTR            23  'strip'
             6350  CALL_FUNCTION_0       0  None
             6353  STORE_FAST           53  'bn'

 L.1112      6356  LOAD_FAST            53  'bn'
             6359  POP_JUMP_IF_TRUE   6371  'to 6371'
             6362  LOAD_CONST               '_BLNK_'
             6365  STORE_FAST           53  'bn'
             6368  JUMP_FORWARD          0  'to 6371'
           6371_0  COME_FROM          6368  '6368'

 L.1113      6371  LOAD_FAST            52  'cl'
             6374  LOAD_ATTR            30  'append'
             6377  LOAD_FAST            53  'bn'
             6380  LOAD_FAST            54  'ol'
             6383  BUILD_LIST_2          2 
             6386  CALL_FUNCTION_1       1  None
             6389  POP_TOP          

 L.1114      6390  LOAD_FAST            44  'f'
             6393  LOAD_CONST               2
             6396  BINARY_SUBTRACT  
             6397  STORE_FAST           44  'f'
             6400  LOAD_CONST               ''
             6403  STORE_FAST           53  'bn'
             6406  LOAD_CONST               ''
             6409  STORE_FAST           54  'ol'
             6412  JUMP_FORWARD          0  'to 6415'
           6415_0  COME_FROM          6412  '6412'

 L.1115      6415  LOAD_FAST            44  'f'
             6418  LOAD_CONST               2
             6421  BINARY_MODULO    
             6422  POP_JUMP_IF_FALSE  6438  'to 6438'
             6425  LOAD_FAST            53  'bn'
             6428  LOAD_FAST            47  'c'
             6431  BINARY_ADD       
             6432  STORE_FAST           53  'bn'
             6435  JUMP_BACK          6298  'to 6298'

 L.1116      6438  LOAD_FAST            54  'ol'
             6441  LOAD_FAST            47  'c'
             6444  BINARY_ADD       
             6445  STORE_FAST           54  'ol'
             6448  JUMP_BACK          6298  'to 6298'
             6451  POP_BLOCK        
           6452_0  COME_FROM          6291  '6291'

 L.1117      6452  LOAD_FAST            53  'bn'
             6455  LOAD_ATTR            23  'strip'
             6458  CALL_FUNCTION_0       0  None
             6461  STORE_FAST           53  'bn'

 L.1118      6464  LOAD_FAST            53  'bn'
             6467  POP_JUMP_IF_TRUE   6479  'to 6479'
             6470  LOAD_CONST               '_BLNK_'
             6473  STORE_FAST           53  'bn'
             6476  JUMP_FORWARD          0  'to 6479'
           6479_0  COME_FROM          6476  '6476'

 L.1119      6479  LOAD_FAST            52  'cl'
             6482  LOAD_ATTR            30  'append'
             6485  LOAD_FAST            53  'bn'
             6488  LOAD_FAST            54  'ol'
             6491  BUILD_LIST_2          2 
             6494  CALL_FUNCTION_1       1  None
             6497  POP_TOP          

 L.1120      6498  BUILD_MAP_0           0  None
             6501  STORE_FAST           55  'commonkey'

 L.1121      6504  LOAD_CONST               'common'
             6507  LOAD_GLOBAL          14  'groupcache'
             6510  LOAD_GLOBAL           5  'groupcounter'
             6513  BINARY_SUBSCR    
             6514  COMPARE_OP            6  in
             6517  POP_JUMP_IF_FALSE  6537  'to 6537'

 L.1122      6520  LOAD_GLOBAL          14  'groupcache'
             6523  LOAD_GLOBAL           5  'groupcounter'
             6526  BINARY_SUBSCR    
             6527  LOAD_CONST               'common'
             6530  BINARY_SUBSCR    
             6531  STORE_FAST           55  'commonkey'
             6534  JUMP_FORWARD          0  'to 6537'
           6537_0  COME_FROM          6534  '6534'

 L.1123      6537  SETUP_LOOP          151  'to 6691'
             6540  LOAD_FAST            52  'cl'
             6543  GET_ITER         
             6544  FOR_ITER            143  'to 6690'
             6547  STORE_FAST           47  'c'

 L.1124      6550  LOAD_FAST            47  'c'
             6553  LOAD_CONST               0
             6556  BINARY_SUBSCR    
             6557  LOAD_FAST            55  'commonkey'
             6560  COMPARE_OP            6  in
             6563  POP_JUMP_IF_FALSE  6582  'to 6582'

 L.1125      6566  LOAD_GLOBAL          11  'outmess'
             6569  LOAD_CONST               'analyzeline: previously defined common block encountered. Skipping.\n'
             6572  CALL_FUNCTION_1       1  None
             6575  POP_TOP          

 L.1126      6576  CONTINUE           6544  'to 6544'
             6579  JUMP_FORWARD          0  'to 6582'
           6582_0  COME_FROM          6579  '6579'

 L.1127      6582  BUILD_LIST_0          0 
             6585  LOAD_FAST            55  'commonkey'
             6588  LOAD_FAST            47  'c'
             6591  LOAD_CONST               0
             6594  BINARY_SUBSCR    
             6595  STORE_SUBSCR     

 L.1128      6596  SETUP_LOOP           88  'to 6687'
             6599  BUILD_LIST_0          0 
             6602  LOAD_GLOBAL          22  'markoutercomma'
             6605  LOAD_FAST            47  'c'
             6608  LOAD_CONST               1
             6611  BINARY_SUBSCR    
             6612  CALL_FUNCTION_1       1  None
             6615  LOAD_ATTR            10  'split'
             6618  LOAD_CONST               '@,@'
             6621  CALL_FUNCTION_1       1  None
             6624  GET_ITER         
             6625  FOR_ITER             18  'to 6646'
             6628  STORE_FAST            9  'x'
             6631  LOAD_FAST             9  'x'
             6634  LOAD_ATTR            23  'strip'
             6637  CALL_FUNCTION_0       0  None
             6640  LIST_APPEND           2  None
             6643  JUMP_BACK          6625  'to 6625'
             6646  GET_ITER         
             6647  FOR_ITER             36  'to 6686'
             6650  STORE_FAST           21  'i'

 L.1129      6653  LOAD_FAST            21  'i'
             6656  POP_JUMP_IF_FALSE  6647  'to 6647'
             6659  LOAD_FAST            55  'commonkey'
             6662  LOAD_FAST            47  'c'
             6665  LOAD_CONST               0
             6668  BINARY_SUBSCR    
             6669  BINARY_SUBSCR    
             6670  LOAD_ATTR            30  'append'
             6673  LOAD_FAST            21  'i'
             6676  CALL_FUNCTION_1       1  None
             6679  POP_TOP          
             6680  JUMP_BACK          6647  'to 6647'
             6683  JUMP_BACK          6647  'to 6647'
             6686  POP_BLOCK        
           6687_0  COME_FROM          6596  '6596'
             6687  JUMP_BACK          6544  'to 6544'
             6690  POP_BLOCK        
           6691_0  COME_FROM          6537  '6537'

 L.1130      6691  LOAD_FAST            55  'commonkey'
             6694  LOAD_GLOBAL          14  'groupcache'
             6697  LOAD_GLOBAL           5  'groupcounter'
             6700  BINARY_SUBSCR    
             6701  LOAD_CONST               'common'
             6704  STORE_SUBSCR     

 L.1131      6705  LOAD_CONST               'common'
             6708  LOAD_FAST            53  'bn'
             6711  LOAD_GLOBAL           5  'groupcounter'
             6714  BUILD_TUPLE_3         3 
             6717  STORE_GLOBAL          2  'previous_context'
             6720  JUMP_FORWARD        779  'to 7502'

 L.1132      6723  LOAD_FAST             1  'case'
             6726  LOAD_CONST               'use'
             6729  COMPARE_OP            2  ==
             6732  POP_JUMP_IF_FALSE  7177  'to 7177'

 L.1133      6735  LOAD_GLOBAL          17  're'
             6738  LOAD_ATTR            18  'match'
             6741  LOAD_CONST               '\\A\\s*(?P<name>\\b[\\w]+\\b)\\s*((,(\\s*\\bonly\\b\\s*:|(?P<notonly>))\\s*(?P<list>.*))|)\\s*\\Z'
             6744  LOAD_FAST             0  'm'
             6747  LOAD_ATTR             0  'group'
             6750  LOAD_CONST               'after'
             6753  CALL_FUNCTION_1       1  None
             6756  LOAD_GLOBAL          17  're'
             6759  LOAD_ATTR            19  'I'
             6762  CALL_FUNCTION_3       3  None
             6765  STORE_FAST           25  'm1'

 L.1134      6768  LOAD_FAST            25  'm1'
             6771  POP_JUMP_IF_FALSE  7153  'to 7153'

 L.1135      6774  LOAD_FAST            25  'm1'
             6777  LOAD_ATTR            44  'groupdict'
             6780  CALL_FUNCTION_0       0  None
             6783  STORE_FAST           56  'mm'

 L.1136      6786  LOAD_CONST               'use'
             6789  LOAD_GLOBAL          14  'groupcache'
             6792  LOAD_GLOBAL           5  'groupcounter'
             6795  BINARY_SUBSCR    
             6796  COMPARE_OP            7  not-in
             6799  POP_JUMP_IF_FALSE  6819  'to 6819'

 L.1137      6802  BUILD_MAP_0           0  None
             6805  LOAD_GLOBAL          14  'groupcache'
             6808  LOAD_GLOBAL           5  'groupcounter'
             6811  BINARY_SUBSCR    
             6812  LOAD_CONST               'use'
             6815  STORE_SUBSCR     
             6816  JUMP_FORWARD          0  'to 6819'
           6819_0  COME_FROM          6816  '6816'

 L.1138      6819  LOAD_FAST            25  'm1'
             6822  LOAD_ATTR             0  'group'
             6825  LOAD_CONST               'name'
             6828  CALL_FUNCTION_1       1  None
             6831  STORE_FAST            5  'name'

 L.1139      6834  BUILD_MAP_0           0  None
             6837  LOAD_GLOBAL          14  'groupcache'
             6840  LOAD_GLOBAL           5  'groupcounter'
             6843  BINARY_SUBSCR    
             6844  LOAD_CONST               'use'
             6847  BINARY_SUBSCR    
             6848  LOAD_FAST             5  'name'
             6851  STORE_SUBSCR     

 L.1140      6852  LOAD_CONST               0
             6855  STORE_FAST           57  'isonly'

 L.1141      6858  LOAD_CONST               'list'
             6861  LOAD_FAST            56  'mm'
             6864  COMPARE_OP            6  in
             6867  POP_JUMP_IF_FALSE  7174  'to 7174'
             6870  LOAD_FAST            56  'mm'
             6873  LOAD_CONST               'list'
             6876  BINARY_SUBSCR    
             6877  LOAD_CONST               None
             6880  COMPARE_OP            9  is-not
           6883_0  COME_FROM          6867  '6867'
             6883  POP_JUMP_IF_FALSE  7174  'to 7174'

 L.1142      6886  LOAD_CONST               'notonly'
             6889  LOAD_FAST            56  'mm'
             6892  COMPARE_OP            6  in
             6895  POP_JUMP_IF_FALSE  6923  'to 6923'
             6898  LOAD_FAST            56  'mm'
             6901  LOAD_CONST               'notonly'
             6904  BINARY_SUBSCR    
             6905  LOAD_CONST               None
             6908  COMPARE_OP            8  is
           6911_0  COME_FROM          6895  '6895'
             6911  POP_JUMP_IF_FALSE  6923  'to 6923'

 L.1143      6914  LOAD_CONST               1
             6917  STORE_FAST           57  'isonly'
             6920  JUMP_FORWARD          0  'to 6923'
           6923_0  COME_FROM          6920  '6920'

 L.1144      6923  LOAD_FAST            57  'isonly'
             6926  LOAD_GLOBAL          14  'groupcache'
             6929  LOAD_GLOBAL           5  'groupcounter'
             6932  BINARY_SUBSCR    
             6933  LOAD_CONST               'use'
             6936  BINARY_SUBSCR    
             6937  LOAD_FAST             5  'name'
             6940  BINARY_SUBSCR    
             6941  LOAD_CONST               'only'
             6944  STORE_SUBSCR     

 L.1145      6945  BUILD_LIST_0          0 
             6948  LOAD_FAST            56  'mm'
             6951  LOAD_CONST               'list'
             6954  BINARY_SUBSCR    
             6955  LOAD_ATTR            10  'split'
             6958  LOAD_CONST               ','
             6961  CALL_FUNCTION_1       1  None
             6964  GET_ITER         
             6965  FOR_ITER             18  'to 6986'
             6968  STORE_FAST            9  'x'
             6971  LOAD_FAST             9  'x'
             6974  LOAD_ATTR            23  'strip'
             6977  CALL_FUNCTION_0       0  None
             6980  LIST_APPEND           2  None
             6983  JUMP_BACK          6965  'to 6965'
             6986  STORE_FAST           20  'll'

 L.1146      6989  BUILD_MAP_0           0  None
             6992  STORE_FAST           58  'rl'

 L.1147      6995  SETUP_LOOP          152  'to 7150'
             6998  LOAD_FAST            20  'll'
             7001  GET_ITER         
             7002  FOR_ITER            141  'to 7146'
             7005  STORE_FAST           49  'l'

 L.1148      7008  LOAD_CONST               '='
             7011  LOAD_FAST            49  'l'
             7014  COMPARE_OP            6  in
             7017  POP_JUMP_IF_FALSE  7111  'to 7111'

 L.1149      7020  LOAD_GLOBAL          17  're'
             7023  LOAD_ATTR            18  'match'
             7026  LOAD_CONST               '\\A\\s*(?P<local>\\b[\\w]+\\b)\\s*=\\s*>\\s*(?P<use>\\b[\\w]+\\b)\\s*\\Z'
             7029  LOAD_FAST            49  'l'
             7032  LOAD_GLOBAL          17  're'
             7035  LOAD_ATTR            19  'I'
             7038  CALL_FUNCTION_3       3  None
             7041  STORE_FAST           34  'm2'

 L.1150      7044  LOAD_FAST            34  'm2'
             7047  POP_JUMP_IF_FALSE  7093  'to 7093'
             7050  LOAD_FAST            34  'm2'
             7053  LOAD_ATTR             0  'group'
             7056  LOAD_CONST               'use'
             7059  CALL_FUNCTION_1       1  None
             7062  LOAD_ATTR            23  'strip'
             7065  CALL_FUNCTION_0       0  None
             7068  LOAD_FAST            58  'rl'
             7071  LOAD_FAST            34  'm2'
             7074  LOAD_ATTR             0  'group'
             7077  LOAD_CONST               'local'
             7080  CALL_FUNCTION_1       1  None
             7083  LOAD_ATTR            23  'strip'
             7086  CALL_FUNCTION_0       0  None
             7089  STORE_SUBSCR     
             7090  JUMP_ABSOLUTE      7121  'to 7121'

 L.1152      7093  LOAD_GLOBAL          11  'outmess'
             7096  LOAD_CONST               'analyzeline: Not local=>use pattern found in %s\n'
             7099  LOAD_FAST            49  'l'
             7102  UNARY_CONVERT    
             7103  BINARY_MODULO    
             7104  CALL_FUNCTION_1       1  None
             7107  POP_TOP          
             7108  JUMP_FORWARD         10  'to 7121'

 L.1154      7111  LOAD_FAST            49  'l'
             7114  LOAD_FAST            58  'rl'
             7117  LOAD_FAST            49  'l'
             7120  STORE_SUBSCR     
           7121_0  COME_FROM          7108  '7108'

 L.1155      7121  LOAD_FAST            58  'rl'
             7124  LOAD_GLOBAL          14  'groupcache'
             7127  LOAD_GLOBAL           5  'groupcounter'
             7130  BINARY_SUBSCR    
             7131  LOAD_CONST               'use'
             7134  BINARY_SUBSCR    
             7135  LOAD_FAST             5  'name'
             7138  BINARY_SUBSCR    
             7139  LOAD_CONST               'map'
             7142  STORE_SUBSCR     
             7143  JUMP_BACK          7002  'to 7002'
             7146  POP_BLOCK        
           7147_0  COME_FROM          6995  '6995'
             7147  JUMP_ABSOLUTE      7174  'to 7174'

 L.1157      7150  JUMP_ABSOLUTE      7502  'to 7502'

 L.1159      7153  LOAD_FAST             0  'm'
             7156  LOAD_ATTR            44  'groupdict'
             7159  CALL_FUNCTION_0       0  None
             7162  PRINT_ITEM       
             7163  PRINT_NEWLINE_CONT

 L.1160      7164  LOAD_GLOBAL          11  'outmess'
             7167  LOAD_CONST               'analyzeline: Could not crack the use statement.\n'
             7170  CALL_FUNCTION_1       1  None
             7173  POP_TOP          
             7174  JUMP_FORWARD        325  'to 7502'

 L.1161      7177  LOAD_FAST             1  'case'
             7180  LOAD_CONST               ('f2pyenhancements',)
             7183  COMPARE_OP            6  in
             7186  POP_JUMP_IF_FALSE  7377  'to 7377'

 L.1162      7189  LOAD_CONST               'f2pyenhancements'
             7192  LOAD_GLOBAL          14  'groupcache'
             7195  LOAD_GLOBAL           5  'groupcounter'
             7198  BINARY_SUBSCR    
             7199  COMPARE_OP            7  not-in
             7202  POP_JUMP_IF_FALSE  7222  'to 7222'

 L.1163      7205  BUILD_MAP_0           0  None
             7208  LOAD_GLOBAL          14  'groupcache'
             7211  LOAD_GLOBAL           5  'groupcounter'
             7214  BINARY_SUBSCR    
             7215  LOAD_CONST               'f2pyenhancements'
             7218  STORE_SUBSCR     
             7219  JUMP_FORWARD          0  'to 7222'
           7222_0  COME_FROM          7219  '7219'

 L.1164      7222  LOAD_GLOBAL          14  'groupcache'
             7225  LOAD_GLOBAL           5  'groupcounter'
             7228  BINARY_SUBSCR    
             7229  LOAD_CONST               'f2pyenhancements'
             7232  BINARY_SUBSCR    
             7233  STORE_FAST           59  'd'

 L.1165      7236  LOAD_FAST             0  'm'
             7239  LOAD_ATTR             0  'group'
             7242  LOAD_CONST               'this'
             7245  CALL_FUNCTION_1       1  None
             7248  LOAD_CONST               'usercode'
             7251  COMPARE_OP            2  ==
             7254  POP_JUMP_IF_FALSE  7346  'to 7346'
             7257  LOAD_CONST               'usercode'
             7260  LOAD_FAST            59  'd'
             7263  COMPARE_OP            6  in
           7266_0  COME_FROM          7254  '7254'
             7266  POP_JUMP_IF_FALSE  7346  'to 7346'

 L.1166      7269  LOAD_GLOBAL          67  'type'
             7272  LOAD_FAST            59  'd'
             7275  LOAD_CONST               'usercode'
             7278  BINARY_SUBSCR    
             7279  CALL_FUNCTION_1       1  None
             7282  LOAD_GLOBAL          67  'type'
             7285  LOAD_CONST               ''
             7288  CALL_FUNCTION_1       1  None
             7291  COMPARE_OP            8  is
             7294  POP_JUMP_IF_FALSE  7317  'to 7317'

 L.1167      7297  LOAD_FAST            59  'd'
             7300  LOAD_CONST               'usercode'
             7303  BINARY_SUBSCR    
             7304  BUILD_LIST_1          1 
             7307  LOAD_FAST            59  'd'
             7310  LOAD_CONST               'usercode'
             7313  STORE_SUBSCR     
             7314  JUMP_FORWARD          0  'to 7317'
           7317_0  COME_FROM          7314  '7314'

 L.1168      7317  LOAD_FAST            59  'd'
             7320  LOAD_CONST               'usercode'
             7323  BINARY_SUBSCR    
             7324  LOAD_ATTR            30  'append'
             7327  LOAD_FAST             0  'm'
             7330  LOAD_ATTR             0  'group'
             7333  LOAD_CONST               'after'
             7336  CALL_FUNCTION_1       1  None
             7339  CALL_FUNCTION_1       1  None
             7342  POP_TOP          
             7343  JUMP_ABSOLUTE      7502  'to 7502'

 L.1170      7346  LOAD_FAST             0  'm'
             7349  LOAD_ATTR             0  'group'
             7352  LOAD_CONST               'after'
             7355  CALL_FUNCTION_1       1  None
             7358  LOAD_FAST            59  'd'
             7361  LOAD_FAST             0  'm'
             7364  LOAD_ATTR             0  'group'
             7367  LOAD_CONST               'this'
             7370  CALL_FUNCTION_1       1  None
             7373  STORE_SUBSCR     
             7374  JUMP_FORWARD        125  'to 7502'

 L.1171      7377  LOAD_FAST             1  'case'
             7380  LOAD_CONST               'multiline'
             7383  COMPARE_OP            2  ==
             7386  POP_JUMP_IF_FALSE  7466  'to 7466'

 L.1172      7389  LOAD_GLOBAL           2  'previous_context'
             7392  LOAD_CONST               None
             7395  COMPARE_OP            8  is
             7398  POP_JUMP_IF_FALSE  7424  'to 7424'

 L.1173      7401  LOAD_GLOBAL          27  'verbose'
             7404  POP_JUMP_IF_FALSE  7420  'to 7420'

 L.1174      7407  LOAD_GLOBAL          11  'outmess'
             7410  LOAD_CONST               'analyzeline: No context for multiline block.\n'
             7413  CALL_FUNCTION_1       1  None
             7416  POP_TOP          
             7417  JUMP_FORWARD          0  'to 7420'
           7420_0  COME_FROM          7417  '7417'

 L.1175      7420  LOAD_CONST               None
             7423  RETURN_VALUE     
           7424_0  COME_FROM          7398  '7398'

 L.1176      7424  LOAD_GLOBAL           5  'groupcounter'
             7427  STORE_FAST           60  'gc'

 L.1178      7430  LOAD_GLOBAL          68  'appendmultiline'
             7433  LOAD_GLOBAL          14  'groupcache'
             7436  LOAD_FAST            60  'gc'
             7439  BINARY_SUBSCR    

 L.1179      7440  LOAD_GLOBAL           2  'previous_context'
             7443  LOAD_CONST               2
             7446  SLICE+2          

 L.1180      7447  LOAD_FAST             0  'm'
             7450  LOAD_ATTR             0  'group'
             7453  LOAD_CONST               'this'
             7456  CALL_FUNCTION_1       1  None
             7459  CALL_FUNCTION_3       3  None
             7462  POP_TOP          
             7463  JUMP_FORWARD         36  'to 7502'

 L.1182      7466  LOAD_GLOBAL          27  'verbose'
             7469  LOAD_CONST               1
             7472  COMPARE_OP            4  >
             7475  POP_JUMP_IF_FALSE  7502  'to 7502'

 L.1183      7478  LOAD_FAST             0  'm'
             7481  LOAD_ATTR            44  'groupdict'
             7484  CALL_FUNCTION_0       0  None
             7487  PRINT_ITEM       
             7488  PRINT_NEWLINE_CONT

 L.1184      7489  LOAD_GLOBAL          11  'outmess'
             7492  LOAD_CONST               'analyzeline: No code implemented for line.\n'
             7495  CALL_FUNCTION_1       1  None
             7498  POP_TOP          
             7499  JUMP_FORWARD          0  'to 7502'
           7502_0  COME_FROM          7499  '7499'
           7502_1  COME_FROM          7463  '7463'
           7502_2  COME_FROM          7374  '7374'
           7502_3  COME_FROM          7174  '7174'
           7502_4  COME_FROM          6720  '6720'
           7502_5  COME_FROM          6202  '6202'
           7502_6  COME_FROM          5160  '5160'
           7502_7  COME_FROM          4427  '4427'
           7502_8  COME_FROM          3693  '3693'
           7502_9  COME_FROM          2591  '2591'
          7502_10  COME_FROM          2489  '2489'
          7502_11  COME_FROM          2301  '2301'
             7502  LOAD_CONST               None
             7505  RETURN_VALUE     

Parse error at or near `JUMP_FORWARD' instruction at offset 4667


def appendmultiline(group, context_name, ml):
    if 'f2pymultilines' not in group:
        group['f2pymultilines'] = {}
    d = group['f2pymultilines']
    if context_name not in d:
        d[context_name] = []
    d[context_name].append(ml)


def cracktypespec0(typespec, ll):
    selector = None
    attr = None
    if re.match('double\\s*complex', typespec, re.I):
        typespec = 'double complex'
    elif re.match('double\\s*precision', typespec, re.I):
        typespec = 'double precision'
    else:
        typespec = typespec.strip().lower()
    m1 = selectpattern.match(markouterparen(ll))
    if not m1:
        outmess('cracktypespec0: no kind/char_selector pattern found for line.\n')
        return
    else:
        d = m1.groupdict()
        for k in d.keys():
            d[k] = unmarkouterparen(d[k])

        if typespec in ('complex', 'integer', 'logical', 'real', 'character', 'type'):
            selector = d['this']
            ll = d['after']
        i = ll.find('::')
        if i >= 0:
            attr = ll[:i].strip()
            ll = ll[i + 2:]
        return (
         typespec, selector, attr, ll)


namepattern = re.compile('\\s*(?P<name>\\b[\\w]+\\b)\\s*(?P<after>.*)\\s*\\Z', re.I)
kindselector = re.compile('\\s*(\\(\\s*(kind\\s*=)?\\s*(?P<kind>.*)\\s*\\)|[*]\\s*(?P<kind2>.*?))\\s*\\Z', re.I)
charselector = re.compile('\\s*(\\((?P<lenkind>.*)\\)|[*]\\s*(?P<charlen>.*))\\s*\\Z', re.I)
lenkindpattern = re.compile('\\s*(kind\\s*=\\s*(?P<kind>.*?)\\s*(@,@\\s*len\\s*=\\s*(?P<len>.*)|)|(len\\s*=\\s*|)(?P<len2>.*?)\\s*(@,@\\s*(kind\\s*=\\s*|)(?P<kind2>.*)|))\\s*\\Z', re.I)
lenarraypattern = re.compile('\\s*(@\\(@\\s*(?!/)\\s*(?P<array>.*?)\\s*@\\)@\\s*[*]\\s*(?P<len>.*?)|([*]\\s*(?P<len2>.*?)|)\\s*(@\\(@\\s*(?!/)\\s*(?P<array2>.*?)\\s*@\\)@|))\\s*(=\\s*(?P<init>.*?)|(@\\(@|)/\\s*(?P<init2>.*?)\\s*/(@\\)@|)|)\\s*\\Z', re.I)

def removespaces(expr):
    expr = expr.strip()
    if len(expr) <= 1:
        return expr
    expr2 = expr[0]
    for i in range(1, len(expr) - 1):
        if expr[i] == ' ' and (expr[i + 1] in '()[]{}=+-/* ' or expr[i - 1] in '()[]{}=+-/* '):
            continue
        expr2 = expr2 + expr[i]

    expr2 = expr2 + expr[-1]
    return expr2


def markinnerspaces--- This code section failed: ---

 L.1232         0  LOAD_CONST               ''
                3  STORE_FAST            1  'l'
                6  LOAD_CONST               0
                9  STORE_FAST            2  'f'

 L.1233        12  LOAD_CONST               "'"
               15  STORE_FAST            3  'cc'

 L.1234        18  LOAD_CONST               '"'
               21  STORE_FAST            4  'cc1'

 L.1235        24  LOAD_CONST               ''
               27  STORE_FAST            5  'cb'

 L.1236        30  SETUP_LOOP          223  'to 256'
               33  LOAD_FAST             0  'line'
               36  GET_ITER         
               37  FOR_ITER            215  'to 255'
               40  STORE_FAST            6  'c'

 L.1237        43  LOAD_FAST             5  'cb'
               46  LOAD_CONST               '\\'
               49  COMPARE_OP            2  ==
               52  POP_JUMP_IF_FALSE    89  'to 89'
               55  LOAD_FAST             6  'c'
               58  LOAD_CONST               ('\\', "'", '"')
               61  COMPARE_OP            6  in
             64_0  COME_FROM            52  '52'
               64  POP_JUMP_IF_FALSE    89  'to 89'

 L.1238        67  LOAD_FAST             1  'l'
               70  LOAD_FAST             6  'c'
               73  BINARY_ADD       
               74  STORE_FAST            1  'l'

 L.1239        77  LOAD_FAST             6  'c'
               80  STORE_FAST            5  'cb'

 L.1240        83  CONTINUE             37  'to 37'
               86  JUMP_FORWARD          0  'to 89'
             89_0  COME_FROM            86  '86'

 L.1241        89  LOAD_FAST             2  'f'
               92  LOAD_CONST               0
               95  COMPARE_OP            2  ==
               98  POP_JUMP_IF_FALSE   146  'to 146'
              101  LOAD_FAST             6  'c'
              104  LOAD_CONST               ("'", '"')
              107  COMPARE_OP            6  in
            110_0  COME_FROM            98  '98'
              110  POP_JUMP_IF_FALSE   146  'to 146'
              113  LOAD_FAST             6  'c'
              116  STORE_FAST            3  'cc'
              119  BUILD_MAP_2           2  None
              122  LOAD_CONST               '"'
              125  LOAD_CONST               "'"
              128  STORE_MAP        
              129  LOAD_CONST               "'"
              132  LOAD_CONST               '"'
              135  STORE_MAP        
              136  LOAD_FAST             6  'c'
              139  BINARY_SUBSCR    
              140  STORE_FAST            4  'cc1'
              143  JUMP_FORWARD          0  'to 146'
            146_0  COME_FROM           143  '143'

 L.1242       146  LOAD_FAST             6  'c'
              149  LOAD_FAST             3  'cc'
              152  COMPARE_OP            2  ==
              155  POP_JUMP_IF_FALSE   171  'to 171'
              158  LOAD_FAST             2  'f'
              161  LOAD_CONST               1
              164  BINARY_ADD       
              165  STORE_FAST            2  'f'
              168  JUMP_FORWARD         65  'to 236'

 L.1243       171  LOAD_FAST             6  'c'
              174  LOAD_FAST             3  'cc'
              177  COMPARE_OP            2  ==
              180  POP_JUMP_IF_FALSE   196  'to 196'
              183  LOAD_FAST             2  'f'
              186  LOAD_CONST               1
              189  BINARY_SUBTRACT  
              190  STORE_FAST            2  'f'
              193  JUMP_FORWARD         40  'to 236'

 L.1244       196  LOAD_FAST             6  'c'
              199  LOAD_CONST               ' '
              202  COMPARE_OP            2  ==
              205  POP_JUMP_IF_FALSE   236  'to 236'
              208  LOAD_FAST             2  'f'
              211  LOAD_CONST               1
              214  COMPARE_OP            2  ==
            217_0  COME_FROM           205  '205'
              217  POP_JUMP_IF_FALSE   236  'to 236'
              220  LOAD_FAST             1  'l'
              223  LOAD_CONST               '@_@'
              226  BINARY_ADD       
              227  STORE_FAST            1  'l'
              230  JUMP_BACK            37  'to 37'
              233  JUMP_FORWARD          0  'to 236'
            236_0  COME_FROM           233  '233'
            236_1  COME_FROM           193  '193'
            236_2  COME_FROM           168  '168'

 L.1245       236  LOAD_FAST             1  'l'
              239  LOAD_FAST             6  'c'
              242  BINARY_ADD       
              243  STORE_FAST            1  'l'
              246  LOAD_FAST             6  'c'
              249  STORE_FAST            5  'cb'
              252  JUMP_BACK            37  'to 37'
              255  POP_BLOCK        
            256_0  COME_FROM            30  '30'

 L.1246       256  LOAD_FAST             1  'l'
              259  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `JUMP_FORWARD' instruction at offset 233


def updatevars(typespec, selector, attrspec, entitydecl):
    last_name = None
    kindselect, charselect, typename = cracktypespec(typespec, selector)
    if attrspec:
        attrspec = [ x.strip() for x in markoutercomma(attrspec).split('@,@') ]
        l = []
        c = re.compile('(?P<start>[a-zA-Z]+)')
        for a in attrspec:
            if not a:
                continue
            m = c.match(a)
            if m:
                s = m.group('start').lower()
                a = s + a[len(s):]
            l.append(a)

        attrspec = l
    el = [ x.strip() for x in markoutercomma(entitydecl).split('@,@') ]
    el1 = []
    for e in el:
        for e1 in [ x.strip() for x in markoutercomma(removespaces(markinnerspaces(e)), comma=' ').split('@ @') ]:
            if e1:
                el1.append(e1.replace('@_@', ' '))

    for e in el1:
        m = namepattern.match(e)
        if not m:
            outmess('updatevars: no name pattern found for entity=%s. Skipping.\n' % `e`)
            continue
        ename = rmbadname1(m.group('name'))
        edecl = {}
        if ename in groupcache[groupcounter]['vars']:
            edecl = groupcache[groupcounter]['vars'][ename].copy()
            not_has_typespec = 'typespec' not in edecl
            if not_has_typespec:
                edecl['typespec'] = typespec
            elif typespec and not typespec == edecl['typespec']:
                outmess('updatevars: attempt to change the type of "%s" ("%s") to "%s". Ignoring.\n' % (ename, edecl['typespec'], typespec))
            if 'kindselector' not in edecl:
                edecl['kindselector'] = copy.copy(kindselect)
            elif kindselect:
                for k in kindselect.keys():
                    if k in edecl['kindselector'] and not kindselect[k] == edecl['kindselector'][k]:
                        outmess('updatevars: attempt to change the kindselector "%s" of "%s" ("%s") to "%s". Ignoring.\n' % (k, ename, edecl['kindselector'][k], kindselect[k]))
                    else:
                        edecl['kindselector'][k] = copy.copy(kindselect[k])

            if 'charselector' not in edecl and charselect:
                if not_has_typespec:
                    edecl['charselector'] = charselect
                else:
                    errmess('updatevars:%s: attempt to change empty charselector to %r. Ignoring.\n' % (
                     ename, charselect))
            elif charselect:
                for k in charselect.keys():
                    if k in edecl['charselector'] and not charselect[k] == edecl['charselector'][k]:
                        outmess('updatevars: attempt to change the charselector "%s" of "%s" ("%s") to "%s". Ignoring.\n' % (k, ename, edecl['charselector'][k], charselect[k]))
                    else:
                        edecl['charselector'][k] = copy.copy(charselect[k])

            if 'typename' not in edecl:
                edecl['typename'] = typename
            elif typename and not edecl['typename'] == typename:
                outmess('updatevars: attempt to change the typename of "%s" ("%s") to "%s". Ignoring.\n' % (ename, edecl['typename'], typename))
            if 'attrspec' not in edecl:
                edecl['attrspec'] = copy.copy(attrspec)
            elif attrspec:
                for a in attrspec:
                    if a not in edecl['attrspec']:
                        edecl['attrspec'].append(a)

        else:
            edecl['typespec'] = copy.copy(typespec)
            edecl['kindselector'] = copy.copy(kindselect)
            edecl['charselector'] = copy.copy(charselect)
            edecl['typename'] = typename
            edecl['attrspec'] = copy.copy(attrspec)
        if m.group('after'):
            m1 = lenarraypattern.match(markouterparen(m.group('after')))
            if m1:
                d1 = m1.groupdict()
                for lk in ['len', 'array', 'init']:
                    if d1[lk + '2'] is not None:
                        d1[lk] = d1[lk + '2']
                        del d1[lk + '2']

                for k in d1.keys():
                    if d1[k] is not None:
                        d1[k] = unmarkouterparen(d1[k])
                    else:
                        del d1[k]

                if 'len' in d1 and 'array' in d1:
                    if d1['len'] == '':
                        d1['len'] = d1['array']
                        del d1['array']
                    else:
                        d1['array'] = d1['array'] + ',' + d1['len']
                        del d1['len']
                        errmess('updatevars: "%s %s" is mapped to "%s %s(%s)"\n' % (typespec, e, typespec, ename, d1['array']))
                if 'array' in d1:
                    dm = 'dimension(%s)' % d1['array']
                    if 'attrspec' not in edecl or not edecl['attrspec']:
                        edecl['attrspec'] = [
                         dm]
                    else:
                        edecl['attrspec'].append(dm)
                        for dm1 in edecl['attrspec']:
                            if dm1[:9] == 'dimension' and dm1 != dm:
                                del edecl['attrspec'][-1]
                                errmess('updatevars:%s: attempt to change %r to %r. Ignoring.\n' % (
                                 ename, dm1, dm))
                                break

                if 'len' in d1:
                    if typespec in ('complex', 'integer', 'logical', 'real'):
                        if 'kindselector' not in edecl or not edecl['kindselector']:
                            edecl['kindselector'] = {}
                        edecl['kindselector']['*'] = d1['len']
                    elif typespec == 'character':
                        if 'charselector' not in edecl or not edecl['charselector']:
                            edecl['charselector'] = {}
                        if 'len' in edecl['charselector']:
                            del edecl['charselector']['len']
                        edecl['charselector']['*'] = d1['len']
                if 'init' in d1:
                    if '=' in edecl and not edecl['='] == d1['init']:
                        outmess('updatevars: attempt to change the init expression of "%s" ("%s") to "%s". Ignoring.\n' % (ename, edecl['='], d1['init']))
                    else:
                        edecl['='] = d1['init']
            else:
                outmess('updatevars: could not crack entity declaration "%s". Ignoring.\n' % (ename + m.group('after')))
        for k in edecl.keys():
            if not edecl[k]:
                del edecl[k]

        groupcache[groupcounter]['vars'][ename] = edecl
        if 'varnames' in groupcache[groupcounter]:
            groupcache[groupcounter]['varnames'].append(ename)
        last_name = ename

    return last_name


def cracktypespec(typespec, selector):
    kindselect = None
    charselect = None
    typename = None
    if selector:
        if typespec in ('complex', 'integer', 'logical', 'real'):
            kindselect = kindselector.match(selector)
            if not kindselect:
                outmess('cracktypespec: no kindselector pattern found for %s\n' % `selector`)
                return
            kindselect = kindselect.groupdict()
            kindselect['*'] = kindselect['kind2']
            del kindselect['kind2']
            for k in kindselect.keys():
                if not kindselect[k]:
                    del kindselect[k]

            for k, i in kindselect.items():
                kindselect[k] = rmbadname1(i)

        elif typespec == 'character':
            charselect = charselector.match(selector)
            if not charselect:
                outmess('cracktypespec: no charselector pattern found for %s\n' % `selector`)
                return
            charselect = charselect.groupdict()
            charselect['*'] = charselect['charlen']
            del charselect['charlen']
            if charselect['lenkind']:
                lenkind = lenkindpattern.match(markoutercomma(charselect['lenkind']))
                lenkind = lenkind.groupdict()
                for lk in ['len', 'kind']:
                    if lenkind[lk + '2']:
                        lenkind[lk] = lenkind[lk + '2']
                    charselect[lk] = lenkind[lk]
                    del lenkind[lk + '2']

            del charselect['lenkind']
            for k in charselect.keys():
                if not charselect[k]:
                    del charselect[k]

            for k, i in charselect.items():
                charselect[k] = rmbadname1(i)

        else:
            if typespec == 'type':
                typename = re.match('\\s*\\(\\s*(?P<name>\\w+)\\s*\\)', selector, re.I)
                if typename:
                    typename = typename.group('name')
                else:
                    outmess('cracktypespec: no typename found in %s\n' % `(typespec + selector)`)
            else:
                outmess('cracktypespec: no selector used for %s\n' % `selector`)
    return (
     kindselect, charselect, typename)


def setattrspec(decl, attr, force=0):
    if not decl:
        decl = {}
    if not attr:
        return decl
    if 'attrspec' not in decl:
        decl['attrspec'] = [
         attr]
        return decl
    if force:
        decl['attrspec'].append(attr)
    if attr in decl['attrspec']:
        return decl
    if attr == 'static' and 'automatic' not in decl['attrspec']:
        decl['attrspec'].append(attr)
    elif attr == 'automatic' and 'static' not in decl['attrspec']:
        decl['attrspec'].append(attr)
    elif attr == 'public' and 'private' not in decl['attrspec']:
        decl['attrspec'].append(attr)
    elif attr == 'private' and 'public' not in decl['attrspec']:
        decl['attrspec'].append(attr)
    else:
        decl['attrspec'].append(attr)
    return decl


def setkindselector(decl, sel, force=0):
    if not decl:
        decl = {}
    if not sel:
        return decl
    if 'kindselector' not in decl:
        decl['kindselector'] = sel
        return decl
    for k in sel.keys():
        if force or k not in decl['kindselector']:
            decl['kindselector'][k] = sel[k]

    return decl


def setcharselector(decl, sel, force=0):
    if not decl:
        decl = {}
    if not sel:
        return decl
    if 'charselector' not in decl:
        decl['charselector'] = sel
        return decl
    for k in sel.keys():
        if force or k not in decl['charselector']:
            decl['charselector'][k] = sel[k]

    return decl


def getblockname(block, unknown='unknown'):
    if 'name' in block:
        return block['name']
    return unknown


def setmesstext(block):
    global filepositiontext
    try:
        filepositiontext = 'In: %s:%s\n' % (block['from'], block['name'])
    except:
        pass


def get_usedict(block):
    usedict = {}
    if 'parent_block' in block:
        usedict = get_usedict(block['parent_block'])
    if 'use' in block:
        usedict.update(block['use'])
    return usedict


def get_useparameters(block, param_map=None):
    global f90modulevars
    if param_map is None:
        param_map = {}
    usedict = get_usedict(block)
    if not usedict:
        return param_map
    else:
        for usename, mapping in usedict.items():
            usename = usename.lower()
            if usename not in f90modulevars:
                outmess('get_useparameters: no module %s info used by %s\n' % (usename, block.get('name')))
                continue
            mvars = f90modulevars[usename]
            params = get_parameters(mvars)
            if not params:
                continue
            if mapping:
                errmess('get_useparameters: mapping for %s not impl.' % mapping)
            for k, v in params.items():
                if k in param_map:
                    outmess('get_useparameters: overriding parameter %s with value from module %s' % (
                     `k`, `usename`))
                param_map[k] = v

        return param_map


def postcrack2(block, tab='', param_map=None):
    if not f90modulevars:
        return block
    else:
        if type(block) == types.ListType:
            ret = []
            for g in block:
                g = postcrack2(g, tab=tab + '\t', param_map=param_map)
                ret.append(g)

            return ret
        setmesstext(block)
        outmess('%sBlock: %s\n' % (tab, block['name']), 0)
        if param_map is None:
            param_map = get_useparameters(block)
        if param_map is not None and 'vars' in block:
            vars = block['vars']
            for n in vars.keys():
                var = vars[n]
                if 'kindselector' in var:
                    kind = var['kindselector']
                    if 'kind' in kind:
                        val = kind['kind']
                        if val in param_map:
                            kind['kind'] = param_map[val]

        new_body = []
        for b in block['body']:
            b = postcrack2(b, tab=tab + '\t', param_map=param_map)
            new_body.append(b)

        block['body'] = new_body
        return block


def postcrack(block, args=None, tab=''):
    """
    TODO:
          function return values
          determine expression types if in argument list
    """
    global usermodules
    if type(block) == types.ListType:
        gret = []
        uret = []
        for g in block:
            setmesstext(g)
            g = postcrack(g, tab=tab + '\t')
            if 'name' in g and '__user__' in g['name']:
                uret.append(g)
            else:
                gret.append(g)

        return uret + gret
    setmesstext(block)
    if not type(block) == types.DictType and 'block' not in block:
        raise Exception('postcrack: Expected block dictionary instead of ' + str(block))
    if 'name' in block and not block['name'] == 'unknown_interface':
        outmess('%sBlock: %s\n' % (tab, block['name']), 0)
    blocktype = block['block']
    block = analyzeargs(block)
    block = analyzecommon(block)
    block['vars'] = analyzevars(block)
    block['sortvars'] = sortvarnames(block['vars'])
    if 'args' in block and block['args']:
        args = block['args']
    block['body'] = analyzebody(block, args, tab=tab)
    userisdefined = []
    if 'use' in block:
        useblock = block['use']
        for k in useblock.keys():
            if '__user__' in k:
                userisdefined.append(k)

    else:
        useblock = {}
    name = ''
    if 'name' in block:
        name = block['name']
    if 'externals' in block and block['externals']:
        interfaced = []
        if 'interfaced' in block:
            interfaced = block['interfaced']
        mvars = copy.copy(block['vars'])
        if name:
            mname = name + '__user__routines'
        else:
            mname = 'unknown__user__routines'
        if mname in userisdefined:
            i = 1
            while '%s_%i' % (mname, i) in userisdefined:
                i = i + 1

            mname = '%s_%i' % (mname, i)
        interface = {'block': 'interface', 'body': [], 'vars': {}, 'name': name + '_user_interface'}
        for e in block['externals']:
            if e in interfaced:
                edef = []
                j = -1
                for b in block['body']:
                    j = j + 1
                    if b['block'] == 'interface':
                        i = -1
                        for bb in b['body']:
                            i = i + 1
                            if 'name' in bb and bb['name'] == e:
                                edef = copy.copy(bb)
                                del b['body'][i]
                                break

                        if edef:
                            if not b['body']:
                                del block['body'][j]
                            del interfaced[interfaced.index(e)]
                            break

                interface['body'].append(edef)
            elif e in mvars and not isexternal(mvars[e]):
                interface['vars'][e] = mvars[e]

        if interface['vars'] or interface['body']:
            block['interfaced'] = interfaced
            mblock = {'block': 'python module', 'body': [interface], 'vars': {}, 'name': mname, 'interfaced': block['externals']}
            useblock[mname] = {}
            usermodules.append(mblock)
    if useblock:
        block['use'] = useblock
    return block


def sortvarnames(vars):
    indep = []
    dep = []
    for v in vars.keys():
        if 'depend' in vars[v] and vars[v]['depend']:
            dep.append(v)
        else:
            indep.append(v)

    n = len(dep)
    i = 0
    while dep:
        v = dep[0]
        fl = 0
        for w in dep[1:]:
            if w in vars[v]['depend']:
                fl = 1
                break

        if fl:
            dep = dep[1:] + [v]
            i = i + 1
            if i > n:
                errmess('sortvarnames: failed to compute dependencies because of cyclic dependencies between ' + (', ').join(dep) + '\n')
                indep = indep + dep
                break
        else:
            indep.append(v)
            dep = dep[1:]
            n = len(dep)
            i = 0

    return indep


def analyzecommon(block):
    if not hascommon(block):
        return block
    commonvars = []
    for k in block['common'].keys():
        comvars = []
        for e in block['common'][k]:
            m = re.match('\\A\\s*\\b(?P<name>.*?)\\b\\s*(\\((?P<dims>.*?)\\)|)\\s*\\Z', e, re.I)
            if m:
                dims = []
                if m.group('dims'):
                    dims = [ x.strip() for x in markoutercomma(m.group('dims')).split('@,@') ]
                n = m.group('name').strip()
                if n in block['vars']:
                    if 'attrspec' in block['vars'][n]:
                        block['vars'][n]['attrspec'].append('dimension(%s)' % (',').join(dims))
                    else:
                        block['vars'][n]['attrspec'] = [
                         'dimension(%s)' % (',').join(dims)]
                elif dims:
                    block['vars'][n] = {'attrspec': ['dimension(%s)' % (',').join(dims)]}
                else:
                    block['vars'][n] = {}
                if n not in commonvars:
                    commonvars.append(n)
            else:
                n = e
                errmess('analyzecommon: failed to extract "<name>[(<dims>)]" from "%s" in common /%s/.\n' % (e, k))
            comvars.append(n)

        block['common'][k] = comvars

    if 'commonvars' not in block:
        block['commonvars'] = commonvars
    else:
        block['commonvars'] = block['commonvars'] + commonvars
    return block


def analyzebody(block, args, tab=''):
    global onlyfuncs
    global skipfuncs
    setmesstext(block)
    body = []
    for b in block['body']:
        b['parent_block'] = block
        if b['block'] in ('function', 'subroutine'):
            if args is not None and b['name'] not in args:
                continue
            else:
                as_ = b['args']
            if b['name'] in skipfuncs:
                continue
            if onlyfuncs and b['name'] not in onlyfuncs:
                continue
            b['saved_interface'] = crack2fortrangen(b, '\n' + '      ', as_interface=True)
        else:
            as_ = args
        b = postcrack(b, as_, tab=tab + '\t')
        if b['block'] == 'interface' and not b['body']:
            if 'f2pyenhancements' not in b:
                continue
        if b['block'].replace(' ', '') == 'pythonmodule':
            usermodules.append(b)
        else:
            if b['block'] == 'module':
                f90modulevars[b['name']] = b['vars']
            body.append(b)

    return body


def buildimplicitrules(block):
    setmesstext(block)
    implicitrules = defaultimplicitrules
    attrrules = {}
    if 'implicit' in block:
        if block['implicit'] is None:
            implicitrules = None
            if verbose > 1:
                outmess('buildimplicitrules: no implicit rules for routine %s.\n' % `(block['name'])`)
        else:
            for k in block['implicit'].keys():
                if block['implicit'][k].get('typespec') not in ('static', 'automatic'):
                    implicitrules[k] = block['implicit'][k]
                else:
                    attrrules[k] = block['implicit'][k]['typespec']

    return (
     implicitrules, attrrules)


def myeval(e, g=None, l=None):
    r = eval(e, g, l)
    if type(r) in [type(0), type(0.0)]:
        return r
    raise ValueError('r=%r' % r)


getlincoef_re_1 = re.compile('\\A\\b\\w+\\b\\Z', re.I)

def getlincoef(e, xset):
    try:
        c = int(myeval(e, {}, {}))
        return (0, c, None)
    except:
        pass

    if getlincoef_re_1.match(e):
        return (1, 0, e)
    else:
        len_e = len(e)
        for x in xset:
            if len(x) > len_e:
                continue
            if re.search('\\w\\s*\\([^)]*\\b' + x + '\\b', e):
                continue
            re_1 = re.compile('(?P<before>.*?)\\b' + x + '\\b(?P<after>.*)', re.I)
            m = re_1.match(e)
            if m:
                try:
                    m1 = re_1.match(e)
                    while m1:
                        ee = '%s(%s)%s' % (m1.group('before'), 0, m1.group('after'))
                        m1 = re_1.match(ee)

                    b = myeval(ee, {}, {})
                    m1 = re_1.match(e)
                    while m1:
                        ee = '%s(%s)%s' % (m1.group('before'), 1, m1.group('after'))
                        m1 = re_1.match(ee)

                    a = myeval(ee, {}, {}) - b
                    m1 = re_1.match(e)
                    while m1:
                        ee = '%s(%s)%s' % (m1.group('before'), 0.5, m1.group('after'))
                        m1 = re_1.match(ee)

                    c = myeval(ee, {}, {})
                    m1 = re_1.match(e)
                    while m1:
                        ee = '%s(%s)%s' % (m1.group('before'), 1.5, m1.group('after'))
                        m1 = re_1.match(ee)

                    c2 = myeval(ee, {}, {})
                    if a * 0.5 + b == c and a * 1.5 + b == c2:
                        return (a, b, x)
                except:
                    pass

                break

        return (None, None, None)


_varname_match = re.compile('\\A[a-z]\\w*\\Z').match

def getarrlen(dl, args, star='*'):
    edl = []
    try:
        edl.append(myeval(dl[0], {}, {}))
    except:
        edl.append(dl[0])

    try:
        edl.append(myeval(dl[1], {}, {}))
    except:
        edl.append(dl[1])

    if type(edl[0]) is type(0):
        p1 = 1 - edl[0]
        if p1 == 0:
            d = str(dl[1])
        else:
            if p1 < 0:
                d = '%s-%s' % (dl[1], -p1)
            else:
                d = '%s+%s' % (dl[1], p1)
    else:
        if type(edl[1]) is type(0):
            p1 = 1 + edl[1]
            if p1 == 0:
                d = '-(%s)' % dl[0]
            else:
                d = '%s-(%s)' % (p1, dl[0])
        else:
            d = '%s-(%s)+1' % (dl[1], dl[0])
        try:
            return (`(myeval(d, {}, {}))`, None, None)
        except:
            pass

    d1, d2 = getlincoef(dl[0], args), getlincoef(dl[1], args)
    if None not in [d1[0], d2[0]]:
        if (
         d1[0], d2[0]) == (0, 0):
            return (`(d2[1] - d1[1] + 1)`, None, None)
        b = d2[1] - d1[1] + 1
        d1 = (d1[0], 0, d1[2])
        d2 = (d2[0], b, d2[2])
        if d1[0] == 0 and d2[2] in args:
            if b < 0:
                return ('%s * %s - %s' % (d2[0], d2[2], -b), d2[2], '+%s)/(%s)' % (-b, d2[0]))
            else:
                if b:
                    return ('%s * %s + %s' % (d2[0], d2[2], b), d2[2], '-%s)/(%s)' % (b, d2[0]))
                return (
                 '%s * %s' % (d2[0], d2[2]), d2[2], ')/(%s)' % d2[0])

        if d2[0] == 0 and d1[2] in args:
            if b < 0:
                return ('%s * %s - %s' % (-d1[0], d1[2], -b), d1[2], '+%s)/(%s)' % (-b, -d1[0]))
            else:
                if b:
                    return ('%s * %s + %s' % (-d1[0], d1[2], b), d1[2], '-%s)/(%s)' % (b, -d1[0]))
                return (
                 '%s * %s' % (-d1[0], d1[2]), d1[2], ')/(%s)' % -d1[0])

        if d1[2] == d2[2] and d1[2] in args:
            a = d2[0] - d1[0]
            if not a:
                return (`b`, None, None)
            if b < 0:
                return ('%s * %s - %s' % (a, d1[2], -b), d2[2], '+%s)/(%s)' % (-b, a))
            if b:
                return ('%s * %s + %s' % (a, d1[2], b), d2[2], '-%s)/(%s)' % (b, a))
            return (
             '%s * %s' % (a, d1[2]), d2[2], ')/(%s)' % a)
        if d1[0] == d2[0] == 1:
            c = str(d1[2])
            if c not in args:
                if _varname_match(c):
                    outmess('\tgetarrlen:variable "%s" undefined\n' % c)
                c = '(%s)' % c
            if b == 0:
                d = '%s-%s' % (d2[2], c)
            else:
                if b < 0:
                    d = '%s-%s-%s' % (d2[2], c, -b)
                else:
                    d = '%s-%s+%s' % (d2[2], c, b)
        else:
            if d1[0] == 0:
                c2 = str(d2[2])
                if c2 not in args:
                    if _varname_match(c2):
                        outmess('\tgetarrlen:variable "%s" undefined\n' % c2)
                    c2 = '(%s)' % c2
                if d2[0] == 1:
                    pass
                elif d2[0] == -1:
                    c2 = '-%s' % c2
                else:
                    c2 = '%s*%s' % (d2[0], c2)
                if b == 0:
                    d = c2
                else:
                    if b < 0:
                        d = '%s-%s' % (c2, -b)
                    else:
                        d = '%s+%s' % (c2, b)
            elif d2[0] == 0:
                c1 = str(d1[2])
                if c1 not in args:
                    if _varname_match(c1):
                        outmess('\tgetarrlen:variable "%s" undefined\n' % c1)
                    c1 = '(%s)' % c1
                if d1[0] == 1:
                    c1 = '-%s' % c1
                elif d1[0] == -1:
                    c1 = '+%s' % c1
                elif d1[0] < 0:
                    c1 = '+%s*%s' % (-d1[0], c1)
                else:
                    c1 = '-%s*%s' % (d1[0], c1)
                if b == 0:
                    d = c1
                else:
                    if b < 0:
                        d = '%s-%s' % (c1, -b)
                    else:
                        d = '%s+%s' % (c1, b)
        c1 = str(d1[2])
        if c1 not in args:
            if _varname_match(c1):
                outmess('\tgetarrlen:variable "%s" undefined\n' % c1)
            c1 = '(%s)' % c1
        if d1[0] == 1:
            c1 = '-%s' % c1
        elif d1[0] == -1:
            c1 = '+%s' % c1
        elif d1[0] < 0:
            c1 = '+%s*%s' % (-d1[0], c1)
        else:
            c1 = '-%s*%s' % (d1[0], c1)
        c2 = str(d2[2])
        if c2 not in args:
            if _varname_match(c2):
                outmess('\tgetarrlen:variable "%s" undefined\n' % c2)
            c2 = '(%s)' % c2
        if d2[0] == 1:
            pass
        elif d2[0] == -1:
            c2 = '-%s' % c2
        else:
            c2 = '%s*%s' % (d2[0], c2)
        if b == 0:
            d = '%s%s' % (c2, c1)
        else:
            if b < 0:
                d = '%s%s-%s' % (c2, c1, -b)
            else:
                d = '%s%s+%s' % (c2, c1, b)
    return (
     d, None, None)


word_pattern = re.compile('\\b[a-z][\\w$]*\\b', re.I)

def _get_depend_dict(name, vars, deps):
    if name in vars:
        words = vars[name].get('depend', [])
        if '=' in vars[name] and not isstring(vars[name]):
            for word in word_pattern.findall(vars[name]['=']):
                if word not in words and word in vars:
                    words.append(word)

        for word in words[:]:
            for w in deps.get(word, []) or _get_depend_dict(word, vars, deps):
                if w not in words:
                    words.append(w)

    else:
        outmess('_get_depend_dict: no dependence info for %s\n' % `name`)
        words = []
    deps[name] = words
    return words


def _calc_depend_dict(vars):
    names = vars.keys()
    depend_dict = {}
    for n in names:
        _get_depend_dict(n, vars, depend_dict)

    return depend_dict


def get_sorted_names(vars):
    """
    """
    depend_dict = _calc_depend_dict(vars)
    names = []
    for name in depend_dict.keys():
        if not depend_dict[name]:
            names.append(name)
            del depend_dict[name]

    while depend_dict:
        for name, lst in depend_dict.items():
            new_lst = [ n for n in lst if n in depend_dict ]
            if not new_lst:
                names.append(name)
                del depend_dict[name]
            else:
                depend_dict[name] = new_lst

    return [ name for name in names if name in vars ]


def _kind_func(string):
    if string[0] in '\'"':
        string = string[1:-1]
    if real16pattern.match(string):
        return 8
    if real8pattern.match(string):
        return 4
    return 'kind(' + string + ')'


def _selected_int_kind_func(r):
    m = 10 ** r
    if m <= 256:
        return 1
    if m <= 65536:
        return 2
    if m <= 4294967296:
        return 4
    if m <= 9223372036854775808:
        return 8
    if m <= 340282366920938463463374607431768211456:
        return 16
    return -1


def _selected_real_kind_func(p, r=0, radix=0):
    if p < 7:
        return 4
    if p < 16:
        return 8
    if platform.machine().lower().startswith('power'):
        if p <= 20:
            return 16
    else:
        if p < 19:
            return 10
        if p <= 20:
            return 16
    return -1


def get_parameters(vars, global_params={}):
    params = copy.copy(global_params)
    g_params = copy.copy(global_params)
    for name, func in [('kind', _kind_func),
     (
      'selected_int_kind', _selected_int_kind_func),
     (
      'selected_real_kind', _selected_real_kind_func)]:
        if name not in g_params:
            g_params[name] = func

    param_names = []
    for n in get_sorted_names(vars):
        if 'attrspec' in vars[n] and 'parameter' in vars[n]['attrspec']:
            param_names.append(n)

    kind_re = re.compile('\\bkind\\s*\\(\\s*(?P<value>.*)\\s*\\)', re.I)
    selected_int_kind_re = re.compile('\\bselected_int_kind\\s*\\(\\s*(?P<value>.*)\\s*\\)', re.I)
    selected_kind_re = re.compile('\\bselected_(int|real)_kind\\s*\\(\\s*(?P<value>.*)\\s*\\)', re.I)
    for n in param_names:
        if '=' in vars[n]:
            v = vars[n]['=']
            if islogical(vars[n]):
                v = v.lower()
                for repl in [
                 ('.false.', 'False'),
                 ('.true.', 'True')]:
                    v = v.replace(*repl)

            v = kind_re.sub('kind("\\1")', v)
            v = selected_int_kind_re.sub('selected_int_kind(\\1)', v)
            if isinteger(vars[n]) and not selected_kind_re.match(v):
                v = v.split('_')[0]
            if isdouble(vars[n]):
                tt = list(v)
                for m in real16pattern.finditer(v):
                    tt[(m.start()):(m.end())] = list(v[m.start():m.end()].lower().replace('d', 'e'))

                v = ('').join(tt)
            if iscomplex(vars[n]):
                if v[0] == '(' and v[-1] == ')':
                    l = markoutercomma(v[1:-1]).split('@,@')
            try:
                params[n] = eval(v, g_params, params)
            except Exception as msg:
                params[n] = v
                outmess('get_parameters: got "%s" on %s\n' % (msg, `v`))

            if isstring(vars[n]) and type(params[n]) is type(0):
                params[n] = chr(params[n])
            nl = n.lower()
            if nl != n:
                params[nl] = params[n]
        else:
            print vars[n]
            outmess('get_parameters:parameter %s does not have value?!\n' % `n`)

    return params


def _eval_length(length, params):
    if length in ('(:)', '(*)', '*'):
        return '(*)'
    return _eval_scalar(length, params)


_is_kind_number = re.compile('\\d+_').match

def _eval_scalar(value, params):
    if _is_kind_number(value):
        value = value.split('_')[0]
    try:
        value = str(eval(value, {}, params))
    except (NameError, SyntaxError):
        return value
    except Exception as msg:
        errmess('"%s" in evaluating %r (available names: %s)\n' % (
         msg, value, params.keys()))

    return value


def analyzevars(block):
    setmesstext(block)
    implicitrules, attrrules = buildimplicitrules(block)
    vars = copy.copy(block['vars'])
    if block['block'] == 'function' and block['name'] not in vars:
        vars[block['name']] = {}
    if '' in block['vars']:
        del vars['']
        if 'attrspec' in block['vars']['']:
            gen = block['vars']['']['attrspec']
            for n in vars.keys():
                for k in ['public', 'private']:
                    if k in gen:
                        vars[n] = setattrspec(vars[n], k)

    svars = []
    args = block['args']
    for a in args:
        try:
            vars[a]
            svars.append(a)
        except KeyError:
            pass

    for n in vars.keys():
        if n not in args:
            svars.append(n)

    params = get_parameters(vars, get_useparameters(block))
    dep_matches = {}
    name_match = re.compile('\\w[\\w\\d_$]*').match
    for v in vars.keys():
        m = name_match(v)
        if m:
            n = v[m.start():m.end()]
            try:
                dep_matches[n]
            except KeyError:
                dep_matches[n] = re.compile('.*\\b%s\\b' % v, re.I).match

    for n in svars:
        if n[0] in attrrules.keys():
            vars[n] = setattrspec(vars[n], attrrules[n[0]])
        if 'typespec' not in vars[n]:
            if not ('attrspec' in vars[n] and 'external' in vars[n]['attrspec']):
                if implicitrules:
                    ln0 = n[0].lower()
                    for k in implicitrules[ln0].keys():
                        if k == 'typespec' and implicitrules[ln0][k] == 'undefined':
                            continue
                        if k not in vars[n]:
                            vars[n][k] = implicitrules[ln0][k]
                        elif k == 'attrspec':
                            for l in implicitrules[ln0][k]:
                                vars[n] = setattrspec(vars[n], l)

                elif n in block['args']:
                    outmess('analyzevars: typespec of variable %s is not defined in routine %s.\n' % (`n`, block['name']))
        if 'charselector' in vars[n]:
            if 'len' in vars[n]['charselector']:
                l = vars[n]['charselector']['len']
                try:
                    l = str(eval(l, {}, params))
                except:
                    pass

                vars[n]['charselector']['len'] = l
        if 'kindselector' in vars[n]:
            if 'kind' in vars[n]['kindselector']:
                l = vars[n]['kindselector']['kind']
                try:
                    l = str(eval(l, {}, params))
                except:
                    pass

                vars[n]['kindselector']['kind'] = l
        savelindims = {}
        if 'attrspec' in vars[n]:
            attr = vars[n]['attrspec']
            attr.reverse()
            vars[n]['attrspec'] = []
            dim, intent, depend, check, note = (None, None, None, None, None)
            for a in attr:
                if a[:9] == 'dimension':
                    dim = a[9:].strip()[1:-1]
                elif a[:6] == 'intent':
                    intent = a[6:].strip()[1:-1]
                elif a[:6] == 'depend':
                    depend = a[6:].strip()[1:-1]
                elif a[:5] == 'check':
                    check = a[5:].strip()[1:-1]
                elif a[:4] == 'note':
                    note = a[4:].strip()[1:-1]
                else:
                    vars[n] = setattrspec(vars[n], a)
                if intent:
                    if 'intent' not in vars[n]:
                        vars[n]['intent'] = []
                    for c in [ x.strip() for x in markoutercomma(intent).split('@,@') ]:
                        if c not in vars[n]['intent']:
                            vars[n]['intent'].append(c)

                    intent = None
                if note:
                    note = note.replace('\\n\\n', '\n\n')
                    note = note.replace('\\n ', '\n')
                    if 'note' not in vars[n]:
                        vars[n]['note'] = [
                         note]
                    else:
                        vars[n]['note'].append(note)
                    note = None
                if depend is not None:
                    if 'depend' not in vars[n]:
                        vars[n]['depend'] = []
                    for c in rmbadname([ x.strip() for x in markoutercomma(depend).split('@,@') ]):
                        if c not in vars[n]['depend']:
                            vars[n]['depend'].append(c)

                    depend = None
                if check is not None:
                    if 'check' not in vars[n]:
                        vars[n]['check'] = []
                    for c in [ x.strip() for x in markoutercomma(check).split('@,@') ]:
                        if c not in vars[n]['check']:
                            vars[n]['check'].append(c)

                    check = None

            if dim and 'dimension' not in vars[n]:
                vars[n]['dimension'] = []
                for d in rmbadname([ x.strip() for x in markoutercomma(dim).split('@,@') ]):
                    star = '*'
                    if d == ':':
                        star = ':'
                    if d in params:
                        d = str(params[d])
                    for p in params.keys():
                        m = re.match('(?P<before>.*?)\\b' + p + '\\b(?P<after>.*)', d, re.I)
                        if m:
                            d = m.group('before') + str(params[p]) + m.group('after')

                    if d == star:
                        dl = [
                         star]
                    else:
                        dl = markoutercomma(d, ':').split('@:@')
                    if len(dl) == 2 and '*' in dl:
                        dl = [
                         '*']
                        d = '*'
                    if len(dl) == 1 and not dl[0] == star:
                        dl = ['1', dl[0]]
                    if len(dl) == 2:
                        d, v, di = getarrlen(dl, block['vars'].keys())
                        if d[:4] == '1 * ':
                            d = d[4:]
                        if di and di[-4:] == '/(1)':
                            di = di[:-4]
                        if v:
                            savelindims[d] = (v, di)
                    vars[n]['dimension'].append(d)

        if 'dimension' in vars[n]:
            if isintent_c(vars[n]):
                shape_macro = 'shape'
            else:
                shape_macro = 'shape'
            if isstringarray(vars[n]):
                if 'charselector' in vars[n]:
                    d = vars[n]['charselector']
                    if '*' in d:
                        d = d['*']
                        errmess('analyzevars: character array "character*%s %s(%s)" is considered as "character %s(%s)"; "intent(c)" is forced.\n' % (
                         d, n,
                         (',').join(vars[n]['dimension']),
                         n, (',').join(vars[n]['dimension'] + [d])))
                        vars[n]['dimension'].append(d)
                        del vars[n]['charselector']
                        if 'intent' not in vars[n]:
                            vars[n]['intent'] = []
                        if 'c' not in vars[n]['intent']:
                            vars[n]['intent'].append('c')
                    else:
                        errmess('analyzevars: charselector=%r unhandled.' % d)
        if 'check' not in vars[n] and 'args' in block and n in block['args']:
            flag = 'depend' not in vars[n]
            if flag:
                vars[n]['depend'] = []
            vars[n]['check'] = []
            if 'dimension' in vars[n]:
                i = -1
                ni = len(vars[n]['dimension'])
                for d in vars[n]['dimension']:
                    ddeps = []
                    ad = ''
                    pd = ''
                    if d not in vars:
                        if d in savelindims:
                            pd, ad = '(', savelindims[d][1]
                            d = savelindims[d][0]
                        else:
                            for r in block['args']:
                                if r not in vars:
                                    continue
                                if re.match('.*?\\b' + r + '\\b', d, re.I):
                                    ddeps.append(r)

                    if d in vars:
                        if 'attrspec' in vars[d]:
                            for aa in vars[d]['attrspec']:
                                if aa[:6] == 'depend':
                                    ddeps += aa[6:].strip()[1:-1].split(',')

                        if 'depend' in vars[d]:
                            ddeps = ddeps + vars[d]['depend']
                    i = i + 1
                    if d in vars and 'depend' not in vars[d] and '=' not in vars[d] and d not in vars[n]['depend'] and l_or(isintent_in, isintent_inout, isintent_inplace)(vars[n]):
                        vars[d]['depend'] = [
                         n]
                        if ni > 1:
                            vars[d]['='] = '%s%s(%s,%s)%s' % (pd, shape_macro, n, i, ad)
                        else:
                            vars[d]['='] = '%slen(%s)%s' % (pd, n, ad)
                        if 1 and 'check' not in vars[d]:
                            if ni > 1:
                                vars[d]['check'] = ['%s%s(%s,%i)%s==%s' % (
                                  pd, shape_macro, n, i, ad, d)]
                            else:
                                vars[d]['check'] = [
                                 '%slen(%s)%s>=%s' % (pd, n, ad, d)]
                        if 'attrspec' not in vars[d]:
                            vars[d]['attrspec'] = [
                             'optional']
                        if 'optional' not in vars[d]['attrspec'] and 'required' not in vars[d]['attrspec']:
                            vars[d]['attrspec'].append('optional')
                    elif d not in ('*', ':'):
                        if flag:
                            if d in vars:
                                if n not in ddeps:
                                    vars[n]['depend'].append(d)
                            else:
                                vars[n]['depend'] = vars[n]['depend'] + ddeps

            elif isstring(vars[n]):
                length = '1'
                if 'charselector' in vars[n]:
                    if '*' in vars[n]['charselector']:
                        length = _eval_length(vars[n]['charselector']['*'], params)
                        vars[n]['charselector']['*'] = length
                    elif 'len' in vars[n]['charselector']:
                        length = _eval_length(vars[n]['charselector']['len'], params)
                        del vars[n]['charselector']['len']
                        vars[n]['charselector']['*'] = length
            if not vars[n]['check']:
                del vars[n]['check']
            if flag and not vars[n]['depend']:
                del vars[n]['depend']
        if '=' in vars[n]:
            if 'attrspec' not in vars[n]:
                vars[n]['attrspec'] = []
            if 'optional' not in vars[n]['attrspec'] and 'required' not in vars[n]['attrspec']:
                vars[n]['attrspec'].append('optional')
            if 'depend' not in vars[n]:
                vars[n]['depend'] = []
                for v, m in dep_matches.items():
                    if m(vars[n]['=']):
                        vars[n]['depend'].append(v)

                if not vars[n]['depend']:
                    del vars[n]['depend']
            if isscalar(vars[n]):
                vars[n]['='] = _eval_scalar(vars[n]['='], params)

    for n in vars.keys():
        if n == block['name']:
            if 'note' in vars[n]:
                block['note'] = vars[n]['note']
            if block['block'] == 'function':
                if 'result' in block and block['result'] in vars:
                    vars[n] = appenddecl(vars[n], vars[block['result']])
                if 'prefix' in block:
                    pr = block['prefix']
                    ispure = 0
                    isrec = 1
                    pr1 = pr.replace('pure', '')
                    ispure = not pr == pr1
                    pr = pr1.replace('recursive', '')
                    isrec = not pr == pr1
                    m = typespattern[0].match(pr)
                    if m:
                        typespec, selector, attr, edecl = cracktypespec0(m.group('this'), m.group('after'))
                        kindselect, charselect, typename = cracktypespec(typespec, selector)
                        vars[n]['typespec'] = typespec
                        if kindselect:
                            if 'kind' in kindselect:
                                try:
                                    kindselect['kind'] = eval(kindselect['kind'], {}, params)
                                except:
                                    pass

                            vars[n]['kindselector'] = kindselect
                        if charselect:
                            vars[n]['charselector'] = charselect
                        if typename:
                            vars[n]['typename'] = typename
                        if ispure:
                            vars[n] = setattrspec(vars[n], 'pure')
                        if isrec:
                            vars[n] = setattrspec(vars[n], 'recursive')
                    else:
                        outmess('analyzevars: prefix (%s) were not used\n' % `(block['prefix'])`)

    if block['block'] not in ('module', 'pythonmodule', 'python module', 'block data'):
        if 'commonvars' in block:
            neededvars = copy.copy(block['args'] + block['commonvars'])
        else:
            neededvars = copy.copy(block['args'])
        for n in vars.keys():
            if l_or(isintent_callback, isintent_aux)(vars[n]):
                neededvars.append(n)

        if 'entry' in block:
            neededvars.extend(block['entry'].keys())
            for k in block['entry'].keys():
                for n in block['entry'][k]:
                    if n not in neededvars:
                        neededvars.append(n)

        if block['block'] == 'function':
            if 'result' in block:
                neededvars.append(block['result'])
            else:
                neededvars.append(block['name'])
        if block['block'] in ('subroutine', 'function'):
            name = block['name']
            if name in vars and 'intent' in vars[name]:
                block['intent'] = vars[name]['intent']
        if block['block'] == 'type':
            neededvars.extend(vars.keys())
        for n in vars.keys():
            if n not in neededvars:
                del vars[n]

    return vars


analyzeargs_re_1 = re.compile('\\A[a-z]+[\\w$]*\\Z', re.I)

def expr2name(a, block, args=[]):
    orig_a = a
    a_is_expr = not analyzeargs_re_1.match(a)
    if a_is_expr:
        implicitrules, attrrules = buildimplicitrules(block)
        at = determineexprtype(a, block['vars'], implicitrules)
        na = 'e_'
        for c in a:
            c = c.lower()
            if c not in string.lowercase + string.digits:
                c = '_'
            na = na + c

        if na[-1] == '_':
            na = na + 'e'
        else:
            na = na + '_e'
        a = na
        while a in block['vars'] or a in block['args']:
            a = a + 'r'

    if a in args:
        k = 1
        while a + str(k) in args:
            k = k + 1

        a = a + str(k)
    if a_is_expr:
        block['vars'][a] = at
    else:
        if a not in block['vars']:
            if orig_a in block['vars']:
                block['vars'][a] = block['vars'][orig_a]
            else:
                block['vars'][a] = {}
        if 'externals' in block and orig_a in block['externals'] + block['interfaced']:
            block['vars'][a] = setattrspec(block['vars'][a], 'external')
    return a


def analyzeargs(block):
    setmesstext(block)
    implicitrules, attrrules = buildimplicitrules(block)
    if 'args' not in block:
        block['args'] = []
    args = []
    for a in block['args']:
        a = expr2name(a, block, args)
        args.append(a)

    block['args'] = args
    if 'entry' in block:
        for k, args1 in block['entry'].items():
            for a in args1:
                if a not in block['vars']:
                    block['vars'][a] = {}

    for b in block['body']:
        if b['name'] in args:
            if 'externals' not in block:
                block['externals'] = []
            if b['name'] not in block['externals']:
                block['externals'].append(b['name'])

    if 'result' in block and block['result'] not in block['vars']:
        block['vars'][block['result']] = {}
    return block


determineexprtype_re_1 = re.compile('\\A\\(.+?[,].+?\\)\\Z', re.I)
determineexprtype_re_2 = re.compile('\\A[+-]?\\d+(_(P<name>[\\w]+)|)\\Z', re.I)
determineexprtype_re_3 = re.compile('\\A[+-]?[\\d.]+[\\d+-de.]*(_(P<name>[\\w]+)|)\\Z', re.I)
determineexprtype_re_4 = re.compile('\\A\\(.*\\)\\Z', re.I)
determineexprtype_re_5 = re.compile('\\A(?P<name>\\w+)\\s*\\(.*?\\)\\s*\\Z', re.I)

def _ensure_exprdict(r):
    if type(r) is type(0):
        return {'typespec': 'integer'}
    if type(r) is type(0.0):
        return {'typespec': 'real'}
    if type(r) is type(complex(0.0, 0.0)):
        return {'typespec': 'complex'}
    assert type(r) is type({}), `r`
    return r


def determineexprtype(expr, vars, rules={}):
    if expr in vars:
        return _ensure_exprdict(vars[expr])
    expr = expr.strip()
    if determineexprtype_re_1.match(expr):
        return {'typespec': 'complex'}
    m = determineexprtype_re_2.match(expr)
    if m:
        if 'name' in m.groupdict() and m.group('name'):
            outmess('determineexprtype: selected kind types not supported (%s)\n' % `expr`)
        return {'typespec': 'integer'}
    m = determineexprtype_re_3.match(expr)
    if m:
        if 'name' in m.groupdict() and m.group('name'):
            outmess('determineexprtype: selected kind types not supported (%s)\n' % `expr`)
        return {'typespec': 'real'}
    for op in ['+', '-', '*', '/']:
        for e in [ x.strip() for x in markoutercomma(expr, comma=op).split('@' + op + '@') ]:
            if e in vars:
                return _ensure_exprdict(vars[e])

    t = {}
    if determineexprtype_re_4.match(expr):
        t = determineexprtype(expr[1:-1], vars, rules)
    else:
        m = determineexprtype_re_5.match(expr)
        if m:
            rn = m.group('name')
            t = determineexprtype(m.group('name'), vars, rules)
            if t and 'attrspec' in t:
                del t['attrspec']
            if not t:
                if rn[0] in rules:
                    return _ensure_exprdict(rules[rn[0]])
        if expr[0] in '\'"':
            return {'typespec': 'character', 'charselector': {'*': '*'}}
    if not t:
        outmess('determineexprtype: could not determine expressions (%s) type.\n' % `expr`)
    return t


def crack2fortrangen(block, tab='\n', as_interface=False):
    setmesstext(block)
    ret = ''
    if isinstance(block, list):
        for g in block:
            if g and g['block'] in ('function', 'subroutine'):
                if g['name'] in skipfuncs:
                    continue
                if onlyfuncs and g['name'] not in onlyfuncs:
                    continue
            ret = ret + crack2fortrangen(g, tab, as_interface=as_interface)

        return ret
    prefix = ''
    name = ''
    args = ''
    blocktype = block['block']
    if blocktype == 'program':
        return ''
    argsl = []
    if 'name' in block:
        name = block['name']
    if 'args' in block:
        vars = block['vars']
        for a in block['args']:
            a = expr2name(a, block, argsl)
            if not isintent_callback(vars[a]):
                argsl.append(a)

        if block['block'] == 'function' or argsl:
            args = '(%s)' % (',').join(argsl)
    f2pyenhancements = ''
    if 'f2pyenhancements' in block:
        for k in block['f2pyenhancements'].keys():
            f2pyenhancements = '%s%s%s %s' % (f2pyenhancements, tab + tabchar, k, block['f2pyenhancements'][k])

    intent_lst = block.get('intent', [])[:]
    if blocktype == 'function' and 'callback' in intent_lst:
        intent_lst.remove('callback')
    if intent_lst:
        f2pyenhancements = '%s%sintent(%s) %s' % (
         f2pyenhancements, tab + tabchar,
         (',').join(intent_lst), name)
    use = ''
    if 'use' in block:
        use = use2fortran(block['use'], tab + tabchar)
    common = ''
    if 'common' in block:
        common = common2fortran(block['common'], tab + tabchar)
    if name == 'unknown_interface':
        name = ''
    result = ''
    if 'result' in block:
        result = ' result (%s)' % block['result']
        if block['result'] not in argsl:
            argsl.append(block['result'])
    body = crack2fortrangen(block['body'], tab + tabchar)
    vars = vars2fortran(block, block['vars'], argsl, tab + tabchar, as_interface=as_interface)
    mess = ''
    if 'from' in block and not as_interface:
        mess = '! in %s' % block['from']
    if 'entry' in block:
        entry_stmts = ''
        for k, i in block['entry'].items():
            entry_stmts = '%s%sentry %s(%s)' % (
             entry_stmts, tab + tabchar, k, (',').join(i))

        body = body + entry_stmts
    if blocktype == 'block data' and name == '_BLOCK_DATA_':
        name = ''
    ret = '%s%s%s %s%s%s %s%s%s%s%s%s%send %s %s' % (tab, prefix, blocktype, name, args, result, mess, f2pyenhancements, use, vars, common, body, tab, blocktype, name)
    return ret


def common2fortran(common, tab=''):
    ret = ''
    for k in common.keys():
        if k == '_BLNK_':
            ret = '%s%scommon %s' % (ret, tab, (',').join(common[k]))
        else:
            ret = '%s%scommon /%s/ %s' % (ret, tab, k, (',').join(common[k]))

    return ret


def use2fortran(use, tab=''):
    ret = ''
    for m in use.keys():
        ret = '%s%suse %s,' % (ret, tab, m)
        if use[m] == {}:
            if ret and ret[-1] == ',':
                ret = ret[:-1]
            continue
        if 'only' in use[m] and use[m]['only']:
            ret = '%s only:' % ret
        if 'map' in use[m] and use[m]['map']:
            c = ' '
            for k in use[m]['map'].keys():
                if k == use[m]['map'][k]:
                    ret = '%s%s%s' % (ret, c, k)
                    c = ','
                else:
                    ret = '%s%s%s=>%s' % (ret, c, k, use[m]['map'][k])
                    c = ','

        if ret and ret[-1] == ',':
            ret = ret[:-1]

    return ret


def true_intent_list(var):
    lst = var['intent']
    ret = []
    for intent in lst:
        try:
            exec 'c = isintent_%s(var)' % intent
        except NameError:
            c = 0

        if c:
            ret.append(intent)

    return ret


def vars2fortran(block, vars, args, tab='', as_interface=False):
    """
    TODO:
    public sub
    ...
    """
    setmesstext(block)
    ret = ''
    nout = []
    for a in args:
        if a in block['vars']:
            nout.append(a)

    if 'commonvars' in block:
        for a in block['commonvars']:
            if a in vars:
                if a not in nout:
                    nout.append(a)
            else:
                errmess('vars2fortran: Confused?!: "%s" is not defined in vars.\n' % a)

    if 'varnames' in block:
        nout.extend(block['varnames'])
    if not as_interface:
        for a in vars.keys():
            if a not in nout:
                nout.append(a)

    for a in nout:
        if 'depend' in vars[a]:
            for d in vars[a]['depend']:
                if d in vars and 'depend' in vars[d] and a in vars[d]['depend']:
                    errmess('vars2fortran: Warning: cross-dependence between variables "%s" and "%s"\n' % (a, d))

        if 'externals' in block and a in block['externals']:
            if isintent_callback(vars[a]):
                ret = '%s%sintent(callback) %s' % (ret, tab, a)
            ret = '%s%sexternal %s' % (ret, tab, a)
            if isoptional(vars[a]):
                ret = '%s%soptional %s' % (ret, tab, a)
            if a in vars and 'typespec' not in vars[a]:
                continue
            cont = 1
            for b in block['body']:
                if a == b['name'] and b['block'] == 'function':
                    cont = 0
                    break

            if cont:
                continue
        if a not in vars:
            show(vars)
            outmess('vars2fortran: No definition for argument "%s".\n' % a)
            continue
        if a == block['name'] and not block['block'] == 'function':
            continue
        if 'typespec' not in vars[a]:
            if 'attrspec' in vars[a] and 'external' in vars[a]['attrspec']:
                if a in args:
                    ret = '%s%sexternal %s' % (ret, tab, a)
                continue
            show(vars[a])
            outmess('vars2fortran: No typespec for argument "%s".\n' % a)
            continue
        vardef = vars[a]['typespec']
        if vardef == 'type' and 'typename' in vars[a]:
            vardef = '%s(%s)' % (vardef, vars[a]['typename'])
        selector = {}
        if 'kindselector' in vars[a]:
            selector = vars[a]['kindselector']
        elif 'charselector' in vars[a]:
            selector = vars[a]['charselector']
        if '*' in selector:
            if selector['*'] in ('*', ':'):
                vardef = '%s*(%s)' % (vardef, selector['*'])
            else:
                vardef = '%s*%s' % (vardef, selector['*'])
        elif 'len' in selector:
            vardef = '%s(len=%s' % (vardef, selector['len'])
            if 'kind' in selector:
                vardef = '%s,kind=%s)' % (vardef, selector['kind'])
            else:
                vardef = '%s)' % vardef
        elif 'kind' in selector:
            vardef = '%s(kind=%s)' % (vardef, selector['kind'])
        c = ' '
        if 'attrspec' in vars[a]:
            attr = []
            for l in vars[a]['attrspec']:
                if l not in ('external', ):
                    attr.append(l)

            if attr:
                vardef = '%s, %s' % (vardef, (',').join(attr))
                c = ','
        if 'dimension' in vars[a]:
            vardef = '%s%sdimension(%s)' % (vardef, c, (',').join(vars[a]['dimension']))
            c = ','
        if 'intent' in vars[a]:
            lst = true_intent_list(vars[a])
            if lst:
                vardef = '%s%sintent(%s)' % (vardef, c, (',').join(lst))
            c = ','
        if 'check' in vars[a]:
            vardef = '%s%scheck(%s)' % (vardef, c, (',').join(vars[a]['check']))
            c = ','
        if 'depend' in vars[a]:
            vardef = '%s%sdepend(%s)' % (vardef, c, (',').join(vars[a]['depend']))
            c = ','
        if '=' in vars[a]:
            v = vars[a]['=']
            if vars[a]['typespec'] in ('complex', 'double complex'):
                try:
                    v = eval(v)
                    v = '(%s,%s)' % (v.real, v.imag)
                except:
                    pass

            vardef = '%s :: %s=%s' % (vardef, a, v)
        else:
            vardef = '%s :: %s' % (vardef, a)
        ret = '%s%s%s' % (ret, tab, vardef)

    return ret


def crackfortran(files):
    global usermodules
    outmess('Reading fortran codes...\n', 0)
    readfortrancode(files, crackline)
    outmess('Post-processing...\n', 0)
    usermodules = []
    postlist = postcrack(grouplist[0])
    outmess('Post-processing (stage 2)...\n', 0)
    postlist = postcrack2(postlist)
    return usermodules + postlist


def crack2fortran(block):
    global f2py_version
    pyf = crack2fortrangen(block) + '\n'
    header = '!    -*- f90 -*-\n! Note: the context of this file is case sensitive.\n'
    footer = '\n! This file was auto-generated with f2py (version:%s).\n! See http://cens.ioc.ee/projects/f2py2e/\n' % f2py_version
    return header + pyf + footer


if __name__ == '__main__':
    files = []
    funcs = []
    f = 1
    f2 = 0
    f3 = 0
    showblocklist = 0
    for l in sys.argv[1:]:
        if l == '':
            pass
        elif l[0] == ':':
            f = 0
        elif l == '-quiet':
            quiet = 1
            verbose = 0
        elif l == '-verbose':
            verbose = 2
            quiet = 0
        elif l == '-fix':
            if strictf77:
                outmess('Use option -f90 before -fix if Fortran 90 code is in fix form.\n', 0)
            skipemptyends = 1
            sourcecodeform = 'fix'
        elif l == '-skipemptyends':
            skipemptyends = 1
        elif l == '--ignore-contains':
            ignorecontains = 1
        elif l == '-f77':
            strictf77 = 1
            sourcecodeform = 'fix'
        elif l == '-f90':
            strictf77 = 0
            sourcecodeform = 'free'
            skipemptyends = 1
        elif l == '-h':
            f2 = 1
        elif l == '-show':
            showblocklist = 1
        elif l == '-m':
            f3 = 1
        elif l[0] == '-':
            errmess('Unknown option %s\n' % `l`)
        elif f2:
            f2 = 0
            pyffilename = l
        elif f3:
            f3 = 0
            f77modulename = l
        elif f:
            try:
                open(l).close()
                files.append(l)
            except IOError as detail:
                errmess('IOError: %s\n' % str(detail))

        else:
            funcs.append(l)

    if not strictf77 and f77modulename and not skipemptyends:
        outmess('  Warning: You have specifyied module name for non Fortran 77 code\n  that should not need one (expect if you are scanning F90 code\n  for non module blocks but then you should use flag -skipemptyends\n  and also be sure that the files do not contain programs without program statement).\n', 0)
    postlist = crackfortran(files, funcs)
    if pyffilename:
        outmess('Writing fortran code to file %s\n' % `pyffilename`, 0)
        pyf = crack2fortran(postlist)
        f = open(pyffilename, 'w')
        f.write(pyf)
        f.close()
    if showblocklist:
        show(postlist)