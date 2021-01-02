"""
Basic python calculation logics recreation as stand-alone functions for better customization.
"""

"""def func_create(func_name): #Не работает
    return exec(func_name)

if __name__ == "__main__":
    multi = func_create("__add__") """

#Basic functions, requires two arguments
def addition(a, b): return a+b

def substraction(a,b): return a-b

def multiplying(a,b): return a*b

def division(a,b): return a/b

#Single argument based functions

def square(a): return a**2

def cube(a): return a**3

def root(a): return a**0.5

def procentify(a): return a/100

#Functions with additional parameters

def raise_to_y_power(a, y): return a**y

#Other functions