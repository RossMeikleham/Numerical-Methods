#Vandermonde Matrix creation

import numpy

#Creates a n * n Vandermonde matrix 
#given a list of n values. 
def vandermonde_matrix(values):
    rows = [[a ** i for i in range (0, len(values))] for a in values]
    return numpy.matrix(rows)
    
#Calculate determinant of a vandermonde matrix
def vandermonde_det(v):
    v = v.transpose()
    matrix = v.tolist()
    
    if len(matrix) == 1:
        return 1

    values = matrix[1] #Obtain initial vandermonde values
    
    det = 1
    for i in range (0, len(values)):
        for j in range (0, i):
            det *= (values[i] - values[j])

    return det
