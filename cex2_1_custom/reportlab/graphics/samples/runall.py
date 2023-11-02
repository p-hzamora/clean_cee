# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\graphics\samples\runall.pyc
# Compiled at: 2013-03-27 15:37:42
import sys, glob, string, inspect, types

def moduleClasses(mod):

    def P(obj, m=mod.__name__, CT=types.ClassType):
        return type(obj) == CT and obj.__module__ == m

    try:
        return inspect.getmembers(mod, P)[0][1]
    except:
        return

    return


def getclass(f):
    return moduleClasses(__import__(f))


def run(format, VERBOSE=0):
    formats = string.split(format, ',')
    for i in range(0, len(formats)):
        formats[i] == string.lower(string.strip(formats[i]))

    allfiles = glob.glob('*.py')
    allfiles.sort()
    for fn in allfiles:
        f = string.split(fn, '.')[0]
        c = getclass(f)
        if c != None:
            print c.__name__
            try:
                for fmt in formats:
                    if fmt:
                        c().save(formats=[fmt], outDir='.', fnRoot=c.__name__)
                        if VERBOSE:
                            print '  %s.%s' % (c.__name__, fmt)

            except:
                print "  COULDN'T CREATE '%s.%s'!" % (c.__name__, format)

    return


if __name__ == '__main__':
    if len(sys.argv) == 1:
        run('pdf,pict,png')
    else:
        try:
            if sys.argv[1] == '-h':
                print 'usage: runall.py [FORMAT] [-h]'
                print '   if format is supplied is should be one or more of pdf,gif,eps,png etc'
                print '   if format is missing the following formats are assumed: pdf,pict,png'
                print '   -h prints this message'
            else:
                t = sys.argv[1:]
                for f in t:
                    run(f)

        except:
            print 'usage: runall.py [FORMAT][-h]'
            print '   if format is supplied is should be one or more of pdf,gif,eps,png etc'
            print '   if format is missing the following formats are assumed: pdf,pict,png'
            print '   -h prints this message'
            raise