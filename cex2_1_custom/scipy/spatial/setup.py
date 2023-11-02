# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\spatial\setup.pyc
# Compiled at: 2013-02-16 13:27:32
from __future__ import division, print_function, absolute_import
from os.path import join

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration, get_numpy_include_dirs
    from numpy.distutils.system_info import get_info
    from distutils.sysconfig import get_python_inc
    config = Configuration('spatial', parent_package, top_path)
    config.add_data_dir('tests')
    config.add_data_dir('benchmarks')
    qhull_src = [
     'geom2.c', 'geom.c', 'global.c', 'io.c', 'libqhull.c', 
     'mem.c', 
     'merge.c', 'poly2.c', 'poly.c', 'qset.c', 
     'random.c', 
     'rboxlib.c', 'stat.c', 'user.c', 'usermem.c', 
     'userprintf.c', 
     'userprintf_rbox.c']
    qhull_src = [ join('qhull', 'src', x) for x in qhull_src ]
    inc_dirs = [
     get_python_inc()]
    if inc_dirs[0] != get_python_inc(plat_specific=1):
        inc_dirs.append(get_python_inc(plat_specific=1))
    inc_dirs.append(get_numpy_include_dirs())
    cfg = dict(get_info('lapack_opt'))
    cfg.setdefault('include_dirs', []).extend(inc_dirs)
    cfg.setdefault('define_macros', []).append(('qh_QHpointer', '1'))
    config.add_extension('qhull', sources=([
     'qhull.c'] + qhull_src), **cfg)
    config.add_extension('ckdtree', sources=['ckdtree.c'])
    config.add_extension('_distance_wrap', sources=[
     join('src', 'distance_wrap.c'), join('src', 'distance.c')], include_dirs=[
     get_numpy_include_dirs()])
    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(maintainer='SciPy Developers', author='Anne Archibald', maintainer_email='scipy-dev@scipy.org', description='Spatial algorithms and data structures', url='http://www.scipy.org', license='SciPy License (BSD Style)', **configuration(top_path='').todict())