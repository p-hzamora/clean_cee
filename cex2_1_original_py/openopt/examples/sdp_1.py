# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\examples\sdp_1.pyc
# Compiled at: 2012-12-08 11:04:59
"""
This is OpenOpt SDP example,
for the problem
http://openopt.org/images/1/12/SDP.png
"""
from numpy import mat
from openopt import SDP
S, d = {}, {}
S[(0, 0)] = mat('-7 -11; -11 3')
S[(0, 1)] = mat('7 -18; -18 8')
S[(0, 2)] = mat('-2 -8; -8 1')
d[0] = mat('33, -9; -9, 26')
S[(1, 0)] = mat('-21 -11 0; -11 10 8; 0 8 5')
S[(1, 1)] = mat('0 10 16; 10 -10 -10; 16 -10 3')
S[(1, 2)] = mat('-5 2 -17; 2 -6 8; -17 -7 6')
d[1] = mat('14, 9, 40; 9, 91, 10; 40, 10, 15')
p = SDP([1, -1, 1], S=S, d=d)
r = p.solve('dsdp', iprint=-1)
f_opt, x_opt = r.ff, r.xf
print 'x_opt: %s' % x_opt
print 'f_opt: %s' % f_opt