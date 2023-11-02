# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\distutils\command\autodist.pyc
# Compiled at: 2013-04-07 07:04:04
"""This module implements additional tests ala autoconf which can be useful."""

def check_inline(cmd):
    """Return the inline identifier (may be empty)."""
    cmd._check_compiler()
    body = '\n#ifndef __cplusplus\nstatic %(inline)s int static_func (void)\n{\n    return 0;\n}\n%(inline)s int nostatic_func (void)\n{\n    return 0;\n}\n#endif'
    for kw in ['inline', '__inline__', '__inline']:
        st = cmd.try_compile(body % {'inline': kw}, None, None)
        if st:
            return kw

    return ''


def check_compiler_gcc4(cmd):
    """Return True if the C compiler is GCC 4.x."""
    cmd._check_compiler()
    body = '\nint\nmain()\n{\n#ifndef __GNUC__ && (__GNUC__ >= 4)\ndie in an horrible death\n#endif\n}\n'
    return cmd.try_compile(body, None, None)