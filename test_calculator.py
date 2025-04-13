# https://github.com/adamtou/lab10-KL-AT/tree/main
# Partner 1: Kevin Liu
# Partner 2: Adam Touati

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        try:
            assert(add(1, 9) == 10)
            assert(add(1, -9) == -8)
            assert(add(-1, -9) == -10)
        except:
            print('add error')

    def test_subtract(self): # 3 assertions
        try:
            assert(subtract(1, 9) == -8)
            assert(subtract(2, 2) == 0)
            assert(subtract(9, -1) == 10)
        except:
            print('subtract error')

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        try:
            assert(mul(0, 9000) == 0)
            assert(mul(-9, 11) == -99)
            assert(mul(11, 11) == 121)
        except:
            print('mult error')

    def test_divide(self): # 3 assertions
        try:
            assert(div(1, 900) == 900)
            assert(div(90, -180) == -2)
            assert(div(30, 600) == 20)
        except:
            print('div error')
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        try:
            with self.assertRaises(ZeroDivisionError):
                div(0, 5)
        except:
            print('zero division error')

    def test_logarithm(self): # 3 assertions
        try:
            assert(logarithm(2, 1) == 0)
            assert(logarithm(3, 3) == 1)
            assert(logarithm(9, 729) == 3)
        except:
            print('logarithm error')

    def test_log_invalid_base(self): # 1 assertion
        try:
            with self.assertRaises(ValueError):
                logarithm(1, 9)
        except:
            print('invalid log error')
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        try:
            with self.assertRaises(ValueError):
                logarithm(0, 5)
        except:
            print('invalid log error')


    def test_hypotenuse(self): # 3 assertions
        try:
            assert(hypotenuse(3, 4) == 5)
            assert(hypotenuse(-5, 12) == 13)
            assert(hypotenuse(-7, -24) == 25)
        except:
            print('hyp error')

    def test_sqrt(self): # 3 assertions
        try:
            assert(square_root(1) == 1)
            assert(square_root(4) == 2)
            assert(square_root(729) == 27)
        except:
            print('sqrt error')

# Do not touch this
if __name__ == "__main__":
    unittest.main()