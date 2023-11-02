# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\lib\PyFontify.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = "\nModule to analyze Python source code; for syntax coloring tools.\n\nInterface::\n\n    tags = fontify(pytext, searchfrom, searchto)\n\n - The 'pytext' argument is a string containing Python source code.\n - The (optional) arguments 'searchfrom' and 'searchto' may contain a slice in pytext.\n - The returned value is a list of tuples, formatted like this::\n    [('keyword', 0, 6, None), ('keyword', 11, 17, None), ('comment', 23, 53, None), etc. ]\n\n - The tuple contents are always like this::\n    (tag, startindex, endindex, sublist)\n\n - tag is one of 'keyword', 'string', 'comment' or 'identifier'\n - sublist is not used, hence always None.\n"
__version__ = '0.4'
import re

def replace(src, sep, rep):
    return rep.join(src.split(sep))


keywordsList = [
 'as', 'assert', 'exec', 
 'del', 'from', 'lambda', 'return', 
 'and', 
 'elif', 'global', 'not', 'try', 
 'break', 'else', 'if', 'or', 'while', 
 'class', 
 'except', 'import', 'pass', 
 'continue', 'finally', 'in', 'print', 
 'def', 
 'for', 'is', 'raise', 'yield']
commentPat = '#[^\\n]*'
pat = 'q[^\\\\q\\n]*(\\\\[\\000-\\377][^\\\\q\\n]*)*q'
quotePat = replace(pat, 'q', "'") + '|' + replace(pat, 'q', '"')
pat = '\n    qqq\n    [^\\\\q]*\n    (\n        (   \\\\[\\000-\\377]\n        |   q\n            (   \\\\[\\000-\\377]\n            |   [^\\q]\n            |   q\n                (   \\\\[\\000-\\377]\n                |   [^\\\\q]\n                )\n            )\n        )\n        [^\\\\q]*\n    )*\n    qqq\n'
pat = ('').join(pat.split())
tripleQuotePat = replace(pat, 'q', "'") + '|' + replace(pat, 'q', '"')
nonKeyPat = '(^|[^a-zA-Z0-9_.\\"\'])'
keyPat = nonKeyPat + '(' + ('|').join(keywordsList) + ')' + nonKeyPat
matchPat = commentPat + '|' + keyPat + '|' + tripleQuotePat + '|' + quotePat
matchRE = re.compile(matchPat)
idKeyPat = '[ \t]*[A-Za-z_][A-Za-z_0-9.]*'
idRE = re.compile(idKeyPat)

def fontify(pytext, searchfrom=0, searchto=None):
    if searchto is None:
        searchto = len(pytext)
    search = matchRE.search
    idSearch = idRE.search
    tags = []
    tags_append = tags.append
    commentTag = 'comment'
    stringTag = 'string'
    keywordTag = 'keyword'
    identifierTag = 'identifier'
    start = 0
    end = searchfrom
    while 1:
        m = search(pytext, end)
        if m is None:
            break
        start = m.start()
        if start >= searchto:
            break
        match = m.group(0)
        end = start + len(match)
        c = match[0]
        if c not in '#\'"':
            if start != searchfrom:
                match = match[1:-1]
                start = start + 1
            else:
                match = match[:-1]
            end = end - 1
            tags_append((keywordTag, start, end, None))
            if match in ('def', 'class'):
                m = idSearch(pytext, end)
                if m is not None:
                    start = m.start()
                    if start == end:
                        match = m.group(0)
                        end = start + len(match)
                        tags_append((identifierTag, start, end, None))
        elif c == '#':
            tags_append((commentTag, start, end, None))
        else:
            tags_append((stringTag, start, end, None))

    return tags


def test(path):
    f = open(path)
    text = f.read()
    f.close()
    tags = fontify(text)
    for tag, start, end, sublist in tags:
        print tag, repr(text[start:end])