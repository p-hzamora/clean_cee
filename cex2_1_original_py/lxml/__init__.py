# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: D:\Dropbox\Programa Calificacion\Para_Compilar\compilacion\CEX\dist\.\lxml\__init__.py
# Compiled at: 2013-12-10 10:12:00


def get_include():
    """
    Returns a list of header include paths (for lxml itself, libxml2
    and libxslt) needed to compile C code against lxml if it was built
    with statically linked libraries.
    """
    import os
    lxml_path = __path__[0]
    include_path = os.path.join(lxml_path, 'includes')
    includes = [include_path, lxml_path]
    for name in os.listdir(include_path):
        path = os.path.join(include_path, name)
        if os.path.isdir(path):
            includes.append(path)

    return includes