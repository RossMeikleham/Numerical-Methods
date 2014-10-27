from functools import reduce
from functools import partial

# Calculate the interpolation polynomial of a given list of x and y tuple pairs
def interpolating_lagrange_poly(pairs):
    #Extract x and y values from tuples
    xs = [x[0] for x in pairs] 
    ys = [y[1] for y in pairs]

    lps = lagrange_polys(xs) 
    return lambda x : sum((ys[i] * lps[i](x)) for i in range(0, len(pairs)))


# Calculates Lagrange basis functions for a given
# list of data points
def lagrange_polys(points):

    # Calculate kth Larange basis polynomial for
    # a given list of data points
    def lagrange_poly(k):
        
        get_term = lambda i,x: 1 if i == k else ((x - points[i]) / (points[k] - points[i]))
        terms = [partial(get_term, i) for i in range(0, len(points))]
        return (lambda x: reduce(lambda a, b: a * b, [term(x) for term in terms]))
    
    return [lagrange_poly(k) for k in range(0, len(points))]



#Examples
lp = lagrange_polys([-1.5, -0.75, 0, 0.75, 1.5])
l0 = lp[0]
l1 = lp[1]
print(l0(1))
print(l1(1))

ilp = interpolating_lagrange_poly([(-1.5,-14.1014),(-0.75,-0.931596),(0,0),(0.75,0.931596),(1.5,14.1014)])
print(ilp(1))

