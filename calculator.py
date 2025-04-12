import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    try:
        return b/a
    except:
        if(a == 0):
            raise ZeroDivisionError
def log(a, b):
    try:
        return math.log(b, a)
    except:
        if (b == 1 or b <= 0 or b):
            raise ValueError

