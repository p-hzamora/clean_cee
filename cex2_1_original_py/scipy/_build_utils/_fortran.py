# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\_build_utils\_fortran.pyc
# Compiled at: 2013-02-16 13:27:28
import re, sys

def _uses_veclib(info):
    r_accelerate = re.compile('Accelerate|vecLib')
    extra_link_args = info.get('extra_link_args', '')
    for arg in extra_link_args:
        if r_accelerate.search(arg):
            return True

    return False


def _uses_mkl(info):
    r_mkl = re.compile('mkl_core')
    libraries = info.get('libraries', '')
    for library in libraries:
        if r_mkl.search(library):
            return True

    return False


def needs_g77_abi_wrapper(info):
    """Returns true if g77 ABI wrapper must be used."""
    if _uses_veclib(info):
        return True
    else:
        if _uses_mkl(info) and sys.platform == 'darwin':
            return True
        return False