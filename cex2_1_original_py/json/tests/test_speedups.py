# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: json\tests\test_speedups.pyc
# Compiled at: 2011-05-30 06:53:52
from json.tests import CTest

class TestSpeedups(CTest):

    def test_scanstring(self):
        self.assertEqual(self.json.decoder.scanstring.__module__, '_json')
        self.assertIs(self.json.decoder.scanstring, self.json.decoder.c_scanstring)

    def test_encode_basestring_ascii(self):
        self.assertEqual(self.json.encoder.encode_basestring_ascii.__module__, '_json')
        self.assertIs(self.json.encoder.encode_basestring_ascii, self.json.encoder.c_encode_basestring_ascii)


class TestDecode(CTest):

    def test_make_scanner(self):
        self.assertRaises(AttributeError, self.json.scanner.c_make_scanner, 1)

    def test_make_encoder(self):
        self.assertRaises(TypeError, self.json.encoder.c_make_encoder, None, b"\xcd}=N\x12L\xf9y\xd7R\xba\x82\xf2'J}\xa0\xcau", None)
        return