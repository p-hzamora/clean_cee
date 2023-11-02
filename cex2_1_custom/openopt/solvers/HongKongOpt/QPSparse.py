# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\solvers\HongKongOpt\QPSparse.pyc
# Compiled at: 2012-12-08 11:04:59
"""
pname, e, Q, A=None, b=None, Aeq=None, beq=None, lb=None, ub=None, c0 = MPSparse(filename)

Reads the description of a QP problem from a file in the extended
MPS format (QPS) described by Istvan Maros and Csaba Meszaros at:
http://www.sztaki.hu/~meszaros/public_ftp/qpdata/qpdata.ps

Returns a tuple (pname, e, Q, Aeq, beq, lb, ub, c0)
name: string
all others: numpy arrays

QPS Format:

The QP problems are assumed to be in the following form:

min f(x) = e'x + 1/2 x' Q x,  Q symmetric and positive semidefinite
                                       
subject to      Aeq x = beq,
                l <= x <= u.

After the BOUNDS section of MPS there is an new section introduced
by a QUADOBJ record followed by columnwise elements of Q; row and
columns are column names of A. Being the matrix symmetrical,
only lower triangular elements are listed.

---------------------------------------------------------------------
Field:    1           2          3         4         5         6
Columns:  2-3        5-12      15-22     25-36     40-47     50-61
0        1         2         3         4         5         6
1234567890123456789012345678901234567890123456789012345678901  << column
 11 22222222  33333333  444444444444   55555555  666666666666  << field
---------------------------------------------------------------

          NAME   problem name

          ROWS

           type     name

          COLUMNS
                   column       row       value     row      value
                    name        name                name
          RHS
                    rhs         row       value     row      value
                    name        name                name
          RANGES
                    range       row       value     row      value
                    name        name                name
          BOUNDS

           type     bound       column     value
                    name        name
          ENDATA
---------------------------------------------------------------------

---------------------------------------------------------------
NAME          QP example
ROWS
 N  obj
 G  r1
 L  r2
COLUMNS
 11 22222222  33333333  444444444444   55555555  666666666666  << field
    c1        r1                 2.0   r2                -1.0
    c1        obj                1.5
    c2        r1                 1.0   r2                 2.0
    c2        obj               -2.0
RHS
    rhs1      r1                 2.0   r2                 6.0
BOUNDS
 UP bnd1      c1                20.0
QUADOBJ
    c1        c1                 8.0
    c1        c2                 2.0
    c2        c2                10.0
ENDATA
---------------------------------------------------------------

"""
from .numpy import *

