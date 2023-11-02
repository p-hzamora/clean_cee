# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: json\tests\test_dump.pyc
# Compiled at: 2011-05-30 06:53:52
from cStringIO import StringIO
from json.tests import PyTest, CTest

class TestDump(object):

    def test_dump(self):
        sio = StringIO()
        self.json.dump({}, sio)
        self.assertEqual(sio.getvalue(), '{}')

    def test_dumps(self):
        self.assertEqual(self.dumps({}), '{}')

    def test_encode_truefalse(self):
        self.assertEqual(self.dumps({True: False, False: True}, sort_keys=True), '{"false": true, "true": false}')
        self.assertEqual(self.dumps({2: 3.0, 4.0: 5, False: 1, 6: True}, sort_keys=True), '{"false": 1, "2": 3.0, "4.0": 5, "6": true}')


class TestPyDump(TestDump, PyTest):
    pass


class TestCDump(TestDump, CTest):
    pass