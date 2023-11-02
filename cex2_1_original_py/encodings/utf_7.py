# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: encodings\utf_7.pyc
# Compiled at: 2011-03-08 09:43:14
""" Python 'utf-7' Codec

Written by Brian Quinlan (brian@sweetapp.com).
"""
import codecs
encode = codecs.utf_7_encode

def decode(input, errors='strict'):
    return codecs.utf_7_decode(input, errors, True)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final=False):
        return codecs.utf_7_encode(input, self.errors)[0]


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    _buffer_decode = codecs.utf_7_decode


class StreamWriter(codecs.StreamWriter):
    encode = codecs.utf_7_encode


class StreamReader(codecs.StreamReader):
    decode = codecs.utf_7_decode


def getregentry():
    return codecs.CodecInfo(name='utf-7', encode=encode, decode=decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)