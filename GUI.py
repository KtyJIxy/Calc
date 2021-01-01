"""
Place, where Graphic User Interface comes to life.
"""

from tkinter import * #To avoid unused import errors import only required.
from Calc.functions_main import * #Same
from Calc.functions_main import * #To avoid unused import errors import only required.

#To use GUI-tkinter use class constructs. Remember __init__!
#Steal Lutz logic and make changes

class MainWindow(Frame): #Inherits tkinter Frame-class, builds up a main program window
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.master.title('PPCC')
        
    def invoke_basic_functions(self): #Activates all functions from functions_main.py
        for functions in dir(Calc.functions_main):
            function = getattr(Calc.functions_main, functions)
            if callable(function):
                function() #Requires re-work to invoke actual buttons