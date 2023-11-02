# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: FuncDesigner\sle.pyc
# Compiled at: 2011-12-14 17:11:20
from FDmisc import FuncDesignerException
from ooFun import oofun, BaseFDConstraint
from numpy import nan, zeros, isscalar, inf

class sle:
    _isInitialized = False
    matrixSLEsolver = 'autoselect'

    def __init__(self, equations, *args, **kwargsForOpenOptSLEconstructor):
        if len(args) > 0:
            FuncDesignerException('incorrect sle definition, too many args are obtained')
        if type(equations) not in [list, tuple, set]:
            raise FuncDesignerException('argument of sle constructor should be Python tuple or list of equations or oofuns')
        self.equations = equations
        try:
            from openopt import SLE
        except:
            s = 'Currently to solve SLEs via FuncDesigner you should have OpenOpt installed; maybe in future the dependence will be ceased'
            raise FuncDesignerException(s)

        self.decodeArgs(*args, **kwargsForOpenOptSLEconstructor)
        if 'iprint' not in kwargsForOpenOptSLEconstructor.keys():
            kwargsForOpenOptSLEconstructor['iprint'] = -1
        self.p = SLE(self.equations, self.startPoint, **kwargsForOpenOptSLEconstructor)
        self.p._Prepare()
        self.A, self.b = self.p.C, self.p.d
        self.n = self.p.C.shape[0]
        self.decode = lambda x: self.p._vector2point(x)

    def solve(self, *args):
        if len(args) > 2:
            raise FuncDesignerException('incorrect number of args, should be at most 2 (startPoint and/or solver name, order: any)')
        self.decodeArgs(*args)
        r = self.p.solve(matrixSLEsolver=self.matrixSLEsolver)
        if r.istop >= 0:
            return r
        R = {}
        for key, value in self.p.x0.items():
            R[key] = value * nan

        r.xf = R
        r.ff = inf
        return r

    def decodeArgs(self, *args, **kwargs):
        hasStartPoint = False
        for arg in args:
            if isinstance(arg, str):
                self.matrixSLEsolver = arg
            elif isinstance(arg, dict):
                startPoint = args[0]
                hasStartPoint = True
            else:
                raise FuncDesignerException('incorrect arg type, should be string (solver name) or dict (start point)')

        if 'startPoint' in kwargs:
            startPoint = kwargs['startPoint']
            hasStartPoint = True
        if not hasStartPoint:
            if hasattr(self, 'startPoint'):
                return
            involvedOOVars = set()
            for Elem in self.equations:
                elem = Elem.oofun if Elem.isConstraint else Elem
                if elem.is_oovar:
                    involvedOOVars.add(elem)
                else:
                    involvedOOVars.update(elem._getDep())

            startPoint = {}
            for oov in involvedOOVars:
                if isscalar(oov.size):
                    startPoint[oov] = zeros(oov.size)
                else:
                    startPoint[oov] = 0

        self.startPoint = startPoint

    def eig(self, *args, **kw):
        from openopt import EIG
        p = EIG(self.A, *args, **kw)
        r = p.solve()
        vectors = []
        for i in range(len(p.eigenvalues)):
            vectors.append(self.decode(p.eigenvectors[:, i]))

        r.eigenvectors = vectors
        return r