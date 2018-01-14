"""Math Funcs

Math utility functions to be used for function compositon
"""
def square(x_val):
    """squares a givein number"""
    return x_val ** 2

def cube(x_val):
    """cubes a given number"""
    return x_val ** 3

def less(x_val, y_val):
    """Compares two numbers and returns True if x is less than y"""
    return x_val < y_val

def greater(x_val, y_val):
    """Compares two numbers and retursn True if x is greater than y"""
    return x_val > y_val

def iseven(x_val):
    """Determines if a number is even"""
    return x_val % 2 == 0

def add(x_val, y_val):
    """Adds two numbers"""
    return x_val + y_val

def mult(x_val, y_val):
    """Multiplies two numbers"""
    return x_val * y_val

def div(x_val, y_val):
    """Divides two numbers"""
    return x_val / y_val
