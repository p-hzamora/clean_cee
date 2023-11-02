# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\runProbSolver.pyc
# Compiled at: 2012-12-08 11:04:59
__docformat__ = 'restructuredtext en'
from time import time, clock
from numpy import asfarray, nan, ones, all, atleast_1d, any, isnan, array_equal, asscalar, asarray, where, ndarray, isscalar, matrix, seterr, isinf
from setDefaultIterFuncs import stopcase, SMALL_DELTA_X, SMALL_DELTA_F, IS_MAX_ITER_REACHED
from check import check
from oologfcn import OpenOptException
from openopt import __version__ as version
from openopt.kernel.ooMisc import isSolved
from nonOptMisc import getSolverFromStringName, EmptyClass
try:
    import setproctitle
    hasSetproctitleModule = True
except ImportError:
    hasSetproctitleModule = False

ConTolMultiplier = 0.8

def runProbSolver(p_, solver_str_or_instance=None, *args, **kwargs):
    p = p_
    if len(args) != 0:
        p.err('unexpected args for p.solve()')
    if hasattr(p, 'was_involved'):
        p.err("You can't run same prob instance for twice. \n    Please reassign prob struct. \n    You can avoid it via using FuncDesigner oosystem.")
    else:
        p.was_involved = True
    if solver_str_or_instance is None:
        if hasattr(p, 'solver'):
            solver_str_or_instance = p.solver
        elif 'solver' in kwargs.keys():
            solver_str_or_instance = kwargs['solver']
    if type(solver_str_or_instance) is str and ':' in solver_str_or_instance:
        isConverter = True
        probTypeToConvert, solverName = solver_str_or_instance.split(':', 1)
        p.solver = getSolverFromStringName(p, solverName)
        solver_params = {}
    else:
        isConverter = False
        if solver_str_or_instance is None:
            p.err('you should provide name of solver')
        else:
            if type(solver_str_or_instance) is str:
                p.solver = getSolverFromStringName(p, solver_str_or_instance)
            else:
                if not solver_str_or_instance.isInstalled:
                    p.err('\n                solver %s seems to be uninstalled yet, \n                check http://openopt.org/%s for install instructions' % (solver_str_or_instance.__name__, p.probType))
                p.solver = solver_str_or_instance
                for key, value in solver_str_or_instance.fieldsForProbInstance.items():
                    setattr(p, key, value)

        p.isConverterInvolved = isConverter
        old_err = seterr(all='ignore')
        if 'debug' in kwargs.keys():
            p.debug = kwargs['debug']
        probAttributes = set(p.__dict__)
        solverAttributes = set(p.solver.__dict__)
        intersection = list(probAttributes.intersection(solverAttributes))
        if len(intersection) != 0:
            if p.debug:
                p.warn('\n            attribute %s is present in both solver and prob \n            (probably you assigned solver parameter in prob constructor), \n            the attribute will be assigned to solver' % intersection[0])
            for elem in intersection:
                setattr(p.solver, elem, getattr(p, elem))

        solver = p.solver.__solver__
        for key, value in kwargs.items():
            if hasattr(p.solver, key):
                if isConverter:
                    solver_params[key] = value
                else:
                    setattr(p.solver, key, value)
            elif hasattr(p, key):
                setattr(p, key, value)
            else:
                p.warn('incorrect parameter for prob.solve(): "' + str(key) + '" - will be ignored (this one has been not found in neither prob nor ' + p.solver.__name__ + ' solver parameters)')

        if p.probType == 'EIG' and 'goal' in kwargs:
            p.err('for EIG parameter "goal" should be used only in class instance definition, not in "solve" method')
        p.iterValues = EmptyClass()
        p.iterCPUTime = []
        p.iterTime = []
        p.iterValues.x = []
        p.iterValues.f = []
        p.iterValues.r = []
        p.iterValues.rt = []
        p.iterValues.ri = []
        p.solutions = []
        if p._baseClassName == 'NonLin':
            p.iterValues.nNaNs = []
        if p.goal in ('max', 'maximum'):
            p.invertObjFunc = True
        p.advanced = EmptyClass()
        p.istop = 0
        p.iter = 0
        p.graphics.nPointsPlotted = 0
        p.finalIterFcnFinished = False
        p.msg = ''
        if type(p.callback) not in (list, tuple):
            p.callback = [p.callback]
        if hasattr(p, 'xlabel'):
            p.graphics.xlabel = p.xlabel
        if p.graphics.xlabel == 'nf':
            p.iterValues.nf = []
        T = time()
        C = clock()
        p._Prepare()
        T = time() - T
        C = clock() - C
        if T > 1 or C > 1:
            p.disp('Initialization: Time = %0.1f CPUTime = %0.1f' % (T, C))
        for fn in ['FunEvals', 'Iter', 'Time', 'CPUTime']:
            if hasattr(p, 'min' + fn) and hasattr(p, 'max' + fn) and getattr(p, 'max' + fn) < getattr(p, 'min' + fn):
                p.warn('min' + fn + ' (' + str(getattr(p, 'min' + fn)) + ') exceeds ' + 'max' + fn + '(' + str(getattr(p, 'max' + fn)) + '), setting latter to former')
                setattr(p, 'max' + fn, getattr(p, 'min' + fn))

        for fn in ['maxFunEvals', 'maxIter']:
            setattr(p, fn, int(getattr(p, fn)))

        if hasattr(p, 'x0'):
            try:
                p.x0 = atleast_1d(asfarray(p.x0).copy())
            except NotImplementedError:
                p.x0 = asfarray(p.x0.tolist())

        for fn in ['lb', 'ub', 'b', 'beq']:
            if hasattr(p, fn):
                fv = getattr(p, fn)
                if fv is not None:
                    if str(type(fv)) == "<class 'map'>":
                        p.err("Python3 incompatibility with previous versions: you can't use 'map' here, use rendered value instead")
                    setattr(p, fn, asfarray(fv).flatten())
                else:
                    setattr(p, fn, asfarray([]))

        if p.solver._requiresFiniteBoxBounds:
            ind1, ind2 = isinf(p.lb), isinf(p.ub)
            if isscalar(p.implicitBounds):
                p.implicitBounds = (-p.implicitBounds, p.implicitBounds)
            p.lb[ind1] = p.implicitBounds[0] if asarray(p.implicitBounds[0]).size == 1 else p.implicitBounds[0][ind1]
            p.ub[ind2] = p.implicitBounds[1] if asarray(p.implicitBounds[1]).size == 1 else p.implicitBounds[0][ind2]
        p.stopdict = {}
        for s in ['b', 'beq']:
            if hasattr(p, s):
                setattr(p, 'n' + s, len(getattr(p, s)))

    p.isUC = p._isUnconstrained()
    isIterPointAlwaysFeasible = p.solver.__isIterPointAlwaysFeasible__ if type(p.solver.__isIterPointAlwaysFeasible__) == bool else p.solver.__isIterPointAlwaysFeasible__(p)
    if isIterPointAlwaysFeasible:
        if p.data4TextOutput[-1] == 'log10(maxResidual)':
            p.data4TextOutput = p.data4TextOutput[:-1]
    elif p.useScaledResidualOutput:
        p.data4TextOutput[-1] = 'log10(MaxResidual/ConTol)'
    if p.showFeas and p.data4TextOutput[-1] != 'isFeasible':
        p.data4TextOutput.append('isFeasible')
    if p.maxSolutions != 1:
        p._nObtainedSolutions = 0
        p.data4TextOutput.append('nSolutions')
    if not p.solver.iterfcnConnected:
        if SMALL_DELTA_X in p.kernelIterFuncs:
            p.kernelIterFuncs.pop(SMALL_DELTA_X)
        if SMALL_DELTA_F in p.kernelIterFuncs:
            p.kernelIterFuncs.pop(SMALL_DELTA_F)
    if not p.solver._canHandleScipySparse:
        if hasattr(p.A, 'toarray'):
            p.A = p.A.toarray()
        if hasattr(p.Aeq, 'toarray'):
            p.Aeq = p.Aeq.toarray()
    if isinstance(p.A, ndarray) and type(p.A) != ndarray:
        p.A = p.A.A
    if isinstance(p.Aeq, ndarray) and type(p.Aeq) != ndarray:
        p.Aeq = p.Aeq.A
    if hasattr(p, 'optVars'):
        p.err('"optVars" is deprecated, use "freeVars" instead ("optVars" is not appropriate for some prob types, e.g. systems of (non)linear equations)')
    p.primalConTol = p.contol
    if not p.solver.__name__.startswith('interalg'):
        p.contol *= ConTolMultiplier
    p.timeStart = time()
    p.cpuTimeStart = clock()
    if p.probType not in ('MINLP', 'IP'):
        p.plotOnlyCurrentMinimum = p.__isNoMoreThanBoxBounded__()
    if p.iprint >= 0:
        p.disp('\n' + '-' * 25 + ' OpenOpt %s ' % version + '-' * 25)
        pt = p.probType if p.probType != 'NLSP' else 'SNLE'
        s = 'solver: ' + p.solver.__name__ + '   problem: ' + p.name + '    type: %s' % pt
        if p.showGoal:
            s += '   goal: ' + p.goal
        p.disp(s)
    p.extras = {}
    try:
        try:
            if isConverter:
                pass
            else:
                nErr = check(p)
                if nErr:
                    p.err('prob check results: ' + str(nErr) + 'ERRORS!')
                if p.probType not in ('IP', 'EIG'):
                    p.iterfcn(p.x0)
                if hasSetproctitleModule:
                    try:
                        originalName = setproctitle.getproctitle()
                        if originalName.startswith('OpenOpt-'):
                            originalName = None
                        else:
                            s = 'OpenOpt-' + p.solver.__name__
                            s += '-' + p.name
                            setproctitle.setproctitle(s)
                    except:
                        originalName = None

                else:
                    p.pWarn("\n                please install setproctitle module \n                (it's available via easy_install and Linux soft channels like apt-get)")
                solver(p)
                if hasSetproctitleModule and originalName is not None:
                    setproctitle.setproctitle(originalName)
        except isSolved:
            if p.istop == 0:
                p.istop = 1000

    finally:
        seterr(**old_err)

    p.contol = p.primalConTol
    if hasattr(p, '_bestPoint') and not any(isnan(p._bestPoint.x)) and p.probType != 'ODE':
        p.iterfcn(p._bestPoint)
    if p.probType != 'EIG':
        if not hasattr(p, 'xf') and not hasattr(p, 'xk'):
            p.xf = p.xk = ones(p.n) * nan
        if hasattr(p, 'xf') and (not hasattr(p, 'xk') or array_equal(p.xk, p.x0)):
            p.xk = p.xf
        if not hasattr(p, 'xf') or all(isnan(p.xf)):
            p.xf = p.xk
        if p.xf is nan:
            p.xf = p.xk = ones(p.n) * nan
        if p.isFeas(p.xf) and (not p.probType == 'MINLP' or p.discreteConstraintsAreSatisfied(p.xf)):
            p.isFeasible = True
        else:
            p.isFeasible = False
    else:
        p.isFeasible = True
    p.isFinished = True
    if p.probType == 'MOP':
        p.isFeasible = True
    elif p.probType == 'IP':
        p.isFeasible = p.rk < p.ftol
    else:
        p.ff = p.fk = p.objFunc(p.xk)
        if type(p.ff) == ndarray and p.ff.size == 1:
            p.ff = p.fk = asscalar(p.ff)
    if not hasattr(p, 'ff') or any(p.ff == nan):
        p.iterfcn, tmp_iterfcn = lambda *args: None, p.iterfcn
        p.ff = p.fk
        p.iterfcn = tmp_iterfcn
    if p.invertObjFunc:
        p.fk, p.ff = -p.fk, -p.ff
    if asfarray(p.ff).size > 1:
        p.ff = p.objFuncMultiple2Single(p.fk)
    if type(p.xf) in (list, tuple) or isscalar(p.xf):
        p.xf = asarray(p.xf)
    p.xf = p.xf.flatten()
    if not p.probType == 'IP':
        p.rf = p.getMaxResidual(p.xf) if 1 else p.rk
        if not p.isFeasible and p.istop > 0:
            p.istop = -100 - p.istop / 1000.0
        if p.istop == 0 and p.iter >= p.maxIter:
            p.istop, p.msg = IS_MAX_ITER_REACHED, 'Max Iter has been reached'
        p.stopcase = stopcase(p)
        p.xk, p.rk = p.xf, p.rf
        if p.invertObjFunc:
            p.fk = -p.ff
            p.iterfcn(p.xf, -p.ff, p.rf)
        else:
            p.fk = p.ff
            p.iterfcn(p.xf, p.ff, p.rf)
        p.__finalize__()
        p.storeIterPoints or delattr(p.iterValues, 'x')
    r = OpenOptResult(p)
    p.invertObjFunc = False
    if p.isFDmodel:
        p.x0 = p._x0
    finalTextOutput(p, r)
    if not hasattr(p, 'isManagerUsed') or p.isManagerUsed == False:
        finalShow(p)
    return r


