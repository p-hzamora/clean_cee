# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\tsp_2.pyc
# Compiled at: 2012-12-08 11:04:59
"""
A simple OpenOpt TSP example for directed graph;
requires networkx (http://networkx.lanl.gov)
and FuncDesigner installed.
For some solvers limitations on time, cputime, "enough" value, basic GUI features are available.
See http://openopt.org/TSP for more details
"""
from .openopt import *
from numpy import sin, cos
import networkx as nx
N = 5
G = nx.DiGraph()
G.add_edges_from([ ('node %d' % i, 'node %d' % j, {'time': 1.5 * (cos(i) + sin(j) + 1) ** 2, 'cost': (i - j) ** 2 + 2 * sin(i) + 2 * cos(j) + 1}) for i in range(N) for j in range(N) if i != j ])
constraints = lambda values: (
 2 * values['time'] + 3 * values['cost'] > 100, 8 * values['time'] + 15 * values['cost'] > 150)
objective = lambda values: values['time'] + 10 * values['cost']
p = TSP(G, objective=objective, constraints=constraints, start='node 3', returnToStart=False)
r = p.solve('lpSolve')
print r.nodes
print r.edges
print r.Edges