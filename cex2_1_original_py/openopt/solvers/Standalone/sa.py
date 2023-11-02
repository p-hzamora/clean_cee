# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\Standalone\sa.pyc
# Compiled at: 2012-12-08 11:04:59
import random, math, numpy as np

def P(prev_score, next_score, temperature):
    if next_score > prev_score:
        return 1.0
    else:
        return math.exp(-abs(next_score - prev_score) / temperature)


class ObjectiveFunction:
    """class to wrap an objective function and 
    keep track of the best solution evaluated"""

    def __init__(self, objective_function):
        self.objective_function = objective_function
        self.best = None
        self.best_score = None
        return

    def __call__(self, solution):
        score = self.objective_function(solution)
        if self.best is None or score > self.best_score:
            self.best_score = score
            self.best = solution
        return score


def kirkpatrick_cooling(start_temp, alpha):
    T = start_temp
    while True:
        yield T
        T = alpha * T


def anneal(init_function, move_operator, objective_function, max_evaluations, start_temp, alpha, prob=None):
    objective_function = ObjectiveFunction(objective_function)
    current = init_function()
    current_score = objective_function(current)
    num_evaluations = 1
    cooling_schedule = kirkpatrick_cooling(start_temp, alpha)
    for temperature in cooling_schedule:
        done = False
        for next in move_operator(current):
            if num_evaluations >= max_evaluations:
                done = True
                break
            next_score = objective_function(next)
            num_evaluations += 1
            p = P(current_score, next_score, temperature)
            if not num_evaluations % 64 and prob is not None:
                prob.iterfcn(np.array(current), -current_score)
                if prob.istop != 0:
                    return (num_evaluations, objective_function.best_score, objective_function.best)
            if random.random() < p:
                current = next
                current_score = next_score
                break

        if done:
            break

    best_score = objective_function.best_score
    best = objective_function.best
    return (
     num_evaluations, best_score, best)