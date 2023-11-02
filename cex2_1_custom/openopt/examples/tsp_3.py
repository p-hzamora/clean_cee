# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\tsp_3.pyc
# Compiled at: 2012-12-08 11:04:59
"""
A simple OpenOpt TSP example for directed multigraph;
requires networkx (http://networkx.lanl.gov)
and FuncDesigner installed.
For some solvers limitations on time, cputime, "enough" value, basic GUI features are available.
See http://openopt.org/TSP for more details
"""
from .openopt import *
from numpy import sin, cos
import networkx as nx
N = 5
G = nx.MultiDiGraph()
G.add_edges_from([ (i, j, {'time': 1.5 * (cos(i) + sin(j) + 1) ** 2, 'cost': (i - j) ** 2 + 2 * sin(i) + 2 * cos(j) + 1, 'way': 'aircraft'}) for i in range(N) for j in range(N) if i != j ])
G.add_edges_from([ (i, j, {'time': 4.5 * (cos(i) - sin(j) + 1) ** 2, 'cost': (i - j) ** 2 + sin(i) + cos(j) + 1, 'way': 'railroad'}) for i in range(int(2 * N / 3)) for j in range(int(N)) if i != j ])
objective = 'time'
constraints = lambda values: (
 2 * values['time'] + 3 * values['cost'] > 100, 8 * values['time'] + 15 * values['cost'] > 150)
p = TSP(G, objective=objective, constraints=constraints, startNode=2, returnToStart=True)
solver = 'glpk'
r = p.solve(solver)
print r.Edges