def finalTextOutput(p, r):
    if p.iprint >= 0:
        if len(p.msg):
            p.disp('istop: ' + str(r.istop) + ' (' + p.msg + ')')
        else:
            p.disp('istop: ' + str(r.istop))
        p.disp('Solver:   Time Elapsed = ' + str(r.elapsed['solver_time']) + ' \tCPU Time Elapsed = ' + str(r.elapsed['solver_cputime']))
        if p.plot:
            p.disp('Plotting: Time Elapsed = ' + str(r.elapsed['plot_time']) + ' \tCPU Time Elapsed = ' + str(r.elapsed['plot_cputime']))
        if p.probType == 'MOP':
            msg = '%d solutions have been obtained' % len(p.solutions.coords)
            p.disp(msg)
            return
        if p.useScaledResidualOutput:
            rMsg = 'max(residuals/requiredTolerances) = %g' % (r.rf / p.contol)
        else:
            rMsg = 'MaxResidual = %g' % r.rf
        if not p.isFeasible:
            nNaNs = (len(where(isnan(p.c(p.xf)))[0]) if hasattr(p, 'c') else 0) + (len(where(isnan(p.h(p.xf)))[0]) if hasattr(p, 'h') else 0)
            if nNaNs == 0:
                nNaNsMsg = ''
            elif nNaNs == 1:
                nNaNsMsg = '1 constraint is equal to NaN, '
            else:
                nNaNsMsg = '%d constraints are equal to NaN, ' % nNaNs
            p.disp('NO FEASIBLE SOLUTION has been obtained (%s%s, objFunc = %0.8g)' % (nNaNsMsg, rMsg, r.ff))
        else:
            if p.maxSolutions == 1:
                msg = 'objFunValue: ' + p.finalObjFunTextFormat % r.ff
                if not p.isUC:
                    msg += ' (feasible, %s)' % rMsg
            else:
                msg = '%d solutions have been obtained' % len(p.solutions)
            p.disp(msg)


