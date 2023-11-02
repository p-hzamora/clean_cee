# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\polynomial\__init__.pyc
# Compiled at: 2013-04-07 07:04:04
"""
A sub-package for efficiently dealing with polynomials.

Within the documentation for this sub-package, a "finite power series,"
i.e., a polynomial (also referred to simply as a "series") is represented
by a 1-D numpy array of the polynomial's coefficients, ordered from lowest
order term to highest.  For example, array([1,2,3]) represents
``P_0 + 2*P_1 + 3*P_2``, where P_n is the n-th order basis polynomial
applicable to the specific module in question, e.g., `polynomial` (which
"wraps" the "standard" basis) or `chebyshev`.  For optimal performance,
all operations on polynomials, including evaluation at an argument, are
implemented as operations on the coefficients.  Additional (module-specific)
information can be found in the docstring for the module of interest.

"""
import warnings
from polynomial import Polynomial
from chebyshev import Chebyshev
from legendre import Legendre
from hermite import Hermite
from hermite_e import HermiteE
from laguerre import Laguerre
from numpy.testing import Tester
test = Tester().test
bench = Tester().bench