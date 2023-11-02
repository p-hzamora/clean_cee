# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\stats\rv.pyc
# Compiled at: 2013-02-16 13:27:32
from __future__ import division, print_function, absolute_import
from numpy import vectorize
from numpy.random import random_sample
__all__ = [
 'randwppf', 'randwcdf']

def randwppf(ppf, args=(), size=None):
    """
    returns an array of randomly distributed integers of a distribution
    whose percent point function (inverse of the CDF or quantile function)
    is given.

    args is a tuple of extra arguments to the ppf function (i.e. shape,
    location, scale), and size is the size of the output.  Note the ppf
    function must accept an array of q values to compute over.

    """
    U = random_sample(size=size)
    return ppf(*((U,) + args))


def randwcdf(cdf, mean=1.0, args=(), size=None):
    """
    Returns an array of randomly distributed integers given a CDF.

    Given a cumulative distribution function (CDF) returns an array of
    randomly distributed integers that would satisfy the CDF.

    Parameters
    ----------
    cdf : function
        CDF function that accepts a single value and `args`, and returns
        an single value.
    mean : float, optional
        The mean of the distribution which helps the solver.  Defaults
        to 1.0.
    args : tuple, optional
        Extra arguments to the cdf function (i.e. shape, location, scale)
    size : {int, None}, optional
        Is the size of the output.  If None, only 1 value will be returned.

    Returns
    -------
    randwcdf : ndarray
        Array of random numbers.

    Notes
    -----
    Can use the ``scipy.stats.distributions.*.cdf`` functions for the
    `cdf` parameter.

    """
    import scipy.optimize as optimize

    def _ppfopt(x, q, *nargs):
        newargs = (
         x,) + nargs
        return cdf(*newargs) - q

    def _ppf(q, *nargs):
        return optimize.fsolve(_ppfopt, mean, args=(q,) + nargs)

    _vppf = vectorize(_ppf)
    U = random_sample(size=size)
    return _vppf(*((U,) + args))