# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\distutils\lib2def.pyc
# Compiled at: 2013-04-07 07:04:04
import re, sys, os, subprocess
__doc__ = 'This module generates a DEF file from the symbols in\nan MSVC-compiled DLL import library.  It correctly discriminates between\ndata and functions.  The data is collected from the output of the program\nnm(1).\n\nUsage:\n    python lib2def.py [libname.lib] [output.def]\nor\n    python lib2def.py [libname.lib] > output.def\n\nlibname.lib defaults to python<py_ver>.lib and output.def defaults to stdout\n\nAuthor: Robert Kern <kernr@mail.ncifcrf.gov>\nLast Update: April 30, 1999\n'
__version__ = '0.1a'
py_ver = '%d%d' % tuple(sys.version_info[:2])
DEFAULT_NM = 'nm -Cs'
DEF_HEADER = 'LIBRARY         python%s.dll\n;CODE           PRELOAD MOVEABLE DISCARDABLE\n;DATA           PRELOAD SINGLE\n\nEXPORTS\n' % py_ver
FUNC_RE = re.compile('^(.*) in python%s\\.dll' % py_ver, re.MULTILINE)
DATA_RE = re.compile('^_imp__(.*) in python%s\\.dll' % py_ver, re.MULTILINE)

def parse_cmd():
    """Parses the command-line arguments.

libfile, deffile = parse_cmd()"""
    if len(sys.argv) == 3:
        if sys.argv[1][-4:] == '.lib' and sys.argv[2][-4:] == '.def':
            libfile, deffile = sys.argv[1:]
        elif sys.argv[1][-4:] == '.def' and sys.argv[2][-4:] == '.lib':
            deffile, libfile = sys.argv[1:]
        else:
            print "I'm assuming that your first argument is the library"
            print 'and the second is the DEF file.'
    elif len(sys.argv) == 2:
        if sys.argv[1][-4:] == '.def':
            deffile = sys.argv[1]
            libfile = 'python%s.lib' % py_ver
        elif sys.argv[1][-4:] == '.lib':
            deffile = None
            libfile = sys.argv[1]
    else:
        libfile = 'python%s.lib' % py_ver
        deffile = None
    return (
     libfile, deffile)


def getnm(nm_cmd=[
 'nm', '-Cs', 'python%s.lib' % py_ver]):
    """Returns the output of nm_cmd via a pipe.

nm_output = getnam(nm_cmd = 'nm -Cs py_lib')"""
    f = subprocess.Popen(nm_cmd, shell=True, stdout=subprocess.PIPE)
    nm_output = f.stdout.read()
    f.stdout.close()
    return nm_output


def parse_nm(nm_output):
    """Returns a tuple of lists: dlist for the list of data
symbols and flist for the list of function symbols.

dlist, flist = parse_nm(nm_output)"""
    data = DATA_RE.findall(nm_output)
    func = FUNC_RE.findall(nm_output)
    flist = []
    for sym in data:
        if sym in func and (sym[:2] == 'Py' or sym[:3] == '_Py' or sym[:4] == 'init'):
            flist.append(sym)

    dlist = []
    for sym in data:
        if sym not in flist and (sym[:2] == 'Py' or sym[:3] == '_Py'):
            dlist.append(sym)

    dlist.sort()
    flist.sort()
    return (dlist, flist)


def output_def(dlist, flist, header, file=sys.stdout):
    """Outputs the final DEF file to a file defaulting to stdout.

output_def(dlist, flist, header, file = sys.stdout)"""
    for data_sym in dlist:
        header = header + '\t%s DATA\n' % data_sym

    header = header + '\n'
    for func_sym in flist:
        header = header + '\t%s\n' % func_sym

    file.write(header)


if __name__ == '__main__':
    libfile, deffile = parse_cmd()
    if deffile is None:
        deffile = sys.stdout
    else:
        deffile = open(deffile, 'w')
    nm_cmd = [
     str(DEFAULT_NM), str(libfile)]
    nm_output = getnm(nm_cmd)
    dlist, flist = parse_nm(nm_output)
    output_def(dlist, flist, DEF_HEADER, deffile)