"""
Python calculation logics recreation as stand-alone functions for better customization.
"""

def square(a): return a**2

def cube(a): return a**3

def sqr_root(a): return a**0.5

def procentify(a): return a/100

#Memory functions
some = 0

def set_int(value):
    global some
    some = value

def get_int():
    return some