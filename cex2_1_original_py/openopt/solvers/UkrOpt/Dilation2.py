# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\UkrOpt\Dilation2.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import dot, sign, zeros, all, isfinite, array, sqrt, any, isnan, pi, sin, arccos, inf, argmax, asfarray
import numpy
from numpy.linalg import norm

class DilationUnit:
    maxScalarComponentsLength = 2

    def __init__(self, vector, dilationCoeff):
        self.scalarComponents = []
        nv = norm(vector)
        assert nv != 0
        self.vectorDirection, self.dilationCoeff = vector / nv, dilationCoeff


class Dilation:
    th_phi = 0.1
    dilationCoeffThreshold = 0.999999
    prevRest = None

    def __init__(self, maxUnitsNum):
        self.maxUnitsNum = maxUnitsNum
        self.units = []
        self.unitsNum = 0
        self.T = numpy.float64
        if hasattr(numpy, 'float128'):
            self.T = numpy.float128

    def addDilationUnit(self, vector, dilationCoeff=0.99999):
        assert all(isfinite(vector))
        self.unitsNum += 1
        v = self.T(vector.copy())
        nv = norm(v)
        v /= nv
        self.units.append(DilationUnit(v, dilationCoeff))
        print 'add new dilation vector; curr num: ', len(self.units)

    def getProjections(self, vv):
        V = self.T(vv)
        NV = norm(V)
        V /= NV
        r = []
        for unit in self.units:
            scalarComponent = dot(unit.vectorDirection, V)
            component = unit.vectorDirection * scalarComponent
            r.append((scalarComponent, component, unit))

        for scalarComponent, component, unit in r:
            V -= component

        return (
         r, V)

    def getDilatedDirection(self, direction):
        projectionsInfo, rest = self.getProjections(direction)
        dilatedDirection = zeros(direction.size)
        for scalarComponent, component, unit in projectionsInfo:
            dilatedDirection += component * unit.dilationCoeff

        return (
         projectionsInfo, dilatedDirection + rest)

    def getRestrictedDilatedDirection(self, direction):
        projectionsInfo, rest = self.getProjections(direction)
        dilatedDirection = zeros(direction.size)
        s, ns = [], []
        for scalarComponent, component, unit in projectionsInfo:
            t = component * unit.dilationCoeff
            s.append(t)
            ns.append(norm(t))
            dilatedDirection += t

        r = dilatedDirection + rest
        nr = norm(r)
        for i in xrange(len(s)):
            if ns[i] < 1e-10 * nr:
                r += 1e-10 * nr * s[i] / ns[i] - s[i]

        return (
         projectionsInfo, r)

    def getMostInsufficientUnit(self, scalarComponents):
        assert self.unitsNum != 0
        ind, miUnit, miValue = 0, self.units[0], self.units[0].dilationCoeff
        for i, unit in enumerate(self.units):
            newValue = unit.dilationCoeff
            if newValue > miValue:
                ind, miUnit, miValue = i, unit, newValue

        return (
         ind, miUnit)

    def updateDilationCoeffs2(self, scalarComponents, rest):
        arr_u = array([ unit.dilationCoeff for unit in self.units ])
        if self.unitsNum == 1:
            self.units[0].dilationCoeff /= 2.0
            return
        m = self.unitsNum
        n = rest.size
        for i, unit in enumerate(self.units):
            c = unit.dilationCoeff * abs(scalarComponents[i]) / n
            if c < 0.125:
                unit.dilationCoeff *= 2.0
            elif c > 0.25:
                unit.dilationCoeff /= 2.0
            print i, unit.dilationCoeff

    def updateDilationCoeffs(self, scalarComponents, rest):
        arr_u = array([ unit.dilationCoeff for unit in self.units ])
        Ui2 = arr_u ** 2
        UiSCi = abs(array([ unit.dilationCoeff * scalarComponents[i] for i, unit in enumerate(self.units) ]))
        Ui2SCi2 = array(UiSCi) ** 2
        S, S2 = sum(Ui2), sum(Ui2SCi2)
        SCi = abs(array(scalarComponents))
        SCi2 = SCi ** 2
        alp = 2.0
        beta = 1.0 / alp
        m, n = self.unitsNum, rest.size
        b = abs(beta)
        nr2 = norm(rest) ** 2
        k = b * sqrt(S2 / sum(Ui2SCi2 * (1.0 - UiSCi)))
        rr = k * (1 - UiSCi)
        assert k > 0
        rr[rr > 4.0] = 4.0
        rr[rr < 0.25] = 0.25
        r = rr * arr_u
        assert len(r) == self.unitsNum == len(self.units)
        for i, unit in enumerate(self.units):
            unit.dilationCoeff = r[i]

        print 'nU=%d k=%0.1g r_min=%0.1g r_max=%0.1g' % (self.unitsNum, k, min(r), max(r))

    def _updateDilationInfo(self, _dilationDirection_, ls, _moveDirection_):
        r = {'increased': 0, 'decreased': 0}
        projectionsInfo, rest = self.getProjections(_dilationDirection_)
        print 'norm(rest1):', norm(rest)
        s = abs(asfarray([ scalarComponent for scalarComponent, component, unit in projectionsInfo ]))
        cond_add = norm(rest) > 0.001
        if cond_add:
            self.addDilationUnit(rest)
            projectionsInfo, rest = self.getProjections(_dilationDirection_)
            print 'norm(rest11):', norm(rest)
        scalarComponents = [ scalarComponent for scalarComponent, component, unit in projectionsInfo ]
        self.updateDilationCoeffs(scalarComponents, rest)
        self.prevRest = rest.copy()
        if self.unitsNum >= self.maxUnitsNum:
            self.unitsNum = 0
            self.units = []
        nRemoved = self.cleanUnnessesaryDilationUnits()
        if nRemoved:
            print 'nRemoved:', nRemoved
        return r

    def cleanUnnessesaryDilationUnits(self):
        indUnitsToRemove = []
        for i, unit in enumerate(self.units):
            if unit.dilationCoeff > self.dilationCoeffThreshold:
                print '>>', unit.dilationCoeff, self.dilationCoeffThreshold
                indUnitsToRemove.append(i)

        for j in xrange(len(indUnitsToRemove)):
            self.units.pop(indUnitsToRemove[-1 - j])

        nRemoved = len(indUnitsToRemove)
        self.unitsNum -= nRemoved
        return nRemoved