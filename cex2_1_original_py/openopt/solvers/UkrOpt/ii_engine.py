# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\UkrOpt\ii_engine.pyc
# Compiled at: 2012-12-08 11:04:59
from interalgLLR import *
from numpy import inf, prod, all, sum

def r14IP(p, nlhc, residual, definiteRange, y, e, vv, asdf1, C, CBKPMV, g, nNodes, frc, fTol, Solutions, varTols, _in, dataType, maxNodes, _s, indTC, xRecord):
    required_sigma = p.ftol * 0.99
    m, n = y.shape
    ip = func10(y, e, vv)
    ip.dictOfFixedFuncs = p.dictOfFixedFuncs
    o, a, definiteRange = func8(ip, asdf1, dataType)
    if not all(definiteRange):
        p.err('\n        numerical integration with interalg is implemented \n        for definite (real) range only, no NaN values in integrand are allowed')
    o, a = o.reshape(2 * n, m).T, a.reshape(2 * n, m).T
    nodes = func11(y, e, None, indTC, None, o, a, _s, p)
    if len(_in) == 0:
        an = nodes
    else:
        an = hstack((_in, nodes)).tolist()
    an.sort(key=(lambda obj: obj.key), reverse=False)
    ao_diff = array([ node.key for node in an ])
    volumes = array([ node.volume for node in an ])
    r10 = ao_diff <= 0.5 * (required_sigma - p._residual) / (prod(p.ub - p.lb) - p._volume)
    ind = where(r10)[0]
    v = volumes[ind]
    p._F += sum(array([ an[i].F for i in ind ]) * v)
    residuals = ao_diff[ind] * v
    p._residual += residuals.sum()
    p._volume += v.sum()
    an = asarray(an, object)
    an = an[where(logical_not(r10))[0]]
    nNodes.append(len(an))
    p.iterfcn(xk=array(nan), fk=p._F, rk=0)
    if p.istop != 0:
        ao_diff = array([ node.key for node in an ])
        volumes = array([ node.volume for node in an ])
        p._residual += sum(ao_diff * volumes)
        _s = None
    return (
     an, g, inf, _s, Solutions, xRecord, frc, CBKPMV)