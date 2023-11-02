# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\lib\xmllib.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = 'From before xmllib was in the Python standard library.\n\nProbably ought to be removed'
import re, string
try:
    import sgmlop
except ImportError:
    sgmlop = None

ENTITYDEFS = {'lt': '<', 
   'gt': '>', 
   'amp': '&', 
   'quot': '"', 
   'apos': "'"}
_S = '[ \t\r\n]+'
_opS = '[ \t\r\n]*'
_Name = '[a-zA-Z_:][-a-zA-Z0-9._:]*'
interesting = re.compile('[&<]')
incomplete = re.compile('&(' + _Name + '|#[0-9]*|#x[0-9a-fA-F]*)?|<([a-zA-Z_:][^<>]*|/([a-zA-Z_:][^<>]*)?|![^<>]*|\\?[^<>]*)?')
ref = re.compile('&(' + _Name + '|#[0-9]+|#x[0-9a-fA-F]+);?')
entityref = re.compile('&(?P<name>' + _Name + ')[^-a-zA-Z0-9._:]')
charref = re.compile('&#(?P<char>[0-9]+[^0-9]|x[0-9a-fA-F]+[^0-9a-fA-F])')
space = re.compile(_S)
newline = re.compile('\n')
starttagopen = re.compile('<' + _Name)
endtagopen = re.compile('</')
starttagend = re.compile(_opS + '(?P<slash>/?)>')
endbracket = re.compile('>')
tagfind = re.compile(_Name)
cdataopen = re.compile('<!\\[CDATA\\[')
cdataclose = re.compile('\\]\\]>')
special = re.compile('<!(?P<special>[^<>]*)>')
procopen = re.compile('<\\?(?P<proc>' + _Name + ')' + _S)
procclose = re.compile('\\?>')
commentopen = re.compile('<!--')
commentclose = re.compile('-->')
doubledash = re.compile('--')
attrfind = re.compile(_opS + '(?P<name>' + _Name + ')(' + _opS + '=' + _opS + '(?P<value>\'[^\']*\'|"[^"]*"|[-a-zA-Z0-9.:+*%?!()_#=~]+))')

