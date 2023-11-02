# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: json\tests\test_float.pyc
# Compiled at: 2011-05-30 06:53:52
import math
from json.tests import PyTest, CTest

class TestFloat(object):

    def test_floats(self):
        for num in [1617161771.765, math.pi, math.pi ** 100,
         math.pi ** (-100), 3.1]:
            self.assertEqual(float(self.dumps(num)), num)
            self.assertEqual(self.loads(self.dumps(num)), num)
            self.assertEqual(self.loads(unicode(self.dumps(num))), num)

    def test_ints(self):
        for num in [1, 1, 4294967296, 18446744073709551616]:
            self.assertEqual(self.dumps(num), str(num))
            self.assertEqual(int(self.dumps(num)), num)
            self.assertEqual(self.loads(self.dumps(num)), num)
            self.assertEqual(self.loads(unicode(self.dumps(num))), num)


class TestPyFloat(TestFloat, PyTest):
    pass


class TestCFloat(TestFloat, CTest):
    pass