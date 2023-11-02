# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\lib\lapack\scons_support.pyc
# Compiled at: 2013-02-16 13:27:30
from __future__ import division, print_function, absolute_import
from os.path import join as pjoin, splitext, basename as pbasename

def generate_interface_emitter(target, source, env):
    base = str(target[0])
    return (['%s.pyf' % base], source)


def do_generate_fake_interface(target, source, env):
    """Generate a (fake) .pyf file from another pyf file (!)."""
    target_name = str(target[0])
    source_name = str(source[0])
    name = splitext(pbasename(target_name))[0]
    f = open(target_name, 'w')
    f.write('python module ' + name + '\n')
    f.write('usercode void empty_module(void) {}\n')
    f.write('interface\n')
    f.write('subroutine empty_module()\n')
    f.write('intent(c) empty_module\n')
    f.write('end subroutine empty_module\n')
    f.write('end interface\nend python module' + name + '\n')
    f.close()
    return 0