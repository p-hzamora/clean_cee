# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: pytz\exceptions.pyc
# Compiled at: 2012-11-06 15:31:10
"""
Custom exceptions raised by pytz.
"""
__all__ = [
 'UnknownTimeZoneError', 'InvalidTimeError', 'AmbiguousTimeError',
 'NonExistentTimeError']

class UnknownTimeZoneError(KeyError):
    """Exception raised when pytz is passed an unknown timezone.

    >>> isinstance(UnknownTimeZoneError(), LookupError)
    True

    This class is actually a subclass of KeyError to provide backwards
    compatibility with code relying on the undocumented behavior of earlier
    pytz releases.

    >>> isinstance(UnknownTimeZoneError(), KeyError)
    True
    """
    pass


class InvalidTimeError(Exception):
    """Base class for invalid time exceptions."""
    pass


class AmbiguousTimeError(InvalidTimeError):
    """Exception raised when attempting to create an ambiguous wallclock time.

    At the end of a DST transition period, a particular wallclock time will
    occur twice (once before the clocks are set back, once after). Both
    possibilities may be correct, unless further information is supplied.

    See DstTzInfo.normalize() for more info
    """
    pass


class NonExistentTimeError(InvalidTimeError):
    """Exception raised when attempting to create a wallclock time that
    cannot exist.

    At the start of a DST transition period, the wallclock time jumps forward.
    The instants jumped over never occur.
    """
    pass