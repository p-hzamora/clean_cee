# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\lib\rparsexml.pyc
# Compiled at: 2013-03-27 15:37:42
"""Very simple and fast XML parser, used for intra-paragraph text.

Devised by Aaron Watters in the bad old days before Python had fast
parsers available.  Constructs the lightest possible in-memory
representation; parses most files we have seen in pure python very
quickly.

The output structure is the same as the one produced by pyRXP,
our validating C-based parser, which was written later.  It will
use pyRXP if available.

This is used to parse intra-paragraph markup.

Example parse::

    <this type="xml">text <b>in</b> xml</this>

    ( "this",
      {"type": "xml"},
      [ "text ",
        ("b", None, ["in"], None),
        " xml"
        ]
       None )

    { 0: "this"
      "type": "xml"
      1: ["text ",
          {0: "b", 1:["in"]},
          " xml"]
    }

Ie, xml tag translates to a tuple:
 (name, dictofattributes, contentlist, miscellaneousinfo)

where miscellaneousinfo can be anything, (but defaults to None)
(with the intention of adding, eg, line number information)

special cases: name of "" means "top level, no containing tag".
Top level parse always looks like this::

    ("", list, None, None)

 contained text of None means <simple_tag/>

In order to support stuff like::

    <this></this><one></one>

AT THE MOMENT &amp; ETCETERA ARE IGNORED. THEY MUST BE PROCESSED
IN A POST-PROCESSING STEP.

PROLOGUES ARE NOT UNDERSTOOD.  OTHER STUFF IS PROBABLY MISSING.
"""
RequirePyRXP = 0
import string
try:
    simpleparse = 0
    import pyRXPU

    def warnCB(s):
        print s


    pyRXP_parser = pyRXPU.Parser(ErrorOnValidityErrors=1, NoNoDTDWarning=1, ExpandCharacterEntities=1, ExpandGeneralEntities=1, warnCB=warnCB, srcName='string input', ReturnUTF8=1)

    def parsexml(xmlText, oneOutermostTag=0, eoCB=None, entityReplacer=None, parseOpts={}):
        pyRXP_parser.eoCB = eoCB
        p = pyRXP_parser.parse(xmlText, **parseOpts)
        return oneOutermostTag and p or ('', None, [p], None)


except ImportError:
    simpleparse = 1

NONAME = ''
NAMEKEY = 0
CONTENTSKEY = 1
CDATAMARKER = '<![CDATA['
LENCDATAMARKER = len(CDATAMARKER)
CDATAENDMARKER = ']]>'
replacelist = [('&lt;', '<'), ('&gt;', '>'), ('&amp;', '&')]

def unEscapeContentList(contentList):
    result = []
    from string import replace
    for e in contentList:
        if '&' in e:
            for old, new in replacelist:
                e = replace(e, old, new)

        result.append(e)

    return result


def parsexmlSimple(xmltext, oneOutermostTag=0, eoCB=None, entityReplacer=unEscapeContentList):
    """official interface: discard unused cursor info"""
    if RequirePyRXP:
        raise ImportError, 'pyRXP not found, fallback parser disabled'
    result, cursor = parsexml0(xmltext, entityReplacer=entityReplacer)
    if oneOutermostTag:
        return result[2][0]
    else:
        return result


if simpleparse:
    parsexml = parsexmlSimple

def parseFile(filename):
    raw = open(filename, 'r').read()
    return parsexml(raw)


verbose = 0

def skip_prologue(text, cursor):
    """skip any prologue found after cursor, return index of rest of text"""
    from string import find
    prologue_elements = ('!DOCTYPE', '?xml', '!--')
    done = None
    while done is None:
        openbracket = find(text, '<', cursor)
        if openbracket < 0:
            break
        past = openbracket + 1
        found = None
        for e in prologue_elements:
            le = len(e)
            if text[past:past + le] == e:
                found = 1
                cursor = find(text, '>', past)
                if cursor < 0:
                    raise ValueError, "can't close prologue %r" % e
                cursor = cursor + 1

        if found is None:
            done = 1

    return cursor


