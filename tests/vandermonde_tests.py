
import unittest
from numericalmethods.vandermonde import *

class TestsVandermonde(unittest.TestCase):
    
    #Test generating Vandermonde matrix
    def test_matrix(self):
        v = vandermonde_matrix([1,2,3,4])
        self.assertEqual(v.tolist(), [[1,1,1,1],[1,2,4,8],[1,3,9,27],[1,4,16,64]])

    #Test determinant of Vandermonde matrix with more than 1 element
    def test_det_multi(self):
        d = vandermonde_det(vandermonde_matrix([1,2,3,4]))
        self.assertEqual(d, 12)

    #Test determinant of Vandermonde matrix with exactly 1 element
    def test_det_single(self):
        d = vandermonde_det(vandermonde_matrix([1]))
        self.assertEqual(d, 1)



#vandermonde_det
if __name__ == '__main__':
    unittest.main()