def finalShow(p):
    if not p.plot:
        return
    pylab = __import__('pylab')
    pylab.ioff()
    if p.show:
        pylab.show()


class OpenOptResult():

    def __call__(self, *args):
        if not self.isFDmodel:
            raise OpenOptException('Is callable for FuncDesigner models only')
        r = []
        for arg in args:
            tmp = [ self._xf[elem] if isinstance(elem, str) else self.xf[elem] for elem in arg.tolist() if isinstance(arg, ndarray) else arg if type(arg) in (tuple, list) else [arg] ]
            tmp = [ asscalar(item) if type(item) in (ndarray, matrix) and item.size == 1 else item for item in tmp ]
            r.append(tmp if type(tmp) not in (list, tuple) or len(tmp) != 1 else tmp[0])

        r = r[0] if len(args) == 1 else r
        if len(args) == 1 and type(r) in (list, tuple) and len(r) > 1:
            r = asfarray(r, dtype=type(r[0]))
        return r

    def __init__(self, p):
        self.rf = asscalar(asarray(p.rf))
        self.ff = asscalar(asarray(p.ff))
        self.isFDmodel = p.isFDmodel
        self.probType = p.probType
        if p.probType == 'EIG':
            self.eigenvalues, self.eigenvectors = p.eigenvalues, p.eigenvectors
        if p.isFDmodel:
            from FuncDesigner import oopoint
            self.xf = dict([ (v, asscalar(val) if isinstance(val, ndarray) and val.size == 1 else v.aux_domain[val] if 'aux_domain' in v.__dict__ else val) for v, val in p.xf.items() ])
            if not hasattr(self, '_xf'):
                self._xf = dict([ (v.name, val) for v, val in self.xf.items() ])
            self.xf = oopoint(self.xf, maxDistributionSize=p.maxDistributionSize)
        else:
            self.xf = p.xf
        self.elapsed = dict()
        self.elapsed['solver_time'] = round(100.0 * (time() - p.timeStart)) / 100.0
        self.elapsed['solver_cputime'] = round(100.0 * (clock() - p.cpuTimeStart)) / 100.0
        for fn in ('ff', 'istop', 'duals', 'isFeasible', 'msg', 'stopcase', 'iterValues',
                   'special', 'extras', 'solutions'):
            if hasattr(p, fn):
                setattr(self, fn, getattr(p, fn))

        if hasattr(p.solver, 'innerState'):
            self.extras['innerState'] = p.solver.innerState
        self.solverInfo = dict()
        for fn in ('homepage', 'alg', 'authors', 'license', 'info', 'name'):
            self.solverInfo[fn] = getattr(p.solver, '__' + fn + '__')

        if p.plot:
            self.elapsed['plot_time'] = round(100 * p.timeElapsedForPlotting[-1]) / 100
            self.elapsed['plot_cputime'] = p.cpuTimeElapsedForPlotting[-1]
        else:
            self.elapsed['plot_time'] = 0
            self.elapsed['plot_cputime'] = 0
        self.elapsed['solver_time'] -= self.elapsed['plot_time']
        self.elapsed['solver_cputime'] -= self.elapsed['plot_cputime']
        self.evals = dict([ (key, val if type(val) == int else round(val * 10) / 10.0) for key, val in p.nEvals.items() ])
        self.evals['iter'] = p.iter