def parsexml0(xmltext, startingat=0, toplevel=1, strip=string.strip, split=string.split, find=string.find, entityReplacer=unEscapeContentList):
    """simple recursive descent xml parser...
       return (dictionary, endcharacter)
       special case: comment returns (None, endcharacter)"""
    NameString = NONAME
    ContentList = AttDict = ExtraStuff = None
    if toplevel is not None:
        xmltext = strip(xmltext)
    cursor = startingat
    firstbracket = find(xmltext, '<', cursor)
    afterbracket2char = xmltext[firstbracket + 1:firstbracket + 3]
    docontents = 1
    if firstbracket < 0:
        if toplevel is not None:
            ContentList = [xmltext[cursor:]]
            if entityReplacer:
                ContentList = entityReplacer(ContentList)
            return (
             (
              NameString, AttDict, ContentList, ExtraStuff), len(xmltext))
        raise ValueError, 'no tags at non-toplevel %s' % repr(xmltext[cursor:cursor + 20])
    L = []
    if toplevel is not None:
        NameString = name = NONAME
        cursor = skip_prologue(xmltext, cursor)
    else:
        if firstbracket < 0:
            raise ValueError, 'non top level entry should be at start tag: %s' % repr(xmltext[:10])
        else:
            if afterbracket2char == '![' and xmltext[firstbracket:firstbracket + 9] == '<![CDATA[':
                startcdata = firstbracket + 9
                endcdata = find(xmltext, CDATAENDMARKER, startcdata)
                if endcdata < 0:
                    raise ValueError, 'unclosed CDATA %s' % repr(xmltext[cursor:cursor + 20])
                NameString = CDATAMARKER
                ContentList = [xmltext[startcdata:endcdata]]
                cursor = endcdata + len(CDATAENDMARKER)
                docontents = None
            else:
                if afterbracket2char == '!-' and xmltext[firstbracket:firstbracket + 4] == '<!--':
                    endcommentdashes = find(xmltext, '--', firstbracket + 4)
                    if endcommentdashes < firstbracket:
                        raise ValueError, 'unterminated comment %s' % repr(xmltext[cursor:cursor + 20])
                    endcomment = endcommentdashes + 2
                    if xmltext[endcomment] != '>':
                        raise ValueError, 'invalid comment: contains double dashes %s' % repr(xmltext[cursor:cursor + 20])
                    return (None, endcomment + 1)
                closebracket = find(xmltext, '>', firstbracket)
                noclose = closebracket < 0
                startsearch = closebracket + 1
                pastfirstbracket = firstbracket + 1
                tagcontent = xmltext[pastfirstbracket:closebracket]
                if '=' not in tagcontent:
                    if tagcontent[-1] == '/':
                        tagcontent = tagcontent[:-1]
                        docontents = None
                    name = strip(tagcontent)
                    NameString = name
                    cursor = startsearch
                else:
                    if '"' in tagcontent:
                        stop = None
                        if noclose or len(split(tagcontent + '.', '"')) % 2:
                            stop = 1
                        while stop is None:
                            closebracket = find(xmltext, '>', startsearch)
                            startsearch = closebracket + 1
                            noclose = closebracket < 0
                            tagcontent = xmltext[pastfirstbracket:closebracket]
                            if noclose or len(split(tagcontent + '.', '"')) % 2:
                                stop = 1

                    if noclose:
                        raise ValueError, 'unclosed start tag %s' % repr(xmltext[firstbracket:firstbracket + 20])
                    cursor = startsearch
                    if xmltext[closebracket - 1] == '/':
                        closebracket = closebracket - 1
                        tagcontent = tagcontent[:-1]
                        docontents = None
                    tagcontent = strip(tagcontent)
                    taglist = split(tagcontent, '=')
                    taglist0 = taglist[0]
                    taglist0list = split(taglist0)
                    name = taglist0list[0]
                    NameString = name
                    attributename = taglist0list[-1]
                    taglist[-1] = taglist[-1] + ' f'
                    AttDict = D = {}
                    taglistindex = 1
                    lasttaglistindex = len(taglist)
                    while taglistindex < lasttaglistindex:
                        attentry = taglist[taglistindex]
                        taglistindex = taglistindex + 1
                        attentry = strip(attentry)
                        if attentry[0] != '"':
                            raise ValueError, 'attribute value must start with double quotes' + repr(attentry)
                        while '"' not in attentry[1:]:
                            if taglistindex > lasttaglistindex:
                                raise ValueError, 'unclosed value ' + repr(attentry)
                            nextattentry = taglist[taglistindex]
                            taglistindex = taglistindex + 1
                            attentry = '%s=%s' % (attentry, nextattentry)

                        attentry = strip(attentry)
                        attlist = split(attentry)
                        nextattname = attlist[-1]
                        attvalue = attentry[:-len(nextattname)]
                        attvalue = strip(attvalue)
                        try:
                            first = attvalue[0]
                            last = attvalue[-1]
                        except:
                            raise ValueError, 'attvalue,attentry,attlist=' + repr((attvalue, attentry, attlist))

                        if first == last == '"' or first == last == "'":
                            attvalue = attvalue[1:-1]
                        D[attributename] = attvalue
                        attributename = nextattname

        if docontents is not None:
            ContentList = L
        while docontents is not None:
            nextopenbracket = find(xmltext, '<', cursor)
            if nextopenbracket < cursor:
                if name == NONAME:
                    docontents = None
                    remainder = xmltext[cursor:]
                    cursor = len(xmltext)
                    if remainder:
                        L.append(remainder)
                else:
                    raise ValueError, 'no close bracket for %s found after %s' % (name, repr(xmltext[cursor:cursor + 20]))
            elif xmltext[nextopenbracket + 1] == '/':
                nextclosebracket = find(xmltext, '>', nextopenbracket)
                if nextclosebracket < nextopenbracket:
                    raise ValueError, 'unclosed close tag %s' % repr(xmltext[nextopenbracket:nextopenbracket + 20])
                closetagcontents = xmltext[nextopenbracket + 2:nextclosebracket]
                closetaglist = split(closetagcontents)
                closename = closetaglist[0]
                if name != closename:
                    prefix = xmltext[:cursor]
                    endlinenum = len(split(prefix, '\n'))
                    prefix = xmltext[:startingat]
                    linenum = len(split(prefix, '\n'))
                    raise ValueError, "at lines %s...%s close tag name doesn't match %s...%s %s" % (
                     linenum, endlinenum, repr(name), repr(closename), repr(xmltext[cursor:cursor + 100]))
                remainder = xmltext[cursor:nextopenbracket]
                if remainder:
                    L.append(remainder)
                cursor = nextclosebracket + 1
                docontents = None
            else:
                remainder = xmltext[cursor:nextopenbracket]
                if remainder:
                    L.append(remainder)
                parsetree, cursor = parsexml0(xmltext, startingat=nextopenbracket, toplevel=None, entityReplacer=entityReplacer)
                if parsetree:
                    L.append(parsetree)

    if ContentList:
        if entityReplacer:
            ContentList = entityReplacer(ContentList)
    t = (
     NameString, AttDict, ContentList, ExtraStuff)
    return (t, cursor)


