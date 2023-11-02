# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: GimpPaletteFile.pyc
# Compiled at: 2010-05-15 16:50:38
import re, string

class GimpPaletteFile:
    rawmode = 'RGB'

    def __init__(self, fp):
        self.palette = map((lambda i: chr(i) * 3), range(256))
        if fp.readline()[:12] != 'GIMP Palette':
            raise SyntaxError, 'not a GIMP palette file'
        i = 0
        while i <= 255:
            s = fp.readline()
            if not s:
                break
            if re.match('\\w+:|#', s):
                continue
            if len(s) > 100:
                raise SyntaxError, 'bad palette file'
            v = tuple(map(int, string.split(s)[:3]))
            if len(v) != 3:
                raise ValueError, 'bad palette entry'
            if 0 <= i <= 255:
                self.palette[i] = chr(v[0]) + chr(v[1]) + chr(v[2])
            i = i + 1

        self.palette = string.join(self.palette, '')

    def getpalette(self):
        return (
         self.palette, self.rawmode)