class SlowXMLParser():

    def __init__(self, verbose=0):
        self.verbose = verbose
        self.reset()

    def reset(self):
        self.rawdata = ''
        self.stack = []
        self.lasttag = '???'
        self.nomoretags = 0
        self.literal = 0
        self.lineno = 1

    def setnomoretags(self):
        self.nomoretags = self.literal = 1

    def setliteral(self, *args):
        self.literal = 1

    def feed(self, data):
        self.rawdata = self.rawdata + data
        self.goahead(0)

    def close(self):
        self.goahead(1)

    def translate_references(self, data):
        newdata = []
        i = 0
        while 1:
            res = ref.search(data, i)
            if res is None:
                newdata.append(data[i:])
                return string.join(newdata, '')
            if data[res.end(0) - 1] != ';':
                self.syntax_error(self.lineno, '; missing after entity/char reference')
            newdata.append(data[i:res.start(0)])
            str = res.group(1)
            if str[0] == '#':
                if str[1] == 'x':
                    newdata.append(chr(string.atoi(str[2:], 16)))
                else:
                    newdata.append(chr(string.atoi(str[1:])))
            else:
                try:
                    newdata.append(self.entitydefs[str])
                except KeyError:
                    newdata.append('&' + str + ';')

            i = res.end(0)

        return

    def goahead(self, end):
        rawdata = self.rawdata
        i = 0
        n = len(rawdata)
        while i < n:
            if self.nomoretags:
                data = rawdata[i:n]
                self.handle_data(data)
                self.lineno = self.lineno + string.count(data, '\n')
                i = n
                break
            res = interesting.search(rawdata, i)
            if res:
                j = res.start(0)
            else:
                j = n
            if i < j:
                data = rawdata[i:j]
                self.handle_data(data)
                self.lineno = self.lineno + string.count(data, '\n')
            i = j
            if i == n:
                break
            if rawdata[i] == '<':
                if starttagopen.match(rawdata, i):
                    if self.literal:
                        data = rawdata[i]
                        self.handle_data(data)
                        self.lineno = self.lineno + string.count(data, '\n')
                        i = i + 1
                        continue
                    k = self.parse_starttag(i)
                    if k < 0:
                        break
                    self.lineno = self.lineno + string.count(rawdata[i:k], '\n')
                    i = k
                    continue
                if endtagopen.match(rawdata, i):
                    k = self.parse_endtag(i)
                    if k < 0:
                        break
                    self.lineno = self.lineno + string.count(rawdata[i:k], '\n')
                    i = k
                    self.literal = 0
                    continue
                if commentopen.match(rawdata, i):
                    if self.literal:
                        data = rawdata[i]
                        self.handle_data(data)
                        self.lineno = self.lineno + string.count(data, '\n')
                        i = i + 1
                        continue
                    k = self.parse_comment(i)
                    if k < 0:
                        break
                    self.lineno = self.lineno + string.count(rawdata[i:k], '\n')
                    i = k
                    continue
                if cdataopen.match(rawdata, i):
                    k = self.parse_cdata(i)
                    if k < 0:
                        break
                    self.lineno = self.lineno + string.count(rawdata[i:i], '\n')
                    i = k
                    continue
                res = procopen.match(rawdata, i)
                if res:
                    k = self.parse_proc(i, res)
                    if k < 0:
                        break
                    self.lineno = self.lineno + string.count(rawdata[i:k], '\n')
                    i = k
                    continue
                res = special.match(rawdata, i)
                if res:
                    if self.literal:
                        data = rawdata[i]
                        self.handle_data(data)
                        self.lineno = self.lineno + string.count(data, '\n')
                        i = i + 1
                        continue
                    self.handle_special(res.group('special'))
                    self.lineno = self.lineno + string.count(res.group(0), '\n')
                    i = res.end(0)
                    continue
            elif rawdata[i] == '&':
                res = charref.match(rawdata, i)
                if res is not None:
                    i = res.end(0)
                    if rawdata[i - 1] != ';':
                        self.syntax_error(self.lineno, '; missing in charref')
                        i = i - 1
                    self.handle_charref(res.group('char')[:-1])
                    self.lineno = self.lineno + string.count(res.group(0), '\n')
                    continue
                res = entityref.match(rawdata, i)
                if res is not None:
                    i = res.end(0)
                    if rawdata[i - 1] != ';':
                        self.syntax_error(self.lineno, '; missing in entityref')
                        i = i - 1
                    self.handle_entityref(res.group('name'))
                    self.lineno = self.lineno + string.count(res.group(0), '\n')
                    continue
            else:
                raise RuntimeError, 'neither < nor & ??'
            res = incomplete.match(rawdata, i)
            if not res:
                data = rawdata[i]
                self.handle_data(data)
                self.lineno = self.lineno + string.count(data, '\n')
                i = i + 1
                continue
            j = res.end(0)
            if j == n:
                break
            self.syntax_error(self.lineno, 'bogus < or &')
            data = res.group(0)
            self.handle_data(data)
            self.lineno = self.lineno + string.count(data, '\n')
            i = j

        if end and i < n:
            data = rawdata[i:n]
            self.handle_data(data)
            self.lineno = self.lineno + string.count(data, '\n')
            i = n
        self.rawdata = rawdata[i:]
        return

    def parse_comment(self, i):
        rawdata = self.rawdata
        if rawdata[i:i + 4] != '<!--':
            raise RuntimeError, 'unexpected call to handle_comment'
        res = commentclose.search(rawdata, i + 4)
        if not res:
            return -1
        if doubledash.search(rawdata, i + 4).start(0) < res.start(0):
            self.syntax_error(self.lineno, "'--' inside comment")
        self.handle_comment(rawdata[i + 4:res.start(0)])
        return res.end(0)

    def parse_cdata(self, i):
        rawdata = self.rawdata
        if rawdata[i:i + 9] != '<![CDATA[':
            raise RuntimeError, 'unexpected call to handle_cdata'
        res = cdataclose.search(rawdata, i + 9)
        if not res:
            return -1
        self.handle_cdata(rawdata[i + 9:res.start(0)])
        return res.end(0)

    def parse_proc(self, i, res):
        rawdata = self.rawdata
        if not res:
            raise RuntimeError, 'unexpected call to parse_proc'
        name = res.group('proc')
        res = procclose.search(rawdata, res.end(0))
        if not res:
            return -1
        self.handle_proc(name, rawdata[res.pos:res.start(0)])
        return res.end(0)

    def parse_starttag(self, i):
        rawdata = self.rawdata
        end = endbracket.search(rawdata, i + 1)
        if not end:
            return -1
        else:
            j = end.start(0)
            attrdict = {}
            res = tagfind.match(rawdata, i + 1)
            if not res:
                raise RuntimeError, 'unexpected call to parse_starttag'
            k = res.end(0)
            tag = res.group(0)
            if hasattr(self, tag + '_attributes'):
                attrlist = getattr(self, tag + '_attributes')
            else:
                attrlist = None
            self.lasttag = tag
            while k < j:
                res = attrfind.match(rawdata, k)
                if not res:
                    break
                attrname, attrvalue = res.group('name', 'value')
                if attrvalue is None:
                    self.syntax_error(self.lineno, 'no attribute value specified')
                    attrvalue = attrname
                elif attrvalue[:1] == "'" == attrvalue[-1:] or attrvalue[:1] == '"' == attrvalue[-1:]:
                    attrvalue = attrvalue[1:-1]
                else:
                    self.syntax_error(self.lineno, 'attribute value not quoted')
                if attrlist is not None and attrname not in attrlist:
                    self.syntax_error(self.lineno, 'unknown attribute %s of element %s' % (
                     attrname, tag))
                if attrname in attrdict:
                    self.syntax_error(self.lineno, 'attribute specified twice')
                attrdict[attrname] = self.translate_references(attrvalue)
                k = res.end(0)

            res = starttagend.match(rawdata, k)
            if not res:
                self.syntax_error(self.lineno, 'garbage in start tag')
            self.finish_starttag(tag, attrdict)
            if res and res.group('slash') == '/':
                self.finish_endtag(tag)
            return end.end(0)

    def parse_endtag(self, i):
        rawdata = self.rawdata
        end = endbracket.search(rawdata, i + 1)
        if not end:
            return -1
        else:
            res = tagfind.match(rawdata, i + 2)
            if not res:
                self.syntax_error(self.lineno, 'no name specified in end tag')
                tag = ''
                k = i + 2
            else:
                tag = res.group(0)
                k = res.end(0)
            if k != end.start(0):
                res = space.match(rawdata, k)
                if res is None or res.end(0) != end.start(0):
                    self.syntax_error(self.lineno, 'garbage in end tag')
            self.finish_endtag(tag)
            return end.end(0)

    def finish_starttag(self, tag, attrs):
        self.stack.append(tag)
        try:
            method = getattr(self, 'start_' + tag)
        except AttributeError:
            self.unknown_starttag(tag, attrs)
            return -1

        self.handle_starttag(tag, method, attrs)
        return 1

    def finish_endtag(self, tag):
        if not tag:
            found = len(self.stack) - 1
            if found < 0:
                self.unknown_endtag(tag)
                return
        else:
            if tag not in self.stack:
                try:
                    method = getattr(self, 'end_' + tag)
                except AttributeError:
                    self.unknown_endtag(tag)

                return
            found = len(self.stack)
            for i in range(found):
                if self.stack[i] == tag:
                    found = i

            while len(self.stack) > found:
                tag = self.stack[-1]
                try:
                    method = getattr(self, 'end_' + tag)
                except AttributeError:
                    method = None

                if method:
                    self.handle_endtag(tag, method)
                else:
                    self.unknown_endtag(tag)
                del self.stack[-1]

        return

    def handle_starttag(self, tag, method, attrs):
        method(attrs)

    def handle_endtag(self, tag, method):
        method()

    def handle_charref(self, name):
        try:
            if name[0] == 'x':
                n = string.atoi(name[1:], 16)
            else:
                n = string.atoi(name)
        except string.atoi_error:
            self.unknown_charref(name)
            return

        if not 0 <= n <= 255:
            self.unknown_charref(name)
            return
        self.handle_data(chr(n))

    entitydefs = ENTITYDEFS

    def handle_entityref(self, name):
        table = self.entitydefs
        if name in table:
            self.handle_data(table[name])
        else:
            self.unknown_entityref(name)
            return

    def handle_data(self, data):
        pass

    def handle_cdata(self, data):
        pass

    def handle_comment(self, data):
        pass

    def handle_proc(self, name, data):
        pass

    def handle_special(self, data):
        pass

    def syntax_error(self, lineno, message):
        raise RuntimeError, 'Syntax error at line %d: %s' % (lineno, message)

    def unknown_starttag(self, tag, attrs):
        pass

    def unknown_endtag(self, tag):
        pass

    def unknown_charref(self, ref):
        pass

    def unknown_entityref(self, ref):
        pass


