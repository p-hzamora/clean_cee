# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\testing\noseclasses.pyc
# Compiled at: 2012-11-06 11:15:42
from __future__ import print_function
import os
from nose.plugins.errorclass import ErrorClass, ErrorClassPlugin

class KnownFailureTest(Exception):
    """Raise this exception to mark a test as a known failing test."""
    pass


class KnownFailureDidNotFailTest(Exception):
    """Raise this exception to mark a test should have failed but did not."""
    pass


class ImageComparisonFailure(AssertionError):
    """Raise this exception to mark a test as a comparison between two images."""
    pass


class KnownFailure(ErrorClassPlugin):
    """Plugin that installs a KNOWNFAIL error class for the
    KnownFailureClass exception.  When KnownFailureTest is raised,
    the exception will be logged in the knownfail attribute of the
    result, 'K' or 'KNOWNFAIL' (verbose) will be output, and the
    exception will not be counted as an error or failure.

    This is based on numpy.testing.noseclasses.KnownFailure.
    """
    enabled = True
    knownfail = ErrorClass(KnownFailureTest, label='KNOWNFAIL', isfailure=False)

    def options(self, parser, env=os.environ):
        env_opt = 'NOSE_WITHOUT_KNOWNFAIL'
        parser.add_option('--no-knownfail', action='store_true', dest='noKnownFail', default=env.get(env_opt, False), help='Disable special handling of KnownFailureTest exceptions')

    def configure(self, options, conf):
        if not self.can_configure:
            return
        self.conf = conf
        disable = getattr(options, 'noKnownFail', False)
        if disable:
            self.enabled = False

    def addError(self, test, err, *zero_nine_capt_args):
        pass