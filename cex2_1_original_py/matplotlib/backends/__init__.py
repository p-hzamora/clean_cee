# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\backends\__init__.pyc
# Compiled at: 2012-10-30 18:11:14
from __future__ import print_function
import matplotlib, inspect, warnings
from matplotlib.rcsetup import interactive_bk
__all__ = [
 'backend', 'show', 'draw_if_interactive', 
 'new_figure_manager', 'backend_version']
backend = matplotlib.get_backend()

def pylab_setup():
    """return new_figure_manager, draw_if_interactive and show for pylab"""
    if backend.startswith('module://'):
        backend_name = backend[9:]
    else:
        backend_name = 'backend_' + backend
        backend_name = backend_name.lower()
        backend_name = 'matplotlib.backends.%s' % backend_name.lower()
    backend_mod = __import__(backend_name, globals(), locals(), [backend_name])
    new_figure_manager = backend_mod.new_figure_manager

    def do_nothing_show(*args, **kwargs):
        frame = inspect.currentframe()
        fname = frame.f_back.f_code.co_filename
        if fname in ('<stdin>', '<ipython console>'):
            warnings.warn("\nYour currently selected backend, '%s' does not support show().\nPlease select a GUI backend in your matplotlibrc file ('%s')\nor with matplotlib.use()" % (
             backend, matplotlib.matplotlib_fname()))

    def do_nothing(*args, **kwargs):
        pass

    backend_version = getattr(backend_mod, 'backend_version', 'unknown')
    show = getattr(backend_mod, 'show', do_nothing_show)
    draw_if_interactive = getattr(backend_mod, 'draw_if_interactive', do_nothing)
    if backend.lower() in ('wx', 'wxagg'):
        Toolbar = backend_mod.Toolbar
        __all__.append('Toolbar')
    matplotlib.verbose.report('backend %s version %s' % (backend, backend_version))
    return (
     backend_mod, new_figure_manager, draw_if_interactive, show)