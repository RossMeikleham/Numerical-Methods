
import unittest
from numericalmethods.romberg import *
from math import log

class TestsRombergIntegration(unittest.TestCase):
    
    #Test integration with e^x
    def test_exp(self):
        fn = lambda x : exp(x)
        a = 1
        b = 1
        self.assertEqual(romberg(a, b, fn, 10), 0)

        fn = lambda x : exp(x)
        a = 0
        b = 1
        self.assertAlmostEqual(romberg(a, b, fn, 10), exp(1) - 1, places = 10)


    #Test integration of constant expression
    def test_const(self):
        fn = lambda x : 1
        a = 32
        b = 50
        self.assertEqual(romberg(a, b, fn, 10), b - a)

   #Test integration of 1/x
    def test_log(self):
        fn = lambda x : 1/x #integration of 1/x = log(x)
        a = 5
        b = 10
        self.assertAlmostEqual(romberg(a, b , fn, 10), log(2))


if __name__ == '__main__':
    unittest.main()
