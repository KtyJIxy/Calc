"""
Place, where Graphic User Interface comes to life.
"""

#from tkinter import * #?To avoid unused import errors import only required.
import tkinter as tk
from Calc.functions_main import * #?Same
#from Calc.functions_main import * #?To avoid unused import errors import only required.

# TODO:To use GUI-tkinter use class constructs. Remember __init__!
# TODO: Steal Lutz logic and make changes

class MainWindow(Frame): #Inherits tkinter Frame-class, builds up a main program window
    def __init__(self, parent=None):
        #Frame.__init__(self, parent)
        super().__init__(master) # ? Don't like calling the super(), but it was in example
        self.master = master
        self.master.title('PPCC')
        self.pack()
        self.invoke_basic_functions() # * calling custom function
        
    def invoke_basic_functions(self): #Activates all functions from functions_main.py
        import Calc.functions_main
        for functions in dir(Calc.functions_main):
            function = getattr(Calc.functions_main, functions)
            if callable(function):
                self.func() = tk.Button(self) # ! Doesn't work. Can't assign for some reason.
                self.func["text"] = "%function_name" %function
                self.func["command"] = self.function()
                self.func.pack(side="top")

root = tk.Tk()
app = Application(master=root)
app.mainloop() # ? From example. Required to startup tkinter-gui.