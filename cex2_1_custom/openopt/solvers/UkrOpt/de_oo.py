# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\UkrOpt\de_oo.pyc
# Compiled at: 2012-12-08 11:04:59
from openopt.kernel.baseSolver import baseSolver
from openopt.kernel.setDefaultIterFuncs import SMALL_DELTA_X, SMALL_DELTA_F
import numpy as np
nanPenalty = 10000000000.0
try:
    from np import random
    Rand = random.rand
    Seed = random.seed
    Randint = random.randint
except:
    import random
    Seed = random.seed

    def Rand(*shape):
        r = np.empty(np.prod(shape))
        for i in range(r.size):
            r[i] = random.random()

        return r.reshape(shape)


    def Randint(low, high=None, size=None):
        assert high is None, 'unimplemented yet'
        if size is None:
            return random.randint(0, low - 1)
        else:
            a = np.empty((np.isscalar(size) or np.prod)(size) if 1 else size, dtype=int)
            for i in range(a.size):
                a[i] = random.randint(0, low - 1)

            return a.reshape(size)


class de(baseSolver):
    __name__ = 'de'
    __license__ = 'BSD'
    __authors__ = 'Stepan Hlushak, stepanko - at - gmail - dot - com, connected to OO by Dmitrey'
    __alg__ = 'Two array differential evolution algorithm, Feoktistov V. Differential Evolution. In Search of Solutions (Springer, 2006)(ISBN 0387368965).'
    iterfcnConnected = True
    __homepage__ = ''
    __isIterPointAlwaysFeasible__ = lambda self, p: p.__isNoMoreThanBoxBounded__()
    __optionalDataThatCanBeHandled__ = ['lb', 'ub', 'A', 'b', 'Aeq', 'beq', 'c', 'h']
    _requiresFiniteBoxBounds = True
    baseVectorStrategy = 'random'
    searchDirectionStrategy = 'random'
    differenceFactorStrategy = 'random'
    population = 'default: 10*nVars will be used'
    differenceFactor = 0.8
    crossoverRate = 0.5
    hndvi = 1
    seed = 150880
    __info__ = "\n        This is two array differential evolution algorithm.\n        \n        Can handle constraints Ax <= b and c(x) <= 0 \n        \n        Finite box-bound constraints lb <= x <= ub are required.\n        \n        Parameters:\n            population - population number (should be ~ 10*nVars),\n            differenceFactor - difference factor (should be in (0,1] range),\n            crossoverRate - constant of crossover (should be ~ 0.5, in (0,1] range),\n            baseVectorStrategy - strategy of selection of base vector, can \n                                   be 'random' (default) or 'best' (best vector).\n            searchDirectionStrategy - strategy for calculation of the difference vector,\n                                    can be 'random' (random direction, default) or \n                                    'best' (direction of the best vectors).\n            differenceFactorStrategy - strategy for difference factror (F), can be\n                                    'constant' (constant factor, default) or\n                                    'random' (F is chosen random for each vector and \n                                    each component of vector).\n            hndvi -   half of number of individuals that take part in creation\n                         of difference vector.\n        "

    def __init__(self):
        pass

    def __solver__(self, p):
        if not p.__isFiniteBoxBounded__():
            p.err('this solver requires finite lb, ub: lb <= x <= ub')
        p.kernelIterFuncs.pop(SMALL_DELTA_X, None)
        p.kernelIterFuncs.pop(SMALL_DELTA_F, None)
        lb, ub = p.lb, p.ub
        D = p.n
        if isinstance(self.population, str):
            NP = 10 * D
        else:
            NP = self.population
        F = self.differenceFactor
        Cr = self.crossoverRate
        Seed(self.seed)
        pop = Rand(NP, D) * (ub - lb) + lb
        if np.any(np.isfinite(p.x0)):
            pop[0] = np.copy(p.x0)
        best, vals, constr_vals = _eval_pop(pop, p)
        Best = p.point(best[2], f=best[0], mr=best[1], mrName=None, mrInd=0)
        if self.baseVectorStrategy == 'random':
            useRandBaseVectStrat = True
        else:
            if self.baseVectorStrategy == 'best':
                useRandBaseVectStrat = False
            else:
                p.err('incorrect baseVectorStrategy, should be "random" or "best", got ' + str(self.baseVectorStrategy))
            if self.searchDirectionStrategy == 'random':
                useRandSearchDirStrat = True
            elif self.searchDirectionStrategy == 'best':
                useRandSearchDirStrat = False
            else:
                p.err('incorrect searchDirectionStrategy, should be "random" or "best", got ' + str(self.searchDirectionStrategy))
            if self.differenceFactorStrategy == 'random':
                useRandDiffFactorStrat = True
            elif self.differenceFactorStrategy == 'constant':
                useRandDiffFactorStrat = False
            else:
                p.err('incorrect differenceFactorStrategy, should be "random" or "constant", got ' + str(self.differenceFactorStrategy))
            for i in range(p.maxIter + 10):
                old_pop = pop
                old_vals = vals
                old_constr_vals = constr_vals
                Old_best = Best
                if useRandBaseVectStrat:
                    try:
                        beta = old_pop[Randint(NP, size=NP)]
                    except:
                        beta = np.array([ old_pop[Randint(NP)] for j in range(NP) ])

                else:
                    beta = np.ones((NP, D), 'd')
                    beta = beta * best[2]
                num_ind = self.hndvi
                if useRandSearchDirStrat:
                    r1_ints = Randint(NP, size=(num_ind, NP))
                    r2_ints = Randint(NP, size=(num_ind, NP))
                    try:
                        barycenter1 = old_pop[r1_ints].sum(0)
                        barycenter2 = old_pop[r2_ints].sum(0)
                    except:
                        assert self.hndvi == 1, 'unimplemented for PyPy yet'
                        barycenter1 = np.array([ old_pop[j] for j in r1_ints[0] ])
                        barycenter2 = np.array([ old_pop[j] for j in r2_ints[0] ])

                else:
                    r_ints = Randint(NP, size=2 * num_ind)
                    list = [ (j, constr_vals[j], vals[j]) for j in r_ints ]
                    list_arr = np.array(list, dtype=[('i', int),
                     (
                      'constr_val', float),
                     (
                      'val', float)])
                    list_arr.sort(order=['constr_val', 'val'])
                    best_list = list_arr[0:num_ind]
                    best_arr = np.array([ j for j, c, f in best_list ], 'i')
                    worst_list = list_arr[num_ind:2 * num_ind]
                    worst_arr = np.array([ j for j, c, f in worst_list ], 'i')
                    try:
                        barycenter1 = old_pop[worst_arr].sum(0) / num_ind
                        barycenter2 = old_pop[best_arr].sum(0) / num_ind
                    except:
                        assert self.hndvi == 1, 'unimplemented for PyPy yet'
                        barycenter1 = np.array([ old_pop[j] for j in worst_arr[0] ])
                        barycenter2 = np.array([ old_pop[j] for j in best_arr[0] ])

                if num_ind != 1:
                    barycenter1 /= num_ind
                    barycenter2 /= num_ind
                delta = barycenter2 - barycenter1
                if useRandDiffFactorStrat:
                    Ft = Rand(NP, D)
                    Ft = Ft * F
                else:
                    Ft = F
                pop = beta + Ft * delta
                cross_v = np.ones((NP, D))
                const_v = Rand(NP, D)
                const_v = np.ceil(const_v - Cr)
                cross_v = cross_v - const_v
                pop = old_pop * const_v + pop * cross_v
                pop = _correct_box_constraints(lb, ub, pop)
                best, vals, constr_vals = _eval_pop(pop, p)
                Best = p.point(best[2], f=best[0], mr=best[1], mrName=None, mrInd=0)
                bool_constr_v = old_constr_vals < constr_vals
                bool_v = old_vals < vals
                zero_constr_v = 1 * ((constr_vals > 0) + (old_constr_vals > 0))
                bool_constr_v = (bool_constr_v * 4 - 2) * zero_constr_v
                bool_v = bool_v * 2 - 1
                bool_v = bool_constr_v + bool_v
                bool_v = bool_v > 0
                old_sel_v = (bool_v * 1).reshape(NP, 1)
                sel_v = np.ones((NP, 1)) - old_sel_v
                pop = old_pop * old_sel_v + pop * sel_v
                old_sel_v = old_sel_v.reshape(NP)
                sel_v = sel_v.reshape(NP)
                vals = old_vals * old_sel_v + vals * sel_v
                constr_vals = old_constr_vals * old_sel_v + constr_vals * sel_v
                if Old_best.betterThan(Best):
                    Best = Old_best
                p.iterfcn(Best)
                if p.istop:
                    return

        return


