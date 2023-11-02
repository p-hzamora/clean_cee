# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\tsp_1.pyc
# Compiled at: 2012-12-08 11:04:59
"""
Simplest OpenOpt TSP example;
requires networkx (http://networkx.lanl.gov)
and FuncDesigner installed.
For some solvers limitations on time, cputime, "enough" value, basic GUI features are available.
See http://openopt.org/TSP for more details
"""
from .openopt import *
from numpy import sin, cos
import networkx as nx
N = 15
G = nx.Graph()
G.add_edges_from([ (i, j, {'time': 1.5 * (cos(i) + sin(j) + 1) ** 2, 'cost': (i - j) ** 2 + 2 * sin(i) + 2 * cos(j) + 1}) for i in range(N) for j in range(N) if i != j ])
p = TSP(G, objective='time', start=2)
r = p.solve('glpk')
print r.nodes
print r.edges
print r.Edges