# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\numarray\util.pyc
# Compiled at: 2013-04-07 07:04:04
import os, numpy as np
__all__ = [
 'MathDomainError', 'UnderflowError', 'NumOverflowError', 
 'handleError', 
 'get_numarray_include_dirs']

class MathDomainError(ArithmeticError):
    pass


class UnderflowError(ArithmeticError):
    pass


class NumOverflowError(OverflowError, ArithmeticError):
    pass


def handleError(errorStatus, sourcemsg):
    """Take error status and use error mode to handle it."""
    modes = np.geterr()
    if errorStatus & np.FPE_INVALID:
        if modes['invalid'] == 'warn':
            print 'Warning: Encountered invalid numeric result(s)', sourcemsg
        if modes['invalid'] == 'raise':
            raise MathDomainError(sourcemsg)
    if errorStatus & np.FPE_DIVIDEBYZERO:
        if modes['dividebyzero'] == 'warn':
            print 'Warning: Encountered divide by zero(s)', sourcemsg
        if modes['dividebyzero'] == 'raise':
            raise ZeroDivisionError(sourcemsg)
    if errorStatus & np.FPE_OVERFLOW:
        if modes['overflow'] == 'warn':
            print 'Warning: Encountered overflow(s)', sourcemsg
        if modes['overflow'] == 'raise':
            raise NumOverflowError(sourcemsg)
    if errorStatus & np.FPE_UNDERFLOW:
        if modes['underflow'] == 'warn':
            print 'Warning: Encountered underflow(s)', sourcemsg
        if modes['underflow'] == 'raise':
            raise UnderflowError(sourcemsg)


def get_numarray_include_dirs():
    base = os.path.dirname(np.__file__)
    newdirs = [os.path.join(base, 'numarray', 'include')]
    return newdirs