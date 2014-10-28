
import unittest
from numericalmethods.lagrange import *

class TestsLagrange(unittest.TestCase):
    
    #Test generating Vandermonde matrix
    def test_lagrange(self):
        points = [(-1.5,-14.1014),(-0.75,-0.931596),(0,0),(0.75,0.931596),(1.5,14.1014)]
        #Should generate function 4.834848x^3 - 1.477474x
        ilp = interpolating_lagrange_poly(points)
        expected_fn = lambda x : (4.834848 *(x ** 3)) - (1.477474 * x)

        #Test with a bunch of values
        for i in range (1, 50):
            self.assertAlmostEqual(expected_fn(i), ilp(i), places = 1)
        



#vandermonde_det
if __name__ == '__main__':
    unittest.main()
