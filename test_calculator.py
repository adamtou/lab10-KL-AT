import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        try:
            assert (add(1, 1) == 2)
            assert (add(1, 2) == 3)
            assert (add(5, 6) == 11)
        except:
            print('add error')

    def test_subtract(self): # 3 assertions
        try:
            assert(subtract(1, 1) == 0)
            assert(subtract(2,1) == 1)
            assert(subtract(6, 7) == -1)
        except:
            print('subtract error')

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        #     # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    #     fill in code

    def test_logarithm(self):  # 3 assertions
        self.assertEqual(logarithm(2, 8), 3.0)
        self.assertEqual(logarithm(4, 1), 0)
        self.assertEqual(logarithm(10, 100), 2)

    def test_log_invalid_base(self):
        try:
            with self.assertRaises(ValueError):
                print(logarithm(1, 5))
        except:
            print('logarithm base error')
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()