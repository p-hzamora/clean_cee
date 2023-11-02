# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\mcp_1.pyc
# Compiled at: 2012-12-08 11:04:59
"""
Simple OpenOpt maximum clique example;
requires networkx (http://networkx.lanl.gov)
and FuncDesigner installed.
Limitations on time, cputime, "enough" value, basic GUI features are available.
"""
from openopt import MCP
import networkx as nx
G = nx.path_graph(15)
G.add_edges_from([ (i, (i + 8) % 15) for i in range(15) ])
p = MCP(G)
r = p.solve('glpk')
print (
 r.ff, r.solution)