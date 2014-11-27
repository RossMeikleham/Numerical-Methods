
from numericalmethods.linear_equations import *

a = numpy.matrix([[8.0, 1.0, -1.0], [2.0, 1.0, 9.0], [1.0, -7.0, 2.0]])
print(doolittle_lu_decomposition(a))
print(crout_lu_decomposition(a)) 

# Equations: 
# 8 = 8x + y - Z
# 12 = 2x + y + 9Z
# -4 = x - 7y + 2z

ax = numpy.matrix([[8.0, 1.0, -1.0], [2.0, 1.0, 9.0], [1.0, -7.0, 2.0]])
b = [8.0, 12.0, -4.0]

print(solve_eqns(ax, b))