class FastXMLParser():

    def __init__(self, verbose=0):
        self.verbose = verbose
        self.reset()

    def reset(self):
        self.rawdata = ''
        self.stack = []
        self.lasttag = '???'
        self.nomoretags = 0
        self.literal = 0
        self.lineno = 1
        self.parser = sgmlop.XMLParser()
        self.feed = self.parser.feed
        self.parser.register(self)

    def setnomoretags(self):
        self.nomoretags = self.literal = 1

    def setliteral(self, *args):
        self.literal = 1

    def feed(self, data):
        self.parser.feed(data)

    def close(self):
        try:
            self.parser.close()
        finally:
            self.parser = None

        return

    def translate_references(self, data):
        newdata = []
        i = 0
        while 1:
            res = ref.search(data, i)
            if res is None:
                newdata.append(data[i:])
                return string.join(newdata, '')
            if data[res.end(0) - 1] != ';':
                self.syntax_error(self.lineno, '; missing after entity/char reference')
            newdata.append(data[i:res.start(0)])
            str = res.group(1)
            if str[0] == '#':
                if str[1] == 'x':
                    newdata.append(chr(string.atoi(str[2:], 16)))
                else:
                    newdata.append(chr(string.atoi(str[1:])))
            else:
                try:
                    newdata.append(self.entitydefs[str])
                except KeyError:
                    newdata.append('&' + str + ';')

            i = res.end(0)

        return

    def finish_starttag(self, tag, attrs):
        self.stack.append(tag)
        try:
            method = getattr(self, 'start_' + tag)
        except AttributeError:
            self.unknown_starttag(tag, attrs)
            return -1

        self.handle_starttag(tag, method, attrs)
        return 1

    def finish_endtag(self, tag):
        if not tag:
            found = len(self.stack) - 1
            if found < 0:
                self.unknown_endtag(tag)
                return
        else:
            if tag not in self.stack:
                try:
                    method = getattr(self, 'end_' + tag)
                except AttributeError:
                    self.unknown_endtag(tag)

                return
            found = len(self.stack)
            for i in range(found):
                if self.stack[i] == tag:
                    found = i

            while len(self.stack) > found:
                tag = self.stack[-1]
                try:
                    method = getattr(self, 'end_' + tag)
                except AttributeError:
                    method = None

                if method:
                    self.handle_endtag(tag, method)
                else:
                    self.unknown_endtag(tag)
                del self.stack[-1]

        return

    def handle_starttag(self, tag, method, attrs):
        method(attrs)

    def handle_endtag(self, tag, method):
        method()

    def handle_charref(self, name):
        try:
            if name[0] == 'x':
                n = string.atoi(name[1:], 16)
            else:
                n = string.atoi(name)
        except string.atoi_error:
            self.unknown_charref(name)
            return

        if not 0 <= n <= 255:
            self.unknown_charref(name)
            return
        self.handle_data(chr(n))

    entitydefs = ENTITYDEFS

    def handle_entityref(self, name):
        table = self.entitydefs
        if name in table:
            self.handle_data(table[name])
        else:
            self.unknown_entityref(name)
            return

    def handle_data(self, data):
        pass

    def handle_cdata(self, data):
        pass

    def handle_comment(self, data):
        pass

    def handle_proc(self, name, data):
        pass

    def handle_special(self, data):
        pass

    def syntax_error(self, lineno, message):
        raise RuntimeError, 'Syntax error at line %d: %s' % (lineno, message)

    def unknown_starttag(self, tag, attrs):
        pass

    def unknown_endtag(self, tag):
        pass

    def unknown_charref(self, ref):
        pass

    def unknown_entityref(self, ref):
        pass


