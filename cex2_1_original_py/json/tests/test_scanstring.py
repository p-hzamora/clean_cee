# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: json\tests\test_scanstring.pyc
# Compiled at: 2011-05-30 06:53:52
import sys
from json.tests import PyTest, CTest

class TestScanstring(object):

    def test_scanstring(self):
        scanstring = self.json.decoder.scanstring
        self.assertEqual(scanstring('"z\\ud834\\udd20x"', 1, None, True), ('z𝄠x', 16))
        if sys.maxunicode == 65535:
            self.assertEqual(scanstring('"z𝄠x"', 1, None, True), ('z𝄠x', 6))
        else:
            self.assertEqual(scanstring('"z𝄠x"', 1, None, True), ('z𝄠x', 5))
        self.assertEqual(scanstring('"\\u007b"', 1, None, True), ('{', 8))
        self.assertEqual(scanstring('"A JSON payload should be an object or array, not a string."', 1, None, True), ('A JSON payload should be an object or array, not a string.',
                                                                                                                     60))
        self.assertEqual(scanstring('["Unclosed array"', 2, None, True), ('Unclosed array',
                                                                          17))
        self.assertEqual(scanstring('["extra comma",]', 2, None, True), ('extra comma',
                                                                         14))
        self.assertEqual(scanstring('["double extra comma",,]', 2, None, True), ('double extra comma',
                                                                                 21))
        self.assertEqual(scanstring('["Comma after the close"],', 2, None, True), ('Comma after the close',
                                                                                   24))
        self.assertEqual(scanstring('["Extra close"]]', 2, None, True), ('Extra close',
                                                                         14))
        self.assertEqual(scanstring('{"Extra comma": true,}', 2, None, True), ('Extra comma',
                                                                               14))
        self.assertEqual(scanstring('{"Extra value after close": true} "misplaced quoted value"', 2, None, True), ('Extra value after close',
                                                                                                                   26))
        self.assertEqual(scanstring('{"Illegal expression": 1 + 2}', 2, None, True), ('Illegal expression',
                                                                                      21))
        self.assertEqual(scanstring('{"Illegal invocation": alert()}', 2, None, True), ('Illegal invocation',
                                                                                        21))
        self.assertEqual(scanstring('{"Numbers cannot have leading zeroes": 013}', 2, None, True), ('Numbers cannot have leading zeroes',
                                                                                                    37))
        self.assertEqual(scanstring('{"Numbers cannot be hex": 0x14}', 2, None, True), ('Numbers cannot be hex',
                                                                                        24))
        self.assertEqual(scanstring('[[[[[[[[[[[[[[[[[[[["Too deep"]]]]]]]]]]]]]]]]]]]]', 21, None, True), ('Too deep',
                                                                                                            30))
        self.assertEqual(scanstring('{"Missing colon" null}', 2, None, True), ('Missing colon',
                                                                               16))
        self.assertEqual(scanstring('{"Double colon":: null}', 2, None, True), ('Double colon',
                                                                                15))
        self.assertEqual(scanstring('{"Comma instead of colon", null}', 2, None, True), ('Comma instead of colon',
                                                                                         25))
        self.assertEqual(scanstring('["Colon instead of comma": false]', 2, None, True), ('Colon instead of comma',
                                                                                          25))
        self.assertEqual(scanstring('["Bad value", truth]', 2, None, True), ('Bad value',
                                                                             12))
        return

    def test_issue3623(self):
        self.assertRaises(ValueError, self.json.decoder.scanstring, 'xxx', 1, 'xxx')
        self.assertRaises(UnicodeDecodeError, self.json.encoder.encode_basestring_ascii, b'xx\xff')

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            self.json.decoder.scanstring('xxx', sys.maxsize + 1)


class TestPyScanstring(TestScanstring, PyTest):
    pass


class TestCScanstring(TestScanstring, CTest):
    pass