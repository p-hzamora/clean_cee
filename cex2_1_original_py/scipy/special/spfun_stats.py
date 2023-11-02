# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\special\spfun_stats.pyc
# Compiled at: 2013-02-16 13:27:32
"""Some more special functions which may be useful for multivariate statistical
analysis."""
from __future__ import division, print_function, absolute_import
import numpy as np
from scipy.special import gammaln as loggam
__all__ = [
 'multigammaln']

def multigammaln(a, d):
    r"""Returns the log of multivariate gamma, also sometimes called the
    generalized gamma.

    Parameters
    ----------
    a : ndarray
        The multivariate gamma is computed for each item of `a`.
    d : int
        The dimension of the space of integration.

    Returns
    -------
    res : ndarray
        The values of the log multivariate gamma at the given points `a`.

    Notes
    -----
    The formal definition of the multivariate gamma of dimension d for a real a
    is::

        \Gamma_d(a) = \int_{A>0}{e^{-tr(A)\cdot{|A|}^{a - (m+1)/2}dA}}

    with the condition ``a > (d-1)/2``, and ``A > 0`` being the set of all the
    positive definite matrices of dimension s.  Note that a is a scalar: the
    integrand only is multivariate, the argument is not (the function is
    defined over a subset of the real set).

    This can be proven to be equal to the much friendlier equation::

        \Gamma_d(a) = \pi^{d(d-1)/4}\prod_{i=1}^{d}{\Gamma(a - (i-1)/2)}.

    References
    ----------
    R. J. Muirhead, Aspects of multivariate statistical theory (Wiley Series in
    probability and mathematical statistics).

    """
    a = np.asarray(a)
    if not np.isscalar(d) or np.floor(d) != d:
        raise ValueError('d should be a positive integer (dimension)')
    if np.any(a <= 0.5 * (d - 1)):
        raise ValueError('condition a (%f) > 0.5 * (d-1) (%f) not met' % (
         a, 0.5 * (d - 1)))
    res = d * (d - 1) * 0.25 * np.log(np.pi)
    if a.size == 1:
        axis = -1
    else:
        axis = 0
    res += np.sum(loggam([ a - (j - 1.0) / 2 for j in range(1, d + 1) ]), axis)
    return res