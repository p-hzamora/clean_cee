# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: json\tests\__init__.pyc
# Compiled at: 2011-05-30 06:53:52
import os, sys, json, doctest, unittest
from test import test_support
cjson = test_support.import_fresh_module('json', fresh=['_json'])
pyjson = test_support.import_fresh_module('json', blocked=['_json'])

class PyTest(unittest.TestCase):
    json = pyjson
    loads = staticmethod(pyjson.loads)
    dumps = staticmethod(pyjson.dumps)


@unittest.skipUnless(cjson, 'requires _json')
class CTest(unittest.TestCase):
    if cjson is not None:
        json = cjson
        loads = staticmethod(cjson.loads)
        dumps = staticmethod(cjson.dumps)


class TestPyTest(PyTest):

    def test_pyjson(self):
        self.assertEqual(self.json.scanner.make_scanner.__module__, 'json.scanner')
        self.assertEqual(self.json.decoder.scanstring.__module__, 'json.decoder')
        self.assertEqual(self.json.encoder.encode_basestring_ascii.__module__, 'json.encoder')


class TestCTest(CTest):

    def test_cjson(self):
        self.assertEqual(self.json.scanner.make_scanner.__module__, '_json')
        self.assertEqual(self.json.decoder.scanstring.__module__, '_json')
        self.assertEqual(self.json.encoder.c_make_encoder.__module__, '_json')
        self.assertEqual(self.json.encoder.encode_basestring_ascii.__module__, '_json')


here = os.path.dirname(__file__)

def test_suite():
    suite = additional_tests()
    loader = unittest.TestLoader()
    for fn in os.listdir(here):
        if fn.startswith('test') and fn.endswith('.py'):
            modname = 'json.tests.' + fn[:-3]
            __import__(modname)
            module = sys.modules[modname]
            suite.addTests(loader.loadTestsFromModule(module))

    return suite


def additional_tests():
    suite = unittest.TestSuite()
    for mod in (json, json.encoder, json.decoder):
        suite.addTest(doctest.DocTestSuite(mod))

    suite.addTest(TestPyTest('test_pyjson'))
    suite.addTest(TestCTest('test_cjson'))
    return suite


def main():
    suite = test_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    main()