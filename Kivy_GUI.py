"""
"Migration" to kivy.
"""

#? p.37 Basics
#? p.43 Limiting Kivy
#? p.51 Touch/buttons
#? p.56 How to avoid death loops
#? p.58 Triggers
#? p.59 Events. Custom events must be registred in __EventDispatcher__ class. Callback and __*args__
#? p.60 List of Properties. Declaration at __class__ level with __**kwargs__
#? p.74 __Layouts__
#? p.82 Backgrounds
#? p.97 __KVLANG__
#? p.115 package for Android
#? p.129 License. __Maybe__ abolish VSC (stritc licensing)
#? p.541 Color Picker
#? p.unknown kivy.uix.settings __module__ - way to implement settings in an app.
#? p.unknown CodeInput. Solution to implementing code support at hand!
#? p.unknown RstDocument - solution to editable PyReader!

import kivy
kivy.require('2.0.0') #! Current is 2.0.0. as of 08/01/2021.
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from Calc.functions_main import *

class MainScreen(GridLayout):
    def calculate(self, calculation): 
        if calculation: 
            try: 
                self.display.text = str(eval(calculation)) 
            except Exception: 
                self.display.text = "Error"

class CalcApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    CalcApp().run()