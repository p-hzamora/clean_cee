# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\sparse\linalg\eigen\arpack\__init__.pyc
# Compiled at: 2013-02-16 13:27:32
"""
Eigenvalue solver using iterative methods.

Find k eigenvectors and eigenvalues of a matrix A using the
Arnoldi/Lanczos iterative methods from ARPACK [1]_,[2]_.

These methods are most useful for large sparse matrices.

  - eigs(A,k)
  - eigsh(A,k)

References
----------
.. [1] ARPACK Software, http://www.caam.rice.edu/software/ARPACK/
.. [2] R. B. Lehoucq, D. C. Sorensen, and C. Yang,  ARPACK USERS GUIDE:
   Solution of Large Scale Eigenvalue Problems by Implicitly Restarted
   Arnoldi Methods. SIAM, Philadelphia, PA, 1998.

"""
from __future__ import division, print_function, absolute_import
from ...arpack import *