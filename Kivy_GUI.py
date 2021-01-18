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
#? p.unknown kivy.uix.settings __module__ - way to implement settings in an app.
#? p.unknown CodeInput. Solution to implementing code support at hand!
#? p.unknown RstDocument - solution to editable PyReader!

import kivy
import time #* Test purposes
kivy.require('2.0.0') #! Current is 2.0.0. as of 08/01/2021.
from kivy.app import App #* Example code below
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class MainScreen(GridLayout): #TODO high possibility of not working as intended due to __wrong__ __class__ inheritance.
    def __init__(self, **kwargs):
        super(Calc, self).__init__(**kwargs) #* I fucking hate __super__ calls
        self.cols = 2 #! No, more. Plan.
        self.rows = 2 #! Purely, my guess. Check.
        #*Nice to know such commands exist. 
        #! Delete in future
        #self.add_widget(Label(text='User Name')) 
        #self.username = TextInput(multiline=False)
        #self.add_widget(self.username)
        #self.add_widget(Label(text='password'))
        #self.password = TextInput(password=True, multiline=False)
        #self.add_widget(self.password)

class Calc(App):
    def build(self):
        #return Label(text='Hello world') #? Example code. Label being root widget application.
        #! import functions_main.py -- GO BACK TO __MainScreen__
        time.sleep(20)
        return MainScreen()
        time.sleep(20)
        

if __name__ == '__main__': #? really neccessary?
    Calc().run()