if sgmlop:
    XMLParser = FastXMLParser
else:
    XMLParser = SlowXMLParser

class TestXMLParser(XMLParser):

    def __init__(self, verbose=0):
        self.testdata = ''
        XMLParser.__init__(self, verbose)

    def handle_data(self, data):
        self.testdata = self.testdata + data
        if len(repr(self.testdata)) >= 70:
            self.flush()

    def flush(self):
        data = self.testdata
        if data:
            self.testdata = ''
            print 'data:', repr(data)

    def handle_cdata(self, data):
        self.flush()
        print 'cdata:', repr(data)

    def handle_proc(self, name, data):
        self.flush()
        print 'processing:', name, repr(data)

    def handle_special(self, data):
        self.flush()
        print 'special:', repr(data)

    def handle_comment(self, data):
        self.flush()
        r = repr(data)
        if len(r) > 68:
            r = r[:32] + '...' + r[-32:]
        print 'comment:', r

    def syntax_error(self, lineno, message):
        print 'error at line %d:' % lineno, message

    def unknown_starttag(self, tag, attrs):
        self.flush()
        if not attrs:
            print 'start tag: <' + tag + '>'
        else:
            print 'start tag: <' + tag,
            for name, value in attrs.items():
                print name + '=' + '"' + value + '"',

            print '>'

    def unknown_endtag(self, tag):
        self.flush()
        print 'end tag: </' + tag + '>'

    def unknown_entityref(self, ref):
        self.flush()
        print '*** unknown entity ref: &' + ref + ';'

    def unknown_charref(self, ref):
        self.flush()
        print '*** unknown char ref: &#' + ref + ';'

    def close(self):
        XMLParser.close(self)
        self.flush()


def test(args=None):
    import sys
    if not args:
        args = sys.argv[1:]
    if args and args[0] == '-s':
        args = args[1:]
        klass = XMLParser
    else:
        klass = TestXMLParser
    if args:
        file = args[0]
    else:
        file = 'test.xml'
    if file == '-':
        f = sys.stdin
    else:
        try:
            f = open(file, 'r')
        except IOError as msg:
            print file, ':', msg
            sys.exit(1)

        data = f.read()
        if f is not sys.stdin:
            f.close()
        x = klass()
        for c in data:
            x.feed(c)

    x.close()


if __name__ == '__main__':
    test()