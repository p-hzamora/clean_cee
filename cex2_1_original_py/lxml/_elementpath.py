# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: c:\Python27\lib\site-packages\lxml-3.2.4-py2.7-win32.egg\lxml\_elementpath.py
# Compiled at: 2013-12-10 10:12:00
import re
xpath_tokenizer_re = re.compile('(\'[^\']*\'|"[^"]*"|::|//?|\\.\\.|\\(\\)|[/.*:\\[\\]\\(\\)@=])|((?:\\{[^}]+\\})?[^/\\[\\]\\(\\)@=\\s]+)|\\s+')

def xpath_tokenizer(pattern, namespaces=None):
    for token in xpath_tokenizer_re.findall(pattern):
        tag = token[1]
        if tag and tag[0] != '{' and ':' in tag:
            try:
                prefix, uri = tag.split(':', 1)
                if not namespaces:
                    raise KeyError
                yield (
                 token[0], '{%s}%s' % (namespaces[prefix], uri))
            except KeyError:
                raise SyntaxError('prefix %r not found in prefix map' % prefix)

        else:
            yield token


def prepare_child(next, token):
    tag = token[1]

    def select(result):
        for elem in result:
            for e in elem.iterchildren(tag):
                yield e

    return select


def prepare_star(next, token):

    def select(result):
        for elem in result:
            for e in elem.iterchildren('*'):
                yield e

    return select


def prepare_self(next, token):

    def select(result):
        return result

    return select


def prepare_descendant(next, token):
    token = next()
    if token[0] == '*':
        tag = '*'
    elif not token[0]:
        tag = token[1]
    else:
        raise SyntaxError('invalid descendant')

    def select(result):
        for elem in result:
            for e in elem.iterdescendants(tag):
                yield e

    return select


def prepare_parent(next, token):

    def select(result):
        for elem in result:
            parent = elem.getparent()
            if parent is not None:
                yield parent

        return

    return select


def prepare_predicate(next, token):
    signature = []
    predicate = []
    while 1:
        token = next()
        if token[0] == ']':
            break
        if token[0] and token[0][:1] in '\'"':
            token = (
             "'", token[0][1:-1])
        signature.append(token[0] or '-')
        predicate.append(token[1])

    signature = ('').join(signature)
    if signature == '@-':
        key = predicate[1]

        def select(result):
            for elem in result:
                if elem.get(key) is not None:
                    yield elem

            return

        return select
    if signature == "@-='":
        key = predicate[1]
        value = predicate[-1]

        def select(result):
            for elem in result:
                if elem.get(key) == value:
                    yield elem

        return select
    if signature == '-' and not re.match('-?\\d+$', predicate[0]):
        tag = predicate[0]

        def select(result):
            for elem in result:
                for _ in elem.iterchildren(tag):
                    yield elem
                    break

        return select
    if signature == "-='" and not re.match('-?\\d+$', predicate[0]):
        tag = predicate[0]
        value = predicate[-1]

        def select(result):
            for elem in result:
                for e in elem.iterchildren(tag):
                    if ('').join(e.itertext()) == value:
                        yield elem
                        break

        return select
    if signature == '-' or signature == '-()' or signature == '-()-':
        if signature == '-':
            index = int(predicate[0]) - 1
            if index < 0:
                if index == -1:
                    raise SyntaxError('indices in path predicates are 1-based, not 0-based')
                else:
                    raise SyntaxError('path index >= 1 expected')
        else:
            if predicate[0] != 'last':
                raise SyntaxError('unsupported function')
            if signature == '-()-':
                try:
                    index = int(predicate[2]) - 1
                except ValueError:
                    raise SyntaxError('unsupported expression')

            else:
                index = -1

        def select(result):
            for elem in result:
                parent = elem.getparent()
                if parent is None:
                    continue
                try:
                    elems = list(parent.iterchildren(elem.tag))
                    if elems[index] is elem:
                        yield elem
                except IndexError:
                    pass

            return

        return select
    raise SyntaxError('invalid predicate')


ops = {'': prepare_child, 
   '*': prepare_star, 
   '.': prepare_self, 
   '..': prepare_parent, 
   '//': prepare_descendant, 
   '[': prepare_predicate}
_cache = {}

def _build_path_iterator(path, namespaces):
    if path[-1:] == '/':
        path = path + '*'
    try:
        return _cache[(path, namespaces and tuple(sorted(namespaces.items())) or None)]
    except KeyError:
        pass

    if len(_cache) > 100:
        _cache.clear()
    if path[:1] == '/':
        raise SyntaxError('cannot use absolute path on element')
    stream = iter(xpath_tokenizer(path, namespaces))
    try:
        _next = stream.next
    except AttributeError:
        _next = stream.__next__

    try:
        token = _next()
    except StopIteration:
        raise SyntaxError('empty path expression')

    selector = []
    while 1:
        try:
            selector.append(ops[token[0]](_next, token))
        except StopIteration:
            raise SyntaxError('invalid path')

        try:
            token = _next()
            if token[0] == '/':
                token = _next()
        except StopIteration:
            break

    _cache[path] = selector
    return selector


def iterfind(elem, path, namespaces=None):
    selector = _build_path_iterator(path, namespaces)
    result = iter((elem,))
    for select in selector:
        result = select(result)

    return result


def find(elem, path, namespaces=None):
    it = iterfind(elem, path, namespaces)
    try:
        try:
            _next = it.next
        except AttributeError:
            return next(it)

        return _next()
    except StopIteration:
        return

    return


def findall(elem, path, namespaces=None):
    return list(iterfind(elem, path, namespaces))


def findtext(elem, path, default=None, namespaces=None):
    el = find(elem, path, namespaces)
    if el is None:
        return default
    else:
        return el.text or ''
        return