import types

def pprettyprint(parsedxml):
    """pretty printer mainly for testing"""
    st = types.StringType
    if type(parsedxml) is st:
        return parsedxml
    else:
        name, attdict, textlist, extra = parsedxml
        if not attdict:
            attdict = {}
        join = string.join
        attlist = []
        for k in attdict.keys():
            v = attdict[k]
            attlist.append('%s=%s' % (k, repr(v)))

        attributes = join(attlist, ' ')
        if not name and attributes:
            raise ValueError, 'name missing with attributes???'
        if textlist is not None:
            textlistpprint = map(pprettyprint, textlist)
            textpprint = join(textlistpprint, '\n')
            if not name:
                return textpprint
            nllist = string.split(textpprint, '\n')
            textpprint = '   ' + join(nllist, '\n   ')
            return '<%s %s>\n%s\n</%s>' % (name, attributes, textpprint, name)
        return '<%s %s/>' % (name, attributes)


dump = 0

def testparse(s):
    from time import time
    from pprint import pprint
    now = time()
    D = parsexmlSimple(s)
    print 'DONE', time() - now
    if dump & 4:
        pprint(D)
    if dump & 1:
        print '============== reformatting'
        p = pprettyprint(D)
        print p


def test():
    testparse('<this type="xml">text &lt;&gt;<b>in</b> <funnytag foo="bar"/> xml</this>\n                 <!-- comment -->\n                 <![CDATA[\n                 <this type="xml">text <b>in</b> xml</this> ]]>\n                 <tag with="<brackets in values>">just testing brackets feature</tag>\n                 ')


filenames = [
 'samples/hamlet.xml']
dump = 1
if __name__ == '__main__':
    test()
    from time import time
    now = time()
    for f in filenames:
        t = open(f).read()
        print 'parsing', f
        testparse(t)

    print 'elapsed', time() - now