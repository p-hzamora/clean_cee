# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\special\specfun.pyc
# Compiled at: 2015-05-29 14:13:22


def __load():
    import imp, os, sys
    try:
        dirname = os.path.dirname(__loader__.archive)
    except NameError:
        dirname = sys.prefix

    path = os.path.join(dirname, 'scipy.special.specfun.pyd')
    mod = imp.load_dynamic(__name__, path)


__load()
del __load