def QPSparse(filename):
    pname = e = Q = A = b = Aeq = beq = lb = ub = None
    c0 = 0.0
    f = open(filename, 'r')
    section = None
    rowtype = {}
    colnum = {}
    colcnt = 0
    acnt = 0
    aeqcnt = 0
    aindx = {}
    aeqindx = {}
    objcoef = {}
    RHSdic = {}
    RANGESdic = {}
    ucnt = 0
    qcnt = 0
    lineno = 0
    for line in f:
        lineno += 1
        line = line.upper().strip('\n\r')
        f1 = line[1:3].strip()
        f2 = line[4:12].strip()
        f3 = line[14:22].strip()
        f4 = line[24:36].strip().replace('D', 'E')
        f4 = 0.0 if f4 == '' else float(f4)
        f5 = line[39:47].strip()
        f6 = line[49:61].strip().replace('D', 'E')
        f6 = 0.0 if f6 == '' else float(f6)
        if line[0] != ' ':
            if section == 'ROWS':
                Alist = [ {} for i in range(acnt) ]
                Aeqlist = [ {} for i in range(aeqcnt) ]
            elif section == 'COLUMNS':
                Q = zeros((colcnt, colcnt))
                ub = array([Inf] * colcnt)
                lb = zeros(colcnt)
            elif section == 'RHS':
                pass
            elif section == 'RANGES':
                pass
            elif section == 'BOUNDS':
                if ucnt == 0:
                    ub = None
            elif section == 'QUADOBJ':
                if qcnt == 0:
                    Q = None
            if f1 == 'AM':
                section = 'NAME'
            else:
                if f1 == 'OW':
                    section = 'ROWS'
                elif f1 == 'OL':
                    section = 'COLUMNS'
            if f1 == 'HS':
                section = 'RHS'
            else:
                if f1 == 'AN':
                    section = 'RANGES'
                elif f1 == 'OU':
                    section = 'BOUNDS'
            if f1 == 'UA':
                section = 'QUADOBJ'
            elif f1 == 'ND':
                section = None
                break
            else:
                f.close()
                raise ValueError('invalid indicator record in line ' + str(lineno) + ': "' + line + '"')
        elif section == 'NAME':
            pname = f3
        elif section == 'ROWS':
            rname = f2
            if f1 == 'N':
                rowtype[rname] = 'N'
                obj = rname
            elif f1 == 'G':
                rowtype[rname] = 'G'
                aindx[rname] = acnt
                acnt += 1
            if f1 == 'L':
                rowtype[rname] = 'L'
                aindx[rname] = acnt
                acnt += 1
            elif f1 == 'E':
                rowtype[rname] = 'E'
                aeqindx[rname] = aeqcnt
                aeqcnt += 1
            else:
                f.close()
                raise ValueError('invalid row type "' + f1 + '" in line ' + str(lineno) + ': "' + line + '"')
        elif section == 'COLUMNS':
            cname = f2
            rnames = [0, 0]
            vals = [0, 0]
            if cname not in colnum:
                colnum[cname] = colcnt
                colcnt += 1
            rnames[0] = f3
            vals[0] = f4
            rnames[1] = f5
            vals[1] = f6
            for i in (0, 1):
                rn = rnames[i]
                value = vals[i]
                if rn == '':
                    break
                if rn == obj:
                    objcoef[cname] = value
                elif rowtype[rn] == 'L':
                    Alist[aindx[rn]][cname] = value
                elif rowtype[rn] == 'G':
                    Alist[aindx[rn]][cname] = -value
                elif rowtype[rn] == 'E':
                    Aeqlist[aeqindx[rn]][cname] = value

        elif section == 'RHS':
            rnames = [0, 0]
            vals = [0, 0]
            rnames[0] = f3
            vals[0] = f4
            rnames[1] = f5
            vals[1] = f6
            for i in (0, 1):
                rname = rnames[i]
                value = vals[i]
                if rname == '':
                    break
                RHSdic[rname] = value

        elif section == 'RANGES':
            rnames = [0, 0]
            vals = [0, 0]
            rnames[0] = f3
            vals[0] = f4
            rnames[1] = f5
            vals[1] = f6
            for i in (0, 1):
                rname = rnames[i]
                value = vals[i]
                if rname == '':
                    break
                RANGESdic[rname] = value

        elif section == 'BOUNDS':
            ic = colnum[f3]
            val = f4
            if f1 == 'UP':
                ub[ic] = f4
                ucnt += 1
            else:
                if f1 == 'LO':
                    lb[ic] = f4
                elif f1 == 'FX':
                    raise ValueError('fixed variable (FX) bound not supported in line ' + str(lineno) + ': "' + line + '"')
            if f1 == 'FR':
                lb[ic] = -Inf
                ub[ic] = Inf
            else:
                if f1 == 'MI':
                    lb[ic] = -Inf
                elif f1 == 'BV':
                    raise ValueError('binary value (BV) bound not supported in line ' + str(lineno) + ': "' + line + '"')
        elif section == 'QUADOBJ':
            ic1 = colnum[f2]
            ic2 = colnum[f3]
            val = f4
            Q[(ic1, ic2)] = val
            if ic1 != ic2:
                Q[(ic2, ic1)] = val
            qcnt += 1

    f.close()
    if section != None:
        raise EOFError('unexpected EOF while in section ' + section)
    if acnt > 0:
        A = zeros((acnt, colcnt))
        b = zeros(acnt)
        for rn in range(acnt):
            for c in Alist[rn]:
                A[(rn, colnum[c])] = Alist[rn][c]

    if aeqcnt > 0:
        Aeq = zeros((aeqcnt, colcnt))
        beq = zeros(aeqcnt)
        for rn in range(aeqcnt):
            for c in Aeqlist[rn]:
                Aeq[(rn, colnum[c])] = Aeqlist[rn][c]

    for rname in RHSdic:
        value = RHSdic[rname]
        rt = rowtype[rname]
        if rt == 'L':
            b[aindx[rname]] = value
        elif rt == 'G':
            b[aindx[rname]] = -value
        elif rt == 'E':
            beq[aeqindx[rname]] = value
        elif rt == 'N':
            c0 = -value

    if A != None:
        addA = zeros((len(RANGESdic), A.shape[1]))
        addb = zeros(len(RANGESdic))
        for rname in RANGESdic:
            index = aindx[rname]
            value = RANGESdic[rname]
            rt = rowtype[rname]
            if rt == 'L':
                b1 = b[index] + abs(value)
            elif rt == 'G':
                b1 = b[index] - abs(value)
            elif rt == 'E':
                raise ValueError('RANGES for rows of type E not yet supported in line ' + str(lineno) + ': "' + line + '"')
            addA[index, :] = -A[index, :]
            addb[index] = -b1

        A = vstack([A, addA])
        b = concatenate([b, addb])
    e = zeros(colcnt)
    for c in objcoef:
        e[colnum[c]] = objcoef[c]

    nvars = e.shape[0]
    if lb != None and (lb == array([-Inf] * nvars)).all():
        lb = None
    if ub != None and (ub == array([Inf] * nvars)).all():
        ub = None
    return (pname, e, Q, A, b, Aeq, beq, lb, ub, c0)