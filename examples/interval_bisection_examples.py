from numericalmethods.intervalbisection import *

fn = lambda x : x**3 - x - 2
print(interval_bisection(fn, 1, 2, 5))
