"""Math Funcs

Math utility functions to be used for function compositon
"""
def square(x):
    """squares a givein number"""
    return x ** 2

def cube(x):
    """cubes a given number"""
    return x ** 3

def less(x, y):
    """Compares two numbers and returns True if x is less than y"""
    return x < y

def greater(x, y):
    """Compares two numbers and retursn True if x is greater than y"""
    return x > y

def iseven(x):
    """Determines if a number is even"""
    return x % 2 == 0

def add(x, y):
    """Adds two numbers"""
    return x + y

def mult(x, y):
    """Multiplies two numbers"""
    return x * y

def div(x, y):
    """Divides two numbers"""
    return x / y
