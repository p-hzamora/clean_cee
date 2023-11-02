# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: FuncDesigner\ode.pyc
# Compiled at: 2013-05-20 19:53:32
from translator import FuncDesignerTranslator
from FDmisc import FuncDesignerException, _getDiffVarsID
from numpy import ndarray, hstack, vstack, isscalar, asarray
from ooVar import oovar
from ooFun import atleast_oofun

class ode:
    _isInitialized = False
    solver = 'scipy_lsoda'

    def __init__(self, equations, startPoint, *args, **kwargs):
        if len(args) > 2:
            raise FuncDesignerException('incorrect ode definition, too many args are obtained')
        if not isinstance(equations, dict):
            raise FuncDesignerException('1st argument of ode constructor should be Python dict')
        if not isinstance(startPoint, dict):
            raise FuncDesignerException('2nd argument of ode constructor should be Python dict')
        if len(args) == 2:
            print "\n            FuncDesigner warning: you're using obsolete ode() API, \n            now time should be passed as 3rd argument {timeVariable: times}\n            or just array of times if equations are time-independend"
            timeVariable, times = args[0], args[1]
        else:
            if len(args) != 1 or type(args[0]) not in (dict, list, tuple, ndarray):
                raise FuncDesignerException('3rd argument of ode constructor must be dict {timeVariable:array_of_times} or just array_of_times')
            if type(args[0]) == dict:
                if len(args[0]) != 1:
                    raise FuncDesignerException('in time argument dict has to have exactly 1 entry')
                timeVariable, times = list(args[0].items())[0]
                if not isinstance(timeVariable, oovar):
                    raise FuncDesignerException('incorrect time variable, must be FuncDesigner oofun')
            else:
                times = args[0]
                timeVariable = None
            self.timeVariable = timeVariable
            if timeVariable is not None and timeVariable in equations:
                raise FuncDesignerException('ode: differentiation of a variable by itself (time by time) is treated as a potential bug and thus is forbidden')
            if not (isinstance(times, (list, tuple)) or isinstance(times, ndarray) and times.ndim == 1):
                raise FuncDesignerException('incorrect user-defined time argument, must be Python list or numpy array of time values')
            self.times = times
            self._fd_func, self._startPoint, self._timeVariable, self._times, self._kwargs = (equations, startPoint, timeVariable, times, kwargs)
            startPoint = dict([ (key, val) for key, val in startPoint.items() ])
            if timeVariable is not None:
                startPoint[timeVariable] = times[0]
            y0 = []
            Funcs = []
            Point4TranslatorAssignment = {}
            for v, func in equations.items():
                func = atleast_oofun(func)
                if not isinstance(v, oovar):
                    raise FuncDesignerException('ode: dict keys must be FuncDesigner oovars, got "%s" instead' % type(v))
                startFVal = asarray(func(startPoint))
                y0.append(asarray(startPoint[v]))
                Funcs.append(func)
                Point4TranslatorAssignment[v] = startFVal
                if startFVal.size != asarray(startPoint[v]).size or hasattr(v, 'size') and isscalar(v.size) and startFVal.size != v.size:
                    raise FuncDesignerException('error in user-defined data: oovar "%s" size is not equal to related function value in start point' % v.name)

        self.y0 = hstack(y0)
        self.varSizes = [ y.size for y in y0 ]
        ooT = FuncDesignerTranslator(Point4TranslatorAssignment)
        self.ooT = ooT

        def func(y, t):
            tmp = dict(ooT.vector2point(y))
            if timeVariable is not None:
                tmp[timeVariable] = t
            return hstack([ func(tmp) for func in Funcs ])

        self.func = func
        _FDVarsID = _getDiffVarsID()

        def derivative(y, t):
            tmp = dict(ooT.vector2point(y))
            if timeVariable is not None:
                tmp[timeVariable] = t
            r = []
            for func in Funcs:
                tt = func.D(tmp, fixedVarsScheduleID=_FDVarsID)
                if timeVariable is not None:
                    tt.pop(timeVariable)
                r.append(ooT.pointDerivative2array(tt))

            return vstack(r)

        self.derivative = derivative
        self.Point4TranslatorAssignment = Point4TranslatorAssignment
        return

    def solve(self, solver='scipy_lsoda', *args, **kwargs):
        if len(args) > 0:
            raise FuncDesignerException('no args are currently available for the function ode::solve')
        solverName = solver if isinstance(solver, str) else solver.__name__
        if solverName.startswith('interalg'):
            try:
                from openopt import ODE
            except ImportError:
                raise FuncDesignerException('You should have openopt insalled')

            prob = ODE(self._fd_func, self._startPoint, **self._kwargs)
            prob.timeVariable = self.timeVariable
            prob.times = self.times
            r = prob.solve(solver, **kwargs)
            y_var = list(prob._x0.keys())[0]
            res = 0.5 * (prob.extras[y_var]['infinums'] + prob.extras[y_var]['supremums'])
            times = hstack((prob.extras['startTimes'], prob.extras['endTimes'][-1]))
            if len(self._times) != 2:
                from scipy.interpolate import InterpolatedUnivariateSpline
                if times[-1] < times[0]:
                    times = times[::-1]
                    res = res[::-1]
                interp = InterpolatedUnivariateSpline(times, res, k=1)
                times = self._times
                res = interp(times)
            r.xf = {y_var: res}
            r._xf = {y_var.name: res}
            if self.timeVariable is not None:
                r.xf[self._timeVariable] = times
                r._xf[self._timeVariable.name] = times
        else:
            if solver != 'scipy_lsoda':
                raise FuncDesignerException('incorrect ODE solver')
            try:
                from scipy import integrate
            except ImportError:
                raise FuncDesignerException('to solve ode you mush have scipy installed, see http://openop.org/SciPy')

            y, infodict = integrate.odeint(self.func, self.y0, self.times, Dfun=self.derivative, full_output=True)
            resultDict = dict(self.ooT.vector2point(y.T))
            for key, value in resultDict.items():
                if min(value.shape) == 1:
                    resultDict[key] = value.flatten()

            r = FuncDesigner_ODE_Result(resultDict)
            r.msg = infodict['message']
            r.extras = {'infodict': infodict}
        return r


class FuncDesigner_ODE_Result:

    def __init__(self, resultDict):
        self.xf = resultDict
        if not hasattr(self, '_xf'):
            self._xf = dict([ (var.name, value) for var, value in resultDict.items() ])

    def __call__(self, *args):
        r = [ self._xf[arg] if isinstance(arg, str) else self.xf[arg] for arg in args ]
        if len(args) == 1:
            return r[0]
        return r