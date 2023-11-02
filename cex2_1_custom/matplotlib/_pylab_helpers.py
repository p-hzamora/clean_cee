# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\_pylab_helpers.pyc
# Compiled at: 2012-10-30 18:11:14
"""
Manage figures for pyplot interface.
"""
from __future__ import print_function
import sys, gc, atexit, traceback

def error_msg(msg):
    print(msg, file=sys.stderr)


class Gcf(object):
    """
    Singleton to manage a set of integer-numbered figures.

    This class is never instantiated; it consists of two class
    attributes (a list and a dictionary), and a set of static
    methods that operate on those attributes, accessing them
    directly as class attributes.

    Attributes:

        *figs*:
          dictionary of the form {*num*: *manager*, ...}

        *_activeQue*:
          list of *managers*, with active one at the end

    """
    _activeQue = []
    figs = {}

    @staticmethod
    def get_fig_manager(num):
        """
        If figure manager *num* exists, make it the active
        figure and return the manager; otherwise return *None*.
        """
        manager = Gcf.figs.get(num, None)
        if manager is not None:
            Gcf.set_active(manager)
        return manager

    @staticmethod
    def destroy(num):
        """
        Try to remove all traces of figure *num*.

        In the interactive backends, this is bound to the
        window "destroy" and "delete" events.
        """
        if not Gcf.has_fignum(num):
            return
        manager = Gcf.figs[num]
        manager.canvas.mpl_disconnect(manager._cidgcf)
        oldQue = Gcf._activeQue[:]
        Gcf._activeQue = []
        for f in oldQue:
            if f != manager:
                Gcf._activeQue.append(f)

        del Gcf.figs[num]
        manager.destroy()
        gc.collect()

    @staticmethod
    def destroy_fig(fig):
        """*fig* is a Figure instance"""
        num = None
        for manager in Gcf.figs.itervalues():
            if manager.canvas.figure == fig:
                num = manager.num
                break

        if num is not None:
            Gcf.destroy(num)
        return

    @staticmethod
    def destroy_all():
        for manager in Gcf.figs.values():
            manager.canvas.mpl_disconnect(manager._cidgcf)
            manager.destroy()

        Gcf._activeQue = []
        Gcf.figs.clear()
        gc.collect()

    @staticmethod
    def has_fignum(num):
        """
        Return *True* if figure *num* exists.
        """
        return num in Gcf.figs

    @staticmethod
    def get_all_fig_managers():
        """
        Return a list of figure managers.
        """
        return Gcf.figs.values()

    @staticmethod
    def get_num_fig_managers():
        """
        Return the number of figures being managed.
        """
        return len(Gcf.figs.values())

    @staticmethod
    def get_active():
        """
        Return the manager of the active figure, or *None*.
        """
        if len(Gcf._activeQue) == 0:
            return
        else:
            return Gcf._activeQue[-1]
            return

    @staticmethod
    def set_active(manager):
        """
        Make the figure corresponding to *manager* the active one.
        """
        oldQue = Gcf._activeQue[:]
        Gcf._activeQue = []
        for m in oldQue:
            if m != manager:
                Gcf._activeQue.append(m)

        Gcf._activeQue.append(manager)
        Gcf.figs[manager.num] = manager


atexit.register(Gcf.destroy_all)