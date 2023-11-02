# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: json\tool.pyc
# Compiled at: 2011-03-08 09:43:16
"""Command-line tool to validate and pretty-print JSON

Usage::

    $ echo '{"json":"obj"}' | python -m json.tool
    {
        "json": "obj"
    }
    $ echo '{ 1.2:3.4}' | python -m json.tool
    Expecting property name: line 1 column 2 (char 2)

"""
import sys, json

def main():
    if len(sys.argv) == 1:
        infile = sys.stdin
        outfile = sys.stdout
    else:
        if len(sys.argv) == 2:
            infile = open(sys.argv[1], 'rb')
            outfile = sys.stdout
        elif len(sys.argv) == 3:
            infile = open(sys.argv[1], 'rb')
            outfile = open(sys.argv[2], 'wb')
        else:
            raise SystemExit(sys.argv[0] + ' [infile [outfile]]')
        try:
            obj = json.load(infile)
        except ValueError as e:
            raise SystemExit(e)

    json.dump(obj, outfile, sort_keys=True, indent=4)
    outfile.write('\n')


if __name__ == '__main__':
    main()