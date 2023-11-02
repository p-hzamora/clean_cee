# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: FuncDesigner\translator.pyc
# Compiled at: 2013-04-09 10:34:14
from numpy import hstack, atleast_1d, cumsum, asfarray, asarray, zeros, ndarray, prod, isscalar, nan, array_equal, copy, array
from FDmisc import FuncDesignerException
from ooPoint import ooPoint
DenseMatrixConstructor = lambda shape: zeros(shape)

class FuncDesignerTranslator:

    def __init__(self, PointOrVariables, **kwargs):
        if isinstance(PointOrVariables, dict):
            Point = PointOrVariables
            Variables = Point.keys()
            self._sizeDict = dict((v, asarray(PointOrVariables[v]).size) for v in PointOrVariables)
            self._shapeDict = dict((v, asarray(PointOrVariables[v]).shape) for v in PointOrVariables)
        else:
            assert type(PointOrVariables) in [list, tuple, set]
            Variables = PointOrVariables
            self._sizeDict = dict((v, v.size if hasattr(v, 'size') and isinstance(v.size, int) else 1) for v in Variables)
            self._shapeDict = dict((v, v.shape if hasattr(v, 'shape') else ()) for v in Variables)
        self._variables = Variables
        self.n = sum(self._sizeDict.values())
        oovar_sizes = list(self._sizeDict.values())
        oovar_indexes = cumsum([0] + oovar_sizes)
        self.oovarsIndDict = dict((v, (oovar_indexes[i], oovar_indexes[i + 1])) for i, v in enumerate(Variables))
        self._SavedValues = {'prevX': nan}

        def vector2point(x):
            isComplexArray = isinstance(x, ndarray) and str(x.dtype).startswith('complex')
            if isComplexArray:
                x = atleast_1d(array(x, copy=True))
            else:
                x = atleast_1d(array(x, copy=True, dtype=float))
            if array_equal(x, self._SavedValues['prevX']):
                return self._SavedValues['prevVal']
            kw = {'skipArrayCast': True} if isComplexArray else {}
            r = ooPoint(((v, x[oovar_indexes[i]:oovar_indexes[i + 1]]) for i, v in enumerate(self._variables)), **kw)
            self._SavedValues['prevVal'] = r
            self._SavedValues['prevX'] = copy(x)
            return r

        self.vector2point = vector2point

    point2vector = lambda self, point: asfarray(atleast_1d(hstack([ point[v] if v in point else zeros(self._shapeDict[v]) for v in self._variables ])))

    def pointDerivative2array(self, pointDerivarive, useSparse=False, func=None, point=None):
        assert useSparse is False, 'sparsity is not implemented in FD translator yet'
        n = self.n
        if len(pointDerivarive) == 0:
            if func is not None:
                assert point is not None
                funcLen = func(point).size
                return DenseMatrixConstructor((funcLen, n))
            raise FuncDesignerException('unclear error, maybe you have constraint independend on any optimization variables')
        key, val = list(pointDerivarive.items())[0]
        if isscalar(val) or isinstance(val, ndarray) and val.shape == ():
            val = atleast_1d(val)
        var_inds = self.oovarsIndDict[key]
        funcLen = int(round(prod(val.shape) / (var_inds[1] - var_inds[0])))
        newStyle = 1
        if useSparse is not False and newStyle:
            assert 0, 'unimplemented yet'
        else:
            if funcLen == 1:
                r = DenseMatrixConstructor(n)
            else:
                r = DenseMatrixConstructor((n, funcLen))
            for key, val in pointDerivarive.items():
                indexes = self.oovarsIndDict[key]
                if r.ndim == 1:
                    r[(indexes[0]):(indexes[1])] = val if isscalar(val) else val.flatten()
                else:
                    r[indexes[0]:indexes[1], :] = val.T
            else:
                if r.ndim > 1:
                    return r.T
                else:
                    return r.reshape(1, -1)

        return