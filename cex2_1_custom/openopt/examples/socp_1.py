# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\socp_1.pyc
# Compiled at: 2012-12-08 11:04:59
"""
OpenOpt SOCP example
for the problem http://openopt.org/images/2/28/SOCP.png
"""
from .numpy import *
from openopt import SOCP
f = array([-2, 1, 5])
C0 = mat('-13 3 5; -12 12 -6')
d0 = [-3, -2]
q0 = array([-12, -6, 5])
s0 = -12
C1 = mat('-3 6 2; 1 9 2; -1 -19 3')
d1 = [0, 3, -42]
q1 = array([-3, 6, -10])
s1 = 27
p = SOCP(f, C=[C0, C1], d=[d0, d1], q=[q0, q1], s=[s0, s1])
r = p.solve('cvxopt_socp')
x_opt, f_opt = r.xf, r.ff
print ' f_opt: %f    x_opt: %s' % (f_opt, x_opt)