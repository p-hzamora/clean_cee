# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: json\tests\test_separators.pyc
# Compiled at: 2011-05-30 06:53:52
import textwrap
from json.tests import PyTest, CTest

class TestSeparators(object):

    def test_separators(self):
        h = [
         [
          'blorpie'], ['whoops'], [], 'd-shtaeou', 'd-nthiouh', 'i-vhbjkhnth', {'nifty': 87}, {'field': 'yes', 'morefield': False}]
        expect = textwrap.dedent('        [\n          [\n            "blorpie"\n          ] ,\n          [\n            "whoops"\n          ] ,\n          [] ,\n          "d-shtaeou" ,\n          "d-nthiouh" ,\n          "i-vhbjkhnth" ,\n          {\n            "nifty" : 87\n          } ,\n          {\n            "field" : "yes" ,\n            "morefield" : false\n          }\n        ]')
        d1 = self.dumps(h)
        d2 = self.dumps(h, indent=2, sort_keys=True, separators=(' ,', ' : '))
        h1 = self.loads(d1)
        h2 = self.loads(d2)
        self.assertEqual(h1, h)
        self.assertEqual(h2, h)
        self.assertEqual(d2, expect)


class TestPySeparators(TestSeparators, PyTest):
    pass


class TestCSeparators(TestSeparators, CTest):
    pass