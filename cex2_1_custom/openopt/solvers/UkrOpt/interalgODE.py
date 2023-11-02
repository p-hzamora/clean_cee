# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\UkrOpt\interalgODE.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import hstack, asarray, abs, atleast_1d, where, logical_not, argsort, vstack, sum, array, nan, all
from FuncDesigner import oopoint

def interalg_ODE_routine(p, solver):
    isIP = p.probType == 'IP'
    isODE = p.probType == 'ODE'
    if isODE:
        f, y0, t, r30, ftol = (
         p.equations, p.x0, p.timeVariable, p.times, p.ftol)
        assert len(f) == 1, 'multiple ODE equations are unimplemented for FuncDesigner yet'
        f = list(f.values())[0]
    else:
        if isIP:
            assert p.n == 1 and p.__isNoMoreThanBoxBounded__()
            f, y0, ftol = p.user.f[0], 0.0, p.ftol
            if p.fTol is not None:
                ftol = p.fTol
            t = list(f._getDep())[0]
            r30 = p.domain[t]
            p.iterfcn(p.point([nan] * p.n))
        else:
            p.err('incorrect prob type for interalg ODE routine')
        eq_var = list(p._x0.keys())[0]
        dataType = solver.dataType
        if type(ftol) == int:
            ftol = float(ftol)
        if len(r30) < 2:
            p.err('length ot time array must be at least 2')
        r37 = abs(r30[-1] - r30[0])
        r28 = asarray(atleast_1d(r30[0]), dataType)
        r29 = asarray(atleast_1d(r30[-1]), dataType)
        storedr28 = []
        r27 = []
        r31 = []
        r32 = []
        r33 = ftol
        F = 0.0
        p._Residual = 0
        for itn in range(p.maxIter + 1):
            if r30[-1] > r30[0]:
                mp = oopoint({t: [r28, r29]}, skipArrayCast=True)
            else:
                mp = oopoint({t: [r29, r28]}, skipArrayCast=True)
            mp.isMultiPoint = True
            delta_y = f.interval(mp, dataType)
            if not all(delta_y.definiteRange):
                p.err('\n            solving ODE with interalg is implemented for definite (real) range only, \n            no NaN values in integrand are allowed')
            r34 = atleast_1d(delta_y.ub)
            r35 = atleast_1d(delta_y.lb)
            r36 = atleast_1d(r34 - r35 <= 0.95 * r33 / r37)
            ind = where(r36)[0]
            if isODE:
                storedr28.append(r28[ind])
                r27.append(r29[ind])
                r31.append(r34[ind])
                r32.append(r35[ind])
            else:
                assert isIP
                F += 0.5 * sum((r29[ind] - r28[ind]) * (r34[ind] + r35[ind]))
            if ind.size != 0:
                tmp = abs(r29[ind] - r28[ind])
                Tmp = sum((r34[ind] - r35[ind]) * tmp)
                r33 -= Tmp
                if isIP:
                    p._residual += Tmp
                r37 -= sum(tmp)
            ind = where(logical_not(r36))[0]
            if ind.size == 0:
                p.istop = 1000
                p.msg = 'problem has been solved according to required tolerance'
                break
            r38, r39 = r28[ind], r29[ind]
            r40 = 0.5 * (r38 + r39)
            r28 = vstack((r38, r40)).flatten()
            r29 = vstack((r40, r39)).flatten()
            if isODE:
                p.iterfcn(fk=r33 / ftol)
            elif isIP:
                p.iterfcn(xk=array(nan), fk=F, rk=0)
            else:
                p.err('bug in interalgODE.py')
            if p.istop != 0:
                break

    if isODE:
        t0, t1, lb, ub = (hstack(storedr28), hstack(r27), hstack(r32), hstack(r31))
        ind = argsort(t0)
        if r30[0] > r30[-1]:
            ind = ind[::-1]
        t0, t1, lb, ub = (
         t0[ind], t1[ind], lb[ind], ub[ind])
        lb, ub = y0 + (lb * (t1 - t0)).cumsum(), y0 + (ub * (t1 - t0)).cumsum()
        p.extras = {'startTimes': t0, 'endTimes': t1, eq_var: {'infinums': lb, 'supremums': ub}}
        return (
         t0, t1, lb, ub)
    else:
        if isIP:
            P = p.point([nan] * p.n)
            P._f = F
            P._mr = r33
            P._mrName = 'None'
            P._mrInd = 0
            p.iterfcn(asarray([nan] * p.n), fk=F, rk=0)
        else:
            p.err('incorrect prob type in interalg ODE routine')
        return