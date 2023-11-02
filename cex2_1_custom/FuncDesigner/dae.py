# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: FuncDesigner\dae.pyc
# Compiled at: 2012-06-09 20:11:06
from ooSystem import ooSystem as oosystem
from FDmisc import FuncDesignerException
from numpy import ndarray

class dae:

    def __init__(self, equations, time, startPoint=None):
        self.equations = equations
        self.startPoint = startPoint
        self.time = time
        s = 'for DAE time must be dict of len 1 or array, '
        if type(time) == dict:
            if len(time) != 1:
                raise FuncDesignerException(s + 'got dict of len ' + str(len(time)))
            self.timeInterval = asarray(next(iter(time.values())))
            self.N = self.timeInterval.size
        else:
            if type(time) not in (list, tuple, ndarray):
                raise FuncDesignerException(s + 'got type %s insead ' + str(type(time)))
            self.N = len(time)
            self.timeInterval = time
        if self.N < 2:
            raise FuncDesignerException('lenght of time must be at least 2')

    def solve(self, solver=None, **kw):
        S = oosystem()
        S &= self.equations
        if self.startPoint is not None:
            startPoint = self.startPoint
        else:
            Dep = set()
            Dep.update(*[ eq._getDep() for eq in self.equations ])
            if None in Dep:
                Dep.remove(None)
            startPoint = {}
            for v in Dep:
                if 'size' in v.__dict__:
                    startPoint[v] = v.size
                else:
                    startPoint[v] = [
                     0] * self.N

        kw2 = kw.copy()
        if solver is not None:
            kw2['solver'] = solver
        r = S.solve(startPoint, **kw2)
        r.plot = self.plot
        self.r = r
        return r

    def plot(self, v, grid='on'):
        try:
            from pylab import plot, grid as Grid, show, legend
        except ImportError:
            raise FuncDesignerException('to plot DAE results you should have matplotlib installed')

        f, = plot(self.timeInterval, self.r(v))
        legend([f], [v.name])
        Grid(grid)
        show()