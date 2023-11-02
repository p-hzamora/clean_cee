# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\lib\extformat.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = '$Id$'
__doc__ = 'Apparently not used anywhere, purpose unknown!'
from tokenize import tokenprog
import sys

def _matchorfail(text, pos):
    match = tokenprog.match(text, pos)
    if match is None:
        raise ValueError(text, pos)
    return (
     match, match.end())


def dictformat(_format, L={}, G={}):
    format = _format
    S = {}
    chunks = []
    pos = 0
    n = 0
    while 1:
        pc = format.find('%', pos)
        if pc < 0:
            break
        nextchar = format[pc + 1]
        if nextchar == '(':
            chunks.append(format[pos:pc])
            pos, level = pc + 2, 1
            while level:
                match, pos = _matchorfail(format, pos)
                tstart, tend = match.regs[3]
                token = format[tstart:tend]
                if token == '(':
                    level = level + 1
                elif token == ')':
                    level = level - 1

            vname = '__superformat_%d' % n
            n += 1
            S[vname] = eval(format[pc + 2:pos - 1], G, L)
            chunks.append('%%(%s)' % vname)
        else:
            nc = pc + 1 + (nextchar == '%')
            chunks.append(format[pos:nc])
            pos = nc

    if pos < len(format):
        chunks.append(format[pos:])
    return ('').join(chunks) % S


def magicformat(format):
    """Evaluate and substitute the appropriate parts of the string."""
    frame = sys._getframe(1)
    return dictformat(format, frame.f_locals, frame.f_globals)


if __name__ == '__main__':
    from reportlab.lib.formatters import DecimalFormatter
    _DF = {}

    def df(n, dp=2, ds='.', ts=','):
        try:
            _df = _DF[(dp, ds)]
        except KeyError:
            _df = _DF[(dp, ds)] = DecimalFormatter(places=dp, decimalSep=ds, thousandSep=ts)

        return _df(n)


    from reportlab.lib.extformat import magicformat
    Z = {'abc': ('ab', 'c')}
    x = 300000.23
    percent = 79.2

    class dingo:
        a = 3


    print magicformat("\n$%%(df(x,dp=3))s --> $%(df(x,dp=3))s\n$%%(df(x,dp=2,ds=',',ts='.'))s --> $%(df(x,dp=2,ds=',',ts='.'))s\n%%(percent).2f%%%% --> %(percent).2f%%\n%%(dingo.a)s --> %(dingo.a)s\n%%(Z['abc'][0])s --> %(Z['abc'][0])s\n")

    def func0(aa=1):

        def func1(bb=2):
            print magicformat('bb=%(bb)s Z=%(Z)r')

        func1('BB')


    func0('AA')