# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\__config__.pyc
# Compiled at: 2013-04-06 18:21:04
__all__ = [
 'get_info', 'show']
atlas_threads_info = {}
blas_opt_info = {'libraries': ['f77blas', 'cblas', 'atlas'], 'library_dirs': ['C:\\local\\lib\\yop\\sse3'], 'language': 'c', 'define_macros': [('ATLAS_INFO', '"\\"?.?.?\\""')]}
umfpack_info = {}
atlas_blas_threads_info = {}
lapack_opt_info = {'libraries': ['lapack', 'f77blas', 'cblas', 'atlas'], 'library_dirs': ['C:\\local\\lib\\yop\\sse3'], 'language': 'f77', 'define_macros': [('ATLAS_INFO', '"\\"?.?.?\\""')]}
atlas_info = {'libraries': ['lapack', 'f77blas', 'cblas', 'atlas'], 'library_dirs': ['C:\\local\\lib\\yop\\sse3'], 'language': 'f77'}
lapack_mkl_info = {}
blas_mkl_info = {}
atlas_blas_info = {'libraries': ['f77blas', 'cblas', 'atlas'], 'library_dirs': ['C:\\local\\lib\\yop\\sse3'], 'language': 'c'}
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