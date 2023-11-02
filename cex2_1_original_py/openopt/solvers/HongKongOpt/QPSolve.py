# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\HongKongOpt\QPSolve.pyc
# Compiled at: 2012-12-08 11:04:59
"""
Copyright (c) 2010 Enzo Michelangeli and IT Vision Ltd

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
from .numpy import *
from LCPSolve import LCPSolve

def QPSolve(Q, e, A=None, b=None, Aeq=None, beq=None, lb=None, ub=None):
    """
    Note: if lb == None lower bounds are assumed to be -Inf
          if ub == None upper bounds are assumed to be +Inf
    i.e., x is NOT assumed to be non-negative by default
    This quadratic solver works by converting the QP problem 
    into an LCP problem. It does well up to few hundred variables
    and dense problems (it doesn't take advantage of sparsity).
    It fails if Aeq is not full row rank, or if Q is singular.
    """
    nvars = Q.shape[0]
    if lb != None:
        delmask = lb != -Inf
        addA = compress(delmask, eye(nvars), axis=0)
        addb = compress(delmask, lb, axis=0)
        A = vstack([A, -addA]) if A != None else -addA
        b = concatenate([b, -addb]) if b != None else -addb
    if ub != None:
        delmask = ub != Inf
        addA = compress(delmask, eye(nvars), axis=0)
        addb = compress(delmask, ub, axis=0)
        A = vstack([A, addA]) if A != None else addA
        b = concatenate([b, addb]) if b != None else addb
    n_ineq = A.shape[0]
    if Aeq != None:
        n_eq = Aeq.shape[0]
        B = vstack([
         hstack([Q, Aeq.T]),
         hstack([-Aeq, zeros((n_eq, n_eq))])])
        A0 = hstack([A, zeros((n_ineq, n_eq))])
    else:
        B = Q
        A0 = A
    BI = linalg.inv(B)
    A0BI = dot(A0, BI)
    M = dot(A0BI, A0.T)
    q = b + dot(A0BI, concatenate((e, beq))) if Aeq != None else b + dot(A0BI, e)
    s, lmbd, retcode = LCPSolve(M, q)
    if retcode[0] == 1:
        xmu = dot(BI, -concatenate([e + dot(A.T, lmbd), beq])) if Aeq != None else dot(BI, -(e + dot(A.T, lmbd)))
        x = xmu[:nvars]
    else:
        x = None
    return (x, retcode)