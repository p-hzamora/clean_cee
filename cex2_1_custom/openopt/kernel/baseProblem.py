# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\baseProblem.pyc
# Compiled at: 2012-12-08 11:04:59
__docformat__ = 'restructuredtext en'
from .numpy import *
from .oologfcn import *
from oographics import Graphics
from setDefaultIterFuncs import setDefaultIterFuncs, denyingStopFuncs
from nonLinFuncs import nonLinFuncs
from residuals import residuals
from ooIter import ooIter
from openopt.kernel.Point import Point
from iterPrint import ooTextOutput
from ooMisc import setNonLinFuncsNumber, assignScript, norm
from nonOptMisc import isspmatrix, scipyInstalled, scipyAbsentMsg, csr_matrix, Vstack, Hstack, EmptyClass, isPyPy, oosolver
from copy import copy as Copy
try:
    from DerApproximator import check_d1
    DerApproximatorIsInstalled = True
except:
    DerApproximatorIsInstalled = False

ProbDefaults = {'diffInt': 1.5e-08, 'xtol': 1e-06, 'noise': 0}
from runProbSolver import runProbSolver
import GUI
from fdmisc import setStartVectorAndTranslators

class user():

    def __init__(self):
        pass


class oomatrix():

    def __init__(self):
        pass

    def matMultVec(self, x, y):
        if not isspmatrix(x):
            return dot(x, y)
        return x._mul_sparse_matrix(csr_matrix(y.reshape((y.size, 1)))).A.flatten()

    def matmult(self, x, y):
        return dot(x, y)

    def dotmult(self, x, y):
        return x * y


class autocreate():

    def __init__(self):
        pass


