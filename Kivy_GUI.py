"""
Kivy Framework based NUI.
"""

import kivy
kivy.require('2.0.0') #! Important.
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from Calc.functions_main import *

from kivy.clock import Clock
from kivy.factory import Factory

import math

class MainScreen(GridLayout):
    def calculate(self, calculation):
        #Uses (eval) for calculation on TextInput info.
        if calculation: 
            try: 
                self.display.text = str(eval(calculation)) 
            except Exception: 
                self.display.text = "Error"

class CalcApp(App):
    def build(self):
        #Builds UI
        return MainScreen()

class LongpressButton(Factory.Button):
    #Factory Button with custom event "long press." Duration is customizable in .kv file directly.
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

if __name__ == '__main__':
    CalcApp().run()