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

def sqr_root(a): return a**0.5

def procentify(a): return a/100

#Functions with additional parameters

def raise_to_y_power(a, y): return a**y

#?Other functions

#!Memory functions

#NOT WORKING
def memorize(a): 
    m1 = a 
    return m1

class M_button():
    def memorize_it(a): 
        m = a

    def memorize_show():
        print (m)

M_plus_button = M_button()

#TEST IN PROGRESS/WORKING

#*global

some = 0

def set_int(value):
    global some
    some = value

def get_int():
    return some

#*class
class internal_var:
    var = 0

    def set_int(self, value):
        self.var = value

    def get_int(self):
        return self.var

iv = internal_var()
iv.set_int(10)
print(iv.get_int())

#*class list
class internal_var:
    var = 0
    multivars = []

    def set_int(self, value):
        self.var = value

    def get_int(self):
        return self.var

    def add_to_list(self, value):
        self.multivars.append(value)

    def get_from_list(self, index):
        return self.multivars[index]

iv = internal_var()
iv.set_int(10)
print(iv.get_int())
iv.add_to_list(1)
print(iv.get_from_list(0))

#*class list + __init__
class internal_var:

    def __init__(self):
        self.var = 0
        self.multivars = []    

    def set_int(self, value):
        self.var = value

    def get_int(self):
        return self.var

    def add_to_list(self, value):
        self.multivars.append(value)

    def get_from_list(self, index):
        return self.multivars[index]

iv = internal_var()
iv.set_int(10)
print(iv.get_int())
iv.add_to_list(1)
print(iv.get_from_list(0))