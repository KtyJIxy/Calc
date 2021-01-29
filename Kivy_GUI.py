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

from kivy.clock import Clock
from kivy.factory import Factory

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

class LongpressButton(Factory.Button):
    __events__ = ('on_long_press', )

    long_press_time = Factory.NumericProperty(1)
    
    def on_state(self, instance, value):
        if value == 'down':
            lpt = self.long_press_time
            self._clockev = Clock.schedule_once(self._do_long_press, lpt)
        else:
            self._clockev.cancel()

    def _do_long_press(self, dt):
        self.dispatch('on_long_press')
        
    def on_long_press(self, *largs):
        pass

class Memorize_Button(LongpressButton):
    #from kivy.uix.behaviors.touchripple import TouchRippleButtonBehavior
    #from kivy.uix.behaviors.button import ButtonBehavior
    #!Ensure unneeded and delete in future.

    #def __init__(self, memory=[]):
        #self.memory = memory
    memory = None
    #def on_press:
    def on_pressed(self, instance, pos):
        if memory is None:
            memory = []
            memory.append(entry.text)
            #memory = entry.text
        else:
            memory.pop()
        return self.memory
        #return memory
    def on_long_press(self, *largs):
        entry.text = memory
        #memory.pop()


if __name__ == '__main__':
    CalcApp().run()