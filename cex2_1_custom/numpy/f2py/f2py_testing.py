# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\f2py\f2py_testing.pyc
# Compiled at: 2013-04-07 07:04:04
import sys, re
from numpy.testing.utils import jiffies, memusage

def cmdline():
    m = re.compile('\\A\\d+\\Z')
    args = []
    repeat = 1
    for a in sys.argv[1:]:
        if m.match(a):
            repeat = eval(a)
        else:
            args.append(a)

    f2py_opts = (' ').join(args)
    return (repeat, f2py_opts)


def run(runtest, test_functions, repeat=1):
    l = [ (t, repr(t.__doc__.split('\n')[1].strip())) for t in test_functions ]
    start_memusage = memusage()
    diff_memusage = None
    start_jiffies = jiffies()
    i = 0
    while i < repeat:
        i += 1
        for t, fname in l:
            runtest(t)
            if start_memusage is None:
                continue
            if diff_memusage is None:
                diff_memusage = memusage() - start_memusage
            else:
                diff_memusage2 = memusage() - start_memusage
                if diff_memusage2 != diff_memusage:
                    print 'memory usage change at step %i:' % i,
                    print diff_memusage2 - diff_memusage,
                    print fname
                    diff_memusage = diff_memusage2

    current_memusage = memusage()
    print 'run', repeat * len(test_functions), 'tests',
    print 'in %.2f seconds' % ((jiffies() - start_jiffies) / 100.0)
    if start_memusage:
        print 'initial virtual memory size:', start_memusage, 'bytes'
        print 'current virtual memory size:', current_memusage, 'bytes'
    return