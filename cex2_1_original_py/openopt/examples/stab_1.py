# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\stab_1.pyc
# Compiled at: 2012-12-08 11:04:59
"""
Simple OpenOpt graph stability number example;
requires networkx (http://networkx.lanl.gov)
and FuncDesigner installed.
For maximum clique problem you could use STAB on complementary graph, for networkx it's nx.complement(G) 
Unlike networkx maximum_independent_set() we search for *exact* solution.
Limitations on time, cputime, "enough" value, basic GUI features are available.
"""
from openopt import STAB
import networkx as nx
G = nx.path_graph(15)
p = STAB(G, includedNodes=[1, 5, 8], excludedNodes=[0, 4, 10])
r = p.solve('interalg', iprint=0)
print (
 r.ff, r.solution)