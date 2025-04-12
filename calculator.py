import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise Exception(ZeroDivisionError)
    return b / a

def logarithm(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise Exception(ValueError)
    return math.log(b, a)

def exponent(a, b):
    return a ** b