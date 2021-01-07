"""
"Migration" to kivy.
"""

#? p.37 Basics
#? p.115 package for Android

import kivy
kivy.require('1.0.6') #! replace with your current kivy version !
from kivy.app import App #* Example code below
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class MainScreen(GridLayout): #TODO high possibility of not working as intended due to __wrong__ __class__ inheritance.
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs) #* I fucking hate __super__ calls
        self.cols = 2 #! No, more. Plan.
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
        return MainScreen()

if __name__ == '__main__': #? really neccessary?
    Calc().run()