# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\lib\blas\setup.pyc
# Compiled at: 2013-02-16 13:27:30
from __future__ import division, print_function, absolute_import
import os, sys, re
from distutils.dep_util import newer_group, newer
from glob import glob
from os.path import join

def needs_cblas_wrapper(info):
    """Returns true if needs c wrapper around cblas for calling from
    fortran."""
    r_accel = re.compile('Accelerate')
    r_vec = re.compile('vecLib')
    res = False
    try:
        tmpstr = info['extra_link_args']
        for i in tmpstr:
            if r_accel.search(i) or r_vec.search(i):
                res = True

    except KeyError:
        pass

    return res


tmpl_empty_cblas_pyf = '\npython module cblas\n  usercode void empty_module(void) {}\n  interface\n    subroutine empty_module()\n      intent(c) empty_module\n    end subroutine empty_module\n  end interface\nend python module cblas\n'

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    from numpy.distutils.system_info import get_info
    config = Configuration('blas', parent_package, top_path)
    blas_opt = get_info('blas_opt', notfound_action=2)
    atlas_version = ([ v[3:-3] for k, v in blas_opt.get('define_macros', []) if k == 'ATLAS_INFO'
                     ] + [None])[0]
    if atlas_version:
        print('ATLAS version: %s' % atlas_version)
    target_dir = ''
    depends = [
     '__file__', 'fblas_l?.pyf.src', 'fblas.pyf.src', 'fblaswrap.f.src', 
     'fblaswrap_veclib_c.c.src']
    if needs_cblas_wrapper(blas_opt):
        sources = (
         [
          'fblas.pyf.src', 'fblaswrap_veclib_c.c.src'],)
    else:
        sources = [
         'fblas.pyf.src', 'fblaswrap.f.src']
    config.add_extension('fblas', sources=sources, depends=depends, extra_info=blas_opt)

    def get_cblas_source(ext, build_dir):
        name = ext.name.split('.')[-1]
        assert name == 'cblas', repr(name)
        if atlas_version is None:
            target = join(build_dir, target_dir, 'cblas.pyf')
            from distutils.dep_util import newer
            if newer(__file__, target):
                f = open(target, 'w')
                f.write(tmpl_empty_cblas_pyf)
                f.close()
        else:
            target = ext.depends[0]
            assert os.path.basename(target) == 'cblas.pyf.src'
        return target

    config.add_extension('cblas', sources=[
     get_cblas_source], depends=[
     'cblas.pyf.src', 'cblas_l?.pyf.src'], extra_info=blas_opt)
    config.add_data_dir('tests')
    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())