class baseProblem(oomatrix, residuals, ooTextOutput):
    isObjFunValueASingleNumber = True
    manage = GUI.manage
    prepared = False
    _baseProblemIsPrepared = False
    name = 'unnamed'
    state = 'init'
    castFrom = ''
    nonStopMsg = ''
    xlabel = 'time'
    plot = False
    show = True
    iter = 0
    cpuTimeElapsed = 0.0
    TimeElapsed = 0.0
    isFinished = False
    invertObjFunc = False
    nProc = 1
    lastPrintedIter = -1
    iterObjFunTextFormat = '%0.3e'
    finalObjFunTextFormat = '%0.8g'
    debug = 0
    iprint = 10
    maxDistributionSize = 0
    maxIter = 1000
    maxFunEvals = 10000
    maxCPUTime = inf
    maxTime = inf
    maxLineSearch = 500
    xtol = ProbDefaults['xtol']
    gtol = 1e-06
    ftol = 1e-06
    contol = 1e-06
    fTol = None
    minIter = 0
    minFunEvals = 0
    minCPUTime = 0.0
    minTime = 0.0
    storeIterPoints = False
    userStop = False
    useSparse = 'auto'
    useAttachedConstraints = False
    x0 = None
    isFDmodel = False
    noise = ProbDefaults['noise']
    showFeas = False
    useScaledResidualOutput = False
    hasLogicalConstraints = False
    A = None
    b = None
    Aeq = None
    beq = None
    scale = None
    goal = None
    showGoal = False
    color = 'b'
    specifier = '-'
    plotOnlyCurrentMinimum = False
    xlim = (nan, nan)
    ylim = (nan, nan)
    legend = ''
    fixedVars = None
    freeVars = None
    istop = 0
    maxSolutions = 1
    fEnough = -inf
    fOpt = None
    implicitBounds = inf
    convex = 'unknown'
    _linear_objective = False

    def __init__(self, *args, **kwargs):
        self.err = ooerr
        self.warn = oowarn
        self.info = ooinfo
        self.hint = oohint
        self.pWarn = ooPWarn
        self.disp = oodisp
        self.data4TextOutput = ['objFunVal', 'log10(maxResidual)']
        self.nEvals = {}
        if hasattr(self, 'expectedArgs'):
            if len(self.expectedArgs) < len(args):
                self.err('Too much arguments for ' + self.probType + ': ' + str(len(args)) + ' are got, at most ' + str(len(self.expectedArgs)) + ' were expected')
            for i, arg in enumerate(args):
                setattr(self, self.expectedArgs[i], arg)

        self.norm = norm
        self.denyingStopFuncs = denyingStopFuncs()
        self.iterfcn = lambda *args, **kwargs: ooIter(self, *args, **kwargs)
        self.graphics = Graphics()
        self.user = user()
        self.F = lambda x: self.objFuncMultiple2Single(self.objFunc(x))
        self.point = lambda *args, **kwargs: Point(self, *args, **kwargs)
        self.timeElapsedForPlotting = [
         0.0]
        self.cpuTimeElapsedForPlotting = [0.0]
        self.debugmsg = lambda msg: oodebugmsg(self, msg)
        self.constraints = []
        self.callback = []
        self.solverParams = autocreate()
        self.userProvided = autocreate()
        self.special = autocreate()
        self.intVars = []
        self.binVars = []
        self.optionalData = []
        if self.allowedGoals is not None:
            if 'min' in self.allowedGoals:
                self.minimize = lambda *args, **kwargs: minimize(self, *args, **kwargs)
            if 'max' in self.allowedGoals:
                self.maximize = lambda *args, **kwargs: maximize(self, *args, **kwargs)
        assignScript(self, kwargs)
        return

    def __finalize__(self):
        if self.isFDmodel:
            self.xf = self._vector2point(self.xf)

    def objFunc(self, x):
        return self.f(x)

    def __isFiniteBoxBounded__(self):
        return all(isfinite(self.ub)) and all(isfinite(self.lb))

    def __isNoMoreThanBoxBounded__(self):
        return self.b.size == 0 and self.beq.size == 0 and (self._baseClassName == 'Matrix' or not self.userProvided.c and not self.userProvided.h)

    def solve(self, *args, **kwargs):
        return runProbSolver(self, *args, **kwargs)

    def _solve(self, *args, **kwargs):
        self.debug = True
        return self.solve(*args, **kwargs)

    def objFuncMultiple2Single(self, f):
        if asfarray(f).size != 1:
            self.err('unexpected f size. The function should be redefined in OO child class, inform OO developers')
        return f

    def inspire(self, newProb, sameConstraints=True):
        newProb.castFrom = self.probType
        fieldsToAssert = [
         'contol', 'xtol', 'ftol', 'gtol', 'iprint', 'maxIter', 
         'maxTime', 'maxCPUTime', 'fEnough', 'goal', 'color', 'debug', 
         'maxFunEvals', 'xlabel']
        if sameConstraints:
            fieldsToAssert += ['lb', 'ub', 'A', 'Aeq', 'b', 'beq']
        for key in fieldsToAssert:
            if hasattr(self, key):
                setattr(newProb, key, getattr(self, key))

        Arr = [
         'f', 'df']
        if sameConstraints:
            Arr += ['c', 'dc', 'h', 'dh', 'd2c', 'd2h']
        for key in Arr:
            if hasattr(self.userProvided, key):
                if getattr(self.userProvided, key):
                    setattr(newProb, key, getattr(self, key)) if self.isFDmodel else setattr(newProb, key, getattr(self.user, key))
                else:
                    setattr(newProb, key, None)

        return

    FuncDesignerSign = 'f'

    def _isFDmodel(self):
        try:
            from FuncDesigner import ooarray, oofun
        except ImportError:
            return False

        fds = getattr(self, self.FuncDesignerSign, None)
        if fds is None:
            return False
        else:
            if isinstance(fds, (oofun, ooarray)):
                return True
            if isinstance(fds, (list, tuple, ndarray)):
                if isinstance(fds[0], (oofun, ooarray)):
                    return True
                if isinstance(fds[0], (list, tuple, ndarray)):
                    return isinstance(fds[0][0], (oofun, ooarray))
            return False

    def _prepare(self):
        if self._baseProblemIsPrepared:
            return
        if self.useSparse == 0:
            self.useSparse = False
        elif self.useSparse == 1:
            self.useSparse = True
        if self.useSparse == 'auto' and not scipyInstalled:
            self.useSparse = False
        if self.useSparse == True and not scipyInstalled:
            self.err("You can't set useSparse=True without scipy installed")
        if self._isFDmodel():
            self.isFDmodel = True
            self._FD = EmptyClass()
            self._FD.nonBoxConsWithTolShift = []
            self._FD.nonBoxCons = []
            from FuncDesigner import _getAllAttachedConstraints, _getDiffVarsID, ooarray, oopoint, oofun
            self._FDVarsID = _getDiffVarsID()
            probDep = set()
            updateDep = --- This code section failed: ---

 L. 324         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             1  'elem'
                6  LOAD_GLOBAL           1  'tuple'
                9  LOAD_GLOBAL           2  'list'
               12  LOAD_GLOBAL           3  'set'
               15  LOAD_GLOBAL           4  'ndarray'
               18  BUILD_TUPLE_4         4 
               21  CALL_FUNCTION_2       2  None
               24  POP_JUMP_IF_FALSE    59  'to 59'
               27  BUILD_LIST_0          0 
               30  LOAD_FAST             1  'elem'
               33  GET_ITER         
               34  FOR_ITER             59  'to 96'
               37  STORE_FAST            2  'f'
               40  LOAD_DEREF            0  'updateDep'
               43  LOAD_FAST             0  'Dep'
               46  LOAD_FAST             2  'f'
               49  CALL_FUNCTION_2       2  None
               52  LIST_APPEND           2  None
               55  JUMP_BACK            34  'to 34'
               58  RETURN_END_IF_LAMBDA
             59_0  COME_FROM            24  '24'

 L. 325        59  LOAD_GLOBAL           0  'isinstance'
               62  LOAD_FAST             1  'elem'
               65  LOAD_DEREF            1  'oofun'
               68  CALL_FUNCTION_2       2  None
               71  POP_JUMP_IF_FALSE    93  'to 93'
               74  LOAD_FAST             0  'Dep'
               77  LOAD_ATTR             5  'update'
               80  LOAD_FAST             1  'elem'
               83  LOAD_ATTR             6  '_getDep'
               86  CALL_FUNCTION_0       0  None
               89  CALL_FUNCTION_1       1  None
               92  RETURN_END_IF_LAMBDA
             93_0  COME_FROM            71  '71'
               93  LOAD_CONST               None
               96  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 92
            if self.probType in ('SLE', 'NLSP', 'SNLE', 'LLSP'):
                equations = self.C if self.probType in ('SLE', 'LLSP') else self.f
                F = equations
                updateDep(probDep, equations)
                ConstraintTags = [ (elem if not isinstance(elem, (list, tuple, ndarray)) else elem[0]).isConstraint for elem in equations ]
                cond_all_oofuns_but_not_cons = not any(ConstraintTags)
                cond_cons = all(ConstraintTags)
                if not cond_all_oofuns_but_not_cons and not cond_cons:
                    raise OpenOptException('for FuncDesigner SLE/SNLE constructors args must be either all-equalities or all-oofuns')
                if self.fTol is not None:
                    fTol = min((self.ftol, self.fTol))
                    self.warn('\n                    both ftol and fTol are passed to the SNLE;\n                    minimal value of the pair will be used (%0.1e);\n                    also, you can modify each personal tolerance for equation, e.g. \n                    equations = [(sin(x)+cos(y)=-0.5)(tol = 0.001), ...]\n                    ' % fTol)
                else:
                    fTol = self.ftol
                self.fTol = self.ftol = fTol
                appender = --- This code section failed: ---

 L. 347         0  LOAD_GLOBAL           0  'isinstance'
                3  LOAD_FAST             0  'arg'
                6  LOAD_GLOBAL           1  'ndarray'
                9  LOAD_GLOBAL           2  'list'
               12  LOAD_GLOBAL           3  'tuple'
               15  LOAD_GLOBAL           4  'set'
               18  BUILD_TUPLE_4         4 
               21  CALL_FUNCTION_2       2  None
               24  POP_JUMP_IF_FALSE    56  'to 56'
               27  BUILD_LIST_0          0 
               30  LOAD_FAST             0  'arg'
               33  GET_ITER         
               34  FOR_ITER             73  'to 110'
               37  STORE_FAST            1  'elem'
               40  LOAD_DEREF            0  'appender'
               43  LOAD_FAST             1  'elem'
               46  CALL_FUNCTION_1       1  None
               49  LIST_APPEND           2  None
               52  JUMP_BACK            34  'to 34'
               55  RETURN_END_IF_LAMBDA
             56_0  COME_FROM            24  '24'

 L. 348        56  LOAD_FAST             0  'arg'
               59  LOAD_ATTR             5  'isConstraint'
               62  POP_JUMP_IF_FALSE   107  'to 107'
               65  LOAD_FAST             0  'arg'
               68  LOAD_ATTR             6  'tol'
               71  LOAD_CONST               0
               74  COMPARE_OP            3  !=
               77  POP_JUMP_IF_FALSE   100  'to 100'
               80  LOAD_FAST             0  'arg'
               83  LOAD_ATTR             7  'oofun'
               86  LOAD_DEREF            1  'fTol'
               89  LOAD_FAST             0  'arg'
               92  LOAD_ATTR             6  'tol'
               95  BINARY_DIVIDE    
               96  BINARY_MULTIPLY  
               97  JUMP_ABSOLUTE       110  'to 110'
              100  LOAD_FAST             0  'arg'
              103  LOAD_ATTR             7  'oofun'
              106  RETURN_END_IF_LAMBDA
            107_0  COME_FROM            62  '62'
              107  LOAD_FAST             0  'arg'
              110  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `RETURN_END_IF_LAMBDA' instruction at offset 106
                EQs = []
                for eq in equations:
                    rr = appender(eq)
                    if type(rr) == list:
                        EQs += rr
                    else:
                        EQs.append(rr)

                if self.probType in ('SLE', 'LLSP'):
                    self.C = EQs
                else:
                    if self.probType in ('NLSP', 'SNLE'):
                        self.f = EQs
                    else:
                        raise OpenOptException('bug in OO kernel')
            else:
                F = [
                 self.f]
                updateDep(probDep, self.f)
            updateDep(probDep, self.constraints)
            for fn in ['lb', 'ub', 'A', 'Aeq', 'b', 'beq']:
                if not hasattr(self, fn):
                    continue
                val = getattr(self, fn)
                if val is not None and any(isfinite(val)):
                    self.err('while using oovars providing lb, ub, A, Aeq for whole prob is forbidden, use for each oovar instead')

            if not isinstance(self.x0, dict):
                self.err('Unexpected start point type: ooPoint or Python dict expected, ' + str(type(self.x0)) + ' obtained')
            x0 = self.x0.copy()
            tmp = []
            for key, val in x0.items():
                if not isinstance(key, (list, tuple, ndarray)):
                    tmp.append((key, val))
                else:
                    val = atleast_1d(val)
                    if len(key) != val.size:
                        self.err('\n                        for the sake of possible bugs prevention lenght of oovars array \n                        must be equal to lenght of its start point value, \n                        assignments like x = oovars(m); startPoint[x] = 0 are forbidden, \n                        use startPoint[x] = [0]*m or np.zeros(m) instead')
                    for i in range(val.size):
                        tmp.append((key[i], val[i]))

            Tmp = dict(tmp)
            if isinstance(self.fixedVars, dict):
                for key, val in self.fixedVars.items():
                    if isinstance(key, (list, tuple, ndarray)):
                        if len(key) != len(val):
                            self.err('\n                            for the sake of possible bugs prevention lenght of oovars array \n                            must be equal to lenght of its start point value, \n                            assignments like x = oovars(m); fixedVars[x] = 0 are forbidden, \n                            use fixedVars[x] = [0]*m or np.zeros(m) instead')
                        for i in range(len(val)):
                            Tmp[key[i]] = val[i]

                    else:
                        Tmp[key] = val

                self.fixedVars = set(self.fixedVars.keys())
            if self.probType != 'ODE':
                Keys = set(Tmp.keys()).difference(probDep)
                for key in Keys:
                    Tmp.pop(key)

            self.x0 = Tmp
            self._categoricalVars = set()
            for key, val in self.x0.items():
                if type(val) in (str, string_):
                    self._categoricalVars.add(key)
                    key.formAuxDomain()
                    self.x0[key] = searchsorted(key.aux_domain, val, 'left')
                elif key.domain is not None and key.domain is not bool and key.domain is not 'bool' and key.domain is not int and val not in key.domain:
                    self.x0[key] = key.domain[0]

            self.x0 = oopoint(self.x0)
            self.x0.maxDistributionSize = self.maxDistributionSize
            if self.probType in ('LP', 'MILP') and self.f.getOrder(self.freeVars, self.fixedVars) > 1:
                self.err('for LP/MILP objective function has to be linear, while this one ("%s") is not' % self.f.name)
            setStartVectorAndTranslators(self)
            self.vectorizable = all([ asarray(self._x0[v]).size == 1 for v in self._freeVarsList ])
            if self.fixedVars is None or self.freeVars is not None and len(self.freeVars) < len(self.fixedVars):
                D_kwargs = {'Vars': self.freeVars}
            else:
                D_kwargs = {'fixedVars': self.fixedVars}
            D_kwargs['useSparse'] = self.useSparse
            D_kwargs['fixedVarsScheduleID'] = self._FDVarsID
            D_kwargs['exactShape'] = True
            self._D_kwargs = D_kwargs
            variableTolerancesDict = dict([ (v, v.tol) for v in self._freeVars ])
            self.variableTolerances = self._point2vector(variableTolerancesDict)
            if len(self._fixedVars) < len(self._freeVars) and 'isdisjoint' in dir(set()):
                areFixed = lambda dep: dep.issubset(self._fixedVars)
                Z = dict([ (v, zeros_like(self._x0[v]) if v not in self._fixedVars else self._x0[v]) for v in self._x0.keys() ])
            else:
                areFixed = lambda dep: dep.isdisjoint(self._freeVars)
                Z = dict([ (v, zeros_like(self._x0[v]) if v in self._freeVars else self._x0[v]) for v in self._x0.keys() ])
            Z = oopoint(Z, maxDistributionSize=self.maxDistributionSize)
            lb, ub = -inf * ones(self.n), inf * ones(self.n)
            A, b, Aeq, beq = ([], [], [], [])
            if type(self.constraints) not in (list, tuple, set):
                self.constraints = [
                 self.constraints]
            oovD = self._oovarsIndDict
            LB = {}
            UB = {}
            C = list(self.constraints)
            self.constraints = set(self.constraints)
            for v in self._x0.keys():
                if not array_equal(v.lb, -inf):
                    self.constraints.add(v >= v.lb)
                if not array_equal(v.ub, inf):
                    self.constraints.add(v <= v.ub)

            if hasattr(self, 'f'):
                if type(self.f) in [list, tuple, set]:
                    C += list(self.f)
                else:
                    C.append(self.f)
            if self.useAttachedConstraints:
                self.constraints.update(_getAllAttachedConstraints(C))
            FF = self.constraints.copy()
            for _F in F:
                if isinstance(_F, (tuple, list, ndarray, set)):
                    FF.update(_F)
                else:
                    FF.add(_F)

            unvectorizableFuncs = set()
            unvectorizableVariables = set([])
            cond = False
            if 1 and isPyPy:
                hasVectorizableFuncs = False
                unvectorizableFuncs = FF
            else:
                hasVectorizableFuncs = False
                if len(unvectorizableVariables) != 0:
                    for ff in FF:
                        _dep = ff._getDep()
                        if cond or len(_dep & unvectorizableVariables) != 0:
                            unvectorizableFuncs.add(ff)
                        else:
                            hasVectorizableFuncs = True

                else:
                    hasVectorizableFuncs = True
            self.unvectorizableFuncs = unvectorizableFuncs
            self.hasVectorizableFuncs = hasVectorizableFuncs
            for v in self._freeVars:
                d = v.domain
                if d is bool or d is 'bool':
                    self.constraints.update([v > 0, v < 1])
                elif d is not None and d is not int and d is not 'int':
                    v.domain = array(list(d))
                    v.domain.sort()
                    self.constraints.update([v >= v.domain[0], v <= v.domain[-1]])
                    if hasattr(v, 'aux_domain'):
                        self.constraints.add(v - (len(v.aux_domain) - 1) <= 0)

            StartPointVars = set(self._x0.keys())
            self.dictOfFixedFuncs = {}
            from FuncDesigner import broadcast
            if self.probType in ('SLE', 'NLSP', 'SNLE', 'LLSP'):
                for eq in equations:
                    broadcast(formDictOfFixedFuncs, eq, self.useAttachedConstraints, self.dictOfFixedFuncs, areFixed, self._x0)

            else:
                broadcast(formDictOfFixedFuncs, self.f, self.useAttachedConstraints, self.dictOfFixedFuncs, areFixed, self._x0)
            if oosolver(self.solver).useLinePoints:
                self._firstLinePointDict = {}
                self._secondLinePointDict = {}
                self._currLinePointDict = {}
            inplaceLinearRender = oosolver(self.solver).__name__ == 'interalg'
            if inplaceLinearRender and hasattr(self, 'f'):
                D_kwargs2 = D_kwargs.copy()
                D_kwargs2['useSparse'] = False
                if type(self.f) in [list, tuple, set]:
                    ff = []
                    for f in self.f:
                        if f.getOrder(self.freeVars, self.fixedVars) < 2:
                            D = f.D(Z, **D_kwargs2)
                            f2 = linear_render(f, D, Z)
                            ff.append(f2)
                        else:
                            ff.append(f)

                    self.f = ff
                elif self.f.getOrder(self.freeVars, self.fixedVars) < 2:
                    D = self.f.D(Z, **D_kwargs2)
                    self.f = linear_render(self.f, D, Z)
                    if self.isObjFunValueASingleNumber:
                        self._linear_objective = True
                        self._linear_objective_factor = self._pointDerivative2array(D).flatten()
                        self._linear_objective_scalar = self.f(Z)
            handleConstraint_args = (
             StartPointVars, areFixed, oovD, A, b, Aeq, beq, Z, D_kwargs, LB, UB, inplaceLinearRender)
            for c in self.constraints:
                if isinstance(c, ooarray):
                    for elem in c:
                        self.handleConstraint(elem, *handleConstraint_args)

                elif c is True:
                    continue
                elif c is False:
                    self.err('one of elements from constraints is "False", solution is impossible')
                elif not hasattr(c, 'isConstraint'):
                    self.err('The type ' + str(type(c)) + ' is inappropriate for problem constraints')
                else:
                    self.handleConstraint(c, *handleConstraint_args)

            if len(b) != 0:
                self.A, self.b = Vstack(A), Hstack(b)
                if hasattr(self.b, 'toarray'):
                    self.b = self.b.toarray()
            if len(beq) != 0:
                self.Aeq, self.beq = Vstack(Aeq), Hstack(beq)
                if hasattr(self.beq, 'toarray'):
                    self.beq = self.beq.toarray()
            for vName, vVal in LB.items():
                inds = oovD[vName]
                lb[(inds[0]):(inds[1])] = vVal

            for vName, vVal in UB.items():
                inds = oovD[vName]
                ub[(inds[0]):(inds[1])] = vVal

            self.lb, self.ub = lb, ub
        else:
            if self.fixedVars is not None or self.freeVars is not None:
                self.err('fixedVars and freeVars are valid for optimization of FuncDesigner models only')
            if self.x0 is None:
                arr = [
                 'lb', 'ub']
                if self.probType in ('LP', 'MILP', 'QP', 'SOCP', 'SDP'):
                    arr.append('f')
                if self.probType in ('LLSP', 'LLAVP', 'LUNP'):
                    arr.append('D')
                for fn in arr:
                    if not hasattr(self, fn):
                        continue
                    fv = asarray(getattr(self, fn))
                    if any(isfinite(fv)):
                        self.x0 = zeros(fv.size)
                        break

            self.x0 = ravel(self.x0)
            if not hasattr(self, 'n'):
                self.n = self.x0.size
            if not hasattr(self, 'lb'):
                self.lb = -inf * ones(self.n)
            if not hasattr(self, 'ub'):
                self.ub = inf * ones(self.n)
            for fn in ('A', 'Aeq'):
                fv = getattr(self, fn)
                if fv is not None:
                    afv = asfarray(fv) if type(fv) in [list, tuple] else fv
                    if len(afv.shape) > 1:
                        if afv.shape[1] != self.n:
                            self.err('incorrect ' + fn + ' size')
                    elif afv.shape != () and afv.shape[0] == self.n:
                        afv = afv.reshape(1, self.n)
                    setattr(self, fn, afv)
                else:
                    setattr(self, fn, asfarray([]).reshape(0, self.n))

        nA, nAeq = prod(self.A.shape), prod(self.Aeq.shape)
        SizeThreshold = 32768
        if scipyInstalled:
            from scipy.sparse import csc_matrix
            if isspmatrix(self.A) or nA > SizeThreshold and flatnonzero(self.A).size < 0.25 * nA:
                self._A = csc_matrix(self.A)
            if isspmatrix(self.Aeq) or nAeq > SizeThreshold and flatnonzero(self.Aeq).size < 0.25 * nAeq:
                self._Aeq = csc_matrix(self.Aeq)
        elif nA > SizeThreshold or nAeq > SizeThreshold:
            self.pWarn(scipyAbsentMsg)
        self._baseProblemIsPrepared = True
        return

    def handleConstraint(self, c, StartPointVars, areFixed, oovD, A, b, Aeq, beq, Z, D_kwargs, LB, UB, inplaceLinearRender):
        from FuncDesigner.ooFun import SmoothFDConstraint, BooleanOOFun
        if not isinstance(c, SmoothFDConstraint) and isinstance(c, BooleanOOFun):
            self.hasLogicalConstraints = True
        probtol = self.contol
        f, tol = c.oofun, c.tol
        _lb, _ub = c.lb, c.ub
        lb_0, ub_0 = copy(_lb), copy(_ub)
        Name = f.name
        dep = set([f]) if f.is_oovar else f._getDep()
        isFixed = areFixed(dep)
        if f.is_oovar and isFixed:
            if self._x0 is None or f not in self._x0:
                self.err('your problem has fixed oovar ' + Name + ' but no value for the one in start point is provided')
            return True
        if not dep.issubset(StartPointVars):
            self.err('your start point has no enough variables to define constraint ' + c.name)
        if tol < 0:
            if any(_lb == _ub):
                self.err("You can't use negative tolerance for the equality constraint " + c.name)
            elif any(_lb - tol >= _ub + tol):
                self.err("You can't use negative tolerance for so small gap in constraint" + c.name)
            Shift = 1.0000000000001 * probtol
            _lb = _lb + Shift
            _ub = _ub - Shift
        if tol != 0:
            self.useScaledResidualOutput = True
        if tol not in (0, probtol, -probtol):
            scaleFactor = abs(probtol / tol)
            f *= scaleFactor
            _lb, _ub = _lb * scaleFactor, _ub * scaleFactor
            Contol = tol
            Contol2 = Contol * scaleFactor
        else:
            Contol = asscalar(copy(probtol))
            Contol2 = Contol
        if isFixed:
            if not c(self._x0, tol=Contol2):
                s = '\'constraint "%s" with all-fixed optimization variables it depends on is infeasible in start point, \n                hence the problem is infeasible, maybe you should change start point\'' % c.name
                self.err(s)
            return True
        from FuncDesigner import broadcast
        broadcast(formDictOfFixedFuncs, f, self.useAttachedConstraints, self.dictOfFixedFuncs, areFixed, self._x0)
        f_order = f.getOrder(self.freeVars, self.fixedVars)
        if self.probType in ('LP', 'MILP', 'LLSP', 'LLAVP') and f_order > 1:
            self.err('for LP/MILP/LLSP/LLAVP all constraints have to be linear, while ' + f.name + ' is not')
        if not f.is_oovar and f_order < 2:
            D_kwargs2 = D_kwargs.copy()
            D_kwargs2['useSparse'] = False
            D = f.D(Z, **D_kwargs2)
            if inplaceLinearRender:
                if any([ asarray(val).size > 1 for val in D.values() ]):
                    self.err('currently interalg can handle only FuncDesigner.oovars(n), not FuncDesigner.oovar() with size > 1')
                f = linear_render(f, D, Z)
        else:
            D = 0
        if f.is_oovar:
            inds = oovD[f]
            f_size = inds[1] - inds[0]
            if any(isfinite(_lb)):
                if _lb.size not in (f_size, 1):
                    self.err('incorrect size of lower box-bound constraint for %s: 1 or %d expected, %d obtained' % (Name, f_size, _lb.size))
                if type(_lb) == ndarray and _lb.size == 1:
                    _lb = _lb.item()
                val = array(f_size * [_lb] if type(_lb) == ndarray and _lb.size < f_size else _lb)
                if f not in LB:
                    LB[f] = val
                else:
                    if val.size > 1 or LB[f].size > 1:
                        LB[f][val > LB[f]] = val[val > LB[f]] if val.size > 1 else asscalar(val)
                    else:
                        LB[f] = max((val, LB[f]))
            if any(isfinite(_ub)):
                if _ub.size not in (f_size, 1):
                    self.err('incorrect size of upper box-bound constraint for %s: 1 or %d expected, %d obtained' % (Name, f_size, _ub.size))
                if type(_ub) == ndarray and _ub.size == 1:
                    _ub = _ub.item()
                val = array(f_size * [_ub] if type(_ub) == ndarray and _ub.size < f_size else _ub)
                if f not in UB:
                    UB[f] = val
                else:
                    if val.size > 1 or UB[f].size > 1:
                        UB[f][val < UB[f]] = val[val < UB[f]] if val.size > 1 else asscalar(val)
                    else:
                        UB[f] = min((val, UB[f]))
        elif _lb == _ub:
            if f_order < 2:
                Aeq.append(self._pointDerivative2array(D))
                beq.append(-f(Z) + _lb)
            else:
                if self.h is None:
                    self.h = [f - _lb]
                else:
                    self.h.append(f - _lb)
        elif isfinite(_ub):
            if f_order < 2:
                A.append(self._pointDerivative2array(D))
                b.append(-f(Z) + _ub)
            else:
                if self.c is None:
                    self.c = [f - _ub]
                else:
                    self.c.append(f - _ub)
        elif isfinite(_lb):
            if f_order < 2:
                A.append(-self._pointDerivative2array(D))
                b.append(f(Z) - _lb)
            else:
                if self.c is None:
                    self.c = [-f + _lb]
                else:
                    self.c.append(-f + _lb)
        else:
            self.err('inform OpenOpt developers of the bug')
        if not f.is_oovar:
            Contol = max((0, Contol2))
            self._FD.nonBoxConsWithTolShift.append((c, f, _lb - Contol, _ub + Contol))
            self._FD.nonBoxCons.append((c, f, _lb, _ub, Contol))
        return False


def formDictOfFixedFuncs(oof, dictOfFixedFuncs, areFixed, startPoint):
    dep = set([oof]) if oof.is_oovar else oof._getDep()
    if areFixed(dep):
        dictOfFixedFuncs[oof] = oof(startPoint)


class MatrixProblem(baseProblem):
    _baseClassName = 'Matrix'
    ftol = 1e-08
    contol = 1e-08
    Awhole = None
    bwhole = None
    dwhole = None

    def __init__(self, *args, **kwargs):
        baseProblem.__init__(self, *args, **kwargs)
        self.kernelIterFuncs = setDefaultIterFuncs('Matrix')

    def _Prepare(self):
        if self.prepared == True:
            return
        baseProblem._prepare(self)
        self.prepared = True

    def _isUnconstrained(self):
        if self.b.size != 0 or self.beq.size != 0:
            return False
        if any(atleast_1d(self.lb) != -inf) or any(atleast_1d(self.ub) != inf):
            return False
        return True


class Parallel():

    def __init__(self):
        self.f = False
        self.c = False
        self.h = False


class Args():

    def __init__(self):
        pass

    f, c, h = (), (), ()


class NonLinProblem(baseProblem, nonLinFuncs, Args):
    _baseClassName = 'NonLin'
    diffInt = ProbDefaults['diffInt']
    c = None
    h = None
    maxViolation = 0.01
    JacobianApproximationStencil = 1

    def __init__(self, *args, **kwargs):
        baseProblem.__init__(self, *args, **kwargs)
        if not hasattr(self, 'args'):
            self.args = Args()
        self.prevVal = {}
        for fn in ['f', 'c', 'h', 'df', 'dc', 'dh', 'd2f', 'd2c', 'd2h']:
            self.prevVal[fn] = {'key': None, 'val': None}

        self.functype = {}
        self.kernelIterFuncs = setDefaultIterFuncs('NonLin')
        return

    def checkdf(self, *args, **kwargs):
        return self.checkGradient('df', *args, **kwargs)

    def checkdc(self, *args, **kwargs):
        return self.checkGradient('dc', *args, **kwargs)

    def checkdh(self, *args, **kwargs):
        return self.checkGradient('dh', *args, **kwargs)

    def checkGradient(self, funcType, *args, **kwargs):
        self._Prepare()
        if not DerApproximatorIsInstalled:
            self.err('To perform gradients check you should have DerApproximator installed, see http://openopt.org/DerApproximator')
        if not getattr(self.userProvided, funcType):
            self.warn("you haven't analitical gradient provided for " + funcType[1:] + ', turning derivatives check for it off...')
            return
        if len(args) > 0:
            if len(args) > 1 or 'x' in kwargs:
                self.err('checkd<func> funcs can have single argument x only (then x should be absent in kwargs )')
            xCheck = asfarray(args[0])
        elif 'x' in kwargs:
            xCheck = asfarray(kwargs['x'])
        else:
            xCheck = asfarray(self.x0)
        maxViolation = 0.01
        if 'maxViolation' in kwargs:
            maxViolation = kwargs['maxViolation']
        self.disp(funcType + ': checking user-supplied gradient of shape (%d, %d)' % (getattr(self, funcType[1:])(xCheck).size, xCheck.size))
        self.disp('according to:')
        self.disp('    diffInt = ' + str(self.diffInt))
        self.disp('    |1 - info_user/info_numerical| < maxViolation = ' + str(maxViolation))
        check_d1(getattr(self, funcType[1:]), getattr(self, funcType), xCheck, **kwargs)
        self.nEvals[funcType[1:]] = 0
        self.nEvals[funcType] = 0

    def _makeCorrectArgs(self):
        argslist = dir(self.args)
        if not ('f' in argslist and 'c' in argslist and 'h' in argslist):
            tmp, self.args = self.args, autocreate()
            self.args.f = self.args.c = self.args.h = tmp
        for j in ('f', 'c', 'h'):
            v = getattr(self.args, j)
            if type(v) != type(()):
                setattr(self.args, j, (v,))

    def __finalize__(self):
        if self.isFDmodel:
            self.xf = self._vector2point(self.xf)

    def _Prepare(self):
        baseProblem._prepare(self)
        if asarray(self.implicitBounds).size == 1:
            self.implicitBounds = [
             -self.implicitBounds, self.implicitBounds]
            self.implicitBounds.sort()
        if hasattr(self, 'solver'):
            if not self.solver.iterfcnConnected:
                if self.solver.funcForIterFcnConnection == 'f':
                    if not hasattr(self, 'f_iter'):
                        self.f_iter = max((self.n, 4))
                elif not hasattr(self, 'df_iter'):
                    self.df_iter = True
        if self.prepared == True:
            return
        else:
            self._makeCorrectArgs()
            for s in ('f', 'df', 'd2f', 'c', 'dc', 'd2c', 'h', 'dh', 'd2h'):
                derivativeOrder = len(s) - 1
                self.nEvals[Copy(s)] = 0
                Attr = getattr(self, s, None)
                if Attr is not None and (not isinstance(Attr, (list, tuple)) or len(Attr) != 0):
                    setattr(self.userProvided, s, True)
                    A = getattr(self, s)
                    if type(A) not in [list, tuple]:
                        A = (
                         A,)
                    setattr(self.user, s, A)
                else:
                    setattr(self.userProvided, s, False)
                if derivativeOrder == 0:
                    setattr(self, s, (lambda x, IND=None, userFunctionType=s, ignorePrev=False, getDerivative=False: self.wrapped_func(x, IND, userFunctionType, ignorePrev, getDerivative)))
                elif derivativeOrder == 1:
                    setattr(self, s, (lambda x, ind=None, funcType=s[-1], ignorePrev=False, useSparse=self.useSparse: self.wrapped_1st_derivatives(x, ind, funcType, ignorePrev, useSparse)))
                elif derivativeOrder == 2:
                    setattr(self, s, getattr(self, 'user_' + s))
                else:
                    self.err('incorrect non-linear function case')

            self.diffInt = ravel(self.diffInt)
            self.vectorDiffInt = self.diffInt.size > 1
            if self.scale is not None:
                self.scale = ravel(self.scale)
                if self.vectorDiffInt or self.diffInt[0] != ProbDefaults['diffInt']:
                    self.info('using both non-default scale & diffInt is not recommended. diffInt = diffInt/scale will be used')
                self.diffInt = self.diffInt / self.scale
            for s in ['c', 'h', 'f']:
                if not getattr(self.userProvided, s):
                    setattr(self, 'n' + s, 0)
                else:
                    setNonLinFuncsNumber(self, s)

            self.prepared = True
            return

    def _isUnconstrained(self):
        return self.b.size == 0 and self.beq.size == 0 and not self.userProvided.c and not self.userProvided.h and (len(self.lb) == 0 or all(isinf(self.lb))) and (len(self.ub) == 0 or all(isinf(self.ub)))


def minimize(p, *args, **kwargs):
    if 'goal' in kwargs:
        if kwargs['goal'] in ('min', 'minimum'):
            p.warn("you shouldn't pass 'goal' to the function 'minimize'")
        else:
            p.err('ambiguous goal has been requested: function "minimize", goal: %s' % kwargs['goal'])
    p.goal = 'minimum'
    return runProbSolver(p, *args, **kwargs)


def maximize(p, *args, **kwargs):
    if 'goal' in kwargs:
        if kwargs['goal'] in ('max', 'maximum'):
            p.warn("you shouldn't pass 'goal' to the function 'maximize'")
        else:
            p.err('ambiguous goal has been requested: function "maximize", goal: %s' % kwargs['goal'])
    p.goal = 'maximum'
    return runProbSolver(p, *args, **kwargs)


def linear_render(f, D, Z):
    import FuncDesigner as fd
    if f.is_oovar:
        return f
    ff = f(Z)
    name, tol, _id = f.name, f.tol, f._id
    f = fd.sum([ v * (val if type(val) != ndarray or val.ndim < 2 else val.flatten()) for v, val in D.items() ]) + (ff if isscalar(ff) or ff.ndim <= 1 else asscalar(ff))
    f.name, f.tol, f._id = name, tol, _id
    return f