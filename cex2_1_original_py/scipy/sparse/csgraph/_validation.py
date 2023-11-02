# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\sparse\csgraph\_validation.pyc
# Compiled at: 2013-02-16 13:27:32
from __future__ import division, print_function, absolute_import
import numpy as np
from scipy.sparse import csr_matrix, isspmatrix, isspmatrix_csc, isspmatrix_csr
from ._tools import csgraph_to_dense, csgraph_from_dense, csgraph_masked_from_dense, csgraph_from_masked
DTYPE = np.float64

def validate_graph(csgraph, directed, dtype=DTYPE, csr_output=True, dense_output=True, copy_if_dense=False, copy_if_sparse=False, null_value_in=0, null_value_out=np.inf, infinity_null=True, nan_null=True):
    """Routine for validation and conversion of csgraph inputs"""
    if not (csr_output or dense_output):
        raise ValueError('Internal: dense or csr output must be true')
    if not directed and isspmatrix_csc(csgraph):
        csgraph = csgraph.T
    if isspmatrix(csgraph):
        if csr_output:
            csgraph = csr_matrix(csgraph, dtype=DTYPE, copy=copy_if_sparse)
        else:
            csgraph = csgraph_to_dense(csgraph, null_value=null_value_out)
    elif np.ma.is_masked(csgraph):
        if dense_output:
            mask = csgraph.mask
            csgraph = np.array(csgraph.data, dtype=DTYPE, copy=copy_if_dense)
            csgraph[mask] = null_value_out
        else:
            csgraph = csgraph_from_masked(csgraph)
    elif dense_output:
        csgraph = csgraph_masked_from_dense(csgraph, copy=copy_if_dense, null_value=null_value_in, nan_null=nan_null, infinity_null=infinity_null)
        mask = csgraph.mask
        csgraph = np.asarray(csgraph.data, dtype=DTYPE)
        csgraph[mask] = null_value_out
    else:
        csgraph = csgraph_from_dense(csgraph, null_value=null_value_in, infinity_null=infinity_null, nan_null=nan_null)
    if csgraph.ndim != 2:
        raise ValueError('compressed-sparse graph must be two dimensional')
    if csgraph.shape[0] != csgraph.shape[1]:
        raise ValueError('compressed-sparse graph must be shape (N, N)')
    return csgraph