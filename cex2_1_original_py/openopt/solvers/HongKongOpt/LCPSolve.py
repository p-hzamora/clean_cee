# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\HongKongOpt\LCPSolve.pyc
# Compiled at: 2012-12-08 11:04:59
""" LCPSolve(M,q): procedure to solve the linear complementarity problem:

       w = M z + q
       w and z >= 0
       w'z = 0

   The procedure takes the matrix M and vector q as arguments.  The
   procedure has three returns.  The first and second returns are
   the final values of the vectors w and z found by complementary
   pivoting.  The third return is a 2 by 1 vector.  Its first
   component is a 1 if the algorithm was successful, and a 2 if a
   ray termination resulted.  The second component is the value of
   the artificial variable upon termination of the algorithm.
   The third component is the number of iterations performed in the
   outer loop.
 
   Derived from: http://www1.american.edu/academic.depts/cas/econ/gaussres/optimize/quadprog.src
   (original GAUSS code by Rob Dittmar <dittmar@stls.frb.org> )

   Lemke's Complementary Pivot algorithm is used here. For a description, see:
   http://ioe.engin.umich.edu/people/fac/books/murty/linear_complementarity_webbook/kat2.pdf

Copyright (c) 2010 Rob Dittmar, Enzo Michelangeli and IT Vision Ltd

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

def LCPSolve(M, q, pivtol=1e-08):
    rayTerm = False
    loopcount = 0
    if (q >= 0.0).all():
        w = q
        z = zeros_like(q)
        retcode = 0.0
    else:
        dimen = M.shape[0]
        tableau = hstack([eye(dimen), -M, -ones((dimen, 1)), asarray(asmatrix(q).T)])
        basis = range(dimen)
        locat = argmin(tableau[:, 2 * dimen + 1])
        basis[locat] = 2 * dimen
        cand = locat + dimen
        pivot = tableau[locat, :] / tableau[(locat, 2 * dimen)]
        tableau -= tableau[:, 2 * dimen:2 * dimen + 1] * pivot
        tableau[locat, :] = pivot
        oldDivideErr = seterr(divide='ignore')['divide']
        while amax(basis) == 2 * dimen:
            loopcount += 1
            eMs = tableau[:, cand]
            missmask = eMs <= 0.0
            quots = tableau[:, 2 * dimen + 1] / eMs
            quots[missmask] = Inf
            locat = argmin(quots)
            if abs(eMs[locat]) > pivtol and not missmask.all():
                pivot = tableau[locat, :] / tableau[(locat, cand)]
                tableau -= tableau[:, cand:cand + 1] * pivot
                tableau[locat, :] = pivot
                oldVar = basis[locat]
                basis[locat] = cand
                if oldVar >= dimen:
                    cand = oldVar - dimen
                else:
                    cand = oldVar + dimen
            else:
                rayTerm = True
                break

        seterr(divide=oldDivideErr)
        vars = zeros(2 * dimen + 1)
        vars[basis] = tableau[:, 2 * dimen + 1]
        w = vars[:dimen]
        z = vars[dimen:2 * dimen]
        retcode = vars[2 * dimen]
    if rayTerm:
        retcode = (
         2, retcode, loopcount)
    else:
        retcode = (
         1, retcode, loopcount)
    return (
     w, z, retcode)