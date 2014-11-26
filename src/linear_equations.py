# Linear Equation solver in python
# Solves equations of form Ax = B, where 
# B and X are column vectors of size n
# and A is a matrix of dimension nxn

import numpy
from copy import copy, deepcopy

def solve_eqns(Ax, B):
    decomp = lu_decomposition(Ax)
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
def lu_decomposition(A):
    rows = A.shape[0]
    cols = A.shape[1]
    
    U = deepcopy(A)
    # Calculate U 
    for i in range(0, rows):
        for j in range(i + 1, rows):
            mul = U[j, i] / U[i, i]
            for k in range(0, cols):
                U[j, k] -= (U[i, k] * mul)
    
    L = deepcopy(A)
    # Calculate L
    for row in range(0, rows):
        for col in range(0, row):
            for i in range(0, col):
                L[row, col] -= (L[row, i] * U[i, row - 1])
            L[row, col] /= U[col, col]

    # Get rid of "upper part" of L matrix
    for row in range(0, rows):
        for col in range(row, cols):
            L[row,col] = 1 if row == col else 0

    return (L, U)

