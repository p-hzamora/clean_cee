# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\distutils\__config__.pyc
# Compiled at: 2013-04-07 08:26:20
__all__ = [
 'get_info', 'show']
blas_info = {}
lapack_info = {}
atlas_threads_info = {}
blas_src_info = {}
blas_opt_info = {}
lapack_src_info = {}
atlas_blas_threads_info = {}
lapack_opt_info = {}
atlas_info = {}
lapack_mkl_info = {}
blas_mkl_info = {}
atlas_blas_info = {}
mkl_info = {}

def get_info(name):
    g = globals()
    return g.get(name, g.get(name + '_info', {}))


def show():
    for name, info_dict in globals().items():
        if name[0] == '_' or type(info_dict) is not type({}):
            continue
        print name + ':'
        if not info_dict:
            print '  NOT AVAILABLE'
        for k, v in info_dict.items():
            v = str(v)
            if k == 'sources' and len(v) > 200:
                v = v[:60] + ' ...\n... ' + v[-60:]
            print '    %s = %s' % (k, v)