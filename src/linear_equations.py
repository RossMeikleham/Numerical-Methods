# Linear Equation solver in python
# Solves equations of form Ax = B, where 
# B and X are column vectors of size n
# and A is a matrix of dimension nxn

import numpy
from copy import copy, deepcopy

def solve_eqns(Ax, B):
    decomp = doolittle_lu_decomposition(Ax)
    l = decomp[0]
    u = decomp[1]

    n = len(B)

    z = []
    for i in range(n):
        z.append((B[i] - sum(z[j] * l[i, j] for j in range(i))) / l[i, i])

    # Back substitute to obtain solutions
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = ((z[i] - sum(x[j] * u[i, j] for j in range(i, n))) / u[i, i])
    
    return x 



# Performs Doolittle LU decomposition of an nxn matrix
# returns a tuple containing "lower triangle" of A (L)
# and "upper triangle" of A (U). Such that A = LU
def doolittle_lu_decomposition(A):
    rows = A.shape[0]
    cols = A.shape[1]
    n = rows

    L = numpy.identity(n)
    U = numpy.zeros((n, n))
    
    for j in range(n):
        for i in range(j + 1):
            s = sum(L[i, k] * U[k, j] for k in range(i))
            U[i, j] = A[i, j] - s
 
        for i in range(j, n):
            s = sum(L[i, k] * U[k, j] for k in range(j))
            L[i, j] = (A[i, j] - s) / U[j, j]

    return (L, U)


# Performs Crout LU decomposition of an nxn matrix
# returns a tuple containing "lower triangle" of A (L)
# and "upper triangle" of A (U). Such that A = LU
def crout_lu_decomposition(A):
    rows = A.shape[0]
    cols = A.shape[1]
    n = rows

    U = numpy.identity(n)
    L = numpy.zeros((n, n))
    
    for j in range(n):
        for i in range(j, n):
            s = sum(L[i, k] * U[k, j] for k in range(j))
            L[i, j] = A[i, j] - s
 
        for i in range(j, n):
            s = sum(L[j, k] * U[k, i] for k in range(j))
            U[j, i] = (A[j, i] - s) / L[j, j]

    return (L, U)

