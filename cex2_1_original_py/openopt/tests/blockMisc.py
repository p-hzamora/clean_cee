# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\tests\blockMisc.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import *
from numpy.linalg import norm

def project2box(x, lb, ub):
    X = atleast_1d(asfarray(x))
    lb, ub = atleast_1d(lb), atleast_1d(ub)
    projection = copy(X)
    ind = where(projection < lb)[0]
    projection[ind] = lb[ind]
    ind = where(projection > ub)[0]
    projection[ind] = ub[ind]
    distance = norm(X - projection)
    return (projection, distance)


def project2box_derivative(x, lb, ub):
    X = atleast_1d(asfarray(x))
    lb, ub = atleast_1d(lb), atleast_1d(ub)
    projection, distance = project2box(X, lb, ub)
    dX = zeros(X.shape)
    if distance == 0:
        return dX
    else:
        dX[where(X > ub)[0]] = 1.0
        dX[where(X < lb)[0]] = -1.0
        return dX


def project2ball(x, radius, center=0.0):
    X = atleast_1d(asfarray(x))
    distance2center = norm(X - center)
    if distance2center <= radius:
        return (copy(x), 0.0)
    else:
        projection = center + (X - center) * (radius / distance2center)
        distance = distance2center - radius
        return (projection, distance)


def project2ball_derivative(x, radius, center=0.0):
    X = atleast_1d(asfarray(x))
    distance2center = norm(X - center)
    if distance2center <= radius:
        return zeros(X.shape)
    else:
        distance = distance2center - radius
        return (X - center) / distance