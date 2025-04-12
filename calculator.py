import math

def square_root(a):
    if a < 0:
        raise Exception(ValueError)
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)
def add(a, b): 
    return a + b
def subtract(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    try:
        return b/a
    except:
        if(a == 0):
            raise ZeroDivisionError

def logarithm(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b