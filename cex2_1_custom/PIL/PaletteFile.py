# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: PIL\PaletteFile.pyc
# Compiled at: 2010-05-15 16:50:38
import string

class PaletteFile:
    rawmode = 'RGB'

    def __init__(self, fp):
        self.palette = map((lambda i: (i, i, i)), range(256))
        while 1:
            s = fp.readline()
            if not s:
                break
            if s[0] == '#':
                continue
            if len(s) > 100:
                raise SyntaxError, 'bad palette file'
            v = map(int, string.split(s))
            try:
                i, r, g, b = v
            except ValueError:
                i, r = v
                g = b = r

            if 0 <= i <= 255:
                self.palette[i] = chr(r) + chr(g) + chr(b)

        self.palette = string.join(self.palette, '')

    def getpalette(self):
        return (
         self.palette, self.rawmode)