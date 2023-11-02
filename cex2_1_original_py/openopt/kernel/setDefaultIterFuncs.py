# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\setDefaultIterFuncs.pyc
# Compiled at: 2012-12-08 11:04:59
__docformat__ = 'restructuredtext en'
from .numpy import *
SMALL_DF = 2
SMALL_DELTA_X = 3
SMALL_DELTA_F = 4
FVAL_IS_ENOUGH = 10
MAX_NON_SUCCESS = 11
USER_DEMAND_STOP = 80
BUTTON_ENOUGH_HAS_BEEN_PRESSED = 88
SOLVED_WITH_UNIMPLEMENTED_OR_UNKNOWN_REASON = 1000
UNDEFINED = 0
IS_NAN_IN_X = -4
IS_LINE_SEARCH_FAILED = -5
IS_MAX_ITER_REACHED = -7
IS_MAX_CPU_TIME_REACHED = -8
IS_MAX_TIME_REACHED = -9
IS_MAX_FUN_EVALS_REACHED = -10
IS_ALL_VARS_FIXED = -11
FAILED_TO_OBTAIN_MOVE_DIRECTION = -13
USER_DEMAND_EXIT = -99
FAILED_WITH_UNIMPLEMENTED_OR_UNKNOWN_REASON = -1000

def stopcase(arg):
    if hasattr(arg, 'istop'):
        istop = arg.istop
    else:
        istop = arg
    if istop > 0:
        return 1
    else:
        if istop in [0, IS_MAX_ITER_REACHED, IS_MAX_CPU_TIME_REACHED, IS_MAX_TIME_REACHED, 
         IS_MAX_FUN_EVALS_REACHED]:
            return 0
        return -1


def setDefaultIterFuncs(className):
    d = dict()
    d[SMALL_DF] = lambda p: small_df(p)
    d[SMALL_DELTA_X] = lambda p: small_deltaX(p)
    d[SMALL_DELTA_F] = lambda p: small_deltaF(p)
    d[FVAL_IS_ENOUGH] = lambda p: isEnough(p)
    d[IS_NAN_IN_X] = lambda p: isNanInX(p)
    d[IS_MAX_ITER_REACHED] = lambda p: isMaxIterReached(p)
    d[IS_MAX_CPU_TIME_REACHED] = lambda p: isMaxCPUTimeReached(p)
    d[IS_MAX_TIME_REACHED] = lambda p: isMaxTimeReached(p)
    if className == 'NonLin':
        d[IS_MAX_FUN_EVALS_REACHED] = lambda p: isMaxFunEvalsReached(p)
    return d


def small_df(p):
    if not hasattr(p, '_df') or p._df is None:
        return False
    if hasattr(p._df, 'toarray'):
        p._df = p._df.toarray()
    if p.norm(p._df) >= p.gtol or not all(isfinite(p._df)) or not p.isFeas(p.iterValues.x[-1]):
        return False
    return (
     True, '|| gradient F(X[k]) || < gtol')


def small_deltaX(p):
    if p.iter == 0:
        return False
    else:
        diffX = p.iterValues.x[-1] - p.iterValues.x[-2]
        if p.scale is not None:
            diffX *= p.scale
        if p.norm(diffX) >= p.xtol:
            return False
        return (
         True, '|| X[k] - X[k-1] || < xtol')
        return


def small_deltaF(p):
    if p.iter == 0:
        return False
    else:
        if isnan(p.iterValues.f[-1]) or isnan(p.iterValues.f[-2]) or p.norm(p.iterValues.f[-1] - p.iterValues.f[-2]) >= p.ftol:
            return False
        return (
         True, '|| F[k] - F[k-1] || < ftol')


def isEnough(p):
    if p.fEnough > asscalar(asarray(p.Fk)) and p.isFeas(p.xk):
        return (True, 'fEnough has been reached')
    else:
        return False


def isNanInX(p):
    if any(isnan(p.xk)):
        return (True, 'NaN in X[k] coords has been obtained')
    else:
        return False


def isMaxIterReached(p):
    if p.iter >= p.maxIter - 1:
        return (True, 'Max Iter has been reached')
    else:
        return False


def isMaxCPUTimeReached(p):
    if p.iterCPUTime[-1] < p.maxCPUTime + p.cpuTimeElapsedForPlotting[-1]:
        return False
    else:
        return (
         True, 'max CPU time limit has been reached')


def isMaxTimeReached(p):
    if p.currtime - p.timeStart < p.maxTime + p.timeElapsedForPlotting[-1]:
        return False
    else:
        return (
         True, 'max time limit has been reached')


def isMaxFunEvalsReached(p):
    if p.nEvals['f'] >= p.maxFunEvals:
        return (True, 'max objfunc evals limit has been reached')
    else:
        return False


def denyingStopFuncs(ProblemGroup=None):
    return {isMinIterReached: 'min iter is not reached yet', isMinTimeReached: 'min time is not reached yet', isMinCPUTimeReached: 'min cputime is not reached yet', isMinFunEvalsReached: 'min objective function evaluations nuber is not reached yet'}


isMinFunEvalsReached = lambda p: p.minFunEvals == 0 or 'f' in p.nEvals.keys() and p.nEvals['f'] >= p.minFunEvals
isMinTimeReached = lambda p: p.currtime - p.timeStart > p.minTime + p.timeElapsedForPlotting[-1]
isMinCPUTimeReached = lambda p: p.iterCPUTime[-1] >= p.minCPUTime + p.cpuTimeElapsedForPlotting[-1]
isMinIterReached = lambda p: p.iter >= p.minIter