# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\distutils\log.pyc
# Compiled at: 2013-04-07 07:04:04
import sys
from distutils.log import *
from distutils.log import Log as old_Log
from distutils.log import _global_log
if sys.version_info[0] < 3:
    from misc_util import red_text, default_text, cyan_text, green_text, is_sequence, is_string
else:
    from numpy.distutils.misc_util import red_text, default_text, cyan_text, green_text, is_sequence, is_string

def _fix_args(args, flag=1):
    if is_string(args):
        return args.replace('%', '%%')
    if flag and is_sequence(args):
        return tuple([ _fix_args(a, flag=0) for a in args ])
    return args


class Log(old_Log):

    def _log(self, level, msg, args):
        if level >= self.threshold:
            if args:
                msg = msg % _fix_args(args)
            print _global_color_map[level](msg)
            sys.stdout.flush()

    def good(self, msg, *args):
        """If we'd log WARN messages, log this message as a 'nice' anti-warn
        message.
        """
        if WARN >= self.threshold:
            if args:
                print green_text(msg % _fix_args(args))
            else:
                print green_text(msg)
            sys.stdout.flush()


_global_log.__class__ = Log
good = _global_log.good

def set_threshold(level, force=False):
    prev_level = _global_log.threshold
    if prev_level > DEBUG or force:
        _global_log.threshold = level
        if level <= DEBUG:
            info('set_threshold: setting thershold to DEBUG level, it can be changed only with force argument')
    else:
        info('set_threshold: not changing thershold from DEBUG level %s to %s' % (prev_level, level))
    return prev_level


def set_verbosity(v, force=False):
    prev_level = _global_log.threshold
    if v < 0:
        set_threshold(ERROR, force)
    elif v == 0:
        set_threshold(WARN, force)
    elif v == 1:
        set_threshold(INFO, force)
    elif v >= 2:
        set_threshold(DEBUG, force)
    return {FATAL: -2, ERROR: -1, WARN: 0, INFO: 1, DEBUG: 2}.get(prev_level, 1)


_global_color_map = {DEBUG: cyan_text, 
   INFO: default_text, 
   WARN: red_text, 
   ERROR: red_text, 
   FATAL: red_text}
set_verbosity(0, force=True)