def _eval_pop(pop, p):
    NP = pop.shape[0]
    constr_vals = np.zeros(NP)
    vals = p.f(pop).flatten()
    vals[np.isnan(vals)] = np.inf
    if p.__isNoMoreThanBoxBounded__():
        best_i = vals.argmin()
        best = (
         vals[best_i], 0, pop[best_i])
    else:
        P = p.point(pop)
        constr_vals = P.mr(checkBoxBounds=False) + nanPenalty * P.nNaNs()
        ind = constr_vals < p.contol
        if not np.any(ind):
            j = np.argmin(constr_vals)
            bestPoint = p.point(pop[j])
        else:
            IND = np.where(ind)[0]
            try:
                P2 = np.atleast_2d(pop[IND])
                F = np.atleast_1d(vals[IND])
            except:
                P2 = np.atleast_2d([ pop[j] for j in IND ])
                F = np.atleast_1d([ vals[j] for j in IND ])

            J = np.nanargmin(F)
            bestPoint = p.point(P2[J], f=F[J])
        best = (
         bestPoint.f(), bestPoint.mr() + nanPenalty * bestPoint.nNaNs(), bestPoint.x)
    return (best, vals, constr_vals)


def _correct_box_constraints(lb, ub, pop):
    diff_lb = pop - lb
    check_lb = diff_lb < 0.0
    scale = 1.0
    while np.any(check_lb):
        check_lb = check_lb * 1
        pop = pop - (1 + scale) * check_lb * diff_lb
        diff_lb = pop - lb
        check_lb = diff_lb < 0.0
        scale /= 2

    diff_ub = pop - ub
    check_ub = diff_ub > 0.0
    scale = 1.0
    while np.any(check_ub):
        check_ub = check_ub * 1
        pop = pop - (1 + scale) * check_ub * diff_ub
        diff_ub = pop - ub
        check_ub = diff_ub > 0.0
        scale /= 2

    return pop