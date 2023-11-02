# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: win32traceutil.pyc
# Compiled at: 2011-03-19 11:51:22
import win32trace

def RunAsCollector():
    import sys
    try:
        import win32api
        win32api.SetConsoleTitle('Python Trace Collector')
    except:
        pass

    win32trace.InitRead()
    print 'Collecting Python Trace Output...'
    try:
        while 1:
            sys.stdout.write(win32trace.blockingread(500))

    except KeyboardInterrupt:
        print 'Ctrl+C'


def SetupForPrint():
    win32trace.InitWrite()
    try:
        print 'Redirecting output to win32trace remote collector'
    except:
        pass

    win32trace.setprint()


if __name__ == '__main__':
    RunAsCollector()
else:
    SetupForPrint()