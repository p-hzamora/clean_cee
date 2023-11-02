# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\oologfcn.pyc
# Compiled at: 2012-12-08 11:04:59


class OpenOptException(BaseException):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def oowarn(msg):
    print 'OpenOpt Warning: %s' % msg


def ooerr(msg):
    print 'OpenOpt Error: %s' % msg
    raise OpenOptException(msg)


pwSet = set()

def ooPWarn(msg):
    if msg in pwSet:
        return
    pwSet.add(msg)
    oowarn(msg)


def ooinfo(msg):
    print 'OpenOpt info: %s' % msg


def oohint(msg):
    print 'OpenOpt hint: %s' % msg


def oodisp(msg):
    print msg


def oodebugmsg(p, msg):
    if p.debug:
        print 'OpenOpt debug msg: %s' % msg