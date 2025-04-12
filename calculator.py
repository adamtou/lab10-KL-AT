import math
<<<<<<< HEAD
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
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def logarithm(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise Exception(ValueError)
    return math.log(b, a)

def exponent(a, b):
    return a ** b