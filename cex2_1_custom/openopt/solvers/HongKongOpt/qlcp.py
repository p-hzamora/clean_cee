# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\HongKongOpt\qlcp.pyc
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
from scipy.linalg import lu_factor, lu_solve
from LCPSolve import LCPSolve

def qlcp(Q, e, A=None, b=None, Aeq=None, beq=None, lb=None, ub=None, QI=None):
    """
    Minimizes e'x + 1/2 x'Q x subject to optional inequality, equality and
    box-bound (converted ti inequality) constraints.
    Note: x is NOT assumed to be non-negative by default.
    This quadratic solver works by converting the QP problem 
    into an LCP problem. It does well up to few hundred variables
    and dense problems (it doesn't take advantage of sparsity).
    If there are equality constraints, the problem may be feasible 
    even when Q is singular. If Q is not singular, it is possible to
    precompute its inverse and pass it as parameter QI (this is
    useful in SQP applications with approximation of the Hessian and
    its inverse, such as DFP or BFGS.
    Returns: x, the solution (or None in case of failure due to ray 
    termination in the LCP solver).
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
    n_ineq = A.shape[0] if A != None else 0
    if Aeq != None:
        n_eq = Aeq.shape[0]
        B = vstack([
         hstack([Q, Aeq.T]),
         hstack([-Aeq, zeros((n_eq, n_eq))])])
        A0 = hstack([A, zeros((n_ineq, n_eq))]) if A != None else None
    else:
        B = Q
        A0 = A
    ee = concatenate((e, beq)) if Aeq != None else e
    if A == None:
        xmu = linalg.solve(B, ee)
        x = xmu[:nvars]
    else:
        if QI == None:
            BI = linalg.inv(B)
        elif Aeq == None:
            BI = QI
        else:
            QIAeqT = dot(QI, Aeq.T)
            SQI = linalg.inv(dot(Aeq, QIAeqT))
            QIAeqTSQI = dot(QIAeqT, SQI)
            BI = vstack([
             hstack([QI - dot(dot(QIAeqTSQI, Aeq), QI), -QIAeqTSQI]),
             hstack([dot(SQI, dot(Aeq, QI)), SQI])])
        A0BI = dot(A0, BI)
        M = dot(A0BI, A0.T)
        q = b + dot(A0BI, ee)
        s, lmbd, retcode = LCPSolve(M, q)
        if retcode[0] == 1:
            kk = -concatenate([e + dot(A.T, lmbd), beq]) if Aeq != None else -(e + dot(A.T, lmbd))
            xmu = dot(BI, kk)
            x = xmu[:nvars]
        else:
            x = None
    return x