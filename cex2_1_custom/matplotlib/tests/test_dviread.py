# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\test_dviread.pyc
# Compiled at: 2012-08-28 11:32:46
from nose.tools import assert_equal
import matplotlib.dviread as dr, os.path
original_find_tex_file = dr.find_tex_file

def setup():
    dr.find_tex_file = lambda x: x


def teardown():
    dr.find_tex_file = original_find_tex_file


def test_PsfontsMap():
    filename = os.path.join(os.path.dirname(__file__), 'baseline_images', 'dviread', 'test.map')
    fontmap = dr.PsfontsMap(filename)
    for n in [1, 2, 3, 4, 5]:
        key = 'TeXfont%d' % n
        entry = fontmap[key]
        assert_equal(entry.texname, key)
        assert_equal(entry.psname, 'PSfont%d' % n)
        if n not in (3, 5):
            assert_equal(entry.encoding, 'font%d.enc' % n)
        elif n == 3:
            assert_equal(entry.encoding, 'enc3.foo')
        if n not in (1, 5):
            assert_equal(entry.filename, 'font%d.pfa' % n)
        else:
            assert_equal(entry.filename, 'font%d.pfb' % n)
        if n == 4:
            assert_equal(entry.effects, {'slant': -0.1, 'extend': 2.2})
        else:
            assert_equal(entry.effects, {})

    entry = fontmap['TeXfont6']
    assert_equal(entry.filename, None)
    assert_equal(entry.encoding, None)
    entry = fontmap['TeXfont7']
    assert_equal(entry.filename, None)
    assert_equal(entry.encoding, 'font7.enc')
    entry = fontmap['TeXfont8']
    assert_equal(entry.filename, 'font8.pfb')
    assert_equal(entry.encoding, None)
    entry = fontmap['TeXfont9']
    assert_equal(entry.filename, '/absolute/font9.pfb')
    return