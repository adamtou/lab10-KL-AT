# https://github.com/adamtou/lab10-KL-AT/tree/main
# Partner 1: Kevin Liu
# Partner 2: Adam Touati

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 asser
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
            with self.assertRaises(ValueError):
                square_root(-1)
        except:
            print('invalid sqrt error')

# Do not touch this
if __name__ == "__main__":
    unittest.main()