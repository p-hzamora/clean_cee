# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\MCP.pyc
# Compiled at: 2012-12-08 11:04:59
from baseProblem import MatrixProblem

class MCP(MatrixProblem):
    _optionalData = []
    probType = 'MCP'
    expectedArgs = ['graph']
    allowedGoals = ['maximum clique']
    showGoal = False
    _init = False

    def __setattr__(self, attr, val):
        if self._init:
            self.err('openopt MCP instances are immutable, arguments should pass to constructor or solve()')
        self.__dict__[attr] = val

    def __init__(self, *args, **kw):
        MatrixProblem.__init__(self, *args, **kw)
        self.__init_kwargs = kw
        self._init = True

    def solve(self, *args, **kw):
        import networkx as nx
        graph = nx.complement(self.graph)
        from openopt import STAB
        KW = self.__init_kwargs
        KW.update(kw)
        P = STAB(graph, **KW)
        r = P.solve(*args)
        return r