# Linear Equation solver in python
# Solves equations of form Ax = B, where 
# B and X are column vectors of size n
# and A is a matrix of dimension nxn

import numpy
from copy import copy, deepcopy

def solve_eqns(Ax, B):
    decomp = crout_lu_decomposition(Ax)
    l = decomp[0]
    u = decomp[1]

    n = len(B)

    z = []
    for i in range(0, n):
        z.append((B[i] - sum(z[j] * l[i, j] for j in range(0, i))) / l[i, i])

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

    U = deepcopy(A)
    # Calculate U 
    for i in range(0, n):
        for j in range(i + 1, n):
            mul = U[j, i] / U[i, i]
            for k in range(0, n):
                U[j, k] -= (U[i, k] * mul)
    
    L = deepcopy(A)
    # Calculate L
    for row in range(0, n):
        for col in range(0, row):
            for i in range(0, col):
                L[row, col] -= (L[row, i] * U[i, row - 1])
            L[row, col] /= U[col, col]

    # Get rid of "upper part" of L matrix
    for row in range(0, n):
        for col in range(row, n):
            L[row,col] = 1 if row == col else 0

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
    
    for j in range(0, n):
        for i in range(j, n):
            sum = 0
            for k in range(0, j):
                sum += L[i, k] * U[k, j] 
            
            L[i, j] = A[i, j] - sum
 
        for i in range(j, n):
            sum = 0;
            for k in range(0, j):
                sum += L[j, k] * U[k, i];
            U[j, i] = (A[j, i] - sum) / L[j, j]

    return (L, U)

