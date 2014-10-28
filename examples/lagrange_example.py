from numericalmethods.lagrange import *


lp = lagrange_polys([-1.5, -0.75, 0, 0.75, 1.5])
l0 = lp[0]
l1 = lp[1]
print(l0(1))
print(l1(1))

ilp = interpolating_lagrange_poly([(-1.5,-14.1014),(-0.75,-0.931596),(0,0),(0.75,0.931596),(1.5,14.1014)])
print(ilp(1))
