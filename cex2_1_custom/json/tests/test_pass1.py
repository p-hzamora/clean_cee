# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: json\tests\test_pass1.pyc
# Compiled at: 2011-05-30 06:53:52
from json.tests import PyTest, CTest
JSON = '\n[\n    "JSON Test Pattern pass1",\n    {"object with 1 member":["array with 1 element"]},\n    {},\n    [],\n    -42,\n    true,\n    false,\n    null,\n    {\n        "integer": 1234567890,\n        "real": -9876.543210,\n        "e": 0.123456789e-12,\n        "E": 1.234567890E+34,\n        "":  23456789012E666,\n        "zero": 0,\n        "one": 1,\n        "space": " ",\n        "quote": "\\"",\n        "backslash": "\\\\",\n        "controls": "\\b\\f\\n\\r\\t",\n        "slash": "/ & \\/",\n        "alpha": "abcdefghijklmnopqrstuvwyz",\n        "ALPHA": "ABCDEFGHIJKLMNOPQRSTUVWYZ",\n        "digit": "0123456789",\n        "special": "`1~!@#$%^&*()_+-={\':[,]}|;.</>?",\n        "hex": "\\u0123\\u4567\\u89AB\\uCDEF\\uabcd\\uef4A",\n        "true": true,\n        "false": false,\n        "null": null,\n        "array":[  ],\n        "object":{  },\n        "address": "50 St. James Street",\n        "url": "http://www.JSON.org/",\n        "comment": "// /* <!-- --",\n        "# -- --> */": " ",\n        " s p a c e d " :[1,2 , 3\n\n,\n\n4 , 5        ,          6           ,7        ],\n        "compact": [1,2,3,4,5,6,7],\n        "jsontext": "{\\"object with 1 member\\":[\\"array with 1 element\\"]}",\n        "quotes": "&#34; \\u0022 %22 0x22 034 &#x22;",\n        "\\/\\\\\\"\\uCAFE\\uBABE\\uAB98\\uFCDE\\ubcda\\uef4A\\b\\f\\n\\r\\t`1~!@#$%^&*()_+-=[]{}|;:\',./<>?"\n: "A key can be any string"\n    },\n    0.5 ,98.6\n,\n99.44\n,\n\n1066\n\n\n,"rosebud"]\n'

class TestPass1(object):

    def test_parse(self):
        res = self.loads(JSON)
        out = self.dumps(res)
        self.assertEqual(res, self.loads(out))
        try:
            self.dumps(res, allow_nan=False)
        except ValueError:
            pass
        else:
            self.fail('23456789012E666 should be out of range')


class TestPyPass1(TestPass1, PyTest):
    pass


class TestCPass1(TestPass1, CTest):
    pass